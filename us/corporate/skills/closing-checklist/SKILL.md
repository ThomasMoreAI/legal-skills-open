---
name: closing-checklist
title: M&A Closing Checklist
description: Drafts M&A closing checklists tracking documents, approvals, consents, and action items from signing through post-closing. Use when coordinating closings for mergers, acquisitions, stock purchases, asset deals, or any corporate transaction requiring multi-party document tracking and funds flow management.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/closing-checklist
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# M&A Closing Checklist

Generates a transaction-specific closing checklist covering corporate authorizations, transaction documents, third-party consents, regulatory filings, funds flow, and post-closing obligations.

## Prerequisites

Before drafting, collect:

1. **Definitive agreement** — purchase/merger agreement with all schedules
2. **Transaction structure** — stock purchase, asset purchase, or merger
3. **Party information** — legal names of buyer, seller, target, escrow agent
4. **Closing logistics** — date, time (with timezone), location or virtual platform
5. **Material contracts** — contracts with change-of-control or consent provisions

## Quick Start

Format every checklist with:

- **Header**: transaction name, parties, closing date/time/method
- **Party legend**: abbreviations (BC = Buyer's Counsel, SC = Seller's Counsel, B = Buyer, S = Seller, EA = Escrow Agent; expand as needed)
- **Item matrix**: `# | Description | Responsible | Cross-Ref (§) | Status`
- **Status stages**: `Draft → Review → Negotiation → Execution → Delivered`

## Checklist Sections

### I. Corporate Authorization

- [ ] Good standing certificates (buyer + seller jurisdictions, dated ≤30 days pre-closing)
- [ ] Board resolutions authorizing transaction (both parties)
- [ ] Shareholder/member approval (if required by governing docs or state law)
- [ ] Certified organizational documents (articles, bylaws/operating agreement)
- [ ] Preferred shareholder, option holder, or warrant holder consents
- [ ] Secretary's certificates authenticating org docs, resolutions, and incumbency

### II. Transaction Documents

**All structures:**
- [ ] Definitive agreement (fully executed with disclosure schedules)
- [ ] Escrow agreement (amount, duration, release conditions, claims procedures)

**Asset purchases — add:**
- [ ] Bill of sale, assignment and assumption agreement
- [ ] Real property deeds/transfer documents
- [ ] IP assignments (patents, trademarks, copyrights, domains + registration formalities)

**Stock purchases — add:**
- [ ] Stock certificates with legends or book-entry transfer docs
- [ ] Stock powers/transfer instruments
- [ ] Director/officer resignations and replacement appointments

**Mergers — add:**
- [ ] Certificate/articles of merger (ready for state filing)
- [ ] Director/officer resignations and appointments

### III. Ancillary Agreements

- [ ] Legal opinions (both counsels — existence, authority, enforceability, no conflicts)
- [ ] Payoff letters + lien releases for all indebtedness (must specify: payoff amount, wire instructions, UCC-3 terminations/mortgage releases)
- [ ] Employment agreements for continuing key employees
- [ ] Non-compete/non-solicitation agreements (comply with state enforceability law)
- [ ] Transition services agreement (scope, duration, fees, SLAs, termination)
- [ ] Other commercial agreements (supply, distribution, licensing)

### IV. Consents & Regulatory

- [ ] Third-party contract consents (all change-of-control/assignment restrictions)
- [ ] HSR Act filing (if thresholds met — track filing date, second requests, waiting period)
- [ ] State antitrust/competition filings
- [ ] Industry-specific regulatory approvals (healthcare, financial services, telecom)
- [ ] Foreign investment review (CFIUS or equivalent)
- [ ] Landlord consents for lease assignments (submit early — extended review typical)
- [ ] Franchisor/licensor approvals

### V. Closing Certificates

- [ ] Seller's officer certificate (rep/warranty bring-down, covenant compliance)
- [ ] Buyer's officer certificate (parallel certifications)
- [ ] Secretary's certificates (both parties — org docs, resolutions, incumbency)
- [ ] Bring-down/MAC certificate (no material adverse change since signing)
- [ ] Tax certificates: W-9 (domestic), FIRPTA under IRC § 1445 (foreign seller), state withholding

### VI. Funds Flow

Prepare a **funds flow memorandum** itemizing: base purchase price, working capital adjustment, escrow deposits (indemnification + earnout), creditor payoffs, transaction expenses (both sides), transfer taxes, and net proceeds to seller. Each line: amount, payee, wire instructions.

- [ ] Wire instructions verified via verbal callback (fraud prevention)
- [ ] Closing/settlement statement for tax reporting

### VII. Post-Closing

- [ ] File certificate of merger (coordinate effective time)
- [ ] Press release (both parties approve; securities law compliance if public)
- [ ] Counterparty notices (customers, suppliers, landlords, lenders)
- [ ] Government filings: HSR notifications, transfer tax returns, bulk sale compliance, license/permit updates, tax authority notifications
- [ ] Corporate record updates (stock ledger, minute books)
- [ ] Asset recording on buyer's books; assumed liability entries

## Pitfalls & Checks

- **Cross-reference every item** to the purchase agreement section creating the obligation
- **Map dependencies** — funds flow requires payoff letters; certificates require covenant completion; sequence accordingly
- **Build lead time** for third-party items (landlord consents, regulatory approvals, lien releases)
- **Version control** — timestamp each circulation; one party maintains the master
- **Jurisdiction-specific** — research state variations for transfer taxes, bulk sale laws, and corporate formalities
- **Wire fraud** — require verbal verification of any wire instruction changes; confirm receipt of all transfers
- **Omit inapplicable sections** — tailor to transaction structure rather than including placeholders
