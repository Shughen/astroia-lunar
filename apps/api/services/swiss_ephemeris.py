"""
Centralized Swiss Ephemeris Service
Single source of truth for all lunar calculations using pyswisseph

This module provides:
- Moon/Sun positions (longitude, sign, degree)
- Lunar phases (8 phases based on Sun-Moon elongation)
- Void of Course calculations (last aspect before sign change)
- Lunar mansions (28 divisions)
- Calendar functions (phase changes, sign ingresses)

All calculations are in UTC. Timezone conversion is for display only.
"""

try:
    import swisseph as swe
    SWISS_EPHEMERIS_AVAILABLE = True
except ImportError:
    SWISS_EPHEMERIS_AVAILABLE = False
    swe = None
    import logging
    logger = logging.getLogger(__name__)
    logger.warning("⚠️ Swiss Ephemeris (pyswisseph) non disponible - certaines fonctions seront limitées")

import logging
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta, timezone
from collections import namedtuple

if 'logger' not in locals():
    logger = logging.getLogger(__name__)

# Constants
ZODIAC_SIGNS = [
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
]

LUNAR_PHASES = [
    'Nouvelle Lune',      # 0° ± 22.5°
    'Premier Croissant',  # 22.5° - 67.5°
    'Premier Quartier',   # 67.5° - 112.5°
    'Lune Gibbeuse',      # 112.5° - 157.5°
    'Pleine Lune',        # 157.5° - 202.5°
    'Lune Disseminante',  # 202.5° - 247.5°
    'Dernier Quartier',   # 247.5° - 292.5°
    'Dernier Croissant'   # 292.5° - 337.5°
]

# Major aspects for Void of Course calculations
MAJOR_ASPECTS = {
    'conjunction': 0,
    'sextile': 60,
    'square': 90,
    'trine': 120,
    'opposition': 180,
}

# Orbs for aspects (in degrees)
ASPECT_ORB = 1.0  # Tight orb for VOC calculations

# Named tuple for cleaner returns
MoonPosition = namedtuple('MoonPosition', ['longitude', 'sign', 'degree', 'phase'])
SunPosition = namedtuple('SunPosition', ['longitude', 'sign', 'degree'])
VocWindow = namedtuple('VocWindow', ['start_time', 'end_time', 'from_sign', 'to_sign'])


def datetime_to_julian_day(dt: datetime) -> float:
    """
    Convert datetime to Julian Day (UT)

    Args:
        dt: datetime object (assumed UTC if naive)

    Returns:
        Julian Day number
    """
    if not SWISS_EPHEMERIS_AVAILABLE:
        raise ImportError("Swiss Ephemeris (pyswisseph) n'est pas installé. Installez-le avec: pip install pyswisseph")
    
    if dt.tzinfo is None:
        # Assume UTC if naive
        dt = dt.replace(tzinfo=timezone.utc)

    # Convert to UTC
    dt_utc = dt.astimezone(timezone.utc)

    # Calculate Julian Day
    jd = swe.julday(
        dt_utc.year,
        dt_utc.month,
        dt_utc.day,
        dt_utc.hour + dt_utc.minute / 60.0 + dt_utc.second / 3600.0
    )

    return jd


def julian_day_to_datetime(jd: float) -> datetime:
    """
    Convert Julian Day to datetime (UTC)

    Args:
        jd: Julian Day number

    Returns:
        datetime object in UTC
    """
    year, month, day, hour = swe.revjul(jd)

    # Convert fractional hour to hour, minute, second
    hour_int = int(hour)
    minute_frac = (hour - hour_int) * 60
    minute_int = int(minute_frac)
    second = int((minute_frac - minute_int) * 60)

    return datetime(year, month, day, hour_int, minute_int, second, tzinfo=timezone.utc)


def degree_to_sign(degree: float) -> str:
    """
    Convert ecliptic degree (0-360) to zodiac sign

    Args:
        degree: Ecliptic longitude (0-360)

    Returns:
        Zodiac sign name
    """
    degree = degree % 360  # Normalize
    sign_index = int(degree / 30)
    return ZODIAC_SIGNS[sign_index]


