---
name: intercreditor-agreement
title: Intercreditor Agreement (Lien Priority)
description: Drafts a first lien/second lien intercreditor agreement governing creditor priority, enforcement rights, and payment waterfalls over shared collateral. Follows LSTA and ABA market-standard conventions. Use when drafting intercreditor agreements, lien subordination agreements, first lien/second lien arrangements, or creditor priority documents in loan and financing transactions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/intercreditor-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Intercreditor Agreement (Lien Priority)

Drafts an intercreditor agreement establishing absolute lien priority between first lien and second lien creditors over shared collateral, incorporating LSTA-standard subordination, standstill, waterfall, turnover, and bankruptcy provisions.

## Prerequisites

Collect before drafting:

1. **First lien credit agreement** — loan amounts, maturity, rates, collateral descriptions
2. **Second lien credit agreement** — same for junior facility
3. **Security agreements** — perfection status, filing details, collateral schedules
4. **Borrower organizational documents** — entity type, jurisdiction
5. **Existing intercreditor/subordination arrangements** (if any)

## Quick Start

Draft all articles in order. Extract obligation amounts, maturity dates, and collateral descriptions from uploaded transaction documents. Mark any statutory citations not independently verified with `[VERIFY]`.

## Output Structure

### Article I — Recitals & Definitions

Establish context referencing both credit facilities and shared collateral. Required defined terms:

| Term | Scope |
|---|---|
| First Lien Obligations | Principal, interest (including post-petition), fees, expenses, indemnities |
| Second Lien Obligations | Same scope for second lien docs |
| Collateral | All shared collateral securing both obligation sets |
| Lien Priority | Absolute first lien superiority regardless of attachment/perfection order |
| Standstill Period | Typically 180 days, triggered by payment default or EOD under first lien docs |
| Discharge of First Lien Obligations | Full payment; cash pay, L/C termination, hedge unwind conditions |
| Insolvency Proceeding | Bankruptcy Code proceedings, receivership, assignment for benefit of creditors, foreign equivalents |

### Article II — Lien Priority & Subordination

- [ ] Absolute first lien priority regardless of attachment/perfection order
- [ ] Subordination covers principal, pre/post-petition interest, fees, expenses, all amounts
- [ ] Priority applies to voluntary payments, enforcement, bankruptcy, collateral dispositions
- [ ] Continues until Discharge of First Lien Obligations
- [ ] Second lien holder may not contest priority or seek equitable subordination

### Article III — Enforcement Rights & Standstill

**First lien holders may** (no second lien consent required):
- Enforce all remedies against collateral
- Accept/reject DIP financing proposals
- Vote on reorganization plans
- Exercise all secured creditor rights

**Second lien holders may NOT during Standstill Period:**
- Accelerate obligations or exercise collateral remedies
- Object to first lien enforcement actions
- Interfere with first lien rights
- Seek adequate protection for second lien interests

**Post-standstill:** Specify limited second lien actions available if first lien enforcement remains incomplete.

### Article IV — Payment Waterfall & Turnover

**Distribution priority (all collateral proceeds):**
1. First Lien Obligations — pay in full
2. Second Lien Obligations — remainder

**Turnover obligations:**
- Immediate remittance of payments received in violation of priority (regardless of knowledge)
- Turned-over amounts treated as first lien collateral proceeds
- Covers borrower payments, collateral proceeds, bankruptcy distributions, all other sources

**Address specifically:** cash collateral use in bankruptcy, adequate protection payments, distributions under confirmed reorganization plans.

### Article V — Representations & Warranties

Mutual representations from both lien holders:

- [ ] Due organization and authority
- [ ] No conflicts with organizational docs or other agreements
- [ ] Valid and perfected security interests
- [ ] All actions taken to establish and maintain lien priority
- [ ] No side agreements contradicting priority scheme
- [ ] Transaction-specific reps (verify against uploaded credit/security docs)

### Article VI — Covenants

**Notice requirements:** Prompt notice of amendments affecting collateral, obligations, or relative rights.

**Second lien amendment restrictions — may not:**
- Increase principal or accelerate maturity
- Increase rates beyond specified thresholds
- Restrict borrower's ability to satisfy first lien obligations

**Bankruptcy coordination:** Proofs of claim, plan voting, DIP financing/asset sale consent.

**Ongoing:** Maintain perfection, cooperate on documentation, precise notice mechanics (addresses, methods, timing).

### Article VII — Bankruptcy & Insolvency

- Agreement constitutes "subordination agreement" under Section 510(a) `[VERIFY]`
- Enforceable before, during, and after any bankruptcy case
- Second lien holders will not oppose first lien motions for stay relief, adequate protection, or cash collateral use
- First lien holders have exclusive DIP financing and cash collateral rights
- Second lien holders may not seek adequate protection unless first lien holders also receive it
- Address post-petition interest and Section 510(c) exception `[VERIFY]`
- Enforceable against trustee or debtor-in-possession

### Article VIII — Miscellaneous

| Provision | Standard |
|---|---|
| Governing law | Specify jurisdiction (typically NY) |
| Amendments | Written consent of all parties |
| Severability | Invalid provisions severable |
| Integration | Supersedes all prior understandings |
| Counterparts | Electronic delivery permitted |
| Successors & assigns | Binding; include assignment mechanics |
| Third-party beneficiaries | None (or specify borrower rights) |
| Jury trial waiver | Mutual waiver |
| Jurisdiction & service | Submission to specified courts |
| Borrower consent | Whether amendments require borrower consent |
| Termination | Conditions for agreement termination |

## Drafting Checks

- [ ] Follow LSTA Model First Lien/Second Lien Intercreditor Agreement conventions
- [ ] Every defined term appears in operative provisions and vice versa
- [ ] Internal cross-references are accurate
- [ ] Consistent capitalization of defined terms throughout
- [ ] Jurisdiction-specific UCC or Bankruptcy Code variations flagged
- [ ] No enforceability opinions — present as drafted terms for counsel review
- [ ] If collateral includes real property, address mortgage subordination separately
- [ ] All unverified statutory citations marked `[VERIFY]`
