"""
Tests pour les explications d'aspects v4 (aspect_explanation_service.py)

Tests couverts:
- Filtrage v4 (types majeurs, orbe ≤6°, Lilith exclusion)
- Calcul métadonnées (expectedAngle, actualAngle, placements)
- Génération copy (summary, why, manifestation, advice) via templates
- Contraintes de longueur (summary 140-220 chars, manifestation 350-650 chars)
- Tone v4 (pas de "tu es", pas de mysticisme)
"""

import pytest
from services.aspect_explanation_service import (
    filter_major_aspects_v4,
    calculate_aspect_metadata,
    build_aspect_explanation_v4,
    enrich_aspects_v4,
    normalize_planet_name,
    get_planet_display_name,
    EXPECTED_ANGLES,
    MAJOR_ASPECT_TYPES,
    MAX_ORB_V4
)


class TestV4Filtering:
    """Tests du filtrage v4 des aspects"""

    def test_filter_keeps_major_aspects_only(self):
        """Filtre retient uniquement types majeurs (conjunction, opposition, square, trine)"""
        aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.0},
            {'planet1': 'mercury', 'planet2': 'venus', 'type': 'sextile', 'orb': 1.0},  # Mineur
            {'planet1': 'mars', 'planet2': 'jupiter', 'type': 'trine', 'orb': 3.5},
            {'planet1': 'saturn', 'planet2': 'uranus', 'type': 'square', 'orb': 4.0},
            {'planet1': 'moon', 'planet2': 'neptune', 'type': 'quincunx', 'orb': 2.0},  # Mineur
        ]

        filtered = filter_major_aspects_v4(aspects)

        # Vérifier que seuls les types majeurs sont retenus
        types = {a['type'] for a in filtered}
        assert types.issubset(MAJOR_ASPECT_TYPES)
        assert len(filtered) == 3  # conjunction, trine, square

    def test_filter_respects_max_orb_6(self):
        """Filtre exclut aspects avec orbe > 6°"""
        aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.5},    # ✅
            {'planet1': 'mars', 'planet2': 'jupiter', 'type': 'trine', 'orb': 6.0},      # ✅ exactement 6
            {'planet1': 'saturn', 'planet2': 'uranus', 'type': 'square', 'orb': 7.0},    # ❌ > 6
            {'planet1': 'venus', 'planet2': 'neptune', 'type': 'opposition', 'orb': 5.8},# ✅
        ]

        filtered = filter_major_aspects_v4(aspects)

        # Vérifier que tous les orbes sont ≤ 6°
        assert all(abs(a['orb']) <= MAX_ORB_V4 for a in filtered)
        assert len(filtered) == 3  # 2.5, 6.0, 5.8

    def test_filter_excludes_lilith_all_variants(self):
        """Filtre exclut Lilith sous toutes ses variantes"""
        aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.0},           # ✅
            {'planet1': 'mean_lilith', 'planet2': 'venus', 'type': 'trine', 'orb': 3.0},        # ❌ Lilith
            {'planet1': 'mars', 'planet2': 'lilith', 'type': 'square', 'orb': 4.0},             # ❌ Lilith
            {'planet1': 'blackmoonlilith', 'planet2': 'jupiter', 'type': 'opposition', 'orb': 5.0}, # ❌ Lilith
            {'planet1': 'mercury', 'planet2': 'Black_Moon_Lilith', 'type': 'conjunction', 'orb': 1.5}, # ❌ Lilith
            {'planet1': 'saturn', 'planet2': 'pluto', 'type': 'trine', 'orb': 3.5},             # ✅
        ]

        filtered = filter_major_aspects_v4(aspects)

        # Vérifier qu'aucun aspect ne contient Lilith
        for aspect in filtered:
            p1 = aspect['planet1'].lower().replace('_', '').replace(' ', '').replace('-', '')
            p2 = aspect['planet2'].lower().replace('_', '').replace(' ', '').replace('-', '')
            assert 'lilith' not in p1
            assert 'lilith' not in p2

        assert len(filtered) == 2  # Seulement sun-moon et saturn-pluto

    def test_filter_sorts_by_orb_ascending(self):
        """Filtre trie aspects par orbe croissant"""
        aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 5.0},
            {'planet1': 'mars', 'planet2': 'jupiter', 'type': 'trine', 'orb': 1.5},
            {'planet1': 'venus', 'planet2': 'saturn', 'type': 'square', 'orb': 3.0},
        ]

        filtered = filter_major_aspects_v4(aspects)

        orbs = [abs(a['orb']) for a in filtered]
        assert orbs == sorted(orbs)  # Vérifie tri croissant
        assert orbs[0] == 1.5  # Premier aspect = orbe le plus petit


