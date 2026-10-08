# Legal Data APIs — Machine-Readable Sources

Companion to `online-sources.md`. That file lists **canonical URLs for human reading**. This file lists **structured APIs** an agent can hit when looking up or fact-checking law programmatically — official, free, and stable enough to script against.

Every API listed here was either used in `scripts/pull_*.py` to build the `references/` corpus or has been verified to return useful data for legal lookup. None require API keys unless noted.

## When to use these APIs

| Need | Best API | Why |
|---|---|---|
| Verbatim text of a federal statute (USC) | uscode.house.gov USLM XML | Official OLRC publication; structured XML; bulk download |
| Verbatim text of a federal regulation (CFR) | eCFR Versioner API | Official; per-Part XML; date-anchored |
| Federal case law / dockets | CourtListener REST API | Free; full text + metadata; covers all federal courts |
| WA appellate opinions (modern) | CourtListener API (filter by court) | Official site has no API; CL covers WA Supreme + COA |
| Bulk historical case law (pre-2020) | Caselaw Access Project (case.law) | Harvard's full digitization, free, no auth, every reporter |
| PACER docket data (free where available) | CourtListener / RECAP archive | Free mirror of PACER docs others have already paid for |
| WA RCW (statute text) | app.leg.wa.gov HTML scrape | No public API; HTML is stable |
| WA court rules | courts.wa.gov PDFs | No public API; PDFs are stable |
| Model UCC | law.cornell.edu HTML scrape | No public API |
| Cross-checking a citation | CourtListener Citation Lookup API | Returns the case text given any citation format |

## 1. uscode.house.gov — USLM XML (federal statutes)

**Source of truth** for the U.S. Code, published by the Office of the Law Revision Counsel. Updated at each new "release point" (new public law).

### Discovering the current release point

The releasepoints index page lists the latest:

```
GET https://uscode.house.gov/download/download.shtml
```

Look for "Current Release Point: Public Law NNN-NN" near the top. The release point is two numbers: `<congress>-<law>`.

### Bulk download a title

```
GET https://uscode.house.gov/download/releasepoints/us/pl/<congress>/<law>/xml_usc<title>@<congress>-<law>.zip
```

Example (Title 15, current as of release 119-84):

```
https://uscode.house.gov/download/releasepoints/us/pl/119/84/xml_usc15@119-84.zip
```

The zip contains a single `usc<NN>.xml` file in **USLM 1.0 schema** (XML namespace `http://xml.house.gov/schemas/uslm/1.0`).

### USLM structure crash course

```xml
<title identifier="/us/usc/t15">
  <chapter identifier="/us/usc/t15/ch41">
    <subchapter identifier="/us/usc/t15/ch41/schV">  <!-- FDCPA -->
      <section identifier="/us/usc/t15/s1692">
        <num value="1692">§ 1692.</num>
        <heading>Congressional findings…</heading>
        <subsection><num>(a)</num><heading>…</heading><chapeau>…</chapeau>…</subsection>
        …
      </section>
    </subchapter>
  </chapter>
</title>
```

Every `<num>`, `<heading>`, `<chapeau>`, `<subsection>`, `<paragraph>`, `<subparagraph>`, `<clause>` is consistent across all titles. Parse with `xml.etree.ElementTree`.

### Reference implementation

`scripts/pull_federal_debt_laws.py` — function `get_usc15_xml()` downloads, `render_subchapter()` walks the tree to Markdown.

## 2. ecfr.gov — Versioner API (federal regulations)

Official, real-time Code of Federal Regulations. Returns structured XML for any Part, anchored to a date.

### Endpoints

```
# Full Part as XML (use this for verbatim regulation text)
GET https://www.ecfr.gov/api/versioner/v1/full/{date}/title-{title}.xml?part={part}

# All amendment versions of a Part as JSON (use to detect changes)
GET https://www.ecfr.gov/api/versioner/v1/versions/title-{title}.json?part={part}

# Structure (TOC) only
GET https://www.ecfr.gov/api/versioner/v1/structure/{date}/title-{title}.json?part={part}

# Search across the entire eCFR
GET https://www.ecfr.gov/api/search/v1/results?query={query}&hierarchy[title]={title}
```

`{date}` is YYYY-MM-DD; the API returns the version in force on that date. Use `date.today().isoformat()` for "now," or pin a date for reproducible output.

