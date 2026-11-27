import json
from pathlib import Path

SAMPLE_PATH = Path("data/sample/bloomberg_reference_sample.json")

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def fetch_raw_bloomberg_history(identifier, start_date, end_date):
    # APPROVED_SAMPLE : start_date et end_date sont ignorés,
    # la fixture contient une période fixe.
    with open(SAMPLE_PATH, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError("Identifier not found in sample: " + identifier)


def normalize_bloomberg_history(raw_data, canonical_ticker):
    if raw_data["canonical_ticker"] != canonical_ticker:
        raise ValueError(
            "Ticker mismatch: " + raw_data["canonical_ticker"]
            + " != " + canonical_ticker
        )

    rows = []

    for obs in raw_data["observations"]:
        rows.append({
            "date": obs["observation_date"],
            "ticker": canonical_ticker,
            "open": float(obs["open_value"]),
            "high": float(obs["high_value"]),
            "low": float(obs["low_value"]),
            "close": float(obs["close_value"]),
            "volume": int(obs["volume_value"]),
        })

    return rows