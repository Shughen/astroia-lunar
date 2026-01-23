"""
Legacy compatibility wrapper for lunar interpretation V1 → V2 migration

DEPRECATED: This module provides backward compatibility for code still using
the old load_lunar_interpretation_with_fallback() function.

New code should use:
    from services.lunar_interpretation_generator import generate_or_get_interpretation

Migration path:
    V1 (deprecated) → V2 via wrapper → V2 direct
"""

import logging
import warnings
from typing import Dict, Any, Optional, Tuple
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

logger = logging.getLogger(__name__)


async def load_lunar_interpretation_with_fallback(
    db: AsyncSession,
    moon_sign: str,
    moon_house: int,
    lunar_ascendant: str,
    preferred_version: int = 2,
    lang: str = 'fr'
) -> Tuple[str, Optional[Dict], str]:
    """
    DEPRECATED: Use generate_or_get_interpretation() instead

    Legacy wrapper for V1 lunar interpretation loading.
    Translates V1 signature (moon_sign/house/asc) to V2 (lunar_return_id).

    Args:
        db: Async SQLAlchemy session
        moon_sign: Moon sign (e.g., 'Aries', 'Taurus')
        moon_house: Moon house (1-12)
        lunar_ascendant: Lunar ascendant sign
        preferred_version: Version (default: 2)
        lang: Language (default: 'fr')

    Returns:
        Tuple[output_text, weekly_advice, source]

    Raises:
        DeprecationWarning: Always (function is deprecated)
        ValueError: If no matching lunar_return found
    """
    # Emit deprecation warning
    warnings.warn(
        "load_lunar_interpretation_with_fallback() is deprecated. "
        "Use generate_or_get_interpretation() from lunar_interpretation_generator instead. "
        "This wrapper will be removed in v3.0.",
        DeprecationWarning,
        stacklevel=2
    )

    logger.warning(
        "legacy_wrapper_called",
        extra={
            "function": "load_lunar_interpretation_with_fallback",
            "moon_sign": moon_sign,
            "moon_house": moon_house,
            "lunar_ascendant": lunar_ascendant
        }
    )

    # Step 1: Find matching lunar_return
    # Strategy: Find most recent lunar_return matching this configuration
    from models import LunarReturn

    result = await db.execute(
        select(LunarReturn)
        .filter_by(
            moon_sign=moon_sign,
            moon_house=moon_house,
            lunar_ascendant=lunar_ascendant
        )
        .order_by(LunarReturn.return_date.desc())
        .limit(1)
    )
    lunar_return = result.scalar_one_or_none()

    if not lunar_return:
        logger.error(
            "legacy_wrapper_no_matching_lunar_return",
            extra={
                "moon_sign": moon_sign,
                "moon_house": moon_house,
                "lunar_ascendant": lunar_ascendant
            }
        )
        raise ValueError(
            f"No LunarReturn found for {moon_sign}/M{moon_house}/ASC{lunar_ascendant}. "
            "Legacy wrapper requires existing LunarReturn in DB."
        )

    # Step 2: Call new V2 generator
    from services.lunar_interpretation_generator import generate_or_get_interpretation

    output_text, weekly_advice, source, model_used = await generate_or_get_interpretation(
        db=db,
        lunar_return_id=lunar_return.id,
        user_id=lunar_return.user_id,
        subject='full',
        version=preferred_version,
        lang=lang,
        force_regenerate=False
    )

    logger.info(
        "legacy_wrapper_success",
        extra={
            "lunar_return_id": lunar_return.id,
            "source": source,
            "model_used": model_used
        }
    )

    # Step 3: Return in V1 format (3-tuple, not 4-tuple)
    return output_text, weekly_advice, source


async def get_fallback_climate(moon_sign: str) -> str:
    """
    DEPRECATED: Use lunar_interpretation_generator._get_hardcoded_fallback() instead

    Legacy fallback for climate templates.
    """
    warnings.warn(
        "get_fallback_climate() is deprecated. "
        "Use _get_hardcoded_fallback() from lunar_interpretation_generator.",
        DeprecationWarning,
        stacklevel=2
    )

    from services.lunar_report_builder import MOON_SIGN_INTRO
    return MOON_SIGN_INTRO.get(moon_sign, f"Mois sous Lune en {moon_sign}.")


async def get_fallback_focus(moon_house: int) -> str:
    """
    DEPRECATED: Use lunar_interpretation_generator._get_hardcoded_fallback() instead

    Legacy fallback for focus templates.
    """
    warnings.warn(
        "get_fallback_focus() is deprecated.",
        DeprecationWarning,
        stacklevel=2
    )

    from services.lunar_report_builder import HOUSE_AXES
    house_label = HOUSE_AXES.get(moon_house, "Domaine de vie")
    return f"Maison {moon_house} : {house_label}."


async def get_fallback_approach(lunar_ascendant: str) -> str:
    """
    DEPRECATED: Use lunar_interpretation_generator._get_hardcoded_fallback() instead

    Legacy fallback for approach templates.
    """
    warnings.warn(
        "get_fallback_approach() is deprecated.",
        DeprecationWarning,
        stacklevel=2
    )

    from services.lunar_report_builder import LUNAR_ASCENDANT_FILTERS
    return LUNAR_ASCENDANT_FILTERS.get(
        lunar_ascendant,
        f"Approche du mois via ASC lunaire {lunar_ascendant}."
    )


# Backward compatibility aliases (for imports)
load_lunar_interpretation = load_lunar_interpretation_with_fallback
