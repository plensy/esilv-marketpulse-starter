# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source: data/sample/bloomberg_reference_sample.json

Reference: docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md (not present in the repository at the time of writing; the mapping below is taken from the fixture itself and from its `schema_note`)

Live connectivity: not demonstrated

The fixture declares `is_live_bloomberg_output: false`. Its provenance states that the values are illustrative teaching values reused from `data/sample/prices.csv` and are not certified Bloomberg historical observations. This document is therefore not proof of live Bloomberg connectivity.

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

Both pairs were verified in the fixture (`canonical_ticker` and `provider_identifier` of each series).

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | teaching wrapper key; string `YYYY-MM-DD`, same format as canonical rows |
| ticker | application mapping | AAPL or SP500, taken from `canonical_ticker` of the series, never from the Bloomberg identifier |
| open | open_value | teaching wrapper key; numeric |
| high | high_value | teaching wrapper key; numeric |
| low | low_value | teaching wrapper key; numeric |
| close | close_value | teaching wrapper key; numeric |
| volume | volume_value | teaching wrapper key; integer for AAPL, `0` for SPX Index |

Teaching wrapper key != Bloomberg LIVE field mnemonic. The keys above come from the approved fallback fixture and are not real Bloomberg field names. In LIVE mode, only field names actually observed in the approved environment may be documented.

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: AAPL US Equity (canonical ticker AAPL)
- Benchmark identifier: SPX Index (canonical ticker SP500)
- Date representation: string `YYYY-MM-DD` in `observation_date`, no time or timezone part
- Input structure: one JSON object with a `series` list. Each series has `role`, `canonical_ticker`, `provider_identifier` and an `observations` list of objects holding the six teaching keys. Observations are in chronological order, 21 per series (2026-09-01 to 2026-09-30)
- Missing fields: none observed. All six keys are present in every observation
- Special normalization notes:
  - the `ticker` value must come from `canonical_ticker`, not from `provider_identifier`
  - SPX Index has `volume_value` equal to `0` (an index has no traded volume); keep it as integer `0`
  - values are already numeric (no text conversion needed), but the provider should still produce `float` for prices and `int` for volume to match the canonical contract
  - the fixture contains no Bloomberg-specific headers or wrapper beyond `series`
- Expected canonical reference: data/sample/bloomberg_reference_expected.json (42 rows: 21 AAPL then 21 SP500, with fields date, ticker, open, high, low, close, volume)