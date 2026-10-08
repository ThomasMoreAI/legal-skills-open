---
name: id-family-court-codearranger
title: Idaho Family Court — Magistrate Division of the District Court
description: 'Use to choose venue and handle filing mechanics for an Idaho domestic-relations case heard in the Magistrate Division of the District Court — divorce, legal separation, separate maintenance, annulment, child support, custody, parenting time, grandparent visitation, and paternity. CRITICAL FLAG: Idaho family cases run on the SEPARATE Idaho Rules of Family Law Procedure (I.R.F.L.P.), not the I.R.C.P., with their own form-of-documents rule (I.R.F.L.P. 208) and mandatory disclosures. Covers venue (county of residence), the "In re the Marriage of" caption, intake, magistrate procedure, iCourt / Odyssey "Guide & File" self-help filing, and Idaho Court Assistance Office forms. Triggers: "file for divorce in Idaho", "Idaho Magistrate Division", "Bonneville County divorce", "Ada County divorce", "I.R.F.L.P.", "Idaho family law procedure", "Idaho Guide & File". Venue and procedural skill; defers substantive law to `id-family-law`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Idaho Family Court — Magistrate Division of the District Court

> **NOT LEGAL ADVICE.** Divorce, custody, support, and parentage
> outcomes have lasting consequences for children, property, and
> finances. Strongly consider consulting a licensed Idaho family-law
> attorney even on an agreed or "simple" matter. This skill is a
> drafting/venue aid; verify the filing county's current local rules
> and the controlling statutes and rules before filing.

Idaho has **no separate, free-standing family trial court**. Family
matters are heard in the **Magistrate Division of the District
Court**. Idaho is organized into **seven judicial districts**; each
county's District Court has a Magistrate Division, and the magistrate
judges hear domestic-relations cases. (For example, **Ada County** is
in the **Fourth Judicial District** (Boise) and **Bonneville County**
is in the **Seventh Judicial District** (Idaho Falls).) This skill
covers **where to file and filing mechanics**. For substantive law —
divorce grounds, community-property division, the maintenance factors,
the child-support guidelines, the best-interests custody standard,
relocation, UCCJEA/UIFSA — see `id-family-law`. For document form, see
`id-statewide-format`.

## CRITICAL: family cases run on the I.R.F.L.P., not the civil rules

Idaho domestic-relations cases are governed by the **Idaho Rules of
Family Law Procedure (I.R.F.L.P.)** — a **separate, self-contained
rule set** distinct from the **Idaho Rules of Civil Procedure
(I.R.C.P.)**. Do not import a civil-rules deadline, motion form, or
discovery practice into a family case without confirming the
I.R.F.L.P. analog. Key consequences:

- **Scope is fixed by I.R.F.L.P. 101.** The Family Law Rules govern
  proceedings for **annulment, divorce, legal separation, separate
  maintenance, child support, custody, grandparent visitation, and
  paternity**. Confirm the current text of I.R.F.L.P. 101 in
  `../id-law-references/references/court-rules/`.
- **Form of documents runs under I.R.F.L.P. 208** — the family analog
  to the I.R.C.P. form-of-documents rule. Use I.R.F.L.P. 208 (not the
  generic I.R.C.P. spec) for the caption and the form of family-case
  papers. See "Form of documents" below.
- **Mandatory disclosures are front-loaded.** The I.R.F.L.P. require
  each party to make **mandatory financial disclosures** (income,
  assets, debts, and supporting documents, plus the information needed
  for support and parenting where children are involved). Treat
  disclosure as an up-front obligation, not discovery you wait to be
  asked for; confirm the current disclosure rule and timing in the
  corpus.
- **Procedure is magistrate-tailored** — the petition/response
  framework, temporary orders, and family-specific motion practice run
  under the I.R.F.L.P.

Flag the I.R.F.L.P.-vs-I.R.C.P. distinction prominently in any family
filing.

## What this venue handles

