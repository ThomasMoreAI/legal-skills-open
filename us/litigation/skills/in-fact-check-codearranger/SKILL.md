---
name: in-fact-check-codearranger
title: Fact-Check Indiana Court Filings
description: 'This skill should be used when the user asks to "fact-check an Indiana filing", "verify Indiana citation", "Indiana citation check", "validate Indiana case cite", "Indiana Style Manual check", "check rule citation Indiana", "verify Indiana Code cite", "Indiana neutral-citation", "Indiana Supreme Court Rule on Citation", or any related verification request. Performs four passes: (1) citation verification (every rule, statute, and case cite checked against canonical sources); (2) internal consistency (party names, cause numbers, dates consistent throughout the document); (3) packet consistency (declarations align with arguments; exhibits referenced match exhibits attached); (4) sworn-vs.-argued consistency (verified facts in declarations match factual recitations in the motion). Trigger phrases: "Indiana fact-check", "verify Ind. Trial R. cite", "check IC citation", "Indiana cite verification", "audit Indiana brief".'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/in-court-docs/skills/in-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Indiana Court Filings

This skill is the **pre-filing audit** for any Indiana court
document. It runs four independent passes and reports defects.
It does NOT modify the document; it produces an audit report.
The audit is mandatory before any high-stakes filing (motion to
dismiss, summary judgment, T.R. 59 motion, appellate brief) and
recommended before any filing of more than 5 pages.

> **NOT LEGAL ADVICE.** Generated content is a drafting aid;
> verify every citation independently against the current
> Indiana Trial Rules, Indiana Code, and case law before filing.

## Pass 1 — Citation verification

Every rule, statute, and case citation in the document must be
verified against an authoritative source. Indiana citation
conventions:

### Rules
- **Format**: `Ind. Trial R. 56(C)` or `T.R. 56(C)`
- **Source**: `courts.in.gov/rules/trial_proc/`
- **Check**: rule number exists, subsection cited is current,
  rule has not been renumbered (Indiana renumbered T.R. 6 and
  T.R. 37 most recently — make sure the cited subsection
  matches current text)

### Evidence Rules
- **Format**: `Ind. Evid. R. 803(6)` or `IRE 803(6)`
- **Source**: `courts.in.gov/rules/evidence/`
- **Check**: rule number exists; the subsection's number has
  not changed in the 2014, 2019, or 2024 amendments

### Indiana Code
- **Format**: `IC 34-11-2-9` (no "§" required); `IC § 34-11-2-9`
  also accepted
- **Source**: `iga.in.gov/laws/` (Indiana General Assembly)
- **Check**: section exists; the section number has not been
  renumbered (IC 24-16 → IC 24-4.5 was a major renumbering in
  1971; IC 34-1-2 was renumbered to IC 34-11 in 1998; IC 34-2-29
  → IC 34-26-5 in 1998)

### Cases
- **Indiana Supreme Court format**: `Smith v. Jones, 123 N.E.3d
  456 (Ind. 2023)` — must include reporter, page, court,
  parenthetical year
- **Indiana Court of Appeals format**: `Smith v. Jones, 123
  N.E.3d 456 (Ind. Ct. App. 2023)`
- **Source**: `courts.in.gov/opinions/` or
  `https://www.in.gov/courts/appellate/` or Westlaw/Lexis
- **Check**: case exists at the cited reporter; the citation is
  pinpoint-accurate; the quoted language matches the source;
  the case has not been overruled (a "negative-treatment" check
  is essential for any case more than 5 years old)

### Federal cases and statutes
- **Federal case**: `Iqbal, 556 U.S. 662 (2009)` or
  `Ashcroft v. Iqbal, 556 U.S. 662 (2009)`
- **Federal statute**: `15 U.S.C. § 1692k(a)(1)` (periods in
  "U.S.C."; § with space before number)
- **Federal regulation**: `12 C.F.R. § 1006.30`
- **Source**: `uscode.house.gov`; `ecfr.gov`

## Pass 2 — Internal consistency

Check that the document itself is internally consistent:

| Check | How to verify |
|-------|---------------|
| Caption matches body | Court name, county, cause number, parties match the body's first paragraph |
| Cause number format | Matches `[CC]C01-YYMM-[CT]-NNNNNN` or `[CC]D01-YYMM-[CT]-NNNNNN`, where county code matches the named county |
| Party names consistent | "Plaintiff" and "Defendant" used the same way throughout; no name spelling drift |
| Dates consistent | Date of filing, date of service, dates referenced in facts all align |
| Pagination | Page numbers match footer count |
| Signature date | Date matches the verification date in any attached declaration |
| Defined terms | Terms defined once (e.g., "the Account") used consistently |
| Cross-references | Internal cross-references (e.g., "as set forth in Paragraph 14") point to the correct paragraph |

