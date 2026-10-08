---
name: mi-family-court-codearranger
title: Michigan Family Court — Family Division of Circuit Court
description: 'Use to choose a venue and handle filing mechanics for Michigan domestic-relations cases in the Family Division of Circuit Court: divorce, custody, parenting time, child/spousal support, paternity, juvenile, adoption, name change, PPOs. Triggers include "Michigan family court", "Friend of the Court Michigan", "Michigan PPO", "file for divorce Michigan", "MCR 3.200 domestic relations", "where to file for divorce in Michigan", "Michigan child support FOC". Covers where to file, Friend of the Court''s role in support/custody/parenting-time enforcement, intake, SCAO mandatory forms, mediation expectations, and self-represented family filings. Defers substantive divorce/custody/support law to `mi-family-law` and document form to `mi-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-family-court
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: family
language: en
---

# Michigan Family Court — Family Division of Circuit Court

> **NOT LEGAL ADVICE.** Divorce, custody, support, and protection-order
> decisions have lasting consequences for children, property, and
> safety. Strongly consider consulting a licensed Michigan family-law
> attorney even on an agreed or "simple" matter. This skill is a
> drafting/venue aid; verify the venue's current local rules and the
> controlling statutes and court rules before filing.

Michigan has no freestanding "family court" trial court. Effective
**January 1, 1998**, the legislature created the **Family Division of
Circuit Court** (the "Family Court") and gave it **sole and exclusive
jurisdiction** over family matters — **MCL 600.1001 et seq.** and
**MCL 600.1021**. The Family Division consolidated matters previously
split between the Circuit Court and the Probate Court so that one
division (and, where the county's family-court plan provides, the same
judge) handles a family's related cases. This skill covers where to
file, the Friend of the Court's role, and filing mechanics. For
substantive law (grounds, custody factors, the child-support formula,
spousal support, parenting time, parentage), see `mi-family-law`. For
document form, see `mi-statewide-format`.

## What this venue handles

Under **MCL 600.1021** the Family Division has sole and exclusive
jurisdiction over, among others:

| Matter | Heard in the Family Division? |
|---|---|
| Divorce, separate maintenance, annulment | **Yes** |
| Property division, spousal support incident to divorce | Yes — with the divorce |
| Child custody and parenting time | **Yes** |
| Child support and enforcement | **Yes** (Friend of the Court) |
| Paternity / parentage — Acknowledgment of Parentage Act + the Paternity Act | **Yes** |
| Juvenile delinquency and child abuse/neglect | **Yes** (formerly Probate) |
| Adoption | **Yes** |
| Name change | **Yes** |
| Emancipation of a minor | **Yes** |
| Personal protection orders (PPOs) | **Yes** — MCL 600.2950 / 600.2950a |
| Guardianship / conservatorship (ancillary) | Coordinated under the county family-court plan |

> Because jurisdiction is **exclusive and consolidated**, a family's
> related cases (e.g., a divorce, a PPO between the spouses, and an
> abuse/neglect petition involving the children) are generally assigned
> together under the county's family-court plan. Confirm the local
> assignment/one-judge practice with the venue skill.

## Venue and the one-court-of-justice structure

- File in the **Circuit Court for the county** of proper venue. For
  divorce, confirm the **residency requirement** (statewide residency
  plus county residency for a set period before filing) under the
  Title 552 dissolution statutes — see `mi-family-law`.
- If there are minor children, confirm Michigan is the child's home
  state under the **UCCJEA** and plead the jurisdictional allegations.
- Each Circuit Court has a **family-court plan** describing how family
  cases are assigned (often "one family, one judge"). The plan and the
  local administrative orders control intake routing — verify with
  `mi-wayne`, `mi-oakland`, `mi-circuit-courts`, or the relevant venue
  skill.

## The Friend of the Court (FOC) — central to support, custody, and parenting time

The **Friend of the Court Act, MCL 552.501 et seq.** (1982 PA 294)
creates an FOC office in **every county**, integral to Family Division
practice. Its statutory purposes include protecting the best interests
of children, helping parties resolve contested matters, and enforcing
custody, parenting-time, and support orders. Functions a filer meets:

- **Investigation and recommendation** on custody, parenting time, and
  support — the FOC may prepare a report the court considers.
- **Support computation / IV-D** — computes support under the **Michigan
  Child Support Formula** (`mi-family-law`), administers **income
  withholding**, works with the state IV-D program. Open an FOC case at
  filing.
- **Enforcement** — support arrears and parenting-time orders via
  show-cause/contempt referrals, license sanctions, and other tools.
- **Dispute resolution / mediation** the FOC offers or refers.

> Many counties require a **Domestic Relations Verified Statement** (or
> equivalent SCAO/FOC intake form) when support, custody, or parenting
> time is at issue, so the FOC can open its file.

## Personal protection orders (PPOs)

PPOs are filed in the **Family Division**. Two statutory tracks:

- **MCL 600.2950 — domestic-relationship PPO.** Available against a
  spouse, former spouse, person with whom the petitioner has a child in
  common, a current/former dating-relationship partner, or a
  current/former household resident. Restrains assault, threats,
  stalking, firearm possession, interference with children, workplace
  contact, and similar conduct, on a **reasonable cause** standard.
- **MCL 600.2950a — stalking / sexual-assault PPO.** For petitioners
  with **no** qualifying domestic relationship (the non-domestic track).

Mechanics to flag (verify the current figures):

- The court may issue an **ex parte** PPO without notice on a showing of
  irreparable injury; an ex parte PPO is effective on entry and is valid
  for at least **182 days** — confirm the current minimum.
- A respondent may **move to terminate or modify** an ex parte PPO
  within the time set by **MCR 3.707** — verify the current window.
- Violation is punishable as **criminal contempt** (for an adult, up to
  **93 days** in jail and a **$500** fine — confirm current penalties).
- The PPO court rules live at **MCR 3.701-3.709**. Use the SCAO **CC/PC
  PPO forms** (petition, order, and the law-enforcement information
  sheet). Route through `mi-draft-motion` / `mi-draft-order` and confirm
  the venue's PPO intake desk.

## The domestic-relations court rules — MCR 3.201-3.229

Subchapter **3.200 of the Michigan Court Rules** governs domestic-
relations actions, overlaying the general civil rules. Among the rules
a filer uses (confirm current text/titles in the corpus):

- **MCR 3.201** — applicability / scope.
- **MCR 3.205** — prior and subsequent orders affecting minors (notice
  to other courts/FOC offices with an existing order).
- **MCR 3.206** — content of the complaint and required allegations
  (incl. the verified statement / FOC information).
- **MCR 3.207** — ex parte, temporary, and protective orders.
- **MCR 3.210** — hearings and trials (incl. default-divorce proofs).
- **MCR 3.211** — judgments and orders (required divorce-judgment
  provisions, incl. support and the **Uniform Support Order**).
- **MCR 3.214-3.219** — FOC procedures, income withholding, support
  enforcement, and FOC-file access. **MCR 3.216** — mediation.
- **MCR 3.229** — verify the current end of the subchapter.

Treat these titles as pointers — verify each against `references/`
before relying on a number; the subchapter is periodically renumbered.

## SCAO mandatory forms

Michigan uses **State Court Administrative Office (SCAO) approved
forms**, many **mandatory** in domestic-relations and PPO practice:

- **FOC series** — support/custody/parenting-time forms (e.g., Uniform
  Child Support Order, parenting-time pleadings, Verified Statement).
- **DV / CC-PC series** — domestic-violence and PPO petition/order forms.
- **MC series** — general civil forms (summons, fee waiver, proof of
  service).

Use the current revision from the SCAO forms catalog; courts may reject
superseded versions. Confirm whether the county requires the SCAO form.

## Filing mechanics

1. **Confirm jurisdiction and venue** — Family Division of the county
   Circuit Court; divorce residency; UCCJEA home-state allegations for
   children (`mi-family-law`).