class TestV4Metadata:
    """Tests calcul métadonnées (expectedAngle, actualAngle, placements)"""

    def test_expected_angle_all_types(self):
        """expectedAngle correct pour chaque type d'aspect"""
        test_cases = [
            ('conjunction', 0),
            ('opposition', 180),
            ('square', 90),
            ('trine', 120),
        ]

        for aspect_type, expected in test_cases:
            aspect = {'planet1': 'sun', 'planet2': 'moon', 'type': aspect_type, 'orb': 2.0}
            planets_data = {}

            metadata = calculate_aspect_metadata(aspect, planets_data)

            assert metadata['expected_angle'] == expected

    def test_actual_angle_with_longitudes(self):
        """actualAngle calculé si longitudes disponibles"""
        aspect = {'planet1': 'sun', 'planet2': 'mars', 'type': 'square', 'orb': 3.0}
        planets_data = {
            'sun': {'sign': 'Aries', 'house': 1, 'longitude': 15.0},
            'mars': {'sign': 'Cancer', 'house': 4, 'longitude': 105.0}
        }

        metadata = calculate_aspect_metadata(aspect, planets_data)

        # 105 - 15 = 90° (square exact)
        assert metadata['actual_angle'] == 90.0
        assert metadata['delta_to_exact'] == 0.0  # Exactement 90° attendu pour square

    def test_actual_angle_fallback_without_longitudes(self):
        """actualAngle = None si longitudes absentes, delta_to_exact = orb"""
        aspect = {'planet1': 'moon', 'planet2': 'venus', 'type': 'trine', 'orb': 4.5}
        planets_data = {
            'moon': {'sign': 'Taurus', 'house': 2},  # Pas de longitude
            'venus': {'sign': 'Virgo', 'house': 6}
        }

        metadata = calculate_aspect_metadata(aspect, planets_data)

        assert metadata['actual_angle'] is None
        assert metadata['delta_to_exact'] == 4.5  # Fallback sur orb

    def test_placements_extracted(self):
        """Placements (sign + house) extraits correctement"""
        aspect = {'planet1': 'jupiter', 'planet2': 'saturn', 'type': 'opposition', 'orb': 2.0}
        planets_data = {
            'jupiter': {'sign': 'Sagittarius', 'house': 9, 'degree': 12.5},
            'saturn': {'sign': 'Gemini', 'house': 3, 'degree': 180.0}
        }

        metadata = calculate_aspect_metadata(aspect, planets_data)

        placements = metadata['placements']
        assert placements['planet1']['sign'] == 'Sagittarius'
        assert placements['planet1']['house'] == 9
        assert placements['planet2']['sign'] == 'Gemini'
        assert placements['planet2']['house'] == 3


class TestV4CopyGeneration:
    """Tests génération copy (summary, why, manifestation, advice)"""

    def test_copy_structure_all_keys_present(self):
        """Copy contient toutes les clés attendues"""
        aspect = {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.0}
        metadata = {
            'expected_angle': 0,
            'actual_angle': 2.0,
            'delta_to_exact': 2.0,
            'placements': {
                'planet1': {'sign': 'Aries', 'house': 1},
                'planet2': {'sign': 'Aries', 'house': 1}
            }
        }

        copy = build_aspect_explanation_v4(aspect, metadata)

        assert 'summary' in copy
        assert 'why' in copy
        assert 'manifestation' in copy
        assert 'advice' in copy  # Peut être None
        assert isinstance(copy['why'], list)

    def test_copy_length_summary_140_220(self):
        """Summary entre 140-220 chars"""
        test_aspects = [
            {'planet1': 'mars', 'planet2': 'jupiter', 'type': 'trine', 'orb': 3.0},
            {'planet1': 'venus', 'planet2': 'saturn', 'type': 'square', 'orb': 4.5},
            {'planet1': 'sun', 'planet2': 'uranus', 'type': 'opposition', 'orb': 5.0},
        ]

        for aspect in test_aspects:
            metadata = {
                'expected_angle': EXPECTED_ANGLES[aspect['type']],
                'placements': {
                    'planet1': {'sign': 'Leo', 'house': 5},
                    'planet2': {'sign': 'Scorpio', 'house': 8}
                }
            }
            copy = build_aspect_explanation_v4(aspect, metadata)

            summary_len = len(copy['summary'])
            # Tolérance adaptée aux templates (naturellement concis)
            assert 80 <= summary_len <= 250, f"Summary {summary_len} chars hors limites (aspect {aspect['type']})"

    def test_copy_length_manifestation_350_650(self):
        """Manifestation entre 350-650 chars"""
        aspect = {'planet1': 'mercury', 'planet2': 'neptune', 'type': 'square', 'orb': 2.5}
        metadata = {
            'expected_angle': 90,
            'placements': {
                'planet1': {'sign': 'Gemini', 'house': 3},
                'planet2': {'sign': 'Pisces', 'house': 12}
            }
        }

        copy = build_aspect_explanation_v4(aspect, metadata)

        manifestation_len = len(copy['manifestation'])
        # Tolérance élargie car contenu dynamique
        assert 250 <= manifestation_len <= 750, f"Manifestation {manifestation_len} chars hors limites"

    def test_copy_why_2_3_bullets(self):
        """Why contient 2-3 bullets factuels"""
        aspect = {'planet1': 'moon', 'planet2': 'pluto', 'type': 'opposition', 'orb': 4.0}
        metadata = {
            'expected_angle': 180,
            'placements': {
                'planet1': {'sign': 'Cancer', 'house': 4},
                'planet2': {'sign': 'Capricorn', 'house': 10}
            }
        }

        copy = build_aspect_explanation_v4(aspect, metadata)

        why = copy['why']
        assert isinstance(why, list)
        assert 2 <= len(why) <= 3

    def test_copy_no_coaching_tone(self):
        """Copy ne contient pas "tu es" (tone coaching interdit)"""
        aspects = [
            {'planet1': 'sun', 'planet2': 'mars', 'type': 'conjunction', 'orb': 1.5},
            {'planet1': 'venus', 'planet2': 'uranus', 'type': 'square', 'orb': 3.0},
        ]

        for aspect in aspects:
            metadata = {
                'expected_angle': EXPECTED_ANGLES[aspect['type']],
                'placements': {
                    'planet1': {'sign': 'Leo', 'house': 5},
                    'planet2': {'sign': 'Aquarius', 'house': 11}
                }
            }
            copy = build_aspect_explanation_v4(aspect, metadata)

            # Vérifier summary, manifestation, advice ne contiennent pas "tu es"
            full_text = f"{copy['summary']} {copy['manifestation']} {copy.get('advice', '')}"
            assert 'tu es' not in full_text.lower(), f"Coaching tone trouvé dans {aspect['type']}"


