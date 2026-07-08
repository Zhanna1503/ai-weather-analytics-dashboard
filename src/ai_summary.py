from anthropic import Anthropic
from src.config import ANTHROPIC_API_KEY

client = Anthropic(api_key=ANTHROPIC_API_KEY)


def summarize_forecast(city_row: dict) -> str:
    prompt = (
        f"You are a weather analyst. Given this forecast data for "
        f"{city_row['city']} on {city_row['date']}:\n"
        f"- Max temp: {city_row['temp_max']}°C\n"
        f"- Min temp: {city_row['temp_min']}°C\n"
        f"- Precipitation: {city_row['precipitation_mm']} mm\n\n"
        f"Write a 1-2 sentence plain-English summary a business "
        f"stakeholder would find useful. No markdown, no bullet points."
    )

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=150,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


if __name__ == "__main__":
    sample_row = {
        "city": "berlin",
        "date": "2026-07-09",
        "temp_max": 23.9,
        "temp_min": 12.3,
        "precipitation_mm": 0.0,
    }

    summary = summarize_forecast(sample_row)
    print(summary)