# Legal Data APIs — Oregon and Federal

The structured-data APIs below provide programmatic access to
Oregon law, federal law, court opinions, and federal court
filings. Prefer these APIs over HTML scraping when the result
will be parsed, indexed, or watched for change.

## Oregon Revised Statutes (ORS)

The Oregon Legislature publishes ORS as HTML pages by chapter.
There is no XML API like USLM, but the HTML is well-formed and
parseable.

### Pattern

```
https://www.oregonlegislature.gov/bills_laws/ors/ors[CHAPTER].html
```

Examples:
- ORS 12: ors012.html
- ORS 20: ors020.html
- ORS 18: ors018.html
- ORS 36: ors036.html
- ORS 40: ors040.html
- ORS 90: ors090.html
- ORS 187: ors187.html
- ORS 646: ors646.html
- ORS 697: ors697.html

### Parsing approach

Each chapter page lists section numbers as anchors. Section
text is in HTML tables; extract by walking the DOM. The
`scripts/pull_oregon_ors.py` script handles the extraction
(parallels the WA `pull_wa_rcw.py` pattern).

### Change detection

The legislature publishes the most recent legislative session's
amendments by the end of the year. Re-pull all relevant chapters
in **November** (after the regular session ends) and again in
**February** (after special sessions, if any).

## Oregon Rules of Civil Procedure (ORCP)

The Council on Court Procedures publishes the ORCP as a
consolidated PDF on a two-year cycle (effective January 1 of
odd-numbered years).

### URL

```
https://counciloncourtprocedures.org/wp-content/uploads/[YYYY]/ORCP.pdf
```

(Exact path varies; `scripts/pull_oregon_rules.py --target orcp`
uses the current PDF link from the CCP homepage.)

### Parsing approach

PDF text extraction via `pdfplumber` or `pymupdf`. Rules are
delimited by "RULE [N]" headers. Each rule has lettered
subsections (A, B, C); each subsection has numbered sub-
subsections in parentheses.

## Uniform Trial Court Rules (UTCR)

Published annually as PDF, effective August 1.

### URL

```
https://www.courts.oregon.gov/rules/UTCR/Documents/UTCR_[YYYY].pdf
```

### Parsing approach

Similar to ORCP — PDF text extraction with chapter / section
delimiters.

## Oregon Evidence Code (OEC)

Codified at ORS Ch. 40 — pulled via the same ORS HTML route.

## Federal law — USC

### USLM XML

The U.S. Code is published in **USLM (United States Legislative
Markup)** XML format:

```
https://uscode.house.gov/download/releasepoints/us/pl/[PL-NN]/usc[NN][a]@[release].xml
```

The current "release point" reflects the latest amendments
published. See https://uscode.house.gov/download/download.shtml.

### Relevant titles for civil practice

- **Title 15** — Commerce and Trade (FDCPA at § 1692; FCRA at
  § 1681; TILA at § 1601)
- **Title 11** — Bankruptcy
- **Title 28** — Judiciary and Judicial Procedure

### Parsing approach

USLM XML is structured and stable. The `scripts/pull_federal_
debt_laws.py` script (from the WA plugin) extracts FDCPA, FCRA,
TILA, ECOA, etc. The Oregon plugin can reuse this output rather
than re-pulling federal law.

## Federal regulations — eCFR

### eCFR Versioner API

```
https://www.ecfr.gov/api/versioner/v1/full/[YYYY-MM-DD]/title-[NN].xml
```

This API returns the CFR text as XML for any date in the past,
supporting **point-in-time** queries critical for verifying
the version of a regulation in effect at a particular event
date (FDCPA / Reg F enforcement actions, for example).

### Relevant titles

- **Title 12** — Banks and Banking (Reg F at part 1006; Reg Z;
  Reg B; Reg V)

### Parsing approach

eCFR XML follows the same DITA-ish structure as USLM. The
existing WA plugin's `pull_federal_debt_laws.py` handles
extraction.

## Court opinions — CourtListener API

### REST API

```
https://www.courtlistener.com/api/rest/v3/
```

