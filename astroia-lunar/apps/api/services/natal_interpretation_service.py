"""
Service pour générer des interprétations astrologiques via Claude (Anthropic)
Version 2 - Prompt refondé, Sonnet + fallback Haiku
"""

import logging
from typing import Dict, Any, Optional, List, Tuple
from anthropic import Anthropic, APIError, APIConnectionError, RateLimitError
from schemas.natal_interpretation import ChartPayload
from config import settings
from pathlib import Path

logger = logging.getLogger(__name__)

# Version du prompt (utilisé pour le cache)
# v2 = prompt Lunation moderne avec micro-rituel, aspects orb <=3°
# v3 = prompt senior astrologer, aspects majeurs orb <=6°, sans micro-rituel
# Configurable via .env: NATAL_INTERPRETATION_VERSION=3
PROMPT_VERSION = settings.NATAL_INTERPRETATION_VERSION

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

# Mapping signe français → anglais (pour fichiers markdown)
SIGN_FR_TO_EN = {
    'bélier': 'aries',
    'belier': 'aries',  # Variante sans accent
    'taureau': 'taurus',
    'gémeaux': 'gemini',
    'gemeaux': 'gemini',  # Variante sans accent
    'cancer': 'cancer',
    'lion': 'leo',
    'vierge': 'virgo',
    'balance': 'libra',
    'scorpion': 'scorpio',
    'sagittaire': 'sagittarius',
    'capricorne': 'capricorn',
    'verseau': 'aquarius',
    'poissons': 'pisces'
}


def load_pregenerated_interpretation(
    subject: str,
    sign: str,
    house: int,
    version: int = 2
) -> Optional[str]:
    """
    Charge une interprétation pré-générée depuis les fichiers markdown

    Args:
        subject: Nom du sujet (sun, moon, etc.)
        sign: Nom du signe en français (Verseau, Taureau, etc.)
        house: Numéro de maison (1-12)
        version: Version du prompt (2 ou 4)

    Returns:
        Texte markdown complet OU None si fichier introuvable
    """
    # Normaliser le signe (minuscule, sans espaces)
    sign_normalized = sign.lower().strip()

    # Mapping FR → EN pour les signes (essayer avec et sans accents)
    sign_en = SIGN_FR_TO_EN.get(sign_normalized)

    # Si pas trouvé, essayer sans accents
    if not sign_en:
        sign_no_accents = sign_normalized.replace('é', 'e').replace('è', 'e').replace('ê', 'e')
        sign_en = SIGN_FR_TO_EN.get(sign_no_accents)

    # Si toujours pas trouvé, utiliser la valeur normalisée comme fallback
    if not sign_en:
        sign_en = sign_no_accents if sign_no_accents else sign_normalized

    # Chemin fichier
    base_path = Path(__file__).parent.parent
    file_path = base_path / f"data/natal_interpretations/v{version}/{subject}/{sign_en}_{house}.md"

    if not file_path.exists():
        logger.warning(f"⚠️ Fichier introuvable: {file_path}")
        return None

    try:
        # Lire le fichier
        content = file_path.read_text(encoding='utf-8')

        # Extraire le markdown (après frontmatter YAML)
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                markdown_text = parts[2].strip()
                logger.info(f"✅ Interprétation pré-générée chargée: {subject} en {sign} M{house} ({len(markdown_text)} chars)")
                return markdown_text

        # Si pas de frontmatter, retourner le contenu brut
        logger.info(f"✅ Interprétation pré-générée chargée (sans frontmatter): {subject} en {sign} M{house}")
        return content.strip()

    except Exception as e:
        logger.error(f"❌ Erreur lecture fichier {file_path}: {e}")
        return None


def get_anthropic_client() -> Anthropic:
    """
    Crée un client Anthropic avec la clé API depuis settings
    """
    if not settings.ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY non défini dans .env")

    return Anthropic(api_key=settings.ANTHROPIC_API_KEY)


