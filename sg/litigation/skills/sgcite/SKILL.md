---
name: sgcite
title: sgcite — Singapore Court Citation Checker
description: Use when verifying Singapore court citations in legal submissions, checking for hallucinated cases in AI-generated text, or validating citations against eLitigation.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/sgcite
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: sg
practice: litigation
language: en
tags: [citation, singapore, legal-research, hallucination-detection, elitigation]
---

# sgcite — Singapore Court Citation Checker

## When to Use

- Reviewing legal submissions before filing
- Checking AI-generated legal text for hallucinated citations
- Verifying that cited Singapore cases actually exist in eLitigation
- Detecting fabricated case names, paragraph references, or distorted quotations
- Routine citation audit for Singapore law documents

## How It Works

### Input

A legal text (submission, memo, brief, AI-generated draft) containing Singapore court citations.

### Process

1. **Extract** — Parse all case citations from the text
2. **Validate** — Query eLitigation (Singapore's case law database) for each citation
3. **Check** — Detect:
   - Hallucinated authorities (case doesn't exist)
   - Mismatched case names (case exists but different party names)
   - Fabricated paragraph references
   - Distorted quotations
4. **Report** — Flag each issue with specific location and explanation

### Output

```
✓ 5 citations verified
✗ 2 issues found:
  - [Para 23] "ABC v DEF [2023] SGHC 45" — Case not found in eLitigation
  - [Para 41] Quotation distorted — actual text differs from cited passage
```

## Example

```bash
npx sgcite check ./my-submission.docx
```

Or import as a library in your legal workflow tools.

## Audience and Work Shape

Audience: Singapore-qualified lawyers, paralegals, and litigation-support teams running a pre-filing or pre-circulation citation check. Not for unsupervised drafting or non-lawyer use.

Work shape: Pattern-Matched Review. Each citation is checked against a known reference (eLitigation). Output is a list of findings, not a sign-off.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. A `verified` result means "the cited case was found in eLitigation with matching party names" — not "this citation is correctly used in your submission" and not "this submission is fit to file."

**Privilege and confidentiality.** sgcite sends extracted citation text (and quoted passages, when checking for distorted quotations) to eLitigation. Do not invoke on privileged or unfiled draft material unless your firm has assessed that routing the cited extracts through a public case-law database is acceptable. Configure the tool to send citation strings only (not surrounding context) where possible.

**Accountability.** A qualified lawyer must review each flagged and each `verified` citation before filing or circulating the submission. The skill does not sign off on accuracy of use, substantive correctness, or fitness to file.

## Confidence Bands

- **High** — citation extracted cleanly, eLitigation returns an exact match on case name and citation reference.
- **Medium** — citation matched on case name or reference but with a fuzzy hit, neutral citation variant, or paragraph reference not present in the source. Flag for lawyer review.
- **Low / Review** — possible distorted quotation, ambiguous case name, non-SG citation in input, or eLitigation lookup failed. Do not present as `verified`; route to REVIEW.

## Out of Scope

- Does not check substantive accuracy of cited holdings or whether the citation supports the proposition advanced.
- Does not cover non-Singapore citations or unreported decisions outside eLitigation.
- Does not constitute citation-review or quality-control sign-off for purposes of professional rules.
- Does not handle PDPA, privilege, or confidentiality-by-design — the user controls what text is passed in.

## Escalation

Stop and route to the responsible lawyer when:
- a citation cannot be resolved with High confidence after one pass;
- quoted text in the submission differs materially from the eLitigation source;
- the input appears to contain non-SG citations (treat as unsupported by this skill);
- the input contains material that may be privileged and the firm has not approved external lookups.

## Limitations

- Only covers Singapore court decisions in eLitigation
- Does not verify substantive accuracy of cited holdings
- Some unreported decisions may not be available
