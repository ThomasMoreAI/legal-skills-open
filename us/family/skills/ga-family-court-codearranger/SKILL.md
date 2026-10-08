---
name: ga-family-court-codearranger
title: Georgia Family Court — Family Matters in the Superior Court
description: 'Use to choose venue and handle filing mechanics for a Georgia domestic-relations case — divorce, separate maintenance, annulment, custody and visitation, child support, legitimation and paternity, contempt and modification, adoption, termination of parental rights, and family-violence protective orders. CRITICAL: Georgia has NO separate statewide family-court trial court — these cases are heard in the SUPERIOR COURT (general-jurisdiction trial court), with divorce jurisdiction vested by O.C.G.A. § 19-5-1. Some high-volume circuits run a Family Division or family case-management track by local rule / standing order. Triggers: "where do I file for divorce in Georgia", "Fulton family division", "Superior Court family case", "custody filing Georgia", "Cobb County divorce", "Georgia legitimation filing", "Georgia child support case", "Georgia parenting plan", "Georgia TPO family violence", "Petitioner Respondent divorce Georgia". Venue and procedural skill; defers substantive law
  to `ga-family-law`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Georgia Family Court — Family Matters in the Superior Court

> **NOT LEGAL ADVICE.** Divorce, custody, support, legitimation, and
> family-violence outcomes have lasting consequences for children,
> property, and safety. Strongly consider consulting a licensed
> Georgia family-law attorney even on an agreed or "simple" matter.
> This skill is a drafting/venue aid; verify the filing county's
> current local rules, any Family Division standing order, and the
> controlling statutes before filing. Local rules and judge-specific
> practices change; confirm with the clerk first.

Georgia has **no separate, free-standing family-court trial court**
and **no single statewide Family Division statute.** Domestic-relations
matters are heard in the **Superior Court** — Georgia's
general-jurisdiction trial court. Divorce jurisdiction is **vested in
the Superior Court by O.C.G.A. § 19-5-1.** Several high-volume circuits
run a **Family Division or a family case-management track by local
rule or standing order** — for example, **Fulton County Superior Court**
and **DeKalb** operate dedicated Family Divisions, and **Cobb (Cobb
Judicial Circuit, Marietta)** and **Gwinnett (Gwinnett Judicial
Circuit, Lawrenceville)** run family case-management tracks. Treat the
**existence and procedure of any Family Division as a per-court
(venue-specific) detail** to verify with the local clerk and the
controlling standing order. This skill covers **where to file and
filing mechanics**; substantive law lives in `ga-family-law`.

## Procedure is the Civil Practice Act

Georgia family cases run on the **Georgia Civil Practice Act (O.C.G.A.
Title 9, Ch. 11)** and the **Uniform Superior Court Rules**, in the
Superior Court. Title 19 (Domestic Relations) supplies the substantive
law and certain special procedures (the waiting period, the mandatory
parenting plan, the financial-disclosure requirements). A circuit's
**Family Division standing order** — common in family cases — may add
**mutual restraining provisions** (preserving the status quo, barring
dissipation of assets, restricting relocation of children) and
**mandatory parenting seminars** that take effect on filing. These are
**per-circuit**: confirm whether the filing court has a standing order
and what it requires before filing.

## What this venue handles

| Matter | Heard in the Superior Court? |
|---|---|
| Divorce / separate maintenance / annulment | **Yes** (O.C.G.A. § 19-5-1) |
| Equitable division of property | Yes — with the divorce |
| Alimony | Yes — with the divorce (O.C.G.A. § 19-6-1 et seq.) |
| Custody and visitation | **Yes** (O.C.G.A. § 19-9-3) |
| Child support and modification | **Yes** (O.C.G.A. § 19-6-15) |
| Legitimation | **Yes** (O.C.G.A. § 19-7-22) |
| Paternity | **Yes** (O.C.G.A. § 19-7-40 et seq.) |
| Contempt and modification | **Yes** |
| Adoption | **Yes** |
| Termination of parental rights | **Yes** |
| **Family-violence protective orders (TPOs)** | **Yes** (O.C.G.A. § 19-13-1 et seq.) — distinct procedure (see below) |
| UCCJEA / UIFSA jurisdiction | O.C.G.A. § 19-9-40 et seq. / § 19-11-100 et seq. |

