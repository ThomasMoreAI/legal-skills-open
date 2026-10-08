---
name: tn-family-law-codearranger
title: Tennessee Family Law — Title 36
description: 'Subject-matter bundle for Tennessee family-law matters. Covers Title 36: divorce grounds + procedure (§ 36-4-101 fault/irreconcilable-differences; § 36-4-103 60/90-day waiting period); equitable distribution (§ 36-4-121); income-shares child support (§ 36-5-101 + current Guidelines); four alimony types with rehabilitative/transitional preference (§ 36-5-121); permanent parenting plans + best-interest factors (§§ 36-6-401, 36-6-106); relocation (post-2018 § 36-6-108 60-day notice framework); UCCJEA jurisdiction (§ 36-6-201 et seq.); UIFSA interstate enforcement (§ 36-5-2001 et seq.); parentage/paternity; orders of protection (§ 36-3-601 et seq.); no Tennessee common-law marriage. For venue mechanics use `tn-family-court`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Tennessee Family Law — Title 36

> **NOT LEGAL ADVICE.** Family-law cases carry long-term
> consequences for property, children, and finances. Strongly
> consider consulting a licensed Tennessee family-law attorney
> even on a "simple" or "agreed" divorce. Generated content is a
> drafting aid; verify against current statutes, the current
> child-support Guidelines, and case law before filing.

This subject-matter bundle covers the substantive Tennessee
domestic-relations law of **Title 36** of the Tennessee Code:
**divorce**, **annulment**, **legal separation**, **equitable
distribution**, **child support**, **alimony**, the **permanent
parenting plan**, **parentage / paternity**, **relocation**, and
**orders of protection**. It supplies the law; the venue mechanics
live in `tn-family-court` (Circuit / Chancery) and `tn-juvenile-court`
(Title 37), and document format lives in `tn-statewide-format`.

## Snapshot — Tennessee family-law principles

- **Divorce is both fault and no-fault.** Tennessee recognizes
  approximately **fifteen fault grounds** plus the no-fault ground
  of **irreconcilable differences** — all listed at **Tenn. Code
  Ann. § 36-4-101**. The irreconcilable-differences procedure is at
  **§ 36-4-103**.
- **Mandatory waiting period.** For an irreconcilable-differences
  divorce, the complaint must be on file at least **60 days** before
  a hearing if the parties have **no unmarried minor child**, and at
  least **90 days** if there **is** an unmarried child under 18 —
  **§ 36-4-103(a)**. (This is the waiting period, not a residency
  rule; do not confuse it with § 36-4-101.)
- **Equitable distribution — NOT community property.** Marital
  property is **classified** (marital vs. separate) and the marital
  estate is then **divided equitably** — not necessarily equally —
  under the factors at **§ 36-4-121(c)**.
- **Child support uses the income-shares model.** Statutory basis at
  **§ 36-5-101**; the operative **Tennessee Child Support
  Guidelines** are the DHS regulations at **Tenn. Comp. R. & Regs.
  ch. 1240-02-04**. Verify the current Guidelines figures and
  worksheet — they are amended periodically.
- **Four statutory alimony types** at **§ 36-5-121**: alimony in
  futuro, alimony in solido, rehabilitative alimony, and transitional
  alimony — with a **statutory preference for rehabilitative and
  transitional** support over long-term in futuro.
- **Permanent parenting plan required** in every divorce / custody
  case involving a minor child — **§ 36-6-401 et seq.** Custody
  decisions apply the **best-interest factors at § 36-6-106(a)**.
- **Common-law marriage is NOT recognized** if contracted in
  Tennessee; a common-law marriage **valid where contracted**
  elsewhere is recognized by comity.

## Filing path — where a family case goes

| Matter | Forum | Skill |
|---|---|---|
| Divorce, annulment, legal separation | **Circuit OR Chancery Court** | `tn-family-court` |
| Custody / support **incident to divorce** | Circuit / Chancery (with the divorce) | `tn-family-court` |
| Custody / support between **married** parents | Circuit / Chancery | `tn-family-court` |
| Parentage / paternity / legitimation | **Juvenile Court** | `tn-juvenile-court` |
| Custody / support of children of **unmarried** parents | **Juvenile Court** | `tn-juvenile-court` |
| Dependency & neglect; termination of parental rights | **Juvenile Court** | `tn-juvenile-court` |
| Order of protection | Circuit / Chancery / General Sessions (and Juvenile for juveniles) | this skill + venue |

