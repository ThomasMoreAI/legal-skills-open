---
name: id-pro-se-codearranger
title: Pro Se Drafting for Idaho
description: Use when drafting Idaho court documents for a self-represented (pro se) litigant. Triggers include "represent myself in Idaho", "Idaho pro se", "self-represented Idaho court", "filing without a lawyer in Idaho", "Idaho Court Assistance Office", "Idaho court forms", "Guide & File Idaho", "iCourt self-help", "fee waiver Idaho court", "waive Idaho filing fees", "do I need an ISB number to file", and "ISB number self-represented". Covers the pro-se drafting framework adapted for Idaho civil practice, the I.R.C.P. 11 certification (self-represented filers omit the ISB number), service of process under I.R.C.P. 4 and of subsequent papers under I.R.C.P. 5, the iCourt E-File optional-opt-in consequence for self-represented filers, fee waiver / deferral, the Idaho Court Assistance Office self-help forms, and interpreter / ADA accommodations. Composes with `id-statewide-format`, the `id-draft-*` scaffolders, and the venue skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Idaho

> **NOT LEGAL ADVICE.** This skill helps a self-represented party
> prepare paper and procedure. It is not a substitute for advice
> from a licensed Idaho attorney, and you should consult one where
> the stakes warrant. Verify against the current Idaho Rules of
> Civil Procedure, the Idaho Code, the I.R.E.F.S., and local rules
> before filing.

Use this skill alongside `id-statewide-format` whenever the filer is
unrepresented. Idaho courts use **"self-represented"** interchangeably
with "pro se."

## Use the official Idaho form where one exists

Idaho has a mature self-help ecosystem; reach for an official form
**before** drafting from scratch:

- The **Idaho Court Assistance Office (CAO)** publishes statewide
  fillable forms and instructions for common civil, family, and
  protection-order matters (through the Idaho Judicial Branch at
  isc.idaho.gov / courtselfhelp.idaho.gov). Where a statewide form
  exists, courts expect it and clerks process it faster.
- The **iCourt Odyssey "Guide & File"** assisted interview is the
  self-help front end for assembling and e-filing many self-help
  packets.

When an Idaho Supreme Court / CAO form covers the task, prefer it;
reserve free-form drafting (`id-draft-motion` and the other
`id-draft-*` scaffolders) for filings with no governing form.
Confirm the current revision before filing — forms are revised
periodically (see `id-law-references`).

## The pro-se drafting framework — adapted for Idaho

Idaho courts read self-represented filings with some leniency on
form, but will **not act as the filer's lawyer** — they will not
supply missing elements or develop the record. Form slips are
tolerated if the substance is present, but the filer does the
advocacy. Apply this to every filing:

1. State the relief clearly in the opening sentence.
2. Cite the rule or statute (I.R.C.P. ____ / I.C. § ____).
3. State the facts that satisfy each element, with verification or
   an affidavit / declaration where facts must be proven (see
   `id-draft-declaration`).
4. Apply the controlling Idaho authority (Idaho Reports + Pacific
   Reporter — see `id-fact-check`).
5. Conclude with the specific order sought.

## Signature block — self-represented filers omit the ISB number

The signature on every filing **certifies** under **I.R.C.P. 11**
that, to the best of the signer's knowledge after reasonable
inquiry, the filing is warranted by existing law or a non-frivolous
argument and is not interposed for an improper purpose. This
certification — and the Rule 11 sanctions that back it — **apply to
self-represented filers just as to attorneys.**

Idaho-licensed attorneys sign with their **Idaho State Bar number
(ISB #)**. A self-represented filer **has no ISB number and omits
that field** — do not write "N/A." Add a clear self-represented
designation:

```
                                   ____________________________
                                   Jane Q. Doe
                                   [Street address]
                                   [City, ID  ZIP]
                                   Phone: (###) ###-####
                                   Email: jane@example.com
                                   Defendant, Self-Represented
```

See `id-statewide-format` for the full caption and signature
conventions, including the attorney/party block seated above the
title of court.

## Service — process (I.R.C.P. 4) vs. subsequent papers (I.R.C.P. 5)

- **Initial process.** Service of the **summons and complaint** is
  governed by **I.R.C.P. 4**, including who may serve, the permitted
  methods, and the proof-of-service requirement. The summons must be
  **served within 182 days of filing** the complaint. Confirm the
  method and the return requirement against the current rule — see
  `id-first-30-days` and the venue skills.
- **Subsequent papers.** After the initial pleading, **I.R.C.P. 5**
  governs service of every later paper (motions, notices, responses)
  on the other parties or their attorneys of record. Permitted
  methods include personal delivery, mail to the last-known address,
  and — where the party has consented — electronic service through
  iCourt.
- File a **certificate of service** stating who was served, when,
  and how. See `id-statewide-format` for the template; for
  service-method deadline add-ons (the **+3 days** when a period
  runs from service by mail under I.R.C.P. 2.2), use `id-deadlines`.

## iCourt E-File — the opt-in consequence for self-represented filers

Idaho's statewide e-filing portal is **iCourt E-File** (Odyssey File
& Serve), governed by the **I.R.E.F.S.**

