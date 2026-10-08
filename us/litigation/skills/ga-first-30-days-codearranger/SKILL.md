---
name: ga-first-30-days-codearranger
title: Georgia — First 30 Days After Service
description: This skill should be used when a Georgia defendant has just been served with a civil complaint, summons, or dispossessory affidavit. Triggers include "I got served in Georgia", "answer a Georgia complaint", "I was sued in Georgia", "30 days to respond", "open a default Georgia", "Georgia default judgment", "motion to dismiss Georgia", "12(b)(6) Georgia", "affirmative defenses Georgia", "counterclaim", "compulsory counterclaim Georgia", "Georgia dispossessory answer". Covers the 30-day answer window under O.C.G.A. § 9-11-12(a), the § 9-11-55 default regime and the 15-day open-as-of-right cure window, the § 9-11-12(b) motion-to-dismiss triage, § 9-11-8(c) affirmative defenses, § 9-11-13(a) compulsory counterclaims, and § 9-11-15(a) amendment as of right.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-first-30-days
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia — First 30 Days After Service

> **NOT LEGAL ADVICE.** Time is short. This skill helps a defendant
> sketch a response and surface the most important deadlines, but
> consult a licensed Georgia attorney about substantive defenses when
> possible. Verify current rules and venue practice before filing.

Use this skill when the defendant has **just been served** with a
civil complaint, petition, or dispossessory affidavit. It frames the
window in which a Georgia defendant must answer, move to dismiss, or
risk default under the Georgia Civil Practice Act (O.C.G.A. Title 9,
Chapter 11).

## The two clocks a pro se defendant must not miss

1. **The 30-day answer clock.** Under O.C.G.A. § 9-11-12(a), the
   answer is due **within 30 days after service of the summons and
   complaint**.
2. **The 15-day open-default cure clock.** If no timely answer is
   filed, the case goes into default; O.C.G.A. § 9-11-55(a) lets a
   defendant **open the default as of right within 15 days** of the
   default date on payment of costs. Miss both and the only path is
   the much harder § 9-11-55(b) motion.

Compute exact dates with `ga-deadlines` / `case-calendar.py` — time
runs under O.C.G.A. § 1-3-1(d)(3) (as incorporated by § 9-11-6(a)):
first day excluded, last day counted, roll forward off a weekend or
§ 1-4-1 legal holiday.

## The clock by document

| Document served | Response | Authority |
|---|---|---|
| Summons & civil complaint | **30 days** to answer | O.C.G.A. § 9-11-12(a) |
| Motion to dismiss denied | answer per court's order | O.C.G.A. § 9-11-12(a) |
| Amended complaint | respond within remaining time, or as ordered | O.C.G.A. § 9-11-15(a) |
| Dispossessory (eviction) affidavit | **7 days** to answer | O.C.G.A. § 44-7-51(b) |
| Magistrate Court statement of claim | informal answer (often oral on the return date) | O.C.G.A. §§ 15-10-40 to 15-10-53 |

> ⚠ **Dispossessory is the short fuse.** An eviction answer is due in
> **7 days** under O.C.G.A. § 44-7-51(b), not 30. If the seventh day
> falls on a weekend or holiday it rolls to the next business day.
> See `ga-magistrate`.

## Triage by court

- **State Court** is the usual debt-collection forum (civil actions of
  any amount, no dollar ceiling; see `ga-state-court`). The full
  30-day CPA answer regime applies.
- **Superior Court** handles general civil plus the subjects reserved
  to it (equity, title to land, divorce). Same 30-day answer.
- **Magistrate Court** ($15,000 civil cap) runs an **informal**
  procedure under O.C.G.A. §§ 15-10-40 to 15-10-53 — the CPA and
  evidence rules are relaxed and the answer is often made orally on
  the return date. A losing party may appeal **de novo** to State or
  Superior Court under O.C.G.A. § 15-10-41(b). See `ga-magistrate`.
- **Dispossessory** (Magistrate Court eviction) — the 7-day answer of
  O.C.G.A. § 44-7-51(b) controls.

## Day-by-day playbook

### Days 0-3 — read the complaint and check service

- **Read every numbered paragraph.** Note who is suing, on what
  claims, for what relief, and identify each alleged contract,
  account, or event.
- **Note the court, county, and civil-action file number** — they go
  on every paper (O.C.G.A. § 9-11-10(a)).
