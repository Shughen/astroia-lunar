"""
Tests for lunar normalization functions.

Tests ensure that various RapidAPI response formats are normalized correctly,
preventing "N/A" values from appearing in the mobile UI.
"""

import pytest
from services.lunar_normalization import (
    normalize_lunar_mansion_response,
    normalize_lunar_return_report_response,
    _extract_mansion_number,
    _extract_mansion_name
)


class TestExtractMansionNumber:
    """Tests for _extract_mansion_number helper"""

    def test_extract_number_field(self):
        """Should extract 'number' field"""
        mansion = {"number": 14}
        assert _extract_mansion_number(mansion) == 14

    def test_extract_id_field(self):
        """Should fallback to 'id' if 'number' absent"""
        mansion = {"id": 7}
        assert _extract_mansion_number(mansion) == 7

    def test_extract_mansion_number_field(self):
        """Should fallback to 'mansion_number'"""
        mansion = {"mansion_number": 21}
        assert _extract_mansion_number(mansion) == 21

    def test_extract_string_number(self):
        """Should convert string to int"""
        mansion = {"number": "14"}
        assert _extract_mansion_number(mansion) == 14

    def test_missing_number(self):
        """Should return None if no number found"""
        mansion = {"name": "Al-Simak"}
        assert _extract_mansion_number(mansion) is None

    def test_invalid_number(self):
        """Should return None if number cannot be converted"""
        mansion = {"number": "invalid"}
        assert _extract_mansion_number(mansion) is None


class TestExtractMansionName:
    """Tests for _extract_mansion_name helper"""

    def test_extract_name_field(self):
        """Should extract 'name' field"""
        mansion = {"name": "Al-Simak"}
        assert _extract_mansion_name(mansion) == "Al-Simak"

    def test_extract_title_field(self):
        """Should fallback to 'title' if 'name' absent"""
        mansion = {"title": "Al-Ghafr"}
        assert _extract_mansion_name(mansion) == "Al-Ghafr"

    def test_extract_mansion_name_field(self):
        """Should fallback to 'mansion_name'"""
        mansion = {"mansion_name": "Az-Zubana"}
        assert _extract_mansion_name(mansion) == "Az-Zubana"

    def test_missing_name(self):
        """Should return None if no name found"""
        mansion = {"number": 14}
        assert _extract_mansion_name(mansion) is None

    def test_non_string_name(self):
        """Should return None if name is not a string"""
        mansion = {"name": 123}
        assert _extract_mansion_name(mansion) is None


class TestNormalizeLunarMansion:
    """Tests for normalize_lunar_mansion_response"""

    def test_standard_response(self):
        """Should normalize standard RapidAPI response"""
        raw = {
            "mansion": {
                "number": 14,
                "name": "Al-Simak",
                "interpretation": "Favorable aux nouveaux projets"
            },
            "upcoming_changes": []
        }

        result = normalize_lunar_mansion_response(raw)

        assert result["mansion"]["number"] == 14
        assert result["mansion"]["name"] == "Al-Simak"
        assert result["mansion"]["interpretation"] == "Favorable aux nouveaux projets"
        assert "upcoming_changes" in result

    def test_alternative_field_names(self):
        """Should handle alternative field names (id, title)"""
        raw = {
            "mansion": {
                "id": 7,
                "title": "Al-Dhira",
                "description": "Test description"
            }
        }

        result = normalize_lunar_mansion_response(raw)

        assert result["mansion"]["number"] == 7
        assert result["mansion"]["name"] == "Al-Dhira"
        assert result["mansion"]["interpretation"] == "Test description"

    def test_missing_mansion_field(self):
        """Should handle missing 'mansion' field gracefully"""
        raw = {"upcoming_changes": []}

        result = normalize_lunar_mansion_response(raw)

        assert result["mansion"]["number"] is None
        assert result["mansion"]["name"] is None
        assert result["mansion"]["interpretation"] is None

    def test_null_values_not_na_string(self):
        """Should return None, not 'N/A' string"""
        raw = {"mansion": {}}

        result = normalize_lunar_mansion_response(raw)

        # Critical: must be None, NOT "N/A"
        assert result["mansion"]["number"] is None
        assert result["mansion"]["name"] is None
        assert result["mansion"]["interpretation"] is None

    def test_preserves_additional_fields(self):
        """Should preserve upcoming_changes and calendar_summary"""
        raw = {
            "mansion": {"number": 1, "name": "Al-Sharatain"},
            "upcoming_changes": [{"change_time": "2026-01-01T12:00:00"}],
            "calendar_summary": {"total": 28}
        }

        result = normalize_lunar_mansion_response(raw)

        assert "upcoming_changes" in result
        assert "calendar_summary" in result
        assert result["calendar_summary"]["total"] == 28


