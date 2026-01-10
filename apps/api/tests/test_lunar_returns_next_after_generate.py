"""
Test supplémentaire: après generate, /next doit renvoyer 200 (pas 404)

Ce test vérifie que la génération rolling garantit qu'il y aura toujours un retour à venir.
"""

import pytest
from httpx import AsyncClient
from unittest.mock import patch, AsyncMock
from fastapi import status
from datetime import datetime, timezone

from main import app


@pytest.mark.asyncio
async def test_next_returns_200_after_generate(override_dependencies):
    """
    Test: Après POST /generate, GET /next doit renvoyer 200 (pas 404)
    
    Scenario:
    1. Générer les retours avec rolling 12 months
    2. Appeler GET /next
    3. Vérifier que ça retourne 200 avec un retour à venir (return_date >= now)
    """
    
    # Mock ephemeris client
    # On génère des retours avec des dates futures (simuler rolling)
    now = datetime.now(timezone.utc)
    
    # Calculer le mois de départ (comme dans generate_lunar_returns)
    if now.day > 15:
        if now.month == 12:
            start_year = now.year + 1
            start_month = 1
        else:
            start_year = now.year
            start_month = now.month + 1
    else:
        start_year = now.year
        start_month = now.month
    
    # Générer des mock responses avec des dates futures
    def mock_ephemeris_response(month_str: str):
        """Génère un mock response avec une date future pour ce mois"""
        # Simuler une date au milieu du mois (15) pour ce mois
        year, month = map(int, month_str.split('-'))
        return_datetime = datetime(year, month, 15, 12, 0, 0, tzinfo=timezone.utc).isoformat() + "Z"
        
        return {
            "return_datetime": return_datetime,
            "ascendant": {"sign": "Taurus"},
            "moon": {"house": 4, "sign": "Aries"},
            "aspects": [],
            "planets": {},
            "houses": {}
        }
    
    # Mock pour compter les appels
    call_count = [0]
    
    async def mock_calculate_lunar_return(*args, target_month, **kwargs):
        call_count[0] += 1
        return mock_ephemeris_response(target_month)
    
    with patch("routes.lunar_returns.ephemeris_client.calculate_lunar_return", 
               new_callable=AsyncMock, side_effect=mock_calculate_lunar_return), \
         patch("routes.lunar_returns.generate_lunar_return_interpretation", return_value="Test interpretation"):
        
        async with AsyncClient(app=app, base_url="http://test") as client:
            # Étape 1: Générer les retours
            generate_response = await client.post(
                "/api/lunar-returns/generate",
                headers={"Authorization": "Bearer test-token"}
            )
            
            assert generate_response.status_code == status.HTTP_201_CREATED, \
                f"Expected 201 for generate, got {generate_response.status_code}. Body: {generate_response.text}"
            
            generate_data = generate_response.json()
            assert generate_data["generated_count"] > 0, \
                f"Expected generated_count > 0, got {generate_data['generated_count']}"
            
            # Étape 2: Appeler GET /next
            next_response = await client.get(
                "/api/lunar-returns/next",
                headers={"Authorization": "Bearer test-token"}
            )
            
            # Vérifier que ça retourne 200 (pas 404)
            assert next_response.status_code == status.HTTP_200_OK, \
                f"Expected 200 for /next after generate, got {next_response.status_code}. Body: {next_response.text}"
            
            next_data = next_response.json()
            
            # Vérifier qu'on a un return_date
            assert "return_date" in next_data, "Response should have 'return_date' field"
            
            # Vérifier que return_date est dans le futur (ou aujourd'hui)
            return_date_str = next_data["return_date"]
            return_date = datetime.fromisoformat(return_date_str.replace('Z', '+00:00'))
            
            assert return_date >= now, \
                f"Expected return_date ({return_date}) >= now ({now}), but it's in the past!"
            
            # Vérifier les champs essentiels
            assert "id" in next_data, "Response should have 'id' field"
            assert "month" in next_data, "Response should have 'month' field"

