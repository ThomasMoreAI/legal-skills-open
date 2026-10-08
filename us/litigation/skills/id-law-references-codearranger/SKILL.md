---
name: id-law-references-codearranger
title: Idaho Law References
description: 'Matter-neutral reference catalog for Idaho civil practice. Maps the Idaho R. Civ. P. (I.R.C.P. — form/caption Rule 2, pleadings Rule 10, signing Rule 11, time computation Rule 2.2 with Rule 6 RESERVED, service Rules 4/5, discovery Rules 30-37, summary judgment Rule 56, default Rule 55, new trial / reconsideration Rules 59 and 11.2, relief Rule 60, costs Rule 54(d)); the SEPARATE Idaho Rules of Family Law Procedure (I.R.F.L.P. — scope Rule 101, child support Rule 120, form Rule 208); the Idaho R. Evid. (I.R.E. — business records Rule 803(6), self-authentication Rule 902(11)); the fees-and-costs framework (I.R.C.P. 54(d); I.C. §§ 12-120, 12-121); Idaho-Reports + Pacific-Reporter citation conventions; and the online-sources / data-API catalog. Triggers: "Idaho civil rule", "I.R.C.P.", "Idaho summary judgment", "Idaho time computation", "I.R.E.", "I.R.F.L.P.", "Idaho Code section", "Idaho citation format", "look up Idaho law on X". Host skill for reference corpora.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-law-references
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
- title: Iar Appellate
  path: references/court-rules/IAR-appellate.md
- title: Ircp Civil Procedure
  path: references/court-rules/IRCP-civil-procedure.md
- title: Ire Evidence
  path: references/court-rules/IRE-evidence.md
- title: Irflp Family Law Procedure
  path: references/court-rules/IRFLP-family-law-procedure.md
- title: Readme
  path: references/court-rules/README.md
- title: Evidence Rules
  path: references/evidence-rules.md
- title: Family Rules
  path: references/family-rules.md
- title: Fees And Costs
  path: references/fees-and-costs.md
- title: Readme
  path: references/id-statutes-debt/README.md
- title: Title11 Exemptions Garnishment
  path: references/id-statutes-debt/Title11-exemptions-garnishment.md
- title: Title5 Limitations
  path: references/id-statutes-debt/Title5-limitations.md
- title: Attorney Fees Costs Title12
  path: references/id-statutes-debt/attorney-fees-costs-Title12.md
- title: Consumer Protection Collection
  path: references/id-statutes-debt/consumer-protection-collection.md
- title: Family Title32
  path: references/id-statutes-debt/family-Title32.md
- title: Holidays Title73
  path: references/id-statutes-debt/holidays-Title73.md
- title: Homestead Title55
  path: references/id-statutes-debt/homestead-Title55.md
- title: Ucc Article9 Title28
  path: references/id-statutes-debt/ucc-article9-Title28.md
- title: Key Cases
  path: references/key-cases.md
- title: Legal Data Apis
  path: references/legal-data-apis.md
- title: Online Sources
  path: references/online-sources.md
---

# Idaho Law References

> **NOT LEGAL ADVICE.** Reference catalog only. Read the cited rule,
> statute, or case in full — and confirm it is current — before relying
> on it.

This is the **matter-neutral** reference index for Idaho civil practice.
Other skills in the `id-court-docs` plugin point here for rule numbers,
statute citations, and case authorities. This skill is also the physical
**host** of the plugin's reference corpora.

## What's here

```
references/
├── civil-rules.md          # I.R.C.P. map (form/caption, pleadings, time, discovery, SJ, costs)
├── evidence-rules.md       # I.R.E. map (relevance, hearsay, business records, authentication)
├── family-rules.md         # Idaho Rules of Family Law Procedure (I.R.F.L.P.) — SEPARATE rule set
├── fees-and-costs.md        # Filing fees + cost / fee-shifting framework
├── citation-format.md      # Idaho Reports + Pacific Reporter citation conventions
├── key-cases.md            # Landmark Idaho civil + family precedents
├── online-sources.md       # Canonical human-facing URLs
├── legal-data-apis.md      # Programmatic access (isc.idaho.gov, legislature.idaho.gov, CourtListener)
├── court-rules/            # Verbatim I.R.C.P./I.R.E./I.R.F.L.P./I.A.R. rule text — corpus
├── id-statutes-debt/       # Verbatim Idaho Code sections for civil practice — corpus
├── federal-debt-laws/      # FDCPA, FCRA, TILA, etc. (symlink into the
│                           #   shared claude-legal-federal-laws plugin)
├── federal-bankruptcy/     # Title 11 U.S.C. (symlink into shared plugin)
└── ucc-model/              # Model UCC Articles 1/2/3/9 (symlink into shared plugin)
```

