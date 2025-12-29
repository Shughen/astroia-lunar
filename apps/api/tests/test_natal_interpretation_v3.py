"""
Tests pour la version 3 des interprétations natales (baseline avant v4)
v3 = prompt senior expérimental (à déprécier au profit de v4)
"""

import pytest
from schemas.natal_interpretation import ChartPayload
from services.natal_interpretation_service import (
    find_relevant_aspect_v3,
    validate_interpretation_length
)


class TestV3AspectFiltering:
    """Tests du filtrage des aspects v3 (aspects majeurs orb ≤6°)"""

    def test_v3_filters_only_major_aspects(self):
        """v3 ne retient que conjonction, opposition, carré, trigone"""
        # Payload avec plusieurs aspects dont seuls les majeurs doivent être retenus
        payload = ChartPayload(
            subject_label="Soleil",
            sign="Bélier",
            house=1,
            aspects=[
                {"planet1": "sun", "planet2": "mars", "type": "conjunction", "orb": 2.0},
                {"planet1": "sun", "planet2": "venus", "type": "sextile", "orb": 1.5},  # Non-majeur → ignoré
                {"planet1": "sun", "planet2": "jupiter", "type": "trine", "orb": 4.0},
                {"planet1": "sun", "planet2": "saturn", "type": "quincunx", "orb": 2.0},  # Non-majeur → ignoré
            ]
        )

        # Doit retourner le premier aspect majeur (conjunction)
        result = find_relevant_aspect_v3("sun", payload)
        assert result is not None
        assert "conjonction" in result.lower()
        assert "mars" in result.lower()

    def test_v3_respects_orb_6_degrees(self):
        """v3 ignore aspects > 6°"""
        payload = ChartPayload(
            subject_label="Lune",
            sign="Taureau",
            house=2,
            aspects=[
                {"planet1": "moon", "planet2": "venus", "type": "trine", "orb": 6.5},  # > 6° → ignoré
                {"planet1": "moon", "planet2": "mars", "type": "square", "orb": 7.0},  # > 6° → ignoré
            ]
        )

        result = find_relevant_aspect_v3("moon", payload)
        assert result is None  # Aucun aspect ≤6° disponible

    def test_v3_accepts_exact_6_degree_orb(self):
        """v3 accepte orb = 6.0° exactement"""
        payload = ChartPayload(
            subject_label="Mercure",
            sign="Gémeaux",
            house=3,
            aspects=[
                {"planet1": "mercury", "planet2": "uranus", "type": "opposition", "orb": 6.0},
            ]
        )

        result = find_relevant_aspect_v3("mercury", payload)
        assert result is not None
        assert "opposition" in result.lower()
        assert "6.0°" in result

    def test_v3_excludes_sextile(self):
        """v3 exclut sextile même avec orb faible"""
        payload = ChartPayload(
            subject_label="Vénus",
            sign="Balance",
            house=7,
            aspects=[
                {"planet1": "venus", "planet2": "mars", "type": "sextile", "orb": 0.5},  # Sextile → ignoré
                {"planet1": "venus", "planet2": "neptune", "type": "square", "orb": 5.0},
            ]
        )

        result = find_relevant_aspect_v3("venus", payload)
        assert result is not None
        assert "carré" in result.lower()  # Doit retourner le carré, pas le sextile

    def test_v3_excludes_quincunx(self):
        """v3 exclut quincunx (aspect mineur)"""
        payload = ChartPayload(
            subject_label="Mars",
            sign="Scorpion",
            house=8,
            aspects=[
                {"planet1": "mars", "planet2": "jupiter", "type": "quincunx", "orb": 1.0},  # Quincunx → ignoré
            ]
        )

        result = find_relevant_aspect_v3("mars", payload)
        assert result is None

    def test_v3_handles_north_node_variants(self):
        """v3 gère les variantes de nommage du Nœud Nord"""
        payload = ChartPayload(
            subject_label="Nœud Nord",
            sign="Verseau",
            house=11,
            aspects=[
                {"planet1": "mean_node", "planet2": "sun", "type": "conjunction", "orb": 3.0},
            ]
        )

        result = find_relevant_aspect_v3("north_node", payload)
        assert result is not None
        assert "conjonction" in result.lower()

    def test_v3_returns_first_major_aspect(self):
        """v3 retourne le premier aspect majeur valide (pas tous)"""
        payload = ChartPayload(
            subject_label="Jupiter",
            sign="Sagittaire",
            house=9,
            aspects=[
                {"planet1": "jupiter", "planet2": "sun", "type": "trine", "orb": 2.0},
                {"planet1": "jupiter", "planet2": "moon", "type": "square", "orb": 3.0},
                {"planet1": "jupiter", "planet2": "venus", "type": "opposition", "orb": 4.0},
            ]
        )

        result = find_relevant_aspect_v3("jupiter", payload)
        # Doit retourner uniquement le premier (trigone à Soleil)
        assert result is not None
        assert "trigone" in result.lower()
        assert "soleil" in result.lower() or "sun" in result.lower()


