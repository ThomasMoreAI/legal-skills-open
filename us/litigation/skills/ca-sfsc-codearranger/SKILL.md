---
name: ca-sfsc-codearranger
title: San Francisco Superior Court (SFSC)
description: This skill should be used when drafting or filing documents in San Francisco Superior Court (SFSC), the superior court serving the City and County of San Francisco. Triggers include "San Francisco Superior Court", "SFSC", "Civic Center Courthouse", "400 McAllister", "Hall of Justice San Francisco", "Dept. 302", "Department 302 San Francisco", "law and motion San Francisco", "reserve a hearing in Dept. 302", "SFSC local rules", "SF Superior Court", "San Francisco tentative ruling", "SFSC eFiling", "File and ServeXpress San Francisco", "ADR San Francisco", "San Francisco case management", "civil motion calendar San Francisco", or any case with an SFSC case number (e.g., CGC-24-123456, CUD-24-123456). Covers SFSC Local Rules, the Dept. 302 law-and-motion calendar, tentative-ruling practice, mandatory eFiling through File & ServeXpress, the SFSC ADR program, and case management conferences. Layer on top of `ca-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-sfsc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Civic Center Courthouse
  path: references/civic-center-courthouse.md
- title: Dept 302 Law And Motion
  path: references/dept-302-law-and-motion.md
- title: Sfsc Local Rules
  path: references/sfsc-local-rules.md
---

# San Francisco Superior Court (SFSC)

Use this skill in addition to `ca-statewide-format` when the
case is in the San Francisco Superior Court. The City and County
of San Francisco is a consolidated city-county; the superior
court serves all civil filings for San Francisco.

## Court locations

| Courthouse | Address | Divisions |
|------------|---------|-----------|
| **Civic Center Courthouse** | 400 McAllister St., San Francisco 94102 | Civil (unlimited), probate, complex civil, family law, appellate |
| **Hall of Justice** | 850 Bryant St., San Francisco 94103 | Criminal, unlawful detainer, small claims, traffic, some limited civil |

For general civil (unlimited civil), all filings and hearings
are at the **Civic Center Courthouse, 400 McAllister Street**.
The building is directly across the street from City Hall and
adjacent to the San Francisco Public Library main branch.

- Clerk's office: Ground floor (Room 103)
- Civil Division clerk: (415) 551-3888
- Court website: **https://www.sfcourts.org**

## Case number formats

| Format | Case type | Example |
|--------|-----------|---------|
| `CGC-YY-NNNNNN` | General civil (unlimited) | `CGC-24-123456` |
| `CUD-YY-NNNNNN` | Unlawful detainer (civil) | `CUD-24-123456` |
| `CLC-YY-NNNNNN` | Limited civil | `CLC-24-123456` |
| `CPF-YY-NNNNNN` | Probate / family (civil side) | `CPF-24-123456` |
| `SCN-YY-NNNNNN` | Small claims | `SCN-24-123456` |

Pull the exact case number from **https://efiling.sfcourts.org**
or the SFSC case portal by searching by party name.

## Caption — SFSC variant

The court name line for SFSC cases:

```
              IN THE SUPERIOR COURT OF CALIFORNIA
                 COUNTY OF SAN FRANCISCO
