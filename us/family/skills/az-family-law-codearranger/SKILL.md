---
name: az-family-law-codearranger
title: Arizona Family Law
description: 'Use for any Arizona family-law / domestic-relations matter: dissolution (divorce), covenant marriage, community-property division, legal decision-making, parenting time, child support, spousal maintenance, relocation, interstate jurisdiction. Triggers: "Arizona divorce", "dissolution of marriage Arizona", "irretrievably broken Arizona", "Arizona divorce waiting period", "covenant marriage Arizona", "Arizona community property", "legal decision-making Arizona", "Arizona parenting time", "Arizona child support", "spousal maintenance Arizona", "Arizona relocation", "Arizona UCCJEA", "Arizona UIFSA". Covers: no-fault dissolution (A.R.S. § 25-312) with 60/90-day waiting, covenant marriage (§ 25-901 et seq.), community-property (§ 25-211/25-213/ 25-318), legal decision-making and parenting time (§ 25-401/25-403), relocation (§ 25-408), child support (§ 25-320 + Guidelines), spousal maintenance (§ 25-319 + Guidelines), bar on common-law marriage (§ 25-111), UCCJEA / UIFSA.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Arizona Family Law

> **NOT LEGAL ADVICE.** This subject-matter bundle describes a
> substantive framework for Arizona domestic-relations matters,
> not legal advice and not strategic advice for any specific case.
> Family-law cases carry long-term consequences for property,
> children, and finances; strongly consider consulting a licensed
> Arizona family-law attorney even on an "agreed" dissolution.
> Outcomes are fact-specific; the choice of claims, defenses, and
> the parenting/support positions belongs to the litigant (and any
> counsel the litigant retains). Verify every rule, threshold,
> waiting period, dollar figure, and citation against current law
> before filing.

This bundle supplies the **substantive law** of Arizona family
practice. The **venue mechanics** — which Superior Court family-law
department, intake, conciliation services, mandatory forms, parent
education, and the order-of-protection procedure — live in
`az-family-court`. Document format lives in `az-statewide-format`.

## Snapshot — Arizona family-law principles

- **No-fault dissolution.** A standard (non-covenant) marriage is
  dissolved on a finding that the **marriage is irretrievably
  broken** — **A.R.S. § 25-312**. No party pleads or proves fault.
- **Covenant marriage is the major exception.** A **covenant
  marriage** (**A.R.S. § 25-901 et seq.**) may be dissolved **only**
  on the limited fault/separation grounds enumerated in
  **A.R.S. § 25-903**. See the dedicated section below.
- **Waiting period — A.R.S. § 25-329.** The court may not hold a
  trial or hearing on (or consider an affidavit-supported submission
  for) a decree of dissolution or legal separation until at least
  **60 days after the date of service of process or acceptance of
  process** — which functionally bars entry of the decree before
  then. **Residency — A.R.S. § 25-312:** a party must have
  been domiciled in Arizona (or stationed there in the armed
  services) for at least **90 days** before filing.
- **Community-property state.** Property acquired during the
  marriage is **community property** — **A.R.S. § 25-211** — and is
  divided **equitably** at dissolution under **A.R.S. § 25-318**.
  Equitable means **fair, and presumptively but not necessarily
  equal**. Separate property is defined at **A.R.S. § 25-213**.
- **"Legal decision-making" and "parenting time," not "custody."**
  Arizona replaced the term *custody* in 2013. Definitions live at
  **A.R.S. § 25-401**; the **best-interests** factors at
  **A.R.S. § 25-403**; the sole-vs-joint framework at
  **A.R.S. § 25-403.01**; the domestic-violence overlay at
  **A.R.S. § 25-403.03**.
- **Child support uses the Arizona Child Support Guidelines.**
  Statutory basis **A.R.S. § 25-320**; the operative figures live in
  the **Guidelines** (an income-shares model).
- **Spousal maintenance — A.R.S. § 25-319** plus the **2023 Arizona
  Spousal Maintenance Guidelines**, the new advisory calculation
  (see below).
