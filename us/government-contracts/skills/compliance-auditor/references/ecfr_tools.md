# eCFR MCP Tool Reference (curated for compliance-auditor)

The vendored `ecfr` MCP exposes 13 read-only tools over the live eCFR API
(no API key). Compliance-auditor only needs the four tools below — load
the rest on demand via `mcp__ecfr__<name>` if a workflow step calls for
them.

## Critical caveat from upstream

eCFR **lags 1–2 business days behind the Federal Register**. When a
clause was amended yesterday the version may not yet be live in eCFR.
Treat C10 (currency) findings as advisory, not authoritative.

## Curated tool whitelist

| Tool                              | Purpose                                                                                                          | Used by check |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------- |
| `mcp__ecfr__lookup_far_clause`    | Resolve a FAR/DFARS section identifier (e.g. `52.212-4`, `15.305`, `2.101`) to current text. Returns 404 if the clause does not exist. | **C9** |
| `mcp__ecfr__get_version_history`  | Version history of a CFR section/part. Returns dated content versions with amendment info.                       | **C10** |
| `mcp__ecfr__compare_versions`     | Diff a CFR section between two dates. Useful when C10 needs to show *what* changed.                              | C10 (drill-in) |
| `mcp__ecfr__find_far_definition`  | Search FAR 2.101 master definition section for a term. Optional enrichment for ambiguous requirement language.   | ad hoc        |

## Tool-call shape

`lookup_far_clause` request:

```json
{ "section_id": "52.212-4" }
```

Defaults to the latest available date. Pass `date: "YYYY-MM-DD"` only
when comparing against a historical snapshot (e.g. for C10 comparison
against the solicitation issuance date).

`get_version_history` request:

```json
{ "title": 48, "section_id": "52.212-4" }
```

Returns a list ordered most-recent-first. The first element's `date` is
the most-recent amendment date.

## Clause-number normalization

Workspace `clause` entities frequently carry messy strings — strip
prefixes like `FAR`, `DFARS`, leading parentheses, and trailing
sub-paragraphs before calling `lookup_far_clause`. Examples:

| Workspace text                       | Normalized `section_id` |
| ------------------------------------ | ----------------------- |
| `FAR 52.212-4(a)(1)`                 | `52.212-4`              |
| `DFARS 252.204-7012`                 | `252.204-7012`          |
| `FAR Subpart 15.3`                   | `15.305` (no — Subpart, skip — only call on resolvable section identifiers) |
| `52.222-50 — Combating Trafficking…` | `52.222-50`             |

If a clause string cannot be reduced to a `^\d{1,3}\.\d{3,4}(-\d+)?$`
shape, **skip** it for C9 — the entity isn't a clause section, it's a
subpart/part header, and `lookup_far_clause` will return a confusing
result. Emit an `info` finding noting the skip rather than a false
positive.

## When eCFR is not available

If `mcp__ecfr__*` tools are not exposed to this run (e.g. the runtime
allowlist excluded it, or the manifest was removed), C9 and C10 are
**deferred** — emit one `info` finding per check naming the deferral
and proceed with C1–C8. Do not fabricate clause-existence verdicts
based on heuristics.