class TestNormalizeLunarReturnReport:
    """Tests for normalize_lunar_return_report_response"""

    def test_standard_response(self):
        """Should normalize standard RapidAPI response"""
        raw = {
            "return_date": "2026-01-15T10:30:00",
            "moon": {"sign": "Taurus", "house": 2},
            "interpretation": "Mois favorable aux finances"
        }

        result = normalize_lunar_return_report_response(raw, request_month="2026-01")

        assert result["month"] == "2026-01"
        assert result["return_date"] == "2026-01-15T10:30:00"
        assert result["moon_sign"] == "Taurus"
        assert result["moon_house"] == 2
        assert result["summary"] == "Mois favorable aux finances"

    def test_moon_as_string(self):
        """Should handle moon as a simple string (not dict)"""
        raw = {
            "moon": "Gemini",
            "interpretation": "Communication favored"
        }

        result = normalize_lunar_return_report_response(raw)

        assert result["moon_sign"] == "Gemini"
        assert result["moon_house"] is None

    def test_alternative_field_names(self):
        """Should handle alternative field names"""
        raw = {
            "lunar_return": {"date": "2026-02-10T08:00:00"},
            "moon": {"zodiac_sign": "Cancer"},
            "summary": "Emotional month"
        }

        result = normalize_lunar_return_report_response(raw)

        assert result["return_date"] == "2026-02-10T08:00:00"
        assert result["moon_sign"] == "Cancer"
        assert result["summary"] == "Emotional month"

    def test_missing_fields(self):
        """Should handle missing fields gracefully with null"""
        raw = {}

        result = normalize_lunar_return_report_response(raw, request_month="2026-03")

        assert result["month"] == "2026-03"
        assert result["return_date"] is None
        assert result["moon_sign"] is None
        assert result["moon_house"] is None
        assert result["lunar_ascendant"] is None
        assert result["summary"] is None

    def test_null_values_not_na_string(self):
        """Should return None, not 'N/A' string"""
        raw = {"moon": {}}

        result = normalize_lunar_return_report_response(raw)

        # Critical: must be None, NOT "N/A"
        assert result["return_date"] is None
        assert result["moon_sign"] is None
        assert result["lunar_ascendant"] is None
        assert result["summary"] is None

    def test_preserves_additional_fields(self):
        """Should preserve aspects, houses, planets"""
        raw = {
            "moon": {"sign": "Leo"},
            "aspects": [{"planet1": "Moon", "planet2": "Sun"}],
            "houses": {"1": {"sign": "Aries"}},
            "planets": {"Sun": {"sign": "Virgo"}}
        }

        result = normalize_lunar_return_report_response(raw)

        assert "aspects" in result
        assert "houses" in result
        assert "planets" in result
        assert len(result["aspects"]) == 1


class TestNormalizationEdgeCases:
    """Tests for edge cases and malformed responses"""

    def test_mansion_with_non_dict_mansion_field(self):
        """Should handle mansion field that is not a dict"""
        raw = {"mansion": "invalid"}

        result = normalize_lunar_mansion_response(raw)

        assert result["mansion"]["number"] is None
        assert result["mansion"]["name"] is None

    def test_return_with_non_dict_moon_field(self):
        """Should handle non-dict moon gracefully"""
        raw = {"moon": 123}

        result = normalize_lunar_return_report_response(raw)

        assert result["moon_sign"] is None
        assert result["moon_house"] is None

    def test_empty_response(self):
        """Should handle completely empty response"""
        raw = {}

        mansion_result = normalize_lunar_mansion_response(raw)
        assert mansion_result["mansion"]["number"] is None

        return_result = normalize_lunar_return_report_response(raw)
        assert return_result["return_date"] is None
