---
name: table-of-authorities-jslandau
title: Table of Authorities Extraction
description: Use when extracting citations from a legal brief to build a Table of Authorities - runs eyecite locally to extract and categorize all legal citations (cases, statutes, constitutional provisions, legislative materials, secondary sources) with short forms (Id., supra, reporter-only cites) already resolved, walks the document for gap categories eyecite does not catch (administrative decisions, popular-name statutes, informal references), and produces a categorized TOA with page references in both structured data and formatted legal output. Document text never leaves the machine.
author: jslandau
author_url: https://github.com/jslandau/legal-tools/tree/main/plugins/legal-tools/skills/table-of-authorities
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Table of Authorities Extraction

## Prerequisites

This skill uses the citation taxonomy, short-form resolution rules, proposition/parenthetical handling, and flag vocabulary defined in the `citation-toolkit` skill. Read `citation-toolkit` first; the steps below refer to its definitions by name rather than restating them. Content that is specific to building a Table of Authorities — the Administrative Decisions category, page-reference aggregation, passim rules, categorization, and the formatted-TOA output — stays in this skill.

When dispatching subtask subagents (citation parsing, short-form resolution, category assignment), follow the **Model Tiers for Subtasks** section of `citation-toolkit` — most per-citation mechanical work in this skill is Haiku-tier.

## Overview

Extract every legal citation from a brief, resolve short forms to their full citations, categorize each authority, and produce a Table of Authorities with page references. Output both structured data (JSON) and formatted legal TOA text.

## When to Use

- Building a Table of Authorities for an appellate brief
- Auditing citations in a legal document
- Cross-referencing authorities across a brief

## Before Starting

Ask the user:
1. **Which court is this brief for?** (Determines passim rules and any formatting requirements from local rules)
2. **What format is the document in?** (PDF, text, DOCX)
3. **Does the document already contain a TOA to exclude?**

## Input Handling

### Supported Document Formats

- **PDF:** Use the Read tool. **Use the document's own page numbering** (footers like "– 1 –", headers like "Page: 8"), NOT raw PDF page numbers.
- **Plain text / Markdown:** Look for explicit page markers (e.g., `## PAGE 1`). Ask the user to clarify format if not obvious.
- **DOCX:** Convert to text first. Page boundaries are approximate without rendering — note this to the user.

### Identifying the Substantive Content

The skill extracts citations from scratch — do NOT rely on or reference any existing TOA in the document. Instead, identify the substantive pages to scan:

1. **Find the body of the brief.** Look for section headings like "INTRODUCTION", "ARGUMENT", "STATEMENT OF THE CASE", "STATEMENT OF FACTS", and "CONCLUSION". These are the pages to scan.
2. **Skip front matter.** Exclude cover pages, certificates of interest, tables of contents, any existing table of authorities, tables of abbreviations, and other preliminary material. These often use roman numeral pagination (i, ii, iii...).
3. **Skip back matter.** Exclude certificates of compliance, certificates of service, and signature pages after the CONCLUSION.
4. **Include footnotes.** Footnotes on substantive pages often contain important citations — sometimes entire string cites live in footnotes. Scan them thoroughly.
5. **Exclude non-authority references.** References to other briefs in the case (e.g., "Blue Br.", "Red Br.", "Appellant's Br."), appendix citations ("Appx123"), and record citations ("R. at 45") are NOT legal authorities and should not appear in the TOA.

## Citation Extraction Process

Work through the document page by page. For each page, extract every legal citation. Track the **current page number** as you go.

### Step 1: Identify All Citations

Extraction follows the **two-pass workflow** in `citation-toolkit`'s "Extraction: eyecite is the primitive" section: eyecite extracts every recognized citation in one call, then a focused human pass adds the gap categories. Do NOT free-form scan the document — that is what eyecite is for.

**Pass 1 — eyecite (local).** Run the local `eyecite_extract.py` script in `citation-toolkit/` over the substantive text. Extraction stays on-machine because briefs are routinely privileged work product. The script's output is a JSON array of citations in document order, with `Id.`/`supra`/short cites already resolved to their antecedents — Step 2 (Short Forms) is largely already done for you.

**Do NOT** use the MCP's `extract_citations` or `analyze_citations` for this — both upload the full document text to Free Law Project's servers. See `citation-toolkit`'s "Confidentiality" note for the bright-line rule. (TOA also doesn't need CourtListener verification anyway — only the citation strings and their pages.)

**Pass 2 — gap pass.** Walk the substantive content once, looking *only* for the gap categories listed in `citation-toolkit`: administrative decisions (PTAB, FTC, SEC, FCC), EU/international cases (ECLI, ECHR), state constitutional provisions, popular-name statutes ("the Lanham Act"), informal constitutional references ("First Amendment"), and statute subsection breakdowns. Add these to the Pass-1 array.

