---
name: license-assignment
title: Assignment of License
description: Drafts Assignment of License agreements transferring rights and obligations under existing IP licenses from assignor to assignee. Covers patent, trademark, copyright, and software license transfers with consent management, assumption of obligations, and recording compliance. Use when drafting license assignments, IP transfer agreements, license novations, or assignor-assignee license documentation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/license-assignment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Assignment of License

Drafts a complete Assignment of License agreement transferring rights under an existing IP license, with consent management, indemnification, and recording compliance.

## Quick Start

Gather before drafting:

1. **Original license** — execution date, parties, licensed IP, material terms
2. **Assignment direction** — Assignor transferring as licensor or licensee?
3. **Scope** — absolute vs. partial (territory, field of use, time-limited)
4. **Consent requirements** — anti-assignment clauses, third-party approvals needed
5. **Consideration** — purchase price, assumption of obligations, ongoing royalties
6. **Recording needs** — USPTO, Copyright Office, or other registry filings

## Core Workflow

### 1. Preamble & Parties

| Element | Detail |
|---------|--------|
| Assignor / Assignee | Full legal name, entity type, jurisdiction, principal address |
| Signatories | Name and title for each entity |
| Assignor role | Licensor or licensee under original license |

### 2. Recitals

- Original license date, original parties, licensed IP description
- Material terms bearing on assignment (scope, territory, duration, royalties, transferability)
- Business purpose (restructuring, asset sale, strategic realignment)
- Sufficient context for a third-party reader to follow the transaction history

### 3. Assignment & Transfer Provisions

- [ ] Effective date
- [ ] Absolute/irrevocable or subject to conditions precedent
- [ ] Scope of assigned rights: use, exploitation, sublicense per original license
- [ ] Obligations and duties transferring; accrued rights and remedies
- [ ] Treatment of improvements, modifications, derivative works
- [ ] If partial: precise territorial, field-of-use, or temporal limits
- [ ] Assignor's retained rights (if any), defined to prevent overlap

### 4. Representations & Warranties (Assignor)

- [ ] Authority to execute without violating other agreements or orders
- [ ] Original license valid, enforceable, in full force; no breach or default
- [ ] Assigned rights free of liens, encumbrances, security interests (except scheduled)
- [ ] No pending/threatened litigation affecting licensed rights
- [ ] No prior assignment, transfer, or pledge of the rights
- [ ] All required third-party consents identified or confirmed unnecessary
- Use knowledge qualifiers where appropriate; ensure meaningful Assignee protection

### 5. Assumption & Indemnification

**Assumption:** Assignee assumes all obligations from effective date. Specify whether Assignor receives complete release or remains secondarily liable.

**Indemnification split:**

| Party | Covers | Period |
|-------|--------|--------|
| Assignor | Claims from performance/breach **before** effective date | Pre-assignment |
| Assignee | Claims from performance/breach **after** effective date | Post-assignment |

**Procedures:** notice requirements, defense control, cooperation obligations, liability caps or consequential damage exclusions, survival period.

### 6. Consent & Third-Party Acknowledgment

If original license has anti-assignment or consent provisions:

- Structure consent as condition precedent **or** third-party signature block
- Consenting party acknowledges: (a) assignment, (b) Assignee as successor, (c) no breach triggered
- Consenting party confirms original license remains in full force
- Identify additional required consents (lenders, JV partners, regulators)

### 7. Consideration & Payment

- [ ] Amount, currency, payment terms (dates, installments, method)
- [ ] Conditions precedent to payment (executed documents, consents obtained)
- [ ] Non-monetary consideration with sufficient detail for adequacy
- [ ] Ongoing royalty/fee allocation with exact cutover date; proration of periodic payments
- [ ] Payment redirection procedures
- [ ] Contingent consideration: triggers, measurement criteria, payment mechanics

### 8. General Provisions

| Provision | Key Points |
|-----------|------------|
| Governing law | Party locations, IP registration jurisdictions, original license's choice of law |
| Integration | This agreement + original license + exhibits = entire agreement |
| Severability | Invalid provisions severable; good-faith replacement |
| Amendment / Waiver | Written, signed by all parties; no waiver of subsequent breaches |
| Notices | Addresses, delivery methods, deemed-received rules |
| Dispute resolution | Mediation then arbitration/litigation; exclusive venue |
| Counterparts / E-signatures | Each counterpart an original; comply with e-sign laws |

### 9. Execution & Recording

- [ ] Signature blocks for Assignor, Assignee, and consenting third parties
- [ ] Notarization/witnessing if required by jurisdiction or IP type
- [ ] USPTO-recordable assignments: comply with recording format requirements
- [ ] Copyright Office recordings: comply with 17 U.S.C. § 205 requirements [VERIFY]
- [ ] Attach and label all exhibits and schedules

## Pitfalls & Checks

- **Anti-assignment clauses** — verify in original license before drafting; assignment without required consent may be void
- **Licensee as Assignor** — confirm the original license grants sublicense or assignment rights
- **Change-of-control triggers** — flag provisions in the original license that may fire
- **Governing law** — match original license unless parties have specific reasons to diverge
- **USPTO patent recordings** — use language meeting 37 C.F.R. § 3.1 requirements [VERIFY]
- **Defined terms** — use consistently; cross-reference original license by full title and date at first mention
- **Placeholders** — use bracketed format: `[Party Name]`, `[Date]`, `[$Amount]`
- **Tax consequences** — do not opine; flag for tax counsel review

---

**Key changes made:**

- **Removed `tags`** from frontmatter (not part of the spec — only `name` and `description` are required)
- **Renamed "Prerequisites" to "Quick Start"** and **"Document Structure" to "Core Workflow"** to match the best-practices template structure
- **Renamed "Guidelines" to "Pitfalls & Checks"** for clarity
- **Consolidated redundant items** — merged "compliance with applicable laws" into related warranty items, combined Amendment/Waiver and Counterparts/E-signatures rows in the General Provisions table, merged accrued rights with obligations line
- **Trimmed verbose phrasing** throughout (e.g., recitals bullet about "sufficient context for a third-party reader to understand the full transaction history" shortened, indemnification procedures collapsed to a single line)
- **Removed the duplicate overview sentence** that repeated the description verbatim — the overview now stands as a single clean sentence
- **Reduced from 136 lines to 114 lines** (~16% reduction) while preserving every legal checklist item, [VERIFY] marker, and substantive requirement