The three symlinked corpora (`federal-debt-laws/`, `federal-bankruptcy/`,
`ucc-model/`) point into the shared `claude-legal-federal-laws` plugin so
the federal text is stored once, not copied per state. The Idaho-specific
corpora (`court-rules/`, `id-statutes-debt/`) and the eight curated `*.md`
index files live physically under this skill.

## Two rule sets — civil vs. family

> **Idaho runs two separate sets of trial-court procedural rules.**
> General civil cases are governed by the **Idaho Rules of Civil Procedure
> (I.R.C.P.)**. **Family-law cases** (annulment, divorce, legal separation,
> separate maintenance, child support, custody, grandparent visitation,
> paternity) are governed by the **Idaho Rules of Family Law Procedure
> (I.R.F.L.P.)** — a distinct rule set with its own numbering, its own
> form-of-documents rule (I.R.F.L.P. 208), and the Idaho Child Support
> Guidelines (I.R.F.L.P. 120). Family cases are heard in the **Magistrate
> Division** of the District Court. Do not cite a civil rule number in a
> family matter or vice versa. The civil-rules map is in
> `references/civil-rules.md`; the family-rules map is in
> `references/family-rules.md`.

## Court structure — terminology

Idaho trial courts and the vocabulary used across this plugin:

| Court | Jurisdiction |
|---|---|
| **District Court** | General-jurisdiction trial court within each of Idaho's seven judicial districts; hears civil claims above the small-claims/magistrate ceilings, felonies, and appeals from the Magistrate Division. Governed by the I.R.C.P. |
| **Magistrate Division** | Division of the District Court; hears family-law cases (under the I.R.F.L.P.), small claims, probate, misdemeanors, and lower-dollar civil matters. Confirm the current civil jurisdictional ceilings. |
| **Small Claims Department** | Informal department of the Magistrate Division for low-dollar claims; relaxed procedure, no attorneys, limited appeal. Confirm the current ceiling. |

Idaho's appellate courts are the **Idaho Court of Appeals** (intermediate)
and the **Idaho Supreme Court** (court of last resort). The Supreme Court
assigns cases to the Court of Appeals; the Supreme Court retains discretionary
review.

## Idaho Rules of Civil Procedure (I.R.C.P.)

The full civil-practice map lives in `references/civil-rules.md`. The
load-bearing features for this plugin:

- **Form and caption — I.R.C.P. 2.** Sets document format: 8½×11 white
  paper, font ≥ 11 point, double or 1.5 line spacing, margins ≥ 1.2" at top
  and sides and ≥ 1" at bottom, the title of court ≥ 3" from the top of page
  one, and the document title at the bottom of each page.
- **Form of pleadings — I.R.C.P. 10.** Captions, numbered paragraphs,
  exhibits.
- **Signing — I.R.C.P. 11.** Certification and sanctions; the attorney's
  **Idaho State Bar (ISB) number** appears in the signature block.
- **Time computation — I.R.C.P. 2.2 (NOTE: Rule 6 is RESERVED).** Idaho
  computes deadlines under **Rule 2.2**, not Rule 6 — Rule 6 is reserved.
  Add **3 days** when a period runs from service by mail.
- **Service — I.R.C.P. 4 (summons; serve within 182 days of filing) and 5
  (papers after the complaint).**
- **Answer — 21 days** after service (I.R.C.P. 12(a)(1)(A)).
- **Summary judgment — I.R.C.P. 56.** Motion must be filed at least **90
  days before trial**; the motion and supporting brief served at least **28
  days before the hearing**; the answering brief at least **14 days before**
  the hearing. See `references/civil-rules.md` for the full timing.
- **Discovery — Rules 30-37.** Interrogatory cap **40 including subparts**
  (Rule 33); production (34); admissions (36; deemed admitted if not
  answered); depositions (30); 30-day response window; motion to compel (37).
- **New trial / alter or amend — I.R.C.P. 59 (14 days); reconsideration —
  I.R.C.P. 11.2 (14 days); relief from judgment — I.R.C.P. 60(b); default —
  I.R.C.P. 55; memorandum of costs — I.R.C.P. 54(d) (14 days).**

Confirm current subrule lettering, day counts, and dollar ceilings against
the verbatim text in `references/court-rules/` (and the canonical
isc.idaho.gov URLs) before relying on them.

## Idaho Rules of Evidence (I.R.E.)

The evidence map lives in `references/evidence-rules.md`. The two most
load-bearing rules for documentary civil practice (especially debt-buyer
and business-records matters):

- **Rule 803(6)** — the **business-records** hearsay exception. A record of
  a regularly conducted activity is admissible where a custodian or other
  qualified witness (or a self-authenticating certification under Rule
  902(11)) lays the foundation that it was made at or near the time by
  someone with knowledge, kept in the regular course of business, and that
  keeping it was a regular practice — unless the source or circumstances
  indicate a lack of trustworthiness.
- **Rule 902(11)** — **self-authentication** of certified domestic records
  of a regularly conducted activity, so no live foundation witness is
  required where the custodian's certification and the advance-notice /
  inspection requirements are met.

