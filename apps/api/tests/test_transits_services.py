"""
Tests unitaires pour les services Transits
"""

import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from datetime import datetime
from uuid import UUID

from services import transits_services
from schemas.transits import TransitsOverviewDB


@pytest.mark.asyncio
async def test_get_natal_transits_success():
    """Test get_natal_transits - succès"""
    mock_response = {
        "aspects": [
            {
                "planet1": "Jupiter",
                "planet2": "Sun",
                "aspect": "trine",
                "orb": 1.2,
                "interpretation": "Expansion et confiance"
            }
        ],
        "transit_date": "2025-01-15"
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await transits_services.get_natal_transits({
            "birth_date": "1989-04-15",
            "transit_date": "2025-01-15"
        })
        
        assert result == mock_response
        assert mock_post.call_count == 1
        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "transits" in call_args[0][0] or "natal" in call_args[0][0]


@pytest.mark.asyncio
async def test_get_lunar_return_transits_success():
    """Test get_lunar_return_transits - succès"""
    mock_response = {
        "aspects": [
            {
                "planet1": "Mars",
                "planet2": "Moon",
                "aspect": "square",
                "orb": 2.3
            }
        ],
        "lunar_return_date": "2025-01-10"
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await transits_services.get_lunar_return_transits({
            "birth_date": "1989-04-15",
            "lunar_return_date": "2025-01-10",
            "transit_date": "2025-01-15"
        })
        
        assert result == mock_response
        assert mock_post.call_count == 1
        call_args = mock_post.call_args
        assert "transits" in call_args[0][0] or "lunar" in call_args[0][0]


def test_generate_transit_insights_with_aspects():
    """Test génération d'insights à partir d'aspects"""
    transits_data = {
        "aspects": [
            {
                "planet1": "Jupiter",
                "planet2": "Sun",
                "aspect": "trine",
                "orb": 1.2,
                "interpretation": "Expansion"
            },
            {
                "planet1": "Saturn",
                "planet2": "Moon",
                "aspect": "square",
                "orb": 0.5,
                "interpretation": "Défi émotionnel"
            }
        ]
    }
    
    insights = transits_services.generate_transit_insights(transits_data)
    
    assert "insights" in insights
    assert "major_aspects" in insights
    assert "energy_level" in insights
    assert len(insights["major_aspects"]) == 2
    assert insights["energy_level"] in ["low", "medium", "high"]


def test_generate_transit_insights_empty():
    """Test génération d'insights avec données vides"""
    insights = transits_services.generate_transit_insights({})
    
    assert insights["insights"] == []
    assert insights["major_aspects"] == []
    assert insights["energy_level"] in ["low", "medium", "high"]  # Default can vary


def test_generate_transit_insights_sorting():
    """Test que les aspects sont triés par orbe (le plus serré en premier)"""
    transits_data = {
        "aspects": [
            {"planet1": "Mars", "planet2": "Venus", "aspect": "opposition", "orb": 5.0},
            {"planet1": "Jupiter", "planet2": "Sun", "aspect": "trine", "orb": 0.3},
            {"planet1": "Saturn", "planet2": "Moon", "aspect": "square", "orb": 2.1}
        ]
    }
    
    insights = transits_services.generate_transit_insights(transits_data)
    
    # Le premier aspect devrait avoir l'orbe le plus petit
    assert insights["major_aspects"][0]["orb"] == 0.3
    assert insights["major_aspects"][0]["transit_planet"] == "Jupiter"


@pytest.mark.asyncio
async def test_natal_transits_error_handling():
    """Test gestion d'erreur sur get_natal_transits"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail="Provider error")):
        with pytest.raises(HTTPException) as exc_info:
            await transits_services.get_natal_transits({"birth_date": "1989-04-15"})
        
        assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_lunar_return_transits_error_handling():
    """Test gestion d'erreur sur get_lunar_return_transits"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout")):
        with pytest.raises(HTTPException) as exc_info:
            await transits_services.get_lunar_return_transits({
                "birth_date": "1989-04-15",
                "lunar_return_date": "2025-01-10"
            })
        
        assert exc_info.value.status_code == 504


def test_transits_overview_db_schema_serialization():
    """Test que TransitsOverviewDB sérialise avec 'overview' et 'summary' (compatibilité)"""
    test_user_id = UUID("550e8400-e29b-41d4-a716-446655440000")
    test_overview_data = {
        "natal_transits": {"aspects": []},
        "insights": {"energy_level": "medium"},
        "last_updated": "2025-01-15T10:00:00"
    }
    
    overview_db = TransitsOverviewDB(
        id=1,
        user_id=test_user_id,
        month="2025-01",
        overview=test_overview_data,
        created_at=datetime.now()
    )
    
    # Sérialiser en dict
    serialized = overview_db.model_dump()
    
    # Vérifier que 'overview' est présent
    assert "overview" in serialized
    assert serialized["overview"] == test_overview_data
    
    # Vérifier que 'summary' est présent (compatibilité)
    assert "summary" in serialized
    assert serialized["summary"] == test_overview_data
    
    # Vérifier que summary == overview
    assert serialized["summary"] == serialized["overview"]

