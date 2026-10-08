---
name: az-law-references-codearranger
title: Arizona Law References
description: 'Matter-neutral reference catalog for Arizona civil practice. Contains Ariz. R. Civ. P. maps (pleadings, mandatory initial disclosure Rule 26.1, tiered-case discovery Rule 26.2 Tier 1/2/3, interrogatories, production, admissions, depositions, summary judgment, default, judgments, relief, compulsory arbitration); separate ARFLP (Arizona Rules of Family Law Procedure); Ariz. R. Evid. including business-records (Rule 803(6)), self-authentication (Rule 902(11)), Daubert adoption (Rule 702); fees-and-costs framework; Bluebook citation conventions; landmark precedents; online-sources/data-API catalog. Triggers: "Arizona civil rule", "Ariz. R. Civ. P.", "Rule 26.1", "Rule 26.2", "tiered discovery", "Arizona summary judgment", "compulsory arbitration", "Arizona evidence rule", "Ariz. R. Evid.", "ARFLP", "A.R.S. § ...", "Arizona citation format", "look up Arizona law on X". Host skill for reference corpora.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-law-references
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Readme
  path: references/az-statutes-debt/README.md
- title: Title12 Limitations
  path: references/az-statutes-debt/Title12-limitations.md
- title: Title12 Procedure Fees
  path: references/az-statutes-debt/Title12-procedure-fees.md
- title: Commercial
  path: references/az-statutes-debt/commercial.md
- title: Comparative Fault
  path: references/az-statutes-debt/comparative-fault.md
- title: Consumer Fraud Collection
  path: references/az-statutes-debt/consumer-fraud-collection.md
- title: Employment
  path: references/az-statutes-debt/employment.md
- title: Exemptions
  path: references/az-statutes-debt/exemptions.md
- title: Family Title25
  path: references/az-statutes-debt/family-Title25.md
- title: Garnishment Execution
  path: references/az-statutes-debt/garnishment-execution.md
- title: Holidays
  path: references/az-statutes-debt/holidays.md
- title: Justice Court
  path: references/az-statutes-debt/justice-court.md
- title: Landlord Tenant
  path: references/az-statutes-debt/landlord-tenant.md
- title: Citation Format
  path: references/citation-format.md
- title: Civil Rules
  path: references/civil-rules.md
- title: Arcp Civil Procedure
  path: references/court-rules/ARCP-civil-procedure.md
- title: Arflp Family Law Procedure
  path: references/court-rules/ARFLP-family-law-procedure.md
- title: Ariz R Evid Evidence
  path: references/court-rules/Ariz-R-Evid-evidence.md
- title: Jcrcp Justice Court
  path: references/court-rules/JCRCP-justice-court.md
- title: Readme
  path: references/court-rules/README.md
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
---

# Arizona Law References

> **NOT LEGAL ADVICE.** Reference catalog only. Read the cited rule,
> statute, or case in full — and confirm it is current — before relying
> on it.

This is the **matter-neutral** reference index for Arizona civil
practice. Other skills in the `az-court-docs` plugin point here for rule
numbers, statute citations, and case authorities. This skill is also the
physical **host** of the plugin's reference corpora.

## What's here

```
references/
├── civil-rules.md          # Ariz. R. Civ. P. map (pleadings, disclosure, tiered discovery, SJ, arbitration)
├── evidence-rules.md       # Ariz. R. Evid. map (relevance, hearsay, authentication, experts, privileges)
├── family-rules.md         # Arizona Rules of Family Law Procedure (ARFLP) — SEPARATE rule set for Title 25
├── fees-and-costs.md       # Filing fees + cost / fee-shifting framework
├── citation-format.md      # Bluebook-based Arizona citation conventions
├── key-cases.md            # Landmark Arizona civil + family precedents
├── online-sources.md       # Canonical human-facing URLs
├── legal-data-apis.md      # Programmatic access (azleg.gov, azcourts.gov, CourtListener)
├── court-rules/            # Verbatim Ariz. R. Civ. P. / Ariz. R. Evid. / ARFLP / local-rule text — corpus
├── az-statutes-debt/       # Arizona Revised Statutes chapters for civil practice — corpus
├── federal-debt-laws/      # FDCPA, FCRA, TILA, etc. (symlink into the
│                           #   shared claude-legal-federal-laws plugin)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink into shared plugin)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink into shared plugin)
```

The three symlinked corpora (`federal-debt-laws/`, `federal-bankruptcy/`,
`ucc-model/`) point into the shared `claude-legal-federal-laws` plugin so
the federal text is stored once, not copied per state. The Arizona-
specific corpora (`court-rules/`, `az-statutes-debt/`) and the eight
curated `*.md` index files live physically under this skill.

## Two rule sets — civil vs. family

