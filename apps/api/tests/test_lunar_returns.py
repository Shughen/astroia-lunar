"""
Tests unitaires pour les endpoints lunar returns

Tests:
- POST /api/lunar-returns/generate retourne 201 quand natal_chart existe (mode mock)
- Erreur JSON structure: vérifie {detail, step, correlation_id}
- DB insert: vérifie que user_id est bien INTEGER
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock
from fastapi import status

from main import app
from models.lunar_return import LunarReturn
from datetime import datetime, timezone
from sqlalchemy import Integer


@pytest.mark.asyncio
async def test_success_generate_201(override_dependencies):
    """
    Test: POST /api/lunar-returns/generate renvoie 201 quand natal_chart existe (mode mock)
    
    Scenario: natal_chart existe pour user_id=1
    - Override oauth2_scheme + get_current_user + get_db (via fixture)
    - Mock ephemeris_client pour éviter les vrais appels API
    - Vérifie statut 201 + structure JSON + generated_count > 0
    """
    
    # Mock ephemeris client (mode mock)
    mock_ephemeris_response = {
        "return_datetime": "2025-01-15T12:00:00Z",
        "ascendant": {"sign": "Taurus"},
        "moon_house": 4,
        "moon_sign": "Aries",
        "aspects": [],
        "planets": {},
        "houses": {}
    }
    
    # Mock ephemeris client et interpretation
    with patch("routes.lunar_returns.ephemeris_client.calculate_lunar_return", 
               new_callable=AsyncMock, return_value=mock_ephemeris_response), \
         patch("routes.lunar_returns.generate_lunar_return_interpretation", return_value="Test interpretation"):
        
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post(
                "/api/lunar-returns/generate",
                headers={"Authorization": "Bearer test-token"}
            )
            
            # Vérifier le statut
            assert response.status_code == status.HTTP_201_CREATED, \
                f"Expected 201, got {response.status_code}. Body: {response.text}"
            
            data = response.json()
            
            # Vérifier la structure de la réponse
            assert "message" in data, "Response should have 'message' field"
            assert "mode" in data, "Response should have 'mode' field (rolling)"
            assert "generated_count" in data, "Response should have 'generated_count' field"
            assert "correlation_id" in data, "Response should have 'correlation_id' field"
            
            # Vérifier que mode est "rolling"
            assert data["mode"] == "rolling", f"Expected mode='rolling', got '{data['mode']}'"
            
            # Vérifier que generated_count > 0 (au moins 1 révolution lunaire générée)
            assert data["generated_count"] > 0, \
                f"Expected generated_count > 0, got {data['generated_count']}"
            
            # Vérifier que correlation_id n'est pas vide
            assert data["correlation_id"], \
                f"Expected non-empty correlation_id, got '{data['correlation_id']}'"


@pytest.mark.asyncio
async def test_get_current_lunar_return_null_when_not_found(override_dependencies):
    """
    Test: GET /api/lunar-returns/current renvoie 200 avec null quand aucune révolution lunaire n'existe

    Scenario: Aucune révolution lunaire pour le mois en cours
    - Vérifie statut 200 (pas 404)
    - Vérifie que le body est null
    """
    # Ne pas ajouter de révolution lunaire au fake_db (empty state)

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get(
            "/api/lunar-returns/current",
            headers={"Authorization": "Bearer test-token"}
        )

        # Vérifier le statut 200 (pas 404!)
        assert response.status_code == status.HTTP_200_OK, \
            f"Expected 200, got {response.status_code}. Body: {response.text}"

        # Vérifier que le body est null (JSON null)
        data = response.json()
        assert data is None, \
            f"Expected null, got {data}"


@pytest.mark.asyncio
async def test_error_json_shape(override_dependencies_no_natal):
    """
    Test: Force une erreur (pas de natal_chart) => réponse JSON contient exactement {detail, step, correlation_id}
    
    Scenario: natal_chart absent
    - Override dependencies avec scenario "natal_missing"
    - Doit renvoyer 404 NOT FOUND
    - Vérifie JSON EXACT: {"detail": {...}, "step": "...", "correlation_id": "..."}
    """
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            "/api/lunar-returns/generate",
            headers={"Authorization": "Bearer test-token"}
        )
        
        # Vérifier le statut 404
        assert response.status_code == status.HTTP_404_NOT_FOUND, \
            f"Expected 404, got {response.status_code}. Body: {response.text}"
        
        data = response.json()
        
        # Vérifier la structure d'erreur JSON exacte
        assert "detail" in data, "Response should have 'detail' field"
        
        # FastAPI encapsule notre dict dans "detail"
        detail_dict = data["detail"]
        assert isinstance(detail_dict, dict), \
            f"Expected detail to be a dict, got {type(detail_dict)}"
        
        # Vérifier les clés exactes: detail, correlation_id, step
        assert "detail" in detail_dict, "Error detail should have 'detail' key"
        assert "correlation_id" in detail_dict, "Error detail should have 'correlation_id' key"
        assert "step" in detail_dict, "Error detail should have 'step' key"
        
        # Vérifier la valeur de step
        assert detail_dict["step"] == "fetch_natal_chart", \
            f"Expected step='fetch_natal_chart', got '{detail_dict['step']}'"
        
        # Vérifier que correlation_id n'est pas vide
        assert detail_dict["correlation_id"], \
            f"Expected non-empty correlation_id, got '{detail_dict['correlation_id']}'"
        
        # Vérifier qu'il n'y a pas d'autres clés inattendues
        expected_keys = {"detail", "correlation_id", "step"}
        actual_keys = set(detail_dict.keys())
        assert actual_keys == expected_keys, \
            f"Unexpected keys in error detail: {actual_keys - expected_keys}. " \
            f"Expected only: {expected_keys}"


@pytest.mark.asyncio
async def test_db_user_id_int():
    """
    Test: insert lunar_returns => user_id est bien int en DB (type attendu + valeur)
    
    Ce test vérifie le modèle SQLAlchemy directement (pas de DB réelle nécessaire).
    - Vérifie que LunarReturn.user_id.type est Integer
    - Créer une instance avec user_id=int
    - Vérifie que user_id reste int (pas UUID)
    """
    
    # Vérifier que le type de colonne dans le modèle SQLAlchemy est Integer
    assert isinstance(LunarReturn.user_id.type, Integer), \
        "LunarReturn.user_id column type should be Integer in SQLAlchemy model"
    
    # Créer une instance de LunarReturn
    test_user_id = 999  # INTEGER
    lunar_return = LunarReturn(
        user_id=test_user_id,
        month="2025-01",
        return_date=datetime(2025, 1, 15, 12, 0, 0, tzinfo=timezone.utc),
        lunar_ascendant="Taurus",
        moon_house=4,
        moon_sign="Aries",
        raw_data={"return_datetime": "2025-01-15T12:00:00Z"}
    )
    
    # Vérifier que user_id est bien un int (pas UUID) dans l'instance Python
    assert isinstance(lunar_return.user_id, int), \
        f"LunarReturn.user_id should be int, got {type(lunar_return.user_id)}"
    assert lunar_return.user_id == test_user_id
    
    # Vérifier qu'on peut le convertir en int sans erreur
    user_id_int = int(lunar_return.user_id)
    assert user_id_int == test_user_id
    assert type(user_id_int) == int
