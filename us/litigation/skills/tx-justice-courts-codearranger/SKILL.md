---
name: tx-justice-courts-codearranger
title: Texas Justice Courts (Justice of the Peace) — TRCP Part V (Rules 500–510)
description: 'Use for any Texas Justice of the Peace ("JP") / Justice Court matter — small-claims cases, debt-claim cases, eviction (forcible entry and detainer), repair-and-remedy, and the de novo appeal to the county court. Governed by TRCP Part V, Rules 500–510. Triggers: "sued in JP court Texas", "justice of the peace court", "small claims Texas", "Texas debt claim case", "eviction citation Texas", "forcible detainer Texas", "answer a JP citation", "appeal JP to county court", "Statement of Inability to Afford Payment", "JP precinct Texas", "Texas eviction 5-day appeal", "do the rules of evidence apply in justice court". CRITICAL QUIRKS: the regular rules of civil procedure and the rules of evidence do NOT apply in justice court except as Part V incorporates them (TRCP 500.3(e)); the answer is due by the end of the 14th day after service of citation (TRCP 502.5); appeal from a JP judgment is de novo to the county court (TRCP 506). Layer on top of `tx-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-justice-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Justice Courts (Justice of the Peace) — TRCP Part V (Rules 500–510)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Justice Court rules,
> precinct practices, and the controlling jurisdictional ceiling
> change; verify with the specific JP precinct clerk and the current
> TRCP Part V before relying on anything here. A default judgment or a
> missed eviction-appeal deadline has real, fast consequences —
> respond promptly and consider consulting a licensed Texas attorney
> or a legal-aid clinic.

Use this skill in addition to `tx-statewide-format` when the matter
is in a Texas **Justice Court** — the court of the **Justice of the
Peace** ("JP"). Each Texas county is divided into **precincts**, each
with one or more elected Justices of the Peace (a precinct may have a
**Place 1** and **Place 2**). The Justice Courts are the highest-
volume civil courts for everyday disputes: small claims, debt-claim
collection suits, and residential evictions.

## What the Justice Courts hear

Justice Court civil jurisdiction is set by statute (Tex. Gov't Code
Ch. 27, **§ 27.031**) and the rules. The Justice Courts hear:

- **Small-claims cases** — ordinary money claims up to the statutory
  ceiling.
- **Debt-claim cases (TRCP 508)** — suits by an assignee, debt
  collector, financial institution, or person/entity primarily in
  the business of lending, to recover a debt, up to the ceiling.
  Most consumer-debt collection suits land here.
- **Eviction (forcible entry and detainer) cases (TRCP 510)** —
  expedited suits to recover possession of residential or commercial
  premises (see below).
- **Repair-and-remedy cases (TRCP 509)** — a residential tenant's
  suit to compel a landlord repair.

The **monetary ceiling** is statutory and **drift-prone** — the
amount in controversy must not exceed the cap (currently in the
range of **$20,000**, exclusive of interest and costs, but **confirm
the current ceiling against `tx-law-references` / Tex. Gov't Code
§ 27.031** and **TRCP 500.3**). Justice Courts do **not** decide
title to land, divorce, or matters within the District Court's
exclusive reach. A claim above the ceiling belongs in a County Court
at Law, the Constitutional County Court, or the District Court — see
`tx-county-courts`.

## CRITICAL QUIRK: the regular rules largely do NOT apply (TRCP 500.3(e))

**TRCP 500.3(e)** is the defining feature of Justice Court practice:
the **other Texas Rules of Civil Procedure and the Texas Rules of
Evidence do NOT apply** in a Justice Court case **except** where
**Part V (Rules 500–510)** specifically incorporates them. Justice
Court procedure is deliberately **simplified and informal** —
designed so a self-represented party can use it. Do not import a
District-Court motion form, a TRCP 166a summary-judgment timeline, a
TRCP 190 discovery-level plan, or an evidence-rule objection into a
JP case as if it controlled; check whether Part V incorporates the
specific mechanic first. Discovery in Justice Court is limited and
generally permitted only with the court's approval (**TRCP 500.9**).

This simplification cuts both ways: the informality favors
self-represented parties, but it also means a debt-buyer plaintiff
may try to prove up an account without the evidentiary formalities
that would apply in a higher court — so scrutinize the plaintiff's
proof and the **chain of title** (see `tx-consumer-debt`).

## Commencement, citation, and the answer deadline

- **Commencement (TRCP 502)** — a plaintiff starts the case by filing
  a **petition** (a sworn statement is not generally required) and
  paying the fee (or filing a **Statement of Inability to Afford
  Payment of Court Costs**). The petition must give a short statement
  of the claim and the relief sought.
- **Citation and service (TRCP 501)** — the clerk issues citation;
  the defendant is served under the rule's methods.
- **Answer deadline (TRCP 502.5)** — the defendant's **answer is due
  by the end of the 14th day after the date the defendant was served
  with citation** (if the 14th day is a Saturday, Sunday, or legal
  holiday, it extends to the next day that is not). **This is NOT the
  District-Court "Monday rule"** — confirm the current 14-day deadline
  against **TRCP 502.5** in the corpus. The answer may be made in
  writing or, where the rule allows, by other means; a **general
  denial** suffices to put the plaintiff to its proof. File the answer
  before the deadline to avoid a default. See `tx-first-30-days`.
