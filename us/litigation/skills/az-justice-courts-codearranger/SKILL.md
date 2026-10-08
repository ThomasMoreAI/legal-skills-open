---
name: az-justice-courts-codearranger
title: Arizona Justice Courts
description: 'Use when filing in or defending a case in an Arizona Justice Court — the limited-jurisdiction trial court and dominant consumer-debt and eviction forum. Triggers: "Arizona Justice Court", "Arizona small claims", "sued for a debt Arizona Justice Court", "Arizona eviction special detainer", "JCRCP", "Justice Court answer Arizona", "justice of the peace Arizona", "small claims division Arizona", "which Justice Court precinct", "appeal Justice Court to Superior Court Arizona". Covers the separate Justice Court Rules of Civil Procedure (JCRCP) — critical flag: do not use Superior Court rules. Covers civil jurisdiction, small-claims division (no appeal), special detainer / forcible detainer eviction procedures, answer deadlines, the high default-judgment volume in debt cases, and appeal to Superior Court. Layer on top of `az-statewide-format`.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-justice-courts
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Justice Courts

> **NOT LEGAL ADVICE.** Drafting and filing guidance only. Verify
> the controlling Justice Court precinct, its local procedures, the
> current jurisdictional and small-claims dollar caps, every day
> count, and the governing rule set against the official sources
> before filing.

Use this skill in addition to `az-statewide-format` when the case
is in an Arizona **Justice Court** (also called a justice of the
peace court / JP court). Justice Courts are the state's
limited-jurisdiction trial courts, organized into **precincts**
within each county, and they are where **most consumer-debt
collection suits and residential evictions are filed.** Above the
Justice Court sits the general-jurisdiction **Superior Court** (see
`az-superior-courts`).

## A separate rule set — JCRCP, not the Superior Court rules

This is the single most important thing to flag. Justice Court
civil cases are governed by the **Justice Court Rules of Civil
Procedure (JCRCP)** — a **distinct rule set** from the Arizona
Rules of Civil Procedure (Ariz. R. Civ. P.) that govern the
Superior Court. **Do not cite or apply the Superior Court rules to
a Justice Court filing.** Small claims matters are governed by
their own small-claims rules, and eviction actions follow the
**Rules of Procedure for Eviction Actions (RPEA)**. Confirm which
rule set controls before drafting captions, motions, deadlines, or
discovery, and verify the current text in the corpus.

The `az-statewide-format` caption, numbered-paragraph, Rule 11
signature-block (with the State Bar of Arizona bar number or a
"Self-Represented" designation), and certificate-of-service
conventions still apply to the *form* of the document, but the
*procedure* runs through the JCRCP.

## Civil money jurisdiction — up to $10,000

A Justice Court has civil jurisdiction where the amount in
controversy, exclusive of interest, costs, and statutorily
authorized attorney fees, does **not exceed the statutory cap under
A.R.S. § 22-201.** Claims above that ceiling belong in Superior
Court. The cap is set by statute and has been raised over time —
**confirm the current figure in the corpus before relying on it**
rather than stating a number that may be stale.

Justice Courts also handle:

- **Small claims** through the small claims division — see below.
- **Residential and commercial eviction** (special detainer and
  forcible detainer) — see below.
- Garnishments and other enforcement ancillary to Justice Court
  judgments (see `az-post-judgment`), plus civil traffic and
  certain criminal matters (criminal scope is outside this skill).

## Small claims division (A.R.S. § 22-503; no appeal under § 22-519)

Each Justice Court has a **small claims division** governed by
A.R.S. § 22-501 et seq. and the small-claims rules. Its
distinctive features:

- **Dollar ceiling lower than the general civil cap**, set by
  **A.R.S. § 22-503** — **point to the corpus for the current
  small-claims cap** rather than stating a figure that may be
  stale.
- **Informal procedure**: no jury, relaxed evidence, a streamlined
  hearing before a justice of the peace or a hearing officer.
- **No attorneys without consent**: a party may not be represented
  by an attorney in the small claims division unless **all parties
  agree** (and the court permits it).
- **NO APPEAL.** Under **A.R.S. § 22-519** there is **no appeal
  from a small claims judgment** — the decision of the hearing
  officer or justice of the peace is **final and binding on both
  parties.** Flag this prominently for any party weighing small
  claims: choosing (or being defaulted in) the small claims
  division forecloses appellate review.
- **Removal/transfer**: a small claims case may be transferred to
  the regular civil docket of the Justice Court (where the regular
  JCRCP and the right to counsel and to appeal apply) on a timely
  request — confirm the current mechanics and deadline in the
  corpus.

