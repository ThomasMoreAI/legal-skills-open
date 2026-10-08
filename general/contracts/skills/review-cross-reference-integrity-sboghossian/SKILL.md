---
name: review-cross-reference-integrity-sboghossian
title: Cross-Reference Integrity Check
description: Use when a drafter or reviewer needs to verify that all internal cross-references in a contract are correct — checking section references, defined term usage, schedule/exhibit references, and capitalized-term consistency. Critical pre-execution QC step that catches structural drafting errors which escape human review on long contracts. Pairs with definitions-consistency for a complete drafting QC pass.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-cross-reference-integrity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Cross-Reference Integrity Check

Systematic scan of a contract for broken or inconsistent internal cross-references — section references pointing to non-existent clauses, defined terms used before they are defined or never defined, and missing schedule/exhibit attachments. A single broken cross-reference in an executed contract can create significant ambiguity or unenforceability; this check is standard QC before any execution.

## When to use this

- Pre-execution review of any long-form contract (above ~15 pages; mandatory above 40 pages)
- After a significant redline or amendment that renumbered clauses
- Before sending a draft to the counterparty — catching your own errors first
- After assembling multiple component documents (recitals, operative clauses, schedules) that were drafted separately
- Pre-closing contract audit in an M&A transaction

## What this check covers

### 1. Broken section / clause references

Every instance of "Section X," "Clause X.Y," "Article X," or "(as defined in Clause Z)" is extracted and verified:

- The referenced section number must exist in the document
- The referenced section must contain the content implied by the referencing language ("see Section 4.2 for the termination procedure" — Section 4.2 must actually address termination)
- No "orphan" references remaining from a prior draft where section numbers have shifted

**Common cause**: a drafter renumbers sections during editing (e.g., adding a new Section 3.4 pushes old 3.4 to 3.5) but does not update all cross-references throughout the document.

### 2. Defined terms — defined but not used

Extract all defined terms from the Definitions section and from inline definitions throughout the document. For each:
- Is the term used at least once outside its definition?
- If not: flag as unused definition — may indicate the clause it served was deleted or that the term was accidentally left from a prior template

Unused definitions are a signal that a substantive clause may have been accidentally removed.

### 3. Defined terms — used but not defined

Extract all capitalized terms used in the operative body of the contract. For each:
- Is it defined in the Definitions section?
- Is it defined inline (e.g., "'Intellectual Property Rights' means...")?
- Is it a standard legal term of art that does not require definition?

Terms that are capitalized but not defined anywhere are a common source of disputes — courts may construe them with their ordinary meaning, which may differ from what the parties intended.

### 4. Defined terms used before defined

In long contracts, a term may be used in Clause 3 but not formally defined until Clause 12. This creates ambiguity for anyone reading the contract sequentially and may render the early usage technically undefined. Best practice: define terms at first use or consolidate all definitions at the front.

### 5. Dual definitions / conflicting definitions

The same term (or substantially the same concept) defined twice with different meanings — most commonly in contracts assembled from multiple precedent documents:
- "Affiliate" defined in the recitals as [definition A] and again in Clause 8.2 as [definition B]
- "Material" used as a defined term in one part, as an ordinary adjective elsewhere
- Different versions of the same concept: "Intellectual Property" vs "IP Rights" vs "Proprietary Rights" — are these the same or different?

### 6. Schedule / exhibit references with missing attachment

Every reference to a Schedule, Exhibit, Annex, or Appendix is extracted and cross-checked:
- Is the referenced schedule attached to the document?
- Is the schedule correctly numbered (Schedule 1 in the body, Annex 1 in the attachment — mismatch)?
- For blank/form schedules (e.g., "Form of Assignment attached as Exhibit A"), is the form present?

Missing schedules on an executed contract are a common source of post-closing disputes about what was agreed.

### 7. Forward references where backward intended

A backward reference points to something already stated ("as defined above" / "the terms set out in Clause 3"). A forward reference points to something not yet stated ("as further described in Clause 15"). When a forward reference is used but should have been backward (e.g., after a draft reordering), the reference becomes nonsensical.

### 8. Capitalized terms not in definitions section

All capitalized terms in the contract that do not appear in the definitions section and are not standard legal/contractual terms of art should be flagged for review. Capitalization implies defined-term status; if the term is not defined, the capitalization misleads readers.

## Output structure

```json
{
  "issues": [
    {
      "location": "Clause 8.3(b)",
      "type": "broken-section-reference | undefined-term | unused-definition | double-definition | missing-schedule | forward-ref-error | undefined-capitalized-term",
      "description": "Cross-reference to 'Section 12.2' but Section 12.2 does not exist. Section 12 ends at 12.1.",
      "suggestedFix": "Update reference to 'Section 12.1' or add Section 12.2 as intended",
      "severity": "critical | material | minor"
    }
  ],
  "allCrossRefs": [
    { "location": "Clause 5.1", "referencedSection": "3.4", "exists": true }
  ],
  "unusedDefinitions": ["list of defined terms not used in the operative text"],
  "undefinedCapitalizedTerms": ["list of capitalized terms with no definition"],
  "missingSchedules": ["list of schedule references with no attached document"],
  "summary": {
    "totalIssues": number,
    "critical": number,
    "material": number,
    "minor": number
  }
}
```

## Severity classification

| Severity | Definition | Examples |
|----------|-----------|----------|
| **Critical** | Creates genuine ambiguity about what the parties agreed to, or makes a clause unenforceable | Undefined term used in a key operative clause; missing schedule containing essential terms |
| **Material** | Likely to be raised in a dispute or noticed by the counterparty's counsel | Broken cross-reference in a payment or termination clause; unused definition suggesting a deleted clause |
| **Minor** | Unlikely to affect interpretation but should be cleaned up for professionalism | Unused boilerplate definition; minor formatting inconsistency in capitalization |

## Sequence of QC checks

This check should be run in sequence with [[review-definitions-consistency]], which addresses how terms are used (consistency of meaning, singular/plural, etc.) rather than whether they are defined at all. Together they form a complete drafting QC pass:

1. [[review-cross-reference-integrity]] — structural integrity (does everything point to the right place?)
2. [[review-definitions-consistency]] — semantic integrity (are terms used consistently with their definitions?)

Both checks should be completed before any pre-execution review or final markup.

## When to escalate to human review

- If more than 5 critical issues are found, the contract has significant structural problems that may require a re-draft, not just a fix list
- If a missing schedule contains terms that are central to the deal (price, scope of services, IP assignment), the contract cannot be executed until the schedule is attached
- If a double definition involves a key commercial term (Affiliate, Intellectual Property, Confidential Information), legal counsel must determine which definition governs before the contract proceeds

## Related skills

- [[review-definitions-consistency]]
- [[review-contract-redline]]
- [[review-missing-clauses]]
