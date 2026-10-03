# JPO

Japan Patent Office Patent Information Retrieval API — patents, designs,
and trademarks.

**Auth**: requires `JPO_API_USERNAME` and `JPO_API_PASSWORD` environment
variables (issued by JPO upon registration; corporate users get higher
daily quotas than individual users).

**Availability**: the JPO MCP tools are **env-gated** — they auto-register
on the MCP surface only when both env vars are present. The hosted public
server `mcp.patentclient.com` intentionally does NOT carry these keys per
JPO TOS, so JPO tools are absent there. Private deploys (e.g. law-tools)
turn the surface on by mounting both secrets in their own Cloud Run env.
Library / Python callers (`from patent_client_agents.jpo import ...`)
work in either case as long as the env vars are set in the calling
process.

The MCP surface is **dispatched by `ip_type`** rather than parallel
patent/design/trademark tools — one tool per use case, with a `Literal`
argument that switches between the three IP types.

## MCP tool surface

| Tool | Args | Notes |
|---|---|---|
| `get_jpo_progress` | `application_number, ip_type` | Full status — works for patent/design/trademark |
| `get_jpo_progress_simple` | `application_number, ip_type` | Status without priority/family |
| `get_jpo_priority_info` | `application_number, ip_type` | Paris + domestic priorities |
| `get_jpo_registration_info` | `application_number, ip_type` | Granted-rights record |
| `get_jpo_number_reference` | `number, kind, ip_type` | Cross-reference application/publication/registration |
| `get_jpo_jplatpat_url` | `application_number, ip_type` | J-PlatPat permalink |
| `get_jpo_applicant` | `applicant, ip_type` | Auto-detects 9-digit code vs exact name |
| `get_jpo_documents` | `application_number, doc_kind, ip_type, parse=True` | Parsed file-history bundle + signed download URL. Pass `parse=False` to skip parsing and return just metadata + URL. |
| `get_jpo_patent_divisional_info` | `application_number` | Patent-only — no design/trademark equivalent |
| `get_jpo_patent_cited_documents` | `application_number` | Patent-only — patent + non-patent citations |
| `get_jpo_pct_national_phase_number` | `number, kind` | Patent-only — PCT lookup |

`ip_type` defaults to `"patent"` everywhere. `doc_kind` defaults to
`"mailed"` (the most useful prosecution-history slice).

## Client

```python
from patent_client_agents.jpo import (
    JpoClient,
    CaseNumberKind,         # 'application' / 'publication' / 'registration'
    PctKind,                # 'international_application' / 'international_publication'
    NumberType,             # numeric codes used inside bibliographyInformation
    parse_document_bundle,  # Shift-JIS XML parser
    DocumentBundle,
    DocumentEntry,
)
```

Library callers still get the per-IP-type methods on `JpoClient` —
`get_patent_progress`, `get_design_progress`, etc. The `ip_type`
dispatch is an MCP-surface concern only.

## Rate limits and quotas

- **10 requests per minute** is the JPO-mandated soft limit (handbook v14
  §3); enforced in-process by `JpoClient`'s rate limiter.
- **Daily caps are per-endpoint**, enforced server-side. Examples:
  - `app_progress` / `app_progress_simple` — 400 / day
  - `divisional_app_info` / `priority_right_app_info` — 30 / day
  - `applicant_attorney_cd` — 200 / day
  - `app_doc_cont_*` (document downloads) — 100 / day
  - `cite_doc_info` — 100 / day
  - `registration_info` — 50 / day
  - `jpp_fixed_address` — 200 / day
- Each response includes `remainAccessCount` (parsed into the `ApiResult`
  envelope but not surfaced on most domain models).
- Daily quota counter resets at 00:00 JST.

## Application number format

JPO patent application numbers are **10 digits** with no separators:
4-digit Gregorian year + 6-digit zero-padded serial. Pass them as
strings without hyphens:

```python
await client.get_patent_progress("2020123456")  # NOT "2020-123456"
```

Design and trademark applications use the same 10-digit format.

## Patent / design / trademark progress

