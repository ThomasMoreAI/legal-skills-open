---
name: document-production-log-summary
title: Document Production Log & Summary
description: Generates a structured log and strategic summary of opposing-party document productions in U.S. litigation discovery. Categorizes by type, date, custodian, and relevance; flags hot documents; tracks privilege assertions per FRCP 26(b)(5); identifies production gaps. Use when organizing voluminous productions, surfacing critical evidence, assessing completeness, or supporting meet-and-confer and motion to compel decisions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/document-production-log-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization, summary]
---

# Document Production Log & Summary

Transforms raw discovery productions into an organized inventory with strategic analysis — hot document flags, privilege tracking, and gap identification.

## Prerequisites

1. **Production materials** — all produced documents with Bates numbers assigned
2. **Discovery requests** — RFPs or subpoenas the production answers
3. **Case caption & CMO** — any provisions governing discovery format or tracking
4. **Producing party's written response** — including blanket objections and privilege assertions

## Output Structure

### 1. Production Header

| Field | Detail |
|---|---|
| Case caption | Full parties + designations |
| Case number / Court | Docket no., jurisdiction |
| Producing party | Name + counsel contact |
| Discovery request answered | RFP Nos. / subpoena date |
| Date received | MM/DD/YYYY |
| Production format | Native / TIFF / PDF; metadata preserved? |
| Bates range | e.g., DEF000001–DEF004872 |
| Total docs / pages / GB | Aggregate counts |
| Blanket objections | Summarize from written response |

### 2. Document Inventory

| Bates No. | Date | Type | Author | Recipient(s) | Custodian | Brief Description | Relevance Category | Priority |
|---|---|---|---|---|---|---|---|---|
| DEF000001 | | Email | | | | | | High/Med/Low |

**Document types:** Emails, contracts, financial records, internal memoranda, reports, meeting minutes, text messages / chat logs, photographs / multimedia.

**Relevance categories** (map to contested issues): Breach / performance, notice / knowledge, damages / valuation, causation, credibility / impeachment, affirmative defenses.

### 3. Hot Documents

For each flagged document:

```
Bates No.: _______
Date: _______
Document: [Type — Author to Recipient]
Why Critical: [Contradicts position X / Establishes knowledge of Y / Corroborates claim Z / Impeaches witness W]
Recommended Action: [Designate as exhibit / Depose custodian / Use in MSJ]
```

**Flag criteria:**
- Contradicts opposing party's stated position
- Establishes knowledge, intent, or notice
- Corroborates liability or damages theory
- Undermines witness credibility
- Creates or breaks key timeline elements

### 4. Privilege Log (FRCP 26(b)(5))

| Log No. | Date | Type | Author | All Recipients | Subject Matter | Privilege Claimed | Basis |
|---|---|---|---|---|---|---|---|
| | | | | | | AC / WP / CI | |

Flag: claims lacking adequate justification, apparent inadvertent disclosures or subject-matter waiver, entries failing FRCP 26(b)(5) specificity requirements.

### 5. Production Completeness Assessment

| Category | Expected | Produced | Gap? |
|---|---|---|---|
| Date range | [case-relevant span] | [actual span] | |
| Key custodians | [list] | [list] | |
| Document types | [per RFPs] | [actual] | |

**Flag for follow-up:**
- Missing custodians who logically possess responsive materials
- Truncated or orphaned email threads
- Time periods underrepresented vs. case chronology
- Corrupted files, password-protected docs, unsearchable formats
- Requested document categories entirely absent

### 6. Executive Summary

1–2 page narrative covering:
1. Overall production statistics
2. Top 5–10 hot documents with significance
3. Key evidentiary strengths surfaced
4. Gaps and recommended next steps (supplemental demand, meet-and-confer, motion to compel)
5. Open privilege disputes requiring resolution

## Guidelines

- **FRCP 34** governs production format; note non-compliance (e.g., ESI not in requested format)
- **FRCP 26(b)(5)** requires privilege logs sufficient for requesting party to assess the claim — flag deficient entries
- **Waiver risk**: Note inadvertent productions immediately; clawback under FRCP 26(b)(5)(B) and FRE 502 may apply [VERIFY jurisdiction-specific orders]
- Never reproduce potentially privileged content — use subject-matter descriptions only
- Custodian gaps are often more strategically significant than document gaps — prioritize custodian completeness
- Deliver in two formats: spreadsheet (filterable) + narrative summary report
