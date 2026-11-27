# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

- Source: `data/sample/bloomberg_reference_sample.json`
- Reference: `docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md`
- Live connectivity: not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

Note: The source keys below are teaching wrapper keys from the approved sample fixture (teaching wrapper key != Bloomberg LIVE field mnemonic).

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Mapped directly as `YYYY-MM-DD` string |
| ticker | application mapping | Preserves canonical `AAPL` or `SP500` |
| open | `open_value` | Converted to `float` |
| high | `high_value` | Converted to `float` |
| low | `low_value` | Converted to `float` |
| close | `close_value` | Converted to `float` |
| volume | `volume_value` | Converted to `int` |

## TD10 handoff

- Access mode: `APPROVED_SAMPLE`
- Instrument identifier: `AAPL US Equity` (canonical `AAPL`)
- Benchmark identifier: `SPX Index` (canonical `SP500`)
- Date representation: `YYYY-MM-DD` via `observation_date`
- Input structure: JSON series entries using teaching wrapper keys
- Missing fields: None in the approved sample fixture
- Special normalization notes: Map wrapper keys to canonical MarketPulse row keys, cast numeric fields to `float`/`int`, and keep Bloomberg identifiers outside `analytics.py`.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
