---
name: investigation-summary
title: Antitrust Investigation Summary
description: Produces structured antitrust investigation summaries for executives and counsel. Triggers on FTC/DOJ probes, state AG investigations, foreign competition authority inquiries, merger investigations, CIDs, subpoenas, or dawn-raid responses.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/investigation-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: antitrust
language: en
tags: [regulatory, summarization, summary]
---

# Antitrust Investigation Summary

Decision-ready antitrust investigation brief with evidence-linked chronology, legal theories, and business risk assessment.

## Quick Start

Gather before drafting:
- Regulatory process documents (CIDs, subpoenas, Second Requests, notices)
- Internal investigation materials (interview memos, forensic reviews, privilege logs)
- Market data (shares, competitors, pricing, entry barriers)
- Public sources (press, filings, complaints, consent decrees)
- Current status (deadlines, productions, negotiations)

## Workflow

### 1. Build Key-Facts Table

Populate and resolve gaps before drafting.

| Field | Detail |
|---|---|
| Investigating Authority | Agency, division, lead office, contact(s) |
| Matter Type | Conduct, merger, or industry sweep |
| Alleged Conduct | Price-fixing, monopolization, exclusive dealing, etc. |
| Market Definition | Product and geographic market as asserted |
| Statutory Hooks | Sherman §1/§2, Clayton §7, FTC Act §5, state/foreign provisions |
| Initiation Trigger | Complaint, market study, HSR, dawn raid, etc. |
| First Notice Date | Date and instrument |
| Procedural Posture | Inquiry, formal investigation, litigation, appeal |
| Key Deadlines | Production dates, meetings, milestones |
| Exposure Signals | Penalties, remedies sought, damages claims |
| Remediation | Compliance changes, business changes |

### 2. Draft Summary

Use this template. Cite every factual assertion with `[source: <id>]`.

```
ATTORNEY-CLIENT PRIVILEGED & WORK PRODUCT
CONFIDENTIAL — ANTITRUST INVESTIGATION SUMMARY

**Executive Overview**
Agency:
Matter Type:
Alleged Conduct:
Market:
Current Status:
Immediate Decisions/Actions:

**Chronology**
| Date | Event | Source | Notes |
|---|---|---|---|

**Allegations & Legal Theories**
| Theory | Conduct | Market Definition | Statutes | Evidence |
|---|---|---|---|---|

**Market & Industry Context**
- Market structure and shares:
- Key competitors:
- Barriers to entry:
- Industry dynamics or consolidation:

**Procedural Status**
- Steps completed:
- Outstanding requests:
- Upcoming milestones:

**Company Response**
- Cooperation posture:
- Privilege/objections asserted:
- Internal investigation steps:
- Remedial measures:

**Outcomes / Scenarios**
- If closed: disposition and conditions.
- If ongoing: likely outcomes and timelines.

**Risk Assessment**
| Risk Category | Exposure | Drivers | Mitigation |
|---|---|---|---|

**Compliance Actions**
- Immediate controls:
- Medium-term enhancements:
- Training or policy updates:
```

### 3. Multi-Jurisdiction Matters

If multiple authorities are involved, create one subsection per authority and a consolidated risk section.

## Pitfalls

- **Allegations vs. facts**: Separate clearly; never speculate.
- **Missing data**: Flag with `[VERIFY]`, especially for uncertain statutes or foreign-law citations.
- **Exact references**: Use precise dates, agency names, and instrument titles — do not paraphrase.
- **Inferences**: Label explicitly and cite the underlying source.
- **Merger matters**: State the asserted theory of harm and any divestiture or behavioral remedy signals.
- **Parallel proceedings**: Include state AGs, EC, CMA, or other competition authorities as separate subsections.
- **Privilege headers**: Maintain `ATTORNEY-CLIENT PRIVILEGED & WORK PRODUCT` on every output.
