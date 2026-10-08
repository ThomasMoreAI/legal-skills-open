---
name: review-definitions-consistency-sboghossian
title: Definitions Consistency Check
description: Use when a drafter or reviewer needs to verify that all defined terms in a contract are used consistently with their definitions — checking for term drift, singular/plural mismatches, inline contradictions, buried central concepts, and capitalization inconsistencies. Pairs with cross-reference-integrity for a complete drafting QC pass on any long-form commercial contract.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/review/review-definitions-consistency
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Definitions Consistency Check

Systematic review of a contract's defined terms — verifying that each term is used consistently with its definition throughout the document, that capitalization is uniform, and that central concepts are properly defined rather than buried in operative clauses. A definitions problem is invisible to a quick read but creates significant interpretive risk if a dispute arises.

## When to use this

- Pre-execution QC on any long-form contract (recommended above 10 pages; essential above 30 pages)
- After assembling a contract from multiple precedent documents (templates from different origins often bring inconsistent definitions)
- When reviewing a counterparty draft for negotiating purposes
- Post-amendment review — amendments often introduce new defined terms that conflict with existing ones
- As part of due diligence reviewing a target's standard form contracts

## What this check covers

### 1. Used consistently throughout

For each defined term, every instance of its use in the operative clauses must:
- Be consistent with the definition — no narrowing, broadening, or recharacterizing the defined concept in context
- Be recognized as the defined term (capitalized or formatted consistently)
- Not be used in a sense that contradicts the definition

**Example of a consistency problem**: "Confidential Information" is defined to include all technical and commercial information. Clause 9.4 says "excluding general Confidential Information that is publicly available" — the definition already excludes public information, so this clause creates a redundancy that could be read as suggesting Confidential Information includes some public information.

### 2. Definition not contradicted by inline use

An inline clause may effectively narrow or expand a definition without updating the defined term:
- "The Company (which for the purposes of this Clause means only the UAE entity)" — this creates a contextual sub-definition that overrides the main definition for one clause, creating confusion about which definition applies elsewhere.
- Flag every instance where a parenthetical or qualifier effectively changes the defined meaning.

### 3. Singular / plural matching

Contracts use defined terms in both singular and plural forms. The definitions section typically defines the singular ("'Agreement' means..."). Check:
- Is plural usage clearly intended to refer to the defined concept ("the Agreements" may be intended to mean "copies of the Agreement" or "multiple agreements")?
- Does the contract include a standard interpretation clause stating that "words importing the singular include the plural and vice versa"? If it does, singular/plural usage is generally not an issue. If not, flag ambiguous plural uses.

### 4. Definition not buried in clause body when central concept

A term that is central to the contract's operation — e.g., what constitutes a "Material Adverse Effect," what "Intellectual Property" includes, who is an "Affiliate" — should be in the definitions section, not defined for the first time deep in an operative clause. A definition buried in Clause 11.3 is:
- Easy to miss in negotiation
- Harder to locate when the contract is relied upon post-closing
- A signal that it may have been inserted without full consideration of cross-contract implications

**Best practice**: All substantive defined terms belong in a consolidated definitions section (Article 1 or a separate Schedule of Definitions). Inline definitions should be limited to terms used only within that specific clause.

### 5. Defined terms in CAPS or Title Case consistently

Most long-form contracts use one of two conventions for indicating a word is a defined term:
- **Initial Capital** (Title Case): "The term 'Agreement' means..." — all defined terms capitalized throughout
- **ALL CAPS**: less common; used in some civil-law influenced contracts

The check: is the convention applied uniformly? If "Intellectual Property" is defined and used as a defined term, is it capitalized every time? If the same word appears uncapitalized ("intellectual property that..."), is that intentional (referring to the generic concept) or an error?

**Flag all instances where a word that matches a defined term is used uncapitalized** — these may be either intentional (the generic concept applies, not the defined one) or errors (the drafter forgot to capitalize). Both require review.

### 6. "Include" vs "including, without limitation" usage

"Including" in a legal context can mean either:
- **Exhaustive**: the list that follows is exhaustive (civil law default interpretation in some jurisdictions)
- **Non-exhaustive**: the list is by way of example, not limitation (common law default)

