---
name: co-fact-check-codearranger
title: Fact-Check Colorado Court Filings
description: 'This skill should be used to fact-check a Colorado court filing before it is filed. Triggers include "fact-check this Colorado filing", "verify citations in my motion", "check the rule citations in this brief", "check Colorado statute citations", "audit this Colorado pleading", "review my pro se filing before I file it", "check that my numbers are consistent across the packet". Runs four passes: (1) citation verification against canonical sources; (2) internal consistency within a single document (dates, dollar amounts, defined terms); (3) packet consistency across motion + declaration + proposed order + certificate of service; (4) sworn- versus-argued consistency between declaration assertions and motion arguments.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/co-court-docs/skills/co-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Colorado Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects errors but does not
> assess legal sufficiency. Verify substantive law independently.

Use this skill before any Colorado court filing leaves the desk. It
runs four passes:

## Pass 1 — Citation verification

For every rule, statute, regulation, and case citation in the
document, verify:

- **Rule cited**: exists and says what the brief claims. Use the
  current C.R.C.P. (Colorado Judicial Branch), CRE, or C.A.R. text.
- **Statute cited**: exists at the cited subsection. Pull from
  https://leg.colorado.gov/colorado-revised-statutes.
- **Federal statute cited**: exists at the cited subsection. Pull
  from https://uscode.house.gov.
- **Regulation cited**: exists at the cited C.F.R. section. Pull
  from https://ecfr.gov.
- **Case cited**: exists; the parallel citation is correct; the
  proposition stands for what the brief claims; the case has not
  been overruled or distinguished by more recent authority.

### Colorado citation format checks

Per `co-statewide-format` and `co-law-references`:

- Colorado Supreme Court (post-2012): `[Party A] v. [Party B], [YEAR] CO [###], ¶ [#], [###] P.3d [###]`
- Colorado Court of Appeals (post-2012): `[Party A] v. [Party B], [YEAR] COA [###], ¶ [#], [###] P.3d [###]`
- Colorado pre-2012: `[Party A] v. [Party B], [###] P.[#d] [###] (Colo. [YEAR])` or `(Colo. App. [YEAR])`
- Colorado statutes: `C.R.S. § XX-XX-XXX` (always with `§`)
- C.R.C.P.: `C.R.C.P. XX(x)(x)` (no `§` for rules)
- CRE: `C.R.E. XXX` (use periods)
- Federal statutes: `XX U.S.C. § XXXX`
- C.F.R.: `XX C.F.R. § XXXX.XX`

Common errors:

- Missing `§` on a Colorado statute citation
- Using a `§` on a C.R.C.P. citation (no `§` for rules)
- Citing pre-2012 Colorado cases with neutral-citation format (only
  post-2012 cases have `[YEAR] CO [###]`)
- Citing to P.3d page when the case has both neutral and parallel —
  use both, paragraph-anchored
- Missing the `(Colo. App. YEAR)` jurisdiction tag on pre-2012 COA
  cases

## Pass 2 — Internal consistency

Within a single document, verify:

- **Dates**: every date stated in the document is consistent with
  every other appearance of that date (date of service, date of
  contract, date of last payment, date of the loan, etc.)
- **Dollar amounts**: every dollar amount is consistent and totals
  add up (principal + interest + fees + costs = total demanded)
- **Defined terms**: any term defined with `(the "Account")` etc. is
  used consistently throughout (no slipping into "the loan" or "the
  debt" once defined as "the Account")
- **Party names**: each party named consistently (no switching
  between "Plaintiff", "Plaintiff Smith", and "Smith")
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  actually exists at the cited location
- **Numbered paragraphs**: sequential without gaps or duplicates

## Pass 3 — Packet consistency

Across the multi-document filing packet (motion + declaration +
proposed order + certificate of service):

- **Caption identical** in every document: court name, case number,
  party names, division, courtroom must match exactly
- **Document title** matches in the motion's certificate of service
  and the proposed order's title bar
- **Dates** align: the certificate of service date should match the
  signature date on the motion; the declaration's "executed on"
  date should align with when the declaration was signed
- **Relief sought** matches: the motion's prayer ("WHEREFORE, the
  Court is respectfully requested to ____") must mirror the
  proposed order's ordering language ("IT IS HEREBY ORDERED that
  ____")
- **Exhibits** referenced in the motion are described in the
  declaration's exhibit list and physically attached
- **Conferral status** in the certificate of conferral is consistent
  with any narrative description of conferral attempts in the motion
  body
- **Page counts** comply with C.R.C.P. 121 § 1-15 limits (15 pages
  motion/response; 10 pages reply) — flag anything over the limit
  before filing

## Pass 4 — Sworn vs. argued

Compare what is sworn-to in the supporting declaration / affidavit
against what is argued in the motion or brief:

- Every **factual assertion** in the motion's argument section
  should be either (a) supported by a citation to a paragraph of the
  declaration, (b) admitted in the pleadings, or (c) a matter of
  judicial notice
- Identify any factual claim in the motion that is **not** supported
  by the declaration — that's a gap to fix before filing
- Identify any factual claim in the declaration that is **not used**
  in the motion — consider whether it belongs in the declaration at
  all
- Verify the declaration's **personal-knowledge foundation** —
  declarations under C.R.S. § 13-27-104 must be based on personal
  knowledge; flag any paragraph that begins "I believe" or "I
  understand" without a foundational basis

## Output format

When invoked on a packet, produce a structured report:

```
FACT-CHECK REPORT — [Document title / Case number]

Pass 1 (Citations)
  PASS  C.R.C.P. 12(b)(5)            — exists; correct subsection
  WARN  C.R.S. § 13-80-103.5         — verify (1)(a) vs (1)(j)
  FAIL  Smith v. Jones, 2019 COA 45  — no such case found at this
        cite; check year (perhaps 2017 COA 45?)

Pass 2 (Internal consistency)
  PASS  Defined terms used consistently
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, declaration, proposed order
  FAIL  Motion seeks $4,500 in fees; Proposed Order awards $4,000

Pass 4 (Sworn vs. argued)
  FAIL  Motion ¶ 3 asserts "Plaintiff sent a 30-day notice"; no
        corresponding declaration paragraph

Summary: 8 PASS / 3 WARN / 3 FAIL — DO NOT FILE until 3 FAILs
resolved.
```

## Composition

- For statewide format checks: `co-statewide-format` +
  `scripts/format-check.py` on the generated `.docx`
- For deadline arithmetic checks: `co-deadlines`
- For pre-filing QC: `co-quality-check` (this skill is the deeper
  evidentiary-citation pass; `co-quality-check` is the lighter
  format-and-content pass)

## References

- `references/citation-checklist.md` — Colorado citation conventions
  with common errors
- `references/cross-document-checks.md` — packet-consistency
  checklist
- `references/sworn-vs-argued.md` — declaration-to-motion mapping
  technique
