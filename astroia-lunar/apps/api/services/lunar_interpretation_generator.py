"""
Service de génération d'interprétations lunaires temporelles
Architecture v2 : séparation faits (LunarReturn) vs narration (LunarInterpretation)

Hiérarchie de génération:
1. LunarInterpretation (DB temporelle) - PRIORITÉ
2. Génération Claude Opus 4.5 - FALLBACK 1
3. LunarInterpretationTemplate (DB templates) - FALLBACK 2
4. Templates hardcodés (CLIMATE_TEMPLATES) - FALLBACK 3
"""

import logging
import asyncio
import time
from typing import Dict, Any, Optional, Tuple
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError
from config import settings
from prometheus_client import Counter, Histogram, Gauge
import structlog
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

# Custom exceptions for error categorization
class LunarInterpretationError(Exception):
    """Base exception for lunar interpretation errors"""
    pass

class ClaudeAPIError(LunarInterpretationError):
    """Claude API specific errors (timeout, rate limit, etc)"""
    pass

class TemplateNotFoundError(LunarInterpretationError):
    """Template not found in database"""
    pass

class InvalidLunarReturnError(LunarInterpretationError):
    """Invalid lunar_return_id provided"""
    pass

# Structured logging
logger = structlog.get_logger(__name__)

# Prometheus metrics
lunar_interpretation_generated = Counter(
    'lunar_interpretation_generated_total',
    'Total lunar interpretations generated',
    ['source', 'model', 'subject', 'version']
)

lunar_interpretation_cache_hit = Counter(
    'lunar_interpretation_cache_hit_total',
    'Total cache hits',
    ['subject', 'version']
)

lunar_interpretation_fallback = Counter(
    'lunar_interpretation_fallback_total',
    'Total fallbacks to templates',
    ['fallback_level']  # 'db_template' | 'hardcoded'
)

lunar_interpretation_duration = Histogram(
    'lunar_interpretation_duration_seconds',
    'Duration of interpretation generation',
    ['source', 'subject'],
    buckets=(0.05, 0.1, 0.5, 1, 2, 5, 10, 30)
)

lunar_active_generations = Gauge(
    'lunar_active_generations',
    'Number of active generations in progress'
)

# Version du prompt (utilisé pour le cache et le versionning)
PROMPT_VERSION = 2

# Configuration Claude
CLAUDE_MODELS = {
    'opus': 'claude-opus-4-5-20251101',
    'sonnet': 'claude-sonnet-4-5-20250929',
    'haiku': 'claude-3-5-haiku-20241022'
}


