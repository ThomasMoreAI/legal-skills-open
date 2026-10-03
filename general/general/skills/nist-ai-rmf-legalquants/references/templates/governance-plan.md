# Output template — Mode 2 (Governance plan)

Load this file only when emitting governance-plan output. Skill-procedure detail lives in `SKILL.md`; this file is the output skeleton.

**Provenance discipline:**
- Every Subcategory ID (e.g., `GOVERN 1.1`) and Action ID (e.g., `GV-1.2-001`) below is a **verbatim quote** from `references/core/` or `references/gai-profile/`. Do not invent or paraphrase.
- "In practice" annotations are **model-authored operational glosses**, not NIST text. Tag the first instance with `[operational gloss — not NIST verbatim]` and italicize as shown.
- Role-ownership recommendations and review-frequency suggestions are model judgment; mark with `[model judgment — adjust to your org]`.

---

```markdown
[WORK-PRODUCT HEADER — see SKILL.md "Output formatting"]

# AI RMF Governance Plan — [Org / scope]

**Mode:** Governance plan
**Scope:** [What's in scope — e.g., "All AI/ML systems," "Customer-facing GenAI only"]
**Sources:** NIST AI 100-1 (Core) [+ NIST AI 600-1 (GenAI Profile) if generative scope]

## Plan summary
[Three to five bullets: what the plan does, how it's organized, where it lives operationally. Verbatim NIST anchors plus the org-specific overlay; mark org-specific recommendations `[model judgment]`.]

## Trustworthy AI commitments
[The seven characteristics, with one line each on what the org's policy commits to. Verbatim NIST definitions in `core/trustworthy-characteristics.md` are the anchor.]

## GOVERN — Policies, accountability, oversight
[For each Category GOVERN 1–6, a section with:]
### GOVERN N — [Category title — verbatim NIST]
**Subcategories to address:**
- **GOVERN N.X** — [verbatim NIST statement]. *In practice: [one-line operational annotation — model gloss, not NIST verbatim].*
- …

**GAI-specific actions (if generative scope):**
- `GV-N.X-NNN` — [verbatim NIST action text].

## MAP / MEASURE / MANAGE governance touchpoints
[Selected Subcategories from other functions that the governance program owns — typically risk tolerance setting (MAP 1.5), TEVV scope (MEASURE 1.1), incident response (MANAGE 4.1), third-party (MAP 4.1 / MANAGE 3.1).]

## Roles and accountability matrix `[model judgment — adjust to your org]`
[Suggested. The framework calls for clarity on who owns what. Propose a roles table — owner, accountable, consulted, informed — for each Subcategory the plan adopts. The role names and assignments are model recommendations to be reviewed against the org's actual structure.]

## Open questions
[Things the framework doesn't decide for you: risk tolerance thresholds, governance committee composition, escalation criteria, review frequency.]

## Next steps
[2–4 concrete next steps. Examples:]
- Walk this plan through your AI governance committee (or equivalent) for ratification.
- Run a Mode 3 assessment against your highest-risk current AI system to test the plan's coverage.
- Set a review cadence (annual at minimum; sooner if NIST publishes a revision or a new Profile).

---
*Source: NIST AI 100-1 (January 2023) and NIST AI 600-1 (July 2024). Subcategories and Suggested Actions are quoted verbatim from the framework. "In practice" annotations and role-ownership matrices are operational glosses produced by the skill, not NIST statements. NIST guidance is non-binding.*
```
