# Legal Data APIs — California and Federal

The structured-data APIs below provide programmatic access to
California law, federal law, court opinions, and federal court
filings. Prefer these APIs over HTML scraping when the result
will be parsed, indexed, or watched for change.

## California Codes (leginfo.legislature.ca.gov)

The California Legislature publishes the California Codes as
HTML pages by code and section. There is no structured XML API
equivalent to USLM, but the leginfo HTML is well-formed and
parseable.

### Section lookup pattern

```
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=[CODE]&sectionNum=[SECTION].
```

Where `[CODE]` is one of:
- `CCP` — Code of Civil Procedure
- `EVID` — Evidence Code
- `CIV` — Civil Code
- `BPC` — Business and Professions Code
- `FIN` — Financial Code
- `COM` — Commercial Code
- `GOV` — Government Code
- `WIC` — Welfare & Institutions Code

And `[SECTION]` is the section number (with trailing period
for some sections — try both if one returns an error).

**Examples**:

```
# CCP § 437c
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=437c.

# Cal. Evid. Code § 1271
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=EVID&sectionNum=1271.

# Civ. Code § 1717
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1717.

# Bus. & Prof. Code § 17200
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=17200.
```

### Table of contents pattern

```
https://leginfo.legislature.ca.gov/faces/codesTOCSelected.xhtml?tocCode=[CODE]
```

Provides the chapter/article/section structure for browsing
the code. Useful for locating a section when the number is
unknown.

### Parsing approach

leginfo pages render section text in `<div>` elements with
class `codesectiongroup`. Extract the section number and text
by parsing the HTML. The `scripts/pull_ca_statutes.py` script
(to be created, paralleling `pull_wa_rcw.py`) will handle bulk
extraction.

### Change detection

The Legislature updates leginfo after each session (typically
September–October for a regular session). Amendments effective
January 1 of the following year. Re-pull all relevant chapters
in **October-November** and again in **February** (for urgency
statutes or special session amendments).

## California Rules of Court (courts.ca.gov)

The Judicial Council publishes the CRC on courts.ca.gov. The
rules are available as:

1. **Individual rule HTML pages** (browseable by title)
2. **Consolidated PDF** (entire CRC in one file)

### HTML rule lookup

```
https://www.courts.ca.gov/cms/rules/index.cfm?title=[N]&linkid=rule[X]_[XXXX]
```

Example (rule 3.1308):
```
https://www.courts.ca.gov/cms/rules/index.cfm?title=three&linkid=rule3_1308
```

The linkid format uses underscores: `rule3_1308` for rule 3.1308.
Titles: `two`, `three`, `four`, `five`, `six`, `seven`, `eight`,
`nine`, `ten`.

### PDF download

```
https://www.courts.ca.gov/cms/rules/index.cfm
```

The consolidated PDF is available on the rules index page;
updated annually and at interim amendment effective dates.

### Parsing approach

PDF text extraction via `pdfplumber` or `pymupdf`. Rules are
delimited by "Rule [X.XXXX]" headers. Subsections use lettered
identifiers `(a)`, `(b)`, etc.

## California court opinions

### California Courts opinions page

```
https://www.courts.ca.gov/opinions-slip.htm
```

Provides daily lists of newly filed opinions by court. Opinions
are linked as PDFs. Not searchable by content; use CourtListener
for full-text search.

### CourtListener REST API

```
https://www.courtlistener.com/api/rest/v3/
```

Endpoints:

- `/courts/` — list of courts
- `/opinions/` — full-text opinions
- `/clusters/` — opinion clusters (parallel cites)
- `/search/` — full-text search

**California court identifiers**:

| Court | CourtListener ID |
|-------|-----------------|
| California Supreme Court | `cal` |
| California Courts of Appeal (all) | `calctapp` |
| California Appellate Dept. Superior Court | `calappdeptsuper` |
| 9th Circuit | `ca9` |
| C.D. Cal. (Los Angeles) | `cacd` |
| N.D. Cal. (San Francisco/San Jose) | `cand` |
| S.D. Cal. (San Diego) | `casd` |
| E.D. Cal. (Sacramento/Fresno) | `caed` |

**Authentication**: Free tier gives 100 requests/day without
API key. Register for a free account for higher rate limits.

**Use cases**:
- **Cite-checking**: paste a citation, verify the case exists
  and the citation is accurate
- **Subsequent history**: search for cases citing a decision
  to check for overruling or distinguishing
- **Holding verification**: pull the opinion text to confirm
  the case stands for the cited proposition

### Query examples

```
# Search California Supreme Court for summary judgment cases
GET https://www.courtlistener.com/api/rest/v3/search/?q=summary+judgment+437c&court=cal&type=o

# Get a specific case by citation
GET https://www.courtlistener.com/api/rest/v3/search/?q=%2225+Cal.4th+826%22&type=o

# Get full opinion text
GET https://www.courtlistener.com/api/rest/v3/opinions/[id]/
```

### Caselaw Access Project (Harvard)

```
https://api.case.law/v1/
```

Better coverage for older California opinions (pre-1990). The
bulk download option covers the California Reports.

**Limitation**: Some jurisdictions are "whitelisted" for
full-text access; California has partial coverage. Verify on
the CAP status page.

## Federal law — USC

### USLM XML

```
https://uscode.house.gov/download/releasepoints/us/pl/[PL-NN]/usc[NN][a]@[release].xml
```

