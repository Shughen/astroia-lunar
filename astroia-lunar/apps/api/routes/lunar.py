"""
Routes FastAPI pour le Luna Pack (P1)
Endpoints pour Lunar Return Report, Void of Course, et Lunar Mansions
"""

from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func
from typing import Dict, Any
from datetime import datetime, date, timezone
import logging
import time

from database import get_db
from services import lunar_services
from services.moon_position import get_current_moon_position
from services.daily_climate import get_daily_climate
from services import voc_cache_service
from schemas.lunar import (
    LunarReturnReportRequest,
    VoidOfCourseRequest,
    LunarMansionRequest,
    LunarResponse
)
from models.lunar_pack import LunarReport, LunarVocWindow, LunarMansionDaily
from models.user import User
from routes.auth import get_current_user

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/lunar", tags=["Luna Pack"])

# Cache global pour metadata (TTL: 10 minutes)
_METADATA_CACHE: Dict[int, Any] = {}  # Key: user_id → (data, timestamp)
METADATA_CACHE_TTL = 600  # 10 minutes


def _deduplicate_mansion_response(result: Dict[str, Any]) -> Dict[str, Any]:
    """
    Déduplique les entrées identiques dans upcoming_changes et calendar_summary.significant_periods.

    Stratégie : key = (change_time, from_mansion.number, to_mansion.name)

    Args:
        result: Réponse brute de l'API avec potentiellement des doublons

    Returns:
        Réponse nettoyée sans doublons
    """
    # Dédupliquer upcoming_changes
    if "upcoming_changes" in result and isinstance(result["upcoming_changes"], list):
        seen = set()
        deduplicated_changes = []

        for change in result["upcoming_changes"]:
            # Créer une clé unique basée sur change_time, from_mansion.number, to_mansion.name
            change_time = change.get("change_time", "")
            from_number = change.get("from_mansion", {}).get("number", 0) if isinstance(change.get("from_mansion"), dict) else 0
            to_name = change.get("to_mansion", {}).get("name", "") if isinstance(change.get("to_mansion"), dict) else ""

            key = (change_time, from_number, to_name)

            if key not in seen:
                seen.add(key)
                deduplicated_changes.append(change)

        result["upcoming_changes"] = deduplicated_changes

    # Dédupliquer calendar_summary.significant_periods (même stratégie)
    if "calendar_summary" in result and isinstance(result["calendar_summary"], dict):
        if "significant_periods" in result["calendar_summary"] and isinstance(result["calendar_summary"]["significant_periods"], list):
            seen = set()
            deduplicated_periods = []

            for period in result["calendar_summary"]["significant_periods"]:
                # Créer une clé unique
                change_time = period.get("change_time", "")
                from_number = period.get("from_mansion", {}).get("number", 0) if isinstance(period.get("from_mansion"), dict) else 0
                to_name = period.get("to_mansion", {}).get("name", "") if isinstance(period.get("to_mansion"), dict) else ""

                key = (change_time, from_number, to_name)

                if key not in seen:
                    seen.add(key)
                    deduplicated_periods.append(period)

            result["calendar_summary"]["significant_periods"] = deduplicated_periods

    return result


@router.get("/current")
async def get_current_moon():
    """
    Calcule la position actuelle de la Lune avec Swiss Ephemeris.

    Retourne la longitude écliptique, le signe zodiacal et la phase lunaire.
    Les résultats sont mis en cache pendant 5 minutes côté serveur.

    **Returns:**
    ```json
    {
      "sign": "Gemini",
      "degree": 67.5,
      "phase": "Premier Quartier"
    }
    ```

    **Phases possibles:**
    - Nouvelle Lune
    - Premier Croissant
    - Premier Quartier
    - Lune Gibbeuse
    - Pleine Lune
    - Lune Disseminante
    - Dernier Quartier
    - Dernier Croissant

    **Signes possibles:**
    Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio,
    Sagittarius, Capricorn, Aquarius, Pisces
    """
    try:
        result = get_current_moon_position()
        logger.info(f"[GET /api/lunar/current] ✅ Moon: {result['degree']}° {result['sign']}, Phase: {result['phase']}")
        return result
    except Exception as e:
        logger.error(f"[GET /api/lunar/current] ❌ Error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to calculate moon position: {str(e)}"
        )


