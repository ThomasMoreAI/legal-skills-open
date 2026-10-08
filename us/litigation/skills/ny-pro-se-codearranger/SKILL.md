---
name: ny-pro-se-codearranger
title: Pro Se Drafting for New York
description: Use when drafting New York court documents for a self- represented (pro se) litigant. Triggers include 'pro se in New York', 'self-represented in NY court', 'I don't have a lawyer for my NY case', 'how to file pro se in Supreme Court', 'pro se in NYC Civil Court', 'represent myself in Kings County', 'self-represented litigant signature block', 'NY court self-help'. Covers the pro-se drafting framework adapted for New York, service protocols under CPLR Article 3, the unique New York signature-block conventions for self-represented parties, and the NY courts' "Self- Represented" / "Help Center" infrastructure (CLARO clinics, the NY Courts CourtHelp portal, and the LawHelpNY referral network).
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ny-court-docs/skills/ny-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for New York

> **NOT LEGAL ADVICE.** This skill assists self-represented
> litigants in drafting their own court documents. It does
> not provide legal advice. Pro se litigants face the same
> rules of procedure as represented parties; verify against
> current rules before filing. For complex matters, or
> matters with substantial sums at stake, consider consulting
> a licensed New York attorney.

## Pro se status in New York

New York courts use **"self-represented litigant"** or
**"pro se"** interchangeably. CPLR 321(a) allows a natural
person to appear without an attorney. A **corporation,
LLC, or partnership** generally **cannot** appear pro se in
Supreme Court (CPLR 321(a) — must be represented by
counsel); narrow exceptions exist in small-claims practice
and certain limited-jurisdiction courts.

## Signature block (pro se)

```
Dated: [City], New York
       [Month Day, Year]

                              _______________________________
                              [PRINT NAME]
                              Self-Represented [Plaintiff/Defendant]
                              [Street Address]
                              [City, State ZIP]
                              [Phone]
                              [Email]
```

Key conventions:

- Use **"Self-Represented Plaintiff"** or **"Self-Represented
  Defendant"** — this is the NY convention; "In Pro Per" and
  similar labels from other jurisdictions are not used here
- **No bar number** (because no attorney admission)
- **Email is recommended** even for paper filings — NYSCEF
  service goes through email, and email service after
  appearance is now common
- **No "Esq."** suffix

## Verification (CPLR 3020 / 3021)

If you serve a verified pleading, the verification is the
sworn statement at the end:

```
VERIFICATION

STATE OF NEW YORK   )
                    ) ss.:
COUNTY OF [COUNTY]  )

[PRINT NAME], being duly sworn, deposes and says: I am
the [Plaintiff/Defendant] in the within action. I have read
the foregoing [Complaint/Answer/etc.] and know the contents
thereof; the same is true to my own knowledge, except as to
matters therein stated to be alleged on information and
belief, and as to those matters I believe them to be true.

                              _______________________________
                              [PRINT NAME]

Sworn to before me this
___ day of __________, [YEAR].

_______________________________
Notary Public
```

Practical note: pro se litigants without notary access can
use a **CPLR 2106 affirmation** in limited circumstances —
but CPLR 2106 historically was for attorneys + medical/
dental/osteopathic professionals only. **CPLR 2106 was
amended in 2023** (L 2023, ch 559) to allow any person to
affirm "under the penalties of perjury" in lieu of an
affidavit. Pro se litigants may now use an affirmation
without a notary.

## Pro-se drafting framework — New York adaptation

The pro-se drafting framework (from the WA / OR plugins) applies in
New York with these state-specific adjustments:

1. **Cite the rule, not the conclusion** — every legal
   assertion must cite a specific CPLR section, statute, or
   case in Tanbook format
2. **Cite the record, not the conclusion** — every factual
   assertion must cite to a specific paragraph of an
   affidavit/affirmation or a specific exhibit page
3. **Use the verb "respectfully"** sparingly — over-use
   reads pro se; reserve for genuine respectful concessions
4. **Use precise NY terminology** — "movant" not "moving
   party"; "respondent" or "non-moving party" for the
   opposing side on a motion; "Affirmation" for attorney
   sworn statements (and pro se 2023+) and "Affidavit" for
   notarized non-attorney statements
5. **Avoid "motion to" + verb constructions for non-CPLR
   motions** — use the actual CPLR section's name (e.g.,
   "motion to dismiss under CPLR 3211(a)(7)" not "motion to
   dismiss for failure to state a claim")
6. **Avoid "declaration"; use affirmation or affidavit** —
   "declaration" is not NY civil-practice terminology

## Service of process (CPLR Article 3)

| Method | Authority | Notes |
|--------|-----------|-------|
| Personal delivery | CPLR 308(1) | First choice; affidavit of service required |
| Substituted ("leave and mail") | CPLR 308(2) | At dwelling/place of business + first-class mail; service complete 10 days after filing affidavit |
| "Nail and mail" | CPLR 308(4) | After "due diligence" fails at 308(1)–(2); affix to door + first-class mail |
| Mail with acknowledgment | CPLR 312-a | Voluntary; complete on signed acknowledgment return |

**CPLR 306-b**: service must be completed **within 120 days**
of filing the summons; failure causes dismissal under CPLR
306-b unless the court extends.

Pro se plaintiffs typically use a **process server** (NYC
license required for paid servers); the process server's
affidavit of service is filed via NYSCEF.

## Pro se resources for New York

| Resource | URL | Purpose |
|----------|-----|---------|
| NY Courts CourtHelp | https://nycourts.gov/courthelp | Statewide pro se portal |
| LawHelpNY | https://lawhelpny.org | Statewide legal-aid referral |
| CLARO clinics | Various NYC Civil Court branches | Free attorney advice for debt cases |
| NYC Civil Court Help Centers | At each Civil Court branch | In-person navigation help |
| NY County Pro Se Office | 60 Centre Street, Room 116 | Supreme Court pro se desk |
| Kings County Pro Se Office | 360 Adams Street, Room 296 | Supreme Court pro se desk |
| Nassau Self-Represented | https://nycourts.gov/courts/10jd/nassau | Pro se resources |
| OCA Forms | https://nycourts.gov/forms | Statewide UCS-form catalog |

## Common pro se motion types

- **Motion to vacate default** (CPLR 5015(a)) — most common
  pro se motion in consumer-debt cases
- **Motion to dismiss** (CPLR 3211) — pre-answer challenge to
  pleading sufficiency or jurisdiction
- **Motion for summary judgment** (CPLR 3212) — must come
  after issue is joined (i.e., after an answer is filed)
- **Order to Show Cause** (CPLR 2214(d)) — for emergency
  relief; requires judicial signature on the OSC itself

## Composition with other ny- skills

- `ny-statewide-format` — format baseline (22 NYCRR § 202.5)
- `ny-draft-motion`, `ny-draft-declaration`,
  `ny-draft-note`, `ny-draft-order` — pro-se drafting framework-adapted
  scaffolders
- `ny-first-30-days` — initial response window
- `ny-deadlines` — CPLR 2103/2103-a timing rules
- `ny-consumer-debt` — debt-buyer defense (the most common
  pro se case type in NY Civil Court)
- `ny-landlord-tenant` — NYC Housing Court pro se practice
