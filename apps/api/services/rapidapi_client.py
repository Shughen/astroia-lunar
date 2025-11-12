"""
Client HTTP générique pour RapidAPI - Best Astrology API
Permet d'appeler tous les endpoints de l'API de manière unifiée
Avec retries, exponential backoff, timeouts, et gestion robuste des erreurs
"""

import httpx
from typing import Dict, Any
from config import settings
import logging
import asyncio
import random
from fastapi import HTTPException

logger = logging.getLogger(__name__)

# Client HTTP asynchrone avec timeout pour les calculs lourds
client = httpx.AsyncClient(timeout=10.0)  # Timeout standard 10s

# Configuration retries
MAX_RETRIES = 3
BASE_BACKOFF = 0.5  # secondes
MAX_BACKOFF = 4.0   # secondes

# Chemins d'endpoints RapidAPI (depuis ENV avec defaults)
# Ces chemins peuvent être surchargés via .env si l'API évolue
LUNAR_RETURN_REPORT_PATH = settings.LUNAR_RETURN_REPORT_PATH
VOID_OF_COURSE_PATH = settings.VOID_OF_COURSE_PATH
LUNAR_MANSIONS_PATH = settings.LUNAR_MANSIONS_PATH
NATAL_TRANSITS_PATH = settings.NATAL_TRANSITS_PATH
LUNAR_RETURN_TRANSITS_PATH = settings.LUNAR_RETURN_TRANSITS_PATH
LUNAR_PHASES_PATH = settings.LUNAR_PHASES_PATH
LUNAR_EVENTS_PATH = settings.LUNAR_EVENTS_PATH
LUNAR_CALENDAR_YEAR_PATH = settings.LUNAR_CALENDAR_YEAR_PATH


async def post_json(path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Effectue un POST JSON sur un endpoint RapidAPI avec retries et exponential backoff.
    
    Args:
        path: Chemin de l'endpoint (ex: /api/v3/charts/lunar_return)
        payload: Données JSON à envoyer
        
    Returns:
        Réponse JSON de l'API
        
    Raises:
        HTTPException: 502 Bad Gateway si l'API provider échoue après retries
    """
    # Construction de l'URL complète
    url = f"{settings.BASE_RAPID_URL}{path}"
    
    # Headers standardisés pour RapidAPI
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }
    
    logger.info(f"📡 Appel RapidAPI: POST {path}")
    
    # Tentatives avec exponential backoff + jitter
    for attempt in range(MAX_RETRIES):
        try:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            logger.info(f"✅ Réponse RapidAPI reçue (status {response.status_code}, attempt {attempt + 1})")
            return data
            
        except httpx.HTTPStatusError as e:
            status = e.response.status_code
            body_preview = e.response.text[:200] if e.response.text else "No body"
            
            # Gestion des erreurs retriables (429, 5xx)
            if status == 429 or (500 <= status < 600):
                if attempt < MAX_RETRIES - 1:
                    # Calcul du backoff avec jitter
                    backoff = min(BASE_BACKOFF * (2 ** attempt), MAX_BACKOFF)
                    jitter = random.uniform(0, 0.3 * backoff)
                    wait_time = backoff + jitter
                    
                    logger.warning(
                        f"⚠️  Erreur {status} de RapidAPI sur {path}, "
                        f"retry {attempt + 1}/{MAX_RETRIES} dans {wait_time:.2f}s"
                    )
                    await asyncio.sleep(wait_time)
                    continue
                else:
                    # Dernière tentative échouée
                    logger.error(f"❌ Échec définitif après {MAX_RETRIES} tentatives: {status} - {body_preview}")
                    raise HTTPException(
                        status_code=502,
                        detail=f"Service provider indisponible après {MAX_RETRIES} tentatives (HTTP {status})"
                    )
            else:
                # Erreur non retriable (400, 401, 403, 404, etc.)
                logger.error(f"❌ Erreur HTTP {status} non retriable de RapidAPI sur {path}: {body_preview}")
                raise HTTPException(
                    status_code=502,
                    detail=f"Erreur provider: HTTP {status}"
                )
                
        except httpx.TimeoutException as e:
            if attempt < MAX_RETRIES - 1:
                backoff = min(BASE_BACKOFF * (2 ** attempt), MAX_BACKOFF)
                jitter = random.uniform(0, 0.3 * backoff)
                wait_time = backoff + jitter
                
                logger.warning(f"⚠️  Timeout RapidAPI sur {path}, retry {attempt + 1}/{MAX_RETRIES} dans {wait_time:.2f}s")
                await asyncio.sleep(wait_time)
                continue
            else:
                logger.error(f"❌ Timeout définitif après {MAX_RETRIES} tentatives sur {path}")
                raise HTTPException(
                    status_code=504,
                    detail=f"Timeout provider après {MAX_RETRIES} tentatives"
                )
                
        except httpx.RequestError as e:
            # Erreur réseau/connectivité
            logger.error(f"❌ Erreur de requête RapidAPI sur {path}: {str(e)}")
            raise HTTPException(
                status_code=502,
                detail=f"Erreur réseau provider: {str(e)}"
            )
            
        except Exception as e:
            # Erreur inattendue
            logger.error(f"❌ Erreur inattendue lors de l'appel RapidAPI {path}: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Erreur interne: {str(e)}"
            )
    
    # Normalement inaccessible (pour mypy)
    raise HTTPException(status_code=502, detail="Erreur provider inattendue")


async def close_client():
    """Ferme proprement le client HTTP (à appeler au shutdown de l'app)"""
    logger.info("Fermeture du client RapidAPI")
    await client.aclose()

