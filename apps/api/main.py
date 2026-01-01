"""
🌙 Lunation API - Point d'entrée principal
FastAPI backend pour calculs astrologiques et révolutions lunaires
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
import uuid

from config import settings
from database import engine, Base
from routes import auth, natal, lunar_returns, lunar, transits, calendar, reports, natal_reading, natal_interpretation
from services import ephemeris_rapidapi

# Configuration logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle events (startup/shutdown)"""
    correlation_id = str(uuid.uuid4())
    
    # Startup
    logger.info(f"[corr={correlation_id}] 🚀 Lunation API démarrage...")
    logger.info(f"[corr={correlation_id}] 📊 Environment: {settings.APP_ENV}")
    logger.info(f"[corr={correlation_id}] 🔗 Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'local'}")
    
    # Schema sanity check au démarrage
    try:
        from database import AsyncSessionLocal
        from utils.schema_sanity_check import check_schema_sanity
        
        async with AsyncSessionLocal() as db:
            is_valid, errors = await check_schema_sanity(db, correlation_id)
            
            if not is_valid:
                error_summary = "\n".join([f"  - {err['message']}" for err in errors])
                error_msg = (
                    f"[corr={correlation_id}] ❌ SCHEMA SANITY CHECK FAILED au démarrage:\n{error_summary}\n"
                    f"Action requise: Exécuter les migrations SQL nécessaires. "
                    f"Voir apps/api/scripts/sql/inspect_core_schema.sql pour diagnostiquer."
                )
                logger.error(error_msg)
                
                # Fail-fast en dev, warn seulement en prod
                if settings.APP_ENV == "development":
                    logger.error(f"[corr={correlation_id}] 🛑 Arrêt du serveur (dev mode fail-fast)")
                    raise RuntimeError(f"Schema sanity check failed: {error_summary}")
            else:
                logger.info(f"[corr={correlation_id}] ✅ Schema sanity check OK au démarrage")
    except RuntimeError:
        # Re-raise RuntimeError (fail-fast en dev)
        raise
    except Exception as e:
        # Pour toute autre erreur (DB indisponible, etc.), on log mais on continue
        logger.warning(
            f"[corr={correlation_id}] ⚠️ Impossible de vérifier le schéma au démarrage: {e}. "
            f"Le serveur continue mais le schéma n'a pas été validé."
        )
    
    # NOTE: Tables créées via Alembic migrations, pas create_all
    # En dev, utiliser : alembic upgrade head
    # if settings.APP_ENV == "development":
    #     async with engine.begin() as conn:
    #         await conn.run_sync(Base.metadata.create_all)
    #     logger.info("✅ Tables créées (dev mode)")
    
    yield
    
    # Shutdown
    logger.info("👋 Arrêt de l'API...")
    
    try:
        await ephemeris_rapidapi.close_client()
    except Exception as e:
        logger.warning(f"Erreur fermeture ephemeris_rapidapi: {e}")
    
    try:
        # Fermeture du client RapidAPI générique
        from services import rapidapi_client
        await rapidapi_client.close_client()
    except Exception as e:
        logger.warning(f"Erreur fermeture rapidapi_client: {e}")
    
    try:
        # Fermeture du client natal_reading_service
        from services import natal_reading_service
        await natal_reading_service.close_client()
    except Exception as e:
        logger.warning(f"Erreur fermeture natal_reading_service: {e}")
    
    try:
        await engine.dispose()
    except Exception as e:
        logger.warning(f"Erreur dispose engine: {e}")


# Initialisation FastAPI
app = FastAPI(
    title="Lunation API",
    description="API pour calculs de révolutions lunaires et thèmes natals",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS (à restreindre en production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.APP_ENV == "development" else [settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(natal.router, prefix="/api", tags=["Natal Chart"])
app.include_router(natal_reading.router, prefix="/api/natal", tags=["Natal Reading"])
app.include_router(natal_interpretation.router, prefix="/api/natal", tags=["Natal Interpretation"])
app.include_router(lunar_returns.router, prefix="/api/lunar-returns", tags=["Lunar Returns"])
app.include_router(lunar.router, tags=["Luna Pack"])
app.include_router(transits.router, tags=["Transits"])
app.include_router(calendar.router, tags=["Calendar"])
app.include_router(reports.router, tags=["Reports"])


@app.get("/")
async def root():
    """Health check"""
    return {
        "app": "Lunation API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """
    Health check détaillé avec vérifications database et RapidAPI.
    Retourne l'état de santé des dépendances critiques.
    """
    health_status = {
        "status": "healthy",
        "checks": {}
    }
    
    # Check 1: Database
    try:
        # Test simple de configuration (pas de requête SQL pour éviter greenlet)
        from database import engine
        if engine:
            health_status["checks"]["database"] = "configured"
        else:
            health_status["checks"]["database"] = "not_configured"
            health_status["status"] = "degraded"
    except Exception as e:
        logger.error(f"Health check database failed: {str(e)}")
        health_status["checks"]["database"] = f"error: {str(e)[:50]}"
        health_status["status"] = "degraded"
    
    # Check 2: RapidAPI configuration
    if settings.RAPIDAPI_KEY and settings.RAPIDAPI_KEY != "":
        health_status["checks"]["rapidapi_config"] = "configured"
    else:
        health_status["checks"]["rapidapi_config"] = "missing_key"
        health_status["status"] = "degraded"
    
    # Check 3: RapidAPI ping (HEAD ou GET simple) - optionnel en mode dev
    # Pour éviter de consommer des crédits API, on fait un simple check de config
    # En production, on pourrait faire un vrai ping si l'API provider le permet
    
    return health_status


@app.get("/health/db")
async def health_check_db():
    """
    Health check spécifique pour la base de données avec vérification du schéma.
    Vérifie que les types de colonnes critiques (id, user_id) correspondent aux attentes.
    """
    correlation_id = str(uuid.uuid4())
    
    health_status = {
        "status": "healthy",
        "correlation_id": correlation_id,
        "checks": {
            "database_connection": "unknown",
            "schema_sanity": "unknown"
        },
        "errors": []
    }
    
    try:
        from database import AsyncSessionLocal
        from utils.schema_sanity_check import check_schema_sanity
        from sqlalchemy import text
        
        async with AsyncSessionLocal() as db:
            # Test de connexion simple
            try:
                await db.execute(text("SELECT 1"))
                health_status["checks"]["database_connection"] = "ok"
            except Exception as e:
                health_status["checks"]["database_connection"] = f"error: {str(e)[:100]}"
                health_status["status"] = "unhealthy"
                health_status["errors"].append(f"Database connection failed: {str(e)}")
                return health_status
            
            # Schema sanity check
            is_valid, errors = await check_schema_sanity(db, correlation_id)
            
            if is_valid:
                health_status["checks"]["schema_sanity"] = "ok"
            else:
                health_status["checks"]["schema_sanity"] = "failed"
                health_status["status"] = "unhealthy"
                health_status["errors"] = [
                    {
                        "table": err["table_name"],
                        "column": err["column_name"],
                        "message": err["message"]
                    }
                    for err in errors
                ]
                
    except Exception as e:
        logger.error(f"[corr={correlation_id}] Health check DB failed: {e}", exc_info=True)
        health_status["status"] = "unhealthy"
        health_status["checks"]["schema_sanity"] = f"error: {str(e)[:100]}"
        health_status["errors"].append(f"Schema check exception: {str(e)}")
    
    return health_status


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )

