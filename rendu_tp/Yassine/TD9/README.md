cat > rendu_tp/Yassine/TD9/README.md <<'EOF'
# TD9 — Bloomberg Introduction

## Objective
Prepare the Bloomberg data mapping for TD10 without implementing a Bloomberg provider.

## Access mode
**APPROVED_SAMPLE**

Live Bloomberg connectivity was not demonstrated. The analysis is based on the approved sample dataset.

## Instruments
- Instrument: AAPL — `AAPL US Equity`
- Benchmark: SP500 — `SPX Index`

## Field mapping
| Canonical field | Sample field |
|---|---|
| date | observation_date |
| ticker | canonical_ticker |
| open | open_value |
| high | high_value |
| low | low_value |
| close | close_value |
| volume | volume_value |

The sample keys are teaching wrapper keys, not Bloomberg LIVE field mnemonics.

## Results
- 21 observations for AAPL
- 21 observations for SP500
- No missing values observed
- SP500 volume is zero in the sample

## TD10 handoff
The expected canonical structure uses the fields `date`, `ticker`, `open`, `high`, `low`, `close`, and `volume`.

Prices should be normalized to floats, volume to integers, and canonical tickers preserved as `AAPL` and `SP500`.
EOF