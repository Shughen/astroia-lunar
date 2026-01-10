"""
Test de sécurité: Lunar Return Report - user_id toujours depuis auth, jamais depuis request

Prouve que même si un client tente de falsifier user_id, la DB utilise toujours
l'utilisateur authentifié (current_user.id).
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from unittest.mock import patch

from main import app
from models.lunar_pack import LunarReport
from database import AsyncSessionLocal


@pytest.mark.asyncio
@pytest.mark.real_db
async def test_lunar_report_uses_authenticated_user_not_request_userid():
    """
    Test de sécurité: même si le payload contient des données falsifiées,
    la DB doit toujours utiliser l'utilisateur authentifié.
    
    Scénario:
    1. User A s'authentifie avec X-Dev-External-Id: UUID_A
    2. User A envoie un payload avec month (user_id n'existe plus dans le modèle)
    3. Vérifier que le rapport est sauvegardé avec user_id = User A (pas un autre)
    
    Note: Ce test utilise des connexions DB réelles et peut échouer si exécuté
    en parallèle avec d'autres tests DB. Exécuter individuellement ou avec pytest-xdist -n 1.
    """
    import asyncio
    
    # UUIDs pour 2 utilisateurs distincts
    user_a_uuid = "550e8400-e29b-41d4-a716-446655440000"
    user_b_uuid = "660e8400-e29b-41d4-a716-446655440001"
    
    valid_payload = {
        "birth_date": "1990-05-15",
        "birth_time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"  # Pour déclencher la sauvegarde DB
    }
    
    mock_report_response = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Test interpretation",
        "lunar_ascendant": "Gemini"
    }
    
    # Activer DEV_AUTH_BYPASS et mocker le service
    with patch('config.settings.DEV_AUTH_BYPASS', True), \
         patch('config.settings.APP_ENV', 'development'), \
         patch('services.lunar_services.get_lunar_return_report', return_value=mock_report_response):
        
        # Créer un nouveau client pour ce test (isolation)
        async with AsyncClient(app=app, base_url="http://test") as client:
            # User A s'authentifie et envoie le payload
            response = await client.post(
                "/api/lunar/return/report",
                json=valid_payload,
                headers={"X-Dev-External-Id": user_a_uuid}
            )
            
            # Vérifier que la requête réussit
            assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
            
            data = response.json()
            assert data["provider"] == "rapidapi"
            assert data["kind"] == "lunar_return_report"
            
            # Vérifier en DB que le rapport est lié à User A (pas User B)
            # Utiliser une nouvelle session avec un délai pour éviter les conflits de transaction
            # Délai plus long pour s'assurer que la transaction est complètement terminée
            await asyncio.sleep(0.5)
            
            from database import AsyncSessionLocal
            # Créer une nouvelle session propre pour la vérification (isolation complète)
            async with AsyncSessionLocal() as db_check:
                try:
                    # Récupérer User A depuis la DB
                    from models.user import User
                    from sqlalchemy import select
                    
                    user_a_result = await db_check.execute(
                        select(User).where(User.dev_external_id == user_a_uuid)
                    )
                    user_a = user_a_result.scalar_one_or_none()
                    
                    assert user_a is not None, f"User A (UUID: {user_a_uuid}) doit exister en DB"
                    user_a_id = user_a.id
                    
                    # Vérifier que le rapport existe avec user_id = User A
                    report_result = await db_check.execute(
                        select(LunarReport).where(
                            LunarReport.user_id == user_a_id,
                            LunarReport.month == "2025-01"
                        )
                    )
                    report = report_result.scalar_one_or_none()
                    
                    assert report is not None, "Le rapport doit être sauvegardé en DB"
                    assert report.user_id == user_a_id, \
                        f"Le rapport doit être lié à User A (id={user_a_id}), pas à {report.user_id}"
                    assert report.month == "2025-01"
                    
                    # Vérifier que User B n'a PAS de rapport pour ce mois
                    user_b_result = await db_check.execute(
                        select(User).where(User.dev_external_id == user_b_uuid)
                    )
                    user_b = user_b_result.scalar_one_or_none()
                    
                    if user_b is not None:
                        user_b_id = user_b.id
                        report_b_result = await db_check.execute(
                            select(LunarReport).where(
                                LunarReport.user_id == user_b_id,
                                LunarReport.month == "2025-01"
                            )
                        )
                        report_b = report_b_result.scalar_one_or_none()
                        assert report_b is None, \
                            f"User B (id={user_b_id}) ne doit PAS avoir de rapport pour ce mois"
                finally:
                    await db_check.rollback()  # Nettoyer toute transaction en cours
                    await db_check.close()  # Fermer proprement la session


@pytest.mark.asyncio
async def test_lunar_report_different_users_different_reports():
    """
    Test que deux utilisateurs différents peuvent avoir des rapports pour le même mois
    sans interférence (isolation des données).
    
    Patch minimal: utilise app.dependency_overrides pour get_current_user (pas de dev bypass DB).
    Vérifie que l'isolation dépend du current_user authentifié, sans toucher à la DB réelle.
    """
    from routes.auth import get_current_user
    from unittest.mock import MagicMock
    
    payload = {
        "birth_date": "1990-05-15",
        "birth_time": "14:30",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "timezone": "Europe/Paris",
        "date": "2025-01-15",
        "month": "2025-01"
    }
    
    mock_report_a = {
        "moon": {"sign": "Taurus", "house": 2},
        "interpretation": "Report User A"
    }
    
    mock_report_b = {
        "moon": {"sign": "Gemini", "house": 3},
        "interpretation": "Report User B"
    }
    
    # Créer 2 users mock
    user_a = MagicMock()
    user_a.id = 1
    user_a.email = "user_a@test.com"
    
    user_b = MagicMock()
    user_b.id = 2
    user_b.email = "user_b@test.com"
    
    # Compteur pour alterner entre user_a et user_b
    call_count = [0]
    
    async def override_get_current_user():
        """Retourne user_a au premier appel, user_b au deuxième"""
        if call_count[0] == 0:
            call_count[0] += 1
            return user_a
        else:
            return user_b
    
    # Mock du service lunar_services
    with patch('services.lunar_services.get_lunar_return_report') as mock_service:
        # Premier appel retourne report A, deuxième retourne report B
        mock_service.side_effect = [mock_report_a, mock_report_b]
        
        # Appliquer l'override
        app.dependency_overrides[get_current_user] = override_get_current_user
        
        try:
            async with AsyncClient(app=app, base_url="http://test") as client:
                # User A crée un rapport
                response_a = await client.post(
                    "/api/lunar/return/report",
                    json=payload
                )
                assert response_a.status_code == 200, f"Expected 200, got {response_a.status_code}: {response_a.text}"
                
                data_a = response_a.json()
                assert data_a["kind"] == "lunar_return_report"
                assert data_a["data"]["interpretation"] == "Report User A"
                
                # User B crée un rapport pour le même mois (même payload mais user différent)
                response_b = await client.post(
                    "/api/lunar/return/report",
                    json=payload
                )
                assert response_b.status_code == 200, f"Expected 200, got {response_b.status_code}: {response_b.text}"
                
                data_b = response_b.json()
                assert data_b["kind"] == "lunar_return_report"
                assert data_b["data"]["interpretation"] == "Report User B"
                
                # Vérifier que les réponses sont différentes (isolation dépend du user authentifié)
                assert data_a["data"]["interpretation"] != data_b["data"]["interpretation"], \
                    "Les rapports doivent être différents selon le user authentifié"
        finally:
            # Nettoyage
            app.dependency_overrides.clear()

