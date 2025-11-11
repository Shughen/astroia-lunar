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
from routes import auth, natal, lunar_returns

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
    
    # Créer les tables (en dev uniquement, utiliser Alembic en prod)
    if settings.APP_ENV == "development":
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info("✅ Tables créées (dev mode)")
    
    yield
    
    # Shutdown
    logger.info("👋 Arrêt de l'API...")
    await engine.dispose()


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
    """Detailed health check"""
    return {
        "status": "healthy",
        "database": "connected",
        "ephemeris_api": "configured" if settings.EPHEMERIS_API_KEY else "missing"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.API_RELOAD
    )

