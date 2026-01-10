"""
Tests unitaires pour le service de lecture natale V2
"""

import json
import pytest
from pathlib import Path

from services.natal_reading_service import (
    parse_positions_from_natal_chart,
    parse_aspects_from_natal_chart,
    build_summary,
    generate_cache_key
)


# Load fixture
FIXTURE_PATH = Path(__file__).parent / "fixtures" / "natal_chart_sample.json"
with open(FIXTURE_PATH, 'r') as f:
    SAMPLE_CHART = json.load(f)


def test_parse_positions_returns_14_points():
    """Vérifie qu'on parse bien 14 positions depuis le fixture"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    assert len(positions) == 14, "Devrait parser 14 positions"
    
    # Vérifier que les noms clés sont présents
    names = [p['name'] for p in positions]
    assert 'Sun' in names
    assert 'Moon' in names
    assert 'Ascendant' in names
    assert 'Jupiter' in names


def test_parse_positions_calculates_degrees_correctly():
    """Vérifie que les degrés sont calculés depuis absolute_longitude"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    # Sun: absolute_longitude = 219.2684731153279 → 219.27 % 30 = 9.27°
    sun = next((p for p in positions if p['name'] == 'Sun'), None)
    assert sun is not None
    assert sun['degree'] > 0, "Le degré du Soleil ne devrait pas être 0"
    assert 9.0 < sun['degree'] < 10.0, f"Soleil devrait être ~9.27°, got {sun['degree']}"
    
    # Moon: absolute_longitude = 253.0219293628491 → 253.02 % 30 = 13.02°
    moon = next((p for p in positions if p['name'] == 'Moon'), None)
    assert moon is not None
    assert moon['degree'] > 0
    assert 13.0 < moon['degree'] < 14.0, f"Lune devrait être ~13.02°, got {moon['degree']}"


def test_parse_positions_includes_french_signs():
    """Vérifie que les signes sont traduits en français"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    sun = next((p for p in positions if p['name'] == 'Sun'), None)
    assert sun['sign'] == 'Sco'
    assert sun['sign_fr'] == 'Scorpion'
    
    moon = next((p for p in positions if p['name'] == 'Moon'), None)
    assert moon['sign'] == 'Sag'
    assert moon['sign_fr'] == 'Sagittaire'


def test_parse_positions_includes_elements():
    """Vérifie que les éléments sont correctement mappés"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    sun = next((p for p in positions if p['name'] == 'Sun'), None)
    assert sun['element'] == 'Eau', "Scorpion devrait être Eau"
    
    moon = next((p for p in positions if p['name'] == 'Moon'), None)
    assert moon['element'] == 'Feu', "Sagittaire devrait être Feu"


def test_parse_positions_includes_emojis():
    """Vérifie que les emojis sont correctement assignés"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    sun = next((p for p in positions if p['name'] == 'Sun'), None)
    assert sun['emoji'] == '☀️'
    
    moon = next((p for p in positions if p['name'] == 'Moon'), None)
    assert moon['emoji'] == '🌙'


def test_parse_positions_detects_retrograde():
    """Vérifie que les rétrogradations sont détectées"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    
    jupiter = next((p for p in positions if p['name'] == 'Jupiter'), None)
    assert jupiter is not None
    assert jupiter['is_retrograde'] is True, "Jupiter devrait être rétrograde dans le fixture"
    
    sun = next((p for p in positions if p['name'] == 'Sun'), None)
    assert sun['is_retrograde'] is False, "Le Soleil ne devrait jamais être rétrograde"


def test_parse_aspects_returns_some_aspects():
    """Vérifie qu'on parse bien les aspects depuis le fixture"""
    aspects = parse_aspects_from_natal_chart(SAMPLE_CHART)
    
    assert len(aspects) >= 3, "Devrait parser au moins 3 aspects"
    
    # Vérifier la structure
    first_aspect = aspects[0]
    assert 'from' in first_aspect
    assert 'to' in first_aspect
    assert 'aspect_type' in first_aspect
    assert 'orb' in first_aspect
    assert 'strength' in first_aspect


