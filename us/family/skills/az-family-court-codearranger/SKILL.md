---
name: az-family-court-codearranger
title: Arizona Family Court — Family Department of the Superior Court
description: 'Use to choose venue and handle filing mechanics for Arizona domestic-relations case in Family Department of Superior Court — dissolution, legal separation, annulment, legal decision-making, parenting time, child support, spousal maintenance, paternity, protective orders. CRITICAL FLAG: family cases run on SEPARATE Arizona Rules of Family Law Procedure (ARFLP), not ARCP, with mandatory disclosure (Rule 49). Covers venue, Conciliation Court, parent information program, parenting conferences, mediation, AZTurboCourt e-filing, family forms. Triggers: "Arizona family court", "file for divorce Arizona", "dissolution of marriage Arizona", "Arizona legal decision-making parenting time", "ARFLP Arizona family rules", "Arizona order of protection", "Conciliation Court Arizona", "Arizona parenting plan", "Arizona Rule 49 disclosure". Venue/procedural skill; defers substantive law to `az-family-law`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Arizona Family Court — Family Department of the Superior Court

> **NOT LEGAL ADVICE.** Dissolution, legal-decision-making, support, and
> protective-order outcomes have lasting consequences for children,
> property, and safety. Strongly consider consulting a licensed Arizona
> family-law attorney even on an agreed or "simple" matter. This skill
> is a drafting/venue aid; verify the venue's current local rules and
> the controlling statutes and rules before filing.

Arizona has **no separate family trial court**. Family matters are heard
in the **Family Department (Family Court) of the Superior Court**, which
has **exclusive original jurisdiction** over Title 25 (Marital and
Domestic Relations) matters. The Superior Court is a single statewide
court sitting county-by-county; the Family Department is the division
that handles domestic-relations cases. This skill covers where to file
and filing mechanics. For substantive law (grounds, the
legal-decision-making best-interests factors, the child-support
guidelines, spousal-maintenance guidelines, parentage), see
`az-family-law`. For document form, see `az-statewide-format`.

## CRITICAL: family cases run on the ARFLP, not the civil rules

Arizona family cases are governed by the **Arizona Rules of Family Law
Procedure (ARFLP)** — a **separate, self-contained rule set** distinct
from the **Arizona Rules of Civil Procedure (Ariz. R. Civ. P.)**. Do not
import a civil-rules deadline, motion form, or discovery practice into a
family case without confirming the ARFLP analog. Key consequences:

- **Pleadings and procedure follow the ARFLP**, including the petition/
  response framework, temporary orders, and the family-specific motion
  practice. Confirm the current rule number in `references/` — the ARFLP
  is periodically renumbered.
- **Mandatory disclosure runs under ARFLP Rule 49**, the family analog to
  civil disclosure. Rule 49 requires each party to disclose income,
  assets, debts, and supporting financial documents (and, where children
  are involved, the information needed for support and parenting). Treat
  Rule 49 disclosure as a front-loaded obligation, not discovery you wait
  to be asked for.
- **Discovery is limited** and family-tailored — verify the current ARFLP
  discovery rules before serving civil-style interrogatories or requests.

Flag the ARFLP-vs-civil distinction prominently in any family filing.

## What this venue handles

| Matter | Heard in the Family Department? |
|---|---|
| Dissolution of marriage (divorce) | **Yes** (A.R.S. § 25-311 et seq.) |
| Legal separation | **Yes** |
| Annulment | **Yes** |
| Property division, spousal maintenance | Yes — with the dissolution (§ 25-318 / § 25-319) |
| **Legal decision-making and parenting time** | **Yes** (A.R.S. § 25-401 et seq.) |
| Child support and enforcement | **Yes** (A.R.S. § 25-320) |
| Paternity / parentage | **Yes** (A.R.S. § 25-801 et seq.) |
| Modification / enforcement of family orders | **Yes** |
| Protective orders (see below) | **Yes** — and other courts share jurisdiction |

> **Terminology — "legal decision-making" and "parenting time," not
> "custody."** Effective with the **2013** statutory change, Arizona
> replaced "custody" with **legal decision-making** (the authority to
> make major decisions, A.R.S. § 25-401(3)) and **parenting time** (the
> schedule of time with the child). Use the current statutory terms in
> Arizona filings; "custody" survives only in older orders and the
> UCCJEA context. Substantive standards live in `az-family-law`.

## Protective orders

Two principal tracks, both available in the Superior Court (and, for many
petitioners, in justice or municipal court — confirm the proper forum):

- **Order of Protection — A.R.S. § 13-3602.** For petitioners in a
  qualifying domestic relationship (defined by reference to the domestic-
  violence statute, A.R.S. § 13-3601). Enjoins domestic-violence
  offenses; the court may order no-contact, stay-away from residence/
  workplace/school, firearm surrender on a credible-threat finding, and
  protection of other designated persons.
- **Injunction Against Harassment — A.R.S. § 12-1809.** For petitioners
  with **no** qualifying domestic relationship — harassment defined as a
  series of acts (or one or more acts of sexual violence) directed at a
  specific person that would seriously alarm, annoy, or harass a
  reasonable person. No filing fee; an injunction generally expires
  **one year after service** unless modified — confirm current figures.

Mechanics to flag (verify current text): the court may issue the order
**without a hearing** on a sufficient showing; the defendant may **request
a hearing** to contest the order within the time the statute/rules allow;
violation is independently enforceable (e.g., arrest under A.R.S.
§ 13-2810 for an injunction against harassment). Route the petition and
order through `az-draft-motion` / `az-draft-order` and confirm the
venue's protective-order intake desk.

