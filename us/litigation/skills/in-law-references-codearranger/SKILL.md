---
name: in-law-references-codearranger
title: Indiana Law References — Canonical Catalog
description: 'Canonical reference catalog for Indiana civil practice. Houses **Indiana Trial Rules**, **Indiana Rules of Evidence**, **Appellate Rules**, **Small Claims Rules**, relevant **IC chapters**, shared **federal-debt-laws** and **UCC model**, and **Indiana Supreme Court Rule on Citation**. Use when asked "what''s the rule...", "Indiana Trial Rule...", "Indiana Code...", "filing fees", "legal holidays", "citation format". Triggers: "Indiana civil rules", "Ind. Trial R.", "Ind. Evid. R.", "Indiana Code lookup", "IC SOL".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Admin Rules
  path: references/court-rules/Admin-Rules.md
- title: Appellate Rules
  path: references/court-rules/Appellate-Rules.md
- title: Evidence Rules
  path: references/court-rules/Evidence-Rules.md
- title: Lake Local Rules
  path: references/court-rules/Lake-Local-Rules.md
- title: Marion Local Rules
  path: references/court-rules/Marion-Local-Rules.md
- title: Professional Conduct
  path: references/court-rules/Professional-Conduct.md
- title: Readme
  path: references/court-rules/README.md
- title: Trial Rules
  path: references/court-rules/Trial-Rules.md
- title: Ic 24 4 5
  path: references/in-statutes-debt/IC-24-4-5.md
- title: Ic 24 5 0 5
  path: references/in-statutes-debt/IC-24-5-0-5.md
- title: Ic 26 1 2
  path: references/in-statutes-debt/IC-26-1-2.md
- title: Ic 26 1 3
  path: references/in-statutes-debt/IC-26-1-3.md
- title: Ic 26 1 9 1
  path: references/in-statutes-debt/IC-26-1-9-1.md
- title: Ic 31 14
  path: references/in-statutes-debt/IC-31-14.md
- title: Ic 31 15
  path: references/in-statutes-debt/IC-31-15.md
- title: Ic 31 16
  path: references/in-statutes-debt/IC-31-16.md
- title: Ic 31 17
  path: references/in-statutes-debt/IC-31-17.md
- title: Ic 31 19
  path: references/in-statutes-debt/IC-31-19.md
- title: Ic 31 21
  path: references/in-statutes-debt/IC-31-21.md
- title: Ic 31 25
  path: references/in-statutes-debt/IC-31-25.md
- title: Ic 31 30
  path: references/in-statutes-debt/IC-31-30.md
- title: Ic 31 32
  path: references/in-statutes-debt/IC-31-32.md
- title: Ic 31 34
  path: references/in-statutes-debt/IC-31-34.md
- title: Ic 31 37
  path: references/in-statutes-debt/IC-31-37.md
- title: Ic 32 21
  path: references/in-statutes-debt/IC-32-21.md
- title: Ic 32 29
  path: references/in-statutes-debt/IC-32-29.md
- title: Ic 32 30
  path: references/in-statutes-debt/IC-32-30.md
- title: Ic 32 31
  path: references/in-statutes-debt/IC-32-31.md
- title: Ic 33 29
  path: references/in-statutes-debt/IC-33-29.md
- title: Ic 34 11
  path: references/in-statutes-debt/IC-34-11.md
- title: Ic 34 26
  path: references/in-statutes-debt/IC-34-26.md
- title: Ic 34 50
  path: references/in-statutes-debt/IC-34-50.md
- title: Ic 34 55
  path: references/in-statutes-debt/IC-34-55.md
- title: Ic 34 57
  path: references/in-statutes-debt/IC-34-57.md
- title: Ic 35 43 5
  path: references/in-statutes-debt/IC-35-43-5.md
- title: Readme
  path: references/in-statutes-debt/README.md
---

# Indiana Law References — Canonical Catalog

This is the matter-neutral reference catalog for Indiana civil
practice. It indexes every authoritative source the other
in-court-docs skills cite. Treat this as the **library** that the
rest of the plugin pulls from. The substantive reference content
itself lives under `references/` in this skill and the dependency
plugin `claude-legal-federal-laws`.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify against the most current Indiana Trial Rules and
> Indiana Code before filing — rules and statutes are amended
> annually.

