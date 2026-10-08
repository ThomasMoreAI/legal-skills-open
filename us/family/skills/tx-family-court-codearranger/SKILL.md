---
name: tx-family-court-codearranger
title: Texas Family Court — Family Matters in the District Courts
description: 'Use to choose venue and handle filing mechanics for a Texas domestic-relations case — divorce, SAPCR (suit affecting the parent-child relationship), custody (conservatorship) and possession, child support, paternity, modification and enforcement, and family-violence protective orders. CRITICAL: Texas has NO separate family-court trial court — these cases are heard in the DISTRICT COURTS (some populous counties designate family district courts), on the Texas Rules of Civil Procedure. Triggers: "file for divorce in Texas", "Texas SAPCR", "Texas custody case", "Texas family district court", "Texas divorce waiting period", "60-day divorce Texas", "Texas protective order", "family violence Texas", "Texas child support case", "Texas conservatorship", "associate judge Texas family", "Petitioner Respondent divorce Texas". Venue and procedural skill; defers substantive law to `tx-family-law`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Texas Family Court — Family Matters in the District Courts

> **NOT LEGAL ADVICE.** Divorce, custody, support, and parentage
> outcomes have lasting consequences for children, property, and
> finances. Strongly consider consulting a licensed Texas family-law
> attorney even on an agreed or "simple" matter. This skill is a
> drafting/venue aid; verify the filing county's current local rules
> and the controlling statutes and rules before filing.

Texas has **no separate, free-standing family trial court**.
Domestic-relations matters are heard in the **District Courts** —
Texas's general-jurisdiction trial court. Some populous counties
**designate family district courts** (District Courts that hear
primarily family dockets), and many counties use **associate judges**
under **Tex. Fam. Code Ch. 201** to hear family matters subject to
de novo review by the referring district judge. This skill covers
**where to file and filing mechanics**. For substantive law —
divorce grounds, the "just and right" community-property division,
conservatorship and possession, the child-support guidelines, spousal
maintenance, UCCJEA/UIFSA, and the protective-order overlay — see
`tx-family-law`. For document form, see `tx-statewide-format`.

## Procedure is the TRCP

Texas family cases run on the **Texas Rules of Civil Procedure
(TRCP)** and the **Texas Family Code**, in the District Courts. There
is no separate "family rules" set displacing the TRCP; the Family
Code supplies the substantive law and certain special procedures
(temporary orders, standing orders, mandatory disclosures in family
cases), layered on top of the TRCP. Confirm the county's local rules
and any **standing orders** that automatically take effect on filing
(many counties impose automatic temporary injunctions / standing
orders preserving the status quo and protecting children at the
moment a divorce or SAPCR is filed) against the corpus and the
county.

## What this venue handles

| Matter | Heard in the District Court? |
|---|---|
| Divorce (decree of divorce) | **Yes** (Tex. Fam. Code Ch. 6) |
| Property division | Yes — with the divorce ("just and right" division, Ch. 7) |
| Spousal maintenance | Yes — with the divorce (Ch. 8) |
| SAPCR — conservatorship & possession | **Yes** (Ch. 153) |
| Child support and enforcement | **Yes** (Ch. 154 + Ch. 157 enforcement) |
| Paternity / parentage | **Yes** (Ch. 160) |
| Modification of family orders | **Yes** (Ch. 156) |
| Annulment / suit to declare marriage void | **Yes** (Ch. 6) |
| **Family-violence protective orders** | **Yes** (Title 4, Ch. 81–88) — distinct procedure (see below) |
| UCCJEA / UIFSA jurisdiction | Ch. 152 / Ch. 159 |

> **Terminology.** Use **Petitioner** and **Respondent** for the
> parties, the **District Court** (or designated family district
> court) for the forum, and **decree of divorce** for the dissolving
> order. The suit concerning children is a **SAPCR** (Suit Affecting
> the Parent-Child Relationship).

## SAPCR intake and standing

