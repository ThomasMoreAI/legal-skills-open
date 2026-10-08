---
name: tx-law-references-codearranger
title: Texas Law References
description: 'Matter-neutral reference catalog for Texas civil practice. Maps the Texas Rules of Civil Procedure (TRCP — pleadings 45/47/57, citation & answer 99 with the "Monday rule," special exceptions 91, Rule 91a dismissal, verified pleas 92/93, sworn account 185, summary judgment 166a incl. no-evidence 166a(i), expedited actions 169, discovery control plans 190 + 194–199/215, time computation Rule 4, new trial 329b, Justice Court Part V Rules 500–510); the Texas Rules of Evidence (business records 803(6), business-records affidavit 902(10)); the Texas Family Code framework (family cases use the TRCP, not a separate rule set); fees-and-costs (CPRC Ch. 38, Ch. 37 UDJA, sanctions); Texas Rules of Form ("Greenbook") citation; and the online-sources / data-API catalog. Triggers: "Texas civil rule", "TRCP", "Texas summary judgment", "no-evidence motion", "Monday rule answer deadline", "sworn account", "Tex. R. Evid.", "Texas Family Code section", "Texas citation format". Host skill for the
  Texas reference corpora.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Citation Format
  path: references/citation-format.md
- title: Civil Rules
  path: references/civil-rules.md
- title: Readme
  path: references/court-rules/README.md
- title: Trap Appellate
  path: references/court-rules/TRAP-appellate.md
- title: Trcp Civil Procedure
  path: references/court-rules/TRCP-civil-procedure.md
- title: Trcp Justice Court
  path: references/court-rules/TRCP-justice-court.md
- title: Tre Evidence
  path: references/court-rules/TRE-evidence.md
- title: Evidence Rules
  path: references/evidence-rules.md
- title: Family Rules
  path: references/family-rules.md
- title: Fees And Costs
  path: references/fees-and-costs.md
- title: Key Cases
  path: references/key-cases.md
- title: Legal Data Apis
  path: references/legal-data-apis.md
- title: Online Sources
  path: references/online-sources.md
- title: Cprc Fees Costs Judgments
  path: references/tx-statutes-debt/CPRC-fees-costs-judgments.md
- title: Cprc Limitations
  path: references/tx-statutes-debt/CPRC-limitations.md
- title: Cprc Proportionate Responsibility
  path: references/tx-statutes-debt/CPRC-proportionate-responsibility.md
- title: Readme
  path: references/tx-statutes-debt/README.md
- title: Dtpa Bus Com
  path: references/tx-statutes-debt/dtpa-bus-com.md
- title: Family Code
  path: references/tx-statutes-debt/family-code.md
- title: Finance Code Debt Collection
  path: references/tx-statutes-debt/finance-code-debt-collection.md
- title: Holidays Courts Govt Code
  path: references/tx-statutes-debt/holidays-courts-govt-code.md
- title: Property Exemptions Eviction
  path: references/tx-statutes-debt/property-exemptions-eviction.md
- title: Ucc Article9 Bus Com
  path: references/tx-statutes-debt/ucc-article9-bus-com.md
---

# Texas Law References

> **NOT LEGAL ADVICE.** Reference catalog only. Read the cited rule,
> statute, or case in full — and confirm it is current — before relying
> on it.

This is the **matter-neutral** reference index for Texas civil practice.
Other skills in the `tx-court-docs` plugin point here for rule numbers,
statute citations, and case authorities. This skill is also the physical
**host** of the plugin's reference corpora.

## What's here

```
references/
├── civil-rules.md          # TRCP map (form/pleadings, citation & answer, SJ, discovery, JP Part V)
├── evidence-rules.md       # Tex. R. Evid. map (relevance, hearsay, business records, authentication)
├── family-rules.md         # Texas family procedure (uses the TRCP) + Family Code anchors
├── fees-and-costs.md        # Filing fees + cost / fee-shifting / sanctions framework
├── citation-format.md      # Texas Rules of Form (Greenbook): S.W. reporter + petition-history
├── key-cases.md            # Landmark Texas civil + family + consumer precedents
├── online-sources.md       # Canonical human-facing URLs
├── legal-data-apis.md      # Programmatic access (statutes.capitol.texas.gov, txcourts.gov, CourtListener)
├── court-rules/            # Verbatim TRCP / Tex. R. Evid. rule text — corpus
├── tx-statutes-debt/       # Verbatim Texas statute sections for civil practice — corpus
├── federal-debt-laws/      # FDCPA, FCRA, TILA, etc. (symlink into the
│                           #   shared claude-legal-federal-laws plugin)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink into shared plugin)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink into shared plugin)
```

