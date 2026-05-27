---
name: bates-citation-verification
title: Bates Citation and Verification
description: Citation format and verification protocol for legal documents that draw on Bates-stamped source records. Defines the bracket citation format, multi-source citation rules, quotation handling, the verification pass that runs before output, and the [UNVERIFIED] flag protocol. Use this skill any time another skill produces a legal work product that cites Bates-stamped pages, including medical chronologies, deposition summaries, demand letters, case briefs, and discovery responses. Also use any time the user asks how to format a citation or verify that a claim is supported by the source.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bates-citation-verification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [litigation, analysis, research]
---

# Bates Citation and Verification

Defines how to cite Bates-stamped source records and how to verify those citations before delivering the work product. This skill is consumed by other skills (medical chronology, deposition summary, demand letters, case briefs) so they share a single citation discipline.

The skill is built for case.dev style retrieval where source records have been ingested with Bates range metadata. Other environments are addressed at the bottom.

## Citation Format

Place citations in square brackets at the end of the sentence or bullet they support. No spaces inside the brackets.

### Single page

```
Patient reported neck pain rated 8/10. [SMITH00145]
```

### Page range

For a fact that spans contiguous pages, use a range with a hyphen:

```
The MRI report concluded multilevel degenerative changes superimposed on
acute L4-L5 disc herniation. [SMITH00203-00207]
```

### Multiple non-contiguous citations

For a single fact supported by multiple non-contiguous Bates locations, comma-separate inside one bracket:

```
The patient reported the same mechanism of injury to four separate providers.
[SMITH00145, SMITH00302, SMITH00489, SMITH00611]
```

### Citing across producing parties

When multiple parties have produced records with different Bates prefixes, always include the prefix even when context makes it obvious. Prefixes change between productions.

```
Plaintiff reported full recovery to her primary care physician [SMITH00422]
but reported continued severe pain to her treating orthopedist three days later.
[JONES_RECORDS00188]
```

## Quotations

Direct quotations must be in quotation marks with citation. Do not paraphrase quoted material that you have rendered as a quotation.

```
Dr. Chen wrote, "Within a reasonable degree of medical probability, the
patient's L4-L5 herniation is causally related to the motor vehicle collision
of March 8, 2024." [SMITH00892]
```

The quote must match the source verbatim. Punctuation, capitalization, and word choice all carry weight in legal writing. Do not "clean up" quoted material. If the source has a typo, quote it with `[sic]`.

If a passage needs to be shortened, use ellipses for omitted material. Do not omit content that changes the meaning.

```
Dr. Chen wrote, "Within a reasonable degree of medical probability, the
patient's L4-L5 herniation is causally related to the motor vehicle collision...
based on the temporal relationship between the incident and onset of symptoms,
the mechanism of injury, and the absence of documented prior lumbar complaints."
[SMITH00892]
```

## The Three Categories

Every claim in the work product falls into one of three categories.

### Verified

The claim is supported by retrieved source content that has been re-checked. Cite the Bates range and include the claim normally.

### Unverified

The claim appears in the records but the specific page cannot be retrieved at the time of preparation. Common reasons:

- Source chunk was retrieved during initial drafting but cannot be re-retrieved during the verification pass (RAG flakiness)
- The claim is a high-level summary that aggregates content across many pages and no single citation suffices
- The records reference an external document (radiology report, lab result) that was not produced

Include the claim and append the flag inline:

```
Patient was hospitalized for three days following the incident.
[UNVERIFIED - claim appears in records but specific page not retrievable]
```

Do not drop unverified claims. Removing the claim hides information from the attorney; flagging it surfaces a follow-up item.

### Contradicted

The retrieved source contradicts the claim. Remove the claim from the work product. If the contradiction is itself useful (impeachment material, inconsistent histories), surface it in the Strategic Analysis or equivalent section with both citations.

## Never Fabricate

Never invent a Bates range. If a fact cannot be tied to a specific page, mark it `[UNVERIFIED]`. Inventing citations is the fastest way to make the attorney sanctionable. This is the single most important rule in this skill.

If you find yourself constructing a Bates range that "should" exist (e.g., "if the chronology spans page 145, then this claim is probably on page 146"), stop and use `[UNVERIFIED]` instead.

## The Verification Pass

Before delivering the work product, run a verification pass. This pass is mandatory, not optional.

### Step 1: Prefix and format preflight

Extract the canonical Bates prefix(es) and citation format from production header pages or the first page of each produced record set. Record the prefix, spacing, digit count, and range. Any citation whose prefix, spacing, or digit pattern does not match is not verified; correct it if the source page proves the right citation, otherwise mark the claim `[UNVERIFIED]`.

### Step 2: Inventory the citations

Extract every citation from the draft work product. For each, you should have:

- The claim it supports (the sentence or bullet ending in the citation)
- The Bates range cited
- Whether the claim contains a direct quotation

### Step 3: Page-level extraction and matching

