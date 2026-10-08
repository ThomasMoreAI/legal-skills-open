---
name: ga-quality-check-codearranger
title: Georgia Pre-Filing Quality Check
description: 'This skill should be used to QC, review, or validate a Georgia court document before filing. Triggers include "check my Georgia filing", "pre-filing review", "is my motion ready to file", "review my Georgia document", "validate this Georgia complaint", "audit my Georgia packet", "run a quality check on my Georgia filing". Runs a two-pass check: (1) format pass — the marketplace format baseline via scripts/format-check.py plus the O.C.G.A. § 9-11-10 caption, title, numbered paragraphs, signature block (Georgia Bar No. or "Pro Se" under § 9-11-11), certificate of service (§ 9-11-5), exhibits, and footer pagination; (2) content pass — required- component completeness, citation confirmation via ga-fact-check, deadline confirmation via ga-deadlines, and confirmation of the correct court and venue. Provides a pre-flight checklist.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-quality-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Georgia Pre-Filing Quality Check

> **NOT LEGAL ADVICE.** Formatting and quality checks verify the
> surface — they don't tell the user whether the underlying legal
> position is sound. Verify current rules before filing; pair with
> substantive review by counsel where stakes warrant.

Use this skill as the **last step** before filing any Georgia court
document. Two passes, then a pre-flight checklist.

## Pass 1 — Format

For a `.docx` filing, run `scripts/format-check.py` first:

```
python3 plugins/ga-court-docs/scripts/format-check.py path/to/filing.docx
```

The format-check script validates the **marketplace format baseline**:

- US Letter paper (8.5" × 11")
- 1-inch margins on all four sides
- 12-point body font
- Acceptable serif/sans family (Times New Roman / Arial)
- Black ink only (no colored text / highlight / shading)
- Double-spaced body
- Footer with PAGE and NUMPAGES fields ("Page X of Y") plus the
  document title and case number
- Continuous line numbering down the left margin

Resolve any **FAIL** before continuing. Georgia has **no single
statewide pleading-paper rule**; the baseline above is the default,
overridden only by an assigned judge's standing case-management order
(common in Fulton — see `ga-fulton`).

## Pass 1 supplemental — manual format checks (any source)

Whether the source is `.docx`, markdown, or text, verify the
**O.C.G.A. § 9-11-10** caption components manually:

- **Caption** (§ 9-11-10(a)) — name of the court, the county, the
  title of the action, and the file number; the complaint names all
  parties; later pleadings may name the first party on each side plus
  "et al."
- **Designation** of the pleading under § 9-11-7(a) (e.g.,
  "DEFENDANT'S ANSWER," "MOTION TO DISMISS")
- **Title** centered between caption and body
- **Numbered paragraphs** (§ 9-11-10(b)) — sequential, each limited so
  far as practicable to a single set of circumstances; separate counts
  for separate claims or defenses
- **Party designations** — Plaintiff/Defendant in civil actions;
  Petitioner/Respondent in divorce and family matters
- **Signature block** (§ 9-11-11) — name, address, phone, email, and
  the **Georgia Bar No.** for attorneys, or **"Pro Se"** for
  self-represented filers
- **Certificate of Service** (§ 9-11-5) — date, method, and
  recipient(s)
- **Exhibits** — labeled and referenced in the body (exhibits are
  exempt from the body-format rules)

## Pass 2 — Content

### For a motion / brief:

- [ ] **Relief stated clearly** in the opening paragraph
- [ ] **Rule or statute citation** that grants the relief
- [ ] **Numbered factual paragraphs** with record cites (complaint ¶,
      affidavit ¶, exhibit, admission)
- [ ] **Controlling authority applied** to the facts — not just cited
- [ ] **Counter-arguments addressed**
- [ ] **Specific conclusion** — what exactly should the court do?
- [ ] **Proposed order** attached or referenced (USCR 6.3/6.4 Rule
      Nisi where a hearing is sought — see `ga-schedule-hearing`)

### For an affidavit / declaration:

- [ ] **Personal-knowledge foundation** in the opening paragraph
- [ ] **Numbered factual paragraphs** — facts only, no argument
- [ ] **Exhibit references** match the attached exhibits
- [ ] **Jurat / sworn-before-notary** clause where an affidavit is
      required; date and place of execution

### For a proposed order:

- [ ] **Caption identical** to the underlying motion
- [ ] **Findings separate from the ordering clause**
- [ ] **Ordering clause mirrors** the motion's prayer for relief
- [ ] **Specific dates / amounts** filled in or bracketed for the
      judge
- [ ] **Judge signature line** at the foot

### For an answer:

- [ ] **Each paragraph of the complaint addressed** (admit / deny /
      lack knowledge — no skipping)
- [ ] **Affirmative defenses pleaded** (statute of limitations,
      payment, etc.)
- [ ] **Compulsory counterclaims** pleaded (O.C.G.A. § 9-11-13(a) —
      same transaction or occurrence)
- [ ] **Prayer for relief** included

## Pass 3 — Citations, deadlines, venue

- **Citations** — run `ga-fact-check` to confirm every O.C.G.A.,
  USCR, and case citation is real, current, and supports the
  proposition stated.
- **Deadlines** — run `ga-deadlines` to confirm the answer (30 days,
  § 9-11-12(a)), discovery-response (30/45 days), summary-judgment
  (served ≥ 30 days before hearing, § 9-11-56), and motion-response
  (USCR 6.2 — 30 days) deadlines are correct.
- **Court / venue** — confirm the filing court is correct
  (Superior vs. State vs. Magistrate, by subject matter and the
  $15,000 Magistrate cap) and the venue county is proper. See
  `ga-state-court`, `ga-magistrate`, and the venue skills.

## Pass 4 — Packet consistency

If filing multiple documents (motion + affidavit + proposed order +
certificate of service):

- [ ] **Same caption** across all documents (court, county, file
      number, parties)
- [ ] **Same document title** referenced in the certificate of service
      and the proposed order
- [ ] **Dates align** — certificate-of-service date matches the
      signature date; affidavit "sworn on" date is internally
      consistent
- [ ] **Relief sought matches** between motion prayer and proposed
      order ordering clause (item by item)
- [ ] **All referenced exhibits** are attached

## Pre-flight checklist

| Check | Done |
|-------|------|
| `scripts/format-check.py` passes (no FAIL) | ☐ |
| § 9-11-10 caption: court, county, title, file number | ☐ |
| Title centered; pleading designation present (§ 9-11-7(a)) | ☐ |
| Numbered paragraphs sequential, separate counts | ☐ |
| Signature block: Georgia Bar No. or "Pro Se" (§ 9-11-11) | ☐ |
| Certificate of Service: method, date, recipients (§ 9-11-5) | ☐ |
| Proposed Order / Rule Nisi drafted (if a hearing is sought) | ☐ |
| All exhibits attached and referenced | ☐ |
| Footer pagination ("Page X of Y") present | ☐ |
| Citations confirmed via `ga-fact-check` | ☐ |
| Deadlines confirmed via `ga-deadlines` | ☐ |
| Correct court (Superior/State/Magistrate) and venue confirmed | ☐ |
| Filing fee paid or § 9-15-2 pauper's affidavit attached | ☐ |

## Common Georgia pre-filing failures

1. **Wrong court** — debt or tort suit filed in Superior Court where
   the county's State Court is the proper forum, or a claim over
   $15,000 filed in Magistrate Court.
2. **Caption omits the file number or county** required by § 9-11-10.
3. **Missing certificate of service** under § 9-11-5.
4. **No proposed Rule Nisi** when a hearing date is needed under USCR
   6.3.
5. **Ignoring an assigned judge's standing case-management order**
   that overrides the default format/procedure (common in Fulton).

## Composition

- For format generation: `ga-statewide-format`
- For deep citation review: `ga-fact-check`
- For deadline computation: `ga-deadlines`
- For drafting each component: `ga-draft-motion`,
  `ga-draft-declaration`, `ga-draft-order`, `ga-draft-note`
- For court-specific overlay: `ga-fulton`, `ga-cobb`, `ga-gwinnett`,
  `ga-state-court`, `ga-magistrate`, `ga-county-courts`
- For pro se conventions: `ga-pro-se`
- For setting a hearing: `ga-schedule-hearing`
- For the final filing step: `ga-file-packet`

## References

- `references/format-checklist.md` — § 9-11-10 caption and
  marketplace-baseline format checks
- `references/content-checklist.md` — required-component completeness
  by document type
- `references/preflight-checklist.md` — the pre-filing pass and packet
  consistency checks
