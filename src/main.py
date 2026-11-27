from analytics import (
    align_series,
    calculate_base_100,
    calculate_period_return,
    calculate_relative_performance,
)
from providers.bloomberg_provider import (
    BLOOMBERG_IDENTIFIERS,
    fetch_raw_bloomberg_history,
    normalize_bloomberg_history,
)

LOOKBACK_LABEL = "1_month"
INTERVAL_LABEL = "Daily"


def build_market_snapshot():
    instrument_ticker = "AAPL"
    benchmark_ticker = "SP500"

    raw_instrument = fetch_raw_bloomberg_history(
        BLOOMBERG_IDENTIFIERS[instrument_ticker], None, None
    )
    raw_benchmark = fetch_raw_bloomberg_history(
        BLOOMBERG_IDENTIFIERS[benchmark_ticker], None, None
    )

    instrument_prices = normalize_bloomberg_history(
        raw_instrument, instrument_ticker
    )
    benchmark_prices = normalize_bloomberg_history(
        raw_benchmark, benchmark_ticker
    )

    aligned_instrument, aligned_benchmark = align_series(
        instrument_prices, benchmark_prices
    )

    instrument_return = calculate_period_return(aligned_instrument)
    benchmark_return = calculate_period_return(aligned_benchmark)

    return {
        "provider": "Bloomberg stage - APPROVED_SAMPLE",
        "lookback": LOOKBACK_LABEL,
        "interval": INTERVAL_LABEL,
        "instrument": {"ticker": instrument_ticker, "name": "Apple Inc."},
        "benchmark": {"ticker": benchmark_ticker, "name": "S&P 500"},
        "instrument_return": instrument_return,
        "benchmark_return": benchmark_return,
        "relative_performance": calculate_relative_performance(
            instrument_return, benchmark_return
        ),
        "instrument_base_100": calculate_base_100(aligned_instrument),
        "benchmark_base_100": calculate_base_100(aligned_benchmark),
    }


def main():
    s = build_market_snapshot()
    rel = round(s["relative_performance"], 2)
    rel_str = "+" + str(rel) if rel > 0 else str(rel)
    inst = s["instrument"]["ticker"]
    bench = s["benchmark"]["ticker"]

    print("=== MarketPulse ===")
    print()
    print("Provider")
    print("Bloomberg stage")
    print()
    print("Access mode")
    print("APPROVED_SAMPLE")
    print()
    print("Market configuration")
    print("Instrument :", inst, "-", s["instrument"]["name"])
    print("Benchmark  :", s["benchmark"]["name"])
    print("Period     :", s["lookback"])
    print("Interval   :", s["interval"])
    print()
    print("Instrument return :", str(round(s["instrument_return"], 2)) + "%")
    print("Benchmark return  :", str(round(s["benchmark_return"], 2)) + "%")
    print()
    print("Relative performance")
    print(inst, "vs", bench, ":", rel_str, "percentage points")
    print()
    print("Base 100")
    print(inst, " :", round(s["instrument_base_100"][0]["value"], 2),
          "->", round(s["instrument_base_100"][-1]["value"], 2))
    print(bench, ":", round(s["benchmark_base_100"][0]["value"], 2),
          "->", round(s["benchmark_base_100"][-1]["value"], 2))


if __name__ == "__main__":
    main()