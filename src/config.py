import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

import json
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent
CITIES_PATH = CONFIG_DIR / "data" / "cities.json"

with open(CITIES_PATH, "r") as f:
    CITIES = json.load(f)