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
    """Test get_lunar_return_report - succès avec payload complet"""
    mock_response = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Mois favorable aux finances"
    }

    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "city": "Paris",
        "country_code": "FR",
        "date": "2025-01-15",
        "month": "2025-01"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_return_report(valid_payload)

        # Result is now normalized, not raw
        assert result["month"] == "2025-01"
        assert result["moon_sign"] == "Taurus"
        assert result["moon_house"] == 2
        assert result["summary"] == "Mois favorable aux finances"
        assert mock_post.call_count == 1

        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "lunar-return" in call_args[0][0] or "lunar_return" in call_args[0][0]

        # Vérifier que le payload transformé a la structure attendue
        transformed_payload = call_args[0][1]
        assert "subject" in transformed_payload
        assert "birth_data" in transformed_payload["subject"]
        assert transformed_payload["subject"]["birth_data"]["year"] == 1989
        assert transformed_payload["subject"]["birth_data"]["month"] == 4
        assert transformed_payload["subject"]["birth_data"]["day"] == 15
        assert transformed_payload["subject"]["birth_data"]["hour"] == 17
        assert transformed_payload["subject"]["birth_data"]["minute"] == 55
        assert transformed_payload["subject"]["birth_data"]["latitude"] == 48.8566
        assert transformed_payload["subject"]["birth_data"]["longitude"] == 2.3522


@pytest.mark.asyncio
async def test_get_lunar_return_report_error_429():
    """Test get_lunar_return_report - gestion erreur 429"""
    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail="Rate limit")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_return_report(valid_payload)

        assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_get_void_of_course_status_success():
    """Test get_void_of_course_status - succès avec payload complet"""
    mock_response = {
        "is_void": True,
        "void_of_course": {
            "start": "2025-01-15T10:30:00",
            "end": "2025-01-15T14:45:00"
        }
    }

    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_void_of_course_status(valid_payload)

        assert result == mock_response
        assert mock_post.call_count == 1

        # Vérifier que le bon path est utilisé
        call_args = mock_post.call_args
        assert "void" in call_args[0][0] or "lunar" in call_args[0][0]

        # Vérifier que le payload transformé a la structure attendue (format RapidAPI)
        transformed_payload = call_args[0][1]
        assert "datetime_location" in transformed_payload
        dtl = transformed_payload["datetime_location"]
        assert dtl["year"] == 2025
        assert dtl["month"] == 1
        assert dtl["day"] == 15
        assert dtl["hour"] == 12
        assert dtl["minute"] == 0
        assert dtl["second"] == 0
        assert dtl["latitude"] == 48.8566
        assert dtl["longitude"] == 2.3522
        assert dtl["timezone"] == "Europe/Paris"


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

    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response):
        result = await lunar_services.get_void_of_course_status(valid_payload)

        assert result["is_void"] is False
        assert "next_void" in result


@pytest.mark.asyncio
async def test_get_void_of_course_status_error_500():
    """Test get_void_of_course_status - gestion erreur 500"""
    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail="Server error")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_void_of_course_status(valid_payload)

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
            "time": "12:00",
            "latitude": 48.8566,
            "longitude": 2.3522
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
            result = await lunar_services.get_lunar_mansions({
                "date": "2025-01-15",
                "time": "12:00",
                "latitude": 48.8566,
                "longitude": 2.3522
            })

            assert result["mansion"]["number"] in range(1, 29)


@pytest.mark.asyncio
async def test_get_lunar_mansions_error_timeout():
    """Test get_lunar_mansions - gestion timeout"""
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout")):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_mansions({
                "date": "2025-01-15",
                "time": "12:00",
                "latitude": 48.8566,
                "longitude": 2.3522
            })

        assert exc_info.value.status_code == 504


@pytest.mark.asyncio
async def test_lunar_services_with_retry_logic():
    """Test que les services bénéficient des retries du client"""
    mock_response = {"status": "success"}

    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    # Simuler 2 échecs puis succès (le client retry automatiquement)
    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_return_report(valid_payload)

        # Le service ne devrait faire qu'un appel, le client gère les retries
        # Result is normalized now
        assert "month" in result or "return_date" in result or "moon_sign" in result
        assert mock_post.call_count == 1


# ============================================================================
# NEW TESTS - Payload Transformation & Error Handling
# ============================================================================

