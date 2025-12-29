"""
Service pour générer des interprétations astrologiques via Claude (Anthropic)
Version 2 - Prompt refondé, Sonnet + fallback Haiku
"""

import logging
from typing import Dict, Any, Optional, List, Tuple
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError
from schemas.natal_interpretation import ChartPayload
from config import settings

logger = logging.getLogger(__name__)

# Version du prompt (utilisé pour le cache)
PROMPT_VERSION = 2

# Mapping emoji par sujet
SUBJECT_EMOJI = {
    'sun': '☀️',
    'moon': '🌙',
    'ascendant': '↑',
    'midheaven': '⬆️',  # Milieu du Ciel (MC)
    'mercury': '☿️',
    'venus': '♀️',
    'mars': '♂️',
    'jupiter': '♃',
    'saturn': '♄',
    'uranus': '♅',
    'neptune': '♆',
    'pluto': '♇',
    'chiron': '⚕️',
    'north_node': '☊',
    'south_node': '☋',
    'lilith': '⚸'
}


def get_anthropic_client() -> Anthropic:
    """
    Crée un client Anthropic avec la clé API depuis settings
    """
    if not settings.ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY non défini dans .env")

    return Anthropic(api_key=settings.ANTHROPIC_API_KEY)


def get_house_label_v2(house_num: int) -> Tuple[str, str]:
    """
    Retourne le label court et la description d'une maison

    Returns:
        tuple: (label_court, description_complete)
    """
    house_data = {
        1: ("identité, apparence", "Maison 1 : identité, apparence, nouveau départ, comment tu te présentes au monde"),
        2: ("ressources, valeurs", "Maison 2 : ressources personnelles, valeurs, sécurité matérielle, rapport à l'argent"),
        3: ("communication, environnement proche", "Maison 3 : communication, apprentissage, environnement proche, frères et sœurs"),
        4: ("foyer, racines", "Maison 4 : foyer, famille, racines, vie privée, bases émotionnelles"),
        5: ("créativité, plaisir", "Maison 5 : créativité, plaisir, expression personnelle, romance, enfants"),
        6: ("quotidien, service", "Maison 6 : quotidien, santé, service, travail, organisation, routines"),
        7: ("relations, partenariats", "Maison 7 : relations, partenariats, l'autre comme miroir, collaboration"),
        8: ("intimité, transformation", "Maison 8 : intimité, transformation, ressources partagées, liens profonds, pouvoir"),
        9: ("philosophie, expansion", "Maison 9 : philosophie, voyages, expansion de conscience, enseignement supérieur"),
        10: ("carrière, accomplissement", "Maison 10 : carrière, accomplissement social, réputation, visibilité publique"),
        11: ("projets collectifs, idéaux", "Maison 11 : projets collectifs, amitiés, idéaux, communauté, réseaux"),
        12: ("spiritualité, inconscient", "Maison 12 : spiritualité, inconscient, transcendance, solitude, ce qui est caché")
    }

    return house_data.get(house_num, ("domaine de vie", f"Maison {house_num}"))


def find_relevant_aspect(subject: str, chart_payload: ChartPayload) -> Optional[str]:
    """
    Trouve UN aspect pertinent (max 1) impliquant le sujet, avec orb <= 3°

    Args:
        subject: Objet céleste concerné
        chart_payload: Données du chart

    Returns:
        Description de l'aspect ou None
    """
    if not chart_payload.aspects or len(chart_payload.aspects) == 0:
        return None

    # Chercher le premier aspect valide impliquant le sujet
    for aspect in chart_payload.aspects:
        if not isinstance(aspect, dict):
            continue

        # Vérifier que le sujet est impliqué
        planet1 = aspect.get('planet1', '').lower().replace(' ', '_')
        planet2 = aspect.get('planet2', '').lower().replace(' ', '_')

        if subject not in [planet1, planet2]:
            continue

        # Vérifier l'orbe
        orb = aspect.get('orb', 999)
        if orb > 3:
            continue

        # Construire la description
        aspect_type = aspect.get('type', '').lower()
        other_planet = planet2 if planet1 == subject else planet1

        aspect_names = {
            'conjunction': 'conjonction',
            'opposition': 'opposition',
            'trine': 'trigone',
            'square': 'carré',
            'sextile': 'sextile'
        }

        aspect_name = aspect_names.get(aspect_type, aspect_type)

        return f"{aspect_name} à {other_planet.replace('_', ' ').title()} (orbe {orb:.1f}°)"

    return None


