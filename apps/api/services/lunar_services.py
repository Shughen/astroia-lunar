"""
Services métier pour le Luna Pack
Wrap des endpoints RapidAPI pour les fonctionnalités lunaires avancées
"""

from typing import Dict, Any
from services import rapidapi_client
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
            "date": "YYYY-MM-DD",  # Date pour laquelle calculer le return
            ...autres paramètres selon doc RapidAPI
        }
        
    Returns:
        Données JSON du rapport lunaire complet
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🌙 Calcul Lunar Return Report pour: {payload.get('date', 'N/A')}")
    result = await rapidapi_client.post_json(rapidapi_client.LUNAR_RETURN_REPORT_PATH, payload)
    logger.info("✅ Lunar Return Report calculé avec succès")
    return result


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
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🌑 Vérification Void of Course pour: {payload.get('date', 'N/A')}")
    result = await rapidapi_client.post_json(rapidapi_client.VOID_OF_COURSE_PATH, payload)
    logger.info("✅ Void of Course calculé avec succès")
    return result


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
            ...autres paramètres selon doc RapidAPI
        }
        
    Returns:
        Données JSON avec le numéro de mansion, nom, et interprétation
        
    Raises:
        HTTPException: 502 si erreur provider
    """
    logger.info(f"🏰 Calcul Lunar Mansion pour: {payload.get('date', 'N/A')}")
    result = await rapidapi_client.post_json(rapidapi_client.LUNAR_MANSIONS_PATH, payload)
    logger.info("✅ Lunar Mansion calculée avec succès")
    return result

