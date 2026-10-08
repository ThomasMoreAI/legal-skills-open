---
name: mi-family-law-codearranger
title: Michigan Family Law
description: 'Use for any Michigan family-law matter: divorce, property division, custody, parenting time, child support, spousal support, relocation. Triggers include "Michigan divorce", "no-fault divorce Michigan", "MCL 552.6", "child custody Michigan", "MCL 722.23" best-interest factors, "parenting time Michigan", "100 mile rule", "Michigan child support formula", "spousal support Michigan", "Sparks v Sparks" equitable distribution. Covers no-fault divorce (MCL 552.6) with 60/180-day waiting periods and residency (MCL 552.9); equitable distribution under Sparks v Sparks factors (MCL 552.19, 552.401); custody and best-interest factors (MCL 722.21, 722.23); established custodial environment; parenting time (MCL 722.27a) and 100-mile change-of-domicile rule (MCL 722.31); income-shares child support (MCL 552.605); spousal support (MCL 552.23, 552.28); UCCJEA/UIFSA for interstate cases.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Michigan Family Law

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a
> substantive framework for Michigan domestic-relations matters,
> not legal advice and not strategic advice for any specific case.
> Family-law cases carry long-term consequences for property,
> children, and finances; strongly consider consulting a licensed
> Michigan family-law attorney even on an "agreed" divorce.
> Outcomes are fact-specific; the choice of claims, defenses, and
> the parenting/support positions belongs to the litigant (and any
> counsel the litigant retains). Verify every rule, threshold,
> deadline, and citation against current law before filing.

This bundle supplies the **substantive law** of Michigan
family practice. The **venue mechanics** — which circuit court,
the Friend of the Court (FOC) intake, mandatory forms, the
Service Member and SCAO process — live in `mi-family-court`.
Document format lives in `mi-statewide-format`.

## Snapshot — Michigan family-law principles

- **No-fault divorce only.** The sole statutory ground is a
  **breakdown of the marriage relationship** to the extent that
  the objects of matrimony have been destroyed and there is no
  reasonable likelihood the marriage can be preserved —
  **MCL 552.6**. No party pleads or proves fault to obtain the
  divorce (though conduct can bear on property and support).
- **Waiting periods — MCL 552.9f.** No proofs may be taken until
  **60 days** after the complaint is filed where there is **no
  minor child**, or **180 days** (6 months) where the parties have
  a **minor child** — the 180-day period reducible by the court
  for unusual hardship or compelling necessity, but the 60-day
  minimum is not waivable.
- **Residency — MCL 552.9.** A complainant must have resided in
  Michigan for **180 days** and in the **county** of filing for
  **10 days** before filing.
- **Equitable distribution — NOT community property.** Property is
  **classified** (marital vs. separate) and the marital estate is
  **divided equitably** — a fair division, not a presumptive 50/50
  — under the **Sparks v Sparks** factors.
- **Custody under the Child Custody Act.** Custody is decided on
  the **best-interest factors at MCL 722.23** (12 factors), against
  the backdrop of the **established custodial environment**
  (MCL 722.27(1)(c)): a court may not change an established
  custodial environment absent **clear and convincing evidence**.
- **Child support uses the Michigan Child Support Formula (MCSF).**
  Statutory basis **MCL 552.605**; the operative figures live in
  the **MCSF Manual** and supplements. The FOC administers
  establishment, review, and enforcement.
- **Spousal support has no rigid formula** — a multi-factor,
  case-by-case analysis under **MCL 552.23 / 552.28**.
- **No common-law marriage.** Abolished by **MCL 551.2** for
  marriages contracted in Michigan on or after **January 1, 1957**;
  a marriage valid where contracted elsewhere is honored.

## Filing path — where a family case goes

Michigan family matters are heard in the **Family Division of the
Circuit Court** in the county of proper venue. Custody, support,
and parenting-time administration run through the county **Friend
of the Court (FOC)**. The venue mechanics, FOC intake, and SCAO
mandatory forms live in `mi-family-court`. Personal protection
orders (PPOs) for domestic violence are filed in the same Family
Division — the **procedural** PPO mechanics are in
`mi-family-court`; this skill addresses only the substantive
family-law overlay.

## Divorce — the only ground (MCL 552.6)

