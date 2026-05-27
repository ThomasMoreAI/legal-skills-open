---
name: ss4-ein-application
title: IRS Form SS-4 — EIN Application
description: Drafts IRS Form SS-4 (EIN Application) by extracting entity details from formation documents. Use when forming a new business entity, applying for a federal tax ID, or preparing EIN applications for corporations, LLCs, partnerships, or sole proprietorships.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ss4-ein-application
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: tax
language: en
tags: [corporate, drafting, letter]
---

# IRS Form SS-4 — EIN Application

Prepares a filing-ready Form SS-4 by extracting verified data from entity formation documents.

## Prerequisites

- **Formation documents** — Articles of incorporation/organization, certificate of formation, or partnership agreement (filed and stamped)
- **Governing documents** — Operating agreement, bylaws, shareholder agreements
- **Responsible party info** — SSN/ITIN, full legal name, title, phone number
- **Business details** — Principal office address (physical, not P.O. Box), mailing address, planned activities, employee projections

## Quick Start

1. Extract data from source documents per the extraction map below
2. Cross-reference legal name across all documents — flag any discrepancies before proceeding
3. Complete each SS-4 line group using verified data
4. Run consistency checks
5. Produce deliverables: completed SS-4, transmittal memo, preparation notes

## Document Extraction Map

| Source Document | Extract |
|---|---|
| Articles of incorporation/organization | Legal name (exact), formation date, entity type, registered agent |
| Operating agreement / bylaws | Management structure, ownership %, officer titles, fiscal year, signing authority |
| Partnership agreement | General partner(s), management authority, ownership interests |
| DBA/assumed name filings | Trade names (Line 2) |
| Board resolutions | S corp election (Form 2553), signing authority |
| Business plan / org chart | Employee projections, NAICS code, business activity description |
| Lease agreements | Physical location address |

## Line-by-Line Completion

### Lines 1–3: Entity Identification

- **Line 1 (Legal name)** — Character-for-character match to formation docs. Exact suffix as filed: "Inc." / "Incorporated" / "LLC" / "L.L.C." etc.
- **Line 2 (Trade name / DBA)** — Only if registered with state/local authority; otherwise blank
- **Line 3 (Mailing address)** — Street/P.O. Box, suite, city, state, ZIP, county

### Lines 4–7b: Location & Responsible Party

- **Line 4a–4b (Physical location)** — Street address only (no P.O. Box). Source from lease or formation docs.
- **Lines 5a–5b (Responsible party)** — Individual who owns/controls entity. Determine by entity type:

| Entity Type | Responsible Party |
|---|---|
| Sole proprietorship | Owner |
| Corporation | Principal officer per bylaws (president, CEO, CFO, treasurer) |
| Partnership | General partner with management authority |
| LLC (member-managed) | Controlling member by ownership % |
| LLC (manager-managed) | Managing member or manager per operating agreement |

- **Line 6 (SSN/ITIN)** — Of responsible party. Flag if foreign individual lacks U.S. TIN.
- **Lines 7a–7b (Phone/Fax)** — Business telephone of responsible party

### Lines 8–9a: Entity Classification

- **Line 8a** — One checkbox matching formation docs: sole proprietor/single-member LLC, partnership, corporation (C corp default), personal service corporation, nonprofit, or other (specify)
- **Line 8b** — S corp election: check if Form 2553 filed or will be filed. Search board resolutions and shareholder consents.
- **Line 8c** — Nonprofits only: check if Form 1023/1023-EZ/1024 filed for tax-exempt status
- **Line 9a** — Formation date from state-stamped filing. Must match exactly.

### Lines 9b–16: Purpose & Operations

- **Line 9b (Reason)** — Primary reason: started new business, hired employees, banking, changed org type, purchased business, trust, pension plan, other
- **Line 10 (First wage date)** — Date wages first/will be paid; "N/A" if no employees
- **Line 11 (Fiscal year close)** — Month from governing docs; default December
- **Lines 12–13 (Employees)** — Agricultural vs. non-agricultural projections from business plan
- **Line 14 (Principal activity)** — Specific description (e.g., "retail sale of organic groceries" not "retail")
- **Line 15 (Products/services)** — Detailed revenue-generating offerings
- **Line 16 (NAICS code)** — 6-digit code matching principal activity. Verify against current NAICS manual.

### Lines 17–18: Authorization & Signature

- **Third-party designee** — If attorney/CPA authorized: name, phone, 5-digit PIN
- **Signature** — Must be signed by authorized individual per governing documents:

| Entity Type | Authorized Signer |
|---|---|
| Sole proprietorship | Owner |
| Partnership | General partner |
| Corporation | Officer authorized by bylaws |
| LLC | Member or manager per operating agreement |

Include: printed name, title, signature line, date, phone number.

## Consistency Checks

Before finalizing, verify:

- [ ] Line 1 legal name matches formation documents character-for-character
- [ ] Entity type (Line 8a) aligns with formation structure
- [ ] Corporation → Line 8b addresses S corp election status
- [ ] "Hired employees" (Line 9b) → Line 10 has specific date (not N/A)
- [ ] Nonprofit → Line 8c addresses exempt status filing
- [ ] Responsible party title matches governing document role
- [ ] Fiscal year (Line 11) matches governing docs
- [ ] NAICS code corresponds to Lines 14–15 activity description
- [ ] All addresses verified against source documents
- [ ] SSN/ITIN provided for responsible party

## Deliverables

1. **Completed Form SS-4** — All lines filled or marked N/A, matching official IRS layout
2. **Transmittal memo** — Entity name, responsible party, submission method, special circumstances
3. **Preparation notes** — Sources per section, assumptions, discrepancies resolved, recommended follow-up

## Pitfalls

- Never fabricate or assume entity details — extract only from verified source documents
- Flag conflicts between formation documents (e.g., differing entity names) and resolve before completing
- If S corp election status is unclear, flag for client confirmation
- NAICS codes change periodically — verify against current classification manual
- Form revision date and OMB number must reflect the most recent official IRS version
- The completed form is a certification under penalties of perjury — all information must be verifiable
