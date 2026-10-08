---
name: oh-hearings-codearranger
title: Ohio Hearings
description: Use to prepare for Ohio court hearings — oral argument, case-management conferences, evidentiary hearings, remote-appearance protocols. Triggers include 'Ohio court hearing', 'Common Pleas oral argument', 'Ohio Civ. R. 53 magistrate', 'Ohio remote hearing', 'Ohio video conferencing court', 'pretrial conference Ohio'. Covers oral-argument conventions, the Civ. R. 53 magistrate process with the 14-day objection clock, remote-appearance practice (Cisco Webex statewide default but per-judge variations). Also covers seeking disqualification (recusal) of a judge — the R.C. 2701.03 affidavit-of-disqualification procedure for Common Pleas judges (filed with the Clerk of the Ohio Supreme Court; Chief Justice rules) and R.C. 2701.031 for municipal/county judges. Triggers include 'recuse Ohio judge', 'disqualify Ohio judge', 'affidavit of disqualification', 'Ohio judge bias', 'R.C. 2701.03'.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-hearings
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Ohio Hearings

> **NOT LEGAL ADVICE.** Each Common Pleas judge publishes
> chambers practice guidelines that supplement the statewide
> rules. Verify the assigned judge's preferences before any
> hearing.

## Hearing types in Ohio civil practice

- **Case-management conference** — Civ. R. 16; mandatory
  early scheduling conference with the assigned judge or
  magistrate
- **Motion-day oral argument** — typically a 5-15 minute
  argument before the judge on the briefed motion
- **Evidentiary hearing** — typically before a magistrate
  under Civ. R. 53; sworn testimony + exhibits
- **Final pretrial** — set by the case-management order;
  parties exchange exhibit + witness lists, jury
  instructions, and motions in limine
- **Bench trial / jury trial** — set by court order;
  governed by Civ. R. 38-50

## Civ. R. 53 magistrates

Ohio Civ. R. 53 is a heavily-used procedural mechanism:
**magistrates** (typically attorneys appointed by the
common pleas judge) hear most civil matters before the
judge enters a final order. The magistrate's decision
includes findings of fact + conclusions of law.

### Magistrate-decision objection clock

- **14 days** to file written objections under Civ. R.
  53(D)(3)(b)(i)
- Objections must specifically identify the disputed
  factual finding or conclusion of law
- Filing a transcript with the objection is at the
  objector's expense
- The judge reviews objections de novo and either adopts,
  modifies, or rejects the magistrate's decision

### Magistrate's interim relief

A magistrate may issue interim orders (Civ. R. 53(D)(2))
that take effect immediately, subject to the 14-day
objection clock.

## Remote-appearance practice

Ohio courts adopted remote conferencing widely during
COVID-19 and most have retained it for routine hearings:

- **Cisco Webex** is the most common platform (Ohio Supreme
  Court endorses Webex for state-court proceedings)
- Some courts (Cuyahoga, Franklin) use Zoom
- **In-person required** for trials, evidentiary hearings,
  and contested motions in most counties
- Each judge's chambers practice guidelines specify the
  platform + when in-person is required

## Etiquette + protocol

- Address the judge as "Your Honor"
- Stand when the judge enters / leaves the courtroom
- Stand to address the court (when in person)
- Identify yourself when called: "Good morning, Your Honor.
  John Smith, [Pro Se / for the defendant]."
- Bring 3 copies of any document you reference (one for
  the judge, one for opposing counsel, one for yourself)

## Seeking disqualification (recusal) of the judge

Ohio does **not** disqualify a sitting trial judge by a
"motion to recuse" filed with that judge. The mechanism is
statutory, and the choice of mechanism depends on the court:

- **Common Pleas judge** — file an **affidavit of
  disqualification** with the **Clerk of the Ohio Supreme
  Court** under **R.C. 2701.03**. The Chief Justice of the
  Supreme Court (not the trial judge) rules on it. Key
  mechanics in `oh-law-references/references/oh-statutes-debt/RC-Chapter-2701.md`:
  - File **not less than seven calendar days** before the
    next scheduled hearing (R.C. 2701.03(B)).
  - The affidavit must state the **specific** facts/grounds
    of bias, prejudice, interest, or disqualification, and
    include the required statements under R.C. 2701.03(B)(1)–(4).
  - A properly filed affidavit **deprives the judge of
    authority** to preside until the Chief Justice rules
    (R.C. 2701.03(D)), except for the limited matters listed
    in (D)(2)–(3).
- **Municipal or county court judge** — the parallel
  procedure is **R.C. 2701.031** (affidavit filed with the
  Clerk of the Supreme Court; the Chief Justice or designee
  rules).
- **Substantive standard** — the Jud. Cond. R. 2.11
  disqualification grounds (personal bias/prejudice,
  financial interest, prior involvement) supply the
  substance; see `oh-law-references/references/court-rules/JudicialConduct.md`.

A pro se litigant who files an ordinary "motion to recuse"
with the trial judge has used the wrong vehicle for a Common
Pleas matter — the affidavit-of-disqualification route is
the operative one. See `oh-cuya` for the Cuyahoga-specific
filing posture.

## Composition with other oh- skills

- `oh-statewide-format` — proposed-order format if the
  hearing produces a ruling
- `oh-schedule-hearing` — chambers scheduling protocols
- `oh-submit-order` — post-hearing proposed-order
  transmittal
- `oh-cuya` / `oh-frank` / etc. — flagship-court chambers
  practice
