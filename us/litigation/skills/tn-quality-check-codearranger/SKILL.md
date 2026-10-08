---
name: tn-quality-check-codearranger
title: Tennessee Pre-Filing Quality Check
description: 'This skill should be used to QC, review, or validate a Tennessee court document before filing. Triggers include "QC this Tennessee document", "review my Tennessee filing", "check this motion before I file it in Tennessee", "validate this Tennessee affidavit", "audit this Tennessee packet", "Tennessee pre-filing review", "run a quality check on my Tennessee filing", "check my Davidson Chancery motion", "is my General Sessions paperwork ready to file". Runs a two-pass check: (1) format pass — Tenn. R. Civ. P. 10.01 caption components, 10.02 numbered paragraphs, 10.03 exhibits, Rule 11 signature, Rule 5 certificate of service, redaction of personal identifiers; (2) content pass — pro-se drafting framework satisfaction (relief stated, rule cited, facts stated, conclusion offered), required-component completeness, packet consistency. Lighter touch than `tn-fact-check` (which goes deep on evidentiary citations and sworn-versus-argued alignment).'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness. It does not assess substantive legal
> sufficiency. Verify against current rules and the filing court's
> local rules before filing.

Use this skill as the **last step** before filing any Tennessee court
document. Two passes, plus a packet-consistency sweep.

## A note on Tennessee format authority

Tennessee has **no single statewide page-limit, margin, or font
rule.** Form is governed by:

- **Tenn. R. Civ. P. 10** — caption, numbered paragraphs, exhibits
- **Tenn. R. Civ. P. 11** — signature
- **Tenn. R. Civ. P. 5** — certificate of service
- Redaction of personal identifiers (verify the current electronic-
  filing / redaction rule of the filing court)

Page limits, margins, font, line spacing, and chambers-copy
requirements are set by **per-county local rules**. This skill checks
the Rule 10 / 11 / 5 components that are statewide and **flags
typography and page-limit items as WARN — local-rule matters to
confirm with the venue.**

## Pass 1 — Format

For a generated filing, run `scripts/format-check.py` first:

```
python3 plugins/tn-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the marketplace common-practice
defaults (US Letter, conventional margins, 12-point body, double or
1.5x spacing, footer with page numbering) and the **Tenn. R. Civ. P.
10.01 caption components**. Because Tennessee sets no statewide
typography rule, the script emits **WARN** (not FAIL) where a value
is a local-rule matter — resolve those by checking the venue's local
rules.

Resolve any **FAIL** from the format check before continuing.

### Format pass — non-`.docx` (markdown / text drafts)

Verify manually:

- **Caption (Tenn. R. Civ. P. 10.01)** — court and county
  (e.g., "IN THE CHANCERY COURT FOR DAVIDSON COUNTY, TENNESSEE"),
  party names, docket / file number, and the title designation per
  Rule 7.01
- **Title** — centered, identifying the document
- **Numbered paragraphs (Tenn. R. Civ. P. 10.02)** — sequential, each
  averment limited to a single set of circumstances
- **Exhibits (Tenn. R. Civ. P. 10.03)** — a copy of any written
  instrument that is an exhibit is attached
- **Signature block (Tenn. R. Civ. P. 11)** — name, address, phone,
  email, and **BPR # (Board of Professional Responsibility number)**
  if an attorney, or the **"Pro Se" / "Self-Represented"** designation
  if not
- **Certificate of Service (Tenn. R. Civ. P. 5)** — date, method, and
  each recipient
- **Line numbering + footer present** (WARN — confirm whether the
  local rules require line numbering; many Tennessee courts do not)
- **Redaction** of personal identifiers (SSNs, financial-account
  numbers, minors' full names) per the venue's redaction rule

## Pass 2 — Content

The content check applies the **pro-se drafting framework**.

### For a motion / memorandum:

- [ ] **Relief stated clearly** in the opening paragraph
- [ ] **Rule or statute citation** that grants the relief (e.g.,
      Tenn. R. Civ. P. 12.02(6); Tenn. R. Civ. P. 56; Tenn. Code Ann.
      § ___)
- [ ] **Numbered factual paragraphs** with record cites (affidavit ¶,
      complaint ¶, exhibit, admission)
- [ ] **Application of controlling authority** — case law applied to
      the facts, not merely strung together
- [ ] **Counter-arguments addressed**
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Proposed order attached / referenced**
- [ ] **Notice of Hearing** prepared and, for a Rule 56 motion, set
      **at least 30 days** after service (Tenn. R. Civ. P. 56.04)

### For an affidavit:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat** — sworn before a notary (Tennessee affidavits are
      sworn; an unsworn declaration is not a substitute unless the
      rule or statute permits one — verify)
- [ ] **Date and place** of execution
- [ ] For a **business-records** affidavit, the custodian /
      qualified-witness foundation under Tenn. R. Evid. 803(6)

### For a proposed order:

- [ ] **Caption identical** to the underlying motion
- [ ] **Findings (if any) separate from the ordering clause**
- [ ] **Ordering clause mirrors** the motion's prayer for relief
- [ ] **Specific dates / amounts** filled in or bracketed for the
      judge
- [ ] **Judge signature line** at the foot; in many courts an
      **"APPROVED AS TO FORM"** line for opposing counsel (see
      `tn-submit-order`)

### For an answer:

- [ ] **Each paragraph of the complaint addressed** (admit / deny /
      lack knowledge — no skipping)
- [ ] **Affirmative defenses pleaded** (statute of limitations,
      payment, lack of standing, etc.)
- [ ] **Compulsory counterclaims** pleaded
- [ ] **Timeliness** — answer due **30 days** after service of the
      summons and complaint (Tenn. R. Civ. P. 12.01)

## Pass 3 — Packet consistency

If filing a packet (motion + affidavit + proposed order + certificate
of service):

- [ ] **Same caption** across all documents — court (Circuit /
      Chancery / General Sessions), county, party names, docket number
- [ ] **Same document title** referenced in the motion's certificate
      of service and the proposed order
- [ ] **Dates align** — certificate-of-service date matches signature
      date on the motion; affidavit jurat date is consistent
- [ ] **Relief sought matches** between motion prayer and proposed
      order ordering clause (item by item)
- [ ] **All referenced exhibits** attached (Tenn. R. Civ. P. 10.03)

## Pre-flight checklist

| Check | Done |
|-------|------|
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| Caption shows correct court, county, party names, docket number | ☐ |
| Numbered paragraphs sequential (Rule 10.02) | ☐ |
| Exhibits attached (Rule 10.03) | ☐ |
| Signature block has BPR # (attorney) or "Pro Se" designation (Rule 11) | ☐ |
| Certificate of Service shows method, date, recipients (Rule 5) | ☐ |
| Personal identifiers redacted | ☐ |
| Proposed Order drafted as a separate document | ☐ |
| Notice of Hearing prepared; Rule 56 hearing set 30+ days out | ☐ |
| Local-rule page limit / typography confirmed for the venue | ☐ |
| `tn-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Tennessee pre-filing failures

1. **Assuming a statewide page limit.** There is none — page limits
   are local. Confirm the filing court's local rules before trusting
   a number.
2. **Rule 56 hearing set too soon.** Tenn. R. Civ. P. 56.04 requires
   the motion be served **at least 30 days before the hearing**; the
   adverse party responds no later than 5 days before. A short notice
   gets the hearing continued or the motion stricken.
3. **Missing BPR number or pro-se designation** in the Rule 11
   signature block.
4. **Wrong court for the amount.** General Sessions civil jurisdiction
   caps at **$25,000** (Tenn. Code Ann. § 16-15-501); forcible entry &
   detainer is unlimited. Filing an over-cap money claim in General
   Sessions is a venue error.
5. **Exhibit referenced but not attached** (Tenn. R. Civ. P. 10.03).
6. **Affidavit not actually sworn** — an unsigned or un-notarized
   "affidavit" carries no evidentiary weight.

## Composition

- For the deep evidentiary-citation and sworn-vs-argued review:
  `tn-fact-check`
- For format generation and the Rule 10 / 11 / 5 baseline:
  `tn-statewide-format`
- For drafting each component: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-order`, `tn-draft-note`
- For deadline arithmetic (Rule 6.01 / 6.05; Tenn. Code Ann.
  § 15-1-101 holidays): `tn-deadlines`
- For court-specific local-rule overlay: `tn-davidson`, `tn-shelby`,
  `tn-knox`, `tn-hamilton`, `tn-county-courts`,
  `tn-general-sessions`
- For the final filing step: `tn-file-packet`

## References

- `tn-statewide-format` for the Tenn. R. Civ. P. 10 / 11 / 5
  baseline and the local-rule typography caveat
- `tn-law-references` for canonical Tenn. R. Civ. P. and Tenn. R.
  Evid. text
- Always confirm current local rules of the filing court — this skill
  checks statewide components and flags local-rule items as WARN.