```python
async with JpoClient() as client:
    # Full progress: title, applicants, dates, priority, family, file wrapper
    progress = await client.get_patent_progress("2020123456")
    progress.invention_title       # e.g. "立体配線構造体の製造方法"
    progress.applicant_attorney    # list[ApplicantAttorney]
    progress.filing_date           # "20200720" (YYYYMMDD, no separators)
    progress.publication_number    # JP wareki publication number
    progress.ad_publication_number # AD-converted publication (e.g. "2021090037")
    progress.registration_number   # "" if not yet registered
    progress.priority_right_information   # list[PriorityInfo]
    progress.parent_application_information  # ParentApplicationInfo | None
    progress.divisional_application_information  # list[DivisionalApplicationInfo]
    progress.bibliography_information  # list[BibliographyInformation] (file wrapper)

    # Simplified: omits priority + family info; same daily quota
    simple = await client.get_patent_progress_simple("2020123456")

    # Priority claims (Paris + domestic)
    priorities = await client.get_patent_priority_info("2020123456")

    # Divisional family (patent-only — no design/trademark equivalent)
    div = await client.get_patent_divisional_info("2020123456")

    # Citations: patent + non-patent (patent-only)
    cites = await client.get_patent_cited_documents("2020123456")

    # Registration record (granted patents only; None if not registered)
    reg = await client.get_patent_registration_info("2020123456")

    # Number cross-reference: kind = application / publication / registration
    ref = await client.get_patent_number_reference(
        CaseNumberKind.APPLICATION, "2020123456"
    )

    # J-PlatPat permalink (free public search portal)
    url = await client.get_patent_jplatpat_url("2020123456")

    # PCT national-phase lookup (patent-only)
    nat = await client.get_patent_pct_national_number(
        PctKind.INTERNATIONAL_APPLICATION, "JP2019011858"
    )
```

The same shape applies to designs (`get_design_*`) and trademarks
(`get_trademark_*`) on the client. From MCP, just pass
`ip_type="design"` or `ip_type="trademark"` to the dispatched tools.

## Applicant lookup

```python
async with JpoClient() as client:
    name = await client.get_patent_applicant_by_code("000003207")
    # -> "トヨタ自動車株式会社"

    matches = await client.get_patent_applicant_by_name("トヨタ自動車株式会社")
    # NOTE: exact match only. "トヨタ" alone returns nothing.
```

## Document bundles (parsed contents + download URL)

JPO's three document endpoints — `application_documents` (opinions +
amendments), `mailed_documents` (rejections + decisions), and
`refusal_notices` (rejection-only subset of mailed) — return a ZIP of
file-history files. **Patents ship JPO-flavoured XML; designs and
trademarks ship HTM** (handbook v14 §2(1) — both Shift-JIS encoded).
From MCP, **a single tool covers all nine combinations**:

```python
result = await get_jpo_documents(
    application_number="2020123456",
    doc_kind="refusal",       # or "application" / "mailed"
    ip_type="patent",         # or "design" / "trademark"
    parse=True,               # default — set False to skip parsing
)
# {
#   "ip_type": "patent",
#   "doc_kind": "refusal",
#   "application_number": "2020123456",
#   "entries": [
#     {
#       "filename": "06124084096-jpntce.xml",
#       "document_name": "拒絶理由通知書",
#       "document_variant": "notice-of-rejection-a131-rn",
#       "legal_date": "20240220",
#       "drafter_name": "黒田　久美子",
#       "articles": ["第29条第1項第3号（新規性）", ...],
#       "body_text": "この出願は、次の理由によって…"
#     }
#   ],
#   "binary_attachments": [],
#   "download_url": "https://mcp.patentclient.com/downloads/jpo/documents/patent/2020123456/refusal?key=...",
#   "resource_uri": "pca://jpo/documents/patent/2020123456/refusal",
#   "filename": "jpo_patent_2020123456_refusal.zip",
#   "content_type": "application/zip"
# }
```

If JPO has no documents on file (status 107 / 108) the tool returns
`{}` regardless of the `parse` value. The raw ZIP is reachable two
ways: fetch the signed `download_url` over HTTPS, or follow the
`resource_uri` via MCP `resources/read` (the path hosted sandboxes
like Claude CoWork take, since the MCP session bypasses the
outbound-HTTP allowlist). Both transports resolve the same cached
bytes — pick whichever your client supports.

Pass `parse=False` to skip the parser and return just the bundle
metadata + the dual-transport download fields (`download_url`,
`resource_uri`, `filename`, `content_type`, `size_bytes`,
`expires_at`). The response shape becomes
`{"application_number", "ip_type", "doc_kind", "entries": [],
"binary_attachments": [], "download_url", "resource_uri", ...}` —
useful when the agent only needs to hand the URL (or resource URI)
to a human reviewer or to a separate processing pipeline.

