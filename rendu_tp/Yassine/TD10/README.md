mkdir -p rendu_tp/Yassine/TD10/captures
cat > rendu_tp/Yassine/TD10/README.md <<'EOF'
# TD10 — Bloomberg Provider

## Objective
Implement a Bloomberg-specific provider boundary while preserving the existing MarketPulse analytics architecture.

## Access mode
APPROVED_SAMPLE

Live Bloomberg connectivity was not demonstrated.

## Architecture

Bloomberg-stage input
        |
        v
bloomberg_provider.py
        |
        v
Canonical rows
        |
        v
align_series()
        |
        v
Shared analytics
        |
        v
MarketPulse snapshot and terminal output

## Bloomberg identifiers

| Canonical ticker | Bloomberg identifier |
|---|---|
| AAPL | AAPL US Equity |
| SP500 | SPX Index |

## Canonical data structure

The provider normalizes input into:

- date
- ticker
- open
- high
- low
- close
- volume

## Reused analytics

The Bloomberg provider must reuse the existing provider-neutral analytics:

- Series alignment
- Period return
- Base 100
- Relative performance

No Bloomberg-specific calculations are implemented in analytics.py.

## Validation

The implementation is validated using the APPROVED_SAMPLE dataset.

This fallback validates the provider boundary and normalization contract but does not demonstrate live Bloomberg connectivity.

## TD11 handoff

The shared application boundary is:

build_market_snapshot(...)

TD11 will consume this snapshot without creating a second provider or analytics path.
EOF