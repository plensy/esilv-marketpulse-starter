
# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source:
data/sample/bloomberg_reference_sample.json

Expected canonical reference:
data/sample/bloomberg_reference_expected.json

Instructor reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md

The instructor reference document is not available
in the current repository.

Live connectivity: not demonstrated.

## Data provenance

The sample contains illustrative teaching values
reused from data/sample/prices.csv.

These values are not certified Bloomberg historical
observations and are not LIVE Bloomberg output.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | ISO date string, YYYY-MM-DD |
| ticker | canonical_ticker | AAPL or SP500 |
| open | open_value | Convert to float |
| high | high_value | Convert to float |
| low | low_value | Convert to float |
| close | close_value | Convert to float |
| volume | volume_value | Convert to int |

All observation fields are teaching wrapper keys.
They are not Bloomberg LIVE field mnemonics.

## Provider identifiers

| Canonical ticker | CSV | Yahoo Finance | Bloomberg |
|---|---|---|---|
| AAPL | AAPL | AAPL | AAPL US Equity |
| SP500 | SP500 | ^GSPC | SPX Index |

## Input structure

The source is a JSON object containing metadata
and a list named series.

Each series contains:

- role
- canonical_ticker
- provider_identifier
- observations

Each observation contains:

- observation_date
- open_value
- high_value
- low_value
- close_value
- volume_value

## Observed instrument data

- Role: instrument
- Canonical ticker: AAPL
- Provider identifier: AAPL US Equity
- Number of observations: 21
- First date: 2026-09-01
- Last date: 2026-09-30
- First close: 250.0
- Last close: 266.2

## Observed benchmark data

- Role: benchmark
- Canonical ticker: SP500
- Provider identifier: SPX Index
- Number of observations: 21
- First date: 2026-09-01
- Last date: 2026-09-30
- First close: 6600.0
- Last close: 6742.0

## Missing fields and special values

No required fields are missing in the supplied
instrument and benchmark observations.

The benchmark volume is zero in all observations.
This value must be preserved during normalization.

It must not be interpreted as verified live
Bloomberg trading volume.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity
- Benchmark identifier: SPX Index
- Date representation: YYYY-MM-DD string
- Input structure: nested JSON with series and observations
- Missing fields: none observed in the supplied sample
- Instrument observations: 21
- Benchmark observations: 21
- Total expected canonical rows: 42
- Lookback: 1 month
- Interval: Daily

### Special normalization notes

- Extract each series from the series list.
- Read observations from each series.
- Preserve canonical tickers AAPL and SP500.
- Map teaching wrapper keys to canonical fields.
- Preserve dates in YYYY-MM-DD format.
- Convert OHLC values to float.
- Convert volume values to int.
- Preserve zero benchmark volume.
- Validate against bloomberg_reference_expected.json.
- Reuse the existing analytics.py functions.
- Keep provider-specific logic outside analytics.py.

## Expected canonical reference

data/sample/bloomberg_reference_expected.json

The expected JSON contains a flat list named rows
with 42 canonical observations.

## Conclusion

The Bloomberg-stage mapping is documented using
the approved teaching sample.

The analytical layer remains provider-neutral.

The Bloomberg provider implementation will be
completed in TD10.