- **Check how service happened.** Personal service, service on an
  agent, or one of the § 9-11-4(f) methods (including publication)?
  Defective service is a live defense under O.C.G.A.
  § 9-11-12(b)(4)-(5) (see below).

### Days 3-10 — choose the response path

A defendant has three principal paths:

1. **Answer** — admit, deny, or plead lack of knowledge as to each
   numbered paragraph; assert affirmative defenses; assert any
   counterclaims.
2. **Motion to dismiss** under O.C.G.A. § 9-11-12(b) — tests the
   pleading without answering on the merits.
3. **Both** — certain § 9-11-12(b) defenses may be raised *in* the
   answer rather than by separate motion.

### O.C.G.A. § 9-11-12(b) defenses — when to move to dismiss

Section 9-11-12(b) lists defenses that may be raised by motion:

- **§ 9-11-12(b)(1)** lack of subject-matter jurisdiction
- **§ 9-11-12(b)(2)** lack of personal jurisdiction
- **§ 9-11-12(b)(3)** improper venue
- **§ 9-11-12(b)(4)** insufficiency of process
- **§ 9-11-12(b)(5)** insufficiency of service of process
- **§ 9-11-12(b)(6)** failure to state a claim upon which relief can
  be granted (the most common pre-answer motion)
- **§ 9-11-12(b)(7)** failure to join an indispensable party

> ⚠ **Defense waiver.** The disfavored-defense defenses — lack of
> personal jurisdiction, improper venue, insufficiency of process,
> and insufficiency of service of process — are **waived** if not
> raised in the answer or by a § 9-11-12 motion (O.C.G.A.
> § 9-11-12(h)). Failure to state a claim and lack of
> subject-matter jurisdiction survive longer.

### Days 10-30 — draft the answer (or motion)

#### Answer structure

```
                      ANSWER, AFFIRMATIVE DEFENSES,
                          AND COUNTERCLAIM

Defendant [Name], pro se, answers Plaintiff's Complaint as follows:

                              ANSWER

1. Defendant denies the allegations of Paragraph 1.

2. Defendant is without knowledge or information sufficient to form a
   belief as to the truth of the allegations of Paragraph 2 and
   therefore denies them.

3. Defendant admits the allegations of Paragraph 3.

[...]

                       AFFIRMATIVE DEFENSES

FIRST DEFENSE. The Complaint fails to state a claim upon which relief
can be granted. O.C.G.A. § 9-11-12(b)(6).

SECOND DEFENSE. Plaintiff's claims are barred in whole or in part by
the applicable statute of limitation.

[...]

                            COUNTERCLAIM

[If asserting a counterclaim, plead it as a separate complaint-style
block with numbered factual allegations and named claims.]

                              PRAYER

WHEREFORE, Defendant prays that the Complaint be dismissed, that
Defendant recover costs, and that the Court grant such further relief
as is just.
```

#### Affirmative defenses — O.C.G.A. § 9-11-8(c)

Plead every affirmative defense that may apply; an unpleaded
affirmative defense is generally waived. Section 9-11-8(c) names,
among others:

- Accord and satisfaction
- Arbitration and award
- Discharge in bankruptcy
- Duress
- Estoppel
- Failure of consideration
- Fraud
- Illegality
- Laches
- License
- Payment
- Release
- Res judicata
- Statute of frauds
- **Statute of limitation** (see chart below)
- Waiver

For the debt-buyer affirmative-defense list (standing / chain of
title, account-stated and meeting-of-the-minds defects,
business-records foundation under O.C.G.A. § 24-8-803(6)), see
`ga-consumer-debt`.

### Statute of limitation — Georgia quick chart

| Claim | SOL | Authority |
|---|---|---|
| Written / simple contract | **6 years** | O.C.G.A. § 9-3-24 |
| Open account, oral or implied contract | **4 years** | O.C.G.A. § 9-3-25 |
| Catch-all contract | **4 years** | O.C.G.A. § 9-3-26 |
| Personal injury to the person | **2 years** | O.C.G.A. § 9-3-33 |
| Defamation / injury to reputation | **1 year** | O.C.G.A. § 9-3-33 |
| Trespass / damage to realty | **4 years** | O.C.G.A. § 9-3-30 |
| Injury to / conversion of personalty | **4 years** | O.C.G.A. §§ 9-3-31, 9-3-32 |

