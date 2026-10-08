---
name: tn-family-court-codearranger
title: Tennessee Family Court — Circuit and Chancery
description: Venue skill for Tennessee divorce and custody/support matters in Circuit or Chancery Courts. Covers where to file, Circuit-vs-Chancery choice, intake mechanics, jurisdiction and venue confirmation, permanent-parenting-plan requirement, UCCJEA allegations (home-state jurisdiction), mediation expectations, mandatory parenting-education seminar, self-represented (pro se) divorce packets, filing fees / fee waivers, service of process, and the 60/90-day irreconcilable-differences waiting period (§ 36-4-103). Defers substantive Title 36 law (grounds, equitable distribution, child support, alimony, parenting-plan best-interest factors, UCCJEA/UIFSA, relocation) to `tn-family-law` and document format to `tn-statewide-format`.
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Tennessee Family Court — Circuit and Chancery

> **NOT LEGAL ADVICE.** Divorce and custody decisions have lasting
> consequences for property, children, and finances. Strongly
> consider consulting a licensed Tennessee family-law attorney even
> on an agreed or "simple" divorce. This skill is a drafting/venue
> aid; verify the venue's current local rules and the controlling
> statutes before filing.

Tennessee has **no separate statewide "family court" trial court**.
Divorce and the parenting / support / property matters incident to a
marriage are heard in the **general-jurisdiction trial courts** —
**Circuit Court** and **Chancery Court**. This skill covers where to
file, how to choose between Circuit and Chancery, and the filing
mechanics. For the substantive law (grounds, equitable distribution,
child support, alimony, parenting plans), see `tn-family-law`. For
document form, see `tn-statewide-format`.

## What this venue handles

| Matter | Heard here? |
|---|---|
| Divorce (fault or irreconcilable differences) | **Yes** — Circuit or Chancery |
| Annulment / legal separation | **Yes** — Circuit or Chancery |
| Equitable distribution of property | Yes — with the divorce |
| Alimony | Yes — with the divorce |
| Permanent parenting plan, custody, and child support **incident to divorce** | Yes — with the divorce |
| Custody / support between parents who **are or were married** | Yes |
| Post-divorce modification (parenting, support, alimony) | Yes — in the court that entered the decree |
| Parentage / custody / support of children of **unmarried** parents | **No** → `tn-juvenile-court` |
| Dependency & neglect; termination of parental rights | **No** → `tn-juvenile-court` |

> Routing rule: if the parents were **never married to each other**,
> establishment of parentage and the resulting custody/support order
> is generally a **Juvenile Court** matter under Title 37 — use
> `tn-juvenile-court`, not this skill. Married-parent and
> divorce-incident parenting goes to **Circuit / Chancery**.

## Circuit vs. Chancery — choosing the court

Both **Circuit Court** (historically a court of law) and **Chancery
Court** (historically a court of equity) have **jurisdiction over
divorce** in Tennessee. A divorce can be properly filed in either.
Practical considerations in choosing:

- **Local practice and judge availability.** In many counties either
  court routinely hears divorces; the choice often turns on docket
  speed, the assigned judge or chancellor, and local custom. Check
  the county's local rules and the clerk's guidance.
- **Equitable relief.** Chancery is the traditional equity court;
  some practitioners file in Chancery where significant equitable or
  property issues (e.g., complex asset tracing, constructive trusts)
  predominate. Equitable distribution under Tenn. Code Ann. § 36-4-121
  is, however, available in either court.
- **The clerk.** In Chancery the clerk is the **Clerk and Master**;
  in Circuit the clerk is the **Circuit Court Clerk**. File with the
  correct clerk for the court chosen.
- **Some counties consolidate domestic cases.** Larger counties may
  have divisions that handle the bulk of domestic matters. Confirm
  the local assignment system before filing.

> Verify the proper **venue (county)** and any residency requirement
> for the grounds relied upon under Title 36, Chapter 4 before
> filing. Filing in the wrong county can draw a motion to transfer.

## Filing mechanics

### 1. Confirm jurisdiction and venue

- **Subject-matter jurisdiction**: Circuit or Chancery has
  jurisdiction over divorce.
- **Venue / residency**: verify the county of proper venue and the
  residency requirement keyed to where the grounds arose under
  Title 36, Chapter 4 (see `tn-family-law`).
- **Jurisdiction over children (UCCJEA)**: if there are minor
  children, confirm Tennessee is the child's home state under the
  **UCCJEA, § 36-6-201 et seq.**, and include the UCCJEA allegations.

### 2. Prepare the complaint and required attachments

- **Complaint for Divorce** stating the ground(s) under
  § 36-4-101 (commonly irreconcilable differences pleaded with
  inappropriate marital conduct in the alternative).
- If proceeding on **irreconcilable differences**, a signed **Marital
  Dissolution Agreement (MDA)** under § 36-4-103.
- If there is a **minor child**, a **Permanent Parenting Plan** under
  § 36-6-401 et seq. and a **child-support worksheet** run on the
  current Guidelines (Tenn. Comp. R. & Regs. ch. 1240-02-04).
- Any **mandatory financial disclosure** form the county's **local
  rules** require.
- Statutory **injunction**: many Tennessee divorces are subject to a
  mutual temporary injunction that issues on filing — confirm the
  current statutory injunction and whether it must be attached/served.