A **SAPCR** is the vehicle for conservatorship (custody), possession
and access (visitation), and child support. SAPCR issues may be
brought **within a divorce** (when the parties have children of the
marriage) or in a **stand-alone SAPCR** (e.g., between unmarried
parents, or by a non-parent with standing). **Standing** to file an
original SAPCR is governed by **Tex. Fam. Code Ch. 102** — a parent
has standing, and certain non-parents (a person with actual care and
control for a statutory period, a grandparent in defined
circumstances, etc.) have standing only where the statute confers it.
Confirm the standing basis against `tx-family-law` and Ch. 102 before
filing; lack of standing is a threshold defect.

## The 60-day divorce waiting period

Texas imposes a **statutory waiting period** between filing the
divorce petition and the earliest date the court may grant the
divorce — generally **60 days** after the petition is filed (subject
to narrow family-violence exceptions). Treat this as a framework
anchor and **confirm the current period and the exception against
`tx-family-law` and the Family Code** (**Tex. Fam. Code § 6.702**)
before calendaring. Residency prerequisites also apply (a domicile
period in Texas and in the county before filing — confirm against
`tx-family-law`, **Tex. Fam. Code § 6.301**). See `tx-deadlines`.

## Family-violence protective orders are a distinct track

A **family-violence protective order** under **Title 4 (Tex. Fam.
Code Ch. 81–88)** runs on its **own statutory procedure** — its own
application, hearing-setting, and findings — even when the same
parties have a pending divorce or SAPCR. Coordinate the two cases but
do not fold the protective-order application into the divorce/SAPCR
petition. Protective-order matters are time-sensitive and often
involve safety concerns; encourage prompt consultation with counsel
or a local family-violence advocate. The substantive overlay (how a
protective order or a history of family violence bears on the
best-interest conservatorship analysis) lives in `tx-family-law`; the
distinct procedure is flagged here so it is not assumed to follow the
ordinary SAPCR path.

> Adoption, termination of parental rights, and child-protective (DFPS)
> suits are likewise specialized proceedings; confirm the governing
> chapter (Ch. 161 termination, Ch. 162 adoption) and any heightened
> procedure before treating them as an ordinary family matter.

## Venue and jurisdiction