## Eviction — special detainer and forcible detainer

Residential evictions run through the Justice Court (or, by
jurisdiction, Superior Court) on a **highly accelerated timeline**
under the **Rules of Procedure for Eviction Actions (RPEA)**. Two
statutory tracks:

- **Special detainer (A.R.S. § 33-1377)** — the residential
  eviction remedy under the **Arizona Residential Landlord and
  Tenant Act (A.R.S. § 33-1301 et seq.)**. The summons commands the
  defendant to appear for trial within a **very short window after
  filing** (a matter of days, with an even faster track for
  material-and-irreparable breach), and the **return date is the
  trial date.** Confirm the exact day counts in the corpus — they
  are short and unforgiving.
- **Forcible entry and forcible detainer (A.R.S. § 12-1171 et
  seq.)** — the general possession remedy, including holdover after
  a written demand for possession.

For the substantive eviction and landlord-tenant law (notice
periods, the Arizona Residential Landlord and Tenant Act, the cure
notices, retaliation, security deposits, the writ of restitution
timeline), use **`az-landlord-tenant`** — these cases live almost
entirely in Justice Court.

## Commencing, serving, and answering a case

- **Commencement**: a civil action is started by filing a
  **complaint** (and summons) in the Justice Court for the
  **precinct** with venue. Identify the correct precinct before
  drafting the caption — do not assume.
- **Service**: under the JCRCP (and, for evictions, the RPEA);
  confirm the permitted methods and proof-of-service requirements
  in the corpus.
- **Answer deadline**: the time to file a written **answer** in a
  regular Justice Court civil case is set by the JCRCP and runs from
  service. **Confirm the current day count in the corpus**, and note
  that the **eviction timeline is far shorter** — in special and
  forcible detainer the defendant typically appears at the trial set
  on the return date rather than answering on the ordinary civil
  clock. For the first responsive pleading and defenses, see
  `az-first-30-days`.

## High default-judgment volume in debt cases

Justice Courts carry an enormous volume of **consumer-debt
collection suits**, and a large share resolve by **default
judgment** when the defendant does not answer or appear. If you are
the defendant, the priority is to calendar the answer deadline
immediately and respond on time; if a default has already entered,
see `az-post-judgment` for set-aside relief. For debt-defense
substance — chain of title, statute of limitations, licensing, and
proof problems — use **`az-consumer-debt`**.

## E-filing — AZTurboCourt

Many Arizona courts accept or require electronic filing through
**AZTurboCourt**, but availability and mandatory status **vary by
county and by Justice Court precinct.** Confirm the controlling
precinct's e-filing status and any paper-filing alternative before
assembling a packet — see `az-file-packet`.

## Appeal — Justice Court to Superior Court (regular civil only)

A party to a **final civil judgment of a Justice Court** (other
than a small claims judgment) may **appeal to the Superior Court**
under **A.R.S. § 22-261.** This is an appeal to the
general-jurisdiction trial court, not to the Court of Appeals.
Contrast the small claims division, where **§ 22-519 bars any
appeal.** Confirm the appeal deadline and the bond/transcript
mechanics in the corpus before relying on them.

## Composition

- For statewide format and the caption / signature / certificate
  mechanics: `az-statewide-format`
- For consumer-debt defense (these suits mostly live here):
  `az-consumer-debt`
- For eviction / special-detainer substance: `az-landlord-tenant`
- For general-jurisdiction matters over the Justice Court cap:
  `az-superior-courts`
- For the first responsive pleading and defenses: `az-first-30-days`
- For default set-aside, garnishment, and enforcement:
  `az-post-judgment`
- For scheduling, filing, and pro se conventions:
  `az-schedule-hearing`, `az-file-packet`, `az-pro-se`

## References

- `az-law-references` — the JCRCP, the small-claims rules, the
  Rules of Procedure for Eviction Actions (RPEA), A.R.S. Title 22
  (§ 22-201 jurisdiction; § 22-503 small claims; § 22-519 no
  small-claims appeal; § 22-261 appeal to Superior Court), the
  Arizona Residential Landlord and Tenant Act (A.R.S. § 33-1301 et
  seq., incl. § 33-1377 special detainer), and forcible-detainer
  statutes (A.R.S. § 12-1171 et seq.). **Confirm the current
  dollar caps and day counts here.**
- azcourts.gov — Justice Court precinct directory; confirm the
  controlling precinct, local procedures, and AZTurboCourt e-filing
  status.
