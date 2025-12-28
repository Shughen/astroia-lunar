"""
Helpers pour extraire les données du thème natal depuis la structure JSONB positions
"""

from typing import Dict, Any, Optional


def extract_big3_from_positions(positions: Optional[Dict[str, Any]]) -> Dict[str, Optional[str]]:
    """
    Extrait le Big3 (Sun, Moon, Ascendant) depuis la structure positions JSONB
    
    Structure attendue (tolérante aux variations):
    - positions["sun"]["sign"] ou positions["sun"]["zodiac_sign"]
    - positions["moon"]["sign"] ou positions["moon"]["zodiac_sign"]
    - positions["ascendant"]["sign"] OU positions["angles"]["ascendant"]["sign"]
    
    Args:
        positions: Dictionnaire JSONB contenant les positions planétaires
                  Peut être None ou vide
    
    Returns:
        Dictionnaire avec:
        {
            "sun_sign": str | None,
            "moon_sign": str | None,
            "ascendant_sign": str | None
        }
    """
    if not positions or not isinstance(positions, dict):
        return {
            "sun_sign": None,
            "moon_sign": None,
            "ascendant_sign": None
        }
    
    # Extraire Sun
    sun_sign = None
    sun_data = positions.get("sun") or positions.get("Sun")
    if sun_data and isinstance(sun_data, dict):
        sun_sign = sun_data.get("sign") or sun_data.get("zodiac_sign") or sun_data.get("sign_name")
    
    # Extraire Moon
    moon_sign = None
    moon_data = positions.get("moon") or positions.get("Moon")
    if moon_data and isinstance(moon_data, dict):
        moon_sign = moon_data.get("sign") or moon_data.get("zodiac_sign") or moon_data.get("sign_name")
    
    # Extraire Ascendant (peut être dans angles ou directement)
    ascendant_sign = None
    ascendant_data = positions.get("ascendant") or positions.get("Ascendant")
    if not ascendant_data:
        # Essayer dans angles
        angles = positions.get("angles") or positions.get("Angles")
        if angles and isinstance(angles, dict):
            ascendant_data = angles.get("ascendant") or angles.get("Ascendant")
    
    if ascendant_data and isinstance(ascendant_data, dict):
        ascendant_sign = ascendant_data.get("sign") or ascendant_data.get("zodiac_sign") or ascendant_data.get("sign_name")
    
    return {
        "sun_sign": sun_sign,
        "moon_sign": moon_sign,
        "ascendant_sign": ascendant_sign
    }


def extract_moon_data_from_positions(positions: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Extrait les données de la Lune depuis positions JSONB
    
    Args:
        positions: Dictionnaire JSONB contenant les positions planétaires
    
    Returns:
        Dictionnaire avec:
        {
            "sign": str | None,
            "degree": float | None,
            "house": int | None
        }
    """
    if not positions or not isinstance(positions, dict):
        return {
            "sign": None,
            "degree": None,
            "house": None
        }
    
    moon_data = positions.get("moon") or positions.get("Moon") or {}
    if not isinstance(moon_data, dict):
        moon_data = {}
    
    return {
        "sign": moon_data.get("sign") or moon_data.get("zodiac_sign") or moon_data.get("sign_name"),
        "degree": moon_data.get("degree") or moon_data.get("absolute_longitude"),
        "house": moon_data.get("house") or moon_data.get("house_number")
    }