Michigan is a **pure no-fault** state. The complaint must allege,
in the statutory language of **MCL 552.6**, that **"there has been
a breakdown of the marriage relationship to the extent that the
objects of matrimony have been destroyed and there remains no
reasonable likelihood that the marriage can be preserved."** No
other ground may be pleaded, and the court may not require proof
of fault to grant the divorce. (Marital **misconduct** can still
be weighed as one factor in property division and spousal support,
but it is not a ground.)

**Residency — MCL 552.9.** Before filing, the complainant (or
defendant) must have resided in **Michigan for 180 days** and in
the **county of filing for 10 days** immediately preceding filing.

## Divorce — the waiting periods (MCL 552.9f)

The statutory waiting periods run from the **filing of the
complaint**:

- **60 days** where the parties have **no minor children** of the
  marriage; and
- **180 days** (6 months) where the parties **have a minor child**.

Under **MCL 552.9f**, the court may, for **unusual hardship or
compelling necessity**, take testimony before the 180-day period
expires — but it may **not** shorten the **60-day** minimum. The
period is a floor on when proofs may be taken, not a residency
rule; confirm the count with `mi-deadlines` and verify the current
text. (See the corpus for the exact statutory wording and any
narrow exceptions.)

## Property distribution — equitable distribution

Michigan is an **equitable-distribution** state, **not** a
community-property state. The court follows a two-step process.

### Step 1 — Classify (marital vs. separate)

Each asset and debt is classified as **marital** or **separate**.

- **Separate property** generally includes property a spouse
  brought into the marriage, and gifts or inheritances received by
  one spouse during the marriage, that have been kept separate.
- **Marital property** generally includes property acquired by
  either spouse during the marriage through the parties' joint
  efforts.
- Separate property can be reached only through the two statutory
  **invasion** doctrines: **MCL 552.23** (invasion where the
  marital estate is **insufficient** for the other spouse's
  suitable support) and **MCL 552.401** (invasion where the other
  spouse **contributed to the acquisition, improvement, or
  accumulation** of the separate property). Plead the basis for
  invasion expressly when seeking a share of separate property.

### Step 2 — Divide the marital estate equitably

Only the **marital estate** is divided, and division need not be
equal. Michigan courts apply the **Sparks v Sparks**, 440 Mich
141 (1992), factors, which include:

- The **duration** of the marriage
- The **contributions** of each party to the marital estate
- The **age** and **health** of the parties
- The **life status** and **earning abilities** of the parties
- The parties' **needs** and **circumstances**
- **Past relations and conduct** of the parties (fault is a
  factor, not a ground)
- General principles of **equity**

The court makes findings on the relevant factors; a division must
be **equitable in light of all the circumstances**. Verify the
controlling factor articulation and the current text of MCL 552.23
and 552.401 in the corpus.

## Child custody — the Child Custody Act (MCL 722.21 et seq.)

Custody is governed by the **Child Custody Act of 1970**,
**MCL 722.21 et seq.** Two concepts frame every custody decision.

### Legal vs. physical custody

- **Legal custody** = decision-making authority over major
  decisions (education, health care, religion). May be **joint** or
  **sole**.
- **Physical custody** = where the child resides. May be **joint**
  or **sole**, and is implemented through the parenting-time
  schedule.

### The established custodial environment (MCL 722.27(1)(c))

Before changing custody, the court must determine whether an
**established custodial environment (ECE)** exists with one or both
parents — i.e., an environment of a **permanent** nature in which
the child **naturally looks to the custodian** for guidance,
discipline, the necessities of life, and parental comfort. The ECE
sets the **burden of proof**:

- If a proposed change would **alter** an established custodial
  environment, the moving party must show by **clear and
  convincing evidence** that the change is in the child's best
  interests.
- If no ECE exists (or the change does not alter it), the standard
  is a **preponderance of the evidence**.

### The 12 best-interest factors (MCL 722.23)

Custody and (where contested) parenting time are decided on the
**twelve best-interest factors** enumerated at **MCL 722.23**
(factors (a)–(l)), which include the emotional ties between child
and parties; the capacity and disposition to give love, guidance,
education, and religion; the capacity to provide food, clothing,
medical care, and material needs; the permanence of the family
unit; the moral fitness, mental and physical health of the
parties; the child's home, school, and community record; the
**reasonable preference of the child** (if of sufficient age and
maturity); the willingness to **facilitate the child's
relationship with the other parent**; **domestic violence**; and
any other relevant factor. The court makes findings on **each**
applicable factor. Verify the **current** enumeration and wording
of MCL 722.23 in the corpus before drafting findings.

