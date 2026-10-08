---
name: tn-first-30-days-codearranger
title: Tennessee — First 30 Days After Service
description: Use when a Tennessee defendant has just been served with a civil complaint, petition, or detainer/civil warrant. Triggers include "answer a Tennessee complaint", "I was sued in Tennessee", "served with a summons in Tennessee", "30 days to answer Tennessee", "Tenn. R. Civ. P. 12", "motion to dismiss Tennessee", "Rule 12.02(6) failure to state a claim", "affirmative defenses Tennessee", "counterclaim Tennessee", "compulsory counterclaim", "default judgment Tennessee", "statute of limitations on a debt in Tennessee", "first 30 days after being sued". Covers the Tenn. R. Civ. P. 12.01 answer window (30 days; 15 days after denial of a Rule 12 motion), the Tenn. R. Civ. P. 12.02 motion-to-dismiss grounds (including 12.02(6) and the conversion-to-Rule-56 trap), the Tenn. Code Ann. § 20-12-119(c) fee-shifting on a 12.02(6) dismissal, affirmative defenses, counterclaims under Rule 13, and the default-judgment risk timeline.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Tennessee attorney about substantive defenses
> when possible.

Use this skill when the defendant has **just been served** with a
civil complaint or petition in **Circuit** or **Chancery** Court. It
frames the response window — the time in which the defendant must
answer, move to dismiss, or risk default.

> **Served with a General Sessions civil warrant instead?** General
> Sessions practice is informal and runs on a court-date / docket-call
> model rather than a paper answer; see `tn-general-sessions`. The
> 30-day answer window below is the Circuit / Chancery rule.

## The clock — Tenn. R. Civ. P. 12.01

| Event | Deadline | Authority |
|---|---|---|
| Answer after service of summons & complaint | **30 days** after service | Tenn. R. Civ. P. 12.01 |
| Reply to a counterclaim / answer to a cross-claim | **30 days** | Tenn. R. Civ. P. 12.01 |
| Responsive pleading after denial of a Rule 12 motion | **15 days** after notice of the court's action | Tenn. R. Civ. P. 12.01 |
| Response to amended complaint | per Tenn. R. Civ. P. 15.01 | Tenn. R. Civ. P. 15 |

Frame these as the **current** day counts; verify against Tenn. R.
Civ. P. 12.01 and add the Tenn. R. Civ. P. 6.05 **3-day mail add-on**
where service was by mail. Compute with `tn-deadlines`.

> ⚠ **Default risk.** If the defendant neither answers nor moves
> within the window, the plaintiff may seek a **default judgment**
> under Tenn. R. Civ. P. 55. Setting aside a default later is harder
> (Tenn. R. Civ. P. 55.02 / 60.02) — see `tn-post-judgment`.

## Day-by-day playbook

### Days 0-3 — read the complaint carefully

- **Read every numbered paragraph.** Note who is suing, on what
  claims, for what relief, and what contracts / accounts / events are
  alleged.
- **Note the court, county, and docket number** — these go on every
  filing (Tenn. R. Civ. P. 10.01 caption).
- **Note the court type**: Circuit (law) vs. Chancery (equity) vs.
  General Sessions (limited jurisdiction). This drives the procedure.
- **Check service** under Tenn. R. Civ. P. 4. Was the defendant
  personally served? Served at the residence? Defective service is a
  Rule 12.02(4)/(5)-type defense — preserve it.

### Days 3-10 — choose the response strategy

Three principal paths:

1. **Answer** — admit, deny, or state lack of knowledge for each
   numbered paragraph (Tenn. R. Civ. P. 8.02); assert affirmative
   defenses (Tenn. R. Civ. P. 8.03); assert any counterclaims (Rule 13).
2. **Motion to Dismiss** under Tenn. R. Civ. P. 12.02 — challenges the
   pleading without answering on the merits. If denied, the responsive
   pleading is due **15 days** after notice of the court's action.
3. **Motion for More Definite Statement** (Tenn. R. Civ. P. 12.05) —
   when the complaint is so vague the defendant cannot reasonably
   respond. Disfavored; rarely granted.

### Tenn. R. Civ. P. 12.02 — grounds to move to dismiss

Rule 12.02 lists defenses that may be raised by motion instead of (or
in addition to) the answer:

- **12.02(1)** lack of subject-matter jurisdiction
- **12.02(2)** lack of personal jurisdiction
- **12.02(3)** improper venue
- **12.02(4)** insufficiency of process
- **12.02(5)** insufficiency of service of process
- **12.02(6)** **failure to state a claim upon which relief can be
  granted** (the most common pre-answer motion)
- **12.02(7)** failure to join a party under Tenn. R. Civ. P. 19

