"""
Tests pour le service de lecture de thème natal
"""

import pytest
from services.natal_reading_service import (
    generate_cache_key,
    parse_positions_to_core_points,
    parse_aspects,
    parse_lunar_info,
    build_summary
)


class TestCacheKey:
    """Tests pour la génération de clés de cache"""
    
    def test_same_birth_data_same_key(self):
        """Mêmes données → même clé"""
        birth_data1 = {
            'year': 1989,
            'month': 11,
            'day': 1,
            'hour': 13,
            'minute': 20,
            'second': 0,
            'latitude': -3.1316,
            'longitude': -59.9825,
            'city': 'Manaus',
            'country_code': 'BR'
        }
        
        birth_data2 = birth_data1.copy()
        
        key1 = generate_cache_key(birth_data1)
        key2 = generate_cache_key(birth_data2)
        
        assert key1 == key2
        assert len(key1) == 32  # SHA256 tronqué
    
    def test_different_time_different_key(self):
        """Heure différente → clé différente"""
        birth_data1 = {
            'year': 1989,
            'month': 11,
            'day': 1,
            'hour': 13,
            'minute': 20,
            'second': 0,
            'latitude': -3.1316,
            'longitude': -59.9825,
            'city': 'Manaus',
            'country_code': 'BR'
        }
        
        birth_data2 = birth_data1.copy()
        birth_data2['hour'] = 14  # 1h de différence
        
        key1 = generate_cache_key(birth_data1)
        key2 = generate_cache_key(birth_data2)
        
        assert key1 != key2
    
    def test_different_place_different_key(self):
        """Lieu différent → clé différente"""
        birth_data1 = {
            'year': 1989,
            'month': 11,
            'day': 1,
            'hour': 13,
            'minute': 20,
            'second': 0,
            'latitude': -3.1316,
            'longitude': -59.9825,
            'city': 'Manaus',
            'country_code': 'BR'
        }
        
        birth_data2 = birth_data1.copy()
        birth_data2['latitude'] = 48.8566
        birth_data2['longitude'] = 2.3522
        birth_data2['city'] = 'Paris'
        
        key1 = generate_cache_key(birth_data1)
        key2 = generate_cache_key(birth_data2)
        
        assert key1 != key2


class TestPositionsParsing:
    """Tests pour le parsing des positions"""
    
    def test_parse_positions_basic(self):
        """Parser des positions de base"""
        mock_data = {
            'subject_data': {
                'sun': {
                    'name': 'Sun',
                    'sign': 'Sco',
                    'position': 9.26,
                    'abs_pos': 219.26,
                    'emoji': '♏️',
                    'element': 'Water',
                    'house': 'Ninth_House',
                    'retrograde': False
                },
                'moon': {
                    'name': 'Moon',
                    'sign': 'Sag',
                    'position': 13.02,
                    'abs_pos': 253.02,
                    'emoji': '♐️',
                    'element': 'Fire',
                    'house': 'Tenth_House',
                    'retrograde': False
                }
            }
        }
        
        positions = parse_positions_to_core_points(mock_data)
        
        assert len(positions) >= 2
        
        sun = next((p for p in positions if p['name'] == 'Sun'), None)
        assert sun is not None
        assert sun['sign_fr'] == 'Scorpion'
        assert sun['element'] == 'Eau'
        assert sun['house'] == 9
        
        moon = next((p for p in positions if p['name'] == 'Moon'), None)
        assert moon is not None
        assert moon['sign_fr'] == 'Sagittaire'
        assert moon['element'] == 'Feu'
        assert moon['house'] == 10


class TestAspectsParsing:
    """Tests pour le parsing des aspects"""
    
    def test_aspect_strength_calculation(self):
        """Calcul de la force des aspects basé sur l'orbe"""
        mock_data = {
            'chart_data': {
                'aspects': [
                    {'point1': 'Sun', 'point2': 'Moon', 'aspect_type': 'trine', 'orb': 0.5},  # strong
                    {'point1': 'Sun', 'point2': 'Mars', 'aspect_type': 'square', 'orb': 2.0},  # medium
                    {'point1': 'Moon', 'point2': 'Venus', 'aspect_type': 'sextile', 'orb': 5.0},  # weak
                ]
            }
        }
        
        aspects = parse_aspects(mock_data)
        
        assert len(aspects) == 3
        assert aspects[0]['strength'] == 'strong'
        assert aspects[1]['strength'] == 'medium'
        assert aspects[2]['strength'] == 'weak'


class TestSummaryBuilding:
    """Tests pour la construction du résumé"""
    
    def test_build_summary_with_big_three(self):
        """Résumé avec Big 3"""
        positions = [
            {'name': 'Sun', 'sign_fr': 'Scorpion', 'element': 'Eau', 'interpretations': {'in_sign': 'Test'}},
            {'name': 'Moon', 'sign_fr': 'Sagittaire', 'element': 'Feu', 'interpretations': {'in_sign': 'Test'}},
            {'name': 'Ascendant', 'sign_fr': 'Verseau', 'element': 'Air', 'interpretations': {'in_sign': 'Test'}},
            {'name': 'Mercury', 'sign_fr': 'Scorpion', 'element': 'Eau', 'interpretations': {}},
        ]
        
        summary = build_summary(positions, [])
        
        assert summary['big_three']['sun']['name'] == 'Sun'
        assert summary['big_three']['moon']['name'] == 'Moon'
        assert summary['big_three']['ascendant']['name'] == 'Ascendant'
        assert summary['dominant_element'] == 'Eau'  # 2 planètes en Eau
        assert len(summary['personality_highlights']) >= 2


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

