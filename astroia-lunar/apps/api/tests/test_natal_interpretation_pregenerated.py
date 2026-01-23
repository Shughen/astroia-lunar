"""
Tests pour les interprétations pré-générées (mode LLM off)
"""

import pytest
from services.natal_interpretation_service import (
    load_pregenerated_interpretation,
    generate_with_sonnet_fallback_haiku,
    SIGN_FR_TO_EN
)
from schemas.natal_interpretation import ChartPayload


def test_sign_mapping_fr_to_en():
    """Test du mapping des signes français vers anglais"""
    assert SIGN_FR_TO_EN['verseau'] == 'aquarius'
    assert SIGN_FR_TO_EN['taureau'] == 'taurus'
    assert SIGN_FR_TO_EN['gémeaux'] == 'gemini'
    assert SIGN_FR_TO_EN['gemeaux'] == 'gemini'  # Variante sans accent
    assert SIGN_FR_TO_EN['balance'] == 'libra'


def test_load_pregenerated_sun_aquarius_11():
    """Test chargement Soleil en Verseau Maison 11"""
    text = load_pregenerated_interpretation('sun', 'Verseau', 11, version=2)

    assert text is not None
    assert len(text) > 900
    assert '☀️ Soleil en Verseau' in text
    assert 'Ton moteur' in text
    assert 'Ton défi' in text
    assert 'Maison 11' in text
    assert 'Micro-rituel' in text


def test_load_pregenerated_moon_taurus_2():
    """Test chargement Lune en Taureau Maison 2"""
    text = load_pregenerated_interpretation('moon', 'Taureau', 2, version=2)

    assert text is not None
    assert len(text) > 900
    assert '🌙 Lune en Taureau' in text
    assert 'Ton moteur' in text


def test_load_pregenerated_mercury_gemini_3():
    """Test chargement Mercure en Gémeaux Maison 3"""
    text = load_pregenerated_interpretation('mercury', 'Gémeaux', 3, version=2)

    assert text is not None
    assert len(text) > 900
    assert '☿️ Mercure en Gémeaux' in text


def test_load_pregenerated_venus_libra_7():
    """Test chargement Vénus en Balance Maison 7"""
    text = load_pregenerated_interpretation('venus', 'Balance', 7, version=2)

    assert text is not None
    assert len(text) > 900
    assert '♀️ Vénus en Balance' in text


def test_load_pregenerated_mars_aries_1():
    """Test chargement Mars en Bélier Maison 1"""
    text = load_pregenerated_interpretation('mars', 'Bélier', 1, version=2)

    assert text is not None
    assert len(text) > 900
    assert '♂️ Mars en Bélier' in text


def test_load_pregenerated_jupiter_sagittarius_9():
    """Test chargement Jupiter en Sagittaire Maison 9"""
    text = load_pregenerated_interpretation('jupiter', 'Sagittaire', 9, version=2)

    assert text is not None
    assert len(text) > 900
    assert '♃ Jupiter en Sagittaire' in text


def test_load_pregenerated_saturn_capricorn_10():
    """Test chargement Saturne en Capricorne Maison 10"""
    text = load_pregenerated_interpretation('saturn', 'Capricorne', 10, version=2)

    assert text is not None
    assert len(text) > 900
    assert '♄ Saturne en Capricorne' in text


def test_load_pregenerated_north_node_aquarius_11():
    """Test chargement Nœud Nord en Verseau Maison 11"""
    text = load_pregenerated_interpretation('north_node', 'Verseau', 11, version=2)

    assert text is not None
    assert len(text) > 900
    assert '☊ Nœud Nord en Verseau' in text


def test_load_pregenerated_not_found():
    """Test fichier inexistant retourne None"""
    text = load_pregenerated_interpretation('pluto', 'Scorpion', 8, version=2)

    assert text is None


def test_load_pregenerated_case_insensitive():
    """Test que le chargement est insensible à la casse"""
    text1 = load_pregenerated_interpretation('sun', 'Verseau', 11, version=2)
    text2 = load_pregenerated_interpretation('sun', 'verseau', 11, version=2)
    text3 = load_pregenerated_interpretation('sun', 'VERSEAU', 11, version=2)

    assert text1 is not None
    assert text1 == text2 == text3


@pytest.mark.asyncio
async def test_generate_with_fallback_mode_off():
    """Test que generate_with_sonnet_fallback_haiku utilise les pré-générées en mode off"""
    from unittest.mock import patch

    # Créer un ChartPayload de test
    chart_payload = ChartPayload(
        subject_label="Soleil",
        sign="Verseau",
        house=11,
        degree=15.5,
        longitude=15.5,
        latitude=48.0,
        ascendant_sign="Bélier",
        aspects=[]
    )

    # Forcer NATAL_LLM_MODE à 'off' pour ce test
    with patch('config.settings.NATAL_LLM_MODE', 'off'):
        # Appeler la fonction (mode off forcé)
        text, model_used = await generate_with_sonnet_fallback_haiku(
            subject='sun',
            chart_payload=chart_payload,
            version=2
        )

        # Vérifier que l'interprétation pré-générée a été chargée
        assert model_used == 'pregenerated'
        assert text is not None
        assert len(text) > 900
        assert '☀️ Soleil en Verseau' in text
        assert 'Ton moteur' in text


@pytest.mark.asyncio
async def test_generate_with_fallback_mode_off_not_found():
    """Test fallback vers placeholder si fichier inexistant"""
    from unittest.mock import patch

    # Créer un ChartPayload pour un fichier qui n'existe pas
    chart_payload = ChartPayload(
        subject_label="Pluton",
        sign="Scorpion",
        house=8,
        degree=20.0,
        longitude=20.0,
        latitude=48.0,
        ascendant_sign="Bélier",
        aspects=[]
    )

    # Forcer NATAL_LLM_MODE à 'off' pour ce test
    with patch('config.settings.NATAL_LLM_MODE', 'off'):
        # Appeler la fonction (mode off forcé)
        text, model_used = await generate_with_sonnet_fallback_haiku(
            subject='pluto',
            chart_payload=chart_payload,
            version=2
        )

        # Vérifier que le placeholder a été utilisé
        assert model_used == 'placeholder'
        assert text is not None
        assert 'Interprétation non disponible' in text


def test_interpretation_quality():
    """Test de qualité des interprétations (longueur, structure)"""
    # Charger plusieurs interprétations et vérifier leur qualité
    test_cases = [
        ('sun', 'Verseau', 11),
        ('moon', 'Taureau', 2),
        ('mercury', 'Gémeaux', 3),
        ('venus', 'Balance', 7),
        ('mars', 'Bélier', 1),
    ]

    for subject, sign, house in test_cases:
        text = load_pregenerated_interpretation(subject, sign, house, version=2)

        # Vérifier la longueur (900-1400 chars)
        assert 900 <= len(text) <= 1400, f"{subject} en {sign} M{house}: {len(text)} chars (attendu 900-1400)"

        # Vérifier structure
        assert '**En une phrase :**' in text
        assert '## Ton moteur' in text
        assert '## Ton défi' in text
        assert '## Micro-rituel' in text

        # Vérifier qu'il n'y a pas de frontmatter YAML
        assert not text.startswith('---')

        # Vérifier qu'il y a bien un titre principal
        assert text.startswith('#')
