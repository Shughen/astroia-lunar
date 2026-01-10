"""
Routes FastAPI pour les Rapports (P5)
Endpoints pour génération de rapports mensuels HTML/PDF
"""

from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from typing import Dict, Any
import logging

from database import get_db
from services import reporting
from models.lunar_pack import LunarReport
from models.transits import TransitsOverview
from models.calendar import LunarEvent

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/reports", tags=["Reports"])


@router.post("/lunar/{user_id}/{month}")
async def generate_lunar_monthly_report(
    user_id: int,
    month: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Génère un rapport mensuel complet combinant:
    - Rapport de révolution lunaire
    - Transits du mois
    - Événements lunaires
    
    Retourne le HTML du rapport (et optionnellement l'URL du PDF).
    
    - **user_id**: ID de l'utilisateur
    - **month**: Mois au format YYYY-MM
    """
    try:
        logger.info(f"📝 Génération rapport mensuel pour user {user_id}, mois {month}")
        
        # Récupérer le rapport lunaire depuis la DB
        stmt_lr = select(LunarReport).where(
            and_(
                LunarReport.user_id == user_id,
                LunarReport.month == month
            )
        )
        result_lr = await db.execute(stmt_lr)
        lr_record = result_lr.scalar_one_or_none()
        lr_data = lr_record.report if lr_record else None
        
        # Récupérer les transits depuis la DB
        stmt_transits = select(TransitsOverview).where(
            and_(
                TransitsOverview.user_id == user_id,
                TransitsOverview.month == month
            )
        )
        result_transits = await db.execute(stmt_transits)
        transits_record = result_transits.scalar_one_or_none()
        transits_data = transits_record.overview if transits_record else None
        
        # Récupérer les événements lunaires du mois
        # Extraire année et mois
        year, month_num = int(month[:4]), int(month[5:7])
        from datetime import date
        start_date = date(year, month_num, 1)
        if month_num == 12:
            end_date = date(year + 1, 1, 1)
        else:
            end_date = date(year, month_num + 1, 1)
        
        stmt_events = select(LunarEvent).where(
            and_(
                LunarEvent.date >= start_date,
                LunarEvent.date < end_date
            )
        ).order_by(LunarEvent.date)
        result_events = await db.execute(stmt_events)
        events_records = result_events.scalars().all()
        events_data = [
            {
                "date": e.date.isoformat(),
                "title": e.title,
                "type": e.event_type,
                "description": e.description
            }
            for e in events_records
        ]
        
        # Générer le rapport
        report = await reporting.generate_monthly_report(
            user_id=user_id,
            month=month,
            lunar_return_data=lr_data,
            transits_data=transits_data,
            events_data=events_data
        )
        
        return {
            "user_id": user_id,
            "month": month,
            "html": report["html"],
            "pdf_url": report.get("pdf_url"),
            "generated_at": "now"
        }
        
    except Exception as e:
        logger.error(f"❌ Erreur génération rapport: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/lunar/{user_id}/{month}/html", response_class=Response)
async def get_lunar_monthly_report_html(
    user_id: int,
    month: str,
    db: AsyncSession = Depends(get_db)
):
    """
    Retourne le rapport mensuel en HTML pur (pour affichage direct dans un navigateur).
    """
    try:
        # Utiliser la même logique que generate_lunar_monthly_report
        report_data = await generate_lunar_monthly_report(user_id, month, db)
        
        return Response(
            content=report_data["html"],
            media_type="text/html"
        )
        
    except Exception as e:
        logger.error(f"❌ Erreur récupération rapport HTML: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

