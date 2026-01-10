"""
Client HTTP pour RapidAPI - Best Astrology API
Calcul de thèmes natals via l'endpoint chart_natal
"""

import httpx
from typing import Dict, Any
from config import settings
import logging

logger = logging.getLogger(__name__)

# Client HTTP asynchrone avec timeout
client = httpx.AsyncClient(timeout=30.0)


async def create_natal_chart(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Appelle l'endpoint RapidAPI pour calculer un thème natal.
    
    Args:
        payload: Données du thème natal (date, heure, lieu, etc.)
        
    Returns:
        Réponse JSON de RapidAPI
        
    Raises:
        httpx.HTTPStatusError: Si l'API retourne une erreur HTTP
    """
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }
    
    logger.info(f"Appel RapidAPI chart_natal avec payload: {payload}")
    
    try:
        response = await client.post(
            settings.NATAL_URL,
            json=payload,
            headers=headers
        )
        response.raise_for_status()
        
        data = response.json()
        logger.info("Réponse RapidAPI reçue avec succès")
        return data
        
    except httpx.HTTPStatusError as e:
        logger.error(f"Erreur HTTP RapidAPI: {e.response.status_code} - {e.response.text}")
        raise
    except httpx.RequestError as e:
        logger.error(f"Erreur de requête RapidAPI: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Erreur inattendue lors de l'appel RapidAPI: {str(e)}")
        raise


async def close_client():
    """Ferme le client HTTP (à appeler au shutdown de l'app)"""
    await client.aclose()

