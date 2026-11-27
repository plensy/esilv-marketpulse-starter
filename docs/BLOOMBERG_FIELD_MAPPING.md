# Bloomberg Field Mapping

## Access mode

APPROVED_SAMPLE

Source:
data/sample/bloomberg_reference_sample.json

Reference:
docs/10_BLOOMBERG_INSTRUCTOR_REFERENCE.md

Live connectivity:
not demonstrated

## Market instruments

| Role | Canonical ticker | Bloomberg identifier |
|---|---|---|
| Instrument | AAPL | AAPL US Equity |
| Benchmark | SP500 | SPX Index |

## Field mapping

| MarketPulse field | Source field or mapping | Status / notes |
|---|---|---|
| date | `observation_date` | Teaching wrapper key (`string`, `YYYY-MM-DD`); not a Bloomberg LIVE field mnemonic |
| ticker | application mapping | Canonical ticker (`AAPL` or `SP500`), distinct from provider identifier (`AAPL US Equity`, `SPX Index`) |
| open | `open_value` | Teaching wrapper key (`float`); not a Bloomberg LIVE field mnemonic |
| high | `high_value` | Teaching wrapper key (`float`); not a Bloomberg LIVE field mnemonic |
| low | `low_value` | Teaching wrapper key (`float`); not a Bloomberg LIVE field mnemonic |
| close | `close_value` | Teaching wrapper key (`float`); not a Bloomberg LIVE field mnemonic |
| volume | `volume_value` | Teaching wrapper key (`int`); not a Bloomberg LIVE field mnemonic (`0` on `SP500` in sample) |

Note: teaching wrapper key != Bloomberg LIVE field mnemonic. Illustrative teaching values reused from starter data; not certified Bloomberg historical observations or proof of live Bloomberg connectivity.

## TD10 handoff

- Access mode: APPROVED_SAMPLE (Live connectivity: not demonstrated)
- Instrument identifier: `AAPL US Equity` (canonical: `AAPL`)
- Benchmark identifier: `SPX Index` (canonical: `SP500`)
- Date representation: ISO date string (`YYYY-MM-DD`, 21 aligned daily observations from `2026-09-01` to `2026-09-30` per series)
- Input structure: JSON object with metadata and a `series` list (`role`, `canonical_ticker`, `provider_identifier`, `observations` array)
- Missing fields: None in `bloomberg_reference_sample.json` (`observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value` all present; `volume_value` is `0` for `SP500`)
- Special normalization notes: Normalize `series[*].observations[*]` into canonical rows (`date`, `ticker`, `open`, `high`, `low`, `close`, `volume`) preserving `AAPL` and `SP500`, keeping `src/analytics.py` provider-neutral, and never labelling fallback output as live Bloomberg retrieval.
- Expected canonical reference: `data/sample/bloomberg_reference_expected.json`
