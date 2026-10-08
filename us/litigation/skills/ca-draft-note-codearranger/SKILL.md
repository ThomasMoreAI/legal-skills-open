---
name: ca-draft-note-codearranger
title: Draft a California Notice of Motion
description: Use this skill when the user asks to draft or scaffold the California scheduling document that places a motion on the court's calendar. Triggers include "scaffold a Notice of Motion", "draft the notice of motion California", "16 court days notice", "CCP 1005 notice", "notice of motion and motion", "notice of motion and demurrer", "draft a motion notice California", "when does my opposition come due", "schedule my California motion". Drafts the Notice of Motion document that combines the scheduling notice with the initial motion header under CCP § 1010, computing service deadlines under CCP § 1005(b) and confirming opposition and reply due dates. Composes with `ca-statewide-format` (always) and the relevant court skill (`ca-lasc`, `ca-sfsc`, or `ca-county-courts`).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ca-court-docs/skills/ca-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a California Notice of Motion

Scaffold the Notice of Motion that opens a California motion
packet, calculates the service and response deadlines under
CCP § 1005(b), and confirms the hearing is properly reserved.

## What a Notice of Motion is in California

In California superior court practice, the **Notice of
Motion** is a **separate, standalone document** (not combined
with the Memorandum of Points and Authorities) that:

1. Places the hearing date, time, and department on the face
   of the filing
2. Identifies the relief sought and the legal grounds
3. States what supporting papers the court will consider
4. Establishes the CCP § 1005(b) service record

The Notice of Motion is typically the **first document** in
the packet, followed by the Memorandum, Declaration(s),
Request for Judicial Notice (if any), Proposed Order, and
Proof of Service.

> **Terminology note**: Washington State's analog is the
> "Note for Motion Docket"; Oregon's analog is the "Notice
> of Hearing". California uses "Notice of Motion" — and it
> doubles as both the scheduling notice and the formal motion
> assertion. The user may come in with either formulation; this
> skill produces the California-correct form.

## When required

A Notice of Motion is required whenever a party files a
motion that requires a hearing. Exceptions:

- **Ex parte applications** (CRC 3.1200–3.1207) do not use
  the standard 16-court-day notice; they use the ex parte
  short notice procedure
- **Motions on shortened time**: when the court grants an
  order shortening time under CRC 3.1300(b), the notice
  period is whatever the court specifies
- **Written oppositions waived**: some departments accept an
  oral motion at a Case Management Conference or hearing;
  this is dept.-specific practice

## Hearing reservation — do this first

Most California superior courts require a hearing date
**reserved before serving the Notice of Motion**. Serving
an unconfirmed date is a common pro se error that forces
a rescheduling.

| Court | Reservation method |
|---|---|
| Los Angeles Superior (LASC) | Court Reservation System (CRS) at lasuperiorcourt.org |
| San Francisco Superior (SFSC) | Civil Division scheduling, sfsuperiorcourt.org |
| Other superior courts | Check the court's local rules and department-specific standing orders |

After reserving, confirm: **date, time, department number,
and judge**. All four fields go in the Notice and the caption.

## CCP § 1005(b) — notice period and response deadlines

The minimum notice period is **16 court days** before the
hearing. Additional days are added depending on service
method:

| Service method | Add to 16 court days |
|---|---|
| Personal service | +0 |
| First-class mail (CA address) | +5 calendar days (CCP § 1013(a)) |
| First-class mail (out-of-state) | +10 calendar days (CCP § 1013(a)) |
| Electronic service (CCP § 1010.6(a)(3)(B)) | +2 court days |
| Overnight delivery (Cal.) | +2 calendar days (CCP § 1013(c)) |
| Overnight delivery (out-of-state) | +3 calendar days (CCP § 1013(c)) |
| Fax service | +2 court days (CCP § 1013(e)) |

**Response deadlines under CCP § 1005(b):**

- Opposition: **9 court days** before the hearing
- Reply: **5 court days** before the hearing

Use `ca-deadlines` to count court days precisely, excluding
weekends and California state holidays (Cal. Gov. Code
§ 6700 et seq.).

### Worked deadline example

Hearing date: Monday, June 30, 2025 (confirmed in Dept. 32)

If served by electronic service (+ 2 court days):

- Latest service date: 16 + 2 = 18 court days before June 30
  (count backwards, skipping weekends and holidays)
- Opposition due: 9 court days before June 30
- Reply due: 5 court days before June 30

Use `ca-deadlines` to get the exact calendar dates.

## What this skill produces

A Notice of Motion with:

1. **Caption** per CRC 2.111 (see `ca-statewide-format`)
2. **Document title**: "NOTICE OF MOTION AND MOTION FOR
   [RELIEF]"
