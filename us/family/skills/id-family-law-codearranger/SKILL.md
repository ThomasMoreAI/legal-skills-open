---
name: id-family-law-codearranger
title: Idaho Family Law
description: 'Use for any Idaho family-law / domestic-relations matter: divorce, legal separation, separate maintenance, annulment, community-property division, custody and parenting time, child support, spousal maintenance, relocation, modification, and interstate jurisdiction. Triggers: "file for divorce in Idaho", "Idaho divorce grounds", "irreconcilable differences Idaho", "community property Idaho", "Idaho child support", "Idaho Child Support Guidelines", "I.R.F.L.P. 120", "Idaho custody best interests", "Idaho spousal maintenance", "Idaho UCCJEA", "common-law marriage Idaho", "Bonneville County divorce". Covers: divorce grounds (I.C. § 32-603 fault + § 32-610 irreconcilable differences), community property (I.C. § 32-903 / § 32-906), spousal maintenance (I.C. § 32-705), child support (I.R.F.L.P. 120 income-shares Guidelines), custody best interests (I.C. § 32-717) + joint-custody presumption (I.C. § 32-717B), relocation, modification, post-1996 common-law marriage abolition (I.C. §
  32-201), and UCCJEA.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Idaho Family Law

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a
> substantive framework for Idaho domestic-relations matters, not legal
> advice and not strategic advice for any specific case. Family-law
> cases carry long-term consequences for property, children, and
> finances; strongly consider consulting a licensed Idaho family-law
> attorney even on an "agreed" divorce. **Outcomes are fact-specific**;
> the choice of claims, defenses, and the parenting/support positions
> belongs to the litigant (and any counsel the litigant retains).
> Verify every rule, threshold, waiting period, dollar figure, and
> citation against current law before filing.

This bundle supplies the **substantive law** of Idaho family practice.
The **venue mechanics** — the Magistrate Division of the District
Court, the I.R.F.L.P. procedural rule set, intake, mandatory financial
disclosures, the I.R.F.L.P. 208 caption, and the Court Assistance
Office / Guide & File forms — live in `id-family-court`. Document
format lives in `id-statewide-format`.

## Snapshot — Idaho family-law principles

- **Both no-fault and fault divorce.** Idaho recognizes
  **irreconcilable differences** as a no-fault ground —
  **I.C. § 32-610** — and a catalog of **fault grounds** at
  **I.C. § 32-603**.
- **Community-property state.** Property acquired during the marriage
  is **community property** — **I.C. § 32-906** — and is divided by the
  court at divorce; separate property is defined at **I.C. § 32-903**.
- **Spousal maintenance is need-and-factor based** —
  **I.C. § 32-705**.
- **Child support follows the Idaho Child Support Guidelines** — an
  **income-shares** model adopted through **I.R.F.L.P. 120**.
- **Custody turns on the child's best interests** — **I.C. § 32-717** —
  with a **presumption that joint custody is in the best interests**
  under **I.C. § 32-717B**.
- **No common-law marriage after January 1, 1996.** **I.C. § 32-201**
  abolished common-law marriage going forward; a common-law marriage
  **entered before** that date remains valid.
- **Civil protection orders are a separate track** — the **Domestic
  Violence Crime Prevention Act, I.C. § 39-6301 et seq.** — not part of
  the I.R.F.L.P. family-law rules.

## Filing path — where a family case goes

Idaho family matters are heard in the **Magistrate Division of the
District Court** for the county of residence. The venue mechanics, the
I.R.F.L.P. procedural rule set, the mandatory-disclosure obligation,
and the Court Assistance Office forms live in `id-family-court`.
Protection orders for domestic violence run **parallel** to a divorce
or custody case — their **procedure** is outside the I.R.F.L.P. (see
`id-family-court`); this skill addresses only the **substantive**
family-law overlay.

## Divorce — grounds (I.C. §§ 32-603, 32-610)

Idaho lets a petitioner proceed on **irreconcilable differences** (no
fault) **or** plead a **fault ground**.

