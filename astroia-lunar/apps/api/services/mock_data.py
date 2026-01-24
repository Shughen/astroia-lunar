"""
Service de génération de données MOCK pour développement
Utilisé quand DEV_MOCK_NATAL=true ou DEV_MOCK_RAPIDAPI=true
"""

import random
from datetime import datetime, date as dt_date
from typing import Dict, Any, List


def calculate_sun_sign(month: int, day: int) -> tuple[str, float]:
    """
    Calcule le signe solaire RÉEL basé sur le mois et le jour
    Retourne (signe, degré approximatif dans le signe)
    """
    # Dates approximatives de début de chaque signe (jour de l'année)
    sign_dates = [
        (datetime(2000, 3, 21).timetuple().tm_yday, "Aries"),      # 21 mars
        (datetime(2000, 4, 20).timetuple().tm_yday, "Taurus"),     # 20 avril
        (datetime(2000, 5, 21).timetuple().tm_yday, "Gemini"),     # 21 mai
        (datetime(2000, 6, 21).timetuple().tm_yday, "Cancer"),     # 21 juin
        (datetime(2000, 7, 23).timetuple().tm_yday, "Leo"),        # 23 juillet
        (datetime(2000, 8, 23).timetuple().tm_yday, "Virgo"),      # 23 août
        (datetime(2000, 9, 23).timetuple().tm_yday, "Libra"),      # 23 septembre
        (datetime(2000, 10, 23).timetuple().tm_yday, "Scorpio"),   # 23 octobre
        (datetime(2000, 11, 22).timetuple().tm_yday, "Sagittarius"), # 22 novembre
        (datetime(2000, 12, 22).timetuple().tm_yday, "Capricorn"), # 22 décembre
        (datetime(2000, 1, 20).timetuple().tm_yday, "Aquarius"),   # 20 janvier
        (datetime(2000, 2, 19).timetuple().tm_yday, "Pisces"),     # 19 février
    ]

    # Calculer le jour de l'année
    birth_date = datetime(2000, month, day)  # Année bissextile pour calcul
    day_of_year = birth_date.timetuple().tm_yday

    # Trouver le signe correspondant
    current_sign = "Capricorn"  # Défaut (fin décembre/début janvier)
    days_in_sign = 0

    for i, (start_day, sign) in enumerate(sign_dates):
        next_idx = (i + 1) % len(sign_dates)
        next_start_day = sign_dates[next_idx][0]

        # Gérer le passage d'année (Capricorne)
        if sign == "Capricorn":
            if day_of_year >= start_day or day_of_year < sign_dates[0][0]:
                current_sign = sign
                if day_of_year >= start_day:
                    days_in_sign = day_of_year - start_day
                else:
                    days_in_sign = day_of_year + (365 - start_day)
                break
        elif start_day <= day_of_year < next_start_day:
            current_sign = sign
            days_in_sign = day_of_year - start_day
            break

    # Calculer degré approximatif (environ 1° par jour, signe = 30°)
    degree = min(days_in_sign * 1.0, 29.99)  # Max 29.99° dans un signe

    return current_sign, degree


def generate_mock_natal_chart(birth_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Génère un thème natal MOCK déterministe basé sur les données de naissance
    Compatible avec le format attendu par routes/natal.py

    Le SIGNE SOLAIRE est calculé CORRECTEMENT basé sur la vraie date.
    Les autres planètes sont aléatoires mais cohérentes.

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

    # Calculer le VRAI signe solaire
    sun_sign, sun_degree = calculate_sun_sign(birth_data['month'], birth_data['day'])

    # Générer positions planétaires
    planetary_positions = []
    for i, planet in enumerate(planets):
        if planet == "sun":
            # Utiliser le VRAI signe solaire calculé
            sign = sun_sign
            degree = sun_degree
            sign_idx = signs.index(sign)
        else:
            # Autres planètes : aléatoires mais cohérentes
            sign_idx = (birth_data['day'] + i * 30 + birth_data['hour']) % 12
            sign = signs[sign_idx]
            degree = random.uniform(0, 30)

        house = ((i + birth_data['hour']) % 12) + 1

        planetary_positions.append({
            "name": planet,
            "sign": sign,
            "sign_abbreviation": sign[:3],
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
