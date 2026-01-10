"""
Tests E2E pour la version 4 des interprétations natales (senior professionnel)
v4 = prompt structuré Fonction → Signe → Maison → Manifestations → Vigilance
"""

import pytest
from schemas.natal_interpretation import ChartPayload
from services.natal_interpretation_service import (
    build_interpretation_prompt_v4_senior,
    validate_interpretation_length,
    PLANET_FUNCTIONS_V4,
    get_opposite_sign_v4
)


class TestV4Helpers:
    """Tests des fonctions helpers v4"""

    def test_planet_functions_v4_completeness(self):
        """v4 a des mappings pour tous les sujets principaux"""
        required_subjects = [
            'sun', 'moon', 'mercury', 'venus', 'mars',
            'jupiter', 'saturn', 'uranus', 'neptune', 'pluto',
            'ascendant', 'midheaven', 'north_node', 'south_node', 'chiron'
        ]
        for subject in required_subjects:
            assert subject in PLANET_FUNCTIONS_V4, f"{subject} manquant dans PLANET_FUNCTIONS_V4"
            assert len(PLANET_FUNCTIONS_V4[subject]) > 0, f"Fonction vide pour {subject}"

    def test_planet_functions_v4_content_quality(self):
        """v4 fonctions sont concises et descriptives"""
        for subject, function in PLANET_FUNCTIONS_V4.items():
            # Fonction doit être courte (< 100 chars)
            assert len(function) < 100, f"{subject}: fonction trop longue ({len(function)} chars)"
            # Fonction ne doit pas contenir "tu" (pas coaching)
            assert 'tu ' not in function.lower(), f"{subject}: fonction contient 'tu'"

    def test_get_opposite_sign_v4_all_pairs(self):
        """v4 get_opposite_sign retourne tous les opposés correctement"""
        pairs = [
            ('Bélier', 'Balance'),
            ('Taureau', 'Scorpion'),
            ('Gémeaux', 'Sagittaire'),
            ('Cancer', 'Capricorne'),
            ('Lion', 'Verseau'),
            ('Vierge', 'Poissons')
        ]
        for sign1, sign2 in pairs:
            assert get_opposite_sign_v4(sign1) == sign2
            assert get_opposite_sign_v4(sign2) == sign1

    def test_get_opposite_sign_v4_unknown_sign(self):
        """v4 get_opposite_sign retourne le signe lui-même si inconnu"""
        assert get_opposite_sign_v4('Unknown') == 'Unknown'


