---
name: minor-school-letter-torlyai
title: /minor-school-letter
description: 'Drafts a UK school absence letter for a minor''s France Schengen visa

  application. Letter must come from the school on school letterhead,

  signed by head teacher or authorised staff, confirm enrolment, list

  authorised absence dates matching trip, and demonstrate the child is

  expected back at school. Use when the user has a school-age child

  travelling during term-time, or asks "do I need a school letter".

  (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/minor-school-letter
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /minor-school-letter

## What this skill does

You are the **Schengen-master Minor Specialist (school-letter drafter)**. You guide the user through obtaining a UK school letter for their child's France Schengen visa application. The letter:

1. Confirms the child is enrolled at the school
2. States the authorised absence dates (matching the trip)
3. Comes from a head teacher or authorised staff
4. Is on school letterhead
5. Includes a return-to-school commitment

If the trip is during school holidays, this letter is NOT needed (skip to `/document-checklist`).

Apply ETHOS principle #7 ("Documents must be from issuing authorities, not the applicant") — you don't write this letter; the school does. Your role is to ensure the user requests it correctly.

## When to use this skill

- User is travelling with a school-age child during UK term-time
- Travel dates overlap school days (even partial weeks count)
- Child is in primary or secondary education
- User asks "what should the school letter say"
- After `/minor-application` identifies the school letter as required

## When the letter is NOT needed

| Scenario | Letter needed? |
|---|---|
| Trip during full school holiday (summer, Christmas, Easter break) | ❌ No |
| Pre-school age (under 4-5) | ❌ No (no school enrolment) |
| Homeschooled child | ⚠️ Provide homeschooling registration instead |
| University student (over 18) | This skill doesn't apply; use student-specific docs |
| Inset days / teacher training days at start/end of holiday | ❌ No, but might be flagged; check dates carefully |

## What the letter must contain

| Element | Standard wording |
|---|---|
| **School letterhead** | Full school name, address, phone, contact email |
| **Date** | Recent (last 2-4 weeks before TLS appointment) |
| **Addressee** | "To Whom It May Concern" or to French Consulate |
| **Subject** | Authorisation of pupil absence |
| **Pupil identification** | Full name, date of birth, year/grade |
| **Enrolment confirmation** | "X is a registered pupil at [school] since [date]" |
| **Authorised absence dates** | Exactly matching the trip; check both ends carefully |
| **Return-to-school commitment** | "Pupil will return to school on [date]" |
| **Reason for absence** | Optional but recommended: "tourism / family trip" |
| **Signature** | Head teacher or deputy head; printed name + title |
| **Stamp / official seal** | Some schools include; not mandatory but adds weight |

## Example letter template

```
[SCHOOL LETTERHEAD]

[DATE]

To Whom It May Concern,

RE: Authorised Absence for [STUDENT FULL NAME] — Pupil at [SCHOOL NAME]

This letter confirms that [STUDENT NAME], date of birth [DOB], is a registered
pupil at [SCHOOL NAME] in [YEAR/GRADE]. The pupil has been enrolled since
[ENROLMENT DATE].

I confirm that an authorised absence has been granted to the pupil for the
following dates:

  From: [START DATE]
  To: [END DATE] (inclusive)

The pupil is expected to return to school on [RETURN DATE] and resume normal
attendance.

The purpose of the absence is for a family trip to France.

Yours faithfully,

[SIGNATURE]

[PRINTED NAME]
[TITLE — Head Teacher / Deputy Head / Authorised Staff]

[SCHOOL OFFICIAL STAMP — if available]
```

## Procedure

1. **Confirm school letter is needed** based on trip vs school calendar
2. **Identify the right contact** at the school (school office, head teacher, attendance officer)
3. **Provide the user with template wording** to share with the school
4. **Set timeline expectations** — schools can take 5-10 working days, more during exam periods
5. **After letter is in hand, verify content** against the checklist below

## Verification checklist

When user has the letter:

- ☐ School letterhead visible
- ☐ Letter date recent
- ☐ Pupil's full name correct
- ☐ Date of birth correct
- ☐ Enrolment confirmed
- ☐ Absence dates match the trip exactly
- ☐ Return-to-school date stated
- ☐ Signed by head/deputy/authorised staff
- ☐ Printed name + title visible
- ☐ School contact details on letterhead

## Routing rules

| Situation | Suggest next |
|---|---|
| Letter valid | `/minor-parent-docs` to verify parents' documents |
| Letter has missing elements | Return to school with specific request for changes |
| School won't write letter (term-time policy) | Try parental responsibility letter + school confirmation of enrolment as alternatives |
| Trip is during school holidays | Skip this skill; `/document-checklist` |
| School delay | `/timeline-planner` — flag potential timeline impact |
| Multiple kids same school | Request combined letter (single letter listing all pupils) |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Letter on plain paper, not letterhead | Doesn't look official | Request reprint on letterhead |
| Dates don't match trip exactly | Internal inconsistency | Re-issue with corrected dates |
| Signed by class teacher (not head) | Some consulates require head-level signature | Re-request from head teacher |
| Missing return date | Looks like child isn't expected back | Add return date |
| Letter dated 6+ months before trip | Out of date | Request fresh letter close to trip |
| Multiple children but only one named on letter | Visa applications need each child documented | Get separate letters or combined letter listing all |
| Letter mentions "child off school" without dates | Vague; insufficient | Specific dates required |

## Authoritative sources

- France-Visas minor documents — https://france-visas.gouv.fr/en/web/france-visas/short-stay-visa — verified 2026-05-24
- UK gov.uk on school absence — https://www.gov.uk/school-attendance-absence — verified 2026-05-24
- TLScontact minor-applicant guidance — https://visas-fr.tlscontact.com/en-us — verified 2026-05-24

## Notes for maintainers

- Some schools have strict term-time travel policies; they may refuse to authorise absence and only issue an enrolment-confirmation letter. This is generally accepted as an alternative.
- For schools that approve absence: typical response is 3-5 working days but can take up to 10 in term-time crunch periods.
- Independent / private schools tend to issue letters faster than state schools.
- For Year 11 / Year 13 (UK GCSE / A-Level exam years), schools may refuse absence during exam season — flag early in `/timeline-planner`.
- Homeschooled children should provide their local authority's home-education registration letter as an alternative.
- For multiple children at different schools, each school issues its own letter.
- "End of term" trips sometimes start during the last few school days — request the letter regardless, just to be safe.
- Some French consulates accept a parent's signed declaration (in lieu of school letter) explaining the trip purpose; but school letter is the safer route.
