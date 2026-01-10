"""
Tests d'intégration pour les endpoints Luna Pack (/api/lunar/voc et /api/lunar/mansion)
Teste le format flat du payload et les codes d'erreur provider (502/504)
"""

import pytest
from unittest.mock import patch
from fastapi import HTTPException
from httpx import AsyncClient

from main import app


@pytest.mark.asyncio
async def test_voc_success_with_flat_payload():
    """Test /api/lunar/voc - succès avec payload flat (format HH:MM)"""
    mock_response = {
        "is_void": True,
        "void_of_course": {
            "start": "2025-12-31T10:30:00",
            "end": "2025-12-31T14:45:00"
        },
        "moon_sign": "Gemini"
    }

    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier la structure de réponse
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "void_of_course"
            assert data["data"] == mock_response
            assert data["cached"] is False

            # Vérifier que le payload a été transformé correctement
            call_args = mock_post.call_args
            transformed_payload = call_args[0][1]
            assert "datetime_location" in transformed_payload
            dtl = transformed_payload["datetime_location"]
            assert dtl["year"] == 2025
            assert dtl["month"] == 12
            assert dtl["day"] == 31
            assert dtl["hour"] == 12
            assert dtl["minute"] == 0
            assert dtl["second"] == 0
            assert dtl["latitude"] == 48.8566
            assert dtl["longitude"] == 2.3522
            assert dtl["timezone"] == "Europe/Paris"


@pytest.mark.asyncio
async def test_voc_success_with_time_hh_mm_ss():
    """Test /api/lunar/voc - accepte le format HH:MM:SS pour time"""
    mock_response = {
        "is_void": False,
        "next_void": {
            "start": "2025-12-31T18:00:00",
            "end": "2025-12-31T22:30:00"
        }
    }

    payload_with_seconds = {
        "date": "2025-12-31",
        "time": "14:30:45",  # Format HH:MM:SS
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=payload_with_seconds)

            assert response.status_code == 200
            data = response.json()
            assert data["data"] == mock_response

            # Vérifier que les secondes sont ignorées (toujours 0)
            transformed_payload = mock_post.call_args[0][1]
            dtl = transformed_payload["datetime_location"]
            assert dtl["hour"] == 14
            assert dtl["minute"] == 30
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_voc_provider_error_502():
    """Test /api/lunar/voc - erreur provider 5xx renvoie bien 502"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler une erreur 502 du provider
    error_detail = {
        "code": "PROVIDER_UNAVAILABLE",
        "message": "Service astrologique indisponible après 3 tentatives (HTTP 503)",
        "provider_error": {"error": "Service unavailable"}
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail=error_detail)):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            # Vérifier que l'erreur 502 est bien propagée (pas 500)
            assert response.status_code == 502
            error_data = response.json()
            assert error_data["detail"]["code"] == "PROVIDER_UNAVAILABLE"


@pytest.mark.asyncio
async def test_voc_provider_timeout_504():
    """Test /api/lunar/voc - timeout provider renvoie bien 504"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler un timeout (504)
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout provider après 3 tentatives")):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/voc", json=flat_payload)

            # Vérifier que l'erreur 504 est bien propagée (pas 500)
            assert response.status_code == 504
            assert "timeout" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_voc_invalid_payload_422():
    """Test /api/lunar/voc - payload invalide renvoie 422 (pas 500 ni 502)"""
    invalid_payload = {
        "date": "2025-12-31",
        # time manquant -> ValueError dans transformation
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/lunar/voc", json=invalid_payload)

        # Vérifier que c'est bien une 422 (erreur de validation)
        assert response.status_code == 422
        error_data = response.json()
        assert error_data["detail"]["code"] == "INVALID_PAYLOAD"
        assert "time" in error_data["detail"]["message"].lower()


@pytest.mark.asyncio
async def test_mansion_success_with_flat_payload():
    """Test /api/lunar/mansion - succès avec payload flat"""
    mock_response = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak",
            "interpretation": "Favorable aux nouveaux projets"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2026-01-01T16:45:00",
                "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                "to_mansion": {"number": 16, "name": "Az-Zubana"}
            }
        ],
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                },
                {
                    "change_time": "2026-01-01T16:45:00",
                    "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                    "to_mansion": {"number": 16, "name": "Az-Zubana"}
                }
            ]
        }
    }

    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris"
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier la structure de réponse
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_mansion"
            assert data["data"] == mock_response
            assert data["cached"] is False

            # Vérifier que le payload a été transformé correctement
            call_args = mock_post.call_args
            transformed_payload = call_args[0][1]
            assert "datetime_location" in transformed_payload
            dtl = transformed_payload["datetime_location"]
            assert dtl["year"] == 2025
            assert dtl["month"] == 12
            assert dtl["day"] == 31
            assert dtl["hour"] == 12
            assert dtl["minute"] == 0
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_mansion_success_with_time_hh_mm_ss():
    """Test /api/lunar/mansion - accepte le format HH:MM:SS pour time"""
    mock_response = {
        "mansion": {
            "number": 7,
            "name": "Al-Dhira",
            "interpretation": "Test"
        }
    }

    payload_with_seconds = {
        "date": "2025-12-31",
        "time": "18:45:30",  # Format HH:MM:SS
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload_with_seconds)

            assert response.status_code == 200
            data = response.json()
            assert data["data"] == mock_response

            # Vérifier que les secondes sont ignorées
            transformed_payload = mock_post.call_args[0][1]
            dtl = transformed_payload["datetime_location"]
            assert dtl["hour"] == 18
            assert dtl["minute"] == 45
            assert dtl["second"] == 0


