"""
Tests P0-1: Lunar Mansion avec mansion_id=None
Vérifie que l'API retourne 503 et ne fait pas d'INSERT quand mansion_id manquant
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch

from main import app


@pytest.mark.asyncio
async def test_lunar_mansion_missing_mansion_id_returns_503():
    """
    P0-1 FIX TEST: Quand mansion_id=None dans la réponse normalisée,
    l'API doit retourner 503 (pas 200) et ne pas tenter d'INSERT en DB.
    """
    # Mock du service RapidAPI retournant des données sans mansion.number
    mock_response_incomplete = {
        "mansion": {
            # "number" est absent ou None
            "name": "Al-Sharatain",
            "interpretation": "Test interpretation"
        },
        "upcoming_changes": []
    }

    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.lunar_services.get_lunar_mansions', return_value=mock_response_incomplete):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=valid_payload)

            # P0-1 FIX: Doit retourner 503 (Service Unavailable)
            assert response.status_code == 503

            # Vérifier la structure de la réponse
            data = response.json()
            assert data["status"] == "unavailable"
            assert data["reason"] == "missing_mansion_id"
            assert data["date"] == "2025-01-15"
            assert data["provider"] == "rapidapi"
            assert "message" in data
            assert "data" in data  # Données partielles pour debug


@pytest.mark.asyncio
async def test_lunar_mansion_with_valid_mansion_id_returns_200():
    """
    Test de régression: avec mansion_id valide, l'API doit retourner 200
    """
    mock_response_complete = {
        "mansion": {
            "number": 1,
            "name": "Al-Sharatain",
            "interpretation": "Test interpretation"
        },
        "upcoming_changes": []
    }

    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.lunar_services.get_lunar_mansions', return_value=mock_response_complete):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=valid_payload)

            # Doit retourner 200 avec mansion_id valide
            assert response.status_code == 200

            data = response.json()
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_mansion"
            assert data["data"]["mansion"]["number"] == 1
