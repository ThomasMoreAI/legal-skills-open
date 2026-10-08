---
name: mi-fact-check-codearranger
title: Fact-Check Michigan Court Filings
description: 'This skill should be used to fact-check a Michigan court filing before it is filed. Triggers include "fact check Michigan filing", "verify MCL citation", "is this Michigan case real", "check my Michigan brief", "MCR citation format", "verify the MCR citations in this motion", "check Mich Comp Laws citations", "audit this Michigan pleading", "review my pro se filing before I file it in Michigan", "check that my numbers are consistent across the packet", and "verify the case cites in my Wayne Circuit brief". Runs four passes: (1) citation verification against authoritative Michigan sources (MCL statutes, MCR / MRE rules, cases in Michigan Appellate Opinion Manual form — Mich, Mich App, NW2d — via CourtListener); (2) internal consistency within a single document (party names, case number, dates, dollar amounts); (3) packet consistency across motion + affidavit + proposed order + proof of service; (4) sworn-versus- argued consistency between affidavit facts and brief assertions.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/mi-court-docs/skills/mi-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Michigan Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently
> against current rules and case law before filing.

Use this skill before any Michigan court filing leaves the desk. It
runs four passes. It is the deeper evidentiary-citation pass;
`mi-quality-check` is the lighter format-and-content pass. This skill
points at the canonical corpora rather than embedding statute text or
section numbers — pull current text from `mi-law-references`.

## Pass 1 — Citation verification

For every rule, statute, and case citation in the document, verify:

- **Rule cited**: exists and says what the brief claims. Use the
  current **Michigan Court Rules (MCR)** or **Michigan Rules of
  Evidence (MRE)** text. Confirm the subsection — e.g., summary
  disposition grounds live in **MCR 2.116(C)(8)** (failure to state a
  claim, pleadings alone) and **MCR 2.116(C)(10)** (no genuine issue
  of material fact, evidentiary record). Michigan uses chapter-dot
  numbering with parenthetical subdivisions.
- **Statute cited**: exists at the cited subsection. Michigan statutes
  are the **Michigan Compiled Laws — MCL NNN.NNNN** (also written
  **Mich Comp Laws**). Confirm against `mi-law-references` /
  legislature.mi.gov; flag any section the brief invented or
  mis-numbered. Confirm limitations periods (MCL 600.5801 et seq.) and
  any governmental-immunity notice statute (GTLA, MCL 691.1407 et seq.)
  against current text rather than memory.
- **Federal statute cited**: exists at the cited subsection (e.g.,
  FDCPA at 15 USC 1692 et seq.). Pull from the federal corpus.
- **Case cited**: exists; the reporter citation is correct; the
  proposition stands for what the brief claims; the case has not been
  overruled. Use **CourtListener** (Michigan Supreme Court = `mich`,
  Court of Appeals = `michctapp`) and the connected CourtListener MCP
  to confirm the case is real and read the holding.

### Michigan citation format checks (Michigan Appellate Opinion Manual)

Michigan's official style is the **Michigan Appellate Opinion Manual
(MAOM)**, not the Bluebook. Its conventions are distinctive — verify
each against the current MAOM via `mi-law-references`:

- **No periods** in the reporter abbreviations: `Mich`, `Mich App`,
  `NW2d` (not "Mich.", "Mich. App.", "N.W.2d"); **`v` with no period**.
- Citation form: `[Party A] v [Party B], [###] Mich [###]; [###] NW2d
  [###] ([YEAR])` — a **semicolon** separates the official and
  regional citations. Court of Appeals uses `Mich App`.
- Example: *Maiden v Rozwood*, 461 Mich 109; 597 NW2d 817 (1999).
- Statutes: `MCL 600.5807` (MAOM omits the `§` symbol and "section").
  Rules: `MCR 2.116(C)(10)` / `MRE 803(6)` (no `§`, no periods).
- Flag Bluebook-style periods (`Mich.`, `N.W.2d`, `v.`) and any
  missing semicolon between parallel cites as a format WARN.

### Unpublished-opinion caution (MCR 7.215(C))

**MCR 7.215(C)(1)** provides that an unpublished Court of Appeals
opinion is **not precedentially binding** under stare decisis; it may
be cited but must be flagged as unpublished, with a copy accompanying
the filing. Verify the rule's current contours, then:

- Flag any unpublished opinion the brief relies on **as if it were
  binding** — soften to persuasive, and confirm a copy is attached.
- Confirm any case marked "(unpublished)" actually is, and any cited
  as published actually appears in `Mich App`.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Party names**: each party named consistently throughout (and in
  the MAOM `v`-no-period form in any case caption).
