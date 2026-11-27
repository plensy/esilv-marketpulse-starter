# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source: data/sample/bloomberg_reference_sample.json

Live connectivity: not demonstrated.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | YYYY-MM-DD |
| ticker | canonical_ticker | AAPL or SP500 |
| open | open_value | float |
| high | high_value | float |
| low | low_value | float |
| close | close_value | float |
| volume | volume_value | int |

These source fields are teaching wrapper keys, not Bloomberg LIVE field mnemonics.

## Observations

- AAPL: 21 observations.
- SP500: 21 observations.
- No null values were found.
- SP500 volume is zero in the approved sample.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity
- Benchmark identifier: SPX Index
- Date representation: YYYY-MM-DD
- Input structure: JSON series containing observations
- Missing fields: none observed in the sample
- Normalization: convert prices to float and volume to int
- Preserve canonical tickers AAPL and SP500

Expected canonical reference:

data/sample/bloomberg_reference_expected.json
