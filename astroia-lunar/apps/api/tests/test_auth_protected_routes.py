"""
Tests d'authentification pour les routes protégées (Sprint 1 Sécurité)

Vérifie que les routes suivantes REJETTENT les requêtes sans authentification:
- POST /api/natal/reading → 401
- GET /api/natal/reading/{cache_key} → 401
- DELETE /api/natal/reading/{cache_key} → 401
- POST /api/reports/lunar/{month} → 401
- GET /api/reports/lunar/{month}/html → 401

Ces tests valident que la protection mise en place dans le Sprint 1 fonctionne.
Les tests de succès avec auth sont couverts par test_lunar_return_auth.py et autres.
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch

from main import app


# ============================================================================
# Tests POST /api/natal/reading
# ============================================================================

@pytest.mark.asyncio
async def test_natal_reading_post_without_auth_returns_401():
    """
    Route POST /api/natal/reading doit nécessiter auth.
    Sans token ni DEV_AUTH_BYPASS, doit retourner 401.
    """
    valid_payload = {
        "birth_data": {
            "date": "1990-05-15",
            "time": "14:30",
            "latitude": 48.8566,
            "longitude": 2.3522,
            "city": "Paris",
            "country": "France",
            "timezone": "Europe/Paris"
        }
    }

    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/natal/reading", json=valid_payload)

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401
            data = response.json()
            assert "detail" in data


# ============================================================================
# Tests GET /api/natal/reading/{cache_key}
# ============================================================================

@pytest.mark.asyncio
async def test_natal_reading_get_without_auth_returns_401():
    """
    Route GET /api/natal/reading/{cache_key} doit nécessiter auth.
    Sans token, doit retourner 401.
    """
    cache_key = "test_cache_key"

    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(f"/api/natal/reading/{cache_key}")

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401


# ============================================================================
# Tests DELETE /api/natal/reading/{cache_key}
# ============================================================================

@pytest.mark.asyncio
async def test_natal_reading_delete_without_auth_returns_401():
    """
    Route DELETE /api/natal/reading/{cache_key} doit nécessiter auth.
    Sans token, doit retourner 401.
    """
    cache_key = "test_cache_key"

    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.delete(f"/api/natal/reading/{cache_key}")

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401


# ============================================================================
# Tests POST /api/reports/lunar/{month}
# ============================================================================

@pytest.mark.asyncio
async def test_lunar_report_post_without_auth_returns_401():
    """
    Route POST /api/reports/lunar/{month} doit nécessiter auth.
    Sans token, doit retourner 401.
    """
    month = "2025-01"

    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post(f"/api/reports/lunar/{month}")

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401


# ============================================================================
# Tests GET /api/reports/lunar/{month}/html
# ============================================================================

@pytest.mark.asyncio
async def test_lunar_report_html_get_without_auth_returns_401():
    """
    Route GET /api/reports/lunar/{month}/html doit nécessiter auth.
    Sans token, doit retourner 401.
    """
    month = "2025-01"

    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(f"/api/reports/lunar/{month}/html")

            # Doit retourner 401 Unauthorized
            assert response.status_code == 401
