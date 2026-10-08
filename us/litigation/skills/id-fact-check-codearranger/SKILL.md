---
name: id-fact-check-codearranger
title: Fact-Check Idaho Court Filings
description: 'Use this skill to fact-check an Idaho court filing before it is filed. Triggers include "fact check Idaho filing", "verify Idaho Code citation", "is this Idaho case real", "check my Idaho brief", "Idaho citation format", "verify the rule cites in my Ada County motion", "I.R.C.P. vs I.R.E. cite", "audit this Idaho pleading", "check that my numbers are consistent across the packet". Runs four passes: (1) citation verification against authoritative Idaho sources (Idaho Code; I.R.C.P. / I.R.E. / I.A.R.; cases in Idaho form — Idaho Reports + P.2d/P.3d, with "(Ct. App. YEAR)" for Court of Appeals — via CourtListener); (2) internal consistency; (3) packet consistency; (4) sworn-versus-argued consistency.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Courtlistener Lookup
  path: references/courtlistener-lookup.md
- title: Idaho Citation Format
  path: references/idaho-citation-format.md
---

# Fact-Check Idaho Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently
> against current rules and case law before filing.

Use this skill before any Idaho court filing leaves the desk. It
runs four passes. It is the deeper evidentiary-citation pass;
`id-quality-check` is the lighter format-and-content pass. This
skill points at the canonical corpora rather than embedding statute
text or section numbers — pull current text from `id-law-references`.

## Pass 1 — Citation verification

For every rule, statute, and case citation, verify:

- **Rule cited**: exists in the correct Idaho rule set and says what
  the brief claims. Confirm the subdivision against current text via
  `id-law-references`. Idaho uses Rule-number plus
  lettered/numbered subparts (e.g., I.R.C.P. 56(a), I.R.C.P.
  7(b)(3)). The civil rules are **I.R.C.P.**, evidence is **I.R.E.**,
  and appellate rules are **I.A.R.**
- **Statute cited**: exists at the cited section. Idaho statutes are
  the **Idaho Code — Idaho Code § NN-NNN** (or **I.C. § NN-NNN**).
  Confirm against `id-law-references`; flag any section the brief
  invented or mis-numbered. Confirm limitations periods against
  current text rather than memory.
- **Federal statute cited**: exists at the cited subsection (e.g.,
  FDCPA at 15 U.S.C. § 1692 et seq.). Pull from the federal corpus.
- **Case cited**: exists; the reporter citation is correct; the
  proposition stands for what the brief claims; the case has not been
  overruled. Use **CourtListener** (Idaho Supreme Court = `idaho`,
  Court of Appeals = `idahoctapp`) and the connected CourtListener
  MCP to confirm the case is real and read the holding.

### Idaho citation format checks

Idaho cites to the **official Idaho Reports** together with the
**Pacific Reporter**. Idaho has **no neutral / public-domain
citation** — do not invent a vendor-neutral cite. Verify each
against current usage via `id-law-references`:

- Case form: `[Party A] v. [Party B], [###] Idaho [###], [###]
  P.[2d/3d] [###] ([YEAR])` — a **comma** separates the official
  Idaho Reports and the Pacific Reporter citations; keep the periods
  in `Idaho`, `P.2d`, `P.3d`, and `v.`
- Example: *Fitzgerald v. Walker*, 113 Idaho 730, 747 P.2d 752
  (1987).
- **Court of Appeals** opinions add a court parenthetical:
  `..., [###] Idaho [###], [###] P.3d [###] (Ct. App. [YEAR])`.
  Verify whether a cited opinion is a Supreme Court or Court of
  Appeals decision and that the parenthetical matches.
- Statutes: `Idaho Code § 9-1406` or `I.C. § 9-1406` (keep the `§`).
  Rules: `I.R.C.P. 56(a)`, `I.R.E. 803(6)`, `I.A.R. 14`.
- Flag a missing `§` on statutes, dropped periods in reporter
  abbreviations, a wrong parallel-cite separator, or a missing
  "(Ct. App. YEAR)" on a Court of Appeals case as a format WARN.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Party names**: each party named consistently throughout (and in
  `v.` form in any case caption); party **designations** match the
  forum (Plaintiff/Defendant vs. Petitioner/Respondent).
- **Case number**: appears identically wherever it recurs, and
  matches the court named in the caption (District Court / Magistrate
  Division).
- **Dates**: every date is consistent across all appearances (date of
  service, date of contract, date of last payment, date judgment was
  entered). A deadline that runs from a stated date must be supported
  by that date.
