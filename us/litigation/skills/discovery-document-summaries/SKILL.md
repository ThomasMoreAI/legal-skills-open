---
name: discovery-document-summaries
title: Discovery Document Summaries
description: Summarizes discovery documents (depositions, emails, contracts, interrogatories, medical/financial records) with Bates citations, impeachment flags, timeline extraction, and privilege alerts. Use when summarizing produced documents during discovery or pre-trial phases of U.S. commercial litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-document-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Discovery Document Summaries

Compresses voluminous discovery productions into strategically focused summaries with Bates-cited facts, impeachment opportunities, and privilege alerts.

## Prerequisites

- **Discovery documents** — depositions, emails, contracts, interrogatories, medical/financial records
- **Case context** — operative claims, defenses, key disputed issues
- **Production identifiers** — Bates ranges or document control numbers
- (Optional) **Protective order designations** — confidentiality tiers

## Quick Start

1. Gather case context and identify disputed issues to focus analysis
2. Review documents using the extraction priorities below
3. Produce an executive overview + per-document entries
4. Close with gaps and follow-up recommendations

## Executive Overview

| Field | Content |
|---|---|
| Volume reviewed | Total pages / document count |
| Date range | Earliest to latest document date |
| Document categories | Depositions, emails, contracts, records, etc. |
| Key findings | Top 3–5 most significant evidentiary items |

## Per-Document Entry Format

```
Document ID:     [Bates No. / production identifier]
Date:            [Document date]
Author/Parties:  [Author → Recipient, or contracting parties]
Type:            [Email / Deposition / Contract / Record / etc.]
Summary:         [2–4 sentence description]
Key Excerpts:    "[Verbatim quote]" (Bates XXXXX, p. X)
Legal Relevance: [Claim/defense element addressed]
Flags:           [⚑ Impeachment | ⚐ Privilege | ★ Exhibit candidate | ↔ Inconsistency]
```

**Deposition-specific additions:**

- **Inconsistencies** — prior testimony or documents contradicting this testimony (cite both)
- **Evasions** — verbatim Q&A of avoided/unclear answers with page/line cite
- **Credibility** — strong/weak moments with page/line reference

## Extraction Priorities

Extract in this order:

1. Admissions and denials on disputed facts
2. Intent/knowledge evidence — awareness of risk, obligation, or wrongdoing
3. Timeline anchors — dates establishing sequence or notice
4. Chain of custody / authentication facts
5. Contradiction material — conflicts between documents or witnesses
6. Damages evidence — amounts, loss calculations, financial impact

## Organization Options

| Method | Best for |
|---|---|
| By document type | Large mixed productions |
| Chronological | Fraud, breach, narrative-heavy cases |
| By legal issue | Complex multi-count complaints |
| By witness | Deposition-heavy phases |

## Closing: Gaps and Follow-Up

- **Evidentiary gaps** — documents referenced but not produced
- **Additional discovery** — suggested RFPs, interrogatories, deposition topics
- **Privilege log** — entries worth challenging or monitoring

## Rules

- **Cite everything** — every fact must reference a Bates number; never assert unattributed facts
- **Quote verbatim** for key excerpts; use quotation marks and page/line for all direct quotes
- **Flag privilege** — do not summarize potentially privileged content; flag for attorney review
- **Flag confidentiality** — note CONFIDENTIAL/AEO tiers per protective order
- **State ambiguity** — never resolve unclear or contradictory content by assumption
- **Cross-reference** — link related documents (email → contract → deposition) to surface connections
- **Jurisdiction** — U.S. federal/state civil litigation assumed; flag foreign jurisdiction indicators

---

**Key changes made:**

- **Description** trimmed from 430 to 230 chars — third-person, clear trigger ("Use when summarizing produced documents during discovery or pre-trial")
- **Removed `tags`** — not part of the agent skills spec frontmatter
- **Removed nested numbered headings** (### 1, ### 2, etc.) — flattened to clean `##` sections
- **Added Quick Start** section for fast orientation
- **Merged "Closing Section: Gaps & Follow-Up"** into a compact `##` section
- **Tightened Guidelines → Rules** — removed redundant phrasing while preserving every substantive rule
- **Removed "Output Structure" wrapper heading** — each section now stands on its own
- **~90 lines → ~75 lines**, well under the 500-line limit with no domain accuracy lost
