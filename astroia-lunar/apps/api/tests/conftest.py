"""
Fixtures et helpers pour les tests FastAPI

Fournit:
- FakeAsyncSession: stub DB sans vraie connection
- Fixtures pour override oauth2_scheme, get_current_user, get_db
"""

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, MagicMock
from typing import AsyncGenerator, Optional, Dict, Any
from sqlalchemy.engine.result import Result
from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from models.user import User
from models.natal_chart import NatalChart
from models.lunar_return import LunarReturn
from datetime import datetime, timezone
import asyncio
import time
import threading


# Liste des tests qui nécessitent une isolation complète des connexions DB
_DB_INTENSIVE_TESTS = [
    "test_lunar_current_missinggreenlet",
    "test_lunar_report_userid_security"
]

# Verrou threading global pour forcer l'exécution séquentielle des tests DB intensifs
_db_test_lock = threading.Lock()

def _get_db_test_lock():
    """Récupère le verrou threading pour les tests DB intensifs"""
    return _db_test_lock

def pytest_runtest_setup(item):
    """
    Hook appelé avant chaque test pour forcer un délai entre les tests
    qui utilisent des connexions DB réelles.
    """
    test_file = str(item.fspath)
    # Vérifier si ce test nécessite une isolation complète
    if any(test_name in test_file for test_name in _DB_INTENSIVE_TESTS):
        # Délai très long pour laisser le temps aux connexions et boucles d'événements de se nettoyer
        # et éviter les conflits avec d'autres tests
        time.sleep(1.0)


def pytest_runtest_teardown(item):
    """
    Hook appelé après chaque test pour forcer un délai.
    On évite de nettoyer le pool de connexions car cela peut affecter d'autres tests.
    """
    test_file = str(item.fspath)
    # Vérifier si ce test nécessite une isolation complète
    if any(test_name in test_file for test_name in _DB_INTENSIVE_TESTS):
        # Délai très long pour laisser le temps aux connexions de se fermer proprement
        # et aux boucles d'événements de se nettoyer
        time.sleep(1.0)


# Store global partagé pour les objets persistés (UNIQUEMENT pour tests)
# Permet de partager les données entre FakeAsyncSession sans partager la session
_FAKE_DB_STORAGE = {
    "objects": []  # Liste d'objets committés (partagés entre sessions)
}

