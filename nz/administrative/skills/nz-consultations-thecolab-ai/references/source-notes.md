# Source notes

- Primary owner: New Zealand Government
- Listing: https://www.govt.nz/browse/engaging-with-government/consultations-have-your-say/consultations-listing/
- Declared outbound host: `www.govt.nz`
- Access mode: bounded, server-rendered HTML retrieval
- Authentication: none
- Last verified: 2026-07-19
- Update cadence: source-managed; deadlines are time-sensitive

## Implemented surface

The listing exposes one `cl-item` per consultation with a title, agency, human-readable
date range, open/closed status, summary and canonical agency consultation URL. The parser
normalises the two dates to ISO dates and preserves the original `date_text`. It deliberately
sets `closing_time_precision` to `date_only` and `closing_timezone` to null because the listing
does not publish an exact time or timezone.

The agency links are returned as provenance but are not fetched, so the connector makes no
outbound request beyond the declared `www.govt.nz` listing host. The cross-government listing
may not include every consultation run elsewhere. The CLI is read-only and never submits a
response.

The deterministic fixture covers open and closed records, dates, agency, summary, ID and source
link. The live smoke test makes one bounded listing request. A layout change that removes all
parseable records fails closed as a source-schema error.
