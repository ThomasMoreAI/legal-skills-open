---
name: immigration-pro-se-codearranger
title: Immigration — Pro Se Orientation
description: 'Use this skill FIRST when a self-represented person needs orientation in any U.S. immigration matter — maps the four separate forums (USCIS benefits, EOIR immigration court/BIA, Department of State consular processing, federal circuit review) so the right downstream skill is used. Triggers: "I got an NTA", "notice to appear", "immigration court date", "master calendar hearing", "USCIS denied", "received an RFE", "my visa was refused", "221g", "appeal to the BIA", "petition for review", "what''s my A-number", "how do I find my case", "do I need a lawyer", "notario", "EOIR-28", "G-28", "self-represented immigration". Enforces documents-not-advice boundary; warns about notario fraud; locates the case (EOIR portal, USCIS account, A-number); establishes controlling deadline; routes to venue-specific skills. Composes with every other skill in this plugin and with state *-pro-se skills.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/immigration-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: immigration
language: en
---

# Immigration — Pro Se Orientation

> **NOT LEGAL ADVICE.** This skill and everything in this plugin produce drafting aids,
> checklists, and document scaffolds — **not legal advice**, and no attorney-client
> relationship is created. Immigration consequences (removal, bars to reentry, loss of
> status) are severe and often irreversible. Verify every deadline, form edition, and
> citation against current law, and **strongly consider consulting a licensed immigration
> attorney or an EOIR-accredited representative** before filing anything.

## Why this skill goes first

U.S. immigration practice is split across **four forums that do not share rules, deadlines,
or filing systems.** Picking the wrong one wastes the (often single) chance to act. Identify
the forum before drafting:

| Forum | What it decides | Governing rules | Route to |
|---|---|---|---|
| **USCIS** (DHS) | Benefit requests — petitions, applications, status | 8 CFR ch. I; the INA | `uscis-benefit-requests` |
| **EOIR immigration court** (DOJ) | Removal / deportation; relief in proceedings | 8 CFR Part 1003 / 1240 / 1208; ICPM | `eoir-removal-defense`, `eoir-motions-to-reopen-reconsider` |
| **Board of Immigration Appeals** (DOJ) | Appeals from immigration-judge decisions | 8 CFR § 1003.1–§ 1003.8; BIAPM | `bia-appeals` |
| **U.S. Court of Appeals** | Judicial review of a final removal order | INA § 242 / 8 U.S.C. § 1252 | `circuit-petition-for-review` |
| **Department of State** (consular) | Visa issuance / refusal abroad | INA; 22 CFR 40–42; 9 FAM | `consular-visa-refusal` |

The full EOIR court system is described in `eoir-immigration-courts`; the master deadline
catalog is in `immigration-deadlines`. Statutory text lives in
[`../../references/immigration-statutes/`](../../references/immigration-statutes/) — cite by
the **INA → 8 U.S.C.** crosswalk in that corpus's README (INA § 240 = 8 U.S.C. § 1229a,
INA § 212 = 8 U.S.C. § 1182, etc.), not from memory.

## First three things to establish

1. **The A-number.** The "A-number" (Alien Registration Number, `A2NN-NNN-NNN`) is the
   person's file key across DHS and EOIR. It is on the NTA, USCIS notices, and the green
   card. Every filing and FOIA request keys off it.
2. **Where the case actually is.** A person can have matters in more than one forum at once.
   Locate each:
   - **In removal proceedings?** Check the EOIR automated case-information system (by
     A-number) for the next hearing date and the filing deadline.
   - **A pending USCIS case?** Check the USCIS online account / receipt number (`XYZ` +
     10 digits) and the case-status tool.
   - Pull the record before drafting — see `immigration-foia` for getting the **A-file**
     (USCIS) and the **Record of Proceedings** (EOIR).
3. **The controlling deadline.** Immigration deadlines are short and frequently
   jurisdictional (a missed BIA-appeal or petition-for-review deadline usually cannot be
   cured). Run `immigration-deadlines` immediately.

## Representation — who may appear, and the fraud warning

- **You may represent yourself** ("pro se" / "self-represented") in any forum.
- In EOIR proceedings, a representative enters via **Form EOIR-28**; before USCIS, via
  **Form G-28**. Only (a) licensed attorneys in good standing and (b) **EOIR-accredited
  representatives** at recognized organizations may represent you (8 CFR Part 1292 /
  § 1003.16). Free / low-cost providers are listed on EOIR's pro-bono and recognized-
  organization rosters.
- **Notario / "immigration consultant" warning.** In much of Latin America a *notario
  público* is a licensed attorney; in the U.S. a "notary" is **not** a lawyer and may not
  give legal advice or select forms for you. Notario fraud is a leading cause of lost cases
  and missed deadlines. A non-attorney who fills in forms for a fee, claims special
  government connections, or tells you to hide facts is a red flag — document it
  (`consumer-harm-documentation` in the federal plugin can scaffold the record).
- **Language access.** EOIR provides interpreters at hearings at no cost; request the
  correct language in advance. Translated documents filed with the court or USCIS need a
  **certificate of translation**.

## How to use the rest of this plugin

- **Format / filing mechanics** for immigration court & the BIA → `eoir-immigration-courts`
  (the ICPM / BIA Practice Manual conventions and the binding 8 CFR Part 1003 rules).
- **Verify any citation** a draft makes → `immigration-fact-check`.
- **Removal defense filings** (EOIR-28, pleadings to the NTA, continuances, change of
  venue, applications for relief) → `eoir-removal-defense`.
- **Reopen or reconsider** a removal order (including in-absentia orders) →
  `eoir-motions-to-reopen-reconsider`.
- **Appeal an IJ decision** to the Board → `bia-appeals`.
- **USCIS** cover letters, evidence indexes, RFE/NOID responses → `uscis-benefit-requests`.
- **Visa refused at a consulate** (§ 221(g), § 212(a) ineligibility, waivers) →
  `consular-visa-refusal`.
- **Judicial review** of a final removal order → `circuit-petition-for-review`.

## Artifacts this skill drafts

- A **forum / posture worksheet** (which forum(s), A-number, receipt numbers, next dates).
- A **case-location checklist** (EOIR portal, USCIS account, FOIA to pull the file).
- A **deadline triage note** that hands off to `immigration-deadlines`.

## Related authority

- INA (8 U.S.C. ch. 12) — [`../../references/immigration-statutes/`](../../references/immigration-statutes/),
  with the INA ↔ 8 U.S.C. crosswalk in its README.
- Representation: **8 CFR Part 1292** / **§ 1003.16** —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md)
  and [`8CFR-292-representation.md`](../../references/immigration-regulations/8CFR-292-representation.md).

## Composition

Goes first, then routes to the forum-specific skills above. Composes with the state
`*-pro-se` skills (for any parallel state-court matter) and with the federal
`consumer-harm-documentation` skill (to log notario fraud or agency misconduct).