- **Dollar amounts**: every amount is consistent and the totals add
  up (principal + interest + fees + costs = total demanded).
- **Defined terms**: any term defined with `(the "Account")` is used
  consistently (no slipping into "the loan" or "the debt").
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to a real location.
- **Numbered paragraphs**: sequential without gaps or duplicates.

## Pass 3 — Packet consistency

Across the multi-document packet (motion + Memorandum + supporting
affidavit/declaration + Notice of Hearing + proposed order +
certificate of service):

- **Caption identical** in every document: court, county, party
  names, and case number must match exactly.
- **Document title** matches between the motion, its certificate of
  service, the Notice of Hearing, and the proposed order's title.
- **Dates align**: the certificate-of-service date should match the
  signature date on the motion; an affidavit's jurat date or a
  declaration's execution date should align with when it was made;
  the hearing date in the Notice of Hearing respects the **14-day**
  (or Rule 56 **28-day**) lead time.
- **Relief sought matches**: the motion's prayer must mirror the
  proposed order's decretal language item by item.
- **Exhibits** referenced in the motion are described in the
  affidavit/declaration and physically attached (exhibits are part of
  the pleading under I.R.C.P. 10).
- **Signature / Bar number**: each signed document carries the
  signer's signature and, for an attorney, the **Idaho State Bar
  number**; a self-represented filer signs without one.

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting affidavit/declaration
against what is argued in the motion or Memorandum:

- Every **factual assertion** in the argument should be (a) supported
  by a citation to a paragraph of the affidavit/declaration, (b)
  admitted in the pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the brief **not** supported by the
  affidavit/declaration — a gap to fix before filing.
- Identify any sworn fact **not used** in the brief — consider
  whether it belongs in the affidavit at all.
- Verify the affidavit/declaration's **personal-knowledge
  foundation** and, for a business-records affidavit, that it
  satisfies the custodian / qualified-witness requirement of **I.R.E.
  803(6)** and any self-authentication under **I.R.E. 902** (verify
  the exact 902 sub-paragraph numbering against current text). Flag
  paragraphs that begin "I believe" or "I understand" without a
  foundation.
- Confirm an **unsworn declaration** carries the **Idaho Code
  § 9-1406** "under penalty of perjury under the laws of the State of
  Idaho" subscription and a date, or the affidavit carries a
  completed jurat.

## Output format

When invoked on a packet, produce a structured verification report:

```
FACT-CHECK REPORT — [Document title / Case number]

Pass 1 (Citations)
  PASS  I.R.C.P. 56(a)                    — exists; correct subpart
  WARN  Idaho Code § 5-216                — confirm written-contract
        limitations period against current Idaho Code text
  FAIL  Smith v. Jones, 999 Idaho 1       — not found on CourtListener
        (idaho / idahoctapp); verify the case is real
  WARN  Fitzgerald v Walker, 113 Idaho    — Bluebook uses periods:
        730                                "Fitzgerald v. Walker"; add
                                           parallel P.2d cite

Pass 2 (Internal consistency)
  PASS  Party names + case number consistent
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, declaration, proposed order
  FAIL  Notice of Hearing date is only 9 days after service — short
        of the I.R.C.P. 7(b)(3) 14-day lead

Pass 4 (Sworn vs. argued)
  FAIL  Memo p.3 asserts "the collector held a license"; no
        corresponding declaration paragraph

Summary: 6 PASS / 3 WARN / 3 FAIL — DO NOT FILE until FAILs resolved.
```

## Composition

- For format checks: `id-statewide-format` + `scripts/format-check.py`
  on the generated document
- For deadline arithmetic checks (I.R.C.P. 2.2 time computation,
  +3-day mail add-on, Idaho holidays under I.C. § 73-108):
  `id-deadlines`
- For the lighter pre-filing format-and-content pass:
  `id-quality-check`
- For canonical statute / rule text: `id-law-references`
- For venue caption + local-rule confirmation: `id-ada`,
  `id-bonneville`, `id-county-courts`, `id-family-court`
- For pro se signature conventions (no bar number): `id-pro-se`

## References to author

- `references/idaho-citation-format.md` — Idaho Reports + P.2d/P.3d
  case form, the "(Ct. App. YEAR)" parenthetical, and I.C. / I.R.C.P.
  / I.R.E. / I.A.R. cite forms
- `references/courtlistener-lookup.md` — confirming Idaho cases via
  CourtListener (`idaho`, `idahoctapp`)
