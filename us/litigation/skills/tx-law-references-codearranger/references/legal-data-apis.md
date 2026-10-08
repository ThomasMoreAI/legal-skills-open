# Texas law — programmatic / data-API access (agent-facing)

> **NOT LEGAL ADVICE.** Integration notes for retrieving Texas legal text
> programmatically. Always confirm currency and that you are reading the
> authoritative version before relying on retrieved text.

This is the agent-facing index of how to fetch Texas statutes, rules, and
opinions programmatically — the companion to the human-facing
`online-sources.md`.

## Texas Statutes — statutes.capitol.texas.gov

- **Section and code pages** are stable, parseable HTML at predictable paths
  under `https://statutes.capitol.texas.gov/`. Each Texas code (Civil Practice
  & Remedies, Finance, Business & Commerce, Property, Government, Family, etc.)
  has chapter and section pages; the site also publishes **per-code PDF
  downloads** of the full code (useful for bulk pulls).
- Fetch strategy: pull the code's table of contents, enumerate the chapter and
  section URLs (or download the per-code PDF), and extract the statute body.
  Use polite rate limiting and atomic writes (mirrors the pull-script
  discipline used for the other corpora in this marketplace). A future
  `scripts/pull_tx_statutes.py` drives the `tx-statutes-debt/` corpus.
- Confirm the **effective date** on each section page — Texas codes are
  amended each biennial legislative session, so check that the version shown is
  the one currently in force.

## Court rules — txcourts.gov

- The **Texas Rules of Civil Procedure**, **Texas Rules of Evidence**, and
  **Texas Rules of Appellate Procedure** are published by the **Supreme Court
  of Texas** as **PDFs** on the Texas Judicial Branch site
  (`https://www.txcourts.gov/rules-forms/rules-standards/`).
- Retrieval is **PDF download + text extraction** (there is no clean JSON rules
  API). Check the **rule-amendments / miscellaneous-docket** pages for pending
  or recently adopted amendments before treating a fetched rule as current. A
  future `scripts/pull_tx_court_rules.py` drives the `court-rules/` corpus.

## Case law — CourtListener (Free Law Project)

CourtListener is the primary programmatic source for Texas opinions.

- **Court identifiers (the `court` field) — confirm exact slugs against the
  CourtListener `/courts/` endpoint before a bulk query:**
  - **Supreme Court of Texas** → typically **`tex`**
  - **Texas Court of Criminal Appeals** → typically **`texcrimapp`**
  - **Texas Courts of Appeals** → the intermediate courts have per-district
    slugs (e.g., `texapp1` … `texapp14`); enumerate them from the `/courts/`
    endpoint rather than guessing.
- **REST API v4** (key recommended for volume):
  - Opinions / clusters / search endpoints under
    `https://www.courtlistener.com/api/rest/v4/`.
  - Filter by court (e.g. `?court=tex`) plus date and citation filters.
  - The **citation-lookup** endpoint resolves a reporter citation (e.g.,
    `544 S.W.2d 367`) to a CourtListener cluster — use it to verify the cases
    in `key-cases.md`, **including the petition-history parenthetical** for
    Court of Appeals opinions.

## Bundled MCP servers — CourtListener + Legal Data Hunter

The shared **`claude-legal-federal-laws`** plugin bundles two free MCP servers
(see its `.mcp.json`): **CourtListener** and **Legal Data Hunter**. When these
are connected in the environment, **prefer them** for on-demand Texas case-law
lookup, citation verification, and full-text opinion retrieval (Supreme Court
of Texas, Court of Criminal Appeals, and the Texas Courts of Appeals). They are
the recommended path for resolving and confirming any citation in
`key-cases.md` before relying on it. The `case-law-research` skill in that
shared plugin drives these servers.

## Regulators — OCCC and the Secretary of State

- The **Office of Consumer Credit Commissioner** (`https://occc.texas.gov/`)
  publishes **licensee lookups** and complaint intake — useful for verifying a
  consumer-credit licensee's status. Treat the lookup as a finding aid; confirm
  current status with the agency.
- The **Texas Secretary of State** (`https://www.sos.state.tx.us/`) is the
  filing office for the **Tex. Fin. Code § 392.101** third-party debt
  collector / credit bureau **surety bond** — use it to check whether a
  third-party collector has filed the required $-amount bond (confirm the
  current bond amount against `tx-statutes-debt/`; **note Texas has no
  debt-collector licensing regime — § 392.101 is a bonding requirement, not a
  license**).

## Verification workflow

1. **Statute** — fetch the statutes.capitol.texas.gov section page; confirm the
   section number and **effective date**; cite as `Tex. <Code> § ...`.
2. **Rule** — fetch the txcourts.gov rule PDF; check the amendments page for a
   pending change; cite as `Tex. R. Civ. P. ...`, `Tex. R. Evid. ...`, or
   `Tex. R. App. P. ...`.
3. **Case** — resolve via CourtListener (MCP or REST), confirm the `S.W.2d` /
   `S.W.3d` cite, the court/year, the **petition history**, and that the
   opinion has not been overruled or superseded; cite per `citation-format.md`.

## Cross-references

- Human-facing URLs for the same sources: `online-sources.md`.
- Citation format for retrieved authority: `citation-format.md`.
- Cases to verify with these tools: `key-cases.md`.
