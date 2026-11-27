
from pathlib import Path
import csv
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)

from providers.yahoo_provider import fetch_yahoo_prices

from providers.bloomberg_provider import (
    fetch_bloomberg_prices,
    ACCESS_MODE,
)


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "sample"

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"

YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


# --------------------------------------------------
# DATA LOADING
# --------------------------------------------------

def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def load_prices():
    with open(DATA_DIR / "prices.csv", encoding="utf-8") as file:
        return list(csv.DictReader(file))


# --------------------------------------------------
# CSV PROVIDER
# --------------------------------------------------

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


def filter_prices(prices, ticker):
    return [
        normalize_price_row(row)
        for row in prices
        if row["ticker"] == ticker
    ]


def fetch_csv_prices(ticker):
    prices = load_prices()
    return filter_prices(prices, ticker)


# --------------------------------------------------
# MARKET SNAPSHOT
# --------------------------------------------------

def build_market_snapshot(
    provider="bloomberg",
    lookback=LOOKBACK_LABEL,
    interval=INTERVAL_LABEL,
):
    instruments = load_instruments()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_ticker = instrument["ticker"]
    benchmark_ticker = benchmark["ticker"]

    # Select the provider
    if provider == "csv":

        instrument_prices = fetch_csv_prices(instrument_ticker)
        benchmark_prices = fetch_csv_prices(benchmark_ticker)

        provider_name = "Local CSV sample"
        access_mode = "LOCAL_CSV_SAMPLE"

    elif provider == "yahoo":

        instrument_prices = fetch_yahoo_prices(
            symbol=YAHOO_SYMBOLS[instrument_ticker],
            canonical_ticker=instrument_ticker,
            period="1mo",
            interval="1d",
        )

        benchmark_prices = fetch_yahoo_prices(
            symbol=YAHOO_SYMBOLS[benchmark_ticker],
            canonical_ticker=benchmark_ticker,
            period="1mo",
            interval="1d",
        )

        provider_name = "Yahoo Finance via yfinance"
        access_mode = "YAHOO_FINANCE"

    elif provider == "bloomberg":

        instrument_prices = fetch_bloomberg_prices(
            instrument_ticker
        )

        benchmark_prices = fetch_bloomberg_prices(
            benchmark_ticker
        )

        provider_name = "Bloomberg stage"
        access_mode = ACCESS_MODE

    else:
        raise ValueError(
            f"Unsupported provider: {provider}. "
            "Choose csv, yahoo, or bloomberg."
        )

    # Validate the returned data
    if not instrument_prices:
        raise ValueError(
            f"No prices found for {instrument_ticker}"
        )

    if not benchmark_prices:
        raise ValueError(
            f"No prices found for {benchmark_ticker}"
        )

    # Existing analytics are reused for every provider
    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    if not aligned_instrument:
        raise ValueError(
            "No common dates found between instrument and benchmark"
        )

    instrument_return = calculate_period_return(
        aligned_instrument
    )

    benchmark_return = calculate_period_return(
        aligned_benchmark
    )

    relative_performance = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base_100 = calculate_base_100(
        aligned_instrument
    )

    benchmark_base_100 = calculate_base_100(
        aligned_benchmark
    )

    # Common output structure
    return {
        "provider": provider_name,
        "access_mode": access_mode,
        "lookback": lookback,
        "interval": interval,
        "instrument": instrument,
        "benchmark": benchmark,
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": relative_performance,
        "instrument_base_100": instrument_base_100,
        "benchmark_base_100": benchmark_base_100,
        "aligned_instrument": aligned_instrument,
        "aligned_benchmark": aligned_benchmark,
    }


# --------------------------------------------------
# APPLICATION
# --------------------------------------------------

def main(provider="bloomberg"):

    snapshot = build_market_snapshot(provider=provider)

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    aligned_instrument = snapshot["aligned_instrument"]

    instrument_base_100 = snapshot["instrument_base_100"]
    benchmark_base_100 = snapshot["benchmark_base_100"]

    print("=== MarketPulse ===")
    print()

    print("Provider:", snapshot["provider"])
    print("Access mode:", snapshot["access_mode"])
    print()

    print("Market configuration")
    print("Instrument:", instrument["ticker"], "-", instrument["name"])
    print("Benchmark:", benchmark["name"])
    print("Period:", snapshot["lookback"])
    print("Interval:", snapshot["interval"])
    print()

    print("Common dates:", len(aligned_instrument))
    print("First date:", aligned_instrument[0]["date"])
    print("Last date:", aligned_instrument[-1]["date"])
    print()

    print(
        f"Instrument return: "
        f"{snapshot['instrument_return']:.2f}%"
    )

    print(
        f"Benchmark return: "
        f"{snapshot['benchmark_return']:.2f}%"
    )

    print()

    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']}: "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    )

    print()

    print("Base 100")

    print(
        f"{instrument['ticker']}: "
        f"{instrument_base_100[0]['value']:.2f} -> "
        f"{instrument_base_100[-1]['value']:.2f}"
    )

    print(
        f"{benchmark['ticker']}: "
        f"{benchmark_base_100[0]['value']:.2f} -> "
        f"{benchmark_base_100[-1]['value']:.2f}"
    )


# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":
    main(provider="bloomberg")
