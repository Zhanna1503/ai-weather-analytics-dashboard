# 🌦️ AI Weather Analytics Dashboard

An end-to-end analytics project that combines **Python**, **Claude AI**, and **Power BI** to turn weather data into business-friendly insights.

Instead of only displaying charts, this dashboard generates natural-language recommendations using a Large Language Model (Claude AI), making weather information easier to interpret.

---

## Dashboard Preview

![Dashboard](PowerBI/Dashboard%20screenshot.png)

---

## Project Architecture

```
Open-Meteo API
        │
        ▼
Python (requests + pandas)
        │
        ▼
Claude AI (Anthropic API)
        │
        ▼
CSV Export
        │
        ▼
Power BI Dashboard
```

---

## Features

- 🌍 Fetches live weather forecasts for multiple European cities
- 📈 Downloads historical weather data
- 🤖 Generates AI-powered weather summaries using Claude AI
- 📊 Visualizes KPIs, trends and AI recommendations in Power BI
- 🔄 Automated data pipeline from API to dashboard

---

## Tech Stack

- Python
- Pandas
- Claude AI (Anthropic API)
- Open-Meteo API
- Power BI
- Requests

---

## Repository Structure

```
.
├── data/              # Generated datasets
├── PowerBI/           # Power BI dashboard (.pbix)
├── screenshots/       # Images used in the README
├── src/               # Source code
├── tests/             # Unit tests
├── main.py            # Project entry point
└── requirements.txt
```

---

## Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Zhanna1503/ai-weather-analytics-dashboard.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```
ANTHROPIC_API_KEY=your_api_key_here
```

### 4. Run

```bash
python main.py
```

The script generates:

- `data/tomorrow_forecast.csv`
- `data/historical_weather.csv`

These files can be refreshed directly inside the Power BI dashboard.

---

## Why I Built This

I've spent the last few years building Power BI dashboards and working with data analytics.

This project explores how generative AI can complement traditional dashboards by automatically transforming structured weather data into clear, business-friendly recommendations.

Rather than replacing dashboards, AI adds another layer of interpretation that helps users understand the data faster.

---

## Future Improvements

- Support additional weather APIs
- One-click Power BI refresh
- Docker deployment
- Interactive Streamlit version
