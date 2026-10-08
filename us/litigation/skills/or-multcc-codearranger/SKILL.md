---
name: or-multcc-codearranger
title: Multnomah County Circuit Court
description: This skill should be used when drafting or filing documents in the Multnomah County Circuit Court (the "Multco Circuit Court" or "MCCC"), Oregon's largest trial court, sitting in Portland. Triggers include "Multnomah", "Multco", "MCCC", "Multnomah County Circuit Court", "Portland Circuit Court", "Multnomah SLR", "Multnomah local rules", "civil motion in Portland", "Central Courthouse Portland", "Donald E. Long Juvenile Justice Complex", "Multnomah civil department", or any case with a Multnomah cause number (`25CV#####` filed in Multnomah). Covers Multnomah Supplemental Local Rules (SLR), civil motion scheduling through the assigned judge's judicial assistant, the Central Courthouse / Justice Center / Juvenile JC venues, eFiling through OJD File and Serve, and the working-copy practice for motions submitted to a specific judge. Layer on top of `or-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-multcc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Central Courthouse
  path: references/central-courthouse.md
- title: Civil Motion Scheduling
  path: references/civil-motion-scheduling.md
- title: Multnomah Slr
  path: references/multnomah-slr.md
---

# Multnomah County Circuit Court

Use this skill in addition to `or-statewide-format` when the case
is in the Multnomah County Circuit Court (MCCC). Multnomah is the
largest trial court in Oregon (~25–30% of all civil filings
statewide) and has the most developed local-rule and motion-
practice ecosystem.

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice.
> Local rules and judge-specific practices change; verify with
> the clerk and the current SLR before relying on anything
> here.

## Court locations and divisions

Multnomah Circuit Court has three principal facilities:

- **Central Courthouse** (the new flagship), 1200 SW 1st Ave,
  Portland OR 97204 — civil, criminal felony, family law,
  probate, mandatory arbitration. Opened 2020, replaced the old
  Multnomah County Courthouse.
- **Justice Center**, 1120 SW 3rd Ave, Portland OR 97204 —
  criminal misdemeanor, in-custody criminal arraignments,
  violations
- **Donald E. Long Juvenile Justice Complex** (the "JJC"),
  1401 NE 68th Ave, Portland OR 97213 — juvenile delinquency and
  juvenile dependency

For civil pleadings, the venue is the **Central Courthouse**. The
caption identifies "FOR THE COUNTY OF MULTNOMAH" — there is no
sub-division reference in the caption (unlike KCDC's
East/South/West divisions in Washington).

## Caption — Multnomah variant

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH
```

Case numbers follow `YYCVNNNNN` for civil cases (e.g.,
`25CV12345`). The first two digits are the year; "CV" is the case
type (civil); the remaining digits are the sequential filing
number for the year.

## Civil motion scheduling — chambers contact, not a calendar clerk

Multnomah does **not** use a centralized motions docket. Each
civil case is assigned to a specific judge at filing (via the
Multnomah civil case-assignment system). Motions are heard on
**that judge's individual calendar**. To set a motion:

**Step 1 — Identify the assigned judge**

The assigned judge appears on the OJD Case Information screen for
the case (visible to the parties and in File and Serve once the
case is filed). For a newly filed case where assignment has not
yet posted, check with Civil Division at (503) 988-3022.

**Step 2 — Contact the judge's judicial assistant (JA)**

Email or call the assigned judge's JA to request a hearing date.
The JA roster is published on the Multnomah Circuit Court website
(courts.oregon.gov/multnomah, "Judges and Staff"):

- Pull the current JA name and email from
  https://www.courts.oregon.gov/courts/multnomah/judges/Pages/default.aspx
  before each request — assignments rotate

In the email, identify:

- Case caption and number
- Motion type (e.g., "Motion to Compel under ORCP 46")
- Estimated argument time
- Whether other parties have been consulted on dates
- Two or three proposed dates that work for the moving party

**Step 3 — JA confirms the date**

The JA will reply confirming the date, courtroom, and mode
(in-person, WebEx, or telephone). Some judges hold all civil
motions on WebEx by default; others prefer in-person. Take what
the JA offers.

**Step 4 — File the Notice of Hearing**

After the JA confirms, file a **Notice of Hearing** through File
and Serve, identifying the date, courtroom, mode, and assigned
judge. The Notice of Hearing is what gives the *record* notice
of the setting (the JA's email is internal scheduling, not part
of the court record).

**Step 5 — Working copies to chambers**

For motions over 5 pages (memorandum + exhibits combined), or for
motions where the judge has specifically requested it, deliver
**working copies** to chambers:

- Multnomah SLR 5.100 governs working copies
- Deliver to the judge's courtroom or chambers via the Central
  Courthouse mail room
- The working copy is a tabbed, bound paper copy of the entire
  packet — motion, memorandum, declaration, exhibits, proposed
  order
- For pro se filers, mailing the working copy to the courtroom
  (addressed to the judicial assistant) is acceptable
- Some judges accept email-only working copies for short motions;
  always confirm with the JA when you request the date

