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


def is_chart_incomplete(positions: Optional[Dict[str, Any]]) -> bool:
    """
    Détecte si un chart natal est incomplet selon les critères MVP.

    Critères de chart complet:
    - positions doit être un dict non vide
    - sun, moon, ascendant doivent être présents
    - planets doit contenir au moins 10 planètes
    - houses doit contenir exactement 12 maisons
    - aspects peut être vide ou absent (accepté en MVP)

    Args:
        positions: Dictionnaire JSONB contenant les positions planétaires

    Returns:
        True si le chart est incomplet, False si complet
    """
    # Vérifier que positions est un dict non vide
    if not positions or not isinstance(positions, dict):
        return True

    # Vérifier Big3 (sun, moon, ascendant)
    if "sun" not in positions:
        return True
    if "moon" not in positions:
        return True

    # Vérifier ascendant (peut être direct ou dans angles)
    has_ascendant = False
    if "ascendant" in positions:
        has_ascendant = True
    elif "angles" in positions and isinstance(positions["angles"], dict):
        if "ascendant" in positions["angles"]:
            has_ascendant = True

    if not has_ascendant:
        return True

    # Vérifier planets (au moins 10)
    planets = positions.get("planets")
    if not planets or not isinstance(planets, dict):
        return True
    if len(planets) < 10:
        return True

    # Vérifier houses (exactement 12)
    houses = positions.get("houses")
    if not houses or not isinstance(houses, dict):
        return True
    if len(houses) != 12:
        return True

    # aspects peut être vide ou absent (accepté)
    return False


# Mapping des signes astrologiques abrégés vers noms complets
SIGN_MAPPING = {
    "Ari": "Aries",
    "Tau": "Taurus",
    "Gem": "Gemini",
    "Can": "Cancer",
    "Leo": "Leo",
    "Vir": "Virgo",
    "Lib": "Libra",
    "Sco": "Scorpio",
    "Sag": "Sagittarius",
    "Cap": "Capricorn",
    "Aqu": "Aquarius",
    "Pis": "Pisces"
}

# Mapping des maisons
HOUSE_MAPPING = {
    "First_House": 1,
    "Second_House": 2,
    "Third_House": 3,
    "Fourth_House": 4,
    "Fifth_House": 5,
    "Sixth_House": 6,
    "Seventh_House": 7,
    "Eighth_House": 8,
    "Ninth_House": 9,
    "Tenth_House": 10,
    "Eleventh_House": 11,
    "Twelfth_House": 12
}


def normalize_subject_data_to_positions(rapidapi_response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalise les données RapidAPI (subject_data) vers le format positions JSONB.

    Args:
        rapidapi_response: Réponse de l'API RapidAPI contenant subject_data

    Returns:
        Dictionnaire positions normalisé avec:
        {
            "sun": {...},
            "moon": {...},
            "ascendant": {...},
            "planets": {...},
            "houses": {...}
        }

    Raises:
        ValueError: Si subject_data est absent
    """
    if "subject_data" not in rapidapi_response:
        raise ValueError("subject_data absent de la réponse RapidAPI")

    subject_data = rapidapi_response["subject_data"]

    # Fonction helper pour normaliser une planète
    def normalize_planet(planet_data: Dict[str, Any]) -> Dict[str, Any]:
        sign_abbr = planet_data.get("sign", "Ari")
        sign_full = SIGN_MAPPING.get(sign_abbr, sign_abbr)

        house_str = planet_data.get("house", "First_House")
        house_num = HOUSE_MAPPING.get(house_str, 1)

        return {
            "sign": sign_full,
            "position": planet_data.get("position", 0.0),
            "house": house_num
        }

    # Normaliser les planètes principales
    sun_data = normalize_planet(subject_data.get("sun", {}))
    moon_data = normalize_planet(subject_data.get("moon", {}))
    ascendant_data = normalize_planet(subject_data.get("ascendant", {}))

    # Construire le dictionnaire planets (toutes les planètes)
    planets = {}
    planet_keys = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto"]

    for key in planet_keys:
        if key in subject_data:
            planets[key] = normalize_planet(subject_data[key])

    # Ajouter Ascendant dans planets
    planets["Ascendant"] = ascendant_data

    # Construire houses (pour l'instant, placeholder car RapidAPI ne retourne pas toujours les cusps)
    houses = {str(i): {"sign": "Aries", "degree": 0.0} for i in range(1, 13)}

    # Construire la structure finale
    positions = {
        "sun": sun_data,
        "moon": moon_data,
        "ascendant": ascendant_data,
        "planets": planets,
        "houses": houses,
        "aspects": []  # Placeholder
    }

    return positions