def generate_placeholder_interpretation(subject: str, chart_payload: ChartPayload, version: int = 2) -> str:
    """
    Génère une interprétation placeholder propre quand le mode LLM est désactivé

    Args:
        subject: Objet céleste concerné
        chart_payload: Données du chart
        version: Version du prompt (pour cohérence)

    Returns:
        Texte placeholder formaté en markdown
    """
    emoji = SUBJECT_EMOJI.get(subject, '⭐')
    subject_label = chart_payload.subject_label
    sign = chart_payload.sign or "signe inconnu"
    house = chart_payload.house or 0

    house_short_label, _ = get_house_label_v2(house) if house else ("domaine de vie", "")

    placeholder = f"""# {emoji} {subject_label} en {sign}

**Interprétation non disponible (mode sans LLM)**

Cette interprétation nécessite l'activation du mode LLM avec l'API Anthropic Claude.

**Données de votre thème :**
- {subject_label} en {sign}
- Maison {house} ({house_short_label})

Pour obtenir une interprétation complète, contactez votre administrateur pour activer le service d'interprétation automatique."""

    return placeholder


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
    # Gérer le cas où aspects est None ou pas une liste
    if not chart_payload.aspects:
        return None
    if not isinstance(chart_payload.aspects, list):
        return None
    if len(chart_payload.aspects) == 0:
        return None

    # Normaliser le sujet pour la comparaison
    subject_normalized = subject.lower().replace(' ', '_')
    
    # Chercher le premier aspect valide impliquant le sujet
    for aspect in chart_payload.aspects:
        if not isinstance(aspect, dict):
            continue

        # Vérifier que le sujet est impliqué (normaliser les noms de planètes)
        planet1 = aspect.get('planet1', '').lower().replace(' ', '_')
        planet2 = aspect.get('planet2', '').lower().replace(' ', '_')
        
        # Mapping des variantes de noms pour le sujet
        subject_variants = [subject_normalized]
        if subject_normalized == 'midheaven':
            subject_variants.extend(['mc', 'medium_coeli', 'mediumcoeli', 'milieu_du_ciel', 'mileuduciel'])
        elif subject_normalized == 'north_node':
            subject_variants.extend(['mean_node', 'truenode', 'meannode', 'noeud_nord', 'noeudnord'])
        elif subject_normalized == 'south_node':
            subject_variants.extend(['noeud_sud', 'noeudsud'])

        if not any(variant in [planet1, planet2] for variant in subject_variants):
            continue

        # Vérifier l'orbe (gérer les cas où orb est None ou un type incorrect)
        orb_raw = aspect.get('orb', 999)
        try:
            orb = abs(float(orb_raw)) if orb_raw is not None else 999
        except (ValueError, TypeError):
            orb = 999
        if orb > 3:
            continue

        # Construire la description
        aspect_type = aspect.get('type', '').lower()
        # Déterminer quelle planète est l'autre (pas le sujet)
        other_planet = planet2 if any(variant == planet1 for variant in subject_variants) else planet1

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
    Construit le prompt v2 avec le nouveau template Lunation

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
    
    # Validation : signe obligatoire
    if not sign or sign.strip() == '':
        logger.error(f"❌ Signe manquant pour {subject} - chart_payload: {chart_payload.model_dump() if hasattr(chart_payload, 'model_dump') else chart_payload}")
        raise ValueError(f"Signe manquant pour {subject_label} ({subject}). Vérifiez que les données du thème natal contiennent le signe du Milieu du Ciel.")

    # Maison (obligatoire pour le prompt)
    house_context = ""
    house_short_label = ""
    if chart_payload.house:
        house_short_label, house_full = get_house_label_v2(chart_payload.house)
        house_context = f"\n- {house_full}"

    # Aspect (max 1, si pertinent)
    aspect_context = ""
    try:
        aspect_desc = find_relevant_aspect(subject, chart_payload)
        if aspect_desc:
            aspect_context = f"\n- Aspect majeur : {aspect_desc}"
    except Exception as aspect_err:
        # #region agent log
        import json
        import time
        try:
            log_data = {
                "location": "natal_interpretation_service.py:177",
                "message": "Error in find_relevant_aspect",
                "data": {
                    "error": str(aspect_err),
                    "error_type": type(aspect_err).__name__,
                    "subject": subject,
                    "has_aspects": bool(chart_payload.aspects),
                    "aspects_type": type(chart_payload.aspects).__name__ if chart_payload.aspects else None
                },
                "timestamp": int(time.time() * 1000),
                "sessionId": "debug-session",
                "runId": "run1",
                "hypothesisId": "F"
            }
            with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                f.write(json.dumps(log_data) + "\n")
        except Exception as log_err:
            logger.warning(f"Erreur écriture log debug: {log_err}")
        # #endregion
        # Ne pas faire échouer la génération si l'aspect échoue, continuer sans aspect
        logger.warning(f"⚠️ Erreur lors de la recherche d'aspect pour {subject}: {aspect_err}")
        aspect_desc = None

    # Ascendant (contexte global)
    asc_context = ""
    if chart_payload.ascendant_sign:
        asc_context = f"\n- Ascendant en {chart_payload.ascendant_sign} (filtre de perception général)"

    # Construire parties conditionnelles AVANT le f-string pour éviter les backslashes
    aspect_mention = " + Aspect" if aspect_desc else ""
    aspect_integration = ". Mention subtile de l'aspect si pertinent." if aspect_desc else ""

    prompt = f"""Tu es un·e astrologue moderne pour l'app Lunation. Ton rôle : éclairer, pas prédire. Ton style : concret, chaleureux, jamais mystique.

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

    # #region agent log
    try:
        log_data = {
            "location": "natal_interpretation_service.py:225",
            "message": "Prompt built successfully",
            "data": {
                "subject": subject,
                "prompt_length": len(prompt),
                "has_house": bool(chart_payload.house),
                "house_value": chart_payload.house,
                "house_short_label": house_short_label
            },
            "timestamp": int(time.time() * 1000),
            "sessionId": "debug-session",
            "runId": "run1",
            "hypothesisId": "G"
        }
        with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as log_err:
        logger.warning(f"Erreur écriture log debug: {log_err}")
    # #endregion

    return prompt


# ============================================================================
# V3 SENIOR PROMPT - Aspects majeurs orb <=6°, sans micro-rituel
# ============================================================================

def find_relevant_aspect_v3(subject: str, chart_payload: ChartPayload) -> Optional[str]:
    """
    Trouve UN aspect majeur pertinent avec orb <= 6°

    Différences avec v2:
    - Orbe étendu à 6° (au lieu de 3°)
    - Filtre UNIQUEMENT les aspects majeurs: conjunction, opposition, square, trine
    - Exclut: sextile, quincunx, semi-sextile, etc.

    Args:
        subject: Objet céleste concerné
        chart_payload: Données du chart

    Returns:
        Description de l'aspect ou None
    """
    # Aspects majeurs acceptés pour v3
    MAJOR_ASPECTS = {'conjunction', 'opposition', 'square', 'trine'}

    # Gérer le cas où aspects est None ou pas une liste
    if not chart_payload.aspects:
        return None
    if not isinstance(chart_payload.aspects, list):
        return None
    if len(chart_payload.aspects) == 0:
        return None

    # Normaliser le sujet pour la comparaison
    subject_normalized = subject.lower().replace(' ', '_')

    # Chercher le premier aspect majeur valide impliquant le sujet
    for aspect in chart_payload.aspects:
        if not isinstance(aspect, dict):
            continue

        # Vérifier que le sujet est impliqué (normaliser les noms de planètes)
        planet1 = aspect.get('planet1', '').lower().replace(' ', '_')
        planet2 = aspect.get('planet2', '').lower().replace(' ', '_')

        # Mapping des variantes de noms pour le sujet
        subject_variants = [subject_normalized]
        if subject_normalized == 'midheaven':
            subject_variants.extend(['mc', 'medium_coeli', 'mediumcoeli', 'milieu_du_ciel', 'mileuduciel'])
        elif subject_normalized == 'north_node':
            subject_variants.extend(['mean_node', 'truenode', 'meannode', 'noeud_nord', 'noeudnord'])
        elif subject_normalized == 'south_node':
            subject_variants.extend(['noeud_sud', 'noeudsud'])

        if not any(variant in [planet1, planet2] for variant in subject_variants):
            continue

        # Filtrer uniquement les aspects majeurs
        aspect_type = aspect.get('type', '').lower()
        if aspect_type not in MAJOR_ASPECTS:
            continue

        # Vérifier l'orbe (orb <= 6° pour v3)
        orb_raw = aspect.get('orb', 999)
        try:
            orb = abs(float(orb_raw)) if orb_raw is not None else 999
        except (ValueError, TypeError):
            orb = 999
        if orb > 6:
            continue

        # Construire la description
        # Déterminer quelle planète est l'autre (pas le sujet)
        other_planet = planet2 if any(variant == planet1 for variant in subject_variants) else planet1

        aspect_names = {
            'conjunction': 'conjonction',
            'opposition': 'opposition',
            'trine': 'trigone',
            'square': 'carré'
        }

        aspect_name = aspect_names.get(aspect_type, aspect_type)

        return f"{aspect_name} à {other_planet.replace('_', ' ').title()} (orbe {orb:.1f}°)"

    return None


def build_interpretation_prompt_v3_senior(
    subject: str,
    chart_payload: ChartPayload
) -> str:
    """
    Construit le prompt v3 'senior astrologer' style

    Différences avec v2:
    - Pas de section "Micro-rituel du jour"
    - Aspects majeurs uniquement (conjonction, opposition, carré, trigone)
    - Orbe ≤6° au lieu de ≤3°
    - Hiérarchisation: Soleil/Lune/ASC > Nœud Nord > autres
    - Style senior professionnel avec exemples comportementaux
    - Garde-fou: si aucun aspect majeur, fallback sur placements clés

    Template v3:
    # {emoji} {Sujet} en {Signe}
    **En une phrase :** ...

    ## Ton moteur
    ...

    ## Ton défi
    ...

    ## Maison {N} en {Signe}
    ...

    (PAS de section Micro-rituel)
    """
    emoji = SUBJECT_EMOJI.get(subject, '⭐')
    subject_label = chart_payload.subject_label
    sign = chart_payload.sign

    # Validation : signe obligatoire
    if not sign or sign.strip() == '':
        logger.error(f"❌ Signe manquant pour {subject} - chart_payload: {chart_payload.model_dump() if hasattr(chart_payload, 'model_dump') else chart_payload}")
        raise ValueError(f"Signe manquant pour {subject_label} ({subject}). Vérifiez que les données du thème natal contiennent le signe du Milieu du Ciel.")

    # Maison (obligatoire pour le prompt)
    house_context = ""
    house_short_label = ""
    if chart_payload.house:
        house_short_label, house_full = get_house_label_v2(chart_payload.house)
        house_context = f"\n- {house_full}"

    # Aspect majeur v3 (orb <= 6°)
    aspect_context = ""
    aspect_desc = None
    try:
        aspect_desc = find_relevant_aspect_v3(subject, chart_payload)
        if aspect_desc:
            aspect_context = f"\n- Aspect majeur : {aspect_desc}"
    except Exception as aspect_err:
        logger.warning(f"⚠️ Erreur lors de la recherche d'aspect v3 pour {subject}: {aspect_err}")
        aspect_desc = None

    # Ascendant (contexte global)
    asc_context = ""
    if chart_payload.ascendant_sign:
        asc_context = f"\n- Ascendant en {chart_payload.ascendant_sign} (filtre de perception général)"

    # Hiérarchie: Soleil/Lune/ASC > Nœud Nord > autres
    priority_level = ""
    if subject in ['sun', 'moon', 'ascendant']:
        priority_level = "\n\n⚠️ PRIORITÉ MAXIMALE: Ce placement est un pilier fondamental de l'identité. Traite-le comme structurant."
    elif subject in ['north_node', 'south_node']:
        priority_level = "\n\n⚠️ PRIORITÉ ÉLEVÉE: Le Nœud Nord représente le chemin de vie, la zone d'inconfort utile. Le Nœud Sud, le confort familier à transcender. Traite ce placement comme un guide d'évolution."

    # Construire parties conditionnelles AVANT le f-string
    aspect_mention = " + Aspect majeur" if aspect_desc else ""
    aspect_integration = ". Si aspect majeur présent, l'intégrer comme tension ou soutien concret." if aspect_desc else ""

    # Fallback si aucun aspect majeur (garde-fou)
    fallback_note = ""
    if not aspect_desc:
        fallback_note = "\n\n(Aucun aspect majeur ≤6° détecté. Concentre-toi sur le triptyque Planète-Signe-Maison comme base solide.)"

    prompt = f"""Tu es un astrologue senior, pédagogique, précis, non ésotérique. Objectif : produire une interprétation structurée, concrète, actionnable.