Endpoints:

- `/courts/` — list of courts
- `/opinions/` — full-text opinions
- `/clusters/` — opinion clusters (parallel cites)
- `/search/` — full-text search

### Oregon court filters

- `court=or` — Oregon Supreme Court
- `court=orctapp` — Oregon Court of Appeals
- `court=ord` — District of Oregon (federal)
- `court=ca9` — 9th Circuit

### Authentication

Free tier: 100 requests/day without API key. Higher rate
limits with a free CourtListener account and API token.

### Use cases

- **Cite-checking**: paste a citation, get the matching
  opinion's metadata (verifies the case exists, the citation
  is correct, and what year)
- **Holding verification**: pull the opinion text and verify
  it stands for the proposition cited
- **Subsequent history**: check whether the case has been
  overruled or distinguished

## Caselaw Access Project (Harvard)

### API

```
https://api.case.law/v1/
```

Better coverage for older opinions (pre-2010). The bulk
download option is available for Oregon Reports.

### Limitations

The CAP API has a Whitelist Restriction for some jurisdictions —
unrestricted access to fully-text "whitelisted" jurisdictions;
metadata-only for others. Oregon is partially whitelisted;
verify on the API status page.

## RECAP (federal court docket access)

For federal cases in the District of Oregon and the 9th Circuit:

### Free archive

```
https://www.courtlistener.com/recap/
```

The Free Law Project's RECAP archive mirrors PACER documents
that users have uploaded. Coverage is partial — useful for
high-profile cases but not comprehensive.

### PACER

Direct PACER access requires registration and per-page fees.
For the Oregon plugin, prefer RECAP / CourtListener for
publicly available opinions; use PACER only when needed for
specific docket entries.

## Patterns for the agent

### Verify a citation

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22316+Or+499%22&type=o
  prompt: Locate the case Buchler v. Oregon Corrections Div.,
          316 Or 499 (1993). Quote the parallel cite, confirm
          year, and identify whether the case is good law.
```

### Pull an ORS section

```
WebFetch:
  url: https://www.oregonlegislature.gov/bills_laws/ors/ors012.html
  prompt: Locate ORS 12.080. Quote the verbatim text of
          subsection (1) and (2). Identify the date of
          enactment and most recent amendment.
```

### Pull a CFR section (point-in-time)

```
WebFetch:
  url: https://www.ecfr.gov/api/versioner/v1/full/2025-01-01/title-12.xml
  prompt: Locate 12 CFR § 1006.30. Quote the verbatim text as
          in effect on January 1, 2025.
```

### Check 9th Circuit on an FDCPA issue

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22FDCPA%22+%221692e%22&type=o&court=ca9&order_by=dateFiled+desc
  prompt: Identify the most recent 9th Circuit opinion
          interpreting 15 USC § 1692e. Provide the citation
          and a one-sentence holding summary.
```

## Quarterly refresh routine

The plugin's pull scripts (in `scripts/`) refresh the reference
corpora on a quarterly cycle:

| Corpus | Source | Frequency |
|--------|--------|-----------|
| ORCP | counciloncourtprocedures.org | Every 6 months (post-effective date) |
| UTCR | courts.oregon.gov/rules/UTCR | Annual (August 1) |
| ORS (debt-relevant chapters) | oregonlegislature.gov | Quarterly |
| OEC (ORS 40) | oregonlegislature.gov | Quarterly |
| Federal debt laws | uscode.house.gov, ecfr.gov | Quarterly |
| UCC model | LII (cornell) | Annual |

The remote-agent routine (`trig_018yahbiUwS1uTUJSuDNrCqG` or
its Oregon-specific equivalent) runs on **Jan/Apr/Jul/Oct 1 at
17:00 UTC** and opens a PR if any corpus changed.

## Safety policy

- WebFetch is the only approved fetch mechanism
- Always cite the URL and date of fetch when relying on a
  source
- Quote verbatim, not paraphrased, when the agent's output
  will be used in a filing
- Flag any change-detection signal (different version, updated
  date, etc.) explicitly to the user