**Page tracking is the skill's responsibility.** eyecite returns character-level span offsets, not page numbers. Build an offset→page map as you scan (whenever you cross a page boundary, note the offset); then for each entry in the Pass-1 array, look up its span start in the map to get the page. Pass-2 cites get the page where you find them. This is much more reliable than re-deriving page numbers from scratch and lets Step 3's aggregation work uniformly across both passes.

The toolkit covers Westlaw/LEXIS citations, informal references, popular-name statutes, grouped and informal rule references, state constitutional provisions, and all the parenthetical handling rules.

Two categorization refinements this skill adds on top of the toolkit's taxonomy:

#### Administrative Decisions (ToA-specific category)

Treat these as a **separate category** in the output TOA, between Cases and Constitutional Provisions. Citations still use the toolkit's Case or administrative patterns:

- **PTAB decisions:** `[Party] v. [Party], IPR[year]-[number] (PTAB [date])`
  - Example: `Apple Inc. v. Fintiv, Inc., IPR2020-00019 (PTAB Mar. 20, 2020)`
- **Agency decisions:** FTC, SEC, FCC orders and opinions

Omit this category if none exist; some briefs fold these into Cases.

#### Statutes — bare-section handling for TOA

If a bare section reference appears (e.g., "§ 230" without subsection), attempt to resolve it to a specific subsection cited nearby. If unresolvable, list it as cited and flag `ambiguous_section_reference` (from `citation-toolkit`'s flag vocabulary).

#### State constitutional provisions

In addition to the federal patterns covered in `citation-toolkit`, include state provisions: `[State] Const. art. [X], § [Y]`.

### Step 2: Resolve Short Forms

eyecite (Pass 1 of Step 1) already resolved `Id.`, `supra`, party-name, and reporter-only short forms for the citations it recognized — each short-form entry in the Pass-1 array has a `resolved_to` pointer to its antecedent. The remaining work in this step is:

- **Pass-2 cites only:** maintain a citation stack across the gap-category cites and resolve any short forms among them by hand, following the **Short Forms** rules in `citation-toolkit` (Id., party-name, reporter-only, supra/supra note, informal references).
- **eyecite short forms flagged `unresolved_short_form`:** try once more against the running stack (including Pass-2 cites). If still unresolved, leave the flag in place for user review — don't guess.

Two ToA-specific caveats worth remembering:

- **Id. chains across pages:** In a chain (X, *Id.*, *Id.*, *Id.*), all resolve back to X. Each *Id.* adds the page where it appears to X's page list (this is what Step 3 aggregates).
- **Id. referring to non-authorities:** `Id.` sometimes refers to an appendix or record cite rather than a legal authority — check what precedes it before resolving.

### Step 3: Aggregate Page References

For each unique authority:
- Collect all pages where it appears (via full citation OR any short form)
- **Page-break citations:** When the citation text itself spans two pages, record BOTH pages. But a citation's page is determined by where the **citation text** appears, not where the surrounding sentence continues. Three scenarios:
  - *Citation straddles break* (e.g., "Bristol-Myers Squibb, 582 U.S." on p.25, "at 264" on p.26) → record **both** pages
  - *Sentence wraps but citation is on one page* (e.g., "consistent with *Bristol-Myers Squibb* and the cases" ends p.25, sentence continues on p.26 with non-citation text) → record **only** the page where the citation text appears
  - *String cite wraps* → only authorities whose actual citation text appears on a given page get that page number
- **Deduplicate** page numbers — each page listed only once
- Sort page numbers in ascending order
- **Passim rules** (determined by court — ask user if unknown):

| Court | Passim allowed? |
|-------|----------------|
| SCOTUS (Rule 34) | No — list every page |
| D.C. Circuit | No |
| 9th Circuit | Discouraged |
| Most other courts | Yes, at 5+ pages |

When in doubt, list all pages individually — it is never wrong to be specific.

### Step 4: Categorize

Assign each authority to exactly one category. Use these categories in this order:

1. **Cases** (always first, alphabetized by first party name)
2. **Administrative Decisions** (PTAB decisions, agency orders — alphabetized by first party name). Omit this category if none exist; some briefs fold these into Cases.
3. **Constitutional Provisions** (federal before state; amendments in numerical order)
4. **Statutes** (federal before state; by title and section number)
5. **Rules and Regulations** (federal rules, then C.F.R., then Fed. Reg.)
6. **Legislative Materials** (congressional records, committee reports, hearing transcripts, markup transcripts)
7. **Other Authorities** (law review articles, treatises, restatements, blog posts, industry reports, web sources — alphabetized by author/organization)

Omit categories with no entries.

### Step 5: Handle Edge Cases and Ambiguities

**Parenthetical citations:** Follow the **Parenthetical Handling** rules in `citation-toolkit`. For ToA purposes specifically: `(quoting X)` gets a page entry for X; `(citing X)`, `(discussing X)`, `(applying X)`, `(overruling X)` do not (flag `citing_parenthetical` as a judgment call per the shared vocabulary). `(holding [description])` is not a separate authority.

**Rule of thumb:** Ask "Is the *brief* invoking this authority, or is the brief just describing what *another case* did with this authority?" Only the former gets a TOA page entry.

**Subsequent history:** Include all subsequent history as part of the citation:
- `cert. denied`, `cert. granted`, `aff'd`, `rev'd`, `vacated`, `remanded`
- `modified by`, `supplemented by`, `clarified by`
- Example: `Force v. Facebook, Inc., 934 F.3d 53 (2d Cir. 2019), cert. denied, 140 S. Ct. 2761 (2020)`
- Example: `Hartford-Empire Co. v. United States, 323 U.S. 386 (1945), modified by 324 U.S. 570 (1945)`

**Multiple cases with same party names:** When the same parties appear in multiple cases (e.g., three different *Microsoft v. Motorola* decisions), each gets its own TOA entry. Short-form resolution must use the reporter volume/page to disambiguate — `Microsoft, 696 F.3d at 876` resolves to the specific case at 696 F.3d 872, not the others.

**S. Ct. reporter:** Treat `S. Ct.` citations identically to `U.S.` citations.

**String cites:** Each authority in a string cite gets its own entry.

**Signal prefixes** (`Cf.`, `contra`, `but see`, `see generally`, etc.): Extract the authority regardless of signal.

**Statute subsections:** When a brief cites `§§ 315(a), (d), and (e)`, default to listing each subsection separately. Flag for user if uncertain whether to consolidate.

## Output

### Structured Data (Primary)

Produce a JSON array. Each entry:

```json
{
  "citation": "Reed v. Town of Gilbert, 576 U.S. 155 (2015)",
  "category": "Cases",
  "pages": [1, 2],
  "short_forms_found": ["Id. at 163", "Reed, 576 U.S. at 163"],
  "flags": []
}
```

The `flags` array captures any ambiguities or issues for user review. Use the names defined in `citation-toolkit`'s **Flag Vocabulary** — for ToA, the relevant ones are `unresolved_short_form`, `ambiguous_section_reference`, `informal_reference`, `uncertain_category`, and `citing_parenthetical`.

### Formatted TOA (Secondary)

Produce a formatted Table of Authorities matching standard legal conventions:

```
TABLE OF AUTHORITIES

                              Page(s)

Cases

Ashcroft v. Free Speech Coalition,
  535 U.S. 234 (2002) ............................. 3

Barr v. American Association of
  Political Consultants, Inc.,
  591 U.S. 610 (2020) ............................. 1

Reed v. Town of Gilbert,
  576 U.S. 155 (2015) .......................... 1, 2

[etc.]

Constitutional Provisions

U.S. Const. amend. I .............................. 1

Statutes

47 U.S.C. § 230(c)(2) ............................ 5
47 U.S.C. § 230(f)(4) (2018) ..................... 3

[etc.]
```

**Formatting rules:**
- Case names in italics (use `*italic*` in markdown output, or instruct the user to italicize in their word processor)
- Indent continuation lines for long citations
- Right-align page numbers with dot leaders
- Page numbers comma-separated; use "passim" only if the court permits it (see passim rules in Step 3)
- Alphabetize within each category (cases by first party name; statutes by title/section; secondary sources by author last name)
- Omit pinpoint pages — use only starting page (e.g., `576 U.S. 155`, not `576 U.S. 155, 163`)
- Preserve treatise citation form including volume number — do NOT rearrange into last-name-first format
- Flag bare section references (e.g., "§ 230 was enacted to promote...") as `ambiguous_section_reference` for user review

## Verification Checklist

After generating the TOA, verify:

- [ ] Every citation in the brief (including parentheticals) has a TOA entry
- [ ] Every short form resolves to a full citation
- [ ] No duplicate page numbers for any entry
- [ ] Categories are in correct order
- [ ] Entries are alphabetized within categories
- [ ] Passim used only if the target court permits it; otherwise all pages listed individually
- [ ] Flags exist for any ambiguous resolutions
- [ ] No entries from excluded sections (existing TOA, table of contents)

## Common Mistakes

Quick-reference for errors not obvious from the steps above:

| Mistake | Fix |
|---------|-----|
| Short form on different page not linked | Short forms add the NEW page to the full citation's page list |
| Citation spanning page break gets one page | Record BOTH pages when the citation text itself straddles the break |
| Sentence wraps → citation credited to next page | The citation's page is where the citation *text* appears, not where the sentence continues |
| Id. resolved to wrong authority in sequence | Track last-cited precisely — when authorities appear in quick succession, Id. resolves to the very last one |

## Iterative Improvement

When you encounter a citation pattern not covered above, or when something is ambiguous:

1. Flag it in the structured output
2. Note the pattern for the user
3. Suggest whether the skill should be updated to handle it

This allows the skill to improve over time as new citation patterns are encountered.
