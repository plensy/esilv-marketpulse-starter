
from pathlib import Path
import json


BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}

ACCESS_MODE = "APPROVED_SAMPLE"

DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "sample"


def fetch_raw_bloomberg_history():
    """
    Load the instructor-approved Bloomberg sample fixture.
    This does not represent live Bloomberg connectivity.
    """
    sample_path = DATA_DIR / "bloomberg_reference_sample.json"

    with open(sample_path, encoding="utf-8") as file:
        return json.load(file)


def normalize_bloomberg_history(raw_data, canonical_ticker):
    """
    Convert Bloomberg-stage sample observations
    into MarketPulse canonical rows.
    """
    series = next(
        (
            item for item in raw_data["series"]
            if item["canonical_ticker"] == canonical_ticker
        ),
        None,
    )

    if series is None:
        raise ValueError(
            f"No Bloomberg sample series found for {canonical_ticker}"
        )

    expected_identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]

    if series["provider_identifier"] != expected_identifier:
        raise ValueError(
            f"Unexpected Bloomberg identifier for {canonical_ticker}"
        )

    rows = []

    for observation in series["observations"]:
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


def fetch_bloomberg_prices(canonical_ticker):
    """
    Fetch and normalize the approved sample data.
    """
    raw_data = fetch_raw_bloomberg_history()

    return normalize_bloomberg_history(
        raw_data,
        canonical_ticker,
    )
