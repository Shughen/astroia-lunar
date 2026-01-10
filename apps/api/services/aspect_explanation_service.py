"""
Service pour générer les explications pédagogiques des aspects majeurs (v4)

Ce module fournit:
- Filtrage v4 des aspects (types majeurs, orbe ≤6°, exclure Lilith)
- Calcul métadonnées (expectedAngle, actualAngle, deltaToExact, placements)
- Génération copy (summary, why, manifestation, advice) via templates
- Support optionnel génération AI (Haiku) derrière flag ASPECT_COPY_ENGINE

Architecture alignée avec natal_interpretation_service.py (template-first, AI optional)
"""

import logging
from typing import Dict, Any, List, Optional, Tuple
import hashlib
from datetime import datetime

logger = logging.getLogger(__name__)

# === CONSTANTES V4 ===

# Types d'aspects majeurs uniquement (v4 senior professionnel)
MAJOR_ASPECT_TYPES = {'conjunction', 'opposition', 'square', 'trine'}

# Orbe maximum pour v4 (strict)
MAX_ORB_V4 = 6.0

# Angles exacts attendus pour chaque type d'aspect
EXPECTED_ANGLES: Dict[str, int] = {
    'conjunction': 0,
    'opposition': 180,
    'square': 90,
    'trine': 120,
}

# Symboles d'aspects pour affichage
ASPECT_SYMBOLS: Dict[str, str] = {
    'conjunction': '☌',
    'opposition': '☍',
    'square': '□',
    'trine': '△',
}

# Noms français des aspects
ASPECT_NAMES_FR: Dict[str, str] = {
    'conjunction': 'Conjonction',
    'opposition': 'Opposition',
    'square': 'Carré',
    'trine': 'Trigone',
}


# === TEMPLATES V4 (TONE SENIOR PROFESSIONNEL) ===

