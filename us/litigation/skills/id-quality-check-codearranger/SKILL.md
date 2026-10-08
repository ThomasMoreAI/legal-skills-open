---
name: id-quality-check-codearranger
title: Idaho Pre-Filing Quality Check
description: 'Use to QC, review, or validate an Idaho court document before filing. Triggers: "quality check Idaho filing", "is my Idaho motion ready to file", "I.R.C.P. 2 / Rule 10 compliance", "pre- filing review Idaho", "QC this Idaho document", "check this motion before I file it in Idaho", "validate this Idaho affidavit", "audit this Idaho packet", "is my Ada County motion ready". Runs two passes plus a packet sweep: (1) format pass — I.R.C.P. 2 caption and form, document title at the bottom of each page, I.R.C.P. 11 signature with Idaho State Bar number, line numbering + footer + "Page X of Y", I.R.C.P. 5 certificate of service; (2) content pass — relief and grounds stated with particularity, Notice of Hearing 14-day timing, affirmative defenses pleaded, required attachments including the proposed order. Lighter touch than `id-fact-check`, which deep-dives evidentiary citations and sworn-vs-argued alignment.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/id-court-docs/skills/id-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
sources:
- title: Content Checklist
  path: references/content-checklist.md
- title: Format Checklist
  path: references/format-checklist.md
---

# Idaho Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness. It does not assess substantive legal
> sufficiency. Verify against the current Idaho Rules of Civil
> Procedure and the local rules of the filing court before filing.

Use this skill as the **last step** before filing any Idaho court
document. Two passes, plus a packet-consistency sweep.

## A note on the forum

Confirm whether the matter is heard in the **District Court** or the
**Magistrate Division** before the format pass — the caption and the
assigned judge title differ, and family-law and small-claims matters
travel in the Magistrate Division. Route family-law filings to
`id-family-court` for the matching caption and party designations
(Petitioner/Respondent rather than Plaintiff/Defendant).

## Pass 1 — Format

For a generated filing, run `scripts/format-check.py` first:

```
python3 plugins/id-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the marketplace common-practice
defaults against the **I.R.C.P. 2** baseline: 8½×11 white paper,
black ink, font **≥ 11 pt**, **double or 1½ spacing**, margins
**≥ 1.2" top/sides and ≥ 1" bottom**, the **title of the court ≥ 3"
from the top of page 1**, the **document title at the bottom of each
page**, and a footer with **document title + "Page X of Y"**
pagination. Where a value is a local-rule matter, the script emits
**WARN** (not FAIL) — resolve those by checking the venue's local
rules. Resolve any **FAIL** before continuing.

### Format pass — non-`.docx` (markdown / text drafts)

Verify manually:

- **Caption (I.R.C.P. 2 / 10(a))** — names of the parties, title of
  the court (e.g., "IN THE DISTRICT COURT OF THE [Nth] JUDICIAL
  DISTRICT OF THE STATE OF IDAHO, IN AND FOR THE COUNTY OF ___"),
  party designations (Plaintiff/Defendant; Petitioner/Respondent in
  family/special matters), the **case number**, and the document
  title
- **Title of the court ≥ 3" from the top** of page 1
- **Document title at the bottom of each page** (I.R.C.P. 2 form
  requirement)
- **Numbered paragraphs (I.R.C.P. 10(b))** — sequential, each
  averment limited to a single set of circumstances; exhibits are
  part of the pleading
- **Motion form (I.R.C.P. 7(b))** — states the relief sought and the
  grounds **with particularity**; supporting Memorandum present
- **Notice of Hearing (I.R.C.P. 7(b)(3))** — present where a motion
  is being set; 14-day (or Rule 56 28-day) timing confirmed
- **Signature block (I.R.C.P. 11)** — name, address, telephone,
  email, and **Idaho State Bar number** if an attorney, or the
  **pro se / self-represented** designation if not; the Rule 11
  signature certifies the filing
- **Certificate of Service (I.R.C.P. 5)** — date, manner of service,
  and each recipient (and the I.R.E.F.S. e-service confirmation
  where e-filed)
- **Line numbering + footer present** with **"Page X of Y"**
- **Sensitive-data handling** — confirm the venue's redaction /
  sealed-document practice before filing

## Pass 2 — Content

The content check applies the pro-se drafting framework. Citation
resolution is delegated to **id-fact-check**; this pass confirms the
component is structurally complete.

### For a motion / Memorandum:

- [ ] **Relief stated clearly** in the opening paragraph (Rule 7(b))
- [ ] **Grounds stated with particularity** (Rule 7(b)(1))
- [ ] **Rule or statute citation** that grants the relief (e.g.,
      I.R.C.P. 56 summary judgment; Rule 12(b) dismissal; I.C. § ___)
- [ ] **Supporting Memorandum** present
- [ ] **Numbered factual paragraphs** with record cites (affidavit/
      declaration ¶, complaint ¶, exhibit, admission)
- [ ] **Application of controlling Idaho authority** — case law
      applied to the facts (citations verified by `id-fact-check`)
- [ ] **Counter-arguments addressed**
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Notice of Hearing** prepared with **14-day** (or Rule 56
      **28-day**) timing, consistent with `id-deadlines`
- [ ] **Proposed order** drafted as a separate document
      (`id-draft-order`)

### For an affidavit / declaration:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat** (notarized affidavit) **or** an **Idaho Code
      § 9-1406 declaration** under penalty of perjury (no notary)
- [ ] **Date and place** of execution
- [ ] For a **business-records** affidavit, the custodian /
      qualified-witness foundation under I.R.E. 803(6)

### For a proposed order / judgment:

- [ ] **Caption identical** to the underlying motion
- [ ] **Recitals/findings separate from the decretal clause** (Order)
- [ ] A **Judgment is a separate document** stating only the relief
      (I.R.C.P. 54(a))
- [ ] **Decretal clause mirrors** the motion's relief, item by item
- [ ] **Rule 54(b) certificate** present only if finality on fewer
      than all claims/parties is intended
- [ ] **Judge signature line + entry line** at the foot; transmittal
      consistent with `id-submit-order`

### For an answer:

- [ ] **Each allegation addressed** (admit / deny / lack of knowledge)
- [ ] **Affirmative defenses pleaded** (statute of limitations,
      payment, lack of standing, etc.) — defenses not pleaded may be
      waived
- [ ] **Compulsory counterclaims** stated (I.R.C.P. 13(a))
- [ ] **Timeliness** — answer deadline confirmed against the proof of
      service via `id-deadlines`

## Pass 3 — Packet consistency

If filing a packet (motion + Memorandum + affidavit/declaration +
Notice of Hearing + proposed order + certificate of service):

- [ ] **Same caption** across all documents — court, county, party
      names, case number, assigned judge
- [ ] **Same document title** referenced in the certificate of
      service, the Notice of Hearing, and the proposed order
- [ ] **Dates align** — certificate-of-service date matches the
      signature date; affidavit jurat / declaration date consistent;
      hearing date respects the 14-day (or 28-day) lead time
- [ ] **Relief sought matches** between motion and proposed order
      (item by item)
- [ ] **All referenced exhibits** attached

## Pre-flight checklist

| Check | Done |
|-------|------|
| Forum confirmed (District Court vs. Magistrate Division) | ☐ |
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| Caption shows court, county, party designations, case number, judge (I.R.C.P. 2) | ☐ |
| Title of court ≥ 3" from top; document title at bottom of each page | ☐ |
| Numbered paragraphs sequential (I.R.C.P. 10(b)) | ☐ |
| Motion states relief + grounds with particularity (I.R.C.P. 7(b)) | ☐ |
| Notice of Hearing meets 14-day (or Rule 56 28-day) timing | ☐ |
| Signature block has Idaho State Bar number (attorney) or self-represented designation (I.R.C.P. 11) | ☐ |
| Certificate of Service shows manner, date, recipients (I.R.C.P. 5) | ☐ |
| Footer carries document title + "Page X of Y" | ☐ |
| Affirmative defenses pleaded (answer) | ☐ |
| Judgment is a separate document (I.R.C.P. 54(a)) | ☐ |
| Proposed order prepared as a separate document | ☐ |
| `id-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Idaho pre-filing failures

1. **Document title not at the bottom of each page** — I.R.C.P. 2
   requires it; a top-only title is a format defect.
2. **Title of the court placed too high** — it must sit at least 3"
   from the top of page 1.
3. **Missing Idaho State Bar number or pro se designation** in the
   I.R.C.P. 11 signature block.
4. **Notice of Hearing short of the 14-day lead** (or the 28-day
   Rule 56 lead) once the mail add-on is counted.
5. **Judgment combined with the order's reasoning** — I.R.C.P. 54(a)
   requires the judgment to be a separate document stating only
   relief.
6. **Affidavit not actually sworn and not a § 9-1406 declaration** —
   an un-notarized "affidavit" without the declaration subscription
   carries no evidentiary weight.

## Composition

- For the deep evidentiary-citation and sworn-vs-argued review:
  `id-fact-check`
- For the format baseline (I.R.C.P. 2 / 7(b) / 11 / 5):
  `id-statewide-format`
- For drafting each component: `id-draft-motion`,
  `id-draft-declaration`, `id-draft-note`, `id-draft-order`
- For deadline arithmetic (14-day / 28-day windows, mail add-on):
  `id-deadlines`
- For the forum/venue: `id-ada`, `id-bonneville`, `id-county-courts`,
  `id-family-court`
- For the final filing step (I.R.E.F.S. assembly): `id-file-packet`

## References to author

- `references/format-checklist.md` — the I.R.C.P. 2 format pass
  expanded
- `references/content-checklist.md` — the per-document-type content
  pass expanded