def calculate_phase_from_elongation(elongation: float) -> str:
    """
    Calculate lunar phase from Sun-Moon elongation angle

    Args:
        elongation: Angle between Moon and Sun (0-360)

    Returns:
        Phase name (French)
    """
    elongation = elongation % 360

    if elongation < 22.5 or elongation >= 337.5:
        return 'Nouvelle Lune'
    elif 22.5 <= elongation < 67.5:
        return 'Premier Croissant'
    elif 67.5 <= elongation < 112.5:
        return 'Premier Quartier'
    elif 112.5 <= elongation < 157.5:
        return 'Lune Gibbeuse'
    elif 157.5 <= elongation < 202.5:
        return 'Pleine Lune'
    elif 202.5 <= elongation < 247.5:
        return 'Lune Disseminante'
    elif 247.5 <= elongation < 292.5:
        return 'Dernier Quartier'
    else:  # 292.5 <= elongation < 337.5
        return 'Dernier Croissant'


def get_moon_longitude(jd_ut: float) -> float:
    """
    Get Moon's ecliptic longitude at Julian Day

    Args:
        jd_ut: Julian Day (UT)

    Returns:
        Ecliptic longitude (0-360)
    """
    if not SWISS_EPHEMERIS_AVAILABLE:
        raise ImportError("Swiss Ephemeris (pyswisseph) n'est pas installé. Installez-le avec: pip install pyswisseph")
    
    result = swe.calc_ut(jd_ut, swe.MOON, swe.FLG_SWIEPH)
    moon_longitude = result[0][0]
    return moon_longitude


def get_sun_longitude(jd_ut: float) -> float:
    """
    Get Sun's ecliptic longitude at Julian Day

    Args:
        jd_ut: Julian Day (UT)

    Returns:
        Ecliptic longitude (0-360)
    """
    result = swe.calc_ut(jd_ut, swe.SUN, swe.FLG_SWIEPH)
    sun_longitude = result[0][0]
    return sun_longitude


def get_planet_longitude(jd_ut: float, planet: int) -> float:
    """
    Get planet's ecliptic longitude at Julian Day

    Args:
        jd_ut: Julian Day (UT)
        planet: Swiss Ephemeris planet constant (swe.MERCURY, swe.VENUS, etc.)

    Returns:
        Ecliptic longitude (0-360)
    """
    result = swe.calc_ut(jd_ut, planet, swe.FLG_SWIEPH)
    return result[0][0]


def get_moon_position(dt: datetime) -> MoonPosition:
    """
    Get complete Moon position at datetime

    Args:
        dt: datetime (UTC)

    Returns:
        MoonPosition(longitude, sign, degree, phase)
    """
    jd = datetime_to_julian_day(dt)

    moon_lon = get_moon_longitude(jd)
    sun_lon = get_sun_longitude(jd)

    sign = degree_to_sign(moon_lon)
    degree_in_sign = moon_lon % 30

    elongation = (moon_lon - sun_lon) % 360
    phase = calculate_phase_from_elongation(elongation)

    return MoonPosition(
        longitude=round(moon_lon, 2),
        sign=sign,
        degree=round(degree_in_sign, 2),
        phase=phase
    )


def get_sun_position(dt: datetime) -> SunPosition:
    """
    Get complete Sun position at datetime

    Args:
        dt: datetime (UTC)

    Returns:
        SunPosition(longitude, sign, degree)
    """
    jd = datetime_to_julian_day(dt)
    sun_lon = get_sun_longitude(jd)

    sign = degree_to_sign(sun_lon)
    degree_in_sign = sun_lon % 30

    return SunPosition(
        longitude=round(sun_lon, 2),
        sign=sign,
        degree=round(degree_in_sign, 2)
    )


def normalize_angle_360(degree: float) -> float:
    """
    Normalise un angle en degrés dans l'intervalle [0, 360)
    
    Args:
        degree: Angle en degrés (peut être négatif ou > 360)
    
    Returns:
        Angle normalisé dans [0, 360)
    """
    return degree % 360


def angle_diff_signed(a: float, b: float) -> float:
    """
    Calcule la différence d'angle signée entre deux angles (dans [-180, 180])
    Utile pour trouver le sens de rotation (applicatif/séparatif)
    
    Args:
        a: Premier angle en degrés (0-360)
        b: Deuxième angle en degrés (0-360)
    
    Returns:
        Différence signée dans [-180, 180]
        - Positif si a > b (dans le sens direct)
        - Négatif si a < b (dans le sens rétrograde)
    """
    a = normalize_angle_360(a)
    b = normalize_angle_360(b)
    
    diff = a - b
    
    # Normaliser dans [-180, 180]
    if diff > 180:
        diff -= 360
    elif diff < -180:
        diff += 360
    
    return diff