## The five pillars of Indiana civil practice law

1. **Indiana Trial Rules** (Ind. Trial R. / T.R.) — adopted by
   the Indiana Supreme Court in 1970, patterned after the Federal
   Rules of Civil Procedure with Indiana-specific deviations
   (e.g., T.R. 56 burden allocation; T.R. 59 motion to correct
   error). Published at `courts.in.gov/rules/trial_proc/`.
2. **Indiana Rules of Evidence** (Ind. Evid. R. / IRE) — adopted
   in 1994; tracks the Federal Rules of Evidence with Indiana
   carve-outs.
3. **Indiana Code** (IC) — the statutory law of Indiana, organized
   into 36 titles. Civil-procedure-relevant titles: IC 1
   (Sovereignty), IC 13 (Environment), IC 23 (Business), IC 24
   (Trade Regulation, including IC 24-4.5 IUCCC and IC 24-5-0.5
   DCSA), IC 26 (Commercial Law / UCC enactment), IC 32 (Real
   Property), IC 33 (Courts and Judicial Procedure), IC 34
   (Civil Procedure), IC 35 (Criminal Law and Procedure), IC 36
   (Local Government).
4. **Indiana Supreme Court Rules** — includes the Rules of
   Appellate Procedure (Ind. App. R.), the Indiana Administrative
   Rules (Ind. Admin. R.), the Rules for Admission to the Bar
   (Ind. Admis. Disc. R.), and the Rule on Citation (within the
   Admission, Discipline, and Citation Rules).
5. **Local Rules** — every county adopts a local rule set under
   the prefix `LR[county-code]`. Marion = LR49, Lake = LR45,
   Hamilton = LR29, etc.

## Indiana Trial Rules — index of the most-cited rules

| Rule | Subject | Cross-skill |
|------|---------|-------------|
| T.R. 3 | Commencement of action | `in-first-30-days` |
| T.R. 3.1 | Appearance | `in-pro-se` |
| T.R. 4 | Process — Summons | `in-pro-se` |
| T.R. 4.1 | Personal service | `in-pro-se` |
| T.R. 4.4 | Service on nonresident | `in-pro-se` |
| T.R. 5 | Service and filing of pleadings | `in-statewide-format` |
| T.R. 5(B) | Service after commencement | `in-statewide-format` |
| T.R. 5(E) | Format of papers | `in-statewide-format` |
| T.R. 6 | Time computation | `in-deadlines` |
| T.R. 6(C) | Answer due 20 days | `in-first-30-days` |
| T.R. 7 | Pleadings allowed; motions | `in-draft-motion` |
| T.R. 8 | General rules of pleading | `in-first-30-days` |
| T.R. 9 | Pleading special matters | `in-first-30-days` |
| T.R. 10 | Form of pleadings | `in-statewide-format` |
| T.R. 11 | Signature; verification | `in-statewide-format` |
| T.R. 12 | Defenses + motions to dismiss | `in-first-30-days` |
| T.R. 12(B)(6) | Failure to state a claim | `in-first-30-days` |
| T.R. 13 | Counterclaim and cross-claim | `in-first-30-days` |
| T.R. 15 | Amended and supplemental pleadings | `in-first-30-days` |
| T.R. 16 | Pre-trial procedure | `in-marion`, `in-lake` |
| T.R. 26 | Discovery — general | `in-discovery` |
| T.R. 30 | Depositions | `in-discovery` |
| T.R. 33 | Interrogatories (25-cap) | `in-discovery` |
| T.R. 34 | Production of documents | `in-discovery` |
| T.R. 36 | Requests for admissions | `in-discovery` |
| T.R. 37 | Motion to compel | `in-discovery` |
| T.R. 41 | Dismissal of actions | `in-first-30-days` |
| T.R. 45 | Subpoena | `in-discovery` |
| T.R. 50 | Judgment on the evidence / JNOV | `in-hearings` |
| T.R. 55 | Default judgment | `in-first-30-days` |
| T.R. 56 | Summary judgment | `in-draft-motion`, `in-discovery` |
| T.R. 59 | Motion to correct error | `in-post-judgment` |
| T.R. 60 | Relief from judgment | `in-post-judgment` |
| T.R. 65 | Preliminary injunction | `in-draft-motion` |
| T.R. 69 | Execution / supplemental proceedings | `in-post-judgment` |

