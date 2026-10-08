---
name: co-draft-note-codearranger
title: Draft a Colorado Notice
description: 'This skill should be used to scaffold a Colorado scheduling document — typically a Notice of Setting (issued by the court), Notice of Hearing (when permitted by local rule), or a related scheduling notice placed on the court''s calendar. Triggers include "draft a Colorado notice of hearing", "Colorado notice of setting", "draft a notice to appear", "scheduling document Colorado", "Colorado calendar notice". Note that in Colorado the court itself typically issues a Notice of Setting after the parties brief a motion; the parties do not self-schedule the way Washington''s "Note for Motion Docket" works. This skill therefore drafts the variants the parties actually file: Notice of Hearing (court-set hearing echoed to the parties), Notice of Withdrawal, Notice of Filing, Notice of Substitution of Counsel, and similar party-filed notices.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-draft-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a Colorado Notice

> **NOT LEGAL ADVICE.** This skill scaffolds a notice document.
> Verify the assigned judge's practice standards and the C.R.C.P.
> rules controlling the specific notice type before filing.

In Colorado civil practice, the **court** typically issues a Notice
of Setting after a motion is fully briefed; the **parties** do not
self-schedule the way they do in some other states (contrast
Washington's Note for Motion Docket). However, several party-filed
notices are common in Colorado practice — this skill covers the
typical formats.

## Notice types in Colorado civil practice

| Notice | Filer | Purpose | Authority |
|--------|-------|---------|-----------|
| Notice of Setting | Court | Court announces it has set a hearing on a previously filed motion | C.R.C.P. 121 § 1-15(4) |
| Notice of Hearing | Filer (when self-scheduling permitted, esp. county court / certain post-judgment) | Notifies parties of a hearing date | C.R.C.P. 121 § 1-15 |
| Notice of Filing | Filer | Cover document accompanying a discrete filing (often unnecessary in e-filed cases) | None specific |
| Notice of Substitution of Counsel | New counsel | Substitutes lead counsel | C.R.C.P. 121 § 1-1 |
| Notice of Withdrawal of Counsel | Withdrawing counsel | Counsel withdraws (subject to court approval if trial imminent) | C.R.C.P. 121 § 1-1(3) |
| Notice of Limited Appearance | Limited-scope counsel | Appearance for a specific event or issue | Colo. R. Prof. Conduct 1.2(c); C.R.C.P. 11(b) |
| Notice of Address Change | Pro se party / counsel | Updates service address | C.R.C.P. 121 § 1-1(4) |
| Notice of Dismissal | Plaintiff (before answer) | Voluntary dismissal under C.R.C.P. 41(a)(1) | C.R.C.P. 41(a)(1) |
| Notice of Appeal | Appellant | Triggers appellate jurisdiction | C.A.R. 3, 4 |

## Standard Notice of Hearing scaffold

```
                [Caption — see co-statewide-format]

                       NOTICE OF HEARING

TO ALL PARTIES AND THEIR COUNSEL OF RECORD:

PLEASE TAKE NOTICE that the [Movant]'s [Motion Title], filed
[date], is set for hearing as follows:

  Date:       [Date]
  Time:       [Time]
  Location:   [Courtroom number, courthouse name, address]
              [OR remote via Webex — meeting ID and password]
  Before:     [Honorable Judge Name, Division ##]
  Length:     [Estimated minutes]

Counsel and parties may appear [in person / by Webex / by phone].
Webex connection details: [URL] / Meeting ID: [###] / Password:
[###]. The Court's preference is documented in [Notice of Setting /
practice standards]; verify before the hearing.

Respectfully submitted this ___ day of __________, 20__.

                                        [Signature block]

                       CERTIFICATE OF SERVICE
[Per co-statewide-format]
```

## Notice of Substitution of Counsel

```
              NOTICE OF SUBSTITUTION OF COUNSEL

PLEASE TAKE NOTICE that [New Counsel] hereby enters an appearance
on behalf of [Party Name] in this matter and substitutes for [Prior
Counsel] as counsel of record. [Prior Counsel] is hereby withdrawn.

The undersigned represents that this substitution will not delay
the proceedings and that the substituting attorney is fully
prepared to proceed in accordance with the case-management order.

Respectfully submitted this ___ day of __________, 20__.

                                        [New Counsel signature block]
                                        [Reg. No. #####]
```

## Notice of Address Change

```
                    NOTICE OF CHANGE OF ADDRESS

The undersigned [Party / Counsel] hereby provides the following
updated contact information:

  Effective Date:   [Date]
  Name:             [Name]
  Role:             [Pro se Party / Counsel for ____]
  New Address:      [Street]
                    [City, CO ZIP]
  New Phone:        (###) ###-####
  New Email:        name@example.com

All future communications and service should be directed to the
above. Service through Colorado Courts E-Filing should be effective
immediately upon update of the e-filing profile.

                                        [Signature block]
```

## Notice of Dismissal — C.R.C.P. 41(a)(1)

A plaintiff may **voluntarily dismiss** the action without leave of
court **before** the defendant has answered or moved for summary
judgment. After that, dismissal requires a court order under
C.R.C.P. 41(a)(2) or a stipulation under 41(a)(1)(B).

```
                       NOTICE OF DISMISSAL
                  (UNDER C.R.C.P. 41(a)(1)(A))

PLEASE TAKE NOTICE that Plaintiff hereby voluntarily dismisses this
action [without prejudice / with prejudice]. No Defendant has filed
an answer or motion for summary judgment, and dismissal under
C.R.C.P. 41(a)(1)(A) is therefore proper without a court order.

The undersigned files this Notice as of right.

                                        [Plaintiff / Counsel
                                         signature block]
```

> ⚠ **Two-dismissal rule**: a second voluntary dismissal of the
> same claim under C.R.C.P. 41(a)(1) operates as an **adjudication
> on the merits** — that is, with prejudice. Track prior dismissals
> before filing a second voluntary dismissal.

## Notice of Appeal — C.A.R. 3

A separate set of rules (the Colorado Appellate Rules) govern the
Notice of Appeal; see `co-post-judgment` for the timing and the form
of the notice. Briefly:

- **Filed in the trial court**, not the appellate court
- **Within 49 days** of entry of judgment (C.A.R. 4(a))
- **Form**: see C.A.R. 3.4 for content requirements; pro se filers
  can use **JDF 1402**

## Composition

- For format: `co-statewide-format`
- For the underlying motion: `co-draft-motion`
- For scheduling the hearing the notice references:
  `co-schedule-hearing`
- For the substantive proposed order: `co-draft-order`
- For pro se conventions: `co-pro-se`

## References

- `references/notice-of-hearing-template.md`
- `references/notice-of-substitution-template.md`
- `references/notice-of-dismissal-template.md`
- `references/notice-of-address-change-template.md`
- `references/notice-of-limited-appearance-template.md`