Use `tn-statewide-format` for the Tenn. R. Civ. P. 10 caption, Rule
11 signature, and redaction of personal identifiers. Use
`tn-draft-motion` / `tn-draft-declaration` / `tn-draft-order` for the
documents themselves, and `tn-family-law` for the substance.

### 3. File with the correct clerk and pay (or waive) the fee

- File with the **Circuit Court Clerk** or the **Clerk and Master**
  (Chancery), depending on the court chosen.
- Filing fees vary by county; a **uniform civil affidavit of
  indigency** may waive the fee for qualifying self-represented
  filers. Confirm the current form with the clerk.
- **E-filing is county-by-county** in Tennessee — there is no
  universal trial-court e-filing mandate. Some counties (e.g.,
  larger metro chancery courts) use an electronic system; others
  accept paper. Confirm the venue's platform and whether it is
  mandatory with the specific venue skill (`tn-davidson`,
  `tn-shelby`, `tn-knox`, `tn-hamilton`, `tn-county-courts`).

### 4. Serve the defendant

Serve the summons and complaint under **Tenn. R. Civ. P. 4**. The
answer is generally due **30 days** after service (`tn-first-30-days`).
For an agreed irreconcilable-differences divorce, the defendant may
sign the MDA and a waiver/joinder rather than be formally served —
confirm the current § 36-4-103 mechanics.

### 5. Observe the § 36-4-103(a) waiting period

For an irreconcilable-differences divorce, the complaint must be on
file at least **60 days** before the hearing if there is **no
unmarried minor child**, or **90 days** if there **is** an unmarried
child under 18. The clock runs from **filing**. Compute it with
`tn-deadlines`.

## The permanent-parenting-plan requirement

If the case involves a minor child, a **Permanent Parenting Plan**
under § 36-6-401 et seq. is **mandatory** before the court will enter
a final decree. The plan must allocate the residential schedule,
decision-making, and child support, and provide a dispute-resolution
mechanism. The court applies the **best-interest factors at
§ 36-6-106(a)**. See `tn-family-law` for the plan content and
factors. Many courts will not set a final hearing until a proposed
parenting plan and the completed parenting-education seminar are on
file.

## Mediation expectations

**Mediation requirements vary by county.** Many Tennessee courts
**order mediation** in contested divorce and parenting cases (often
before a final hearing will be set), and some maintain approved
mediator rosters or Tenn. Sup. Ct. R. 31 listed mediators. Some
courts require an attempt at mediation by local rule. Confirm the
venue's mediation expectation, any required pre-mediation
disclosures, and cost-sharing with the local rules and the relevant
venue skill.

## Mandatory parenting-education seminar

Divorces involving minor children require completion of a **mandatory
parent-education seminar** (commonly cited to § 36-6-408 — **verify
the current citation** and the county's approved provider). File the
completion certificate before the final hearing. Many counties also
impose the seminar requirement by **local rule**; confirm with the
venue skill.

## Self-represented (pro se) divorce intake

- Tennessee provides **approved self-represented forms** for some
  divorce situations through the Administrative Office of the Courts
  (commonly for divorces **with no minor children and limited
  property**, and a separate packet for divorces **with minor
  children**). Confirm the current AOC packet and whether the chosen
  county accepts it.
- Self-represented filers should designate themselves clearly in the
  signature block (no Tennessee bar number) — see `tn-pro-se`.
- Clerks and self-help resources can explain **procedure** but cannot
  give legal advice. Encourage consultation with a licensed Tennessee
  family-law attorney, especially where there are minor children,
  retirement assets, real property, a business, or any disputed
  issue.

## Composition

- For the substantive law (grounds, property, support, alimony,
  parenting plans, relocation, parentage, UCCJEA/UIFSA, orders of
  protection): `tn-family-law`
- For Title 37 matters (parentage, unmarried-parent custody,
  dependency/neglect, TPR): `tn-juvenile-court`
- For format (Rule 10 caption, Rule 11 signature, redaction):
  `tn-statewide-format`
- For the specific county / clerk and e-filing platform:
  `tn-davidson`, `tn-shelby`, `tn-knox`, `tn-hamilton`,
  `tn-county-courts`
- For pro se conventions and AOC forms: `tn-pro-se`
- For the answer and first-30-days response: `tn-first-30-days`
- For the 60/90-day waiting period and other deadlines:
  `tn-deadlines`
- For assembling and preflighting the filing packet: `tn-file-packet`
- For scheduling and hearings: `tn-schedule-hearing`, `tn-hearings`
- For the proposed final decree: `tn-draft-order`, `tn-submit-order`

## References

- `references/circuit-vs-chancery.md` — choosing the court; clerk
  differences (Circuit Court Clerk vs. Clerk and Master)
- `references/divorce-filing-checklist.md` — complaint, MDA, parenting
  plan, worksheet, injunction, financial disclosure
- `references/parenting-plan-requirement.md` — when a plan is required
  and what the court expects before setting a final hearing
- `references/mediation-by-county.md` — where mediation is ordered and
  approved-roster practice
- `references/pro-se-divorce-packets.md` — AOC self-represented divorce
  forms (with / without minor children)
