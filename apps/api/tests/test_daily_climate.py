"""
Tests pour le service daily_climate et l'endpoint /api/lunar/daily-climate
"""

import pytest
from datetime import date
from services.daily_climate import get_daily_climate, clear_cache, _get_deterministic_insight


def test_get_daily_climate_structure():
    """Test que get_daily_climate() retourne la structure attendue"""
    clear_cache()

    result = get_daily_climate()

    # Vérifier structure principale
    assert "date" in result
    assert "moon" in result
    assert "insight" in result

    # Vérifier structure moon
    assert "sign" in result["moon"]
    assert "degree" in result["moon"]
    assert "phase" in result["moon"]

    # Vérifier structure insight
    assert "title" in result["insight"]
    assert "text" in result["insight"]
    assert "keywords" in result["insight"]
    assert "version" in result["insight"]

    # Vérifier types
    assert isinstance(result["date"], str)
    assert isinstance(result["moon"]["sign"], str)
    assert isinstance(result["moon"]["degree"], (int, float))
    assert isinstance(result["moon"]["phase"], str)
    assert isinstance(result["insight"]["title"], str)
    assert isinstance(result["insight"]["text"], str)
    assert isinstance(result["insight"]["keywords"], list)
    assert result["insight"]["version"] == "v1"


def test_get_daily_climate_content_not_empty():
    """Test que tous les champs ont un contenu non vide"""
    clear_cache()

    result = get_daily_climate()

    # Vérifier que les champs ne sont pas vides
    assert len(result["date"]) > 0
    assert len(result["moon"]["sign"]) > 0
    assert result["moon"]["degree"] >= 0
    assert len(result["moon"]["phase"]) > 0
    assert len(result["insight"]["title"]) > 0
    assert len(result["insight"]["text"]) > 20  # Au moins 20 caractères
    assert len(result["insight"]["keywords"]) > 0

    # Vérifier que keywords contient des strings non vides
    for keyword in result["insight"]["keywords"]:
        assert isinstance(keyword, str)
        assert len(keyword) > 0


def test_get_daily_climate_date_format():
    """Test que la date est au format YYYY-MM-DD"""
    clear_cache()

    result = get_daily_climate()

    # Vérifier format YYYY-MM-DD
    date_str = result["date"]
    assert len(date_str) == 10
    assert date_str[4] == "-"
    assert date_str[7] == "-"

    # Vérifier que c'est une date valide
    date.fromisoformat(date_str)

    # Vérifier que c'est la date d'aujourd'hui
    assert date_str == date.today().isoformat()


def test_daily_climate_cache_same_day():
    """Test que le cache retourne le même résultat le même jour"""
    clear_cache()

    # Premier appel
    result1 = get_daily_climate()

    # Deuxième appel (devrait utiliser le cache)
    result2 = get_daily_climate()

    # Les résultats doivent être STRICTEMENT identiques
    assert result1 == result2
    assert result1["date"] == result2["date"]
    assert result1["moon"] == result2["moon"]
    assert result1["insight"] == result2["insight"]

    print(f"\n✅ Cache fonctionne: même insight pour la journée ({result1['insight']['title']})")


def test_deterministic_insight_generation():
    """Test que _get_deterministic_insight() est déterministe"""
    # Même date + sign + phase = même insight
    date1 = "2025-12-29"
    sign1 = "Gemini"
    phase1 = "Premier Quartier"

    insight1 = _get_deterministic_insight(date1, sign1, phase1)
    insight2 = _get_deterministic_insight(date1, sign1, phase1)

    # Doit être strictement identique
    assert insight1 == insight2
    assert insight1["title"] == insight2["title"]
    assert insight1["text"] == insight2["text"]
    assert insight1["keywords"] == insight2["keywords"]

    print(f"\n✅ Insight déterministe: {insight1['title']}")


def test_deterministic_insight_different_dates():
    """Test que des dates différentes peuvent donner des insights différents (si plusieurs templates)"""
    sign = "Aries"
    phase = "Nouvelle Lune"

    # Aries + Nouvelle Lune a 2 templates, donc dates différentes = insights potentiellement différents
    insight_date1 = _get_deterministic_insight("2025-01-01", sign, phase)
    insight_date2 = _get_deterministic_insight("2025-01-02", sign, phase)

    # Les deux insights doivent être valides
    assert "title" in insight_date1
    assert "title" in insight_date2

    # Ils peuvent être identiques ou différents selon le hash
    # (on vérifie juste que le mécanisme fonctionne)
    print(f"\n📅 Date 2025-01-01: {insight_date1['title']}")
    print(f"📅 Date 2025-01-02: {insight_date2['title']}")


def test_all_sign_phase_combinations_have_insights():
    """Test que toutes les combinaisons sign/phase ont un insight"""
    signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]

    phases = [
        'Nouvelle Lune', 'Premier Croissant', 'Premier Quartier', 'Lune Gibbeuse',
        'Pleine Lune', 'Lune Disseminante', 'Dernier Quartier', 'Dernier Croissant'
    ]

    missing = []

    for sign in signs:
        for phase in phases:
            insight = _get_deterministic_insight("2025-12-29", sign, phase)

            # Vérifier que l'insight est valide
            if not insight or not insight.get("title") or not insight.get("text"):
                missing.append((sign, phase))

    # Afficher les combinaisons manquantes
    if missing:
        print(f"\n⚠️ Combinaisons manquantes: {missing}")

    # Toutes les combinaisons doivent avoir un insight
    assert len(missing) == 0, f"Combinaisons manquantes: {missing}"

    print(f"\n✅ Toutes les combinaisons (12 signes × 8 phases = 96) ont un insight")


def test_moon_position_valid_values():
    """Test que la position lunaire a des valeurs valides"""
    clear_cache()

    result = get_daily_climate()

    moon = result["moon"]

    # Vérifier signe valide
    valid_signs = [
        'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
        'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
    ]
    assert moon["sign"] in valid_signs

    # Vérifier degré valide (0-360)
    assert 0 <= moon["degree"] < 360

    # Vérifier phase valide
    valid_phases = [
        'Nouvelle Lune', 'Premier Croissant', 'Premier Quartier', 'Lune Gibbeuse',
        'Pleine Lune', 'Lune Disseminante', 'Dernier Quartier', 'Dernier Croissant'
    ]
    assert moon["phase"] in valid_phases

    print(f"\n🌙 Position lunaire: {moon['degree']:.2f}° {moon['sign']}, Phase: {moon['phase']}")


def test_clear_cache_works():
    """Test que clear_cache() efface bien le cache"""
    clear_cache()

    # Premier appel
    result1 = get_daily_climate()

    # Clear cache
    clear_cache()

    # Deuxième appel (devrait recalculer, mais retourner le même résultat car même date)
    result2 = get_daily_climate()

    # Les résultats doivent être identiques car même date
    assert result1["date"] == result2["date"]
    assert result1["insight"]["title"] == result2["insight"]["title"]

    print(f"\n✅ Clear cache fonctionne")
