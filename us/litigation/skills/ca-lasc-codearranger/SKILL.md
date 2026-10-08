---
name: ca-lasc-codearranger
title: Los Angeles Superior Court (LASC)
description: Use when drafting or filing in Los Angeles Superior Court (LASC), the largest unified trial court in the U.S. Triggers include "Los Angeles Superior Court", "LASC", "Stanley Mosk Courthouse", "Spring Street Courthouse", "LASC Court Reservation System", "LASC CRS", "LASC tentative ruling", "LASC local rules", "Odyssey eFileCA Los Angeles", "CMC statement CM-110", or LASC case numbers (24STCV12345, 24CMCV12345). Covers LASC local rules, Court Reservation System (CRS), tentative-ruling regime, mandatory eFiling via Odyssey eFileCA, and case management conferences. Layer on `ca-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-lasc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Civil Motion Scheduling
  path: references/civil-motion-scheduling.md
- title: Downtown Central
  path: references/downtown-central.md
- title: Lasc Local Rules
  path: references/lasc-local-rules.md
---

# Los Angeles Superior Court (LASC)

Use this skill in addition to `ca-statewide-format` when the
case is in any Los Angeles Superior Court courthouse. LASC is
the largest unified trial court in the United States with
approximately 500 judicial officers serving over 10 million
residents across a county the size of Connecticut and Rhode
Island combined.

## Court locations and civil divisions

LASC has over 30 courthouses. The major civil venues are:

| Courthouse | Address | Case types (civil) |
|------------|---------|-------------------|
| **Stanley Mosk Courthouse** (Central) | 111 N. Hill St., Los Angeles 90012 | Unlimited civil (the flagship); most complex litigation departments |
| **Spring Street Courthouse** | 312 N. Spring St., Los Angeles 90012 | Unlimited civil departments, writs, and appeals |
| **Norwalk Courthouse** | 12720 Norwalk Blvd., Norwalk 90650 | Unlimited and limited civil — Southeast District |
| **Pomona Courthouse South** | 400 Civic Center Plaza, Pomona 91766 | Unlimited and limited civil — East District |
| **Van Nuys Courthouse East/West** | 14340 Sylvan St. / 6230 Sylvan St., Van Nuys 91401 | Unlimited and limited civil — Northwest District |
| **Pasadena Courthouse** | 300 E. Walnut St., Pasadena 91101 | Unlimited civil — Northeast District |
| **Long Beach Courthouse** | 275 Magnolia Ave., Long Beach 90802 | Unlimited and limited civil — South District |
| **Compton Courthouse** | 200 W. Compton Blvd., Compton 90220 | Limited civil — Southwest District |
| **Torrance Courthouse** | 825 Maple Ave., Torrance 90503 | Unlimited and limited civil — Southwest District (Torrance) |
| **Glendale Courthouse** | 600 E. Broadway, Glendale 91206 | Limited civil; unlawful detainer — North District |
| **Chatsworth Courthouse** | 9425 Penfield Ave., Chatsworth 91311 | Unlimited and limited civil — Northwest District (West) |

The department assignment is determined at case filing based on
case type, courthouse of filing, and random assignment (LASC
General Order for civil case assignment). Confirm the department
and courthouse on the LASC case portal.

## Case number formats

| Format | Case type | Example |
|--------|-----------|---------|
| `YYXXXXXXXX` (Stanley Mosk) | Unlimited civil (Central) | `24STCV12345` |
| `YYNWCVNNNNN` | Unlimited civil (Northwest/Van Nuys) | `24NWCV00001` |
| `YYCMCVNNNNN` | Civil — Compton | `24CMCV00001` |
| `YYSMCVNNNNN` | Limited civil (Stanley Mosk) | `24SMCV00001` |
| Various district codes | Other districts | `24PSCV`, `24LBCV`, `24GDCV` etc. |

Pull the exact case number format from the LASC case portal:
**https://www.lacourt.org** — search by party name to confirm the
case number and assigned department.

## Caption — LASC variant

The court name line for LASC cases:

```
              IN THE SUPERIOR COURT OF CALIFORNIA
                   COUNTY OF LOS ANGELES
