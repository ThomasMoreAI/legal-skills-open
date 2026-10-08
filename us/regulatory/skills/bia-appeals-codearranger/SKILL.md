---
name: bia-appeals-codearranger
title: BIA Appeals — Appealing an Immigration Judge's Decision
description: 'Use this skill to appeal an immigration judge''s decision to the Board of Immigration Appeals (BIA) — assemble the EOIR-26 Notice of Appeal, the statement of issues, the optional brief, and fee-waiver request (EOIR-26A). Triggers: "appeal to the BIA", "EOIR-26", "appeal the immigration judge", "30 days to appeal removal", "BIA brief", "summary dismissal BIA", "I want to appeal my removal order", "statement of issues". Produces EOIR-26 scaffold, appeal-brief outline, and fee-waiver cover. Flags the **30-day appeal deadline as jurisdictional and uncurable** (8 CFR § 1003.38). Composes with eoir-removal-defense, circuit-petition-for-review, immigration-deadlines, and immigration-fact-check.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/bia-appeals
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# BIA Appeals — Appealing an Immigration Judge's Decision

> **NOT LEGAL ADVICE.** This skill produces drafting aids, checklists, and document
> scaffolds — **not legal advice**, and no attorney-client relationship is created. A removal
> appeal can be the last chance to stay in the United States. The **30-day appeal deadline is
> jurisdictional and cannot be cured, extended, or reopened** for being late (8 CFR § 1003.38(b),
> (d)) — there is no good-cause exception. Verify every deadline, form edition, fee amount, and
> citation against current law, and **strongly consider a licensed immigration attorney or an
> EOIR-accredited representative** before filing.

## What this skill is for

When an **immigration judge (IJ)** rules against the respondent — denial of relief, an order of
removal, a denied bond, certain motions — the respondent may **appeal to the Board of Immigration
Appeals (BIA)**, the single nationwide appellate body of EOIR. The BIA reviews the IJ's *record*; it
is not a new trial and (with narrow exceptions) takes no new evidence. This skill assembles the
filing package. The structural/format conventions for EOIR filings are in `eoir-immigration-courts`.

## The Form EOIR-26 and the 30-day deadline

- The appeal is taken by filing a **Notice of Appeal from a Decision of an Immigration Judge
  (Form EOIR-26)** **directly with the Board** (8 CFR § 1003.3(a)(1)).
- It must be **received by the Board within 30 calendar days** after the IJ states an oral decision
  or mails / electronically serves a written decision (8 CFR § 1003.38(b)). **Filing = receipt at
  the Board**, not mailing (§ 1003.38(c)) — build in mailing time. If day 30 is a Saturday, Sunday,
  or legal holiday, it rolls to the next business day (§ 1003.38(b)). Run `immigration-deadlines` to
  compute and double-check the date.
- The EOIR-26 must include **proof of service on the opposing party** — DHS/ICE Office of the
  Principal Legal Advisor (OPLA) for the court that decided the case — and be in **English or with a
  certified translation** (8 CFR § 1003.3(a)(1), (a)(3)).
- **Fee or fee waiver.** The Notice must be accompanied by the fee set in 8 CFR § 1103.7 **or** an
  **Appeal Fee Waiver Request (Form EOIR-26A)** (8 CFR § 1003.8(a)). If neither the fee nor the
  EOIR-26A is filed *within the 30 days*, the appeal is **not properly filed** and the IJ's decision
  becomes final as though no appeal had been taken (§ 1003.38(d)). Some appeals need no fee — e.g., a
  custody/bond appeal, or a matter tied to a no-fee application (§ 1003.8(a)(2)).
- A party who **waived appeal** before the IJ cannot file an EOIR-26 (§ 1003.38(b)); so can a person
  whose departure waived the appeal (§ 1003.3(e)).

## Statement of issues — and the summary-dismissal trap

The single most common self-represented error is a **vague** Notice of Appeal. The Board will
**summarily dismiss** an appeal whose Notice fails to "**meaningfully** apprise the Board of the
specific reasons for the appeal" (8 CFR § 1003.1(d)(2)(i)(A)) — a generic "the IJ was wrong" is not
enough. The statement of the basis of appeal (8 CFR § 1003.3(b)) must:

- **Specifically identify** the findings of fact, the conclusions of law, or both, that are challenged.
- For a **question of law**, cite supporting authority.
- For a **factual dispute**, identify the specific contested facts.
- For **discretionary relief**, state whether the error goes to statutory eligibility or to the
  exercise of discretion, and name the specific finding(s) challenged.
- **Check the two boxes**: whether **oral argument** is requested, and whether a **separate written
  brief** will follow.