RÈGLES STRICTES:
- Tu utilises UNIQUEMENT les aspects majeurs fournis (conjonction, opposition, carré, trigone) avec orbe ≤6°.
- Tu hiérarchises : Soleil/Lune/Ascendant > Nœud Nord/Sud > autres planètes.
- Tu relies TOUJOURS : planète + signe + maison{aspect_mention}. Pas de généralités vagues.
- Tu donnes des EXEMPLES COMPORTEMENTAUX concrets, pas de "tu es quelqu'un de...".
- Ton style : français clair, moderne, direct, professionnel.

DONNÉES DU THÈME:
- {subject_label} en {sign}{house_context}{aspect_context}{asc_context}{priority_level}{fallback_note}

TEMPLATE À SUIVRE (EXACT):

# {emoji} {subject_label} en {sign}
**En une phrase :** [UNE phrase très spécifique qui croise {subject_label} + {sign} + Maison {chart_payload.house or 'N'}{aspect_mention}, avec exemple comportemental concret]

## Ton moteur
[2-3 phrases max : ce que {subject_label} en {sign} en Maison {chart_payload.house or 'N'} pousse à faire, rechercher, exprimer. Croiser SYSTÉMATIQUEMENT ces 3 dimensions. Exemples concrets de manifestation (comportements, patterns, situations). Pas "tu es quelqu'un de..."]

