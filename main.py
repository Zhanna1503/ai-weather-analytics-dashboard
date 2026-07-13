from datetime import date, timedelta
import pandas as pd

from src.config import CITIES
from src.fetch_data import fetch_all_cities
from src.fetch_historical import (
    get_historical_weather,
    parse_historical,
)


def fetch_historical_for_all_cities():
    end = date.today() - timedelta(days=5)
    start = end - timedelta(days=30)

    all_data = []

    for city_name, coords in CITIES.items():
        raw = get_historical_weather(
            coords["latitude"],
            coords["longitude"],
            start.isoformat(),
            end.isoformat(),
        )

        city_df = parse_historical(raw, city_name)
        all_data.append(city_df)

    result = pd.concat(all_data, ignore_index=True)

    result.to_csv(
        "data/historical_weather.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("Historical weather saved.")

    return result


def main():
    print("Fetching tomorrow's forecast...")

    forecast = fetch_all_cities(CITIES)

    forecast.to_csv(
        "data/tomorrow_forecast.csv",
        index=False,
        encoding="utf-8-sig",
    )

    print("Tomorrow forecast saved.")

    print("Fetching historical weather...")

    fetch_historical_for_all_cities()

    print("Done.")


if __name__ == "__main__":
    main()