def build_interpretation_prompt_v2(
    subject: str,
    chart_payload: ChartPayload
) -> str:
    """
    Construit le prompt v2 avec le nouveau template Astroia

    Template:
    # {emoji} {Sujet} en {Signe}
    **En une phrase :** ...

    ## Ton moteur
    ...

    ## Ton défi
    ...

    ## La maison {N} en clair
    ...

    ## Micro-rituel du jour (2 min)
    - ...
    """
    emoji = SUBJECT_EMOJI.get(subject, '⭐')
    subject_label = chart_payload.subject_label
    sign = chart_payload.sign

    # Maison (obligatoire pour le prompt)
    house_context = ""
    house_short_label = ""
    if chart_payload.house:
        house_short_label, house_full = get_house_label_v2(chart_payload.house)
        house_context = f"\n- {house_full}"

    # Aspect (max 1, si pertinent)
    aspect_context = ""
    aspect_desc = find_relevant_aspect(subject, chart_payload)
    if aspect_desc:
        aspect_context = f"\n- Aspect majeur : {aspect_desc}"

    # Ascendant (contexte global)
    asc_context = ""
    if chart_payload.ascendant_sign:
        asc_context = f"\n- Ascendant en {chart_payload.ascendant_sign} (filtre de perception général)"

    # Construire parties conditionnelles AVANT le f-string pour éviter les backslashes
    aspect_mention = " + Aspect" if aspect_desc else ""
    aspect_integration = ". Mention subtile de l'aspect si pertinent." if aspect_desc else ""

    prompt = f"""Tu es un·e astrologue moderne pour l'app Astroia. Ton rôle : éclairer, pas prédire. Ton style : concret, chaleureux, jamais mystique.

DONNÉES DU THÈME:
- {subject_label} en {sign}{house_context}{aspect_context}{asc_context}

TEMPLATE À SUIVRE (EXACT):

# {emoji} {subject_label} en {sign}
**En une phrase :** [UNE phrase très spécifique qui croise {subject_label} + {sign} + Maison {chart_payload.house or 'N'}{aspect_mention}, pas de généralité]

## Ton moteur
[2-3 phrases max : ce que {subject_label} en {sign} en Maison {chart_payload.house or 'N'} pousse à faire, rechercher, exprimer. Croiser SYSTÉMATIQUEMENT ces 3 dimensions. Concret, pas "tu es quelqu'un de..."]

## Ton défi
[1-2 phrases : le piège typique de {subject_label} en {sign} en Maison {chart_payload.house or 'N'}. Équilibré lumière-ombre.]

## Maison {chart_payload.house or 'N'} en {sign}
[1-2 phrases : comment {subject_label} exprime {sign} concrètement dans le domaine de la Maison {chart_payload.house or 'N'} ({house_short_label}). Croiser les 3 infos{aspect_integration}]

## Micro-rituel du jour (2 min)
- [Action relationnelle concrète pour {subject_label} en {sign} en Maison {chart_payload.house or 'N'}, formulée à l'infinitif]
- [Action corps/respiration concrète]
- [Journal prompt : 1 question ouverte sur le croisement planète-signe-maison]

CONTRAINTES STRICTES:
1. LONGUEUR: 900 à 1200 caractères (max absolu 1400). Compte tes caractères.
2. INTERDIT: "tu es quelqu'un de...", "tu ressens profondément...", généralités vides.
3. INTERDIT: Prédictions ("tu vas rencontrer...", "il arrivera...").
4. INTERDIT: Conseils santé/diagnostic.
5. OBLIGATOIRE: CROISER SYSTÉMATIQUEMENT {subject_label} + {sign} + Maison {chart_payload.house or 'N'} dans CHAQUE section. C'est le triptyque central de l'interprétation.
6. TON: Présent ou infinitif. Jamais futur. Vocabulaire simple, moderne.
7. FORMAT: Markdown strict. Les ## sont obligatoires. Pas de titre supplémentaire après le #.

GÉNÈRE L'INTERPRÉTATION MAINTENANT (français, markdown, 900-1200 chars):"""

    return prompt


def validate_interpretation_length(text: str) -> Tuple[bool, int]:
    """
    Valide que l'interprétation respecte les contraintes de longueur

    Returns:
        tuple: (is_valid, length)
    """
    length = len(text)
    return (900 <= length <= 1400), length


