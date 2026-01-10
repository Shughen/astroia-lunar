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
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post', return_value=mock_response) as mock_post:
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
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post') as mock_post:
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
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post') as mock_post:
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
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        with patch('asyncio.sleep', return_value=None):
            with pytest.raises(HTTPException) as exc_info:
                await rapidapi_client.post_json("/test/path", {})
            
            assert exc_info.value.status_code == 502
            # Le detail est maintenant un dict avec code, message, provider_error
            assert isinstance(exc_info.value.detail, dict)
            assert exc_info.value.detail["code"] == "PROVIDER_UNAVAILABLE"
            assert "après 3 tentatives" in exc_info.value.detail["message"]


@pytest.mark.asyncio
async def test_post_json_non_retriable_error():
    """Test erreur non retriable (400, 401, 404, etc.)"""
    mock_response_error = MagicMock()
    mock_response_error.status_code = 401
    mock_response_error.text = "Unauthorized"
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "401", request=MagicMock(), response=mock_response_error
    )
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        with pytest.raises(HTTPException) as exc_info:
            await rapidapi_client.post_json("/test/path", {})
        
        # Ne devrait pas retry
        assert exc_info.value.status_code == 502
        # Le detail est maintenant un dict avec code, message, provider_error
        assert isinstance(exc_info.value.detail, dict)
        assert exc_info.value.detail["code"] == "PROVIDER_AUTH_ERROR"
        assert "authentification" in exc_info.value.detail["message"].lower()


@pytest.mark.asyncio
async def test_post_json_timeout_retry():
    """Test retry sur timeout"""
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post') as mock_post:
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
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post', side_effect=httpx.TimeoutException("Timeout")):
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
    
    # Désactiver le mode mock pour ce test
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False), \
         patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
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


@pytest.mark.asyncio
async def test_post_json_403_not_subscribed_fallback_mock():
    """Test fallback sur mock quand RapidAPI retourne 403 'not subscribed'"""
    mock_response_error = MagicMock()
    mock_response_error.status_code = 403
    mock_response_error.text = '{"message": "You are not subscribed to this API."}'
    mock_response_error.json.return_value = {"message": "You are not subscribed to this API."}
    mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
        "403", request=MagicMock(), response=mock_response_error
    )

    with patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
        # Appel sur endpoint Lunar Mansion (qui a un mock disponible)
        result = await rapidapi_client.post_json(
            rapidapi_client.LUNAR_MANSIONS_PATH,
            {
                "datetime_location": {
                    "year": 2025,
                    "month": 1,
                    "day": 15,
                    "hour": 12,
                    "minute": 0,
                    "second": 0,
                    "latitude": 48.8566,
                    "longitude": 2.3522,
                    "timezone": "Europe/Paris"
                }
            }
        )

        # Vérifier que le résultat est un mock (pas une erreur)
        assert result is not None
        assert result.get("_mock") is True
        assert result.get("_reason") == "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
        assert "mansion" in result
        assert result["mansion"]["number"] >= 1
        assert result["mansion"]["number"] <= 28


@pytest.mark.asyncio
async def test_post_json_429_rate_limit_returns_429():
    """Test que 429 (rate limit) retourne bien 429 avec code RAPIDAPI_RATE_LIMIT après retries"""
    from config import settings

    # S'assurer que DEV_MOCK_RAPIDAPI est désactivé pour ce test
    original_value = settings.DEV_MOCK_RAPIDAPI
    settings.DEV_MOCK_RAPIDAPI = False

    try:
        mock_response_error = MagicMock()
        mock_response_error.status_code = 429
        mock_response_error.text = '{"message": "Rate limit exceeded"}'
        mock_response_error.json.return_value = {"message": "Rate limit exceeded"}
        mock_response_error.raise_for_status.side_effect = httpx.HTTPStatusError(
            "429", request=MagicMock(), response=mock_response_error
        )

        with patch.object(rapidapi_client.client, 'post', return_value=mock_response_error):
            with patch('asyncio.sleep', return_value=None):
                with pytest.raises(HTTPException) as exc_info:
                    await rapidapi_client.post_json("/test/path", {})

                # Vérifier que c'est bien un 429 avec le bon code
                assert exc_info.value.status_code == 429
                assert isinstance(exc_info.value.detail, dict)
                assert exc_info.value.detail["code"] == "RAPIDAPI_RATE_LIMIT"
                assert "Rate limit" in exc_info.value.detail["message"]
    finally:
        settings.DEV_MOCK_RAPIDAPI = original_value