@router.get("/daily-climate")
async def get_daily_lunar_climate():
    """
    Récupère le Daily Lunar Climate avec insight stable sur 24h.

    Combine la position lunaire actuelle avec un insight déterministe généré
    en fonction de la date, du signe et de la phase lunaire.

    Le contenu reste STRICTEMENT identique pour toute la journée (cache 24h).

    **Returns:**
    ```json
    {
      "date": "2025-12-29",
      "moon": {
        "sign": "Gemini",
        "degree": 67.5,
        "phase": "Premier Quartier"
      },
      "insight": {
        "title": "Synthèse Brillante",
        "text": "Rassemblez les informations dispersées...",
        "keywords": ["synthèse", "cohérence", "intelligence", "clarté"],
        "version": "v1"
      }
    }
    ```

    **Cache:** 24h (invalidation automatique au changement de date)
    """
    try:
        result = get_daily_climate()
        logger.info(f"[GET /api/lunar/daily-climate] ✅ Climate (date: {result['date']}, insight: {result['insight']['title']})")
        return result
    except Exception as e:
        logger.error(f"[GET /api/lunar/daily-climate] ❌ Error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate daily climate: {str(e)}"
        )


@router.post("/return/report", response_model=LunarResponse, status_code=200)
async def lunar_return_report(
    request: LunarReturnReportRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)  # P0-2 FIX: Auth required
):
    """
    Génère un rapport mensuel de révolution lunaire.

    Le rapport contient l'analyse complète de la position de retour de la Lune
    et ses implications pour le mois à venir.

    - **month**: (Optionnel) Format YYYY-MM pour indexation et sauvegarde en DB
    - **payload**: Données requises par RapidAPI (date, coords, etc.)

    **Authentification requise**: Bearer token ou DEV_AUTH_BYPASS
    
    **Sécurité**: L'utilisateur authentifié est toujours utilisé pour la persistance DB,
    jamais le payload client.

    Raises:
        HTTPException:
            - 401 si non authentifié
            - 422 si payload invalide (champs manquants ou mauvais format)
            - 502 si erreur provider RapidAPI
    """
    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    # Validation explicite: garantir que current_user a un id valide
    if not current_user or not hasattr(current_user, 'id') or current_user.id is None:
        logger.error("❌ Authentification invalide: current_user ou current_user.id manquant")
        raise HTTPException(
            status_code=401,
            detail="Authentification invalide: utilisateur non identifié"
        )
    
    try:
        user_id = int(current_user.id)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"❌ Erreur extraction user_id: {e}, current_user={current_user}")
        raise HTTPException(
            status_code=401,
            detail="Authentification invalide: impossible d'identifier l'utilisateur"
        )

    try:
        # Conversion du modèle Pydantic en dict pour l'API
        # Exclure user_id et month du payload provider (user_id n'existe plus, month est pour DB uniquement)
        logger.info(f"📝 Génération Lunar Return Report - user_id: {user_id}, month: {request.month}")

        # === CACHE DB CHECK (Performance Optimization) ===
        # Vérifier d'abord si un rapport existe en DB pour éviter l'appel RapidAPI (2-3s)
        existing_report = None
        if request.month:
            try:
                stmt = select(LunarReport).where(
                    and_(
                        LunarReport.user_id == user_id,
                        LunarReport.month == request.month
                    )
                )
                result_db = await db.execute(stmt)
                existing_report = result_db.scalar_one_or_none()

                if existing_report:
                    # Cache TTL: 30 jours (rapports lunaires valides 1 mois)
                    from datetime import datetime, timedelta, timezone
                    cache_age = datetime.now(timezone.utc) - existing_report.created_at
                    cache_ttl_days = 30

                    if cache_age.days < cache_ttl_days:
                        # Cache hit: retourner le rapport existant sans appel API
                        logger.info(
                            f"⚡ Cache hit - user_id: {user_id}, month: {request.month}, "
                            f"age: {cache_age.days}j/{cache_ttl_days}j"
                        )
                        return {
                            "provider": "cache",
                            "report": existing_report.report,
                            "cached_at": existing_report.created_at.isoformat(),
                            "cache_age_days": cache_age.days
                        }
                    else:
                        # Cache expiré: on va regénérer
                        logger.info(
                            f"🔄 Cache expired - user_id: {user_id}, month: {request.month}, "
                            f"age: {cache_age.days}j > {cache_ttl_days}j"
                        )
            except Exception as e:
                logger.warning(f"⚠️  Erreur cache check: {str(e)}, fallback to API call")

        # === APPEL RAPIDAPI (si cache miss ou expired) ===
        payload = request.model_dump(exclude_none=True, exclude={"month"})
        if request.month:
            payload["month"] = request.month

        result = await lunar_services.get_lunar_return_report(payload)

        # Détecter si la réponse est un mock (pour mettre le bon provider)
        is_mock = result.get("_mock", False)
        provider = "mock" if is_mock else "rapidapi"

        # Sauvegarde en DB si month fourni
        # security: never trust request.user_id - always use authenticated user_id snapshot
        if request.month:
            try:
                if existing_report:
                    # Mise à jour du rapport existant (cache refresh)
                    existing_report.report = result
                    logger.info(f"♻️  Cache refresh - user_id: {user_id}, month: {request.month}")
                else:
                    # Création d'un nouveau rapport
                    lunar_report = LunarReport(
                        user_id=user_id,  # security: never trust request.user_id
                        month=request.month,
                        report=result
                    )
                    db.add(lunar_report)
                    logger.info(f"💾 Nouveau rapport sauvegardé - user_id: {user_id}, month: {request.month}")

                # FIX: flush avant commit pour détecter les erreurs de contrainte AVANT commit
                await db.flush()
                await db.commit()

            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde DB: {str(e)}")
                # FIX: rollback explicite pour libérer proprement la session
                try:
                    await db.rollback()
                except Exception:
                    pass  # Si rollback échoue, on ignore (session peut être déjà fermée)
                # On continue malgré l'erreur DB, on retourne quand même les données

        return LunarResponse(
            provider=provider,
            kind="lunar_return_report",
            data=result,
            cached=False
        )

    except HTTPException:
        # Re-raise HTTPExceptions (from rapidapi_client or transformation)
        # They already have proper status codes and error details
        raise

    except ValueError as e:
        # Payload transformation errors (missing fields, invalid format)
        logger.error(f"❌ Payload invalide: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail={
                "code": "INVALID_PAYLOAD",
                "message": str(e),
                "hint": "Vérifiez que birth_date (YYYY-MM-DD), birth_time (HH:MM), latitude, et longitude sont fournis"
            }
        )

    except Exception as e:
        # Unexpected errors
        logger.error(f"❌ Erreur inattendue lors de la génération du Lunar Return Report: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail={
                "code": "INTERNAL_ERROR",
                "message": "Erreur interne du serveur",
                "details": str(e)
            }
        )


