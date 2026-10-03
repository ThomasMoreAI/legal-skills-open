# Output template — Mode 1 (Consult)

Load this file only when emitting consult-mode output. Skill-procedure detail lives in `SKILL.md`; this file is the output skeleton.

**Provenance discipline:**
- Every Subcategory ID (e.g., `GOVERN 1.1`) and Action ID (e.g., `GV-1.2-001`) below is a **verbatim quote** from `references/core/` or `references/gai-profile/`. Do not invent or paraphrase.
- Any **applicability judgment** ("this risk applies here") is a model inference, not a NIST statement. Tag it inline with `[model judgment — verify against system specifics]` on first use.
- If you can't assess something without more user input, list it under "Open questions" rather than guessing.

---

```markdown
[WORK-PRODUCT HEADER — see SKILL.md "Output formatting"]

# AI RMF Consult — [System / question]

**System type:** [General AI / Generative AI / Mixed]
**Mode:** Consult
**Sources:** NIST AI 100-1 (Core) [+ NIST AI 600-1 (GenAI Profile) if applicable]

## Bottom line
[Two to four sentences. What does the framework say to do for this system? What's most load-bearing? Mark inferential claims inline: `[model judgment — verify against system specifics]`.]

## Applicable risks (GenAI Profile)
[Omit if non-GenAI. Otherwise: short table of the 12 risks that plausibly apply, with one-line justifications. The applicability call itself is model judgment; the risk *name* is verbatim NIST.]

| Risk (NIST verbatim) | Why it likely applies here `[model judgment — verify]` |
|---|---|
| Confabulation | Customer-facing summaries from an LLM — wrong info reaches users. |
| Data Privacy | Prompts may include user PII; training data unknown. |
| …  | … |

## Suggested actions
[The verbatim NIST text for the relevant Subcategories / actions, grouped by function. Verbatim only — do not summarize.]

### GOVERN
| Subcategory / Action | Statement (verbatim NIST) |
|---|---|
| **GOVERN 1.1** | Legal and regulatory requirements involving AI are understood, managed, and documented. |
| `GV-1.2-001` | Establish transparency policies and processes for documenting the origin and history of training data and generated data for GAI applications… |

### MAP
[…]

### MEASURE
[…]

### MANAGE
[…]

## Open questions
[2–4 things the framework can't answer without more input from the user. Be specific.]
- Who owns AI incident response at your org? (Needed for GOVERN 4.3 / MANAGE 4.1.)
- Do you have a vendor-AI review process for the foundation-model provider? (Needed for GOVERN 6.1.)

## Next steps
[2–4 concrete next steps the user can take from here. Pull from the Open questions above. Examples:]
- For a documented impact assessment of this system, re-run this skill in **assessment** mode.
- Capture the answers to the Open questions in your AI use-case registry or system documentation, then revisit the affected Subcategories.
- Surface this analysis to whoever owns AI policy / vendor review at your org.

---
*Source: NIST AI 100-1 (January 2023) and NIST AI 600-1 (July 2024). Subcategories and Suggested Actions are quoted verbatim. Applicability calls marked `[model judgment]` are inferences from the user's system description, not NIST statements. NIST guidance is non-binding — this output is research input for a human decision, not a substitute for counsel.*
```