| Matter | Heard in the Magistrate Division under the I.R.F.L.P.? |
|---|---|
| Divorce (decree of divorce) | **Yes** (I.C. § 32-601 et seq.) |
| Legal separation / separate maintenance | **Yes** |
| Annulment | **Yes** |
| Property division, spousal maintenance | Yes — with the divorce (I.C. § 32-712 / § 32-705) |
| Child custody and parenting time | **Yes** (I.C. § 32-717) |
| Child support and enforcement | **Yes** (I.C. § 32-706 + I.R.F.L.P. 120 Guidelines) |
| Grandparent visitation | **Yes** (I.R.F.L.P. 101 scope) |
| Paternity / parentage | **Yes** |
| Modification / enforcement of family orders | **Yes** |
| **Civil protection orders** | **No — NOT under the I.R.F.L.P.** (see below) |

> **Terminology.** Use **Petitioner** and **Respondent** for the
> parties, the **Magistrate Division** for the forum, and **decree of
> divorce** for the dissolving order. The dissolving judge is the
> **magistrate judge**.

## Civil protection orders are a SEPARATE track

Civil protection orders are **not** governed by the I.R.F.L.P.
(I.R.F.L.P. 101 does not list them). They are issued under the
**Domestic Violence Crime Prevention Act, I.C. § 39-6301 et seq.**, on
their own statutory procedure. A protection-order petition runs on a
distinct intake path even when the same parties also have a pending
divorce or custody case in the Magistrate Division — coordinate the
two cases but do not fold the protection order into the I.R.F.L.P.
petition. The substantive overlay (how a protection order bears on the
best-interests custody analysis) lives in `id-family-law`; the
distinct procedure is flagged here so it is not assumed to follow the
family-law rules.

> Adoption, termination of parental rights, guardianship, and child
> protective (CPN) proceedings are likewise outside the I.R.F.L.P. 101
> scope; confirm the governing rule set before treating any of them as
> a family-law matter under these rules.

## Venue and jurisdiction

- File in the **District Court (Magistrate Division) for the county of
  residence.** Venue for a domestic-relations action is the county
  where a party resides; confirm the residency/venue requirement for
  the specific cause of action.
- Confirm Idaho's **residency requirement for divorce** (the
  petitioner's required period of residence in the state before
  filing) — see `id-family-law`.
- If there are minor children, confirm Idaho is the child's **home
  state** under the **UCCJEA** (I.C. § 32-11-101 et seq.) and plead the
  jurisdictional allegations (`id-family-law`).
- Confirm the county's Magistrate Division assignment and
  case-management practice with the relevant venue skill
  (`id-bonneville`, `id-county-courts`).

## The caption — "In re the Marriage of" / "In re"

Family-case captions in the Magistrate Division typically read **In re
the Marriage of** for divorce, legal separation, and separate
maintenance (naming both spouses as Petitioner and Respondent), or
**In re** for the underlying status proceeding. Build the caption
under **I.R.F.L.P. 208** with the District Court / Magistrate Division
designation, the county, and the judicial district. Designate the
parties **Petitioner** and **Respondent**. See `id-statewide-format`
for the line-numbered pleading paper, footer, and signature
conventions, and confirm the I.R.F.L.P. 208 caption form in the
corpus.

## Form of documents (I.R.F.L.P. 208)

Family-case papers follow **I.R.F.L.P. 208**, which parallels the
I.R.C.P. form-of-documents rule: **8½ × 11** paper, body text of at
least **11-point** type, and **double or 1.5** line spacing.
Electronically filed family documents are filed through **iCourt /
Odyssey File & Serve (I.R.E.F.S.)**. Run the document form against
`id-statewide-format` and confirm the current I.R.F.L.P. 208 text in
`../id-law-references/references/court-rules/`.

## Filing mechanics

1. **Confirm jurisdiction and venue** — Magistrate Division of the
   county of residence; divorce residency; UCCJEA home-state
   allegations for children (`id-family-law`).
