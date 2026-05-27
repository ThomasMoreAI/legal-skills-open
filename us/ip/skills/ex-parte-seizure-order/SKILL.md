---
name: ex-parte-seizure-order
title: Ex Parte Seizure Order
description: Drafts U.S. ex parte seizure orders authorizing immediate property or asset seizure without notice. Enforces the four-factor ex parte standard, FRCP 65, Lanham Act seizure provisions (15 U.S.C. § 1116(d)), bond requirements, and due process safeguards. Use when drafting ex parte seizure orders, TRO-based asset seizure, or IP counterfeiting seizure orders in federal or state court.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/ex-parte-seizure-order
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Ex Parte Seizure Order

Drafts a court-ready ex parte seizure order with findings, scope, bond, and due process provisions for IP or asset-based litigation.

## Prerequisites

Collect before drafting:

- **Case caption** — court, division, case number, parties with procedural designations
- **Factual record** — declarations, investigative reports, or financial records establishing urgency (dissipation risk, destruction, irreparable harm)
- **Property description** — physical descriptions, serial numbers, locations, valuations, or digital/IP asset identifiers
- **Legal basis** — Lanham Act § 34(d) / 15 U.S.C. § 1116(d) for counterfeiting; FRCP 65 for TRO-based seizure; or state analog
- **Executing party** — U.S. Marshals, local law enforcement, court-appointed receiver, or PI with law enforcement escort
- **Bond amount** — security covering seized property value plus anticipated business interruption damages

## Order Structure

### 1. Caption and Title

Standard case caption followed by "EX PARTE SEIZURE ORDER."

### 2. Recitals

- Date/time of application; note no appearance by defendant
- Documents reviewed (motion, memorandum, declarations, exhibits)
- Finding that notice would defeat relief (specify destruction/concealment risk)

### 3. Findings of Fact — Four-Factor Analysis

Each factor requires a specific finding with record citations:

| Factor | Required Finding |
|--------|-----------------|
| Likelihood of success | Prima facie case established — cite Decl. ¶ ___, Ex. ___ |
| Irreparable injury | Delay causes destruction/dissipation/ongoing IP harm |
| Inadequacy of other remedies | Monetary damages and ordinary process insufficient |
| Balance of hardships | Plaintiff's harm from denial exceeds defendant's harm from grant |

**Lanham Act counterfeiting seizures** require additional findings under § 1116(d)(4)(B): (a) defendant would destroy/hide goods if notified; (b) plaintiff has not publicized the application; (c) court has subject-matter jurisdiction. Always verify current statutory text.

### 4. Seizure Provisions

**Property** — list with particularity:
- Category, physical description, serial/model numbers
- Location(s) with address, unit, access hours
- Digital assets: specify forensic imaging method and access limitations

**Executing parties** — identify authorized agents (Marshals, local law enforcement, receiver, counsel with escort)

**Execution parameters:**
- Permissible hours (e.g., 6:00 a.m.–10:00 p.m.)
- Entry conditions (peaceable; forced entry only if specified condition met)
- Inventory requirement: itemized list with photographic documentation
- Minimize interference with non-seized operations

**Effective period** — specify start date/time through expiration date/event.

### 5. Chain of Custody and Storage

- Custodian/facility for seized items
- Preservation conditions (perishable goods, digital forensic images)
- Access restricted to specified parties pending further order

### 6. Bond and Security

- Plaintiff posts bond of $[AMOUNT] with Clerk by [DATE/TIME] as condition of order taking effect
- Failure to post bond: order automatically vacated

### 7. Post-Seizure Notice and Hearing

- Serve defendant within 24–48 hours of execution with copy of order, motion, and all supporting papers
- Adversarial hearing no later than 14 days post-seizure
- Defendant may move to dissolve or modify on showing of changed circumstances or wrongful seizure
- Counter-bond option: defendant posts $[AMOUNT] to regain possession pending final resolution

### 8. Prohibitions and Safeguards

- No unnecessary damage during seizure
- No seizure of property outside described categories
- No review of seized materials by plaintiff/agents until further order

### 9. Signature Block

Standard judicial signature block with date, judge name, title, and court.

## Pitfalls and Checks

- **Property specificity** — vague descriptions are grounds for quashing; err toward maximum detail
- **Lanham Act vs. FRCP 65** — distinct frameworks; confirm which applies and include correct statutory findings
- **Bond adequacy** — must reflect realistic value of all seized property plus business interruption; underestimating creates wrongful seizure liability
- **14-day hearing** — due process floor; never omit scheduling or noting this requirement
- **Digital assets** — include specific forensic preservation protocol; generic "seize computers" language is routinely challenged
- **State court** — verify analogous state seizure statute and local rules for divergent bond/notice requirements
- **No ex parte contact** — order application must not be disclosed to opposing party or counsel before entry
- **Senior review** — required before filing; due process errors risk sanctions or fee-shifting