def find_lunar_return(
    natal_moon_longitude: float,
    start_dt: datetime,
    search_window_hours: int = 48,
    tolerance_seconds: int = 60
) -> Optional[datetime]:
    """
    Trouve le moment exact où la Lune revient à sa position natale (Lunar Return)
    
    Algorithme:
    1. Approximation: utiliser le mois sidéral (~27.32 jours) pour estimer la date
    2. Bracket: scanner autour de l'approx avec un pas de 30 min pour trouver un changement de signe
    3. Refinement: bisection jusqu'à tolérance (60s par défaut)
    
    Args:
        natal_moon_longitude: Longitude écliptique natale de la Lune (0-360°)
        start_dt: Date de départ pour la recherche (UTC)
        search_window_hours: Fenêtre de recherche en heures (défaut: 48h)
        tolerance_seconds: Tolérance en secondes pour le raffinement (défaut: 60s)
    
    Returns:
        datetime du Lunar Return (UTC) ou None si non trouvé
    """
    if not SWISS_EPHEMERIS_AVAILABLE:
        logger.warning("[LunarReturn] ⚠️ Swiss Ephemeris non disponible - impossible de calculer le Lunar Return")
        return None
    
    logger.info(
        f"[LunarReturn] Recherche Lunar Return - "
        f"λ_natal={natal_moon_longitude:.2f}°, "
        f"start={start_dt.isoformat()}, "
        f"window={search_window_hours}h"
    )
    
    # Normaliser la longitude natale
    natal_lon = normalize_angle_360(natal_moon_longitude)
    
    # Étape 1: Approximation - utiliser le mois sidéral (~27.321582 jours)
    # On cherche dans une fenêtre autour de start_dt
    search_start = start_dt
    search_end = start_dt + timedelta(hours=search_window_hours)
    
    # Étape 2: Bracket - scanner avec un pas de 30 minutes
    step_minutes = 30
    current_dt = search_start
    prev_diff = None
    bracket_start = None
    bracket_end = None
    
    while current_dt <= search_end:
        jd = datetime_to_julian_day(current_dt)
        moon_lon = get_moon_longitude(jd)
        diff = angle_diff_signed(moon_lon, natal_lon)
        
        # Chercher un changement de signe (passage par 0)
        if prev_diff is not None:
            # Si on passe de négatif à positif ou vice versa, on a trouvé un bracket
            if (prev_diff < 0 and diff >= 0) or (prev_diff > 0 and diff <= 0):
                bracket_start = current_dt - timedelta(minutes=step_minutes)
                bracket_end = current_dt
                logger.info(
                    f"[LunarReturn] Bracket trouvé: "
                    f"{bracket_start.isoformat()} (diff={prev_diff:.4f}°) → "
                    f"{bracket_end.isoformat()} (diff={diff:.4f}°)"
                )
                break
        
        prev_diff = diff
        current_dt += timedelta(minutes=step_minutes)
    
    if bracket_start is None or bracket_end is None:
        logger.warning(
            f"[LunarReturn] ❌ Aucun bracket trouvé dans la fenêtre de recherche"
        )
        return None
    
    # Étape 3: Refinement par bisection
    tolerance_td = timedelta(seconds=tolerance_seconds)
    max_iterations = 20
    iteration = 0
    
    while (bracket_end - bracket_start) > tolerance_td and iteration < max_iterations:
        mid_dt = bracket_start + (bracket_end - bracket_start) / 2
        
        jd_mid = datetime_to_julian_day(mid_dt)
        moon_lon_mid = get_moon_longitude(jd_mid)
        diff_mid = angle_diff_signed(moon_lon_mid, natal_lon)
        
        # Calculer les différences aux extrémités
        jd_start = datetime_to_julian_day(bracket_start)
        moon_lon_start = get_moon_longitude(jd_start)
        diff_start = angle_diff_signed(moon_lon_start, natal_lon)
        
        # Bisection: garder l'intervalle qui contient le zéro
        if diff_start * diff_mid < 0:
            # Le zéro est entre start et mid
            bracket_end = mid_dt
        else:
            # Le zéro est entre mid et end
            bracket_start = mid_dt
        
        iteration += 1
    
    # Prendre le milieu final comme résultat
    result_dt = bracket_start + (bracket_end - bracket_start) / 2
    
    # Vérification finale
    jd_result = datetime_to_julian_day(result_dt)
    moon_lon_result = get_moon_longitude(jd_result)
    final_diff = abs(angle_diff_signed(moon_lon_result, natal_lon))
    
    logger.info(
        f"[LunarReturn] ✅ Lunar Return trouvé: "
        f"{result_dt.isoformat()}, "
        f"λ_moon={moon_lon_result:.4f}°, "
        f"diff={final_diff:.4f}° "
        f"({iteration} itérations)"
    )
    
    return result_dt


