"""
Configuration SQLAlchemy (async)
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool
from sqlalchemy import JSON
from sqlalchemy.dialects import postgresql
from config import settings
import os
import sys

# Convertir postgresql:// en postgresql+asyncpg://
DATABASE_URL = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Log pour debug (masquer le mot de passe)
import logging
from urllib.parse import urlparse
logger = logging.getLogger(__name__)
parsed = urlparse(settings.DATABASE_URL)
logger.info(f"🔗 Database URL: postgresql://{parsed.username}:***@{parsed.hostname}:{parsed.port}{parsed.path}")
logger.info(f"🔗 Database host: {parsed.hostname}")
logger.info(f"🔗 Database port: {parsed.port}")

# Détection environnement test: APP_ENV == "test" OU pytest est importé
# Utilise sys.modules pour détecter pytest de manière fiable à l'import
IS_PYTEST = "pytest" in sys.modules
IS_TEST_ENV = os.getenv("APP_ENV", "").lower() == "test" or IS_PYTEST

# Engine async
# En test: NullPool pour éviter les problèmes de pool/isolement DB
# En prod/dev: pool normal
engine_kwargs = {
    "echo": True if settings.APP_ENV == "development" else False
}
if IS_TEST_ENV:
    engine_kwargs["poolclass"] = NullPool
else:
    engine_kwargs["pool_size"] = settings.DATABASE_POOL_SIZE
    engine_kwargs["max_overflow"] = settings.DATABASE_MAX_OVERFLOW

engine = create_async_engine(DATABASE_URL, **engine_kwargs)

# Session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class Base(DeclarativeBase):
    """Base pour tous les modèles SQLAlchemy"""
    pass


# Helper pour type JSON compatible multi-dialectes
# PostgreSQL: utilise JSONB (meilleur performance)
# SQLite: utilise JSON
def JSONBColumn(*args, **kwargs):
    """
    Retourne JSONB pour PostgreSQL, JSON pour autres dialectes (ex: SQLite en test)
    Usage: data = JSONBColumn(nullable=False) au lieu de Column(JSONB, nullable=False)
    """
    # Déterminer le dialecte depuis l'URL
    if "postgresql" in DATABASE_URL:
        return postgresql.JSONB(*args, **kwargs)
    else:
        return JSON(*args, **kwargs)


async def get_db():
    """Dependency pour récupérer une session DB"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