@router.post("/voc", response_model=LunarResponse, status_code=200)
async def void_of_course(
    request: VoidOfCourseRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Obtient les informations Void of Course (VoC) de la Lune.

    Le VoC représente la période où la Lune ne fait plus d'aspects majeurs
    avant de changer de signe - considérée comme peu propice aux initiatives.

    - **date**: Date à vérifier (YYYY-MM-DD)
    - **time**: Heure (HH:MM)
    - **coords**: Latitude/longitude pour calcul précis

    Raises:
        HTTPException:
            - 422 si payload invalide (champs manquants ou mauvais format)
            - 502 si erreur provider RapidAPI
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)

        logger.info(f"🌑 Vérification Void of Course - date: {request.date}")

        # Appel au service RapidAPI (avec transformation du payload)
        result = await lunar_services.get_void_of_course_status(payload)

        # Détecter si la réponse est un mock (pour mettre le bon provider)
        is_mock = result.get("_mock", False)
        provider = "mock" if is_mock else "rapidapi"

        # Option: Sauvegarder les fenêtres VoC actives en DB (avec anti-doublons)
        # (uniquement si le provider retourne start_at/end_at)
        if "void_of_course" in result and isinstance(result["void_of_course"], dict):
            voc_data = result["void_of_course"]

            # Vérifier si des fenêtres sont présentes
            if "start" in voc_data and "end" in voc_data:
                try:
                    start_at = datetime.fromisoformat(voc_data["start"])
                    end_at = datetime.fromisoformat(voc_data["end"])

                    # Sauvegarder avec protection anti-doublons et retry logic
                    await voc_cache_service.save_voc_window_safe(
                        db=db,
                        start_at=start_at,
                        end_at=end_at,
                        source=result
                    )

                except Exception as e:
                    logger.warning(f"⚠️  Impossible de sauvegarder la fenêtre VoC: {str(e)}")

        return LunarResponse(
            provider=provider,
            kind="void_of_course",
            data=result,
            cached=False
        )

    except HTTPException:
        # Re-raise HTTPExceptions (from rapidapi_client or transformation)
        # They already have proper status codes and error details
        raise

    except ValueError as e:
        # Payload transformation errors (missing fields, invalid format)
        logger.error(f"❌ Payload invalide pour VoC: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail={
                "code": "INVALID_PAYLOAD",
                "message": str(e),
                "hint": "Vérifiez que date (YYYY-MM-DD), time (HH:MM), latitude, et longitude sont fournis"
            }
        )

    except Exception as e:
        # Unexpected errors (NOT database errors - those are logged but don't block response)
        logger.error(f"❌ Erreur inattendue lors du calcul du Void of Course: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "code": "INTERNAL_ERROR",
                "message": "Erreur interne du serveur",
                "details": str(e)
            }
        )


