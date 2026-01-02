"""
Test pour reproduire et vérifier le fix du bug MissingGreenlet sur /api/lunar-returns/current

Bug original:
- Appel /current avec DB vide → génération rolling → commit → accès current_user.id
- SQLAlchemy tente un lazy-load sync → MissingGreenlet

Fix:
- Extraire user_id = current_user.id AVANT tout await/commit
- Utiliser user_id (int primitif) dans toutes les queries
"""

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from main import app
from database import AsyncSessionLocal
from models.lunar_return import LunarReturn
from models.user import User


@pytest.fixture
async def client():
    """Client HTTP async pour tester l'API"""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def db_session():
    """Session DB async pour setup/cleanup"""
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
async def test_user(db_session: AsyncSession):
    """Créer un user de test avec dev_external_id"""
    # Vérifier si le user existe déjà
    result = await db_session.execute(
        select(User).where(User.dev_external_id == "550e8400-e29b-41d4-a716-446655440000")
    )
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            email="test+550e8400@local.dev",
            hashed_password="$2b$12$fake_hash",
            dev_external_id="550e8400-e29b-41d4-a716-446655440000",
            is_active=True,
            is_premium=False,
        )
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)

    yield user

    # Cleanup: supprimer les lunar_returns du user de test
    await db_session.execute(
        delete(LunarReturn).where(LunarReturn.user_id == user.id)
    )
    await db_session.commit()


@pytest.mark.asyncio
async def test_current_after_purge_no_missinggreenlet(client: AsyncClient, test_user: User, db_session: AsyncSession):
    """
    Test: Appeler /current avec DB vide ne doit PAS provoquer MissingGreenlet

    Scenario:
    1. Purge lunar_returns pour vider la table
    2. Appel /current → devrait générer rolling et renvoyer 200
    3. Vérifier qu'aucune exception MissingGreenlet n'est levée
    """
    # Étape 1: Purge
    purge_response = await client.post(
        "/api/lunar-returns/dev/purge",
        headers={"X-Dev-External-Id": "550e8400-e29b-41d4-a716-446655440000"},
    )
    assert purge_response.status_code == 200, f"Purge failed: {purge_response.text}"

    purge_data = purge_response.json()
    print(f"Purge: deleted_count={purge_data.get('deleted_count')}")

    # Étape 2: Appel /current avec DB vide (devrait générer rolling)
    current_response = await client.get(
        "/api/lunar-returns/current",
        headers={"X-Dev-External-Id": "550e8400-e29b-41d4-a716-446655440000"},
    )

    # Vérifier: pas de 500 (MissingGreenlet provoque un 500)
    assert current_response.status_code != 500, f"MissingGreenlet error (500): {current_response.text}"

    # Accepter 200 (révolution trouvée/générée) ou 204/null (DB vraiment vide en edge case)
    assert current_response.status_code in [200, 204], f"Unexpected status: {current_response.status_code}"

    if current_response.status_code == 200:
        current_data = current_response.json()
        print(f"Current lunar return: month={current_data.get('month')}, id={current_data.get('id')}")

        # Vérifier structure minimale
        assert "month" in current_data, "Response should contain 'month'"
        assert "return_date" in current_data, "Response should contain 'return_date'"


@pytest.mark.asyncio
async def test_current_concurrent_requests(client: AsyncClient, test_user: User, db_session: AsyncSession):
    """
    Test: Concurrence sur /current (2 requêtes simultanées) ne doit pas crash

    Scenario:
    1. Purge
    2. Lancer 2 appels /current simultanés
    3. Vérifier que les deux renvoient 200 (ou l'un renvoie 200, l'autre peut retry)
    """
    import asyncio

    # Purge
    purge_response = await client.post(
        "/api/lunar-returns/dev/purge",
        headers={"X-Dev-External-Id": "550e8400-e29b-41d4-a716-446655440000"},
    )
    assert purge_response.status_code == 200

    # Lancer 2 requêtes simultanées
    async def call_current():
        return await client.get(
            "/api/lunar-returns/current",
            headers={"X-Dev-External-Id": "550e8400-e29b-41d4-a716-446655440000"},
        )

    responses = await asyncio.gather(call_current(), call_current())

    # Vérifier qu'aucune n'a crash avec 500
    for i, resp in enumerate(responses):
        assert resp.status_code != 500, f"Request {i+1} failed with 500: {resp.text}"
        print(f"Request {i+1}: status={resp.status_code}")

    # Au moins une des deux doit renvoyer 200 (l'autre peut être 200 ou retry)
    success_count = sum(1 for r in responses if r.status_code == 200)
    assert success_count >= 1, "At least one request should succeed with 200"