- File in the **District Court** (or designated family district
  court) of the **county of proper venue.** For divorce, confirm the
  Texas **residency / domicile** prerequisites (**Tex. Fam. Code
  § 6.301**); for a SAPCR, confirm venue under **Tex. Fam. Code
  Ch. 103** (generally the child's county of residence).
- If there are minor children, confirm Texas is the child's **home
  state** under the **UCCJEA (Tex. Fam. Code Ch. 152)** and plead the
  jurisdictional allegations (`tx-family-law`).
- Confirm the county's family-docket assignment, whether the matter
  is referred to an **associate judge (Ch. 201)**, and the county's
  automatic standing orders with the venue skill (`tx-hcdc`,
  `tx-dcdc`, `tx-county-courts`).

## The caption — "In the Matter of the Marriage of" / "In the Interest of"

Texas family-case captions conventionally read **In the Matter of the
Marriage of [Spouse] and [Spouse]** for a divorce (and, where there
are children, add **and In the Interest of [Child(ren)], Child(ren)**),
or **In the Interest of [Child(ren)], Child(ren)** for a stand-alone
SAPCR. Designate the parties **Petitioner** and **Respondent**. Build
the caption in the District Court for the county under
`tx-statewide-format` (the **§** divider, the line-numbered pleading
paper, the footer, and the TRCP 57 signature block).

## Filing mechanics

1. **Confirm jurisdiction and venue** — District Court of the proper
   county; divorce residency (**§ 6.301**); SAPCR venue (**Ch. 103**);
   UCCJEA home-state allegations for children (`tx-family-law`).
2. **Prepare the initiating documents** — the **Original Petition for
   Divorce** (or Original SAPCR / Petition to Establish Parentage),
   stating the statutory ground (no-fault **insupportability**,
   **Tex. Fam. Code § 6.001**, and/or a fault ground), the
   conservatorship / possession and support requests for children,
   and the property allegations. Use `tx-statewide-format` for the
   caption and form, and `tx-draft-motion` / `tx-draft-declaration` /
   `tx-draft-order` for the documents.
3. **Check for automatic standing orders** — many counties impose an
   automatic temporary injunction / standing order on filing.
   Determine whether the county has one and attach/serve it as the
   local rule requires.
4. **Use TexasLawHelp.org / Texas Supreme Court forms** —
   self-represented filers can prepare Texas's official, court-
   approved family-law forms (uncontested divorce with/without
   children, SAPCR, modification) through **TexasLawHelp.org** and the
   guided-filing tools, which assemble the petition and supporting
   forms for filing through eFileTexas. Confirm the current packet and
   that the county accepts it.
5. **File and pay (or waive) the fee** — with the District Clerk; a
   **Statement of Inability to Afford Payment of Court Costs** may be
   available for qualifying self-represented filers. Confirm the
   county's filing fee and the eFileTexas path for the case type
   (`tx-file-packet`, and the venue skill).
6. **Serve** the petition and any citation under the applicable
   service rule; the **Original Answer / response** window follows the
   TRCP (the **TRCP 99 "Monday rule"** answer deadline) —
   `tx-first-30-days`.
7. **Waiting period and disclosures** — track the **60-day** divorce
   waiting period tied to **§ 6.702** (confirm the current figure —
   `tx-family-law`, `tx-deadlines`) and exchange the mandatory
   family-case disclosures.

## Self-represented (pro se) family intake

- Texas provides extensive **TexasLawHelp.org** resources and
  court-approved form packets for family matters, plus guided-filing
  tools that assemble the petition and supporting forms for filing
  through eFileTexas. Confirm the current packet and the county's
  acceptance.
- Designate the filer clearly as self-represented in the signature
  block (no State Bar of Texas number) — see `tx-pro-se`.
- Clerks and self-help-center staff explain **procedure**, not legal
  advice. Encourage consultation with a licensed Texas family-law
  attorney where there are minor children, retirement assets, real
  property, a business, safety concerns, or any disputed issue.

## Composition

- For substantive law (divorce grounds, community-property
  classification and the "just and right" division, spousal
  maintenance eligibility and caps, the Ch. 153 conservatorship and
  Standard Possession Order, the Ch. 154 child-support guideline
  percentages and the net-resources cap, modification, UCCJEA/UIFSA,
  and the protective-order substantive overlay): `tx-family-law`
- For document format and the Texas caption: `tx-statewide-format`
- For the specific county / clerk / family-docket assignment and
  e-filing: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`
- For pro se conventions and TexasLawHelp forms: `tx-pro-se`
- For the response and the TRCP 99 "Monday rule": `tx-first-30-days`
- For deadlines, the waiting period, and time computation:
  `tx-deadlines`
- For drafting the petition / response / motion: `tx-draft-motion`
- For sworn declarations / financial affidavits / unsworn
  declarations (Tex. Civ. Prac. & Rem. Code § 132.001):
  `tx-draft-declaration`
- For the proposed decree / order: `tx-draft-order`, `tx-submit-order`
- For assembling and preflighting the filing packet:
  `tx-file-packet`
- For scheduling and hearings: `tx-schedule-hearing`, `tx-hearings`
- For citation verification: `tx-fact-check`

## References

- `../tx-law-references/references/court-rules/` — the TRCP and Texas
  Rules of Evidence for cross-reference, plus county local-rules and
  standing-order pointers
- `../tx-law-references/references/tx-statutes-debt/` and the Texas
  Family Code corpus — the substantive family statutes invoked in the
  petition (Ch. 6, 7, 8, 102, 103, 152, 153, 154, 156, 157, 159, 160,
  and Title 4 protective orders), cross-referenced from
  `tx-family-law`
