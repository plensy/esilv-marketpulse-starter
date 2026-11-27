from pathlib import Path
import csv
import json


if __package__:
    from .providers.bloomberg_provider import (
        fetch_raw_bloomberg_history,
        normalize_bloomberg_history,
    )
    from .analytics import (
        align_series,
        calculate_base_100,
        calculate_period_return,
        calculate_relative_performance,
    )
else:
    from providers.bloomberg_provider import (
        fetch_raw_bloomberg_history,
        normalize_bloomberg_history,
    )
    from analytics import (
        align_series,
        calculate_base_100,
        calculate_period_return,
        calculate_relative_performance,
    )

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


def get_first_close(prices):
    first_row = prices[0]
    return float(first_row["close"])


def get_last_close(prices):
    last_row = prices[-1]
    return float(last_row["close"])


def get_first_date(prices):
    return prices[0]["date"]


def get_last_date(prices):
    return prices[-1]["date"]


def display_configuration():
    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}")


def display_market_summary(asset, prices, period_return, show_currency=True):
    currency = ""
    if show_currency:
        currency = " " + asset["currency"]

    print(f"{asset['ticker']} - {asset['name']}")
    print("Provider     : Bloomberg stage")
    print(f"Observations : {len(prices)}")
    print(f"First date   : {get_first_date(prices)}")
    print(f"Last date    : {get_last_date(prices)}")
    print(f"First close  : {get_first_close(prices):.2f}{currency}")
    print(f"Last close   : {get_last_close(prices):.2f}{currency}")
    print(f"Period return : {period_return:.2f}%")

def fetch_bloomberg_prices():
    instrument_raw = fetch_raw_bloomberg_history("AAPL US Equity")
    benchmark_raw = fetch_raw_bloomberg_history("SPX Index")

    instrument_prices = normalize_bloomberg_history(
        instrument_raw,
        "AAPL",
    )
    benchmark_prices = normalize_bloomberg_history(
        benchmark_raw,
        "SP500",
    )

    return instrument_prices, benchmark_prices
def build_market_snapshot(instrument, benchmark):
    instrument_prices, benchmark_prices = fetch_bloomberg_prices()

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices,
        benchmark_prices,
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": "Bloomberg stage",
        "access_mode": "APPROVED_SAMPLE",
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": {
            **instrument,
            "prices": aligned_instrument,
        },
        "benchmark": {
            **benchmark,
            "prices": aligned_benchmark,
        },
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return,
            benchmark_return,
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }

def main():
    instruments = load_instruments()

    snapshot = build_market_snapshot(
        instruments["instrument"],
        instruments["benchmark"],
    )

    instrument = snapshot["instrument"]
    benchmark = snapshot["benchmark"]

    print("=== MarketPulse ===")
    print()
    print("Provider    : Bloomberg stage")
    print("Access mode : APPROVED_SAMPLE")
    print(f"Period      : {snapshot['lookback']}")
    print(f"Interval    : {snapshot['interval']}")
    print()

    display_market_summary(
        instrument,
        instrument["prices"],
        snapshot["instrument_return"],
    )
    print()
    display_market_summary(
        benchmark,
        benchmark["prices"],
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
        f"AAPL  : {snapshot['instrument_base_100'][0]['value']:.2f} "
        f"-> {snapshot['instrument_base_100'][-1]['value']:.2f}"
    )
    print(
        f"SP500 : {snapshot['benchmark_base_100'][0]['value']:.2f} "
        f"-> {snapshot['benchmark_base_100'][-1]['value']:.2f}"
    )

if __name__ == "__main__":
    main()
