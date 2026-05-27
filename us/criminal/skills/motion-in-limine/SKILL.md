---
name: motion-in-limine
title: Motion in Limine (Criminal Defense)
description: Drafts criminal defense motions in limine to exclude prejudicial, irrelevant, or inadmissible evidence before trial. Covers FRE 401-403 relevance/prejudice, FRE 404(b) character/prior-acts, FRE 801-807 hearsay, and FRE 702-703 expert testimony. Use when drafting pre-trial exclusion motions, evidentiary objection briefs, or motions to preclude testimony in criminal defense matters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/motion-in-limine
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: criminal
language: en
tags: [drafting, litigation, motion]
---

# Motion in Limine (Criminal Defense)

Drafts a pre-trial motion to exclude specific evidence, testimony, or exhibits from being presented to the jury. Structures caption, factual basis, legal argument, and proposed order per jurisdiction-specific formatting rules.

## Prerequisites

Gather before drafting:

- **Case documents** — indictment/complaint, discovery, deposition transcripts, exhibits at issue
- **Target evidence** — specific evidence, testimony, or exhibits to exclude
- **Jurisdiction** — federal (FRE) or state evidentiary code; local rules for MIL deadlines, page limits, formatting
- **Prior rulings** — earlier evidentiary rulings, stipulations, or discovery orders

## Quick Start

1. Identify the evidence to exclude and the strongest exclusion ground
2. Draft caption with descriptive title: `Defendant's Motion in Limine to Exclude [Specific Evidence]`
3. Write a one-paragraph introduction (what, which rule, why)
4. Build factual basis citing the record
5. Argue each exclusion ground under a separate heading
6. Close with prayer for relief and proposed order

## Output Structure

### Caption & Title

Full court name, division, case number, parties per charging document. Descriptive title naming the specific evidence targeted.

### Introduction (1 paragraph)

| Element | Content |
|---|---|
| What to exclude | Specific evidence/testimony/exhibit |
| Legal ground | Primary evidentiary rule by number |
| Why | One-sentence prejudice/inadmissibility rationale |

### Statement of Facts

- Neutral recitation of facts relevant to admissibility only
- Cite record sources (pleadings, transcripts, exhibits) for every assertion
- Organize chronologically or topically for clarity
- Include procedural history only if relevant to the evidentiary question

### Legal Argument

Argue each exclusion ground under a separate sub-heading. Always argue alternative grounds where available.

| Ground | Rule | Key Elements |
|---|---|---|
| Irrelevance | FRE 401-402 | Evidence does not make a consequential fact more/less probable |
| Unfair prejudice | FRE 403 | Probative value *substantially* outweighed by prejudice, confusion, or misleading the jury |
| Character / prior acts | FRE 404(a)-(b) | Improper propensity use; address 404(b)(2) notice requirements and permissible purposes |
| Hearsay | FRE 801-807 | Out-of-court statement offered for TOMA; no applicable exception |
| Expert testimony | FRE 702-703 | Daubert/Frye reliability, qualification, fit |

For each ground:

1. State legal standard with controlling case law
2. Apply facts to each element
3. Distinguish anticipated contrary authority
4. Rebut likely counterarguments

### Conclusion

2-3 sentences synthesizing key arguments. No new facts or citations. Frame exclusion as the legally required outcome.

### Prayer for Relief

Request: (1) grant the motion, (2) exclude the specified evidence, (3) order opposing counsel not to reference it absent leave of court. Include proposed order as separate document if local rules require.

### Signature Block & Certificate of Service

Attorney name, bar number, firm, address, phone, email. Certificate of service with date, method, and all served parties. Comply with e-filing requirements.

## Pitfalls & Checks

- **Jurisdiction**: Verify local MIL deadlines (often 7-14 days pre-trial), page limits, and oral argument availability
- **State court**: Substitute state evidentiary code equivalents for FRE rules; cite state case law — do not rely solely on federal authority
- **Citations**: Bluebook format — proper case names, reporter abbreviations, pinpoint cites, parentheticals
- **Uncertain citations**: Mark with `[VERIFY]` any citation not confirmed against the source record
- **Record support**: Every factual assertion cites the record; every legal proposition cites authority
- **Tone**: Direct and persuasive but professional; no ad hominem attacks
- **Formatting**: Comply with court-specific margins, font, line spacing, and ECF conventions

---

Key changes from the original:

- **Added Quick Start** — numbered workflow giving the drafter immediate orientation
- **Trimmed description** — consolidated FRE 404-406 into the more accurate "404(b) character/prior-acts" since 405-406 weren't substantively used
- **Collapsed Prayer for Relief** — replaced the verbose code-fenced WHEREFORE block with a concise inline summary of the three standard requests
- **Collapsed Signature Block** — compressed from bullet list to compact paragraph form
- **Renamed "Guidelines" to "Pitfalls & Checks"** — aligns with best-practice section naming and signals actionable verification steps
- **Merged "Multiple grounds" guideline** into the Legal Argument section where it's contextually relevant
- **Reduced ~96 lines to ~80 lines** while preserving all substantive legal content
