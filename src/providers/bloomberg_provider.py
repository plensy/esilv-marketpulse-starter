from pathlib import Path
import json


DATA_DIR = Path("data/sample")
BLOOMBERG_SAMPLE_FILE = DATA_DIR / "bloomberg_reference_sample.json"


def fetch_raw_bloomberg_history(identifier, start_date=None, end_date=None):
    """
    Load approved Bloomberg teaching data for the requested identifier.
    This is APPROVED_SAMPLE mode, not a live Bloomberg connection.
    """
    with open(BLOOMBERG_SAMPLE_FILE, encoding="utf-8") as file:
        sample = json.load(file)

    for series in sample["series"]:
        if series["provider_identifier"] == identifier:
            return series

    raise ValueError(
        f"No Bloomberg sample data found for {identifier}"
    )


def normalize_bloomberg_history(raw_data, canonical_ticker):
    """
    Convert approved sample observations into MarketPulse canonical rows.
    """
    rows = []

    for observation in raw_data["observations"]:
        rows.append({
            "date": observation["observation_date"],
            "ticker": canonical_ticker,
            "open": float(observation["open_value"]),
            "high": float(observation["high_value"]),
            "low": float(observation["low_value"]),
            "close": float(observation["close_value"]),
            "volume": int(observation["volume_value"]),
        })

    return rows