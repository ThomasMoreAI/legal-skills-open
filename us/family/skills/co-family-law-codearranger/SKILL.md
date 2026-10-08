---
name: co-family-law-codearranger
title: Colorado Family Law — Divorce, Annulment, Child Support
description: 'Use for Colorado family-law matters — dissolution/annulment/legal separation, parental responsibilities, parenting time, child support, maintenance. Covers **Uniform Dissolution of Marriage Act (UDMA — C.R.S. art. 10 of title 14)**, **C.R.C.P. 16.2** mandatory domestic case management with **Sworn Financial Statement**, **C.R.S. § 14-10-115** child-support guidelines, **C.R.S. § 14-10-114** maintenance, allocation of parental responsibilities (**C.R.S. § 14-10-124**), modification (**C.R.S. § 14-10-122**), common-law marriage. Triggers: "divorce Colorado", "Colorado dissolution", "Colorado custody", "C.R.S. 14-10", "UDMA", "child support guideline".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-family-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Colorado Family Law — Divorce, Annulment, Child Support

> **NOT LEGAL ADVICE.** Family-law cases involve significant
> long-term consequences for property, children, and finances.
> Strongly consider consulting a licensed Colorado family-law
> attorney even on "simple" dissolutions.

This subject-matter bundle covers the principal Colorado domestic-
relations cases: **dissolution of marriage** (divorce), **declaration
of invalidity** (annulment), **legal separation**, **allocation of
parental responsibilities**, **parenting time**, **child support**,
and **maintenance** (spousal support / alimony).

Colorado adopted the **Uniform Dissolution of Marriage Act (UDMA)**
in 1971 and codified it at **C.R.S. art. 10 of title 14**. The UDMA
is the principal statutory framework. C.R.C.P. 16.2 supplies the
**domestic-case management** rules — distinctively Colorado in its
mandatory financial-disclosure obligations.

> **NOT LEGAL ADVICE.** Output from this skill is a drafting aid;
> verify with current statutes and local rules before filing.

## Snapshot — Colorado family-law principles

- **No-fault state**: Colorado is a pure no-fault state. The only
  ground for dissolution is that the marriage is **"irretrievably
  broken"** (C.R.S. § 14-10-106(1)(a)(II)). Conduct of the parties
  is **not relevant** to dissolution itself but may affect specific
  issues (e.g., dissipation of marital property, fitness for
  parenting time).
- **Residency**: at least one party must have been a domiciliary of
  Colorado for **at least 91 days** before filing (C.R.S.
  § 14-10-106(1)(a)(I)).
- **Mandatory 91-day waiting period**: the decree cannot enter
  until **91 days after** the later of: (a) service on the
  Respondent or (b) the Respondent's signature on a waiver
  (C.R.S. § 14-10-106(1)(a)(III)).
- **Marital property** is **equitably divided** (C.R.S.
  § 14-10-113), not necessarily equally. Colorado is **not** a
  community-property state.
- **Maintenance** is **statutory-guideline-based** (with discretion)
  under the 2014 maintenance reform — C.R.S. § 14-10-114.
- **Child support** is **guideline-based** with the income-shares
  model — C.R.S. § 14-10-115.
- **"Parental responsibilities"** replaced "custody" terminology in
  1998. The court allocates **decision-making responsibility**
  (legal custody equivalent) and **parenting time** (physical
  custody equivalent) — C.R.S. § 14-10-124.
- **Common-law marriage** is **recognized** in Colorado on a fact-
  intensive showing — *People v. Lucero*, 747 P.2d 660 (Colo.
  1987); modernized in *In re Marriage of Hogsett & Neale*, 2021 CO 1
  (rejecting traditional gender-role test, applying a more
  flexible totality-of-circumstances test).

## Filing path — district court only

All Colorado domestic-relations cases file in the **district court**
of the county where:

- The petitioner resides, OR
- The respondent resides (if there is no Colorado petitioner-county
  per § 14-10-105)

