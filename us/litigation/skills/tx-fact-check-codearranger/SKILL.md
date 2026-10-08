---
name: tx-fact-check-codearranger
title: Fact-Check Texas Court Filings
description: 'Use this skill to fact-check a Texas court filing before it is filed. Triggers include "fact check Texas filing", "verify Texas Code citation", "is this Texas case real", "check my Texas brief", "Texas citation format", "verify the rule cites in my Harris County motion", "TRCP vs Tex. R. Evid. cite", "check the court of appeals district on my cite", "pet. denied parenthetical Texas", "audit this Texas pleading", "check that my numbers are consistent across the packet". Runs four passes: (1) citation verification against authoritative Texas sources (the Texas codes; TRCP / Tex. R. Evid. / Tex. R. App. P.; cases in Texas form — South Western Reporter with the court-of-appeals district and petition-history parenthetical — via the case-law tools); (2) internal consistency; (3) packet consistency; (4) sworn-versus-argued consistency.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Texas Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently
> against current rules and case law before filing.

Use this skill before any Texas court filing leaves the desk. It runs
four passes. It is the deeper evidentiary-citation pass;
`tx-quality-check` is the lighter format-and-content pass. This skill
points at the canonical corpora rather than embedding statute text or
section numbers — pull current text from `tx-law-references`.

## Pass 1 — Citation verification

For every rule, statute, and case citation, verify:

- **Rule cited**: exists in the correct Texas rule set and says what
  the brief claims. Confirm the subdivision against current text via
  `tx-law-references`. Texas uses Rule-number plus lettered / numbered
  subparts (e.g., TRCP 166a(i), TRCP 197.2, TRCP 93(10)). The civil
  rules are the **Texas Rules of Civil Procedure (Tex. R. Civ. P. /
  TRCP)**; evidence is the **Texas Rules of Evidence (Tex. R. Evid.)**;
  appellate rules are the **Texas Rules of Appellate Procedure (Tex. R.
  App. P.)**.
- **Statute cited**: exists at the cited section, in the correct
  **code**. Texas statutes are organized into named codes — confirm the
  cite names the right one and the section exists:
  - **Tex. Civ. Prac. & Rem. Code** (e.g., § 16.004 limitations,
    § 31.002 turnover, § 132.001 unsworn declaration, § 34.001 dormancy)
  - **Tex. Fin. Code** (e.g., Ch. 392 Texas Debt Collection Act)
  - **Tex. Bus. & Com. Code** (e.g., Ch. 17 DTPA; the Texas UCC)
  - **Tex. Prop. Code** (e.g., Ch. 41 homestead, Ch. 42 personal
    property)
  - **Tex. Gov't Code** (e.g., § 662.003 holidays; court-organization
    chapters)
  - **Tex. Family Code** (e.g., Ch. 6 divorce, Ch. 153 conservatorship,
    Ch. 154 child support)
  Confirm against `tx-law-references`; flag any section the brief
  invented, mis-numbered, or placed in the wrong code. Confirm
  limitations periods against current text rather than memory.
- **Federal statute cited**: exists at the cited subsection (e.g.,
  FDCPA at 15 U.S.C. § 1692 et seq.). Pull from the federal corpus.
- **Case cited**: exists; the reporter citation is correct; the
  proposition stands for what the brief claims; the case has not been
  overruled or its petition history mis-stated. Use the connected
  **CourtListener** / case-law tools to confirm the case is real and
  read the holding (Supreme Court of Texas, the Courts of Appeals, and
  the Court of Criminal Appeals).

### Texas citation-format checks

Texas abolished its official Texas Reports; cite the **South Western
Reporter** in **Texas Rules of Form ("Greenbook")** style. Verify each
against current usage via `tx-law-references`:

- **Supreme Court of Texas**: `[Party A] v. [Party B], [###] S.W.[2d/3d]
  [###] (Tex. [YEAR])` — e.g., *In re Columbia Med. Ctr.*, 290 S.W.3d
  204 (Tex. 2009). Keep the periods in `S.W.2d`, `S.W.3d`, `Tex.`, and
  `v.`
