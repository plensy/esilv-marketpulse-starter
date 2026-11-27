from pathlib import Path
import json

ACCESS_MODE = "APPROVED_SAMPLE"

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

DEFAULT_SAMPLE_PATH = Path("data/sample/bloomberg_reference_sample.json")


def fetch_raw_bloomberg_history(
    identifier,
    start_date=None,
    end_date=None,
    sample_path=DEFAULT_SAMPLE_PATH,
):
    with open(sample_path, encoding="utf-8") as file:
        payload = json.load(file)

    for series in payload.get("series", []):
        if series.get("provider_identifier") == identifier:
            observations = series.get("observations", [])
            if not observations:
                raise ValueError(f"No Bloomberg sample observations for {identifier}")
            return observations

    raise ValueError(f"Unsupported Bloomberg identifier in sample: {identifier}")


def normalize_bloomberg_history(raw_data, canonical_ticker):
    rows = []
    for observation in raw_data:
        rows.append({
            "date": str(observation["observation_date"]),
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })
    return rows


def fetch_bloomberg_prices(
    identifier,
    canonical_ticker,
    start_date=None,
    end_date=None,
):
    raw_observations = fetch_raw_bloomberg_history(
        identifier=identifier,
        start_date=start_date,
        end_date=end_date,
    )
    return normalize_bloomberg_history(
        raw_data=raw_observations,
        canonical_ticker=canonical_ticker,
    )
