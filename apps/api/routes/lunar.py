"""
Routes FastAPI pour le Luna Pack (P1)
Endpoints pour Lunar Return Report, Void of Course, et Lunar Mansions
"""

from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Dict, Any
from datetime import datetime, date
import logging

from database import get_db
from services import lunar_services
from services.moon_position import get_current_moon_position
from services.daily_climate import get_daily_climate
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

    - **user_id**: (Optionnel) ID utilisateur pour sauvegarder en base
    - **month**: (Optionnel) Format YYYY-MM pour indexation
    - **payload**: Données requises par RapidAPI (date, coords, etc.)

    **Authentification requise**: Bearer token ou DEV_AUTH_BYPASS

    Raises:
        HTTPException:
            - 401 si non authentifié
            - 422 si payload invalide (champs manquants ou mauvais format)
            - 502 si erreur provider RapidAPI
    """
    # 🔒 CRITIQUE: Extraire user_id IMMÉDIATEMENT pour éviter MissingGreenlet
    user_id = int(current_user.id)

    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)

        logger.info(f"📝 Génération Lunar Return Report - user: {user_id}, month: {request.month}")

        # Appel au service RapidAPI (avec transformation du payload)
        result = await lunar_services.get_lunar_return_report(payload)

        # Sauvegarde en DB si user_id et month fournis
        if request.user_id and request.month:
            try:
                # Vérifier si un rapport existe déjà pour ce mois
                stmt = select(LunarReport).where(
                    and_(
                        LunarReport.user_id == request.user_id,
                        LunarReport.month == request.month
                    )
                )
                existing = await db.execute(stmt)
                existing_report = existing.scalar_one_or_none()

                if existing_report:
                    # Mise à jour du rapport existant
                    existing_report.report = result
                    logger.info(f"♻️  Rapport existant mis à jour pour {request.month}")
                else:
                    # Création d'un nouveau rapport
                    lunar_report = LunarReport(
                        user_id=request.user_id,
                        month=request.month,
                        report=result
                    )
                    db.add(lunar_report)
                    logger.info(f"💾 Nouveau rapport sauvegardé pour {request.month}")

                await db.commit()

            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde DB: {str(e)}")
                await db.rollback()
                # On continue malgré l'erreur DB, on retourne quand même les données

        return LunarResponse(
            provider="rapidapi",
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
        
        # Option: Sauvegarder les fenêtres VoC actives en DB
        # (uniquement si le provider retourne start_at/end_at)
        if "void_of_course" in result and isinstance(result["void_of_course"], dict):
            voc_data = result["void_of_course"]
            
            # Vérifier si des fenêtres sont présentes
            if "start" in voc_data and "end" in voc_data:
                try:
                    start_at = datetime.fromisoformat(voc_data["start"])
                    end_at = datetime.fromisoformat(voc_data["end"])
                    
                    # Insérer la fenêtre VoC en DB
                    voc_window = LunarVocWindow(
                        start_at=start_at,
                        end_at=end_at,
                        source=result
                    )
                    db.add(voc_window)
                    await db.commit()
                    logger.info(f"💾 Fenêtre VoC sauvegardée: {start_at} -> {end_at}")
                    
                except Exception as e:
                    logger.warning(f"⚠️  Impossible de sauvegarder la fenêtre VoC: {str(e)}")
                    await db.rollback()
        
        return LunarResponse(
            provider="rapidapi",
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
                existing = await db.execute(stmt)
                existing_mansion = existing.scalar_one_or_none()

                if existing_mansion:
                    # Mise à jour
                    existing_mansion.mansion_id = mansion_id
                    existing_mansion.data = result
                    await db.commit()
                    logger.info(f"♻️  Mansion #{mansion_id} mise à jour pour {target_date}")
                else:
                    # Création
                    mansion_entry = LunarMansionDaily(
                        date=target_date,
                        mansion_id=mansion_id,
                        data=result
                    )
                    db.add(mansion_entry)
                    await db.commit()
                    logger.info(f"💾 Mansion #{mansion_id} sauvegardée pour {target_date}")

            except Exception as e:
                logger.error(f"❌ Erreur sauvegarde DB mansion: {str(e)}")
                await db.rollback()
                # Continue malgré erreur DB, on retourne quand même les données

        return LunarResponse(
            provider="rapidapi",
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
    Vérifie s'il y a une fenêtre VoC active actuellement.
    """
    try:
        now = datetime.now()
        
        stmt = select(LunarVocWindow).where(
            and_(
                LunarVocWindow.start_at <= now,
                LunarVocWindow.end_at >= now
            )
        )
        result = await db.execute(stmt)
        active_voc = result.scalar_one_or_none()
        
        if active_voc:
            return {
                "is_active": True,
                "start_at": active_voc.start_at.isoformat(),
                "end_at": active_voc.end_at.isoformat(),
                "source": active_voc.source
            }
        else:
            return {"is_active": False}
            
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


@router.get("/voc/status", response_model=Dict[str, Any])
async def get_voc_status(db: AsyncSession = Depends(get_db)):
    """
    Endpoint unifié pour l'écran VoC MVP (Phase 1.3).

    Retourne :
    - now : fenêtre VoC active maintenant (ou null)
    - next : prochaine fenêtre VoC à venir
    - upcoming : liste 2-3 prochaines fenêtres (24-48h)
    """
    try:
        now = datetime.now()

        # 1. VoC actif maintenant ?
        stmt_current = select(LunarVocWindow).where(
            and_(
                LunarVocWindow.start_at <= now,
                LunarVocWindow.end_at >= now
            )
        )
        result_current = await db.execute(stmt_current)
        active_voc = result_current.scalar_one_or_none()

        current_window = None
        if active_voc:
            current_window = {
                "is_active": True,
                "start_at": active_voc.start_at.isoformat(),
                "end_at": active_voc.end_at.isoformat()
            }

        # 2. Prochaine fenêtre VoC
        stmt_next = select(LunarVocWindow).where(
            LunarVocWindow.start_at > now
        ).order_by(LunarVocWindow.start_at.asc()).limit(1)

        result_next = await db.execute(stmt_next)
        next_voc = result_next.scalar_one_or_none()

        next_window = None
        if next_voc:
            next_window = {
                "start_at": next_voc.start_at.isoformat(),
                "end_at": next_voc.end_at.isoformat()
            }

        # 3. Upcoming (2-3 prochaines fenêtres dans les 48h)
        hours_48 = now + timedelta(hours=48)
        stmt_upcoming = select(LunarVocWindow).where(
            and_(
                LunarVocWindow.start_at > now,
                LunarVocWindow.start_at <= hours_48
            )
        ).order_by(LunarVocWindow.start_at.asc()).limit(3)

        result_upcoming = await db.execute(stmt_upcoming)
        upcoming_vocs = result_upcoming.scalars().all()

        upcoming_windows = [
            {
                "start_at": voc.start_at.isoformat(),
                "end_at": voc.end_at.isoformat()
            }
            for voc in upcoming_vocs
        ]

        return {
            "now": current_window,
            "next": next_window,
            "upcoming": upcoming_windows
        }

    except Exception as e:
        logger.error(f"❌ Erreur récupération VoC status: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

