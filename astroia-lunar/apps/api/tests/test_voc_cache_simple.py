"""
Tests simplifiés pour le service de cache VoC (voc_cache_service.py)
Tests unitaires sans dépendance DB réelle
"""

import pytest
import time
from datetime import datetime, timedelta, timezone
from unittest.mock import AsyncMock, MagicMock, patch

from services import voc_cache_service
from models.lunar_pack import LunarVocWindow


@pytest.fixture(autouse=True)
def clear_voc_cache():
    """Clear cache avant et après chaque test"""
    voc_cache_service.clear_cache()
    yield
    voc_cache_service.clear_cache()


class TestVoCCacheLogic:
    """Tests de la logique de cache sans DB réelle"""

    def test_clear_cache(self):
        """Test: clear_cache invalide tous les caches"""
        # Setup: simuler cache rempli
        voc_cache_service._VOC_STATUS_CACHE["data"] = {"test": "data"}
        voc_cache_service._VOC_STATUS_CACHE["timestamp"] = time.time()
        voc_cache_service._VOC_CURRENT_CACHE["data"] = {"test": "data"}
        voc_cache_service._VOC_CURRENT_CACHE["timestamp"] = time.time()

        # Act
        voc_cache_service.clear_cache()

        # Assert
        assert voc_cache_service._VOC_STATUS_CACHE["data"] is None
        assert voc_cache_service._VOC_STATUS_CACHE["timestamp"] == 0
        assert voc_cache_service._VOC_CURRENT_CACHE["data"] is None
        assert voc_cache_service._VOC_CURRENT_CACHE["timestamp"] == 0

    def test_get_cache_stats_empty(self):
        """Test: stats de cache vide"""
        # Act
        stats = voc_cache_service.get_cache_stats()

        # Assert
        assert "voc_status" in stats
        assert "voc_current" in stats
        assert stats["voc_status"]["has_data"] is False
        assert stats["voc_current"]["has_data"] is False

    def test_get_cache_stats_with_data(self):
        """Test: stats de cache avec données"""
        # Setup: remplir le cache
        voc_cache_service._VOC_STATUS_CACHE["data"] = {"test": "data"}
        voc_cache_service._VOC_STATUS_CACHE["timestamp"] = time.time()

        # Act
        stats = voc_cache_service.get_cache_stats()

        # Assert
        assert stats["voc_status"]["has_data"] is True
        assert stats["voc_status"]["age_seconds"] is not None
        assert stats["voc_status"]["age_seconds"] >= 0

    @pytest.mark.asyncio
    async def test_get_voc_status_cache_hit(self):
        """Test: cache hit pour get_voc_status_cached"""
        # Setup: pré-remplir le cache
        cached_data = {
            "now": {"is_active": True, "start_at": "2026-01-16T20:00:00+00:00", "end_at": "2026-01-16T22:00:00+00:00"},
            "next": None,
            "upcoming": []
        }
        voc_cache_service._VOC_STATUS_CACHE["data"] = cached_data
        voc_cache_service._VOC_STATUS_CACHE["timestamp"] = time.time()

        # Mock DB session (ne devrait pas être appelé)
        mock_db = AsyncMock()
        mock_db.execute = AsyncMock()

        # Act
        result = await voc_cache_service.get_voc_status_cached(mock_db)

        # Assert: cache hit, DB non appelé
        mock_db.execute.assert_not_called()
        assert result == cached_data

    @pytest.mark.asyncio
    async def test_get_current_voc_cache_hit(self):
        """Test: cache hit pour get_current_voc_cached"""
        # Setup: pré-remplir le cache
        cached_data = {
            "is_active": False,
            "start_at": None,
            "end_at": None,
            "source": None
        }
        voc_cache_service._VOC_CURRENT_CACHE["data"] = cached_data
        voc_cache_service._VOC_CURRENT_CACHE["timestamp"] = time.time()

        # Mock DB session (ne devrait pas être appelé)
        mock_db = AsyncMock()
        mock_db.execute = AsyncMock()

        # Act
        result = await voc_cache_service.get_current_voc_cached(mock_db)

        # Assert: cache hit, DB non appelé
        mock_db.execute.assert_not_called()
        assert result == cached_data

    @pytest.mark.asyncio
    async def test_get_voc_status_cache_miss_and_fill(self):
        """Test: cache miss puis remplissage"""
        # Setup: mock DB pour retourner des VoC
        mock_db = AsyncMock()

        # Mock current VoC
        now = datetime.now(timezone.utc)
        mock_current_voc = MagicMock(spec=LunarVocWindow)
        mock_current_voc.start_at = now - timedelta(hours=1)
        mock_current_voc.end_at = now + timedelta(hours=1)

        # Mock next VoC
        mock_next_voc = MagicMock(spec=LunarVocWindow)
        mock_next_voc.start_at = now + timedelta(hours=2)
        mock_next_voc.end_at = now + timedelta(hours=3)

        # Mock results - scalars() et first() sont synchrones
        mock_current_scalars = MagicMock()
        mock_current_scalars.first = MagicMock(return_value=mock_current_voc)
        mock_current_result = MagicMock()
        mock_current_result.scalars = MagicMock(return_value=mock_current_scalars)

        mock_next_result = MagicMock()
        mock_next_result.scalar_one_or_none = MagicMock(return_value=mock_next_voc)

        mock_upcoming_scalars = MagicMock()
        mock_upcoming_scalars.all = MagicMock(return_value=[])
        mock_upcoming_result = MagicMock()
        mock_upcoming_result.scalars = MagicMock(return_value=mock_upcoming_scalars)

        mock_db.execute = AsyncMock(side_effect=[mock_current_result, mock_next_result, mock_upcoming_result])

        # Act
        result = await voc_cache_service.get_voc_status_cached(mock_db)

        # Assert: DB appelé, cache rempli
        assert mock_db.execute.call_count == 3  # 3 requêtes parallèles
        assert result is not None
        assert result["now"] is not None
        assert result["now"]["is_active"] is True
        assert result["next"] is not None

        # Vérifier que le cache est rempli
        assert voc_cache_service._VOC_STATUS_CACHE["data"] == result

    @pytest.mark.asyncio
    async def test_cache_ttl_expiration(self):
        """Test: cache expire après TTL"""
        # Setup: remplir cache avec TTL expiré
        voc_cache_service._VOC_CURRENT_CACHE["data"] = {"old": "data"}
        voc_cache_service._VOC_CURRENT_CACHE["timestamp"] = time.time() - 200  # Expiré (TTL=60s)

        # Mock DB pour retourner nouvelle donnée - scalars() et first() sont synchrones
        mock_db = AsyncMock()
        mock_scalars = MagicMock()
        mock_scalars.first = MagicMock(return_value=None)
        mock_result = MagicMock()
        mock_result.scalars = MagicMock(return_value=mock_scalars)
        mock_db.execute = AsyncMock(return_value=mock_result)

        # Act
        result = await voc_cache_service.get_current_voc_cached(mock_db)

        # Assert: DB appelé (cache expiré)
        mock_db.execute.assert_called_once()
        assert result["is_active"] is False

    @pytest.mark.asyncio
    async def test_save_voc_window_no_duplicate(self):
        """Test: save_voc_window_safe évite les doublons"""
        # Setup: mock DB avec fenêtre existante
        mock_db = AsyncMock()

        existing_voc = MagicMock(spec=LunarVocWindow)
        existing_voc.id = 1
        existing_voc.start_at = datetime(2026, 1, 16, 10, 0, tzinfo=timezone.utc)
        existing_voc.end_at = datetime(2026, 1, 16, 12, 0, tzinfo=timezone.utc)
        existing_voc.source = {"old": "data"}

        mock_result = AsyncMock()
        mock_result.scalar_one_or_none = MagicMock(return_value=existing_voc)
        mock_db.execute = AsyncMock(return_value=mock_result)
        mock_db.flush = AsyncMock()
        mock_db.commit = AsyncMock()

        # Act: sauvegarder la même fenêtre avec source différent
        result = await voc_cache_service.save_voc_window_safe(
            db=mock_db,
            start_at=existing_voc.start_at,
            end_at=existing_voc.end_at,
            source={"new": "data"}
        )

        # Assert: source mis à jour, pas de doublon
        assert result == existing_voc
        assert result.source == {"new": "data"}
        mock_db.commit.assert_called_once()

    @pytest.mark.asyncio
    async def test_fallback_on_stale_cache_when_db_error(self):
        """Test: fallback sur cache expiré en cas d'erreur DB"""
        # Setup: cache expiré
        stale_data = {"stale": "data"}
        voc_cache_service._VOC_STATUS_CACHE["data"] = stale_data
        voc_cache_service._VOC_STATUS_CACHE["timestamp"] = time.time() - 500  # Très expiré

        # Mock DB pour simuler erreur
        mock_db = AsyncMock()
        from sqlalchemy.exc import OperationalError
        mock_db.execute = AsyncMock(side_effect=OperationalError("DB connection failed", None, None))

        # Act: devrait retourner le cache expiré comme fallback
        result = await voc_cache_service.get_voc_status_cached(mock_db)

        # Assert: fallback sur cache expiré
        assert result == stale_data


