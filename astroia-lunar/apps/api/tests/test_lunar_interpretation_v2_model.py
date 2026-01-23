"""
Tests pour les modèles LunarInterpretation et LunarInterpretationTemplate (V2)

Pattern de test:
1. Utilise @pytest.mark.real_db (vraie DB PostgreSQL)
2. Tests CRUD basiques
3. Tests constraints UNIQUE
4. Tests relations FK
5. Skip automatique si DB inaccessible

Note: Ces tests nécessitent une DB PostgreSQL accessible.
Si DB inaccessible, les tests sont automatiquement skippés.
"""

import pytest
import pytest_asyncio
from sqlalchemy import text, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from database import AsyncSessionLocal
from models.user import User
from models.lunar_return import LunarReturn
from models.lunar_interpretation import LunarInterpretation
from models.lunar_interpretation_template import LunarInterpretationTemplate
from datetime import datetime, timezone
import uuid


@pytest_asyncio.fixture
async def async_db_session():
    """
    Fixture qui crée une session DB asynchrone pour les tests
    Skip automatiquement si DB inaccessible
    """
    async with AsyncSessionLocal() as session:
        # Tester la connexion
        try:
            await session.execute(text("SELECT 1"))
        except Exception as e:
            pytest.skip(f"DB not accessible: {str(e)[:100]}")

        yield session


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_create_lunar_interpretation_template(async_db_session: AsyncSession):
    """
    Test création d'un template 'full' complet
    """
    template = LunarInterpretationTemplate(
        template_type="full",
        moon_sign="Aries",
        moon_house=1,
        lunar_ascendant="Leo",
        version=2,
        lang="fr",
        template_text="Template test Aries M1 Asc Leo",
        model_used="claude-opus-4-5-test"
    )

    async_db_session.add(template)
    await async_db_session.commit()
    await async_db_session.refresh(template)

    # Vérifications
    assert template.id is not None
    assert template.template_type == "full"
    assert template.moon_sign == "Aries"
    assert template.moon_house == 1
    assert template.lunar_ascendant == "Leo"
    assert template.version == 2
    assert template.lang == "fr"
    assert template.created_at is not None

    # Cleanup
    await async_db_session.delete(template)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_unique_constraint_template(async_db_session: AsyncSession):
    """
    Test contrainte UNIQUE sur lunar_interpretation_templates
    """
    # Créer premier template
    template1 = LunarInterpretationTemplate(
        template_type="full",
        moon_sign="Taurus",
        moon_house=2,
        lunar_ascendant="Virgo",
        version=2,
        lang="fr",
        template_text="Template 1"
    )
    async_db_session.add(template1)
    await async_db_session.commit()

    # Essayer de créer un doublon (même clé composite)
    template2 = LunarInterpretationTemplate(
        template_type="full",
        moon_sign="Taurus",
        moon_house=2,
        lunar_ascendant="Virgo",
        version=2,
        lang="fr",
        template_text="Template 2 (doublon)"
    )
    async_db_session.add(template2)

    # Doit lever une IntegrityError
    with pytest.raises(IntegrityError):
        await async_db_session.commit()

    # Rollback après l'erreur
    await async_db_session.rollback()

    # Cleanup
    await async_db_session.delete(template1)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_query_template_by_combination(async_db_session: AsyncSession):
    """
    Test query d'un template par combinaison exacte
    """
    # Créer template
    template = LunarInterpretationTemplate(
        template_type="climate",
        moon_sign="Gemini",
        version=2,
        lang="fr",
        template_text="Ambiance Gemini test"
    )
    async_db_session.add(template)
    await async_db_session.commit()

    # Query par combinaison
    stmt = select(LunarInterpretationTemplate).where(
        LunarInterpretationTemplate.template_type == "climate",
        LunarInterpretationTemplate.moon_sign == "Gemini",
        LunarInterpretationTemplate.version == 2,
        LunarInterpretationTemplate.lang == "fr"
    )
    result = await async_db_session.execute(stmt)
    found_template = result.scalar_one_or_none()

    assert found_template is not None
    assert found_template.template_text == "Ambiance Gemini test"

    # Cleanup
    await async_db_session.delete(template)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_create_lunar_interpretation_with_user_and_return(async_db_session: AsyncSession):
    """
    Test création d'une interprétation lunaire complète (avec User et LunarReturn)
    """
    # Créer User
    user = User(
        email=f"test_lunar_{uuid.uuid4().hex[:8]}@example.com",
        hashed_password="hashed_pw_test"
    )
    async_db_session.add(user)
    await async_db_session.commit()
    await async_db_session.refresh(user)

    # Créer LunarReturn
    lunar_return = LunarReturn(
        user_id=user.id,
        month="2024-05",
        return_date=datetime(2024, 5, 15, 12, 0, 0, tzinfo=timezone.utc),
        moon_sign="Cancer",
        moon_house=4,
        lunar_ascendant="Capricorn"
    )
    async_db_session.add(lunar_return)
    await async_db_session.commit()
    await async_db_session.refresh(lunar_return)

    # Créer Interprétation
    interpretation = LunarInterpretation(
        user_id=user.id,
        lunar_return_id=lunar_return.id,
        subject="full",
        version=2,
        lang="fr",
        input_json={"moon_sign": "Cancer", "moon_house": 4},
        output_text="Interprétation test Cancer M4",
        model_used="claude-opus-4-5-test"
    )
    async_db_session.add(interpretation)
    await async_db_session.commit()
    await async_db_session.refresh(interpretation)

    # Vérifications
    assert interpretation.id is not None
    assert interpretation.user_id == user.id
    assert interpretation.lunar_return_id == lunar_return.id
    assert interpretation.subject == "full"
    assert interpretation.output_text == "Interprétation test Cancer M4"
    assert interpretation.created_at is not None

    # Cleanup (ordre important : interpretation → lunar_return → user)
    await async_db_session.delete(interpretation)
    await async_db_session.delete(lunar_return)
    await async_db_session.delete(user)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_unique_constraint_lunar_interpretation(async_db_session: AsyncSession):
    """
    Test contrainte UNIQUE sur (lunar_return_id, subject, lang, version)
    """
    # Créer User et LunarReturn
    user = User(
        email=f"test_unique_{uuid.uuid4().hex[:8]}@example.com",
        hashed_password="hashed_pw_test"
    )
    async_db_session.add(user)
    await async_db_session.commit()
    await async_db_session.refresh(user)

    lunar_return = LunarReturn(
        user_id=user.id,
        month="2024-06",
        return_date=datetime(2024, 6, 15, 12, 0, 0, tzinfo=timezone.utc),
        moon_sign="Leo",
        moon_house=5,
        lunar_ascendant="Aquarius"
    )
    async_db_session.add(lunar_return)
    await async_db_session.commit()
    await async_db_session.refresh(lunar_return)

    # Créer première interprétation
    interpretation1 = LunarInterpretation(
        user_id=user.id,
        lunar_return_id=lunar_return.id,
        subject="full",
        version=2,
        lang="fr",
        input_json={},
        output_text="Première interprétation"
    )
    async_db_session.add(interpretation1)
    await async_db_session.commit()

    # Essayer de créer un doublon
    interpretation2 = LunarInterpretation(
        user_id=user.id,
        lunar_return_id=lunar_return.id,
        subject="full",  # Même
        version=2,       # Même
        lang="fr",       # Même
        input_json={},
        output_text="Deuxième interprétation (doublon)"
    )
    async_db_session.add(interpretation2)

    # Doit lever une IntegrityError
    with pytest.raises(IntegrityError):
        await async_db_session.commit()

    # Rollback
    await async_db_session.rollback()

    # Cleanup
    await async_db_session.delete(interpretation1)
    await async_db_session.delete(lunar_return)
    await async_db_session.delete(user)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_cascade_delete_lunar_return(async_db_session: AsyncSession):
    """
    Test cascade delete quand on supprime un LunarReturn
    """
    # Créer User et LunarReturn
    user = User(
        email=f"test_cascade_{uuid.uuid4().hex[:8]}@example.com",
        hashed_password="hashed_pw_test"
    )
    async_db_session.add(user)
    await async_db_session.commit()
    await async_db_session.refresh(user)

    lunar_return = LunarReturn(
        user_id=user.id,
        month="2024-07",
        return_date=datetime(2024, 7, 15, 12, 0, 0, tzinfo=timezone.utc),
        moon_sign="Virgo",
        moon_house=6,
        lunar_ascendant="Pisces"
    )
    async_db_session.add(lunar_return)
    await async_db_session.commit()
    await async_db_session.refresh(lunar_return)

    # Créer Interprétation
    interpretation = LunarInterpretation(
        user_id=user.id,
        lunar_return_id=lunar_return.id,
        subject="full",
        version=2,
        lang="fr",
        input_json={},
        output_text="Test cascade"
    )
    async_db_session.add(interpretation)
    await async_db_session.commit()
    await async_db_session.refresh(interpretation)
    interpretation_id = interpretation.id

    # Supprimer LunarReturn
    await async_db_session.delete(lunar_return)
    await async_db_session.commit()

    # L'interprétation doit être supprimée aussi (CASCADE)
    stmt = select(LunarInterpretation).where(LunarInterpretation.id == interpretation_id)
    result = await async_db_session.execute(stmt)
    found = result.scalar_one_or_none()
    assert found is None

    # Cleanup User
    await async_db_session.delete(user)
    await async_db_session.commit()


