---
name: ga-cobb-codearranger
title: Cobb County courts (Marietta, Georgia)
description: This skill should be used when drafting or filing documents in any Cobb County, Georgia court — the Superior Court of Cobb County (Cobb Judicial Circuit), the State Court of Cobb County, the Cobb County Magistrate Court, or Cobb Probate/Juvenile. Triggers include "file in Cobb County", "Cobb County Superior Court", "Cobb State Court debt suit", "Cobb domestic standing order", "Marietta court", "Cobb magistrate small claims", "PeachCourt Cobb", "Cobb divorce", "Cobb dispossessory", or "Cobb continuing garnishment". Covers which Cobb court hears a given matter, the Cobb caption variants, the two Cobb domestic standing orders that attach automatically at filing, the Domestic Relations Financial Affidavit deadlines, and Cobb's PeachCourt e-filing platform (not Odyssey eFileGA). Layer on top of `ga-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-cobb
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Cobb County courts (Marietta, Georgia)

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Local rules,
> standing orders, judge counts, and addresses change; verify with
> the clerk and the current court pages before relying on anything
> here.

Use this skill in addition to `ga-statewide-format` when the matter is
in a **Cobb County** court. Cobb County is a single-county circuit —
the **Cobb Judicial Circuit** covers only Cobb County. Marietta is the
county seat, and all four trial courts sit there.

The single most important Cobb-specific facts to get right are: (1)
choosing the correct Cobb court for the subject matter, and (2)
remembering that Cobb e-files through **PeachCourt**, not Odyssey
eFileGA, and that in domestic cases the **domestic standing order is
already in force the moment the case is filed**.

## The four Cobb trial courts

### Superior Court of Cobb County

- **70 Haynes Street, Marietta, GA 30090**; 11 Superior Court judges
  (verify the current bench against the court page — judge counts
  change with each legislative add-on and election).
- General-jurisdiction court with **exclusive** jurisdiction over
  divorce, equity, title to land, and felonies (Ga. Const. art. VI,
  § IV; O.C.G.A. § 15-6-8). Powers are catalogued at O.C.G.A.
  § 15-6-8; the circuit/judgeship statute is O.C.G.A. § 15-6-1.
- Domestic-relations cases are assigned **randomly** among the judges
  — there is **no named family division** in Cobb. Whatever judge
  draws the case sets the schedule, so identify the assigned judge
  early and check that judge's individual practices.

### State Court of Cobb County

- **12 East Park Square, Marietta, GA 30090**; 12 State Court judges
  (verify against the current court page).
- Limited-jurisdiction court under O.C.G.A. § 15-7-4. Its **Civil
  Division hears civil actions of ANY amount — there is no dollar
  ceiling** — plus misdemeanors and traffic. It **cannot** hear
  equity, divorce, title, or felonies (those are Superior-exclusive).
- Because the Superior/State split in Georgia is by **subject matter,
  not dollar amount**, the State Court is the **principal forum for
  Cobb debt-collection and tort suits**. A money judgment with no
  equitable component normally belongs here, however large.

### Cobb County Magistrate Court

- **32 Waddell Street, Marietta, GA 30090**.
- **Small claims** up to **$15,000** (O.C.G.A. § 15-10-2(5)).
- **Dispossessory** (eviction) — the $15,000 cap does **not** apply
  to a dispossessory money judgment.
- **Continuing garnishment** — a garnishment runs for **1,095 days**
  once issued.
- A writ of **fieri facias (FiFa)** issues on default (or after **10
  days** if the case is contested) and is recorded on the **Superior
  Court General Execution Docket (GED)** to become a lien.
- Procedure is **informal** — the Civil Practice Act and the evidence
  rules are relaxed (O.C.G.A. §§ 15-10-40 to 15-10-53), parties may
  appear pro se, and a corporation may appear through an officer or
  employee.
- A losing party gets a **de novo appeal** to the State or Superior
  Court (O.C.G.A. § 15-10-41(b)).

### Probate and Juvenile

- **Probate Court** — wills, estates, guardianship/conservatorship,
  involuntary commitment, and the issuance of **marriage licenses and
  weapons-carry licenses**.
- **Juvenile Court** — delinquency, children-in-need-of-services,
  dependency, and termination of parental rights (under 18).

## Caption — Cobb variants

For a Superior Court matter:

```
              SUPERIOR COURT OF COBB COUNTY
                    STATE OF GEORGIA

[PLAINTIFF / PETITIONER NAME],          )
                                        )
        Plaintiff,                      )   Civil Action
                                        )   File No. ____________
   v.                                   )
                                        )
[DEFENDANT / RESPONDENT NAME],          )
                                        )
        Defendant.                      )

                  [TITLE OF DOCUMENT]
```

For a State Court matter, the heading reads **"STATE COURT OF COBB
COUNTY / STATE OF GEORGIA"**; everything else is the same.

