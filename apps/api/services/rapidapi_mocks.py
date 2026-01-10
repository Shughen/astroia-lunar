"""
Mock RapidAPI - Génération de données déterministes pour DEV
Permet de tester l'app sans clé RapidAPI (notamment lorsque not subscribed)
"""

import hashlib
from typing import Dict, Any
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


def _hash_location_date(date_str: str, latitude: float, longitude: float) -> int:
    """
    Génère un hash déterministe basé sur date + localisation.
    Utilisé pour garantir la cohérence des mocks (même input = même output)

    Args:
        date_str: Date au format YYYY-MM-DD
        latitude: Latitude
        longitude: Longitude

    Returns:
        Hash integer (0-999999)
    """
    key = f"{date_str}_{latitude}_{longitude}"
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % 1000000


def generate_lunar_mansion_mock(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un mock déterministe pour Lunar Mansion.

    Args:
        payload: Requête RapidAPI avec datetime_location

    Returns:
        Réponse mock compatible avec le schéma normalisé
    """
    dt_loc = payload.get("datetime_location", {})
    date_str = f"{dt_loc.get('year', 2025)}-{dt_loc.get('month', 1):02d}-{dt_loc.get('day', 1):02d}"
    latitude = dt_loc.get("latitude", 48.8566)
    longitude = dt_loc.get("longitude", 2.3522)

    # Hash déterministe pour sélectionner une mansion (1-28)
    hash_val = _hash_location_date(date_str, latitude, longitude)
    mansion_number = (hash_val % 28) + 1

    # Noms des 28 mansions (système arabe/indien)
    mansion_names = [
        "Al-Sharatain", "Al-Butain", "Al-Thurayya", "Al-Dabaran",
        "Al-Haq'ah", "Al-Han'ah", "Al-Dhira", "Al-Nathrah",
        "Al-Tarf", "Al-Jabhah", "Al-Zubrah", "Al-Sarfah",
        "Al-Awwa", "Al-Simak", "Al-Ghafr", "Al-Zubana",
        "Al-Iklil", "Al-Qalb", "Al-Shaulah", "Al-Na'am",
        "Al-Baldah", "Sa'd al-Dhabih", "Sa'd Bula", "Sa'd al-Su'ud",
        "Sa'd al-Akhbiyah", "Al-Fargh al-Mukdim", "Al-Fargh al-Thani", "Al-Batn al-Hut"
    ]

    mansion_name = mansion_names[mansion_number - 1]

    # Calcul de la prochaine mansion (mansion suivante, +1 jour)
    next_mansion_number = (mansion_number % 28) + 1
    next_mansion_name = mansion_names[next_mansion_number - 1]

    # Heure de changement (déterministe basée sur le hash)
    base_hour = (hash_val % 24)
    base_minute = ((hash_val // 24) % 60)

    # Générer une date de changement réaliste (dans les 24-48h)
    change_date = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=1, hours=base_hour, minutes=base_minute)

    logger.info(f"🎭 Mock Lunar Mansion: #{mansion_number} ({mansion_name}) pour {date_str}")

    return {
        "mansion": {
            "number": mansion_number,
            "name": mansion_name,
            "interpretation": f"Mock interpretation for {mansion_name}. This is a development mock response."
        },
        "upcoming_changes": [
            {
                "change_time": change_date.isoformat(),
                "from_mansion": {
                    "number": mansion_number,
                    "name": mansion_name
                },
                "to_mansion": {
                    "number": next_mansion_number,
                    "name": next_mansion_name
                }
            }
        ],
        "calendar_summary": {
            "significant_periods": []
        },
        "_mock": True,
        "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    }


def generate_void_of_course_mock(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un mock déterministe pour Void of Course.

    Args:
        payload: Requête RapidAPI avec datetime_location

    Returns:
        Réponse mock compatible avec le schéma attendu
    """
    dt_loc = payload.get("datetime_location", {})
    date_str = f"{dt_loc.get('year', 2025)}-{dt_loc.get('month', 1):02d}-{dt_loc.get('day', 1):02d}"
    latitude = dt_loc.get("latitude", 48.8566)
    longitude = dt_loc.get("longitude", 2.3522)

    # Hash déterministe pour déterminer si VoC actif (50% de chance)
    hash_val = _hash_location_date(date_str, latitude, longitude)
    is_void = (hash_val % 2) == 0

    # Signe lunaire (12 signes)
    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    moon_sign = signs[hash_val % 12]

    base_time = datetime.strptime(f"{date_str} {dt_loc.get('hour', 12):02d}:{dt_loc.get('minute', 0):02d}", "%Y-%m-%d %H:%M")

    logger.info(f"🎭 Mock Void of Course: {'Actif' if is_void else 'Inactif'} pour {date_str}")

    if is_void:
        # VoC actif: fenêtre de 2-6h
        duration_hours = (hash_val % 4) + 2  # 2-5h
        start_time = base_time - timedelta(hours=1)
        end_time = start_time + timedelta(hours=duration_hours)

        return {
            "is_void": True,
            "void_of_course": {
                "start": start_time.isoformat(),
                "end": end_time.isoformat()
            },
            "moon_sign": moon_sign,
            "_mock": True,
            "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
        }
    else:
        # VoC inactif: prochain VoC dans 12-48h
        next_start_hours = ((hash_val % 36) + 12)  # 12-47h
        next_start = base_time + timedelta(hours=next_start_hours)
        next_end = next_start + timedelta(hours=3)

        return {
            "is_void": False,
            "next_void": {
                "start": next_start.isoformat(),
                "end": next_end.isoformat()
            },
            "moon_sign": moon_sign,
            "_mock": True,
            "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
        }


def generate_lunar_return_report_mock(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un mock déterministe pour Lunar Return Report.

    Args:
        payload: Requête RapidAPI avec subject.birth_data et return_month

    Returns:
        Réponse mock compatible avec le schéma normalisé
    """
    birth_data = payload.get("subject", {}).get("birth_data", {})
    return_month = payload.get("return_month", "2025-01")
    latitude = birth_data.get("latitude", 48.8566)
    longitude = birth_data.get("longitude", 2.3522)

    # Date de retour lunaire (estimée au 15 du mois)
    return_date = f"{return_month}-15T10:30:00"

    # Hash pour sélectionner signe et maison
    hash_val = _hash_location_date(return_month, latitude, longitude)

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    moon_sign = signs[hash_val % 12]
    moon_house = (hash_val % 12) + 1
    moon_degree = (hash_val % 30) + 1.5

    logger.info(f"🎭 Mock Lunar Return Report: {return_month} - Lune en {moon_sign} M{moon_house}")

    return {
        "return_date": return_date,
        "moon": {
            "sign": moon_sign,
            "degree": moon_degree,
            "house": moon_house
        },
        "interpretation": f"Mock interpretation for Lunar Return in {moon_sign}. This is a development mock response.",
        "_mock": True,
        "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    }