- **No common-law marriage.** Arizona requires a **license + lawful
  solemnization** — **A.R.S. § 25-111** — so cohabitation alone
  creates no marriage; a marriage **valid where contracted** is
  honored.

## Filing path — where a family case goes

Arizona family matters are heard in the **Superior Court** of the
county of proper venue (each county Superior Court has a family-law
department or assigned family-law judges/commissioners). The venue
mechanics, conciliation services, parent-education requirement, and
the AOC mandatory forms live in `az-family-court`. Orders of
protection for domestic violence run parallel to dissolution and
parenting cases — the **procedural** order-of-protection mechanics
are in `az-family-court`; this skill addresses only the substantive
family-law overlay.

## Dissolution — the standard ground (A.R.S. § 25-312)

For a **non-covenant** marriage, Arizona is a **pure no-fault**
state. The court enters a decree on a finding that the **marriage
is irretrievably broken** — **A.R.S. § 25-312(A)(3)**. No other ground
is required and the court may not condition the decree on proof of
fault. If one party denies the marriage is irretrievably broken,
the court may order a **conciliation conference** or continue the
matter, but irretrievable breakdown remains the ultimate finding.

**Residency / domicile — A.R.S. § 25-312(A)(1).** At least one party
must have been **domiciled in Arizona** (or been a member of the
armed services stationed in Arizona) for at least **90 days** before
the petition is filed. Confirm the exact count in the corpus.

## Dissolution — the 60-day waiting period (A.R.S. § 25-329)

Under **A.R.S. § 25-329**, the court may **not** consider an
affidavit-supported submission, or hold a trial or hearing, on an
application for a decree of dissolution or legal separation until
**60 days after the date of service of process or the date of
acceptance of process** — which functionally means no decree can be
entered before the 60th day. This is a floor on the trial/hearing
(and thus the decree), **not** a residency rule and **not** a
cooling-off period that bars filing. Calculate the count with
`az-deadlines` and verify the current text in the corpus.

## CRITICAL — Covenant marriage (A.R.S. § 25-901 et seq.)

Arizona is **one of the few covenant-marriage states.** A couple
may elect at the time of marriage by signing the statutory
**declaration of intent** (**A.R.S. § 25-901**) after premarital
counseling — or may **convert** an existing valid marriage into a
covenant marriage (**A.R.S. § 25-902**) by recording the § 25-901(B)
declaration with a certified copy of their marriage certificate
(converting couples need **not** repeat the § 25-901 premarital
counseling). **Always confirm at intake whether the marriage is a
covenant marriage**, because it changes the available grounds
entirely.

A **covenant marriage cannot be dissolved on the no-fault
"irretrievably broken" ground.** It may be dissolved **only** on the
limited grounds enumerated in **A.R.S. § 25-903**, which (verify the
current list in the corpus) include such things as:

- **Adultery** by the other spouse;
- Commission of a **felony** with a sentence of death or
  imprisonment;
- **Abandonment** for at least one year;
- **Physical or sexual abuse** of the spouse, a child, a relative,
  or **domestic violence**;
- Living **separate and apart** continuously without reconciliation
  for the statutory period; and
- **Habitual drug/alcohol abuse**, or **both spouses' agreement** to
  the dissolution.

The same limited-grounds regime applies to **legal separation** of a
covenant marriage (**A.R.S. § 25-904**). Plead the specific
§ 25-903 ground and its supporting facts. Do **not** plead
"irretrievably broken" for a covenant marriage. Verify the full,
current grounds catalog before drafting.

## Property distribution — community property (A.R.S. §§ 25-211, 25-213, 25-318)

Arizona is a **community-property** state — **not** an
equitable-distribution-of-everything state. The analysis is a
classification step followed by a division step.

### Step 1 — Classify (community vs. sole and separate)

- **Community property** — **A.R.S. § 25-211** — is all property
  **acquired by either spouse during the marriage**, with the
  statutory exceptions. Both spouses have an undivided one-half
  interest in community property.
