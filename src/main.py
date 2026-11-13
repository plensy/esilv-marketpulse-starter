
from pathlib import Path
import csv
import json

DATA_DIR = Path("data/sample")

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


def get_first_close(prices):
    first_row = prices[0]
    return float(first_row["close"])


def get_last_close(prices):
    last_row = prices[-1]
    return float(last_row["close"])


def display_market_summary(asset, prices, show_currency=True):
    print(f"{asset['ticker']} - {asset['name']}")
    print(f"Observations : {len(prices)}")
    print(f"Currency     : {asset['currency']}")

    first = get_first_close(prices)
    last = get_last_close(prices)

    if show_currency:
        print(f"First close  : {first:.2f} {asset['currency']}")
        print(f"Last close   : {last:.2f} {asset['currency']}")
    else:
        print(f"First close  : {first:.2f}")
        print(f"Last close   : {last:.2f}")


def main():
    instruments = load_instruments()
    prices = load_prices()

    instrument = instruments["instrument"]
    benchmark = instruments["benchmark"]

    instrument_prices = filter_prices(prices, instrument["ticker"])
    benchmark_prices = filter_prices(prices, benchmark["ticker"])

    print("=== MarketPulse ===\n")

    print("Market configuration")
    print(f"Period   : {LOOKBACK_LABEL}")
    print(f"Interval : {INTERVAL_LABEL}\n")

    print("Instrument")
    display_market_summary(instrument, instrument_prices, show_currency=True)

    print("\nBenchmark")
    display_market_summary(benchmark, benchmark_prices, show_currency=True)


if __name__ == "__main__":
    main()