@pytest.mark.real_db
@pytest.mark.asyncio
async def test_multiple_subjects_same_return(async_db_session: AsyncSession):
    """
    Test que plusieurs sujets différents peuvent coexister pour le même lunar_return
    """
    # Créer User et LunarReturn
    user = User(
        email=f"test_multi_{uuid.uuid4().hex[:8]}@example.com",
        hashed_password="hashed_pw_test"
    )
    async_db_session.add(user)
    await async_db_session.commit()
    await async_db_session.refresh(user)

    lunar_return = LunarReturn(
        user_id=user.id,
        month="2024-08",
        return_date=datetime(2024, 8, 15, 12, 0, 0, tzinfo=timezone.utc),
        moon_sign="Libra",
        moon_house=7,
        lunar_ascendant="Aries"
    )
    async_db_session.add(lunar_return)
    await async_db_session.commit()
    await async_db_session.refresh(lunar_return)

    # Créer plusieurs sujets
    subjects = ["full", "climate", "focus"]
    for subject in subjects:
        interpretation = LunarInterpretation(
            user_id=user.id,
            lunar_return_id=lunar_return.id,
            subject=subject,
            version=2,
            lang="fr",
            input_json={},
            output_text=f"Interprétation {subject}"
        )
        async_db_session.add(interpretation)

    await async_db_session.commit()

    # Vérifier les 3 interprétations existent
    stmt = select(LunarInterpretation).where(
        LunarInterpretation.lunar_return_id == lunar_return.id
    )
    result = await async_db_session.execute(stmt)
    results = result.scalars().all()
    assert len(results) == 3

    # Cleanup
    for interp in results:
        await async_db_session.delete(interp)
    await async_db_session.delete(lunar_return)
    await async_db_session.delete(user)
    await async_db_session.commit()