2. **Prepare the initiating documents** — the petition stating the
   statutory basis (divorce ground, custody, support, paternity); for
   matters with children, the custody/parenting and support
   allegations. Use **I.R.F.L.P. 208** for the caption and form via
   `id-statewide-format`, and `id-draft-motion` /
   `id-draft-declaration` / `id-draft-order` for the documents.
3. **Build the mandatory financial disclosures early** — assemble the
   income, asset, debt, and supporting-document disclosure required by
   the I.R.F.L.P. at the outset, not when asked.
4. **Use the Idaho Court Assistance Office / "Guide & File" forms** —
   self-represented filers can prepare Idaho's official family-law
   form packets (divorce with/without children, custody, modification,
   paternity) through the Court Assistance Office self-help portal
   (**courtselfhelp.idaho.gov**) and the **Odyssey "Guide & File"**
   guided-interview tool, which assembles the petition and supporting
   forms for filing through iCourt. Confirm the current packet and
   that the county accepts it.
5. **File and pay (or waive) the fee** — with the District Court
   Clerk; a **fee waiver** may be available for qualifying
   self-represented filers. Confirm the county's filing fee and the
   I.R.E.F.S. e-filing path for the case type (`id-file-packet`, and
   the venue skill).
6. **Serve** the petition under the applicable service rule within the
   service period; the response window runs under the I.R.F.L.P.
   (`id-first-30-days`).
7. **Disclosure and waiting period** — exchange the mandatory
   financial disclosures and track the divorce **waiting period** tied
   to **I.C. § 32-716** (do not assume an exact day count — see
   `id-family-law` and `id-deadlines`).

## Self-represented (pro se) family intake

- Idaho provides extensive **Court Assistance Office** resources and
  official form packets for family matters through
  **courtselfhelp.idaho.gov** and the **Guide & File** guided
  interview. Confirm the current packet and the county's acceptance.
- Designate the filer clearly as self-represented in the signature
  block (no Idaho State Bar number) — see `id-pro-se`.
- Clerks and Court Assistance Office staff explain **procedure**, not
  legal advice. Encourage consultation with a licensed Idaho
  family-law attorney where there are minor children, retirement
  assets, real property, a business, safety concerns, or any disputed
  issue.
- If a party needs a disability accommodation for any hearing or
  filing step, route the request through `id-ada`.

## Composition

- For substantive law (divorce grounds, community-property
  classification and division, spousal maintenance, the I.R.F.L.P. 120
  child-support guidelines, the best-interests custody standard and
  the joint-custody presumption, relocation, UCCJEA/UIFSA, and the
  protection-order substantive overlay): `id-family-law`
- For document format and the I.R.F.L.P. 208 caption:
  `id-statewide-format`
- For the specific county / clerk / Magistrate Division assignment and
  e-filing: `id-bonneville`, `id-county-courts`
- For pro se conventions and Court Assistance Office forms:
  `id-pro-se`
- For the response and first-response window under the I.R.F.L.P.:
  `id-first-30-days`
- For deadlines, the waiting period, and time computation:
  `id-deadlines`
- For drafting the petition / response / motion: `id-draft-motion`
- For sworn declarations / financial affidavits: `id-draft-declaration`
- For the proposed decree / order: `id-draft-order`, `id-submit-order`
- For assembling and preflighting the filing packet (I.R.E.F.S.):
  `id-file-packet`
- For scheduling and hearings: `id-schedule-hearing`, `id-hearings`
- For disability accommodations: `id-ada`
- For citation verification: `id-fact-check`
- For canonical I.R.F.L.P. text, the child-support guidelines, and the
  Title 32 statutes: `id-law-references`

## References

- `../id-law-references/references/court-rules/` — the I.R.F.L.P.
  verbatim, including **I.R.F.L.P. 101** (scope), **I.R.F.L.P. 120**
  (child-support guidelines + worksheets), and **I.R.F.L.P. 208**
  (form of documents / caption); the I.R.C.P. and I.R.E.F.S. for
  cross-reference
- `../id-law-references/references/id-statutes-debt/` and the Idaho
  Code Title 32 corpus — the substantive family statutes invoked in
  the petition (cross-referenced from `id-family-law`)
