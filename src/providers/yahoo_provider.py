import yfinance as yf


CANONICAL_TO_YAHOO = {
    "AAPL": "AAPL",
    "SP500": "^GSPC",
}


def fetch_yahoo_prices(canonical_ticker, lookback="1mo", interval="1d"):
    yahoo_symbol = CANONICAL_TO_YAHOO[canonical_ticker]

    data = yf.download(
        yahoo_symbol,
        period=lookback,
        interval=interval,
        auto_adjust=False,
        multi_level_index=False,
        progress=False,
    )

    prices = []

    for date, row in data.iterrows():
        observation = {
            "date": date.strftime("%Y-%m-%d"),
            "ticker": canonical_ticker,
            "open": float(row["Open"]),
            "high": float(row["High"]),
            "low": float(row["Low"]),
            "close": float(row["Close"]),
            "volume": int(row["Volume"]),
        }

        prices.append(observation)

    prices.sort(key=lambda row: row["date"])

    return prices