- The file-number line is **"Civil Action File No. ____"** — left
  blank for the clerk / PeachCourt to assign at filing; do not invent
  a number.
- Party designations: **Plaintiff / Defendant** in ordinary civil
  cases; **Petitioner / Respondent** in divorce and other domestic
  matters.
- For the page setup (US Letter, 1" margins, 12-pt serif,
  double-spacing, line numbering, footer), follow
  `ga-statewide-format` and O.C.G.A. § 9-11-10.

## E-filing — PeachCourt (NOT Odyssey eFileGA)

Cobb County files through **PeachCourt**, not the Odyssey eFileGA
platform used in many other Georgia counties. **Do not assume
eFileGA** — confirm PeachCourt before preparing an upload.

- **Superior Court** civil e-filing has been **mandatory since
  October 1, 2018**.
- **State Court** e-filing is also **mandatory**.
- **Pro se** litigants **may** e-file through PeachCourt.

PeachCourt **auto-generates** several documents at filing rather than
requiring the filer to supply them:

- the **Case Initiation Form**,
- the **Disclosure Statement**,
- the **Summons**, and
- the **Sheriff's Entry of Service**.

Critically, in a domestic case PeachCourt **auto-attaches the
domestic standing order at the moment of filing** — see the next
section.

## The two Cobb domestic standing orders (a notable trap)

Cobb attaches **two** standing orders in domestic-relations cases.
Both bind the parties as soon as the case is filed — there is no
separate hearing or service step that triggers them, and a filer
unfamiliar with Cobb can violate them without realizing they exist.

### 1. Domestic Relations Standing Order & Rule Nisi

Automatically restrains both parties, from filing, from:

- **removing a child from Georgia for more than one week** —
  **note this is NARROW**: it is a one-week out-of-state-removal
  restraint, **not** a flat anti-relocation clause;
- **harassing** the other party;
- **disposing of assets**, except **in the ordinary course of
  business or for an emergency / necessities**;
- **changing insurance** coverage;
- **disconnecting utilities**; and
- **interfering with the other party's mail**.

It also requires, as part of the domestic case:

- a **Domestic Relations Financial Affidavit (DRFA)** under
  **USCR 24.2**, plus a **Child Support Worksheet**, **filed at least
  15 days before the hearing** and **updated at least 10 days before**
  the hearing; and
- attendance at the divorcing-parents seminar (see the second order).

**Violating the standing order is punishable as contempt.**

### 2. Co-Parenting Seminar Standing Order (USCR 24.8)

- The parties must **complete the co-parenting / divorcing-parents
  seminar within 30 days of the final judgment**.
- There is a **$50 fee**, which is **waivable**.

There is **no business court in Cobb** — Cobb operates accountability
courts (e.g., drug/mental-health courts) but does not participate in a
business-case division.

## Cobb traps for non-Cobb filers

1. **The domestic standing order is already in force at filing.** It
   binds both parties immediately — conduct that is fine pre-filing
   (selling property, changing insurance, taking a child out of state
   for a trip) can become contempt the instant the case is filed.
2. **There are TWO standing orders**, not one — the Domestic
   Relations Standing Order & Rule Nisi *and* the Co-Parenting Seminar
   Standing Order.
3. **The financial-affidavit deadlines are tight** — DRFA + Child
   Support Worksheet at least **15 days** before the hearing, updated
   at least **10 days** before.
4. **The child-removal clause is NARROW** — it restrains taking a
   child out of Georgia for more than a week; it is not a blanket bar
   on relocation, and should not be paraphrased as one.
5. **Cobb uses PeachCourt, not Odyssey eFileGA.** Preparing a filing
   for the wrong platform wastes time; PeachCourt also auto-generates
   the case-initiation paperwork and auto-attaches the standing order.

## Composition

- `ga-statewide-format` — page setup, caption baseline, line numbering
- `ga-state-court` — civil-any-amount practice (the principal Cobb
  forum for debt/tort)
- `ga-magistrate` — small claims, dispossessory, garnishment mechanics
- `ga-family-court` — divorce/domestic drafting and the DRFA
- `ga-consumer-debt` — debt-collection subject-matter content
- `ga-first-30-days` — answer, defenses, counterclaims
- `ga-file-packet` — assembling and preflighting a Cobb filing
- `ga-schedule-hearing` — Rule Nisi and hearing-setting mechanics
- `ga-deadlines` — time computation and the 15-day/10-day DRFA windows

## References

- `references/cobb-superior-local-practice.md` — Superior Court bench,
  random domestic assignment, local practices, addresses to verify
- `references/cobb-standing-orders.md` — full text/summary of the two
  domestic standing orders and the DRFA / Child Support Worksheet
  deadlines
- `references/cobb-efiling-peachcourt.md` — PeachCourt workflows,
  auto-generated documents, pro se e-filing
- `references/cobb-magistrate-small-claims.md` — small-claims cap,
  dispossessory, continuing garnishment, FiFa / GED recording
