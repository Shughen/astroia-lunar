"""
Client HTTP générique pour RapidAPI - Best Astrology API
Permet d'appeler tous les endpoints de l'API de manière unifiée
Avec retries, exponential backoff, timeouts, et gestion robuste des erreurs

Mode DEV_MOCK_RAPIDAPI:
- Si DEV_MOCK_RAPIDAPI=true OU si RapidAPI retourne 403 "not subscribed"
- Utilise des mocks déterministes au lieu d'appeler l'API
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

    Mode DEV_MOCK_RAPIDAPI:
    - Si settings.DEV_MOCK_RAPIDAPI=true, retourne directement un mock
    - Si RapidAPI retourne 403 "not subscribed", fallback sur mock

    Args:
        path: Chemin de l'endpoint (ex: /api/v3/charts/lunar_return)
        payload: Données JSON à envoyer

    Returns:
        Réponse JSON de l'API ou mock déterministe

    Raises:
        HTTPException:
            - 422 si payload invalide (erreur client)
            - 400 si bad request (erreur client)
            - 401 si non autorisé (erreur config API key)
            - 502 si erreur provider 5xx après retries
            - 504 si timeout après retries
    """
    # Mode DEV_MOCK_RAPIDAPI: bypass RapidAPI et retourner mock directement
    if settings.DEV_MOCK_RAPIDAPI:
        logger.warning(f"🎭 DEV_MOCK_RAPIDAPI enabled -> using mock for {path}")
        return _get_mock_response(path, payload)

    # Construction de l'URL complète
    url = f"{settings.BASE_RAPID_URL}{path}"

    # Headers standardisés pour RapidAPI
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": settings.RAPIDAPI_HOST,
        "x-rapidapi-key": settings.RAPIDAPI_KEY,
    }

    # Log payload summary (sans PII sensibles)
    payload_summary = {
        "endpoint": path,
        "has_subject": "subject" in payload,
        "has_birth_data": "subject" in payload and "birth_data" in payload.get("subject", {}),
        "fields": list(payload.keys())
    }
    logger.info(f"📡 Appel RapidAPI: POST {path} | Payload: {payload_summary}")

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
            body_preview = e.response.text[:500] if e.response.text else "No body"

            # Parse error response if JSON
            error_details = None
            try:
                error_json = e.response.json()
                error_details = error_json
            except Exception:
                error_details = {"raw_error": body_preview}

            # Map client errors (4xx) - ne pas retry, retourner immédiatement
            if status == 400:
                # Bad Request - erreur de format/payload
                logger.error(f"❌ Bad Request (400) de RapidAPI sur {path}: {error_details}")
                raise HTTPException(
                    status_code=400,
                    detail={
                        "code": "BAD_REQUEST",
                        "message": "Requête invalide envoyée à l'API astrologique",
                        "provider_error": error_details
                    }
                )

            elif status == 401:
                # Unauthorized - problème API key
                logger.error(f"❌ Unauthorized (401) de RapidAPI sur {path}: {error_details}")
                raise HTTPException(
                    status_code=502,  # 502 car c'est une erreur de config serveur
                    detail={
                        "code": "PROVIDER_AUTH_ERROR",
                        "message": "Erreur d'authentification avec le fournisseur astrologique",
                        "provider_error": error_details
                    }
                )

            elif status == 403:
                # Forbidden - quota/permissions ou not subscribed
                # Détecter si c'est un problème de subscription
                error_message = error_details.get("message", "") if isinstance(error_details, dict) else str(error_details)
                is_not_subscribed = "not subscribed" in error_message.lower()

                if is_not_subscribed:
                    # Not subscribed - fallback sur mock pour éviter de bloquer l'app en dev
                    logger.warning(f"⚠️  RapidAPI not subscribed (403) sur {path} -> fallback sur mock")
                    return _get_mock_response(path, payload)
                else:
                    # Autre erreur 403 (quota, permissions, etc.)
                    logger.error(f"❌ Forbidden (403) de RapidAPI sur {path}: {error_details}")
                    raise HTTPException(
                        status_code=502,  # 502 car c'est une erreur côté provider
                        detail={
                            "code": "PROVIDER_FORBIDDEN",
                            "message": "Accès refusé par le fournisseur astrologique (quota ou permissions)",
                            "provider_error": error_details
                        }
                    )

            elif status == 404:
                # Not Found - endpoint invalide
                logger.error(f"❌ Not Found (404) de RapidAPI sur {path}: {error_details}")
                raise HTTPException(
                    status_code=502,
                    detail={
                        "code": "PROVIDER_NOT_FOUND",
                        "message": f"Endpoint introuvable: {path}",
                        "provider_error": error_details
                    }
                )

            elif status == 422:
                # Unprocessable Entity - validation payload échouée
                logger.error(f"❌ Unprocessable Entity (422) de RapidAPI sur {path}: {error_details}")
                raise HTTPException(
                    status_code=422,
                    detail={
                        "code": "INVALID_PAYLOAD",
                        "message": "Les données envoyées sont invalides pour l'API astrologique",
                        "provider_error": error_details,
                        "hint": "Vérifiez que tous les champs requis (birth_date, latitude, longitude) sont présents et au bon format"
                    }
                )

            # Gestion des erreurs retriables (429, 5xx)
            elif status == 429 or (500 <= status < 600):
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
                    logger.error(f"❌ Échec définitif après {MAX_RETRIES} tentatives: {status} - {error_details}")

                    # 429 = Rate Limit après retries -> code spécifique
                    if status == 429:
                        raise HTTPException(
                            status_code=429,
                            detail={
                                "code": "RAPIDAPI_RATE_LIMIT",
                                "message": "Rate limit reached. Try later.",
                                "provider_error": error_details
                            }
                        )
                    else:
                        # Autres erreurs 5xx
                        raise HTTPException(
                            status_code=502,
                            detail={
                                "code": "PROVIDER_UNAVAILABLE",
                                "message": f"Service astrologique indisponible après {MAX_RETRIES} tentatives (HTTP {status})",
                                "provider_error": error_details
                            }
                        )
            else:
                # Autre erreur 4xx non gérée explicitement
                logger.error(f"❌ Erreur HTTP {status} inattendue de RapidAPI sur {path}: {error_details}")
                raise HTTPException(
                    status_code=502,
                    detail={
                        "code": "PROVIDER_ERROR",
                        "message": f"Erreur inattendue du fournisseur astrologique (HTTP {status})",
                        "provider_error": error_details
                    }
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
            # Erreur inattendue (ne devrait pas arriver, mais éviter 500)
            logger.error(f"❌ Erreur inattendue lors de l'appel RapidAPI {path}: {str(e)}", exc_info=True)
            raise HTTPException(
                status_code=502,
                detail={
                    "code": "PROVIDER_UNEXPECTED_ERROR",
                    "message": "Erreur inattendue lors de la communication avec le fournisseur astrologique",
                    "details": str(e)
                }
            )
    
    # Normalement inaccessible (pour mypy)
    raise HTTPException(status_code=502, detail="Erreur provider inattendue")


def _get_mock_response(path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Retourne un mock déterministe basé sur le path de l'endpoint.
    Utilisé quand DEV_MOCK_RAPIDAPI=true ou quand RapidAPI retourne 403 "not subscribed"

    Args:
        path: Chemin de l'endpoint RapidAPI
        payload: Payload de la requête (pour génération déterministe)

    Returns:
        Mock JSON compatible avec le schéma attendu

    Raises:
        HTTPException: 501 si l'endpoint n'a pas de mock disponible
    """
    from services.rapidapi_mocks import (
        generate_lunar_mansion_mock,
        generate_void_of_course_mock,
        generate_lunar_return_report_mock
    )

    # Router vers le bon mock selon le path
    if path == LUNAR_MANSIONS_PATH or "mansions" in path.lower():
        return generate_lunar_mansion_mock(payload)
    elif path == VOID_OF_COURSE_PATH or "void-of-course" in path.lower() or "voc" in path.lower():
        return generate_void_of_course_mock(payload)
    elif path == LUNAR_RETURN_REPORT_PATH or "lunar-return-report" in path.lower():
        return generate_lunar_return_report_mock(payload)
    else:
        # Endpoint non mocké - retourner une erreur
        logger.error(f"❌ Aucun mock disponible pour {path}")
        raise HTTPException(
            status_code=501,
            detail={
                "code": "MOCK_NOT_IMPLEMENTED",
                "message": f"Mock non disponible pour l'endpoint {path}",
                "hint": "Contactez l'équipe dev ou activez RapidAPI subscription"
            }
        )


async def close_client():
    """Ferme proprement le client HTTP (à appeler au shutdown de l'app)"""
    logger.info("Fermeture du client RapidAPI")
    await client.aclose()

