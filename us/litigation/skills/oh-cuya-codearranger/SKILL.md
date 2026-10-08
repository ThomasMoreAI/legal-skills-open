---
name: oh-cuya-codearranger
title: Cuyahoga County Court of Common Pleas (Cleveland)
description: Use when drafting or filing in Cuyahoga County Court of Common Pleas (Cleveland). Triggers include the court name, its case number format, and local-rule references. Layers on top of `oh-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-cuya
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Cuyahoga County Court of Common Pleas (Cleveland)

> **NOT LEGAL ADVICE.** Verify the assigned judge's chambers
> practice + the court's current Loc. R. before every filing.

## At a glance

- **Court**: Cuyahoga County Court of Common Pleas (Cleveland)
- **Region**: Lake Erie / Northeast Ohio
- **Population**: 1.26M
- **Address**: Justice Center Complex, 1200 Ontario St., Cleveland, OH 44113
- **Appellate district**: 8th Judicial District (Ohio Court of Appeals)
- **E-filing**: cpdocket.cp.cuyahogacounty.us

## Distinctives

- Cuyahoga is Ohio's largest county by population and the highest civil-filing volume in the state.
- Heavy consumer-debt docket — many cases route to Cleveland Municipal Court (~$15k cap) before reaching Common Pleas.
- Loc. R. 8.0(E) governs discovery motions: discovery requests and responses are **not** filed with the court, and any motion on a discovery dispute must attach the disputed request and the responses to it. (Loc. R. 21.x is Arbitration/Mediation; former 21.2–21.4 are repealed.)
- Several judges require working paper copies for briefs over 15 pages.
- Full verbatim rules: `oh-law-references/references/local-rules/Cuyahoga-CommonPleas-LocalRules.md` (July 2025).

## Filing flow

1. **Caption** per Civ. R. 10(A) — see `oh-statewide-format`
2. **E-file** via the court's portal (per-court system —
   not a statewide platform)
3. **Working copies** if required by chambers practice
4. **Certificate of service** on every party
5. **Notice of Hearing** if the motion requires a hearing
   date (see `oh-schedule-hearing`)

## Disqualifying the assigned judge

To seek removal of a Cuyahoga Common Pleas judge for bias,
prejudice, or interest, **do not** file a motion to recuse
with the judge. File an **affidavit of disqualification**
with the **Clerk of the Ohio Supreme Court** under
**R.C. 2701.03** — the Chief Justice rules on it, and a
timely affidavit suspends the judge's authority to preside
until that ruling. Full mechanics (the 7-day-before-hearing
timing, required contents, and authority-suspension rule)
are in `oh-hearings` → "Seeking disqualification (recusal)
of the judge" and the statute at
`oh-law-references/references/oh-statutes-debt/RC-Chapter-2701.md`.

## Composition with other oh- skills

- `oh-statewide-format` — Civ. R. 10 caption + signature
- `oh-discovery` — Civ. R. 33/34/36 practice
- `oh-first-30-days` — 28-day Civ. R. 12(A)(1) answer
- `oh-hearings` — R.C. 2701.03 affidavit of disqualification
- `oh-draft-motion` / `-declaration` / `-note` / `-order` —
  scaffolders adapted to this court's local rules
- `oh-pro-se` — pro-se conventions
- `oh-file-packet` — court-specific e-filing portal
- `oh-consumer-debt` — debt-buyer defense framework
