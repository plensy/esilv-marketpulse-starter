import json


ACCESS_MODE = "APPROVED_SAMPLE"

SAMPLE_FILE = "data/sample/bloomberg_reference_sample.json"

BLOOMBERG_IDENTIFIERS = {
    "AAPL": "AAPL US Equity",
    "SP500": "SPX Index",
}


def load_sample():
    file = open(SAMPLE_FILE, encoding="utf-8")
    data = json.load(file)
    file.close()
    return data

def find_series(data, identifier):
    for series in data["series"]:
        if series["provider_identifier"] == identifier:
            return series
    raise ValueError("Series not found: " + identifier)

def normalize_series(series):
    ticker = series["canonical_ticker"]
    rows = []
    for observation in series["observations"]:
        row = {}
        row["date"] = observation["observation_date"]
        row["ticker"] = ticker
        row["open"] = float(observation["open_value"])
        row["high"] = float(observation["high_value"])
        row["low"] = float(observation["low_value"])
        row["close"] = float(observation["close_value"])
        row["volume"] = int(observation["volume_value"])
        rows.append(row)
    return rows

def fetch_bloomberg_prices(canonical_ticker):
    identifier = BLOOMBERG_IDENTIFIERS[canonical_ticker]
    data = load_sample()
    series = find_series(data, identifier)
    rows = normalize_series(series)
    return rows

def fetch_raw_bloomberg_history(identifier, start_date, end_date):
    raise NotImplementedError("LIVE Bloomberg access is not available")