## Ton défi
[1-2 phrases : le piège typique de {subject_label} en {sign} en Maison {chart_payload.house or 'N'}. Équilibré lumière-ombre. Exemple concret de comment ce piège se manifeste.]

## Maison {chart_payload.house or 'N'} en {sign}
[1-2 phrases : comment {subject_label} exprime {sign} concrètement dans le domaine de la Maison {chart_payload.house or 'N'} ({house_short_label}). Croiser les 3 infos{aspect_integration} Exemples de situations réelles.]

CONTRAINTES STRICTES:
1. LONGUEUR: 700 à 1000 caractères (max absolu 1200). Compte tes caractères.
2. INTERDIT: "tu es quelqu'un de...", "tu ressens profondément...", généralités vides.
3. INTERDIT: Prédictions ("tu vas rencontrer...", "il arrivera...").
4. INTERDIT: Conseils santé/diagnostic.
5. OBLIGATOIRE: CROISER SYSTÉMATIQUEMENT {subject_label} + {sign} + Maison {chart_payload.house or 'N'} dans CHAQUE section. C'est le triptyque central.
6. OBLIGATOIRE: Exemples comportementaux concrets, situations réelles, patterns observables.
7. TON: Présent ou infinitif. Jamais futur. Vocabulaire simple, moderne, professionnel.
8. FORMAT: Markdown strict. Les ## sont obligatoires. Pas de titre supplémentaire après le #.
9. PAS DE SECTION MICRO-RITUEL: Le template s'arrête après "Maison N en Signe".

GÉNÈRE L'INTERPRÉTATION MAINTENANT (français, markdown, 700-1000 chars):"""

    return prompt


# ============================================================================
# V4 SENIOR PROFESSIONNEL - Fonction → Signe → Maison → Manifestations
# ============================================================================

# Mapping des fonctions planétaires (archétypes)
PLANET_FUNCTIONS_V4 = {
    'sun': 'identité centrale, énergie vitale, volonté',
    'moon': 'besoins émotionnels, sécurité, réactions instinctives',
    'mercury': 'intellect, communication, analyse',
    'venus': 'valeurs, relations, capacité à recevoir',
    'mars': 'action, désir, affirmation',
    'jupiter': 'expansion, sens, optimisme',
    'saturn': 'structure, limites, responsabilité',
    'uranus': 'innovation, liberté, rupture',
    'neptune': 'dissolution, inspiration, transcendance',
    'pluto': 'transformation, pouvoir, régénération',
    'ascendant': 'masque social, façon d\'entrer en contact',
    'midheaven': 'vocation, image publique, accomplissement',
    'north_node': 'chemin de vie, territoire à conquérir',
    'south_node': 'acquis passés, zone de confort',
    'chiron': 'blessure originelle, don de guérison'
}


def get_opposite_sign_v4(sign: str) -> str:
    """Retourne le signe opposé (pour axe NN/NS)"""
    opposites = {
        'Bélier': 'Balance', 'Balance': 'Bélier',
        'Taureau': 'Scorpion', 'Scorpion': 'Taureau',
        'Gémeaux': 'Sagittaire', 'Sagittaire': 'Gémeaux',
        'Cancer': 'Capricorne', 'Capricorne': 'Cancer',
        'Lion': 'Verseau', 'Verseau': 'Lion',
        'Vierge': 'Poissons', 'Poissons': 'Vierge'
    }
    return opposites.get(sign, sign)