def find_next_moon_sign_change(start_dt: datetime, max_hours: int = 72) -> Optional[datetime]:
    """
    Find when Moon changes to next zodiac sign

    Args:
        start_dt: Starting datetime (UTC)
        max_hours: Maximum search window

    Returns:
        datetime of sign change, or None if not found
    """
    start_jd = datetime_to_julian_day(start_dt)
    start_sign = degree_to_sign(get_moon_longitude(start_jd))

    # Binary search for sign change
    low_jd = start_jd
    high_jd = start_jd + (max_hours / 24.0)

    # Check if sign changes in window
    end_sign = degree_to_sign(get_moon_longitude(high_jd))
    if start_sign == end_sign:
        return None

    # Binary search with 1-minute precision
    precision_days = 1 / (24 * 60)  # 1 minute

    while (high_jd - low_jd) > precision_days:
        mid_jd = (low_jd + high_jd) / 2
        mid_sign = degree_to_sign(get_moon_longitude(mid_jd))

        if mid_sign == start_sign:
            low_jd = mid_jd
        else:
            high_jd = mid_jd

    return julian_day_to_datetime(high_jd)


def calculate_aspect_angle(lon1: float, lon2: float) -> Tuple[Optional[str], float]:
    """
    Calculate aspect between two longitudes

    Args:
        lon1: First longitude (0-360)
        lon2: Second longitude (0-360)

    Returns:
        (aspect_name, exact_angle) or (None, angle) if no major aspect
    """
    angle = abs(lon1 - lon2)
    if angle > 180:
        angle = 360 - angle

    # Check for major aspects
    for aspect_name, aspect_angle in MAJOR_ASPECTS.items():
        if abs(angle - aspect_angle) <= ASPECT_ORB:
            return (aspect_name, angle)

    return (None, angle)


def find_last_major_aspect_before_sign_change(start_dt: datetime) -> Optional[Tuple[datetime, str, str]]:
    """
    Find Moon's last major aspect before it changes sign

    Args:
        start_dt: Starting datetime (UTC)

    Returns:
        (aspect_time, aspect_name, planet_name) or None if no aspect found
    """
    # Find next sign change
    sign_change_dt = find_next_moon_sign_change(start_dt)
    if not sign_change_dt:
        return None

    # Planets to check
    planets = [
        (swe.SUN, 'Sun'),
        (swe.MERCURY, 'Mercury'),
        (swe.VENUS, 'Venus'),
        (swe.MARS, 'Mars'),
        (swe.JUPITER, 'Jupiter'),
        (swe.SATURN, 'Saturn'),
    ]

    last_aspect_time = None
    last_aspect_name = None
    last_planet_name = None

    # Check each planet for aspects
    current_dt = start_dt
    step = timedelta(minutes=10)

    while current_dt < sign_change_dt:
        jd = datetime_to_julian_day(current_dt)
        moon_lon = get_moon_longitude(jd)

        for planet_id, planet_name in planets:
            planet_lon = get_planet_longitude(jd, planet_id)
            aspect_name, _ = calculate_aspect_angle(moon_lon, planet_lon)

            if aspect_name:
                # Found an aspect - record it
                last_aspect_time = current_dt
                last_aspect_name = aspect_name
                last_planet_name = planet_name

        current_dt += step

    if last_aspect_time:
        return (last_aspect_time, last_aspect_name, last_planet_name)

    return None


