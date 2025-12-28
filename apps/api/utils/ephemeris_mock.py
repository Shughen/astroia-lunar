"""
Mock DEV pour générer des données astrologiques minimales
Utilisé quand EPHEMERIS_API_KEY n'est pas configurée et DEV_MOCK_EPHEMERIS=True
"""

from typing import Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


# Mapping simple : mois de naissance → signe solaire (approximatif)
_MONTH_TO_SUN_SIGN = {
    1: "Capricorn", 2: "Aquarius", 3: "Pisces", 4: "Aries",
    5: "Taurus", 6: "Gemini", 7: "Cancer", 8: "Leo",
    9: "Virgo", 10: "Libra", 11: "Scorpio", 12: "Sagittarius"
}

# Signes lunaires (rotation simple basée sur le jour)
_MOON_SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
               "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

# Ascendants possibles
_ASCENDANT_SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]


def generate_mock_natal_chart(
    date: str,  # YYYY-MM-DD
    time: str,  # HH:MM
    latitude: float,
    longitude: float,
    timezone: str = "Europe/Paris"
) -> Dict[str, Any]:
    """
    Génère un thème natal mock minimal pour le mode DEV
    
    Args:
        date: Date de naissance YYYY-MM-DD
        time: Heure de naissance HH:MM
        latitude: Latitude du lieu de naissance
        longitude: Longitude du lieu de naissance
        timezone: Fuseau horaire
        
    Returns:
        Structure similaire à l'API Ephemeris avec données minimales
    """
    logger.warning(f"🎭 MODE MOCK DEV - Génération données fake pour date={date} {time}")
    
    # Parser la date
    year, month, day = map(int, date.split("-"))
    
    # Parser l'heure (supporte HH:MM et HH:MM:SS)
    try:
        # Utiliser datetime.time.fromisoformat pour gérer les deux formats
        from datetime import time as dt_time
        time_obj = dt_time.fromisoformat(time)
        hour = time_obj.hour
        minute = time_obj.minute
    except (ValueError, AttributeError):
        # Fallback : parser manuellement HH:MM
        time_parts = time.split(":")
        hour = int(time_parts[0])
        minute = int(time_parts[1]) if len(time_parts) > 1 else 0
    
    # Calculer signe solaire (basé sur le mois, approximatif)
    sun_sign = _MONTH_TO_SUN_SIGN.get(month, "Aries")
    sun_degree = float((day * 30 / 31) % 30)  # Degré approximatif dans le signe
    sun_longitude = (month - 1) * 30 + sun_degree  # Longitude zodiacale approximative
    
    # Calculer signe lunaire (basé sur le jour, rotation simple)
    moon_sign_index = (day - 1) % len(_MOON_SIGNS)
    moon_sign = _MOON_SIGNS[moon_sign_index]
    moon_degree = float((hour * 30 / 24) % 30)
    moon_longitude = (moon_sign_index * 30) + moon_degree
    
    # Calculer ascendant (basé sur l'heure, rotation simple)
    ascendant_sign_index = hour % len(_ASCENDANT_SIGNS)
    ascendant_sign = _ASCENDANT_SIGNS[ascendant_sign_index]
    ascendant_degree = float((minute * 30 / 60) % 30)
    
    # Maison de la Lune (approximatif : 1-12)
    moon_house = (hour % 12) + 1
    
    return {
        "sun": {
            "sign": sun_sign,
            "degree": round(sun_degree, 2),
            "absolute_longitude": round(sun_longitude, 2),
            "house": 1  # Maison approximative
        },
        "moon": {
            "sign": moon_sign,
            "degree": round(moon_degree, 2),
            "absolute_longitude": round(moon_longitude, 2),
            "house": moon_house
        },
        "ascendant": {
            "sign": ascendant_sign,
            "degree": round(ascendant_degree, 2)
        },
        "planets": {
            "Sun": {"sign": sun_sign, "degree": round(sun_degree, 2)},
            "Moon": {"sign": moon_sign, "degree": round(moon_degree, 2)},
            "Mercury": {"sign": sun_sign, "degree": round(sun_degree + 5, 2)},
            "Venus": {"sign": sun_sign, "degree": round(sun_degree + 10, 2)},
            "Mars": {"sign": sun_sign, "degree": round(sun_degree + 15, 2)},
        },
        "houses": {
            "1": {"sign": ascendant_sign, "degree": round(ascendant_degree, 2)},
            "2": {"sign": _ASCENDANT_SIGNS[(ascendant_sign_index + 1) % 12], "degree": 0},
            "3": {"sign": _ASCENDANT_SIGNS[(ascendant_sign_index + 2) % 12], "degree": 0},
        },
        "aspects": [
            {
                "from_planet": "Sun",
                "to_planet": "Moon",
                "aspect_type": "trine",
                "orb": round(abs(sun_longitude - moon_longitude) % 120, 2)
            }
        ]
    }


def generate_mock_lunar_return(
    natal_moon_degree: float,
    natal_moon_sign: str,
    target_month: str,  # YYYY-MM
    birth_latitude: float,
    birth_longitude: float,
    timezone: str = "Europe/Paris"
) -> Dict[str, Any]:
    """
    Génère une révolution lunaire mock minimal pour le mode DEV
    
    Args:
        natal_moon_degree: Degré natale de la Lune
        natal_moon_sign: Signe natale de la Lune
        target_month: Mois cible YYYY-MM
        birth_latitude: Latitude du lieu de naissance
        birth_longitude: Longitude du lieu de naissance
        timezone: Fuseau horaire
        
    Returns:
        Structure similaire à l'API Ephemeris avec données minimales
    """
    logger.warning(f"🎭 MODE MOCK DEV - Génération révolution lunaire fake pour {target_month}")
    
    # Date estimée (15 du mois)
    year, month = map(int, target_month.split("-"))
    return_datetime = f"{target_month}-15T12:00:00"
    
    # Ascendant approximatif (basé sur le mois)
    ascendant_sign_index = month % len(_ASCENDANT_SIGNS)
    ascendant_sign = _ASCENDANT_SIGNS[ascendant_sign_index]
    
    # Maison de la Lune (1-12)
    moon_house = (month % 12) + 1
    
    return {
        "return_datetime": return_datetime,
        "ascendant": {
            "sign": ascendant_sign,
            "degree": 10.5
        },
        "moon": {
            "sign": natal_moon_sign,  # Même signe que natal
            "degree": natal_moon_degree,  # Même degré que natal
            "house": moon_house
        },
        "planets": {
            "Moon": {"sign": natal_moon_sign, "degree": natal_moon_degree},
        },
        "houses": {
            "1": {"sign": ascendant_sign, "degree": 10.5},
        },
        "aspects": [
            {
                "from_planet": "Moon",
                "to_planet": "Sun",
                "aspect_type": "trine",
                "orb": 2.5
            }
        ]
    }