The three symlinked corpora (`federal-debt-laws/`, `federal-bankruptcy/`,
`ucc-model/`) point into the shared `claude-legal-federal-laws` plugin so
the federal text is stored once, not copied per state. The Texas-specific
corpora (`court-rules/`, `tx-statutes-debt/`) and the eight curated `*.md`
index files live physically under this skill.

## One civil-procedure rule set — including family cases

> **Texas does not have a separate family-procedure rule set.** General
> civil cases AND family-law cases (divorce, suits affecting the
> parent-child relationship) are both governed by the **Texas Rules of Civil
> Procedure (TRCP)**. There is no Texas analog to a stand-alone
> "family rules" code: family **procedure** runs on the TRCP, while the
> family **substantive** law lives in the **Texas Family Code**. Use
> "Petitioner/Respondent" for the parties in a family matter and
> "Plaintiff/Defendant" in general civil. The civil-rules map is in
> `references/civil-rules.md`; the family-specific procedural anchors and the
> Family Code map are in `references/family-rules.md`.

## Court structure — terminology

Texas trial and appellate courts and the vocabulary used across this plugin:

| Court | Jurisdiction |
|---|---|
| **District Court** | General-jurisdiction trial court (no upper civil jurisdictional limit); hears larger civil disputes, title to land, divorce and SAPCR (family), and felonies. Numbered and named by the county they sit in (e.g., "234th Judicial District Court of Harris County, Texas"). Some populous counties designate **family district courts**. Governed by the TRCP. |
| **County Court at Law (statutory county court)** | Mid-tier civil jurisdiction, probate (in many counties), and **de novo appeals from Justice Courts**. Civil jurisdictional caps are statutory (Gov't Code ch. 25) and drift-prone — confirm against the corpus. |
| **Constitutional County Court** | The county judge's court; limited civil and probate jurisdiction (Gov't Code ch. 26). Confirm the current amount-in-controversy limits against the corpus. |
| **Justice Court (Justice of the Peace / "JP court")** | Governed by **TRCP Part V, Rules 500–510**. Hears small-claims and debt-claim cases up to a statutory ceiling, **eviction (forcible entry & detainer)** under TRCP 510, and repair-and-remedy. Each county is divided into **JP precincts** (sometimes Place 1 / Place 2). Appeals go **de novo to the county court** (TRCP 506). **TRCP 500.3(e): the other rules of civil procedure and the rules of evidence do NOT apply in JP court** except where Part V incorporates them. |
| **Courts of Appeals** | The intermediate appellate courts, organized by district; hear civil and criminal appeals from the trial courts. |
| **Supreme Court of Texas** | The **civil** court of last resort. |
| **Court of Criminal Appeals** | The **criminal** court of last resort. Texas has **two** courts of last resort. |

## Texas Rules of Civil Procedure (TRCP)

The full civil-practice map lives in `references/civil-rules.md`. The
load-bearing features for this plugin:

- **Form of pleadings — Rules 45 & 47.** Plain statement of the cause of
  action; no technical forms. **Rule 47(c)** requires a **statement of the
  range of relief sought** (a Texas pleading requirement) — failure to plead
  the 47(c) range can bar a default judgment.
- **Signing — Rule 57.** Signature block with the signer's **State Bar of
  Texas bar number**, address, phone, email, and fax (a self-represented
  party signs and gives a mailing address).
- **Citation and answer — Rule 99 (the "Monday rule").** A defendant's answer
  is due **"by 10:00 a.m. on the Monday next after the expiration of twenty
  days after the date of service."** This is **not** a flat 20-day count —
  flag the Monday rule whenever computing a district- or county-court answer
  deadline. (Justice-court answer timing is different — see TRCP 502.5 in
  `civil-rules.md`.)
- **Time computation — Rule 4.** Exclude the first day, include the last; if
  the last day is a Saturday, Sunday, or **legal holiday**, the period runs
  to the next day that is not. Legal holidays are enumerated in **Tex. Gov't
  Code § 662.003** (see `tx-statutes-debt/`).
- **Special exceptions — Rule 91.** The Texas vehicle to challenge defects or
  vagueness in a pleading; **there is no general demurrer in Texas**.
- **Rule 91a — dismissal of a baseless cause of action.** Motion to dismiss a
  cause of action that **has no basis in law or fact** (the Texas analog to a
  12(b)(6) motion); filed within **60 days** of the first pleading asserting
  the challenged claim. The 91a fee rule was changed by 2019 legislation —
  confirm the current fee-shifting text in `court-rules/`.
- **Verified pleadings — Rules 92 & 93.** **Rule 92** is the general denial;
  **Rule 93** lists the matters that must be denied **under oath / by verified
  pleading** (e.g., lack of capacity, defect of parties, and — critically —
  **denial of a sworn account under Rule 185**).