def calculate_void_of_course(dt: datetime) -> Dict[str, Any]:
    """
    Calculate Void of Course status for given datetime

    Args:
        dt: datetime (UTC)

    Returns:
        {
            "is_void": bool,
            "void_start": datetime or None,
            "void_end": datetime or None,
            "current_sign": str,
            "next_sign": str or None,
            "last_aspect": {"time": datetime, "type": str, "with": str} or None
        }
    """
    jd = datetime_to_julian_day(dt)
    moon_lon = get_moon_longitude(jd)
    current_sign = degree_to_sign(moon_lon)

    # Find next sign change
    next_sign_change = find_next_moon_sign_change(dt)
    if not next_sign_change:
        logger.warning("[VOC] Could not find next sign change")
        return {
            "is_void": False,
            "void_start": None,
            "void_end": None,
            "current_sign": current_sign,
            "next_sign": None,
            "last_aspect": None
        }

    next_sign = degree_to_sign(get_moon_longitude(datetime_to_julian_day(next_sign_change)))

    # Find last major aspect
    last_aspect_info = find_last_major_aspect_before_sign_change(dt)

    if not last_aspect_info:
        # No aspect found - Moon is void from now until sign change
        return {
            "is_void": True,
            "void_start": dt,
            "void_end": next_sign_change,
            "current_sign": current_sign,
            "next_sign": next_sign,
            "last_aspect": None
        }

    aspect_time, aspect_name, planet_name = last_aspect_info

    # Check if we're past the last aspect (VOC period)
    is_void = dt >= aspect_time

    return {
        "is_void": is_void,
        "void_start": aspect_time if is_void else None,
        "void_end": next_sign_change if is_void else None,
        "current_sign": current_sign,
        "next_sign": next_sign,
        "last_aspect": {
            "time": aspect_time.isoformat(),
            "type": aspect_name,
            "with": planet_name
        }
    }


def find_lunar_phase_changes(start_date: datetime, end_date: datetime) -> List[Dict[str, Any]]:
    """
    Find all lunar phase changes in date range

    Args:
        start_date: Start datetime (UTC)
        end_date: End datetime (UTC)

    Returns:
        List of phase change events:
        [
            {
                "datetime": "2025-01-29T12:00:00Z",
                "phase": "Nouvelle Lune",
                "moon_longitude": 309.5,
                "moon_sign": "Aquarius"
            },
            ...
        ]
    """
    phase_changes = []
    current_dt = start_date
    step = timedelta(hours=1)

    prev_phase = None

    while current_dt <= end_date:
        moon_pos = get_moon_position(current_dt)

        if prev_phase and moon_pos.phase != prev_phase:
            # Phase changed - record it
            phase_changes.append({
                "datetime": current_dt.isoformat(),
                "phase": moon_pos.phase,
                "moon_longitude": moon_pos.longitude,
                "moon_sign": moon_pos.sign
            })

        prev_phase = moon_pos.phase
        current_dt += step

    return phase_changes


def get_lunar_mansion(moon_longitude: float) -> Dict[str, Any]:
    """
    Calculate lunar mansion (1-28) from Moon longitude

    The 28 lunar mansions divide the ecliptic into ~12.86° segments

    Args:
        moon_longitude: Moon's ecliptic longitude (0-360)

    Returns:
        {
            "number": 1-28,
            "name": str,  # Traditional Arabic name
            "degree_start": float,
            "degree_end": float
        }
    """
    mansion_size = 360 / 28  # ~12.857°
    mansion_number = int(moon_longitude / mansion_size) + 1

    # Traditional Arabic mansion names
    mansion_names = [
        "Al-Sharatain", "Al-Butain", "Al-Thurayya", "Al-Dabaran",
        "Al-Haqah", "Al-Hana'h", "Al-Dhira", "Al-Nathrah",
        "Al-Tarf", "Al-Jabhah", "Al-Zubrah", "Al-Sarfah",
        "Al-Awwa", "Al-Simak", "Al-Ghafr", "Al-Zubana",
        "Al-Iklil", "Al-Qalb", "Al-Shawlah", "Al-Na'am",
        "Al-Baldah", "Sa'd al-Dhabih", "Sa'd Bula", "Sa'd al-Su'ud",
        "Sa'd al-Akhbiyah", "Al-Fargh al-Mukdim", "Al-Fargh al-Thani", "Batn al-Hut"
    ]

    degree_start = (mansion_number - 1) * mansion_size
    degree_end = mansion_number * mansion_size

    return {
        "number": mansion_number,
        "name": mansion_names[mansion_number - 1],
        "degree_start": round(degree_start, 2),
        "degree_end": round(degree_end, 2)
    }


# Cache for performance (optional)
_cache: Dict[str, Any] = {}


def clear_cache():
    """Clear all caches"""
    global _cache
    _cache.clear()
    logger.info("[Swiss Ephemeris] Cache cleared")