@pytest.mark.asyncio
async def test_mansion_provider_error_502():
    """Test /api/lunar/mansion - erreur provider 5xx renvoie bien 502"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler une erreur 502 du provider
    error_detail = {
        "code": "PROVIDER_UNAVAILABLE",
        "message": "Service astrologique indisponible après 3 tentatives (HTTP 500)",
        "provider_error": {"error": "Internal server error"}
    }

    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=502, detail=error_detail)):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            # Vérifier que l'erreur 502 est bien propagée (pas 500)
            assert response.status_code == 502
            error_data = response.json()
            assert error_data["detail"]["code"] == "PROVIDER_UNAVAILABLE"


@pytest.mark.asyncio
async def test_mansion_provider_timeout_504():
    """Test /api/lunar/mansion - timeout provider renvoie bien 504"""
    flat_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    # Simuler un timeout (504)
    with patch('services.rapidapi_client.post_json', side_effect=HTTPException(status_code=504, detail="Timeout provider après 3 tentatives")):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=flat_payload)

            # Vérifier que l'erreur 504 est bien propagée (pas 500)
            assert response.status_code == 504
            assert "timeout" in response.json()["detail"].lower()


@pytest.mark.asyncio
async def test_mansion_invalid_payload_422():
    """Test /api/lunar/mansion - payload invalide renvoie 422 (pas 500 ni 502)"""
    invalid_payload = {
        "date": "2025-12-31",
        "time": "12:00",
        # latitude manquante -> ValueError dans transformation
        "longitude": 2.3522
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/api/lunar/mansion", json=invalid_payload)

        # Vérifier que c'est bien une 422 (erreur de validation)
        assert response.status_code == 422
        error_data = response.json()
        assert error_data["detail"]["code"] == "INVALID_PAYLOAD"
        assert "latitude" in error_data["detail"]["message"].lower()


@pytest.mark.asyncio
async def test_voc_and_mansion_use_same_datetime_location_format():
    """Test que VoC et Mansion utilisent le même format datetime_location"""
    mock_voc_response = {"is_void": False}
    mock_mansion_response = {"mansion": {"number": 1, "name": "Al-Sharatain"}}

    payload = {
        "date": "2025-12-31",
        "time": "23:59",
        "latitude": -33.9249,
        "longitude": 18.4241,
        "timezone": "Africa/Johannesburg"
    }

    # Test VoC transformation
    with patch('services.rapidapi_client.post_json', return_value=mock_voc_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            await client.post("/api/lunar/voc", json=payload)

            voc_transformed = mock_post.call_args[0][1]
            assert "datetime_location" in voc_transformed
            voc_dtl = voc_transformed["datetime_location"]

    # Test Mansion transformation
    with patch('services.rapidapi_client.post_json', return_value=mock_mansion_response) as mock_post:
        async with AsyncClient(app=app, base_url="http://test") as client:
            await client.post("/api/lunar/mansion", json=payload)

            mansion_transformed = mock_post.call_args[0][1]
            assert "datetime_location" in mansion_transformed
            mansion_dtl = mansion_transformed["datetime_location"]

    # Vérifier que les deux transformations sont identiques
    assert voc_dtl == mansion_dtl
    assert mansion_dtl["year"] == 2025
    assert mansion_dtl["month"] == 12
    assert mansion_dtl["day"] == 31
    assert mansion_dtl["hour"] == 23
    assert mansion_dtl["minute"] == 59
    assert mansion_dtl["second"] == 0
    assert mansion_dtl["latitude"] == -33.9249
    assert mansion_dtl["longitude"] == 18.4241
    assert mansion_dtl["timezone"] == "Africa/Johannesburg"


@pytest.mark.asyncio
async def test_mansion_deduplication_upcoming_changes():
    """Test que la déduplication fonctionne sur upcoming_changes"""
    # Mock response avec doublons dans upcoming_changes
    mock_response_with_duplicates = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },  # Doublon exact
            {
                "change_time": "2026-01-01T16:45:00",
                "from_mansion": {"number": 15, "name": "Al-Ghafr"},
                "to_mansion": {"number": 16, "name": "Az-Zubana"}
            }
        ]
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés
            upcoming_changes = data["data"]["upcoming_changes"]
            assert len(upcoming_changes) == 2  # Au lieu de 3

            # Vérifier que les entrées uniques sont conservées
            assert upcoming_changes[0]["change_time"] == "2025-12-31T15:30:00"
            assert upcoming_changes[0]["from_mansion"]["number"] == 14
            assert upcoming_changes[0]["to_mansion"]["name"] == "Al-Ghafr"

            assert upcoming_changes[1]["change_time"] == "2026-01-01T16:45:00"
            assert upcoming_changes[1]["from_mansion"]["number"] == 15
            assert upcoming_changes[1]["to_mansion"]["name"] == "Az-Zubana"


@pytest.mark.asyncio
async def test_mansion_deduplication_calendar_summary():
    """Test que la déduplication fonctionne sur calendar_summary.significant_periods"""
    # Mock response avec doublons dans significant_periods
    mock_response_with_duplicates = {
        "mansion": {
            "number": 7,
            "name": "Al-Dhira"
        },
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },  # Doublon exact
                {
                    "change_time": "2025-12-31T10:00:00",
                    "from_mansion": {"number": 7, "name": "Al-Dhira"},
                    "to_mansion": {"number": 8, "name": "An-Nathrah"}
                },  # Triple
                {
                    "change_time": "2026-01-02T14:00:00",
                    "from_mansion": {"number": 8, "name": "An-Nathrah"},
                    "to_mansion": {"number": 9, "name": "At-Tarf"}
                }
            ]
        }
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés
            significant_periods = data["data"]["calendar_summary"]["significant_periods"]
            assert len(significant_periods) == 2  # Au lieu de 4

            # Vérifier que les entrées uniques sont conservées
            assert significant_periods[0]["change_time"] == "2025-12-31T10:00:00"
            assert significant_periods[1]["change_time"] == "2026-01-02T14:00:00"


@pytest.mark.asyncio
async def test_mansion_deduplication_both():
    """Test que la déduplication fonctionne sur les deux listes en même temps"""
    # Mock response avec doublons dans les deux listes
    mock_response_with_duplicates = {
        "mansion": {
            "number": 14,
            "name": "Al-Simak"
        },
        "upcoming_changes": [
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            },
            {
                "change_time": "2025-12-31T15:30:00",
                "from_mansion": {"number": 14, "name": "Al-Simak"},
                "to_mansion": {"number": 15, "name": "Al-Ghafr"}
            }
        ],
        "calendar_summary": {
            "significant_periods": [
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                },
                {
                    "change_time": "2025-12-31T15:30:00",
                    "from_mansion": {"number": 14, "name": "Al-Simak"},
                    "to_mansion": {"number": 15, "name": "Al-Ghafr"}
                }
            ]
        }
    }

    payload = {
        "date": "2025-12-31",
        "time": "12:00",
        "latitude": 48.8566,
        "longitude": 2.3522
    }

    with patch('services.rapidapi_client.post_json', return_value=mock_response_with_duplicates):
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/api/lunar/mansion", json=payload)

            assert response.status_code == 200
            data = response.json()

            # Vérifier que les doublons ont été supprimés dans les deux listes
            upcoming_changes = data["data"]["upcoming_changes"]
            assert len(upcoming_changes) == 1

            significant_periods = data["data"]["calendar_summary"]["significant_periods"]
            assert len(significant_periods) == 1
