"""
Routes FastAPI pour le Calendrier Lunaire (P3)
Endpoints pour phases, événements et calendrier annuel
"""

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
from typing import Dict, Any
from datetime import datetime, date
import logging

from database import get_db
from services import calendar_services
from schemas.calendar import (
    LunarPhasesRequest,
    LunarEventsRequest,
    LunarCalendarYearRequest,
    MonthlyCalendarRequest,
    CalendarResponse,
    MonthlyCalendarResponse
)
from models.calendar import LunarEvent, LunarPhase

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/calendar", tags=["Calendar"])


@router.post("/phases", response_model=CalendarResponse, status_code=200)
async def lunar_phases(
    request: LunarPhasesRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Obtient les phases lunaires précises pour une période donnée.
    
    Retourne les dates et heures exactes des nouvelles lunes, pleines lunes,
    premiers quartiers et derniers quartiers.
    
    - **start_date**: Date de début (YYYY-MM-DD)
    - **end_date**: Date de fin (YYYY-MM-DD)
    """
    try:
        payload = request.model_dump(exclude_none=True)
        
        logger.info(f"🌓 Requête Lunar Phases: {request.start_date} -> {request.end_date}")
        
        # Appel au service RapidAPI
        result = await calendar_services.get_lunar_phases(payload)
        
        # Sauvegarde optionnelle en DB des phases
        # (pour cache et analytics, pas bloquant si échec)
        try:
            if "phases" in result and isinstance(result["phases"], list):
                for phase in result["phases"]:
                    phase_date = date.fromisoformat(phase.get("date", ""))
                    phase_type = phase.get("type", "unknown")
                    
                    # Vérifier si existe déjà
                    stmt = select(LunarPhase).where(
                        and_(
                            LunarPhase.date == phase_date,
                            LunarPhase.phase_type == phase_type
                        )
                    )
                    existing = await db.execute(stmt)
                    if not existing.scalar_one_or_none():
                        lunar_phase = LunarPhase(
                            date=phase_date,
                            time=phase.get("time", "00:00:00"),
                            phase_type=phase_type,
                            illumination=int(phase.get("illumination", 0) * 100),
                            meta=phase
                        )
                        db.add(lunar_phase)
                
                await db.commit()
                logger.info("💾 Phases lunaires sauvegardées en cache")
        except Exception as e:
            logger.warning(f"⚠️  Erreur sauvegarde phases: {str(e)}")
            await db.rollback()
        
        return CalendarResponse(
            provider="rapidapi",
            kind="lunar_phases",
            data=result,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur calcul Lunar Phases: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.post("/events", response_model=CalendarResponse, status_code=200)
async def lunar_events(
    request: LunarEventsRequest,
    db: AsyncSession = Depends(get_db)
):
    """
    Obtient les événements lunaires spéciaux (éclipses, superlunes, etc.).
    
    - **start_date**: Date de début
    - **end_date**: Date de fin
    - **event_types**: (Optionnel) Filtrer par types d'événements
    """
    try:
        payload = request.model_dump(exclude_none=True)
        
        logger.info(f"🌒 Requête Lunar Events: {request.start_date} -> {request.end_date}")
        
        # Appel au service RapidAPI
        result = await calendar_services.get_lunar_events(payload)
        
        # Sauvegarde optionnelle en DB
        try:
            if "events" in result and isinstance(result["events"], list):
                for event in result["events"]:
                    event_date = date.fromisoformat(event.get("date", ""))
                    event_type = event.get("type", "unknown")
                    title = event.get("title", "")
                    
                    # Vérifier si existe déjà
                    stmt = select(LunarEvent).where(
                        and_(
                            LunarEvent.date == event_date,
                            LunarEvent.event_type == event_type,
                            LunarEvent.title == title
                        )
                    )
                    existing = await db.execute(stmt)
                    if not existing.scalar_one_or_none():
                        lunar_event = LunarEvent(
                            date=event_date,
                            time=event.get("time"),
                            event_type=event_type,
                            title=title,
                            description=event.get("description"),
                            meta=event
                        )
                        db.add(lunar_event)
                
                await db.commit()
                logger.info("💾 Événements lunaires sauvegardés en cache")
        except Exception as e:
            logger.warning(f"⚠️  Erreur sauvegarde événements: {str(e)}")
            await db.rollback()
        
        return CalendarResponse(
            provider="rapidapi",
            kind="lunar_events",
            data=result,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur calcul Lunar Events: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.post("/year", response_model=CalendarResponse, status_code=200)
async def lunar_calendar_year(request: LunarCalendarYearRequest):
    """
    Obtient le calendrier lunaire complet pour une année.
    
    Retourne toutes les nouvelles/pleines lunes, éclipses et événements majeurs
    pour l'année entière.
    
    - **year**: Année (ex: 2025)
    """
    try:
        payload = request.model_dump(exclude_none=True, exclude={'year'})
        
        logger.info(f"📅 Requête Lunar Calendar Year: {request.year}")
        
        # Appel au service RapidAPI avec année dans l'URL
        result = await calendar_services.get_lunar_calendar_year(request.year, payload)
        
        return CalendarResponse(
            provider="rapidapi",
            kind="lunar_calendar_year",
            data=result,
            cached=False
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur calcul Lunar Calendar Year: {str(e)}")
        raise HTTPException(
            status_code=502,
            detail=f"Erreur provider RapidAPI: {str(e)}"
        )


@router.get("/month", response_model=MonthlyCalendarResponse)
async def monthly_calendar(
    year: int,
    month: int,
    latitude: float = 48.8566,
    longitude: float = 2.3522,
    timezone: str = "Europe/Paris",
    db: AsyncSession = Depends(get_db)
):
    """
    Génère un calendrier mensuel combiné avec phases, mansions et événements.
    
    Croise les données de plusieurs sources pour créer une vue calendrier unifiée.
    
    - **year**: Année (ex: 2025)
    - **month**: Mois (1-12)
    - **latitude/longitude**: Coordonnées (Paris par défaut)
    """
    try:
        logger.info(f"📆 Génération calendrier mensuel: {year}-{month:02d}")
        
        # Construire les dates de début et fin du mois
        start_date = date(year, month, 1)
        if month == 12:
            end_date = date(year + 1, 1, 1)
        else:
            end_date = date(year, month + 1, 1)
        
        # Récupérer les phases du mois depuis le cache DB
        stmt_phases = select(LunarPhase).where(
            and_(
                LunarPhase.date >= start_date,
                LunarPhase.date < end_date
            )
        )
        result_phases = await db.execute(stmt_phases)
        phases = result_phases.scalars().all()
        
        # Récupérer les événements du mois depuis le cache DB
        stmt_events = select(LunarEvent).where(
            and_(
                LunarEvent.date >= start_date,
                LunarEvent.date < end_date
            )
        )
        result_events = await db.execute(stmt_events)
        events = result_events.scalars().all()
        
        # Générer le calendrier (logique simplifiée)
        # TODO: Améliorer avec fusion complète des données
        days = []
        summary = {
            "new_moons": sum(1 for p in phases if p.phase_type == "new_moon"),
            "full_moons": sum(1 for p in phases if p.phase_type == "full_moon"),
            "eclipses": sum(1 for e in events if "eclipse" in e.event_type),
            "special_events": len(events)
        }
        
        return MonthlyCalendarResponse(
            year=year,
            month=month,
            days=days,
            summary=summary
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur génération calendrier mensuel: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