class TestV3LengthValidation:
    """Tests de validation de longueur v3 (700-1200 chars)"""

    def test_v3_length_valid_min(self):
        """v3 accepte 700 chars minimum"""
        text = "x" * 700
        is_valid, length = validate_interpretation_length(text, version=3)
        assert is_valid is True
        assert length == 700

    def test_v3_length_valid_max(self):
        """v3 accepte 1200 chars maximum"""
        text = "x" * 1200
        is_valid, length = validate_interpretation_length(text, version=3)
        assert is_valid is True
        assert length == 1200

    def test_v3_length_too_short(self):
        """v3 rejette < 700 chars"""
        text = "x" * 699
        is_valid, length = validate_interpretation_length(text, version=3)
        assert is_valid is False
        assert length == 699

    def test_v3_length_too_long(self):
        """v3 rejette > 1200 chars"""
        text = "x" * 1201
        is_valid, length = validate_interpretation_length(text, version=3)
        assert is_valid is False
        assert length == 1201

    def test_v3_length_optimal(self):
        """v3 accepte longueur optimale 900 chars"""
        text = "x" * 900
        is_valid, length = validate_interpretation_length(text, version=3)
        assert is_valid is True
        assert length == 900


class TestV3AspectEdgeCases:
    """Tests des cas limites v3"""

    def test_v3_handles_empty_aspects(self):
        """v3 gère payload sans aspects"""
        payload = ChartPayload(
            subject_label="Saturne",
            sign="Capricorne",
            house=10,
            aspects=[]
        )

        result = find_relevant_aspect_v3("saturn", payload)
        assert result is None

    def test_v3_handles_none_aspects(self):
        """v3 gère aspects=None"""
        payload = ChartPayload(
            subject_label="Uranus",
            sign="Verseau",
            house=11,
            aspects=None
        )

        result = find_relevant_aspect_v3("uranus", payload)
        assert result is None

    def test_v3_handles_malformed_aspect(self):
        """v3 gère aspect mal formaté (skip sans crash)"""
        payload = ChartPayload(
            subject_label="Neptune",
            sign="Poissons",
            house=12,
            aspects=[
                {"planet1": "neptune"},  # Aspect incomplet → skip
                {"planet1": "neptune", "planet2": "venus", "type": "trine", "orb": 5.0},
            ]
        )

        result = find_relevant_aspect_v3("neptune", payload)
        # Doit retourner le deuxième aspect valide
        assert result is not None
        assert "trigone" in result.lower()

    def test_v3_handles_invalid_orb(self):
        """v3 gère orb invalide (None, string, etc.)"""
        payload = ChartPayload(
            subject_label="Pluton",
            sign="Scorpion",
            house=8,
            aspects=[
                {"planet1": "pluto", "planet2": "mars", "type": "conjunction", "orb": None},  # Orb None → skip
                {"planet1": "pluto", "planet2": "venus", "type": "square", "orb": "invalid"},  # Orb string → skip
                {"planet1": "pluto", "planet2": "sun", "type": "opposition", "orb": 4.5},
            ]
        )

        result = find_relevant_aspect_v3("pluto", payload)
        # Doit retourner le troisième aspect avec orb valide
        assert result is not None
        assert "opposition" in result.lower()
