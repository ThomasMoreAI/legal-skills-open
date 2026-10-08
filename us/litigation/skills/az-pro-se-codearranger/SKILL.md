---
name: az-pro-se-codearranger
title: Pro Se Drafting for Arizona
description: This skill should be used when drafting Arizona court documents for a self-represented (pro se) litigant. Triggers include "represent myself Arizona", "Arizona pro se", "self-represented Arizona court", "filing without a lawyer in Arizona", "Arizona self-service center", "Arizona court forms", "fee waiver A.R.S. 12-302", "defer or waive court fees Arizona", "AZTurboCourt", "do I need a bar number to file in Arizona". Covers the pro-se drafting framework adapted for Arizona civil practice, the Rule 11 certification (self-represented filers omit the bar number), service of process under Ariz. R. Civ. P. 4 / 4.1 / 4.2 and service of subsequent papers under Rule 5, fee deferral and waiver under A.R.S. § 12-302, the Arizona Judicial Branch Self-Service Center and county Law Library Resource Centers, AZTurboCourt e-filing, and interpreter / ADA accommodations. Composes with `az-statewide-format`, the `az-draft-*` scaffolders, and the venue skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Arizona

> **NOT LEGAL ADVICE.** This skill helps a self-represented party prepare
> paper and procedure. It is not a substitute for advice from a licensed
> Arizona attorney, and you should consult one where the stakes warrant.
> Verify against the current Arizona Rules of Civil Procedure, the A.R.S.,
> and local rules before filing.

