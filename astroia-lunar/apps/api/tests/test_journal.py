"""
Tests pour les routes Journal (POST /entry, GET /entries, GET /today)
Vérifie l'authentification, la création, la récupération et la suppression d'entrées
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch
from datetime import date

from main import app


@pytest.mark.asyncio
async def test_create_journal_entry_without_auth_returns_401():
    """
    Test: Route POST /api/journal/entry doit nécessiter auth.
    Sans token ni DEV_AUTH_BYPASS, doit retourner 401.
    """
    valid_payload = {
        "date": "2026-01-16",
        "mood": "calm",
        "note": "Belle journée",
        "month": "2026-01"
    }

    # Désactiver DEV_AUTH_BYPASS pour ce test
    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/journal/entry", json=valid_payload)
            assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_journal_entry_with_dev_bypass_succeeds(setup_test_db):
    """
    Test: Créer une entrée de journal avec DEV_AUTH_BYPASS actif.
    Doit retourner 201 Created.
    """
    valid_payload = {
        "date": "2026-01-16",
        "mood": "calm",
        "note": "Belle journée",
        "month": "2026-01"
    }

    # Activer DEV_AUTH_BYPASS
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post(
                "/api/journal/entry",
                json=valid_payload,
                headers={"X-Dev-User-Id": "1"}
            )

            # Doit retourner 201 Created
            assert response.status_code == 201

            data = response.json()
            assert data["user_id"] == 1
            assert data["date"] == "2026-01-16"
            assert data["mood"] == "calm"
            assert data["note"] == "Belle journée"
            assert data["month"] == "2026-01"
            assert "id" in data
            assert "created_at" in data


@pytest.mark.asyncio
async def test_update_existing_journal_entry(setup_test_db):
    """
    Test: Mettre à jour une entrée existante (même date).
    Doit retourner 201 et mettre à jour l'entrée.
    """
    initial_payload = {
        "date": "2026-01-17",
        "mood": "neutral",
        "note": "Journée normale",
        "month": "2026-01"
    }

    updated_payload = {
        "date": "2026-01-17",
        "mood": "excited",
        "note": "Finalement super journée!",
        "month": "2026-01"
    }

    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Créer l'entrée initiale
            response1 = await client.post(
                "/api/journal/entry",
                json=initial_payload,
                headers={"X-Dev-User-Id": "1"}
            )
            assert response1.status_code == 201
            entry_id = response1.json()["id"]

            # Mettre à jour l'entrée (même date)
            response2 = await client.post(
                "/api/journal/entry",
                json=updated_payload,
                headers={"X-Dev-User-Id": "1"}
            )

            assert response2.status_code == 201
            data = response2.json()

            # Doit avoir le même ID (mise à jour, pas création)
            assert data["id"] == entry_id
            assert data["mood"] == "excited"
            assert data["note"] == "Finalement super journée!"
            assert "updated_at" in data


@pytest.mark.asyncio
async def test_get_journal_entries_without_auth_returns_401():
    """
    Test: Route GET /api/journal/entries doit nécessiter auth.
    """
    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get("/api/journal/entries")
            assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_journal_entries_empty(setup_test_db):
    """
    Test: Récupérer les entrées d'un utilisateur qui n'en a pas.
    Doit retourner une liste vide.
    """
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(
                "/api/journal/entries",
                headers={"X-Dev-User-Id": "9999"}  # User sans entrées
            )

            assert response.status_code == 200
            data = response.json()
            assert data["total"] == 0
            assert data["entries"] == []


@pytest.mark.asyncio
async def test_get_journal_entries_with_filter(setup_test_db):
    """
    Test: Récupérer les entrées filtrées par mois lunaire.
    """
    entries = [
        {"date": "2026-01-10", "mood": "calm", "month": "2026-01"},
        {"date": "2026-01-15", "mood": "excited", "month": "2026-01"},
        {"date": "2026-02-05", "mood": "sad", "month": "2026-02"},
    ]

    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Créer les entrées
            for entry in entries:
                await client.post(
                    "/api/journal/entry",
                    json=entry,
                    headers={"X-Dev-User-Id": "2"}
                )

            # Récupérer les entrées du mois 2026-01
            response = await client.get(
                "/api/journal/entries?month=2026-01",
                headers={"X-Dev-User-Id": "2"}
            )

            assert response.status_code == 200
            data = response.json()
            assert data["total"] == 2
            assert data["month"] == "2026-01"
            assert len(data["entries"]) == 2


@pytest.mark.asyncio
async def test_get_today_entry_without_auth_returns_401():
    """
    Test: Route GET /api/journal/today doit nécessiter auth.
    """
    with patch('config.settings.DEV_AUTH_BYPASS', False):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get("/api/journal/today")
            assert response.status_code == 401


@pytest.mark.asyncio
async def test_get_today_entry_not_found(setup_test_db):
    """
    Test: Récupérer l'entrée du jour quand elle n'existe pas.
    Doit retourner 200 avec None.
    """
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.get(
                "/api/journal/today",
                headers={"X-Dev-User-Id": "8888"}  # User sans entrée aujourd'hui
            )

            assert response.status_code == 200
            # FastAPI retourne null pour None
            assert response.json() is None


@pytest.mark.asyncio
async def test_get_today_entry_found(setup_test_db):
    """
    Test: Récupérer l'entrée du jour quand elle existe.
    """
    today_str = date.today().isoformat()
    payload = {
        "date": today_str,
        "mood": "calm",
        "note": "Entrée d'aujourd'hui",
        "month": "2026-01"
    }

    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Créer l'entrée d'aujourd'hui
            await client.post(
                "/api/journal/entry",
                json=payload,
                headers={"X-Dev-User-Id": "3"}
            )

            # Récupérer l'entrée du jour
            response = await client.get(
                "/api/journal/today",
                headers={"X-Dev-User-Id": "3"}
            )

            assert response.status_code == 200
            data = response.json()
            assert data is not None
            assert data["date"] == today_str
            assert data["mood"] == "calm"


@pytest.mark.asyncio
async def test_delete_journal_entry(setup_test_db):
    """
    Test: Supprimer une entrée de journal.
    Doit retourner 204 No Content.
    """
    payload = {
        "date": "2026-01-18",
        "mood": "neutral",
        "note": "À supprimer",
        "month": "2026-01"
    }

    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Créer l'entrée
            create_response = await client.post(
                "/api/journal/entry",
                json=payload,
                headers={"X-Dev-User-Id": "4"}
            )
            assert create_response.status_code == 201
            entry_id = create_response.json()["id"]

            # Supprimer l'entrée
            delete_response = await client.delete(
                f"/api/journal/entry/{entry_id}",
                headers={"X-Dev-User-Id": "4"}
            )
            assert delete_response.status_code == 204

            # Vérifier que l'entrée n'existe plus
            get_response = await client.get(
                "/api/journal/entries",
                headers={"X-Dev-User-Id": "4"}
            )
            data = get_response.json()
            entry_ids = [e["id"] for e in data["entries"]]
            assert entry_id not in entry_ids


@pytest.mark.asyncio
async def test_delete_journal_entry_not_found(setup_test_db):
    """
    Test: Supprimer une entrée qui n'existe pas ou appartient à un autre user.
    Doit retourner 404.
    """
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'):

        async with AsyncClient(app=app, base_url="http://test") as client:
            # Essayer de supprimer une entrée inexistante
            response = await client.delete(
                "/api/journal/entry/99999",
                headers={"X-Dev-User-Id": "5"}
            )
            assert response.status_code == 404
