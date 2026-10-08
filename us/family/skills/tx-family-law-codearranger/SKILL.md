---
name: tx-family-law-codearranger
title: Texas Family Law
description: 'Use for any Texas family-law / domestic-relations matter: divorce, annulment, community-property division, conservatorship (custody) and possession (visitation), child support, spousal maintenance, modification, and interstate jurisdiction. Triggers: "file for divorce in Texas", "Texas divorce grounds", "insupportability divorce Texas", "60-day waiting period divorce Texas", "community property Texas", "just and right division Texas", "Texas child support cap", "joint managing conservator Texas", "Standard Possession Order Texas", "Holley factors", "Texas spousal maintenance", "common-law marriage Texas", "SAPCR Texas", "UCCJEA Texas custody jurisdiction", "Texas protective order". Covers divorce grounds (Ch. 6), the 60-day waiting period (§ 6.702), community property (§ 3.003) and "just and right" division (Ch. 7), conservatorship & possession (Ch. 153), child support (Ch. 154), maintenance (Ch. 8), informal marriage (§ 2.401), SAPCR, UCCJEA (Ch. 152) / UIFSA (Ch. 159), and
  Title 4 protective orders.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Texas Family Law

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a substantive framework for Texas
> domestic-relations matters, not legal advice and not strategic advice for any specific case.
> Family-law cases carry long-term consequences for property, children, and finances; strongly
> consider consulting a licensed Texas family-law attorney even on an "agreed" divorce. **Outcomes
> are fact-specific**; the choice of claims, defenses, and the parenting / support positions belongs
> to the litigant (and any counsel the litigant retains). Verify every rule, threshold, waiting
> period, dollar figure, net-resources cap, and citation against current law before filing.

This bundle supplies the **substantive law** of Texas family practice. The **venue mechanics** — the
District Court (and any designated **family district court**) where Texas family cases are heard, the
associate-judge system (Tex. Fam. Code Ch. 201), intake, e-filing through eFileTexas.gov, and the
caption / cover-sheet conventions — live in `tx-family-court`. Document format lives in
`tx-statewide-format`. Procedure is the **Texas Rules of Civil Procedure** (there is **no separate
family-court trial court**; family matters are heard in the District Courts).

## Snapshot — Texas family-law principles

- **No-fault and fault divorce.** Texas recognizes **insupportability** as the no-fault ground —
  **Tex. Fam. Code § 6.001** — and a catalog of **fault grounds** at **§§ 6.002–6.007**.
- **A 60-day waiting period** must elapse after the petition is filed before the court may grant the
  divorce — **§ 6.702** (with narrow family-violence exceptions — confirm in the corpus).
- **Community-property state.** Property possessed by either spouse during or on dissolution of the
  marriage is **presumed community property** — **§ 3.003** — and the court divides the community
  estate in a manner it deems **"just and right"** under **Ch. 7**.
- **Conservatorship, not "custody" labels.** Texas decides **conservatorship** (decision-making) and
  **possession and access** (time with the child) under **Ch. 153**, with a **rebuttable presumption
  that the parents should be appointed joint managing conservators** — **§ 153.131** — and a
  statutory **Standard Possession Order** at **§ 153.252**.
- **Child support is a percentage-of-net-resources guideline model** — **Ch. 154** — with guideline
  percentages that step up by the number of children before the court.
- **Spousal maintenance is narrowly available** — **Ch. 8** — with statutory eligibility gates and
  caps on amount and duration.
- **Texas recognizes informal (common-law) marriage** — **§ 2.401** — by agreement + cohabitation +
  holding out, or by a registered declaration.
- **Protective orders for family violence** run under **Title 4 (Ch. 81–88)** — a separate track
  whose findings can bear on conservatorship and possession.

## Filing path — where a Texas family case goes

Texas family matters (divorce, annulment, and **Suits Affecting the Parent-Child Relationship**) are
filed in a **District Court** of the county of proper venue. Some populous counties designate
**family district courts**; many counties refer matters to **associate judges** under **Ch. 201**
whose recommendations become orders subject to **de novo** appeal to the referring court. The venue
mechanics, the associate-judge process, e-filing, and the caption conventions live in
`tx-family-court`. Parties are styled **Petitioner** and **Respondent**. The initiating pleading is
an **Original Petition** (e.g., **Original Petition for Divorce**); the responsive pleading is an
**Original Answer** (often a general denial under TRCP 92), and a respondent who wants affirmative
relief files a **Counterpetition**.