@pytest.mark.asyncio
async def test_dev_mock_rapidapi_enabled():
    """Test que DEV_MOCK_RAPIDAPI=true bypass RapidAPI et retourne mock"""
    from config import settings

    # Temporairement activer le mode mock
    original_value = settings.DEV_MOCK_RAPIDAPI
    settings.DEV_MOCK_RAPIDAPI = True

    try:
        # Appel direct sans mocker httpx - le client ne devrait même pas être appelé
        result = await rapidapi_client.post_json(
            rapidapi_client.VOID_OF_COURSE_PATH,
            {
                "datetime_location": {
                    "year": 2025,
                    "month": 1,
                    "day": 15,
                    "hour": 12,
                    "minute": 0,
                    "second": 0,
                    "latitude": 48.8566,
                    "longitude": 2.3522,
                    "timezone": "Europe/Paris"
                }
            }
        )

        # Vérifier que le résultat est un mock
        assert result is not None
        assert result.get("_mock") is True
        assert "is_void" in result or "void_of_course" in result or "next_void" in result

    finally:
        # Restaurer la valeur originale
        settings.DEV_MOCK_RAPIDAPI = original_value


@pytest.mark.asyncio
async def test_mock_lunar_return_report():
    """Test génération mock pour Lunar Return Report"""
    from config import settings

    original_value = settings.DEV_MOCK_RAPIDAPI
    settings.DEV_MOCK_RAPIDAPI = True

    try:
        result = await rapidapi_client.post_json(
            rapidapi_client.LUNAR_RETURN_REPORT_PATH,
            {
                "subject": {
                    "name": "Test User",
                    "birth_data": {
                        "year": 1990,
                        "month": 5,
                        "day": 15,
                        "hour": 14,
                        "minute": 30,
                        "second": 0,
                        "latitude": 48.8566,
                        "longitude": 2.3522,
                        "timezone": "Europe/Paris",
                        "city": "Paris",
                        "country_code": "FR"
                    }
                },
                "return_month": "2025-01"
            }
        )

        # Vérifier structure du mock
        assert result is not None
        assert result.get("_mock") is True
        assert "return_date" in result
        assert "moon" in result
        assert result["moon"]["sign"] in ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                                           "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
        assert 1 <= result["moon"]["house"] <= 12

    finally:
        settings.DEV_MOCK_RAPIDAPI = original_value


@pytest.mark.asyncio
async def test_mock_metadata_preserved_after_normalization():
    """Test que les champs _mock et _reason sont préservés après normalisation"""
    from services.lunar_normalization import normalize_lunar_mansion_response, normalize_lunar_return_report_response

    # Mock response avec metadata
    mock_mansion = {
        "mansion": {
            "number": 5,
            "name": "Al-Haq'ah"
        },
        "_mock": True,
        "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    }

    # Normaliser
    normalized = normalize_lunar_mansion_response(mock_mansion)

    # Vérifier que _mock et _reason sont préservés
    assert normalized.get("_mock") is True
    assert normalized.get("_reason") == "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    assert normalized["mansion"]["number"] == 5

    # Test pour Lunar Return Report
    mock_return = {
        "return_date": "2025-01-15T10:30:00",
        "moon": {
            "sign": "Gemini",
            "house": 3
        },
        "_mock": True,
        "_reason": "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    }

    normalized_return = normalize_lunar_return_report_response(mock_return, request_month="2025-01")

    assert normalized_return.get("_mock") is True
    assert normalized_return.get("_reason") == "DEV_MOCK_RAPIDAPI enabled or RapidAPI not subscribed"
    assert normalized_return["moon_sign"] == "Gemini"

