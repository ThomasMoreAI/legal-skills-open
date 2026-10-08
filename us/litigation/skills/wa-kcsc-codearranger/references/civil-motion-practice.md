# Civil Motion Practice — KCSC

KCSC's civil motion practice is governed by **King County LCR 7** read
with **CR 6** time computation (and RCW 1.16.050 holidays). Unlike KCDC,
KCSC has **no central scheduling email** (`KCDC.CivilMGT` is a KCDC
artifact — it does **not** apply here). Most contested motions are
**self-noted** to the **assigned judge's department**, subject to that
department's posted procedures; agreed and certain procedural matters go
through **Ex Parte**.

## Noting a motion (4-step protocol)

1. **Identify where the motion is heard.**

   - **Case has an assigned judge**: note the motion on that
     department's civil motion calendar, following the department's
     posted procedures. The department page (linked from
     `https://kingcounty.gov/en/court/superior-court`) will say whether
     the department uses self-noting, requires a scheduling-clerk
     touchpoint, has page limits beyond LCR 10, etc.
   - **Cross-departmental / pre-assignment**: certain matters go to
     **Chief Civil**.
   - **Agreed orders, defaults, supplemental-proceeding orders, many
     procedural orders**: present through **Ex Parte via the Clerk** (or
     in person at the Ex Parte and Probate Department).
   - **RALJ appeals from KCDC**: follow the King County LCR's RALJ
     provisions and the RALJ rules.

2. **Compute the LCR 7 / CR 6 notice period.**

   Read the **current** LCR 7 before noting. As a general orientation —
   confirm the exact text:

   - **Noted civil motion (served in person)**: commonly at least
     **9 court days** before the hearing.
   - **Opposition / response**: due a set number of court days before
     the hearing per LCR 7.
   - **Reply**: due by the LCR 7 deadline (often noon a fixed number of
     court days before the hearing).
   - **Service method adjustment**: LCR 7 / CR 5 adjust periods for
     non-personal service.

   Apply **RCW 1.16.050** holidays. Use the `wa-deadlines` skill and
   `plugins/wa-court-docs/scripts/case-calendar.py` — never eyeball it.
   LCR 7 has been amended; do not rely on memorized numbers.

3. **Confirm the motion.**

   The moving party generally must **confirm** the motion by the LCR 7
   deadline (and state whether **oral argument** is requested). The
   department's posted procedure says how (typically an online
   confirmation page tied to the department).

   **An unconfirmed motion is struck.** This is the single most common
   way a contested motion drops off the calendar in KCSC; calendar the
   confirmation deadline the moment you note the motion.

4. **Deliver working copies and e-file the packet.**

   - **Working copies** to chambers by the LCR 7 deadline through the
     Clerk's **Submit Working Copies** tool (or as the department
     directs), with the working-copy coversheet — see
     `filing-procedures.md`.
   - **E-file** the Note, Motion, Memorandum (if any), Declaration(s)
     with exhibits, and Proposed Order through the Superior Court
     Clerk's **E-Filing application** (linked from the DJA filing page).
   - **Serve** under CR 5 the same day; attach a Certificate /
     Declaration of Service.

> ⚠ **Two ways KCSC motions silently die:** (a) the cause number on the
> packet omits the LCR 82 case-assignment-area code, so the Clerk
> rejects the filing; or (b) the moving party doesn't confirm the
> motion by the LCR 7 deadline, so the department strikes it. Calendar
> both at noting.

## Case Schedule — LCR 4

For most civil case types, the Clerk issues an **Order Setting Civil
Case Schedule** at filing, fixing deadlines keyed to the filing date:

- **Confirmation of joinder of parties, claims, and defenses**
- **Disclosure of possible primary witnesses** / **additional witnesses**
- **Discovery cutoff**
- **Deadline for dispositive (typically summary-judgment) motions**
- **Status conference** (some case types)
- **Pretrial / mediation / settlement-conference deadlines**
- **Trial date**

Some case types are exempt from the standard schedule (check the
case-type list in the current **LCR 4**). Missing a Case Schedule
deadline can result in sanctions or **exclusion of witnesses/evidence**.
Treat the Case Schedule as binding alongside CR 6 time computation; use
`wa-deadlines` to compute every date.

## Working copies are required (LCR 7)

KCSC **requires** working copies — a courtesy/bench copy of the motion
materials delivered to the assigned judge's department (or to Ex Parte)
by the LCR 7 deadline. This is the key procedural difference from KCDC
(where working copies are generally not required).

Mechanics — confirm the current LCR 7 and the Clerk's "working copies"
instructions:

- **Delivery channel**: the Clerk's electronic **Submit Working Copies**
  tool (linked from the DJA filing page). Many departments accept this;
  some accept or prefer **paper** working copies — check the department's
  posted procedure.
- **Deadline**: due a set number of court days before the hearing
  (per LCR 7) — typically tied to the motion or response/reply timing.
- **Coversheet**: each set carries the **working-copy designation /
  coversheet** identifying the judge/department, the hearing date, and
  the moving party.
- **Contents**: the motion, memorandum, declarations, exhibits, and
  proposed order — everything the judge needs to rule.
- **Working copies are NOT filed** in the Clerk's record; they are
  delivered to chambers separately from the e-filed documents.

## Note for Civil Motion Calendar — required content

KCSC uses a King County Note for Civil Motion Calendar form. Pull the
current version from the DJA forms page; required content:

- Court and case caption (with the LCR 82 area code, `SEA` or `KNT`)
- Department assignment (judge name, department number, facility)
- Motion being noted (exact title)
- Hearing date and time (chosen to satisfy LCR 7 / CR 6 notice)
- Whether **oral argument** is requested
- Time estimate
- Movant's signature, address, email
- Certificate of Service (included or separate)

A template skeleton lives in the SKILL.md ("Note for Civil Motion
Calendar — recommended template").

## Confirmations, continuances, and strikes

- **Confirmations**: **required** for contested civil motions under
  LCR 7. Confirm by the LCR 7 / department deadline. Unconfirmed motions
  are struck. (This differs from KCDC, which does not use a pre-hearing
  confirmation.)
- **Continuances**: by agreement, submit an **Agreed Order to Continue**
  via the Ex Parte process before the hearing. Contested continuances go
  as a **noted motion** to the assigned department.
- **Strikes**: notify the assigned department and serve the other
  parties promptly; follow the department's posted strike procedure.
