# Online Sources — Canonical URLs for Agent Fetching

This catalog lists stable, agent-friendly URLs for the primary sources
this plugin cites. **The goal is to fetch current rule and statute text
at drafting time** rather than relying on potentially-stale copies in
the reference files. The reference files in this plugin are
interpretive aids; when quoting or citing specific subsections in a
filing, fetch from the canonical source and confirm the text.

> **For programmatic / structured lookup**, see the companion
> [`legal-data-apis.md`](./legal-data-apis.md) — covers the USLM
> XML release-point downloads, the eCFR Versioner XML/JSON API, and
> the CourtListener REST API for case-law lookup and citation
> verification. Prefer those APIs when an agent needs machine-readable
> output (cite-checking, bulk extraction, change detection).

## How to use this file

When a drafting skill needs the current text of a rule, statute, or
regulation:

1. Find the right canonical URL pattern in the tables below
2. Fetch the current text (via WebFetch or equivalent)
3. Quote from the fetched text in the filing
4. If the fetched text differs from what this plugin's references say,
   **trust the fetched text** and flag the discrepancy to the user

These URL patterns have been selected for **stability** (do not change
over time), **cleanness** (HTML not JavaScript-rendered where
possible), and **deep-linkability** (direct to the section, not the
landing page).

## Washington Court Rules

Base: `https://www.courts.wa.gov/court_rules/`

| Rule set | Purpose | Deep-link pattern |
|----------|---------|-------------------|
| CR | Civil Rules (Superior Court) | `?fa=court_rules.display&group=sup&set=CR&ruleid=supcr[NN]` |
| CRLJ | Civil Rules for Courts of Limited Jurisdiction (District / Municipal) | `?fa=court_rules.display&group=clj&set=CRLJ&ruleid=cljcrlj[NN]` |
| ER | Evidence Rules | `?fa=court_rules.display&group=ga&set=ER&ruleid=gaer[NNNN]` |
| GR | General Rules | `?fa=court_rules.display&group=ga&set=GR&ruleid=gagr[NN]` |
| RAP | Rules of Appellate Procedure | `?fa=court_rules.display&group=app&set=RAP&ruleid=apprap[NN].[NN]` |
| RPC | Rules of Professional Conduct | `?fa=court_rules.display&group=ga&set=RPC&ruleid=garpc[N].[N]` |

Examples:

- **CR 26** (discovery scope and limits):
  `https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=sup&set=CR&ruleid=supcr26`
- **CRLJ 26** (KCDC discovery):
  `https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=clj&set=CRLJ&ruleid=cljcrlj26`
- **ER 803** (hearsay exceptions):
  `https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=ER&ruleid=gaer0803`
- **GR 14** (format of pleadings):
  `https://www.courts.wa.gov/court_rules/?fa=court_rules.display&group=ga&set=GR&ruleid=gagr14`

**Reliability note**: courts.wa.gov is the official Washington Courts
site. URLs have been stable for many years. HTML is clean and
scrapable. If a URL 404s, drop back to the rule-set landing page and
search for the rule number.

## Washington Statutes (RCW)

Base: `https://app.leg.wa.gov/RCW/`

| Pattern | Example |
|---------|---------|
| Title page | `https://app.leg.wa.gov/RCW/default.aspx?cite=4.16` |
| Section page | `https://app.leg.wa.gov/RCW/default.aspx?cite=4.16.040` |
| Subsection (anchor) | `https://app.leg.wa.gov/RCW/default.aspx?cite=19.16.250#(12)` |

Frequently-needed general-civil cites:

- **RCW 4.16** (statutes of limitations — subject-matter skills
  provide the applicable subsection)
- **RCW 4.84** (costs and attorney fees)
- **RCW 4.84.330** (reciprocal fee-shifting)
- **RCW 6.27** (garnishment)
- **RCW 9A.72.085** (declarations under penalty of perjury)
- **RCW 1.16.050** (legal holidays, used in CR 6 time
  computation)

Subject-matter-specific RCW cites (e.g., RCW 19.16 Collection
Agency Act, RCW 19.86 Consumer Protection Act, RCW 62A.9A UCC
Article 9) live in the relevant subject-matter skill (e.g.,
`wa-consumer-debt/references/online-sources-consumer-debt.md`).

**Reliability note**: leg.wa.gov is authoritative. The URL has been
stable since 2010+. Section pages include a "history of" link showing
the legislative history — useful for spotting recent amendments.

## Federal Regulations — general pattern

Base: `https://www.ecfr.gov/current/`

URL pattern for a specific section:

