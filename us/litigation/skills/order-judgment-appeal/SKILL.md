---
name: order-judgment-appeal
title: Order and Judgment on Appeal
description: Drafts a U.S. appellate Order and Judgment memorializing disposition after review of a lower-court ruling. Covers captioning, jurisdictional recitals, standards of review, issue-by-issue holdings, remand directives, costs, and mandate language. Use when preparing an appellate order, judgment, disposition, affirm/reverse/remand order, or mandate-ready directive.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/order-judgment-appeal
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Order and Judgment on Appeal

Produces a final, enforceable appellate order and judgment stating jurisdiction, analysis, and disposition.

## Prerequisites

1. Appellate and lower-court case numbers
2. Party names with procedural roles (appellant, appellee, intervenor)
3. Trial judge name and date of order/judgment under review
4. Notice of appeal filing date and jurisdictional basis
5. Issues on appeal with applicable standards of review
6. Record citations for key facts and rulings
7. Disposition instructions (affirm/reverse/vacate/modify/remand)
8. Costs/fees authority and mandate issuance rule

## Quick Start

Draft in sequence: caption → jurisdiction → issues/standards → analysis → disposition → remand (if any) → costs/mandate → authentication.

## Output Structure

### 1. Caption Block

[APPELLATE COURT NAME]
[Division / District]

[Case Caption]
Appellate Case No. [___]
Trial Court No. [___]
Trial Judge: [___]

ORDER AND JUDGMENT
[Date]

### 2. Jurisdiction and Procedural History

Concise chronological summary establishing:
- Appealed order/judgment and date
- Timely notice of appeal
- Issues presented
- Briefing and oral argument status
- Standard(s) of review for each issue

### 3. Issues and Standards of Review

| Issue | Standard of Review | Record Reference |
|---|---|---|
| [Issue 1] | De novo / abuse of discretion / clearly erroneous / substantial evidence | [Cite] |

### 4. Analysis and Holdings

Per issue:

Issue [#]. [Statement]
Standard of Review: [standard]
Holding: [affirm/reverse/modify/vacate]
Reasoning: [1–3 sentences with controlling authority and record cite]

### 5. Disposition

IT IS ORDERED AND ADJUDGED that:
1. The [trial court order/judgment] is [affirmed/reversed/vacated/modified] as to [Issue].
2. The matter is [remanded] for [specific action].
3. [Costs/fees disposition].

### 6. Remand Instructions (if applicable)

Specify:
- Scope of remand and required proceedings
- Limits on trial court discretion
- Jurisdiction retained or returned
- Deadline or timeline if imposed

### 7. Costs, Fees, and Mandate

Costs on appeal are awarded to [party] pursuant to [authority].
Attorney's fees on appeal are [granted/denied] and [remanded for determination / set at $X].
The mandate shall issue [date/under rule].

### 8. Authentication

DATED: [Date]

________________________________
[Presiding Judge/Justice], [Title]

ATTEST:
________________________________
Clerk of the Court

## Pitfalls

- Maintain neutral judicial tone — not advocacy
- State the standard of review explicitly for every issue
- Separate each issue's outcome in the disposition — no ambiguity
- If modifying or remanding, specify exact changes or required actions
- Use jurisdiction-specific formatting and citation rules
- Include mandate language if required by local rule
- Mark uncertain authority with `[VERIFY]`