## Parenting time (MCL 722.27a)

Parenting time is governed by **MCL 722.27a**. The statute
expresses a policy that a child is generally best served by a
**strong relationship with both parents** and that parenting time
shall be granted in a frequency, duration, and type **reasonably
calculated to promote a strong relationship**, unless it would
endanger the child's physical, mental, or emotional health. The
statute lists factors the court may consider in setting a
schedule, and parenting time is administered and enforced through
the **FOC** (see `mi-family-court`).

## Change of domicile / relocation — the 100-mile rule (MCL 722.31)

Where a court order governs custody and **no parent has sole legal
custody**, a parent may **not** change a child's **legal residence
more than 100 miles** from the child's legal residence at the time
of the order's commencement without the other parent's consent or
**court permission** — **MCL 722.31**. The cap is measured in
**miles, not by state lines** — it applies to an out-of-state move
the same as to an in-state move, and is **not** triggered by a move
of any distance under 100 miles even if it crosses into another
state. The rule does not apply where a parent has **sole legal
custody** (MCL 722.31(2)), where the child's two residences were
already more than 100 miles apart at the time of the order
(MCL 722.31(3)), or where the move brings the two residences
**closer** together (MCL 722.31(3)).

When deciding a contested change of domicile, the court considers
the statutory factors at **MCL 722.31(4)** — the codification of
the **D'Onofrio** factors as adopted in Michigan (e.g.,
*Rittershaus v Rittershaus*):

1. Whether the move has the **capacity to improve the quality of
   life** for both the child and the relocating parent.
2. The **degree to which each parent has complied** with, and
   utilized, the parenting-time order, and whether the move is
   motivated by a desire to **frustrate** parenting time.
3. The degree to which the court can **modify the parenting-time
   schedule** to preserve and foster the child's relationship with
   the non-relocating parent, and whether each parent is likely to
   comply with a modified schedule.
4. The extent to which the opposing parent's resistance is
   motivated by a desire to secure a **financial advantage** with
   respect to support.
5. **Domestic violence**, regardless of whether directed against
   or witnessed by the child.

Where a change of domicile would also alter the **established
custodial environment**, the clear-and-convincing best-interest
analysis (above) is triggered as well. Verify the current factor
text at MCL 722.31 in the corpus.

## Child support (MCL 552.605 + the Michigan Child Support Formula)

Michigan support is set by formula. The statutory directive at
**MCL 552.605** requires the court to order support **in the amount
determined by the Michigan Child Support Formula (MCSF)** unless it
finds, on the record, that application of the formula would be
**unjust or inappropriate** (a deviation must be supported by
specific findings).

The MCSF is an **income-shares** model: both parents' incomes are
combined, a base support obligation is determined for the number
of children, and the obligation is apportioned between the parents
and adjusted for **parenting time / overnights** and add-ons
(child-care and medical/health-care premiums). The formula also
addresses **imputation of income** where a parent is voluntarily
unemployed or underemployed. Establishment, review, and
**enforcement** (income withholding, license/tax-refund actions,
contempt) run through the county **Friend of the Court**.
Modification requires a **change of circumstances**.

> The MCSF schedules, percentages, low-income thresholds, and
> overnight tables live in the **MCSF Manual and supplements** and
> are **amended periodically** — always run the **current**
> official formula rather than relying on stale figures. See the
> corpus and `mi-law-references` for the controlling numbers.

## Spousal support / alimony (MCL 552.23, 552.28)

Michigan has **no rigid spousal-support formula**. Support is
awarded under **MCL 552.23** on a **case-by-case**, multi-factor
analysis. Courts weigh factors developed in the case law,
including: the parties' **past relations and conduct**; the
**length of the marriage**; each party's **ability to work**; the
**source and amount of property** awarded in the division; each
party's **age** and **health**; the parties' **needs** and
**prior standard of living**; the **ability to pay**; and general
principles of **equity**.

- **Modifiability — MCL 552.28.** Periodic spousal support is
  **modifiable** on a change of circumstances. Support ordered
  **"in gross"** (a fixed, non-modifiable total) is **not**
  modifiable — draft and characterize the award deliberately.

## Common-law marriage (MCL 551.2)

