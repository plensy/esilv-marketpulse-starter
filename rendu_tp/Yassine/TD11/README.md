cat > rendu_tp/Yassine/TD11/README.md <<'EOF'
# TD11 - Dash Dashboard

## Objective
Build a visual dashboard for MarketPulse using Dash and Plotly.

## Implementation
- Created `src/dashboard.py`.
- Installed Dash and Plotly.
- The dashboard consumes `build_market_snapshot()` from `src/main.py`.
- No provider calls or financial calculations are implemented in the dashboard.
- Displays provider, instrument, benchmark, lookback and interval.
- Displays instrument return, benchmark return and relative performance.
- Plots both instrument and benchmark Base 100 series.

## Validation
- Dashboard successfully launched using:
  `python src/dashboard.py`
- Dashboard opened successfully in the browser.
- Terminal output and dashboard values were verified to be consistent.

## Screenshot
See the `captures/` directory.
EOF