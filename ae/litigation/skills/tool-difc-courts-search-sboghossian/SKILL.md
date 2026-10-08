---
name: tool-difc-courts-search-sboghossian
title: Tool — DIFC Courts Search
description: Use when searching DIFC Courts case law or checking case status for matters before the Dubai International Financial Centre Courts — an English common-law court in Dubai's financial free zone. Covers Court of First Instance, Court of Appeal, Small Claims Tribunal, and Wills & Probate Registry. Returns party names, case numbers, judge, judgment PDFs. Note the DIFC-LCIA arbitration centre was replaced by DIAC in 2021. Pair with ADGM courts search for forum-shopping analysis.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-difc-courts-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: litigation
language: en
---

# Tool — DIFC Courts Search

## What it does

Searches the DIFC Courts case database and returns structured case information including parties, judge, division, status, and links to published judgments. DIFC Courts apply English common law, making them one of the two most important English-language court systems in the UAE (alongside ADGM Courts in Abu Dhabi).

## Jurisdiction background

**DIFC** (Dubai International Financial Centre) is established by UAE Federal Law No. 8/2004 and Dubai Law No. 9/2004. Its courts are entirely separate from UAE Federal and Dubai onshore courts.

Key features:
- English common law applies (English law as developed by common-law courts worldwide, with DIFC modifications)
- Proceedings conducted in English; judgments published in English
- Court of First Instance (CFI), Court of Appeal (CA)
- Small Claims Tribunal (SCT) for claims up to USD 200,000 (fast-track, limited discovery)
- Wills & Probate Registry for expatriate estates

**Critical: DIFC-LCIA arbitration centre** was wound up in 2021 following the Dubai government's restructuring of arbitration institutions. Arbitrations that would have been under DIFC-LCIA rules are now administered by the **Dubai International Arbitration Centre (DIAC)** under the 2022 DIAC Arbitration Rules. Flag this in any discussion of DIFC arbitration clauses referencing DIFC-LCIA.

**Enforcement in Dubai:** DIFC judgments are directly enforceable within the DIFC. Enforcement in onshore Dubai (outside DIFC) is governed by DIFC Law No. 12/2020, which provides for ratification through the Dubai Court of First Instance — a relatively streamlined process. Enforcement in other UAE emirates and internationally requires conventional ratification proceedings.

## Setup / auth

- Public case search available through DIFC Courts portal; no API key required for basic search.
- Full-text judgment search available on the DIFC Courts website (https://www.difccourts.ae).
- Implement caching for repeated queries on the same party.

## Capabilities

### Search parameters

| Parameter | Type | Notes |
|---|---|---|
| `partyName` | string | Corporate or individual; partial match supported |
| `caseNumber` | string | Format: `CFI-NNN-YYYY` (Court of First Instance), `CA-NNN-YYYY` (Court of Appeal), `SCT-NNN-YYYY` (Small Claims) |
| `judgeSearch` | string | Filter by judge name — important for practice intelligence on judicial tendencies |
| `practiceArea` | enum | Commercial, Employment, Financial Services, Property, Wills & Probate |
| `dateFrom` / `dateTo` | ISO date | Date range for judgment |
| `citationSearch` | string | Find cases that cite a specific earlier authority |
| `keywordSearch` | string | Full-text search within published judgments |

### Output schema

```json
{
  "totalHits": 8,
  "cases": [
    {
      "caseNumber": "CFI-045-2023",
      "division": "Court of First Instance",
      "parties": {
        "claimant": "Dubai Property Holdings Ltd",
        "defendant": "International Asset Management SARL"
      },
      "practiceArea": "Commercial",
      "filedDate": "2023-06-01",
      "status": "Final judgment delivered",
      "judge": "Justice Al Muhairi",
      "judgments": [
        {
          "date": "2024-02-20",
          "type": "Judgment on liability and quantum",
          "pdfUrl": "https://www.difccourts.ae/judgments/..."
        }
      ],
      "summary": "Breach of shareholders agreement; oppression remedy sought"
    }
  ]
}
```

## Usage patterns

### Pattern 1 — Case status check

"What is the status of CFI-045-2023?"
→ Search by `caseNumber` → return current status + judgment links

### Pattern 2 — Party litigation history

"Has [company] been involved in DIFC litigation?"
→ Search by `partyName` → surface all cases as claimant or defendant → flag for due diligence report

### Pattern 3 — Precedent research

"What has the DIFC Court said about good faith in contract interpretation?"
→ Search by `keywordSearch: "good faith"` + `practiceArea: Commercial` → extract and summarise key judgments

### Pattern 4 — Forum-shopping analysis (DIFC vs ADGM)

When a client is structuring a transaction and has a choice of DIFC or ADGM as the governing forum:
- Compare precedent depth on the relevant legal issue (both courts)
- Compare procedural timelines (DIFC SCT is often faster for small commercial claims)
- Compare enforceability: DIFC judgment enforceability in Dubai vs ADGM in Abu Dhabi
- Consider which court has more familiar precedent for the legal issue (DIFC has a longer judgment history)

See [[tool-adgm-courts-search]] for ADGM search.

### Pattern 5 — Wills & Probate

"Is there a registered DIFC will for [name]?"
→ Search Wills & Probate Registry — note that this is a registration database, not a litigation database; wills registered here may be restricted access.

## DIFC arbitration note

**Post-2021 arbitration clauses:** Contracts with DIFC-LCIA clauses should be reviewed. If the dispute has not yet been commenced:
- DIFC-LCIA Rules are no longer operative
- Parties should agree to DIAC, LCIA (London), ICC, or another institutional ruleset
- DIFC Courts can still seat arbitrations under the DIFC Arbitration Law (DIFC Law No. 1/2008 as amended) — the court's supervisory jurisdiction remains
- See [[draft-arbitration-clause]] for updated clause recommendations

## Permissions & safety

- Return publicly available judgment information only; do not attempt to access sealed or confidential orders.
- Do not summarise a judgment without flagging the judgment date and status — an older CFI judgment may have been appealed.
- Never represent a DIFC case search as a sanctions or KYC check; it is one layer of a due-diligence review.

## Failure modes

| Failure | Response |
|---|---|
| Case not found | Return `totalHits: 0`; suggest searching by party name if case number is uncertain |
| DIFC-LCIA reference in contract | Flag that DIFC-LCIA no longer operates; recommend updating the clause |
| Enforcement in onshore Dubai | Explain the DIFC Law No. 12/2020 ratification pathway |
| Judgment appealed | Flag CA case if found; do not present CFI judgment as final if an appeal is pending |

## Related skills

- [[tool-adgm-courts-search]]
- [[research-case-law-mena]]
- [[pa-workflow-litigation]]
- [[draft-arbitration-clause]]
