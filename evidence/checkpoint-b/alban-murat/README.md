# Checkpoint B — Alban Murat (`alban-murat`)

## 1. Individual Pull Request & Code Review (TD05–TD06)
- **Pull Request:** [#4 — feat: display data provider label in summary](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/4)
- **Branches:** `feature/display-provider-label` -> `main`
- **Reviewer:** `@josephineSov` (approved)
- **Reviewed Pull Request:** [#7 — docs: add TD05 quick start instructions](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/7) — approved by `@alban-murat`

## 2. Live Yahoo Finance Integration (TD08)
- **Pull Request:** [#9 — feat: add Yahoo Finance market data provider](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/9)
- **Branches:** `feature/yahoo-provider` -> `main` (merge commit `0fdffa8`)
- **Contribution (Student 1 / Integrator):** Wired the `PROVIDER = "yahoo"` / `"csv"` switch into `src/main.py` (`e4bdec5`) and verified live retrieval (`AAPL` vs `SP500`, `1mo` / `1d`) reusing `src/analytics.py` unchanged.

## Attached Screenshots
- `01_pull_request.png` — Pull Request #4 status and approval from `@josephineSov`.
- `02_code_review.png` — Code review approval submitted on Pull Request #7.
- `03_yahoo_market_data.png` — Live Yahoo Finance market data retrieval in `python src/main.py`.
- `04_instrument_benchmark.png` — Aligned comparison (`AAPL` vs `SP500`, `1 month`, `Daily`) with period returns and Base 100.