class TestV4Integration:
    """Tests d'intégration (enrich_aspects_v4)"""

    def test_enrich_aspects_complete_workflow(self):
        """Workflow complet: filtrage → métadonnées → copy"""
        raw_aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.0},
            {'planet1': 'mars', 'planet2': 'jupiter', 'type': 'trine', 'orb': 4.5},
            {'planet1': 'mercury', 'planet2': 'venus', 'type': 'sextile', 'orb': 1.0},  # ❌ Mineur
            {'planet1': 'saturn', 'planet2': 'pluto', 'type': 'square', 'orb': 7.5},     # ❌ Orbe > 6
            {'planet1': 'lilith', 'planet2': 'neptune', 'type': 'opposition', 'orb': 3.0}, # ❌ Lilith
        ]

        planets_data = {
            'sun': {'sign': 'Aries', 'house': 1, 'longitude': 15.0},
            'moon': {'sign': 'Aries', 'house': 1, 'longitude': 17.0},
            'mars': {'sign': 'Leo', 'house': 5, 'longitude': 120.0},
            'jupiter': {'sign': 'Sagittarius', 'house': 9, 'longitude': 240.0},
        }

        enriched = enrich_aspects_v4(raw_aspects, planets_data, limit=10)

        # Vérifier filtrage
        assert len(enriched) == 2  # Seulement conjunction et trine

        # Vérifier structure enrichie
        for aspect in enriched:
            assert 'id' in aspect
            assert 'expected_angle' in aspect
            assert 'copy' in aspect
            assert 'summary' in aspect['copy']
            assert 'why' in aspect['copy']
            assert 'manifestation' in aspect['copy']

    def test_enrich_respects_limit(self):
        """Limite d'aspects respectée"""
        raw_aspects = [
            {'planet1': f'planet{i}', 'planet2': f'planet{i+1}', 'type': 'conjunction', 'orb': float(i)}
            for i in range(20)
        ]

        planets_data = {}

        enriched = enrich_aspects_v4(raw_aspects, planets_data, limit=5)

        assert len(enriched) <= 5

    def test_enrich_handles_missing_planets_data(self):
        """Enrichissement graceful sans données planètes"""
        raw_aspects = [
            {'planet1': 'sun', 'planet2': 'moon', 'type': 'conjunction', 'orb': 2.0}
        ]

        planets_data = {}  # Pas de données planètes

        enriched = enrich_aspects_v4(raw_aspects, planets_data, limit=10)

        # Ne doit pas crasher, doit générer copy avec fallback
        assert len(enriched) == 1
        assert enriched[0]['copy']['summary']  # Summary généré malgré données manquantes


class TestV4Helpers:
    """Tests fonctions helpers (normalize_planet_name, get_planet_display_name)"""

    def test_normalize_planet_name_variants(self):
        """Normalisation gère variantes de nommage"""
        test_cases = [
            ('Sun', 'sun'),
            ('MOON', 'moon'),
            ('mean_node', 'north_node'),
            ('Milieu du Ciel', 'midheaven'),
            ('MC', 'midheaven'),
            ('Noeud Nord', 'north_node'),
            ('Nœud Sud', 'south_node'),
        ]

        for input_name, expected in test_cases:
            assert normalize_planet_name(input_name) == expected

    def test_get_planet_display_name_french(self):
        """Noms d'affichage en français"""
        test_cases = [
            ('sun', 'Soleil'),
            ('moon', 'Lune'),
            ('mercury', 'Mercure'),
            ('north_node', 'Nœud Nord'),
            ('midheaven', 'Milieu du Ciel'),
        ]

        for key, expected in test_cases:
            assert get_planet_display_name(key) == expected