2. **Prepare the initiating documents** — the complaint/petition stating
   the statutory basis; the FOC **Verified Statement** where support or
   children are involved; for divorce with children, the information the
   court needs to enter custody, parenting-time, and a Uniform Support
   Order; PPO petition where protection is sought. Use
   `mi-statewide-format` for the **MCR 1.109** format/caption/signature
   and redaction of protected personal identifiers, and `mi-draft-motion`
   / `mi-draft-declaration` / `mi-draft-order` for the documents.
3. **File and pay (or waive) the fee** — with the Circuit Court Clerk;
   an **MC 20 fee-waiver** affidavit may waive fees for qualifying
   self-represented filers. Confirm the county's filing fee and whether
   **MiFILE** (Michigan's statewide e-filing system) is mandatory for the
   case type and venue (`mi-file-packet`, and the venue skill).
4. **Serve** the summons and complaint/petition under **MCR 2.105**
   within the summons period; the answer is generally due per the civil
   rules (`mi-first-30-days`). PPO service and the law-enforcement entry
   into LEIN follow the PPO rules.
5. **FOC intake** — the FOC opens its file; expect referral to FOC
   investigation, mediation, or a referee for support/parenting-time.
6. **Mediation / ADR** — see below.

## Mediation and ADR expectations

Michigan courts routinely refer contested custody and parenting-time
disputes to **domestic-relations mediation under MCR 3.216**, and the
**FOC** offers or refers parenting-time mediation. Many courts use
**referees** (FOC referees) to hear support and parenting-time matters
and issue recommended orders subject to a **de novo** judicial review on
timely objection — confirm the county's referee practice and the
objection window. Verify each venue's mediation order, screening for
domestic violence, and cost-sharing with the venue skill.

## Self-represented (pro se) family intake

- Michigan provides extensive **self-help resources** and SCAO
  **do-it-yourself** packets (e.g., divorce with/without children, PPO,
  custody/parenting-time motions) through the courts' self-help
  resources and Michigan Legal Help. Confirm the current packet and that
  the county accepts it.
- Designate the filer clearly as self-represented in the signature block
  (no Michigan bar number) — see `mi-pro-se`.
- Clerks and the FOC explain **procedure**, not legal advice. Encourage
  consultation with a licensed Michigan family-law attorney where there
  are minor children, retirement assets, real property, a business,
  safety concerns, or any disputed issue.

## Composition

- For substantive law (grounds, custody best-interest factors, the
  Michigan Child Support Formula, spousal support, parenting time,
  parentage under the Acknowledgment of Parentage Act and the Paternity
  Act, UCCJEA/UIFSA): `mi-family-law`
- For format (MCR 1.109 caption, signature, redaction):
  `mi-statewide-format`
- For the specific county / clerk / family-court plan and e-filing:
  `mi-wayne`, `mi-oakland`, `mi-circuit-courts`
- For pro se conventions and SCAO/self-help forms: `mi-pro-se`
- For the answer and first-response window: `mi-first-30-days`
- For deadlines and time computation: `mi-deadlines`
- For assembling and preflighting the filing packet (MiFILE):
  `mi-file-packet`
- For scheduling and hearings (including FOC referee hearings):
  `mi-schedule-hearing`, `mi-hearings`
- For the proposed judgment/order and Uniform Support Order:
  `mi-draft-order`, `mi-submit-order`

## References

- `references/family-division-jurisdiction.md` — MCL 600.1001 / 600.1021
  scope; the 1998 consolidation; the county family-court plan
- `references/friend-of-the-court.md` — MCL 552.501 et seq.; FOC
  investigation, support computation, income withholding, enforcement,
  referee practice and de novo review
- `references/ppo-procedure.md` — MCL 600.2950 / 600.2950a; MCR
  3.701-3.709; ex parte issuance, the 182-day term, termination/
  modification window, contempt penalties, SCAO PPO forms
- `references/mcr-3200-series.md` — the domestic-relations court rules
  (MCR 3.201-3.229) with current titles
- `references/scao-forms-and-intake.md` — FOC / DV / CC-PC / MC form
  series; the Verified Statement; self-help and do-it-yourself packets
