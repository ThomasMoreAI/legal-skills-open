---
name: tn-law-references-codearranger
title: Tennessee Law References
description: 'Matter-neutral reference catalog for Tennessee civil practice. Contains Tenn. R. Civ. P. / Tenn. R. Evid. summaries, fees-and-costs framework, citation format (Tenn. Sup. Ct. R. 4 published/unpublished; Bluebook), court structure (Circuit, Chancery, General Sessions with its $25k cap + unlimited detainer jurisdiction; 10-day de novo appeal), and local-rules index. Emphasizes 803(6) business-records exception and 902 self- authentication (critical for debt matters). Hosts the reference corpora: verbatim court-rules (Tenn. R. Civ. P., Tenn. R. Evid., local rules), tn-statutes-debt (Tennessee Code chapters), federal-debt-laws (symlink), federal-bankruptcy (symlink), ucc-model (symlink). Other skills cite this one for rule numbers and case authorities.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Readme
  path: references/court-rules/README.md
- title: Tenn Local Rules Practice
  path: references/court-rules/Tenn-Local-Rules-Practice.md
- title: Tenn Rules Appellate Procedure
  path: references/court-rules/Tenn-Rules-Appellate-Procedure.md
- title: Tenn Rules Civil Procedure
  path: references/court-rules/Tenn-Rules-Civil-Procedure.md
- title: Tenn Rules Evidence
  path: references/court-rules/Tenn-Rules-Evidence.md
- title: Tenn Supreme Court Rules
  path: references/court-rules/Tenn-Supreme-Court-Rules.md
- title: Readme
  path: references/tn-statutes-debt/README.md
- title: Tenn Code T15 Ch1
  path: references/tn-statutes-debt/Tenn-Code-T15-Ch1.md
- title: Tenn Code T16 Ch15
  path: references/tn-statutes-debt/Tenn-Code-T16-Ch15.md
- title: Tenn Code T20 Ch12
  path: references/tn-statutes-debt/Tenn-Code-T20-Ch12.md
- title: Tenn Code T20 Ch16
  path: references/tn-statutes-debt/Tenn-Code-T20-Ch16.md
- title: Tenn Code T20 Ch6
  path: references/tn-statutes-debt/Tenn-Code-T20-Ch6.md
- title: Tenn Code T24 Ch5
  path: references/tn-statutes-debt/Tenn-Code-T24-Ch5.md
- title: Tenn Code T26 Ch2
  path: references/tn-statutes-debt/Tenn-Code-T26-Ch2.md
- title: Tenn Code T26 Ch3
  path: references/tn-statutes-debt/Tenn-Code-T26-Ch3.md
- title: Tenn Code T27 Ch5
  path: references/tn-statutes-debt/Tenn-Code-T27-Ch5.md
- title: Tenn Code T28 Ch3
  path: references/tn-statutes-debt/Tenn-Code-T28-Ch3.md
- title: Tenn Code T29 Ch18
  path: references/tn-statutes-debt/Tenn-Code-T29-Ch18.md
- title: Tenn Code T29 Ch20
  path: references/tn-statutes-debt/Tenn-Code-T29-Ch20.md
- title: Tenn Code T29 Ch26
  path: references/tn-statutes-debt/Tenn-Code-T29-Ch26.md
- title: Tenn Code T36 Ch3
  path: references/tn-statutes-debt/Tenn-Code-T36-Ch3.md
- title: Tenn Code T36 Ch4
  path: references/tn-statutes-debt/Tenn-Code-T36-Ch4.md
- title: Tenn Code T36 Ch5
  path: references/tn-statutes-debt/Tenn-Code-T36-Ch5.md
- title: Tenn Code T36 Ch6
  path: references/tn-statutes-debt/Tenn-Code-T36-Ch6.md
- title: Tenn Code T37 Ch1
  path: references/tn-statutes-debt/Tenn-Code-T37-Ch1.md