@router.post("/mansion", status_code=200)
async def lunar_mansion(
    request: LunarMansionRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Obtient les informations sur la mansion lunaire du jour.

    Les 28 mansions lunaires sont un système ancien divisant l'orbite lunaire
    en 28 segments, chacun ayant sa propre signification et influence.

    - **date**: Date à vérifier (YYYY-MM-DD)
    - **coords**: Latitude/longitude pour calcul précis
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)

        logger.info(f"🏰 Calcul Lunar Mansion - date: {request.date}")

        # Appel au service RapidAPI
        result = await lunar_services.get_lunar_mansions(payload)

        # Détecter si la réponse est un mock (pour mettre le bon provider)
        is_mock = result.get("_mock", False)
        provider = "mock" if is_mock else "rapidapi"

        # Dédupliquer upcoming_changes et calendar_summary.significant_periods
        result = _deduplicate_mansion_response(result)

        # P0-1 FIX: Vérifier mansion_id AVANT de tenter la sauvegarde DB
        mansion_data = result.get("mansion", {})
        mansion_id = mansion_data.get("number") if isinstance(mansion_data, dict) else None

        # Si mansion_id manquant => 503 Service Unavailable (provider data incomplete)
        if mansion_id is None:
            # Log debug: clés présentes dans raw response pour debug
            from fastapi.responses import JSONResponse
            raw_keys = list(result.keys())
            mansion_keys = list(mansion_data.keys()) if isinstance(mansion_data, dict) else []
            logger.warning(
                f"⚠️  mansion_id=None | raw_response_keys={raw_keys} | "
                f"mansion_keys={mansion_keys} | provider data incomplete"
            )

            return JSONResponse(
                status_code=503,
                content={
                    "status": "unavailable",
                    "reason": "missing_mansion_id",
                    "date": request.date,
                    "provider": "rapidapi",
                    "message": "Lunar Mansion data temporarily unavailable (provider returned incomplete data)",
                    "data": result  # Retourner les données partielles pour debug
                }
            )

        # mansion_id présent => on peut sauvegarder en DB
        if request.date:
            try:
                target_date = date.fromisoformat(request.date)

                # Upsert: vérifier si existe déjà pour cette date
                stmt = select(LunarMansionDaily).where(LunarMansionDaily.date == target_date)
                result_db = await db.execute(stmt)
                existing_mansion = result_db.scalar_one_or_none()

                if existing_mansion:
                    # Mise à jour
                    existing_mansion.mansion_id = mansion_id
                    existing_mansion.data = result
                else:
                    # Création
                    mansion_entry = LunarMansionDaily(
                        date=target_date,
                        mansion_id=mansion_id,
                        data=result
                    )
                    db.add(mansion_entry)

                # FIX: flush avant commit pour détecter les erreurs de contrainte AVANT commit
                await db.flush()
                await db.commit()

                if existing_mansion:
                    logger.info(f"♻️  Mansion #{mansion_id} mise à jour pour {target_date}")
                else:
                    logger.info(f"💾 Mansion #{mansion_id} sauvegardée pour {target_date}")

            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde DB mansion: {str(e)}")
                # FIX: rollback explicite pour libérer proprement la session
                try:
                    await db.rollback()
                except Exception:
                    pass  # Si rollback échoue, on ignore (session peut être déjà fermée)
                # Continue malgré erreur DB, on retourne quand même les données

        return LunarResponse(
            provider=provider,
            kind="lunar_mansion",
            data=result,
            cached=False
        )

    except HTTPException:
        # Re-raise HTTPExceptions (from rapidapi_client or transformation)
        # They already have proper status codes and error details
        raise

    except ValueError as e:
        # Payload transformation errors (missing fields, invalid format)
        logger.error(f"❌ Payload invalide pour Lunar Mansion: {str(e)}")
        raise HTTPException(
            status_code=422,
            detail={
                "code": "INVALID_PAYLOAD",
                "message": str(e),
                "hint": "Vérifiez que date (YYYY-MM-DD), time (HH:MM), latitude, et longitude sont fournis"
            }
        )

    except Exception as e:
        # Unexpected errors
        logger.error(f"❌ Erreur inattendue lors du calcul de la Lunar Mansion: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail={
                "code": "INTERNAL_ERROR",
                "message": "Erreur interne du serveur",
                "details": str(e)
            }
        )