Both **Circuit Court** (a court of law) and **Chancery Court** (a
court of equity) have jurisdiction over divorce in Tennessee; see
`tn-family-court` for choosing between them. Title 37 matters
(parentage, unmarried-parent custody, dependency/neglect, TPR) go to
**Juvenile Court**; see `tn-juvenile-court`.

## Divorce — grounds (§ 36-4-101)

Tennessee divorce grounds are enumerated at **Tenn. Code Ann.
§ 36-4-101**. They fall into two categories.

### Fault grounds (approximately fifteen)

The fault grounds include, among others:

- **Adultery**
- **Desertion** — willful or malicious desertion for one full year
  without reasonable cause
- **Inappropriate marital conduct** (historically "cruel and inhuman
  treatment") — conduct rendering cohabitation unsafe or improper
- **Habitual drunkenness or drug abuse** contracted after marriage
- **Conviction of an infamous crime / felony imprisonment**
- **Bigamy** (either party knowingly married another)
- **Impotence / incapacity** at the time of the marriage
- **Refusal to move to Tennessee** with the other spouse and
  willful absence for two years
- **Indignities** rendering the spouse's position intolerable
- **Abandonment / failure to provide**

> Verify the **exact subsection numbering and the precise wording**
> of any ground at the current text of § 36-4-101 before pleading
> it; the list and its sub-numbering are periodically amended.

### No-fault ground — irreconcilable differences (§ 36-4-101(a)(14))

**Irreconcilable differences** is the no-fault ground at
**§ 36-4-101(a)(14)**. An irreconcilable-differences divorce
requires either (a) a written, signed **Marital Dissolution
Agreement** (MDA) resolving property and debts, plus a **permanent
parenting plan** if there are minor children, or (b) the matter is
tried after a contested ground is also pleaded. The procedure is at
**§ 36-4-103**.

## Divorce — procedure and the waiting period (§ 36-4-103)

The irreconcilable-differences procedure is governed by **§ 36-4-103**.
Key points:

1. **Pleading.** A divorce may be sought on irreconcilable
   differences alone, or paired with a fault ground pleaded in the
   alternative (a common practice so the case can proceed even if
   the agreement falls through).
2. **The agreement.** For an agreed irreconcilable-differences
   divorce, the parties must execute a written **Marital Dissolution
   Agreement** and, if minor children are involved, a **permanent
   parenting plan** (see below).
3. **The waiting period — § 36-4-103(a).** The complaint must be on
   file for at least:
   - **60 days** before the hearing if there is **no unmarried minor
     child** of the marriage, or
   - **90 days** before the hearing if there **is** an unmarried
     child under 18.
4. **No default for irreconcilable differences.** A divorce cannot be
   granted on irreconcilable differences by default; the statute
   requires the agreement (or a contested trial on another ground).

> The waiting period runs from **filing the complaint**, not from
> service. Confirm the count with `tn-deadlines` and verify against
> the current text of § 36-4-103(a).

## Annulment and legal separation

- **Annulment** treats a marriage as **void or voidable from the
  outset** (e.g., bigamy, incest, lack of capacity, fraud going to
  the essentials of the marriage). It is **rare** and the grounds
  are narrow; most "I want an annulment" requests are actually
  divorces. Research the specific basis and verify the governing
  Title 36 provisions before pleading annulment rather than divorce.
- **Legal separation** lets spouses live separately and have the
  court resolve property, support, and parenting while **remaining
  married** (often for religious or insurance reasons). It can later
  be converted to an absolute divorce. Confirm the current
  legal-separation provisions within Title 36, ch. 4.

## Equitable distribution — property (§ 36-4-121)

Tennessee is an **equitable-distribution** state, **not** a
community-property state. The court follows a two-step process under
**§ 36-4-121**:

### Step 1 — Classify

Each asset and debt is classified as **marital** or **separate**.

- **Separate property** generally includes property owned before the
  marriage, gifts and inheritances to one spouse, and (subject to
  exceptions) income from and appreciation of separate property.
- **Marital property** generally includes property acquired during
  the marriage and the increase in value of separate property to
  which both spouses substantially contributed, plus retirement
  benefits accrued during the marriage.
- **Transmutation** and **commingling** can convert separate property
  to marital property; **dissipation** (waste) of marital assets is a
  distribution factor. Verify the exact classification rules and
  defined terms at the current § 36-4-121.

### Step 2 — Divide the marital estate equitably

Only **marital property** is divided. The court divides it
**equitably** (a fair division, not necessarily 50/50) considering
the factors at **§ 36-4-121(c)**, which typically include:

- Duration of the marriage
- Age, physical and mental health, vocational skills, employability,
  earning capacity, and financial needs of each party
- Tangible / intangible contributions to the marital estate,
  including contribution as a homemaker
- Each party's separate assets
- The economic circumstances of each party at the time the division
  is to become effective
- Tax consequences and the value of separate property

Separate property is confirmed to its owner and is not divided
(though it can inform an alimony award).

## Child support — income-shares (§ 36-5-101; Guidelines ch. 1240-02-04)

Tennessee uses the **income-shares model**: both parents' incomes are
combined, the Guidelines assign a basic support obligation for the
number of children, and that obligation is apportioned between the
parents in proportion to their incomes and adjusted for parenting
time.

- **Statutory basis:** **§ 36-5-101**.
- **Guidelines:** the **Tennessee Child Support Guidelines** at
  **Tenn. Comp. R. & Regs. ch. 1240-02-04**, promulgated by the
  Department of Human Services. The Guidelines supply the income
  schedule, the Child Support Worksheet, and the deviation criteria.

Worksheet inputs typically include:

- Each parent's **gross income** (with statutory adjustments for
  self-employment, pre-existing support orders, other children in the
  home, etc.)
