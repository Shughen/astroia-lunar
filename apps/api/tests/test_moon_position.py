"""
Tests pour le service moon_position (Swiss Ephemeris)
"""

import pytest
from services.moon_position import (
    degree_to_sign,
    calculate_moon_phase,
    get_current_moon_position,
    clear_cache
)


def test_degree_to_sign():
    """Test conversion degré → signe zodiacal"""
    assert degree_to_sign(0) == 'Aries'
    assert degree_to_sign(15) == 'Aries'
    assert degree_to_sign(29.99) == 'Aries'
    assert degree_to_sign(30) == 'Taurus'
    assert degree_to_sign(60) == 'Gemini'
    assert degree_to_sign(90) == 'Cancer'
    assert degree_to_sign(120) == 'Leo'
    assert degree_to_sign(150) == 'Virgo'
    assert degree_to_sign(180) == 'Libra'
    assert degree_to_sign(210) == 'Scorpio'
    assert degree_to_sign(240) == 'Sagittarius'
    assert degree_to_sign(270) == 'Capricorn'
    assert degree_to_sign(300) == 'Aquarius'
    assert degree_to_sign(330) == 'Pisces'
    assert degree_to_sign(359.99) == 'Pisces'

    # Test normalisation 360°+
    assert degree_to_sign(360) == 'Aries'
    assert degree_to_sign(390) == 'Taurus'


def test_calculate_moon_phase():
    """Test calcul phase lunaire selon élongation"""
    # Nouvelle Lune (0° ± 22.5°)
    assert calculate_moon_phase(0, 0) == 'Nouvelle Lune'
    assert calculate_moon_phase(10, 5) == 'Nouvelle Lune'
    assert calculate_moon_phase(350, 340) == 'Nouvelle Lune'

    # Premier Croissant (22.5° - 67.5°)
    assert calculate_moon_phase(50, 0) == 'Premier Croissant'

    # Premier Quartier (67.5° - 112.5°)
    assert calculate_moon_phase(90, 0) == 'Premier Quartier'

    # Lune Gibbeuse (112.5° - 157.5°)
    assert calculate_moon_phase(135, 0) == 'Lune Gibbeuse'

    # Pleine Lune (157.5° - 202.5°)
    assert calculate_moon_phase(180, 0) == 'Pleine Lune'
    assert calculate_moon_phase(200, 20) == 'Pleine Lune'

    # Lune Disseminante (202.5° - 247.5°)
    assert calculate_moon_phase(225, 0) == 'Lune Disseminante'

    # Dernier Quartier (247.5° - 292.5°)
    assert calculate_moon_phase(270, 0) == 'Dernier Quartier'

    # Dernier Croissant (292.5° - 337.5°)
    assert calculate_moon_phase(315, 0) == 'Dernier Croissant'


def test_get_current_moon_position():
    """Test calcul position actuelle de la Lune (Swiss Ephemeris)"""
    # Clear cache avant le test
    clear_cache()

    result = get_current_moon_position()

    # Vérifier structure
    assert 'sign' in result
    assert 'degree' in result
    assert 'phase' in result

    # Vérifier types
    assert isinstance(result['sign'], str)
    assert isinstance(result['degree'], (int, float))
    assert isinstance(result['phase'], str)

    # Vérifier valeurs
    valid_signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    assert result['sign'] in valid_signs
    assert 0 <= result['degree'] < 360

    valid_phases = [
        'Nouvelle Lune', 'Premier Croissant', 'Premier Quartier', 'Lune Gibbeuse',
        'Pleine Lune', 'Lune Disseminante', 'Dernier Quartier', 'Dernier Croissant'
    ]
    assert result['phase'] in valid_phases

    print(f"\n✅ Position lunaire calculée: {result['degree']:.2f}° {result['sign']}, Phase: {result['phase']}")


def test_cache_works():
    """Test que le cache fonctionne (résultat identique en moins de 5 minutes)"""
    clear_cache()

    result1 = get_current_moon_position()
    result2 = get_current_moon_position()

    # Les deux résultats doivent être identiques (cache hit)
    assert result1 == result2
    print(f"\n✅ Cache fonctionne: {result1}")
