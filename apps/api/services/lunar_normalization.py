"""
Normalization layer for RapidAPI Lunar responses.

Transforms variable RapidAPI responses into stable, predictable schemas
that the mobile app can rely on. Prevents "N/A" values from appearing in the UI.
"""

from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


def normalize_lunar_mansion_response(raw_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize Lunar Mansion response from RapidAPI to stable schema.

    Handles multiple possible field names from RapidAPI with fallbacks.
    Never returns "N/A" string - uses null instead.

    Args:
        raw_response: Raw JSON from RapidAPI

    Returns:
        Normalized dict with stable structure:
        {
            "mansion": {
                "number": int|null,
                "name": str|null,
                "interpretation": str|null
            },
            "upcoming_changes": [...],  # preserved as-is
            "calendar_summary": {...},  # preserved as-is
            "raw": {...}  # if debug mode
        }
    """
    logger.debug(f"🔄 Normalizing Lunar Mansion response (keys: {list(raw_response.keys())})")

    normalized = {}

    # Extract mansion data with multiple fallbacks
    mansion_raw = raw_response.get("mansion", {})
    if not isinstance(mansion_raw, dict):
        logger.warning(f"⚠️  mansion field is not a dict: {type(mansion_raw)}")
        mansion_raw = {}

    mansion_normalized = {
        "number": _extract_mansion_number(mansion_raw),
        "name": _extract_mansion_name(mansion_raw),
        "interpretation": mansion_raw.get("interpretation") or mansion_raw.get("description") or mansion_raw.get("meaning")
    }

    normalized["mansion"] = mansion_normalized

    # Preserve other fields as-is (upcoming_changes, calendar_summary, etc.)
    for key in ["upcoming_changes", "calendar_summary", "provider", "datetime_location"]:
        if key in raw_response:
            normalized[key] = raw_response[key]

    # Optional: include raw response for debugging (can be disabled in production)
    if logger.isEnabledFor(logging.DEBUG):
        normalized["raw"] = raw_response

    logger.info(f"✅ Normalized Lunar Mansion: #{mansion_normalized['number']} - {mansion_normalized['name']}")

    return normalized


def _extract_mansion_number(mansion_dict: Dict[str, Any]) -> Optional[int]:
    """
    Extract mansion number with multiple fallbacks.

    Tries: number → id → mansion_number → mansion_id → index
    """
    for key in ["number", "id", "mansion_number", "mansion_id", "index"]:
        value = mansion_dict.get(key)
        if value is not None:
            try:
                return int(value)
            except (ValueError, TypeError):
                logger.warning(f"⚠️  Cannot convert mansion {key}={value} to int")
                continue

    logger.warning("⚠️  No valid mansion number found in response")
    return None


def _extract_mansion_name(mansion_dict: Dict[str, Any]) -> Optional[str]:
    """
    Extract mansion name with multiple fallbacks.

    Tries: name → title → mansion_name → label → arabic_name
    """
    for key in ["name", "title", "mansion_name", "label", "arabic_name"]:
        value = mansion_dict.get(key)
        if value and isinstance(value, str):
            return value

    logger.warning("⚠️  No valid mansion name found in response")
    return None


def normalize_lunar_return_report_response(raw_response: Dict[str, Any], request_month: Optional[str] = None) -> Dict[str, Any]:
    """
    Normalize Lunar Return Report response from RapidAPI to stable schema.

    Handles multiple possible field names from RapidAPI with fallbacks.
    Never returns "N/A" string - uses null instead.

    Args:
        raw_response: Raw JSON from RapidAPI
        request_month: Optional month from request (format: "YYYY-MM")

    Returns:
        Normalized dict with stable structure:
        {
            "month": "YYYY-MM"|null,
            "return_date": "ISO8601"|null,
            "moon_sign": "Aries"|null,
            "moon_house": 1|null,
            "lunar_ascendant": "Gemini"|null,
            "summary": str|null,
            "interpretation": str|null,
            "raw": {...}  # if debug mode
        }
    """
    logger.debug(f"🔄 Normalizing Lunar Return Report (keys: {list(raw_response.keys())})")

    normalized = {}

    # Month (from request, not response)
    normalized["month"] = request_month

    # Return date with fallbacks (step by step to avoid 'or' with empty dict)
    return_date = raw_response.get("return_date")
    if not return_date:
        lunar_return = raw_response.get("lunar_return")
        if isinstance(lunar_return, dict):
            return_date = lunar_return.get("date")
    if not return_date:
        data = raw_response.get("data")
        if isinstance(data, dict):
            return_date = data.get("return_date")
    if not return_date:
        return_date = raw_response.get("date")

    normalized["return_date"] = return_date

    # Moon sign with fallbacks
    moon_data = raw_response.get("moon", {})
    if not isinstance(moon_data, dict):
        # Sometimes moon is just a string like "Aries"
        if isinstance(moon_data, str):
            normalized["moon_sign"] = moon_data
            normalized["moon_house"] = None
        else:
            normalized["moon_sign"] = None
            normalized["moon_house"] = None
    else:
        normalized["moon_sign"] = (
            moon_data.get("sign") or
            moon_data.get("zodiac_sign") or
            moon_data.get("zodiac")
        )
        normalized["moon_house"] = moon_data.get("house")

    # Lunar Ascendant with fallbacks
    normalized["lunar_ascendant"] = (
        raw_response.get("lunar_ascendant") or
        raw_response.get("ascendant") or
        raw_response.get("rising_sign") or
        raw_response.get("lunar_return", {}).get("ascendant") if isinstance(raw_response.get("lunar_return"), dict) else None
    )

    # Summary/Interpretation with fallbacks
    normalized["summary"] = (
        raw_response.get("summary") or
        raw_response.get("interpretation") or
        raw_response.get("description") or
        raw_response.get("report") or
        raw_response.get("text")
    )

    normalized["interpretation"] = raw_response.get("interpretation")

    # Preserve any additional structured data
    for key in ["aspects", "houses", "planets", "provider"]:
        if key in raw_response:
            normalized[key] = raw_response[key]

    # Optional: include raw response for debugging
    if logger.isEnabledFor(logging.DEBUG):
        normalized["raw"] = raw_response

    logger.info(f"✅ Normalized Lunar Return: month={normalized['month']}, moon={normalized['moon_sign']}, return_date={normalized['return_date']}")

    return normalized
