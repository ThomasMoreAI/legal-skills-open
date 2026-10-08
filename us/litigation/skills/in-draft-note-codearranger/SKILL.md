---
name: in-draft-note-codearranger
title: Draft an Indiana Notice of Hearing / Notice of Setting
description: 'This skill should be used when the user asks to "draft an Indiana Notice of Hearing", "Indiana Notice of Setting", "Indiana Notice of Trial", "Indiana Notice of Submission", "schedule a motion for hearing Indiana", "Notice of Setting Marion", "Indiana motion docket", "Indiana motion calendar note", "Indiana hearing notice template", or any related scheduling-document request. Scaffolds the Notice of Hearing / Notice of Setting that places a motion on the court''s calendar. Indiana does NOT use the Washington "Note for Motion Calendar" terminology — the analog here is a Notice of Hearing under T.R. 73(C), and in some Marion / Lake Civil Divisions the court itself issues the Notice of Setting rather than the party. Trigger phrases: "Indiana Notice of Hearing", "Indiana Notice of Setting", "Indiana T.R. 73(C)", "Indiana motion docket", "schedule motion Indiana", "Marion Notice of Hearing", "Lake Notice of Setting".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft an Indiana Notice of Hearing / Notice of Setting

In Indiana civil practice, the scheduling document that places a
motion before the court is called a **Notice of Hearing** or a
**Notice of Setting**. The terminology and procedure differ from
Washington's "Note for Motion Calendar" or California's "Notice
of Motion."

The Indiana practice in most counties:

1. The movant files the motion + memorandum + declaration +
   proposed order
2. **The court** (judicial assistant or bailiff) reviews the
   filing and issues a **Notice of Setting** designating the
   date, time, and location of the hearing
3. The Notice of Setting is served on all parties via Odyssey

In some counties (Hamilton, Allen, Vanderburgh), the movant must
request a setting; in Marion Civil Division, the court typically
sets non-evidentiary motions for ruling on the briefs without
oral argument unless argument is requested. The Notice of
Hearing scaffolded here is filed when the party requests a
specific hearing date OR when the court has not yet acted and
the party wants to expedite.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> always confirm hearing-setting protocol with the assigned
> courtroom's judicial assistant before filing.

## Two scheduling-document patterns

### Pattern 1: Notice of Hearing (party-issued)

Used when the party requests oral argument on a pending motion
and proposes a hearing date. T.R. 73(C):

> "If a hearing is requested, the request shall be in writing
> and shall set forth a brief statement of the nature of the
> hearing requested."

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

                  NOTICE OF HEARING ON
        DEFENDANT'S MOTION TO [RELIEF]

TO:  All Parties of Record

PLEASE TAKE NOTICE that Defendant's Motion to [RELIEF], filed
[date], is hereby set for oral argument before [JUDGE NAME] in
Courtroom [#] on [DATE] at [TIME].

Counsel and pro se parties are directed to:

   - Appear in person (or via the Court's Webex room at [URL])
   - Be prepared to argue the motion on the merits
   - Bring any exhibits not already on the record

Estimated hearing duration: [X minutes]


Date: _______________      _______________________________
                              [SIGNER NAME], [Pro Se / Atty. No.]
                              [Street Address]
                              [City, IN ZIP]
                              Telephone: (___) ___-____
                              Email: ________________________


                       CERTIFICATE OF SERVICE

I certify that on [DATE] a copy of the foregoing was served via
the Indiana E-Filing System on all counsel of record.

                              _______________________________
                              [SIGNER NAME]
```

### Pattern 2: Request for Setting (party-issued, court completes)

Used when the party files a motion and asks the court to set a
hearing date. The party leaves the date / time / courtroom
blanks for the court to fill in.

```
                     STATE OF INDIANA
                  IN THE [COURT NAME] COURT
              [COUNTY NAME] COUNTY, INDIANA

[PLAINTIFF NAME],                   )
                                    )
            Plaintiff,              )    Cause No. [###]
                                    )
        v.                          )
                                    )
[DEFENDANT NAME],                   )
                                    )
            Defendant.              )

      DEFENDANT'S REQUEST FOR HEARING SETTING ON
        MOTION TO [RELIEF]

Defendant respectfully requests the Court set Defendant's Motion
to [RELIEF], filed [date], for oral argument under Indiana
Trial Rule 73(C). Defendant proposes a hearing of [X minutes]
duration. The motion involves [brief description of issues] and
oral argument would assist the Court because [reason].

Available dates for Defendant: [list 3-5 dates]


Date: _______________      _______________________________
                              [SIGNER NAME], [Pro Se / Atty. No.]
```

## How the assigned courtroom routes the setting

In Marion Civil Division:

1. Motion filed via Odyssey
2. Judicial assistant docket-checks within 1-3 business days
3. JA emails parties with proposed date(s), or issues an Order
   Setting Hearing
4. Court enters the Order Setting Hearing; Odyssey serves all
   parties

In Lake County Civil Division 5 (Hammond):

1. Motion filed via Odyssey
2. JA may set the hearing automatically based on the case-
   management standing order
3. Notice of Setting issued by the court

In county Circuit Courts:

1. Motion filed via Odyssey
2. Parties typically call chambers or email the JA to discuss
   available dates
3. Setting order issued by the court

## Hearing types — what to specify

| Hearing type | Typical duration | Set for ... |
|--------------|------------------|-------------|
| Status conference | 10-20 min | Marion CMS conferences |
| Pretrial conference | 30-60 min | After discovery complete |
| Motion hearing (non-evidentiary) | 15-30 min | Oral argument on a T.R. 7 motion |
| Summary judgment hearing | 30-60 min | T.R. 56(C) hearing |
| Evidentiary hearing | 1-3 hours | Preliminary injunction, contempt, protective order |
| Bench trial | 1-3 days | Trial on the merits without jury |
| Jury trial | 2-7 days | Trial with jury |

Specify the expected duration in the Notice / Request — judges
allocate calendar slots by duration.

## Webex setting

If the assigned courtroom is on Webex, the Notice should include
the Webex URL and dial-in:

```
   This hearing will be conducted via Cisco Webex pursuant to
Indiana Administrative Rule 14. To appear:

   - URL: [Courtroom's Webex URL from the court website]
   - Dial-in: [Phone number]
   - Meeting ID: [###]
   - Password: [###]

Parties are reminded to:
   - Test camera + microphone 60 min before
   - Mute by default; unmute when called
   - Camera on, dressed appropriately
   - Indicate your appearance as "[Last], [First] — [role]"
```

## Composition

- `in-statewide-format` for T.R. 5(E) format + T.R. 10 caption
- `in-marion` / `in-lake` / `in-county-courts` for venue setting
  protocols
- `in-pro-se` for self-represented service
- `in-schedule-hearing` for the upstream setting workflow
- `in-hearings` for the actual hearing preparation
- `in-draft-motion` for the motion that the Notice schedules

## References

- `references/notice-of-hearing-template.md` — full scaffolded
  Notice of Hearing
- `references/request-for-setting-template.md` — Request for
  Setting
- `references/webex-notice-template.md` — Webex-specific Notice
  language

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
