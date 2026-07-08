import matplotlib.pyplot as plt
import pandas as pd


def plot_temperature_comparison(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(6, 4))

    x = df["city"]
    ax.bar(x, df["temp_max"], label="Max Temp (°C)", color="tomato")
    ax.bar(x, df["temp_min"], label="Min Temp (°C)", color="steelblue", alpha=0.7)

    ax.set_title(f"Tomorrow's Forecast ({df['date'].iloc[0]})")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()

    plt.tight_layout()
    plt.savefig("data/temperature_comparison.png")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("data/tomorrow_forecast.csv")
    plot_temperature_comparison(df)