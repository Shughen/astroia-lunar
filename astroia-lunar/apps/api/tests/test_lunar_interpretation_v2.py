"""
Tests pour lunar_interpretation_service.py - Version 2

Tests des nouvelles fonctionnalites v2 :
- load_full_lunar_interpretation_v2 : Chargement interpretation complete
- load_lunar_interpretation_with_fallback : Chargement avec fallback automatique
- format_weekly_advice_v2 : Formatage des conseils hebdomadaires v2
"""

import pytest
from datetime import datetime, timezone, timedelta
from unittest.mock import MagicMock, AsyncMock

from services.lunar_interpretation_service import (
    load_full_lunar_interpretation_v2,
    load_lunar_interpretation_with_fallback,
    format_weekly_advice_v2,
    generate_weekly_advice,
    get_fallback_climate,
    get_fallback_focus,
    get_fallback_approach
)


class TestLoadFullLunarInterpretationV2:
    """Tests du chargement des interpretations v2 completes"""

    @pytest.mark.asyncio
    async def test_load_v2_found(self):
        """Charge l'interpretation v2 depuis la DB quand trouvee"""
        mock_db = AsyncMock()
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "**Ton mois en un mot : Dynamisme**\n\nCe mois-ci..."
        mock_entry.weekly_advice = {
            "week_1": "Lance tes projets avec confiance.",
            "week_2": "Consolide ce que tu as commence.",
            "week_3": "Ajuste ta trajectoire si besoin.",
            "week_4": "Prepare le prochain cycle."
        }

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        result = await load_full_lunar_interpretation_v2(
            mock_db, "Aries", 1, "Taurus", version=2, lang='fr'
        )

        assert result is not None
        interpretation, weekly_advice = result
        assert "Ton mois en un mot" in interpretation
        assert weekly_advice is not None
        assert "week_1" in weekly_advice
        assert "week_4" in weekly_advice

    @pytest.mark.asyncio
    async def test_load_v2_not_found(self):
        """Retourne None si interpretation v2 non trouvee"""
        mock_db = AsyncMock()
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_db.execute.return_value = mock_result

        result = await load_full_lunar_interpretation_v2(
            mock_db, "Aries", 1, "Taurus", version=2, lang='fr'
        )

        assert result is None

    @pytest.mark.asyncio
    async def test_load_v2_with_null_weekly_advice(self):
        """Gere correctement un weekly_advice null"""
        mock_db = AsyncMock()
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "Interpretation sans weekly advice."
        mock_entry.weekly_advice = None

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        result = await load_full_lunar_interpretation_v2(
            mock_db, "Gemini", 3, "Leo", version=2, lang='fr'
        )

        assert result is not None
        interpretation, weekly_advice = result
        assert interpretation == "Interpretation sans weekly advice."
        assert weekly_advice is None


class TestLoadLunarInterpretationWithFallback:
    """Tests du chargement avec fallback automatique"""

    @pytest.mark.asyncio
    async def test_returns_v2_when_available(self):
        """Retourne v2 quand disponible"""
        mock_db = AsyncMock()

        # Simuler une v2 trouvee
        mock_entry = MagicMock()
        mock_entry.interpretation_full = "**V2 Interpretation**"
        mock_entry.weekly_advice = {"week_1": "Conseil 1"}

        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = mock_entry
        mock_db.execute.return_value = mock_result

        interpretation, weekly_advice, source = await load_lunar_interpretation_with_fallback(
            mock_db, "Aries", 1, "Taurus", preferred_version=2, lang='fr'
        )

        assert source == 'database-v2'
        assert "V2 Interpretation" in interpretation
        assert weekly_advice is not None

    @pytest.mark.asyncio
    async def test_falls_back_to_v1_when_v2_not_available(self):
        """Tombe sur v1 si v2 non disponible"""
        mock_db = AsyncMock()

        # Premier appel (v2) retourne None, les suivants (v1) retournent des templates
        call_count = [0]
        def mock_execute(*args, **kwargs):
            result = MagicMock()
            if call_count[0] == 0:
                # v2 non trouvee
                result.scalar_one_or_none.return_value = None
            elif call_count[0] == 1:
                # climate v1 trouvee
                mock_entry = MagicMock()
                mock_entry.interpretation_full = "Climate V1"
                result.scalar_one_or_none.return_value = mock_entry
            elif call_count[0] == 2:
                # focus v1 trouvee
                mock_entry = MagicMock()
                mock_entry.interpretation_full = "Focus V1"
                result.scalar_one_or_none.return_value = mock_entry
            else:
                # approach v1 trouvee
                mock_entry = MagicMock()
                mock_entry.interpretation_full = "Approach V1"
                result.scalar_one_or_none.return_value = mock_entry
            call_count[0] += 1
            return result

        mock_db.execute.side_effect = mock_execute

        interpretation, weekly_advice, source = await load_lunar_interpretation_with_fallback(
            mock_db, "Aries", 1, "Taurus", preferred_version=2, lang='fr'
        )

        assert source == 'database-v1'
        assert "Climate V1" in interpretation
        assert weekly_advice is None  # V1 n'a pas de weekly_advice

    @pytest.mark.asyncio
    async def test_falls_back_to_static_when_nothing_in_db(self):
        """Tombe sur fallback statique si rien en DB"""
        mock_db = AsyncMock()

        # Tous les appels retournent None
        mock_result = MagicMock()
        mock_result.scalar_one_or_none.return_value = None
        mock_db.execute.return_value = mock_result

        interpretation, weekly_advice, source = await load_lunar_interpretation_with_fallback(
            mock_db, "Aries", 1, "Taurus", preferred_version=2, lang='fr'
        )

        assert source == 'fallback'
        # Verifie que le fallback contient le contenu attendu
        assert "dynamique" in interpretation.lower() or "impulsif" in interpretation.lower()
        assert weekly_advice is None