async def generate_or_get_interpretation(
    db: AsyncSession,
    lunar_return_id: int,
    user_id: int,
    subject: str = 'full',
    version: int = PROMPT_VERSION,
    lang: str = 'fr',
    force_regenerate: bool = False
) -> Tuple[str, Optional[Dict], str, str]:
    """
    Génère ou récupère une interprétation lunaire temporelle

    Args:
        db: Session async SQLAlchemy
        lunar_return_id: ID de la révolution lunaire
        user_id: ID de l'utilisateur
        subject: Type d'interprétation ('full' | 'climate' | 'focus' | 'approach')
        version: Version du prompt (default: 2)
        lang: Langue (default: 'fr')
        force_regenerate: Force la régénération même si existe (default: False)

    Returns:
        Tuple[output_text, weekly_advice, source, model_used]
        - output_text: Texte de l'interprétation
        - weekly_advice: Conseils hebdomadaires (JSON) ou None
        - source: 'db_temporal' | 'claude' | 'db_template' | 'hardcoded'
        - model_used: Nom du modèle utilisé

    Raises:
        ValueError: Si lunar_return_id invalide
    """
    from models import LunarInterpretation, LunarInterpretationTemplate, LunarReturn

    start_time = time.time()

    logger.info(
        "lunar_interpretation_generation_started",
        lunar_return_id=lunar_return_id,
        user_id=user_id,
        subject=subject,
        version=version,
        lang=lang
    )

    try:
        lunar_active_generations.inc()  # Start tracking

        # 1. Charger le LunarReturn (validation)
        lunar_return = await db.get(LunarReturn, lunar_return_id)
        if not lunar_return:
            raise InvalidLunarReturnError(f"LunarReturn {lunar_return_id} not found")

        # 2. Vérifier cache DB temporelle (sauf si force_regenerate)
        if not force_regenerate:
            logger.debug("checking_db_temporal_cache")
            result = await db.execute(
                select(LunarInterpretation).filter_by(
                    lunar_return_id=lunar_return_id,
                    subject=subject,
                    version=version,
                    lang=lang
                )
            )
            interpretation = result.scalar_one_or_none()

            if interpretation:
                # Record metrics for cache hit
                lunar_interpretation_cache_hit.labels(
                    subject=subject,
                    version=str(version)
                ).inc()

                duration = time.time() - start_time
                lunar_interpretation_duration.labels(
                    source='db_temporal',
                    subject=subject
                ).observe(duration)

                logger.info(
                    "lunar_interpretation_cache_hit",
                    lunar_return_id=lunar_return_id,
                    interpretation_id=str(interpretation.id),
                    model_used=interpretation.model_used,
                    duration_ms=int(duration * 1000)
                )

                return (
                    interpretation.output_text,
                    interpretation.weekly_advice,
                    'db_temporal',
                    interpretation.model_used or 'unknown'
                )

        # 3. Génération via Claude Opus 4.5
        try:
            logger.info("generating_via_claude")
            output_text, weekly_advice, input_context = await _generate_via_claude(
                lunar_return=lunar_return,
                subject=subject,
                version=version,
                lang=lang
            )

            # Sauvegarder en DB temporelle
            interpretation = LunarInterpretation(
                user_id=user_id,
                lunar_return_id=lunar_return_id,
                subject=subject,
                version=version,
                lang=lang,
                input_json=input_context,
                output_text=output_text,
                weekly_advice=weekly_advice,
                model_used=CLAUDE_MODELS['opus']
            )
            db.add(interpretation)
            await db.commit()
            await db.refresh(interpretation)

            # Record metrics for generation
            lunar_interpretation_generated.labels(
                source='claude',
                model=CLAUDE_MODELS['opus'],
                subject=subject,
                version=str(version)
            ).inc()

            duration = time.time() - start_time
            lunar_interpretation_duration.labels(
                source='claude',
                subject=subject
            ).observe(duration)

            logger.info(
                "lunar_interpretation_generated",
                lunar_return_id=lunar_return_id,
                interpretation_id=str(interpretation.id),
                source='claude',
                model_used=CLAUDE_MODELS['opus'],
                duration_ms=int(duration * 1000)
            )

            return output_text, weekly_advice, 'claude', CLAUDE_MODELS['opus']

        except ClaudeAPIError as e:
            logger.warning(
                "claude_generation_failed",
                lunar_return_id=lunar_return_id,
                error=str(e)
            )
            # Rollback si erreur lors du save
            await db.rollback()
        except Exception as e:
            logger.error(
                "lunar_interpretation_generation_error",
                lunar_return_id=lunar_return_id,
                error=str(e)
            )
            await db.rollback()

        # 4. Fallback vers templates DB
        logger.info("falling_back_to_db_template")
        template_result = await _get_template_fallback(
            db=db,
            moon_sign=lunar_return.moon_sign,
            moon_house=lunar_return.moon_house,
            lunar_ascendant=lunar_return.lunar_ascendant,
            template_type=subject,
            version=version,
            lang=lang
        )

        if template_result:
            output_text, weekly_advice = template_result

            # Record metrics for DB template fallback
            lunar_interpretation_fallback.labels(
                fallback_level='db_template'
            ).inc()

            duration = time.time() - start_time
            lunar_interpretation_duration.labels(
                source='db_template',
                subject=subject
            ).observe(duration)

            logger.info(
                "lunar_interpretation_fallback_db_template",
                lunar_return_id=lunar_return_id,
                source='db_template',
                duration_ms=int(duration * 1000)
            )

            return output_text, weekly_advice, 'db_template', 'template'

        # 5. Fallback hardcodé (dernier recours)
        logger.warning("falling_back_to_hardcoded_template")
        output_text = _get_hardcoded_fallback(
            moon_sign=lunar_return.moon_sign,
            moon_house=lunar_return.moon_house,
            lunar_ascendant=lunar_return.lunar_ascendant,
            subject=subject
        )

        if not output_text:
            raise TemplateNotFoundError(
                f"No template found for {lunar_return.moon_sign}/{lunar_return.moon_house}/{lunar_return.lunar_ascendant}"
            )

        # Record metrics for hardcoded fallback
        lunar_interpretation_fallback.labels(
            fallback_level='hardcoded'
        ).inc()

        duration = time.time() - start_time
        lunar_interpretation_duration.labels(
            source='hardcoded',
            subject=subject
        ).observe(duration)

        logger.info(
            "lunar_interpretation_fallback_hardcoded",
            lunar_return_id=lunar_return_id,
            source='hardcoded',
            duration_ms=int(duration * 1000)
        )

        return output_text, None, 'hardcoded', 'placeholder'

    finally:
        lunar_active_generations.dec()  # End tracking


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type((APIConnectionError, RateLimitError)),
    reraise=True
)
async def _call_claude_with_retry(client: Anthropic, prompt: str, max_tokens: int, model: str) -> str:
    """Call Claude with automatic retry on transient errors"""
    logger.debug("calling_claude_api")

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