The current "release point" reflects the latest amendments
published. See https://uscode.house.gov/download/download.shtml.

**Relevant titles for California civil practice**:

- **Title 15** — Commerce and Trade (FDCPA at § 1692; FCRA at
  § 1681; TILA at § 1601; ECOA at § 1691)
- **Title 11** — Bankruptcy
- **Title 28** — Judiciary and Judicial Procedure

**Parsing approach**: USLM XML is structured and stable. The
`scripts/pull_federal_debt_laws.py` script (from the WA plugin)
extracts FDCPA, FCRA, TILA, ECOA, etc. The CA plugin re-uses
this output rather than re-pulling federal law.

## Federal regulations — eCFR

### eCFR Versioner API

```
https://www.ecfr.gov/api/versioner/v1/full/[YYYY-MM-DD]/title-[NN].xml
```

This API returns the CFR text as XML for any date in the past,
supporting **point-in-time** queries critical for verifying
the version of a regulation in effect at a particular event
date (FDCPA / Reg F enforcement actions, for example).

**Relevant titles**:

- **Title 12** — Banks and Banking (Reg F at part 1006 = 12
  C.F.R. pt. 1006; Reg Z at part 1026; Reg B at part 1002;
  Reg V at part 1022)

**Parsing approach**: eCFR XML follows a DITA-ish structure
similar to USLM. The existing WA plugin's
`pull_federal_debt_laws.py` handles extraction.

### eCFR query example

```
# Pull Reg F as of January 1, 2026
GET https://www.ecfr.gov/api/versioner/v1/full/2026-01-01/title-12.xml
  [then parse to pt. 1006]

# Point-in-time: version of 12 CFR § 1006.30 on a specific date
GET https://www.ecfr.gov/api/versioner/v1/full/2024-07-01/title-12.xml
```

## Judicial Council forms

The Judicial Council publishes forms as PDFs at:

```
https://www.courts.ca.gov/forms.htm
```

Forms are indexed by form number and subject. For a direct
form download:

```
https://www.courts.ca.gov/documents/[form-code].pdf
```

Example:
```
# MC-010 (Memorandum of Costs)
https://www.courts.ca.gov/documents/mc010.pdf

# CM-010 (Civil Case Cover Sheet)
https://www.courts.ca.gov/documents/cm010.pdf

# DISC-001 (Form Interrogatories — General)
https://www.courts.ca.gov/documents/disc001.pdf
```

## Patterns for the agent

### Verify a California case citation

```
WebFetch:
  url: https://www.courtlistener.com/?q=%2225+Cal.4th+826%22&type=o&court=cal
  prompt: Locate the case Aguilar v. Atlantic Richfield Co.
          (2001) 25 Cal.4th 826. Confirm the year, the parties,
          and the holding on burden-shifting for summary judgment.
          If this case has been overruled or limited by a
          subsequent California Supreme Court decision,
          identify that case.
```

### Pull a CCP section

```
WebFetch:
  url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=437c.
  prompt: Locate CCP § 437c. Quote the verbatim text of
          subdivisions (a), (b), and (c). Identify the most
          recent amendment date and effective date.
```

### Pull a CEC section

```
WebFetch:
  url: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=EVID&sectionNum=1271.
  prompt: Locate Cal. Evid. Code § 1271. Quote the verbatim
          text. Identify the date of most recent amendment.
```

### Pull a CRC rule

```
WebFetch:
  url: https://www.courts.ca.gov/cms/rules/index.cfm?title=three
  prompt: Locate Cal. Rules of Court, rule 3.1350. Quote the
          verbatim text of the rule, including its subdivision
          (a) through (j). Identify the current effective date.
```

### Pull a CFR section (point-in-time)

```
WebFetch:
  url: https://www.ecfr.gov/api/versioner/v1/full/2025-01-01/title-12.xml
  prompt: Locate 12 C.F.R. § 1006.30. Quote the verbatim text
          as in effect on January 1, 2025.
```

### Check 9th Circuit on an FDCPA issue

```
WebFetch:
  url: https://www.courtlistener.com/?q=%22FDCPA%22+%221692e%22&type=o&court=ca9&order_by=dateFiled+desc
  prompt: Identify the most recent 9th Circuit opinion
          interpreting 15 U.S.C. § 1692e. Provide the citation
          and a one-sentence holding summary.
```

## Quarterly refresh routine

The plugin's pull scripts (in `scripts/`) refresh the reference
corpora on a quarterly cycle:

| Corpus | Source | Frequency |
|--------|--------|-----------|
| CCP / CEC / Civ. Code / BPC | leginfo.legislature.ca.gov | Quarterly |
| CRC | courts.ca.gov/cms/rules | Annual + interim amendments |
| Federal debt laws | uscode.house.gov, ecfr.gov | Quarterly |
| UCC model | LII (cornell) | Annual |
| LASC / SFSC / OCSC local rules | Each court's website | Quarterly |

The remote-agent routine runs on **Jan/Apr/Jul/Oct 1 at 17:00
UTC** and opens a PR if any corpus changed.

## Safety policy

- WebFetch is the only approved fetch mechanism
- Always cite the URL and date of fetch when relying on a source
- Quote verbatim, not paraphrased, when the agent's output will
  be used in a filing
- Flag any change-detection signal (different version, updated
  date, statute amendment) explicitly to the user
