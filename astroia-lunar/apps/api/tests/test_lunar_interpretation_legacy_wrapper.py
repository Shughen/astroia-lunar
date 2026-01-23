"""Tests for legacy wrapper backward compatibility"""

import pytest
import pytest_asyncio
import warnings
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from services.lunar_interpretation_legacy_wrapper import (
    load_lunar_interpretation_with_fallback,
    get_fallback_climate,
    get_fallback_focus,
    get_fallback_approach
)
from database import AsyncSessionLocal


@pytest_asyncio.fixture(scope="function")
async def db_session():
    """Session DB async pour setup/cleanup"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.rollback()
            await session.close()


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires real DB connection (Supabase)")
async def test_legacy_wrapper_emits_deprecation_warning(db_session):
    """Legacy wrapper should emit DeprecationWarning"""

    # Create test user
    from models import User, LunarReturn
    user = User(email="test@legacy.com", hashed_password="hash")
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    # Create test lunar_return
    lunar_return = LunarReturn(
        user_id=user.id,
        month="2026-02",
        moon_sign="Aries",
        moon_house=1,
        lunar_ascendant="Taurus",
        return_date=datetime(2026, 2, 1, 10, 0, 0)
    )
    db_session.add(lunar_return)
    await db_session.commit()

    # Call legacy function
    with pytest.warns(DeprecationWarning, match="deprecated"):
        result = await load_lunar_interpretation_with_fallback(
            db=db_session,
            moon_sign="Aries",
            moon_house=1,
            lunar_ascendant="Taurus"
        )

    assert len(result) == 3  # 3-tuple (V1 format)
    output_text, weekly_advice, source = result
    assert isinstance(output_text, str)
    assert source in ['db_temporal', 'claude', 'db_template', 'hardcoded']


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires real DB connection (Supabase)")
async def test_legacy_wrapper_no_lunar_return_raises(db_session):
    """Legacy wrapper should raise ValueError if no matching LunarReturn"""

    with pytest.raises(ValueError, match="No LunarReturn found"):
        with pytest.warns(DeprecationWarning):
            await load_lunar_interpretation_with_fallback(
                db=db_session,
                moon_sign="Nonexistent",
                moon_house=999,
                lunar_ascendant="Invalid"
            )


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires real DB connection (Supabase)")
async def test_legacy_wrapper_finds_most_recent_lunar_return(db_session):
    """Legacy wrapper should find the most recent matching LunarReturn"""

    # Create test user
    from models import User, LunarReturn
    user = User(email="test@recent.com", hashed_password="hash")
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    # Create two lunar_returns with same configuration but different dates
    older_return = LunarReturn(
        user_id=user.id,
        month="2026-01",
        moon_sign="Gemini",
        moon_house=3,
        lunar_ascendant="Leo",
        return_date=datetime(2026, 1, 1, 10, 0, 0)
    )
    newer_return = LunarReturn(
        user_id=user.id,
        month="2026-02",
        moon_sign="Gemini",
        moon_house=3,
        lunar_ascendant="Leo",
        return_date=datetime(2026, 2, 1, 10, 0, 0)
    )
    db_session.add(older_return)
    db_session.add(newer_return)
    await db_session.commit()

    # Call legacy function - should use newer_return
    with pytest.warns(DeprecationWarning):
        result = await load_lunar_interpretation_with_fallback(
            db=db_session,
            moon_sign="Gemini",
            moon_house=3,
            lunar_ascendant="Leo"
        )

    # Verify it worked (source should be one of the valid options)
    output_text, weekly_advice, source = result
    assert isinstance(output_text, str)
    assert len(output_text) > 0


@pytest.mark.asyncio
async def test_fallback_climate_emits_warning():
    """get_fallback_climate() should emit DeprecationWarning"""

    with pytest.warns(DeprecationWarning):
        result = await get_fallback_climate("Aries")
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.asyncio
async def test_fallback_focus_emits_warning():
    """get_fallback_focus() should emit DeprecationWarning"""

    with pytest.warns(DeprecationWarning):
        result = await get_fallback_focus(1)
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.asyncio
async def test_fallback_approach_emits_warning():
    """get_fallback_approach() should emit DeprecationWarning"""

    with pytest.warns(DeprecationWarning):
        result = await get_fallback_approach("Taurus")
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.asyncio
@pytest.mark.skip(reason="Requires real DB connection (Supabase)")
async def test_legacy_wrapper_returns_v1_format(db_session):
    """Legacy wrapper should return 3-tuple (not 4-tuple like V2)"""

    # Create test user and lunar_return
    from models import User, LunarReturn
    user = User(email="test@format.com", hashed_password="hash")
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)

    lunar_return = LunarReturn(
        user_id=user.id,
        month="2026-03",
        moon_sign="Cancer",
        moon_house=4,
        lunar_ascendant="Virgo",
        return_date=datetime(2026, 3, 1, 10, 0, 0)
    )
    db_session.add(lunar_return)
    await db_session.commit()

    # Call legacy function
    with pytest.warns(DeprecationWarning):
        result = await load_lunar_interpretation_with_fallback(
            db=db_session,
            moon_sign="Cancer",
            moon_house=4,
            lunar_ascendant="Virgo"
        )

    # V1 format: 3-tuple
    assert len(result) == 3
    output_text, weekly_advice, source = result

    # V2 format would be: 4-tuple with model_used as 4th element
    # Verify we're NOT getting a 4-tuple
    assert not isinstance(result, tuple) or len(result) != 4
