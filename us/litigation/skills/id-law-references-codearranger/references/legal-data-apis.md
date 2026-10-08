# Idaho law — programmatic / data-API access (agent-facing)

> **NOT LEGAL ADVICE.** Integration notes for retrieving Idaho legal text
> programmatically. Always confirm currency and that you are reading the
> authoritative version before relying on retrieved text.

This is the agent-facing index of how to fetch Idaho statutes, rules, and
opinions programmatically — the companion to the human-facing
`online-sources.md`.

## Idaho Code — legislature.idaho.gov

- **Section pages** are stable, parseable HTML at predictable paths:
  - Pattern:
    `https://legislature.idaho.gov/statutesrules/idstat/title<title>/t<title>ch<chapter>/sect<section>/`
  - Example (I.C. § 5-216, Title 5 ch. 2):
    `https://legislature.idaho.gov/statutesrules/idstat/Title5/T5CH2/SECT5-216/`
  - The chapter index pages list every section in the chapter — useful for
    enumerating a chapter for a bulk pull.
- Fetch strategy: pull the title/chapter index, enumerate the section URLs,
  fetch each section page, and extract the statute body. Use polite rate
  limiting and atomic writes (mirrors the pull-script discipline used for the
  other corpora in this marketplace). A future `scripts/pull_idaho_statutes.py`
  drives the `id-statutes-debt/` corpus.

## Court rules — isc.idaho.gov

- The Idaho Rules of Civil Procedure, Rules of Evidence, Rules of Family Law
  Procedure, Appellate Rules, and the electronic-filing rules are published on
  the **Idaho Supreme Court (isc.idaho.gov)** rules pages.
  - Per-rule print pattern: `https://isc.idaho.gov/rules-procedure/print/ircp/<n>`
  - Per-rule "new" pattern: `https://isc.idaho.gov/ircp<n>-new`
  - Rule-set landing pages: `https://isc.idaho.gov/rules-procedure/irefs`
    (electronic filing), `https://isc.idaho.gov/rules-procedure/irfl` (family
    law), `https://isc.idaho.gov/rules-procedure/ire` (evidence).
- There is no single clean JSON API; retrieval is HTML scraping of the rules
  pages. Check the rules-amendment / pending-order pages before treating a
  fetched rule as current. A future `scripts/pull_idaho_rules.py` drives the
  `court-rules/` corpus.

## Case law — CourtListener (Free Law Project)

CourtListener is the primary programmatic source for Idaho opinions.

- **Court identifiers (the `court` field):**
  - **Idaho Supreme Court** → **`idaho`**
  - **Idaho Court of Appeals** → **`idahoctapp`**
  - (Confirm the exact court slugs against the CourtListener `/courts/`
    endpoint before a bulk query.)
- **REST API v4** (key recommended for volume):
  - Opinions / clusters / search endpoints under
    `https://www.courtlistener.com/api/rest/v4/`.
  - Filter by court (e.g. `?court=idaho`) plus date and citation filters.
  - The **citation-lookup** endpoint resolves a reporter citation (e.g.,
    `113 Idaho 730`) to a CourtListener cluster — use it to verify the cases
    in `key-cases.md`.

## Bundled MCP servers — CourtListener + Legal Data Hunter

The shared **`claude-legal-federal-laws`** plugin bundles two free MCP servers
(see its `.mcp.json`): **CourtListener** and **Legal Data Hunter**. When these
are connected in the environment, **prefer them** for on-demand Idaho case-law
lookup, citation verification, and full-text opinion retrieval (Idaho Supreme
Court and Court of Appeals). They are the recommended path for resolving and
confirming any citation in `key-cases.md` before relying on it. The
`case-law-research` skill in that shared plugin drives these servers.

## Idaho Department of Finance — collection-agency licensing

- The **Idaho Department of Finance** (finance.idaho.gov) administers the
  **Idaho Collection Agency Act** (I.C. § 26-2222 et seq.) and the Idaho
  Credit Code. Its site publishes licensee lookups and regulatory guidance —
  useful for verifying whether a collector/debt buyer is licensed
  (I.C. § 26-2223). Treat the licensee search as a finding aid; confirm
  current status with the Department.

## Verification workflow

1. **Statute** — fetch the legislature.idaho.gov section page; confirm the
   section number and effective date; cite as `I.C. § ...`.
2. **Rule** — fetch the isc.idaho.gov rule page; check for a pending
   amendment; cite as `I.R.C.P. ...`, `I.R.E. ...`, `I.R.F.L.P. ...`, or
   `I.A.R. ...`.
3. **Case** — resolve via CourtListener (MCP or REST), confirm the parallel
   `Idaho` + `P.2d`/`P.3d` cite and the court/year, and check that the opinion
   has not been overruled or superseded; cite per `citation-format.md`.

## Cross-references

- Human-facing URLs for the same sources: `online-sources.md`.
- Citation format for retrieved authority: `citation-format.md`.
- Cases to verify with these tools: `key-cases.md`.
