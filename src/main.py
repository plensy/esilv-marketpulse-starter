from pathlib import Path
import json

from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.yahoo_provider import fetch_yahoo_prices
from providers.bloomberg_provider import ACCESS_MODE, fetch_bloomberg_prices


DATA_DIR = Path("data/sample")

LOOKBACK_LABEL = "1 month"
INTERVAL_LABEL = "Daily"
PROVIDER_LABEL = "Bloomberg stage"

YAHOO_SYMBOLS = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def load_instruments():
    with open(DATA_DIR / "instruments.json", encoding="utf-8") as file:
        return json.load(file)


def get_first_close(prices):
    return float(prices[0]["close"])


def get_last_close(prices):
    return float(prices[-1]["close"])

def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def display_market_summary(asset, prices, period_return, show_currency=True):
    currency = ""
    if show_currency:
        currency = " " + asset["currency"]

    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Market        : {asset['market']}")
    print(f"Observations  : {len(prices)}")
    print(f"First date    : {get_first_date(prices)}")
    print(f"Last date     : {get_last_date(prices)}")
    print(f"First close   : {get_first_close(prices):.2f}{currency}")
    print(f"Last close    : {get_last_close(prices):.2f}{currency}")
    print(f"Period return : {period_return:.2f}%")


def build_market_snapshot():
    instruments = load_instruments()
    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = fetch_bloomberg_prices(instrument["ticker"])
    benchmark_prices = fetch_bloomberg_prices(benchmark["ticker"])

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)
    relative = calculate_relative_performance(
        instrument_return,
        benchmark_return,
    )

    instrument_base = calculate_base_100(aligned_instrument)
    benchmark_base = calculate_base_100(aligned_benchmark)

    snapshot = {}
    snapshot["provider"] = PROVIDER_LABEL
    snapshot["access_mode"] = ACCESS_MODE
    snapshot["lookback"] = LOOKBACK_LABEL
    snapshot["interval"] = INTERVAL_LABEL
    snapshot["instrument"] = instrument
    snapshot["benchmark"] = benchmark
    snapshot["instrument_prices"] = aligned_instrument
    snapshot["benchmark_prices"] = aligned_benchmark
    snapshot["instrument_return"] = instrument_return
    snapshot["benchmark_return"] = benchmark_return
    snapshot["relative_performance"] = relative
    snapshot["instrument_base_100"] = instrument_base
    snapshot["benchmark_base_100"] = benchmark_base
    return snapshot


def main():
    snapshot = build_market_snapshot()

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]
    instrument_base = snapshot["instrument_base_100"]
    benchmark_base = snapshot["benchmark_base_100"]

    print("=== MarketPulse ===")
    print()
    print("Market configuration")
    print(f"Period   : {snapshot['lookback']}")
    print(f"Interval : {snapshot['interval']}")
    print(f"Provider : {snapshot['provider']}")
    print(f"Access mode : {snapshot['access_mode']}")
    print()
    print("Instrument")
    display_market_summary(
        instrument,
        snapshot["instrument_prices"],
        snapshot["instrument_return"],
    )
    print()
    print("Benchmark")
    display_market_summary(
        benchmark,
        snapshot["benchmark_prices"],
        snapshot["benchmark_return"],
        show_currency=False,
    )
    print()
    print("Relative performance")
    print(
        f"{instrument['ticker']} vs {benchmark['ticker']} : "
        f"{snapshot['relative_performance']:+.2f} percentage points"
    )
    print()
    print("Base 100")
    print(
        f"{instrument['ticker']:<6}: "
        f"{instrument_base[0]['value']:.2f} -> "
        f"{instrument_base[-1]['value']:.2f}"
    )
    print(
        f"{benchmark['ticker']:<6}: "
        f"{benchmark_base[0]['value']:.2f} -> "
        f"{benchmark_base[-1]['value']:.2f}"
    )


if __name__ == "__main__":
    main()