- **Separate property** — **A.R.S. § 25-213** — is property a spouse
  **owned before marriage**, and property acquired during marriage
  by **gift, devise, or descent**, plus the **increase, rents,
  issues, and profits** of separate property. Property acquired
  **after service** of a dissolution petition (where the petition
  results in a decree) is also separate (see § 25-211).
- **Commingling.** Separate property that is **commingled** with
  community property so that it can no longer be traced may lose its
  separate character; the spouse asserting a separate interest bears
  the burden of **tracing**. Community contributions to a separate
  asset (e.g., mortgage paydown on a pre-marital home, or community
  labor enhancing a separate business) can create **community
  liens** / reimbursement claims. Address tracing and any community
  lien expressly.

### Step 2 — Divide the community equitably (A.R.S. § 25-318)

At dissolution the court divides the **community, joint tenancy, and
common property equitably** under **A.R.S. § 25-318** — **"equitable"
need not be exactly equal**, though Arizona courts treat a
substantially **equal** division as the norm absent a sound reason
to depart. Separate property is **confirmed** to the owning spouse
and is **not** divided. The court also allocates **community debts**.
Verify the controlling articulation and the current text of
§ 25-318 in the corpus.

## Legal decision-making and parenting time (A.R.S. §§ 25-401 to 25-403.03)

Arizona **replaced "custody" with "legal decision-making" and
"parenting time" effective January 1, 2013.** Draft in the current
terms.

### Definitions — A.R.S. § 25-401

- **Legal decision-making** = the legal right and responsibility to
  make **all nonemergency legal decisions** for a child (education,
  health care, religious training, personal care) — § 25-401(3). It
  may be awarded **sole** (one parent makes the major decisions —
  § 25-401(6)) or **joint** (both parents share decision-making —
  § 25-401(2)).
- **Parenting time** = the schedule of **when** each parent has the
  child and is responsible for routine care during that time.

### Best interests — A.R.S. § 25-403

Legal decision-making and parenting time are decided on the **best
interests of the child** under the enumerated factors at
**A.R.S. § 25-403** — including the past, present, and potential
relationship between each parent and the child; the child's
relationships and adjustment to home, school, and community; the
child's wishes if of suitable age and maturity; the mental and
physical health of all involved; **which parent is more likely to
allow frequent, meaningful, and continuing contact** with the other;
**domestic violence or child abuse**; coercion or duress in
obtaining an agreement; and others. In contested cases the court
must make **specific findings on the record** as to the relevant
factors. Verify the current enumeration of § 25-403 in the corpus
before drafting findings.

### Sole vs. joint — A.R.S. § 25-403.01

**A.R.S. § 25-403.01** governs the choice between **sole** and
**joint** legal decision-making and directs additional factors
(including the agreement or lack of agreement of the parents and
whether joint decision-making is logistically possible). There is
**no presumption** for or against either parent based on the
parent's sex.

### Domestic violence — A.R.S. § 25-403.03

**A.R.S. § 25-403.03** controls where there is **significant
domestic violence** or a **significant history** of domestic
violence: it creates a **rebuttable presumption against awarding
joint or sole legal decision-making to the perpetrator** and
structures supervised or restricted parenting time. Plead and prove
the domestic-violence findings carefully where they apply.

## Relocation of a child (A.R.S. § 25-408)

Where both parents reside in Arizona and a court order on legal
decision-making or parenting time is in effect, a parent who intends
to **relocate the child** — **out of state, or more than 100 miles
within Arizona** — must give the other parent at least **45 days'
advance written notice** under **A.R.S. § 25-408** (verify the
distance and notice count in the corpus). The non-moving parent may
**petition to prevent the relocation** within the statutory window.

On a contested relocation the court decides in the child's **best
interests**, and the parent seeking to relocate bears the **burden
of proving the move is in the child's best interests**. Section
25-408 lists relocation-specific factors (e.g., the reasons for and
against the move, the prospective advantages, each parent's
motives, the effect on the child's stability and relationships, and
whether a realistic, cost-effective revised parenting schedule is
possible). Verify the current factor list before drafting.

