"""
Service complémentaire pour calculer les planètes/points manquants dans le thème natal
Utilise Swiss Ephemeris pour calculer Uranus, Neptune, Pluton, Nœuds, Lilith, Chiron

Ces éléments ne sont pas retournés par RapidAPI par défaut, donc on les calcule séparément.
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)

# Vérifier si Swiss Ephemeris est disponible
try:
    import swisseph as swe
    SWISS_EPHEMERIS_AVAILABLE = True
except ImportError:
    SWISS_EPHEMERIS_AVAILABLE = False
    swe = None
    logger.warning("⚠️ Swiss Ephemeris non disponible - calculs complémentaires désactivés")

# Constantes Swiss Ephemeris pour les planètes/points
# Constantes Swiss Ephemeris (sans préfixe SE_)
PLANET_CODES = {
    "uranus": swe.URANUS if SWISS_EPHEMERIS_AVAILABLE else None,
    "neptune": swe.NEPTUNE if SWISS_EPHEMERIS_AVAILABLE else None,
    "pluto": swe.PLUTO if SWISS_EPHEMERIS_AVAILABLE else None,
    "mean_node": swe.TRUE_NODE if SWISS_EPHEMERIS_AVAILABLE else None,  # Nœud Nord moyen
    "true_node": swe.TRUE_NODE if SWISS_EPHEMERIS_AVAILABLE else None,  # Nœud Nord vrai
    "south_node": None,  # Calculé comme opposé du Nœud Nord
    "chiron": swe.CHIRON if SWISS_EPHEMERIS_AVAILABLE else None,
    "lilith": swe.TRUE_LILITH if SWISS_EPHEMERIS_AVAILABLE else None,  # Lilith vraie (Lune Noire)
}

ZODIAC_SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

SIGN_ABBREVIATIONS = {
    'Aries': 'Ari', 'Taurus': 'Tau', 'Gemini': 'Gem', 'Cancer': 'Can',
    'Leo': 'Leo', 'Virgo': 'Vir', 'Libra': 'Lib', 'Scorpio': 'Sco',
    'Sagittarius': 'Sag', 'Capricorn': 'Cap', 'Aquarius': 'Aqu', 'Pisces': 'Pis'
}


def longitude_to_zodiac(longitude: float) -> Dict[str, Any]:
    """
    Convertit une longitude écliptique (0-360°) en signe et degré
    
    Args:
        longitude: Longitude écliptique en degrés (0-360)
        
    Returns:
        {
            "sign": "Aries",
            "sign_abbr": "Ari",
            "degree": 15.5,  # Degré dans le signe (0-30)
            "longitude": 45.5  # Longitude absolue
        }
    """
    # Normaliser à [0, 360)
    longitude = longitude % 360
    
    sign_index = int(longitude // 30)
    degree_in_sign = longitude % 30
    
    sign = ZODIAC_SIGNS[sign_index]
    sign_abbr = SIGN_ABBREVIATIONS[sign]
    
    return {
        "sign": sign,
        "sign_abbr": sign_abbr,
        "degree": round(degree_in_sign, 2),
        "longitude": round(longitude, 2)
    }


def calculate_complementary_positions(
    birth_datetime: datetime,
    latitude: float,
    longitude: float
) -> List[Dict[str, Any]]:
    """
    Calcule les positions complémentaires manquantes (Uranus, Neptune, Pluton, Nœuds, Lilith, Chiron)
    
    Args:
        birth_datetime: Date et heure de naissance (datetime object, UTC)
        latitude: Latitude de naissance
        longitude: Longitude de naissance
        
    Returns:
        Liste de positions au format:
        [
            {
                "name": "uranus",
                "sign": "Aries",
                "sign_abbr": "Ari",
                "degree": 15.5,
                "house": 1,  # Calculé si possible
                "is_retrograde": False
            },
            ...
        ]
    """
    if not SWISS_EPHEMERIS_AVAILABLE:
        logger.warning("⚠️ Swiss Ephemeris non disponible - positions complémentaires non calculées")
        return []
    
    # Convertir datetime en Julian Day
    year = birth_datetime.year
    month = birth_datetime.month
    day = birth_datetime.day
    hour = birth_datetime.hour + birth_datetime.minute / 60.0 + birth_datetime.second / 3600.0
    
    jd = swe.julday(year, month, day, hour, swe.GREG_CAL)
    
    positions = []
    
    # Calculer chaque planète/point
    for name, planet_code in PLANET_CODES.items():
        if planet_code is None:
            # Nœud Sud : opposé du Nœud Nord (sera calculé après)
            continue
        
        try:
            # Calculer la position (même API que dans swiss_ephemeris.py)
            result = swe.calc_ut(jd, planet_code, swe.FLG_SWIEPH)
            if result is None or len(result) < 2:
                logger.warning(f"⚠️ Impossible de calculer {name}")
                continue
            
            # result[0] = [longitude, latitude, distance, speed_long, speed_lat, speed_dist]
            longitude = result[0][0]
            speed_long = result[0][3] if len(result[0]) > 3 else 0
            
            # Convertir en signe et degré
            zodiac = longitude_to_zodiac(longitude)
            
            # Détecter rétrogradation (vitesse négative)
            is_retrograde = speed_long < 0
            
            positions.append({
                "name": name,
                "sign": zodiac["sign"],
                "sign_abbr": zodiac["sign_abbr"],
                "degree": zodiac["degree"],
                "longitude": zodiac["longitude"],
                "house": 0,  # À calculer avec le système de maisons si nécessaire
                "is_retrograde": is_retrograde
            })
            
        except Exception as e:
            logger.warning(f"⚠️ Erreur calcul {name}: {e}")
            continue
    
    # Calculer le Nœud Sud (opposé du Nœud Nord)
    north_node = next((p for p in positions if p["name"] == "mean_node"), None)
    if north_node:
        south_longitude = (north_node["longitude"] + 180) % 360
        zodiac = longitude_to_zodiac(south_longitude)
        positions.append({
            "name": "south_node",
            "sign": zodiac["sign"],
            "sign_abbr": zodiac["sign_abbr"],
            "degree": zodiac["degree"],
            "longitude": zodiac["longitude"],
            "house": 0,  # À calculer séparément si nécessaire
            "is_retrograde": False
        })
    
    logger.info(f"✅ {len(positions)} positions complémentaires calculées")
    return positions


def merge_complementary_positions(
    rapidapi_positions: List[Dict[str, Any]],
    complementary_positions: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Fusionne les positions RapidAPI avec les positions complémentaires calculées
    
    Args:
        rapidapi_positions: Positions retournées par RapidAPI
        complementary_positions: Positions calculées avec Swiss Ephemeris
        
    Returns:
        Liste fusionnée de toutes les positions
    """
    # Créer un dict pour lookup rapide
    rapidapi_dict = {pos.get("name", "").lower(): pos for pos in rapidapi_positions}
    
    # Ajouter les positions complémentaires qui ne sont pas déjà présentes
    merged = list(rapidapi_positions)
    
    for comp_pos in complementary_positions:
        name_lower = comp_pos.get("name", "").lower()
        if name_lower not in rapidapi_dict:
            # Convertir au format RapidAPI
            merged.append({
                "name": comp_pos["name"].title(),  # "uranus" -> "Uranus"
                "sign": comp_pos["sign_abbr"],  # Format abrégé comme RapidAPI
                "degree": comp_pos["degree"],
                "absolute_longitude": comp_pos["longitude"],
                "house": comp_pos.get("house", 0),
                "is_retrograde": comp_pos.get("is_retrograde", False)
            })
    
    return merged