Credit-card debt is generally treated as a **written contract**
(6 years, O.C.G.A. § 9-3-24) where the card was used under a written
cardmember agreement. If a debt buyer cannot produce the written
agreement and pleads open account or account stated, the **4-year**
period of O.C.G.A. § 9-3-25 may apply — a foundation gap worth
pressing. A new promise to pay must be **in writing** (O.C.G.A.
§ 9-3-110); part payment supported by written evidence can revive the
period (O.C.G.A. § 9-3-112). Fraud tolls accrual until discovery
(O.C.G.A. § 9-3-96). See `ga-consumer-debt`.

### Counterclaims — O.C.G.A. § 9-11-13

- **Compulsory counterclaim (§ 9-11-13(a)).** Any claim the defendant
  has against the plaintiff **arising out of the same transaction or
  occurrence** must be raised at the time of the answer **or it is
  waived**. Do not assume a related claim "isn't part of this case."
- **Permissive counterclaim (§ 9-11-13(b)).** An unrelated claim may
  be raised but is not required.
- A pro se defendant should plead **all known counterclaims** with
  the answer.

### Amendment as of right — O.C.G.A. § 9-11-15(a)

A party may amend a pleading **as a matter of course at any time
before entry of a pretrial order** under O.C.G.A. § 9-11-15(a). After
the pretrial order, amendment requires leave of court or the
opposing party's written consent. This generous window means a
hurried initial answer can usually be corrected — but the answer
must still be **filed on time** to avoid default.

## The default regime — O.C.G.A. § 9-11-55

This is the heart of the "first 30 days" stakes:

- **Default on the merits.** If the defendant files no answer within
  the 30 days, the case is **in default** and the plaintiff may take
  judgment as if every well-pleaded allegation were admitted
  (O.C.G.A. § 9-11-55(a)).
- **Open as of right — the 15-day cure (§ 9-11-55(a)).** The default
  **may be opened as a matter of right** by filing an answer and
  **paying costs** within **15 days** of the day of default. This is
  the single most important escape valve for a defendant who missed
  the answer date.
- **After the 15 days — § 9-11-55(b).** Once the cure window closes,
  the default may be opened only on motion showing one of three
  grounds — **providential cause**, **excusable neglect**, or a
  **proper case** — and only if the movant also satisfies **four
  conditions**: a meritorious defense, a showing under oath, the
  offer to plead instanter, and payment of costs. See *Bowen v.
  Savoy*, 308 Ga. 204 (2020), on the standard for opening a default.

> ⚠ **Calendar both clocks the moment you are served.** Day 30 for the
> answer; day 30 + 15 for the open-as-of-right deadline if the answer
> slips. Use `ga-deadlines`.

## Filing the answer or motion

- **File** in the court named in the caption (State, Superior, or
  Magistrate) by the deadline, with the civil-action file number.
- **E-file** where required — most Georgia State and Superior civil
  filings are mandatory e-file (PeachCourt or Odyssey eFileGA,
  depending on county). See `ga-statewide-format` and the venue skill
  (`ga-fulton`, `ga-cobb`, `ga-gwinnett`, `ga-county-courts`).
- **Pay the answer filing fee** or apply for a pauper's affidavit /
  fee waiver.
- **Serve** every subsequent paper on all parties under O.C.G.A.
  § 9-11-5 and include a **certificate of service**.

## Composition

- For format baseline: `ga-statewide-format`
- For deadline arithmetic: `ga-deadlines`
- For drafting the answer / motion to dismiss: `ga-draft-motion`
- For the usual debt forum and informal answer practice:
  `ga-state-court`, `ga-magistrate`
- For matter-specific defenses (debt-buyer): `ga-consumer-debt`
- For verifying citations before filing: `ga-fact-check`
- After judgment (opening default, garnishment, exemptions):
  `ga-post-judgment`

## References

- `references/answer-template.md` — full answer / affirmative-defense
  / counterclaim scaffold under the Georgia CPA
- `references/default-and-open-default.md` — the § 9-11-55 timeline,
  the 15-day open-as-of-right cure, and the § 9-11-55(b) four
  conditions (with *Bowen v. Savoy*, 308 Ga. 204 (2020))
- `references/motion-to-dismiss-12b.md` — § 9-11-12(b) defense triage
  and waiver map