- **★ Court of Appeals**: must include **both the district and the
  petition-history parenthetical** —
  `[Party A] v. [Party B], [###] S.W.3d [###] (Tex. App.—[District]
  [YEAR], [pet. history])` — e.g., *Doe v. Roe*, 123 S.W.3d 456 (Tex.
  App.—Dallas 2003, pet. denied). The **"pet. denied / pet. ref'd /
  pet. dism'd / no pet."** (or, for older cases, "writ ref'd / writ
  ref'd n.r.e. / no writ") subsequent-history parenthetical is a Texas
  signature. Flag a Court of Appeals cite **missing the district**
  (the em-dash "Tex. App.—Houston [14th Dist.]" form) or **missing the
  petition-history parenthetical** as a format WARN. Confirm the
  district matches the deciding court.
- **Court of Criminal Appeals**: `(Tex. Crim. App. [YEAR])` — verify a
  criminal cite is not mis-attributed to the Supreme Court of Texas
  (Texas has **two courts of last resort**).
- **Statutes**: `Tex. Civ. Prac. & Rem. Code § 16.004`; `Tex. Fam. Code
  § 154.125`; `Tex. Bus. & Com. Code § 17.50` (keep the `§`).
  **Rules**: `Tex. R. Civ. P. 166a`; `Tex. R. Evid. 803(6)`.
- Flag a missing `§` on statutes, dropped periods in reporter
  abbreviations, a wrong reporter series, a Court of Appeals cite with
  no district or no petition-history parenthetical, or a criminal cite
  attributed to the wrong high court as a format WARN.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Party names**: each party named consistently throughout (and in
  `v.` form in any case caption); party **designations** match the
  forum (**Plaintiff/Defendant** in general civil; **Petitioner/
  Respondent** in family law).
- **Cause number**: appears identically wherever it recurs, and matches
  the court named in the caption (District Court / County Court at Law /
  Justice Court, and the correct county).
- **Dates**: every date is consistent across all appearances (date of
  service, date of contract, date of last payment, date judgment was
  signed). A deadline that runs from a stated date must be supported by
  that date.
- **Dollar amounts**: every amount is consistent and the totals add up
  (principal + interest + fees + costs = total demanded), and the
  pleaded **TRCP 47(c) relief range** is consistent with the amount
  demanded.
- **Defined terms**: any term defined with `(the "Account")` is used
  consistently (no slipping into "the loan" or "the debt").
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to a real location.
- **Numbered paragraphs**: sequential without gaps or duplicates.

## Pass 3 — Packet consistency

Across the multi-document packet (motion + supporting affidavit /
unsworn declaration + Notice of Hearing or Submission + proposed order
+ certificate of service):

- **Caption identical** in every document: court, county, party names,
  and cause number must match exactly.
- **Document title** matches between the motion, its certificate of
  service, the Notice of Hearing / Submission, and the proposed order's
  title.
- **Dates align**: the certificate-of-service date should match the
  signature date on the motion; an affidavit's jurat date or an unsworn
  declaration's execution date should align with when it was made; the
  hearing / submission date respects the applicable lead time (the
  local notice clock, or the **TRCP 166a 21-day** summary-judgment lead
  with the response due 7 days before).
- **Relief sought matches**: the motion's prayer must mirror the
  proposed order's decretal language item by item.
- **Exhibits** referenced in the motion are described in the affidavit /
  declaration and physically attached.
- **Signature / bar number**: each signed document carries the signer's
  signature and, for an attorney, the **State Bar of Texas bar
  number**; a self-represented filer signs without one (TRCP 57).

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting affidavit / unsworn
declaration against what is argued in the motion or response:

- Every **factual assertion** in the argument should be (a) supported
  by a citation to a paragraph of the affidavit / declaration, (b)
  admitted in the pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the brief **not** supported by the
  affidavit / declaration — a gap to fix before filing.
