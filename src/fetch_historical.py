import requests
import pandas as pd
from datetime import date, timedelta
from src.config import CITIES


def get_historical_weather(latitude: float, longitude: float, start_date: str, end_date: str) -> dict:
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "auto",
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise RuntimeError("Historical Weather API took too long to respond (timeout).")
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Historical Weather API returned an error: {e}")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to reach Historical Weather API: {e}")

    return response.json()


def parse_historical(raw_data: dict, city_name: str) -> pd.DataFrame:
    try:
        daily = raw_data["daily"]
        df = pd.DataFrame({
            "date": daily["time"],
            "temp_max": daily["temperature_2m_max"],
            "temp_min": daily["temperature_2m_min"],
            "precipitation_mm": daily["precipitation_sum"],
        })
    except KeyError as e:
        raise ValueError(f"Unexpected API response format: {e}")

    df["temp_max"] = df["temp_max"].round(1).astype(float)
    df["temp_min"] = df["temp_min"].round(1).astype(float)
    df["city"] = city_name
    return df


if __name__ == "__main__":
    end = date.today() - timedelta(days=5)
    start = end - timedelta(days=30)

    all_data = []

    for city_name, coords in CITIES.items():
        raw = get_historical_weather(
            coords["latitude"], coords["longitude"],
            start.isoformat(), end.isoformat()
        )
        city_df = parse_historical(raw, city_name)
        all_data.append(city_df)

    result = pd.concat(all_data, ignore_index=True)
    result.to_csv("data/historical_weather.csv", index=False, encoding="utf-8-sig")
    print(result)