---
name: ga-family-law-codearranger
title: Georgia Family Law — Divorce, Custody, Child Support, Alimony
description: 'Use for Georgia family-law matters — divorce, equitable division of marital property, child custody, parenting plans, child support, alimony, family-violence protective orders, legitimation, and paternity. Covers the 13 grounds for divorce (O.C.G.A. § 19-5-3) including no-fault "irretrievably broken", the 6-month residency rule (§ 19-5-2), equitable distribution (*Stokes*; § 19-5-13), the income-shares child-support guidelines (§ 19-6-15), best-interests custody with the mandatory parenting plan (§§ 19-9-3, 19-9-1) and the age-14 child-election quirk, alimony with the adultery/desertion bar (§§ 19-6-1, 19-6-5), the Family Violence Act / TPO (§ 19-13-1 et seq.), the UCCJEA (§§ 19-9-40 to 19-9-104), UIFSA, common-law marriage abolition (§ 19-3-1.1), and legitimation vs. paternity (§§ 19-7-22, 19-7-40). Triggers: "file for divorce in Georgia", "Georgia child support calculator", "equitable division", "custody best interests Georgia", "modify alimony", "TPO Georgia".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Georgia Family Law — Divorce, Custody, Child Support, Alimony

> **NOT LEGAL ADVICE.** This subject-matter bundle describes
> a procedural and substantive framework for Georgia cases in
> this area, not legal advice and not strategic advice for
> any specific case. Outcomes are fact-specific; the choice
> of defenses, claims, motions, and discovery belongs to the
> litigant (and any counsel the litigant retains). Verify
> every rule, deadline, and citation against current law
> before filing. Family-law cases carry significant
> long-term consequences for property, children, and finances
> — strongly consider consulting a licensed Georgia
> family-law attorney even on a "simple" divorce.

This bundle covers the principal Georgia domestic-relations matters:
**divorce** (dissolution of marriage), **equitable division of
property**, **child custody and parenting plans**, **child support**,
**alimony** (spousal support), **family-violence protective orders**,
**legitimation**, and **paternity**.

Georgia family law is codified primarily in **O.C.G.A. Title 19**
(Domestic Relations). Divorce, custody, alimony, and equitable
division are heard in the **Superior Court** (O.C.G.A. § 19-5-1).
Procedure runs on the Georgia Civil Practice Act (O.C.G.A. Title 9,
Ch. 11) and the Uniform Superior Court Rules.

## Snapshot — Georgia family-law principles