> **Arizona runs two separate sets of trial-court procedural rules.**
> General civil cases are governed by the **Arizona Rules of Civil
> Procedure (Ariz. R. Civ. P.)**. **Title 25 family-law cases**
> (dissolution, legal separation, paternity, legal decision-making /
> custody, parenting time, child support, spousal maintenance) are
> governed by the **Arizona Rules of Family Law Procedure (ARFLP)** — a
> distinct rule set with its own numbering, its own disclosure rule
> (ARFLP Rule 49), and family-specific procedures (resolution management
> conferences, parenting conferences, ADR). Do not cite a civil rule
> number in a family matter or vice versa. The civil-rules map is in
> `references/civil-rules.md`; the family-rules map is in
> `references/family-rules.md`.

## Court structure — terminology

Arizona trial courts and the vocabulary used across this plugin:

| Court | Jurisdiction |
|---|---|
| **Superior Court** | General-jurisdiction trial court; one in each of Arizona's 15 counties. Hears civil claims above the justice-court ceiling, family-law (Title 25) matters, probate, and appeals from the limited-jurisdiction courts. Governed by the Ariz. R. Civ. P. (civil) and the ARFLP (family). |
| **Justice Court** | Limited-jurisdiction court (justice of the peace); civil money claims up to the statutory ceiling, eviction (forcible / special detainer) actions, and small claims. Confirm the current civil jurisdictional ceiling in `references/az-statutes-debt/`. |
| **Small Claims Division** | Informal division of the Justice Court for low-dollar claims; relaxed procedure with limited or no appeal — confirm the current ceiling and appeal rules. |
| **Municipal (City) Court** | Limited-jurisdiction court for city ordinance and criminal / traffic matters; generally not a civil money-damages forum. |

Arizona has **15 counties**. The appellate courts are the **Arizona Court
of Appeals** (intermediate; **Division One** in Phoenix and **Division
Two** in Tucson) and the **Arizona Supreme Court** (court of last resort).

## Arizona Rules of Civil Procedure (Ariz. R. Civ. P.)

The full civil-practice map lives in `references/civil-rules.md`. The
load-bearing features for this plugin:

- **Pleadings — Rules 7-15.** Forms of pleadings and motions, the
  complaint and answer, defenses including the **Rule 12(b)(6)** motion to
  dismiss for failure to state a claim, counterclaims and cross-claims,
  and amendment under Rule 15.
- **Mandatory initial disclosure — Rule 26.1.** Arizona requires broad,
  automatic disclosure of witnesses, documents, the factual and legal
  bases of claims and defenses, and the computation of damages **without
  waiting for a discovery request**. This is a distinctive Arizona
  feature; treat it as the spine of Arizona discovery.
- **Tiered-case discovery — Rule 26.2.** Cases are assigned to **Tier 1,
  Tier 2, or Tier 3** based primarily on the amount in controversy, and
  each tier carries its own caps on deposition hours, interrogatories,
  requests for production, requests for admission, and the discovery
  period. Tier assignment can be adjusted for proportionality. The current
  dollar thresholds and per-tier limits are in `references/civil-rules.md`
  (stated with "verify current") and in the verbatim rule under
  `references/court-rules/`.
- **Interrogatories — Rule 33** (a general 40-interrogatory ceiling, but
  the operative cap in a given case is usually the Rule 26.2 tier limit —
  confirm which controls); **production — Rule 34**; **admissions — Rule
  36**; **depositions — Rule 30.**
- **Summary judgment — Rule 56.** Arizona's analog to FRCP 56; the
  governing standard was set in *Orme School v. Reeves* (see
  `references/key-cases.md`).
- **Default — Rule 55** (entry of default and default judgment).
- **Judgments — Rules 54 and 58** (form, entry, and the Rule 54(b) / (c)
  finality provisions).
- **New trial — Rule 59; relief from judgment — Rule 60.**
- **Compulsory arbitration — Rules 72-77.** Civil cases at or under the
  county's arbitration jurisdictional limit are routed to mandatory,
  non-binding arbitration, with a right to appeal for a trial de novo. The
  dollar limit is **set by each county by local rule** — confirm the
  current figure for the filing county.

Confirm current subrule lettering, day counts, dollar ceilings, and tier
thresholds against the verbatim text in `references/court-rules/` and the
statutes in `references/az-statutes-debt/` before relying on them.

## Arizona Rules of Evidence (Ariz. R. Evid.)

The evidence map lives in `references/evidence-rules.md`. The two most
load-bearing rules for documentary civil practice (especially debt-buyer
and business-records matters):

- **Rule 803(6)** — the **business-records** hearsay exception. A record
  of a regularly conducted activity is admissible if a custodian or other
  qualified witness (or a self-authenticating certification under Rule
  902(11)) lays the foundation that it was made at or near the time by
  someone with knowledge, kept in the regular course of business, and that
  keeping it was a regular practice — unless the source or circumstances
  indicate a lack of trustworthiness.