def build_interpretation_prompt_v4_senior(
    subject: str,
    chart_payload: ChartPayload
) -> str:
    """
    Construit le prompt v4 'senior professionnel' style
    
    Template structuré:
    1. Fonction planétaire → 2. Coloration signe → 3. Domaine vie (maison)
    4. Manifestations observables → 5. Vigilance
    
    Cas spécial Nœud Nord/Sud: traité comme axe d'évolution
    Lilith exclue (validation en amont dans route)
    """
    emoji = SUBJECT_EMOJI.get(subject, '⭐')
    subject_label = chart_payload.subject_label
    sign = chart_payload.sign

    # Validation : signe obligatoire
    if not sign or sign.strip() == '':
        logger.error(f"❌ v4: Signe manquant pour {subject}")
        raise ValueError(f"Signe manquant pour {subject_label} ({subject}).")

    # Fonction planétaire archétypale
    planet_function = PLANET_FUNCTIONS_V4.get(subject, 'fonction archétypale')

    # Maison
    house_context = ""
    house_short_label = ""
    if chart_payload.house:
        house_short_label, house_full = get_house_label_v2(chart_payload.house)
        house_context = f"\n- {house_full}"

    # Aspect majeur v4 (réutilise find_relevant_aspect_v3: orb <= 6°, majeurs uniquement)
    aspect_context = ""
    aspect_desc = None
    try:
        aspect_desc = find_relevant_aspect_v3(subject, chart_payload)
        if aspect_desc:
            aspect_context = f"\n- Aspect majeur : {aspect_desc}"
    except Exception as aspect_err:
        logger.warning(f"⚠️ v4: Erreur recherche aspect pour {subject}: {aspect_err}")
        aspect_desc = None

    # Ascendant (contexte global)
    asc_context = ""
    if chart_payload.ascendant_sign:
        asc_context = f"\n- Ascendant en {chart_payload.ascendant_sign}"

    # Cas spécial: Axe des Nœuds (traiter comme axe d'évolution)
    is_node = subject in ['north_node', 'south_node']
    node_context = ""

    if is_node:
        opposite_sign = get_opposite_sign_v4(sign)
        opposite_house = ((chart_payload.house or 1) + 6 - 1) % 12 + 1  # Maison opposée

        if subject == 'north_node':
            node_context = f"\n\n⚠️ AXE D'ÉVOLUTION: Nœud Nord en {sign} (Maison {chart_payload.house}) = chemin de vie. Nœud Sud en {opposite_sign} (Maison {opposite_house}) = acquis à transcender. Traiter l'axe comme dynamique évolutive."
        else:  # south_node
            opposite_sign_nn = get_opposite_sign_v4(sign)  # NN est à l'opposé du NS
            opposite_house_nn = ((chart_payload.house or 1) + 6 - 1) % 12 + 1
            node_context = f"\n\n⚠️ AXE D'ÉVOLUTION: Nœud Sud en {sign} (Maison {chart_payload.house}) = confort familier. Nœud Nord en {opposite_sign_nn} (Maison {opposite_house_nn}) = territoire à conquérir. Traiter l'axe comme dynamique évolutive."

    # Fallback si aucun aspect majeur
    fallback_note = ""
    if not aspect_desc:
        fallback_note = "\n\n(Aucun aspect majeur ≤6° détecté. Concentre-toi sur Fonction-Signe-Maison.)"

    # Construire parties conditionnelles
    aspect_mention = " + Aspect" if aspect_desc else ""

    # Template v4 selon type de sujet
    if is_node:
        # Template spécial pour les Nœuds (axe)
        prompt = f"""Tu es un astrologue senior professionnel. Style : précis, concret, pédagogique, non ésotérique.

DONNÉES DU THÈME:
- {subject_label} en {sign}{house_context}{aspect_context}{asc_context}{node_context}{fallback_note}

TEMPLATE À SUIVRE (EXACT):

# {emoji} {subject_label} en {sign}

## 1. L'axe des Nœuds Lunaires
[2 phrases : expliquer que c'est un AXE d'évolution, pas juste un point. {subject_label} en {sign} = {'chemin de vie à développer' if subject == 'north_node' else 'acquis passés à transcender'}. L'autre pôle enrichit le sens.]

## 2. Fonction du {'Nœud Nord' if subject == 'north_node' else 'Nœud Sud'}
[2 phrases : {planet_function}. Expliciter cette fonction archétypale avant de parler du signe.]

## 3. Coloration {sign}
[2 phrases : comment {sign} module cette fonction. Exemples comportementaux concrets. Pas de "tu es...".]

## 4. Domaine de vie (Maison {chart_payload.house or 'N'})
[2 phrases : où cet axe se joue concrètement. Maison {chart_payload.house or 'N'} = {house_short_label}. Situations réelles{'. Intégrer aspect si pertinent' if aspect_desc else ''}.]

## 5. Manifestations observables
[2-3 phrases : patterns comportementaux concrets. Exemples de situations vécues (max 3 exemples). {'Dynamique NN/NS : tension entre confort et croissance' if subject == 'north_node' else "Dynamique NS/NN : dépasser l'acquis pour évoluer"}.]

## 6. Vigilance
[1-2 phrases : piège typique. {'Rester bloqué dans le Nœud Sud' if subject == 'north_node' else 'Dévaloriser les acquis du Nœud Sud'}. Exemple concret factuel, non mystique.]

CONTRAINTES STRICTES:
1. LONGUEUR: 800-1100 chars (max 1300).
2. INTERDIT: "tu es...", prédictions, conseils santé, spiritualisation, coaching.
3. OBLIGATOIRE: Croiser Fonction + Signe + Maison + Axe NN/NS.
4. OBLIGATOIRE: Max 3 exemples comportementaux concrets, incarnés.
5. TON: Professionnel analytique. Présent/infinitif. Vocabulaire simple.
6. FORMAT: Markdown strict, ## obligatoires.
7. VIGILANCE: Courte, factuelle, non mystique.

GÉNÈRE L'INTERPRÉTATION (français, markdown, 800-1100 chars):"""

    else:
        # Template standard planètes/points
        prompt = f"""Tu es un astrologue senior professionnel. Style : précis, concret, pédagogique, non ésotérique.

DONNÉES DU THÈME:
- {subject_label} en {sign}{house_context}{aspect_context}{asc_context}{fallback_note}

TEMPLATE À SUIVRE (EXACT):

# {emoji} {subject_label} en {sign}

## 1. Fonction planétaire
[2 phrases : {planet_function}. Expliciter cette fonction archétypale de {subject_label} avant de parler du signe. Qu'est-ce que {subject_label} fait dans un thème ?]

## 2. Coloration par {sign}
[2 phrases : comment {sign} module la fonction de {subject_label}. Exemples comportementaux concrets. Pas de "tu es...".]

## 3. Domaine de vie (Maison {chart_payload.house or 'N'})
[2 phrases : où {subject_label} en {sign} s'exprime concrètement. Maison {chart_payload.house or 'N'} = {house_short_label}. Situations réelles{'. Intégrer aspect comme tension ou soutien' if aspect_desc else ''}.]

## 4. Manifestations observables
[2-3 phrases : patterns comportementaux concrets. Exemples de situations vécues (max 3 exemples). Croiser systématiquement Fonction + Signe + Maison{aspect_mention}.]

## 5. Vigilance
[1-2 phrases : piège typique de {subject_label} en {sign} en Maison {chart_payload.house or 'N'}. Factuel, non mystique. Exemple concret.]

CONTRAINTES STRICTES:
1. LONGUEUR: 800-1100 chars (max 1300).
2. INTERDIT: "tu es...", prédictions, conseils santé, spiritualisation, coaching.
3. OBLIGATOIRE: Croiser Fonction + Signe + Maison{aspect_mention}.
4. OBLIGATOIRE: Max 3 exemples comportementaux concrets, incarnés.
5. TON: Professionnel analytique. Présent/infinitif. Vocabulaire simple.
6. FORMAT: Markdown strict, ## obligatoires.
7. MANIFESTATIONS: Concrètes, incarnées, max 3 exemples.
8. VIGILANCE: Courte, factuelle, non mystique.

GÉNÈRE L'INTERPRÉTATION (français, markdown, 800-1100 chars):"""

    return prompt