class FakeAsyncSession:
    """
    Stub AsyncSession minimal pour les tests.
    Ne crée pas de vraie connection DB (évite greenlet).

    Supporte:
    - execute(query) -> FakeResult
    - scalar_one_or_none() -> objet mocké ou None
    - commit(), rollback(), close()
    - add(), refresh()

    IMPORTANT: Chaque instance est indépendante (pas de session partagée),
    mais les données committées sont persistées dans _FAKE_DB_STORAGE pour
    permettre la persistence entre requêtes HTTP.
    """

    def __init__(self, scenario: Optional[str] = None):
        """
        Args:
            scenario: "natal_exists" | "natal_missing" | None (default: natal_exists)
        """
        self.scenario = scenario or "natal_exists"
        self._added_objects = []  # Objets non-committés (propres à cette session)
        self._committed = False
        
    async def get(self, model_class, object_id):
        """
        Récupère un objet par ID depuis le storage.

        Args:
            model_class: Classe du modèle (ex: LunarReturn)
            object_id: ID de l'objet à récupérer

        Returns:
            Instance de l'objet ou None si non trouvé
        """
        # Chercher dans le storage global
        for obj in _FAKE_DB_STORAGE["objects"]:
            if isinstance(obj, model_class) and hasattr(obj, 'id') and obj.id == object_id:
                return obj

        # Chercher dans les objets non-committés de cette session
        for obj in self._added_objects:
            if isinstance(obj, model_class) and hasattr(obj, 'id') and obj.id == object_id:
                return obj

        return None

    async def execute(self, query):
        """Retourne un FakeResult selon le scenario"""
        query_str = str(query)

        # Créer un FakeResult
        fake_result = FakeResult()

        # Gestion des requêtes d'agrégation pour metadata endpoint
        if "GROUP BY" in query_str and "model_used" in query_str:
            # Query GROUP BY model_used pour distribution
            # Retourner des résultats de test
            fake_result._all_rows = [
                ('claude-opus-4-5-20251101', 5),
                ('template', 3)
            ]
            return fake_result
        elif "COUNT(*)" in query_str or "count(" in query_str.lower():
            # Query COUNT pour total
            from models.lunar_interpretation import LunarInterpretation
            # Compter dans storage
            count = len([o for o in _FAKE_DB_STORAGE["objects"] if isinstance(o, LunarInterpretation)])
            fake_result._scalar = count
            return fake_result
        elif "MAX(created_at)" in query_str or "max(created_at)" in query_str.lower():
            # Query MAX pour dernière génération
            fake_result._scalar = datetime.now(timezone.utc)
            return fake_result

        # Si query pour NatalChart
        if "NatalChart" in query_str or "natal_charts" in query_str:
            if self.scenario == "natal_exists":
                # Créer un mock natal_chart avec tous les attributs nécessaires
                mock_natal = MagicMock(spec=NatalChart)
                mock_natal.id = "123e4567-e89b-12d3-a456-426614174000"
                mock_natal.user_id = 1
                mock_natal.latitude = 48.8566
                mock_natal.longitude = 2.3522
                mock_natal.timezone = "Europe/Paris"
                mock_natal.positions = {
                    "moon": {
                        "sign": "Aries",
                        "degree": 15.5,
                        "house": 1
                    },
                    "sun": {
                        "sign": "Taurus",
                        "degree": 10.0
                    },
                    "angles": {
                        "ascendant": {
                            "sign": "Leo",
                            "degree": 5.0
                        }
                    }
                }
                fake_result._scalar = mock_natal
            else:  # natal_missing
                fake_result._scalar = None
        elif "LunarReturn" in query_str or "lunar_returns" in query_str:
            # Si c'est un DELETE, supprimer depuis le storage global
            if "DELETE" in query_str.upper() or "delete" in query_str:
                # Extraire user_id si présent dans la query (pour filter le DELETE)
                initial_count = len([o for o in _FAKE_DB_STORAGE["objects"] if isinstance(o, LunarReturn)])

                if "user_id" in query_str:
                    # DELETE avec filtre user_id
                    _FAKE_DB_STORAGE["objects"] = [
                        o for o in _FAKE_DB_STORAGE["objects"]
                        if not (isinstance(o, LunarReturn) and hasattr(o, 'user_id') and o.user_id == 1)
                    ]
                else:
                    # DELETE sans filtre (tous les LunarReturn)
                    _FAKE_DB_STORAGE["objects"] = [
                        o for o in _FAKE_DB_STORAGE["objects"]
                        if not isinstance(o, LunarReturn)
                    ]

                final_count = len([o for o in _FAKE_DB_STORAGE["objects"] if isinstance(o, LunarReturn)])
                fake_result._rowcount = initial_count - final_count
                return fake_result
            
            # Si c'est un SELECT, filtrer depuis le storage global (objets committés)
            # PLUS les objets de cette session (non encore committés)
            all_returns = (
                [obj for obj in _FAKE_DB_STORAGE["objects"] if isinstance(obj, LunarReturn)] +
                [obj for obj in self._added_objects if isinstance(obj, LunarReturn)]
            )
            lunar_returns = all_returns
            
            # Filtrer par user_id si présent dans la query
            if "user_id" in query_str:
                # Extraire user_id de la query (simplifié: on assume user_id == 1 dans les tests)
                lunar_returns = [lr for lr in lunar_returns if hasattr(lr, 'user_id') and lr.user_id == 1]
            
            # Filtrer par return_date >= now si présent
            if "return_date" in query_str and ">=" in query_str:
                now = datetime.now(timezone.utc)
                # Filtrer les objets qui ont un return_date valide et >= now
                filtered_returns = []
                for lr in lunar_returns:
                    if hasattr(lr, 'return_date') and lr.return_date:
                        # Comparer les dates (gérer les timezone-aware et naive)
                        lr_date = lr.return_date
                        if lr_date.tzinfo is None:
                            # Si naive, supposer UTC
                            from datetime import timezone as tz
                            lr_date = lr_date.replace(tzinfo=tz.utc)
                        if lr_date >= now:
                            filtered_returns.append(lr)
                lunar_returns = filtered_returns
            
            # Trier par return_date ASC si ORDER BY présent
            if "ORDER BY" in query_str.upper() or "order_by" in query_str:
                lunar_returns.sort(key=lambda x: x.return_date if hasattr(x, 'return_date') and x.return_date else datetime.min.replace(tzinfo=timezone.utc))
            
            # Appliquer LIMIT si présent
            if "LIMIT" in query_str.upper() or "limit" in query_str:
                # Extraire le nombre (simplifié: on assume limit(1) ou limit(12))
                if "limit(1)" in query_str.lower() or ".limit(1)" in query_str:
                    lunar_returns = lunar_returns[:1]
                elif "limit(12)" in query_str.lower() or ".limit(12)" in query_str:
                    lunar_returns = lunar_returns[:12]
            
            # Si c'est un scalar_one_or_none (SELECT avec limit(1))
            if "limit(1)" in query_str.lower() or ".limit(1)" in query_str:
                fake_result._scalar = lunar_returns[0] if lunar_returns else None
            else:
                # Sinon, retourner la liste via scalars()
                fake_result._scalars_list = lunar_returns
        else:
            # Autres queries (par défaut None)
            fake_result._scalar = None
            
        return fake_result
    
    async def commit(self):
        """Commit les objets ajoutés dans le storage global partagé"""
        self._committed = True
        # Persister les objets ajoutés dans le storage global
        for obj in self._added_objects:
            # Éviter les doublons (check par id si présent)
            if hasattr(obj, 'id') and obj.id:
                # Supprimer ancien objet avec même id si existe
                _FAKE_DB_STORAGE["objects"] = [
                    o for o in _FAKE_DB_STORAGE["objects"]
                    if not (hasattr(o, 'id') and o.id == obj.id)
                ]
            _FAKE_DB_STORAGE["objects"].append(obj)
        self._added_objects = []  # Clear après commit
    
    async def flush(self):
        """No-op pour les tests"""
        pass
    
    async def rollback(self):
        self._committed = False
    
    def add(self, obj):
        # Assigner un id automatique si l'objet n'en a pas (pour les tests)
        if hasattr(obj, 'id') and obj.id is None:
            # Générer un id simple basé sur l'index
            obj.id = len(self._added_objects) + 1
        self._added_objects.append(obj)
    
    def refresh(self, obj):
        pass  # No-op pour les tests
    
    def close(self):
        pass  # No-op pour les tests
    
    async def begin_nested(self):
        """Retourne un context manager pour savepoint (no-op dans les tests)"""
        class FakeNestedTransaction:
            async def __aenter__(self):
                return self
            
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                pass
            
            async def commit(self):
                """No-op pour les tests"""
                pass
        
        return FakeNestedTransaction()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.close()


