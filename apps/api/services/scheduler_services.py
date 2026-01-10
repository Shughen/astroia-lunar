"""
Services de planification pour notifications et tâches périodiques (P4)
Utilise APScheduler pour rafraîchir les données VoC et autres tâches récurrentes
"""

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import logging

from services import lunar_services
from database import get_db
from models.lunar_pack import LunarVocWindow

logger = logging.getLogger(__name__)

# Instance du scheduler (singleton)
scheduler = AsyncIOScheduler()


async def refresh_voc_windows():
    """
    Tâche périodique pour rafraîchir les fenêtres Void of Course.
    
    Appelée toutes les 2 heures pour maintenir les données VoC à jour.
    En production, cette tâche devrait être déplacée vers un worker séparé.
    """
    logger.info("🔄 Rafraîchissement automatique des fenêtres VoC...")
    
    try:
        # Calculer les fenêtres VoC pour les 7 prochains jours
        # (logique simplifiée, à adapter selon les besoins réels)
        now = datetime.now()
        end_date = now + timedelta(days=7)
        
        # Payload générique (Paris par défaut)
        payload = {
            "start_date": now.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "latitude": 48.8566,
            "longitude": 2.3522,
            "timezone": "Europe/Paris"
        }
        
        # Appel au service (si l'API provider le supporte)
        # result = await lunar_services.get_void_of_course_status(payload)
        
        # Pour l'instant, log uniquement
        logger.info("✅ Rafraîchissement VoC terminé (placeholder)")
        
    except Exception as e:
        logger.error(f"❌ Erreur lors du rafraîchissement VoC: {str(e)}")


async def get_next_voc_window() -> dict:
    """
    Récupère la prochaine fenêtre VoC depuis la DB.
    
    Returns:
        {
            "start_at": "2025-01-15T10:30:00+01:00",
            "end_at": "2025-01-15T14:45:00+01:00",
            "time_until": "2h 15min"
        }
        ou None si aucune fenêtre trouvée
    """
    try:
        async for db in get_db():
            from sqlalchemy import select
            
            now = datetime.now()
            
            # Chercher la prochaine fenêtre VoC
            stmt = select(LunarVocWindow).where(
                LunarVocWindow.start_at > now
            ).order_by(LunarVocWindow.start_at).limit(1)
            
            result = await db.execute(stmt)
            next_voc = result.scalar_one_or_none()
            
            if next_voc:
                time_until = next_voc.start_at - now
                hours = int(time_until.total_seconds() // 3600)
                minutes = int((time_until.total_seconds() % 3600) // 60)
                
                return {
                    "start_at": next_voc.start_at.isoformat(),
                    "end_at": next_voc.end_at.isoformat(),
                    "time_until": f"{hours}h {minutes}min",
                    "time_until_seconds": int(time_until.total_seconds())
                }
            
            return None
            
    except Exception as e:
        logger.error(f"❌ Erreur récupération next VoC: {str(e)}")
        return None


def start_scheduler():
    """
    Démarre le scheduler avec les tâches périodiques.
    
    IMPORTANT: En production, déplacer vers un worker dédié (Celery, RQ, etc.)
    pour éviter de surcharger le serveur web.
    """
    if not scheduler.running:
        # Tâche: Rafraîchir les fenêtres VoC toutes les 2 heures
        scheduler.add_job(
            refresh_voc_windows,
            trigger='interval',
            hours=2,
            id='refresh_voc',
            name='Rafraîchir fenêtres Void of Course',
            replace_existing=True
        )
        
        scheduler.start()
        logger.info("✅ Scheduler démarré avec tâches périodiques")
    else:
        logger.info("ℹ️  Scheduler déjà en cours d'exécution")


def stop_scheduler():
    """Arrête le scheduler proprement."""
    if scheduler.running:
        scheduler.shutdown(wait=False)
        logger.info("👋 Scheduler arrêté")

