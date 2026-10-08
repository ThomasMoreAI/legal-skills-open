---
name: mi-pro-se-codearranger
title: Pro Se Drafting for Michigan
description: This skill should be used when drafting Michigan court documents for a self-represented (pro se) litigant. Triggers include "Michigan pro se", "represent myself Michigan", "self-represented Michigan court", "filing without a lawyer in Michigan", "drafting a pro se motion in Michigan", "answer without an attorney", "SCAO form", "MC 20 fee waiver", "fee waiver Michigan court", "Michigan Legal Help", "do I need a bar number to file pro se". Covers the pro-se drafting framework adapted for Michigan civil practice, the MCR 1.109(E) signature requirement (self-represented filers OMIT the P-number), service of subsequent papers under MCR 2.107, the MC 20 fee-waiver (suspension of fees) under MCR 2.002, court interpreters under MCR 1.111 and ADA accommodations, the SCAO approved-forms ecosystem, and Michigan Legal Help self-help resources. Composes with `mi-statewide-format`, `mi-draft-motion`, and the venue skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Michigan

> **NOT LEGAL ADVICE.** This skill helps a self-represented party
> prepare paper and procedure. It is not a substitute for advice from a
> licensed Michigan attorney, and you should consult one where the
> stakes warrant. Verify against the current Michigan Court Rules and
> local practice before filing.

Use this skill alongside `mi-statewide-format` whenever the filer is
unrepresented. Michigan courts use **"self-represented"** (the SCAO /
Michigan Legal Help phrasing) interchangeably with "pro se."

## Use the official SCAO form where one exists

Michigan has an unusually mature self-help ecosystem; reach for an
official form **before** drafting from scratch:

- The **State Court Administrative Office (SCAO)** publishes statewide
  approved forms in numbered series — the **MC** (general
  civil/miscellaneous), **DC** (district court), and **FOC** (Friend of
  the Court / domestic) series among others. Where a SCAO form exists,
  courts expect it and clerks process it faster.
- **Michigan Legal Help (michiganlegalhelp.org)** hosts guided "Do-It-
  Yourself" interviews that assemble the correct SCAO forms for common
  matters (divorce, custody, eviction defense, small claims, name
  change, fee waivers) and explain the steps.

When a SCAO form covers the task, prefer it; reserve free-form drafting
(`mi-draft-motion` and the other `mi-draft-*` scaffolders) for filings
with no governing form. Confirm the current revision on
courts.michigan.gov — SCAO revises forms periodically.

## The pro-se drafting framework — adapted for Michigan

Michigan courts read self-represented filings with some leniency on
form, but will **not act as the filer's lawyer** — they will not supply
missing elements of a claim or defense or develop the record. Form slips
are tolerated if the substance is present, but the filer does the
advocacy. Apply this to every filing:

1. State the relief clearly in the opening sentence.
2. Cite the rule or statute (MCR ____ / MCL § ____).
3. State the facts that satisfy each element, with verification or an
   affidavit where facts must be proven (see `mi-draft-declaration`).
4. Apply the controlling Michigan authority.
5. Conclude with the specific order sought.

## Signature block — self-represented filers omit the P-number

**MCR 1.109(E)** requires every document to be signed; the signature
**certifies** that, to the best of the signer's knowledge, the filing is
well-grounded in fact, warranted by law, and not interposed for an
improper purpose. This certification — and MCR 1.109(E) sanctions —
**apply to self-represented filers just as to attorneys.**

Michigan-licensed attorneys sign with their **State Bar P-number**. A
self-represented filer **has no P-number and omits that field** — do not
write "N/A." Add a clear self-represented designation:

```
                                        ____________________________
                                        Jane Q. Doe
                                        [Street address]
                                        [City, MI ZIP]
                                        Phone: (###) ###-####
                                        Email: jane@example.com
                                        Defendant, Self-Represented
```

See `mi-statewide-format` for the full caption and signature conventions.

## Service of subsequent papers — MCR 2.107

