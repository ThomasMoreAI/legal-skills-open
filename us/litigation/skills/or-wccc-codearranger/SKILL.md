---
name: or-wccc-codearranger
title: Washington County Circuit Court (Oregon)
description: 'Use this skill when drafting or filing documents in Washington County Circuit Court (Oregon — "WCCC"), Oregon''s second-largest trial court in Hillsboro. Triggers include "Washington County" (Oregon context), "WCCC", "Hillsboro Circuit Court", "Hillsboro courthouse", "Washington County SLR", "Washington County local rules", or any Oregon case in Washington County (25CV##### format). **Important**: "Washington County" in Oregon (Hillsboro seat) is distinct from the state of Washington — use `wa-court-docs` for Washington state courts. Covers Washington County SLR, civil motion scheduling via Civil Division, Hillsboro courthouse details, OJD File and Serve eFiling, and working-copy practice (15-page threshold). Layer on top of `or-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/or-court-docs/skills/or-wccc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Civil Motion Practice
  path: references/civil-motion-practice.md
- title: Hillsboro Courthouse
  path: references/hillsboro-courthouse.md
- title: Washington County Slr
  path: references/washington-county-slr.md
---

# Washington County Circuit Court (Oregon)

Use this skill in addition to `or-statewide-format` when the
case is in the **Washington County Circuit Court (Oregon)**. This
is Oregon's second-busiest circuit court (Multnomah is first;
Clackamas and Lane are usually close behind).

> **NOT LEGAL ADVICE.** These notes describe the venue's
> procedural mechanics as a drafting aid, not legal advice.
> Local rules and judge-specific practices change; verify with
> the clerk and the current SLR before relying on anything
> here.

> ⚠ **Naming caution**: "Washington County" in Oregon is the
> suburban Portland county whose seat is Hillsboro. It is
> distinct from the state of Washington. For courts in the state
> of Washington (King County, Pierce County, etc.), use the
> `wa-court-docs` plugin.

## Court location

Washington County Circuit Court sits at the **Washington County
Public Services Building / Courthouse** complex in Hillsboro:

- Street: 145 NE 2nd Avenue, Hillsboro OR 97124
- Civil Division phone: (503) 846-2950
- Court website: https://www.courts.oregon.gov/courts/washington/Pages/default.aspx

Civil and family-law courtrooms are in the main courthouse
building. Juvenile is in the Juvenile Services Center, 222 SW
1st Avenue. Probate and small claims are in the Civil Department
within the main courthouse.

