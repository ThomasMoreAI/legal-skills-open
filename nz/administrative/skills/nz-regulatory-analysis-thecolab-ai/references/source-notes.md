# Official source notes

## Scope

This skill is intentionally current-surface discovery, not archive recovery. It uses:

- Ministry for Regulation RAS index: `https://www.regulation.govt.nz/publications-and-resources/regulatory-analysis-summaries/`
- Ministry for the Environment Cabinet paper/RIS index: `https://environment.govt.nz/what-government-is-doing/cabinet-papers-and-regulatory-impact-statements/`

Both are public, official, keyless HTML surfaces. The declared outbound hosts are `www.regulation.govt.nz` and `environment.govt.nz`. The skill has no hidden collector, database, proxy, receipt, or archive dependency.

- Authentication: none
- Last verified: 2026-09-12

## Requests and parsing

- Ministry for Regulation search uses its public index `query` parameter and parses `search-result__wrapper` result cards. It follows the official next-page control, deduplicates publication URLs, and reports the total only after reaching the final page. Pagination is capped at 10 pages; a continuing or cyclic paginator fails explicitly rather than returning a false partial total. Displayed title, publication date, and author are retained.
- Ministry for the Environment search uses its public index `keyword` parameter and parses the JSON object embedded in the `listing-results-container` attribute. Only a JSON value optionally followed by the site's literal `['id']`, `['results']`, or `['total']` binding is accepted; other expressions fail closed.
- Detail inspection parses the page heading, a displayed update metadata value when present, and same-host `.pdf` anchors. Page type comes from the heading, not the Environment index directory name. URL fragments are removed and duplicate PDF links are collapsed.
- Redirects are manually bounded to three and must stay on an allowed host and publication path. Paths are repeatedly decoded to stability before allowlist and traversal checks, then canonically encoded. HTML bodies are capped at 2 MB. Every request has a 10-second timeout.

The environment listing is a website implementation surface rather than a published API. Either site can change its HTML. Missing required listing structures therefore return parser failure (exit 6), not a successful empty result.

## Document typing

Type classification uses visible titles, link labels, and filenames. It keeps these concepts distinct:

- Regulatory Analysis Summary (RAS)
- Regulatory Impact Statement (RIS)
- Regulatory Impact Assessment (RIA)
- Supplementary Analysis Report
- Cost Recovery Impact Statement
- independent/external quality assessment
- department/agency/panel quality assessment
- otherwise-labelled quality assessment
- Cabinet paper, Cabinet minute, briefing, other PDF/page

A label-derived type is discovery metadata, not an assessment of the document's substance or compliance. A neutral detail-page heading remains `publication_page`; the shared Environment directory path is never treated as a Cabinet-paper label. Read the linked document before making substantive claims.

## Empty, blocked, and unavailable states

A parsed official listing with zero matching results is successful empty data. An access challenge or HTTP 401/403/429/451 is blocked (exit 4). Network/server failures are unavailable (exit 5). Unexpected media types, changed parser structure, unsafe/cyclic pagination, or result sets beyond the page bound are failures (exit 6). The deterministic tests exercise pagination and totals, repeatedly encoded traversal, adversarial listing expressions, external URLs, duplicate fragments, blocked-page markers, wrong media types, and type ambiguity. The live smoke checks both sources' normal and alphanumeric no-match contracts plus Environment detail classification.

## Verification

Last meaningful source and fixture verification: 2026-09-12. Run:

```bash
python3 skills/nz-regulatory-analysis/scripts/test_contract.py
python3 skills/nz-regulatory-analysis/tests/test_parser.py
python3 scripts/run_smoke_tests.py nz-regulatory-analysis
```
