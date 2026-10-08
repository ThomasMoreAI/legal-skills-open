---
name: tx-pro-se-codearranger
title: Pro Se Drafting for Texas
description: Use when drafting Texas court documents for a self-represented (pro se) litigant. Triggers include "represent myself in Texas", "Texas pro se", "self-represented Texas court", "filing without a lawyer in Texas", "TexasLawHelp forms", "eFileTexas self-represented", "do I need a Texas bar number to file", "Statement of Inability to Afford Payment of Court Costs", "waive Texas filing fees", "Texas fee waiver affidavit", "unsworn declaration Texas", "sign a Texas pleading without a lawyer", "serve the other side in Texas". Covers the pro-se drafting framework for Texas civil practice, the TRCP 57 signature by an unrepresented party, the unsworn-declaration option under CPRC § 132.001, service of subsequent papers under TRCP 21a, eFileTexas e-filing, the Statement of Inability to Afford Payment of Court Costs (the fee-waiver instrument that replaced the pauper's affidavit), and the TexasLawHelp.org self-help forms. Composes with `tx-statewide-format`, the `tx-draft-*` scaffolders,
  and the venue skills.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-pro-se
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Pro Se Drafting for Texas

> **NOT LEGAL ADVICE.** This skill helps a self-represented party
> prepare paper and procedure. It is not a substitute for advice from
> a licensed Texas attorney, and you should consult one where the
> stakes warrant. Verify against the current Texas Rules of Civil
> Procedure, the Texas Rules of Evidence, the relevant Texas codes,
> and local rules before filing.

Use this skill alongside `tx-statewide-format` whenever the filer is
unrepresented. Texas courts use **"self-represented"** and
**"pro se"** interchangeably.

## Use the official Texas form where one exists

Texas has a mature self-help ecosystem; reach for an official form
**before** drafting from scratch:

- **TexasLawHelp.org** publishes statewide guided forms and
  instructions for common civil, family, eviction, debt-claim, and
  protective-order matters, maintained by the Texas Legal Services
  Center with the support of the Texas Access to Justice Commission.
  Where a statewide form exists, courts expect it and clerks process
  it faster.
- The Supreme Court of Texas has **promulgated** standardized forms
  (e.g., uncontested-divorce forms, the Statement of Inability to
  Afford Payment of Court Costs) that a court must accept.

When a Supreme Court / TexasLawHelp form covers the task, prefer it;
reserve free-form drafting (`tx-draft-motion` and the other
`tx-draft-*` scaffolders) for filings with no governing form. Confirm
the current revision before filing — forms are revised periodically
(see `tx-law-references`).

## The pro-se drafting framework — adapted for Texas

Texas courts read self-represented filings with some leniency on form,
but hold a pro se litigant to the **same substantive standards** as a
represented party — the court will **not act as the filer's lawyer**
and will not supply missing elements or develop the record. Apply this
to every filing:

1. State the relief clearly in the opening sentence.
2. Cite the rule or statute (Tex. R. Civ. P. ____ / Tex. [Code] §
   ____).
3. State the facts that satisfy each element, supported by an
   affidavit or an **unsworn declaration** where facts must be proven
   (see `tx-draft-declaration`).
4. Apply the controlling Texas authority (South Western Reporter, with
   the court-of-appeals district and petition-history parenthetical —
   see `tx-fact-check`).
5. Conclude with the specific order sought.

Texas petitions also carry two house requirements a pro se filer often
misses, both surfaced by `tx-statewide-format`:

- **Rule 47(c) statement of relief sought** — the original petition
  must plead the range of monetary relief (e.g., "Plaintiff seeks
  monetary relief of $250,000 or less"). Omitting it can bar a default
  and draw special exceptions.
- **TRCP 78a Civil Case Information Sheet** — filed with the initial
  pleading.

## Signature block — self-represented filers omit the bar number

Every filing must be **signed**. **TRCP 57** requires that a party not
represented by an attorney sign their pleadings and state their
address, telephone number, email address, and (if any) fax number. The
signature is a certification (TRCP 13) that the pleading is not
groundless and brought in bad faith or for harassment; **Rule 13 and
Chapter 10 sanctions reach self-represented filers just as they reach
attorneys.**

Texas-licensed attorneys sign with their **State Bar of Texas bar
number**. A self-represented filer **has no bar number and omits that
field** — do not write "N/A." Add a clear self-represented
designation:

```
                                   ____________________________
                                   Jane Q. Doe
                                   [Street address]
                                   [City, TX  ZIP]
                                   Telephone: (###) ###-####
                                   Email: jane@example.com
                                   Defendant, Pro Se
```

See `tx-statewide-format` for the full caption and signature
conventions.

## The unsworn declaration — CPRC § 132.001

Texas lets an **unsworn declaration** substitute for an affidavit,
verification, or other sworn statement in most civil matters. Under
**Tex. Civ. Prac. & Rem. Code § 132.001**, an unsworn declaration is
valid if it is **in writing and subscribed** by the declarant as true
under penalty of perjury, in substantially the statutory form, and
includes the declarant's **date of birth and address**. This lets a
pro se filer verify a pleading or supply declaration testimony
**without finding a notary**. A handful of instruments still require a
true notarized affidavit (confirm the carve-outs against the current
statute — see `tx-law-references`).

```
"My name is ______________, my date of birth is __________, and my
address is ____________________. I declare under penalty of perjury
that the foregoing is true and correct. Executed in ______ County,
State of Texas, on the ___ day of __________, 20__.
                                   ____________________________
                                   Declarant"
```

The drafting mechanics of affidavits, verifications, and unsworn
declarations live in `tx-draft-declaration`.

## Service — citation (TRCP 99/106) vs. subsequent papers (TRCP 21a)

- **Initial process (citation).** Service of the **citation and
  petition** is formal — by a sheriff, constable, or authorized
  process server under **TRCP 99 and 106** (and TRCP 103). A
  self-represented **plaintiff may not serve their own citation.**
  Defective service is a defense the defendant can raise — see
  `tx-first-30-days`.
- **Subsequent papers.** After the petition, **TRCP 21 and 21a**
  govern service of every later paper (motions, notices, responses,
  discovery) on the other parties or their attorneys of record.
  Permitted methods include e-service (mandatory for anyone who
  e-files), commercial delivery, mail, and — by agreement — fax or
  email. File a **certificate of service** stating who was served,
  when, and how (`tx-statewide-format` carries the template). For the
  **+3-day add-on** that TRCP 21a applies to certain service methods,
  use `tx-deadlines`.

## eFileTexas — the statewide e-filing portal

Texas's mandatory statewide e-filing portal is **eFileTexas.gov**
(Tyler Technologies Odyssey File & Serve), under **TRCP 21(f)** and the
Supreme Court's e-filing rules.

- **E-filing is mandatory for attorneys** in civil cases in all courts.
- **Self-represented filers may e-file** (it is encouraged, and some
  courts and case types route everyone through the portal); paper
  filing remains available to pro se litigants where the local court
  permits it.
- E-service through the portal is the default for served e-filers; the
  envelope's service contacts must be set correctly.

Confirm whether your court expects paper or e-filing for
self-represented parties, and which document types are accepted — see
`tx-file-packet`.

## Fee waiver — the Statement of Inability to Afford Payment of Court Costs

A filer who cannot afford court costs files a **Statement of Inability
to Afford Payment of Court Costs** under **TRCP 145**. This sworn
statement **replaced the old "affidavit of inability to pay" /
"pauper's affidavit."**

- The Supreme Court has **promulgated the form**; the clerk must accept
  it, and no filing fee may be charged for filing it.
- A filer is presumed unable to afford costs if they receive certain
  public benefits, are represented by a legal-aid provider, or have
  income below the operative federal-poverty multiple — otherwise the
  statement details income, assets, expenses, and debts.
- Costs may be challenged by motion; the court may then hold a hearing
  and require proof, and may order partial payment.

File the Statement with (or before) the document that triggers the fee.
Confirm the current form and the operative standard rather than a fixed
income figure (the threshold drifts — see `tx-law-references`).

## Interpreters and ADA accommodations

- **Court interpreters.** Texas courts provide a spoken-language or
  sign-language interpreter for a limited-English-proficient or deaf /
  hard-of-hearing party or witness. Request one from the clerk or court
  coordinator early.
- **ADA accommodations.** Texas courts provide reasonable
  accommodations for litigants with disabilities; each court publishes
  an ADA-access contact. Request well before the hearing date.

## Picking the right court / tier

A self-represented filer must route to the correct trial court and
tier:

| Court / tier | Civil scope |
|---|---|
| **District Court** | General civil jurisdiction (no upper limit), title to land, divorce & SAPCR, larger disputes |
| **County Court at Law / Constitutional County Court** | Mid-tier civil amounts (statutory caps — confirm against the corpus), probate in many counties, de novo appeals from Justice Court |
| **Justice Court (Justice of the Peace)** | Small-claims / debt-claim cases up to the statutory ceiling (confirm against Gov't Code § 27.031 / TRCP 500.3), eviction (forcible detainer), repair-and-remedy — governed by TRCP 500–510 |

Justice-court procedure is simplified: under **TRCP 500.3(e)** the
other Rules of Civil Procedure and the Rules of Evidence do **not**
apply in justice court except where Part V (Rules 500–510)
specifically incorporates them. Route to the venue skill for your
court: `tx-hcdc`, `tx-dcdc`, `tx-county-courts` (county-court-at-law
and justice-court roll-up), and `tx-family-court`. The clerk's office
can explain filing mechanics and fees but **cannot give legal
advice.**

## Common self-represented pitfalls in Texas

1. **Drafting from scratch when a TexasLawHelp / Supreme Court form
   exists** — check first; the form is expected and clerks process it
   faster.
2. **Writing "N/A" for the bar number** — omit the field and add "Pro
   Se" with your party role instead (TRCP 57).
3. **Omitting the Rule 47(c) relief range or the TRCP 78a information
   sheet** from the original petition — both are house requirements.
4. **Trying to serve your own citation** — initial process must be
   served by an authorized person (TRCP 103/106), not the party.
5. **Notarizing when an unsworn declaration would do** — CPRC §
   132.001 lets you verify under penalty of perjury without a notary
   (include date of birth and address).
6. **Missing the answer deadline** — Texas uses the **Monday rule**
   (TRCP 99), not a flat count; see `tx-first-30-days` and
   `tx-deadlines`.
7. **Filing in the wrong tier** — confirm District Court vs. County
   Court at Law vs. Justice Court against the amount and subject matter
   first.

## Composition

- Format and signature block: `tx-statewide-format`
- Drafting scaffolders: `tx-draft-motion`, `tx-draft-declaration`
  (affidavits / unsworn declarations / verifications), `tx-draft-note`
  (notices of hearing), `tx-draft-order` (proposed orders — signed
  only by the judge)
- Answer and first responses (the Monday-rule answer, TRCP 99):
  `tx-first-30-days`
- Deadline math (TRCP 4 computation, TRCP 21a service add-on):
  `tx-deadlines`
- Filing and e-filing: `tx-file-packet`
- Subject bundle: `tx-consumer-debt`; family: `tx-family-law`,
  `tx-family-court`
- Venue overlay: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`

## References

- `tx-law-references` — canonical TRCP, Tex. R. Evid., Texas codes,
  and Texas-form pointers
- Confirm the current TexasLawHelp / Supreme Court form revisions, the
  TRCP 145 Statement-of-Inability standard and form, and the
  eFileTexas requirements before filing