- **Irreconcilable differences — I.C. § 32-610.** The no-fault ground:
  differences that have caused the irremediable breakdown of the
  marriage. Most uncontested Idaho divorces proceed on this ground.
- **Fault grounds — I.C. § 32-603.** The enumerated fault grounds
  include **adultery**, **extreme cruelty**, **willful desertion**,
  **willful neglect**, **habitual intemperance**, and **conviction of a
  felony**. Plead the specific ground and its supporting facts where a
  fault ground is used. Confirm the current, full enumeration of
  § 32-603 in `../id-law-references/references/id-statutes-debt/`.

> **Residency.** Confirm Idaho's residency requirement for divorce (the
> petitioner's required period of residence in the state before filing)
> against the current statute before pleading the jurisdictional
> allegation.

## Divorce — the waiting period (tied to I.C. § 32-716)

Idaho imposes a **statutory waiting period** before the court may enter
a decree of divorce, tied to **I.C. § 32-716** and the reconciliation
mechanics. **Do not hardcode an exact day count** — published sources
conflict and the figure is drift-prone. **Confirm the current waiting
period** against the statute and the county's practice, and calculate
the count with `id-deadlines`. The period is a floor on entry of the
decree, not a bar on filing; section 32-716 also frames the court's
ability to direct a reconciliation/cooling-off interval.

## Property distribution — community property (I.C. §§ 32-903, 32-906)

Idaho is a **community-property** state. The analysis is a
classification step followed by a division step.

### Step 1 — Classify (separate vs. community)

- **Separate property — I.C. § 32-903** — is property a spouse
  **owned before marriage**, plus property acquired during marriage by
  **gift, bequest, devise, or descent**, together with the **rents,
  issues, and profits** of separate property. It remains the owning
  spouse's separate estate.
- **Community property — I.C. § 32-906** — is all other property
  acquired by either spouse **during the marriage** (with the statutory
  exceptions). Both spouses hold a present, undivided one-half interest
  in the community estate.
- **Quasi-community property.** Property acquired while domiciled
  elsewhere that **would have been community property had it been
  acquired in Idaho** can be treated as **quasi-community property**
  for division purposes; flag and characterize it where the parties
  moved to Idaho from a non-community-property state.
- **Commingling and tracing.** Separate property **commingled** with
  community property so that it can no longer be traced may lose its
  separate character; the spouse asserting a separate interest bears
  the **tracing** burden. Community contributions to a separate asset
  (e.g., mortgage paydown on a pre-marital home, or community labor
  enhancing a separate business) can create reimbursement / community
  claims. Address tracing and any reimbursement claim expressly.

### Step 2 — Divide the community

At divorce the court **divides the community property**. Confirm the
current statutory standard and the controlling articulation (and any
"substantially equal absent compelling reasons" gloss) in
`../id-law-references/references/id-statutes-debt/`. Separate property
is **confirmed** to the owning spouse and is not divided; the court
also allocates **community debts**.

## Spousal maintenance (I.C. § 32-705)

Idaho spousal maintenance is governed by **I.C. § 32-705**. The court
may grant maintenance only if it finds the spouse seeking it **lacks
sufficient property** to provide for reasonable needs **and** is
**unable to support themselves through employment**. If that threshold
is met, the court sets the **amount and duration** after weighing the
statutory factors — including the financial resources of the spouse
seeking maintenance, the time needed to acquire education or training,
the **duration of the marriage**, the age and physical and emotional
condition of the spouse seeking maintenance, the ability of the paying
spouse to meet their own needs while paying, the tax consequences, and
fault of either party where relevant. Plead the threshold finding and
the factors; verify the current § 32-705 enumeration in the corpus.

## Child support (Idaho Child Support Guidelines — I.R.F.L.P. 120)

Idaho child support is set by the **Idaho Child Support Guidelines**,
adopted through **I.R.F.L.P. 120** (with worksheets in the rule's
appendices). The statutory duty of support is rooted in **I.C.
§ 32-706**; the operative figures and worksheet live in the
Guidelines.

The Guidelines use an **income-shares** model:

- **Combine** both parents' gross incomes to find combined parental
  gross income.