async def _generate_via_claude(
    lunar_return: Any,
    subject: str,
    version: int,
    lang: str
) -> Tuple[str, Optional[Dict], Dict]:
    """
    Génère une interprétation via Claude Opus 4.5

    Returns:
        Tuple[output_text, weekly_advice, input_context]
    """
    # Construire le contexte d'entrée
    input_context = _build_input_context(lunar_return, subject, version, lang)

    # Construire le prompt
    prompt = _build_prompt(input_context, subject, version, lang)

    # Appeler Claude
    client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
    max_tokens = 1200 if subject == 'full' else 600

    try:
        # Call Claude with retry logic and timeout
        output_text = await asyncio.wait_for(
            _call_claude_with_retry(
                client=client,
                prompt=prompt,
                max_tokens=max_tokens,
                model=CLAUDE_MODELS['opus']
            ),
            timeout=30.0  # 30 seconds max
        )

        # Parser weekly_advice si subject='full'
        weekly_advice = None
        if subject == 'full':
            weekly_advice = _parse_weekly_advice(output_text)

        return output_text, weekly_advice, input_context

    except asyncio.TimeoutError:
        logger.error("claude_timeout", timeout_seconds=30)
        raise ClaudeAPIError("Claude API timeout after 30s")
    except (APIError, APIConnectionError, RateLimitError) as e:
        logger.error("claude_api_call_failed", error=str(e), retries_exhausted=True)
        raise ClaudeAPIError(f"Claude API failed: {e}")


def _build_input_context(
    lunar_return: Any,
    subject: str,
    version: int,
    lang: str
) -> Dict[str, Any]:
    """
    Construit le contexte complet pour la génération Claude

    Stocké en DB pour traçabilité et régénération
    """
    return {
        'lunar_return_id': lunar_return.id,
        'user_id': lunar_return.user_id,
        'month': lunar_return.month,
        'return_date': lunar_return.return_date.isoformat() if lunar_return.return_date else None,
        'moon_sign': lunar_return.moon_sign,
        'moon_house': lunar_return.moon_house,
        'lunar_ascendant': lunar_return.lunar_ascendant,
        'aspects': lunar_return.aspects,
        'planets': lunar_return.planets,
        'houses': lunar_return.houses,
        'subject': subject,
        'version': version,
        'lang': lang,
        'generated_at': datetime.utcnow().isoformat()
    }


def _build_prompt(
    input_context: Dict,
    subject: str,
    version: int,
    lang: str
) -> str:
    """
    Construit le prompt pour Claude selon le sujet

    Version 2 : Prompt moderne, ton accessible, structuré
    """
    moon_sign = input_context['moon_sign']
    moon_house = input_context['moon_house']
    lunar_ascendant = input_context['lunar_ascendant']
    aspects = input_context.get('aspects', [])

    if subject == 'full':
        # Interprétation complète du mois
        prompt = f"""Tu es un astrologue professionnel senior. Génère une interprétation complète de révolution lunaire mensuelle.

**Contexte astronomique:**
- Lune en {moon_sign}, Maison {moon_house}
- Ascendant lunaire: {lunar_ascendant}
- Aspects lunaires: {_format_aspects(aspects)}

**Consignes:**
1. Tonalité générale du mois (2-3 phrases)
2. Ressources disponibles (2-3 phrases)
3. Défis à naviguer (2-3 phrases)
4. Dynamiques émotionnelles (2-3 phrases)

**Style:**
- Ton chaleureux et accessible (tutoiement)
- Concret et applicable
- 800-1000 caractères
- Structuré en 4 paragraphes

Génère l'interprétation complète maintenant."""

    elif subject == 'climate':
        # Climat émotionnel seulement
        prompt = f"""Tu es un astrologue professionnel senior. Génère le climat émotionnel d'une révolution lunaire.

**Contexte:**
- Lune en {moon_sign}

**Consignes:**
- Décris l'ambiance émotionnelle générale du mois
- Ton chaleureux (tutoiement)
- 200-300 caractères
- 2-3 phrases

Génère le climat maintenant."""

    elif subject == 'focus':
        # Focus zones de vie
        prompt = f"""Tu es un astrologue professionnel senior. Génère les zones de focus d'une révolution lunaire.

**Contexte:**
- Lune en Maison {moon_house}

**Consignes:**
- Décris les domaines de vie activés ce mois
- Ton chaleureux (tutoiement)
- 200-300 caractères
- 2-3 phrases

Génère le focus maintenant."""

    elif subject == 'approach':
        # Approche du mois
        prompt = f"""Tu es un astrologue professionnel senior. Génère l'approche d'une révolution lunaire.

**Contexte:**
- Ascendant lunaire: {lunar_ascendant}

**Consignes:**
- Décris la meilleure approche pour aborder ce mois
- Ton chaleureux (tutoiement)
- 200-300 caractères
- 2-3 phrases

Génère l'approche maintenant."""

    else:
        raise ValueError(f"Subject inconnu: {subject}")

    return prompt


