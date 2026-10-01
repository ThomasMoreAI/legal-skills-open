# nz-parliament — API & source notes

Data source: **bills.parliament.nz**, a Blazor front-end backed by a public
same-origin JSON API. Keyless, read-only; no login, account, or browser needed.

## Endpoints

### Search / list bills — `POST /api/data/search`
JSON request body (send the full shape — omitting fields makes the API return
HTTP 500). Key fields:

| field | value |
|-------|-------|
| `documentPreset` | `1` (bills; this endpoint only serves bills — other presets 500) |
| `keyword` | full-text search string, or `null` |
| `billTab` | `"Current"` (default) or `"All"` |
| `column` / `direction` | sort; `17` / `1` = the site default (latest activity) |
| `pageSize` / `page` | paging (CLI caps `pageSize` at 50) |
| `status`, `documentTypes`, `documentSubtypes`, `billStages`, `terminatedReasons` | arrays, send `[]` |
| (many other fields) | send `null` — see `_search_payload` in `cli.py` |

Response: `{ "results": [...], "pageSize", "page", "totalResults" }`. Each result
is **camelCase**: `id`, `title`, `billNumber`, `itemType` (Government / Member's /
Local / Private), `status`, `billCurrentStageName`, `parliamentNumber`,
`lastStageDate`, etc. Note: the **sponsoring MP is not in search results**
(`memberName` is null even for Member's bills) — it only appears in the detail.

### Bill detail — `GET /api/data/Bill/{id}`
`{id}` is the GUID from a search result. Response is **PascalCase**: `Title`,
`BillNumber`, `BillTypeName`, `BillStatusName`, `BillCurrentStageName`,
`ParliamentNumber`, `Description`, `IntroducedDate`, `FirstReadingDate`,
`BillLegislationUrl`, `Stages` (`[{Name, Date}]`), `Attachments`, and `Members`
(`[{PreferredFormOfAddress, DisplayName, SortedName, ...}]` — no party field).

### Facets — `POST /api/data/Facet`
Same body as search; returns available filter values (`parliaments`,
`committees`, `documentStages`, etc). Not used by the CLI but handy for discovery.

## Resolution

`bill <ref>`: if `<ref>` is a GUID it is fetched directly; otherwise it is treated
as a bill number (e.g. `324-1`), searched across all bills, and matched on exact
`billNumber` (falling back to the top hit).

## Bill page URLs

Human pages are `https://bills.parliament.nz/v/6/{id}` (the `/v/6/` view prefix is
stable on the current site). Search results carry no URL, so the CLI constructs it.

## Scope / limitations

This API covers **bills and their legislative progress** only. MP directory data,
votes/divisions, Hansard, written questions, and petitions live on
`www.parliament.nz`, which is a Blazor SPA behind Radware bot protection and has no
clean keyless API — they are out of scope for this skill (candidates for a future
`--browser` extension).

## CI / smoke tests

`smoke_test.py` exercises `bills`, keyword search, and `bill` detail. All are
keyless. Network / upstream 5xx errors are treated as SKIP, not failures.