Case-number format: `YYYYDR0#####`. Case type code `DR` (domestic
relations).

### Jefferson County District Court (1st JD) — Family Law Division

Jefferson County handles one of the highest volumes of family law
cases in Colorado. Key information:

- **Courthouse**: 100 Jefferson County Parkway, Golden, CO 80401
- **Family Law Division Phone**: (303) 271-6390
- **Hours**: Monday-Friday, 8:00 AM - 4:30 PM
- **Case assignment**: Family law cases are assigned to specific
  divisions based on case type and filing date
- **Family Court Facilitator**: Available for pro se parties to
  assist with forms and procedural questions (not legal advice)
- **Mandatory mediation**: Most contested family law cases are
  ordered to mediation through the 1st JD's approved mediator list
- **Initial Status Conference (ISC)**: Typically scheduled within
  42 days of service; handled by magistrates or family court
  facilitators

**Jefferson County Family Law Local Practices**:

- **Temporary Orders**: Family court magistrates hear temporary
  orders motions; hearings typically scheduled 4-6 weeks out
- **Child and Family Investigators (CFI)**: The 1st JD maintains
  an approved CFI roster for contested parenting cases
- **Parenting Classes**: Mandatory "Helping Children Succeed After
  Divorce" class required for all cases involving minor children
- **Electronic Filing**: All family law documents must be filed
  through CCEFS; proposed orders submitted electronically
- **Sworn Financial Statement**: Strict enforcement of the 42-day
  deadline; late filing can result in sanctions

## Case types within domestic relations

| Case type | Statute | When to use |
|---|---|---|
| Dissolution of Marriage (divorce) | C.R.S. § 14-10-106 | Spouses seeking to legally end a valid marriage |
| Legal Separation | C.R.S. § 14-10-106 (same petition, different decree request) | Spouses who want to live separately but remain married (religious / insurance reasons; later convertible to dissolution) |
| Declaration of Invalidity of Marriage (annulment) | C.R.S. § 14-10-111 | The marriage was **never** valid (specific grounds — see below) |
| Allocation of Parental Responsibilities (no marriage) | C.R.S. § 14-10-123 | Unmarried parents seeking court orders on decision-making and parenting time |
| Post-Decree Modification | C.R.S. § 14-10-122 | Existing decree needs change (child support, parenting time, maintenance) |

## Annulment vs. dissolution — grounds for declaration of invalidity (C.R.S. § 14-10-111)

A **declaration of invalidity of marriage** (Colorado's term for
annulment) is **rare**. The marriage must have been **invalid from
the outset**. Grounds:

1. **Lack of capacity** to consent (intoxication, mental
   incapacity, force, duress, fraud going to the essentials of the
   marriage)
2. **Impotence** for sex existing at the time of the marriage and
   continuing through the proceeding (the petitioner must not have
   known)
3. **Under age 18** without parental / judicial consent
4. **Same parties already lawfully married** to others (bigamy)
5. **Marriage prohibited by law** (incest within the prohibited
   degrees — C.R.S. § 14-2-110)
6. **Jest or dare** — entered into as a joke or on a dare

> ⚠ Most "I want an annulment" requests are actually **dissolution
> requests under a misunderstanding**. The C.R.S. § 14-10-111 grounds
> are narrow. A marriage that the parties later realize was a
> mistake is not invalid — they need a dissolution.

**Time limits for annulment**:

- Lack of capacity / impotence / fraud — **6 months** after gaining
  knowledge
- Underage — **24 months** after marriage / until petitioner attains
  18
- Bigamy / incest / jest — **5 years** after marriage, or before
  death of either party

The decree of invalidity, once entered, treats the marriage as
**never having existed**. Practical consequence: there is no
marital property, no marital debts (in the traditional sense),
though courts may apply equitable doctrines like quantum meruit or
unjust enrichment to division.

## Dissolution of marriage — the standard path