Other commonly cited rules: relevance (401-403), hearsay (801-807), and
authentication (901-902). See `references/evidence-rules.md`.

## Idaho Rules of Family Law Procedure (I.R.F.L.P.)

Family cases use the **separate I.R.F.L.P.** rule set in the **Magistrate
Division**, not the I.R.C.P. The map lives in `references/family-rules.md`.
Anchors: scope (I.R.F.L.P. 101), the **Idaho Child Support Guidelines**
(I.R.F.L.P. 120, income-shares model), and form of documents (I.R.F.L.P.
208). Substantive family law is statutory in **Idaho Code Title 32**
(community property I.C. § 32-906; common-law marriage abolished after
January 1, 1996, I.C. § 32-201). See `references/id-statutes-debt/family-Title32.md`.

## Fees and costs

The fees-and-costs framework lives in `references/fees-and-costs.md`. Idaho
follows the **American rule** — each party bears its own attorney fees
unless a statute, rule, or contract shifts them. Key hooks:

- **I.R.C.P. 54(d)** — taxable **costs to the prevailing party**, claimed by
  a memorandum of costs filed within **14 days** of judgment.
- **I.C. § 12-120** — attorney fees to the prevailing party in certain
  actions, including **§ 12-120(3)** (commercial transactions) and
  **§ 12-120(1)** (claims at or below a stated small-claims dollar cap).
- **I.C. § 12-121** — discretionary attorney fees where a case was brought,
  pursued, or defended **frivolously**, unreasonably, or without foundation.
- **I.C. § 12-123** — sanctions for **frivolous conduct** in a civil action.

Filing fees are set by **I.C. § 31-3201**. Confirm current dollar amounts
with the clerk of the filing court and against `references/id-statutes-debt/`.

## Citation format

Idaho uses **Bluebook** plus **Idaho State Bar** conventions, with
**parallel citation** to the official **Idaho Reports** and the regional
**Pacific Reporter**. Details and examples are in
`references/citation-format.md`. Highlights:

- **Cases**: `Smith v. Jones, 113 Idaho 730, 747 P.2d 752 (1987)` —
  Idaho Reports first, then `P.2d` / `P.3d`. Court of Appeals opinions add
  **`(Ct. App. YEAR)`** in the parenthetical. **Idaho has no neutral /
  public-domain citation.**
- **Statutes**: `I.C. § 5-216` (Idaho Code; section symbol).
- **Rules**: `I.R.C.P. 56`; `I.R.E. 803(6)`; `I.R.F.L.P. 120`;
  `I.A.R. 14`.

## E-filing — iCourt / Odyssey File & Serve

Idaho e-files through **iCourt / Odyssey File & Serve**, governed by the
**Idaho Rules for Electronic Filing and Service (I.R.E.F.S.)**. E-filing is
**mandatory for attorneys** (I.R.E.F.S. 4(a)) and **optional for
self-represented parties** (I.R.E.F.S. 4(b)); the electronic-document format
is set by I.R.E.F.S. 6. See `references/online-sources.md` for the portal.

## Online sources and data APIs

- Human-facing canonical URLs (isc.idaho.gov for the rules,
  legislature.idaho.gov for the Idaho Code, icourt.idaho.gov,
  finance.idaho.gov): see `references/online-sources.md`.
- Programmatic access (isc.idaho.gov rule pages, legislature.idaho.gov Idaho
  Code, CourtListener Idaho courts, the bundled CourtListener + Legal Data
  Hunter MCP servers): see `references/legal-data-apis.md`.

## Composition

- Every other Idaho skill cites this one for rule numbers, statute numbers,
  and case authorities.
- For statewide document format: `id-statewide-format`.
- For the filing court's mechanics: the district / venue skills.
- For pro se conventions: `id-pro-se`.
- For matter-specific bundles: `id-consumer-debt` and the family-law bundle.

## References

- `references/civil-rules.md` — I.R.C.P. civil-practice map
- `references/evidence-rules.md` — I.R.E. map
- `references/family-rules.md` — Idaho Rules of Family Law Procedure (I.R.F.L.P.) map
- `references/fees-and-costs.md` — fees and cost / fee-shifting framework
- `references/citation-format.md` — Idaho Reports + Pacific Reporter citation conventions
- `references/key-cases.md` — landmark Idaho civil + family precedents
- `references/online-sources.md` — canonical human-facing URLs
- `references/legal-data-apis.md` — programmatic access index
- `references/court-rules/` — verbatim I.R.C.P. / I.R.E. / I.R.F.L.P. / I.A.R. rule text (bounded set)
- `references/id-statutes-debt/` — verbatim Idaho Code sections for civil practice (bounded set)
- `references/federal-debt-laws/` — federal-law corpus (symlink)
- `references/federal-bankruptcy/` — Title 11 U.S.C. corpus (symlink)
- `references/ucc-model/` — Model UCC text (symlink)
