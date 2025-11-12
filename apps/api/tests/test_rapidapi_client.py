"""
Tests unitaires pour le client RapidAPI
Vérifie les retries, exponential backoff, timeouts, et gestion d'erreurs
"""

import pytest
from unittest.mock import AsyncMock, patch, MagicMock
import httpx
from fastapi import HTTPException

from services import rapidapi_client


@pytest.mark.asyncio
async def test_post_json_success():
    """Test d'un appel réussi au premier essai"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "success", "data": {"moon": "Taurus"}}
    
    with patch.object(rapidapi_client.client, 'post', return_value=mock_response) as mock_post:
        result = await rapidapi_client.post_json("/test/path", {"key": "value"})
        
        assert result == {"status": "success", "data": {"moon": "Taurus"}}
        assert mock_post.call_count == 1


@pytest.mark.asyncio
async def test_post_json_retry_on_429():
    """Test retry sur erreur 429 (rate limit)"""
    # Premier appel: 429, deuxième: succès
    mock_response_error = MagicMock()
    mock_response_error.status_code = 429
    mock_response_error.text = "Rate limit exceeded"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "429", request=MagicMock(), response=mock_response_error
    )
    
    mock_response_success = MagicMock()
    mock_response_success.status_code = 200
    mock_response_success.json.return_value = {"status": "success"}
    
    with patch.object(rapidapi_client.client, 'post') as mock_post:
        mock_post.side_effect = [
            mock_response_error,
            mock_response_success
        ]
        
        # Mock asyncio.sleep pour accélérer le test
        with patch('asyncio.sleep', return_value=None):
            result = await rapidapi_client.post_json("/test/path", {})
            
            assert result == {"status": "success"}
            assert mock_post.call_count == 2


@pytest.mark.asyncio
async def test_post_json_retry_on_500():
    """Test retry sur erreur 500 (server error)"""
    mock_response_error = MagicMock()
    mock_response_error.status_code = 500
    mock_response_error.text = "Internal server error"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "500", request=MagicMock(), response=mock_response_error
    )
    
    mock_response_success = MagicMock()
    mock_response_success.status_code = 200
    mock_response_success.json.return_value = {"status": "success"}
    
    with patch.object(rapidapi_client.client, 'post') as mock_post:
        mock_post.side_effect = [
            mock_response_error,
            mock_response_success
        ]
        
        with patch('asyncio.sleep', return_value=None):
            result = await rapidapi_client.post_json("/test/path", {})
            
            assert result == {"status": "success"}
            assert mock_post.call_count == 2


@pytest.mark.asyncio
async def test_post_json_max_retries_exceeded():
    """Test échec après MAX_RETRIES tentatives"""
    mock_response_error = MagicMock()
    mock_response_error.status_code = 503
    mock_response_error.text = "Service unavailable"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "503", request=MagicMock(), response=mock_response_error
    )
    
    with patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        with patch('asyncio.sleep', return_value=None):
            with pytest.raises(HTTPException) as exc_info:
                await rapidapi_client.post_json("/test/path", {})
            
            assert exc_info.value.status_code == 502
            assert "après 3 tentatives" in exc_info.value.detail


@pytest.mark.asyncio
async def test_post_json_non_retriable_error():
    """Test erreur non retriable (400, 401, 404, etc.)"""
    mock_response_error = MagicMock()
    mock_response_error.status_code = 401
    mock_response_error.text = "Unauthorized"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "401", request=MagicMock(), response=mock_response_error
    )
    
    with patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        with pytest.raises(HTTPException) as exc_info:
            await rapidapi_client.post_json("/test/path", {})
        
        # Ne devrait pas retry
        assert exc_info.value.status_code == 502
        assert "HTTP 401" in exc_info.value.detail


@pytest.mark.asyncio
async def test_post_json_timeout_retry():
    """Test retry sur timeout"""
    with patch.object(rapidapi_client.client, 'post') as mock_post:
        # Premier appel: timeout, deuxième: succès
        mock_response_success = MagicMock()
        mock_response_success.status_code = 200
        mock_response_success.json.return_value = {"status": "success"}
        
        mock_post.side_effect = [
            httpx.TimeoutException("Timeout"),
            mock_response_success
        ]
        
        with patch('asyncio.sleep', return_value=None):
            result = await rapidapi_client.post_json("/test/path", {})
            
            assert result == {"status": "success"}
            assert mock_post.call_count == 2


@pytest.mark.asyncio
async def test_post_json_timeout_max_retries():
    """Test échec après MAX_RETRIES timeouts"""
    with patch.object(rapidapi_client.client, 'post', side_effect=httpx.TimeoutException("Timeout")):
        with patch('asyncio.sleep', return_value=None):
            with pytest.raises(HTTPException) as exc_info:
                await rapidapi_client.post_json("/test/path", {})
            
            assert exc_info.value.status_code == 504
            assert "Timeout" in exc_info.value.detail


@pytest.mark.asyncio
async def test_exponential_backoff():
    """Test que le backoff augmente exponentiellement"""
    import asyncio
    
    mock_response_error = MagicMock()
    mock_response_error.status_code = 503
    mock_response_error.text = "Unavailable"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "503", request=MagicMock(), response=mock_response_error
    )
    
    sleep_times = []
    
    async def mock_sleep(seconds):
        sleep_times.append(seconds)
    
    with patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        with patch('asyncio.sleep', side_effect=mock_sleep):
            try:
                await rapidapi_client.post_json("/test/path", {})
            except HTTPException:
                pass
    
    # Vérifier que les temps augmentent (avec jitter, donc pas strictement)
    assert len(sleep_times) == 2  # MAX_RETRIES - 1
    assert sleep_times[0] >= 0.5  # BASE_BACKOFF
    assert sleep_times[1] >= sleep_times[0]  # Doit augmenter


def test_endpoint_constants_loaded():
    """Test que les constantes de chemins sont chargées depuis config"""
    assert rapidapi_client.LUNAR_RETURN_REPORT_PATH is not None
    assert rapidapi_client.VOID_OF_COURSE_PATH is not None
    assert rapidapi_client.LUNAR_MANSIONS_PATH is not None
    assert rapidapi_client.NATAL_TRANSITS_PATH is not None
    assert rapidapi_client.LUNAR_PHASES_PATH is not None

