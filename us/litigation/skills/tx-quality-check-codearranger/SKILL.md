---
name: tx-quality-check-codearranger
title: Texas Pre-Filing Quality Check
description: 'Use to QC, review, or validate a Texas court document before filing. Triggers: "quality check Texas filing", "is my Texas motion ready to file", "pre-filing review Texas", "QC this Texas document", "check this petition before I file it in Texas", "validate this Texas affidavit", "audit this Texas packet", "is my Harris County motion ready", "review my Texas answer". Runs two passes plus a packet sweep: (1) format pass — caption and form, document title, Tex. R. Civ. P. 57 signature with State Bar of Texas bar number (or self-represented designation), line numbering + footer + "Page X of Y", Tex. R. Civ. P. 21a certificate of service, and the Tex. R. Civ. P. 47(c) relief-range statement on a petition; (2) content pass — relief and grounds stated, Notice of Hearing timing, verified denial where required, affirmative defenses pleaded, required attachments including the proposed order. Lighter touch than `tx-fact-check`, which deep-dives evidentiary citations and sworn-vs-argued
  alignment.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tx-court-docs/skills/tx-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Texas Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** This skill detects errors in form and
> structural completeness — it verifies the **surface**. It does not
> assess whether the underlying legal position is sound. Verify
> against the current Texas Rules of Civil Procedure and the local
> rules of the filing court before filing.

Use this skill as the **last step** before filing any Texas court
document. Two passes, plus a packet-consistency sweep.

## A note on the forum

Confirm the **court level** before the format pass — District Court,
County Court at Law / Constitutional County Court, or Justice Court
(JP). Caption wording and judge title differ, and **justice-court
procedure is simplified**: under Tex. R. Civ. P. 500.3(e) the regular
rules of civil procedure and the rules of evidence largely do **not**
apply in justice court except where TRCP Part V (Rules 500–510)
incorporates them. Route family-law filings to `tx-family-court` for
the matching caption and the **Petitioner/Respondent** designations
(rather than Plaintiff/Defendant).

## Pass 1 — Format

For a generated filing, run `scripts/format-check.py` first:

```
python3 plugins/tx-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the marketplace common-practice
defaults (line numbering, footer, "Page X of Y", caption, signature)
against the Texas baseline. Where a value is a local-rule matter, the
script emits **WARN** (not FAIL) — resolve those by checking the
venue's local rules. Resolve any **FAIL** before continuing.

### Format pass — non-`.docx` (markdown / text drafts)

Verify manually:

- **Caption** — names of the parties, the court (e.g., "In the [Nth]
  Judicial District Court of [County] County, Texas"), party
  designations (Plaintiff/Defendant; Petitioner/Respondent in
  family/special matters), the **cause number**, and the document
  title
- **Pleading form (Tex. R. Civ. P. 45 / 47)** — a plain statement of
  the cause of action; numbered paragraphs; and, on a petition, the
  **Tex. R. Civ. P. 47(c) statement of the range of relief sought**
  (a Texas requirement — its omission can bar a default judgment)
- **Motion form (Tex. R. Civ. P. 21)** — states the grounds and the
  relief sought; "TO THE HONORABLE JUDGE" opener; PRAYER closes
- **Notice of Hearing (Tex. R. Civ. P. 21)** — present where a motion
  is being set; submission vs. oral hearing chosen; the notice floor
  (or the Rule 166a 21-day track) confirmed
- **Signature block (Tex. R. Civ. P. 57)** — name, address, telephone,
  email, fax, and **State Bar of Texas bar number** if an attorney, or
  the **pro se / self-represented** designation if not
- **Certificate of Service (Tex. R. Civ. P. 21a)** — date, manner of
  service, and each recipient (and the eFileTexas e-service confirmation
  where e-filed)
- **Line numbering + footer present** with **"Page X of Y"** and the
  document title
- **Sensitive-data handling** — confirm the redaction practice (e.g.,
  truncating Social Security and financial-account numbers) before
  filing

## Pass 2 — Content

The content check applies the pro-se drafting framework. Citation
resolution is delegated to **tx-fact-check**; this pass confirms the
component is structurally complete.

### For a motion:

- [ ] **Relief stated clearly** in the opening paragraph (Rule 21)
- [ ] **Grounds stated** for the relief
- [ ] **Rule or statute citation** that grants the relief (e.g.,
      Tex. R. Civ. P. 166a summary judgment; Rule 91a dismissal;
      CPRC § ___)
- [ ] **Numbered factual paragraphs** with record cites (affidavit/
      declaration ¶, petition ¶, exhibit, admission)
- [ ] **Application of controlling Texas authority** — case law
      applied to the facts (citations verified by `tx-fact-check`)
- [ ] **Counter-arguments addressed**
- [ ] **PRAYER** — what exactly should the court do?
- [ ] **Notice of Hearing** prepared with the Rule 21(b) notice floor
      (or Rule 166a **21-day** track), consistent with `tx-deadlines`
- [ ] For **Rule 166a(i) no-evidence**: the **specific elements** with
      no evidence are stated
- [ ] For **Rule 91a**: filed within **60 days** of the challenged
      pleading; rests on the pleadings only
- [ ] **Proposed order** drafted as a separate document (`tx-draft-order`)

### For a petition:

- [ ] **Tex. R. Civ. P. 47(c) statement of relief range** present
- [ ] **Discovery control plan level** stated (Tex. R. Civ. P. 190 —
      Level 1/2/3; expedited actions under Rule 169)
- [ ] **Jurisdiction and venue** alleged
- [ ] **Numbered paragraphs**; plain statement of each cause of action
- [ ] **PRAYER** for relief; request for citation to issue

### For an affidavit / unsworn declaration:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat** (notarized affidavit) **or** a **CPRC § 132.001
      unsworn declaration** under penalty of perjury (no notary), with
      the prescribed jurat (printed name, date of birth, address,
      county and state of execution)
- [ ] For a **business-records** affidavit, the custodian /
      qualified-witness foundation under Tex. R. Evid. 902(10)

### For a proposed order / judgment:

- [ ] **Caption identical** to the underlying motion
- [ ] **Recitals separate from the decretal clause** ("IT IS ORDERED")
- [ ] **Decretal clause mirrors** the motion's PRAYER, item by item
- [ ] **A final judgment disposes of all parties and all claims** (or
      the interlocutory status is intended and clear)
- [ ] **Judge signature / "SIGNED this ___ day" line** at the foot;
      "submitted by" line; transmittal consistent with `tx-submit-order`

### For an Original Answer:

- [ ] **General denial** (Tex. R. Civ. P. 92) and/or specific denials
- [ ] **Verified denial under oath** where Tex. R. Civ. P. 93 requires
      it (e.g., denial of a **sworn account** under Rule 93(10) / Rule
      185, lack of capacity, defect of parties) — an unverified denial
      may fail to put the matter in issue
- [ ] **Affirmative defenses pleaded** (limitations, payment, lack of
      standing, etc.) — defenses not pleaded may be waived
- [ ] **Compulsory counterclaims** stated (Tex. R. Civ. P. 97)
- [ ] **Timeliness** — answer deadline confirmed against the return of
      service via `tx-deadlines` (the Rule 99 "Monday rule" in
      district/county court; the **end of the 14th day** after service
      in justice court under Rule 502.5)

## Pass 3 — Packet consistency

If filing a packet (petition/motion + proposed order + Notice of
Hearing + affidavit/declaration + certificate of service + civil case
information sheet):

- [ ] **Same caption** across all documents — court, county, party
      names, cause number
- [ ] **Same document title** referenced in the certificate of service,
      the Notice of Hearing, and the proposed order
- [ ] **Dates align** — certificate-of-service date matches the
      signature date; affidavit jurat / declaration date consistent;
      hearing/submission date respects the notice floor
- [ ] **Relief sought matches** between motion (PRAYER) and proposed
      order (item by item)
- [ ] **All referenced exhibits** attached

## Pre-flight checklist

| Check | Done |
|-------|------|
| Forum confirmed (District / County Court at Law / Justice Court) | ☐ |
| `scripts/format-check.py` run; no FAIL (WARN items confirmed against local rules) | ☐ |
| Caption shows court, county, party designations, cause number | ☐ |
| Pleading/motion form correct; petition carries the Rule 47(c) relief range | ☐ |
| Notice of Hearing meets the notice floor (or Rule 166a 21-day track) | ☐ |
| Signature block has State Bar of Texas number (attorney) or self-represented designation (Rule 57) | ☐ |
| Certificate of Service shows manner, date, recipients (Rule 21a) | ☐ |
| Footer carries document title + "Page X of Y" | ☐ |
| Verified denial filed where Rule 93 requires it (answer) | ☐ |
| Affirmative defenses pleaded (answer) | ☐ |
| Final judgment disposes of all parties and claims | ☐ |
| Proposed order prepared as a separate document | ☐ |
| `tx-fact-check` deep audit run (if high-stakes filing) | ☐ |

## Common Texas pre-filing failures

1. **Missing Tex. R. Civ. P. 47(c) relief-range statement** on a
   petition — can bar a default judgment.
2. **Unverified denial of a sworn account** — Tex. R. Civ. P. 93(10) /
   Rule 185 require a denial **under oath**; a bare general denial does
   not put a properly verified account in issue.
3. **No-evidence motion that fails to state the specific elements** —
   Tex. R. Civ. P. 166a(i) requires the motion to identify the elements
   on which there is no evidence.
4. **Notice of Hearing short of the notice floor** (or the Rule 166a
   21-day track) once the +3-day mail/email add-on is counted.
5. **Missing State Bar of Texas number or self-represented
   designation** in the Tex. R. Civ. P. 57 signature block.
6. **A "final" judgment that does not dispose of all parties and
   claims** — it is interlocutory and generally not appealable.

## Composition

- For the deep evidentiary-citation and sworn-vs-argued review:
  `tx-fact-check`
- For the format baseline (caption / Rule 21 / Rule 57 / Rule 21a):
  `tx-statewide-format`
- For drafting each component: `tx-draft-motion`,
  `tx-draft-declaration`, `tx-draft-note`, `tx-draft-order`
- For deadline arithmetic (notice floor, Rule 166a 21-day track, mail
  add-on, the Rule 99 "Monday rule"): `tx-deadlines`
- For the forum/venue: `tx-hcdc`, `tx-dcdc`, `tx-county-courts`,
  `tx-family-court`
- For the final filing step (eFileTexas assembly): `tx-file-packet`

## References to author

- `references/format-checklist.md` — the format pass expanded
- `references/content-checklist.md` — the per-document-type content
  pass expanded