```

Note: San Francisco is both the city and the county — the caption
reads "COUNTY OF SAN FRANCISCO" even though the filing entity
is formally the City and County of San Francisco.

## Mandatory eFiling — File & ServeXpress

SFSC mandates electronic filing for represented parties in civil
cases through **File & ServeXpress** (FServeXpress).

- Portal: **https://www.fileandservexpress.com/**
- SFSC-specific help: **https://www.sfcourts.org/civil-division/efiling/**
- Accepted format: PDF only
- File-size limit: varies by document type; typically 10-25 MB
  per document
- Account required: attorneys must register a firm account;
  pro se filers may use a self-represented-filer account

Pro se (self-represented) filers may still paper-file at the
clerk's counter (Room 103, Civic Center Courthouse) during
business hours: Monday-Friday, 8:30 a.m.-4:00 p.m. (verify
current hours at **https://www.sfcourts.org**).

## Department 302 — Law and Motion

Department 302 is the SFSC **law and motion department** for
general unlimited civil cases. It handles:

- Demurrers (Code Civ. Proc., § 430.10 et seq.)
- Motions to strike (Code Civ. Proc., § 435 et seq.)
- Discovery motions (Code Civ. Proc., § 2016.010 et seq.)
- Motions for summary judgment/adjudication (Code Civ. Proc.,
  § 437c)
- All other law and motion matters in unlimitied civil cases
  not assigned to a specific complex or writs department

**Department 302 location**: Civic Center Courthouse, Room 302
(third floor)

**Hearing schedule**: Dept. 302 law-and-motion calendar is
typically held at **9:00 a.m. on court days** (Monday-Friday,
excluding court holidays). Some motions may be calendared at
other times; confirm on the reservation system.

**Department 302 clerk contact**:
- Phone: (415) 551-4012 (confirm current number at sfcourts.org)
- For ex parte matters: call Dept. 302 directly

**Note on department assignment**: Not all civil motions go to
Dept. 302. Cases assigned to the **Complex Civil Program**
(Dept. 302 handles the general civil law-and-motion but complex
cases have dedicated departments, currently Dept. 302 and Dept.
610). Cases in the direct-calendar system (rare) go to the
assigned judge's department. Confirm the correct department on
the case portal before reserving a hearing.

## Reservation system — SFSC Civil Reservation

To reserve a law-and-motion date in Dept. 302:

**Step 1 — Access the SFSC Civil Reservation System**

Go to: **https://www.sfcourts.org/civil-division/reservations/**

Log in with a court account or proceed as a guest. Select
"Department 302 — Law and Motion" from the department menu.

**Step 2 — Select motion type and date**

Choose the motion type from the dropdown (Demurrer, Motion to
Compel, MSJ, etc.). Select an available date. The system will
display available 9:00 a.m. calendar slots.

**Step 3 — Record the reservation number**

The system issues a **Reservation ID** (also called a "reservation
number"). Include this on the face of the Notice of Motion:

```
Date:  [Reserved date]
Time:  9:00 a.m.
Dept.: 302
Judge: Honorable [Assigned Judge]
Reservation ID: [Number]
```

**Step 4 — File the motion with the reserved date**

File through File & ServeXpress. Select Department 302 in the
filing portal. Ensure the reserved date in the motion matches
the reservation system.

**Timing rules**: California law requires the moving party to
give at least **16 court days' notice** before most civil motions
under Code Civ. Proc., § 1005(b). Count court days (excluding
Saturdays, Sundays, and holidays). Add 5 calendar days if service
is by mail (Code Civ. Proc., § 1005(b)); 2 court days if by
overnight courier; 0 if by hand or electronic service.

## Tentative-ruling regime (CRC 3.1308; SFSC Local Rule 8.3)

SFSC Dept. 302 uses a tentative-ruling system under Cal. Rules
of Court, rule 3.1308(a)(1) and SFSC Local Rule 8.3:

1. **Tentative ruling posted**: by **4:00 p.m. the court day
   before** the hearing date.

2. **Where to find tentatives**:
   **https://www.sfcourts.org/civil-division/tentative-rulings/**
   Search by case number or department. Alternatively, call
   Dept. 302 at (415) 551-4012 the afternoon before the hearing.

3. **Contest the tentative**:
   - Any party wishing to argue must notify **all other parties**
     AND **Dept. 302** by **4:00 p.m.** on the court day before
     the hearing.
   - Notify the department by phone: (415) 551-4012.
   - If no party timely contests, the tentative **automatically
     becomes the order** without a hearing.

4. **If contested**: hearing proceeds at the scheduled time.
   The court may adopt, modify, or reject the tentative at its
   discretion.

5. **Uncontested tentative practice**: If you are satisfied with
   the tentative and the opposing party has not contested by
   4:00 p.m., you need not appear. The tentative is entered as
   the order.

**Practical checklist the afternoon before a SFSC hearing**:

- [ ] Check tentative on sfcourts.org by 4:00 p.m.
- [ ] If unfavorable or unclear: call Dept. 302 clerk by 4:00 p.m.
      to contest; immediately call/email opposing counsel/party
- [ ] If favorable and no contest: no appearance required;
      confirm by calling Dept. 302 at 8:30 a.m. the morning of
      the hearing

## SFSC ADR program

San Francisco Superior Court has one of the most active
**Alternative Dispute Resolution (ADR)** programs in California.
SFSC Local Rules, Division IV govern ADR.

**ADR forms**:
- **Early Neutral Evaluation (ENE)**: A neutral evaluator gives
  a non-binding assessment; particularly effective in contract
  and commercial cases
- **Mediation**: Private mediator selected by the parties from
  the SFSC panel or by agreement; court will order mediation
  at the CMC
- **Arbitration** (non-binding judicial arbitration): For cases
  at or below $50,000 (Code Civ. Proc., § 1141.11; SFSC Local
  Rule 4.1)

**ADR timeline**:
- At the CMC, the court typically orders ADR to be completed
  within a specified period before the trial date
- Parties must complete ADR before the Final Status Conference
  (FSC) or risk sanctions
- ADR coordinator: SFSC ADR Office, (415) 551-3876

**Mediator panel**: https://www.sfcourts.org/adr/

## Case management conferences (CMC) at SFSC

SFSC schedules a CMC approximately 180 days after filing of the
complaint (SFSC Local Rules).

**CMC statement (CM-110)**:
- File and serve form CM-110 no later than **15 calendar days**
  before the CMC (Cal. Rules of Court, rule 3.725(c))
- The CM-110 asks about ADR, trial estimate, discovery, related
  cases, and case complexity
- SFSC requires that the parties confer before the CMC about ADR
  selection (SFSC Local Rule)

**At the CMC**: the judge sets trial date, discovery cutoff,
motion cutoff, FSC date, and ADR deadline. SFSC CMCs are
typically brief (5-10 minutes) unless the case involves complex
scheduling issues.

## SFSC Local Rules — key sections

SFSC Local Rules are posted at:
**https://www.sfcourts.org/civil-division/local-rules/**

| Rule | Subject |
|------|---------|
| 2.1 | Case management — filing requirements |
| 2.4 | Related cases |
| 3.1–3.6 | CMC, case schedule |
| 4.1–4.12 | ADR program |
| 5.1 | Discovery conferences |
| 5.3 | Discovery disputes — meet-and-confer requirements |
| 7.1 | Law and motion — notice requirements |
| 8.1–8.4 | Dept. 302 law-and-motion calendar and tentative rulings |
| 9.1 | Summary judgment motions |
| 10.1 | Complex Civil Program |
| 11.1 | Unlawful detainer — expedited schedule |

Key civil discovery rule: Code Civ. Proc., § 2016.040 requires
a written meet-and-confer declaration for all discovery motions.
SFSC Local Rule 5.3 elaborates — parties must meet and confer
by telephone or in person (email alone is not sufficient in SFSC
practice unless the parties have agreed in writing to use email
for M&C).

## Separate statement (discovery motions)

Same as LASC: Cal. Rules of Court, rule 3.1345 requires a
Separate Statement for motions to compel further discovery
responses. File as a separate document.

## Filing fees

Same Government Code schedule as all California superior courts
(Gov. Code, §§ 70600-70679). SFSC-specific note: SFSC adds a
$20 "Complex Litigation" surcharge for cases initially designated
complex. Check current fees at **https://www.sfcourts.org/fees/**.

Fee waiver: Cal. Rules of Court, rule 3.50; Judicial Council form
FW-001.

## Document set for a noticed motion in SFSC Dept. 302

1. **Notice of Motion and Motion** (with SFSC Reservation ID,
   date 9:00 a.m., Dept. 302, judge, in caption)
2. **Memorandum of Points and Authorities**
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order**
5. **Separate Statement** (for discovery motions; CRC 3.1345)
6. **Proof of Service** (POS-030 or declaration of service)

File each as a separate PDF through File & ServeXpress, selecting
Department 302.

## Ex parte applications — SFSC

For emergency relief before a noticed hearing:

- Notice to all parties by **10:00 a.m.** the court day before
  the ex parte application (CRC 3.1203)
- File the application at the Civic Center clerk's window (Room
  103) or through File & ServeXpress; submit to Dept. 302
- Bring a proposed order and a declaration of notice

Ex parte matters are heard at the start of Dept. 302's calendar,
typically at 9:00 a.m., unless the judge directs otherwise.

## References

- `references/civic-center-courthouse.md` — Civic Center
  Courthouse venue details, parking, clerk's office, room guide
- `references/dept-302-law-and-motion.md` — Dept. 302 calendar,
  tentative-ruling protocol, reservation step-by-step
- `references/sfsc-local-rules.md` — SFSC local rules summary
  for civil practice, discovery, ADR, and case management

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