## Conciliation Court, parent information, and ADR

- **Conciliation Court — A.R.S. § 25-381.01 et seq.** Counties may
  operate a Conciliation Court whose statutory purpose includes promoting
  reconciliation and the amicable settlement of domestic-relations
  disputes. Either party may petition; communications in conciliation are
  confidential (A.R.S. § 25-381.16). The Conciliation Court is also the
  county vehicle for many court-connected family services.
- **Mandatory parent information program.** Arizona requires parties to a
  dissolution, legal separation, or paternity action **involving minor
  children** to attend a court-approved **parent information / education
  program** before the matter concludes — confirm the venue's program,
  deadline, and certificate-of-completion requirement.
- **Parenting conferences / ADR / mediation.** Counties refer contested
  legal-decision-making and parenting-time disputes to **parenting
  conferences**, **mediation**, or evaluations through Conciliation Court
  Services. Verify the venue's referral order, the domestic-violence
  screening practice, and any cost-sharing.

## Venue and jurisdiction

- File in the **Superior Court for the county** of proper venue. For
  dissolution, confirm the **domicile/residency requirement** (one party
  domiciled in Arizona for the statutory period before filing) under
  A.R.S. § 25-312 — see `az-family-law`.
- If there are minor children, confirm Arizona is the child's home state
  under the **UCCJEA** and plead the jurisdictional allegations.
- Confirm the county's Family Department assignment and case-management
  practice with the relevant venue skill (`az-maricopa`, `az-pima`,
  `az-superior-courts`).

## Filing mechanics

1. **Confirm jurisdiction and venue** — Family Department of the county
   Superior Court; dissolution residency/domicile; UCCJEA home-state
   allegations for children (`az-family-law`).
2. **Prepare the initiating documents** — the petition stating the
   statutory basis; for matters with children, the parenting/legal-
   decision-making allegations and the support information; the protective-
   order petition where protection is sought. Use `az-statewide-format`
   for the caption, signature, and redaction of protected identifiers, and
   `az-draft-motion` / `az-draft-declaration` / `az-draft-order` for the
   documents. Build the **ARFLP Rule 49** disclosure (financial affidavit
   / supporting documents) early.
3. **Use the Self-Service Center family forms where available** — Arizona
   courts publish self-service-center packets (dissolution with/without
   children, parenting, paternity, protective orders). Confirm the current
   packet and that the county accepts it.
4. **File and pay (or waive) the fee** — with the Superior Court Clerk; an
   **application for deferral or waiver** of fees may be available for
   qualifying self-represented filers. Confirm the county's filing fee and
   whether **AZTurboCourt** (Arizona's e-filing portal) is the filing path
   for the case type and venue (`az-file-packet`, and the venue skill).
5. **Serve** the petition under the applicable service rule within the
   service period; the response window runs under the ARFLP
   (`az-first-30-days`). Protective-order service and law-enforcement
   entry follow the protective-order rules.
6. **Disclosure and ADR** — exchange ARFLP Rule 49 disclosure; complete
   the parent information program where children are involved; expect
   referral to a parenting conference, mediation, or evaluation.

## Self-represented (pro se) family intake

- Arizona provides extensive **self-service-center** resources and form
  packets for family matters. Confirm the current packet and the county's
  acceptance.
- Designate the filer clearly as self-represented in the signature block
  (no Arizona bar number) — see `az-pro-se`.
- Clerks and self-service staff explain **procedure**, not legal advice.
  Encourage consultation with a licensed Arizona family-law attorney where
  there are minor children, retirement assets, real property, a business,
  safety concerns, or any disputed issue.

## Composition

- For substantive law (dissolution grounds and findings, the legal-
  decision-making best-interests factors under A.R.S. § 25-403, parenting
  plans, the child-support guidelines, the spousal-maintenance guidelines
  under A.R.S. § 25-319, paternity, UCCJEA/UIFSA): `az-family-law`
- For format (caption, signature, redaction): `az-statewide-format`
- For the specific county / clerk / Family Department assignment and
  e-filing: `az-maricopa`, `az-pima`, `az-superior-courts`
- For pro se conventions and self-service-center forms: `az-pro-se`
- For the response and first-response window under the ARFLP:
  `az-first-30-days`
- For deadlines and time computation: `az-deadlines`
- For assembling and preflighting the filing packet (AZTurboCourt):
  `az-file-packet`
- For scheduling and hearings: `az-schedule-hearing`, `az-hearings`
- For the proposed decree/order: `az-draft-order`, `az-submit-order`

## References

- `references/family-department-jurisdiction.md` — Superior Court
  exclusive jurisdiction over Title 25; the Family Department structure;
  venue and dissolution domicile/residency under A.R.S. § 25-312
- `references/arflp-and-rule-49.md` — the ARFLP as a separate rule set
  from the Ariz. R. Civ. P.; Rule 49 mandatory disclosure; limited
  family discovery
- `references/decision-making-parenting-time.md` — the 2013 terminology
  change; A.R.S. § 25-401 definitions; § 25-403 best interests pointer
- `references/protective-orders.md` — A.R.S. § 13-3602 order of
  protection; A.R.S. § 12-1809 injunction against harassment; issuance,
  hearing-request, and enforcement mechanics
- `references/conciliation-and-adr.md` — A.R.S. § 25-381.01 et seq.
  Conciliation Court; the parent information program; parenting
  conferences and mediation
- `references/forms-and-efiling.md` — self-service-center family form
  packets; AZTurboCourt e-filing; fee deferral/waiver
