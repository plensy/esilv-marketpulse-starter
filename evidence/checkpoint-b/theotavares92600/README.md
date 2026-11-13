# Checkpoint B - Théo TAVARES

## Identity

 Name: Théo TAVARES
 GitHub: theotavares92600
 Branch: `feature/yahoo-provider`
 Role on TD08: Lead Yahoo provider

## Main commits

 `db83cf5` chore(yahoo): add provider stub and yfinance dependency
 `1ce0a29` feat(yahoo): add yfinance provider and provider switch

## My Pull Request

 **PR #10** - feat: add Yahoo Finance market data provider
  New module `src/providers/yahoo_provider.py` returning canonical observation
  rows from Yahoo Finance, `yfinance` added to `requirements.txt`, and a
  provider switch in `src/main.py`. `src/analytics.py` was reused unchanged.

## Pull Request I reviewed

 Pending: no teammate Pull Request was open during the TD08 session.
  To be completed as soon as one is available.

## Evidence

 `01_pull_request.png` - PR #10 with title, author, source and target branch.
 `02_code_review.png` - PENDING (see above).
 `03_yahoo_market_data.png` - live retrieval from Yahoo Finance returning
  canonical rows for SP500 (ticker translated from `^GSPC`).
 `04_instrument_benchmark.png` - MarketPulse showing instrument and benchmark
  over the same lookback (1 month) and interval (daily).