For each cited claim, verify with independent page-level PDF OCR/text-layer extraction from the cited Bates page. Vault search may find candidate support during drafting, but vault-search-only support is non-final and must be marked `[UNVERIFIED]` unless page-level extraction confirms it.

For each citation, verify:

1. The cited Bates range exists in the production
2. The Bates prefix matches the canonical prefix and format
3. The literal page text supports the claim verbatim or by clear paraphrase
4. For quotations, the quoted text appears verbatim in the source
5. The source date on the page, if visible, is consistent with the encounter or claim date

### Step 4: Categorize and act

Based on the re-check, each citation falls into one of these outcomes:

| Outcome | Action |
|---------|--------|
| Page-level extraction verified, claim supported | No change |
| Citation verified, claim partially supported | Narrow the claim to what the source supports |
| Citation verified but content does not support the claim | Remove the claim or change the citation |
| Citation is supported only by vault search | Mark `[UNVERIFIED]` or rerun page-level extraction |
| Citation cannot be page-verified | Mark `[UNVERIFIED]` |
| Quoted text differs from source | Correct the quote to match the source verbatim |
| Bates range or prefix does not exist in production | Remove the citation, mark `[UNVERIFIED]`, log as a finding |

### Step 5: Spot check sample

After the systematic pass, randomly select 5 percent of claims (minimum 5, maximum 20) and have a second pass of retrieval done. This catches cases where the first verification pass had a systematic error.

### Step 6: Log the verification

Add an auditable verification log. Each row must include citation, claim, retrieval method, Bates page, source date if visible, supporting excerpt, result, and corrective action. Also add a count summary to the methodology section:

```
Citation verification: [N] total citations, [N] independently page-verified,
[N] vault-search-only, [N] spot-checked, [N] flagged UNVERIFIED, [N] corrected
or removed. Verification completed [date].
```

The numbers tell the attorney how confident to be. A chronology with 200 verified citations and zero flags is suspicious (no one bats 1.000 against real records). A chronology with 200 claims and 50 UNVERIFIED flags suggests retrieval was unreliable and the attorney should rerun.

## Verification Examples

### Example 1: Citation verified

Draft:
```
Patient was diagnosed with C5-C6 disc herniation. [SMITH00203]
```

Verification: Re-retrieve SMITH00203. Source contains MRI report with impression "C5-C6 disc herniation with left foraminal narrowing."

Action: Verified. No change.

### Example 2: Claim partially supported

Draft:
```
Patient was diagnosed with severe C5-C6 disc herniation requiring surgery. [SMITH00203]
```

Verification: Source mentions C5-C6 disc herniation but says nothing about severity or surgery.

Action: Narrow the claim:
```
Patient was diagnosed with C5-C6 disc herniation. [SMITH00203]
```

The "severity" and "surgery" elements either need their own citation or need to be removed.

### Example 3: Quoted text differs

Draft:
```
Dr. Chen opined that the herniation was "directly caused by the collision." [SMITH00892]
```

Verification: Source actually says "causally related to the motor vehicle collision."

Action: Correct the quote:
```
Dr. Chen opined that the herniation was "causally related to the motor vehicle
collision." [SMITH00892]
```

This matters. "Directly caused" and "causally related" mean different things in tort law.

### Example 4: Bates range does not exist

Draft:
```
Patient reported headaches at the ER visit. [SMITH00050]
```

Verification: SMITH production runs SMITH00001 through SMITH00047. SMITH00050 does not exist.

Action: Mark UNVERIFIED and log:
```
Patient reported headaches at the ER visit. [UNVERIFIED - original citation
SMITH00050 not present in production]
```

This is also a finding for Strategic Analysis: production may be missing pages.

## Operating Environments

### Bates-stamped RAG (case.dev native)

Default. All examples above assume this environment.

### Local PDF files without Bates stamps

Use file name plus page number in the same bracket format:

```
Patient reported neck pain. [smith_records.pdf p.45]
```

State the citation scheme in the document header. Verification pass logic is identical; "re-retrieve" means open the PDF to the cited page.

### Mixed Bates and non-Bates sources

Be consistent within a section. Prefer Bates where available. If both must coexist, the methodology section must explain the convention.

### No source access (degraded mode)

If the work product is being produced from records summarized in context only, mark the entire output `[CITATION UNAVAILABLE - produced from in-context summary only]` at the top. The verification pass cannot run. Recommend the attorney rerun against full records.

## Troubleshooting

- **Bates range is missing from the production**: Remove the invented range, mark the claim `[UNVERIFIED]`, and log the missing page range as a production gap.
- **Quotation does not match the source**: Correct the quote verbatim or convert it to a paraphrase with citation; never preserve cleaned-up quote text.
- **Retrieval is flaky across passes**: Keep the claim only if it appeared in records, mark it `[UNVERIFIED]`, and note the retrieval instability in methodology.
- **Multiple sources support one claim**: Use one bracket with comma-separated Bates locations rather than repeating the same sentence.