- **Number of days** the child spends with each parent (the
  parenting-time adjustment)
- **Work-related child-care** costs
- **Health-insurance** premium for the child
- **Recurring uninsured medical** expenses

A court may **deviate** from the presumptive Guidelines amount with
written findings of why the deviation is in the child's best interest.

> The dollar figures, the income schedule, and the worksheet are set
> by **regulation** and are amended periodically — always confirm the
> **current** Tenn. Comp. R. & Regs. ch. 1240-02-04 and run the
> current official worksheet rather than relying on stale numbers.

**Enforcement** runs through the Tennessee Department of Human
Services child-support program (wage assignment, license action, tax
intercept, contempt). Interstate establishment, modification, and
enforcement go through **UIFSA at § 36-5-2001 et seq.** (registration
and enforcement at §§ 36-5-2601 et seq.).

## Alimony — the four Tennessee types (§ 36-5-121)

Tennessee recognizes **four statutory forms of spousal support** at
**§ 36-5-121**:

| Type | Nature |
|---|---|
| **Alimony in futuro** (periodic) | Long-term periodic support where economic rehabilitation is **not** feasible; modifiable; typically terminates on death or remarriage of the recipient |
| **Alimony in solido** (lump sum) | A definite, fixed total amount (payable in a lump or in installments); generally **not modifiable**; may include an award of attorney's fees |
| **Rehabilitative alimony** | Temporary support to enable the economically disadvantaged spouse to acquire education / training and become self-sufficient |
| **Transitional alimony** | Support for a set period to help a spouse **adjust** to the economic consequences of divorce where rehabilitation is not needed but transition assistance is |

**Statutory preference.** Section 36-5-121 expresses a **legislative
preference for rehabilitative and transitional alimony** over
long-term alimony in futuro; in futuro is awarded where rehabilitation
is not feasible.

The court considers the statutory factors (including the relative
earning capacity and need of the parties, duration of the marriage,
the standard of living during the marriage, separate and marital
assets after division, the disadvantaged spouse's education and
training needs, and — where relevant — relative fault). Verify the
current factor list and the modifiability rules for each type at
§ 36-5-121.

