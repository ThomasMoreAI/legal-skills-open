---
name: ucc-lien-release
title: Evidence of UCC Lien Release
description: Drafts Evidence of UCC Lien Release documents proving termination of security interests perfected under the Uniform Commercial Code. Extracts UCC-1 filing numbers, party information, and collateral descriptions from uploaded documents for compliant drafting. Use for UCC lien releases, UCC-3 termination evidence, security interest discharge certificates, or asset purchase closings requiring proof of clear title.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ucc-lien-release
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
tags: [agreement, drafting, transactional, certificate]
---

# Evidence of UCC Lien Release

Drafts a formal document proving termination of UCC security interests for closing binders, due diligence packages, and title verification.

## Prerequisites

1. **Original UCC-1 financing statement** — file number, filing date, jurisdiction, filing office
2. **Security agreement** — execution date, principal amount, collateral description
3. **Party details** — full legal names, entity types, jurisdictions of organization, addresses (secured party + debtor(s))
4. **UCC-3 termination statement** (if filed) — file number, filing date, file-stamped copy
5. **Payoff/satisfaction evidence** — payoff statements, wire confirmations, canceled checks, settlement documents
6. **UCC-3 amendments/continuations** (if any) — file numbers, dates, purposes

## Output Structure

### 1. Document Header

| Element | Detail |
|---|---|
| Title | "Evidence of UCC Lien Release" or "Certificate of UCC Lien Termination" |
| Date | Date of preparation |
| Secured Party | Full legal name, entity type, jurisdiction, address |
| Debtor(s) | Full legal name (including DBAs), entity type, jurisdiction, address |
| Original UCC-1 | File number, filing date, filing office (Secretary of State + state) |
| Amendments/Continuations | Each filing: file number, date, purpose |

Party names must match exactly as on the original UCC-1.

### 2. Secured Transaction Description

- Security agreement execution date and principal amount
- Collateral description — mirror the UCC-1 language exactly
- Article 9 classifications: equipment, inventory, accounts, chattel paper, instruments, general intangibles
- After-acquired property / proceeds / products scope
- Subsequent modifications to the secured obligation

### 3. Release and Termination Statement

```
[Secured Party] hereby unconditionally and irrevocably releases, terminates,
and fully discharges all security interests, liens, and claims in the
Collateral described herein, arising under or related to UCC-1 Financing
Statement No. [______], filed [date] with [filing office].

All obligations secured by the Financing Statement have been fully satisfied,
performed, and discharged. [Secured Party] claims no further interest in the
Collateral or any proceeds thereof.

Effective Date of Release: [date]
```

- **Partial release**: Clearly delineate what is released vs. what remains encumbered
- **UCC-3 termination**: State whether filed (file number + date) or to be filed, and by whom

### 4. Exhibits

Reference as labeled exhibits:

- [ ] Filed UCC-3 termination statement (file-stamped copy)
- [ ] Original UCC-1 financing statement
- [ ] UCC-3 amendments/continuations (chronological)
- [ ] Payoff statement from secured party
- [ ] Payment evidence (wire confirmations, canceled checks)
- [ ] Release/acknowledgment letter from secured party
- [ ] Court order, bankruptcy discharge, or settlement agreement (if applicable)

For complex filing histories, include a chronological summary table:

| # | Filing Type | File Number | Date | Purpose |
|---|---|---|---|---|
| 1 | UCC-1 | | | Original filing |
| 2 | UCC-3 | | | Amendment/Continuation/Termination |

### 5. Execution Block

- **Secured party signature line** — name, title, authority basis
- **Entity formalities**: Officer (corporation) or manager/authorized member (LLC)
- **Notary acknowledgment** — include if required by state law, document will be recorded, or jurisdictional custom dictates [VERIFY]
- **Certification statement**: Signatory affirms all information true, all obligations satisfied, no further amounts owed
- Debtor signature is optional (unilateral release is standard)

## Guidelines

- Cross-reference all names, file numbers, dates, and collateral descriptions exactly against original UCC filings
- Mirror UCC-1 collateral language verbatim — do not paraphrase
- Flag any missing or inconsistent filing details; request clarification before finalizing
- Multi-jurisdiction filings: address each jurisdiction separately with its own filing references
- Format for closing binders: sequential page numbering, title/date in footer, labeled exhibits
- Jurisdiction: US; state-specific notary and execution requirements vary [VERIFY]