## Child support (A.R.S. § 25-320 + the Arizona Child Support Guidelines)

Arizona support is set by guideline. **A.R.S. § 25-320** directs the
court to order support **in the amount resulting from the Arizona
Child Support Guidelines** unless a deviation is justified by
written findings that the guideline amount would be **inappropriate
or unjust** in light of the child's best interests.

The Guidelines use an **income-shares** model: both parents' gross
incomes are combined, a basic support obligation is determined from
the schedule for the number of children, and the obligation is
apportioned between the parents and adjusted for **parenting-time
days**, **medical / dental / vision insurance**, **child-care
costs**, and other add-ons. The Guidelines also address
**attribution of income** to a parent who is voluntarily unemployed
or underemployed. Establishment, review, and enforcement (income
withholding, license actions, contempt) run through the court and
the Division of Child Support Services (see `az-family-court`).
**Modification** requires a **substantial and continuing change of
circumstances** (a deviation of a threshold percentage permits a
**simplified** modification).

> The Child Support Guidelines schedule, the self-support reserve,
> the parenting-time adjustment table, and the add-on rules live in
> the **Arizona Child Support Guidelines** and are **amended
> periodically** — always run the **current** official Guidelines
> and worksheet rather than relying on stale figures. See the corpus
> and `az-law-references` for the controlling numbers.

## Spousal maintenance (A.R.S. § 25-319 + the 2023 Guidelines)

**A.R.S. § 25-319** is a **two-step** statute. First, the court
determines **eligibility** under § 25-319(A) — e.g., the spouse
lacks sufficient property to provide for reasonable needs, cannot be
self-sufficient through appropriate employment (or is the custodian
of a child whose circumstances make outside employment
inappropriate), contributed to the other's earning ability, or had a
marriage of long duration and an age that precludes adequate
employment. **If** eligible, the court then sets the **amount and
duration** under the § 25-319 factors.

> **2023 Arizona Spousal Maintenance Guidelines.** Effective in
> **2023**, Arizona adopted **advisory Spousal Maintenance
> Guidelines** that produce a **calculated suggested range** for the
> **amount and duration** of maintenance once eligibility is
> established under § 25-319(A). The Guidelines are **advisory** —
> the court may deviate with findings — but they are the new default
> starting point and replace the prior purely discretionary,
> factor-only approach to quantum. **Run the current Guidelines
> calculator**; the formula inputs, duration multipliers, and any
> caps live in the Guidelines, not in this skill. See the corpus and
> `az-law-references`.

## Common-law marriage (A.R.S. § 25-111)

Arizona does **not** recognize common-law marriage. **A.R.S.
§ 25-111** requires a **marriage license** and a **lawful
solemnization** for a valid Arizona marriage; cohabitation,
reputation, and a holding-out as married do **not** create a
marriage in Arizona no matter how long. However, a common-law
marriage **validly contracted in another state** that recognizes it
is **honored** in Arizona under the rule that Arizona recognizes
marriages valid **where contracted**. A party asserting an
out-of-state common-law marriage must plead and prove its validity
under that state's law.

## Jurisdiction over children and interstate cases

- **UCCJEA — A.R.S. § 25-1001 et seq.** governs subject-matter
  jurisdiction over **legal-decision-making / parenting-time**
  determinations. The child's **home state** generally controls.
  Plead the UCCJEA jurisdictional allegations and the required
  information about the child's residences for the prior period in
  the petition.
- **UIFSA — A.R.S. § 25-1201 et seq.** governs interstate **support**
  establishment, modification, and enforcement, including
  registration of out-of-state orders and the
  continuing-exclusive-jurisdiction rules.

## Orders of protection / domestic violence (cross-reference)

Domestic-violence **orders of protection** are commonly sought
alongside a dissolution or parenting case, and their findings can
bear directly on the **best-interests** analysis and the
**§ 25-403.03** domestic-violence presumption above. The
**procedural** order-of-protection mechanics — the petition, the
ex parte standard, the hearing on request, and service — live in
`az-family-court`. Coordinate any protective order with the
parenting-time provisions across the cases.