- **Default judgment (TRCP 503)** — if the defendant does not answer
  by the deadline, the plaintiff may move for a **default judgment**;
  the court may require proof of the claim and damages. A defendant
  who learns of a default has limited avenues (motion to set aside /
  new trial under the Part V procedure) — act fast.

## Eviction (forcible entry and detainer) — TRCP 510 (expedited)

Eviction cases run on a **compressed, expedited timeline** under
**TRCP 510**:

- The suit is for **possession** (and may include unpaid rent within
  the ceiling). The landlord must have given the statutory **notice
  to vacate** (Tex. Prop. Code Ch. 24) before filing.
- After service, the case is set for **trial quickly** (the rule sets
  a short window — confirm the current setting against TRCP 510).
- **Appeal is very fast**: a party may appeal an eviction judgment to
  the county court within **5 days** after the judgment is signed, by
  filing an appeal bond, making a cash deposit, or filing a
  **Statement of Inability to Afford Payment**; a tenant who appeals
  to stay in possession during a residential eviction appeal must also
  comply with the rule's **pay-rent-into-the-registry** requirements.
  **Confirm the current 5-day eviction-appeal deadline and the
  pay-rent conditions against TRCP 510** — missing them forfeits the
  appeal and possession. See `tx-deadlines` and `tx-post-judgment`.

Eviction is time-critical and consequential; flag the short deadlines
prominently and encourage prompt action and, where possible, legal
aid.

## De novo appeal to the county court (TRCP 506)

A party who loses in Justice Court may appeal **de novo** — a
brand-new trial — to the **county court** (the County Court at Law or
the Constitutional County Court, per the county's structure). Under
**TRCP 506**, the appellant perfects the appeal by filing, within the
rule's deadline, an **appeal bond**, a **cash deposit**, or a
**Statement of Inability to Afford Payment of Court Costs**. The
ordinary civil appeal window is short (confirm the current
non-eviction appeal deadline against TRCP 506; eviction is the
**5-day** track under TRCP 510). On perfection, the case is tried
anew in the county court as if it had originated there — the destination
court and its procedure live in `tx-county-courts`.

## Precincts, places, and filing

- Each county is divided into **JP precincts**; a precinct may have
  one or more **Places** (Place 1 / Place 2), each with its own
  Justice of the Peace and clerk. **Venue** within the county
  generally lies in the precinct where the defendant resides or where
  the claim/eviction premises is located — confirm the applicable
  venue rule (TRCP 502.4 / 510.4) and the correct precinct before
  filing.
- **E-filing** runs through **eFileTexas.gov** (Odyssey File &
  Serve); Justice Courts participate, and self-represented filers may
  e-file or file with the precinct clerk in person — confirm the
  precinct's accepted methods.
- The assisted self-help front end is **TexasLawHelp.org**, which
  hosts JP-court forms (answer, Statement of Inability, eviction
  answer, appeal).

## Caption — Justice Court variant

```
                          CAUSE NO. ____________

[PLAINTIFF],                       §   IN THE JUSTICE COURT
                                   §
       Plaintiff,                  §   PRECINCT [N], PLACE [N]
v.                                 §
                                   §
[DEFENDANT],                       §
       Defendant.                  §   [COUNTY] COUNTY, TEXAS
```

See `tx-statewide-format` for the full caption with the **§**
divider, the line-numbered pleading paper, the footer, and the
signature block. A self-represented filer omits the State Bar of
Texas number and signs as pro se. Confirm the precinct/place
designation with the precinct clerk.

**Agent behavior:** before drafting an answer, calendaring a
deadline, or assembling an appeal, confirm (1) the correct **precinct
and Place** and its clerk, (2) the **answer deadline (TRCP 502.5,
end of the 14th day)** or, for eviction, the **TRCP 510** trial
setting and **5-day** appeal deadline, (3) the current **jurisdictional
ceiling** from the corpus, and (4) the eFileTexas posture. Treat
Part V as the controlling rule set and do not assume a higher court's
procedure applies (TRCP 500.3(e)).

## Composition

- For statewide format and the Texas caption: `tx-statewide-format`
- For Smith County's JP precincts (Tyler): `tx-smith-county-jp`
- For the destination of a de novo appeal (county court):
  `tx-county-courts`
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
- For citation verification: `tx-fact-check`

## References

- `tx-law-references` — TRCP **Part V (Rules 500–510)**, including
  **500.3(e)** (rules of procedure/evidence inapplicability), **502 /
  502.5** (commencement / 14-day answer), **503** (default), **506**
  (de novo appeal to county court), **508** (debt-claim cases),
  **509** (repair-and-remedy), and **510** (eviction); Tex. Gov't
  Code Ch. 27 / **§ 27.031** (JP civil jurisdiction); Tex. Prop. Code
  Ch. 24 (forcible entry and detainer)
- TexasLawHelp.org and the precinct clerk — confirm the current
  jurisdictional ceiling, the precinct/place layout, the eFileTexas
  posture, and the JP-court forms