> **Terminology.** Use **Petitioner** and **Respondent** for the
> parties and the **Superior Court** (or its Family Division, where the
> circuit has one) for the forum. Note that **legitimation and paternity
> are distinct** — a paternity action establishing support does not by
> itself confer custody or visitation; legitimation under § 19-7-22 is
> the vehicle for an unwed biological father's parental rights. Confirm
> the right vehicle against `ga-family-law`.

## Required filings unique to family cases

- **Domestic Relations Financial Affidavit (DRFA).** A sworn statement
  of income, expenses, assets, and debts is a **standard required
  filing** in contested divorce, support, and modification matters.
  Confirm the circuit's current form and exchange/filing deadline with
  the local rule. Use `ga-draft-declaration` for the sworn form.
- **Child Support Worksheet.** Where children are involved, the
  **Georgia Child Support Worksheet** generated through the **Georgia
  Child Support Commission calculator** (the official income-shares
  worksheet) is a standard required filing. The substantive
  income-shares calculation (BCSO table, add-ons, deviations) lives in
  `ga-family-law` (O.C.G.A. § 19-6-15).
- **Parenting Plan — mandatory.** A **Parenting Plan is mandatory under
  O.C.G.A. § 19-9-1** in any case involving custody/visitation of a
  minor child (schedule, holidays, decision-making, transportation).
  The court will not enter a final custody order without one. The
  required contents are detailed in `ga-family-law`.

## Family-violence protective orders are a distinct track

A **family-violence Temporary Protective Order (TPO)** under **O.C.G.A.
§ 19-13-1 et seq.** runs on its **own statutory procedure** — even when
the same parties have a pending divorce or custody case. Coordinate the
two cases but do not fold the TPO petition into the divorce/custody
filing. Key framework features to verify against `ga-family-law`:

- **Free to file** — no filing fee for a family-violence TPO petition;
  use the standardized **GSCCCA** TPO forms.
- **Venue** is the **respondent's county** (O.C.G.A. § 19-13-2).
- The court may issue an **ex parte TPO** good for **up to 30 days**,
  with a **mandatory hearing within ~30 days** (O.C.G.A. § 19-13-3);
  after a hearing the court may enter a protective order up to one year
  (extendable).

TPO matters are time-sensitive and often involve safety concerns;
encourage prompt consultation with counsel or a local family-violence
advocate.

> Adoption and termination of parental rights are likewise specialized
> proceedings with heightened procedure; confirm the governing
> statutory scheme before treating them as an ordinary family matter.

## Venue and jurisdiction

- File in the **Superior Court of the county of proper venue.** For
  divorce, venue is **generally the respondent's county** (**O.C.G.A.
  § 19-5-2**); confirm the Georgia **residency** prerequisite (a bona
  fide resident period before filing) against `ga-family-law` and
  § 19-5-2.
- For a family-violence TPO, venue is the **respondent's county**
  (§ 19-13-2).
- If there are minor children, confirm Georgia is the child's **home
  state** under the **UCCJEA (O.C.G.A. § 19-9-40 et seq.)** and plead
  the jurisdictional allegations (`ga-family-law`).
- Confirm the circuit's family-docket assignment, **whether a Family
  Division or family case-management track applies**, and any
  **automatic standing order** with the venue skill (`ga-fulton`,
  `ga-cobb`, `ga-gwinnett`, `ga-county-courts`).

## The caption and parties

Designate the parties **Petitioner** and **Respondent** and the forum
the **Superior Court** of the county (its **Family Division** where the
circuit runs one). Build the caption under `ga-statewide-format` (the
O.C.G.A. § 9-11-10 caption, the Uniform Superior Court Rules form, and
the signature block).

## Filing mechanics

1. **Confirm jurisdiction and venue** — Superior Court of the proper
   county; divorce residency and venue (**§ 19-5-2**); TPO venue
   (**§ 19-13-2**); UCCJEA home-state allegations for children
   (`ga-family-law`).
2. **Check the circuit's Family Division / standing order** — determine
   whether the filing court has a Family Division or family
   case-management track and whether an **automatic standing order**
   (mutual restraining provisions, mandatory parenting seminar) takes
   effect on filing; comply with and serve it as the local rule
   requires.
3. **Prepare the initiating documents** — the **Petition for Divorce**
   (or Petition for Legitimation / Petition to Establish Paternity /
   Petition for Modification / Petition for Contempt), pleading the
   statutory ground and the custody/support/property requests. Use
   `ga-statewide-format` for the caption and form and `ga-draft-motion`
   / `ga-draft-declaration` / `ga-draft-order` for the documents.
