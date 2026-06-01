---
name: in-schedule-hearing
title: Reserve a Hearing Date — Indiana
description: 'This skill should be used when the user asks to "reserve a hearing date Indiana", "Marion JA email", "schedule a motion hearing Indiana", "request a hearing date Marion Superior", "Lake civil hearing schedule", "Indiana judicial assistant contact", "Hamilton County hearing setting", "Indiana motion setting", or any related hearing-scheduling request. Drafts the contact email or scheduling form to the courtroom''s judicial assistant or bailiff to request a hearing date, consistent with the venue court''s setting protocol. Marion Civil Division typically issues a Notice of Setting on its own initiative; other counties require the party to request and propose dates. Trigger phrases: "Indiana JA email", "Marion hearing setting", "Lake hearing date request", "Indiana courtroom secretary contact", "schedule Marion motion hearing".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-schedule-hearing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Reserve a Hearing Date — Indiana

This skill drafts the request to the courtroom's judicial
assistant (JA) or bailiff to schedule a hearing on a pending
motion. In Indiana, hearing-setting practice varies by county:

- **Marion Civil Division**: Court typically sets non-evidentiary
  motions for ruling on the briefs without oral argument; if
  argument is requested, JA proposes dates.
- **Lake Civil Division 5 (Hammond)**: JA sets routinely based
  on the courtroom's standing calendar.
- **Hamilton, Allen, Vanderburgh**: party requests the setting
  by contact email; JA coordinates.
- **Most county Circuit Courts**: party calls or emails chambers
  to discuss available dates; setting order issued by court.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> always confirm hearing-setting protocol with the assigned
> courtroom's JA before filing a Notice of Hearing.

## Step 1 — Identify the assigned courtroom

The cause number identifies the assigned courtroom:

`49D01-2503-PL-001234` → Marion Superior Court, Civil Division 1

Look up the courtroom on the court's website (Marion:
`indy.gov/agency/marion-superior-court`; Lake:
`lakecountyin.gov/superior-court`). The page lists:

- Judge's name
- Judicial assistant's name + email
- Courtroom number + location
- Chambers practice page (if any)
- Webex URL (if used)

## Step 2 — Draft the scheduling contact

### Marion Civil Division — JA email template

```
To: [JA email — typically firstname.lastname@indy.gov]
From: [Pro se filer email]
Subject: [Cause No.] — Request for Hearing Setting on [Motion]

Dear [Judicial Assistant Name],

I am [Party Name], the [Defendant / Plaintiff], appearing pro
se in [Cause No.]. I write to request a hearing setting on
[Defendant's / Plaintiff's] Motion to [RELIEF], filed [date]
via Odyssey.

The motion is fully briefed (response filed [date]; reply
filed [date]). I respectfully request oral argument under
Trial Rule 73(C) because [reason — e.g., "the motion involves
factual disputes about service of process under Trial Rule
4.1"].

Estimated hearing duration: [X minutes].

Available dates for me:
   - [Date 1]
   - [Date 2]
   - [Date 3]

Please advise whether [Court / Hon. JUDGE NAME] will set this
matter for hearing, and if so, on which date.

Thank you,
[Party Name], Pro Se
[Address]
[Phone]
[Email]
```

### Lake Civil Division 5 — JA email template

```
To: [Lake JA email — typically last.first@lakecountyin.gov]
Subject: [Cause No.] — Hearing Request

Dear [Judicial Assistant Name],

I am [Party Name], pro se [Defendant / Plaintiff] in [Cause
No.]. I am writing to request a hearing setting on the
following motion:

   Motion to [RELIEF], filed via Odyssey on [date]

The motion has been fully briefed. I am available on the
following dates:

   - [Date 1]
   - [Date 2]
   - [Date 3]

Please confirm the hearing setting at the Court's earliest
convenience.

Sincerely,
[Party Name], Pro Se
[Contact info]
```

### County Circuit Court — Phone call protocol

For smaller counties (Crawford, Switzerland, Ohio), the assigned
judge's office typically prefers a phone call:

```
Caller script:

"Good morning, this is [Party Name] calling about Cause No.
[#####] in the [County] Circuit Court. I'm the [Defendant /
Plaintiff] appearing pro se, and I'd like to discuss
scheduling a hearing on my Motion to [RELIEF], filed last
week.

Could you tell me what dates the Court has available for a
[X-minute] hearing?

[Wait for response. Note dates on calendar.]

Yes, [date] works for me. Will the Court issue a Notice of
Setting, or should I file a Notice of Hearing myself?

[Note the answer.]

Thank you very much."
```

After the call, document the call in your case file:

```
Phone log:
   Date: [date]
   Time: [time]
   With: [JA name] at [chambers number]
   Subject: hearing setting on Motion to [RELIEF]
   Outcome: hearing set for [date] at [time]; court will issue
            Notice of Setting; will appear via Webex at [URL]
```

## Step 3 — Wait for the Notice of Setting

Once the JA issues the Notice of Setting (typically 1-3 business
days):

- The Notice appears in Odyssey as an entered document
- Email notification is sent to all Service Contacts
- Calendar the hearing date immediately
- Calendar reminder dates (1 week before, day before)

If the JA does NOT issue a Notice of Setting within a reasonable
time (typically 5-10 business days), file a Notice of Hearing
yourself proposing the agreed date (see `in-draft-note`).

## Hearing-type duration estimates

When requesting a setting, give the JA an accurate duration
estimate:

| Hearing type | Typical estimate |
|--------------|------------------|
| Status conference | 10-15 min |
| Pretrial conference | 30-45 min |
| T.R. 12(B)(6) motion to dismiss | 20-30 min |
| T.R. 56 summary judgment | 45-60 min |
| T.R. 60(B) motion to vacate | 30-45 min |
| Preliminary injunction (evidentiary) | 2-4 hours |
| Contempt hearing (evidentiary) | 1-2 hours |
| Discovery motion (T.R. 37) | 15-30 min |
| Motion to compel arbitration | 30 min |
| Bench trial | 1-3 days |

Overestimate slightly — JAs prefer to allocate too much time
than too little. If the hearing concludes early, the court
recovers the unused time for the next case.

## Webex setting considerations

If the courtroom uses Webex (Marion CD-3, Lake CD-5, most
populous-county civil courts use it for routine motions):

- The Notice of Setting will include the Webex URL
- Test camera + mic 60 min before
- Have a backup phone-dial-in number ready
- Be prepared to display documents via screen-share if needed

For evidentiary hearings, most Marion / Lake civil judges
prefer in-person; party can move for in-person setting on a
showing of need.

## Continuance vs. resetting

If the assigned hearing date doesn't work, file a Motion to
Continue under T.R. 53.5 at least 7 days before the hearing.
Continuances must be by written motion in Marion (LR49-TR53.5)
and most populous-county venues. The motion should:

- State current setting
- Identify the reason for continuance
- Propose new dates
- Indicate whether opposing party agrees

## Composition

- `in-statewide-format` for the format of any Notice / Motion
  to Continue
- `in-marion` / `in-lake` / `in-county-courts` for venue setting
  protocol
- `in-pro-se` for self-represented contact conventions
- `in-draft-note` for the Notice of Hearing scaffolder
- `in-hearings` for hearing preparation once set

## References

- `references/ja-email-templates.md` — per-county JA contact
  templates
- `references/chambers-phone-script.md` — phone-call scripts for
  smaller counties
- `references/continuance-motion-template.md` — T.R. 53.5
  motion to continue
- `references/duration-estimates.md` — hearing-type duration
  guide

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
