from pathlib import Path
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

# MarketPulse - main entry point
DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def normalize_price_row(row):
    """Convert the text fields of a CSV row into numeric values."""
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def main():
    instruments = load_instruments()
    prices = [normalize_price_row(row) for row in load_prices()]

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    print("=== MarketPulse ===")
    print("Provider: CSV")
    print()
    print("Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    print(f"Market: {instrument['market']}")
    print(f"First date: {get_first_date(instrument_prices)}")
    print(f"Last date: {get_last_date(instrument_prices)}")
    print(f"Last price: {instrument_latest['close']:.2f} {instrument['currency']}")
    print()
    print("Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    print(f"Market: {benchmark['market']}")
    print(f"First date: {get_first_date(benchmark_prices)}")
    print(f"Last date: {get_last_date(benchmark_prices)}")
    print(f"Last level: {benchmark_latest['close']:.2f}")
    print()
    print(f"Data period: {LOOKBACK_LABEL}")
    print(f"Observation frequency: {INTERVAL_LABEL}")
    print()
    print("Observations")
    print(f"{instrument['ticker']}: {len(instrument_prices)}")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)}")
    print()
    print("Performance comparison")
    print(f"Common dates: {len(aligned_instrument)}")
    print(f"{instrument['ticker']} period return: {instrument_return:.2f}%")
    print(f"{benchmark['ticker']} period return: {benchmark_return:.2f}%")
    print(
        f"Relative performance: {relative_performance:+.2f} percentage points"
    )
    print()
    print("Base 100")
    print(
        f"{instrument['ticker']:<6}: "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']:<6}: "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()