## Permanent parenting plan and best interest (§§ 36-6-401, 36-6-106)

Every divorce or custody case involving a **minor child** requires a
**permanent parenting plan** under **§ 36-6-401 et seq.** The plan
allocates:

- **Residential schedule** (day-to-day, holidays, school breaks,
  summer) and designation of the **primary residential parent**
- **Decision-making authority** (education, non-emergency health
  care, religious upbringing, extracurriculars) — sole or joint
- **Child-support** terms (with the worksheet)
- A **dispute-resolution** process (often mediation)

The court selects and modifies a residential schedule under the
**best-interest factors at § 36-6-106(a)**, which include (verify the
current enumerated list):

- The strength, nature, and stability of the child's relationship
  with each parent
- Each parent's past and potential performance of parenting
  responsibilities and willingness to facilitate a relationship with
  the other parent
- The child's developmental needs and the continuity / stability of
  the child's environment
- The moral, physical, mental, and emotional fitness of each parent
- The child's reasonable preference (if of sufficient age and
  maturity)
- Evidence of physical or emotional abuse, and each parent's
  employment schedule

> The factor enumeration in § 36-6-106(a) has been amended over time;
> confirm the **current** factor list and numbering before drafting
> findings or a proposed parenting plan.

## Parental relocation (§ 36-6-108) — amended effective July 1, 2018

The relocation statute is **§ 36-6-108**, **substantially amended
effective July 1, 2018**. Under the current statute:

- A parent who intends to relocate **outside Tennessee** or **more
  than 50 miles** from the other parent **within** Tennessee must
  send the other parent **notice at least 60 days** before the move
  (with statutory content and method requirements).
- If the other parent files a timely objection, the court decides
  relocation under a **best-interest multifactor analysis**.

> **Stale-source warning.** Many older Tennessee relocation
> resources describe the **pre-2018** framework (the "100-mile"
> distinction and a presumption tied to which parent spent the most
> time with the child). That framework was **replaced** effective
> July 1, 2018. Use only post-2018 authority, and verify the current
> notice content, timing, and the controlling best-interest factors
> at § 36-6-108.

## Parentage / paternity and legitimation

Establishing **parentage** (paternity) and **legitimation** for a
child of **unmarried** parents is generally a **Juvenile Court** matter
under Title 37 (see `tn-juvenile-court`), though parentage can also be
adjudicated within other proceedings. Once parentage is established,
custody and support follow the same Title 36 substantive framework
(income-shares support, best-interest parenting plan) covered above.
Confirm the controlling parentage provisions and the proper forum for
the specific facts.

## Common-law marriage

Tennessee **does not recognize common-law marriage contracted within
Tennessee**. A purported common-law marriage created by cohabitation
and reputation in Tennessee is **not** a valid marriage here. However,
a common-law marriage that was **validly contracted in another state**
that recognizes it will generally be **recognized in Tennessee by
comity**. If a party asserts an out-of-state common-law marriage,
plead and prepare to prove the validity of the marriage under the law
of the state where it was formed.

## Jurisdiction over children and interstate cases