@router.post("/interpretation/regenerate", status_code=201)
async def regenerate_lunar_interpretation(
    request: Dict[str, Any],
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Force la régénération d'une interprétation lunaire

    Args:
        request: Body JSON avec lunar_return_id et subject (optionnel)

    Returns:
        Nouvelle interprétation générée avec metadata complètes

    Raises:
        404: Si lunar_return_id inexistant ou non accessible
        403: Si l'utilisateur n'a pas les permissions

    **Cas d'usage**:
    - Amélioration du prompt (nouvelle version model)
    - Utilisateur insatisfait de la qualité
    - Debug/test génération Claude

    **Comportement**:
    - Ignore cache DB temporelle
    - Force appel Claude Opus 4.5 (ou fallback templates si échec)
    - Sauvegarde nouvelle version en DB
    - Ancienne version reste en historique

    **Rate limiting**:
    - Recommandé : max 10 regenerates/jour par user (à implémenter si nécessaire)
    """
    from services.lunar_interpretation_generator import generate_or_get_interpretation
    from models.lunar_return import LunarReturn

    lunar_return_id = request.get("lunar_return_id")
    subject = request.get("subject", "full")

    if not lunar_return_id:
        raise HTTPException(status_code=422, detail="lunar_return_id is required")

    logger.info(
        f"Force regenerate requested by user {current_user.id} for lunar_return {lunar_return_id}",
        extra={'user_id': current_user.id, 'lunar_return_id': lunar_return_id, 'subject': subject}
    )

    # Vérifier que lunar_return existe et appartient à l'utilisateur
    lunar_return = await db.get(LunarReturn, lunar_return_id)

    if not lunar_return:
        raise HTTPException(status_code=404, detail="LunarReturn not found")

    if lunar_return.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="You don't have permission to regenerate this interpretation"
        )

    # Forcer régénération (ignore cache DB temporelle)
    try:
        output, weekly, source, model = await generate_or_get_interpretation(
            db=db,
            lunar_return_id=lunar_return_id,
            user_id=current_user.id,
            subject=subject,
            force_regenerate=True  # KEY: Force regeneration
        )
    except Exception as e:
        logger.error(
            f"Failed to regenerate interpretation: {e}",
            extra={'lunar_return_id': lunar_return_id, 'error': str(e)}
        )
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

    logger.info(
        f"Interpretation regenerated successfully",
        extra={
            'lunar_return_id': lunar_return_id,
            'source': source,
            'model': model
        }
    )

    return {
        'interpretation': output,
        'weekly_advice': weekly,
        'metadata': {
            'source': source,
            'model_used': model,
            'subject': subject,
            'regenerated_at': datetime.utcnow().isoformat(),
            'forced': True
        }
    }


# Endpoints bonus: récupérer depuis la DB (cache)

@router.get("/return/report/history/{user_id}", response_model=list[Dict[str, Any]])
async def get_user_lunar_reports(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    """
    Récupère l'historique des rapports lunaires d'un utilisateur.
    """
    try:
        stmt = select(LunarReport).where(LunarReport.user_id == user_id).order_by(LunarReport.month.desc())
        result = await db.execute(stmt)
        reports = result.scalars().all()
        
        return [
            {
                "month": r.month,
                "report": r.report,
                "created_at": r.created_at.isoformat()
            }
            for r in reports
        ]
        
    except Exception as e:
        logger.error(f"❌ Erreur récupération historique: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/voc/current", response_model=Dict[str, Any])
async def get_current_voc_status(db: AsyncSession = Depends(get_db)):
    """
    Vérifie s'il y a une fenêtre VoC active actuellement avec cache (TTL: 1 min).

    Optimisations:
    - Cache en mémoire (1 minute)
    - Retry logic pour requêtes DB
    - Fallback sur cache expiré en cas d'erreur DB
    """
    try:
        return await voc_cache_service.get_current_voc_cached(db)

    except Exception as e:
        logger.error(f"❌ Erreur vérification VoC actif: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/mansion/today", response_model=Dict[str, Any])
async def get_today_mansion(db: AsyncSession = Depends(get_db)):
    """
    Récupère la mansion lunaire du jour depuis le cache.
    """
    try:
        today = date.today()
        
        stmt = select(LunarMansionDaily).where(LunarMansionDaily.date == today)
        result = await db.execute(stmt)
        mansion = result.scalar_one_or_none()
        
        if mansion:
            return {
                "date": mansion.date.isoformat(),
                "mansion_id": mansion.mansion_id,
                "data": mansion.data,
                "cached": True
            }
        else:
            return {
                "message": "Aucune mansion en cache pour aujourd'hui. Utilisez POST /api/lunar/mansion."
            }
            
    except Exception as e:
        logger.error(f"❌ Erreur récupération mansion du jour: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/voc/next_window", response_model=Dict[str, Any])
async def get_next_voc_window():
    """
    Récupère la prochaine fenêtre Void of Course depuis la DB.

    Utile pour planifier des notifications et alertes.
    """
    try:
        from services.scheduler_services import get_next_voc_window

        next_voc = await get_next_voc_window()

        if next_voc:
            return next_voc
        else:
            return {
                "message": "Aucune fenêtre VoC à venir dans la base de données."
            }

    except Exception as e:
        logger.error(f"❌ Erreur récupération next VoC window: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/voc/cache_stats", response_model=Dict[str, Any])
async def get_voc_cache_stats():
    """
    Retourne les statistiques des caches VoC (pour monitoring et debug).

    Utile pour:
    - Vérifier que le cache fonctionne correctement
    - Monitorer la performance
    - Debugging en cas de problème
    """
    try:
        return voc_cache_service.get_cache_stats()

    except Exception as e:
        logger.error(f"❌ Erreur récupération cache stats: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/voc/status", response_model=Dict[str, Any])
async def get_voc_status(db: AsyncSession = Depends(get_db)):
    """
    Endpoint unifié pour l'écran VoC MVP (Phase 1.3) avec cache optimisé.

    Retourne :
    - now : fenêtre VoC active maintenant (ou null)
    - next : prochaine fenêtre VoC à venir
    - upcoming : liste 2-3 prochaines fenêtres (24-48h)

    Optimisations:
    - Cache en mémoire (TTL: 2 minutes)
    - Retry logic pour requêtes DB (3 retries avec exponential backoff)
    - Requêtes DB parallélisées (current, next, upcoming en parallèle)
    - Fallback sur cache expiré en cas d'erreur DB
    """
    try:
        return await voc_cache_service.get_voc_status_cached(db)

    except Exception as e:
        logger.error(f"❌ Erreur récupération VoC status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/interpretation/metadata", response_model=Dict[str, Any])
async def get_interpretation_metadata(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Récupère les statistiques d'utilisation des interprétations lunaires pour l'utilisateur.

    Retourne :
    - total_interpretations : Nombre total d'interprétations générées
    - models_used : Répartition par modèle (count + percentage)
    - cached_rate : Taux d'utilisation du cache (%)
    - last_generated : Date de la dernière génération

    **Authentification requise** : Bearer token ou DEV_AUTH_BYPASS

    Cache : 10 minutes (600s)

    Optimisations :
    - Requêtes SQL groupées et optimisées
    - Cache en mémoire par user_id
    - Indexes utilisés : user_id, created_at, model_used

    Raises:
        HTTPException:
            - 401 si non authentifié
            - 500 si erreur serveur
    """
    global _METADATA_CACHE

    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    if not current_user or not hasattr(current_user, 'id') or current_user.id is None:
        logger.error("❌ Authentification invalide: current_user ou current_user.id manquant")
        raise HTTPException(
            status_code=401,
            detail="Authentification invalide: utilisateur non identifié"
        )

    try:
        user_id = int(current_user.id)
    except (ValueError, TypeError, AttributeError) as e:
        logger.error(f"❌ Erreur extraction user_id: {e}, current_user={current_user}")
        raise HTTPException(
            status_code=401,
            detail="Authentification invalide: impossible d'identifier l'utilisateur"
        )

    # === CACHE CHECK ===
    current_time = time.time()
    if user_id in _METADATA_CACHE:
        cached_data, timestamp = _METADATA_CACHE[user_id]
        cache_age = current_time - timestamp

        if cache_age < METADATA_CACHE_TTL:
            logger.debug(f"[Metadata] ✅ Cache hit for user {user_id} (age: {int(cache_age)}s)")
            return {**cached_data, "cached": True, "cache_age_seconds": int(cache_age)}

    # === CACHE MISS - CALCULATE METADATA ===
    logger.debug(f"[Metadata] 🔄 Cache miss for user {user_id}, calculating...")

    try:
        from models.lunar_interpretation import LunarInterpretation

        # 1. Total interpretations
        total_stmt = select(func.count(LunarInterpretation.id)).where(
            LunarInterpretation.user_id == user_id
        )
        total_result = await db.execute(total_stmt)
        total_interpretations = total_result.scalar() or 0

        # 2. Models used distribution
        models_stmt = select(
            LunarInterpretation.model_used,
            func.count(LunarInterpretation.id).label('count')
        ).where(
            LunarInterpretation.user_id == user_id
        ).group_by(
            LunarInterpretation.model_used
        ).order_by(
            func.count(LunarInterpretation.id).desc()
        )
        models_result = await db.execute(models_stmt)
        models_data = models_result.all()

        models_used = []
        for model, count in models_data:
            percentage = (count / total_interpretations * 100) if total_interpretations > 0 else 0
            models_used.append({
                "model": model or "unknown",
                "count": count,
                "percentage": round(percentage, 2)
            })

        # 3. Cached rate (heuristic: interpretations created in last hour are "new")
        one_hour_ago = datetime.now(timezone.utc) - timedelta(hours=1)
        new_stmt = select(func.count(LunarInterpretation.id)).where(
            and_(
                LunarInterpretation.user_id == user_id,
                LunarInterpretation.created_at >= one_hour_ago
            )
        )
        new_result = await db.execute(new_stmt)
        new_count = new_result.scalar() or 0

        cached_count = total_interpretations - new_count
        cached_rate = (cached_count / total_interpretations * 100) if total_interpretations > 0 else 0

        # 4. Last generated
        last_stmt = select(func.max(LunarInterpretation.created_at)).where(
            LunarInterpretation.user_id == user_id
        )
        last_result = await db.execute(last_stmt)
        last_generated = last_result.scalar()

        # Build response
        metadata = {
            "total_interpretations": total_interpretations,
            "models_used": models_used,
            "cached_rate": round(cached_rate, 2),
            "last_generated": last_generated.isoformat() if last_generated else None
        }

        # Update cache
        _METADATA_CACHE[user_id] = (metadata, current_time)
        logger.info(
            f"[Metadata] 💾 Metadata calculated for user {user_id}: "
            f"{total_interpretations} interpretations, "
            f"{len(models_used)} models, "
            f"{cached_rate:.1f}% cached"
        )

        return {**metadata, "cached": False}

    except Exception as e:
        logger.error(
            f"[Metadata] ❌ Error calculating metadata for user {user_id}: {str(e)}",
            exc_info=True
        )
        raise HTTPException(
            status_code=500,
            detail={
                "code": "INTERNAL_ERROR",
                "message": "Erreur lors du calcul des statistiques",
                "details": str(e)
            }
        )