4. **Assemble the required family filings** — the **Domestic Relations
   Financial Affidavit**, the **Child Support Worksheet** (Georgia
   Child Support Commission calculator) where children are involved,
   and the **mandatory Parenting Plan (§ 19-9-1)** for any custody
   matter.
5. **File and pay (or waive) the fee** — with the **Clerk of Superior
   Court** of the county. A self-represented filer who cannot afford
   costs may file a **poverty affidavit / pauper's affidavit under
   O.C.G.A. § 9-15-2** to proceed without prepayment of costs (a
   family-violence TPO petition is free to file). Confirm the county's
   filing fee and the e-filing path: Georgia counties file electronically
   through **PeachCourt** or **Odyssey eFileGA**, depending on the
   county (`ga-file-packet`, and the venue skill).
6. **Serve** the petition under the applicable service rule (personal
   service of the summons and petition); track the **answer/response**
   window under the Civil Practice Act (`ga-first-30-days`). For a TPO,
   the ex parte order and hearing notice are served on the respondent.
7. **Track the waiting period and disclosures** — confirm the **divorce
   waiting period** (no final no-fault divorce until the statutory
   period runs after service) against `ga-family-law` and § 19-5-3, and
   complete any mandatory parenting seminar (`ga-deadlines`,
   `ga-schedule-hearing`).

## Self-represented (pro se) family intake

- Georgia courts publish self-help family-law **forms and packets**
  (uncontested divorce with/without minor children, legitimation,
  modification) through the Judicial Council / Administrative Office of
  the Courts and the county clerks; **GSCCCA** publishes the standardized
  **family-violence TPO** forms. Confirm the current packet and that the
  county accepts it.
- File with the **Clerk of Superior Court** of the county of proper
  venue (generally the respondent's county, § 19-5-2). Designate the
  filer clearly as self-represented in the signature block (no State Bar
  of Georgia number) — see `ga-pro-se`.
- Clerks and self-help-center staff explain **procedure**, not legal
  advice. Encourage consultation with a licensed Georgia family-law
  attorney where there are minor children, retirement assets, real
  property, a business, safety concerns, or any disputed issue.

## Composition

- For substantive law (divorce grounds and the waiting period, equitable
  division, alimony, the § 19-9-3 best-interests custody analysis and
  the child's-election rule, the § 19-6-15 income-shares child-support
  calculation, legitimation vs. paternity, the mandatory parenting plan,
  UCCJEA/UIFSA, and the family-violence overlay): `ga-family-law`
- For document format and the Georgia caption: `ga-statewide-format`
- For the specific county / clerk / Family Division assignment and
  e-filing: `ga-fulton`, `ga-cobb`, `ga-gwinnett`, `ga-county-courts`
- For pro se conventions and self-help forms: `ga-pro-se`
- For the response and the first-30-days posture: `ga-first-30-days`
- For deadlines, the divorce waiting period, and time computation:
  `ga-deadlines`
- For drafting the petition / response / motion: `ga-draft-motion`
- For the Domestic Relations Financial Affidavit and other sworn
  declarations: `ga-draft-declaration`
- For the proposed parenting plan / decree / order: `ga-draft-order`,
  `ga-submit-order`
- For assembling and preflighting the filing packet: `ga-file-packet`
- For scheduling and hearings: `ga-schedule-hearing`, `ga-hearings`
- For citation verification: `ga-fact-check`

## References

- `references/family-division-local-practice.md` — how the high-volume
  circuits (Fulton, DeKalb, Cobb, Gwinnett) run Family Divisions /
  family case-management tracks and their standing orders; per-circuit
  verification pointers
- `references/intake-checklist.md` — the family-case filing checklist
  (venue, required affidavit/worksheet/parenting plan, fee or pauper's
  affidavit, e-filing path, service)
- `references/required-financial-affidavit.md` — the Domestic Relations
  Financial Affidavit and Child Support Worksheet requirements and
  contents
- `references/tpo-intake.md` — the family-violence TPO intake path
  (free filing, GSCCCA forms, ex parte order, hearing within ~30 days,
  § 19-13-1 et seq.)
- `../ga-law-references/references/court-rules/` — the Civil Practice
  Act, Uniform Superior Court Rules, and county local-rule / standing-
  order pointers for cross-reference