- **UCCJEA — § 36-6-201 et seq.** governs subject-matter jurisdiction
  over **custody / parenting** determinations. The child's **home
  state** generally controls. Plead the UCCJEA jurisdictional
  allegations (and any required affidavit of the child's residences)
  in the petition.
- **UIFSA — § 36-5-2001 et seq.** governs interstate **child-support**
  establishment, modification, and enforcement, including
  registration of out-of-state orders (§§ 36-5-2601 et seq.).

## Orders of protection / domestic abuse (§ 36-3-601 et seq.)

Civil **orders of protection** for domestic abuse, stalking, and
sexual assault are governed by **§ 36-3-601 et seq.** A petition may
be filed (often without a filing fee at the outset) and the court may
enter an **ex parte** temporary order, followed by a hearing on an
extended order. Orders of protection frequently run parallel to a
divorce or parentage case; coordinate the parenting and possession
provisions across the cases. Verify the current petition form, the
hearing timeline, and the duration provisions at § 36-3-601 et seq.

## Mandatory parenting-education seminar

In divorce and custody cases involving **minor children**, Tennessee
requires the parents to complete a **mandatory parenting-education
seminar** before the parenting plan is finalized. This requirement is
commonly cited to **§ 36-6-408** — **verify the current citation and
the county's approved provider list**, because both the statutory
cross-reference and the local provider lists are updated periodically.
Many counties also require the seminar by **local rule**; check the
venue with `tn-family-court`.

## Mandatory financial disclosures

Tennessee family practice relies on sworn financial disclosure. Where
the **local rules** require it (and in many counties they do), the
parties must exchange a **Rule 16-type / sworn financial statement**
(income, expenses, assets, debts) — analogous to a mandatory
disclosure obligation. The content and deadline are **set by the
county's local rules**, so confirm the requirement and the form with
`tn-family-court` and the venue skill for the specific court. A
complete, truthful financial affidavit is essential to property
division, child support, and alimony; knowing falsification carries
serious consequences.

## Drafting checklist

- [ ] Forum chosen correctly (Circuit/Chancery vs. Juvenile) per the
      filing-path table — see `tn-family-court` / `tn-juvenile-court`
- [ ] Ground(s) pleaded correctly under § 36-4-101 (and
      irreconcilable differences pleaded under § 36-4-101(a)(14) with
      the § 36-4-103 procedure)
- [ ] Waiting period (60 / 90 days) calculated from filing under
      § 36-4-103(a) — verify with `tn-deadlines`
- [ ] Property classified (marital vs. separate) before proposing an
      equitable division under § 36-4-121
- [ ] Child support run on the **current** official Guidelines
      worksheet (ch. 1240-02-04)
- [ ] Alimony request identifies the correct **type** under
      § 36-5-121
- [ ] Permanent parenting plan drafted under § 36-6-401 et seq. with
      § 36-6-106(a) best-interest support
- [ ] Relocation handled under the **post-2018** § 36-6-108 framework
- [ ] UCCJEA / UIFSA allegations included where there is an
      interstate element
- [ ] Mandatory parenting seminar and any local financial-disclosure
      requirement satisfied

## Composition

- For format and the Rule 10 caption: `tn-statewide-format`
- For the divorce venue (Circuit / Chancery), parenting-plan
  requirement, and intake: `tn-family-court`
- For Title 37 matters (parentage, unmarried-parent custody,
  dependency/neglect, TPR): `tn-juvenile-court`
- For drafting the complaint / petition / motion: `tn-draft-motion`
- For sworn declarations / affidavits: `tn-draft-declaration`
- For a proposed decree / order: `tn-draft-order`, `tn-submit-order`
- For pro se conventions and self-represented intake: `tn-pro-se`
- For the 60/90-day waiting period and other deadlines:
  `tn-deadlines`
- For hearings and oral argument: `tn-hearings`
- For citation verification: `tn-fact-check`
- For canonical Title 36 text and the Guidelines: `tn-law-references`

## References

- `references/divorce-grounds.md` — § 36-4-101 fault grounds +
  irreconcilable differences detail
- `references/divorce-procedure.md` — § 36-4-103 procedure and the
  60/90-day waiting period
- `references/equitable-distribution.md` — § 36-4-121 classification +
  the § 36-4-121(c) factors
- `references/child-support-guidelines.md` — § 36-5-101 + Tenn. Comp.
  R. & Regs. ch. 1240-02-04 income-shares worksheet inputs
- `references/alimony.md` — the four § 36-5-121 alimony types and the
  rehabilitative/transitional preference
- `references/parenting-plan.md` — § 36-6-401 et seq. permanent
  parenting plan + § 36-6-106(a) best-interest factors
- `references/relocation.md` — the post-July-1-2018 § 36-6-108
  framework
- `references/uccjea-uifsa.md` — § 36-6-201 et seq. and § 36-5-2001
  et seq.
- `references/orders-of-protection.md` — § 36-3-601 et seq.