## Pass 3 — Packet consistency

When the filing is a packet (e.g., motion + memorandum +
declaration + proposed order), verify:

| Check | How |
|-------|-----|
| Caption identical across all packet documents | Same court, county, parties, cause number on every page-1 caption |
| Exhibit list matches attached exhibits | Memorandum references "Exhibit A" and Exhibit A is attached to the declaration; the count and labels match |
| Declaration supports the argument | Every factual assertion in the memo that requires a sworn predicate has a corresponding paragraph in the declaration |
| Proposed Order matches relief requested | The relief sought in the motion is exactly what the proposed order grants |
| Service list complete | Certificate of Service lists every party of record per Odyssey Service Contacts |

## Pass 4 — Sworn-vs.-argued consistency

Indiana courts hold counsel and pro se filers to strict
candor under T.R. 11(B) and the Indiana Rules of Professional
Conduct (Rule 3.3 — candor to the tribunal). Every factual
representation in a memorandum should either:

- Be supported by a sworn declaration paragraph or exhibit
- Be presented as a legal argument (clearly marked)
- Be a procedural fact (e.g., "On March 15, 2024, Defendant was
  served with the Complaint") — these are usually verifiable from
  the docket

The audit checks:

- Every "Defendant has paid" / "Plaintiff failed to" / "On [date],
  X happened" assertion in the memo has a corresponding
  paragraph in the supporting declaration
- The declaration paragraph is signed under penalties for
  perjury (T.R. 11(B) / IC 35-44.1-2-1)
- No factual assertion appears in the memo that is contradicted
  by a sworn paragraph elsewhere in the packet
- No statement of fact appears in the memo that is contradicted
  by an attached exhibit (e.g., memo says "the contract was
  signed in 2020"; Exhibit A shows a 2018 signature)

## Common Indiana-specific citation errors

| Error | Why it matters | Fix |
|-------|----------------|-----|
| Citing "IC 34-1-2-9" (old) | Indiana renumbered Title 34 in 1998 | Use IC 34-11-2-9 |
| Citing "IC 24-16-..." (old IUCCC) | Renumbered to IC 24-4.5 in 1971 | Use IC 24-4.5-... |
| Using "v." inconsistently | Indiana style is "v." (no "vs.") | Use "v." throughout |
| Missing "(Ind." in case cite | Some practitioners drop "(Ind. 2023)" — non-standard | Include "(Ind. YYYY)" |
| Citing "Ind. R. Evid." | Outdated abbreviation | Use "Ind. Evid. R." or "IRE" |
| "Trial Rule" without "Ind." prefix in interstate context | Ambiguous in federal court | Use "Ind. Trial R." |
| Local rule prefix wrong | LR49 (Marion) vs LR45 (Lake) vs LR29 (Hamilton) | Match the venue county code |
| Cause-number county digit wrong | First two digits must match venue county | Cross-check with county code map |

## Audit workflow

```
1. Run the document through the format-check.py script first
   (T.R. 5(E) compliance)
2. Pass 1: extract every citation, verify against canonical
   source
3. Pass 2: party-name, cause-number, date cross-check
4. Pass 3: open every packet document side-by-side; verify
   captions and exhibit references match
5. Pass 4: line-by-line comparison of memo factual statements
   vs. declaration paragraphs
6. Produce audit report with severity-flagged defects:
   - BLOCKING: citation error, mismatched cause number, missing
     declaration support for a sworn fact
   - WARNING: stylistic inconsistency, missing pinpoint cite
   - INFO: opportunity for stronger citation or sharper drafting
```

## Composition

- `in-statewide-format` for T.R. 5(E) / T.R. 10 baseline
- `in-law-references` as the canonical citation source
- `in-marion` / `in-lake` / `in-county-courts` for local-rule
  prefix verification
- `in-quality-check` for the full pre-filing QC (runs fact-check
  as one of its sub-passes)

## References

- `references/citation-checklist.md` — per-citation-type
  checklist
- `references/common-errors.md` — Indiana-specific citation
  errors with examples
- `references/negative-treatment.md` — how to check for
  overruling / superseding
- `references/sworn-vs-argued-audit.md` — sample audit report
  format

**NOT LEGAL ADVICE.** Generated content is a drafting aid; verify
against current rules and case law before filing.