## Caption — Washington County variant

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF WASHINGTON
```

Case numbers follow `YYCVNNNNN` for civil cases (e.g.,
`25CV12345`). Same statewide format as Multnomah; the venue is
identified by the "FOR THE COUNTY OF WASHINGTON" header line and
the assigned department.

## Civil motion scheduling — Civil Division contact

Unlike Multnomah's individual-calendar model, Washington County
uses a **lightly centralized** scheduling approach: motions are
heard on the assigned judge's calendar, but date reservations
flow through the **Civil Division** at the courthouse rather than
individual JAs. This is faster for routine motions but means
less individual-judge customization.

**Step 1 — Identify the assigned judge**

The assigned judge appears on the OJD Case Information page and
in File and Serve. New civil cases are assigned at filing.

**Step 2 — Contact the Civil Division to request a date**

Email or call the Civil Division to request a date on the
assigned judge's calendar:

- Phone: (503) 846-2950
- Email: WCCCCivilCT@ojd.state.or.us (or the current address
  posted on the website)

Specify:

- Case caption and number
- Assigned judge
- Motion type and estimated argument time
- Two or three proposed dates

**Step 3 — Civil Division confirms**

The Civil Division replies with the confirmed date, courtroom,
and mode. For some judges, the JA confirms separately; for
others, the Civil Division clerk has full authority.

**Step 4 — File the Notice of Hearing**

File the Notice of Hearing on File and Serve. Washington County
SLR 5.045 requires the Notice to be filed **simultaneously with
the motion** for non-arbitration cases (this is stricter than
Multnomah's 3-day window).

**Step 5 — Working copies**

Washington County SLR 5.100 requires working copies for motions
over 15 pages total. Deliver to the Civil Department clerk's
counter or to chambers (the Civil Division will route).

## Authoritative source — pull current judge roster

The Washington County Circuit Court website is the canonical
source for judges, courtrooms, and standing orders:

**https://www.courts.oregon.gov/courts/washington/Pages/default.aspx**

Judges rotate dockets every two years (January 1 cycle, typical).
Pull the current roster each session.

## Washington County SLR — Supplemental Local Rules

Key civil sections:

| SLR | Subject |
|-----|---------|
| 1.001 | Effective date and scope |
| 5.025 | Setting motions through the Civil Division |
| 5.045 | Notice of Hearing filed with motion |
| 5.046 | Meet-and-confer certification for discovery motions |
| 5.100 | Working copies (over 15 pages) |
| 5.101 | Submission of orders |
| 7.010 | Telephonic / WebEx hearings |
| 8.010 | Mandatory arbitration (ORS 36.400) |
| 12.010 | Pretrial conference |

Pull the current SLR PDF from
https://www.courts.oregon.gov/courts/washington/rules.

## Mandatory arbitration

Washington County implements ORS 36.400 mandatory arbitration
identically to Multnomah: cases between $10,000 and $50,000 go
to arbitration. The Arbitration Commissioner's office at the
courthouse handles assignments to the OJD arbitrator panel.

If your case is in arbitration:

- File motions in the arbitration proceeding, not before the
  circuit judge
- Title: "(IN ARBITRATION PROCEEDING UNDER ORS 36.400)"
- The arbitrator's decisions are appealable to the circuit
  judge via trial de novo under ORS 36.425

## eFiling and service

Washington County uses File and Serve like all OJD circuits.
Document codes and service mechanics are identical to Multnomah
(UTCR 21.100).

Self-represented parties not registered for eService must be
served by mail or hand delivery under ORCP 9 D — see `or-pro-se`.

## Filing fees

Same statewide schedule under ORS 21.135-21.170. Verify at
https://www.courts.oregon.gov/services/fees/Pages/default.aspx.

## Document set for a motion in Washington County

1. **Motion**
2. **Memorandum in Support**
3. **Supporting Declaration(s)** with exhibits
4. **Proposed Order** ("[PROPOSED]" in title)
5. **Notice of Hearing** — filed simultaneously with the motion
   under WCCC SLR 5.045
6. **Certificate of Service**
7. **Working copies** if total packet exceeds 15 pages

## Scheduling email — recommended template

```
To:      WCCCCivilCT@ojd.state.or.us
Subject: Hearing Date Request — [Case Short Title],
         Case No. [Cause Number]

Civil Division:

I am [Counsel of record / Defendant, pro se] in [case short
title], Case No. [cause number], assigned to the Hon. [Judge
Name].

I am requesting a hearing date for [Motion Title], to be filed
[date]. Estimated argument time: [X minutes].

Proposed dates:
   [Date 1]
   [Date 2]
   [Date 3]

I have / have not conferred with opposing counsel on these
dates.

If the Court prefers WebEx, please advise so I can include the
connection details on the Notice of Hearing.

Thank you,
[Name][, pro se / OSB #]
[Contact info]
```

## Comparison to Multnomah

| Aspect | Multnomah | Washington Co |
|--------|-----------|---------------|
| Scheduling | Through assigned judge's JA | Through Civil Division |
| Working-copy threshold | 25 pages | 15 pages |
| Notice of Hearing timing | Within 3 business days of JA confirm | Filed simultaneously with motion |
| Meet-and-confer requirement | SLR 5.045 | SLR 5.046 |
| Default hearing mode | WebEx for routine motions | Mix — judge-dependent |
| Ex parte hours | M–F 8:30–12:00 in dedicated dept | Civil Division counter, mornings |

## References

- `references/hillsboro-courthouse.md` — venue info, courtrooms,
  judges, working-copy delivery
- `references/civil-motion-practice.md` — full motion practice
  walkthrough
- `references/washington-county-slr.md` — local rules summary
