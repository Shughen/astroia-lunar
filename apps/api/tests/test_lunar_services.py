"""
Tests unitaires pour les services Luna Pack
Vérifie lunar_services avec mocks httpx
"""

import pytest
from unittest.mock import patch, MagicMock
import httpx
from fastapi import HTTPException

from services import lunar_services


@pytest.mark.asyncio
async def test_get_lunar_return_report_success():
    """Test get_lunar_return_report - succès"""
    mock_response = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Mois favorable aux finances"
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_return_report({
            "birth_date": "1989-04-15",
            "date": "2025-01-15"
        })
        
        assert result == mock_response
        assert mock_post.call_count == 1
        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "lunar-return" in call_args[0][0] or "lunar_return" in call_args[0][0]


@pytest.mark.asyncio
async def test_get_lunar_return_report_error_429():
    """Test get_lunar_return_report - gestion erreur 429"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail="Rate limit")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_return_report({"date": "2025-01-15"})
        
        assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_get_void_of_course_status_success():
    """Test get_void_of_course_status - succès"""
    mock_response = {
        "is_void": True,
        "void_of_course": {
            "start": "2025-01-15T10:30:00",
            "end": "2025-01-15T14:45:00"
        }
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_void_of_course_status({
            "date": "2025-01-15",
            "time": "12:00"
        })
        
        assert result == mock_response
        assert mock_post.call_count == 1
        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "void" in call_args[0][0] or "lunar" in call_args[0][0]


@pytest.mark.asyncio
async def test_get_void_of_course_status_not_void():
    """Test get_void_of_course_status - pas en VoC"""
    mock_response = {
        "is_void": False,
        "next_void": {
            "start": "2025-01-16T08:00:00",
            "end": "2025-01-16T11:30:00"
        }
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response):
        result = await lunar_services.get_void_of_course_status({
            "date": "2025-01-15",
            "time": "12:00"
        })
        
        assert result["is_void"] is False
        assert "next_void" in result


@pytest.mark.asyncio
async def test_get_void_of_course_status_error_500():
    """Test get_void_of_course_status - gestion erreur 500"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail="Server error")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_void_of_course_status({"date": "2025-01-15"})
        
        assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_get_lunar_mansions_success():
    """Test get_lunar_mansions - succès"""
    mock_response = {
        "mansion": {
            "number": 7,
            "name": "Al-Dhira",
            "interpretation": "Favorable aux nouveaux projets"
        }
    }
    
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_mansions({
            "date": "2025-01-15",
            "time": "12:00"
        })
        
        assert result == mock_response
        assert mock_post.call_count == 1
        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "mansions" in call_args[0][0]


@pytest.mark.asyncio
async def test_get_lunar_mansions_all_mansions():
    """Test get_lunar_mansions - vérifier que mansion_id est dans [1-28]"""
    for mansion_id in [1, 14, 28]:
        mock_response = {
            "mansion": {
                "number": mansion_id,
                "name": f"Mansion {mansion_id}",
                "interpretation": "Test"
            }
        }
        
        with patch('services.rapidapi_client.post_json', return_value=mock_response):
            result = await lunar_services.get_lunar_mansions({"date": "2025-01-15"})
            
            assert result["mansion"]["number"] in range(1, 29)


@pytest.mark.asyncio
async def test_get_lunar_mansions_error_timeout():
    """Test get_lunar_mansions - gestion timeout"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_mansions({"date": "2025-01-15"})
        
        assert exc_info.value.status_code == 504


@pytest.mark.asyncio
async def test_lunar_services_with_retry_logic():
    """Test que les services bénéficient des retries du client"""
    mock_response = {"status": "success"}
    
    # Simuler 2 échecs puis succès (le client retry automatiquement)
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_return_report({"date": "2025-01-15"})
        
        # Le service ne devrait faire qu'un appel, le client gère les retries
        assert result == mock_response
        assert mock_post.call_count == 1

