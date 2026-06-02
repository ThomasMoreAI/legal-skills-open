---
name: co-denver
title: Denver District Court (2nd Judicial District)
description: This skill should be used when drafting or filing documents in the Denver District Court (2nd Judicial District) or Denver County Court. Triggers include "Denver District Court", "Denver County Court", "2nd JD", "Lindsey-Flanigan Courthouse", "Colorado civil division Denver", or any case with a case number in the format "2025CV031234" or "2025C0##### " filed in Denver. Covers the Lindsey-Flanigan Courthouse civil divisions, the 2nd JD's local rules and case-management practices, the Denver District Court's use of Colorado Courts E-Filing System (CCEFS), the Civil Division motion-practice norms (chambers / division assignments, judge's preferences), and 2nd JD Administrative Orders. Layer on top of `co-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-denver
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Denver District Court (2nd Judicial District)

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> every step against the current 2nd JD local rules and chambers
> preferences before filing.

Use this skill in addition to `co-statewide-format` when the case is
in the **Denver District Court** or **Denver County Court** (the 2nd
Judicial District). Denver is unique among Colorado JDs in that the
City and County of Denver is coextensive with one judicial district,
so the 2nd JD covers only Denver County.

- **District Court** — handles civil claims over $25,000, all
  domestic relations, probate, mental health, juvenile, and criminal
  felony matters. C.R.S. § 13-5-126.
- **County Court** — limited jurisdiction up to $25,000, eviction
  (FED), small claims (up to $7,500 under C.R.S. § 13-6-403),
  traffic, and misdemeanors. C.R.C.P. 312.1.

Both courts sit primarily at the **Lindsey-Flanigan Courthouse**,
520 W. Colfax Ave., Denver, CO 80204, though specialty divisions
(probate, juvenile) sit at separate facilities.

## Caption — Denver District Court variant

```
DISTRICT COURT, CITY AND COUNTY OF DENVER, COLORADO
Lindsey-Flanigan Courthouse
520 W. Colfax Ave.
Denver, CO 80204

Plaintiff(s): MIDLAND CREDIT MANAGEMENT, INC.,    ▲ COURT USE ONLY ▲
                                                  ┌───────────────────┐
v.                                                │ Case Number:      │
                                                  │  2025CV031234     │
Defendant(s): JANE DOE.                           │                   │
                                                  │ Division: 209     │
                                                  │ Courtroom: 209    │
                                                  └───────────────────┘

                  ANSWER AND COUNTERCLAIM
```

For **Denver County Court** (limited jurisdiction), the heading
substitutes "COUNTY COURT, CITY AND COUNTY OF DENVER, COLORADO" and
the case-number format becomes `2025C0######` (a "C0" prefix).

## Case-number formats

| Court | Format | Example |
|-------|--------|---------|
| District Court — civil | `YYYYCV0#####` | `2025CV031234` |
| District Court — domestic relations | `YYYYDR0#####` | `2025DR031234` |
| District Court — probate | `YYYYPR0#####` | `2025PR031234` |
| County Court — civil | `YYYYC0######` | `2025C0123456` |
| County Court — eviction (FED) | `YYYYC0######` (subset) | `2025C0123457` |
| County Court — small claims | `YYYYS0######` | `2025S0123456` |

The case number is assigned at filing by CCEFS; do not invent or
guess. The "Division" number identifies the chambers (a single
judge); the "Courtroom" number identifies the physical room.
**Division ≠ Courtroom in Denver** (unlike many smaller JDs where
they often match).

## Division and judge assignment

The Denver District Court has 23 active civil divisions. Civil cases
are assigned randomly by CCEFS at filing; complex commercial matters
may be assigned to a designated commercial calendar under the 2nd
JD's Business Court program.

The clerk's office publishes a current judge-and-division roster:

**https://www.coloradojudicial.gov/courts/judicial-districts/2nd-judicial-district**

Agent behavior: when drafting a notice, scheduling a hearing, or
preparing for an appearance, fetch the current division-judge mapping
and the assigned judge's chambers-specific practice standards. Many
Denver judges publish **practice standards** that supplement the
C.R.C.P. and 2nd JD local rules — these change at judicial rotation
and after any new judicial appointment.

## Motion practice — C.R.C.P. 121 § 1-15 + judge's practice standards

Motions in Denver follow the statewide C.R.C.P. 121 § 1-15 timing:

- **Motion**: filed any time (no advance leave required for most
  motions)
- **Response**: due **21 days** after service of the motion
  (C.R.C.P. 121 § 1-15(1)(b))
- **Reply**: due **7 days** after service of the response
  (C.R.C.P. 121 § 1-15(1)(d))
- **Hearings**: decided on the briefs unless the court orders oral
  argument. The court will issue a **Notice of Setting** when it sets
  a hearing — the parties do not self-schedule.

**Page limits** under C.R.C.P. 121 § 1-15(1)(a):

- Motion / response: **15 pages**
- Reply: **10 pages**
- Excess pages require leave of court via a separate motion.

Many Denver judges' practice standards modify these defaults — e.g.,
requiring a **chambers copy** (a paper "judge's copy") for motions
exceeding 25 pages, requiring **certificates of conferral** under
C.R.C.P. 121 § 1-15(8), or imposing **bench-book deadlines** for
expert disclosures. Always check the assigned judge's practice
standards before filing.

## Certificate of conferral / duty to confer (C.R.C.P. 121 § 1-15(8))

For non-dispositive motions, the moving party must, **before filing**,
**confer with all opposing parties** to attempt to resolve the
dispute and must include a statement at the foot of the motion
certifying:

- **Whether** the moving party has conferred
- **Whether** the other parties agree or disagree (or non-response)

Example certificate language:

```
                CERTIFICATE OF CONFERRAL
                (C.R.C.P. 121 § 1-15(8))

Pursuant to C.R.C.P. 121 § 1-15(8), the undersigned conferred with
[opposing counsel / opposing party] on [date] regarding the relief
requested in this Motion. [Opposing counsel] [opposes / does not
oppose / takes no position on] the Motion.
```

Failure to confer is a frequent ground for summary denial in Denver;
the certificate is **mandatory** for non-dispositive motions, and
dispositive motions (Rule 12(b), Rule 56) are excused but should
still document any attempts to resolve.

## Case management — C.R.C.P. 16 + Denver practice

Within ~28 days after the case is at issue, the parties must file a
**Proposed Case Management Order** under C.R.C.P. 16(b). The Denver
District Court's practice is:

- The court issues a **Delay Reduction Order** at filing that sets
  initial deadlines (typically the C.R.C.P. 16(b) defaults)
- The parties **confer** under C.R.C.P. 16(b)(2) and file a joint
  proposed CMO 7 days before the initial CMC
- The court holds an **initial Case Management Conference** ~ 49 days
  after the case is at issue (C.R.C.P. 16(b)) — by phone or
  in-person at the judge's discretion

Failure to comply with C.R.C.P. 16 can result in striking pleadings
or sanctions; Denver is known for active case management.

## Filing — CCEFS (Colorado Courts E-Filing)

Attorneys must e-file through **Colorado Courts E-Filing (CCEFS)**:

**https://www.jbits.courts.state.co.us/efiling/**

Pro se filers may either:

- Use **CCEFS Pro Se** (free account; requires verification) — only
  active in some county courts but expanding to district court
- File **paper** at the Lindsey-Flanigan Courthouse clerk's window
  (basement level)
- Use **email filing** when the clerk has authorized it for a
  specific case

The Denver Clerk's Office: (720) 865-8301. Civil division clerk:
(720) 865-8410.

Filing fees (district court civil):

- New complaint: $235 (standard) or higher per damages tier under
  C.R.S. § 13-32-101
- Answer/response: $192
- Most motions: no separate filing fee
- Fee waiver: file **JDF 205** (Motion to File without Payment) +
  **JDF 206** (Affidavit) — see C.R.S. § 13-16-103

## Service of process and service of pleadings

- **Initial service of process** must be by a sheriff, private
  process server, or otherwise per C.R.C.P. 4 within 63 days of
  filing the complaint
- **Subsequent papers** are served per C.R.C.P. 5 — CCEFS e-service
  is automatic for represented parties; pro se opposing parties may
  require service by mail, hand delivery, or email under C.R.C.P.
  5(b)(2)(E)
- **Certificate of service** required on every filed paper

## Document set for a filed motion

A Denver motion packet should travel as:

1. **Motion** (with title in ALL CAPS, citing the rule invoked)
2. **Supporting Affidavit / Declaration(s)** with exhibits
3. **Certificate of Conferral** (C.R.C.P. 121 § 1-15(8)) — included
   in the motion or as the last page
4. **Proposed Order** granting the relief (separate document)
5. **Certificate of Service**

CCEFS requires each component to be uploaded as a **separate PDF**
with the matching document code.

## Self-help / pro se resources

The 2nd JD operates a **Self-Help Center** at the Lindsey-Flanigan
Courthouse and online: courts staff cannot give legal advice but can
help with form selection and procedure. The Colorado Judicial Branch
publishes **JDF (Judicial Department Forms)** for most pro se uses:

**https://www.coloradojudicial.gov/self-help**

Common JDF forms for civil cases:

- **JDF 76** — Answer (county court civil)
- **JDF 80** — Civil Cover Sheet (district court)
- **JDF 205 / 206** — Motion / Affidavit to File without Payment
- **JDF 1402** — Pro Se Notice of Appeal (limited jurisdiction)

## Composition

- For statewide format: `co-statewide-format`
- For drafting the motion itself: `co-draft-motion`
- For setting hearings: `co-schedule-hearing`
- For filing mechanics: `co-file-packet`
- For pro se conventions: `co-pro-se`

## References

- `references/lindsey-flanigan-courthouse.md` — facility info,
  divisions, parking
- `references/civil-divisions.md` — division-to-judge mapping and
  judge's practice standards index
- `references/filing-procedures.md` — CCEFS workflows, document codes,
  service mechanics
- `references/business-court.md` — Denver's commercial-case program