3. **Introductory "PLEASE TAKE NOTICE" paragraph** — hearing
   details, relief sought
4. **Grounds paragraph** — legal basis with citations
5. **Supporting papers statement** — enumeration of all
   papers the court should consider
6. **Date and signature block**

## Template

```
[UPPER-LEFT: Party info / attorney info per CRC 2.111]

[UPPER-RIGHT: Case number; Hearing date, time, dept., judge]

          SUPERIOR COURT OF THE STATE OF CALIFORNIA
                    COUNTY OF LOS ANGELES

VELOCITY CAPITAL, LLC,               )
                                     )   Case No. 25STCV12345
          Plaintiff,                 )
                                     )   NOTICE OF MOTION AND
     v.                              )   MOTION TO COMPEL FURTHER
                                     )   RESPONSES TO REQUESTS FOR
JANE DOE,                            )   PRODUCTION, SET ONE, UNDER
                                     )   CCP § 2031.310; MEMORANDUM
          Defendant.                 )   OF POINTS AND AUTHORITIES
                                     )
                                     )   Hearing:
                                     )   Date:   [DATE]
                                     )   Time:   [TIME]
                                     )   Dept.:  [DEPT. NO.]
                                     )   Judge:  Hon. [NAME]
                                     )   Reservation No.: [No.]



TO PLAINTIFF VELOCITY CAPITAL, LLC AND ITS COUNSEL OF RECORD:

PLEASE TAKE NOTICE that on [DATE], at [TIME], in Department
[##] of the above-entitled court, located at [COURTHOUSE
ADDRESS, CITY, CA ZIP], Defendant Jane Doe will, and hereby
does, move for an order:

    (1) compelling Plaintiff to serve further verified
        responses to Defendant's Requests for Production, Set
        One, Nos. 3, 5, and 6, without objection; and

    (2) compelling Plaintiff to produce all documents
        responsive to those Requests within 10 days of the
        order; and

    (3) awarding Defendant monetary sanctions under CCP
        § 2023.030(a) in the amount of $[AMOUNT] against
        Plaintiff and its counsel of record.

This Motion is made pursuant to CCP § 2031.310 on the grounds
that Plaintiff's objections to Requests Nos. 3, 5, and 6 are
meritless, that Plaintiff's responses are incomplete, and
that Plaintiff's failure to comply was without substantial
justification within the meaning of CCP § 2023.030.

This Motion is based on:
    —   this Notice of Motion;
    —   the accompanying Memorandum of Points and Authorities;
    —   the Separate Statement of Items in Dispute required
        by CRC 3.1345;
    —   the Declaration of Jane Doe, with Exhibits A through
        C, filed herewith;
    —   the pleadings and papers on file in this action; and
    —   such oral argument as the Court may permit at the
        hearing.

DATED: _______________

                                    ____________________________
                                    JANE DOE
                                    Defendant, In Pro Per
                                    [Address]
                                    [Phone]
                                    [Email]
```

## Title line conventions

The title "NOTICE OF MOTION AND MOTION FOR [RELIEF]" is the
California standard. Some courts and some motion types have
specific title variations:

| Motion type | Standard title form |
|---|---|
| Demurrer | "NOTICE OF DEMURRER AND DEMURRER TO [TARGET PLEADING]" — no "MOTION" in the title; demurrers are treated as a distinct filing from motions in California practice |
| Motion to strike | "NOTICE OF MOTION AND MOTION TO STRIKE" |
| Summary judgment | "NOTICE OF MOTION AND MOTION FOR SUMMARY JUDGMENT [OR IN THE ALTERNATIVE, SUMMARY ADJUDICATION]" |
| Anti-SLAPP | "NOTICE OF MOTION AND SPECIAL MOTION TO STRIKE UNDER CCP § 425.16" |
| Motion to compel | "NOTICE OF MOTION AND MOTION TO COMPEL FURTHER RESPONSES TO [INTERROGATORIES / REQUESTS FOR PRODUCTION / REQUESTS FOR ADMISSIONS]" |
| Motion in limine | "MOTION IN LIMINE NO. [#] TO EXCLUDE [TOPIC]" — typically no separate "Notice" filed; notice is incorporated |

## Relief enumeration — be specific

The "PLEASE TAKE NOTICE" paragraph must state **specifically**
what the court is being asked to order. Vague formulations
("to compel discovery") are disfavored. Enumerate:

```
    (1) compelling Plaintiff to serve further verified
        responses to Requests Nos. 3, 5, and 6, without
        objections;
    (2) compelling Plaintiff to produce all documents
        responsive to Requests Nos. 3, 5, and 6 within
        10 days; and
    (3) awarding monetary sanctions of $[amount].
```

Specificity prevents the losing party from arguing that the
order is broader than what was noticed.

