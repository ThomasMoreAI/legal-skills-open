---
name: underwriting-agreement
title: Underwriting Agreement
description: Drafts a firm-commitment underwriting agreement for SEC-registered U.S. public offerings, covering purchase terms, greenshoe, reps and warranties, covenants, closing conditions, indemnification, and market-out rights. Use when drafting or reviewing underwriting agreements, firm commitment deals, over-allotment options, or listing approvals; trigger on "underwriting agreement", "firm commitment", "public offering", "greenshoe", "over-allotment", "registration statement", "prospectus".
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/underwriting-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: capital-markets
language: en
---

# Underwriting Agreement

Produces a firm-commitment underwriting agreement for a SEC-registered public offering, aligning issuer, selling stockholders, and underwriters on economics, disclosure liability, and closing mechanics.

## Quick Start

Gather before drafting:

1. **Transaction snapshot** — issuer, offering type, ticker/exchange, size, price range, selling stockholders
2. **Registration materials** — effective registration statement, base prospectus, preliminary/final prospectus, free writing prospectuses
3. **Underwriting terms** — discount/commission, expenses, syndicate details, lock-up duration, greenshoe parameters
4. **Closing logistics** — date/time, DTC settlement, wire instructions, listing approval status
5. **Deliverables** — comfort letter scope, legal opinions, officer certificates, bring-down diligence

## Deal Inputs

| Item | Placeholder |
| --- | --- |
| Issuer legal name / jurisdiction | [Issuer] |
| Selling stockholders (if any) | [Selling Stockholders] |
| Representative underwriter | [Lead Underwriter] |
| Securities / class | [Security Type] |
| Firm shares | [Firm Shares] |
| Price to public | [Public Price] |
| Underwriting discount | [Discount] |
| Net proceeds to issuer | [Net Proceeds] |
| Over-allotment % and term | [Up to 15% / 30 days] |
| Exchange listing | [Exchange] |
| Governing law | [New York] |
| Closing date/time/location | [Closing] |

## Document Outline

1. Parties and Recitals
2. Definitions
3. Purchase and Sale
4. Over-Allotment Option (Greenshoe)
5. Delivery and Payment (DTC / Fedwire)
6. Representations and Warranties
7. Covenants
8. Conditions to Closing
9. Indemnification
10. Contribution
11. Termination / Market-Out
12. Lock-Up Agreements
13. Miscellaneous

## Section Checklists

**Purchase and Sale** — Firm-commitment, several not joint; firm shares, public price, discount, net price; selling stockholder allocation if applicable.

**Over-Allotment Option** — Option size and term; exercise mechanics and notice; allocation and settlement.

**Delivery and Payment** — DTC book-entry delivery; Fedwire instructions; closing sequence and location.

**Reps and Warranties** — Company: status, authorization, capitalization, valid issuance; registration statement/prospectus accuracy (no material misstatements/omissions); GAAP conformity; no MAC; legal compliance; no material litigation. Underwriters: securities law compliance; distribution only with permitted materials.

**Covenants** — Maintain registration effectiveness; file reports/supplements; no additional issuances or inconsistent disclosures; use of proceeds per prospectus; Regulation M compliance.

**Conditions to Closing** — Registration effective, no stop order; reps true at closing; auditor comfort letter; legal opinions (issuer counsel + underwriters' counsel); listing approval and good standing certificates; officer certificates and bring-down diligence.

**Indemnification** — Company indemnifies underwriters for issuer-supplied disclosure; underwriters indemnify company for underwriter-supplied disclosure; covered party scope and defense procedures.

**Contribution** — Relative fault and relative benefit allocation; public policy fallback if indemnity unavailable.

**Termination / Market-Out** — MAC in issuer or markets; trading suspensions or exchange closures; force majeure and legal impediments.

**Lock-Up** — Covered persons, duration, permitted transfers; release mechanics and notice.

**Miscellaneous** — Governing law and venue; assignment restrictions; amendments/waivers; counterparts and e-signatures; entire agreement and severability.

## Required Deliverables

| Deliverable | Provider | Timing |
| --- | --- | --- |
| Comfort letter | Auditors | Closing |
| Legal opinions | Issuer counsel / Underwriters' counsel | Closing |
| Officer certificates | Issuer | Closing |
| DTC eligibility | Issuer / Transfer agent | Pre-closing |
| Exchange listing approval | Exchange | Pre-closing |
| Lock-up agreements | Insiders | Pricing |

## Pitfalls and Checks

- All economic terms must match the prospectus and underwriting section disclosure exactly.
- Explicitly identify information furnished by underwriters (affects indemnification scope).
- Confirm DTC eligibility, listing approval, and closing mechanics before finalizing.
- Include Regulation M stabilization limitations.
- Address FINRA Rule 5110 compensation and conflict rules where applicable [VERIFY].
- If the deal is best-efforts or contingent, do **not** use firm-commitment structure; assess Rule 10b-9 applicability [VERIFY].
- Default to New York governing law unless parties require a different forum.
- Replace all bracket placeholders and validate all cross-references before release.

---

**Key changes from original:**
- Removed `tags` (not part of the Agent Skills spec frontmatter)
- Tightened `description` — dropped "Securities Act of 1933" keyword stuffing, kept actionable triggers
- Collapsed "Prerequisites" into a leaner "Quick Start" section
- Renamed "Output Structure / Process" → split into focused sections (Deal Inputs, Document Outline, Section Checklists)
- Compressed section checklists from multi-line bullet lists into dense single-paragraph entries — same coverage, ~40% fewer tokens
- Removed template clauses (verbose boilerplate; better suited for a `references/` file if needed)
- Renamed "Guidelines" → "Pitfalls and Checks" for scannability
- Reduced from 171 lines to ~100 lines while preserving all domain-critical content