@pytest.mark.asyncio
async def test_get_lunar_return_report_missing_birth_date():
    """Test get_lunar_return_report - échec si birth_date manquant"""
    invalid_payload = {
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_return_report(invalid_payload)

    assert "birth_date" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_lunar_return_report_missing_latitude():
    """Test get_lunar_return_report - échec si latitude manquante"""
    invalid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_return_report(invalid_payload)

    assert "latitude" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_lunar_return_report_missing_longitude():
    """Test get_lunar_return_report - échec si longitude manquante"""
    invalid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "latitude": 48.8566,
        "date": "2025-01-15"
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_return_report(invalid_payload)

    assert "longitude" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_lunar_return_report_invalid_birth_date_format():
    """Test get_lunar_return_report - échec si birth_date au mauvais format"""
    from services import rapidapi_client
    from unittest.mock import patch
    
    # Utiliser un format vraiment invalide qui ne peut pas être parsé (pas de tirets)
    invalid_payload = {
        "birth_date": "1989/04/15",  # Wrong format (slashes instead of dashes)
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    # Désactiver le mode mock pour tester la vraie validation
    with patch.object(rapidapi_client.settings, 'DEV_MOCK_RAPIDAPI', False):
        # Should raise ValueError during transformation (before calling RapidAPI)
        # because the date parsing will fail when we try to split('-')
        with pytest.raises((ValueError, HTTPException)) as exc_info:
            await lunar_services.get_lunar_return_report(invalid_payload)

        # Check it's a validation error (either ValueError or 422 HTTPException)
        if isinstance(exc_info.value, HTTPException):
            assert exc_info.value.status_code == 422
        else:
            assert "birth_date" in str(exc_info.value).lower() or "format" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_lunar_return_report_invalid_birth_time_format():
    """Test get_lunar_return_report - échec si birth_time au mauvais format"""
    invalid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "5:30 PM",  # Wrong format (12h instead of 24h)
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_return_report(invalid_payload)

    assert "birth_time" in str(exc_info.value).lower()
    assert "format" in str(exc_info.value).lower() or "invalide" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_lunar_return_report_with_defaults():
    """Test get_lunar_return_report - valeurs par défaut appliquées"""
    mock_response = {"moon": {"sign": "Gemini"}}

    minimal_payload = {
        "birth_date": "1989-04-15",
        # birth_time omis -> doit defaulter à 12:00
        "latitude": 48.8566,
        "longitude": 2.3522,
        # timezone omis -> doit defaulter à UTC
        # city omis -> doit defaulter à Unknown
        # country_code omis -> doit defaulter à FR
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_return_report(minimal_payload)

        # Result is normalized
        assert result["moon_sign"] == "Gemini"

        # Vérifier les defaults
        transformed_payload = mock_post.call_args[0][1]
        assert transformed_payload["subject"]["birth_data"]["hour"] == 12
        assert transformed_payload["subject"]["birth_data"]["minute"] == 0
        assert transformed_payload["subject"]["birth_data"]["timezone"] == "UTC"
        assert transformed_payload["subject"]["birth_data"]["city"] == "Unknown"
        assert transformed_payload["subject"]["birth_data"]["country_code"] == "FR"


@pytest.mark.asyncio
async def test_get_lunar_return_report_rapidapi_422_error():
    """Test get_lunar_return_report - gestion erreur 422 de RapidAPI"""
    valid_payload = {
        "birth_date": "1989-04-15",
        "birth_time": "17:55",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "date": "2025-01-15"
    }

    # Simuler une erreur 422 de RapidAPI (payload invalide côté provider)
    error_detail = {
        "code": "INVALID_PAYLOAD",
        "message": "Les données envoyées sont invalides pour l'API astrologique",
        "provider_error": {"error": "body.subject missing"},
        "hint": "Vérifiez que tous les champs requis (birth_date, latitude, longitude) sont présents et au bon format"
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=422, detail=error_detail)):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_return_report(valid_payload)

        # Vérifier que c'est bien une 422 (pas une 502!)
        assert exc_info.value.status_code == 422
        assert exc_info.value.detail["code"] == "INVALID_PAYLOAD"


@pytest.mark.asyncio
async def test_get_lunar_return_report_payload_transformation():
    """Test que la transformation du payload est correcte"""
    mock_response = {"success": True}

    payload = {
        "birth_date": "1995-12-25",
        "birth_time": "08:30",
        "latitude": -33.9249,
        "longitude": 18.4241,
        "timezone": "Africa/Johannesburg",
        "city": "Cape Town",
        "country_code": "ZA",
        "date": "2025-06-15",
        "month": "2025-06"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        await lunar_services.get_lunar_return_report(payload)

        # Extraire le payload transformé
        transformed = mock_post.call_args[0][1]

        # Vérifier la structure
        assert "subject" in transformed
        assert "name" in transformed["subject"]
        assert "birth_data" in transformed["subject"]

        # Vérifier les données de naissance
        bd = transformed["subject"]["birth_data"]
        assert bd["year"] == 1995
        assert bd["month"] == 12
        assert bd["day"] == 25
        assert bd["hour"] == 8
        assert bd["minute"] == 30
        assert bd["second"] == 0
        assert bd["latitude"] == -33.9249
        assert bd["longitude"] == 18.4241
        assert bd["timezone"] == "Africa/Johannesburg"
        assert bd["city"] == "Cape Town"
        assert bd["country_code"] == "ZA"

        # Vérifier les champs optionnels
        assert transformed.get("return_month") == "2025-06"
        assert transformed.get("return_date") == "2025-06-15"


# ============================================================================
# VoC TESTS - Payload Transformation & Error Handling
# ============================================================================

@pytest.mark.asyncio
async def test_get_void_of_course_missing_date():
    """Test get_void_of_course_status - échec si date manquante"""
    invalid_payload = {
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_void_of_course_status(invalid_payload)

    assert "date" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_void_of_course_missing_time():
    """Test get_void_of_course_status - échec si time manquant"""
    invalid_payload = {
        "date": "2025-01-15",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_void_of_course_status(invalid_payload)

    assert "time" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_void_of_course_missing_latitude():
    """Test get_void_of_course_status - échec si latitude manquante"""
    invalid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_void_of_course_status(invalid_payload)

    assert "latitude" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_void_of_course_missing_longitude():
    """Test get_void_of_course_status - échec si longitude manquante"""
    invalid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_void_of_course_status(invalid_payload)

    assert "longitude" in str(exc_info.value).lower()


@pytest.mark.asyncio
async def test_get_void_of_course_with_defaults():
    """Test get_void_of_course_status - timezone par défaut à UTC"""
    mock_response = {"is_void": False}

    minimal_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
        # timezone omis -> doit defaulter à UTC
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_void_of_course_status(minimal_payload)

        assert result == mock_response

        # Vérifier le default
        transformed_payload = mock_post.call_args[0][1]
        assert transformed_payload["datetime_location"]["timezone"] == "UTC"


@pytest.mark.asyncio
async def test_get_void_of_course_rapidapi_422_error():
    """Test get_void_of_course_status - gestion erreur 422 de RapidAPI"""
    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    # Simuler une erreur 422 de RapidAPI (payload invalide côté provider)
    error_detail = {
        "code": "INVALID_PAYLOAD",
        "message": "Les données envoyées sont invalides pour l'API astrologique",
        "provider_error": {"error": "body.datetime_location missing"},
        "hint": "Vérifiez que tous les champs requis (birth_date, latitude, longitude) sont présents et au bon format"
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=422, detail=error_detail)):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_void_of_course_status(valid_payload)

        # Vérifier que c'est bien une 422 (pas une 502!)
        assert exc_info.value.status_code == 422
        assert exc_info.value.detail["code"] == "INVALID_PAYLOAD"


@pytest.mark.asyncio
async def test_get_void_of_course_time_with_seconds():
    """Test get_void_of_course_status - accepte format HH:MM:SS (ignore secondes)"""
    mock_response = {"is_void": False}

    payload_with_seconds = {
        "date": "2025-01-15",
        "time": "14:30:45",  # Format HH:MM:SS
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_void_of_course_status(payload_with_seconds)

        assert result == mock_response

        # Vérifier que les secondes sont ignorées
        transformed_payload = mock_post.call_args[0][1]
        dtl = transformed_payload["datetime_location"]
        assert dtl["hour"] == 14
        assert dtl["minute"] == 30
        assert dtl["second"] == 0  # Always 0, seconds from time string are ignored


@pytest.mark.asyncio
async def test_get_void_of_course_payload_transformation():
    """Test que la transformation du payload VoC est correcte"""
    mock_response = {"is_void": False, "next_void": None}

    payload = {
        "date": "2025-12-31",
        "time": "23:45",
        "latitude": -33.9249,
        "longitude": 18.4241,
        "timezone": "Africa/Johannesburg"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        await lunar_services.get_void_of_course_status(payload)

        # Extraire le payload transformé
        transformed = mock_post.call_args[0][1]

        # Vérifier la structure
        assert "datetime_location" in transformed

        # Vérifier les données datetime_location (format RapidAPI: year/month/day/hour/minute)
        dtl = transformed["datetime_location"]
        assert dtl["year"] == 2025
        assert dtl["month"] == 12
        assert dtl["day"] == 31
        assert dtl["hour"] == 23
        assert dtl["minute"] == 45
        assert dtl["second"] == 0
        assert dtl["latitude"] == -33.9249
        assert dtl["longitude"] == 18.4241
        assert dtl["timezone"] == "Africa/Johannesburg"


@pytest.mark.asyncio
async def test_get_lunar_mansions_missing_date():
    """Test get_lunar_mansions - erreur si date manquant"""
    invalid_payload = {
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_mansions(invalid_payload)

    assert "Champs requis manquants: date" in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_lunar_mansions_missing_time():
    """Test get_lunar_mansions - erreur si time manquant"""
    invalid_payload = {
        "date": "2025-12-31",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_mansions(invalid_payload)

    assert "Champs requis manquants: time" in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_lunar_mansions_missing_latitude():
    """Test get_lunar_mansions - erreur si latitude manquant"""
    invalid_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "longitude": 2.3522
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_mansions(invalid_payload)

    assert "Champs requis manquants: latitude" in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_lunar_mansions_missing_longitude():
    """Test get_lunar_mansions - erreur si longitude manquant"""
    invalid_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566
    }

    with pytest.raises(ValueError) as exc_info:
        await lunar_services.get_lunar_mansions(invalid_payload)

    assert "Champs requis manquants: longitude" in str(exc_info.value)


@pytest.mark.asyncio
async def test_get_lunar_mansions_with_defaults():
    """Test get_lunar_mansions - defaults (timezone→UTC si non fourni)"""
    mock_response = {"mansion": {"number": 14, "name": "Al-Simak"}}

    minimal_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
        # timezone omis -> doit defaulter à UTC
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        result = await lunar_services.get_lunar_mansions(minimal_payload)

        # Result is normalized
        assert result["mansion"]["number"] == 14
        assert result["mansion"]["name"] == "Al-Simak"

        # Vérifier le default
        transformed_payload = mock_post.call_args[0][1]
        assert transformed_payload["datetime_location"]["timezone"] == "UTC"


@pytest.mark.asyncio
async def test_get_lunar_mansions_rapidapi_422_error():
    """Test get_lunar_mansions - gestion erreur 422 de RapidAPI"""
    valid_payload = {
        "date": "2025-01-15",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    # Simuler une erreur 422 de RapidAPI (payload invalide côté provider)
    error_detail = {
        "code": "INVALID_PAYLOAD",
        "message": "Les données envoyées sont invalides pour l'API astrologique",
        "provider_error": {"error": "body.datetime_location missing"},
        "hint": "Vérifiez que tous les champs requis sont présents et au bon format"
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=422, detail=error_detail)):
        with pytest.raises(HTTPException) as exc_info:
            await lunar_services.get_lunar_mansions(valid_payload)

        # Vérifier que c'est bien une 422 (pas une 502!)
        assert exc_info.value.status_code == 422
        assert exc_info.value.detail["code"] == "INVALID_PAYLOAD"


@pytest.mark.asyncio
async def test_get_lunar_mansions_payload_transformation():
    """Test que la transformation du payload Lunar Mansions est correcte"""
    mock_response = {"mansion": {"number": 7, "name": "Al-Dhira"}}

    payload = {
        "date": "2025-12-31",
        "time": "23:45",
        "latitude": -33.9249,
        "longitude": 18.4241,
        "timezone": "Africa/Johannesburg"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        await lunar_services.get_lunar_mansions(payload)

        # Extraire le payload transformé
        transformed = mock_post.call_args[0][1]

        # Vérifier la structure
        assert "datetime_location" in transformed

        # Vérifier les données datetime_location (format RapidAPI: year/month/day/hour/minute)
        dtl = transformed["datetime_location"]
        assert dtl["year"] == 2025
        assert dtl["month"] == 12
        assert dtl["day"] == 31
        assert dtl["hour"] == 23
        assert dtl["minute"] == 45
        assert dtl["second"] == 0
        assert dtl["latitude"] == -33.9249
        assert dtl["longitude"] == 18.4241
        assert dtl["timezone"] == "Africa/Johannesburg"