For library callers, the parsing layer is exposed directly:

```python
from patent_client_agents.jpo import parse_document_bundle

async with JpoClient() as client:
    raw = await client.get_design_application_documents("2020015234")
    bundle = parse_document_bundle(
        raw.zip_bytes,
        doc_kind="application",
        ip_type="design",
        application_number="2020015234",
    )
    for entry in bundle.entries:
        print(entry.document_name, entry.legal_date)
```

### Schema notes

`DocumentBundle.entries` has uniform shape across all nine
(ip_type × doc_kind) combinations:

- **applicant-filed docs** (`doc_kind="application"`) populate
  `document_code` (e.g. `A153` for opinion, `A1523` for amendment),
  `document_variant` (`response-a53` / `amendment-a523`),
  `applicant_names`, `dispatch_number` (the office-action ID being
  responded to), and `body_text`.
- **mailed / refusal docs** populate `document_name` (e.g.
  `拒絶理由通知書`), `legal_date` (drafting date), `drafter_name`
  (examiner), `articles` (statutes cited), and `body_text`. The
  `document_code` is empty — JPO mails docs use `document_name` for
  classification.

`binary_attachments` lists filenames of any non-XML / non-HTM files
in the archive (the parser doesn't decode them; fetch the raw ZIP if
you need them).

## Status codes and error handling

The API returns a `result.statusCode` on every JSON response:

| Code | Meaning | Client behaviour |
|------|---------|------------------|
| 100 | Success | Returns the parsed model |
| 107 | No data for query | Returns `None` / `[]` / `{}` |
| 108 | No document body | Returns empty bundle |
| 111 | Number out of scope | Returns `None` / `[]` / `{}` |
| 203 | Daily limit exceeded | Raises `RateLimitError` |
| 204 | Bad parameter | Raises `ApiError` |
| 208 | Invalid characters in parameter | Raises `ApiError` |
| 210 | Invalid token | Raises `AuthenticationError` (auto-retries once) |
| 212 | Invalid auth credentials | Raises `AuthenticationError` |
| 301 | URL not found | Raises `NotFoundError` |
| 302 / 999 | Server error / timeout | Raises `ApiError` |
| 303 | Concentrated access (transient) | Raises `RateLimitError` — back off and retry |
| 400 | Invalid request | Raises `ApiError` |

For HTTP-level errors, vanilla httpx exceptions propagate (with the
exception of HTTP 429 which becomes `RateLimitError`).

## Quirks worth knowing

- **`case_number_reference` and `pct_national_phase_application_number`
  use descriptive `kind` strings**, not the numeric `NumberType` codes.
  Pass `CaseNumberKind.APPLICATION` (= "application") for the former
  and `PctKind.INTERNATIONAL_APPLICATION` (= "international_application")
  for the latter. The numeric `NumberType` enum (01-12) is for the
  `numberType` field *inside* `bibliographyInformation` rows.
- **`applicant_attorney/{name}` requires an exact match** — partial
  queries return status 107.
- **Document endpoints return raw ZIP bytes**, not JSON. Patents ship
  XML, designs and trademarks ship HTM (handbook v14 §2(1)). Both
  formats are **Shift-JIS encoded** (not UTF-8); the
  `parse_document_bundle` helper decodes both for you, but if you walk
  the ZIP yourself decode each entry with `raw.decode("shift_jis")`
  (cp932 as a tolerant fallback).
- **Document bundles are only available for filings after January
  2019** — matches J-PlatPat's search scope. Older applications still
  surface metadata via `app_progress`, but `app_doc_cont_*` returns
  empty bundles for them.
- **`jpp_fixed_address` returns the URL under key `URL`**, not
  `jplatpatUrl` (the OpenAPI spec is wrong).
- **`cite_doc_info` returns `patentDoc` and `nonPatentDoc` as arrays**,
  not the singleton objects the OpenAPI spec describes.
- **`applicant_attorney_cd` returns a single name string**
  (`applicantAttorneyName`), not a list.
- **`case_number_reference` returns a single object**, not a list.
- The MCP `get_jpo_documents` tool returns parsed entries **and**
  dual-transport download handles for the raw ZIP (HMAC-signed
  `download_url` + `pca://jpo/documents/...` `resource_uri`). Agents
  that need binaries the parser doesn't surface should follow either
  transport; CoWork-style sandboxed agents follow `resource_uri` via
  `resources/read`, URL-comfortable clients follow `download_url`
  over HTTPS.
