# FMA NZ source notes

## Warnings and alerts

Primary source:

- <https://www.fma.govt.nz/library/warnings-and-alerts/>

Observed listing behavior:

- Search is public with `BasicSearch` query parameter, e.g. `?BasicSearch=scam`.
- Pagination uses `?start=N`, with a page step of 15 in current HTML.
- Each list item includes title, detail link, summary paragraph, and display date.

Detail pages:

- Detail URLs are under `/library/warnings-and-alerts/<slug>/`.
- Pages expose a short `meta description` and title.
- Publish date is commonly available via an in-page `published__text` span.

Download endpoint (legacy mention in issue):

- Required params in observed implementation: `DateFrom` and `DateTo` (YYYY-MM-DD)
  - <https://www.fma.govt.nz/library/warnings-and-alerts/downloadWarnings/?DateFrom=2026-01-01&DateTo=2026-12-31>
- Response is CSV with a filename like `Warnings_and_Alerts_FMA_2026-01-01_to_2026-12-31.csv`.
- Calling without dates returns HTTP 400.

## Licensed provider listing

Primary source:

- <https://www.fma.govt.nz/business/licensed-providers/>

Observed list behavior:

- Same public result-list HTML pattern as warnings index with link, summary, and term chips.
- Search uses `BasicSearch` and can be constrained by provider type terms when present.
  - Crowdfunding terms seen in results: `Crowdfunding providers`
  - P2P terms seen in results: `Peer-to-peer lending service providers`
- Type pages under `/business/services/crowdfunding/`, `/business/services/peer-to-peer-lending-providers/`, and `/business/services/financial-advice-provider/` are useful for context and guidance.

Provider detail pages:

- Example entity page pattern: `/business/licensed-providers/<slug>/`.
- Detail pages typically expose `meta description` with provider name and classification text and FSP number.

## Advice provider register (cross-check)

Primary pointer:

- FMA licensed-services guidance and register pointer:
  - <https://www.fma.govt.nz/business/services/financial-advice-provider/>
  - FSP Register landing page linked from FMA: <https://fsp-register.companiesoffice.govt.nz/>

Observed limitation:

- The FSP register entrypoint in this environment is JS/login-fronted and does not provide a stable public query endpoint in the fetched HTML shell.
- This skill therefore returns source links and capability notes for advice-provider checks and does not mirror the full FSPR entity query flow.

## General caveats

- Upstream pages may return Incapsula/anti-bot style 403 in some hosts.
- Commands return `upstream_unavailable` with exit code 2 to avoid fabricating results.
