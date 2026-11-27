from pathlib import Path
import csv
import json
from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import (
    ACCESS_MODE,
    BLOOMBERG_IDENTIFIERS,
    fetch_bloomberg_prices,
)

DATA_DIR = Path("data/sample")

PROVIDER_LABEL = "Bloomberg stage"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def normalize_price_row(row):
    return {
        "date": row["date"],
        "ticker": row["ticker"],
        "open": float(row["open"]),
        "high": float(row["high"]),
        "low": float(row["low"]),
        "close": float(row["close"]),
        "volume": int(row["volume"]),
    }


def build_market_snapshot(
    instrument_ticker="AAPL",
    benchmark_ticker="SP500",
):
    instrument_prices = fetch_bloomberg_prices(
        identifier=BLOOMBERG_IDENTIFIERS[instrument_ticker],
        canonical_ticker=instrument_ticker,
    )
    benchmark_prices = fetch_bloomberg_prices(
        identifier=BLOOMBERG_IDENTIFIERS[benchmark_ticker],
        canonical_ticker=benchmark_ticker,
    )

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

    return {
        "provider": PROVIDER_LABEL,
        "access_mode": ACCESS_MODE,
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": instrument_ticker,
        "benchmark": benchmark_ticker,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": instrument_base_100,
        "benchmark_base_100": benchmark_base_100,
    }


def main():
    snapshot = build_market_snapshot()
    instrument_ticker = snapshot["instrument"]
    benchmark_ticker = snapshot["benchmark"]
    instrument_return = snapshot["instrument_return"]
    benchmark_return = snapshot["benchmark_return"]
    relative_performance = snapshot["relative_performance"]
    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    rel_perf_rounded = round(relative_performance, 2)
    if rel_perf_rounded > 0:
        rel_perf_str = "+" + str(rel_perf_rounded)
    else:
        rel_perf_str = str(rel_perf_rounded)

    print("=== MarketPulse ===")
    print()
    print("Provider")
    print(snapshot["provider"])
    print()
    print("Access mode")
    print(snapshot["access_mode"])
    print()
    print("Market configuration")
    print("Instrument :", instrument_ticker, "- Apple Inc.")
    print("Benchmark  : S&P 500")
    print("Period     :", snapshot["lookback"])
    print("Interval   :", snapshot["interval"])
    print()
    print("Instrument return :", str(round(instrument_return, 2)) + "%")
    print("Benchmark return  :", str(round(benchmark_return, 2)) + "%")
    print()
    print("Relative performance")
    print(instrument_ticker, "vs", benchmark_ticker, ":", rel_perf_str, "percentage points")
    print()
    print("Base 100")
    print(instrument_ticker, " :", round(instrument_base_100[0]["value"], 2), "->", round(instrument_base_100[-1]["value"], 2))
    print(benchmark_ticker, ":", round(benchmark_base_100[0]["value"], 2), "->", round(benchmark_base_100[-1]["value"], 2))


if __name__ == "__main__":
    main()
