---
name: tx-smith-county-jp-codearranger
title: Smith County Justice Court (Tyler, Texas)
description: 'Use for a Justice of the Peace ("JP") / Justice Court matter in Smith County, Texas (county seat Tyler) — small-claims, debt-claim, and eviction (forcible detainer) cases in a Smith County precinct, and the de novo appeal to a Smith County Court at Law. Triggers: "Smith County Justice Court", "Tyler Texas JP court", "sued in Smith County precinct", "Smith County eviction", "Smith County small claims", "Smith County debt claim", "Smith County JP precinct", "Smith County Precinct 1 / 2 / 3 / 4 / 5", "Justice of the Peace Tyler", "appeal Smith County JP to county court at law", "Smith County Place 1 Place 2". Layers on top of `tx-justice-courts` (the statewide TRCP Part V, Rules 500–510 framework) and `tx-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-smith-county-jp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Smith County Justice Court (Tyler, Texas)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Smith County's
> precinct/place layout, the assigned Justice of the Peace, and local
> filing practices change; verify with the specific Smith County JP
> precinct and the current TRCP Part V before relying on anything
> here. A default judgment or a missed eviction-appeal deadline has
> fast, real consequences — respond promptly and consider consulting
> a licensed Texas attorney or a legal-aid clinic.

Use this skill when the matter is in a **Smith County Justice Court**
— the court of a **Justice of the Peace** sitting in a Smith County
**precinct**. Smith County's county seat is **Tyler**. This
skill **layers on top of** `tx-justice-courts` (which carries the
statewide **TRCP Part V, Rules 500–510** framework) and
`tx-statewide-format`. Read those for the rules that control;
everything below is the Smith County overlay.

## The Smith County JP precincts

Smith County is divided into **Justice of the Peace precincts** —
commonly **Precinct 1, 2, 3, 4, and 5** — and some precincts have a
**Place 1 / Place 2** (each Place with its own elected Justice of the
Peace and clerk). **Confirm the current precinct/place layout and the
assigned Justice of the Peace with Smith County** before filing or
answering — the precinct count and the Place divisions change, and
**venue within the county** generally lies in the precinct where the
defendant resides or where the eviction premises is located (confirm
the applicable venue rule, TRCP 502.4 / 510.4, and the correct
precinct).

## What the Smith County Justice Courts hear

The Smith County JP courts hear the same matters as every Texas
Justice Court, under **TRCP Part V**:

- **Small-claims** money cases up to the statutory ceiling;
- **Debt-claim cases (TRCP 508)** — most consumer-debt collection
  suits in the county, including those by debt buyers and collectors;
- **Eviction (forcible entry and detainer) (TRCP 510)** — expedited,
  with the **5-day** appeal track;
- **Repair-and-remedy (TRCP 509)**.

The **monetary ceiling** is statutory and **drift-prone** — confirm
the current cap against **Tex. Gov't Code § 27.031** and **TRCP
500.3** via `tx-law-references` (and see `tx-justice-courts`). The
**TRCP 500.3(e)** quirk applies fully: the ordinary rules of civil
procedure and the rules of evidence do **not** apply in the Smith
County Justice Court except as Part V incorporates them.

## Answer deadline and default

The defendant's **answer is due by the end of the 14th day after
service of citation (TRCP 502.5)** — the simplified Justice Court
deadline, **not** the District-Court "Monday rule." File the answer
(a general denial suffices to put the plaintiff to its proof) before
the deadline to avoid a **default judgment under TRCP 503**. Confirm
the current 14-day figure against the corpus. See `tx-justice-courts`
and `tx-first-30-days`.

## Eviction practice in the precinct

Eviction suits in a Smith County precinct run on the compressed
**TRCP 510** timeline — a quick trial setting after service (the
landlord must first have given the **Tex. Prop. Code Ch. 24** notice
to vacate), and a **5-day** appeal window to the county court, with
the rule's **pay-rent-into-the-registry** conditions for a tenant who
appeals to stay in possession. **Confirm the current 5-day deadline
and pay-rent conditions against TRCP 510** — missing them forfeits
the appeal and possession. See `tx-justice-courts`, `tx-deadlines`,
and `tx-post-judgment`.

## Debt-claim practice in the precinct

Smith County JP debt-claim cases (TRCP 508) are the everyday forum
for consumer-debt collection in the county. The simplified procedure
means a plaintiff may try to prove up the account without
higher-court evidentiary formalities — scrutinize the plaintiff's
proof, the **chain of title** from the original creditor through each
assignee, the **four-year limitations** posture, and the **Texas Debt
Collection Act / DTPA** overlay. The substantive defenses live in
`tx-consumer-debt`; the JP-court mechanics live in
`tx-justice-courts`.

