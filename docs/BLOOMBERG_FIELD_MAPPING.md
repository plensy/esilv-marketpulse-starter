# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md (not available in the repository)

Live connectivity:
not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Inspected inputs

- Instrument: provider_identifier = AAPL US Equity, canonical_ticker = AAPL, 21 observations from 2026-09-01 to 2026-09-30
- Benchmark: provider_identifier = SPX Index, canonical_ticker = SP500, 21 observations from 2026-09-01 to 2026-09-30

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | teaching wrapper key, string YYYY-MM-DD |
| ticker | application mapping | AAPL or SP500 (canonical_ticker), never the Bloomberg identifier |
| open | open_value | teaching wrapper key |
| high | high_value | teaching wrapper key |
| low | low_value | teaching wrapper key |
| close | close_value | teaching wrapper key |
| volume | volume_value | teaching wrapper key, always 0 for SPX Index |

teaching wrapper key != Bloomberg LIVE field mnemonic

No Bloomberg field mnemonic is used in this document.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity -> AAPL
- Benchmark identifier: SPX Index -> SP500
- Date representation: string YYYY-MM-DD in observation_date
- Input structure: JSON object with a "series" list; each series has role, canonical_ticker, provider_identifier and a list of observations
- Missing fields: none in the sample; volume_value is 0 for SPX Index (an index has no traded volume)
- Special normalization notes: use canonical_ticker for ticker; convert prices to float and volume to int; sample values are illustrative teaching values, not real Bloomberg data
- Expected canonical reference: data/sample/bloomberg_reference_expected.json
