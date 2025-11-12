"""
Service de lecture de thème natal - VERSION PROPRE
Utilise UNIQUEMENT l'endpoint /api/v3/charts/natal
"""

import httpx
import hashlib
import logging
from typing import Dict, Any, List

from config import settings

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


async def call_rapidapi_natal_chart(birth_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Appelle l'endpoint unique /api/v3/charts/natal
    Retourne: { "subject_data": {...}, "chart_data": {...} }
    """
    url = f"{settings.BASE_RAPID_URL}/api/v3/charts/natal"
    
    payload = {
        "subject": {
            "name": birth_data.get('city', 'User'),
            "birth_data": birth_data
        },
        "options": {
            "house_system": "P",  # Placidus
            "aspect_types": ["major"],  # Major aspects only
            "orb_system": "standard"
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }
    
    logger.info(f"🌐 Appel RapidAPI: /api/v3/charts/natal pour {birth_data.get('city')}")
    
    try:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Logger les stats de la réponse
        if 'chart_data' in data:
            num_positions = len(data.get('chart_data', {}).get('planetary_positions', []))
            num_aspects = len(data.get('chart_data', {}).get('aspects', []))
            logger.info(f"✅ Réponse RapidAPI reçue: {num_positions} positions, {num_aspects} aspects")
        else:
            logger.warning(f"⚠️ Pas de 'chart_data' dans la réponse ! Keys: {list(data.keys())}")
        
        return data
        
    except httpx.HTTPStatusError as e:
        logger.error(f"❌ Erreur HTTP RapidAPI: {e.response.status_code} - {e.response.text}")
        raise
    except Exception as e:
        logger.error(f"❌ Erreur RapidAPI: {str(e)}")
        raise


def parse_positions_from_natal_chart(chart_response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Parse les positions depuis la réponse de /api/v3/charts/natal
    
    Structure attendue:
    {
      "chart_data": {
        "planetary_positions": [  ← NOM CORRECT !
          {
            "name": "Sun",
            "sign": "Sco",
            "degree": 0.0,  # Souvent à 0
            "absolute_longitude": 219.27,  # La vraie valeur
            "house": 9,
            "is_retrograde": false
          }
        ]
      }
    }
    """
    chart_data = chart_response.get("chart_data", {})
    positions_list = chart_data.get("planetary_positions", [])
    
    if not positions_list:
        logger.warning("[Parser] Aucune position trouvée dans chart_data.planetary_positions")
        return []
    
    # Mappings signes → français et éléments
    sign_mapping = {
        'Ari': 'Bélier', 'Tau': 'Taureau', 'Gem': 'Gémeaux', 'Can': 'Cancer',
        'Leo': 'Lion', 'Vir': 'Vierge', 'Lib': 'Balance', 'Sco': 'Scorpion',
        'Sag': 'Sagittaire', 'Cap': 'Capricorne', 'Aqu': 'Verseau', 'Pis': 'Poissons',
    }
    
    sign_to_element = {
        'Ari': 'Feu', 'Leo': 'Feu', 'Sag': 'Feu',
        'Tau': 'Terre', 'Vir': 'Terre', 'Cap': 'Terre',
        'Gem': 'Air', 'Lib': 'Air', 'Aqu': 'Air',
        'Can': 'Eau', 'Sco': 'Eau', 'Pis': 'Eau',
    }
    
    planet_emojis = {
        'Sun': '☀️', 'Moon': '🌙', 'Mercury': '☿️', 'Venus': '♀️', 'Mars': '♂️',
        'Jupiter': '♃', 'Saturn': '♄', 'Uranus': '♅', 'Neptune': '♆', 'Pluto': '♇',
        'Ascendant': '⬆️', 'Medium_Coeli': '🔺', 'Mean_Node': '☊', 'Chiron': '⚷',
    }
    
    parsed_positions = []
    
    for pos in positions_list:
        if not pos or 'name' not in pos:
            continue
        
        name = pos.get('name', 'Unknown')
        sign = pos.get('sign', 'Ari')
        house = pos.get('house', 0)
        
        # RapidAPI met souvent degree à 0 → utiliser absolute_longitude
        raw_degree = pos.get('degree')
        abs_long = pos.get('absolute_longitude')
        
        if isinstance(raw_degree, (int, float)) and raw_degree != 0:
            degree_in_sign = float(raw_degree)
        elif isinstance(abs_long, (int, float)):
            degree_in_sign = float(abs_long) % 30
        else:
            degree_in_sign = 0.0
        
        parsed_positions.append({
            'name': name,
            'sign': sign,
            'sign_fr': sign_mapping.get(sign, sign),
            'degree': round(degree_in_sign, 2),
            'house': house,
            'is_retrograde': bool(pos.get('is_retrograde', False)),
            'emoji': planet_emojis.get(name, '⭐'),
            'element': sign_to_element.get(sign, 'Inconnu'),
            'interpretations': {
                'in_sign': '',
                'in_house': '',
                'dignity': '',
            }
        })
    
    logger.info(f"[Parser] ✅ {len(parsed_positions)} positions parsées depuis chart_data.planetary_positions")
    return parsed_positions


def parse_aspects_from_natal_chart(chart_response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Parse les aspects depuis la réponse de /api/v3/charts/natal
    
    Structure attendue:
    {
      "chart_data": {
        "aspects": [
          {
            "point1": "Sun",
            "point2": "Moon",
            "aspect_type": "opposition",
            "orb": 2.38
          }
        ]
      }
    }
    """
    chart_data = chart_response.get("chart_data", {})
    aspects_list = chart_data.get("aspects", [])
    
    if not aspects_list:
        logger.warning("[Parser] Aucun aspect trouvé dans chart_data.aspects")
        return []
    
    parsed_aspects = []
    
    for asp in aspects_list:
        p1 = asp.get("point1")
        p2 = asp.get("point2")
        aspect_type = asp.get("aspect_type")
        orb = asp.get("orb")
        
        if not (p1 and p2 and aspect_type):
            continue
        
        # Calculer la force basée sur l'orbe
        strength = "medium"
        if isinstance(orb, (int, float)):
            abs_orb = abs(float(orb))
            if abs_orb < 1.5:
                strength = "strong"
            elif abs_orb > 5:
                strength = "weak"
        
        parsed_aspects.append({
            'from': p1,
            'to': p2,
            'aspect_type': aspect_type,
            'orb': float(orb) if isinstance(orb, (int, float)) else 0.0,
            'strength': strength,
            'interpretation': ''
        })
    
    logger.info(f"[Parser] ✅ {len(parsed_aspects)} aspects parsés depuis chart_data.aspects")
    return parsed_aspects


def build_summary(positions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Construit un résumé du thème"""
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
    
    # Calculer élément dominant
    element_counts = {}
    for p in positions:
        elem = p.get('element')
        if elem and elem != 'Inconnu':
            element_counts[elem] = element_counts.get(elem, 0) + 1
    
    dominant_element = max(element_counts, key=element_counts.get) if element_counts else None
    
    # Highlights
    highlights = []
    if sun:
        highlights.append(f"Soleil en {sun['sign_fr']}")
    if moon:
        highlights.append(f"Lune en {moon['sign_fr']}")
    
    return {
        'big_three': {
            'sun': sun,
            'moon': moon,
            'ascendant': asc
        },
        'personality_highlights': highlights,
        'dominant_element': dominant_element,
        'dominant_mode': None
    }


async def generate_natal_reading(
    birth_data: Dict[str, Any],
    options: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Génère une lecture complète de thème natal
    Utilise UNIQUEMENT /api/v3/charts/natal (1 seul appel API)
    
    Returns:
        {
            'reading': { positions, aspects, lunar, summary, full_report_text },
            'api_calls_count': 1
        }
    """
    options = options or {}
    logger.info(f"🌟 Génération lecture natal pour {birth_data.get('city')}")
    
    # Appel unique à /charts/natal
    chart_response = await call_rapidapi_natal_chart(birth_data)
    
    # Parser positions et aspects
    positions = parse_positions_from_natal_chart(chart_response)
    aspects = parse_aspects_from_natal_chart(chart_response)
    
    # Construire le résumé
    summary = build_summary(positions)
    
    # Informations lunaires basiques (du subject_data si disponible)
    subject_data = chart_response.get("subject_data", {})
    lunar = {
        'phase': 'Unknown',
        'phase_angle': None,
        'lunar_day': None,
        'mansion': None,
        'void_of_course': False,
        'interpretation': None,
        'emoji': '🌙'
    }
    
    reading = {
        'positions': positions,
        'aspects': aspects,
        'lunar': lunar,
        'summary': summary,
        'full_report_text': None
    }
    
    logger.info(f"✅ Lecture générée: {len(positions)} positions, {len(aspects)} aspects (1 appel API)")
    
    return {
        'reading': reading,
        'api_calls_count': 1
    }


async def close_client():
    """Ferme le client HTTP (à appeler au shutdown)"""
    await client.aclose()