- **E-filing is mandatory for attorneys** (I.R.E.F.S. 4(a)) but
  **optional for self-represented individuals** (I.R.E.F.S. 4(b)).
- **Important consequence:** once a self-represented party **opts in
  to e-filing, they are bound to e-file for the life of the case** —
  you cannot e-file one document and then revert to paper. Decide
  deliberately before the first electronic submission.
- **E-filing constitutes consent to electronic service** (I.R.E.F.S.
  17), and documents must meet the **PDF / size requirements** of
  I.R.E.F.S. 6.
- The Odyssey **Guide & File** interview assists self-represented
  filers with assembly and submission.

Confirm whether your court expects paper or e-filing for
self-represented parties, and which document types are accepted —
see `id-file-packet`.

## Fee waiver / deferral

A filer who cannot afford court fees may apply to the court to
**waive or defer** filing fees and costs. Eligibility is keyed to
indigency (public-assistance receipt, income below the operative
threshold, or inability to pay without substantial hardship). File
the application with (or before) the document that triggers the fee,
using the CAO fee-waiver form. Confirm the current standard and the
operative form rather than a fixed income figure (the threshold
drifts — see `id-law-references`).

## Interpreters and ADA accommodations

- **Court interpreters.** Idaho courts provide a foreign-language or
  sign-language interpreter for a limited-English-proficient or deaf
  / hard-of-hearing party or witness in the cases the rules cover.
  Request one from the clerk early.
- **ADA accommodations.** Idaho courts provide reasonable
  accommodations for litigants with disabilities (a request form is
  published). Request well before the hearing date.

## Picking the right court / tier

A self-represented filer must route to the correct trial court and
tier:

| Court / tier | Civil scope |
|---|---|
| **District Court** (district judge) | Civil claims **over $5,000**; equity; felonies; appeals from the Magistrate Division |
| **Magistrate Division** (magistrate judge) | Civil claims **$5,000 or less** (I.C. § 1-2208); eviction (forcible entry / unlawful detainer); probate; **all family-law actions**; misdemeanors; traffic; juvenile |
| **Small Claims Department** | Claims **up to $5,000** (I.C. § 1-2301); no punitive damages; no pain-and-suffering; simplified, attorney-optional |

Route to the venue skill for your court: `id-ada` (Ada County /
Fourth District, Boise), `id-bonneville` (Bonneville County /
Seventh District, Idaho Falls), `id-county-courts` (other counties
and judicial districts), and `id-family-court` (Magistrate-Division
family mechanics). The clerk's office and the Court Assistance Office
can explain filing mechanics and fees but **cannot give legal
advice.**

## Common self-represented pitfalls in Idaho

1. **Drafting from scratch when a CAO statewide form exists** — check
   the Court Assistance Office and Guide & File first; the form is
   expected.
2. **Writing "N/A" for the ISB number** — omit the field and add
   "Self-Represented" with your role instead.
3. **Opting in to iCourt e-filing without realizing it locks you in**
   — once you e-file, you must e-file for the life of the case
   (I.R.E.F.S. 4(b)).
4. **Underweighting the I.R.C.P. 11 certification** — sanctions reach
   self-represented filers; the signature is a sworn-quality
   representation.
5. **Confusing process service (I.R.C.P. 4, summons within 182 days)
   with later-paper service (I.R.C.P. 5)** — they have different
   mechanics and proofs.
6. **Filing in the wrong tier** — confirm District Court vs.
   Magistrate Division vs. Small Claims against the amount and
   subject matter first ($5,000 line; family always Magistrate).
7. **Forgetting the page-1 layout** — the title of court must begin
   ≥ 3" from the top and the document title must appear at the bottom
   of each page (I.R.C.P. 2); see `id-statewide-format`.

## Composition

- Format and signature block: `id-statewide-format`
- Drafting scaffolders: `id-draft-motion`, `id-draft-declaration`
  (affidavits / declarations / verifications), `id-draft-note`
  (notices of hearing), `id-draft-order` (proposed orders — signed
  only by the judge)
- Answer and first responses (21-day answer, I.R.C.P. 12(a)):
  `id-first-30-days`
- Deadline math (I.R.C.P. 2.2 computation, mail-service add-on):
  `id-deadlines`
- Filing and e-filing: `id-file-packet`
- Subject bundle: `id-consumer-debt`; family: `id-family-law`,
  `id-family-court`
- Venue overlay: `id-ada`, `id-bonneville`, `id-county-courts`

## References

- `id-law-references` — canonical I.R.C.P., I.R.E., I.R.E.F.S.,
  Idaho Code, and Idaho-form pointers
- Confirm current CAO / Guide & File form revisions, the fee-waiver
  standard, the $5,000 Magistrate-Division / Small-Claims cap
  (I.C. § 1-2208 / § 1-2301), and iCourt E-File requirements at
  isc.idaho.gov before filing
