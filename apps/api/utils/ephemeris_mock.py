"""
Mock DEV pour générer des données astrologiques minimales
Utilisé quand EPHEMERIS_API_KEY n'est pas configurée et DEV_MOCK_EPHEMERIS=True
"""

from typing import Dict, Any
from datetime import datetime, timedelta
from datetime import timezone as dt_timezone
import logging

logger = logging.getLogger(__name__)

# Import Swiss Ephemeris pour le calcul réel des Lunar Returns
try:
    from services.swiss_ephemeris import (
        find_lunar_return,
        get_moon_position,
        get_sun_position,
        datetime_to_julian_day,
        get_moon_longitude,
        get_sun_longitude,
        degree_to_sign,
        SWISS_EPHEMERIS_AVAILABLE as SWE_AVAILABLE
    )
    SWISS_EPHEMERIS_AVAILABLE = SWE_AVAILABLE
except (ImportError, AttributeError):
    SWISS_EPHEMERIS_AVAILABLE = False
    logger.warning("⚠️ Swiss Ephemeris non disponible - utilisation du placeholder")


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
    
    Si Swiss Ephemeris est disponible, calcule le vrai Lunar Return.
    Sinon, utilise un placeholder (15 du mois à 12:00).
    
    Args:
        natal_moon_degree: Degré natale de la Lune (dans le signe, 0-30)
        natal_moon_sign: Signe natale de la Lune
        target_month: Mois cible YYYY-MM
        birth_latitude: Latitude du lieu de naissance
        birth_longitude: Longitude du lieu de naissance
        timezone: Fuseau horaire
        
    Returns:
        Structure similaire à l'API Ephemeris avec données minimales
    """
    year, month = map(int, target_month.split("-"))
    
    # Calculer la longitude écliptique natale complète (0-360°)
    # Si natal_moon_degree est déjà une longitude absolue (> 30), l'utiliser directement
    # Sinon, calculer depuis le signe et le degré dans le signe
    if natal_moon_degree is not None and natal_moon_degree > 30:
        # C'est déjà une longitude absolue
        natal_moon_longitude = natal_moon_degree % 360
        logger.debug(f"Utilisation longitude absolue: {natal_moon_longitude:.2f}°")
    else:
        # Calculer depuis signe + degré dans le signe
        sign_index = _MOON_SIGNS.index(natal_moon_sign) if natal_moon_sign in _MOON_SIGNS else 0
        natal_moon_longitude = (sign_index * 30) + (natal_moon_degree or 0)
        logger.debug(
            f"Calcul longitude depuis signe: {natal_moon_sign} ({sign_index}) + "
            f"degre={natal_moon_degree} = {natal_moon_longitude:.2f}°"
        )
    
    # Date de départ pour la recherche (milieu du mois)
    search_start = datetime(year, month, 15, 12, 0, 0, tzinfo=dt_timezone.utc)
    
    if SWISS_EPHEMERIS_AVAILABLE:
        # Calcul réel du Lunar Return
        logger.info(
            f"🎭 MODE MOCK DEV - Calcul réel Lunar Return pour {target_month} "
            f"(λ_natal={natal_moon_longitude:.2f}°)"
        )
        
        return_dt = find_lunar_return(
            natal_moon_longitude=natal_moon_longitude,
            start_dt=search_start,
            search_window_hours=48,
            tolerance_seconds=60
        )
        
        if return_dt is None:
            # Fallback si la recherche échoue
            logger.warning(
                f"⚠️ Calcul Lunar Return échoué pour {target_month}, "
                f"utilisation du placeholder"
            )
            return_dt = search_start
        else:
            logger.info(
                f"✅ Lunar Return calculé: {return_dt.isoformat()}"
            )
        
        # Calculer les positions à ce moment
        moon_pos = get_moon_position(return_dt)
        sun_pos = get_sun_position(return_dt)
        
        # Ascendant approximatif (basé sur l'heure)
        ascendant_sign_index = return_dt.hour % len(_ASCENDANT_SIGNS)
        ascendant_sign = _ASCENDANT_SIGNS[ascendant_sign_index]
        
        # Maison de la Lune (1-12, approximatif basé sur l'heure)
        moon_house = (return_dt.hour % 12) + 1
        
        return_datetime_str = return_dt.isoformat()
        
    else:
        # Fallback: placeholder amélioré (approximation réaliste sans Swiss Ephemeris)
        logger.warning(
            f"🎭 MODE MOCK DEV - Placeholder amélioré (Swiss Ephemeris non disponible) "
            f"pour {target_month}"
        )
        
        # Approximation réaliste : utiliser le mois sidéral (~27.32 jours) pour varier les dates
        # Calculer un offset basé sur le numéro du mois depuis janvier pour créer de la variété
        # On veut que les dates varient entre le 10 et le 20 du mois, avec des heures variées
        month_offset = (year - 2025) * 12 + (month - 1)  # Numéro de mois depuis janvier 2025
        lunar_cycle_offset = month_offset * 27.321582  # Mois sidéral en jours
        
        # Calculer le jour du mois (entre 10 et 20) basé sur l'offset
        # Utiliser plusieurs facteurs pour éviter les répétitions et le 15 fixe
        # Variation principale basée sur le cycle lunaire
        cycle_day = int((lunar_cycle_offset % 27.32) / 27.32 * 11)  # 0-10
        # Variation secondaire basée sur le mois
        month_day = (month * 13) % 11  # 0-10, utilise nombre premier pour plus de variation
        # Variation tertiaire basée sur l'année
        year_day = (year * 7) % 11  # 0-10
        
        # Combiner les variations pour éviter les répétitions
        combined_offset = (cycle_day + month_day + year_day) % 11  # 0-10
        calculated_day = 10 + combined_offset  # Entre 10 et 20
        
        # S'assurer qu'on n'a jamais exactement 15 (trop proche de l'ancien placeholder)
        if calculated_day == 15:
            calculated_day = 14 if (month % 2 == 0) else 16
        
        # Calculer l'heure (entre 8h et 20h) basée sur l'offset
        # Utiliser plusieurs facteurs pour plus de variation
        hour_base = int((lunar_cycle_offset * 3) % 12)  # 0-11
        hour_month = (month * 5) % 12  # Variation basée sur le mois
        hour_variation = (hour_base + hour_month) % 12
        calculated_hour = 8 + hour_variation  # Entre 8h et 19h
        
        # Calculer les minutes (0, 15, 30, 45) pour plus de réalisme
        minute_variation = int((lunar_cycle_offset * 4 + month * 3) % 4) * 15  # 0, 15, 30, 45
        
        return_dt = datetime(year, month, calculated_day, calculated_hour, minute_variation, 0, tzinfo=dt_timezone.utc)
        return_datetime_str = return_dt.isoformat()
        
        logger.info(
            f"📅 Placeholder amélioré: {target_month} → {return_datetime_str} "
            f"(jour={calculated_day}, heure={calculated_hour:02d}:{minute_variation:02d})"
        )
        
        # Ascendant approximatif (basé sur le mois)
        ascendant_sign_index = month % len(_ASCENDANT_SIGNS)
        ascendant_sign = _ASCENDANT_SIGNS[ascendant_sign_index]
        
        # Maison de la Lune (1-12, variée)
        moon_house = (month_offset % 12) + 1
        
        moon_pos = None
        sun_pos = None
    
    # Construire la réponse
    result = {
        "return_datetime": return_datetime_str,
        "ascendant": {
            "sign": ascendant_sign,
            "degree": 10.5
        },
        "moon": {
            "sign": moon_pos.sign if moon_pos else natal_moon_sign,
            "degree": moon_pos.degree if moon_pos else natal_moon_degree,
            "house": moon_house
        },
        "planets": {
            "Moon": {
                "sign": moon_pos.sign if moon_pos else natal_moon_sign,
                "degree": moon_pos.degree if moon_pos else natal_moon_degree
            },
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
    
    if sun_pos:
        result["planets"]["Sun"] = {
            "sign": sun_pos.sign,
            "degree": sun_pos.degree
        }
    
    return result