ASPECT_TEMPLATES_V4: Dict[str, Dict[str, Any]] = {
    'conjunction': {
        'summary': "{p1} et {p2} fusionnent leurs énergies en {sign1}. Symbiose puissante, intensité garantie.",
        'why': [
            "Angle 0° : les deux planètes occupent le même degré zodiacal",
            "Fusion d'énergies : impossible de dissocier {p1_function} et {p2_function}",
            "Effet d'amplification mutuelle : chaque planète renforce l'autre"
        ],
        'manifestation': (
            "{p1} ({p1_function}) et {p2} ({p2_function}) agissent comme un seul moteur. "
            "Cette fusion se déploie en {sign1}, colorant l'expression de manière homogène. "
            "Maison {house1} : {house1_label}. "
            "Concrètement : {concrete_example}. "
            "Attention à l'indissociation : difficile de mobiliser {p1} sans activer {p2} (et inversement)."
        ),
        'advice': "Observer les contextes où cette fusion devient un atout (synergie) vs. un piège (confusion des rôles).",
        'concrete_examples': {
            ('sun', 'mercury'): "pensée et identité fusionnent → expression très personnelle, subjectivité assumée",
            ('moon', 'venus'): "besoins émotionnels et affectifs alignés → attachement rapide, émotions esthétisées",
            ('mars', 'jupiter'): "action et expansion combinées → initiatives ambitieuses, énergie débordante",
            ('default', 'default'): "les fonctions planétaires se confondent → expression unitaire, difficulté à séparer les registres"
        }
    },

    'opposition': {
        'summary': "{p1} ({sign1}) et {p2} ({sign2}) face à face. Tension polarisée, équilibre à construire.",
        'why': [
            "Angle 180° : les deux planètes occupent des signes opposés du zodiaque",
            "Axe de tension : {p1_function} vs. {p2_function} en polarité",
            "Dynamique miroir : chaque planète révèle ce que l'autre occulte"
        ],
        'manifestation': (
            "{p1} en {sign1} (Maison {house1}) tire vers {house1_label}, "
            "tandis que {p2} en {sign2} (Maison {house2}) oriente vers {house2_label}. "
            "Axe de vie structurant : impossible d'ignorer l'une des polarités sans déséquilibre. "
            "Concrètement : {concrete_example}. "
            "Objectif : intégration consciente, pas élimination d'un pôle."
        ),
        'advice': "Chercher le juste milieu entre les deux pôles : ni exclusion, ni alternance chaotique.",
        'concrete_examples': {
            ('sun', 'moon'): "identité solaire vs. besoins lunaires → négociation constante entre volonté et ressenti",
            ('venus', 'mars'): "désir affectif vs. pulsion d'action → équilibre attraction/autonomie",
            ('mercury', 'jupiter'): "analyse détaillée vs. vision globale → dialogue entre précision et perspective",
            ('default', 'default'): "deux fonctions en miroir → tension créatrice, nécessité d'intégrer les contraires"
        }
    },

    'square': {
        'summary': "{p1} ({sign1}) et {p2} ({sign2}) en friction. Tension dynamique, moteur de changement.",
        'why': [
            "Angle 90° : les deux planètes occupent des signes en quadrature (modes incompatibles)",
            "Conflit fonctionnel : {p1_function} et {p2_function} se contrarient",
            "Friction productive : l'inconfort génère du mouvement et des ajustements"
        ],
        'manifestation': (
            "{p1} en {sign1} (Maison {house1}) cherche à {house1_label}, "
            "mais {p2} en {sign2} (Maison {house2}) impose {house2_label}, "
            "créant une friction interne. "
            "Concrètement : {concrete_example}. "
            "Cette tension n'est pas pathologique : elle force l'adaptation, la créativité, la résolution de problèmes."
        ),
        'advice': "Utiliser la friction comme catalyseur : ne pas chercher à éliminer la tension, mais à la canaliser.",
        'concrete_examples': {
            ('sun', 'saturn'): "volonté d'expression vs. exigence de structure → frustrations formatives, discipline difficile mais nécessaire",
            ('moon', 'uranus'): "besoins de sécurité vs. pulsions de changement → instabilité émotionnelle productive",
            ('mars', 'neptune'): "action directe vs. dissolution des frontières → difficulté à passer à l'acte, ajustements constants",
            ('default', 'default'): "deux fonctions en conflit modal → inconfort structurel, levier de croissance"
        }
    },

    'trine': {
        'summary': "{p1} ({sign1}) et {p2} ({sign2}) en harmonie fluide. Synergie naturelle, facilité d'expression.",
        'why': [
            "Angle 120° : les deux planètes occupent des signes de même élément (feu, terre, air, eau)",
            "Compatibilité élémentale : {p1_function} et {p2_function} parlent le même langage",
            "Fluidité : pas de friction, circulation d'énergie naturelle"
        ],
        'manifestation': (
            "{p1} en {sign1} (Maison {house1}) nourrit {house1_label}, "
            "et {p2} en {sign2} (Maison {house2}) amplifie {house2_label} sans effort. "
            "Concrètement : {concrete_example}. "
            "Attention : la facilité peut générer de la complaisance (talent non exploité, confort non questionné)."
        ),
        'advice': "Mobiliser activement cette ressource : la fluidité n'est pas synonyme d'automatisme vertueux.",
        'concrete_examples': {
            ('sun', 'jupiter'): "identité et expansion alignées → confiance naturelle, optimisme facile, risque de sur-extension",
            ('moon', 'neptune'): "besoins émotionnels et imaginaire fluides → empathie spontanée, porosité à surveiller",
            ('venus', 'saturn'): "affectivité et structure compatibles → relations stables, loyauté naturelle, risque de rigidité",
            ('default', 'default'): "deux fonctions en harmonie élémentale → facilité, talent, vigilance sur la passivité"
        }
    }
}


# === FONCTIONS PLANÉTAIRES V4 (RÉUTILISÉES DEPUIS NATAL_INTERPRETATION_SERVICE) ===
# Import depuis natal_interpretation_service pour cohérence
try:
    from services.natal_interpretation_service import PLANET_FUNCTIONS_V4