> **Caution on the brief box.** If the EOIR-26 says a brief will be filed and then none is filed (and
> no reasonable explanation is given by the deadline), the appeal can be **summarily dismissed on
> that ground alone** (8 CFR § 1003.1(d)(2)(i)(E)). Promise a brief only if it will be filed. Other
> summary-dismissal grounds include an untimely appeal, lack of Board jurisdiction, and an appeal
> filed for an improper purpose or with no arguable basis (§ 1003.1(d)(2)(i)).

## Briefing schedule and page limits

- **Brief vs. EOIR-26 alone.** A brief is **optional** — a well-drafted statement of issues on the
  EOIR-26 can stand alone — but a brief is usually where the real argument lives.
- **Schedule.** For transcribed cases, the **Board sets the briefing schedule after the transcript is
  available** (8 CFR § 1003.3(c)(1)); the appellant typically gets **21 days** (non-detained) or
  21-day simultaneous briefing (detained). The Board may, on **written motion for good cause**,
  extend up to **90 days** (§ 1003.3(c)(1)). Reply briefs are by leave of the Board.
- **Page limits / format.** Page limits, the cover page, and formatting come from the **BIA Practice
  Manual** (procedural guidance, not law) — confirm the current limit there before filing. Cite the
  **regulation** for anything jurisdictional; use the manual only for mechanics.

## Standard of review — what the Board may second-guess (8 CFR § 1003.1(d)(3))

Frame every issue to the correct standard:

| Type of issue | BIA standard of review |
|---|---|
| IJ's **findings of fact** (including **credibility**) | **Clearly erroneous** — the Board does **not** review facts de novo (§ 1003.1(d)(3)(i)) |
| **Questions of law, discretion, and judgment** (and all other issues) | **De novo** (§ 1003.1(d)(3)(ii)) |

A factual challenge must show the finding was *clearly erroneous* — not merely that a different
finding was possible. A legal/discretionary challenge gets fresh review. Mis-labeling a factual
dispute as legal (or vice versa) weakens the appeal.

## What is appealable — and what is NOT this skill

- **Appealable here:** IJ decisions over which the Board has jurisdiction under 8 CFR § 1003.1 —
  removal orders, denials of relief, bond/custody determinations (§ 1003.38(a)), and certain IJ
  rulings. Some matters lie with the IJ, not the Board (§ 1003.1(d)(2)(i)(F)) — confirm jurisdiction.
- **Motion to reopen / reconsider — different route.** A motion to **reopen** (new facts/evidence) or
  **reconsider** (legal/factual error) asks the *same tribunal* to revisit its own decision; it is not
  an appeal and runs on different deadlines and standards. Route those to
  `eoir-motions-to-reopen-reconsider`.
- **After the BIA — the petition for review.** The **BIA's decision is the administratively final
  order of removal** and starts the **30-day clock** to file a **petition for review** with the
  **U.S. Court of Appeals** under INA § 242 (8 U.S.C. § 1252). That clock is also jurisdictional and
  separate from this appeal. Route to `circuit-petition-for-review` immediately on a BIA loss.

## Artifacts this skill drafts

- An **EOIR-26 cover + statement-of-issues scaffold** — caption with name and **A-number**, the IJ /
  court, the decision date and 30-day deadline, a specific issue-by-issue statement keyed to the
  § 1003.1(d)(3) standard of review, the oral-argument and brief-to-follow elections, and a
  certificate of service on OPLA.
- An **appeal-brief outline** — Statement of the Case; Statement of Facts (with record cites);
  Issues Presented; Standard of Review; Argument (one issue per heading, each tagged de novo vs.
  clear-error); Conclusion / relief requested; proof of service.
- A **fee-waiver (Form EOIR-26A) cover** — the inability-to-pay declaration framing and a checklist
  to file it *with* the EOIR-26 inside the 30 days.

## Related authority

- **8 CFR Part 1003** — Board powers and **standard of review** at § 1003.1(d)(3); **summary
  dismissal** at § 1003.1(d)(2); **Notice of Appeal / statement of basis** at § 1003.3; **fees** at
  § 1003.8; the **30-day appeal time** at § 1003.38 —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md).
- **BIA Practice Manual** (filing mechanics, page limits, cover page) —
  [`../../references/court-rules/BIA-Practice-Manual.md`](../../references/court-rules/BIA-Practice-Manual.md).
- **INA § 240 / 8 U.S.C. § 1229a** (removal proceedings) and **INA § 242 / 8 U.S.C. § 1252**
  (judicial review) —
  [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md),
  with the INA ↔ 8 U.S.C. crosswalk in that corpus's README.

## Composition

Builds on `eoir-immigration-courts` (EOIR filing format / cover page / service on OPLA) and the
record produced in `eoir-removal-defense`. Distinct from `eoir-motions-to-reopen-reconsider` (which
revisits a decision rather than appealing it). Hands off to `circuit-petition-for-review` once the
BIA issues its final order. `immigration-deadlines` computes the 30-day appeal and briefing clocks;
`immigration-fact-check` verifies every regulation and record citation before filing.
