# Acceptance Test Plan — Enhance Prompt v1.0.0

## Skill summary

Front-running agent that rewrites a user's short natural-language prompt into a structured legal prompt before submission. Adds role, jurisdiction, audience, scope, output format, constraints, and citation expectations. Shows the user the expansion before submission, allowing edit-and-submit, submit-as-is, or skip-to-original.

## Test corpus requirements

This skill's test "corpus" is a set of 15–20 prompts of varying quality, covering:

- **At least 4 short-and-vague prompts** ("review this contract", "is this NDA okay", "summarize this") — the canonical use case.
- **At least 3 already-structured prompts** that don't need much enhancement.
- **At least 3 prompts that mix multiple tasks** ("review this NDA and rewrite the indemnification clause") — testing how the skill handles task-decomposition.
- **At least 2 prompts that are out of scope** for legal AI (e.g., "what's the weather", "schedule a meeting") — testing refusal.
- **At least 2 prompts that imply legal advice** ("should I sign this", "is this enforceable") — testing how the skill scopes inputs that imply outcome predictions.
- **At least 2 prompts referencing a specific skill** ("apply NDA Review to this", "use the SaaS playbook on this") — testing how Enhance Prompt interacts with attached skills.

The prompt set is documented as `test-corpus/enhance-prompt/test-prompts.md`.

## Test scenarios

### Scenario 1: Short-and-vague prompt enhancement

**Inputs:** A vague natural-language prompt: "review this NDA".

**Expected output structure:**
- The expanded prompt is more specific: it adds role (in-house counsel), jurisdiction (where the document indicates or US default), audience (executive / business stakeholder if not specified), scope (review for unusual provisions, perspective-calibrated), output format (structured report with severity tags and citations), citation expectations.
- The expansion is shown to the user as an editable preview before submission.
- The user can edit the expansion, submit as-is, or skip to original.

**Expected calibration:**
- The expansion preserves the user's underlying intent.
- The expansion does not invent intent the user did not signal.
- The expansion is operationally useful — running the expanded prompt produces a meaningfully better result than running the original.
- The expansion includes a "if any of these defaults are wrong, please correct" affordance.

**Edge cases to verify:**
- The skill does not add a perspective input where the user has not signaled which side of the deal they are on.
- The skill does not invent jurisdiction where neither the prompt nor the document indicates one.
- The skill does add common defaults (e.g., "review for unusual provisions" if the user says "review") that match the typical user intent.

**Pass criteria:**
- Structural pass: Expansion is shown; format is consistent.
- Calibration pass: Reviewing attorney confirms the expansion preserves intent and adds operationally-useful structure.

### Scenario 2: Already-structured prompt

**Inputs:** A well-formed prompt: "Apply the NDA Review skill to this attached NDA from a recipient perspective; flag any provisions that depart from market standard for a vendor evaluation context; produce a markdown report with severity tags."

**Expected output structure:** The expansion is minimal or null; the user is told the prompt is already well-structured and is offered the option to submit as-is.

**Expected calibration:**
- The skill recognizes that the prompt is already structured.
- The skill does not add unnecessary expansions.
- If the expansion is null, the skill says so explicitly.

**Edge cases to verify:**
- The skill does not over-expand a prompt that is already specific.
- If small additions could improve the prompt (e.g., adding "and provide recommended language for any flagged provisions"), the skill suggests them as optional rather than imposing them.

**Pass criteria:** Skill respects the user's already-clear input.

### Scenario 3: Multi-task prompt

**Inputs:** "Review this NDA and rewrite the indemnification clause to make it more favorable to the recipient."

**Expected output structure:** The expansion identifies the multi-task structure (review → rewrite) and either:
(a) Presents the prompt as a sequence of two tasks (review, then targeted rewrite), or
(b) Asks the user to clarify which task is primary.

**Expected calibration:**
- The skill does not silently collapse the two tasks into one.
- The skill handles task-decomposition coherently.