> **Conversion-to-Rule-56 trap.** On a **12.02(6)** motion, if
> matters **outside the pleadings** are presented to and not excluded
> by the court, the motion is **treated as one for summary judgment
> under Tenn. R. Civ. P. 56**, and all parties must be given a
> reasonable opportunity to present Rule 56 material. Do not attach
> outside evidence to a 12.02(6) motion unless you intend to convert
> it. The Rule 56 summary-judgment standard itself — restored to the
> federal/*Celotex* model by *Rye v. Women's Care Center of Memphis,
> MPLLC*, 477 S.W.3d 235 (Tenn. 2015) — is developed in
> `tn-draft-motion`; this skill flags it at a pointer level.

> ⚠ **Fee-shifting on a 12.02(6) dismissal.** Under **Tenn. Code Ann.
> § 20-12-119(c)**, a party that **prevails on a 12.02(6)** motion may
> recover costs and reasonable attorney's fees from the non-prevailing
> party, **capped at $10,000**. This cuts both ways: a defendant who
> wins dismissal can recover; a defendant whose own 12.02(6) motion
> the court rejects is not exposed under (c), but a defendant who files
> claims later dismissed could be. Verify the current statute and case
> law applying it before relying on the cap or its scope.

> **Defense waiver.** The Rule 12.02(2), (3), (4), and (5) defenses are
> waived if not raised in the first responsive pleading or motion
> (Tenn. R. Civ. P. 12.08). 12.02(6) and subject-matter jurisdiction
> are not waived the same way — verify the current rule.

### Days 10-30 — draft the answer (or the motion)

#### Answer structure

```
                       ANSWER, AFFIRMATIVE DEFENSES,
                            AND COUNTERCLAIM

   Defendant [Name], responds to Plaintiff's Complaint as follows:

                              ANSWER

   1. Defendant denies the allegations in paragraph 1.

   2. Defendant lacks knowledge or information sufficient to form a
      belief as to the truth of the allegations in paragraph 2 and
      therefore denies them.

   3. Defendant admits the allegations in paragraph 3.

   [...]

                        AFFIRMATIVE DEFENSES

   First Defense — Statute of Limitations. Plaintiff's claims are
   barred in whole or in part by the applicable statute of limitations
   (see SOL chart below).

   Second Defense — Failure to State a Claim. The Complaint fails to
   state a claim upon which relief can be granted, Tenn. R. Civ. P.
   12.02(6).

   [...]

                            COUNTERCLAIM

   [If asserting a counterclaim, plead it as a complaint-style block
   with numbered factual allegations and named claims.]

                          PRAYER FOR RELIEF

   WHEREFORE, Defendant respectfully requests that the Court dismiss
   the Complaint with prejudice, award Defendant costs and fees as
   allowed by law, and grant such further relief as is just.
```

#### Affirmative-defense catalog — Tenn. R. Civ. P. 8.03

Plead all that may apply; failure to plead an affirmative defense
typically waives it. Common defenses include:

- Statute of limitations (very common — see chart)
- Payment / accord and satisfaction / release
- Discharge in bankruptcy
- Estoppel / waiver / laches
- Failure of consideration
- Fraud / illegality
- Statute of frauds
- Res judicata / claim preclusion
- Failure to state a claim (Tenn. R. Civ. P. 12.02(6))
- Lack of standing / chain of title (in debt-buyer cases — see
  `tn-consumer-debt`)

### Statute of limitations — Tennessee quick chart (Title 28)

| Claim | SOL | Authority |
|---|---|---|
| Written contracts / open accounts (incl. most credit-card debt) | **6 years** | Tenn. Code Ann. § 28-3-109 |
| Sale of goods (UCC) | **4 years** | Tenn. Code Ann. § 47-2-725 |
| Personal injury / personal torts | **1 year** | Tenn. Code Ann. § 28-3-104 |
| Property damage | **3 years** | Tenn. Code Ann. § 28-3-105 |
| Libel | 1 year / Slander 6 months | Tenn. Code Ann. § 28-3-103 / -104 |
| FDCPA (federal) | 1 year from violation | 15 U.S.C. § 1692k(d) |

The contract clock generally runs from breach; for open / revolving
accounts the accrual date (often last payment / activity) is
**fact-dependent** — verify. A **sworn account** under Tenn. Code Ann.
§ 24-5-107 is an evidentiary device (an affidavit shifts the burden to
the defendant to deny under oath), **not a separate SOL**.

### Counterclaims and cross-claims — Tenn. R. Civ. P. 13

- **Compulsory counterclaim** (13.01): a claim arising out of the same
  transaction or occurrence — **must** be pleaded or it is waived.
- **Permissive counterclaim** (13.02): an unrelated claim — may be
  pleaded.
- **Cross-claim** (13.07): a claim against a co-party.
- Plead **all known counterclaims** at the time of answer; Tennessee
  applies compulsory-counterclaim preclusion.

## Filing the answer / motion

- **File** with the clerk of the Circuit or Chancery Court (confirm the
  venue's e-filing platform — Davidson Chancery Odyssey/eFileTN; Shelby
  eFlex; others Tybera/TnCIS or paper).
- **Serve** all parties under Tenn. R. Civ. P. 5 and include a
  **Certificate of Service**.
- **Sign** under Tenn. R. Civ. P. 11.

## Composition

- For statewide format: `tn-statewide-format`
- For drafting the answer / motion / declaration: `tn-draft-motion`,
  `tn-draft-declaration`
- For the summary-judgment standard (the *Rye* / Rule 56 detail):
  `tn-draft-motion`
- For the filing court: `tn-davidson`, `tn-shelby`, `tn-knox`,
  `tn-hamilton`, `tn-county-courts`, `tn-general-sessions`
- For deadline arithmetic: `tn-deadlines`
- For matter-specific defenses: `tn-consumer-debt`, `tn-family-law`,
  `tn-landlord-tenant`, `tn-personal-injury`

## References

- `references/answer-template.md` — full answer scaffold
- `references/motion-to-dismiss-template.md` — Tenn. R. Civ. P.
  12.02(6) template with the § 20-12-119(c) fee note
- `references/affirmative-defense-catalog.md` — annotated catalog
- `references/counterclaim-checklist.md`
- `references/service-defects.md` — Tenn. R. Civ. P. 4 analysis
- `references/default-prevention.md` — how the default clock works