### Common parts for debt-collection cases

| Part | Reg | Implements |
|---|---|---|
| 12 CFR 1006 | Reg F | FDCPA |
| 12 CFR 1022 | Reg V | FCRA |
| 12 CFR 1026 | Reg Z | TILA |
| 12 CFR 1002 | Reg B | ECOA |

### Reference implementation

`scripts/pull_federal_debt_laws.py` — function `fetch_cfr_part_xml()` and `render_cfr_part()`.

## 3. Case law — three complementary sources

There are three good free programmatic sources for case law. Use them together: each has a sweet spot.

| Source | Best for | Format | Auth |
|---|---|---|---|
| **CourtListener REST API** | citation lookup, full-text search, recent cases, federal dockets | JSON | optional |
| **Caselaw Access Project (CAP)** | bulk historical case law (1658–2020), every published US case | bulk static (JSON/PDF/TAR per volume) | none |
| **Justia / FindLaw / Google Scholar** | quick HTML lookup when an API would be overkill | HTML | none |

**Decision rule:**
- *"Is this cite real and what does it say?"* → CourtListener `citation-lookup`
- *"Give me every WA Supreme Court opinion from 1995–2020"* → CAP bulk
- *"What are the recent FDCPA cases out of W.D. Wash.?"* → CourtListener search
- *"Just paste the opinion text into a brief"* → CourtListener cluster API or CAP per-case JSON

### 3a. CourtListener REST API

