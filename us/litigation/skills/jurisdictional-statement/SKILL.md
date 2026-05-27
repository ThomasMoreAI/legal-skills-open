---
name: jurisdictional-statement
title: Jurisdictional Statement
description: Drafts jurisdictional statements for U.S. appellate courts establishing authority to hear an appeal, procedural compliance, and timeliness. Covers 28 U.S.C. §§ 1291/1292, FRAP Rule 4, state appellate rules, finality analysis, interlocutory exceptions, tolling, and cross-appeals. Use when preparing appellate filings, jurisdictional briefs, or responding to jurisdictional challenges.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/jurisdictional-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Jurisdictional Statement

Drafts a jurisdictional statement establishing appellate authority and procedural compliance to prevent dismissal for want of jurisdiction.

## Prerequisites

Gather before drafting:

- Final judgment or appealable order with docket entry number
- Filed notice of appeal with date stamp
- Full docket sheet (trial and appellate courts)
- Post-trial motions (if any) — FRCP 50/52/59 or state equivalents, with filing and disposition dates
- Applicable court rules — FRAP, local circuit rules, or state appellate rules
- All parties with appellate designations

## Quick Start

1. Identify the jurisdictional basis (§ 1291 final decision, § 1292 interlocutory, collateral order, etc.)
2. Build a timeliness timeline from judgment entry through notice of appeal
3. Verify deadline arithmetic: entry date + period = due date; filing date ≤ due date
4. Check for special issues (cross-appeals, multiple parties, standing)
5. Format caption and citations per the specific court's rules

## Drafting Workflow

### 1. Caption

Format per the appellate court's local rules. Include: full court name, all parties with appellate designations, both trial and appellate case numbers, and document title per court rules.

### 2. Basis for Jurisdiction

Identify the applicable grant of appellate jurisdiction:

| Basis | Authority | Scope |
|-------|-----------|-------|
| Final decision | 28 U.S.C. § 1291 | All claims, all parties disposed |
| Interlocutory — injunctions | 28 U.S.C. § 1292(a)(1) | Granting/refusing/modifying injunctions |
| Interlocutory — certified | 28 U.S.C. § 1292(b) | Controlling question of law, certified by district court |
| Collateral order | *Cohen v. Beneficial Indus. Loan Corp.*, 337 U.S. 541 (1949) | Conclusive, important question, effectively unreviewable |
| Partial final judgment | FRCP 54(b) | Express determination of no just reason for delay |
| Mandamus | 28 U.S.C. § 1651 | All Writs Act, extraordinary circumstances |

For state appeals, cite the specific state statute, constitutional provision, or court rule.

Then explain why the order falls within the cited grant. For final judgments, address finality. For interlocutory appeals, demonstrate the applicable exception with authority.

### 3. Timeliness

Build a chronological timeline:

```
[DATE] — Judgment/order entered (Dkt. No. ___)
[DATE] — Post-trial motion filed under FRCP ___ (if applicable)
[DATE] — Post-trial motion decided (if applicable)
[DATE] — Notice of appeal filed (Dkt. No. ___)
[DATE] — Filing deadline
```

**Federal deadlines (FRAP Rule 4):**

| Scenario | Deadline |
|----------|----------|
| Standard civil | 30 days from judgment entry |
| U.S. government party | 60 days from judgment entry |
| FRCP 50(b)/52(b)/59 motion pending | 30/60 days from disposition of last such motion |
| Criminal | 14 days from judgment entry |
| Cross-appeal | 14 days after first notice or within original deadline (whichever later) |

For state appeals, cite the exact rule and compute the deadline.

Address tolling from post-trial motions with rule citations. If notice was premature, cite FRAP 4(a)(2) (ripens upon entry) or *FirsTier Mortgage Co. v. Investors Mortgage Ins. Co.*, 498 U.S. 269 (1991) [VERIFY].

### 4. Special Issues

Address if applicable:

- **Multiple parties** — notice identifies all appellants and encompasses all claims on appeal
- **Cross-appeals** — separate jurisdictional basis and timeliness for each
- **Amended notices** — relation back under FRAP 4(a)(4)(B)(ii) or state equivalent
- **Jurisdictional defects** — assess curability and cite cure/waiver authority
- **Standing/mootness** — confirm Article III requirements remain satisfied
- **Sovereign immunity** — address if government entity is a party

### 5. Record Citations

Every factual assertion must cite to the appellate record per the court's format — federal: `(R. at ___)` or `(App. ___)`; state: per local requirements.

## Pitfalls

- **Finality traps** — unresolved counterclaims, pending fee motions, or unadjudicated parties defeat § 1291 finality
- **Late vs. premature** — premature is often curable; late is almost never curable — verify timing with extreme care
- **Local rules** — courts may require a separate jurisdictional statement or a section within the opening brief; check circuit/state-specific rules
- **Citation verification** — confirm statutes are current and cases are good law; mark uncertain citations with [VERIFY]
- **Format compliance** — minor formatting deviations can result in clerk rejection

---