## Supporting papers statement

The final paragraph of the Notice enumerates every document
the court will consider. This serves as the "evidence relied
upon" in California practice — the equivalent of Oregon's
"Evidence Relied Upon" section in the motion body, but here
it appears in the Notice.

Enumerate:
- The Notice itself
- The Memorandum of Points and Authorities
- The Separate Statement (if required by CRC 3.1345)
- Each named declaration with exhibits
- Any Request for Judicial Notice
- Pleadings and papers on file
- "Such oral and documentary evidence as may be received at
  the hearing"

## Notice of Ruling (post-hearing)

After the hearing, the **prevailing party** prepares a Notice
of Ruling that confirms what the court ruled. This is a
separate document from the Proposed Order. Format:

```
NOTICE OF RULING ON DEFENDANT'S MOTION TO COMPEL

TO ALL PARTIES AND THEIR COUNSEL OF RECORD:

PLEASE TAKE NOTICE that on [DATE], the above-entitled court,
the Honorable [JUDGE], presiding in Department [##],
ruled as follows on Defendant's Motion to Compel:

    [One or two sentences accurately summarizing the court's
     ruling — e.g., "The Motion was GRANTED. Plaintiff is
     ordered to serve further responses and produce
     documents within 10 days. Sanctions of $[amount] were
     awarded against Plaintiff."]

The Court signed the proposed order on [DATE]. A copy of the
signed order is attached hereto.

DATED: _______________

                                    ____________________________
                                    JANE DOE
                                    Defendant, In Pro Per
```

Distinguish the Notice of Ruling from the formal Proposed
Order drafted under CRC 3.1312 — both are commonly used in
California practice, and the Notice of Ruling is the faster
notification mechanism.

## Ex parte applications — different procedure

If the motion is time-sensitive and the standard 16-court-day
timeline won't work, the party must apply for an **ex parte
order** (CRC 3.1200–3.1207):

- Give **24 hours' telephonic and written notice** to all
  parties (CRC 3.1204(b)) — unless notice would frustrate
  the purpose of the order
- File an **ex parte application** (not a motion) with a
  declaration of notice, statement of the relief requested,
  and supporting papers
- Appear in the ex parte department (check local rules)

This skill does not scaffold ex parte applications. See
`ca-hearings` or the court-specific skill for ex parte
procedures.

## Pro se notes

- Pro se litigants in California are described as acting "In
  Pro Per" (not "pro se" — California courts use the Latin
  "in propria persona" abbreviated "In Pro Per")
- The State Bar number is omitted on the signature block for
  In Pro Per filers
- Service by electronic means is available to pro se filers
  if they agree to accept electronic service per CCP
  § 1010.6(a)(1)

## Local variations

### Los Angeles Superior Court (LASC)

- Hearing reservation through the Court Reservation System
  (CRS): lasuperiorcourt.org
- Include the CRS reservation number in the caption or
  cover page
- Some departments require a **Notice of Hearing
  Reservation** e-mailed to the department before filing

### San Francisco Superior Court (SFSC)

- Scheduling through the Civil Division portal
- Complex Civil departments (Dept. 301, 302) have additional
  local rules; check the department's standing orders at
  sfsuperiorcourt.org

### Other counties

See `ca-county-courts` for county-specific scheduling
portals and hearing reservation procedures.

## Layered composition

This skill ALWAYS composes with:

- **`ca-statewide-format`** — caption, line numbers, format
- **The relevant court skill** — `ca-lasc`, `ca-sfsc`, or
  `ca-county-courts` — for hearing reservation method and
  department-specific caption details

It typically composes with:

- **`ca-draft-motion`** — the Memorandum follows the Notice
- **`ca-draft-declaration`** — the supporting declaration
  is listed in the Notice's supporting papers paragraph
- **`ca-draft-order`** — the Proposed Order is also listed

## Quality checks

Before serving and filing:

- **`ca-deadlines`** — verify the service date gives the
  required notice count under CCP § 1005(b)
- **`ca-fact-check`** — confirm hearing date, time, dept.,
  judge, and case number are correct
- **`ca-quality-check`** — CRC 2.100–2.119 format pass

A Notice served with the wrong date or wrong department
number is the most common pro se scheduling error and may
result in the motion being taken off-calendar.

## Cross-references

- `ca-statewide-format` — caption format + CRC 2.111
- `ca-deadlines` — CCP § 1005 court-day computation
- `ca-schedule-hearing` — hearing reservation workflow
- `ca-lasc` — LASC Court Reservation System
- `ca-sfsc` — SFSC Civil Division scheduling
- `ca-county-courts` — other counties

**NOT LEGAL ADVICE.** Generated content is a drafting aid;
verify against current rules and case law before filing.
