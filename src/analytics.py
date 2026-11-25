"""MarketPulse analytics: pure functions for comparison (TD07)."""


def index_by_date(prices):
    return {row["date"]: row for row in prices}


def align_series(instrument_prices, benchmark_prices):
    instrument_by_date = index_by_date(instrument_prices)
    benchmark_by_date = index_by_date(benchmark_prices)

    common_dates = sorted(instrument_by_date.keys() & benchmark_by_date.keys())

    aligned_instrument = [instrument_by_date[date] for date in common_dates]
    aligned_benchmark = [benchmark_by_date[date] for date in common_dates]

    return aligned_instrument, aligned_benchmark


def calculate_period_return(prices):
    if not prices:
        raise ValueError("Price series cannot be empty")

    first_close = float(prices[0]["close"])
    last_close = float(prices[-1]["close"])

    if first_close == 0:
        raise ValueError("First close cannot be zero")

    return ((last_close / first_close) - 1.0) * 100.0


def calculate_base_100(prices):
    if not prices:
        raise ValueError("Cannot compute base 100 on an empty price series.")

    first_close = float(prices[0]["close"])
    if first_close == 0.0:
        raise ValueError("First close price cannot be zero.")

    return [
        {
            "date": row["date"],
            "ticker": row["ticker"],
            "value": (float(row["close"]) / first_close) * 100.0,
        }
        for row in prices
    ]


def calculate_relative_performance(instrument_return, benchmark_return):
    return instrument_return - benchmark_return