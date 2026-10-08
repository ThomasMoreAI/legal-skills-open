---
name: az-quality-check-codearranger
title: Arizona Pre-Filing Quality Check
description: 'Use to QC, review, or validate an Arizona court document before filing. Triggers: "quality check Arizona filing", "is my Arizona motion ready to file", "Ariz. R. Civ. P. 10 compliance", "pre-filing review Arizona", "QC this Arizona document", "check this motion before I file it in Arizona", "validate this Arizona affidavit", "audit this Arizona packet", "is my Maricopa Superior Court motion ready". Runs two passes: (1) format pass — Ariz. R. Civ. P. 10 caption, Rule 7.1 motion form, Rule 11 signature with State Bar bar number, line numbering + footer + "Page X of Y", Rule 5 certificate of service; (2) content pass — affirmative defenses pleaded, correct rule set for forum (ARCP vs. ARFLP vs. JCRCP critical flag), required attachments including proposed form of order. Lighter touch than `az-fact-check`, which deep-dives evidentiary citations and sworn-vs-argued alignment.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/az-court-docs/skills/az-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Arizona Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness. It does not assess substantive legal
> sufficiency. Verify against the current Arizona Rules of Civil
> Procedure and the local rules and administrative orders of the
> filing court before filing.

Use this skill as the **last step** before filing any Arizona court
document. Two passes, plus a packet-consistency sweep.

## A note on the rule set for the forum

Arizona has **three distinct trial-court rule sets**, and a filing
must conform to the one that governs its forum. Confirm the correct
set before the format pass:

- **Ariz. R. Civ. P. (ARCP)** — Superior Court civil actions
- **Ariz. R. Fam. Law P. (ARFLP)** — Superior Court family-law
  matters (dissolution, legal decision-making, parenting time,
  support); captions and pleading forms differ from ARCP
- **Justice Court Rules of Civil Procedure (JCRCP)** — Justice Court
  civil actions (including the small-claims division)

This skill checks the ARCP baseline by default; **flag a forum
mismatch as FAIL** and route family-law and Justice Court filings to
the matching rule set (`az-family-court`, `az-justice-courts`).

## Pass 1 — Format

For a generated filing, run `scripts/format-check.py` first:

```
python3 plugins/az-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the marketplace common-practice
defaults (US Letter, conventional margins, body font, double or 1.5x
spacing, footer with **document title + "Page X of Y"** pagination)
against the Ariz. R. Civ. P. 10 / Rule 7.1 baseline. Where a value is
a local-rule or administrative-order matter, the script emits
**WARN** (not FAIL) — resolve those by checking the venue's local
rules. Resolve any **FAIL** before continuing.

### Format pass — non-`.docx` (markdown / text drafts)

Verify manually:

- **Caption (Rule 10(a))** — court and county (e.g., "IN THE SUPERIOR
  COURT OF THE STATE OF ARIZONA / IN AND FOR THE COUNTY OF MARICOPA"),
  party names with designations, **case number** and assigned
  division/judge, and the document title
- **Title** — identifying the document (e.g., "MOTION FOR SUMMARY
  JUDGMENT")
- **Numbered paragraphs (Rule 10(b))** — sequential, each averment
  limited to a single set of circumstances; separate counts where
  required
- **Motion form (Rule 7.1)** — states the relief sought, the grounds,
  and the supporting authority; oral-argument request, if any, noted
  per Rule 7.1
- **Signature block (Rule 11)** — name, address, telephone, email, and
  **State Bar of Arizona bar number** if an attorney, or the
  **"Self-Represented" / pro se** designation if not; the Rule 11
  signature certifies the filing
- **Certificate of Service (Rule 5)** — date, manner of service, and
  each recipient (and the AZTurboCourt e-service confirmation where
  e-filed)
- **Line numbering + footer present** with **"Page X of Y"** (the
  pleading-paper line numbering and footer are marketplace
  conventions — confirm the venue does not prohibit them)
- **Sensitive-data handling** — confirm the venue's redaction /
  sealed-document practice for protected identifiers before filing

## Pass 2 — Content

The content check applies the pro-se drafting framework. Citation
resolution is delegated to **az-fact-check**; this pass confirms the
component is structurally complete and that the correct forum rule set
governs.

### For a motion / brief:

- [ ] **Correct rule set** for the forum (ARCP / ARFLP / JCRCP)
- [ ] **Relief stated clearly** in the opening paragraph (Rule 7.1)
- [ ] **Rule or statute citation** that grants the relief (e.g.,
      Ariz. R. Civ. P. 56 summary judgment; Rule 12(b) dismissal;
      A.R.S. § ___)
- [ ] **Numbered factual paragraphs** with record cites (affidavit ¶,
      complaint ¶, exhibit, admission)
- [ ] **Application of controlling authority** — case law applied to
      the facts, not merely strung together (citations verified by
      `az-fact-check`)
- [ ] **Counter-arguments addressed**
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Proposed form of order attached / lodged** with the motion
      (see `az-submit-order`)
- [ ] **Oral-argument request** included or omitted per Rule 7.1, and
      hearing/response timing consistent with `az-deadlines`

### For an affidavit / declaration:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat** — sworn before a notary, or an unsworn declaration
      under penalty of perjury where a declaration is permitted
- [ ] **Date and place** of execution
- [ ] For a **business-records** affidavit, the custodian /
      qualified-witness foundation under Ariz. R. Evid. 803(6)

### For a proposed form of order:

- [ ] **Caption identical** to the underlying motion (Rule 10(a))
- [ ] **Findings (if any) separate from the ordering clause**
- [ ] **Ordering clause mirrors** the motion's prayer for relief
- [ ] **Specific dates / amounts** filled in or bracketed for the judge
- [ ] **Judge signature line** at the foot; transmittal consistent with
      `az-submit-order`

### For an answer:

- [ ] **Each allegation of the complaint addressed** (admit / deny /
      lack of knowledge — no skipping) under Rule 8(c)
- [ ] **Affirmative defenses pleaded** under **Rule 8(d)** (statute of
      limitations, payment, lack of standing, etc.) — defenses not
      pleaded may be waived
- [ ] **Compulsory counterclaims** stated (Rule 13(a))
- [ ] **Timeliness** — answer deadline confirmed against the proof of
      service via `az-deadlines`

## Pass 3 — Packet consistency

If filing a packet (motion + affidavit + proposed order + certificate
of service):

- [ ] **Same caption** across all documents — court, county, party
      names, case number, assigned division/judge
- [ ] **Same document title** referenced in the certificate of service
      and the proposed order
- [ ] **Dates align** — certificate-of-service date matches the
      signature date on the motion; affidavit jurat date is consistent
- [ ] **Relief sought matches** between motion prayer and proposed
      order ordering clause (item by item)
- [ ] **All referenced exhibits** attached

## Pre-flight checklist

| Check | Done |
|-------|------|
| Correct forum rule set confirmed (ARCP / ARFLP / JCRCP) | ☐ |
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| Caption shows correct court, county, party names, case number, division/judge (Rule 10(a)) | ☐ |
| Numbered paragraphs sequential (Rule 10(b)) | ☐ |
| Motion states relief, grounds, authority (Rule 7.1) | ☐ |
| Signature block has State Bar of Arizona bar number (attorney) or "Self-Represented" designation (Rule 11) | ☐ |
| Certificate of Service shows manner, date, recipients (Rule 5) | ☐ |
| Footer carries document title + "Page X of Y" | ☐ |
| Affirmative defenses pleaded (Rule 8(d)) | ☐ |
| Proposed form of order lodged with the motion | ☐ |
| Response / hearing timing confirmed via `az-deadlines` | ☐ |
| Local-rule page limit / chambers-copy practice confirmed for the venue | ☐ |
| `az-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Arizona pre-filing failures

1. **Wrong rule set for the forum** — an ARCP-formatted pleading filed
   in a family-law or Justice Court matter; confirm ARCP vs. ARFLP vs.
   JCRCP first.
2. **Missing State Bar of Arizona bar number or pro se designation**
   in the Rule 11 signature block.
3. **Affirmative defenses not pleaded** — Rule 8(d) requires defenses
   be set forth; omitted defenses can be waived.
4. **No proposed form of order lodged** with a motion.
5. **Caption missing the case number or assigned division** required by
   Rule 10(a).
6. **Affidavit not actually sworn** — an un-notarized "affidavit"
   carries no evidentiary weight unless an unsworn declaration under
   penalty of perjury is permitted.

## Composition

- For the deep evidentiary-citation and sworn-vs-argued review:
  `az-fact-check`
- For the format baseline (Rule 10 / 7.1 / 11 / 5): `az-statewide-format`
- For drafting each component: `az-draft-motion`, `az-draft-declaration`,
  `az-draft-order`, `az-draft-note`
- For deadline arithmetic (response and hearing windows): `az-deadlines`
- For the correct forum rule set: `az-maricopa`, `az-pima`,
  `az-superior-courts`, `az-family-court`, `az-justice-courts`
- For the final filing step (AZTurboCourt assembly): `az-file-packet`

## References

- `az-statewide-format` for the Ariz. R. Civ. P. 10 / 7.1 / 11 / 5
  baseline and the local-rule page-limit caveat
- `az-law-references` for canonical Arizona rule and statute text
- Always confirm the current local rules and administrative orders of
  the filing court — this skill checks statewide components and flags
  local-practice items as WARN.