Use this skill alongside `az-statewide-format` whenever the filer is
unrepresented. Arizona courts use **"self-represented"** (the Judicial
Branch's preferred phrasing) interchangeably with "pro se."

## Use the official Arizona form where one exists

Arizona has a mature self-help ecosystem; reach for an official form
**before** drafting from scratch:

- The **Arizona Judicial Branch Self-Service Center**
  (azcourts.gov/selfservicecenter) publishes statewide fillable forms and
  instructions for common civil, family, and probate matters. Where a
  statewide form exists, courts expect it and clerks process it faster.
- Many counties — Maricopa and Pima especially — operate **Law Library
  Resource Centers (LLRCs)** with county-specific packets, form kits, and
  self-help guidance. Some matters also have local Superior Court forms.

When an Arizona Supreme Court or county form covers the task, prefer it;
reserve free-form drafting (`az-draft-motion` and the other `az-draft-*`
scaffolders) for filings with no governing form. Confirm the current
revision before filing — forms are revised periodically (see
`az-law-references`).

## The pro-se drafting framework — adapted for Arizona

Arizona courts read self-represented filings with some leniency on form,
but will **not act as the filer's lawyer** — they will not supply missing
elements or develop the record. Form slips are tolerated if the substance
is present, but the filer does the advocacy. Apply this to every filing:

1. State the relief clearly in the opening sentence.
2. Cite the rule or statute (Ariz. R. Civ. P. ____ / A.R.S. § ____).
3. State the facts that satisfy each element, with verification or an
   affidavit where facts must be proven (see `az-draft-declaration`).
4. Apply the controlling Arizona authority.
5. Conclude with the specific order sought.

## Signature block — self-represented filers omit the bar number

The signature on every filing **certifies** under **Ariz. R. Civ. P. 11**
that, to the best of the signer's knowledge after reasonable inquiry, the
filing is well-grounded in fact, warranted by law, and not interposed for
an improper purpose. This certification — and the Rule 11 sanctions that
back it — **apply to self-represented filers just as to attorneys.**

Arizona-licensed attorneys sign with their **State Bar of Arizona bar
number**. A self-represented filer **has no bar number and omits that
field** — do not write "N/A." Add a clear self-represented designation:

```
                                        ____________________________
                                        Jane Q. Doe
                                        [Street address]
                                        [City, AZ ZIP]
                                        Phone: (###) ###-####
                                        Email: jane@example.com
                                        Defendant, Self-Represented
```

See `az-statewide-format` for the full caption and signature conventions.

## Service — process (Rule 4 / 4.1 / 4.2) vs. subsequent papers (Rule 5)

- **Initial process.** Service of the summons and the original pleading is
  governed by **Ariz. R. Civ. P. 4** (general provisions, process server
  requirements), **Rule 4.1** (service within Arizona), and **Rule 4.2**
  (service outside Arizona). Confirm the method, who may serve, and the
  proof-of-service requirement against the current rule — see
  `az-first-30-days` and the venue skills.
- **Subsequent papers.** After the initial pleading, **Ariz. R. Civ. P. 5**
  governs service of every later paper (motions, notices, responses) on
  the other parties or their attorneys of record. Permitted methods
  include personal delivery, mail to the last-known address, and, where
  authorized, electronic service through the court's e-filing system.
- File a **certificate of service** stating who was served, when, and how.
  See `az-statewide-format` for the template; for service-method deadline
  add-ons use `az-deadlines`.

## Fee deferral and waiver — A.R.S. § 12-302

A filer who cannot afford court fees may apply to the court to **defer or
waive** filing fees and costs under **A.R.S. § 12-302** — a **deferral**
postpones payment (typically on a plan); a **waiver** excuses it.
Eligibility is keyed to indigency (specified public assistance, income
below the statutory threshold, or inability to pay without substantial
hardship). File the application with (or before) the document that
triggers the fee. Confirm the current § 12-302 standard and the operative
form rather than a fixed income figure (the threshold drifts — see
`az-law-references`).

## E-filing, interpreters, and ADA accommodations

- **AZTurboCourt** is the Arizona courts' statewide e-filing portal;
  many courts require or accept e-filing through it. Confirm whether your
  court mandates e-filing and which document types it covers — see
  `az-file-packet`.
- **Court interpreters.** Arizona courts provide a foreign-language or
  sign-language interpreter for a limited-English-proficient or deaf /
  hard-of-hearing party or witness, at no cost in the cases the rules
  cover. Request one from the clerk early.
- **ADA accommodations.** Arizona courts provide reasonable accommodations
  for litigants with disabilities (a request form is published). Request
  well before the hearing date.

## Picking the right court

A self-represented filer must route to the correct trial court:

| Court | Civil scope |
|---|---|
| **Superior Court** | General-jurisdiction civil (above the Justice Court cap); family (dissolution, custody, support); probate; appeals from limited-jurisdiction courts |
| **Justice Courts** | Limited civil at or below the jurisdictional cap; small claims; residential eviction / special detainer |
| **Municipal Courts** | City-code criminal, traffic, and ordinance matters (not the general civil forum) |

Route to the venue skill for your court: `az-maricopa` (Maricopa County),
`az-pima` (Pima County), `az-superior-courts` (other counties' Superior
Courts), `az-justice-courts` (limited civil / small claims / eviction),
and `az-family-court` (family-court mechanics). The clerk's office and the
Self-Service Center can explain filing mechanics and fees but **cannot
give legal advice.**

## Common self-represented pitfalls in Arizona

1. **Drafting from scratch when a statewide or LLRC form exists** — check
   the Self-Service Center and your county Law Library Resource Center
   first; the form is expected.
2. **Writing "N/A" for the bar number** — omit the field and add
   "Self-Represented" with your role instead.
3. **Underweighting the Rule 11 certification** — sanctions reach pro se
   filers; the signature is a sworn-quality representation.
4. **Confusing process service (Rule 4 / 4.1 / 4.2) with later-paper
   service (Rule 5)** — they have different mechanics and proofs.
5. **Paying fees you could have had deferred or waived** — apply under
   A.R.S. § 12-302.
6. **Filing in the wrong court** — confirm Superior vs. Justice vs.
   Municipal against the amount and subject matter first.

## Composition

- Format and signature block: `az-statewide-format`
- Drafting scaffolders: `az-draft-motion`, `az-draft-declaration`
  (affidavits / verifications), `az-draft-note` (notices of hearing),
  `az-draft-order` (proposed orders)
- Answer and first responses: `az-first-30-days`
- Deadline math (service add-ons, computation): `az-deadlines`
- Filing and e-filing: `az-file-packet`
- Subject bundles: `az-consumer-debt`, `az-family-law`, `az-family-court`,
  `az-landlord-tenant`, `az-personal-injury`, `az-employment`,
  `az-commercial-disputes`
- Venue overlay: `az-maricopa`, `az-pima`, `az-superior-courts`,
  `az-justice-courts`

## References

- `az-law-references` — canonical Ariz. R. Civ. P., evidence, fees, and
  Arizona-form pointers
- Confirm current statewide / LLRC form revisions, the A.R.S. § 12-302
  deferral/waiver standard, the Justice Court jurisdictional cap, and
  AZTurboCourt e-filing requirements at azcourts.gov before filing
