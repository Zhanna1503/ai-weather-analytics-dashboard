from datetime import datetime, timezone
from src.ai_summary import summarize_forecast
import requests
import pandas as pd
from src.config import CITIES


def get_tomorrow_forecast(latitude: float, longitude: float) -> dict:
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
        "forecast_days": 2
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError("Weather API took too long to respond (timeout).")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Weather API returned an error: {e}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to reach Weather API: {e}")

    return response.json()


def parse_tomorrow(raw_data: dict) -> dict:
    try:
        daily = raw_data["daily"]
        tomorrow_index = 1

        tomorrow = {
            "date": daily["time"][tomorrow_index],
            "temp_max": daily["temperature_2m_max"][tomorrow_index],
            "temp_min": daily["temperature_2m_min"][tomorrow_index],
            "precipitation_mm": daily["precipitation_sum"][tomorrow_index],
        }
    except (KeyError, IndexError) as e:
        raise ValueError(f"Unexpected API response format: {e}")

    return tomorrow


def fetch_all_cities(cities: dict) -> pd.DataFrame:
    rows = []
    fetched_at = datetime.now(timezone.utc).isoformat()

    for city_name, coords in cities.items():
        raw_data = get_tomorrow_forecast(coords["latitude"], coords["longitude"])
        tomorrow = parse_tomorrow(raw_data)
        tomorrow["city"] = city_name
        tomorrow["ai_summary"] = summarize_forecast(tomorrow)
        tomorrow["fetched_at"] = fetched_at
        rows.append(tomorrow)

    df = pd.DataFrame(rows)
    df["temp_max"] = df["temp_max"].round(1).astype(float)
    df["temp_min"] = df["temp_min"].round(1).astype(float)
    column_order = ["fetched_at", "city", "date", "temp_max", "temp_min", "precipitation_mm", "ai_summary"]
    return df[column_order]


if __name__ == "__main__":
    df = fetch_all_cities(CITIES)
    print(df)
    df.to_csv("data/tomorrow_forecast.csv", index=False, encoding="utf-8-sig")