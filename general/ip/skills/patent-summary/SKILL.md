---
name: patent-summary
title: Patent Application Summary
description: Generates structured, prosecution-ready summaries of patent applications covering bibliographic data, claims analysis, and strategic observations. Use when summarizing patent filings, preparing for prosecution, conducting portfolio review, licensing negotiations, or freedom-to-operate analysis.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/patent-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Patent Application Summary

Produces a structured summary of a patent application for prosecution, licensing, litigation, or portfolio management. Requires the application document (specification, claims, abstract, drawings) and any priority/related filings.

## Quick Start

1. Gather the patent application and any related filings
2. Identify target audience (prosecution, licensing, litigation, portfolio)
3. Generate the summary following the output structure below
4. Flag prosecution risks and strategic observations
5. Review against checks at the bottom

## Output Structure

### 1. Executive Overview

Two to three sentences: invention essence, technical field, broadest claim scope.

### 2. Bibliographic Data

| Field | Extract |
|---|---|
| Application No. | — |
| Filing Date | — |
| Inventor(s) | — |
| Assignee | — |
| Priority Claims | — |
| Related Applications | — |
| Technical Field | — |

### 3. Background & Problem

- Problem the invention addresses
- Key prior art cited; how applicant distinguishes
- Novelty and non-obviousness positioning

### 4. Invention Description

- How it works — components, steps, or architecture
- Core innovations vs. prior art
- Key embodiments with practical applications
- Write accessibly for non-specialist attorneys; maintain technical precision

### 5. Drawings & Figures

| Figure | Description |
|---|---|
| Fig. N | — |

Summarize each referenced figure. Omit unreferenced figures.

### 6. Claims Analysis

| Claim | Type | Scope Summary |
|---|---|---|
| 1 | Independent | — |
| N | Independent | — |
| Key dependents | Dependent | — |

- **Total claims**: [count] — **Independent**: [count]
- **Format flags**: Note means-plus-function (§ 112(f)), Beauregard, or Jepson claims

### 7. Strategic Observations

**Scope & Strength**

- Claim breadth assessment
- Design-around vulnerabilities
- Commercially significant dependent claim narrowings

**Prosecution Risk Flags**

| Issue | Risk | Notes |
|---|---|---|
| Enablement (§ 112(a)) | Low/Med/High | — |
| Written Description | Low/Med/High | — |
| Indefiniteness (§ 112(b)) | Low/Med/High | — |
| Prior Art Overlap | Low/Med/High | — |

**Commercial & Portfolio**

- Licensing or FTO considerations
- Recommended next steps

## Checks

- Cite specific section headings, claim numbers, and figure references throughout
- Target 1–3 pages; balance comprehensiveness with conciseness
- Use precise IP terminology; keep descriptions accessible to non-specialist attorneys
- Flag potentially relevant uncited prior art with `[NOTE]`
- Do not opine on patentability — present observations only
- For continuations/divisionals, note parent filing relationship
- Default jurisdiction: U.S. (USPTO) unless specified otherwise

---

Shall I try writing this to the file again?