class FakeResult:
    """Stub pour sqlalchemy.engine.result.Result"""

    def __init__(self):
        self._scalar = None
        self._scalars_list = []
        self._all_rows = []  # For GROUP BY results
        self._rowcount = None

    def scalar_one_or_none(self):
        return self._scalar

    def scalar(self):
        return self._scalar

    def scalars(self):
        # Si on a une liste de scalars (pour SELECT multiple), la retourner
        if hasattr(self, '_scalars_list') and self._scalars_list:
            return iter(self._scalars_list)
        # Sinon, retourner un itérable vide
        return iter([])

    def all(self):
        """Retourne toutes les lignes (pour GROUP BY, etc.)"""
        # Check for _all_rows first (for GROUP BY aggregations)
        if hasattr(self, '_all_rows') and self._all_rows:
            return self._all_rows
        return self._scalars_list if hasattr(self, '_scalars_list') else []

    @property
    def rowcount(self):
        """Retourne le rowcount si disponible"""
        return self._rowcount


@pytest.fixture
def fake_user():
    """Mock User pour les tests"""
    user = MagicMock(spec=User)
    user.id = 1
    user.email = "test@example.com"
    user.birth_latitude = "48.8566"
    user.birth_longitude = "2.3522"
    user.birth_timezone = "Europe/Paris"
    return user