except ImportError:
    logger.warning("⚠️ Impossible d'importer PLANET_FUNCTIONS_V4 depuis natal_interpretation_service, fallback local")
    # Fallback local (copie simplifiée)
    PLANET_FUNCTIONS_V4 = {
        'sun': 'identité centrale, énergie vitale, volonté',
        'moon': 'besoins émotionnels, sécurité, réactions instinctives',
        'mercury': 'intellect, communication, analyse',
        'venus': 'désir, valeurs, esthétique, affectivité',
        'mars': 'action, pulsion, combat, affirmation',
        'jupiter': 'expansion, optimisme, foi, générosité',
        'saturn': 'structure, limite, responsabilité, temps',
        'uranus': 'rupture, innovation, indépendance',
        'neptune': 'dissolution, imaginaire, transcendance',
        'pluto': 'transformation radicale, pouvoir, mort-renaissance',
        'ascendant': 'interface au monde, persona',
        'midheaven': 'accomplissement, visibilité sociale',
        'north_node': 'chemin évolutif, direction de vie',
        'south_node': 'acquis karmiques, zone de confort',
        'chiron': 'blessure archétypale, guérison',
    }


# === LABELS MAISONS (RÉUTILISÉS DEPUIS NATALCHARTUTILS) ===
HOUSE_LABELS = {
    1: "identité, apparence",
    2: "ressources, valeurs",
    3: "communication, environnement proche",
    4: "foyer, racines",
    5: "créativité, plaisir",
    6: "quotidien, service",
    7: "relations, partenariats",
    8: "intimité, transformation",
    9: "philosophie, expansion",
    10: "carrière, accomplissement",
    11: "projets collectifs, idéaux",
    12: "spiritualité, inconscient"
}


# === FILTRAGE V4 ===

