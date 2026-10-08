---
name: az-fact-check-codearranger
title: Fact-Check Arizona Court Filings
description: 'Use this skill to fact-check an Arizona court filing before it is filed. Triggers include "fact check Arizona filing", "verify A.R.S. citation", "is this Arizona case real", "check my Arizona brief", "ARCP vs ARFLP", "Arizona citation format", "verify the rule cites in my Maricopa motion", "which rule set applies in Justice Court", "audit this Arizona pleading", and "check that my numbers are consistent across the packet". Runs four passes: (1) citation verification against authoritative Arizona sources (A.R.S. statutes; Ariz. R. Civ. P. / Ariz. R. Evid. / Arizona Rules of Family Law Procedure / Justice Court Rules of Civil Procedure; cases in Arizona/Bluebook form — Ariz. / Ariz. App. / P.2d / P.3d — via CourtListener); (2) internal consistency; (3) packet consistency; (4) sworn-versus-argued consistency.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Arizona Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently
> against current rules and case law before filing.

Use this skill before any Arizona court filing leaves the desk. It
runs four passes. It is the deeper evidentiary-citation pass;
`az-quality-check` is the lighter format-and-content pass. This skill
points at the canonical corpora rather than embedding statute text or
section numbers — pull current text from `az-law-references`.

## The Arizona forum trap — verify the right rule SET first

Arizona uses **different procedural rule sets depending on the
forum**, and a filing that cites the wrong set is defective even if
the quoted text is otherwise accurate. Before checking individual
cites, confirm the document's rule citations match its court:

- **Superior Court, general civil** → **Ariz. R. Civ. P.** (e.g.,
  Rule 8 pleading, Rule 12 motions, Rule 56 summary judgment).
- **Superior Court, family-law matters (Title 25 — dissolution,
  legal decision-making/parenting time, child support, paternity)**
  → **Arizona Rules of Family Law Procedure (ARFLP)**, NOT the civil
  rules. A family petition citing "Ariz. R. Civ. P. 12" instead of
  the ARFLP analog is a red flag.
- **Justice Court (civil up to the jurisdictional cap, small claims,
  most eviction/forcible-detainer)** → **Justice Court Rules of Civil
  Procedure (JCRCP)**, NOT the Superior Court civil rules.
- **Evidence** in all of the above → **Ariz. R. Evid.**

Flag any filing whose rule set does not match the venue named in its
caption. When unsure which forum a document targets, resolve that
before Pass 1.

## Pass 1 — Citation verification

For every rule, statute, and case citation, verify:

- **Rule cited**: exists in the **correct rule set for the forum**
  (see the trap above) and says what the brief claims. Confirm the
  subdivision against current text via `az-law-references` /
  azcourts.gov. Arizona uses Rule-number plus lettered/numbered
  subparts (e.g., Ariz. R. Civ. P. 56(a)).
- **Statute cited**: exists at the cited section. Arizona statutes
  are the **Arizona Revised Statutes — A.R.S. § NN-NNN**. Confirm
  against `az-law-references` / azleg.gov; flag any section the brief
  invented or mis-numbered. Confirm limitations periods (A.R.S.
  Title 12, ch. 5) against current text rather than memory.
- **Federal statute cited**: exists at the cited subsection (e.g.,
  FDCPA at 15 U.S.C. § 1692 et seq.). Pull from the federal corpus.
- **Case cited**: exists; the reporter citation is correct; the
  proposition stands for what the brief claims; the case has not been
  overruled. Use **CourtListener** (Arizona Supreme Court = `ariz`,
  Court of Appeals = `arizctapp`) and the connected CourtListener MCP
  to confirm the case is real and read the holding.

### Arizona citation format checks (Bluebook / Arizona conventions)

Arizona follows **Bluebook** form with Arizona reporter abbreviations.
Verify each against current usage via `az-law-references`:

- Case form: `[Party A] v. [Party B], [###] Ariz. [###], [###] P.[2d/3d]
  [###] ([YEAR])` — a **comma** separates the official Arizona and
  the regional Pacific Reporter citations; periods in `Ariz.`,
  `Ariz. App.`, and `v.`
- Example: *Orme School v. Reeves*, 166 Ariz. 301, 802 P.2d 1000
  (1990).
- Court of Appeals uses **`Ariz. App.`** (older) or `Ariz.` with a
  division parenthetical for newer opinions — confirm the current
  form rather than assuming.
- Statutes: `A.R.S. § 12-541` (keep the `§`; "A.R.S." not "ARS").
  Rules: `Ariz. R. Civ. P. 56`, `ARFLP 78`, `JCRCP 121`,
  `Ariz. R. Evid. 803(6)`.
- Flag missing `§` on statutes, dropped periods in reporter
  abbreviations, and a wrong parallel-cite separator as a format WARN.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Party names**: each party named consistently throughout (and in
  Bluebook `v.` form in any case caption).
