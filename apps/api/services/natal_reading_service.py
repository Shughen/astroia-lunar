"""
Service pour générer des lectures complètes de thèmes natals
Optimisé pour minimiser les appels API (plan BASIC : 100 req/mois)
"""

import httpx
import hashlib
import json
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from config import settings
import logging

logger = logging.getLogger(__name__)


# Client HTTP réutilisable
client = httpx.AsyncClient(timeout=60.0)


def generate_cache_key(birth_data: Dict[str, Any]) -> str:
    """
    Génère une clé de cache unique basée sur les données de naissance
    Format: hash(yyyy-mm-ddThh:mm:ss|lat|lon|city|country)
    """
    key_parts = [
        f"{birth_data['year']:04d}-{birth_data['month']:02d}-{birth_data['day']:02d}",
        f"T{birth_data['hour']:02d}:{birth_data['minute']:02d}:{birth_data.get('second', 0):02d}",
        f"{birth_data['latitude']:.6f}",
        f"{birth_data['longitude']:.6f}",
        birth_data.get('city', 'unknown'),
        birth_data.get('country_code', 'XX'),
    ]
    key_string = "|".join(key_parts)
    return hashlib.sha256(key_string.encode()).hexdigest()[:32]


async def call_rapidapi_endpoint(
    endpoint_path: str,
    payload: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Appel générique à un endpoint RapidAPI Best Astrology
    
    Args:
        endpoint_path: Chemin de l'endpoint (ex: "/api/v3/data/positions/enhanced")
        payload: Données à envoyer
    
    Returns:
        Réponse JSON de l'API
    """
    url = f"{settings.BASE_RAPID_URL}{endpoint_path}"
    
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }
    
    logger.info(f"🌐 Appel RapidAPI: {endpoint_path}")
    
    try:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info(f"✅ Réponse RapidAPI reçue: {endpoint_path}")
        return data
        
    except httpx.HTTPStatusError as e:
        logger.error(f"❌ Erreur HTTP RapidAPI {endpoint_path}: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        logger.error(f"❌ Erreur RapidAPI {endpoint_path}: {str(e)}")
        raise


async def get_enhanced_positions(
    birth_data: Dict[str, Any],
    language: str = "fr"
) -> Dict[str, Any]:
    """
    Appel 1: Positions enrichies avec interprétations
    Endpoint: POST /api/v3/data/positions/enhanced
    """
    payload = {
        "subject": {
            "name": f"{birth_data.get('city', 'User')}",
            "birth_data": birth_data
        },
        "options": {
            "house_system": "P",  # Placidus
            "language": language,
            "tradition": "psychological",
            "detail_level": "full",  # Valeurs acceptées: basic, standard, full, professional
            "zodiac_type": "Tropic",
            "active_points": [
                "Sun", "Moon", "Mercury", "Venus", "Mars",
                "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto",
                "Ascendant", "Medium_Coeli", "Mean_Node", "Chiron"
            ],
            "precision": 2
        }
    }
    
    return await call_rapidapi_endpoint("/api/v3/data/positions/enhanced", payload)


async def get_enhanced_aspects(
    birth_data: Dict[str, Any],
    language: str = "fr"
) -> Dict[str, Any]:
    """
    Appel 2: Aspects enrichis avec interprétations
    Endpoint: POST /api/v3/data/aspects/enhanced
    """
    payload = {
        "subject": {
            "name": f"{birth_data.get('city', 'User')}",
            "birth_data": birth_data
        },
        "options": {
            "aspect_types": ["major"],  # conjunction, opposition, trine, square, sextile
            "language": language,
            "orb_system": "standard",
            "include_interpretations": True
        }
    }
    
    return await call_rapidapi_endpoint("/api/v3/data/aspects/enhanced", payload)


async def get_lunar_metrics(
    birth_data: Dict[str, Any],
    language: str = "fr"
) -> Dict[str, Any]:
    """
    Appel 3: Métriques lunaires
    Endpoint: POST /api/v3/data/lunar_metrics
    """
    payload = {
        "subject": {
            "name": f"{birth_data.get('city', 'User')}",
            "birth_data": birth_data
        },
        "options": {
            "language": language,
            "include_mansion": True,
            "include_voc": True
        }
    }
    
    return await call_rapidapi_endpoint("/api/v3/data/lunar_metrics", payload)


async def get_natal_report(
    birth_data: Dict[str, Any],
    language: str = "fr"
) -> Dict[str, Any]:
    """
    Appel 4 (optionnel): Rapport natal complet
    Endpoint: POST /api/v3/reports/natal
    """
    payload = {
        "subject": {
            "name": f"{birth_data.get('city', 'User')}",
            "birth_data": birth_data
        },
        "options": {
            "language": language,
            "report_type": "comprehensive",
            "house_system": "P"
        }
    }
    
    return await call_rapidapi_endpoint("/api/v3/reports/natal", payload)


def parse_positions_to_core_points(positions_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Convertit les positions enrichies en CorePoints
    """
    core_points = []
    
    # Mapping signes abrégés → français
    sign_mapping = {
        'Ari': 'Bélier', 'Tau': 'Taureau', 'Gem': 'Gémeaux', 'Can': 'Cancer',
        'Leo': 'Lion', 'Vir': 'Vierge', 'Lib': 'Balance', 'Sco': 'Scorpion',
        'Sag': 'Sagittaire', 'Cap': 'Capricorne', 'Aqu': 'Verseau', 'Pis': 'Poissons',
    }
    
    # Mapping signes → éléments (RapidAPI ne fournit pas l'élément)
    sign_to_element = {
        'Ari': 'Feu', 'Leo': 'Feu', 'Sag': 'Feu',
        'Tau': 'Terre', 'Vir': 'Terre', 'Cap': 'Terre',
        'Gem': 'Air', 'Lib': 'Air', 'Aqu': 'Air',
        'Can': 'Eau', 'Sco': 'Eau', 'Pis': 'Eau',
    }
    
    # Mapping planètes → emojis (RapidAPI ne fournit pas les emojis)
    planet_emojis = {
        'Sun': '☀️', 'Moon': '🌙', 'Mercury': '☿️', 'Venus': '♀️', 'Mars': '♂️',
        'Jupiter': '♃', 'Saturn': '♄', 'Uranus': '♅', 'Neptune': '♆', 'Pluto': '♇',
        'Ascendant': '⬆️', 'Medium_Coeli': '⬆️', 'Mean_Node': '☊', 'Chiron': '⚷',
    }
    
    # Gérer trois structures possibles:
    # 1. Enveloppe { success, data: { positions: [...] } } (endpoint /positions/enhanced)
    # 2. Direct { positions: [...] } (non utilisé)
    # 3. Chart data { chart_data: { positions: [...] } } (endpoint /charts/natal)
    
    positions_list = []
    
    if 'data' in positions_data and 'positions' in positions_data['data']:
        # Structure avec enveloppe (ancien endpoint /positions/enhanced)
        logger.info('[Parser] Détection structure avec enveloppe data')
        data_content = positions_data['data']
        positions_list = data_content['positions']
    elif 'chart_data' in positions_data:
        # Structure chart_data (endpoint /charts/natal)
        logger.info('[Parser] Détection structure chart_data (endpoint unique)')
        if 'positions' in positions_data['chart_data']:
            positions_list = positions_data['chart_data']['positions']
        else:
            logger.warning(f"[Parser] chart_data trouvé mais sans positions. Keys: {list(positions_data['chart_data'].keys())}")
            return core_points
    elif 'positions' in positions_data:
        # Structure directe
        logger.info('[Parser] Détection structure directe')
        positions_list = positions_data['positions']
    else:
        logger.warning(f'[Parser] Structure inconnue, keys: {list(positions_data.keys())}')
        return core_points
    
    logger.info(f'[Parser] ✅ {len(positions_list)} positions trouvées')
    
    # DEBUG: Afficher la structure du premier élément
    if positions_list and len(positions_list) > 0:
        logger.info(f'[Parser] 🔍 Premier élément: {positions_list[0]}')
    
    # Parser chaque position de l'array
    for pos in positions_list:
        if not pos or 'name' not in pos:
            continue
        
        point_name = pos.get('name', 'Unknown')
        logger.info(f'[Parser] ✅ Parsing {point_name} depuis array')
        
        # Extraire les données
        sign = pos.get('sign', 'Ari')
        house = pos.get('house', 1)
        
        # Calculer le degré depuis absolute_longitude (0-360°)
        # Le degré dans le signe = absolute_longitude % 30
        absolute_lon = pos.get('absolute_longitude', 0.0)
        degree_in_sign = round(absolute_lon % 30, 2)
        
        core_point = {
            'name': point_name,
            'sign': sign,
            'sign_fr': sign_mapping.get(sign, sign),
            'degree': degree_in_sign,
            'house': house,
            'is_retrograde': pos.get('is_retrograde', False),
            'emoji': planet_emojis.get(point_name, '⭐'),
            'element': sign_to_element.get(sign, 'Inconnu'),
            'interpretations': {
                'in_sign': pos.get('interpretation_in_sign', ''),
                'in_house': pos.get('interpretation_in_house', ''),
                'dignity': pos.get('dignity', ''),
            }
        }
        
        core_points.append(core_point)
    
    logger.info(f'[Parser] ✅ Parsé {len(core_points)} positions')
    return core_points


def parse_aspects(aspects_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Convertit les aspects depuis /api/v3/charts/natal
    Structure: aspects_data['chart_data']['aspects'] = [{point1, point2, aspect_type, orb}, ...]
    """
    aspects = []
    
    # Les aspects sont dans chart_data.aspects (endpoint /charts/natal)
    if 'chart_data' in aspects_data and 'aspects' in aspects_data['chart_data']:
        aspects_list = aspects_data['chart_data']['aspects']
    elif 'aspects' in aspects_data:
        # Fallback si structure directe
        aspects_list = aspects_data['aspects']
    else:
        aspects_list = []
    
    logger.info(f'[Parser] 🔍 Aspects trouvés: {len(aspects_list)}')
    
    # DEBUG: Afficher le premier aspect si présent
    if aspects_list and len(aspects_list) > 0:
        logger.info(f'[Parser] 🔍 Premier aspect: {aspects_list[0]}')
    
    for aspect in aspects_list:
        # Calculer la force de l'aspect basée sur l'orbe
        orb = abs(aspect.get('orb', 10))
        if orb < 1:
            strength = "strong"
        elif orb < 3:
            strength = "medium"
        else:
            strength = "weak"
        
        aspects.append({
            'from': aspect.get('point1'),
            'to': aspect.get('point2'),
            'aspect_type': aspect.get('aspect_type'),
            'orb': aspect.get('orb'),
            'strength': strength,
            'interpretation': aspect.get('interpretation', '')
        })
    
    return aspects


def parse_lunar_info(lunar_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convertit les métriques lunaires
    """
    if not lunar_data:
        return {
            'phase': 'Unknown',
            'phase_angle': None,
            'lunar_day': None,
            'emoji': '🌙',
            'mansion': None,
            'void_of_course': False,
            'interpretation': None
        }
    
    subject_data = lunar_data.get('subject_data', {})
    lunar_phase = subject_data.get('lunar_phase', {})
    
    return {
        'phase': lunar_phase.get('moon_phase_name', 'Unknown'),
        'phase_angle': lunar_phase.get('degrees_between_s_m'),
        'lunar_day': lunar_phase.get('moon_phase'),
        'emoji': lunar_phase.get('moon_emoji', '🌙'),
        'mansion': lunar_data.get('mansion'),
        'void_of_course': lunar_data.get('void_of_course', False),
        'interpretation': lunar_data.get('interpretation')
    }


def build_summary(positions: List[Dict], aspects: List[Dict]) -> Dict[str, Any]:
    """
    Construit un résumé du thème
    """
    if not positions:
        return {
            'big_three': {'sun': None, 'moon': None, 'ascendant': None},
            'personality_highlights': [],
            'dominant_element': None,
            'dominant_mode': None
        }
    
    # Extraire Big 3
    sun = next((p for p in positions if p.get('name') == 'Sun'), None)
    moon = next((p for p in positions if p.get('name') == 'Moon'), None)
    asc = next((p for p in positions if p.get('name') == 'Ascendant'), None)
    
    # Compter les éléments
    elements = {}
    for pos in positions:
        elem = pos.get('element', 'Inconnu')
        if elem and elem != 'Inconnu':
            elements[elem] = elements.get(elem, 0) + 1
    
    dominant_element = max(elements, key=elements.get) if elements else None
    
    # Highlights simples
    highlights = []
    if sun and sun.get('sign_fr'):
        interp = sun.get('interpretations', {}).get('in_sign', '') or ''
        if interp:
            highlights.append(f"Soleil en {sun['sign_fr']} - {interp[:50]}...")
        else:
            highlights.append(f"Soleil en {sun['sign_fr']}")
    
    if moon and moon.get('sign_fr'):
        interp = moon.get('interpretations', {}).get('in_sign', '') or ''
        if interp:
            highlights.append(f"Lune en {moon['sign_fr']} - {interp[:50]}...")
        else:
            highlights.append(f"Lune en {moon['sign_fr']}")
    
    return {
        'big_three': {
            'sun': sun,
            'moon': moon,
            'ascendant': asc
        },
        'personality_highlights': highlights,
        'dominant_element': dominant_element,
        'dominant_mode': None  # À calculer si besoin
    }


async def generate_natal_reading(
    birth_data: Dict[str, Any],
    options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Génère une lecture complète de thème natal
    Fait 3-4 appels API selon les options
    
    Returns:
        NatalReading complet
    """
    if options is None:
        options = {}
    
    language = options.get('language', 'fr')
    include_full_report = options.get('include_full_report', False)
    
    api_calls_count = 0
    
    logger.info(f"🌟 Génération lecture natal pour {birth_data.get('city')}")
    
    # Appel UNIQUE: /api/v3/charts/natal (contient positions + aspects + house_cusps)
    # Cet endpoint est plus simple et inclut les aspects (contrairement à /aspects/enhanced)
    logger.info("🌟 Utilisation de l'endpoint unique /api/v3/charts/natal")
    try:
        chart_data = await call_rapidapi_endpoint(
            "/api/v3/charts/natal",
            {
                "subject": {
                    "name": f"{birth_data.get('city', 'User')}",
                    "birth_data": birth_data
                },
                "options": {
                    "house_system": "P",  # Placidus
                    "aspect_types": ["major"],  # major aspects only
                    "orb_system": "standard"
                }
            }
        )
        api_calls_count += 1
        
        # Les positions et aspects sont dans la même réponse
        positions_data = chart_data
        aspects_data = chart_data
        
        # DEBUG: Logger le nombre d'aspects trouvés
        if chart_data and 'chart_data' in chart_data and 'aspects' in chart_data['chart_data']:
            logger.info(f"✅ Endpoint unique retourne {len(chart_data['chart_data']['aspects'])} aspects")
        elif chart_data and 'aspects' in chart_data:
            logger.info(f"✅ Endpoint unique retourne {len(chart_data['aspects'])} aspects")
        else:
            logger.warning(f"⚠️ Aucun aspect trouvé dans la réponse de /charts/natal")
            
    except Exception as e:
        logger.error(f"❌ Erreur endpoint /charts/natal: {e}")
        raise
    
    # Appel 3: Métriques lunaires (fallback: utiliser positions_data)
    try:
        lunar_data = await get_lunar_metrics(birth_data, language)
        api_calls_count += 1
    except Exception as e:
        logger.warning(f"⚠️ Métriques lunaires non disponibles (endpoint n'existe pas), utilisation fallback: {e}")
        # Utiliser les données lunaires du premier appel (déjà présentes)
        lunar_data = positions_data
    
    # Appel 4 (optionnel): Rapport complet
    full_report_text = None
    if include_full_report:
        try:
            report_data = await get_natal_report(birth_data, language)
            full_report_text = report_data.get('report_text') or report_data.get('interpretation')
            api_calls_count += 1
        except Exception as e:
            logger.warning(f"Erreur rapport complet (non bloquant): {e}")
    
    # Parser les données depuis la réponse unique
    logger.info(f"📊 Parsing chart_data (keys: {list(chart_data.keys())[:7]})")
    positions = parse_positions_to_core_points(positions_data)
    logger.info(f"📊 Positions parsées: {len(positions)} points")
    
    aspects = parse_aspects(aspects_data)
    logger.info(f"📊 Aspects parsés: {len(aspects)} aspects")
    
    lunar = parse_lunar_info(lunar_data)
    summary = build_summary(positions, aspects)
    logger.info(f"📊 Summary big_three: sun={summary['big_three']['sun'] is not None}, moon={summary['big_three']['moon'] is not None}")
    
    reading = {
        'positions': positions,
        'aspects': aspects,
        'lunar': lunar,
        'summary': summary,
        'full_report_text': full_report_text,
    }
    
    logger.info(f"✅ Lecture générée avec {api_calls_count} appel(s) API")
    
    return {
        'reading': reading,
        'api_calls_count': api_calls_count,
        'source': 'api'
    }


async def close_client():
    """Ferme le client HTTP"""
    await client.aclose()