### Step 1 — Verify jurisdiction and residency

- **Residency**: at least one party must have been a domiciliary of
  Colorado for 91+ days before filing. Track dates carefully.
- **Subject-matter jurisdiction**: Colorado district court has
  jurisdiction over the marital status under C.R.S. § 14-10-106.
- **Personal jurisdiction over Respondent**: required for orders
  regarding property, maintenance, or child support; can be
  established by service in Colorado, consent, or long-arm
  jurisdiction under C.R.S. § 13-1-124.
- **UCCJEA jurisdiction over children**: governs decision-making
  and parenting time. Colorado follows the Uniform Child Custody
  Jurisdiction and Enforcement Act at C.R.S. art. 13 of title 14.
  "Home state" of the child controls.

### Step 2 — File the Petition

Use **JDF 1099** (Petition for Dissolution of Marriage or Legal
Separation). The petition states:

- Marriage date and place
- Date of separation
- Names, addresses, and dates of birth of the parties
- Names and dates of birth of any minor children
- Whether the wife is pregnant
- Allegation that the marriage is irretrievably broken
- Allegation of residency (91 days)
- Property and debts (summary; detail goes in the Sworn Financial
  Statement)
- Whether maintenance is sought
- Whether child support and parenting time orders are sought
- Prayer for the relief requested

**Filing fee**: $230 (district court dissolution). Fee waiver via
JDF 205/206 if eligible.

The petition can be filed jointly (as **co-petitioners**) or by
one party as **Petitioner** with the other as **Respondent**.
Joint petitions reduce conflict and speed the case.

### Step 3 — Service on Respondent (if not a joint petition)

Service under C.R.C.P. 4. The 91-day waiting period starts at
service.

### Step 4 — Mandatory disclosures under C.R.C.P. 16.2

Colorado's distinctive feature: **C.R.C.P. 16.2** imposes mandatory
financial-and-disclosure obligations in domestic cases. Within
**42 days** of service:

1. **Sworn Financial Statement (SFS)** — JDF 1111 (or JDF 1112 if
   the case involves child support). The SFS is the most important
   document in any Colorado domestic case. **Knowing falsification
   is perjury** under C.R.S. § 18-8-503.
2. **Supporting documents** — three years of tax returns, three
   months of pay stubs, three months of statements for every
   financial account, real-estate documents, retirement-account
   statements, etc.
3. **Disclosure certificate** — JDF 1104, confirming the
   disclosures were complete.

The penalty for incomplete or late disclosures includes monetary
sanctions, contempt, and (in serious cases) reversal of the
decree's property division — see *In re Marriage of Cardona &
Castro*, 2014 CO 3.

### Step 5 — Temporary orders (optional)

Either party may move for **temporary orders** under C.R.S.
§ 14-10-108 covering temporary maintenance, temporary child
support, temporary parenting time, exclusive use of the marital
residence, and restraining orders against asset dissipation. Use
**JDF 1100** for the motion.

The court typically holds a temporary-orders hearing within 30-60
days of the motion.

### Step 6 — Initial Status Conference (ISC)

Within 42 days of service, the court typically schedules an
**Initial Status Conference** under C.R.C.P. 16.2(d)(1). The ISC is
short (15-30 min), held with a **family-court facilitator** or the
judge. Topics:

- Whether the case is contested
- Mediation requirement
- Scheduling

### Step 7 — Mediation (if not waived)

Many Colorado JDs **require mediation** in contested dissolutions.
The Colorado Office of Dispute Resolution (CDR) provides court-
referred mediators on a sliding-fee basis. Mediation is on
**parenting issues and financial issues** separately or together.

### Step 8 — Permanent Orders Hearing

For contested cases, the **Permanent Orders Hearing** is the trial.
The court decides:

- Whether marriage is irretrievably broken (almost always granted
  if both parties acknowledge)