- **Rule 902(11)** — **self-authentication** of certified domestic records
  of a regularly conducted activity, so no live foundation witness is
  required where the certification and advance-notice requirements are
  met.

Other commonly cited rules: **401-403** (relevance; probative value vs.
unfair prejudice), **702** (expert testimony — Arizona **adopted the
*Daubert* reliability standard by rule effective January 1, 2012**),
**801-807** (hearsay), **901-902** (authentication), and the privilege
rules. See `references/evidence-rules.md`.

## Fees and costs

The fees-and-costs framework lives in `references/fees-and-costs.md`.
Arizona generally follows the **American rule** — each party bears its own
attorney's fees unless a statute, rule, or contract shifts them. Key
hooks:

- **A.R.S. § 12-341** — taxable **costs to the prevailing party** (as of
  right).
- **A.R.S. § 12-341.01** — **discretionary attorney's fees in contested
  contract actions.** This is the central fee-shifting statute in
  consumer-debt and contract litigation; the award is discretionary and is
  capped at the reasonable fees actually paid or owed. Confirm the current
  text.
- **Rule 68** (Ariz. R. Civ. P.) — **offer of judgment** with sanctions
  against a party that rejects an offer and fails to obtain a more
  favorable result. The ARFLP has its own analog for family cases —
  confirm.
- **A.R.S. § 12-302** — **deferral or waiver of court fees and costs** for
  parties unable to pay; the court may defer, waive, or set a payment
  schedule.

Confirm current dollar amounts (filing fees, ceilings) with the clerk of
the filing court and against `references/az-statutes-debt/`.

## Citation format

Arizona uses **Bluebook-based** citation. Details and examples are in
`references/citation-format.md`. Highlights:

- **Cases**: parallel cite to the official **Arizona Reports** and the
  regional **Pacific Reporter** — e.g.,
  `State v. X, 123 Ariz. 456, 789 P.2d 12 (1990)`. Court of Appeals
  opinions carry **`Ariz. App.`** and a `P.2d` / `P.3d` parallel cite.
  Italicize case names; place the year in parentheses.
- **Statutes**: `A.R.S. § 12-541` (Arizona Revised Statutes; section
  symbol).
- **Rules**: `Ariz. R. Civ. P. 56`; `Ariz. R. Evid. 803(6)`; `ARFLP 49`.

## Local rules — where they live

Statewide civil format follows the Ariz. R. Civ. P.; family format the
ARFLP. Individual Superior Courts adopt **local rules** for venue-specific
mechanics (motion scheduling, courtesy copies, civil cover sheets).
E-filing is via **AZTurboCourt** and county e-filing systems; electronic
filing is mandatory in a growing set of courts — confirm whether e-filing
is required in the venue. See `references/online-sources.md` for the rules
and self-service portals.

## Online sources and data APIs

- Human-facing canonical URLs (azcourts.gov for the rules, self-service
  center, and AZTurboCourt; azleg.gov for the A.R.S.; the Arizona
  appellate opinions site): see `references/online-sources.md`.
- Programmatic access (azleg.gov ARS pages, azcourts.gov rules,
  CourtListener Arizona Supreme Court + Court of Appeals, the connected
  CourtListener MCP): see `references/legal-data-apis.md`.

## Composition

- Every other Arizona skill cites this one for rule numbers, statute
  numbers, and case authorities.
- For statewide document format: `az-statewide-format`.
- For the filing court's mechanics: the county / venue skills.
- For pro se conventions: `az-pro-se`.
- For matter-specific bundles: `az-consumer-debt` and the family-law
  bundle.

## References

- `references/civil-rules.md` — Ariz. R. Civ. P. civil-practice map
- `references/evidence-rules.md` — Ariz. R. Evid. map
- `references/family-rules.md` — Arizona Rules of Family Law Procedure (ARFLP) map
- `references/fees-and-costs.md` — fees and cost / fee-shifting framework
- `references/citation-format.md` — Bluebook-based Arizona citation conventions
- `references/key-cases.md` — landmark Arizona civil + family precedents
- `references/online-sources.md` — canonical human-facing URLs
- `references/legal-data-apis.md` — programmatic access index
- `references/court-rules/` — verbatim Ariz. R. Civ. P. / Ariz. R. Evid. / ARFLP / local-rule corpus
- `references/az-statutes-debt/` — Arizona Revised Statutes chapters for civil practice
- `references/federal-debt-laws/` — federal-law corpus (symlink)
- `references/federal-bankruptcy/` — Title 11 U.S.C. corpus (symlink)
- `references/ucc-model/` — Model UCC text (symlink)
