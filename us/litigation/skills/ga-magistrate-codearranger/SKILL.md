---
name: ga-magistrate-codearranger
title: Georgia Magistrate Court (Small Claims) — O.C.G.A. § 15-10-2
description: 'Use for any Georgia Magistrate Court matter — the small-claims and limited-jurisdiction civil court with statement-of-claim practice and deliberately informal procedure. Civil jurisdiction is capped (verify the current O.C.G.A. § 15-10-2(5) cap); dispossessory (eviction), garnishment, and attachment within the cap are also heard. Triggers: "Georgia small claims", "Magistrate Court Georgia", "magistrate court statement of claim", "answer a magistrate suit", "sued for under the cap in Georgia", "appeal magistrate de novo", "dispossessory warrant", "garnishment magistrate court", "can a company sue me in magistrate court", "small claims jurisdictional limit Georgia". KEY POINTS: procedure is informal (CPA and evidence rules relaxed; parties appear pro se; corporations may appear through an officer or agent); appeal is DE NOVO to State or Superior Court. Layers on top of `ga-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-magistrate
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Magistrate Court (Small Claims) — O.C.G.A. § 15-10-2

> **NOT LEGAL ADVICE.** These notes describe the venue's procedural
> mechanics as a drafting aid, not legal advice. Magistrate Court
> rules, county practices, and the jurisdictional cap change; verify
> with the Magistrate Court clerk and the current Uniform Magistrate
> Court Rules before relying on anything here. A default or a missed de
> novo appeal deadline has real, fast consequences — respond promptly
> and consider consulting a licensed Georgia attorney or a legal-aid
> clinic.

Use this skill in addition to `ga-statewide-format` when the matter is
in a Georgia **Magistrate Court** — the small-claims, limited-
jurisdiction civil court that sits in **every county**. It is built to
be usable by self-represented parties: pleadings are simple, the
procedure is informal, and the dollar stakes are capped.

## Jurisdiction and the dollar cap

Magistrate Court civil jurisdiction is set by **O.C.G.A. § 15-10-2**.
The core grants the bundle cares about:

- **Civil claims up to the statutory cap (O.C.G.A. § 15-10-2(5))** —
  the cap is **$15,000** (exclusive of interest, costs, and attorney's
  fees). Note: this figure has stood at **$15,000 since 1999**, and a
  **2024 amendment did not raise it** — but treat "$15,000" as a
  figure to **verify against the current § 15-10-2(5) cap** before
  relying on it.
- **Dispossessory (eviction) proceedings (O.C.G.A. § 15-10-2(6))** —
  the dollar cap **does not apply** to the money judgment in a
  dispossessory action; the court can enter a possession-and-rent
  judgment exceeding the cap. See `ga-county-courts` for county
  variations in dispossessory practice.
- **Garnishment and attachment within the cap** — post-judgment
  garnishment and statutory attachment may be heard. **There is no
  prejudgment attachment** in Magistrate Court.
- Distress warrants and certain other limited proceedings.

A claim **above** the § 15-10-2(5) cap belongs in **State Court** (any
amount, see `ga-state-court`) or **Superior Court**.

## Informal procedure (O.C.G.A. §§ 15-10-40 to 15-10-53)

The defining feature of Magistrate Court is its **informality**. Under
**O.C.G.A. §§ 15-10-40 to 15-10-53** and the **Uniform Magistrate
Court Rules**:

- The full **Civil Practice Act** and the **rules of evidence are
  relaxed** — the proceeding is summary and the magistrate is not
  bound by the formalities that govern a State or Superior Court trial.
- **Parties appear pro se** as the norm; the process is designed for
  self-represented litigants.
- **Corporations and other entities may appear through an officer or
  agent** (not only through a licensed attorney) — a notable
  departure from higher-court practice.
- Pleading is by **statement of claim**, not a formal CPA complaint
  (below).

Because the rules are relaxed, do **not** import a State-Court motion
form, a § 9-11-56 summary-judgment timeline, or formal CPA discovery
into a Magistrate case as if it controlled — check whether the Uniform
Magistrate Court Rules provide for the mechanic first. The informality
favors a self-represented defendant, but it also lets a debt-buyer
plaintiff try to prove up an account without the evidentiary
formalities a higher court would require — so scrutinize the
plaintiff's proof and the **chain of title** (see `ga-consumer-debt`).