- Division of marital property
- Allocation of marital debts
- Maintenance award (amount, duration)
- Allocation of parental responsibilities
- Parenting time
- Child support
- Attorneys' fees and costs

Uncontested cases often proceed by **decree on the pleadings** —
the parties submit a Separation Agreement and Parenting Plan, the
court reviews and enters the decree at or just after the 91-day
waiting period expires.

### Step 9 — Decree of Dissolution

After the 91-day waiting period and the court is satisfied with the
disclosures and any contested issues are resolved or tried, the
court enters the **Decree of Dissolution of Marriage** (JDF 1116).

The decree typically includes:

- Finding that the marriage is irretrievably broken
- Confirmation of jurisdiction and residency
- Restoration of former name if requested
- Incorporation of the Separation Agreement (uncontested) or the
  court's findings (contested)
- Incorporation of the Parenting Plan (if children)
- Child support order with worksheet attached
- Maintenance order (if any)
- Disposition of property and debts

## Maintenance — C.R.S. § 14-10-114

Colorado modernized maintenance ("spousal support") in 2014. The
statute provides **guideline amounts** (advisory) and a list of
factors. The 2024 amendments (HB24-1078) further refined the
framework.

### Guideline amount (advisory)

For marriages of **3 years or longer**, the guideline maintenance
amount is calculated using:

- **40% of the higher earner's monthly adjusted gross income**, minus
- **50% of the lower earner's monthly adjusted gross income**
- Adjusted for combined income tiers; capped where combined income
  exceeds the statutory ceiling

For marriages of **less than 3 years**, there is no guideline; the
court applies discretion based on the factors below.

### Guideline duration (advisory)

The duration is a function of the length of the marriage:

| Length of marriage | Maintenance duration |
|---|---|
| 3 years | 11 months (~31%) |
| 5 years | 21 months (~35%) |
| 10 years | 45 months (37.5%) |
| 15 years | 78 months (43%) |
| 20 years | 120 months (50%) |

Marriages over 20 years may receive indefinite maintenance.

### Statutory factors (mandatory consideration)

The court must consider:

- Financial resources of each party
- Marketable skills and educational background
- Time required to acquire training
- Standard of living during marriage
- Length of the marriage
- Age and health of each party
- Ability of the obligor to pay while supporting himself / herself

### Statute of limitations / modification

Maintenance is modifiable on a **"substantial and continuing
change of circumstances"** under C.R.S. § 14-10-122(1)(a). Common
triggers: job loss, retirement, remarriage of the recipient
(terminates), cohabitation (may terminate).

## Child support — C.R.S. § 14-10-115

Colorado uses the **income-shares model**. Both parents' incomes
are pooled, the guideline assigns a basic support amount, and that
amount is divided between the parents in proportion to their
respective incomes.

### Calculating child support

The official child-support **worksheet** is **JDF 1820 E** (online
worksheet calculator) at:

**https://www.coloradojudicial.gov/forms/child-support-calculator**

Inputs:

- Both parents' **gross monthly income** (with adjustments for
  pre-existing court-ordered support, taxes, etc.)
- **Number of overnights** with each parent (parenting time)
- **Cost of work-related child care**
- **Cost of health insurance** for the child
- **Extraordinary medical expenses** (regular but recurring)

Outputs:

- Basic child-support obligation
- Each parent's share
- Recommended order amount

### Parenting-time adjustment

When the obligor has **at least 93 overnights per year**, the
guideline shifts to a **shared physical care** formula that
reduces the obligor's basic obligation proportionally. This is the
**"93-overnight rule"** — see C.R.S. § 14-10-115(8).

### Imputation of income

If a parent is **voluntarily unemployed or underemployed**, the
court may **impute income** based on potential earning capacity —
C.R.S. § 14-10-115(5)(b). The court considers prior employment,
education, available jobs in the local market, and reasons for the
employment decision.

### Duration

