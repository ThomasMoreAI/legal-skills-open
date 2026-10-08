---
name: tool-courtlistener-us-sboghossian
title: Tool — CourtListener (US Case Law Database)
description: Use when researching US federal and state case law, searching court opinions, or accessing the PACER-alternative CourtListener database for free public access to US court decisions. Relevant for US-law matters and comparative-law research referencing US precedent alongside MENA or EU law. CourtListener is operated by the Free Law Project and provides a public API at no cost.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/tool/tool-courtlistener-us
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tool — CourtListener (US Case Law Database)

## What it does

Searches CourtListener — the Free Law Project's open database of US federal and state court opinions — to retrieve case law, docket information, and oral argument audio. Provides programmatic access via a REST API without the PACER fees associated with the official federal courts system.

CourtListener is the primary free alternative to Westlaw and LexisNexis for US case law. For citation-verified BigLaw-quality research, CoCounsel (Westlaw-integrated) remains preferable; CourtListener is ideal for open research, comparative law, and matters where Westlaw access is not available.

## Setup / auth

- **Public REST API:** https://www.courtlistener.com/api/rest/v3/
- **Authentication:** API token (free registration at courtlistener.com)
- **Rate limits:** 5,000 requests per day on the free tier; higher limits available
- **Data coverage:** 6M+ opinions spanning US Supreme Court, all federal circuit courts, federal district courts, and most state supreme and appellate courts

## Capabilities

### Search parameters

| Parameter | Notes |
|---|---|
| `q` | Full-text keyword search across opinion text |
| `court` | Filter by court ID (e.g., `scotus`, `ca2`, `dcd`, `casd`) |
| `filed_after` / `filed_before` | Date range for opinion filing |
| `cited_gt` | Filter by citation count (useful to surface frequently cited decisions) |
| `judge` | Filter by author judge |
| `docket_number` | Retrieve specific case by docket number |
| `status` | `Published` (precedential) vs `Unpublished` / `Memorandum` |

### Endpoints

- `/opinions/` — opinion text, metadata, citations
- `/dockets/` — full docket with entries
- `/clusters/` — opinion clusters (groups parallel opinions in the same case)
- `/citations/` — citation network (who cites whom)
- `/courts/` — list of covered courts and their identifiers

### Output schema (opinions)

```json
{
  "id": 12345,
  "case_name": "Smith v. Jones Corp.",
  "court": "United States Court of Appeals, Second Circuit",
  "date_filed": "2023-04-15",
  "docket_number": "22-1234",
  "status": "Published",
  "judges": "Sotomayor, J., Calabresi, J., Park, J.",
  "citation": "2023 WL 2945123",
  "absolute_url": "https://www.courtlistener.com/opinion/12345/",
  "download_url": "https://storage.courtlistener.com/pdf/...",
  "summary": "Contract interpretation; implied covenant of good faith...",
  "citations_to": [{ "id": 6789, "case_name": "...", "year": 2019 }]
}
```

## Usage patterns

### Pattern 1 — US precedent for comparative research

A MENA contract dispute involves a governing-law clause selecting New York law. Search CourtListener for relevant Second Circuit / SDNY opinions on the contested contractual provision to support the legal analysis.

### Pattern 2 — Check for controlling authority

Before drafting a legal argument under US federal law, run a CourtListener search to identify controlling circuit precedent and check whether a position is well-settled or contested.

### Pattern 3 — Citation network analysis

Identify the most-cited cases on a US legal issue by using the `cited_gt` filter and the citation network endpoint — surfaces influential authority quickly.

### Pattern 4 — PACER cost avoidance

CourtListener provides free access to most federal opinions that would otherwise require PACER fees. For standard research tasks where Westlaw is unavailable, CourtListener covers the majority of federal opinions.

## Limitations

- **No Westlaw editorial enhancements:** CourtListener does not provide KeyCite, headnotes, or editorial flags (overruled, distinguished). For citation status (whether a case has been overruled), supplement with Westlaw or a dedicated citator.
- **Coverage gaps:** Some older opinions and certain state courts are not fully covered. Check the court coverage list before relying on a "no results" finding.
- **Unpublished opinions:** Included in the database but marked as such; confirm whether the applicable circuit court allows citation of unpublished opinions.
- **Not a substitute for professional research:** For high-stakes US litigation or transactional work, verified Westlaw/Lexis citations remain the professional standard.

## When to use CoCounsel instead

For US-law-heavy matters where:
- The client has a TR/Westlaw enterprise license
- Bluebook-precise, citation-verified authority is required
- Deposition summaries or contract analysis against Westlaw treatises are needed

See [[tool-cocounsel]] for the full decision framework.

## Related skills

- [[tool-cocounsel]]
- [[tool-eur-lex-eu]]
- [[research-case-law-mena]]
- [[tool-companies-house-uk]]
