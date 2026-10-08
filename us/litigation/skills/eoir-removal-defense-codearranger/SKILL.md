---
name: eoir-removal-defense-codearranger
title: EOIR — Removal Defense (Respondent Filings)
description: 'Use this skill to assemble respondent filings in removal proceedings before an immigration judge (the substantive companion to eoir-immigration-courts). Covers entering appearance, pleading to the Notice to Appear (admit/deny allegations, concede/contest charges), designating relief, and motions (continuance, change of venue, administrative closure, prehearing statement). Triggers: "I got an NTA", "notice to appear", "master calendar hearing", "plead to the charges", "deny allegations", "removal defense", "designate relief", "cancellation of removal", "asylum in immigration court", "voluntary departure", "motion to continue", "change of venue", "administrative closure". Produces pleading scaffold (admit/deny + concede/contest), motion-to-continue and motion-to-change-venue scaffolds, relief-application cover/index. Routes reopen/reconsider motions to eoir-motions-to-reopen-reconsider.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/eoir-removal-defense
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# EOIR — Removal Defense (Respondent Filings)

> **NOT LEGAL ADVICE.** Drafting aids, scaffolds, and checklists only — not legal advice, and
> no attorney-client relationship is created. **Removal proceedings are high-stakes: an order of
> removal can mean permanent separation, multi-year or permanent bars to reentry, and loss of
> status — and many steps (especially concessions and missed deadlines) are hard or impossible
> to undo.** A licensed immigration attorney or an EOIR-accredited representative is **strongly
> advised** before you plead or file anything. Verify every form edition, deadline, and citation
> against current law.

This skill produces the respondent's substantive filings; **filing format, the caption/cover
page, service on DHS/ICE OPLA, exhibit tabbing, and ECAS vs. paper come from
`eoir-immigration-courts`.** Statutory text lives in the
[`../../references/immigration-statutes/`](../../references/immigration-statutes/) corpus — cite
by the **INA → 8 U.S.C.** crosswalk in its README (INA § 240 = 8 U.S.C. § 1229a, § 240A = § 1229b,
§ 240B = § 1229c, § 208 = § 1158, § 245 = § 1255, § 237 = § 1227, § 212 = § 1182), not from memory.

## Entering an appearance

- **A representative** enters with **Form EOIR-28** (the EOIR equivalent of a court appearance) —
  attorneys and EOIR-accredited reps only (see `immigration-pro-se` for who may appear and the
  notario-fraud warning).
- **A pro se respondent** files **no appearance form** — you are already a party. Format and
  signature-block mechanics defer to `eoir-immigration-courts`.

## Pleading to the Notice to Appear (the master calendar hearing)

At the **master calendar hearing (MCH)** the respondent **pleads to the NTA (Form I-862)**. The
pleading has three moving parts, and the IJ takes them on the record under 8 CFR § 1240.10:

1. **The factual allegations** (numbered ¶¶ in the NTA — alienage, manner of entry, status, any
   convictions). For **each** allegation: **admit** or **deny** (or "deny for lack of knowledge").
2. **The charge(s) of removability** — cited as grounds of **deportability under INA § 237 /
   8 U.S.C. § 1227** (for someone admitted) or **inadmissibility under INA § 212 / 8 U.S.C.
   § 1182** (for an arriving alien or one not admitted). For each charge: **concede** or
   **contest**.
3. **Designate the relief sought** and the **country of removal** (or decline to designate).

**Why concessions are high-stakes — flag this to the user.** Admitting the factual allegations
and **conceding the charge** establishes removability and **shifts the burden to the respondent**
to prove eligibility for relief in the exercise of discretion (8 CFR § 1240.8(d)). A concession is
generally **binding and hard to undo**. By contrast, if the respondent **contests** removability,
DHS must prove a deportability charge by **clear and convincing evidence** (8 CFR § 1240.8(a)); for
an applicant for admission, the respondent bears the burden of proving admissibility
(§ 1240.8(b)/(c)). **Do not concede reflexively** — the choice drives the whole case. The burden
framework is statutory at **INA § 240(c) / 8 U.S.C. § 1229a(c)**.

## The relief menu — designate, then route to the application

Relief is requested in proceedings; each form of relief has its own application and is handed off
to the skill that drafts it:

| Relief | Statute | Application form | Routes to |
|---|---|---|---|
| **Asylum / withholding / CAT** | INA § 208 / 8 U.S.C. § 1158 (asylum); withholding & CAT in proceedings | **Form I-589** | `eoir-removal-defense` (this skill) + the asylum reference at 8 CFR Part 1208 |
| **Cancellation of removal — LPR** | INA § 240A(a) / 8 U.S.C. § 1229b(a) | **Form EOIR-42A** | this skill |
| **Cancellation of removal — non-LPR** | INA § 240A(b) / 8 U.S.C. § 1229b(b) | **Form EOIR-42B** | this skill |
| **Adjustment of status** | INA § 245 / 8 U.S.C. § 1255 | **Form I-485** (filed in proceedings) | this skill; `uscis-benefit-requests` for the underlying petition |
| **Voluntary departure** | INA § 240B / 8 U.S.C. § 1229c | (oral/written request; pre- or post-conclusion) | this skill |

The relief-application **cover/index** scaffold below assembles the application, the supporting
exhibits (tabbed per `eoir-immigration-courts`), and the proof of service. Eligibility analysis is
NOT in scope — verify the substantive bars and thresholds against the statute and 8 CFR.

## Motions in proceedings

- **Motion to continue.** Filed on a **good-cause** showing (8 CFR § 1003.29; the
  continuance/filing-extension limits at 8 CFR § 1240.10(h)). State the specific cause (e.g.,
  retaining counsel, awaiting a pending USCIS petition, gathering evidence), the length sought, and
  whether DHS opposes.
- **Motion to change venue.** Decided under the 8 CFR Part 1003 / § 1240.10 framework and the
  ICPM; typically requires **pleading to the NTA**, stating a **fixed new address**, and a
  good-cause showing (usually a move). Route format through `eoir-immigration-courts`.
- **Motion to administratively close or to terminate.** Administrative closure removes the case from
  the active docket; **termination** ends proceedings (e.g., a defective NTA, or DHS lacks a
  sustainable charge). Both are decided by the IJ under the Part 1003 framework.
- **Prehearing statement + the call-up deadline.** Before the **individual / merits hearing**, the
  IJ (or the ICPM default) sets a **filing "call-up" deadline** for exhibits, witness lists, and a
  prehearing statement. The deadline is firm — **late exhibits can be refused** (8 CFR § 1240.7(g)).
  Run `immigration-deadlines` to fix the date.

**Motions to REOPEN or RECONSIDER are a separate skill** — route those to
`eoir-motions-to-reopen-reconsider`.

## Artifacts this skill drafts

- A **pleading scaffold** — allegation-by-allegation **admit/deny** plus **concede/contest** per
  charge, with the burden-shift warning surfaced.
- A **motion-to-continue scaffold** (good-cause statement + length + DHS position).
- A **motion-to-change-venue scaffold** (plea to the NTA + fixed new address + good cause).
- A **relief-application cover/index** (application form + tabbed exhibits + proof of service).

## Related authority

- **8 CFR Part 1240** (removal proceedings — pleading § 1240.10, burdens § 1240.8, evidence/call-up
  § 1240.7, continuances § 1240.10(h)) —
  [`../../references/immigration-regulations/8CFR-1240-removal-eoir.md`](../../references/immigration-regulations/8CFR-1240-removal-eoir.md).
- **8 CFR Part 1003** (EOIR/BIA/IJ proceedings — motions, continuances § 1003.29, venue) —
  [`../../references/immigration-regulations/8CFR-1003-eoir-bia.md`](../../references/immigration-regulations/8CFR-1003-eoir-bia.md).
- **8 CFR Part 1208** (asylum before EOIR) —
  [`../../references/immigration-regulations/8CFR-1208-asylum-eoir.md`](../../references/immigration-regulations/8CFR-1208-asylum-eoir.md).
- Statutes: **§ 1229a** (removal + § 1229a(c) burden), **§ 1229b** (cancellation), **§ 1229c**
  (voluntary departure), **§ 1158** (asylum), **§ 1255** (adjustment), **§ 1227** (deportability),
  **§ 1182** (inadmissibility) — [`../../references/immigration-statutes/INA-II-immigration.md`](../../references/immigration-statutes/INA-II-immigration.md).

## Composition

Builds on `eoir-immigration-courts` (format, caption, service on OPLA, ECAS) for every filing's
mechanics. `immigration-deadlines` supplies the MCH, call-up, and motion clocks;
`immigration-fact-check` verifies citations. Reopen/reconsider go to
`eoir-motions-to-reopen-reconsider`; appeals of the IJ's decision go to `bia-appeals`. Where relief
depends on an underlying USCIS petition (adjustment) or a consular step, composes with
`uscis-benefit-requests` and `consular-visa-refusal`.
