---
name: corporate-bylaws
title: Corporate Bylaws
description: Drafts complete U.S. corporate bylaws harmonized with Articles of Incorporation and tailored to state statute (Delaware GCL, MBCA, or state-specific). Use for new corporation formations, governance overhauls, or updating existing bylaws for closely-held or emerging-growth corporations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/corporate-bylaws
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting, research]
---

# Corporate Bylaws

Produces a complete, internally consistent set of bylaws matched to the corporation's Articles, jurisdiction, ownership structure, and governance philosophy.

## Prerequisites

1. **Articles of Incorporation** — filed copy; extract: legal name, state, authorized share classes/counts, par value, liability/indemnification provisions, bylaw amendment restrictions
2. **State statute** — identify jurisdiction; research mandatory vs. default provisions, notice periods, quorum floors, virtual meeting rules, indemnification scope
3. **Governance intake** — ownership structure (closely-held vs. dispersed), IPO plans, board size/structure, voting standard preference, cumulative voting stance, written consent policy, officer positions

## Quick Start

Draft bylaws using Articles I–IX below. Flag unresolved choices with `[CLIENT CHOICE]` and statutory questions with `[VERIFY: jurisdiction]`.

## Article Structure

### I — Corporate Identity

- **Name**: exact match to filed Articles including designator
- **Purpose**: general business clause unless professional/benefit corp requires specificity
- **Principal office**: full address; board may relocate without amendment
- **Registered office**: distinguish from principal; reference statutory agent

### II — Shareholders

**Meetings**
- Annual: board-determinable date within 13 months of prior; in-person/virtual/hybrid `[VERIFY: jurisdiction]`
- Special: called by board, Chair, CEO, or shareholders holding `___`% (10% closely-held; 25%+ dispersed)

**Notice**: 10–60 days (verify state floor); state date/time/place; special meetings must describe purpose; specify deemed-given rules per delivery method

**Quorum & Voting**
- Quorum: majority of outstanding voting shares (may reduce to 1/3 in most states)
- Routine matters: majority of shares present at quorum
- Fundamental transactions: majority or supermajority of all outstanding `[CLIENT CHOICE]`
- Cumulative voting: include mechanics or expressly disclaim `[CLIENT CHOICE]`

**Proxies**: written or electronic; 11-month default duration; revocable unless coupled with interest

**Written Consent**: permitted or prohibited `[CLIENT CHOICE]` — prohibit if IPO anticipated; if permitted, specify threshold and notice to non-consenting shareholders

### III — Board of Directors

**Composition**: fixed number or range with board discretion `[CLIENT CHOICE]`

**Structure**

| Type | Use Case |
|---|---|
| Unitary (annual) | Shareholder accountability; preferred for closely-held |
| Classified (2–3 yr terms) | Continuity; takeover defense |

**Voting standard**: plurality (seats always filled) or majority with resignation/holdover policy `[CLIENT CHOICE]`

**Removal**: with or without cause `[CLIENT CHOICE]`; majority or supermajority of outstanding shares

**Meetings**: quarterly minimum for regular (no notice if pre-scheduled); special called by Chair, CEO, or 2 directors; quorum = majority of directors in office; action = majority present; remote permitted; unanimous written consent in lieu

**Conflicts**: mandatory disclosure; interested director abstains; safe harbor = disinterested director/shareholder approval `[VERIFY: jurisdiction]`

### IV — Officers

**Required** (verify state minimums): President/CEO, Secretary, Treasurer/CFO

**Authorities**

| Officer | Core Authority |
|---|---|
| CEO/President | General supervision; execute contracts within board thresholds; hire/terminate |
| Secretary | Minutes, stock ledger, notices, record authentication, seal custody |
| CFO/Treasurer | Funds custody, financial records, banking, checks/EFTs within board limits |

Board may create additional positions by resolution. Board may remove any officer with or without cause (does not affect employment contract rights).

### V — Committees

Formed by board resolution. **Non-delegable functions** (statutory): amend Articles/bylaws, approve mergers/asset sales, declare dividends, authorize shares beyond limits, fill board vacancies (check state law).

**Standing committees to consider**: Audit (financial integrity, auditor oversight), Compensation (executive pay, equity plans), Nominating/Governance (candidates, evaluations) — all composed of independent directors.

### VI — Capital Stock

- **Form**: certificated or uncertificated book-entry `[CLIENT CHOICE]`
- **Issuance**: per board resolution within Articles limits
- **Transfers**: record in stock ledger; require proper endorsement; may refuse non-compliant transfers
- **Lost certificates**: affidavit + indemnity bond (`___`× value) + replacement fee

### VII — Indemnification

- **Mandatory**: directors/officers wholly successful on merits — indemnify all expenses
- **Permissive**: directors, officers, may extend to employees/agents — requires good faith standard (civil: best interests; criminal: no reasonable cause to believe unlawful)
- **Prohibited**: liability to corporation in derivative action; improper personal benefit
- **Expense advancement**: mandatory or permissive `[CLIENT CHOICE]`; require repayment undertaking (need not be secured)
- **D&O insurance**: explicitly authorize, including unindemnifiable liabilities
- **Savings clause**: rights non-exclusive; maximum protection permitted by law

### VIII — Financial and Administrative

- **Fiscal year**: calendar or `___`; board may change by resolution
- **Books/records**: maintain at principal office; identify shareholder inspection rights per statute
- **Contract execution**: tiered approval thresholds (officer / CEO / board) by dollar amount
- **Checks/EFTs**: designated officers; co-signature above `$___`
- **Seal**: optional; authorize use and custody

### IX — Amendments

| By | Vote | Scope |
|---|---|---|
| Board | Majority at quorum | All unless Articles reserve to shareholders |
| Shareholders | Majority of outstanding (supermajority for protected provisions) | All |

Supermajority protection (2/3 or 3/4) for: indemnification, quorum floors, fundamental transaction thresholds, amendment provision itself `[CLIENT CHOICE]`. Verify Articles for restrictions on board amendment authority.

## Checks

- **Articles supremacy**: cross-check every provision — Articles prevail in any conflict
- **Mandatory vs. default**: only opt out of defaults with specific governance reason
- **Closely-held vs. dispersed**: simplify formalities for closely-held (lower quorums, broader consent); tighten for dispersed
- **IPO readiness**: if anticipated, align with NYSE/Nasdaq standards — prohibit written consent, adopt majority voting, expand independent director requirements
- **Internal consistency**: verify all cross-references, defined terms, quorum thresholds, notice periods, and voting standards
- **Citations**: mark all statutory references with `[VERIFY]` — do not assert section numbers without confirming current codification
- **Jurisdiction**: Delaware GCL differs materially from MBCA defaults — confirm applicable statute before drafting