def _format_aspects(aspects: list) -> str:
    """Formate les aspects pour le prompt"""
    if not aspects:
        return "Aucun aspect majeur"

    formatted = []
    for aspect in aspects[:5]:  # Limiter à 5 aspects
        planet1 = aspect.get('first_planet', '?')
        planet2 = aspect.get('second_planet', '?')
        aspect_type = aspect.get('aspect', '?')
        formatted.append(f"{planet1}-{planet2} {aspect_type}")

    return ", ".join(formatted)


def _parse_weekly_advice(output_text: str) -> Optional[Dict]:
    """
    Parse les conseils hebdomadaires depuis le texte généré

    TODO: Implémenter parsing structuré si Claude génère du JSON
    Pour l'instant, retourne None (conseils dans output_text)
    """
    # Pour v2, on pourrait demander à Claude de générer un JSON structuré
    # Pour l'instant, on stocke tout dans output_text
    return None


async def _get_template_fallback(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    template_type: str,
    version: int,
    lang: str
) -> Optional[Tuple[str, Optional[Dict]]]:
    """
    Récupère un template depuis lunar_interpretation_templates

    Returns:
        Tuple[template_text, weekly_advice_template] ou None
    """
    from models import LunarInterpretationTemplate

    # Construire le filtre selon le template_type
    filters = {
        'template_type': template_type,
        'version': version,
        'lang': lang
    }

    if template_type == 'full':
        filters['moon_sign'] = moon_sign
        filters['moon_house'] = moon_house
        filters['lunar_ascendant'] = lunar_ascendant
    elif template_type == 'climate':
        filters['moon_sign'] = moon_sign
    elif template_type == 'focus':
        filters['moon_house'] = moon_house
    elif template_type == 'approach':
        filters['lunar_ascendant'] = lunar_ascendant

    result = await db.execute(
        select(LunarInterpretationTemplate).filter_by(**filters)
    )
    template = result.scalar_one_or_none()

    if template:
        return template.template_text, template.weekly_advice_template

    return None


def _get_hardcoded_fallback(
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    subject: str
) -> str:
    """
    Dernier recours : templates hardcodés

    Réutilise les templates existants dans lunar_report_builder.py
    """
    if subject == 'full':
        # Utiliser les templates CLIMATE_TEMPLATES existants
        from services.lunar_report_builder import CLIMATE_TEMPLATES

        template = CLIMATE_TEMPLATES.get((moon_sign, moon_house))
        if not template:
            template = CLIMATE_TEMPLATES.get((moon_sign, None), "Mois d'ajustement lunaire.")

        return template

    elif subject == 'climate':
        from services.lunar_report_builder import MOON_SIGN_INTRO
        return MOON_SIGN_INTRO.get(
            moon_sign,
            f"Mois sous influence de la Lune en {moon_sign}."
        )

    elif subject == 'focus':
        from services.lunar_report_builder import HOUSE_AXES
        house_label = HOUSE_AXES.get(moon_house, "Domaine de vie")
        return f"Maison {moon_house} activée : {house_label}."

    elif subject == 'approach':
        from services.lunar_report_builder import LUNAR_ASCENDANT_FILTERS
        return LUNAR_ASCENDANT_FILTERS.get(
            lunar_ascendant,
            f"Approche du mois filtrée par ascendant lunaire en {lunar_ascendant}."
        )

    return "Interprétation lunaire en cours de génération."
