"""
Configuration pytest pour les tests API
Utilise une base SQLite en mémoire pour éviter les problèmes de permissions
"""

import pytest
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool
from httpx import AsyncClient
from passlib.context import CryptContext

# PATCH: Remplacer JSONB/UUID par types compatibles SQLite
from sqlalchemy import JSON, String
from sqlalchemy.dialects import postgresql
# Remplacer la classe JSONB par JSON et UUID par String
postgresql.JSONB = JSON
postgresql.UUID = lambda *args, **kwargs: String(36)

from database import Base, get_db
from main import app
from models.user import User


# Configuration de la base de données de test (SQLite temporaire)
import os
import tempfile

# Utiliser un fichier temporaire dans /tmp/claude/ (autorisé par sandbox)
TEST_DB_PATH = "/tmp/claude/test_astroia.db"
os.makedirs("/tmp/claude", exist_ok=True)

# Supprimer le fichier de test s'il existe déjà
if os.path.exists(TEST_DB_PATH):
    try:
        os.remove(TEST_DB_PATH)
    except Exception:
        pass

TEST_DATABASE_URL = f"sqlite+aiosqlite:///{TEST_DB_PATH}"

# Engine de test avec NullPool pour isolation complète
test_engine = create_async_engine(
    TEST_DATABASE_URL,
    poolclass=NullPool,
    echo=False,  # Mettre True pour debug SQL
)

# Session factory pour les tests
TestSessionLocal = async_sessionmaker(
    test_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# Context pour hasher les passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@pytest.fixture()
async def setup_test_db():
    """
    Fixture qui crée la DB de test pour les tests qui en ont besoin.
    Ne s'exécute plus automatiquement (autouse=False).

    Usage: ajouter 'setup_test_db' aux paramètres des tests qui utilisent la DB.
    """
    # Supprimer le fichier de test s'il existe pour garantir un état propre
    if os.path.exists(TEST_DB_PATH):
        try:
            os.remove(TEST_DB_PATH)
        except Exception:
            pass

    # Créer toutes les tables
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Créer des users de test par défaut (pour DEV_AUTH_BYPASS)
    async with TestSessionLocal() as session:
        try:
            from datetime import datetime
            now = datetime.utcnow()
            # Créer users avec ID 1-10 pour les tests
            for user_id in range(1, 11):
                user = User(
                    id=user_id,
                    email=f"test{user_id}@test.com",
                    hashed_password=pwd_context.hash("testpass"),
                    birth_date="1990-01-01",
                    birth_time="12:00",
                    birth_latitude="48.8566",
                    birth_longitude="2.3522",
                    birth_place_name="Paris, France",
                    birth_timezone="Europe/Paris",
                    created_at=now  # Fournir explicitement pour SQLite
                )
                session.add(user)
            await session.commit()
        except Exception as e:
            print(f"Warning: Could not create test users: {e}")
            await session.rollback()

    yield  # Le test s'exécute ici

    # Nettoyer toutes les tables après le test
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    # Supprimer le fichier de test
    if os.path.exists(TEST_DB_PATH):
        try:
            os.remove(TEST_DB_PATH)
        except Exception:
            pass  # Ignorer les erreurs de suppression


async def override_get_db():
    """
    Override de la dépendance get_db pour utiliser la DB de test
    """
    async with TestSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


# Override de la dépendance get_db dans l'app FastAPI
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
async def test_client(setup_test_db):
    """
    Fixture qui fournit un client HTTP de test
    Utilise automatiquement la DB de test via l'override
    Dépend de setup_test_db pour avoir une DB propre
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.fixture
async def test_db(setup_test_db):
    """
    Fixture qui fournit une session DB de test directement
    Utile pour les tests qui ont besoin de manipuler la DB directement
    Dépend de setup_test_db pour avoir une DB propre
    """
    async with TestSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