def test_parse_aspects_calculates_strength():
    """Vérifie que la force des aspects est calculée correctement"""
    aspects = parse_aspects_from_natal_chart(SAMPLE_CHART)
    
    # Sun-Saturn sextile orb=0.110 → strong
    sun_saturn = next((a for a in aspects if 
                       (a['from'] == 'Sun' and a['to'] == 'Saturn') or
                       (a['from'] == 'Saturn' and a['to'] == 'Sun')), None)
    
    if sun_saturn:
        assert sun_saturn['strength'] == 'strong', "Orbe < 1.5 devrait être 'strong'"


def test_parse_aspects_handles_missing_aspects():
    """Vérifie que le parser gère l'absence d'aspects"""
    empty_chart = {"chart_data": {"aspects": []}}
    aspects = parse_aspects_from_natal_chart(empty_chart)
    
    assert aspects == []


def test_build_summary_extracts_big_three():
    """Vérifie que build_summary extrait le Big 3 correctement"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    summary = build_summary(positions)
    
    assert 'big_three' in summary
    assert summary['big_three']['sun'] is not None
    assert summary['big_three']['moon'] is not None
    assert summary['big_three']['ascendant'] is not None
    
    # Vérifier les valeurs
    assert summary['big_three']['sun']['name'] == 'Sun'
    assert summary['big_three']['moon']['name'] == 'Moon'
    assert summary['big_three']['ascendant']['name'] == 'Ascendant'


def test_build_summary_calculates_dominant_element():
    """Vérifie que l'élément dominant est calculé"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    summary = build_summary(positions)
    
    assert 'dominant_element' in summary
    assert summary['dominant_element'] in ['Feu', 'Terre', 'Air', 'Eau']


def test_build_summary_creates_highlights():
    """Vérifie que les highlights sont créés"""
    positions = parse_positions_from_natal_chart(SAMPLE_CHART)
    summary = build_summary(positions)
    
    assert 'personality_highlights' in summary
    assert len(summary['personality_highlights']) >= 2
    assert any('Soleil' in h for h in summary['personality_highlights'])
    assert any('Lune' in h for h in summary['personality_highlights'])


def test_generate_cache_key_is_unique():
    """Vérifie que la clé de cache est unique et déterministe"""
    birth_data_1 = {
        'year': 1989,
        'month': 11,
        'day': 1,
        'hour': 13,
        'minute': 20,
        'second': 0,
        'city': 'Manaus',
        'country_code': 'BR',
        'latitude': -3.1316333,
        'longitude': -59.9825041
    }
    
    birth_data_2 = {
        'year': 1989,
        'month': 11,
        'day': 1,
        'hour': 13,
        'minute': 21,  # Différent !
        'second': 0,
        'city': 'Manaus',
        'country_code': 'BR',
        'latitude': -3.1316333,
        'longitude': -59.9825041
    }
    
    key1a = generate_cache_key(birth_data_1)
    key1b = generate_cache_key(birth_data_1)
    key2 = generate_cache_key(birth_data_2)
    
    # Même données → même clé
    assert key1a == key1b
    
    # Données différentes → clés différentes
    assert key1a != key2
    
    # Taille correcte (32 caractères)
    assert len(key1a) == 32


def test_parse_positions_handles_empty_chart():
    """Vérifie que le parser gère un chart vide proprement"""
    empty_chart = {"chart_data": {"positions": []}}
    positions = parse_positions_from_natal_chart(empty_chart)
    
    assert positions == []


def test_parse_positions_handles_missing_chart_data():
    """Vérifie que le parser gère l'absence de chart_data"""
    invalid_chart = {}
    positions = parse_positions_from_natal_chart(invalid_chart)
    
    assert positions == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

