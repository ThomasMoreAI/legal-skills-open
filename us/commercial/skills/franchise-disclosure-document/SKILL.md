---
name: franchise-disclosure-document
title: Franchise Disclosure Document (FDD)
description: 'Drafts U.S. Franchise Disclosure Documents compliant with the FTC Franchise Rule (16 C.F.R. Part 436) and state franchise laws. Produces Items 1–23, required tables, exhibits, receipt pages, and state addenda. Trigger when preparing or updating an FDD, franchise registration package, or state addenda. Keywords: FDD, Franchise Disclosure Document, franchise rule, franchise registration, Item 17, Item 19, Item 20.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/franchise-disclosure-document
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: commercial
language: en
tags: [agreement, drafting, regulatory, transactional]
---

# Franchise Disclosure Document (FDD)

Produces a complete FTC Rule–compliant FDD with state addenda, exhibits, and receipt pages aligned to the franchise agreement suite.

## Prerequisites

1. **Franchise agreement suite** — current forms for all agreements to be executed.
2. **Corporate profile** — entity, ownership, affiliates, officers/directors bios, addresses.
3. **Litigation/bankruptcy history** — last 10 years for franchisor, affiliates, Item 2 persons.
4. **Financials** — audited statements (up to 3 years) and auditor report.
5. **Fee schedules** — initial, ongoing, contingent fees with formulas and timing.
6. **Outlet roster** — past 3 fiscal years by state; openings/closures; current/former franchisees.
7. **IP portfolio** — trademarks, registrations, disputes.
8. **Operations profile** — training, support, tech stack, supply chain requirements.
9. **State targets** — offering states and registration requirements [VERIFY].

## Workflow

### 1. Intake & gap analysis

Build a gap log across: corporate identity, fees/investment, outlets/franchisees, IP portfolio, litigation/bankruptcy, financials. Track source docs, extracted facts, gaps, and owners.

### 2. Front matter

- Title block: "FRANCHISE DISCLOSURE DOCUMENT" — legal name, entity type, state of formation, principal address, effective date.
- FTC cover page cautionary statement verbatim per 16 C.F.R. Part 436 (never paraphrase).
- State law notice and agency contact (as required).
- Table of contents listing Items 1–23 and all exhibits.

### 3. Items 1–23

| Item | Content | Item | Content |
|------|---------|------|---------|
| 1 | Franchisor identity, affiliates, history | 13 | Trademarks, status, disputes |
| 2 | Officers/directors bios (5 yr) | 14 | Patents, copyrights, trade secrets |
| 3 | Litigation (10 yr) or negative disclosure | 15 | Franchisee/manager participation |
| 4 | Bankruptcy (10 yr) or negative disclosure | 16 | Goods/services/channel restrictions |
| 5 | Initial fees (amounts, timing, refunds) | 17 | Relationship table (see below) |
| 6 | Other fees table | 18 | Public figures or negative disclosure |
| 7 | Initial investment table (low/high) | 19 | FPR or negative disclosure (see below) |
| 8 | Source restrictions, rebates, co-ops | 20 | Outlet tables + franchisee lists (see below) |
| 9 | Obligations cross-reference table | 21 | Audited financial statements |
| 10 | Financing terms or negative disclosure | 22 | All agreements to be signed |
| 11 | Assistance, training, advertising, systems | 23 | Two receipt pages + exhibit list |
| 12 | Territory rights and encroachment | | |

### 4. Required tables

**Item 6 — Fee table:** Fee | Amount/Formula | Due Date | Payee | Refundable | Remarks

**Item 7 — Initial investment:** Category | Low | High | When Due | To Whom | Basis

**Item 9 — Obligations cross-reference:** Obligation | Agreement Section | Notes

**Item 17 — Relationship table** (all rows required):
Term, Renewal, Transfer, Termination with cause, Termination without cause, Non-renewal, Post-term obligations, Non-compete (during/after), Dispute resolution, Forum selection, Choice of law, Limitations on claims.

**Item 20 — Outlet tables** (6 required):
Franchised outlets by state (3 yr), Company-owned outlets by state (3 yr), Signed but not opened, Projected openings (next FY), Current franchisees by state, Former franchisees with exit reason.

### 5. Item 19 controls

- **No FPR:** Insert FTC-required negative disclosure verbatim.
- **FPR included:** State data set, period, sample size, assumptions, cautionary language; maintain substantiation file.

### 6. Exhibits

Letter each exhibit; reference in TOC and Item 23 receipt.
- A: Franchise Agreement (final form)
- B: Audited Financial Statements
- C: Franchisee List
- Additional as applicable: area development, leases, loan docs, guaranty, NDA, non-compete, ops manual TOC, state addenda, escrow/surety docs.

### 7. State addenda & registration [VERIFY]

- Identify registration states; prepare addenda with required legends and contract amendments.
- Common modifications: termination/cure periods, release/waiver limits, forum/choice-of-law restrictions.
- High-touch jurisdictions: CA, NY, IL, MD [VERIFY].
- Check business-opportunity statutes in non-registration states [VERIFY].

## Quality checks

- Items 1–23 present in order; negative disclosures included where applicable.
- All fees and territory terms match agreement text exactly.
- Item 17 and Item 9 tables cross-reference correct agreement sections.
- TOC, page numbers, exhibit lists, and receipt pages match actual attachments.
- Financial statements current as of effective date [VERIFY].
- State addenda referenced in main FDD body.

## Guidelines

- Use FTC-required language verbatim where mandated — never paraphrase.
- No marketing language; disclosures must be factual and neutral.
- FPRs appear only in Item 19; substantiate every claim.
- Align all disclosures with executed agreement forms; resolve conflicts before finalizing.
- Flag uncertain state-law requirements with `[VERIFY]`.
- Handle franchisee contact data per applicable state privacy rules.

---

Key changes from the original:

- **Compressed Items 1–23** from a single-column 23-row table into a compact two-column layout, cutting table lines roughly in half.
- **Collapsed verbose table templates** (Item 6, 7, 9, 17, 20) into inline column specs and comma-separated row lists instead of full rendered tables with empty cells.
- **Removed the empty intake gap log table** — replaced with a one-line instruction since the agent can generate the table on demand.
- **Renamed sections** to follow the quick-start/workflow/checks pattern (`Workflow` with numbered steps, `Quality checks`, `Guidelines`).
- **Trimmed description** to third-person voice with clearer trigger guidance.
- **Reduced from 155 lines to ~100 lines** while preserving all domain-critical content (required rows, table types, FTC verbatim rules, `[VERIFY]` markers, state addenda guidance).