## Indiana Rules of Evidence — index

| Rule | Subject |
|------|---------|
| IRE 401-403 | Relevance |
| IRE 404-405 | Character evidence |
| IRE 602 | Personal knowledge |
| IRE 607-609 | Witness impeachment |
| IRE 701-704 | Lay and expert opinion |
| IRE 801 | Hearsay definitions |
| IRE 803 | Hearsay exceptions (always admissible) |
| IRE 803(6) | Business records exception |
| IRE 803(8) | Public records exception |
| IRE 804 | Hearsay exceptions (declarant unavailable) |
| IRE 901 | Authentication |
| IRE 902 | Self-authentication |
| IRE 902(11) | Self-authentication of business records |
| IRE 1002 | Best evidence rule |
| IRE 1006 | Summary of voluminous records |

## Indiana Code — chapters relevant to civil practice

### Title 33 — Courts and Judicial Procedure

- **IC 33-28** — Circuit Courts
- **IC 33-29** — Superior Courts; small-claims dockets
- **IC 33-34** — Marion County Small Claims Courts
- **IC 33-37** — Filing fees and court costs (IC 33-37-4-4 is the
  primary civil-fee schedule)
- **IC 33-37-3** — Indigent filing (CCS Form 1042 affidavit)

### Title 34 — Civil Procedure

- **IC 34-11** — Statutes of limitations
  - IC 34-11-2-7 — open accounts (6 years)
  - IC 34-11-2-9 — written contracts for property (10 years)
  - IC 34-11-2-11 — written contract for money signed by party
    charged (6 years)
  - IC 34-11-2-13 — promissory notes (6 years)
- **IC 34-26-5** — Civil protective orders
- **IC 34-37-2** — Oaths and affirmations
- **IC 34-52** — Costs and attorney fees
- **IC 34-55-10-2** — Homestead exemption ($22,750 individual /
  $45,500 joint)
- **IC 34-55-10-3** — Other property exemptions

### Title 24 — Trade Regulation (consumer law)

- **IC 24-4.5** — Indiana Uniform Consumer Credit Code (IUCCC)
  - IC 24-4.5-3 — Consumer loans
  - IC 24-4.5-5-101 et seq. — Remedies and penalties
  - IC 24-4.5-5-105 — Wage garnishment cap
- **IC 24-5-0.5** — Deceptive Consumer Sales Act (DCSA) —
  treble-damages UTPA analog
- **IC 24-5-15** — Credit Services Organizations Act

### Title 26 — Commercial Law

- **IC 26-1-1** — UCC Article 1 (General Provisions)
- **IC 26-1-2** — UCC Article 2 (Sales)
- **IC 26-1-3.1** — UCC Article 3 (Negotiable Instruments — 1991
  revision adopted by Indiana)
- **IC 26-1-9.1** — UCC Article 9 (Secured Transactions — 2001
  revision adopted by Indiana)

### Title 1 — General Provisions

- **IC 1-1-9-1** — Legal holidays

## Indiana legal holidays (IC 1-1-9-1)

The statewide legal holidays per IC 1-1-9-1:

- New Year's Day (January 1)
- MLK Day (3rd Monday of January)
- Lincoln's Birthday (February 12) — observed but offices remain
  open