## Divorce — grounds (Tex. Fam. Code §§ 6.001–6.007)

Texas lets a petitioner proceed on **insupportability** (no fault) **or** plead a **fault ground**.

- **Insupportability — § 6.001.** The no-fault ground: the marriage has become insupportable because
  of discord or conflict of personalities that destroys the legitimate ends of the marriage and
  prevents any reasonable expectation of reconciliation. Most Texas divorces proceed on this ground.
- **Fault grounds — §§ 6.002–6.007.** The enumerated fault grounds include **cruelty (§ 6.002)**,
  **adultery (§ 6.003)**, **conviction of a felony (§ 6.004)**, **abandonment (§ 6.005)**, **living
  apart (§ 6.006)** for the statutory period, and **confinement in a mental hospital (§ 6.007)**.
  Plead the specific ground and its supporting facts where a fault ground is used; fault can bear on
  a disproportionate **"just and right"** property division and on maintenance. Confirm the current,
  full enumeration in `../tx-law-references/references/tx-statutes-debt/`.
- **Annulment and void marriage.** Texas also provides for **annulment** (e.g., underage, fraud,
  duress, intoxication — Ch. 6, Subchapter B) and suits to **declare a marriage void** (bigamy,
  consanguinity — Subchapter C). Identify whether the facts support annulment / void rather than
  divorce.

## Divorce — residency (§ 6.301) and the 60-day waiting period (§ 6.702)

- **Residency — § 6.301.** Before filing for divorce, a party (the petitioner **or** the respondent)
  must have been a **domiciliary of Texas for the preceding 6 months** and a **resident of the county
  of filing for the preceding 90 days**. Plead the residency allegation; confirm the current periods
  against the corpus.
- **The 60-day waiting period — § 6.702.** The court **may not grant** a divorce before the **60th
  day** after the date the suit was filed (narrow exceptions exist, e.g., certain family-violence
  situations — confirm in the corpus). The period is a **floor on entry of the decree**, not a bar
  on filing. Calculate the count with `tx-deadlines`.

## Property distribution — community property (§ 3.003) and "just and right" division (Ch. 7)

Texas is a **community-property** state. The analysis is a **characterization** step followed by a
**division** step.

### Step 1 — Characterize (separate vs. community)

- **Community-property presumption — § 3.003.** Property possessed by either spouse during or on
  dissolution of marriage is **presumed to be community property**; a spouse claiming an asset is
  **separate** must prove it by **clear and convincing evidence**.
- **Separate property.** Property a spouse **owned before marriage**, or acquired during marriage by
  **gift, devise, or descent**, plus certain **personal-injury recoveries** (other than for lost
  earning capacity), is separate. Separate property is **confirmed** to the owning spouse and is
  **not divided** — the court divides only the **community** estate.
- **Commingling and tracing.** Separate property **commingled** with community funds so that it can
  no longer be traced may lose its separate character; the spouse asserting a separate interest bears
  the **tracing** burden (clear and convincing). Address tracing expressly.
- **Reimbursement and economic contribution.** Where the **community estate** funds improvements to,
  or pays down debt on, a **separate** asset (or vice versa), a **claim for reimbursement** can arise
  (Tex. Fam. Code Ch. 3, Subchapter E). Plead any reimbursement claim and identify the contributing
  and benefited estates.

### Step 2 — Divide the community ("just and right")

At divorce the court divides the **community estate** in a manner it deems **"just and right,"**
having due regard for the rights of each party and any children — **Ch. 7 (§ 7.001)**. The division
**need not be equal**; the court may order a **disproportionate** division on factors such as fault
in the breakup, disparity of earning capacity, education, health, who has custody of the children,
and wasting of community assets. Separate property is confirmed to its owner; the court also
**allocates community debts**. Confirm the controlling articulation and any "just and right" factors
in `../tx-law-references/references/tx-statutes-debt/`.

## Conservatorship and possession (Tex. Fam. Code Ch. 153)

Texas frames child issues as **conservatorship** (rights and duties / decision-making) and
**possession and access** (the time-sharing schedule), all decided on the **best interest of the
child**.

### Conservatorship — the joint-managing presumption (§ 153.131)

- **Managing vs. possessory conservators.** The court appoints **managing conservator(s)** (who hold
  the bundle of parental rights and duties) and may appoint a **possessory conservator**.
