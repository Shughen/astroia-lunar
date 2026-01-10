"""
Service pour calculer la position actuelle de la Lune avec Swiss Ephemeris
Calcule la longitude écliptique, le signe zodiacal et la phase lunaire
"""

try:
    import swisseph as swe
    SWISS_EPHEMERIS_AVAILABLE = True
except ImportError:
    SWISS_EPHEMERIS_AVAILABLE = False
    swe = None

from datetime import datetime, timezone
from typing import Dict, Any
import logging
from functools import lru_cache
import time

logger = logging.getLogger(__name__)

# Cache global avec timestamp
_CACHE: Dict[str, Any] = {
    "data": None,
    "timestamp": 0,
    "ttl": 300  # 5 minutes en secondes
}


def degree_to_sign(degree: float) -> str:
    """
    Convertit un degré zodiacal (0-360) en signe astrologique

    Args:
        degree: Degré écliptique (0-360)

    Returns:
        Nom du signe zodiacal
    """
    signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    # Normaliser le degré dans l'intervalle 0-360
    normalized_degree = degree % 360

    # Chaque signe fait 30°
    sign_index = int(normalized_degree / 30)

    # Sécurité : si on dépasse 11, retourner Pisces
    if sign_index > 11:
        sign_index = 11

    return signs[sign_index]


def calculate_moon_phase(moon_longitude: float, sun_longitude: float) -> str:
    """
    Calcule la phase lunaire à partir de l'élongation Soleil-Lune

    Args:
        moon_longitude: Longitude écliptique de la Lune (0-360°)
        sun_longitude: Longitude écliptique du Soleil (0-360°)

    Returns:
        Nom de la phase lunaire
    """
    # Calcul de l'élongation (angle Soleil-Lune)
    elongation = (moon_longitude - sun_longitude) % 360

    # Mapping des phases selon l'élongation
    # Nouvelle Lune: 0° ± 22.5° (337.5° - 22.5°)
    # Premier Croissant: 22.5° - 67.5°
    # Premier Quartier: 67.5° - 112.5°
    # Lune Gibbeuse: 112.5° - 157.5°
    # Pleine Lune: 157.5° - 202.5° (180° ± 22.5°)
    # Lune Disseminante: 202.5° - 247.5°
    # Dernier Quartier: 247.5° - 292.5°
    # Dernier Croissant: 292.5° - 337.5°

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


def get_current_moon_position() -> Dict[str, Any]:
    """
    Calcule la position actuelle de la Lune avec cache de 5 minutes

    Returns:
        {
            "sign": "Gemini",
            "degree": 67.5,
            "phase": "Premier Quartier"
        }

    Raises:
        Exception: Si le calcul Swiss Ephemeris échoue
    """
    global _CACHE

    if not SWISS_EPHEMERIS_AVAILABLE:
        logger.warning("[MoonPosition] ⚠️ Swiss Ephemeris non disponible - retour données mock")
        # Retourner des données mock minimales
        return {
            "sign": "Gemini",
            "degree": 67.5,
            "phase": "Premier Quartier"
        }

    # Vérifier le cache
    current_time = time.time()
    if _CACHE["data"] is not None and (current_time - _CACHE["timestamp"]) < _CACHE["ttl"]:
        logger.info(f"[MoonPosition] Cache hit (age: {int(current_time - _CACHE['timestamp'])}s)")
        return _CACHE["data"]

    try:
        # Date/heure actuelle en UTC
        now = datetime.now(timezone.utc)

        # Convertir en Julian Day Number pour Swiss Ephemeris
        julian_day = swe.julday(
            now.year,
            now.month,
            now.day,
            now.hour + now.minute / 60.0 + now.second / 3600.0
        )

        logger.info(f"[MoonPosition] Calcul pour JD={julian_day:.6f} ({now.isoformat()})")

        # Calculer la position de la Lune
        # swe.MOON = 1, swe.FLG_SWIEPH = 2 (fichiers ephemeris Swiss)
        moon_result = swe.calc_ut(julian_day, swe.MOON, swe.FLG_SWIEPH)
        moon_longitude = moon_result[0][0]  # Longitude écliptique en degrés

        # Calculer la position du Soleil pour la phase lunaire
        sun_result = swe.calc_ut(julian_day, swe.SUN, swe.FLG_SWIEPH)
        sun_longitude = sun_result[0][0]

        # Déterminer le signe zodiacal
        sign = degree_to_sign(moon_longitude)

        # Calculer la phase lunaire
        phase = calculate_moon_phase(moon_longitude, sun_longitude)

        logger.info(
            f"[MoonPosition] ✅ Moon: {moon_longitude:.2f}° ({sign}), "
            f"Sun: {sun_longitude:.2f}°, Phase: {phase}"
        )

        # Construire la réponse
        result = {
            "sign": sign,
            "degree": round(moon_longitude, 2),
            "phase": phase
        }

        # Mettre à jour le cache
        _CACHE["data"] = result
        _CACHE["timestamp"] = current_time

        return result

    except Exception as e:
        logger.error(f"[MoonPosition] ❌ Erreur calcul Swiss Ephemeris: {e}", exc_info=True)
        raise Exception(f"Failed to calculate moon position: {str(e)}")


def clear_cache():
    """Efface le cache (utile pour les tests)"""
    global _CACHE
    _CACHE["data"] = None
    _CACHE["timestamp"] = 0
    logger.info("[MoonPosition] Cache cleared")