@pytest.fixture
def override_dependencies(fake_user):
    """
    Fixture qui override oauth2_scheme, get_current_user, et get_db.
    Scenario par défaut: "natal_exists"

    Usage:
        @pytest.mark.asyncio
        async def test_something(override_dependencies):
            # Les overrides sont déjà appliqués
            async with AsyncClient(app=app, base_url="http://test") as client:
                ...
            # Nettoyage automatique après le test
    """
    from routes.auth import oauth2_scheme, get_current_user
    from database import get_db

    # IMPORTANT: Clear le storage global AVANT chaque test pour isolation
    _FAKE_DB_STORAGE["objects"].clear()

    # Override oauth2_scheme pour retourner un token factice
    async def override_oauth2_scheme():
        return "test-token"

    # Override get_current_user pour retourner fake_user
    async def override_get_current_user():
        return fake_user

    # Override get_db pour créer une NOUVELLE session par requête (éviter "another operation is in progress")
    async def override_get_db():
        session = FakeAsyncSession(scenario="natal_exists")
        yield session

    # Appliquer les overrides
    app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[get_db] = override_get_db

    yield

    # Nettoyage
    app.dependency_overrides.clear()
    _FAKE_DB_STORAGE["objects"].clear()  # Clean storage après test


@pytest.fixture
def override_dependencies_no_natal(fake_user):
    """
    Fixture similaire mais avec scenario "natal_missing"

    Usage:
        @pytest.mark.asyncio
        async def test_error(override_dependencies_no_natal):
            # Les overrides sont déjà appliqués (natal_chart absent)
            async with AsyncClient(app=app, base_url="http://test") as client:
                ...
    """
    from routes.auth import oauth2_scheme, get_current_user
    from database import get_db

    # IMPORTANT: Clear le storage global AVANT chaque test pour isolation
    _FAKE_DB_STORAGE["objects"].clear()

    async def override_oauth2_scheme():
        return "test-token"

    async def override_get_current_user():
        return fake_user

    async def override_get_db():
        async_session = FakeAsyncSession(scenario="natal_missing")
        yield async_session

    app.dependency_overrides[oauth2_scheme] = override_oauth2_scheme
    app.dependency_overrides[get_current_user] = override_get_current_user
    app.dependency_overrides[get_db] = override_get_db

    yield

    app.dependency_overrides.clear()
    _FAKE_DB_STORAGE["objects"].clear()  # Clean storage après test


@pytest.fixture(autouse=True)
async def real_db_isolation(request):
    """
    Fixture autouse qui isole les tests marqués real_db via TRUNCATE.

    Exécute TRUNCATE ... RESTART IDENTITY CASCADE avant ET après chaque test
    pour garantir une isolation complète des données.

    Utilise un engine dédié avec NullPool pour éviter toute collision avec
    l'engine global de l'app.

    Skip automatiquement le test si la DB n'est pas accessible.
    """
    # Ne s'applique que si le test est marqué real_db
    if not request.node.get_closest_marker("real_db"):
        yield
        return

    from sqlalchemy.ext.asyncio import create_async_engine
    from sqlalchemy.pool import NullPool
    from sqlalchemy import text
    from config import settings

    # Créer un engine dédié avec NullPool uniquement pour les TRUNCATE
    # Convertir postgresql:// en postgresql+asyncpg://
    database_url = settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
    truncate_engine = create_async_engine(database_url, poolclass=NullPool)

    try:
        # Tester la connexion DB - skip si inaccessible
        try:
            async with truncate_engine.begin() as conn:
                await conn.execute(
                    text("TRUNCATE TABLE lunar_reports, lunar_returns, users RESTART IDENTITY CASCADE")
                )
        except Exception as e:
            await truncate_engine.dispose()
            pytest.skip(f"DB not accessible (required for @pytest.mark.real_db tests): {str(e)[:100]}")

        yield

        # TRUNCATE après le test (un seul statement multi-tables)
        async with truncate_engine.begin() as conn:
            await conn.execute(
                text("TRUNCATE TABLE lunar_reports, lunar_returns, users RESTART IDENTITY CASCADE")
            )
    finally:
        # Fermer proprement les connexions
        await truncate_engine.dispose()


# ============================================================================
# CACHE INTERPRETATION ISOLATION
# ============================================================================

@pytest.fixture(autouse=True, scope="function")
def clear_interpretation_cache_between_tests():
    """
    Fixture autouse qui clear le cache d'interprétation avant ET après chaque test.

    Garantit l'isolation complète entre tests utilisant les caches:
    - lunar_climate, lunar_focus, lunar_approach
    - lunar_v2_full
    - natal_pregenerated

    Évite les interférences entre tests qui utilisent les services d'interprétation.
    """
    try:
        from services.interpretation_cache_service import clear_cache
        clear_cache()
    except ImportError:
        # Si le module n'existe pas encore, skip silencieusement
        pass

    yield

    try:
        from services.interpretation_cache_service import clear_cache
        clear_cache()
    except ImportError:
        pass