The standard common law drafting fix is "including, without limitation" or "including but not limited to" to make clear the list is not exhaustive. Check:
- Are some "including" clauses qualified as "without limitation" while others are not? If inconsistent, it may suggest the unqualified ones are intended to be exhaustive — which may or may not be intended.
- Are civil-law jurisdictions involved? In French law or Lebanese law, the default may differ; the contract should be explicit.

### 7. Circular definitions

A circular definition defines a term by reference to another term that itself includes the first term:
- "'Affiliate' includes any entity that Controls or is Controlled by the Company, where 'Control' means ownership of more than 50% of the entity by an Affiliate."

This is either tautological (no practical meaning) or ambiguous. Flag and recommend a non-circular restatement.

### 8. Over-broad or over-narrow definitions

Compare each definition to market standard:
- **Over-broad**: "Intellectual Property means all works, inventions, know-how, data, and any other information however arising" — so broad as to potentially encompass things neither party intended (e.g., personal data; pre-existing IP).
- **Over-narrow**: "Confidential Information means only written information marked 'Confidential'" — excludes oral disclosures and unmarked written information; likely under-protects in practice.

Flag significant divergences from market standard definitions with a recommendation.

## Output structure

```json
{
  "findings": [
    {
      "term": "Intellectual Property",
      "definition": {
        "location": "Article 1 Definitions",
        "text": "means all patents, trademarks, copyrights, trade secrets, and know-how"
      },
      "inconsistencies": [
        {
          "location": "Clause 8.3",
          "excerpt": "...including all intellectual property (whether or not registered)...",
          "issue": "Term used uncapitalized; unclear whether this refers to the defined term or generic IP concept. If defined term, 'registered' qualifier is already within scope; if generic, scope may differ.",
          "severity": "material"
        }
      ]
    }
  ],
  "suggestedDefinitions": [
    {
      "term": "Material Adverse Effect",
      "issue": "Used 7 times in the operative clauses but not defined. Recommend adding a definition.",
      "suggestedText": "[Standard MAE definition language — to be tailored]"
    }
  ],
  "capitalizationInconsistencies": [
    { "term": "affiliate", "locations": ["Clause 4.2", "Clause 9.1"], "issue": "Used uncapitalized in these clauses; appears as defined term 'Affiliate' elsewhere" }
  ],
  "summary": {
    "totalFindingsCount": number,
    "critical": number,
    "material": number,
    "minor": number
  }
}
```

## Severity classification

| Severity | Definition |
|----------|-----------|
| **Critical** | The inconsistency creates a materially different legal outcome depending on interpretation; likely to be raised in a dispute |
| **Material** | Would be raised in careful negotiation or by experienced counterparty's counsel; creates interpretive risk |
| **Minor** | Cosmetic inconsistency; unlikely to affect interpretation but should be corrected for professionalism |

## Pairing with cross-reference integrity

This check tests *meaning* consistency. [[review-cross-reference-integrity]] tests *structural* integrity (references pointing to correct locations). Run both checks together:

1. First [[review-cross-reference-integrity]] — confirms the document's internal structure is sound
2. Then [[review-definitions-consistency]] — confirms defined terms are semantically consistent

Together they constitute a complete drafting QC pass before execution.

## Common definitions requiring special attention

These terms recur across most commercial contracts and are frequent sources of inconsistency:

| Term | Common issues |
|------|--------------|
| **Affiliate** | Circular definition; too broad (includes all subsidiaries); too narrow (excludes sister companies); jurisdiction-specific issues (UAE definitions of "control") |
| **Confidential Information** | Failure to include oral disclosures; failure to exclude public domain; too broad (catches public regulatory filings) |
| **Intellectual Property** | Pre-existing IP vs created IP confusion; failure to specify whether "rights in" vs "the IP itself" is assigned |
| **Material Adverse Effect / MAC** | Often undefined; when defined, the carve-outs determine the real scope |
| **Change of Control** | Definition of "control" — ownership % threshold varies (50.1%? majority board seats?) |
| **Business Day** | Which jurisdiction's business days? Important for Dubai (Fri-Sat weekend) vs UK (Sat-Sun weekend) vs US |

## Related skills

- [[review-cross-reference-integrity]]
- [[review-contract-redline]]
- [[review-missing-clauses]]