Child support continues until each child turns **19** (or 21 if the
child is incapacitated or still in high school), at which point the
order terminates as to that child but continues as to younger
children if any — C.R.S. § 14-10-115(13)(a).

### Enforcement

The Colorado **Child Support Services (CSS)** within the Department
of Human Services enforces child-support orders, including:

- Wage withholding (automatic on every order)
- License revocation
- Tax refund interception
- Contempt
- Criminal non-support (C.R.S. § 14-6-101 — willful non-support)

### Modification

Child support can be **modified** when the guideline calculation
results in **at least a 10% change** from the existing order
amount **and** the change is "substantial and continuing" — C.R.S.
§ 14-10-122(1)(b). The 10% threshold is a bright-line rule.

## Parental responsibilities and parenting time — C.R.S. § 14-10-124

Colorado replaced "custody" terminology with **"parental
responsibilities"** in 1998 (S.B. 98-093). The court allocates:

1. **Decision-making responsibility** (analogous to "legal
   custody") — who decides on major issues (education, medical
   care, religion, extracurriculars). Can be **joint** or **sole**.
2. **Parenting time** (analogous to "physical custody") — the
   schedule of when the child is with each parent.

### Best-interests standard

The court applies the **best interests of the child** standard
under C.R.S. § 14-10-124(1.5), considering:

- Wishes of the child (if mature)
- Wishes of the parents
- Relationship between the child and each parent
- Adjustment of the child to home, school, community
- Mental and physical health of all individuals
- Ability of each parent to encourage a relationship with the
  other parent
- Past involvement of each parent
- Geographic proximity of the parents
- History of domestic violence or child abuse (under C.R.S.
  § 14-10-124(4), domestic violence is a significant negative
  factor against unsupervised parenting time)

### Parenting plan — JDF 1129

The parties (or the court if contested) develop a **Parenting Plan**
addressing:

- Regular parenting-time schedule (typically a 2-2-3 or 50/50 or
  4-3 schedule)
- Holiday schedule
- Summer / school-break schedule
- Decision-making allocation
- Communication protocols (text, email, FamilyWizard, etc.)
- Travel and relocation procedures
- Methods for resolving future disputes (mediation clause)

### Modification of parental responsibilities

Modification of **parenting time** (frequency, not designation)
requires showing it is in the child's best interests — C.R.S.
§ 14-10-129. **Decision-making modification** requires a higher
showing — that the existing order is **physically or emotionally
endangering** the child — C.R.S. § 14-10-131.

**Relocation**: a parent seeking to relocate the child more than 100
miles or out of state must comply with C.R.S. § 14-10-129(2) —
**90-day notice** to the other parent and court approval.

## Common-law marriage

Colorado is one of a small number of states still **recognizing
common-law marriage**. The standard:

- *People v. Lucero*, 747 P.2d 660 (Colo. 1987) — traditional test:
  cohabitation + mutual agreement to be married + public reputation
  as married + acting as married couple
- *In re Marriage of Hogsett & Neale*, 2021 CO 1 — modernized test:
  same elements but **gender-neutral** and considering modern factors
  (joint tax returns, beneficiary designations, joint accounts, use
  of "husband/wife"/"spouse" terminology, marital references in
  social media, etc.)

When asserting common-law marriage in a dissolution, plead it
specifically in the petition (or response) and prepare to prove it
at the permanent-orders hearing.

## Same-sex marriage

Colorado has fully recognized same-sex marriages since **October
2014** (federal recognition via *Obergefell v. Hodges*, 576 U.S.
644 (2015)). All UDMA provisions apply equally. Common-law marriage
applies to same-sex couples per *Hogsett & Neale*.

## Common pro se mistakes

1. **Filing a dissolution petition when you wanted an annulment** —
   the grounds for declaration of invalidity are narrow; verify
   before filing.
2. **Missing the C.R.C.P. 16.2 SFS deadline (42 days)** — the
   sanction can include reversal of property division.
