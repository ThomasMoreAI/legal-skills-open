---
name: shareholder-agreement
title: Shareholder Agreement
description: 'Drafts U.S. shareholder agreements governing ownership, control, transfers, valuation, and exits with enforceable governance and dispute frameworks. Use when drafting or updating shareholder/stockholder agreements, ROFR and buy-sell terms, drag-along/tag-along rights, founder vesting, or closely held governance. Trigger keywords: shareholder agreement, stockholder agreement, ROFR, tag-along, drag-along, buy-sell, cap table, founder vesting.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/shareholder-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Shareholder Agreement

Drafts a company-specific shareholder agreement aligned to the charter, bylaws, and applicable state law.

## Prerequisites

1. Jurisdiction of incorporation and entity type (corp vs. close corp).
2. Current charter and bylaws (with amendments).
3. Cap table by class/series with ownership percentages and special rights.
4. Shareholder roster with roles (founder, investor, employee, passive).
5. Governance model and approval thresholds.
6. Transfer/exit objectives (liquidity controls, buy-sell triggers).
7. Dispute resolution preference (court vs. arbitration).
8. Restrictive covenant policy and enforceability constraints.

## Output Structure / Process

**Draft Order**

1. Parties, recitals, effective date, document hierarchy.
2. Definitions.
3. Capitalization and preemptive rights.
4. Governance and voting.
5. Information and inspection rights.
6. Transfer restrictions and liquidity mechanisms.
7. Valuation and purchase mechanics.
8. Restrictive covenants and confidentiality.
9. Dispute resolution.
10. Exit events, change of control, IPO termination.
11. General provisions.
12. Schedules, exhibits, signature blocks.

**Required Inputs**

| Item | Notes |
| --- | --- |
| Company legal name, state, incorporation date | Match charter |
| Principal place of business | For venue and notices |
| Shareholder roster | Full legal names/entities |
| Cap table | Class, series, votes, preferences |
| Board structure | Seats, designation rights |
| Approval thresholds | Board vs. shareholder levels |
| Transfer restrictions | ROFR, permitted transfers |
| Exit mechanics | Drag/tag, sale of control |
| Valuation method | FMV, formula, appraisal |
| Payment terms | Cash vs. note |
| Dispute resolution | Negotiation/mediation/arbitration |
| Restrictive covenants (optional) | State-law dependent |

**Governance Approval Matrix**

| Action | Board | Shareholder |
| --- | --- | --- |
| Amend charter/bylaws | Supermajority | Supermajority |
| Issue new equity | Supermajority | Majority |
| Debt above $X | Majority | N/A |
| M&A / sale of assets | Supermajority | Supermajority |
| Related-party transactions | Majority (disinterested) | Majority |
| Hire/terminate CEO | Majority | N/A |

**Core Clause Checklist**

- [ ] Parties, recitals, effective date, hierarchy vs. charter/bylaws
- [ ] Definitions: Affiliate, Transfer, Permitted Transferee, FMV, Change of Control, Cause, Good Reason
- [ ] Capitalization schedule with class/series rights
- [ ] Preemptive rights or explicit waiver
- [ ] Board composition and designation rights
- [ ] Shareholder voting by class and written consent
- [ ] Meeting notice, quorum, remote participation
- [ ] Information and inspection rights
- [ ] ROFR with process timelines
- [ ] Co-sale (tag-along) and drag-along mechanics
- [ ] Permitted transfers and joinder requirement
- [ ] Involuntary transfer treatment (death/divorce/bankruptcy)
- [ ] Valuation method and appraisal dispute mechanics
- [ ] Payment terms: down payment, note terms, interest
- [ ] Restrictive covenants and confidentiality (if enforceable)
- [ ] Dispute resolution ladder and carve-outs
- [ ] Exit events, IPO termination, dissolution
- [ ] Notices, amendments, severability, waiver
- [ ] Spousal consent if applicable

**Key Clause Language**

Hierarchy — Agreement supplements Charter and Bylaws. Conflict order: Charter → this Agreement → Bylaws, to the extent permitted by law.

ROFR — Selling shareholder delivers written notice (transferee, shares, price, terms). Company has [30] days to elect; if declined, non-selling shareholders have [30] days pro rata with oversubscription.

Tag-along — If holders of >[50]% propose a transfer, each other shareholder may participate pro rata on identical terms within [10] days.

Drag-along — Upon >[X]% voting power approval, all shareholders sell on same terms; pro rata escrow/indemnity capped at proceeds.

Valuation — FMV by [method]. Appraisal dispute: parties choose appraiser within [15] days, else [ASA/JAMS] appoints. Complete within [60–90] days. Discounts for lack of control/marketability: [include/exclude].

Note terms — Deferred price over [3–5] years at [AFR + X%], prepayable, secured by purchased shares, default accelerates.

Restrictive covenants — Non-compete/non-solicit for [active shareholders], [12–24] months, [defined territory/business]. Confidentiality [3–5] years; trade secrets indefinitely.

Dispute resolution — Notice → executive meeting [15] days → mediation [60] days → [arbitration/court]. Equitable relief for confidentiality, noncompete, transfer restrictions.

**Schedules / Exhibits**

- Schedule A: Capitalization Table
- Schedule B: Shareholder Contact Information
- Exhibit 1: Form of Joinder
- Exhibit 2: Form of Promissory Note
- Exhibit 3: Spousal Consent (if applicable)

**Quality Checks**

- [ ] Defined terms consistent; no undefined capitalized terms
- [ ] Cross-references accurate
- [ ] Charter/bylaws conflict check completed
- [ ] Transfer restrictions comply with state statute
- [ ] Noncompete/nonsolicit enforceability confirmed for jurisdiction
- [ ] Arbitration clause and carve-outs consistent
- [ ] Signature blocks match entity authority

## Guidelines

- Confirm state corporate statute requirements for transfer restriction enforceability.
- Avoid unreasonable restraints on alienation; document legitimate business purpose.
- Limit restrictive covenants to enforceable scope; exclude restricted jurisdictions unless narrowed to trade secrets.
- Coordinate founder/employee vesting with equity plan and tax counsel for 83(b) timing.
- Ensure securities law compliance for private transfers and certificate legends.
- Use spousal consent in community property states.
- Do not override mandatory charter provisions or statutory minority protections.
- Use conspicuous jury trial waiver only if enforceable in jurisdiction.
