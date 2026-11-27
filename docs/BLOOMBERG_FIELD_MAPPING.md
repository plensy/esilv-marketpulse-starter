# Bloomberg Field Mapping

## 1. Access mode

Access mode: `APPROVED_SAMPLE`

No live Bloomberg environment was available during TD09.

The mapping is based exclusively on the instructor-approved sample files:

- `data/sample/bloomberg_reference_sample.json`
- `data/sample/bloomberg_reference_expected.json`
- `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`

The sample contains illustrative teaching values. It is not live Bloomberg output and does not demonstrate Bloomberg connectivity.

The keys used in the sample are teaching wrapper keys, not Bloomberg field mnemonics.

## 2. Instrument and benchmark identifiers

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

The Bloomberg identifier is provider-specific. MarketPulse must preserve its canonical ticker.

## 3. Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | observation_date | Teaching wrapper key |
| ticker | canonical_ticker | Application mapping: AAPL or SP500 |
| open | open_value | Teaching wrapper key |
| high | high_value | Teaching wrapper key |
| low | low_value | Teaching wrapper key |
| close | close_value | Teaching wrapper key |
| volume | volume_value | Teaching wrapper key |

These mappings describe the approved sample structure only. They do not establish actual Bloomberg field mnemonics.

## 4. Instrument input: AAPL

- Role: instrument
- Canonical ticker: `AAPL`
- Provider identifier: `AAPL US Equity`
- Source: `data/sample/bloomberg_reference_sample.json`
- Observations: 21

The sample uses the following wrapper keys:

- `observation_date`
- `open_value`
- `high_value`
- `low_value`
- `close_value`
- `volume_value`

## 5. Benchmark input: SP500

- Role: benchmark
- Canonical ticker: `SP500`
- Provider identifier: `SPX Index`
- Source: `data/sample/bloomberg_reference_sample.json`
- Observations: 21

The provider identifier `SPX Index` must not replace the canonical ticker `SP500`.

## 6. Canonical output

The expected canonical reference is:

`data/sample/bloomberg_reference_expected.json`

It contains 42 rows:

- 21 rows with ticker `AAPL`
- 21 rows with ticker `SP500`

Each row uses the canonical fields:

`date`, `ticker`, `open`, `high`, `low`, `close`, `volume`.

## 7. Missing fields and normalization notes

- No live Bloomberg response was available for inspection.
- Actual Bloomberg field mnemonics are therefore not verified.
- The sample provides all seven canonical fields through teaching wrapper keys.
- Benchmark volume is represented as `0` in the sample.
- Dates are represented as strings in `YYYY-MM-DD` format.
- No Bloomberg credentials or session secrets are used or committed.

## 8. TD10 handoff

- Access mode: `APPROVED_SAMPLE`
- Instrument identifier: `AAPL US Equity`
- Benchmark identifier: `SPX Index`
- Date representation: `YYYY-MM-DD` string
- Input structure: JSON object containing a `series` array and `observations` arrays
- Missing fields: No canonical fields are missing in the approved sample
- Special normalization notes:
  - Map `AAPL US Equity` to canonical ticker `AAPL`
  - Map `SPX Index` to canonical ticker `SP500`
  - Treat sample keys as teaching wrapper keys, not Bloomberg field mnemonics
  - Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