class TestV4PromptStructure:
    """Tests de la structure du prompt v4"""

    def test_v4_prompt_standard_planet_structure(self):
        """v4 prompt standard contient les 5 sections obligatoires"""
        payload = ChartPayload(
            subject_label="Soleil",
            sign="Bélier",
            house=1,
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('sun', payload)

        # Vérifier présence des sections obligatoires
        assert "## 1. Fonction planétaire" in prompt
        assert "## 2. Coloration par" in prompt
        assert "## 3. Domaine de vie" in prompt
        assert "## 4. Manifestations observables" in prompt
        assert "## 5. Vigilance" in prompt

        # Vérifier que la fonction planétaire est mentionnée
        assert PLANET_FUNCTIONS_V4['sun'] in prompt

    def test_v4_prompt_north_node_has_axis_context(self):
        """v4 prompt North Node traite l'axe NN/NS"""
        payload = ChartPayload(
            subject_label="Nœud Nord",
            sign="Verseau",
            house=11,
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('north_node', payload)

        # Vérifier contexte axe
        assert "AXE D'ÉVOLUTION" in prompt
        assert "Nœud Nord en Verseau" in prompt
        assert "Nœud Sud en Lion" in prompt  # Opposé de Verseau
        assert "Maison 5" in prompt  # Maison opposée à 11

        # Vérifier sections spéciales pour NN
        assert "## 1. L'axe des Nœuds Lunaires" in prompt
        assert "## 2. Fonction du Nœud Nord" in prompt

    def test_v4_prompt_south_node_has_axis_context(self):
        """v4 prompt South Node traite l'axe NS/NN"""
        payload = ChartPayload(
            subject_label="Nœud Sud",
            sign="Lion",
            house=5,
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('south_node', payload)

        # Vérifier contexte axe
        assert "AXE D'ÉVOLUTION" in prompt
        assert "Nœud Sud en Lion" in prompt
        assert "Nœud Nord en Verseau" in prompt  # Opposé de Lion
        assert "Maison 11" in prompt  # Maison opposée à 5

        # Vérifier sections spéciales pour NS
        assert "## 1. L'axe des Nœuds Lunaires" in prompt
        assert "## 2. Fonction du Nœud Sud" in prompt

    def test_v4_prompt_includes_aspect_if_present(self):
        """v4 prompt intègre aspect majeur si disponible"""
        payload = ChartPayload(
            subject_label="Lune",
            sign="Taureau",
            house=2,
            aspects=[
                {"planet1": "moon", "planet2": "venus", "type": "trine", "orb": 3.5}
            ]
        )
        prompt = build_interpretation_prompt_v4_senior('moon', payload)

        # Aspect doit être mentionné
        assert "Aspect majeur" in prompt or "aspect" in prompt.lower()

    def test_v4_prompt_handles_missing_house(self):
        """v4 prompt gère l'absence de maison"""
        payload = ChartPayload(
            subject_label="Chiron",
            sign="Poissons",
            house=None,  # Pas de maison
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('chiron', payload)

        # Ne doit pas crasher, doit avoir fallback 'N'
        assert "Maison N" in prompt or "maison" in prompt.lower()

    def test_v4_prompt_contraintes_strictes(self):
        """v4 prompt contient les contraintes de longueur et style"""
        payload = ChartPayload(
            subject_label="Mars",
            sign="Scorpion",
            house=8,
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('mars', payload)

        # Vérifier contraintes v4
        assert "800-1100 chars" in prompt or "800-1300" in prompt
        assert "INTERDIT" in prompt
        assert "tu es" in prompt.lower()  # Mentionné comme interdit
        assert "Professionnel analytique" in prompt or "professionnel" in prompt.lower()

    def test_v4_prompt_rejects_missing_sign(self):
        """v4 prompt rejette payload sans signe"""
        payload = ChartPayload(
            subject_label="Vénus",
            sign="",  # Signe vide
            house=7,
            ascendant_sign="Bélier"
        )

        with pytest.raises(ValueError, match="Signe manquant"):
            build_interpretation_prompt_v4_senior('venus', payload)


class TestV4LengthValidation:
    """Tests de validation de longueur v4 (800-1300 chars)"""

    def test_v4_length_valid_min_boundary(self):
        """v4 accepte 800 chars minimum"""
        text = "x" * 800
        is_valid, length = validate_interpretation_length(text, version=4)
        assert is_valid is True
        assert length == 800

    def test_v4_length_valid_max_boundary(self):
        """v4 accepte 1300 chars maximum"""
        text = "x" * 1300
        is_valid, length = validate_interpretation_length(text, version=4)
        assert is_valid is True
        assert length == 1300

    def test_v4_length_too_short(self):
        """v4 rejette < 800 chars"""
        text = "x" * 799
        is_valid, length = validate_interpretation_length(text, version=4)
        assert is_valid is False
        assert length == 799

    def test_v4_length_too_long(self):
        """v4 rejette > 1300 chars"""
        text = "x" * 1301
        is_valid, length = validate_interpretation_length(text, version=4)
        assert is_valid is False
        assert length == 1301

    def test_v4_length_optimal_target(self):
        """v4 accepte longueur optimale 900-1100 chars"""
        for length in [900, 1000, 1100]:
            text = "x" * length
            is_valid, actual_length = validate_interpretation_length(text, version=4)
            assert is_valid is True
            assert actual_length == length


class TestV4Integration:
    """Tests d'intégration v4 (structure complète)"""

    def test_v4_prompt_sun_complete_example(self):
        """v4 génère un prompt complet cohérent pour le Soleil"""
        payload = ChartPayload(
            subject_label="Soleil",
            sign="Lion",
            house=10,
            ascendant_sign="Scorpion",
            aspects=[
                {"planet1": "sun", "planet2": "jupiter", "type": "trine", "orb": 4.0}
            ]
        )
        prompt = build_interpretation_prompt_v4_senior('sun', payload)

        # Vérifications de cohérence
        assert "Soleil" in prompt
        assert "Lion" in prompt
        assert "Maison 10" in prompt
        assert "Scorpion" in prompt  # Ascendant
        assert "identité centrale" in prompt or "volonté" in prompt  # Fonction Soleil
        assert "jupiter" in prompt.lower() or "Jupiter" in prompt  # Aspect trigone

        # Structure markdown
        assert prompt.startswith("Tu es un astrologue senior professionnel")
        assert "# ☀️ Soleil en Lion" in prompt or "# 🌟 Soleil en Lion" in prompt

    def test_v4_prompt_north_node_complete_example(self):
        """v4 génère un prompt complet pour Nœud Nord avec axe"""
        payload = ChartPayload(
            subject_label="Nœud Nord",
            sign="Capricorne",
            house=10,
            ascendant_sign="Bélier"
        )
        prompt = build_interpretation_prompt_v4_senior('north_node', payload)

        # Vérifications axe NN/NS
        assert "Nœud Nord en Capricorne" in prompt
        assert "Nœud Sud en Cancer" in prompt  # Opposé
        assert "Maison 10" in prompt  # Maison NN
        assert "Maison 4" in prompt  # Maison opposée (NS)
        assert "chemin de vie" in prompt.lower()
        assert "acquis" in prompt.lower() or "confort" in prompt.lower()

        # Structure spéciale NN
        assert "## 1. L'axe des Nœuds Lunaires" in prompt
        assert "## 6. Vigilance" in prompt  # 6 sections pour NN/NS

    def test_v4_uses_same_aspect_filter_as_v3(self):
        """v4 réutilise le filtre d'aspects v3 (majeurs, orb ≤6°)"""
        from services.natal_interpretation_service import find_relevant_aspect_v3

        # Aspect majeur orb ≤6° doit être retenu
        payload_valid = ChartPayload(
            subject_label="Mercure",
            sign="Gémeaux",
            house=3,
            aspects=[
                {"planet1": "mercury", "planet2": "uranus", "type": "opposition", "orb": 5.5}
            ]
        )
        aspect = find_relevant_aspect_v3('mercury', payload_valid)
        assert aspect is not None
        assert "opposition" in aspect.lower()

        # Sextile (aspect mineur) doit être ignoré
        payload_invalid = ChartPayload(
            subject_label="Vénus",
            sign="Balance",
            house=7,
            aspects=[
                {"planet1": "venus", "planet2": "mars", "type": "sextile", "orb": 2.0}
            ]
        )
        aspect = find_relevant_aspect_v3('venus', payload_invalid)
        assert aspect is None  # Sextile ignoré même avec orb faible