def validate_interpretation_length(text: str, version: int = 2) -> Tuple[bool, int]:
    """
    Valide que l'interprétation respecte les contraintes de longueur

    Args:
        text: Texte de l'interprétation
        version: Version du prompt (2 ou 3)

    Returns:
        tuple: (is_valid, length)
    """
    length = len(text)
    if version == 4:
        # v4: 800-1300 chars (senior professionnel structuré)
        return (800 <= length <= 1300), length
    elif version == 3:
        # v3: 700-1200 chars (senior expérimental déprécié)
        return (700 <= length <= 1200), length
    else:
        # v2: 900-1400 chars (moderne avec micro-rituel)
        return (900 <= length <= 1400), length


async def generate_with_sonnet_fallback_haiku(
    subject: str,
    chart_payload: Dict[str, Any] | ChartPayload,
    version: int = None
) -> Tuple[str, str]:
    """
    Génère une interprétation avec Claude Sonnet, fallback sur Haiku si erreur

    Stratégie (NATAL_LLM_MODE):
    - Si "off" (default): retourne placeholder sans appel API
    - Si "anthropic":
      1. Essayer Sonnet 3.5
      2. Si erreur (429, timeout, 5xx) -> fallback Haiku
      3. Si erreur auth/credit (401, 400) -> fallback placeholder
      4. Valider longueur selon version (v2: 900-1400, v3: 700-1200, v4: 800-1300)
      5. Si hors limites -> retry 1x avec prompt d'ajustement
      6. Si toujours hors limites -> tronquer proprement

    Args:
        subject: Objet céleste à interpréter
        chart_payload: Données du chart
        version: Version du prompt (2, 3, ou 4). Si None, utilise PROMPT_VERSION global.

    Returns:
        tuple: (interpretation_text, model_used)
    """
    # Utiliser PROMPT_VERSION global si non spécifié
    if version is None:
        version = PROMPT_VERSION

    # Convertir en ChartPayload si nécessaire
    if isinstance(chart_payload, dict):
        payload = ChartPayload(**chart_payload)
    else:
        payload = chart_payload

    # Vérifier le mode LLM
    llm_mode = settings.NATAL_LLM_MODE.lower()

    if llm_mode != "anthropic":
        # Mode off : essayer de charger interprétation pré-générée
        logger.info(f"🚫 NATAL_LLM_MODE={llm_mode} - Recherche interprétation pré-générée pour {subject} en {payload.sign}")

        # Essayer de charger l'interprétation pré-générée
        pregenerated_text = load_pregenerated_interpretation(
            subject=subject,
            sign=payload.sign or "",
            house=payload.house or 1,
            version=version
        )

        if pregenerated_text:
            logger.info(f"✅ Interprétation pré-générée trouvée pour {subject} en {payload.sign}")
            return pregenerated_text, "pregenerated"

        # Si pas de fichier, fallback sur placeholder
        logger.warning(f"⚠️ Pas d'interprétation pré-générée pour {subject} en {payload.sign} M{payload.house}, fallback placeholder")
        placeholder_text = generate_placeholder_interpretation(subject, payload, version)
        return placeholder_text, "placeholder"
    # #region agent log
    import json
    import time
    try:
        log_data = {
            "location": "natal_interpretation_service.py:221",
            "message": "generate_with_sonnet_fallback_haiku entry",
            "data": {
                "subject": subject,
                "payload_type": type(payload).__name__,
                "payload_sign": payload.sign if hasattr(payload, 'sign') else None
            },
            "timestamp": int(time.time() * 1000),
            "sessionId": "debug-session",
            "runId": "run1",
            "hypothesisId": "C"
        }
        with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as log_err:
        logger.warning(f"Erreur écriture log debug: {log_err}")
    # #endregion

    # #region agent log
    try:
        log_data = {
            "location": "natal_interpretation_service.py:245",
            "message": f"Before build_interpretation_prompt_v{version}",
            "data": {
                "subject": subject,
                "payload_sign": payload.sign,
                "payload_house": payload.house,
                "payload_subject_label": payload.subject_label,
                "version": version
            },
            "timestamp": int(time.time() * 1000),
            "sessionId": "debug-session",
            "runId": "run1",
            "hypothesisId": "D"
        }
        with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
            f.write(json.dumps(log_data) + "\n")
    except Exception as log_err:
        logger.warning(f"Erreur écriture log debug: {log_err}")
    # #endregion

    # Construire le prompt selon la version
    try:
        if version == 4:
            prompt = build_interpretation_prompt_v4_senior(subject, payload)
        elif version == 3:
            prompt = build_interpretation_prompt_v3_senior(subject, payload)
        else:
            prompt = build_interpretation_prompt_v2(subject, payload)
    except Exception as prompt_err:
        # #region agent log
        try:
            log_data = {
                "location": "natal_interpretation_service.py:250",
                "message": "Error in build_interpretation_prompt_v2",
                "data": {
                    "error": str(prompt_err),
                    "error_type": type(prompt_err).__name__,
                    "subject": subject,
                    "payload_sign": payload.sign if hasattr(payload, 'sign') else None
                },
                "timestamp": int(time.time() * 1000),
                "sessionId": "debug-session",
                "runId": "run1",
                "hypothesisId": "E"
            }
            with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                f.write(json.dumps(log_data) + "\n")
        except Exception as log_err:
            logger.warning(f"Erreur écriture log debug: {log_err}")
        # #endregion
        raise

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
            
            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:300",
                    "message": "Before Claude API call",
                    "data": {
                        "model": model_name,
                        "subject": subject,
                        "prompt_length": len(prompt),
                        "prompt_preview": prompt[:200] + "..." if len(prompt) > 200 else prompt
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "H"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion

            message = client.messages.create(
                model=model_id,
                max_tokens=2048,
                temperature=0.7,
                messages=[{"role": "user", "content": prompt}],
                timeout=30.0
            )
            
            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:440",
                    "message": "Claude API call successful",
                    "data": {
                        "model": model_name,
                        "has_content": bool(message.content),
                        "content_length": len(message.content) if message.content else 0,
                        "content_type": type(message.content).__name__ if message.content else None,
                        "first_item_type": type(message.content[0]).__name__ if message.content and len(message.content) > 0 else None,
                        "has_text_attr": hasattr(message.content[0], 'text') if message.content and len(message.content) > 0 else False
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "I"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion

            # Gérer le cas où message.content est vide ou mal formaté
            if not message.content or len(message.content) == 0:
                raise ValueError(f"Claude {model_name} a retourné un contenu vide")
            
            # Vérifier que le premier élément a un attribut text
            if not hasattr(message.content[0], 'text'):
                raise ValueError(f"Claude {model_name} a retourné un format de contenu inattendu: {type(message.content[0])}")
            
            text_content = message.content[0].text.strip()
            
            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:465",
                    "message": "Text content extracted",
                    "data": {
                        "model": model_name,
                        "text_length": len(text_content),
                        "text_preview": text_content[:100] if text_content else "EMPTY"
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "L"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion
            is_valid, length = validate_interpretation_length(text_content, version)

            # Définir les seuils selon la version
            if version == 4:
                min_chars, max_chars, target_range = 800, 1300, "900-1100"
            elif version == 3:
                min_chars, max_chars, target_range = 700, 1200, "800-1000"
            else:
                min_chars, max_chars, target_range = 900, 1400, "1000-1200"

            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:493",
                    "message": "After validate_interpretation_length",
                    "data": {
                        "model": model_name,
                        "version": version,
                        "length": length,
                        "is_valid": is_valid,
                        "will_truncate": length > max_chars,
                        "min_chars": min_chars,
                        "max_chars": max_chars
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "M"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion

            logger.info(f"✅ {model_name} v{version} - Texte généré: {length} chars (valid={is_valid})")

            # Si longueur invalide, retry 1x avec prompt d'ajustement
            if not is_valid and length < min_chars:
                logger.warning(f"⚠️ Texte trop court ({length} chars), retry avec expansion")
                adjust_prompt = f"{prompt}\n\nATTENTION: Le texte précédent était trop court ({length} chars). Développe davantage en gardant le même template, vise {target_range} caractères."

                message = client.messages.create(
                    model=model_id,
                    max_tokens=2048,
                    temperature=0.7,
                    messages=[{"role": "user", "content": adjust_prompt}],
                    timeout=30.0
                )

                text_content = message.content[0].text.strip()
                is_valid, length = validate_interpretation_length(text_content, version)
                logger.info(f"✅ Retry {model_name} v{version}: {length} chars (valid={is_valid})")

            elif not is_valid and length > max_chars:
                logger.warning(f"⚠️ Texte trop long ({length} chars), retry avec réduction")
                adjust_prompt = f"{prompt}\n\nATTENTION: Le texte précédent était trop long ({length} chars). Réduis-le à {target_range} caractères en retirant les répétitions et en gardant l'essentiel."

                message = client.messages.create(
                    model=model_id,
                    max_tokens=2048,
                    temperature=0.7,
                    messages=[{"role": "user", "content": adjust_prompt}],
                    timeout=30.0
                )

                text_content = message.content[0].text.strip()
                is_valid, length = validate_interpretation_length(text_content, version)
                logger.info(f"✅ Retry {model_name} v{version}: {length} chars (valid={is_valid})")

            # Si toujours trop long après retry, tronquer proprement
            if length > max_chars:
                truncate_to = max_chars - 3
                logger.warning(f"⚠️ Tronquage à {max_chars} chars (était {length})")
                text_content = text_content[:truncate_to] + "..."
                length = len(text_content)

            logger.info(f"✅ Interprétation finale v{version}: {length} chars, modèle={model_name}")

            # Calculer nombre d'aspects disponibles pour comparaison v2/v3
            aspect_count_v2 = 0  # aspects avec orb <=3°
            aspect_count_v3 = 0  # aspects majeurs avec orb <=6°
            if payload.aspects and isinstance(payload.aspects, list):
                MAJOR_ASPECTS = {'conjunction', 'opposition', 'square', 'trine'}
                for aspect in payload.aspects:
                    if not isinstance(aspect, dict):
                        continue
                    try:
                        orb = abs(float(aspect.get('orb', 999)))
                        aspect_type = aspect.get('type', '').lower()

                        if orb <= 3:
                            aspect_count_v2 += 1
                        if orb <= 6 and aspect_type in MAJOR_ASPECTS:
                            aspect_count_v3 += 1
                    except (ValueError, TypeError):
                        continue

            # Log comparatif v2/v3 pour analyse qualitative
            logger.info(f"📊 Aspects disponibles: v2={aspect_count_v2} (orb<=3°), v3={aspect_count_v3} (majeurs orb<=6°)")

            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:540",
                    "message": "Before return from generate_with_sonnet_fallback_haiku",
                    "data": {
                        "version": version,
                        "model": model_name,
                        "final_length": length,
                        "aspect_count_v2": aspect_count_v2,
                        "aspect_count_v3": aspect_count_v3,
                        "text_preview": text_content[:150] if text_content else "EMPTY"
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "N"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion

            return text_content, model_name

        except (RateLimitError, APIConnectionError) as e:
            logger.warning(f"⚠️ {model_name} échec ({type(e).__name__}): {str(e)[:100]}")
            # #region agent log
            try:
                log_data = {
                    "location": "natal_interpretation_service.py:508",
                    "message": "Claude API error (RateLimit/Connection)",
                    "data": {
                        "error": str(e),
                        "error_type": type(e).__name__,
                        "model": model_name,
                        "subject": subject
                    },
                    "timestamp": int(time.time() * 1000),
                    "sessionId": "debug-session",
                    "runId": "run1",
                    "hypothesisId": "J"
                }
                with open('/Users/remibeaurain/astroia/.cursor/debug.log', 'a') as f:
                    f.write(json.dumps(log_data) + "\n")
            except Exception as log_err:
                logger.warning(f"Erreur écriture log debug: {log_err}")
            # #endregion
            last_error = e
            # Continuer vers le fallback
            continue

        except APIError as e:
            error_code = getattr(e, 'status_code', 0)
            error_type = getattr(e, 'type', '')

            # 401 authentication_error = clé API invalide -> fallback placeholder
            if error_code == 401 or 'authentication_error' in str(e):
                logger.warning(f"⚠️ {model_name} auth invalide (401), fallback vers placeholder")
                placeholder_text = generate_placeholder_interpretation(subject, payload, version)
                return placeholder_text, "placeholder-auth-error"

            # 400 insufficient_quota ou credit = crédits épuisés -> fallback placeholder
            if error_code == 400 and ('insufficient_quota' in str(e) or 'credit' in str(e).lower()):
                logger.warning(f"⚠️ {model_name} crédits insuffisants (400), fallback vers placeholder")
                placeholder_text = generate_placeholder_interpretation(subject, payload, version)
                return placeholder_text, "placeholder-credit-error"

            # 404 not_found_error = modèle non accessible -> fallback vers autre modèle
            if error_code == 404 or 'not_found_error' in str(e):
                logger.warning(f"⚠️ {model_name} non accessible (404), fallback")
                last_error = e
                continue

            # 429, 5xx = erreurs temporaires -> fallback vers autre modèle
            if error_code in [429, 500, 502, 503, 504]:
                logger.warning(f"⚠️ {model_name} échec (HTTP {error_code}), fallback")
                last_error = e
                continue

            # Autres erreurs (400 non-credit, etc.) = non-récupérables
            logger.error(f"❌ {model_name} erreur non-récupérable: {e}")
            raise Exception(f"Erreur API Claude ({model_name}): {str(e)}")

    # Si tous les modèles ont échoué
    if last_error:
        logger.error(f"❌ Tous les modèles ont échoué, dernière erreur: {last_error}")
        raise Exception(f"Impossible de générer l'interprétation: {str(last_error)}")

    raise Exception("Aucun modèle disponible")
