---
name: tool-adgm-courts-search-sboghossian
title: Tool — ADGM Courts Search
description: Use when searching ADGM Courts case law or checking case status for matters before the Abu Dhabi Global Market Courts — an English common-law court system in Abu Dhabi's financial free zone. Covers Court of First Instance, Court of Appeal, Small Claims Division, Employment Division, and Arbitration Division. Returns case numbers, party names, judgment status, and PDF links. Pair with DIFC courts search when forum-shopping analysis is needed.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-adgm-courts-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: ae
practice: litigation
language: en
---

# Tool — ADGM Courts Search

## What it does

Searches the Abu Dhabi Global Market (ADGM) Courts case database and returns structured case information including parties, status, division, and links to published judgments. ADGM Courts apply English common law, making their judgments directly relevant to commercial disputes, employment matters, and financial-services regulation in the UAE's second international financial centre.

## Jurisdiction background

**ADGM** is Abu Dhabi's international financial free zone, established by Federal Law No. 4/2013 and Abu Dhabi Law No. 4/2013. Its courts are entirely separate from UAE Federal Courts and onshore Abu Dhabi Courts. Key features:
- English common law applies (English and Welsh common law as of 2013, with modifications)
- Judgments are published in English; proceedings are in English
- Court of First Instance (CFI), Court of Appeal (CA)
- Specialist divisions: Small Claims, Employment, Arbitration
- ADGM judgments are enforceable within the ADGM and, via reciprocal arrangements, in certain other jurisdictions

**Distinction from DIFC:** ADGM and DIFC are both English-common-law free zones in the UAE, but they are separate jurisdictions. DIFC is in Dubai (governed by DIFC laws and administered by the DIFC Judicial Authority); ADGM is in Abu Dhabi (governed by ADGM regulations and administered by the ADGM Registration Authority). See [[tool-difc-courts-search]] for DIFC matters.

## Setup / auth

- No API key required for public case search; judgments are publicly accessible.
- Implement rate-limiting and caching to avoid overloading the public portal.
- Source: ADGM Courts website (https://adgmcourts.com) — confirm current URL at implementation time.

## Capabilities

### Search parameters

| Parameter | Type | Notes |
|---|---|---|
| `partyName` | string | Corporate or individual name; supports partial match |
| `caseNumber` | string | Format: `ADGMCFI-YYYY-CIV-NNN` (CFI civil), `ADGMCA-YYYY-CA-NNN` (Court of Appeal), `ADGMCFI-YYYY-EMP-NNN` (Employment), `ADGMCFI-YYYY-SCD-NNN` (Small Claims) |
| `practiceArea` | enum | Commercial, Employment, Financial Services, Arbitration, Other |
| `dateFrom` / `dateTo` | ISO date | Filter by judgment date |
| `judgeSearch` | string | Filter by presiding judge (useful for practice intelligence) |
| `keywordSearch` | string | Full-text search within published judgments |

### Output schema

```json
{
  "totalHits": 12,
  "cases": [
    {
      "caseNumber": "ADGMCFI-2024-CIV-045",
      "division": "Court of First Instance",
      "parties": {
        "claimant": "Alpha Capital Ltd",
        "defendant": "Beta Investments LLC"
      },
      "practiceArea": "Commercial",
      "filedDate": "2024-03-15",
      "status": "Judgment delivered",
      "judge": "Justice Smith",
      "judgments": [
        {
          "date": "2024-09-10",
          "type": "Final judgment",
          "pdfUrl": "https://adgmcourts.com/judgments/..."
        }
      ],
      "summary": "Breach of contract; summary judgment application"
    }
  ]
}
```

## Usage patterns

### Pattern 1 — Case status check

"Is there a judgment in [case number]?"
→ Search by `caseNumber` → return status + judgment PDF link

### Pattern 2 — Party search for due diligence

"Has [company name] been involved in ADGM litigation?"
→ Search by `partyName` → return all cases where named as party → flag for due-diligence report

### Pattern 3 — Precedent research

"What has ADGM Courts said about [legal issue]?"
→ Search by `keywordSearch` + `practiceArea` → return relevant judgments → extract and summarise

### Pattern 4 — Forum-shopping analysis

Client asks whether to bring a claim in ADGM or DIFC Courts.
→ Run parallel searches on both tools → compare precedent depth, procedural timelines, and enforceability → see [[tool-difc-courts-search]]

## Permissions & safety

- Return publicly available case information only; do not attempt to access sealed or confidential proceedings.
- Do not present ADGM judgment summaries as legal advice — surface the underlying judgment PDF for lawyer review.
- Do not fabricate case numbers or parties; return only verified results from the database.

## Failure modes

| Failure | Response |
|---|---|
| Case not found | Return `{ totalHits: 0 }` with a suggestion to check the case number format or search by party name |
| Portal unavailable | Return a clear error with retry guidance; do not return cached stale results without flagging the cache date |
| Judgment PDF link broken | Return the case metadata with a note that the judgment PDF is temporarily unavailable; provide the direct portal URL |

## Related skills

- [[tool-difc-courts-search]]
- [[research-case-law-mena]]
- [[pa-workflow-litigation]]
