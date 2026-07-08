from src.fetch_data import parse_tomorrow


def test_parse_tomorrow_extracts_correct_fields():
    fake_api_response = {
        "daily": {
            "time": ["2026-07-08", "2026-07-09"],
            "temperature_2m_max": [22.5, 23.9],
            "temperature_2m_min": [11.9, 12.3],
            "precipitation_sum": [0.0, 1.2],
        }
    }

    result = parse_tomorrow(fake_api_response)

    assert result["date"] == "2026-07-09"
    assert result["temp_max"] == 23.9
    assert result["temp_min"] == 12.3
    assert result["precipitation_mm"] == 1.2