- **Joint-managing-conservator presumption — § 153.131.** Unless rebutted, it is a **rebuttable
  presumption** that appointing the parents as **joint managing conservators** is in the child's
  best interest. The presumption is **removed** by a finding of a **history of family violence**
  (§ 153.004), which also restricts conservatorship and possession. Joint managing conservatorship
  does **not** mean equal possession — the **possession schedule** is set separately.

### Possession and access — the Standard Possession Order (§ 153.252)

- **Standard Possession Order (SPO) — § 153.252.** For a child **3 and older**, the SPO is the
  **statutory presumptive schedule** (the familiar first/third/fifth-weekend, Thursday, alternating
  holiday, and extended-summer framework, with an **expanded SPO** election affecting pickup/return
  times). The SPO is **presumed** to be in the child's best interest and to provide **reasonable
  minimum possession**; deviations require findings. Different rules apply for **children under 3**
  (§ 153.254) and where **distance between the parties** is significant (§ 153.312 et seq.).
- **Best interest — the *Holley* factors.** Best interest is guided by the **non-exclusive *Holley*
  factors** (*Holley v. Adams*, 544 S.W.2d 367 (Tex. 1976)) — the child's desires, the child's
  present and future emotional and physical needs, any danger to the child, the parental abilities
  of those seeking custody, available programs, the parties' plans for the child, the stability of
  the proposed home, acts or omissions of a parent, and any excuse for them. (This is a **stable**
  case cite.) In a contested case the court makes findings on the relevant factors.

## Child support (Tex. Fam. Code Ch. 154) — percentage-of-net-resources guidelines

Texas child support uses a **percentage-of-the-obligor's-net-resources** guideline model
(distinct from an income-shares model): the guideline applies a **percentage to the obligor's
monthly net resources** that **steps up by the number of children** before the court.

