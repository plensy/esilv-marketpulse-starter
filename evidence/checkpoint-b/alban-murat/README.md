# Checkpoint B — Alban Murat (`alban-murat`)

## Pull Request & Code Review
- **Pull Request:** [#8 — feat: add core quantitative analytics module](https://github.com/alban-murat/esilv-marketpulse-g02-t01/pull/8)
- **Branches:** `feature/analytics` -> `main`
- **Merge Commit:** `230e9eb`
- **Reviewer:** `@josephineSov` (approved)

## Contributions
- Implemented `align_series` in `src/analytics.py` to align instrument and benchmark time series on common trading dates.
- Wired the analytics pipeline (`align_series`, `calculate_period_return`, `calculate_base_100`, `calculate_relative_performance`) into `src/main.py` with fallback import support.

## Validation (`python src/main.py` on `main`)
- **Aligned sessions:** `21`
- **AAPL period return:** `+6.48%`
- **SP500 period return:** `+2.15%`
- **Relative performance:** `+4.33 percentage points`
- **Base 100:** `AAPL` `100.00 -> 106.48` | `SP500` `100.00 -> 102.15`

## Attached Screenshots
- `01_pull_request.png` — Pull Request #8 status, review approval, and merge into `main`.
- `02_execution_output.png` — Terminal execution of `python src/main.py` on `main`.