- Determine the **basic support obligation** from the Guidelines
  schedule for the number of children, then **apportion** it between
  the parents **in proportion** to each parent's share of combined
  income.
- **Adjust** for **shared / split physical custody** where a parent has
  the child more than the Guidelines' overnight threshold (commonly
  expressed as **more than ~25% of overnights** — confirm the current
  trigger and formula), and for **work-related child-care costs** and
  **health-insurance premiums** for the children.
- A **modest per-child minimum** support amount applies — **verify the
  current guideline figures** rather than relying on a remembered
  number.

The court orders the Guidelines amount unless a **deviation** is
justified by written findings that the guideline amount would be unjust
or inappropriate. Establishment, review, and enforcement (income
withholding, license actions, contempt) run through the Magistrate
Division and Idaho's child-support enforcement program.

> The Guidelines schedule, the self-support reserve, the shared-custody
> overnight adjustment, and the add-on rules are **amended
> periodically** — always run the **current** official Idaho Child
> Support Guidelines and worksheet rather than relying on stale
> figures. See `../id-law-references/references/court-rules/` (I.R.F.L.P.
> 120) and `id-law-references` for the controlling numbers.

## Custody and parenting time (I.C. §§ 32-717, 32-717B)

### Best interests — I.C. § 32-717

Custody and parenting time are decided on the **best interests of the
child** under the factors at **I.C. § 32-717** — including the wishes
of the parents; the wishes of the child as to custody; the
interaction and interrelationship of the child with parents and
siblings; the child's adjustment to home, school, and community; the
character and circumstances of all involved; the need to promote
continuity and stability; and **domestic violence**, whether or not in
the presence of the child. In contested cases the court makes findings
on the relevant factors. Verify the current § 32-717 enumeration in the
corpus before drafting findings.

### Joint-custody presumption — I.C. § 32-717B

**I.C. § 32-717B** defines **joint legal custody** and **joint physical
custody** and provides a **presumption that joint custody is in the
best interests of the child** absent a preponderance showing to the
contrary. The statute also provides that the presumption does **not**
apply where one parent is found to have committed **domestic violence**.
Frame the parenting plan to the joint-custody presumption and address
any rebuttal expressly.

## Relocation of a child

Idaho has **no automatic prohibition** on a custodial parent moving;
relocation that affects an existing custody or parenting-time order is
analyzed under the **best-interests** standard (I.C. § 32-717), and a
proposed move is commonly handled as a **modification** of the existing
order. Address the reasons for the move, its effect on the child's
relationship with the non-moving parent, and a realistic revised
parenting schedule. Confirm any notice obligation in the existing
decree and the current case law before drafting; coordinate with
UCCJEA jurisdiction where the move crosses state lines.

## Modification

An existing custody, parenting-time, or support order may be modified
on a showing of a **substantial and material change of circumstances**
since the last order, with the modified terms judged against the
child's **best interests** (custody) or the **current Guidelines**
(support). Plead the changed circumstances specifically; a custody
modification and a support modification are distinct showings.

## Common-law marriage (I.C. § 32-201)

Idaho **abolished common-law marriage for marriages entered after
January 1, 1996** — **I.C. § 32-201**. After that date, a valid Idaho
marriage requires a license and solemnization; cohabitation and
holding-out create no marriage. **But a common-law marriage entered
before January 1, 1996 remains valid** — so screen the date the parties
began holding themselves out as married. A party asserting a pre-1996
common-law marriage must plead and prove its formation before that
date.

## Civil protection orders / domestic violence (cross-reference)

Domestic-violence **civil protection orders** are commonly sought
alongside a divorce or custody case, and their findings can bear
directly on the **best-interests** analysis and the **§ 32-717B**
joint-custody presumption. Protection orders are issued under the
**Domestic Violence Crime Prevention Act, I.C. § 39-6301 et seq.** —
**not** under the I.R.F.L.P. — so they run on a **separate procedural
track**. The procedural mechanics live in `id-family-court`; coordinate
any protection order with the parenting-time provisions across the
cases.

