from pathlib import Path
import csv
import json

try:
    from src.analytics import (
        align_series,
        calculate_period_return,
        calculate_base_100,
        calculate_relative_performance,
    )
    from src.providers.yahoo_provider import fetch_yahoo_prices
except ModuleNotFoundError:
    from analytics import (
        align_series,
        calculate_period_return,
        calculate_base_100,
        calculate_relative_performance,
    )
    from providers.yahoo_provider import fetch_yahoo_prices


DATA_DIR = Path("data/sample")

# These starter values mirror config/settings.yml.
# settings.yml is a human-readable configuration contract in the CORE.
# Parsing YAML is optional and is not required by the 18-hour lab sequence.
PROVIDER = "yahoo"  # "yahoo" or "csv"
LOOKBACK = "1mo"
INTERVAL = "1d"
LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def filter_prices(prices, ticker):
    return [row for row in prices if row["ticker"] == ticker]


def display_market_metadata(asset):
    print(f"Market: {asset['market']}")
    print(f"Currency: {asset['currency']}")


def main():
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    if PROVIDER == "yahoo":
        instrument_prices = fetch_yahoo_prices(
            instrument["ticker"], lookback=LOOKBACK, interval=INTERVAL
        )
        benchmark_prices = fetch_yahoo_prices(
            benchmark["ticker"], lookback=LOOKBACK, interval=INTERVAL
        )
        provider_label = "Yahoo Finance"
    elif PROVIDER == "csv":
        prices = load_prices()
        instrument_prices = filter_prices(prices, instrument["ticker"])
        benchmark_prices = filter_prices(prices, benchmark["ticker"])
        provider_label = "CSV"
    else:
        raise ValueError(f"Unsupported provider: {PROVIDER}")

    instrument_latest = instrument_prices[-1]
    benchmark_latest = benchmark_prices[-1]

    print("=== MarketPulse ===")
    print()
    print("Tracked Instrument")
    print(f"{instrument['ticker']} - {instrument['name']}")
    display_market_metadata(instrument)
    print(f"Latest close price: {float(instrument_latest['close']):.2f} {instrument['currency']}")
    print()
    print("Reference Benchmark")
    print(f"{benchmark['ticker']} - {benchmark['name']}")
    display_market_metadata(benchmark)
    print(f"Latest close level: {float(benchmark_latest['close']):.2f}")
    print()
    print("Sample Configuration")
    print(f"Lookback period: {LOOKBACK_LABEL}")
    print(f"Sampling interval: {INTERVAL_LABEL}")
    print(f"Provider: {provider_label}")
    print()
    print("Observation Count")
    print(f"{instrument['ticker']}: {len(instrument_prices)} observations")
    print(f"{benchmark['ticker']}: {len(benchmark_prices)} observations")

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices, benchmark_prices
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative_perf = calculate_relative_performance(
        instrument_return, benchmark_return
    )

    instrument_base_100 = calculate_base_100(aligned_instrument)
    benchmark_base_100 = calculate_base_100(aligned_benchmark)

    print()
    print("Comparison (aligned)")
    print(f"Aligned sessions        : {len(aligned_instrument)}")
    print(f"{instrument['ticker']} period return      : {instrument_return:+.2f}%")
    print(f"{benchmark['ticker']} period return     : {benchmark_return:+.2f}%")
    print(f"Relative performance    : {relative_perf:+.2f} percentage points")
    print()
    print("Base 100")
    print(
        f"{instrument['ticker']}   : {instrument_base_100[0]['value']:.2f} -> {instrument_base_100[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']}  : {benchmark_base_100[0]['value']:.2f} -> {benchmark_base_100[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()