## Filing — eFileTexas plus the precinct clerk

Smith County e-files through **eFileTexas.gov** (Odyssey File &
Serve). A self-represented filer may e-file or file with the **precinct
clerk** in person — confirm the precinct's accepted methods, the
filing fee, and the **Statement of Inability to Afford Payment of
Court Costs** option with the specific precinct. The assisted
self-help front end is **TexasLawHelp.org**, which hosts the JP-court
forms (answer, Statement of Inability, eviction answer, appeal).

## De novo appeal to a Smith County Court at Law

A party who loses in a Smith County Justice Court may appeal **de
novo** — a brand-new trial — to a **Smith County Court at Law** (the
county court that hears JP appeals under the county's structure;
confirm which county court takes the appeal). The appellant perfects
the appeal under **TRCP 506** (ordinary civil) or **TRCP 510**
(eviction, the **5-day** track) by filing an appeal bond, a cash
deposit, or a Statement of Inability to Afford Payment within the
deadline. The destination court and its procedure live in
`tx-county-courts`.

## Smith County's higher-tier courts belong to other skills

This skill covers **only** the Smith County **Justice (JP) Courts**.
Smith County's higher-tier matters are handled elsewhere:

- Smith County's **District Courts** — the **7th, 114th, 241st,
  321st (family), and 475th** Judicial District Courts (confirm the
  current list with the district clerk) — and its **County Courts at
  Law** are covered by **`tx-county-courts`** for general civil
  matters.
- Smith County **family matters** (divorce, SAPCR — often heard in
  the **321st** family district court) are covered by
  **`tx-family-court`** and **`tx-family-law`**.

Route a matter above the JP ceiling, a title-to-land dispute, a
divorce/SAPCR, or any matter outside Part V to those skills.

## Caption — Smith County Justice Court variant

```
                          CAUSE NO. ____________

[PLAINTIFF],                       §   IN THE JUSTICE COURT
                                   §
       Plaintiff,                  §   PRECINCT [N], PLACE [N]
v.                                 §
                                   §
[DEFENDANT],                       §
       Defendant.                  §   SMITH COUNTY, TEXAS
```

See `tx-statewide-format` for the full caption with the **§**
divider, the line-numbered pleading paper, the footer, and the
signature block (a self-represented filer omits the State Bar of
Texas number and signs pro se). **Confirm the precinct/place
designation with the Smith County precinct clerk.**

**Agent behavior:** before drafting an answer, calendaring a
deadline, or assembling an appeal, verify with the specific Smith
County JP precinct (1) the **current precinct/place layout and the
assigned Justice of the Peace**, (2) the **answer deadline (TRCP
502.5)** or, for eviction, the **TRCP 510** setting and **5-day**
appeal deadline, (3) the current **jurisdictional ceiling** from the
corpus, and (4) the eFileTexas / precinct-clerk filing posture. Treat
**TRCP Part V** as the controlling rule set (TRCP 500.3(e)).

## Composition

- For the statewide Justice Court framework (TRCP 500–510, the
  500.3(e) quirk, the 14-day answer, the de novo appeal trigger):
  `tx-justice-courts`
- For statewide format and the Texas caption: `tx-statewide-format`
- For the destination of a de novo appeal (Smith County Court at
  Law): `tx-county-courts`
- For Smith County's District Courts and family matters:
  `tx-county-courts`, `tx-family-court`, `tx-family-law`
- For the answer / general denial and default avoidance:
  `tx-first-30-days`
- For consumer-debt defenses (sworn account, chain of title, SOL,
  TDCA / DTPA): `tx-consumer-debt`
- For deadline computation (TRCP 4 holidays; the 14-day answer; the
  5-day eviction appeal): `tx-deadlines`
- For post-judgment relief, garnishment, and exemptions:
  `tx-post-judgment`
- For drafting the answer / motion / notice / order:
  `tx-draft-motion`, `tx-draft-note`, `tx-draft-order`
- For sworn / unsworn declarations (Tex. Civ. Prac. & Rem. Code
  § 132.001): `tx-draft-declaration`
- For assembling and e-filing a packet: `tx-file-packet`
- For pro se conventions: `tx-pro-se`

## References

- `tx-justice-courts` — the statewide TRCP Part V (Rules 500–510)
  framework this skill overlays
- `tx-law-references` — TRCP Part V, Tex. Gov't Code Ch. 27 /
  § 27.031 (JP civil jurisdiction), and Tex. Prop. Code Ch. 24
  (forcible entry and detainer)
- TexasLawHelp.org and the Smith County precinct clerk — confirm the
  current precinct/place layout, the assigned Justice of the Peace,
  the jurisdictional ceiling, and the filing posture
