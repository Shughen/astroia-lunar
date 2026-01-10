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
# Constantes Swiss Ephemeris
PLANET_CODES = {
    "uranus": swe.URANUS if SWISS_EPHEMERIS_AVAILABLE else None,
    "neptune": swe.NEPTUNE if SWISS_EPHEMERIS_AVAILABLE else None,
    "pluto": swe.PLUTO if SWISS_EPHEMERIS_AVAILABLE else None,
    "mean_node": swe.MEAN_NODE if SWISS_EPHEMERIS_AVAILABLE else None,  # Nœud Nord moyen
    "true_node": swe.TRUE_NODE if SWISS_EPHEMERIS_AVAILABLE else None,  # Nœud Nord vrai
    "south_node": None,  # Calculé comme opposé du Nœud Nord
    "chiron": swe.CHIRON if SWISS_EPHEMERIS_AVAILABLE else None,
    # Lilith n'a pas de constante directe, on la calculera depuis l'apogée lunaire
    "lilith": None,  # Sera calculé séparément
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


def calculate_house_from_longitude(
    planet_longitude: float,
    house_cusps: List[float]
) -> int:
    """
    Détermine dans quelle maison (1-12) se trouve une planète selon sa longitude écliptique
    
    Args:
        planet_longitude: Longitude écliptique de la planète (0-360)
        house_cusps: Liste des 12 cuspides des maisons (longitudes absolues)
        
    Returns:
        Numéro de la maison (1-12)
    """
    if not house_cusps or len(house_cusps) < 12:
        return 0
    
    # Normaliser toutes les longitudes à [0, 360)
    planet_longitude = planet_longitude % 360
    normalized_cusps = [c % 360 for c in house_cusps[:12]]
    
    # Trouver la maison : la planète est dans la maison dont la cuspide est juste avant sa longitude
    for i in range(12):
        cusp_current = normalized_cusps[i]
        cusp_next = normalized_cusps[(i + 1) % 12]
        
        # Gérer le cas où on traverse le 0° (Bélier)
        if cusp_next < cusp_current:
            # On traverse le 0° (ex: Maison 7 à 330°, Maison 8 à 0°)
            if planet_longitude >= cusp_current or planet_longitude < cusp_next:
                return i + 1
        else:
            # Cas normal (cuspides dans l'ordre croissant)
            if cusp_current <= planet_longitude < cusp_next:
                return i + 1
    
    # Si aucune maison trouvée (ne devrait pas arriver), retourner la maison 1
    return 1


def calculate_complementary_positions(
    birth_datetime: datetime,
    latitude: float,
    longitude: float,
    house_cusps: Optional[List[float]] = None
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
            
            # Calculer la maison si les cuspides sont disponibles
            house = 0
            if house_cusps:
                house = calculate_house_from_longitude(zodiac["longitude"], house_cusps)
            
            positions.append({
                "name": name,
                "sign": zodiac["sign"],
                "sign_abbr": zodiac["sign_abbr"],
                "degree": zodiac["degree"],
                "longitude": zodiac["longitude"],
                "house": house,
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
        # Calculer la maison pour le Nœud Sud
        house = 0
        if house_cusps:
            house = calculate_house_from_longitude(zodiac["longitude"], house_cusps)
        
        positions.append({
            "name": "south_node",
            "sign": zodiac["sign"],
            "sign_abbr": zodiac["sign_abbr"],
            "degree": zodiac["degree"],
            "longitude": zodiac["longitude"],
            "house": house,
            "is_retrograde": False
        })
    
    # Calculer Lilith (Lune Noire) = Apogée moyenne de la Lune
    try:
        result = swe.calc_ut(jd, swe.MEAN_APOG, swe.FLG_SWIEPH)
        if result is not None and len(result) >= 2:
            lilith_longitude = result[0][0]
            zodiac = longitude_to_zodiac(lilith_longitude)
            
            # Calculer la maison pour Lilith
            house = 0
            if house_cusps:
                house = calculate_house_from_longitude(zodiac["longitude"], house_cusps)
            
            positions.append({
                "name": "lilith",
                "sign": zodiac["sign"],
                "sign_abbr": zodiac["sign_abbr"],
                "degree": zodiac["degree"],
                "longitude": zodiac["longitude"],
                "house": house,
                "is_retrograde": False
            })
    except Exception as e:
        logger.warning(f"⚠️ Erreur calcul Lilith: {e}")
    
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
    
    # Éviter les doublons mean_node/true_node (garder seulement mean_node)
    has_north_node = any(
        pos.get("name", "").lower() in ["mean_node", "true_node", "nœud nord", "north_node"]
        for pos in merged
    )
    
    for comp_pos in complementary_positions:
        name_lower = comp_pos.get("name", "").lower()
        
        # Si c'est un nœud et qu'on en a déjà un, skip
        if name_lower in ["mean_node", "true_node"] and has_north_node:
            continue
        
        if name_lower not in rapidapi_dict:
                # Convertir au format RapidAPI avec noms traduits pour affichage
                name = comp_pos["name"]
                # Traduire les noms pour affichage
                if name == "mean_node" or name == "true_node":
                    display_name = "Nœud Nord"  # Unifier mean_node et true_node en "Nœud Nord"
                elif name == "south_node":
                    display_name = "Nœud Sud"
                else:
                    display_name = name  # Garder le nom original pour les autres
                
                merged.append({
                    "name": display_name,  # Nom traduit pour affichage
                    "sign": comp_pos["sign_abbr"],  # Format abrégé comme RapidAPI
                    "degree": comp_pos["degree"],
                    "absolute_longitude": comp_pos["longitude"],
                    "house": comp_pos.get("house", 0),
                    "is_retrograde": comp_pos.get("is_retrograde", False)
                })
    
    return merged

