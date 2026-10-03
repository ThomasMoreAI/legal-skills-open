# Output template — Mode 3 (Assessment)

Load this file only when emitting impact-assessment output. Skill-procedure detail lives in `SKILL.md`; this file is the output skeleton.

**Provenance discipline (most important in this mode — assessments are referenced later by readers who weren't in the conversation):**

- Every Subcategory ID (e.g., `GOVERN 1.1`) and Action ID (e.g., `GV-1.2-001`) below is a **verbatim quote** from `references/core/` or `references/gai-profile/`. Do not invent or paraphrase.
- Every "assessment paragraph" under a Subcategory is a **model finding**, not NIST text. The Subcategory statement is verbatim; the paragraph evaluating the system against it is model-authored. Make the boundary explicit by italicizing each assessment paragraph and prefixing with *Assessment:* or by tagging `[model assessment — verify against system documentation]`.
- The recommendation (Deploy / Deploy with conditions / Do not deploy) is **model judgment** with a high stakes. Tag with `[model recommendation — owner must independently verify]` and make conditions point to specific Subcategories so they're auditable.
- If you lack input to assess a Subcategory, write "Insufficient input — see Open items" rather than guessing.

---

```markdown
[WORK-PRODUCT HEADER — see SKILL.md "Output formatting"]

# AI RMF Impact Assessment — [System name]

**Prepared:** [date] | **Status:** DRAFT
**System type:** [General AI / Generative AI / Mixed]
**Mode:** Full assessment
**Sources:** NIST AI 100-1 + NIST AI 600-1 [drop 600-1 if non-GenAI]

## Executive summary
[Two paragraphs. What the system is, what NIST flags, the recommendation. Mark the recommendation `[model recommendation — owner must independently verify]`.]

## System description
[What the system does. Inputs, outputs, decision authority, users affected, deployment context. Half a page. Pull from user input; do not invent details — flag missing facts as Open items.]

## MAP — Context
[Pull the applicable MAP Subcategories. For each: verbatim statement + one-paragraph assessment of this system.]

### MAP 1.1 — [verbatim NIST statement]
*Assessment `[model assessment — verify against system documentation]`:* [Assessment paragraph.]

[Repeat for each applicable Subcategory.]

[If GenAI:]
### GAI risks identified (from NIST AI 600-1 §2)
[Risk-by-risk: does it apply here? Why? Risk names are verbatim NIST; applicability is `[model judgment]`.]

## MEASURE — Evaluation
[Same pattern. Pull MEASURE Subcategories + GAI Profile Actions for the system's risks.]

## MANAGE — Response and monitoring
[Same pattern. MANAGE Subcategories + GAI Profile Actions covering incident response, monitoring, decommissioning.]

## GOVERN — Policy and accountability touchpoints
[Same pattern. Which GOVERN Subcategories apply to this system, given the org's policy.]

## Trustworthy AI characteristic check
[Brief — one or two sentences per characteristic on whether the system supports or risks it. Characteristic names verbatim; the support/risk call is `[model judgment]`.]

## Recommendation `[model recommendation — owner must independently verify]`
[Deploy / Deploy with conditions / Do not deploy.]

**Conditions** (if any) — each must cite a specific Subcategory so it is auditable:
- Address `MEASURE 2.7` — security & resilience evaluation — before production deployment. (Specifically: complete penetration testing of the prompt boundary.)
- Document the AI policy commitments per `GOVERN 1.2`.

## Open items / questions for the system owner
[Things you couldn't assess without more input. Be specific about what input would close each item.]

## Cite check
[List every Subcategory and Action ID cited above. Sanity check: every citation must resolve to a real line in `references/`. If any cited ID is not in `references/`, that's a bug — remove or correct before delivery.]

---
*Source: NIST AI 100-1 (January 2023) and NIST AI 600-1 (July 2024). Subcategories and Suggested Actions are quoted verbatim. All "Assessment" paragraphs, applicability calls, and the final Recommendation are model judgments produced from the user's system description, not NIST statements. NIST guidance is non-binding. This assessment is research input for a documented organizational decision — not a substitute for counsel.*
```
