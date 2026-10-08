---
name: ny-draft-declaration-codearranger
title: Draft a New York Affirmation or Affidavit
description: 'Scaffold an affirmation (CPLR 2106) or affidavit (CPLR 2309) for a New York court filing. Triggers include ''draft an affirmation'', ''New York affidavit'', ''CPLR 2106 affirmation'', ''affirmation in support'', ''affidavit of merit'', ''affidavit of service'', ''affidavit in opposition'', ''NY sworn statement'', ''NY declaration of [person]'', ''verify a NY pleading''. Produces an affirmation under the amended CPLR 2106 (post-2023 — any person may affirm under penalty of perjury without a notary) or a traditional CPLR 2309 affidavit, conformed to CPLR 2101 paper-format rules. **Note**: NY uses "affirmation/affidavit" terminology — the word "declaration" does not appear in NY civil practice. This skill is named draft-declaration for filename consistency but produces NY-correct affirmations/affidavits.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-draft-declaration
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Draft a New York Affirmation or Affidavit

> **NOT LEGAL ADVICE.** Sworn statements are subject to
> perjury sanctions. Verify every factual statement.

## Affirmation v. affidavit — choose correctly

| Document | Authority | Notary? | Who can sign |
|---|---|---|---|
| **Affirmation** | CPLR 2106 (as amended 2023) | **No** | Any person, attorney or layperson |
| Affidavit | CPLR 2309 | **Yes** | Any person |

**2023 amendment (L 2023, ch 559)** democratized affirmation:
before, only attorneys (and certain medical/dental
professionals) could affirm without a notary. Now any person
may use the CPLR 2106 affirmation form, ending the
notary-bottleneck for pro se filers.

When to choose each:

- **Affirmation**: default for nearly all situations in
  Supreme Court / Civil Court motion practice
- **Affidavit**: required in specific contexts — verification
  of pleading under CPLR 3020 (some statutes require notary);
  affidavit of service when not by NY-licensed process
  server; affidavit in support of attachment under CPLR
  6212; affidavit of merit in default judgment under CPLR
  3215(b) — historically required (but the CCFA 2022 changes
  shifted this — see `ny-consumer-debt`)

## CPLR 2106 affirmation template

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]
----------------------------------------- X

         AFFIRMATION OF [NAME] IN SUPPORT OF MOTION

[NAME], being duly affirmed, hereby affirms the truth of
the following under penalty of perjury pursuant to CPLR
2106:

1. I am the [Plaintiff/Defendant] in this action. I am
   over 18 years of age and competent to testify to the
   matters set forth herein. I make this affirmation in
   support of [PARTY]'s motion [DESCRIBE].

2. [Fact paragraphs — numbered, one fact each]

3. [Continue numbered]

4. Attached as Exhibit A is a true and accurate copy of
   [DESCRIPTION]. The exhibit is in the form I received
   it from [SOURCE].

[...]

[FINAL PARAGRAPH — the "ask":]
N. For the reasons set forth in this Affirmation and in
   the accompanying Memorandum of Law, [PARTY] respectfully
   requests that the Court [SPECIFIC RELIEF].

Dated: [CITY], New York
       [Month Day, Year]

                              _______________________________
                              [PRINT NAME]
                              Self-Represented [Plaintiff/Defendant]
                              [Street Address]
                              [City, State ZIP]
                              [Phone]
                              [Email]
```

## CPLR 2309 affidavit template

For situations where notary is required (or strongly
preferred):

```
SUPREME COURT OF THE STATE OF NEW YORK
COUNTY OF [COUNTY]
----------------------------------------- X
[CAPTION]
----------------------------------------- X

         AFFIDAVIT OF [NAME] IN SUPPORT OF MOTION

STATE OF NEW YORK   )
                    ) ss.:
COUNTY OF [COUNTY]  )

[NAME], being duly sworn, deposes and says:

1. I am the [Plaintiff/Defendant] in this action [...]

2. [...]

[FINAL PARAGRAPH]
N. For the reasons set forth herein, I respectfully request
   that the Court [SPECIFIC RELIEF].

                              _______________________________
                              [PRINT NAME]

Sworn to before me this
___ day of __________, [YEAR].

_______________________________
Notary Public, State of New York
Commission expires: ____________
```

## Drafting rules — facts only

The affirmation/affidavit is a **sworn statement of facts** —
not legal argument. Per CPLR 3024(b), a court may strike
**scandalous or prejudicial** matter; pure legal argument in
an affirmation is also routinely stricken.

- **One fact per paragraph** — numbered
- **First-person**: "I served the notice" not "the
  defendant served"
- **Personal knowledge**: each fact must be within the
  affiant's personal knowledge unless explicitly "upon
  information and belief"
- **Attach exhibits**: every document referenced should be an
  Exhibit attached to the affirmation
- **Cross-reference exhibits**: "Attached as Exhibit A is a
  true and accurate copy of [...]"
- **Avoid legal conclusions**: "The plaintiff failed to serve
  proper process" → legal conclusion; rewrite as
  "Plaintiff's process server filed an affidavit stating
  service at [ADDRESS]; I did not reside at [ADDRESS] on
  that date" (factual)

## Exhibit attachment conventions

- **Lettered**: Exhibits A, B, C... (NY convention; numbered
  exhibits are uncommon)
- **Tabbed**: for paper filings, tabbed dividers
- **Bookmarked**: for NYSCEF/PDF filings, PDF bookmarks at
  the start of each exhibit
- **Bates-stamped** (recommended): for filings with multiple
  exhibits, Bates-stamp pages

## Common affirmation types

| Type | When |
|------|------|
| Affirmation in Support of Motion | With a Notice of Motion |
| Affirmation in Opposition | Responding to a motion |
| Affirmation in Reply | Replying to opposition |
| Affirmation in Support of OSC | With an Order to Show Cause |
| Affirmation of Service | After serving a paper |
| Affirmation of Engagement (CPLR 125) | Adjournment request |
| Affirmation of Good Faith (22 NYCRR § 202.20-f) | With a motion to compel |
| Affirmation of Merit | With a motion to vacate default (CPLR 5015(a)(1)) |

## Composition with other ny- skills

- `ny-statewide-format` — caption + paper format
- `ny-draft-motion` — coordinated with the motion's memo
- `ny-pro-se` — pro se signature block / verification
- `ny-fact-check` — pre-filing affirmation fact-check
