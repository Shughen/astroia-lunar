"""
Service de génération de données MOCK pour développement
Utilisé quand DEV_MOCK_NATAL=true ou DEV_MOCK_RAPIDAPI=true
"""

import random
from typing import Dict, Any, List


def generate_mock_natal_chart(birth_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un thème natal MOCK déterministe basé sur les données de naissance
    Compatible avec le format attendu par routes/natal.py

    Args:
        birth_data: Dictionnaire avec year, month, day, hour, minute, latitude, longitude, timezone

    Returns:
        Dictionnaire au format RapidAPI natal chart response
    """
    # Seed pour reproductibilité (même date = même thème)
    seed = f"{birth_data['year']}{birth_data['month']}{birth_data['day']}{birth_data['hour']}{birth_data['minute']}"
    random.seed(hash(seed))

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    planets = ["sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn",
               "uranus", "neptune", "pluto"]

    # Générer positions planétaires
    planetary_positions = []
    for i, planet in enumerate(planets):
        sign_idx = (birth_data['day'] + i * 30 + birth_data['hour']) % 12
        degree = random.uniform(0, 30)
        house = ((i + birth_data['hour']) % 12) + 1

        planetary_positions.append({
            "name": planet,
            "sign": signs[sign_idx],
            "sign_abbreviation": signs[sign_idx][:3],
            "degree": degree,
            "house": house,
            "retrograde": random.choice([True, False]) if planet not in ["sun", "moon"] else False,
            "absolute_longitude": sign_idx * 30 + degree
        })

    # Ajouter Ascendant
    asc_sign_idx = (birth_data['hour'] * 2 + birth_data['minute'] // 30) % 12
    asc_degree = random.uniform(0, 30)
    planetary_positions.append({
        "name": "ascendant",
        "sign": signs[asc_sign_idx],
        "sign_abbreviation": signs[asc_sign_idx][:3],
        "degree": asc_degree,
        "house": 1,
        "absolute_longitude": asc_sign_idx * 30 + asc_degree
    })

    # Ajouter Medium Coeli (MC)
    mc_sign_idx = (asc_sign_idx + 9) % 12
    mc_degree = random.uniform(0, 30)
    planetary_positions.append({
        "name": "medium_coeli",
        "sign": signs[mc_sign_idx],
        "sign_abbreviation": signs[mc_sign_idx][:3],
        "degree": mc_degree,
        "house": 10,
        "absolute_longitude": mc_sign_idx * 30 + mc_degree
    })

    # Générer cuspides des maisons
    house_cusps = []
    for i in range(12):
        cusp_sign_idx = (asc_sign_idx + i) % 12
        cusp_degree = random.uniform(0, 30) if i > 0 else asc_degree
        house_cusps.append({
            "house": i + 1,
            "sign": signs[cusp_sign_idx],
            "absolute_longitude": cusp_sign_idx * 30 + cusp_degree,
            "degree": cusp_degree
        })

    # Générer aspects (quelques exemples)
    aspect_types = ["conjunction", "opposition", "trine", "square", "sextile"]
    aspects = []

    # Générer 5-10 aspects aléatoires
    num_aspects = random.randint(5, 10)
    for _ in range(num_aspects):
        planet1 = random.choice(planets[:7])  # Planètes intérieures
        planet2 = random.choice(planets)
        if planet1 != planet2:
            aspects.append({
                "from": planet1,
                "to": planet2,
                "aspect_type": random.choice(aspect_types),
                "orb": random.uniform(0.1, 6.0),
                "applying": random.choice([True, False])
            })

    # Format de réponse compatible avec RapidAPI
    return {
        "chart_data": {
            "planetary_positions": planetary_positions,
            "house_cusps": house_cusps,
            "aspects": aspects
        },
        "subject_data": {
            "name": birth_data.get("city", "Mock User"),
            "birth_data": birth_data
        }
    }


def generate_mock_lunar_return(birth_data: Dict[str, Any], return_date: str) -> Dict[str, Any]:
    """
    Génère une révolution lunaire MOCK

    Args:
        birth_data: Données de naissance
        return_date: Date de la révolution lunaire (ISO format)

    Returns:
        Dictionnaire au format RapidAPI lunar return response
    """
    seed = f"{birth_data['year']}{return_date}"
    random.seed(hash(seed))

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    moon_sign_idx = random.randint(0, 11)
    moon_house = random.randint(1, 12)
    lunar_asc_idx = random.randint(0, 11)

    return {
        "return_data": {
            "moon_sign": signs[moon_sign_idx],
            "moon_house": moon_house,
            "lunar_ascendant": signs[lunar_asc_idx],
            "return_date": return_date,
            "planetary_positions": [],
            "aspects": []
        }
    }