> `https://www.ecfr.gov/current/title-[N]/chapter-[X]/subchapter-[Y]/part-[NNNN]/subpart-[Z]/section-[NNNN.NN]`

**Reliability note**: eCFR is the official, real-time Code of Federal
Regulations. "Current" URLs always show the version in force today.
For historical versions, use `past/YYYY-MM-DD` in place of `current`.

Subject-matter skills catalog the specific CFR parts relevant to
them (e.g., `wa-consumer-debt/references/online-sources-consumer-debt.md`
for Regulation F).

## Federal Statutes — general pattern

Primary official source:

- `https://www.govinfo.gov/app/collection/uscode/title-[N]` (U.S.
  Code on govinfo)

Scrape-friendly mirror (Cornell LII):

- `https://www.law.cornell.edu/uscode/text/[title]/[section]`

**Reliability note**: Cornell LII is not the official U.S. Code, but
the text is accurate and regularly updated. Use it for *reading*;
cite the U.S. Code when filing.

Subject-matter skills catalog specific federal statutes relevant to
their subject (e.g., `wa-consumer-debt/references/online-sources-consumer-debt.md`
for the FDCPA, 15 U.S.C. § 1692 et seq.).

## Case Law

### Washington appellate opinions

Official: `https://www.courts.wa.gov/opinions/`

Search interface exists but is not deep-linkable by case name. Better
for agents:

- **CourtListener** — free, API-accessible, stable per-case URLs:
  `https://www.courtlistener.com/opinion/[ID]/[slug]/`
- **Google Scholar** (case law tab):
  `https://scholar.google.com/scholar_case?case=[case_id]` — stable
  once discovered

Suggested fetch order:

1. CourtListener first (cleanest HTML, API option)
2. Google Scholar as fallback
3. courts.wa.gov for a cite-check against the official reporter

### Federal opinions

- **CourtListener** as above (covers federal too)
- **Ninth Circuit** opinions:
  `https://www.ca9.uscourts.gov/opinions/` — official
- **PACER** (paywalled; avoid unless user explicitly authorizes)

## King County District Court (KCDC)

Canonical operational URL for KCDC civil filings:

- `https://kingcounty.gov/en/court/district-court/courts-jails-legal-system/civil-filings`

What to fetch there:

- Current Note for Motion Docket form (per division)
- Civil motion calendar / hearing days
- Zoom meeting IDs, dial-in numbers, tech-support contact
- Division courtroom assignments (e.g., Burien, Redmond, Seattle)
- Document codes for e-filing
- CivilMGT email address for hearing-date reservations

**Reliability note**: the KCDC civil-filings page is updated when
divisions change procedures. Always fetch for the most recent Note
form and Zoom connection details before preparing a filing.

## King County Local Rules

- **KCLCR** (Superior Court local civil rules):
  `https://kingcounty.gov/en/court/superior-court/courts-jails-legal-system/resources-research/local-rules`
- **KCDCLCR** (District Court local civil rules):
  Navigate from
  `https://kingcounty.gov/en/court/district-court/courts-jails-legal-system`
  to "Local Rules" for the district court (the specific path is
  subject to the county's navigation rearrangements; fetch the
  district-court landing page and follow the "local rules" link).

## Subject-matter agency resources

Subject-matter skills catalog the regulator resources relevant to
their subject (CFPB and FTC for consumer finance; HUD for tenancy;
EEOC for employment; etc.). See the subject-matter skill's own
online-sources reference for specifics — e.g.,
`wa-consumer-debt/references/online-sources-consumer-debt.md`.

## Fetching strategy notes for the agent

- **Prefer one source at a time**: fetch, read, decide whether you
  have what you need before fetching another
- **Official over mirror** when citing; mirror over official when
  *reading for comprehension* (mirrors are usually cleaner HTML)
- **Confirm the version/effective-date** on any regulation or rule
  fetched — rules are amended; statutes are amended; cases can be
  superseded
- **Note in the filing** if a rule number has changed recently — a
  judge appreciates knowing "formerly CR 26(i), renumbered 2022" and
  so forth
- **Do not fetch paywalled content** (PACER, Westlaw, Lexis) unless
  the user explicitly authorizes a specific lookup they will pay for

## When a canonical source is unavailable

If WebFetch fails for a canonical URL:

1. Do **not** try an alternative non-canonical fetch method
2. Tell the user the fetch failed and what URL was attempted
3. Fall back to the inline content in this plugin's references
4. Flag explicitly in the filing draft that the citation was not
   verified against the canonical source