## Jurisdiction over children and interstate cases

- **UCCJEA — I.C. § 32-11-101 et seq.** governs subject-matter
  jurisdiction over **custody / parenting-time** determinations. The
  child's **home state** generally controls. Plead the UCCJEA
  jurisdictional allegations and the required information about the
  child's residences for the prior period in the petition.
- **UIFSA — I.C. Title 7, Chapter 10.** governs interstate **support**
  establishment, modification, and enforcement, including registration
  of out-of-state orders and the continuing-exclusive-jurisdiction
  rules.

## Drafting checklist

- [ ] Forum correct (Magistrate Division of the District Court, county
      of residence) — see `id-family-court`
- [ ] Divorce ground pleaded — **irreconcilable differences**
      (I.C. § 32-610) **or** a specific **I.C. § 32-603** fault ground
      with supporting facts
- [ ] Residency alleged; **waiting period** tied to I.C. § 32-716
      **confirmed (not hardcoded)** and calculated with `id-deadlines`
- [ ] Property **classified** (separate vs. community,
      I.C. §§ 32-903 / 32-906; **quasi-community** if the parties moved
      from a non-community state) with **tracing** and any
      **reimbursement** claim addressed before proposing a division;
      community debts allocated
- [ ] Spousal maintenance analyzed under **I.C. § 32-705** — threshold
      finding first, then amount/duration on the factors
- [ ] Custody + parenting time framed to the **best-interests factors**
      (I.C. § 32-717) and the **joint-custody presumption**
      (I.C. § 32-717B); domestic-violence findings addressed where they
      apply
- [ ] Child support run on the **current** Idaho Child Support
      Guidelines (**I.R.F.L.P. 120**, income-shares) with the
      shared-custody overnight adjustment, child-care, and health-
      insurance add-ons; **verify current figures**; any deviation
      supported by written findings
- [ ] Any relocation handled as a best-interests **modification**
      (I.C. § 32-717) with notice and revised-schedule showings
- [ ] Common-law-marriage date screened against the **January 1, 1996**
      cutoff (I.C. § 32-201)
- [ ] UCCJEA (I.C. § 32-11-101 et seq.) / UIFSA (I.C. Title 7 ch. 10)
      allegations included where there is an interstate element
- [ ] Any companion **protection order** routed on its **separate**
      I.C. § 39-6301 track (see `id-family-court`)

## Composition

- For format and the I.R.F.L.P. 208 caption: `id-statewide-format`
- For the Magistrate Division venue, the I.R.F.L.P. procedural rules,
  mandatory disclosures, Court Assistance Office forms, and the
  protection-order procedure: `id-family-court`
- For the county / clerk / Magistrate Division assignment:
  `id-bonneville`, `id-county-courts`
- For drafting the petition / response / motion: `id-draft-motion`
- For sworn declarations / financial affidavits: `id-draft-declaration`
- For a proposed decree / order: `id-draft-order`, `id-submit-order`
- For pro se conventions and self-represented intake: `id-pro-se`
- For the waiting period and other deadlines: `id-deadlines`
- For hearings and oral argument: `id-hearings`
- For disability accommodations: `id-ada`
- For citation verification: `id-fact-check`
- For canonical Idaho Code Title 32 text, the Idaho Child Support
  Guidelines, and the I.R.F.L.P.: `id-law-references`

## References

- `../id-law-references/references/court-rules/` — the I.R.F.L.P.
  verbatim, including **I.R.F.L.P. 120** (the Idaho Child Support
  Guidelines + worksheets) and **I.R.F.L.P. 101 / 208**
- `../id-law-references/references/id-statutes-debt/` and the Idaho Code
  **Title 32** corpus — divorce grounds (§§ 32-603, 32-610), community
  property (§§ 32-903, 32-906), spousal maintenance (§ 32-705), child
  support (§ 32-706), custody (§§ 32-717, 32-717B), common-law marriage
  (§ 32-201), the UCCJEA (§ 32-11-101 et seq.); and Title 7 ch. 10
  (UIFSA) and Title 39 (§ 39-6301 et seq., protection orders)
