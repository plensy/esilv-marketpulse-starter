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
| date | `observation_date` | Mapped from teaching wrapper key (`YYYY-MM-DD`); teaching wrapper key != Bloomberg LIVE field |
| ticker | application mapping | Preserves canonical MarketPulse ticker (`AAPL` or `SP500`) instead of `AAPL US Equity` / `SPX Index` |
| open | `open_value` | Mapped from teaching wrapper key (`float`); teaching wrapper key != Bloomberg LIVE field mnemonic |
| high | `high_value` | Mapped from teaching wrapper key (`float`); teaching wrapper key != Bloomberg LIVE field mnemonic |
| low | `low_value` | Mapped from teaching wrapper key (`float`); teaching wrapper key != Bloomberg LIVE field mnemonic |
| close | `close_value` | Mapped from teaching wrapper key (`float`); teaching wrapper key != Bloomberg LIVE field mnemonic |
| volume | `volume_value` | Mapped from teaching wrapper key (`int`); teaching wrapper key != Bloomberg LIVE field mnemonic |

## TD10 handoff

- Access mode: APPROVED_SAMPLE
- Instrument identifier: `AAPL US Equity` (canonical ticker: `AAPL`)
- Benchmark identifier: `SPX Index` (canonical ticker: `SP500`)
- Date representation: ISO-8601 date string (`YYYY-MM-DD`) from `observation_date`
- Input structure: JSON sample (`data/sample/bloomberg_reference_sample.json`) containing series keyed by `provider_identifier` and `canonical_ticker` with teaching wrapper observation keys (`observation_date`, `open_value`, `high_value`, `low_value`, `close_value`, `volume_value`)
- Missing fields: None in the approved sample fixture; if a volume or OHLC field is absent or null in any record, handle explicitly in TD10 rather than guessing values
- Special normalization notes:
  - Keep provider-specific identifiers (`AAPL US Equity`, `SPX Index`) strictly inside `src/providers/bloomberg_provider.py`
  - Ensure output rows conform to the MarketPulse canonical row contract (`date`, `ticker`, `open`, `high`, `low`, `close`, `volume`) so `src/analytics.py` remains unchanged
  - Expected canonical reference: `data/sample/bloomberg_reference_expected.json`