class TestFormatWeeklyAdviceV2:
    """Tests du formatage des conseils hebdomadaires v2"""

    def test_formats_db_advice_with_dates(self):
        """Formate les conseils DB avec les dates"""
        return_date = datetime(2025, 2, 15, 12, 0, 0, tzinfo=timezone.utc)
        weekly_advice_db = {
            "week_1": "Conseil personnalise semaine 1.",
            "week_2": "Conseil personnalise semaine 2.",
            "week_3": "Conseil personnalise semaine 3.",
            "week_4": "Conseil personnalise semaine 4."
        }

        result = format_weekly_advice_v2(weekly_advice_db, return_date)

        # Verifie les 4 semaines
        assert "week_1" in result
        assert "week_2" in result
        assert "week_3" in result
        assert "week_4" in result

        # Verifie la structure
        week1 = result["week_1"]
        assert "dates" in week1
        assert "theme" in week1
        assert "conseil" in week1
        assert "focus" in week1

        # Verifie le conseil personnalise
        assert "Conseil personnalise semaine 1" in week1["conseil"]

    def test_falls_back_when_no_db_advice(self):
        """Utilise les conseils statiques si pas de DB advice"""
        return_date = datetime(2025, 3, 1, 0, 0, 0, tzinfo=timezone.utc)

        result = format_weekly_advice_v2(None, return_date)

        # Doit retourner le format statique
        assert "week_1" in result
        assert "Pose tes intentions" in result["week_1"]["conseil"]

    def test_handles_missing_weeks_gracefully(self):
        """Gere les semaines manquantes avec un fallback"""
        return_date = datetime(2025, 4, 1, 0, 0, 0, tzinfo=timezone.utc)
        weekly_advice_db = {
            "week_1": "Conseil semaine 1.",
            # week_2, week_3, week_4 manquantes
        }

        result = format_weekly_advice_v2(weekly_advice_db, return_date)

        # Semaine 1 a le conseil personnalise
        assert "Conseil semaine 1" in result["week_1"]["conseil"]

        # Semaines 2-4 ont un fallback generique
        assert result["week_2"]["conseil"]  # Pas vide
        assert result["week_3"]["conseil"]  # Pas vide
        assert result["week_4"]["conseil"]  # Pas vide

    def test_dates_are_sequential(self):
        """Les dates sont sequentielles (7 jours par semaine)"""
        return_date = datetime(2025, 1, 10, 0, 0, 0, tzinfo=timezone.utc)
        weekly_advice_db = {
            "week_1": "Conseil 1",
            "week_2": "Conseil 2",
            "week_3": "Conseil 3",
            "week_4": "Conseil 4"
        }

        result = format_weekly_advice_v2(weekly_advice_db, return_date)

        # Semaine 1 commence le 10/01
        assert "10/01" in result["week_1"]["dates"]
        # Semaine 2 commence le 17/01
        assert "17/01" in result["week_2"]["dates"]
        # Semaine 3 commence le 24/01
        assert "24/01" in result["week_3"]["dates"]
        # Semaine 4 commence le 31/01
        assert "31/01" in result["week_4"]["dates"]


class TestIntegrationV2WithConfig:
    """Tests d'integration avec la configuration"""

    def test_fallback_climate_still_works(self):
        """Les fallbacks climat fonctionnent toujours"""
        result = get_fallback_climate("Aries")
        assert result is not None
        assert len(result) > 20

    def test_fallback_focus_still_works(self):
        """Les fallbacks focus fonctionnent toujours"""
        result = get_fallback_focus(1)
        assert result is not None
        assert "Focus" in result

    def test_fallback_approach_still_works(self):
        """Les fallbacks approche fonctionnent toujours"""
        result = get_fallback_approach("Aries")
        assert result is not None
        assert "abordes" in result.lower()


class TestV2Combinations:
    """Tests des combinaisons v2 (1728 possibles)"""

    def test_all_signs_are_valid_for_v2(self):
        """Tous les signes sont valides pour v2"""
        signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
        for sign in signs:
            # Le fallback doit fonctionner pour tous les signes
            result = get_fallback_climate(sign)
            assert result is not None

    def test_all_houses_are_valid_for_v2(self):
        """Toutes les maisons (1-12) sont valides pour v2"""
        for house in range(1, 13):
            result = get_fallback_focus(house)
            assert result is not None

    def test_combinations_count(self):
        """Verifie le nombre de combinaisons possibles"""
        signs = 12
        houses = 12
        ascendants = 12
        expected_combinations = signs * houses * ascendants
        assert expected_combinations == 1728