class TestRetryLogic:
    """Tests de la retry logic"""

    @pytest.mark.asyncio
    async def test_retry_decorator_success_on_second_attempt(self):
        """Test: retry réussit à la 2ème tentative"""
        # Setup: fonction qui échoue 1 fois puis réussit
        call_count = {"count": 0}

        @voc_cache_service._with_db_retry(max_retries=3)
        async def failing_function():
            call_count["count"] += 1
            if call_count["count"] == 1:
                from sqlalchemy.exc import OperationalError
                raise OperationalError("DB error", None, None)
            return "success"

        # Act
        result = await failing_function()

        # Assert
        assert result == "success"
        assert call_count["count"] == 2  # 1 échec + 1 succès

    @pytest.mark.asyncio
    async def test_retry_decorator_fails_after_max_retries(self):
        """Test: retry échoue après max tentatives"""
        # Setup: fonction qui échoue toujours
        @voc_cache_service._with_db_retry(max_retries=2)
        async def always_failing_function():
            from sqlalchemy.exc import OperationalError
            raise OperationalError("DB error", None, None)

        # Act & Assert: devrait lever l'exception après 2 tentatives
        from sqlalchemy.exc import OperationalError
        with pytest.raises(OperationalError):
            await always_failing_function()

    @pytest.mark.asyncio
    async def test_retry_decorator_does_not_retry_non_sql_errors(self):
        """Test: retry ne réessaye pas les erreurs non-SQL"""
        # Setup: fonction qui lève une erreur non-SQL
        call_count = {"count": 0}

        @voc_cache_service._with_db_retry(max_retries=3)
        async def non_sql_error_function():
            call_count["count"] += 1
            raise ValueError("Not a SQL error")

        # Act & Assert: devrait lever immédiatement sans retry
        with pytest.raises(ValueError):
            await non_sql_error_function()

        # Vérifier qu'il n'y a eu qu'une seule tentative
        assert call_count["count"] == 1
