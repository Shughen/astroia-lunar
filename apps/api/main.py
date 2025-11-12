"""
🌙 Astroia Lunar API - Point d'entrée principal
FastAPI backend pour calculs astrologiques et révolutions lunaires
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from config import settings
from database import engine, Base
from routes import auth, natal, lunar_returns, lunar, transits, calendar, reports
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
    # Startup
    logger.info("🚀 Astroia Lunar API démarrage...")
    logger.info(f"📊 Environment: {settings.APP_ENV}")
    logger.info(f"🔗 Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'local'}")
    
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
        await engine.dispose()
    except Exception as e:
        logger.warning(f"Erreur dispose engine: {e}")


# Initialisation FastAPI
app = FastAPI(
    title="Astroia Lunar API",
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
app.include_router(lunar_returns.router, prefix="/api/lunar-returns", tags=["Lunar Returns"])
app.include_router(lunar.router, tags=["Luna Pack"])
app.include_router(transits.router, tags=["Transits"])
app.include_router(calendar.router, tags=["Calendar"])
app.include_router(reports.router, tags=["Reports"])


@app.get("/")
async def root():
    """Health check"""
    return {
        "app": "Astroia Lunar API",
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )

