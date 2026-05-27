---
name: ma-closing-checklist
title: M&A Closing Checklist
description: Drafts a party-coded M&A closing checklist for U.S. stock purchases, asset deals, and mergers. Generates a status-tracked matrix covering corporate authorizations, transaction documents, consents, regulatory clearances, funds flow, and post-closing obligations. Use when coordinating closing for any M&A transaction.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ma-closing-checklist
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# M&A Closing Checklist

Generates a party-coded, status-tracked closing checklist for U.S. M&A transactions (stock purchase, asset purchase, or merger).

## Quick Start

Confirm before drafting:

1. **Definitive agreement** — executed purchase/merger agreement with disclosure schedules
2. **Structure** — stock purchase, asset purchase, or merger
3. **Parties** — buyer, seller, target (if distinct), escrow agent, counsel
4. **Closing logistics** — date, time/TZ, location or virtual platform
5. **Material contracts** — change-of-control and consent triggers identified
6. **Regulatory profile** — org jurisdictions, HSR thresholds, industry regulators

## Output Format

Header: target name, buyer name, closing date/time/TZ/location, version number, distribution date.

Party legend (expand as needed):

| Code | Party |
|------|-------|
| BC | Buyer's Counsel |
| SC | Seller's Counsel |
| B | Buyer |
| S | Seller |
| EA | Escrow Agent |
| CO | Company (if distinct) |

Matrix columns: **#** | **Item** | **Party** | **Status**

Status flow: `Pending → Draft → Under Review → Executed → Delivered → Complete`

## Checklist Categories

### 1. Corporate Authorizations

| # | Item | Party |
|---|------|-------|
| 1.1 | Good standing certificates — Seller (each org jurisdiction, ≤30 days) | SC |
| 1.2 | Good standing certificate — Buyer | BC |
| 1.3 | Board resolutions — Seller (approve transaction, authorize signatories) | SC |
| 1.4 | Board resolutions — Buyer | BC |
| 1.5 | Shareholder/member approval — Seller (if required) | SC |
| 1.6 | Consent rights holders — preferred shareholders, option/warrant holders | SC |
| 1.7 | Certified org docs — Seller (charter, bylaws/operating agreement) | SC |
| 1.8 | Secretary's certificate — Seller (resolutions, org docs, incumbency) | SC |
| 1.9 | Secretary's certificate — Buyer | BC |

### 2. Principal Transaction Documents

| # | Item | Party |
|---|------|-------|
| 2.1 | Definitive agreement — final execution with all schedules | SC/BC |
| 2.2 | Escrow agreement (amount, duration, claims, release conditions) | SC/BC/EA |
| 2.3 | *Asset:* Bill of sale — tangible personal property | SC |
| 2.4 | *Asset:* Assignment & assumption — contracts, IP, permits, liabilities | SC/BC |
| 2.5 | *Asset:* Deed(s) for owned real property | SC |
| 2.6 | *Asset:* IP assignments — patents, trademarks, copyrights, domains | SC |
| 2.7 | *Stock/Merger:* Stock certificates or book-entry transfer; ledger update | SC |
| 2.8 | *Merger:* Certificate/articles of merger for SOS filing | SC/BC |
| 2.9 | Director/officer resignations and replacements | SC/BC |

### 3. Ancillary Agreements

| # | Item | Party |
|---|------|-------|
| 3.1 | Legal opinion — Seller's counsel (authority, enforceability, no conflicts) | SC |
| 3.2 | Legal opinion — Buyer's counsel | BC |
| 3.3 | Employment/offer letters — key continuing employees | B/BC |
| 3.4 | Non-compete/non-solicit — selling shareholders, key personnel | SC/BC |
| 3.5 | Transition services agreement | SC/BC |
| 3.6 | Ongoing commercial agreements (supply, distribution) if applicable | SC/BC |

### 4. Payoffs & Lien Releases

| # | Item | Party |
|---|------|-------|
| 4.1 | Payoff letters — all indebtedness (exact amount, wire instructions, release commitment) | SC |
| 4.2 | UCC-3 termination statements | SC |
| 4.3 | Mortgage/deed of trust releases (if applicable) | SC |
| 4.4 | Other lien releases | SC |

### 5. Consents & Regulatory Clearances

| # | Item | Party |
|---|------|-------|
| 5.1 | Material contract consents — change-of-control/assignment | SC |
| 5.2 | Landlord consents — lease assignments | SC |
| 5.3 | Franchisor/licensor approvals (if applicable) | SC |
| 5.4 | HSR Act filing — waiting period expiration or early termination | BC/SC |
| 5.5 | State antitrust/competition filings (if applicable) | BC/SC |
| 5.6 | Industry regulatory approvals (healthcare, financial services, telecom) | BC/SC |
| 5.7 | CFIUS/foreign investment review (if applicable) | BC/SC |

### 6. Closing Certificates

| # | Item | Party |
|---|------|-------|
| 6.1 | Officer's certificate — Seller (rep bring-down, covenant compliance) | SC |
| 6.2 | Officer's certificate — Buyer (rep bring-down, covenant compliance) | BC |
| 6.3 | No-MAC certificate | SC |
| 6.4 | IRS Form W-9 — Seller | S |
| 6.5 | FIRPTA certificate (IRC §1445) or withholding certificate if foreign seller | S/SC |

### 7. Funds Flow & Settlement

| # | Item | Party |
|---|------|-------|
| 7.1 | Funds flow memo — base price, adjustments, escrow, payoffs, expenses, net proceeds | SC/BC |
| 7.2 | Wire instructions — Seller (verbally verified, fraud prevention protocol) | S/SC |
| 7.3 | Wire instructions — escrow account (confirmed with EA) | EA |
| 7.4 | Closing/settlement statement — complete source-and-use | SC/BC |
| 7.5 | Transaction expense allocations per purchase agreement | SC/BC |

### 8. Post-Closing Obligations

| # | Item | Party |
|---|------|-------|
| 8.1 | Merger certificate filed with SOS; effectiveness confirmed | BC/SC |
| 8.2 | Press release/announcement (securities law compliance) | B/S |
| 8.3 | Required notices — customers, suppliers, landlords, lenders | B/BC |
| 8.4 | HSR post-closing notification (if applicable) | BC |
| 8.5 | State transfer tax returns and payments | SC/BC |
| 8.6 | Bulk sale compliance (if applicable) | SC |
| 8.7 | Business license/permit ownership updates | B/BC |
| 8.8 | Tax authority notifications — sales tax, payroll registrations | B/BC |
| 8.9 | Corporate records update — stock ledger, minute books | BC |
| 8.10 | Purchase price allocation (IRC §1060 for asset deals) | SC/BC |

## Critical Checks

- **Version every distribution** — all parties must confirm current version
- **Flag long-lead items early** — landlord consents, regulatory approvals cannot wait until closing week
- **Sequencing** — funds flow memo requires all payoff letters; closing certs require covenant performance
- **Wire fraud** — verbal confirmation protocol for all wire instructions; never accept email-only changes
- **Legal opinions** — negotiate scope and reliance parties early to avoid closing delays
- **Good standing timing** — typically ≤30 days pre-closing; confirm with buyer's counsel and lender
- **FIRPTA** — foreign sellers require IRC §1445 withholding [VERIFY current rate]; seller may seek IRS withholding certificate
- **Bulk sales** — check UCC Article 6 / state statutes for asset deals [VERIFY applicable states]
- **Cross-reference** — tie each item to the specific purchase agreement section
- **Jurisdiction** — adapt for state transfer taxes, recording fees, merger statutes, and foreign filings
