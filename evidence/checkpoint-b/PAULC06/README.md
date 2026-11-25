# Checkpoint B — Paul Courty (`PAULC06`)

## Pull Request & Code Review
- **Pull Request:** [#6 — feat: improve terminal labels](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/6)
- **Branches:** `feature/improve-terminal-labels` -> `main`
- **Code Review:** [#9 — feat: add Yahoo Finance market data provider](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/9) (`@PAULC06` — approved)

## Contributions
- Improved terminal output labels and readability in `src/main.py` (`feature/improve-terminal-labels`).
- Reviewed and validated PR #9 (`feature/yahoo-provider`): verified canonical contract compliance (`AAPL` and `SP500` mapping without exposing `^GSPC`), absence of `print` statements in `src/providers/yahoo_provider.py`, preservation of `src/analytics.py`, and live execution with `yfinance`.

## Validation (`python src/main.py` on `main`)
- **Provider:** `Yahoo Finance` (`1 month`, `Daily`)
- **Aligned sessions:** `23`
- **AAPL period return:** `+2.40%`
- **SP500 period return:** `-7.47%`
- **Relative performance:** `+9.88 percentage points`
- **Base 100:** `AAPL` `100.00 -> 102.40` | `SP500` `100.00 -> 92.53`

## Attached Screenshots
- `01_pull_request.png` — Merged Pull Request #6 (`feature/improve-terminal-labels` -> `main`).
- `02_code_review.png` — Approved code review with technical verification comments on Pull Request #9.
- `03_yahoo_market_data.png` — Live Yahoo Finance canonical data retrieval (`fetch_yahoo_prices`).
- `04_instrument_benchmark.png` — Full terminal output of `python src/main.py` comparing `AAPL` and `SP500` (`1 month`, `Daily`).