- **Case number**: the case number appears identically wherever it
  recurs, and matches the court (Circuit / District / Probate).
- **Dates**: every date is consistent across all appearances (date of
  service, date of contract, date of last payment, date judgment was
  entered). Deadlines that run from a stated date must be supported by
  that date.
- **Dollar amounts**: every amount is consistent and the totals add up
  (principal + interest + fees + costs = total demanded). Confirm the
  demand respects the venue's jurisdictional cap (small claims and
  District Court limits differ from Circuit Court).
- **Defined terms**: any term defined with `(the "Account")` is used
  consistently (no slipping into "the loan" or "the debt").
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to a real location.
- **Numbered paragraphs**: sequential without gaps or duplicates, as
  MCR 2.113 contemplates separately numbered averments.

## Pass 3 — Packet consistency

Across the multi-document packet (motion + supporting affidavit +
proposed order + proof of service):

- **Caption identical** in every document: court, county, party names,
  and case number must match exactly (MCR 1.109 / MCR 2.113).
- **Document title** matches between the motion and its proof of
  service and the proposed order's title.
- **Dates align**: the proof-of-service date should match the
  signature date on the motion; the affidavit's jurat date should
  align with when it was sworn.
- **Relief sought matches**: the motion's prayer ("WHEREFORE, movant
  respectfully requests ____") must mirror the proposed order's
  ordering language ("IT IS ORDERED ____"), item by item.
- **Exhibits** referenced in the motion are described in the affidavit
  and physically attached.
- **Signature / P-number**: each signed document carries the signer's
  signature and, for an attorney, the State Bar **P-number**
  (MCR 1.109(E)); a self-represented filer signs without one.
- **Page limits / typography**: verify against MCR 1.109 and the
  venue's local rules; flag any limit you cannot confirm.

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting affidavit against what is
argued in the motion or brief:

- Every **factual assertion** in the argument should be (a) supported
  by a citation to a paragraph of the affidavit, (b) admitted in the
  pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the brief **not** supported by the
  affidavit — a gap to fix before filing.
- Identify any sworn fact **not used** in the brief — consider whether
  it belongs in the affidavit at all.
- Verify the affidavit's **personal-knowledge foundation** and, for a
  business-records affidavit, that it satisfies the custodian /
  qualified-witness requirement of **MRE 803(6)** and any
  self-authentication under **MRE 902** (verify the exact 902
  sub-paragraph numbering against current MRE text). Flag paragraphs
  that begin "I believe" or "I understand" without a foundation.

## Output format

When invoked on a packet, produce a structured verification report:

```
FACT-CHECK REPORT — [Document title / Case number]

Pass 1 (Citations)
  PASS  MCR 2.116(C)(10)               — exists; correct subrule
  WARN  MCL 600.5807                   — confirm contract limitations
        period + accrual against current MCL text
  FAIL  Smith v Jones, 999 Mich 1      — not found on CourtListener
        (mich / michctapp); verify the case is real
  WARN  Maiden v. Rozwood, 461 Mich.   — MAOM uses no periods:
        109                              "Maiden v Rozwood, 461 Mich 109"

Pass 2 (Internal consistency)
  PASS  Party names + case number consistent
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, affidavit, proposed order
  FAIL  Proof of service dated before the motion signature date

Pass 4 (Sworn vs. argued)
  FAIL  Brief p.3 asserts "the collector held a license"; no
        corresponding affidavit paragraph

Summary: 6 PASS / 3 WARN / 3 FAIL — DO NOT FILE until FAILs resolved.
```

## Composition

- For format checks: `mi-statewide-format` + `scripts/format-check.py`
  on the generated document
- For deadline arithmetic checks (MCR 1.108 computation, MCR 2.107(C)
  service add-ons, Michigan holidays): `mi-deadlines`
- For the lighter pre-filing format-and-content pass:
  `mi-quality-check`
- For canonical statute / rule text: `mi-law-references`
- For venue caption + local-rule confirmation:
  `mi-wayne` / `mi-oakland` / `mi-circuit-courts` / `mi-district-courts`
- For pro se signature conventions (no P-number): `mi-pro-se`

## References

- `mi-law-references` for canonical MCL, MCR, and MRE text plus the
  Michigan Appellate Opinion Manual citation conventions
- **CourtListener** (`mich` Supreme Court, `michctapp` Court of
  Appeals) and the connected CourtListener MCP to confirm a case is
  real and read its holding
- Confirm all citations against current authoritative sources before
  filing; this skill flags suspect citations but does not warrant
  their accuracy. Verify current local rules of the filing court.