- **Net resources.** Start from the obligor's **gross resources** (wages, self-employment income,
  and the categories listed in **§ 154.062**), then subtract the statutory deductions (income taxes
  for a single person, Social Security / mandatory retirement, union dues, and the cost of the
  child's health- and dental-insurance) to reach **monthly net resources**.
- **The guideline percentages — § 154.125.** A guideline percentage is applied to net resources,
  **increasing with the number of children** before the court (with adjustments under **§§ 154.128–154.129**
  when the obligor supports children in more than one household). State the model qualitatively; do
  **not** rely on a remembered percentage table — confirm the current percentages against
  `../tx-law-references/references/tx-statutes-debt/`.
- **The cap on net resources — do NOT hard-code.** The guideline percentages apply only up to a
  **statutory cap on monthly net resources** (§ 154.125); above the cap, support requires proof of
  the child's **proven needs**. The cap dollar figure is **adjusted every six years** by the Title
  IV-D agency for inflation — **point to the corpus and verify the current cap**; never embed the
  dollar amount as a load-bearing fact.
- **Income withholding.** Support is enforced primarily by an **order / writ of withholding from
  earnings** (Ch. 158) — wage withholding for child support is an **exception** to the general
  protections on wages. Medical and dental support are ordered alongside (§ 154.181 et seq.).
- **Modification.** A support order may be modified on a **material and substantial change in
  circumstances** since the order, **or** if it has been **3 years** since the order and the
  guideline amount would differ from the current order by the statutory threshold (a **percentage or
  dollar** threshold — confirm against the corpus) — **§ 156.401**.

> The guideline percentages, the **net-resources cap**, the multi-family adjustment, and the
> deduction rules are **amended periodically** (and the cap is re-indexed every six years) — always
> run the **current** Texas guidelines and figures rather than relying on stale numbers. See
> `../tx-law-references/references/tx-statutes-debt/` (Tex. Fam. Code Ch. 154) and `tx-law-references`
> for the controlling numbers.

## Spousal maintenance (Tex. Fam. Code Ch. 8)

Texas court-ordered **spousal maintenance** is **narrowly available** — Texas does not have liberal
"alimony." The spouse seeking maintenance must clear an **eligibility gate** (§ 8.051) and then the
court sets amount and duration subject to **statutory caps**.

- **Eligibility — § 8.051.** The spouse seeking maintenance must lack sufficient property
  (including separate property awarded in the divorce) to provide for their **minimum reasonable
  needs**, **and** fall into a qualifying category: (1) the other spouse was convicted of or received
  deferred adjudication for **family violence** within the statutory window; (2) the marriage lasted
  **10 years or longer** and the seeking spouse lacks the ability to earn sufficient income for
  minimum reasonable needs; (3) the seeking spouse cannot earn sufficient income due to an
  **incapacitating physical or mental disability**; or (4) the seeking spouse is the custodian of a
  child of the marriage who requires substantial care due to a disability.
- **Caps on amount and duration — §§ 8.054, 8.055 — do NOT hard-code.** The **duration** of
  maintenance is capped on a sliding scale tied to the **length of the marriage** (with exceptions
  for disability), and the **monthly amount** is capped by statute at the lesser of a **dollar
  ceiling** or a **percentage of the obligor's average monthly gross income**. The dollar ceiling and
  the percentage are **drift-prone** — **point to the corpus and verify the current figures**; do not
  embed them. The court weighs the **§ 8.052** factors (education, employment skills, duration of the
  marriage, age, earning ability, contributions as homemaker, marital misconduct, etc.) in setting
  amount and duration within the caps.
- **Contractual alimony.** Parties may **agree** to support beyond the statutory maintenance limits
  by **contract** (often incorporated into the decree) — a separate animal from court-ordered
  Ch. 8 maintenance.

## Informal (common-law) marriage (Tex. Fam. Code § 2.401)

**Texas recognizes informal (common-law) marriage.** Under **§ 2.401**, an informal marriage is
established either by (a) a signed, **registered Declaration of Informal Marriage**, or (b) proof
that the couple **agreed to be married**, **and after the agreement lived together** in Texas as
spouses, **and represented to others** (held out) that they were married. All three elements of the
proof route must be shown.

- **Why it matters.** An informal marriage is a **valid marriage** — it must be dissolved by
  **divorce**, and it carries the same **community-property** and support consequences. Screen for it
  whenever an unmarried couple separates after living together.
- **The two-year presumption.** If a proceeding to prove an informal marriage is **not commenced
  within two years** after the parties separated and ceased living together, there is a **rebuttable
  presumption** that the parties did not enter into an agreement to be married (§ 2.401(b)) —
  pin the separation date.
- A party asserting an informal marriage must **plead and prove** its formation; a party denying it
  contests the three elements (or invokes the two-year presumption).

## Suit Affecting the Parent-Child Relationship (SAPCR)

A **SAPCR** is the Texas vehicle for establishing or modifying **conservatorship, possession and
access, child support, and medical/dental support** — whether brought standalone (e.g., by unmarried
parents, after a paternity finding under Ch. 160, or by a qualifying non-parent with standing under
§ 102.003) or as part of a divorce that involves children. The conservatorship (Ch. 153) and child
support (Ch. 154) rules above govern the merits of a SAPCR. **Standing** to file a SAPCR is itself a
threshold issue (§ 102.003) — confirm the petitioner's standing category.

## Jurisdiction over children and interstate cases

- **UCCJEA — Tex. Fam. Code Ch. 152.** Governs **subject-matter jurisdiction** over child-custody
  (conservatorship / possession) determinations. The child's **home state** generally controls.
  Plead the UCCJEA jurisdictional allegations and the required information about the child's
  residences for the prior period in the petition (the **§ 152.209** information statement).
- **UIFSA — Tex. Fam. Code Ch. 159.** Governs interstate **child-support** establishment,
  modification, and enforcement, including registration of out-of-state orders and the
  **continuing, exclusive jurisdiction** rules that decide which state may modify a support order.

## Protective orders / family violence (Title 4, Ch. 81–88)

Civil **protective orders** for **family violence** are issued under **Title 4 (Ch. 81–88)** of the
Family Code — a **separate procedural track** from a divorce or SAPCR, though they are commonly
sought alongside one. A **finding of family violence** can **remove the joint-managing-conservator
presumption** (§ 153.131) and restrict conservatorship and possession (§ 153.004), so coordinate any
protective order with the parenting provisions across the cases. **Temporary ex parte** orders
(Ch. 83) are available on a showing of a clear and present danger; final protective orders follow a
hearing. The procedural mechanics live in `tx-family-court`; this skill addresses the substantive
overlay on conservatorship and possession.

## Drafting checklist

- [ ] Forum / venue correct (District Court — or designated family district court — of the county of
      proper venue); associate-judge referral noted — see `tx-family-court`
- [ ] Parties styled **Petitioner / Respondent**; **Original Petition for Divorce** (or annulment /
      void / SAPCR) drafted; TRCP 47(c) statement of relief range included where required
- [ ] Divorce ground pleaded — **insupportability (§ 6.001)** **or** a specific **§§ 6.002–6.007**
      fault ground with supporting facts
- [ ] **Residency (§ 6.301)** alleged (6 months state / 90 days county); **60-day waiting period
      (§ 6.702)** calendared with `tx-deadlines`
- [ ] Property **characterized** (community presumption § 3.003; separate property proven by clear
      and convincing evidence) with **tracing** and any **reimbursement** claim addressed before
      proposing a **"just and right"** division (Ch. 7); community debts allocated
- [ ] Conservatorship framed to the **joint-managing presumption (§ 153.131)**; any **family-violence
      (§ 153.004)** finding addressed; possession set to the **Standard Possession Order (§ 153.252)**
      or a supported deviation; best interest analyzed under the ***Holley*** factors
- [ ] Child support run on the **current** Texas guidelines (Ch. 154 percentage-of-net-resources):
      net resources computed (§ 154.062 / § 154.125), the **net-resources cap verified against the
      corpus (not hard-coded)**, income withholding (Ch. 158) and medical/dental support included;
      any deviation supported by findings
- [ ] Spousal maintenance analyzed under **Ch. 8** — **eligibility gate (§ 8.051)** first, then
      amount/duration within the **statutory caps (§§ 8.054–8.055) verified against the corpus**, on
      the § 8.052 factors
- [ ] Informal-marriage facts screened against **§ 2.401** (agreement + cohabitation + holding out,
      or registered declaration; two-year presumption) where the parties were unmarried
- [ ] UCCJEA (**Ch. 152**, incl. the § 152.209 information statement) / UIFSA (**Ch. 159**)
      allegations included where there is an interstate element
- [ ] Any companion **protective order** routed on its **separate Title 4 (Ch. 81–88)** track and
      coordinated with conservatorship / possession (see `tx-family-court`)

## Composition

- For format and the family-case caption: `tx-statewide-format`
- For the District Court / family district court venue, the associate-judge process, mandatory
  disclosures, e-filing, and the protection-order procedure: `tx-family-court`
- For the county / clerk / court assignment: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`
- For drafting the petition / answer / counterpetition / motion: `tx-draft-motion`
- For sworn affidavits / unsworn declarations (CPRC § 132.001) and financial information statements:
  `tx-draft-declaration`
- For a proposed decree / order: `tx-draft-order`, `tx-submit-order`
- For pro se conventions and self-represented intake: `tx-pro-se`
- For the waiting period and other deadlines: `tx-deadlines`
- For hearings and oral argument: `tx-hearings`; for scheduling: `tx-schedule-hearing`
- For citation verification: `tx-fact-check`
- For pre-filing quality control and packet assembly: `tx-quality-check`, `tx-file-packet`
- For canonical Tex. Fam. Code text, the Texas child-support guidelines, and the TRCP:
  `tx-law-references`

## References

- `../tx-law-references/references/tx-statutes-debt/` and the Tex. Fam. Code corpus — divorce grounds
  (§§ 6.001–6.007), residency (§ 6.301) and the 60-day waiting period (§ 6.702); community-property
  presumption (§ 3.003) and "just and right" division (Ch. 7); conservatorship and possession
  (Ch. 153 — §§ 153.004, 153.131, 153.252); child support (Ch. 154 — §§ 154.062, 154.125, 154.129;
  modification § 156.401; withholding Ch. 158); spousal maintenance (Ch. 8 — §§ 8.051, 8.052,
  8.054, 8.055); informal marriage (§ 2.401); SAPCR standing (§ 102.003); UCCJEA (Ch. 152) and
  UIFSA (Ch. 159); protective orders (Title 4, Ch. 81–88)
- `../tx-law-references/references/court-rules/` — the Texas Rules of Civil Procedure governing
  family suits (no separate family-court trial court; procedure is the TRCP), including TRCP 47(c)
  (statement of relief), 92 (general denial), and 99 (Monday-rule answer in District / County Court)
- Self-help forms: **TexasLawHelp.org** carries the statewide guided family-law forms (divorce with
  and without children, SAPCR, protective orders); the District / County Clerk and any Court
  Assistance resources are detailed in `tx-family-court`
