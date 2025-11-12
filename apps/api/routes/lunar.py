"""
Routes FastAPI pour le Luna Pack (P1)
Endpoints pour Lunar Return Report, Void of Course, et Lunar Mansions
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Dict, Any
from datetime import datetime, date
import logging

from database import get_db
from services import lunar_services
from schemas.lunar import (
    LunarReturnReportRequest, 
    VoidOfCourseRequest, 
    LunarMansionRequest,
    LunarResponse
)
from models.lunar_pack import LunarReport, LunarVocWindow, LunarMansionDaily

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/lunar", tags=["Luna Pack"])


@router.post("/return/report", response_model=LunarResponse, status_code=200)
async def lunar_return_report(
    request: LunarReturnReportRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Génère un rapport mensuel de révolution lunaire.
    
    Le rapport contient l'analyse complète de la position de retour de la Lune
    et ses implications pour le mois à venir.
    
    - **user_id**: (Optionnel) ID utilisateur pour sauvegarder en base
    - **month**: (Optionnel) Format YYYY-MM pour indexation
    - **payload**: Données requises par RapidAPI (date, coords, etc.)
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)
        
        logger.info(f"📝 Génération Lunar Return Report - user: {request.user_id}, month: {request.month}")
        
        # Appel au service RapidAPI
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
        
    except Exception as e:
        logger.error(f"❌ Erreur lors de la génération du Lunar Return Report: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
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
    """
    try:
        # Conversion du modèle Pydantic en dict pour l'API
        payload = request.model_dump(exclude_none=True)
        
        logger.info(f"🌑 Vérification Void of Course - date: {request.date}")
        
        # Appel au service RapidAPI
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
        
    except Exception as e:
        logger.error(f"❌ Erreur lors du calcul du Void of Course: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.post("/mansion", response_model=LunarResponse, status_code=200)
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
        
        # Option: Sauvegarder la mansion du jour en DB
        if request.date and "mansion" in result:
            try:
                mansion_data = result["mansion"]
                mansion_id = mansion_data.get("number", 0)
                target_date = date.fromisoformat(request.date)
                
                # Upsert: vérifier si existe déjà pour cette date
                stmt = select(LunarMansionDaily).where(LunarMansionDaily.date == target_date)
                existing = await db.execute(stmt)
                existing_mansion = existing.scalar_one_or_none()
                
                if existing_mansion:
                    # Mise à jour
                    existing_mansion.mansion_id = mansion_id
                    existing_mansion.data = result
                    logger.info(f"♻️  Mansion existante mise à jour pour {target_date}")
                else:
                    # Création
                    mansion_entry = LunarMansionDaily(
                        date=target_date,
                        mansion_id=mansion_id,
                        data=result
                    )
                    db.add(mansion_entry)
                    logger.info(f"💾 Nouvelle mansion sauvegardée pour {target_date}")
                
                await db.commit()
                
            except Exception as e:
                logger.warning(f"⚠️  Impossible de sauvegarder la mansion: {str(e)}")
                await db.rollback()
        
        return LunarResponse(
            provider="rapidapi",
            kind="lunar_mansion",
            data=result,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur lors du calcul de la Lunar Mansion: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
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