**Edge cases to verify:**
- If the two tasks would naturally chain (review surfaces issues; rewrite addresses one of them), the skill makes the chaining explicit.
- If the two tasks conflict (review against market standards vs. rewrite to favor one side), the skill flags the conflict.

**Pass criteria:** Skill handles multi-task input transparently.

### Scenario 4: Out-of-scope prompt

**Inputs:** "What's the weather today?"

**Expected behavior:**
- The skill identifies that the prompt is not a legal task.
- The skill explicitly notes its scope (legal-domain prompts) and declines to enhance.
- The skill optionally suggests appropriate alternatives (general-purpose AI for non-legal tasks).

**Pass criteria:** Explicit refusal.

### Scenario 5: Implies legal advice

**Inputs:** "Should I sign this contract?"

**Expected behavior:**
- The skill identifies the implicit legal-advice request.
- The skill either:
(a) Reframes the prompt to a contract-review prompt with a "review for issues to inform your decision" framing, or
(b) Notes the legal-advice scoping and asks the user to reframe.
- The skill does not silently produce a "should you sign" recommendation as the enhanced prompt.

**Pass criteria:** Skill scopes legal-advice prompts appropriately.

### Scenario 6: References a specific skill

**Inputs:** "Apply NDA Review to this attached NDA."

**Expected output structure:** The expansion enriches the prompt with skill-specific defaults (perspective, deal context, output format) appropriate to NDA Review's input schema. If the document and prompt allow inference of perspective or other inputs, the expansion suggests them; if not, the expansion notes that inputs would improve the analysis.

**Expected calibration:**
- The expansion respects the user's skill choice.
- The expansion does not switch to a different skill ("oh, but DPA Checklist Review would be better").
- The expansion adds skill-relevant context (perspective, mode if applicable).

**Edge cases to verify:**
- If the skill referenced doesn't fit the document type (e.g., user requests NDA Review on an MSA), the skill flags the mismatch and suggests the right skill.

**Pass criteria:** Expansion respects user's skill choice while adding skill-relevant context.

## Refusal scenarios

### Refusal 1: Out-of-scope (covered in Scenario 4 above)

### Refusal 2: Prompt asks for outcome prediction

**Input:** "Will I win if I sue under this contract?"

**Expected behavior:** Skill declines to enhance or scope-shifts to "what provisions affect my position in litigation under this contract" — with explicit acknowledgment that outcome prediction is out of scope.

**Pass criteria:** Skill scopes outcome-prediction prompts.

## Cross-cutting verification

- **Expansion preserves intent.** Reviewing the user's original prompt and the expansion side-by-side, the expansion is recognizably the same task with added structure.
- **Expansion is operationally usable.** Running the expansion produces meaningfully better results than running the original.
- **Skill is itself inspectable.** When attached, the user can read the SKILL.md driving the enhancement.
- **Refusals are clean.** Out-of-scope prompts are explicitly declined.
- **No invented inputs.** The skill does not invent perspectives, jurisdictions, or contexts the user did not signal.

## Pass / fail decision

Enhance Prompt v1.0.0 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation by a reviewing attorney or skilled reviewer.
3. Both refusal scenarios trigger documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

Enhance Prompt is a meta-skill that operates on prompts rather than documents. Calibration is about whether the expansion is *useful* — not about whether the expansion is correct in some abstract sense.

Specific competencies for the reviewer:

- Recognizing when an expansion adds operational structure vs. when it adds noise.
- Recognizing when an expansion preserves intent vs. when it has subtly shifted intent.
- Recognizing when an expansion overreaches (asserting perspective the user didn't signal).

A simple practical test the reviewer can apply: "Would the expansion produce a meaningfully better result than the original prompt?" If yes, the expansion is calibrated. If no (the expansion is just longer), the calibration is off.

Calibration assessment is documented in `test-results/enhance-prompt-v1.0.0/calibration-assessment.md`.