## Statement-of-claim practice and the answer

- **Commencement** — the plaintiff files a short **statement of
  claim** describing the demand; the clerk issues a summons and the
  defendant is served.
- **Answer** — the defendant responds within the period set by the
  statute and the Uniform Magistrate Court Rules (an answer may be
  oral or written depending on county practice). **Confirm the current
  answer deadline** with the Magistrate Court clerk before
  calendaring. A general denial puts the plaintiff to its proof.
- **Default** — failure to answer/appear can result in a default
  judgment for the plaintiff; the magistrate may require proof of the
  claim and damages. Act before the deadline. See `ga-first-30-days`
  for the answer framework (adapted to the informal posture).

## DE NOVO appeal to State or Superior Court

A party who loses in Magistrate Court has a **de novo** appeal — a
**brand-new trial** in the higher court, not a record-review appeal:

- **General civil appeal (O.C.G.A. § 15-10-41(b))** — appeal is **de
  novo** to the **State Court** (if the county has one) or the
  **Superior Court**, perfected within the rule's deadline. **Confirm
  the current § 15-10-41(b) appeal window** — it is short.
- **Dispossessory appeals (O.C.G.A. § 44-7-56)** — eviction judgments
  appeal under the dispossessory statute on its own (also short)
  timeline; a tenant who appeals to remain in possession faces
  pay-rent-into-the-registry conditions. **Confirm the current
  § 44-7-56 deadline and conditions** — missing them forfeits the
  appeal and possession.

On a de novo appeal the case is tried anew in the destination court as
if it had originated there — the destination court and its full CPA
procedure live in `ga-state-court` (or, for superior-exclusive
subjects, the Superior Court via `ga-county-courts`).

## Caption — Magistrate Court variant

```
                  MAGISTRATE COURT OF [COUNTY] COUNTY
                          STATE OF GEORGIA

[PLAINTIFF],                        )
                                    )
        Plaintiff,                  )   Civil Action File No. _________
                                    )
v.                                  )
                                    )
[DEFENDANT],                        )
                                    )
        Defendant.                  )

              STATEMENT OF CLAIM / [DOCUMENT TITLE]
```

Most Magistrate Courts supply a fill-in **statement-of-claim** form;
when drafting a free-form paper, the caption reads **"MAGISTRATE COURT
OF [COUNTY] COUNTY / STATE OF GEORGIA"** with a **"Civil Action File
No. ____"**. See `ga-statewide-format` for the pleading-paper
baseline and the pro se signature block; the magistrate form may
supersede the full formal layout — confirm with the clerk.

**Agent behavior:** before drafting, confirm (1) the claim falls
**within the current § 15-10-2(5) cap** (or is a dispossessory /
garnishment matter where a different rule applies), (2) the **answer
deadline** and the **de novo appeal window** (O.C.G.A. § 15-10-41(b);
dispossessory under § 44-7-56), (3) whether the county supplies a
**statement-of-claim form** and accepts oral vs. written answers, and
(4) the county's **e-filing posture** (Magistrate e-filing is often
optional — see `ga-county-courts`). Treat the Uniform Magistrate Court
Rules as the controlling rule set and do not assume full CPA procedure
applies.

## Composition

- For statewide format and the Georgia caption: `ga-statewide-format`
- For the destination of a de novo appeal (civil-any-amount forum):
  `ga-state-court`
- For per-county Magistrate practice, dispossessory variations, and
  e-filing posture: `ga-county-courts`
- For the answer / general denial and default avoidance:
  `ga-first-30-days`
- For consumer-debt defenses (chain of title, account-stated, SOL):
  `ga-consumer-debt`
- For deadline computation and Georgia legal holidays: `ga-deadlines`
- For assembling and filing a packet: `ga-file-packet`
- For citation verification: `ga-fact-check`

## References

- `references/magistrate-jurisdiction.md` — O.C.G.A. § 15-10-2 grants,
  the § 15-10-2(5) civil cap, and § 15-10-2(6) dispossessory
- `references/informal-procedure.md` — O.C.G.A. §§ 15-10-40 to
  15-10-53 informal procedure, statement-of-claim practice, and entity
  appearance through an officer or agent
- `references/de-novo-appeal.md` — O.C.G.A. § 15-10-41(b) de novo
  appeal and § 44-7-56 dispossessory appeals
