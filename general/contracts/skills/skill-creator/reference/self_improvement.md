# Self-Improvement Instruction Template

When a user opts into self-improvement (`self_improvement: true` in frontmatter), the skill includes a Self-Improvement section at the end of `SKILL.md` that instructs the model to ask for feedback after each use and propose updates.

## The standard template

Insert this section verbatim, with the only adjustment being the skill name (replacing `<skill-name>` with the actual name):

---

## Self-improvement

After producing the output, ask the user:

> "Is there anything you'd change about this output or the approach the skill took? If yes, tell me — I can update the skill itself so future runs reflect what you learned this time."

If the user provides feedback that constitutes a substantive change to how the skill should work — a new criterion to check, a missing edge case, a change to the output format, a refinement to the workflow — propose a specific edit to this skill's SKILL.md and ask the user to confirm before applying it.

Format proposed edits like this:

> **Proposed update to `<skill-name>` (v<current> → v<next>):**
>
> *Section affected:* [Workflow / Edge cases / Output / Inputs / etc.]
>
> *Change:*
> [Show the specific addition, deletion, or modification.]
>
> *Reason:*
> [One sentence on why, drawn from the user's feedback.]
>
> Apply this change? (yes / modify / no)

If the user says "yes," apply the edit and bump the skill's version (semver: patch for clarifications, minor for new behavior, major for breaking changes).

If the user says "modify," accept their refinement and re-propose.

If the user says "no" or doesn't respond to the proposal, do not apply the change. The skill is the user's; they decide what gets in.

If the feedback is purely cosmetic (a typo, a minor wording preference) — apply it without proposing first, and note the change briefly: *"Updated the output heading per your preference."*

If the feedback is substantive but the user says "yes" without reviewing — push back once: *"This will change how the skill behaves on every future run. Want to see the proposed edit first, or apply it directly?"* Then proceed based on the response.

---

## Versioning rules

- **Patch (1.0.0 → 1.0.1):** Typo fixes, wording clarifications that don't change behavior.
- **Minor (1.0.0 → 1.1.0):** Added criteria, new edge case handling, expanded output sections, new optional inputs.
- **Major (1.0.0 → 2.0.0):** Changed required inputs, changed output format, removed criteria, anything that breaks compatibility with prior outputs.

The skill's frontmatter `version` field tracks this. Self-improvement updates rewrite the frontmatter to reflect the new version.

## A note on overwriting

Self-improvement should never silently overwrite the skill. The skill is the user's intellectual property — their judgment encoded as text. Treat it that way. Always show the proposed change, always ask, always default to "no" on ambiguous responses.

## A note on scope

Self-improvement updates the skill's instructions, not its identity. Do not rename the skill, do not change its core purpose, do not narrow or expand its scope dramatically based on a single use. Those are decisions for the user to make deliberately, not drift via incremental updates.

If feedback suggests the user wants a fundamentally different skill — *"actually, I want this to also handle MSAs, not just NDAs"* — say so:

> "That sounds like it's beyond an update — it'd change what this skill is. I can either widen this skill to cover both NDAs and MSAs (and we'd want to revisit the workflow), or we can keep this one as-is and create a separate MSA skill alongside it. Which do you want?"

The user decides whether the skill grows or splits.