- **Divorce grounds**: O.C.G.A. § 19-5-3 lists **13 grounds** — 12
  fault grounds plus the no-fault ground (#13) that the marriage is
  **"irretrievably broken."** *Harwell v. Harwell*, 233 Ga. 89
  (1974), construes "irretrievably broken." A no-fault petition under
  § 19-5-3(13) cannot result in a divorce **until at least 30 days
  after the date of service** on the respondent.
- **Residency**: a party must have been a **bona fide resident of
  Georgia for six months** before filing (O.C.G.A. § 19-5-2). A
  person stationed on a Georgia military post for one year is treated
  as a resident.
- **Venue**: Superior Court of the **respondent's county** of
  residence (O.C.G.A. § 19-5-2; constitutional venue for divorce).
- **Parties**: in a Georgia divorce the moving party is the
  **PETITIONER** and the other spouse is the **RESPONDENT**.
- **Property — equitable distribution**: Georgia is an
  **equitable-distribution** state, **not** a community-property
  state. *Stokes v. Stokes*, 246 Ga. 765, 273 S.E.2d 169 (1980),
  recognized equitable division of marital property; § 19-5-13
  governs the award. **Separate property** (gifts, inheritance, and
  pre-marital assets) is generally **not** divided (O.C.G.A.
  § 19-3-9) unless it has been **commingled** into the marital
  estate.
- **Child support — income shares**: O.C.G.A. § 19-6-15 uses the
  **income-shares** model. Combine both parents' adjusted gross
  monthly income, apply the **Basic Child Support Obligation (BCSO)**
  table, then prorate by each parent's income share.
- **Custody — best interests**: O.C.G.A. § 19-9-3. **No presumption**
  in favor of either parent or any form of custody; the **judge (not
  a jury)** decides; a **parenting plan is mandatory** (§ 19-9-1).
- **Alimony — discretionary**: O.C.G.A. § 19-6-1 et seq. Alimony is
  **authorized, not mandatory**, and is **barred** where the
  separation was caused by the seeking party's **adultery or
  desertion** (§ 19-6-1(b)).
- **Jurisdiction over children**: the **UCCJEA** (O.C.G.A.
  §§ 19-9-40 to 19-9-104) governs which state may decide custody;
  **UIFSA** (O.C.G.A. §§ 19-11-100 to 19-11-191) governs interstate
  support.
- **Common-law marriage**: **abolished prospectively** — no
  common-law marriage may be entered in Georgia **on or after
  January 1, 1997** (O.C.G.A. § 19-3-1.1); valid pre-1997 common-law
  marriages remain recognized.

## Filing path — Superior Court

Georgia divorce, custody, alimony, and equitable-division actions are
filed in the **Superior Court** (O.C.G.A. § 19-5-1), normally in the
county where the **respondent resides** (O.C.G.A. § 19-5-2). Some
high-volume circuits operate a dedicated **Family Division** by local
rule (Fulton and DeKalb have standing Family Divisions; Cobb and
Gwinnett run family case-management tracks). Family-division
assignment and local domestic-relations forms are **venue-specific** —
cross-reference `ga-family-court` and the relevant county venue skill.

## Case types within domestic relations

| Case type | Statute | When to use |
|---|---|---|
| Divorce (dissolution of marriage) | O.C.G.A. § 19-5-1 et seq. | Spouses seeking to legally end a valid marriage |
| Custody / parenting plan | O.C.G.A. §§ 19-9-1, 19-9-3 | Determination or modification of legal/physical custody and a parenting plan |
| Child support (establishment / modification) | O.C.G.A. § 19-6-15 | Establish or modify a support obligation |
| Alimony | O.C.G.A. § 19-6-1 et seq. | Spousal support during or after divorce |
| Family-violence protective order (TPO) | O.C.G.A. § 19-13-1 et seq. | Protection from a family or household member |
| Legitimation | O.C.G.A. § 19-7-22 | An unwed biological father seeking parental rights |
| Paternity | O.C.G.A. § 19-7-40 et seq. | Establish biological fatherhood (chiefly for support) |

## Divorce — the standard path

### Step 1 — Verify grounds, residency, and venue

- **Grounds (O.C.G.A. § 19-5-3)**: thirteen grounds are available —
  twelve fault grounds (including adultery, desertion, cruel
  treatment, habitual intoxication, and others enumerated in the
  statute) and the no-fault ground that the marriage is
  **"irretrievably broken"** (§ 19-5-3(13)). Most pro se petitions
  proceed on the no-fault ground. *Harwell v. Harwell*, 233 Ga. 89
  (1974), is the controlling construction of "irretrievably broken."
- **Residency (O.C.G.A. § 19-5-2)**: confirm six months of bona fide
  Georgia residency before filing. The court will dismiss for lack of
  jurisdiction if the residency requirement is not met.
- **Venue**: file in the Superior Court of the **respondent's
  county**.

### Step 2 — File the Petition for Divorce

The **Petition for Divorce** identifies the parties (PETITIONER and
RESPONDENT), the marriage date, the date and county of separation,
any minor children, the grounds relied on, and the relief sought
(equitable division, alimony, custody, child support, restoration of
a former name, attorney's fees). Many circuits provide approved pro
se divorce packets; venue-specific forms are tracked in
`references/forms.md` and the venue skills.

### Step 3 — Serve the Respondent

Service follows the Georgia Civil Practice Act (O.C.G.A. Title 9,
Ch. 11). The **30-day clock** embedded in § 19-5-3(13) runs from the
**date of service** — a no-fault divorce cannot be granted until at
least 30 days after the respondent is served. Where the respondent
acknowledges service and consents, an **uncontested** divorce can be
finalized shortly after the 30-day minimum; defaults and
service-by-publication cases take longer.

### Step 4 — Temporary (pendente lite) relief

Either party may seek **temporary alimony, temporary child support,
temporary custody, exclusive use of the marital residence, and
restraints on dissipating assets** while the case is pending. The
temporary-alimony authority is O.C.G.A. § 19-6-3; attorney's fees in
divorce/alimony actions are authorized by § 19-6-2.

### Step 5 — Financial disclosure and discovery

The parties exchange financial information needed to value the
marital estate and run the child-support worksheet. Use
`ga-discovery` for the mechanics; the child-support worksheet inputs
are described below.

### Step 6 — Resolution: settlement agreement or trial

- **Uncontested / settled**: the parties sign a **Settlement
  Agreement** (and a **Parenting Plan** if there are children); the
  court can enter the **Final Judgment and Decree of Divorce** after
  the 30-day minimum.
- **Contested**: the court (judge, **not** a jury, decides custody)
  resolves equitable division, alimony, custody, and child support at
  a final hearing or bench trial. Either party may demand a jury on
  the issues a jury may hear in Georgia divorce (e.g., certain
  property/alimony questions), but **custody is decided by the
  judge** (§ 19-9-3).

### Step 7 — Final Judgment and Decree

The decree confirms jurisdiction and residency, dissolves the
marriage, divides marital property and debt equitably, sets alimony
(if any), incorporates the Parenting Plan and a child-support order
with the worksheet attached, and restores a former name if requested.

## Equitable division of property — O.C.G.A. § 19-5-13

Georgia divides **marital property equitably** — meaning **fairly**,
which is **not necessarily equally**. *Stokes v. Stokes*, 246 Ga.
765, 273 S.E.2d 169 (1980), established equitable division as
Georgia's regime; § 19-5-13 governs the equitable award.

### Marital vs. separate property

- **Marital property** — assets and debts acquired during the
  marriage by the labor or investment of either spouse — is subject
  to equitable division.
- **Separate property** — **gifts, inheritances, and pre-marital
  assets** belonging to one spouse — is generally **not** divided
  (O.C.G.A. § 19-3-9). The classic pitfall is **commingling**:
  separate property that is mixed into the marital estate (e.g.,
  inheritance deposited into a joint account and used for marital
  purposes) can lose its separate character and become divisible.

### How the court divides

The court considers the contributions of each spouse (including
homemaking and child-rearing), the conduct of the parties toward the
marital estate, the relative needs and circumstances of the parties,
and other equitable factors. Document the **source and tracing** of
any asset claimed as separate.

## Child support — O.C.G.A. § 19-6-15 (income-shares)

> ⚠ **A revised O.C.G.A. § 19-6-15 took effect January 1, 2026, and
> is now the controlling statute.** Pull the **current** (post-Jan. 1,
> 2026) text of § 19-6-15 and use the current worksheet and tables —
> do not rely on figures or worksheet layouts from earlier versions.

Georgia uses the **income-shares** model. The mechanics:

1. Determine each parent's **adjusted gross monthly income**.
2. **Combine** both parents' adjusted gross income.
3. Apply the **Basic Child Support Obligation (BCSO) table** to the
   combined income and the number of children to find the presumptive
   basic obligation. *(Verify current BCSO amounts against the
   post-Jan. 1, 2026 § 19-6-15 schedule.)*
4. **Prorate** the basic obligation between the parents in proportion
   to each parent's share of the combined income.
5. Apply **adjustments / add-ons**: the cost of the child's **health
   insurance**, **work-related child care**, and a **parenting-time
   adjustment**.

The result is the **rebuttable presumptive** amount. A court may
**deviate** from the presumptive amount, but a deviation requires
**written findings** explaining the basis and why the deviation
serves the child's best interest. A **self-support reserve /
low-income adjustment** protects a low-earning obligor.

### Use the official calculator

The **Georgia Child Support Commission** publishes the official
**online child-support calculator and worksheet**
(csconlinecalc.georgiacourts.gov). Courts expect the worksheet to be
completed and submitted; run the numbers with the calculator and
attach the worksheet to the order. *(Confirm the calculator reflects
the post-Jan. 1, 2026 § 19-6-15 revisions before relying on output.)*

### Modification — O.C.G.A. § 19-6-15(k)

A child-support order may be **modified** on a substantial change in
circumstances. Section 19-6-15(k) recognizes modification where a
parent has suffered an **involuntary loss of income of 25% or more**,
among other triggers. Verify the current modification provisions in
the post-Jan. 1, 2026 statute.

## Custody and parenting plans — O.C.G.A. §§ 19-9-1, 19-9-3

### Best-interests standard

Custody is decided by the **best interests of the child** (O.C.G.A.
§ 19-9-3). There is **no presumption** favoring either parent or any
particular custody arrangement, and the **judge — not a jury —**
decides custody. The court weighs the statutory factors at
**§ 19-9-3(a)(3)** (the parent-child bond, each parent's capacity to
provide for the child, home stability, the child's adjustment, and
the like). Where family violence is present, the child's **safety is
the primary consideration** (§ 19-9-3(a)(4)).

### Mandatory parenting plan — O.C.G.A. § 19-9-1

A **parenting plan is mandatory** in any case involving custody. The
plan must address the **physical-custody schedule** (regular,
holiday, and vacation time), **decision-making authority** (education,
health, religion, extracurriculars), **transportation/exchange
arrangements**, and how the parents will resolve future disputes.

### Child election — the Georgia age-14 quirk

Georgia gives older children a statutory voice in custody:

- **Age 14 and older (§ 19-9-3(a)(5))**: a child **may select** the
  parent with whom the child wishes to live, and that **selection is
  controlling unless the selected parent is determined not to be in
  the child's best interest**. A child's election can constitute a
  **material change in circumstances** sufficient to seek
  modification — but the election may be exercised to modify custody
  **only once within a two-year period**.
- **Ages 11–13 (§ 19-9-3(a)(6))**: the court **considers** the
  child's desires and educational needs, but the child's choice is
  **not controlling**, and the child's wishes **alone do not
  constitute a material change** in circumstances.
- **Under 11**: the court may consider the child's wishes in its
  discretion, but is not required to.

### Modification of custody

Modification requires a **material change in circumstances**
affecting the child's welfare, after which the court re-applies the
best-interests standard. Section 19-9-3(i) provides protections
related to a parent's **military deployment**.

## Alimony — O.C.G.A. § 19-6-1 et seq.

### Authorized, not mandatory

Alimony is an **allowance for support** that a court **may** award —
it is **discretionary, not mandatory** (O.C.G.A. § 19-6-1(a)). Either
spouse may be the obligor.

### The adultery / desertion bar — § 19-6-1(b)

Alimony is **barred** to a party whose **adultery or desertion caused
the separation**, proved by a **preponderance of the evidence**
(O.C.G.A. § 19-6-1(b)). This fault bar is a distinctive Georgia
feature — the conduct must be the cause of the separation.

### The eight factors — § 19-6-5

When alimony is allowed, the amount and duration turn on the
**eight statutory factors** (O.C.G.A. § 19-6-5): the standard of
living during the marriage; the duration of the marriage; the age and
physical/emotional condition of each party; the financial resources
of each party; the time needed to acquire education or training to
find employment; the contributions of each party to the marriage
(including homemaking, child care, and assistance to the other
spouse's career); the earning capacity and fixed liabilities of each
party; and any other relevant equitable factors.

### Temporary alimony and fees

**Pendente lite (temporary) alimony** while the case is pending is
authorized by O.C.G.A. § 19-6-3; **attorney's fees** in divorce and
alimony actions are authorized by O.C.G.A. § 19-6-2.

### Termination and modification — § 19-6-19

Alimony **terminates upon the remarriage** of the recipient.
Post-decree, alimony is **modifiable** on a change in circumstances
under O.C.G.A. § 19-6-19, which also includes the Georgia
**cohabitation ("live-in lover") provision** — voluntary cohabitation
of the recipient with a third party in a meretricious relationship
can support modification or termination.

## Family-violence protective orders (TPO) — O.C.G.A. § 19-13-1 et seq.

The **Family Violence Act** provides civil protective orders for
victims of family violence.

- **Definition and qualifying relationships (§ 19-13-1)**: "family
  violence" covers certain acts — simple assault, battery, stalking,
  criminal damage to property, unlawful restraint, criminal trespass,
  and any felony — committed between people in a **qualifying
  relationship** (current or former spouses, parents of the same
  child, parents and children, stepparents and stepchildren, foster
  parents and foster children, and others living or formerly living
  in the same household). **Reasonable parental discipline is
  excluded.**
- **Venue (§ 19-13-2)**: the petition is generally filed where the
  **respondent resides**.
- **Ex parte TPO (§ 19-13-3)**: the court may issue an **ex parte
  temporary protective order** lasting **up to 30 days**, with a
  hearing required before the order can be extended.
- **Protective order (§ 19-13-4)**: after a hearing, the court may
  enter a protective order for **up to one year**, **extendable to
  three years or made permanent**. Available relief includes
  **no-contact** directives, **exclusive use of the residence**,
  **temporary custody and visitation**, **temporary support**, and
  **possession of property**.
- **No filing fee**; the **GSCCCA** publishes the standard TPO forms
  (the SC-15 / SC-16 series). Cross-reference `references/forms.md`.

## Jurisdiction over children and interstate support

### UCCJEA — O.C.G.A. §§ 19-9-40 to 19-9-104

The **Uniform Child Custody Jurisdiction and Enforcement Act**
determines which state may make or modify a custody determination.
The general rule is **home-state jurisdiction** (O.C.G.A. § 19-9-61) —
the state where the child has lived with a parent for the six months
before the proceeding. **Temporary emergency jurisdiction** exists
where the child is present in Georgia and is abandoned or needs
protection from mistreatment or abuse (O.C.G.A. § 19-9-64).

### UIFSA — O.C.G.A. §§ 19-11-100 to 19-11-191

The **Uniform Interstate Family Support Act** governs the
**establishment, enforcement, and modification of support orders
across state lines** and the rule of **continuing, exclusive
jurisdiction** over a support order.

## Common-law marriage — O.C.G.A. § 19-3-1.1

Georgia **abolished common-law marriage prospectively**: **no**
common-law marriage may be **entered in Georgia on or after January
1, 1997** (O.C.G.A. § 19-3-1.1). Common-law marriages **validly
formed before January 1, 1997** remain recognized. A party asserting
a pre-1997 common-law marriage in a divorce must plead and prove its
formation.

## Legitimation vs. paternity

These are **different** proceedings and are frequently confused.

- **Legitimation — O.C.G.A. § 19-7-22**: legitimation is the
  Superior Court process by which the **biological father of a child
  born out of wedlock obtains legal parental rights** (custody,
  visitation, inheritance). Apart from marrying the mother or a valid
  voluntary acknowledgment of legitimation, **legitimation is the
  only way an unwed biological father acquires parental rights.**
  Section 19-7-22(h) also addresses third-party legitimation.
- **Paternity — O.C.G.A. §§ 19-7-40, 19-7-43**: paternity establishes
  the **biological fact** of fatherhood, chiefly so a **support
  obligation** can be imposed.
- **Key point**: **paternity is not legitimation.** Establishing
  paternity (e.g., for child support) does **not** by itself confer
  custody or visitation rights on the father — the father must
  **legitimate** the child to obtain those rights.

## Common pro se mistakes

1. **Filing before meeting the six-month residency** (§ 19-5-2) —
   the court will dismiss for lack of jurisdiction.
2. **Expecting an instant no-fault divorce** — § 19-5-3(13) bars a
   divorce until at least **30 days after service**.
3. **Treating Georgia as a community-property (50/50) state** — it is
   **equitable distribution**; division is fair, not automatically
   equal (*Stokes*; § 19-5-13).
4. **Losing separate property through commingling** — keep
   gift/inheritance/pre-marital assets segregated and traceable
   (§ 19-3-9).
5. **Skipping the official child-support worksheet** — courts require
   the Georgia Child Support Commission worksheet; run the current
   (post-Jan. 1, 2026) § 19-6-15 calculator.
6. **Omitting a parenting plan** — a parenting plan is **mandatory**
   in any custody case (§ 19-9-1).
7. **Assuming a 14-year-old's choice always controls** — the
   selection is controlling **only if** the selected parent is in the
   child's best interest, and the election may modify custody only
   **once every two years** (§ 19-9-3(a)(5)).
8. **Seeking alimony after one's own adultery or desertion caused the
   separation** — alimony is **barred** (§ 19-6-1(b)).
9. **Establishing paternity and assuming it grants visitation** — an
   unwed father must **legitimate** (§ 19-7-22), not merely establish
   paternity, to obtain custody/visitation.

## Composition

- For statewide format baseline: `ga-statewide-format`
- For the dedicated Family Division and family-court procedure:
  `ga-family-court`
- For the specific venue (Family-Division assignment, local
  domestic-relations forms): `ga-fulton`, `ga-cobb`, `ga-gwinnett`
- For drafting the petition / motion: `ga-draft-motion`
- For affidavits / declarations: `ga-draft-declaration`
- For the proposed final decree / order: `ga-draft-order`
- For time computation and Georgia holidays (the 30-day post-service
  minimum, answer deadlines): `ga-deadlines`
- For citation verification: `ga-fact-check`
- For pre-filing format + content QC: `ga-quality-check`

## References

- `references/dissolution.md` — divorce grounds (§ 19-5-3), residency
  (§ 19-5-2), venue, the 30-day post-service minimum, and the
  step-by-step procedure
- `references/property-distribution.md` — equitable division
  (*Stokes*; § 19-5-13), marital vs. separate property, and
  commingling (§ 19-3-9)
- `references/child-support.md` — income-shares mechanics, BCSO
  table, add-ons, deviations, and modification (§ 19-6-15; flag the
  Jan. 1, 2026 revision)
- `references/parenting-plan.md` — mandatory parenting-plan elements
  (§ 19-9-1) and a Georgia-style scaffold
- `references/alimony.md` — discretionary award, the adultery /
  desertion bar, the eight factors, termination, and modification
  (§§ 19-6-1, 19-6-3, 19-6-5, 19-6-19)
- `references/family-violence-tpo.md` — Family Violence Act, ex parte
  TPO, protective-order relief and duration (§ 19-13-1 et seq.)
- `references/uccjea.md` — home-state and emergency custody
  jurisdiction (§§ 19-9-40 to 19-9-104)
- `references/uifsa.md` — interstate establishment, enforcement, and
  modification of support (§§ 19-11-100 to 19-11-191)
- `references/legitimation-paternity.md` — legitimation (§ 19-7-22)
  vs. paternity (§§ 19-7-40, 19-7-43) and why they differ
- `references/common-law-marriage.md` — prospective abolition and the
  pre-1997 carve-out (§ 19-3-1.1)
- `references/forms.md` — annotated index of Georgia and venue
  domestic-relations forms (divorce petition, parenting plan,
  child-support worksheet, GSCCCA TPO SC-15/SC-16 series)
- `references/examples/` — worked Georgia examples