After the initial summons and complaint, **MCR 2.107** governs service
of every later paper (motions, notices, responses) on the other parties:

- Serve every filed paper on every other party (or that party's attorney
  of record). Permitted methods include personal delivery, mail to the
  last-known address, and, where authorized, electronic service through
  the court's e-filing system (MiFILE).
- File a **proof of service** stating who was served, when, and how. See
  `mi-statewide-format` for the template; for service-method deadline
  add-ons use `mi-deadlines`.

(Service of the original summons and complaint is governed by MCR 2.105 —
see `mi-first-30-days` / the venue skills.)

## Fee waiver — the MC 20 under MCR 2.002

A filer who cannot afford court fees may ask the court to **waive or
suspend fees and costs** under **MCR 2.002** by filing the SCAO
**MC 20, Fee Waiver Request** (paired with the MC 20a order). MCR 2.002
provides for suspension on a showing of indigency — receipt of public
assistance, income below the rule's threshold, or other inability to
pay. File the MC 20 with (or before) the document that triggers the fee.
Confirm the current MCR 2.002 standard and MC 20 revision rather than
relying on a fixed income figure (the threshold drifts — see
`mi-law-references`).

## Court interpreters and ADA accommodations

- **Court interpreters**: **MCR 1.111** governs appointment of a
  foreign-language or sign-language interpreter for a limited-English-
  proficient or deaf/hard-of-hearing party or witness, at no cost to the
  party in the cases the rule covers. Request one from the clerk early.
- **ADA accommodations**: Michigan courts provide reasonable
  accommodations for litigants with disabilities (SCAO publishes a
  request form). Request well before the hearing date.

## Picking the right court

A self-represented filer must route to the correct trial court:

| Court | Civil scope |
|---|---|
| **Circuit Court** | General civil over $25,000; family division (divorce, custody, support); appeals from District/Probate |
| **District Court** | Civil up to $25,000; landlord-tenant / eviction; small claims (up to the statutory cap — verify the current amount) |
| **Probate Court** | Decedents' estates, guardianship, conservatorship, mental-health and certain minor matters |

Route to the venue skill for your court: `mi-wayne` (Wayne County),
`mi-oakland` (Oakland County), `mi-36th-district` (36th District Court,
Detroit), `mi-circuit-courts` (other circuits), `mi-district-courts`
(other district courts), and `mi-family-court` (family-division
mechanics). The clerk's office can explain filing mechanics and fees but
**cannot give legal advice.**

## Common self-represented pitfalls in Michigan

1. **Drafting from scratch when a SCAO form exists** — check
   courts.michigan.gov / Michigan Legal Help first; the form is expected.
2. **Writing "N/A" for the P-number** — omit the field and add
   "Self-Represented" with your role instead.
3. **Underweighting the MCR 1.109(E) certification** — sanctions reach
   pro se filers; the signature is a sworn-quality representation.
4. **Skipping the MCR 2.107 proof of service** — unproven service can
   sink an otherwise-timely filing.
5. **Paying fees you could have had waived** — file the MC 20 (MCR 2.002).
6. **Filing in the wrong court** — confirm Circuit vs. District vs.
   Probate against the amount and subject matter first.

## Composition

- Format and signature block: `mi-statewide-format`
- Drafting scaffolders: `mi-draft-motion`, `mi-draft-declaration`
  (affidavits/verifications), `mi-draft-note` (notices of hearing),
  `mi-draft-order` (proposed orders)
- Answer and first responses: `mi-first-30-days`
- Deadline math (service add-ons, computation): `mi-deadlines`
- Subject bundles: `mi-consumer-debt`, `mi-family-law`,
  `mi-family-court`, `mi-landlord-tenant`
- Venue overlay: `mi-wayne`, `mi-oakland`, `mi-36th-district`,
  `mi-circuit-courts`, `mi-district-courts`

## References

- `mi-law-references` — canonical MCR, MRE, fees, and SCAO-form pointers
- Confirm current SCAO form revisions, the MCR 2.002 indigency standard,
  and the small-claims cap at courts.michigan.gov before filing