- **Suit on a sworn account — Rule 185.** A properly verified account is
  prima facie proof of the debt **unless** the defendant files a **sworn
  denial** (TRCP 93(10) / 185). The verified denial is mandatory to put the
  account in issue.
- **Summary judgment — Rule 166a.** Traditional **166a(c)** and the
  distinct **no-evidence motion 166a(i)** (a Texas signature device). The
  motion is served at least **21 days** before the hearing; the response is
  due **7 days** before the hearing. Confirm current day counts in the corpus.
- **Expedited actions — Rule 169** and **discovery control plans — Rule
  190.** Rule 190 sets **Level 1** (expedited / lower-dollar, tied to Rule
  169), **Level 2** (the default plan), and **Level 3** (a court-ordered
  tailored plan). Expedited actions under Rule 169 apply to claims at or below
  a statutory ceiling — confirm the current ceiling and discovery-period day
  counts in the corpus.
- **Discovery — Rules 194 (required disclosures), 196 (production), 197
  (interrogatories), 198 (requests for admission — deemed admitted if not
  answered), 199 (oral depositions), 215 (sanctions / motion to compel).**
  Responses are generally due in **30 days**; **Rule 193.7** makes produced
  documents self-authenticating unless timely objected to (useful in debt
  cases). Confirm the interrogatory cap and the +3-days nuances in the corpus.
- **New trial — Rule 329b.** A motion for new trial is due **30 days after
  the judgment is signed**; the court's **plenary power** runs 30 days,
  extended by timely post-judgment motions.
- **Justice Court — Part V, Rules 500–510.** Commencement (502),
  answer & default (502.5 / 503), appeal de novo to county court (506), debt
  claim cases (508), and eviction / forcible detainer (510). **Rule 500.3(e)**
  is the key quirk: the regular rules of civil procedure and evidence do not
  apply in JP court except as Part V incorporates them.

Confirm current subrule lettering, day counts, and dollar ceilings against
the verbatim text in `references/court-rules/` (and the canonical txcourts.gov
URLs) before relying on them.

## Texas Rules of Evidence (Tex. R. Evid.)

The evidence map lives in `references/evidence-rules.md`. The two most
load-bearing rules for documentary civil practice (especially debt-buyer and
business-records matters):

- **Rule 803(6)** — the **business-records** hearsay exception. A record of a
  regularly conducted activity is admissible where a custodian or other
  qualified witness (or a self-authenticating business-records affidavit under
  Rule 902(10)) lays the foundation that it was made at or near the time by
  someone with knowledge, kept in the regular course of business, and that
  keeping it was a regular practice — unless the source or circumstances
  indicate a lack of trustworthiness.
- **Rule 902(10)** — **self-authentication of business records by affidavit.**
  Texas-specific: 902(10) supplies the **affidavit form** and the pre-trial
  **filing and notice** mechanics, so no live custodian is required. This is
  the device debt buyers use; the classic defense is attacking the affiant's
  **basis of knowledge of the original creditor's records**.

Other commonly cited rules: relevance (401–403), hearsay (801–807), and
authentication (901–902). **Note: the rules of evidence generally do NOT
apply in Justice Court** (TRCP 500.3(e)). See `references/evidence-rules.md`.

## Texas family procedure — the TRCP, not a separate rule set

Family cases (divorce, SAPCR) are filed and litigated under the **TRCP**;
there is no separate family-procedure rule set. The **substantive** family
law is statutory in the **Texas Family Code**. The map lives in
`references/family-rules.md`. Anchors: divorce **Ch. 6** (no-fault
insupportability § 6.001, the **60-day waiting period** § 6.702, residency
§ 6.301), the **"just and right" division** of the community estate (**Ch.
7**) with the **community-property presumption** (**§ 3.003**),
conservatorship & possession (**Ch. 153**, incl. the **Standard Possession
Order**), child support (**Ch. 154**, percentage-of-net-resources model with
a drift-prone statutory cap — point to the corpus), **UCCJEA Ch. 152**,
**UIFSA Ch. 159**, and **Title 4 protective orders**. **SAPCR** = Suit
Affecting the Parent-Child Relationship; there is no separate family **trial
court** — these are heard in the District Courts (some counties designate
family district courts, with **associate judges** under Ch. 201). See
`references/family-rules.md` and `tx-statutes-debt/`.

## Fees and costs

The fees-and-costs framework lives in `references/fees-and-costs.md`. Texas
follows the **American rule** — each party bears its own attorney fees unless
a statute, rule, or contract shifts them. Key hooks:

- **CPRC Ch. 38** — attorney fees to a **prevailing party** on a claim for an
  oral or written contract (and sworn-account claims). **Amended in 2021** to
  expand the recoverable-from defendants beyond individuals/corporations to
  reach **LLCs and other organizations** — confirm the current text. This is a
  **two-way exposure** in contract/debt litigation.
- **CPRC Ch. 37 (UDJA)** — the Uniform Declaratory Judgments Act authorizes
  the court to award **reasonable and necessary attorney fees** as are
  equitable and just.
- **Sanctions** — **TRCP 13** (sanctions for groundless/bad-faith pleadings)
  and **CPRC Ch. 9 / Ch. 10** (sanctions for frivolous or improper pleadings
  and signed filings).
- **TRCP 91a fees** — fee-shifting tied to a Rule 91a dismissal motion
  (changed by 2019 legislation — confirm the current rule).
- **Filing fees** and the **Statement of Inability to Afford Payment of Court
  Costs** (the fee-waiver instrument that replaced the pauper's affidavit).

Do **not** embed dollar amounts here — confirm current figures with the clerk
of the filing court and against `references/tx-statutes-debt/`.

## Citation format — Texas Rules of Form ("Greenbook")

Texas uses the **Texas Rules of Form** (the "Greenbook," published by the
Texas Law Review Association). Texas abolished its official Texas Reports, so
cite the **South Western Reporter**. Details and examples are in
`references/citation-format.md`. Highlights:

- **Supreme Court of Texas**: `In re Columbia Med. Ctr., 290 S.W.3d 204 (Tex.
  2009)` — reporter `S.W.3d` (or `S.W.2d`), court designation `Tex.`
- **Court of Appeals**: include the **district** and the **petition-history
  parenthetical**: `Doe v. Roe, 123 S.W.3d 456 (Tex. App.—Dallas 2003, pet.
  denied)`. The **"pet. denied / pet. ref'd / no pet."** writ-or-petition
  history is a Texas signature.
- **Statutes**: `Tex. Civ. Prac. & Rem. Code § 16.004`; `Tex. Fam. Code
  § 154.125`; `Tex. Bus. & Com. Code § 17.50`.
- **Rules**: `Tex. R. Civ. P. 166a`; `Tex. R. Evid. 803(6)`.

## E-filing — eFileTexas (Odyssey File & Serve)

Texas e-files statewide through **eFileTexas.gov** (Tyler Technologies
Odyssey File & Serve), under **TRCP 21(f)** and the Supreme Court's e-filing
rules (with the Tex. R. Jud. Admin. 10 technology standards). E-filing is
**mandatory for attorneys** in civil cases in all courts; **self-represented
filers may e-file** (and are encouraged to). Justice courts also file through
eFileTexas. The assisted self-help front end is **TexasLawHelp.org**. See
`references/online-sources.md` for the portal.

## Online sources and data APIs

- Human-facing canonical URLs (statutes.capitol.texas.gov for the statutes,
  txcourts.gov for the rules and the Supreme Court, efiletexas.gov,
  TexasLawHelp.org, occc.texas.gov, the Secretary of State, county clerks):
  see `references/online-sources.md`.
- Programmatic access (statutes.capitol.texas.gov, txcourts.gov rule PDFs,
  CourtListener Texas courts, the bundled CourtListener + Legal Data Hunter
  MCP servers): see `references/legal-data-apis.md`.

## Composition

- Every other Texas skill cites this one for rule numbers, statute numbers,
  and case authorities.
- For statewide document format: `tx-statewide-format`.
- For the filing court's mechanics: the district / county / justice-court
  venue skills (`tx-hcdc`, `tx-dcdc`, `tx-county-courts`, `tx-justice-courts`,
  `tx-smith-county-jp`).
- For pro se conventions: `tx-pro-se`.
- For matter-specific bundles: `tx-consumer-debt` and the family-law bundle.

## References

- `references/civil-rules.md` — TRCP civil-practice map
- `references/evidence-rules.md` — Tex. R. Evid. map
- `references/family-rules.md` — Texas family procedure (TRCP) + Family Code map
- `references/fees-and-costs.md` — fees, costs, and sanctions framework
- `references/citation-format.md` — Texas Rules of Form (Greenbook) conventions
- `references/key-cases.md` — landmark Texas civil + family + consumer precedents
- `references/online-sources.md` — canonical human-facing URLs
- `references/legal-data-apis.md` — programmatic access index
- `references/court-rules/` — verbatim TRCP / Tex. R. Evid. text (bounded set)
- `references/tx-statutes-debt/` — verbatim Texas statute sections for civil practice (bounded set)
- `references/federal-debt-laws/` — federal-law corpus (symlink)
- `references/federal-bankruptcy/` — Title 11 U.S.C. corpus (symlink)
- `references/ucc-model/` — Model UCC text (symlink)