Free Software Foundation–hosted, run by the Free Law Project. The single best programmatic source for federal case law and an excellent source for state appellate cases (covers all 50 states' courts of last resort and most intermediate appellate courts).

### Base

```
https://www.courtlistener.com/api/rest/v3/
```

API key is **optional** (anonymous = ~5,000 req/hour). For higher limits register at https://www.courtlistener.com/help/api/rest/ and put the token in `Authorization: Token {key}`.

### Most useful endpoints for fact-checking

```
# Citation lookup — give it a cite, get back the case
POST https://www.courtlistener.com/api/rest/v3/citation-lookup/
Content-Type: application/json
{"text": "199 Wn.2d 1, 502 P.3d 339 (2022)"}

# Search opinions
GET https://www.courtlistener.com/api/rest/v3/search/?type=o&q=Bain+v+Metropolitan&court=washsc

# Get a specific opinion's text
GET https://www.courtlistener.com/api/rest/v3/opinions/{id}/

# Get the cluster (case-level metadata + all sub-opinions)
GET https://www.courtlistener.com/api/rest/v3/clusters/{id}/

# Filter by court (Washington courts: court=washsc, washctapp)
GET https://www.courtlistener.com/api/rest/v3/search/?type=o&court=washsc&q=...
```

### Court IDs of interest (WA + relevant federal)

| Court | court ID |
|---|---|
| WA Supreme Court | `washsc` |
| WA Court of Appeals | `washctapp` |
| US Supreme Court | `scotus` |
| US Court of Appeals, 9th Circuit | `ca9` |
| US District Court, W.D. Wash. | `wawd` |

Full list: `GET https://www.courtlistener.com/api/rest/v3/courts/?jurisdiction=S` (states) or `=F` (federal).

### When to prefer CourtListener over Google Scholar

- You need machine-readable JSON, not HTML
- You need stable, parseable citations (CL returns all parallel citations)
- You're cite-checking many cites at once
- You need full-text search

### Reference implementation

Not yet wired into a script in this repo, but the citation-lookup endpoint is the cleanest path for `wa-fact-check` to verify any cite in a brief.

### 3b. Caselaw Access Project (CAP) — case.law

Harvard Law School's digitization of every published US case from 1658 to 2020. **Went fully open in March 2024** — no API key, no rate limit, fully redistributable. Hosted as static files on Cloudflare R2 at `static.case.law`.

**Coverage:** ~6.7 million cases, 360 years. Every state and federal reporter Harvard could lay hands on. Stops at 2020 — for newer cases, use CourtListener.

#### Discovering volumes

Three top-level metadata files:

```
GET https://static.case.law/ReportersMetadata.json     # all reporters (slug, name, jurisdiction)
GET https://static.case.law/VolumesMetadata.json       # every volume of every reporter
GET https://static.case.law/JurisdictionsMetadata.json # every jurisdiction
```

#### Per-volume access

For each `(reporter_slug, volume_number)`:

```
# Browseable HTML index of cases in that volume
https://static.case.law/<reporter>/<volume>/

# All cases in the volume as a zip of JSON files (richest format)
https://static.case.law/<reporter>/<volume>.zip

# Same content as a tar
https://static.case.law/<reporter>/<volume>.tar

# CSV index of what's inside the tar
https://static.case.law/<reporter>/<volume>.tar.csv

# Original digitized PDF of the bound volume
https://static.case.law/<reporter>/<volume>.pdf
```

#### Useful reporter slugs for this repo

| Slug | Reporter |
|---|---|
| `wash` | Washington Reports (1st series) |
| `wash-2d` | Washington Reports, 2d Series |
| `wash-app` | Washington Appellate Reports |
| `wash-terr` | Washington Territory Reports |
| `p2d` / `p3d` | Pacific Reporter (2d / 3d) |
| `us` | U.S. Reports (Supreme Court) |
| `s-ct` | Supreme Court Reporter |
| `f` / `f2d` / `f3d` | Federal Reporter |
| `f-supp` / `f-supp-2d` / `f-supp-3d` | Federal Supplement |

#### Per-case JSON shape

Inside `<volume>.zip` each case is a JSON file with: `name`, `name_abbreviation`, `decision_date`, `docket_number`, `first_page` / `last_page`, `citations`, `court`, `jurisdiction`, `casebody.opinions[]` (with `text`, `author`, `type`).

#### When to choose CAP over CourtListener

- You want **bulk** download (whole reporter, whole jurisdiction)
- You want **historical** cases (CL coverage thins for older opinions)
- You don't want any rate limit or auth
- You want the original **PDF scan** alongside the OCR text

#### When NOT to use CAP

- Cases after **2020** (use CourtListener)
- You need **case-name search** (CAP is volume-organized, not searchable; you need to know the citation already, or scan the metadata)
- Federal **dockets** (use CourtListener / RECAP)

### 3c. RECAP — federal docket data via CourtListener

[RECAP](https://free.law/recap/) is the Free Law Project's free archive of PACER documents. PACER itself charges per-page fees; RECAP holds the documents people have already paid for, mirrored for free.

Access RECAP through the same CourtListener API:

```
# Search PACER docs in RECAP
GET https://www.courtlistener.com/api/rest/v3/search/?type=r&q=...

# Get a docket
GET https://www.courtlistener.com/api/rest/v3/dockets/{id}/

# Get a docket entry's documents
GET https://www.courtlistener.com/api/rest/v3/recap-documents/?docket_entry={id}
```

For documents not yet in RECAP, you can pay PACER per page (1¢/page, $3 cap per document) — but for fact-checking purposes, what's already in RECAP usually suffices.

## 4. govinfo.gov — Federal Register / USC / CFR fallback

Run by GPO. Slower-moving than uscode.house.gov for USC and ecfr.gov for CFR, but **adds the Federal Register** which is where new CFR amendments first publish.

```
# Federal Register issues
GET https://api.govinfo.gov/collections/FR/{startDate}/{endDate}?api_key={key}

# Search across all collections
GET https://api.govinfo.gov/search?api_key={key}
```

API key is **required** (free at https://api.data.gov/signup/).

Use cases:
- Finding the latest CFR amendments before they appear in eCFR (~24 hour lag)
- Pulling agency guidance documents (CFPB advisories, FTC opinion letters)
- Bulk operations across the entire FR

## 5. Washington-specific lookups (no formal APIs)

These have no public APIs but stable HTML structures suitable for lightweight scraping:

| Source | URL pattern | What to expect |
|---|---|---|
| RCW chapter | `https://app.leg.wa.gov/RCW/default.aspx?cite=<chapter>` | Chapter caption + section table |
| RCW section | `https://app.leg.wa.gov/RCW/default.aspx?cite=<chapter>.<section>` | Section text + history + notes |
| WA court rule (HTML) | `https://www.courts.wa.gov/court_rules/?fa=court_rules.list&group=<group>&set=<set>` | Lists rules; each row links to a PDF |
| WA court rule (PDF) | `https://www.courts.wa.gov/court_rules/pdf/<set>/<filename>.pdf` | Verbatim rule text |
| WA appellate opinion (PDF) | `https://www.courts.wa.gov/opinions/pdf/<filename>.pdf` | Verbatim opinion (date-stamped filename, not stable for arbitrary lookup) |

Reference implementations: `scripts/pull_wa_rcw.py`, `scripts/pull_court_rules.py`.

## 6. Cornell Legal Information Institute (LII) — HTML mirror

No API, but Cornell's HTML is the cleanest free mirror of the USC, CFR, and model UCC. Useful for human reading; not authoritative for citation.

| Source | URL pattern |
|---|---|
| USC section | `https://www.law.cornell.edu/uscode/text/<title>/<section>` |
| CFR section | `https://www.law.cornell.edu/cfr/text/<title>/<part>.<section>` |
| Model UCC | `https://www.law.cornell.edu/ucc/<article>/<article>-<section>` |
| WA appellate cases | `https://www.law.cornell.edu/wa/...` (limited; prefer CourtListener) |

Reference implementation: `scripts/pull_ucc.py`.

## Etiquette

These services are free and run on government / non-profit infrastructure. To stay welcome:

- **Send a User-Agent string identifying yourself** (e.g., `claude-legal/1.0 (+url) <purpose>`). All four scripts in `scripts/pull_*.py` do this.
- **Cap concurrency at ~12 workers** when scraping (the four pullers default to 8–12).
- **Cache aggressively** when iterating. The federal puller caches the USC zip in `/tmp/claude-legal-cache/` so repeated runs don't re-download 30 MB.
- **Back off on 5xx**. Don't hammer if a service is having a bad day; retry with exponential delay.
- **Don't scrape PACER** without explicit user authorization (it's paywalled per page; CourtListener's RECAP archive has most of it for free).

## Quick-reference: which API for which question

> "What does 15 U.S.C. § 1692c actually say?"
> → `xml_usc15@<release>.zip` from uscode.house.gov, or for a one-off, `https://www.law.cornell.edu/uscode/text/15/1692c`.

> "What does 12 C.F.R. § 1006.6 actually say?"
> → `https://www.ecfr.gov/api/versioner/v1/full/<today>/title-12.xml?part=1006`.

> "Is *Bain v. Metropolitan Mortgage*, 175 Wn.2d 83 (2012), a real case and is the holding I'm citing accurate?"
> → CourtListener citation-lookup: `POST /api/rest/v3/citation-lookup/` with `{"text": "175 Wn.2d 83 (2012)"}`. Returns the case URL + opinion text.
> → For the original-volume PDF: `https://static.case.law/wash-2d/175.pdf`.

> "Give me every Washington Court of Appeals opinion from 2018 — bulk."
> → CAP: walk `https://static.case.law/wash-app/`, download per-volume `.zip` for the volumes covering 2018, parse the JSON cases.

> "What's been filed in *Smith v. Jones*, 2:24-cv-01234, W.D. Wash. lately?"
> → CourtListener docket: `GET /api/rest/v3/dockets/?court=wawd&docket_number=24-cv-01234`. Then iterate `recap-documents` for the entries.

> "Has CR 26 changed since 2024?"
> → Fetch `https://www.courts.wa.gov/court_rules/pdf/CR/SUP_CR_26_00_00.pdf`; the bottom of the rule lists adoption + amendment dates.

> "What's the current statute of limitations on accounts receivable in Washington?"
> → `https://app.leg.wa.gov/RCW/default.aspx?cite=4.16.040` (subsection (2) — six years).

> "Did the CFPB just amend Reg F?"
> → eCFR versions endpoint: `GET https://www.ecfr.gov/api/versioner/v1/versions/title-12.json?part=1006`. Latest entry's `amendment_date` is the most recent change.

## Refresh & verify

- `scripts/pull_court_rules.py` — refreshes WA court rules
- `scripts/pull_federal_debt_laws.py` — refreshes USC + CFR (statutes/regs)
- `scripts/pull_ucc.py` — refreshes model UCC
- `scripts/pull_wa_rcw.py` — refreshes WA RCW

These are the same four scripts the quarterly remote agent runs; see `routine: trig_018yahbiUwS1uTUJSuDNrCqG` for the schedule.
