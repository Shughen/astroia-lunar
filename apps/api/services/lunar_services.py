"""
Services métier pour le Luna Pack
Wrap des endpoints RapidAPI pour les fonctionnalités lunaires avancées
"""

from typing import Dict, Any
from services import rapidapi_client
from services.lunar_normalization import (
    normalize_lunar_mansion_response,
    normalize_lunar_return_report_response
)
import logging

logger = logging.getLogger(__name__)


async def get_lunar_return_report(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient le rapport mensuel de révolution lunaire depuis RapidAPI.

    Le rapport contient l'analyse complète de la position de la Lune de retour
    et ses implications pour le mois à venir.

    Args:
        payload: {
            "birth_date": "YYYY-MM-DD",
            "birth_time": "HH:MM",
            "latitude": float,
            "longitude": float,
            "timezone": "Europe/Paris",
            "city": "Paris",
            "country_code": "FR",
            "date": "YYYY-MM-DD",  # Date pour laquelle calculer le return
            "month": "YYYY-MM",  # Optionnel: mois de la révolution lunaire
            ...autres paramètres selon doc RapidAPI
        }

    Returns:
        Données JSON normalisées du rapport lunaire avec schéma stable

    Raises:
        HTTPException: 422 si payload invalide, 502 si erreur provider
    """
    logger.info(f"🌙 Calcul Lunar Return Report pour: {payload.get('date', 'N/A')}")

    # Transform flat payload to RapidAPI nested format
    rapidapi_payload = _transform_to_rapidapi_format(payload)

    # Get raw response from RapidAPI
    raw_result = await rapidapi_client.post_json(rapidapi_client.LUNAR_RETURN_REPORT_PATH, rapidapi_payload)

    # Normalize response to stable schema
    normalized_result = normalize_lunar_return_report_response(
        raw_result,
        request_month=payload.get('month')
    )

    logger.info("✅ Lunar Return Report calculé et normalisé avec succès")
    return normalized_result


def _transform_to_rapidapi_format(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforme le payload plat en format attendu par RapidAPI.

    RapidAPI attend une structure avec:
    - subject.birth_data contenant les données de naissance structurées
    - return_month pour le mois de calcul (optionnel)

    Args:
        payload: Format plat avec birth_date, birth_time, latitude, etc.

    Returns:
        Format RapidAPI avec subject.birth_data nested

    Raises:
        ValueError: Si les champs requis sont manquants
    """
    # Validate required fields
    required_fields = ['birth_date', 'latitude', 'longitude']
    missing_fields = [field for field in required_fields if not payload.get(field)]
    if missing_fields:
        raise ValueError(f"Champs requis manquants: {', '.join(missing_fields)}")

    # Parse birth_date: "1989-04-15" -> year=1989, month=4, day=15
    birth_date = payload.get('birth_date')
    try:
        year, month, day = birth_date.split('-')
        year, month, day = int(year), int(month), int(day)
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Format birth_date invalide (attendu: YYYY-MM-DD): {birth_date}") from e

    # Parse birth_time: "17:55" -> hour=17, minute=55
    birth_time = payload.get('birth_time', '12:00')  # Default to noon if not provided
    try:
        hour, minute = birth_time.split(':')
        hour, minute = int(hour), int(minute)
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Format birth_time invalide (attendu: HH:MM): {birth_time}") from e

    # Construct RapidAPI nested payload
    rapidapi_payload = {
        "subject": {
            "name": payload.get('city', 'User'),
            "birth_data": {
                "year": year,
                "month": month,
                "day": day,
                "hour": hour,
                "minute": minute,
                "second": 0,
                "latitude": payload.get('latitude'),
                "longitude": payload.get('longitude'),
                "timezone": payload.get('timezone', 'UTC'),
                "city": payload.get('city', 'Unknown'),
                "country_code": payload.get('country_code', 'FR')
            }
        }
    }

    # Add optional return_month if provided (format: "2025-11")
    if 'month' in payload:
        rapidapi_payload['return_month'] = payload['month']

    # Add optional return date if provided (format: "2025-11-15")
    if 'date' in payload and payload['date'] != birth_date:
        rapidapi_payload['return_date'] = payload['date']

    # Add any options if provided
    if 'options' in payload:
        rapidapi_payload['options'] = payload['options']

    logger.debug(f"📤 Transformed payload for RapidAPI: subject.name={rapidapi_payload['subject']['name']}, "
                f"birth_data={rapidapi_payload['subject']['birth_data']['year']}-"
                f"{rapidapi_payload['subject']['birth_data']['month']}-"
                f"{rapidapi_payload['subject']['birth_data']['day']}")

    return rapidapi_payload


async def get_void_of_course_status(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les informations Void of Course (VoC) de la Lune.

    Le VoC représente la période où la Lune ne fait plus d'aspects majeurs
    avant de changer de signe - considérée comme peu propice aux initiatives.

    Args:
        payload: {
            "date": "YYYY-MM-DD",
            "time": "HH:MM",
            "latitude": float,
            "longitude": float,
            "timezone": "Europe/Paris",
            ...autres paramètres selon doc RapidAPI
        }

    Returns:
        Données JSON avec les fenêtres VoC (start/end) et statut actuel

    Raises:
        HTTPException: 422 si payload invalide, 502 si erreur provider
    """
    logger.info(f"🌑 Vérification Void of Course pour: {payload.get('date', 'N/A')}")

    # Transform flat payload to RapidAPI nested format
    rapidapi_payload = _transform_voc_to_rapidapi_format(payload)

    result = await rapidapi_client.post_json(rapidapi_client.VOID_OF_COURSE_PATH, rapidapi_payload)
    logger.info("✅ Void of Course calculé avec succès")
    return result


def _transform_voc_to_rapidapi_format(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforme le payload plat en format attendu par RapidAPI pour VoC.

    RapidAPI attend une structure avec:
    - datetime_location contenant year, month, day, hour, minute (int) + latitude, longitude, timezone

    Args:
        payload: Format plat avec date (YYYY-MM-DD), time (HH:MM), latitude, longitude, timezone

    Returns:
        Format RapidAPI avec datetime_location nested et composantes datetime parsées

    Raises:
        ValueError: Si les champs requis sont manquants ou format invalide
    """
    # Validate required fields for VoC
    required_fields = ['date', 'time', 'latitude', 'longitude']
    missing_fields = [field for field in required_fields if not payload.get(field)]
    if missing_fields:
        raise ValueError(f"Champs requis manquants: {', '.join(missing_fields)}")

    # Parse date: "2025-12-31" -> year=2025, month=12, day=31
    date_str = payload.get('date')
    try:
        year, month, day = date_str.split('-')
        year, month, day = int(year), int(month), int(day)
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Format date invalide (attendu: YYYY-MM-DD): {date_str}") from e

    # Parse time: "12:00" or "12:00:00" -> hour=12, minute=0
    time_str = payload.get('time')
    try:
        time_parts = time_str.split(':')
        hour, minute = int(time_parts[0]), int(time_parts[1])
        # Ignore seconds if provided (HH:MM:SS format)
    except (ValueError, AttributeError, IndexError) as e:
        raise ValueError(f"Format time invalide (attendu: HH:MM): {time_str}") from e

    # Construct RapidAPI nested payload for VoC
    rapidapi_payload = {
        "datetime_location": {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": 0,
            "latitude": payload.get('latitude'),
            "longitude": payload.get('longitude'),
            "timezone": payload.get('timezone', 'UTC')
        }
    }

    # Add any options if provided
    if 'options' in payload:
        rapidapi_payload['options'] = payload['options']

    logger.debug(f"📤 Transformed VoC payload for RapidAPI: datetime_location={rapidapi_payload['datetime_location']}")

    return rapidapi_payload


async def get_lunar_mansions(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les informations sur la mansion lunaire actuelle (système des 28 mansions).

    Les 28 mansions lunaires sont un système ancien divisant l'orbite lunaire
    en 28 segments, chacun ayant sa propre signification et influence.

    Args:
        payload: {
            "date": "YYYY-MM-DD",
            "time": "HH:MM",
            "latitude": float,
            "longitude": float,
            "timezone": "Europe/Paris",
            ...autres paramètres selon doc RapidAPI
        }

    Returns:
        Données JSON normalisées avec schéma stable (number, name toujours présents)

    Raises:
        HTTPException: 422 si payload invalide, 502 si erreur provider
    """
    logger.info(f"🏰 Calcul Lunar Mansion pour: {payload.get('date', 'N/A')}")

    # Transform flat payload to RapidAPI nested format
    rapidapi_payload = _transform_mansion_to_rapidapi_format(payload)

    # Get raw response from RapidAPI
    raw_result = await rapidapi_client.post_json(rapidapi_client.LUNAR_MANSIONS_PATH, rapidapi_payload)

    # Normalize response to stable schema
    normalized_result = normalize_lunar_mansion_response(raw_result)

    logger.info("✅ Lunar Mansion calculée et normalisée avec succès")
    return normalized_result


def _transform_mansion_to_rapidapi_format(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Transforme le payload plat en format attendu par RapidAPI pour Lunar Mansions.

    RapidAPI attend une structure avec:
    - datetime_location contenant year, month, day, hour, minute (int) + latitude, longitude, timezone

    Args:
        payload: Format plat avec date (YYYY-MM-DD), time (HH:MM), latitude, longitude, timezone

    Returns:
        Format RapidAPI avec datetime_location nested et composantes datetime parsées

    Raises:
        ValueError: Si les champs requis sont manquants ou format invalide
    """
    # Validate required fields for Lunar Mansions
    required_fields = ['date', 'time', 'latitude', 'longitude']
    missing_fields = [field for field in required_fields if not payload.get(field)]
    if missing_fields:
        raise ValueError(f"Champs requis manquants: {', '.join(missing_fields)}")

    # Parse date: "2025-12-31" -> year=2025, month=12, day=31
    date_str = payload.get('date')
    try:
        year, month, day = date_str.split('-')
        year, month, day = int(year), int(month), int(day)
    except (ValueError, AttributeError) as e:
        raise ValueError(f"Format date invalide (attendu: YYYY-MM-DD): {date_str}") from e

    # Parse time: "12:00" or "12:00:00" -> hour=12, minute=0
    time_str = payload.get('time')
    try:
        time_parts = time_str.split(':')
        hour, minute = int(time_parts[0]), int(time_parts[1])
        # Ignore seconds if provided (HH:MM:SS format)
    except (ValueError, AttributeError, IndexError) as e:
        raise ValueError(f"Format time invalide (attendu: HH:MM): {time_str}") from e

    # Construct RapidAPI nested payload for Lunar Mansions
    rapidapi_payload = {
        "datetime_location": {
            "year": year,
            "month": month,
            "day": day,
            "hour": hour,
            "minute": minute,
            "second": 0,
            "latitude": payload.get('latitude'),
            "longitude": payload.get('longitude'),
            "timezone": payload.get('timezone', 'UTC')
        }
    }

    # Add any options if provided
    if 'options' in payload:
        rapidapi_payload['options'] = payload['options']

    logger.debug(f"📤 Transformed Mansion payload for RapidAPI: datetime_location={rapidapi_payload['datetime_location']}")

    return rapidapi_payload