def filter_major_aspects_v4(aspects: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Filtre les aspects selon règles v4 (senior professionnel)

    Règles:
    - Types majeurs uniquement: conjunction, opposition, square, trine
    - Orbe strict: <= 6°
    - Exclure Lilith (mean_lilith, lilith, blackmoonlilith, etc.)

    Args:
        aspects: Liste brute des aspects

    Returns:
        Aspects filtrés et triés par orbe croissant
    """
    filtered = []

    for aspect in aspects:
        # 1. Type majeur uniquement
        aspect_type = aspect.get('type', '').lower()
        if aspect_type not in MAJOR_ASPECT_TYPES:
            continue

        # 2. Orbe <= 6°
        orb = abs(aspect.get('orb', 999))
        if orb > MAX_ORB_V4:
            continue

        # 3. Exclure Lilith (toutes variantes)
        planet1 = aspect.get('planet1', '').lower().replace('_', '').replace(' ', '').replace('-', '')
        planet2 = aspect.get('planet2', '').lower().replace('_', '').replace(' ', '').replace('-', '')

        if 'lilith' in planet1 or 'lilith' in planet2:
            continue

        filtered.append(aspect)

    # Tri par orbe croissant (aspects les plus serrés en premier)
    filtered.sort(key=lambda a: abs(a.get('orb', 999)))

    return filtered


# === CALCUL MÉTADONNÉES ===

def calculate_aspect_metadata(
    aspect: Dict[str, Any],
    planets_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Calcule les métadonnées enrichies pour un aspect

    Args:
        aspect: Aspect brut (planet1, planet2, type, orb)
        planets_data: Dict des planètes avec positions (sign, degree, house, longitude)

    Returns:
        {
            'expected_angle': 0|90|120|180,
            'actual_angle': float|None (si longitudes disponibles),
            'delta_to_exact': float|None,
            'placements': {
                'planet1': {'sign': str, 'house': int|None},
                'planet2': {'sign': str, 'house': int|None}
            }
        }
    """
    aspect_type = aspect.get('type', '').lower()
    planet1_key = aspect.get('planet1', '').lower()
    planet2_key = aspect.get('planet2', '').lower()
    orb = aspect.get('orb', 0.0)

    # Expected angle
    expected_angle = EXPECTED_ANGLES.get(aspect_type, 0)

    # Récupérer placements (sign + house) depuis planets_data
    # planets_data est un dict avec des clés comme 'sun', 'moon', 'mercury', etc.
    planet1_data = None
    planet2_data = None

    # Recherche flexible (prendre en compte variantes de nommage)
    for key, data in planets_data.items():
        key_normalized = key.lower().replace('_', '').replace(' ', '').replace('-', '')
        p1_normalized = planet1_key.replace('_', '').replace(' ', '').replace('-', '')
        p2_normalized = planet2_key.replace('_', '').replace(' ', '').replace('-', '')

        if key_normalized == p1_normalized or key.lower() == planet1_key:
            planet1_data = data
        if key_normalized == p2_normalized or key.lower() == planet2_key:
            planet2_data = data

    placements = {
        'planet1': {
            'sign': planet1_data.get('sign', '') if planet1_data else '',
            'house': planet1_data.get('house') if planet1_data else None
        },
        'planet2': {
            'sign': planet2_data.get('sign', '') if planet2_data else '',
            'house': planet2_data.get('house') if planet2_data else None
        }
    }

    # Actual angle (si longitudes disponibles)
    actual_angle = None
    delta_to_exact = None

    if planet1_data and planet2_data:
        lon1 = planet1_data.get('longitude') or planet1_data.get('degree')
        lon2 = planet2_data.get('longitude') or planet2_data.get('degree')

        if lon1 is not None and lon2 is not None:
            # Calculer angle réel (shortest arc)
            angle_diff = abs(lon1 - lon2)
            if angle_diff > 180:
                angle_diff = 360 - angle_diff

            actual_angle = round(angle_diff, 2)
            delta_to_exact = round(abs(actual_angle - expected_angle), 2)

    # Si actual_angle pas disponible, utiliser orb comme approximation de delta_to_exact
    if actual_angle is None and orb is not None:
        delta_to_exact = round(abs(orb), 2)

    return {
        'expected_angle': expected_angle,
        'actual_angle': actual_angle,
        'delta_to_exact': delta_to_exact,
        'placements': placements
    }


# === GÉNÉRATION COPY (TEMPLATE-BASED) ===

def normalize_planet_name(planet_name: str) -> str:
    """
    Normalise le nom de planète pour lookup dans PLANET_FUNCTIONS_V4

    Args:
        planet_name: Nom brut (ex: "Sun", "mean_node", "Milieu du Ciel")

    Returns:
        Nom normalisé (ex: "sun", "north_node", "midheaven")
    """
    normalized = planet_name.lower().strip().replace('_', ' ').replace('-', ' ')

    # Mapping variantes → clés PLANET_FUNCTIONS_V4
    mapping = {
        'sun': 'sun', 'soleil': 'sun',
        'moon': 'moon', 'lune': 'moon',
        'mercury': 'mercury', 'mercure': 'mercury',
        'venus': 'venus', 'vénus': 'venus',
        'mars': 'mars',
        'jupiter': 'jupiter',
        'saturn': 'saturn', 'saturne': 'saturn',
        'uranus': 'uranus',
        'neptune': 'neptune',
        'pluto': 'pluto', 'pluton': 'pluto',
        'ascendant': 'ascendant',
        'midheaven': 'midheaven', 'mc': 'midheaven', 'medium coeli': 'midheaven',
        'milieu du ciel': 'midheaven',
        'north node': 'north_node', 'mean node': 'north_node', 'true node': 'north_node',
        'noeud nord': 'north_node', 'nœud nord': 'north_node',
        'south node': 'south_node', 'noeud sud': 'south_node', 'nœud sud': 'south_node',
        'chiron': 'chiron'
    }

    return mapping.get(normalized, normalized.replace(' ', '_'))


def get_planet_display_name(planet_key: str) -> str:
    """
    Retourne le nom français d'affichage d'une planète

    Args:
        planet_key: Clé normalisée (ex: "sun", "north_node")

    Returns:
        Nom français (ex: "Soleil", "Nœud Nord")
    """
    display_names = {
        'sun': 'Soleil',
        'moon': 'Lune',
        'mercury': 'Mercure',
        'venus': 'Vénus',
        'mars': 'Mars',
        'jupiter': 'Jupiter',
        'saturn': 'Saturne',
        'uranus': 'Uranus',
        'neptune': 'Neptune',
        'pluto': 'Pluton',
        'ascendant': 'Ascendant',
        'midheaven': 'Milieu du Ciel',
        'north_node': 'Nœud Nord',
        'south_node': 'Nœud Sud',
        'chiron': 'Chiron'
    }

    return display_names.get(planet_key, planet_key.capitalize())


def build_aspect_explanation_v4(
    aspect: Dict[str, Any],
    metadata: Dict[str, Any]
) -> Dict[str, str]:
    """
    Génère l'explication pédagogique d'un aspect via templates v4

    Args:
        aspect: Aspect brut (planet1, planet2, type, orb)
        metadata: Métadonnées calculées (expected_angle, actual_angle, placements, etc.)

    Returns:
        {
            'summary': str (140-220 chars),
            'why': List[str] (2-3 bullets factuels),
            'manifestation': str (350-650 chars),
            'advice': str|None (1 phrase max, optionnel)
        }
    """
    aspect_type = aspect.get('type', '').lower()
    planet1_raw = aspect.get('planet1', '')
    planet2_raw = aspect.get('planet2', '')

    # Normaliser les noms de planètes
    planet1_key = normalize_planet_name(planet1_raw)
    planet2_key = normalize_planet_name(planet2_raw)

    # Récupérer template
    template = ASPECT_TEMPLATES_V4.get(aspect_type)
    if not template:
        logger.warning(f"⚠️ Aucun template pour aspect type '{aspect_type}', fallback générique")
        return {
            'summary': f"{get_planet_display_name(planet1_key)} et {get_planet_display_name(planet2_key)} en aspect {aspect_type}.",
            'why': [
                f"Aspect de type {aspect_type}",
                f"Orbe: {abs(aspect.get('orb', 0)):.1f}°"
            ],
            'manifestation': f"Aspect {aspect_type} entre {planet1_key} et {planet2_key}. Explication non disponible.",
            'advice': None
        }

    # Récupérer fonctions planétaires
    p1_function = PLANET_FUNCTIONS_V4.get(planet1_key, 'fonction non définie')
    p2_function = PLANET_FUNCTIONS_V4.get(planet2_key, 'fonction non définie')

    # Récupérer placements
    placements = metadata.get('placements', {})
    sign1 = placements.get('planet1', {}).get('sign', 'N/A')
    sign2 = placements.get('planet2', {}).get('sign', 'N/A')
    house1 = placements.get('planet1', {}).get('house')
    house2 = placements.get('planet2', {}).get('house')

    house1_label = HOUSE_LABELS.get(house1, 'domaine de vie') if house1 else 'domaine non défini'
    house2_label = HOUSE_LABELS.get(house2, 'domaine de vie') if house2 else 'domaine non défini'

    # Sélectionner exemple concret (match par paire de planètes ou fallback)
    concrete_examples = template.get('concrete_examples', {})
    concrete_example = concrete_examples.get(
        (planet1_key, planet2_key),
        concrete_examples.get(
            (planet2_key, planet1_key),  # Essayer ordre inversé
            concrete_examples.get(('default', 'default'), 'interaction planétaire spécifique')
        )
    )

    # Construire summary
    summary = template['summary'].format(
        p1=get_planet_display_name(planet1_key),
        p2=get_planet_display_name(planet2_key),
        sign1=sign1,
        sign2=sign2
    )

    # Construire why (remplacer placeholders)
    why = [
        bullet.format(
            p1_function=p1_function,
            p2_function=p2_function
        )
        for bullet in template['why']
    ]

    # Construire manifestation
    manifestation = template['manifestation'].format(
        p1=get_planet_display_name(planet1_key),
        p2=get_planet_display_name(planet2_key),
        p1_function=p1_function,
        p2_function=p2_function,
        sign1=sign1,
        sign2=sign2,
        house1=house1 or 'N',
        house2=house2 or 'N',
        house1_label=house1_label,
        house2_label=house2_label,
        concrete_example=concrete_example
    )

    # Advice (optionnel)
    advice = template.get('advice')

    return {
        'summary': summary,
        'why': why,
        'manifestation': manifestation,
        'advice': advice
    }


# === FONCTION PRINCIPALE D'ENRICHISSEMENT ===

def enrich_aspects_v4(
    aspects: List[Dict[str, Any]],
    planets_data: Dict[str, Any],
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Enrichit les aspects bruts avec métadonnées + copy v4

    Workflow:
    1. Filtrer aspects v4 (types majeurs, orbe ≤6°, exclure Lilith)
    2. Trier par orbe croissant
    3. Limiter à N aspects (default: 10)
    4. Pour chaque aspect:
       - Calculer métadonnées (expectedAngle, actualAngle, placements)
       - Générer copy (summary, why, manifestation, advice)
       - Ajouter ID unique (hash stable)

    Args:
        aspects: Liste brute des aspects
        planets_data: Dict des planètes avec positions (sign, house, longitude)
        limit: Nombre max d'aspects à retourner (default: 10)

    Returns:
        Liste d'aspects enrichis:
        [
            {
                'id': str,
                'planet1': str,
                'planet2': str,
                'type': str,
                'orb': float,
                'expected_angle': 0|90|120|180,
                'actual_angle': float|None,
                'delta_to_exact': float|None,
                'placements': {...},
                'copy': {
                    'summary': str,
                    'why': List[str],
                    'manifestation': str,
                    'advice': str|None
                }
            },
            ...
        ]
    """
    logger.info(f"[AspectExplanation] Enrichissement aspects v4 - {len(aspects)} aspects bruts")

    # 1. Filtrer v4
    filtered_aspects = filter_major_aspects_v4(aspects)
    logger.info(f"[AspectExplanation] Après filtrage v4: {len(filtered_aspects)} aspects retenus")

    # 2. Limiter
    limited_aspects = filtered_aspects[:limit]

    # 3. Enrichir
    enriched = []
    for aspect in limited_aspects:
        try:
            # Calculer métadonnées
            metadata = calculate_aspect_metadata(aspect, planets_data)

            # Générer copy
            copy = build_aspect_explanation_v4(aspect, metadata)

            # Générer ID unique (hash stable basé sur planet1+planet2+type)
            aspect_id = hashlib.md5(
                f"{aspect.get('planet1')}_{aspect.get('planet2')}_{aspect.get('type')}".encode()
            ).hexdigest()[:12]

            # Construire aspect enrichi
            enriched_aspect = {
                'id': aspect_id,
                'planet1': aspect.get('planet1'),
                'planet2': aspect.get('planet2'),
                'type': aspect.get('type'),
                'orb': aspect.get('orb'),
                'expected_angle': metadata.get('expected_angle'),
                'actual_angle': metadata.get('actual_angle'),
                'delta_to_exact': metadata.get('delta_to_exact'),
                'placements': metadata.get('placements'),
                'copy': copy
            }

            enriched.append(enriched_aspect)

            logger.debug(
                f"[AspectExplanation] Aspect enrichi: {aspect.get('planet1')}-{aspect.get('planet2')} "
                f"({aspect.get('type')}) - orbe {abs(aspect.get('orb', 0)):.1f}° - "
                f"summary {len(copy['summary'])} chars, manifestation {len(copy['manifestation'])} chars"
            )

        except Exception as e:
            logger.error(
                f"❌ Erreur enrichissement aspect {aspect.get('planet1')}-{aspect.get('planet2')}: {e}",
                exc_info=True
            )
            # Skip cet aspect en cas d'erreur
            continue

    logger.info(f"✅ [AspectExplanation] {len(enriched)} aspects enrichis")

    return enriched