- Identify any sworn fact **not used** in the brief — consider whether
  it belongs in the affidavit at all.
- Verify the affidavit / declaration's **personal-knowledge
  foundation** and, for a business-records affidavit, that it satisfies
  the custodian / qualified-witness requirement of **Tex. R. Evid.
  803(6)** and the self-authentication mechanics of **Tex. R. Evid.
  902(10)** (the affidavit form and pre-trial notice/filing — verify
  the exact 902(10) sub-paragraph numbering against current text). In a
  debt case, scrutinize whether the affiant shows knowledge of the
  **original creditor's** records. Flag paragraphs that begin "I
  believe" or "I understand" without a foundation.
- **Sworn-account / verified-denial check.** If the petition pleads a
  **sworn account (TRCP 185)**, confirm the verification is proper; if
  the answer contests it, confirm the **verified denial (TRCP 93(10) /
  185)** is present and sworn (or carries a CPRC § 132.001 declaration).
- Confirm an **unsworn declaration** carries the **Tex. Civ. Prac. &
  Rem. Code § 132.001** subscription "under penalty of perjury,"
  including the declarant's **date of birth and address** and a date, or
  the affidavit carries a completed jurat.

## Output format

When invoked on a packet, produce a structured verification report:

```
FACT-CHECK REPORT — [Document title / Cause number]

Pass 1 (Citations)
  PASS  Tex. R. Civ. P. 166a(i)            — exists; correct subpart
  WARN  Tex. Civ. Prac. & Rem. Code        — confirm 4-year debt
        § 16.004                             limitations period against
                                             current code text
  FAIL  Smith v. Jones, 999 S.W.3d 1        — not found; verify the case
                                             is real on CourtListener
  WARN  Doe v. Roe, 123 S.W.3d 456          — Court of Appeals cite is
        (Tex. App. 2003)                     missing the district and the
                                             petition-history parenthetical
                                             (e.g., "Tex. App.—Dallas
                                             2003, pet. denied")

Pass 2 (Internal consistency)
  PASS  Party names + cause number consistent
  WARN  Pleaded relief range (Rule 47(c)) does not match the amount
        demanded in the prayer

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, declaration, proposed order
  FAIL  Summary-judgment hearing is only 14 days after service — short
        of the TRCP 166a 21-day lead

Pass 4 (Sworn vs. argued)
  FAIL  Motion p.3 asserts "the affiant reviewed the original
        creditor's records"; declaration shows no such foundation
  WARN  Answer contests a TRCP 185 sworn account but the verified
        denial is not sworn (no jurat / no § 132.001 declaration)

Summary: 5 PASS / 4 WARN / 3 FAIL — DO NOT FILE until FAILs resolved.
```

## Composition

- For format checks: `tx-statewide-format` + `scripts/format-check.py`
  on the generated document
- For deadline arithmetic checks (TRCP 4 time computation, the TRCP 21a
  +3-day add-on, the TRCP 99 Monday rule, Tex. Gov't Code § 662.003
  holidays): `tx-deadlines`
- For the lighter pre-filing format-and-content pass: `tx-quality-check`
- For canonical statute / rule text: `tx-law-references`
- For venue caption + local-rule confirmation: `tx-hcdc`, `tx-dcdc`,
  `tx-county-courts`, `tx-family-court`
- For pro se signature conventions (no bar number): `tx-pro-se`
- For sworn-account / chain-of-title scrutiny in debt cases:
  `tx-consumer-debt`

## References to author

- `references/texas-citation-format.md` — South Western Reporter case
  form, the "Tex. App.—[District] [YEAR], [pet. history]"
  parenthetical, the two-high-courts distinction, and the Tex. [Code] /
  TRCP / Tex. R. Evid. / Tex. R. App. P. cite forms
- `references/courtlistener-lookup.md` — confirming Texas cases via the
  case-law tools (Supreme Court of Texas, Courts of Appeals, Court of
  Criminal Appeals)