- title: Tenn Code T47 Ch11
  path: references/tn-statutes-debt/Tenn-Code-T47-Ch11.md
- title: Tenn Code T47 Ch14
  path: references/tn-statutes-debt/Tenn-Code-T47-Ch14.md
- title: Tenn Code T47 Ch18
  path: references/tn-statutes-debt/Tenn-Code-T47-Ch18.md
- title: Tenn Code T47 Ch2
  path: references/tn-statutes-debt/Tenn-Code-T47-Ch2.md
- title: Tenn Code T62 Ch20
  path: references/tn-statutes-debt/Tenn-Code-T62-Ch20.md
- title: Tenn Code T66 Ch28
  path: references/tn-statutes-debt/Tenn-Code-T66-Ch28.md
- title: Tenn Code T66 Ch7
  path: references/tn-statutes-debt/Tenn-Code-T66-Ch7.md
---

# Tennessee Law References

> **NOT LEGAL ADVICE.** Reference catalog only. Read the cited rule,
> statute, or case in full — and confirm it is current — before
> relying on it.

This is the **matter-neutral** reference index for Tennessee civil
practice. Other skills in the `tn-court-docs` plugin point here for
rule numbers, statute citations, and case authorities. This skill is
also the physical **host** of the plugin's reference corpora.

## What's here

```
references/
├── court-rules/            # Verbatim rule text (Tenn. R. Civ. P.,
│                           #   Tenn. R. Evid., local rules) — corpus
├── tn-statutes-debt/       # Tennessee Code Annotated chapters most
│                           #   relevant to civil practice — corpus
├── federal-debt-laws/      # FDCPA, FCRA, TILA, etc. (symlink into
│                           #   the shared claude-legal-federal-laws plugin)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink into shared plugin)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink into
                            #   shared plugin)
```

The three symlinked corpora (`federal-debt-laws/`,
`federal-bankruptcy/`, `ucc-model/`) point into the shared
`claude-legal-federal-laws` plugin so the federal text is stored once,
not copied per state. The Tennessee-specific corpora (`court-rules/`,
`tn-statutes-debt/`) live physically under this skill.

## Court structure — terminology

Tennessee trial courts and the vocabulary used across this plugin:

| Court | Jurisdiction |
|---|---|
| **Circuit Court** | General-jurisdiction court of **law** (torts, contracts, larger civil matters, divorce) |
| **Chancery Court** | General-jurisdiction court of **equity** (injunctions, specific performance, many divorces; the Clerk & Master is the equity clerk) |
| **General Sessions Court** | **Limited**-jurisdiction court; civil cap **$25,000** (Tenn. Code Ann. § 16-15-501), unlimited in forcible entry & detainer (eviction); informal practice — see below |

Tennessee has **95 counties** organized into roughly 31 judicial
districts. Flagship counties: **Davidson (Nashville) — 20th JD**,
**Shelby (Memphis) — 30th JD**, **Knox (Knoxville) — 6th JD**, and
**Hamilton (Chattanooga) — 11th JD**. Divorce jurisdiction lies in
both Circuit and Chancery; **Juvenile Courts** (Title 37) handle
parentage, custody/support of children of unmarried parents,
dependency & neglect, and termination of parental rights.

> **General Sessions is informal.** The Tenn. R. Civ. P. do **not**
> apply in General Sessions except where specifically made
> applicable, and there is **no formal discovery as of right**. A
> party dissatisfied with a General Sessions civil judgment may appeal
> **de novo to Circuit Court within 10 days** of entry (Tenn. Code
> Ann. § 27-5-108) — verify the current period.

## Tenn. R. Civ. P. — Tennessee Rules of Civil Procedure

The Tenn. R. Civ. P. (often "TRCP") govern civil actions in the
Circuit and Chancery Courts. Rules every Tennessee civil practitioner
uses:

| Rule | Subject |
|---|---|
| Tenn. R. Civ. P. 4 | Process — summons and service (90-day issuance / return) |
| Tenn. R. Civ. P. 5 | Service and filing of subsequent papers |
| Tenn. R. Civ. P. 6 | Time computation (6.01) and the 3-day mail add-on (6.05) |
| Tenn. R. Civ. P. 7 | Pleadings allowed; designation of parties |
| Tenn. R. Civ. P. 8 | General rules of pleading |
| Tenn. R. Civ. P. 10 | Form of pleadings (10.01 caption; 10.02 numbered paragraphs; 10.03 attach written instrument) |
| Tenn. R. Civ. P. 11 | Signing of pleadings and motions |
| Tenn. R. Civ. P. 12 | Defenses and objections (12.01 answer; 12.02 grounds, incl. 12.02(6) failure to state a claim) |
| Tenn. R. Civ. P. 13 | Counterclaim and cross-claim (compulsory vs. permissive) |
| Tenn. R. Civ. P. 15 | Amended and supplemental pleadings |
| Tenn. R. Civ. P. 26 | Discovery — scope and general provisions |
| Tenn. R. Civ. P. 30 / 31 | Depositions (oral / written questions) |
| Tenn. R. Civ. P. 33 | Interrogatories (no statewide numeric cap) |
| Tenn. R. Civ. P. 34 | Production of documents and things |
| Tenn. R. Civ. P. 36 | Requests for admission |
| Tenn. R. Civ. P. 37 | Failure to make discovery; motion to compel; sanctions |
| Tenn. R. Civ. P. 54 | Judgments; costs |
| Tenn. R. Civ. P. 55 | Default |
| Tenn. R. Civ. P. 56 | Summary judgment (56.04 — motion served at least 30 days before the hearing) |
| Tenn. R. Civ. P. 59 | Post-trial motions (59.04 motion to alter or amend; 30-day non-extendable window) |
| Tenn. R. Civ. P. 60 | Relief from judgment or order (60.02 grounds) |

Confirm current day counts and subsection lettering against the
verbatim text in `references/court-rules/` before relying on them.

## Tenn. R. Evid. — Tennessee Rules of Evidence

The Tenn. R. Evid. track the federal model closely. The two most
load-bearing rules for documentary civil practice (especially
debt-buyer and business-records matters):

- **Tenn. R. Evid. 803(6)** — the **business-records** hearsay
  exception. A record of a regularly conducted activity is admissible
  if a **custodian or other qualified witness** lays the foundation
  (made at or near the time by someone with knowledge, kept in the
  regular course, regular practice to keep it) — unless the source or
  circumstances indicate a lack of trustworthiness. A
  self-authenticating certification can substitute for live testimony.
- **Tenn. R. Evid. 902** — **self-authentication**. Certain records
  (certified copies of public records, and certified domestic business
  records) are self-authenticating, so no extrinsic foundation
  testimony is required. The exact subsection number of the certified
  business-records provision (the 902(11)-equivalent) is **not pulled
  verbatim here — verify the current subsection lettering** in
  `references/court-rules/` before citing it.

Other commonly cited rules: 401-403 (relevance), 404(b) (other acts),
408 (compromise offers), 602 (personal knowledge), 702-703 (experts),
801-807 (hearsay), 901 (authentication), 1001-1008 (best evidence).

## Fees and costs

Tennessee follows the **American rule** — each party bears its own
attorney's fees unless a statute, rule, or contract shifts them.
Authorities frequently invoked in civil practice:

- **Tenn. Code Ann. § 20-12-119(c)** — a party who prevails on a Tenn.
  R. Civ. P. **12.02(6)** (failure to state a claim) dismissal may
  recover costs and reasonable attorney's fees, **capped at $10,000**,
  from the non-prevailing party. A Tennessee-specific fee-shifting
  hook; see `tn-first-30-days`.
- **Tenn. Code Ann. § 47-18-109** — Tennessee Consumer Protection Act:
  discretionary attorney's fees, and treble damages for a willful or
  knowing violation.