## Drafting checklist

- [ ] Forum correct (Superior Court family-law department, proper
      county venue) — see `az-family-court`
- [ ] **Covenant marriage screened at intake** — if covenant, plead
      a specific **A.R.S. § 25-903** ground (NOT "irretrievably
      broken"); if standard, plead the marriage is **irretrievably
      broken** under § 25-312
- [ ] Residency/domicile (90 days, A.R.S. § 25-312) alleged;
      **60-day** post-service waiting period (A.R.S. § 25-329)
      calculated with `az-deadlines`
- [ ] Property **classified** (community vs. sole and separate,
      A.R.S. §§ 25-211 / 25-213) with **tracing** and any
      **community lien** addressed before proposing an **equitable**
      division under A.R.S. § 25-318; community debts allocated
- [ ] Legal decision-making + parenting time framed in the **current
      2013 terms**, with findings on the **best-interests factors**
      (A.R.S. § 25-403) and the sole-vs-joint analysis (§ 25-403.01);
      **§ 25-403.03** domestic-violence presumption addressed where
      it applies
- [ ] Any relocation handled under **A.R.S. § 25-408** (45-day
      notice; out-of-state or 100-mile trigger; best-interests
      burden on the moving parent)
- [ ] Child support run on the **current** Arizona Child Support
      Guidelines; any deviation supported by written findings under
      A.R.S. § 25-320
- [ ] Spousal maintenance analyzed in **two steps** — eligibility
      under A.R.S. § 25-319(A), then amount/duration via the **2023
      Spousal Maintenance Guidelines** with deviation findings if any
- [ ] UCCJEA / UIFSA allegations included where there is an
      interstate element

## Composition

- For format and the Ariz. R. Civ. P. 10 caption: `az-statewide-format`
- For the family-law department venue, conciliation services, parent
  education, AOC mandatory forms, and order-of-protection mechanics:
  `az-family-court`
- For Superior Court venue generally: `az-superior-courts`,
  `az-maricopa`, `az-pima`, `az-superior-courts`
- For drafting the petition / response / motion: `az-draft-motion`
- For sworn declarations / affidavits: `az-draft-declaration`
- For a proposed decree / order: `az-draft-order`, `az-submit-order`
- For pro se conventions and self-represented intake: `az-pro-se`
- For the 60-day waiting period and other deadlines: `az-deadlines`
- For hearings and oral argument: `az-hearings`
- For citation verification: `az-fact-check`
- For canonical A.R.S. text, the Child Support Guidelines, and the
  2023 Spousal Maintenance Guidelines: `az-law-references`

## References

- `references/dissolution-grounds-residency.md` — A.R.S. § 25-312
  irretrievably-broken ground + 90-day domicile, A.R.S. § 25-329
  60-day waiting period
- `references/covenant-marriage.md` — A.R.S. § 25-901 / 25-902
  declaration + conversion, the § 25-903 limited dissolution grounds,
  § 25-904 legal separation
- `references/community-property.md` — community vs. sole-and-separate
  classification (A.R.S. §§ 25-211 / 25-213), commingling and tracing,
  community liens, equitable division under A.R.S. § 25-318
- `references/legal-decision-making-parenting-time.md` — A.R.S. § 25-401
  definitions, § 25-403 best-interests factors, § 25-403.01 sole vs.
  joint, § 25-403.03 domestic-violence presumption
- `references/relocation.md` — A.R.S. § 25-408 notice + the
  best-interests relocation standard and factors
- `references/child-support.md` — A.R.S. § 25-320 + the income-shares
  Arizona Child Support Guidelines and worksheet inputs
- `references/spousal-maintenance.md` — A.R.S. § 25-319 two-step
  eligibility + factors and the 2023 Arizona Spousal Maintenance
  Guidelines advisory calculation
- `references/uccjea-uifsa.md` — A.R.S. § 25-1001 et seq. and
  A.R.S. § 25-1201 et seq.