3. **Underreporting income on the SFS** — perjury; can also lead to
   reversal of the decree.
4. **Not calculating child support with the official worksheet** —
   judge will require the worksheet; submit JDF 1820 with the
   inputs documented.
5. **Trying to negotiate custody language as "primary custody"** —
   Colorado replaced that term in 1998; use "parental
   responsibilities" / "decision-making" / "parenting time" only.
6. **Filing for divorce before meeting the 91-day residency** —
   the court will dismiss for lack of jurisdiction; wait until day
   91.
7. **Filing for dissolution while parties are not yet "separated"
   under § 14-10-106** — no formal separation required, but the
   factual basis for "irretrievably broken" should be alleged in
   the petition.

## Jefferson County-Specific Resources

### 1st JD Family Court Services

- **Self-Help Center**: 100 Jefferson County Parkway, 1st Floor
  - Walk-in hours: Monday-Friday, 8:00 AM - 4:00 PM
  - Forms assistance, procedural guidance, referrals
  - Spanish-language assistance available
- **Family Court Facilitator**: Room 1020
  - Reviews pro se documents for completeness
  - Cannot provide legal advice but can explain procedures
  - Appointment recommended: (303) 271-6540
- **Mediation Services**: Office of Dispute Resolution
  - Court-ordered mediation coordinator: (303) 271-6850
  - Sliding-fee scale available for qualified parties
- **Parenting Coordination**: For high-conflict cases
  - Court maintains approved PC roster
  - Typically appointed by court order after repeated disputes

### Jefferson County Child Support Services

- **Location**: 900 Jefferson County Parkway, Golden, CO 80401
- **Phone**: (303) 271-4300
- **Services**: Establishment, modification, enforcement
- **Walk-in hours**: Tuesday and Thursday, 8:00 AM - 3:00 PM

### Important Jefferson County Family Law Contacts

- **Clerk of Court (Family Division)**: (303) 271-6390
- **Case Management**: (303) 271-6215
- **CCEFS Help Desk**: (303) 271-6560
- **Law Library**: (303) 271-6335 (self-help resources)
- **Victim Services** (DV cases): (303) 271-6959
- **1st JD Website**: www.courts.state.co.us/Courts/District/Index.cfm?District_ID=1

## Composition

- For statewide format: `co-statewide-format`
- For drafting the petition / response / motion:
  `co-draft-motion`
- For declarations: `co-draft-declaration`
- For the proposed decree: `co-draft-order`,
  `co-submit-order`
- For the specific court: `co-denver`, `co-arapahoe`,
  `co-county-courts` (includes Jefferson County details)
- For pro se workflows + JDF forms: `co-pro-se`
- For deadlines (91-day waiting period, 42-day SFS): `co-deadlines`
- For hearings: `co-hearings`
- For post-decree modification: `co-post-judgment` (some overlap),
  this skill

## References

- `references/udma-overview.md` — full UDMA structural map
- `references/dissolution-procedure.md` — step-by-step procedure
- `references/annulment-grounds.md` — declaration of invalidity in
  detail
- `references/legal-separation.md` — separation vs. dissolution
  vs. annulment
- `references/crcp-16-2-disclosures.md` — Sworn Financial Statement
  and supporting docs
- `references/maintenance-calculation.md` — § 14-10-114 guideline
  with example computations
- `references/child-support-guideline.md` — § 14-10-115 income-
  shares with worksheet inputs
- `references/parental-responsibilities.md` — § 14-10-124
  best-interests framework
- `references/parenting-plan-template.md` — JDF 1129-style scaffold
- `references/common-law-marriage.md` — Lucero / Hogsett & Neale
  framework
- `references/post-decree-modification.md` — § 14-10-122 standards
- `references/uccjea.md` — home-state jurisdiction over children
- `references/jdf-family-forms.md` — annotated index (JDF 1099,
  1100, 1102, 1104, 1111, 1116, 1129, 1820 E, etc.)