## Authoritative source — pull the current judge roster every time

The Multnomah Circuit Court website is the canonical source for
judges, judicial assistants, courtrooms, and standing orders:

**https://www.courts.oregon.gov/courts/multnomah/Pages/default.aspx**

**Agent behavior**: when drafting a Notice of Hearing or working-
copy cover note, fetch the current JA contact info from that
page. Judge rotations occur in January each year (and sometimes
mid-year); do not cache assignments across sessions.

## Multnomah SLR — Supplemental Local Rules

Multnomah's SLR adds detail on top of the statewide UTCR. Key
sections for civil motion practice:

| SLR | Subject |
|-----|---------|
| 1.001 | Effective date and scope |
| 5.015 | Notice of Hearing on Motion |
| 5.025 | Setting motions (chambers-based, by JA) |
| 5.045 | Meet-and-confer certification for discovery motions |
| 5.100 | Working copies — when, how, and where |
| 5.101 | Submission of orders to chambers |
| 7.010 | Telephonic and remote hearings |
| 8.010 | Mandatory arbitration program (under ORS 36.400) |
| 12.010 | Pretrial conferences and trial readiness |
| 14.010 | Mediation referrals |

The current Multnomah SLR PDF lives at
https://www.courts.oregon.gov/courts/multnomah/rules — pull it
when a specific SLR section is invoked, because Multnomah updates
its SLRs more frequently than other counties.

## Mandatory arbitration

ORS 36.400 et seq. requires arbitration for civil cases where
the amount in controversy is between $10,000 and $50,000 (the
ceiling is set by ORS 36.405 and is currently $50,000 statewide;
Multnomah elects the statutory ceiling). Multnomah SLR 8.010
implements this.

If the case is in arbitration:

- Discovery is limited (see arbitration program rules)
- Motions go to the arbitrator, not the judge — caption the
  motion accordingly: "MOTION TO COMPEL... (IN ARBITRATION
  PROCEEDING UNDER ORS 36.400)"
- A trial de novo can be requested after the arbitration award
  per ORS 36.425, but only after fees are paid

## eFiling and service

Multnomah requires eFiling for all civil matters through File and
Serve (https://oregon.tylertech.cloud). Document codes are
specific:

- Motion → "Motion (Other)" or "Motion to [Type]" if listed
- Memorandum → "Memorandum in Support of Motion"
- Declaration → "Declaration of [Name]"
- Notice of Hearing → "Notice of Hearing"
- Proposed Order → "Order — Proposed"

Service through eService (File and Serve) counts as service for
registered parties (UTCR 21.100, ORCP 9 G(1)(d)). Self-
represented parties not registered must be served by mail or hand
delivery — see `or-pro-se` for the protocol.

## Filing fees

Multnomah civil filing fees track the OJD statewide schedule
under ORS 21.135-21.170:

- Complaint or counterclaim over $10,000: $281 (subject to
  legislative update — pull current fee from
  https://www.courts.oregon.gov/services/fees/Pages/default.aspx)
- Motion: $11 per side per motion (some motion types are free —
  see ORS 21.260)
- Fee waiver: ORS 21.682 (filing-fee deferral); ORS 20.140 (in
  forma pauperis status)

Fee-waiver applications are filed simultaneously with the
underlying pleading on File and Serve; the fee is deferred
pending the court's order on the application.

## Document set for a noted motion in Multnomah

1. **Motion** (primary relief sought)
2. **Memorandum in Support** (if argument is more than 1 page)
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order** ("[PROPOSED]" bracket in title)
5. **Notice of Hearing** (filed separately after JA confirms
   date)
6. **Certificate of Service** (separately or as a page in each
   document)
7. **Working copies to chambers** (for motions over 5 pages or
   where the judge requests)

eFile each as a separate PDF through File and Serve. Working
copies are delivered separately (paper or email per the JA's
preference).

## Scheduling email — recommended template

```
To:      [Assigned Judge's JA email]
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Dear [Judicial Assistant Name]:

I am [Counsel of record / Defendant, pro se] in [case short
title], Case No. [cause number], assigned to the Hon. [Judge
Name].

I am requesting to reserve a date for hearing on Defendant's
[motion title], filed (or to be filed) on [date]. I estimate
[20 minutes / 30 minutes] of argument.

I propose the following dates:
   [Option 1]
   [Option 2]
   [Option 3]

I have [contacted / not yet contacted] opposing counsel about
these dates. [If contacted: opposing counsel [agrees / objects
to / has not responded re] dates as follows: ...]

If WebEx is the preferred mode for the Court, please advise so
I can include the connection details on the Notice of Hearing.

Thank you,
[Name][, pro se designation if applicable] [, OSB # ___ if
counsel]
[Address]
[Phone]
[Email]
```

## References

- `references/central-courthouse.md` — Central Courthouse venue
  info, courtrooms, judges, mail-room directions
- `references/civil-motion-scheduling.md` — JA contact protocol,
  working copies, courtesy copies
- `references/multnomah-slr.md` — local rules summary, frequent
  references