async def generate_with_sonnet_fallback_haiku(
    subject: str,
    chart_payload: Dict[str, Any] | ChartPayload
) -> Tuple[str, str]:
    """
    Génère une interprétation avec Claude Sonnet, fallback sur Haiku si erreur

    Stratégie:
    1. Essayer Sonnet 3.5
    2. Si erreur (429, timeout, 5xx) -> fallback Haiku
    3. Valider longueur (900-1200 chars, max 1400)
    4. Si hors limites -> retry 1x avec prompt d'ajustement
    5. Si toujours hors limites -> tronquer à 1400 proprement

    Returns:
        tuple: (interpretation_text, model_used)
    """
    # Convertir en ChartPayload si nécessaire
    if isinstance(chart_payload, dict):
        payload = ChartPayload(**chart_payload)
    else:
        payload = chart_payload

    # Construire le prompt v2
    prompt = build_interpretation_prompt_v2(subject, payload)

    client = get_anthropic_client()

    # Liste des modèles à essayer
    models_to_try = [
        ("claude-3-5-sonnet-20241022", "sonnet"),  # Sonnet 3.5 en priorité
        ("claude-3-haiku-20240307", "haiku")       # Fallback Haiku
    ]

    last_error = None

    for model_id, model_name in models_to_try:
        try:
            logger.info(f"🤖 Appel Claude {model_name} pour {subject} en {payload.sign}")

            message = client.messages.create(
                model=model_id,
                max_tokens=2048,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}],
                timeout=30.0
            )

            text_content = message.content[0].text.strip()
            is_valid, length = validate_interpretation_length(text_content)

            logger.info(f"✅ {model_name} - Texte généré: {length} chars (valid={is_valid})")

            # Si longueur invalide, retry 1x avec prompt d'ajustement
            if not is_valid and length < 900:
                logger.warning(f"⚠️ Texte trop court ({length} chars), retry avec expansion")
                adjust_prompt = f"{prompt}\n\nATTENTION: Le texte précédent était trop court ({length} chars). Développe davantage en gardant le même template, vise 1000-1200 caractères."

                message = client.messages.create(
                    model=model_id,
                    max_tokens=2048,
                    temperature=0.7,
                    messages=[{"role": "user", "content": adjust_prompt}],
                    timeout=30.0
                )

                text_content = message.content[0].text.strip()
                is_valid, length = validate_interpretation_length(text_content)
                logger.info(f"✅ Retry {model_name}: {length} chars (valid={is_valid})")

            elif not is_valid and length > 1400:
                logger.warning(f"⚠️ Texte trop long ({length} chars), retry avec réduction")
                adjust_prompt = f"{prompt}\n\nATTENTION: Le texte précédent était trop long ({length} chars). Réduis-le à 1000-1200 caractères en retirant les répétitions et en gardant l'essentiel."

                message = client.messages.create(
                    model=model_id,
                    max_tokens=2048,
                    temperature=0.7,
                    messages=[{"role": "user", "content": adjust_prompt}],
                    timeout=30.0
                )

                text_content = message.content[0].text.strip()
                is_valid, length = validate_interpretation_length(text_content)
                logger.info(f"✅ Retry {model_name}: {length} chars (valid={is_valid})")

            # Si toujours trop long après retry, tronquer proprement
            if length > 1400:
                logger.warning(f"⚠️ Tronquage à 1400 chars (était {length})")
                text_content = text_content[:1397] + "..."
                length = len(text_content)

            logger.info(f"✅ Interprétation finale: {length} chars, modèle={model_name}")

            return text_content, model_name

        except (RateLimitError, APIConnectionError) as e:
            logger.warning(f"⚠️ {model_name} échec ({type(e).__name__}): {str(e)[:100]}")
            last_error = e
            # Continuer vers le fallback
            continue

        except APIError as e:
            error_code = getattr(e, 'status_code', 0)
            error_type = getattr(e, 'type', '')

            # 401 authentication_error = clé API invalide -> fallback
            if error_code == 401 or 'authentication_error' in str(e):
                logger.warning(f"⚠️ {model_name} auth invalide (401), fallback")
                last_error = e
                continue

            # 404 not_found_error = modèle non accessible -> fallback
            if error_code == 404 or 'not_found_error' in str(e):
                logger.warning(f"⚠️ {model_name} non accessible (404), fallback")
                last_error = e
                continue

            # 429, 5xx = erreurs temporaires -> fallback
            if error_code in [429, 500, 502, 503, 504]:
                logger.warning(f"⚠️ {model_name} échec (HTTP {error_code}), fallback")
                last_error = e
                continue

            # Autres erreurs (400, etc.) = non-récupérables
            logger.error(f"❌ {model_name} erreur non-récupérable: {e}")
            raise Exception(f"Erreur API Claude ({model_name}): {str(e)}")

    # Si tous les modèles ont échoué
    if last_error:
        logger.error(f"❌ Tous les modèles ont échoué, dernière erreur: {last_error}")
        raise Exception(f"Impossible de générer l'interprétation: {str(last_error)}")

    raise Exception("Aucun modèle disponible")