Michigan **abolished common-law marriage** by **MCL 551.2** for
marriages contracted within the state on or after **January 1,
1957**. Cohabitation and reputation in Michigan do **not** create a
marriage. However, a common-law marriage **validly contracted in
another state** that recognizes it is honored in Michigan under the
rule that Michigan recognizes marriages valid **where contracted**.
A party asserting an out-of-state common-law marriage must plead
and prove its validity under that state's law.

## Jurisdiction over children and interstate cases

- **UCCJEA — MCL 722.1101 et seq.** governs subject-matter
  jurisdiction over **custody / parenting-time** determinations.
  The child's **home state** generally controls. Plead the UCCJEA
  jurisdictional allegations (and the required affidavit of the
  child's residences for the prior period) in the complaint or
  petition.
- **UIFSA — MCL 552.2101 et seq.** governs interstate **support**
  establishment, modification, and enforcement, including
  registration of out-of-state orders and the
  continuing-exclusive-jurisdiction rules.

## PPOs / domestic violence (cross-reference)

Domestic-violence and stalking **personal protection orders
(PPOs)** are filed in the Family Division and frequently run
parallel to a divorce or custody case; their issuance can bear on
the **best-interest** and **domestic-violence** factors above. The
**procedural** PPO mechanics — petition forms, the ex parte
standard, the show-cause hearing, and service — live in
`mi-family-court`. Coordinate any PPO with the parenting-time and
possession provisions across the cases.

## Drafting checklist

- [ ] Forum correct (Circuit Court Family Division, proper county
      venue) — see `mi-family-court`
- [ ] Sole no-fault ground pleaded in the **MCL 552.6** statutory
      language; residency (180-day state / 10-day county) under
      MCL 552.9 alleged
- [ ] Waiting period (60 / 180 days from filing) calculated under
      MCL 552.9f — verify with `mi-deadlines`
- [ ] Property **classified** (marital vs. separate) before
      proposing an equitable division under the **Sparks** factors;
      invasion of separate property pleaded under MCL 552.23 /
      552.401 if sought
- [ ] Custody analyzed against the **established custodial
      environment** (MCL 722.27(1)(c)) with findings on the **12
      best-interest factors** (MCL 722.23)
- [ ] Parenting time framed under MCL 722.27a; any relocation
      handled under the **100-mile rule** + MCL 722.31(4) factors
- [ ] Child support run on the **current** official **MCSF**;
      deviation, if any, supported by record findings under
      MCL 552.605
- [ ] Spousal support request identifies whether periodic
      (modifiable, MCL 552.28) or **in gross** (non-modifiable)
- [ ] UCCJEA / UIFSA allegations included where there is an
      interstate element

## Composition

- For format and the MCR 1.109 caption: `mi-statewide-format`
- For the Family Division venue, FOC intake, SCAO mandatory forms,
  and PPO mechanics: `mi-family-court`
- For drafting the complaint / petition / motion: `mi-draft-motion`
- For sworn declarations / affidavits: `mi-draft-declaration`
- For a proposed judgment of divorce / order: `mi-draft-order`,
  `mi-submit-order`
- For pro se conventions and self-represented intake: `mi-pro-se`
- For the 60/180-day waiting period and other deadlines:
  `mi-deadlines`
- For hearings and oral argument: `mi-hearings`
- For citation verification: `mi-fact-check`
- For canonical MCL text and the MCSF Manual: `mi-law-references`

## References

- `references/divorce-grounds-residency.md` — MCL 552.6 no-fault
  ground, MCL 552.9 residency, MCL 552.9f waiting periods
- `references/property-division.md` — marital vs. separate
  classification, the Sparks v Sparks factors, invasion under
  MCL 552.19 / 552.23 / 552.401
- `references/custody.md` — Child Custody Act (MCL 722.21 et seq.),
  the 12 best-interest factors (MCL 722.23), established custodial
  environment (MCL 722.27(1)(c))
- `references/parenting-time-relocation.md` — MCL 722.27a parenting
  time + the 100-mile change-of-domicile rule (MCL 722.31) and the
  D'Onofrio / Rittershaus factors
- `references/child-support.md` — MCL 552.605 + the Michigan Child
  Support Formula income-shares model and worksheet inputs
- `references/spousal-support.md` — MCL 552.23 factors and the
  MCL 552.28 modifiable-vs-in-gross distinction
- `references/uccjea-uifsa.md` — MCL 722.1101 et seq. and
  MCL 552.2101 et seq.