- **15 U.S.C. § 1692k(a)(3)** — FDCPA attorney's fees to a prevailing
  consumer.
- **Contractual fee provisions** — enforceable per their terms; verify
  reasonableness.

Filing-fee schedules are set by statute and by the clerk of each
court; confirm the current amount with the clerk of the filing court.

## Citation format

Tennessee uses **standard Bluebook** citation; there is no mandatory
Tennessee-specific style manual.

- **Cases**: South Western Reporter — `S.W.`, `S.W.2d`, `S.W.3d`.
  - Tennessee Supreme Court: `Rye v. Women's Care Ctr. of Memphis, MPLLC, 477 S.W.3d 235 (Tenn. 2015)`
  - Court of Appeals: `Smith v. Jones, 123 S.W.3d 456 (Tenn. Ct. App. 2018)`
  - Court of Criminal Appeals: `State v. Doe, 234 S.W.3d 567 (Tenn. Crim. App. 2007)`
- **Statutes**: `Tenn. Code Ann. § 28-3-109` (or `T.C.A. § 28-3-109`).
- **Rules**: `Tenn. R. Civ. P. 56.04`; `Tenn. R. Evid. 803(6)`.
- **Publication / citability** — **Tenn. Sup. Ct. R. 4** governs.
  **Published** opinions are controlling authority; **unpublished**
  opinions are **persuasive** unless designated not-for-citation.
  Flag an opinion's published/unpublished status when citing it.
- **Federal**: `15 U.S.C. § 1692g(b)`; `12 C.F.R. § 1006.34`.

## Local rules — where they live

Tennessee has **no single statewide page-limit / margin / font rule**.
Document form is governed by **Tenn. R. Civ. P. 10** (caption,
numbered paragraphs, exhibits) and **Rule 11** (signature), plus
redaction of personal identifiers (verify the current electronic-filing
and redaction rule for the venue). Page limits, typography,
chambers-copy requirements, and motion-day mechanics are set by
**per-county LOCAL RULES**.

- Local rules are indexed on the AOC **"Local Rules of Practice"**
  page at **tncourts.gov**.
- E-filing is **county-by-county** with no universal mandate: Davidson
  Chancery uses Odyssey / eFileTN (Tyler); Shelby uses eFlex; other
  counties use Tybera (TnCIS) or paper. **Confirm the venue's platform
  and whether e-filing is mandatory** with the clerk before filing.

## Online sources

- **Tennessee Administrative Office of the Courts / Judicial Branch**:
  https://www.tncourts.gov (rules of court, local rules index, opinions)
- **Tenn. R. Civ. P. and Tenn. R. Evid.**: published at tncourts.gov
- **Tennessee Code Annotated**: via the Tennessee General Assembly at
  https://www.capitol.tn.gov (plus public / commercial mirrors)
- **Tennessee appellate opinions**: tncourts.gov opinions search and
  **CourtListener** (Tennessee Supreme Court, Court of Appeals, Court
  of Criminal Appeals)

See the `references/` corpora for verbatim rule and statute text.

## Composition

- Every other Tennessee skill cites this one for rule numbers, statute
  numbers, and case authorities.
- For the filing court's mechanics: `tn-davidson`, `tn-shelby`,
  `tn-knox`, `tn-hamilton`, `tn-county-courts`, `tn-general-sessions`.
- For matter-specific bundles: `tn-consumer-debt`, `tn-family-law`,
  `tn-landlord-tenant`, `tn-personal-injury`.
- For timing arithmetic: `tn-deadlines`.

## References

- `references/court-rules/` — verbatim Tenn. R. Civ. P. / Tenn. R.
  Evid. / local-rule corpus
- `references/tn-statutes-debt/` — Tennessee Code Annotated chapters
  most relevant to civil practice
- `references/federal-debt-laws/` — federal-law corpus (symlink)
- `references/federal-bankruptcy/` — Title 11 U.S.C. corpus (symlink)
- `references/ucc-model/` — Model UCC text (symlink)
