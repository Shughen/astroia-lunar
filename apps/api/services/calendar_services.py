"""
Services métier pour le Calendrier Lunaire (P3)
Phases lunaires, événements spéciaux, et calendrier annuel
"""

from typing import Dict, Any, List
from datetime import datetime, date
from services import rapidapi_client
import logging

logger = logging.getLogger(__name__)


async def get_lunar_phases(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les phases lunaires précises pour une période donnée.
    
    Retourne les dates et heures exactes des nouvelles lunes, pleines lunes,
    premiers quartiers et derniers quartiers.
    
    Args:
        payload: {
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "latitude": float,         # Optionnel pour heure locale
            "longitude": float,
            "timezone": "Europe/Paris"
        }
        
    Returns:
        Liste des phases lunaires avec dates/heures précises
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🌓 Calcul Lunar Phases de {payload.get('start_date')} à {payload.get('end_date')}")
    result = await rapidapi_client.post_json(rapidapi_client.LUNAR_PHASES_PATH, payload)
    logger.info("✅ Lunar Phases calculées avec succès")
    return result


async def get_lunar_events(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Obtient les événements lunaires spéciaux (éclipses, superlunes, etc.).
    
    Args:
        payload: {
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "latitude": float,
            "longitude": float,
            "event_types": ["eclipse", "supermoon", "micromoon"]  # Optionnel
        }
        
    Returns:
        Liste des événements lunaires spéciaux
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🌒 Calcul Lunar Events de {payload.get('start_date')} à {payload.get('end_date')}")
    result = await rapidapi_client.post_json(rapidapi_client.LUNAR_EVENTS_PATH, payload)
    logger.info("✅ Lunar Events calculés avec succès")
    return result


async def get_lunar_calendar_year(year: int, payload: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Obtient le calendrier lunaire complet pour une année.
    
    Retourne toutes les nouvelles/pleines lunes, éclipses et événements majeurs
    pour l'année entière.
    
    Args:
        year: Année (ex: 2025)
        payload: Paramètres optionnels (latitude, longitude, timezone)
        
    Returns:
        Calendrier lunaire annuel complet
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"📅 Calcul Lunar Calendar pour l'année {year}")
    
    # Le calendrier utilise GET avec l'année dans l'URL
    path = f"{rapidapi_client.LUNAR_CALENDAR_YEAR_PATH}/{year}"
    
    # Si le provider supporte POST, on peut aussi passer les params
    # Sinon, on peut faire un GET simple
    result = await rapidapi_client.post_json(path, payload or {})
    logger.info("✅ Lunar Calendar annuel calculé avec succès")
    return result


def generate_monthly_calendar(
    phases_data: Dict[str, Any],
    mansions_data: List[Dict[str, Any]],
    events_data: Dict[str, Any],
    year: int,
    month: int
) -> Dict[str, Any]:
    """
    Génère un calendrier mensuel combiné avec phases, mansions et événements.
    
    Croise les données de plusieurs sources pour créer une vue calendrier unifiée.
    
    Args:
        phases_data: Données des phases lunaires du mois
        mansions_data: Liste des mansions quotidiennes
        events_data: Événements lunaires spéciaux
        year: Année
        month: Mois (1-12)
        
    Returns:
        {
            "year": 2025,
            "month": 1,
            "days": [
                {
                    "date": "2025-01-15",
                    "day_of_week": "Wednesday",
                    "phases": ["new_moon"],
                    "mansion": {"id": 7, "name": "Al-Dhira"},
                    "events": ["supermoon"],
                    "lunar_day": 1
                }
            ],
            "summary": {
                "new_moons": 1,
                "full_moons": 1,
                "eclipses": 0,
                "special_events": 2
            }
        }
    """
    # TODO: Implémenter la logique de fusion des données
    # Pour l'instant, retourner une structure de base
    
    calendar_days = []
    summary = {
        "new_moons": 0,
        "full_moons": 0,
        "eclipses": 0,
        "special_events": 0
    }
    
    # Logique simplifiée - à améliorer avec les vraies données
    return {
        "year": year,
        "month": month,
        "days": calendar_days,
        "summary": summary
    }