```

For cases assigned to a specific district courthouse, some
practitioners add the courthouse name below the county line,
but this is not required by CRC 2.111. The case number suffix
identifies the district (e.g., ST = Stanley Mosk, NW =
Northwest, CM = Compton).

## Mandatory eFiling — Odyssey eFileCA

LASC mandates electronic filing for represented parties in civil
cases through **Odyssey eFileCA** (Tyler Technologies). Pro se
(self-represented) filers may, but are not required to, use the
e-filing system.

- Portal: **https://efiling.lacourt.org** (LASC-specific entry
  point into the Odyssey platform)
- Accepted format: PDF only
- File-size limit: 25 MB per document; split larger filings
- Filing fee payment: credit card via portal
- Service of process: Odyssey does not handle initial service;
  use traditional service (process server, sheriff, etc.) for
  summons and complaint
- eService for subsequent filings: parties who register on the
  portal receive eService automatically

Self-represented filers may also paper-file at the clerk's
counter during business hours. Hours vary by courthouse — check
**https://www.lacourt.org/courthouse/** for current hours.

## LASC Court Reservation System (CRS)

For civil motions in unlimited civil cases, the moving party
must **reserve a hearing date** through the LASC Court Reservation
System (CRS) **before** filing the motion (or at the time of
filing in some departments). The CRS is the LASC's online
reservation portal.

**Step 1 — Identify the assigned department and courthouse**

Check the LASC case portal at **https://www.lacourt.org** for
the assigned department. The department determines which
reservation calendar to use.

**Step 2 — Access the CRS**

Go to: **https://www.lacourt.org/courtreservation/ui/index.aspx**

Create an account or log in. Select the courthouse, department,
and motion type from the dropdown menus.

**Step 3 — Reserve a date**

Select an available date from the calendar. The CRS will issue
a **reservation number** (also called a "CRS number" or "booking
number"). Record this number — it goes on the face of the
motion.

**Step 4 — Include the CRS number on the motion**

In the caption area of the Notice of Motion, state:

```
Date:  [Reserved date]
Time:  [Reserved time, e.g., 10:00 a.m. / 8:30 a.m.]
Dept.: [Department number]
Judge: Hon. [Judge name]
Reservation No.: [CRS confirmation number]
```

**Step 5 — File the motion with the reserved date**

File through Odyssey eFileCA with the correct department selected.
The clerk will confirm or reject the filing; an accepted filing
appears in the case portal.

**CRS notes**:
- Not all departments use the CRS; some departments have
  independent calendaring through the department clerk.
  Always confirm which method the assigned department uses —
  check the LASC department pages at **https://www.lacourt.org/division/civil/civil.aspx**
- For ex parte applications, the CRS is not used; ex parte
  matters are set by calling the department clerk directly.
- Some departments require a minimum notice period (e.g., 16
  court days for a Code Civ. Proc., § 1005 motion); make sure
  the reserved date meets the statutory notice requirement.

## Tentative-ruling regime (CRC 3.1308; LASC Local Rule 3.31)

LASC uses a tentative-ruling system for most civil law and
motion hearings under Cal. Rules of Court, rule 3.1308(a)(1) and
LASC Local Rule 3.31:

1. **Tentative ruling posted**: The court posts its tentative
   ruling by **2:00 p.m. the court day before** the hearing
   (i.e., by 2:00 p.m. on Monday for a Tuesday 10:00 a.m.
   hearing).

2. **Where to find tentatives**: **https://www.lacourt.org/tentativerulingweb/ui/**
   Search by case number or department.

3. **Contest the tentative**:
   - Any party who wishes to argue (contest the tentative) must
     notify **all other parties** and the **department clerk** by
     **4:00 p.m.** on the court day before the hearing.
   - Call the clerk's phone line for the specific department.
     Department phone numbers are listed at the LASC website.
   - If no party contests, the tentative becomes the **final
     ruling** without a hearing.

4. **If contested**: the hearing proceeds as scheduled. The
   judge may adopt, modify, or reject the tentative at the hearing.

5. **No hearing on uncontested tentatives**: If you are satisfied
   with the tentative and no other party contests, you do not
   need to appear. The tentative is automatically entered as the
   court's order.

**Practical workflow**:

- Check the tentative by 2:00 p.m. the day before the hearing
- If unfavorable: call the department clerk by 4:00 p.m. to
  contest, then call or email opposing counsel/party
- If favorable: confirm no other party has contested; no
  appearance required

## Case management conferences (CMC)

LASC schedules a Case Management Conference (CMC) approximately
120 days after the filing of the complaint (Cal. Rules of Court,
rule 3.722).

**CMC statement (form CM-110)**:
- File and serve the Judicial Council form CM-110 no later than
  **15 calendar days** before the CMC (Cal. Rules of Court, rule
  3.725(c))
- The CM-110 asks about service of process, ADR, trial estimate,
  related cases, and discovery status
- Both sides must file separate CM-110s unless they agree to a
  joint CM-110

**At the CMC**: the judge sets the trial date, discovery cut-off,
motion cut-off, FSC (Final Status Conference), and ADR deadline.
The CMC order (sometimes called a "Case Schedule Order") controls
the case timeline.

## LASC local rules — key sections

LASC Local Rules (California Rules of Court, local rules of the
Superior Court of California, County of Los Angeles):

| Rule | Subject |
|------|---------|
| 2.2 | Electronic filing — mandatory for represented parties |
| 2.3 | Electronic service |
| 3.5 | Trial date setting and continuances |
| 3.10 | Motions in limine |
| 3.20–3.25 | Summary judgment practice |
| 3.26 | Demurrers |
| 3.28 | Case management and CMC |
| 3.31 | Tentative rulings |
| 3.57 | Discovery motions — separate statement requirement |
| 7.9 | Unlawful detainer |
| 8.90–8.100 | Complex litigation (Complex Civil Program at CCW) |

The full LASC Local Rules are posted at:
**https://www.lacourt.org/rules/ui/index.aspx**

Always pull the current version before citing — LASC updates
local rules regularly, typically with each new calendar year.

## Separate statement (discovery motions)

For any motion to compel further discovery responses in LASC,
a **Separate Statement** is required under Cal. Rules of Court,
rule 3.1345 and LASC Local Rule 3.57. The separate statement:

- Sets out each discovery request in full
- States the response given by the responding party
- States why the response is deficient (good cause argument)
- Is filed and served as a **separate document** from the motion
  (not incorporated into the memorandum)

Failure to file a separate statement is grounds for denial of
the motion. Use the required format from CRC 3.1345(c).

## Complex litigation

Cases designated as complex civil litigation under Cal. Rules
of Court, rule 3.400 are sent to the **Complex Civil Program**,
located at the **Central Civil West Courthouse** (600 S.
Commonwealth Ave., Los Angeles 90005). Complex cases have their
own rules, CMC procedures, and department-specific standing
orders. Common complex designations: class actions, coordinated
proceedings, construction defect, environmental, securities
fraud, mass torts.

## Filing fees

LASC follows the Government Code schedule:

- Complaint (unlimited civil): $435 (Gov. Code, § 70611; subject
  to annual inflation adjustment)
- Complaint (limited civil, over $10,000): $225
- Motion: $60 per motion (Gov. Code, § 70617)
- Summary judgment motion: $500 (Gov. Code, § 70617(e))
- Fee waiver: Cal. Rules of Court, rule 3.50–3.63; Judicial
  Council form FW-001

Pull current fees from **https://www.lacourt.org/division/civil/fees.aspx**
before advising on specific amounts — fees change with the
Government Code.

## Document set for a noticed motion in LASC

1. **Notice of Motion and Motion** (with CRS reservation number,
   date, time, dept., and judge in the caption)
2. **Memorandum of Points and Authorities** (filed separately
   or combined with the motion)
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order** (titled "[PROPOSED] ORDER")
5. **Separate Statement** (required for discovery motions under
   CRC 3.1345; not required for non-discovery motions)
6. **Proof of Service** (Judicial Council form POS-030 or
   declaration of service under Code Civ. Proc., § 1013a)

eFile each as a separate PDF through Odyssey eFileCA.

## Scheduling email — ex parte applications

For **ex parte** relief (emergency relief before a noticed
hearing), contact the assigned department clerk directly. The
LASC ex parte procedure requires:

1. **Notice to all parties**: by **10:00 a.m. the court day
   before** the ex parte application, unless exceptional
   circumstances prevent prior notice (Cal. Rules of Court, rule
   3.1203)
2. **Application**: filed at the clerk's window or submitted
   via eFiling at the start of the court day (typically 8:30 a.m.)
3. **Declaration re notice**: explaining who was notified, when,
   and by what method (or why notice was not given)

Ex parte relief standards: immediate danger of irreparable harm;
inability to seek relief through a regularly noticed motion
(Cal. Rules of Court, rule 3.1202(c)).

## References

- `references/downtown-central.md` — Stanley Mosk and Spring
  Street courthouse details, parking, clerk windows, courtroom
  layout
- `references/civil-motion-scheduling.md` — CRS step-by-step,
  notice requirements, discovery-motion timing
- `references/lasc-local-rules.md` — key LASC local rules
  affecting civil motion practice, tentatives, and CMC

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