- **Case number**: appears identically wherever it recurs, and
  matches the court named in the caption (Superior / Justice).
- **Dates**: every date is consistent across all appearances (date of
  service, date of contract, date of last payment, date judgment was
  entered). Deadlines that run from a stated date must be supported by
  that date.
- **Dollar amounts**: every amount is consistent and the totals add up
  (principal + interest + fees + costs = total demanded). Confirm the
  demand respects the venue's jurisdictional cap (Justice Court and
  small-claims limits differ from Superior Court).
- **Defined terms**: any term defined with `(the "Account")` is used
  consistently (no slipping into "the loan" or "the debt").
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to a real location.
- **Numbered paragraphs**: sequential without gaps or duplicates.

## Pass 3 — Packet consistency

Across the multi-document packet (motion + supporting affidavit/
declaration + proposed order + certificate/proof of service):

- **Caption identical** in every document: court, county, party
  names, and case number must match exactly.
- **Document title** matches between the motion, its certificate of
  service, and the proposed order's title.
- **Dates align**: the certificate-of-service date should match the
  signature date on the motion; an affidavit's jurat date should
  align with when it was sworn.
- **Relief sought matches**: the motion's prayer ("WHEREFORE, movant
  respectfully requests ____") must mirror the proposed order's
  ordering language item by item.
- **Exhibits** referenced in the motion are described in the
  affidavit/declaration and physically attached.
- **Signature / Bar number**: each signed document carries the
  signer's signature and, for an attorney, the **State Bar of Arizona
  bar number**; a self-represented filer signs without one.
- **Page limits / typography**: verify against the applicable rule set
  and the venue's local rules; flag any limit you cannot confirm.

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting affidavit/declaration
against what is argued in the motion or brief:

- Every **factual assertion** in the argument should be (a) supported
  by a citation to a paragraph of the affidavit/declaration, (b)
  admitted in the pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the brief **not** supported by the
  affidavit — a gap to fix before filing.
- Identify any sworn fact **not used** in the brief — consider whether
  it belongs in the affidavit at all.
- Verify the affidavit's **personal-knowledge foundation** and, for a
  business-records affidavit, that it satisfies the custodian /
  qualified-witness requirement of **Ariz. R. Evid. 803(6)** and any
  self-authentication under **Ariz. R. Evid. 902** (verify the exact
  902 sub-paragraph numbering against current text). Flag paragraphs
  that begin "I believe" or "I understand" without a foundation.

## Output format

When invoked on a packet, produce a structured verification report:

```
FACT-CHECK REPORT — [Document title / Case number]

Rule-set check
  PASS  Forum = Superior Court civil; cites Ariz. R. Civ. P. (correct)
  FAIL  Caption names Family Court (Title 25) but motion cites
        Ariz. R. Civ. P. 12 — should cite the ARFLP analog

Pass 1 (Citations)
  PASS  Ariz. R. Civ. P. 56(a)            — exists; correct subpart
  WARN  A.R.S. § 12-548                   — confirm written-contract
        limitations period against current A.R.S. text
  FAIL  Smith v. Jones, 999 Ariz. 1       — not found on CourtListener
        (ariz / arizctapp); verify the case is real
  WARN  Orme School v Reeves, 166 Ariz.   — Bluebook uses periods:
        301                                "Orme School v. Reeves"

Pass 2 (Internal consistency)
  PASS  Party names + case number consistent
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, declaration, proposed order
  FAIL  Certificate of service dated before the motion signature date

Pass 4 (Sworn vs. argued)
  FAIL  Brief p.3 asserts "the collector held a license"; no
        corresponding declaration paragraph

Summary: 6 PASS / 3 WARN / 3 FAIL — DO NOT FILE until FAILs resolved.
```

## Composition

- For format checks: `az-statewide-format` + `scripts/format-check.py`
  on the generated document
- For deadline arithmetic checks (time computation, service add-ons,
  Arizona holidays): `az-deadlines`
- For the lighter pre-filing format-and-content pass: `az-quality-check`
- For canonical statute / rule text: `az-law-references`
- For venue caption + local-rule confirmation:
  `az-maricopa` / `az-pima` / `az-superior-courts` / `az-justice-courts`
- For family-forum rule-set confirmation (ARFLP): `az-family-court`
- For pro se signature conventions (no bar number): `az-pro-se`

## References

- `az-law-references` for canonical A.R.S. text; Ariz. R. Civ. P.,
  Ariz. R. Evid., Arizona Rules of Family Law Procedure (ARFLP), and
  Justice Court Rules of Civil Procedure (JCRCP); and Arizona/Bluebook
  citation conventions
- **CourtListener** (`ariz` Supreme Court, `arizctapp` Court of
  Appeals) and the connected CourtListener MCP to confirm a case is
  real and read its holding
- Confirm all citations against current authoritative sources before
  filing; this skill flags suspect citations but does not warrant
  their accuracy. Verify current local rules of the filing court.
