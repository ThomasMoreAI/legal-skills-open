# Arizona law — programmatic / data-API access (agent-facing)

> **NOT LEGAL ADVICE.** Integration notes for retrieving Arizona legal
> text programmatically. Always confirm currency and that you are reading
> the authoritative version before relying on retrieved text.

This is the agent-facing index of how to fetch Arizona statutes, rules,
and opinions programmatically — the companion to the human-facing
`online-sources.md`.

## Arizona Revised Statutes (A.R.S.) — azleg.gov

- **Section pages** are stable, parseable HTML at predictable paths:
  - Pattern: `https://www.azleg.gov/ars/<title>/<zero-padded-section>.htm`
  - Example: `https://www.azleg.gov/ars/25/00211.htm` (A.R.S. § 25-211);
    `https://www.azleg.gov/ars/12/00341-01.htm` (A.R.S. § 12-341.01 — confirm
    the exact slug, which encodes the decimal section number).
- **Title index**: `https://www.azleg.gov/arstitle/` lists every title and
  links to chapter/article/section pages — useful for enumerating the
  sections in a chapter for a bulk pull.
- Fetch strategy: pull the title index, walk the chapter/article links to
  enumerate section URLs, then fetch each section page and extract the
  statute body. Use polite rate limiting and atomic writes. (Mirrors the
  pull-script discipline used for the other corpora in this marketplace.)

## Court rules — azcourts.gov

- The Arizona Rules of Civil Procedure, Rules of Evidence, and Rules of
  Family Law Procedure are published on `https://www.azcourts.gov/rules`
  and in the official court-rules volumes. There is no single clean JSON
  API; retrieval is HTML/PDF scraping of the rules pages. Check the
  rules-forum / pending-amendments pages before treating a fetched rule as
  current.

## Case law — CourtListener (Free Law Project)

CourtListener is the primary programmatic source for Arizona opinions.

- **Court identifiers (the `court` field):**
  - **Arizona Supreme Court** → **`ariz`**
  - **Arizona Court of Appeals** → **`arizctapp`** (covers Division One
    and Division Two; filter by division within results where needed)
- **REST API v4** (key recommended for volume):
  - Opinions / clusters: `https://www.courtlistener.com/api/rest/v4/`
    (e.g., the `search`, `clusters`, and `opinions` endpoints).
  - Filter by court, e.g. `?court=ariz` or `?court=arizctapp`, plus
    date and citation filters.
  - Citation lookup: the **citation-lookup** endpoint resolves a
    reporter citation (e.g., `166 Ariz. 301`) to a CourtListener cluster
    — useful for verifying the cases in `key-cases.md`.
- **Connected CourtListener MCP** — when the CourtListener MCP server is
  authenticated in this environment, prefer it for case lookup,
  citation verification, and full-text retrieval of Arizona opinions
  (Supreme Court `ariz`, Court of Appeals `arizctapp`). It is the
  recommended path for resolving and verifying any citation in
  `key-cases.md` before relying on it.

## Verification workflow

1. **Statute** — fetch the azleg.gov section page; confirm the section
   number and effective date; cite as `A.R.S. § ...`.
2. **Rule** — fetch the azcourts.gov rule; check the rules-forum for a
   pending amendment; cite as `Ariz. R. Civ. P. ...`, `Ariz. R. Evid.
   ...`, or `ARFLP ...`.
3. **Case** — resolve via CourtListener (MCP or REST), confirm the
   parallel `Ariz.` + `P.2d`/`P.3d` cite and the court/year, and check
   that the opinion has not been overruled or superseded; cite per
   `citation-format.md`.

## Cross-references

- Human-facing URLs for the same sources: `online-sources.md`.
- Citation format for retrieved authority: `citation-format.md`.
- Cases to verify with these tools: `key-cases.md`.