- Washington's Birthday / Presidents' Day (3rd Monday of February)
- **Good Friday** — Indiana-specific (most states don't observe)
- **Primary Election Day** (1st Tuesday after 1st Monday in May
  in even-numbered years) — Indiana-specific
- Memorial Day (last Monday of May)
- Independence Day (July 4)
- Labor Day (1st Monday of September)
- Columbus Day (2nd Monday of October) — formally observed
- **General Election Day** (1st Tuesday after 1st Monday in
  November in even-numbered years) — Indiana-specific
- Veterans Day (November 11)
- Thanksgiving (4th Thursday of November)
- Day after Thanksgiving — by Governor's proclamation most years
- Christmas (December 25)

For T.R. 6 deadline math, the courts treat all IC 1-1-9-1
holidays as non-judicial days. The plugin's `case-calendar.py`
script encodes these rules.

## Citation format — Indiana Supreme Court Rule on Citation

The Indiana Supreme Court's Rule on Citation is part of the
Indiana Rules of Admission, Discipline, and Citation. Highlights:

- **Cases**: *Smith v. Jones*, 123 N.E.3d 456 (Ind. 2023)
  (Supreme); *Smith v. Jones*, 123 N.E.3d 456 (Ind. Ct. App.
  2023) (Court of Appeals)
- **Reporters**: N.E.3d (current); N.E.2d (1936-2003); N.E.
  (pre-1936); Ind. Reporter (pre-1981, in parallel with N.E.)
- **Trial Rules**: Ind. Trial R. 56(C) or T.R. 56(C)
- **Evidence Rules**: Ind. Evid. R. 803(6) or IRE 803(6)
- **Statutes**: IC 34-11-2-9 (no "§" required; "IC § 34-11-2-9"
  also accepted)
- **Constitution**: Ind. Const. art. 1, § 12
- **Local Rules**: LR49-TR5-203 (Marion, Format of Documents)
- **Federal**: 15 U.S.C. § 1692k; 12 C.F.R. § 1006.30

## Filing fees (IC 33-37-4-4)

The statewide civil filing-fee schedule (as of 2024 indexing):

| Case Type | Base Fee | Total (with county costs) |
|-----------|----------|---------------------------|
| Civil Plenary (PL) | $157 | $177 |
| Civil Tort (CT) | $157 | $177 |
| Civil Collection (CC) | $157 | $177 |
| Small Claims (SC, ≤ $1500) | $35 | $55 |
| Small Claims (SC, $1500-$10000) | $50 | $70 |
| Mortgage Foreclosure (MF) | $157 | $177 |
| Probate (EU / ES) | $157 | $177 |

Counties may add up to $20 in additional cost components under IC
33-37-5; consult the venue clerk's fee schedule for the exact
amount.

Indigent waivers under IC 33-37-3-2 (CCS Form 1042) cover the
entire fee, including Sheriff service ($30-50) and e-filing
transaction fee ($10-15).

## Reference corpora — shared across plugins

The federal-debt-laws corpus is shared across all state plugins
in this marketplace. For Indiana, it is available via the
`claude-legal-federal-laws` dependency plugin (declared in this
plugin's `plugin.json`). Sources:

- **FDCPA** — 15 U.S.C. §§ 1692-1692p; Reg F at 12 C.F.R. pt.
  1006
- **FCRA** — 15 U.S.C. §§ 1681-1681x; Reg V at 12 C.F.R. pt. 1022
- **TILA** — 15 U.S.C. §§ 1601-1667f; Reg Z at 12 C.F.R. pt. 1026
- **ECOA** — 15 U.S.C. §§ 1691-1691f; Reg B at 12 C.F.R. pt. 1002
- **UCC Model Articles** — 1, 2, 3, 9 (Cornell LII) — Indiana
  enacts these at IC 26-1-2, IC 26-1-3.1, IC 26-1-9.1

## In-corpus references

- `references/trial-rules-summary.md` — quick-look table of every
  Trial Rule
- `references/evidence-rules-summary.md` — quick-look table of
  every Evidence Rule
- `references/in-statutes-debt/` — populated by parallel agent;
  Indiana Code chapters relevant to consumer practice
- `references/court-rules/` — populated by parallel agent;
  verbatim text of Trial Rules, Evidence Rules, Appellate Rules,
  Small Claims Rules
- `references/online-sources.md` — agent-facing URL catalog
- `references/legal-data-apis.md` — structured API endpoints
  (iga.in.gov, courts.in.gov, etc.)

## Composition

Every other in-court-docs skill cites this reference catalog by
specific rule, statute, or case. Always cite the canonical source
from this catalog rather than restating from memory.

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against the most current Indiana Trial Rules, Indiana Code, and
case law before filing.
