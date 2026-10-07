# Worked Example — Short Prompt Expanded

This example shows Enhance Prompt applied to a typical short, vague legal prompt. The user has just typed the input; no skills are attached, no chat history is relevant, no specific files are in scope.

## Input

```yaml
raw_input: "what should i watch for in vendor contracts"
attached_skills: []
attached_files: []
chat_history: []
jurisdiction: "US-default"
```

## Skip-condition check

Walk through the skip conditions:

- Already well-structured? No — 7 words, no role, format, scope, or audience specified.
- Conversational or interpersonal? No — substantive question.
- Follow-up question? No — chat_history is empty.
- Operational? No — substantive analytical question.
- Explicit opt-out? No.
- Skill attached that handles this? No — attached_skills empty.

Proceed with expansion.

## Gap identification

Walk through the seven elements:

- **Role:** missing. Default to in-house counsel.
- **Jurisdiction:** prompt is jurisdictionally agnostic ("vendor contracts" generally), but governing law and contract-formation issues are jurisdiction-dependent. Fold in jurisdiction = US-default. Note assumption.
- **Audience:** missing. The phrasing ("what should I watch for") suggests the user is the audience — they want the answer for themselves, not for forwarding. Default audience = in-house user.
- **Scope:** missing. "What should I watch for" is high-level orientation, not deep analysis. Add scope: a checklist of common issues organized by importance.
- **Output format:** missing. For a checklist-style ask, structured headings or bullets are appropriate. Specify.
- **Constraints:** missing. Standard "draft for human review" applies. Add.
- **Citation expectations:** N/A — no document in scope.

## Output

```yaml
expansion_applied: true

expanded_prompt: |
  As in-house counsel, identify the most important issues to watch for when
  reviewing vendor contracts. Treat this as a general orientation checklist
  rather than a deep analysis of any specific document. Cover the issues
  that recur across most vendor contract types (SaaS, professional
  services, equipment, recurring goods/services), and note where
  vendor-type-specific considerations would change the analysis.

  Output as a structured list organized by importance (issues that warrant
  the most attention first). For each issue, briefly state what it is, why
  it matters, and what a reasonable position looks like. Cite specific
  contract types where relevant.

  Assume US commercial context and Delaware-default contract law unless
  the user specifies otherwise.

  This output is a draft for human review, not a final legal opinion.

reasoning:
  - "Made the role explicit (in-house counsel) so the response is anchored in commercial pragmatism rather than litigation-focused thinking."
  - "Set scope as 'general orientation checklist' so the model produces a usable list rather than a comprehensive treatise."
  - "Specified output format (structured list, organized by importance) so you can scan rather than read."
  - "Added jurisdiction default (US/Delaware) since vendor-contract issues like indemnification scope and limitation-of-liability conventions vary by jurisdiction."
  - "Added the standard 'draft for human review' framing — the model will produce useful starting points rather than overconfident final answers."

skip_reason: null

preview_to_user: |
  ## Enhance Prompt — Review before sending

  **Expanded prompt:**

  As in-house counsel, identify the most important issues to watch for when
  reviewing vendor contracts. Treat this as a general orientation checklist
  rather than a deep analysis of any specific document. Cover the issues
  that recur across most vendor contract types (SaaS, professional
  services, equipment, recurring goods/services), and note where
  vendor-type-specific considerations would change the analysis.

  Output as a structured list organized by importance (issues that warrant
  the most attention first). For each issue, briefly state what it is, why
  it matters, and what a reasonable position looks like. Cite specific
  contract types where relevant.

  Assume US commercial context and Delaware-default contract law unless
  the user specifies otherwise.

  This output is a draft for human review, not a final legal opinion.

  **Why these changes:**

  - Made the role explicit (in-house counsel) so the response is anchored
    in commercial pragmatism rather than litigation-focused thinking.
  - Set scope as 'general orientation checklist' so the model produces a
    usable list rather than a comprehensive treatise.
  - Specified output format (structured list, organized by importance)
    so you can scan rather than read.
  - Added jurisdiction default (US/Delaware) since vendor-contract issues
    like indemnification scope and limitation-of-liability conventions
    vary by jurisdiction.
  - Added the standard 'draft for human review' framing — the model will
    produce useful starting points rather than overconfident final answers.

  [ Submit expanded ] [ Edit ] [ Submit original ]
```

## What this example demonstrates

- **The expansion preserves the user's substantive intent.** "What should I watch for" became "identify the most important issues to watch for" — the verb and the framing are unchanged.
- **Each addition has a justification.** The reasoning section is five bullets, one per substantive change. Each bullet explains *why* the change adds value, not just *what* changed.
- **Length growth is proportional.** Input: 7 words. Expanded: ~110 words. About 15x growth, which is at the upper end of acceptable (2–5x is the target) — but here the input was so short that 2x growth would not have surfaced the implicit elements meaningfully. Judgment call.
- **Skipped elements are not padded.** No citation expectations were added because no document is in scope. No audience was added beyond "the user" because the prompt's phrasing made that clear.
- **The user can edit, accept, or skip.** The application surfaces all three options. Enhance Prompt does not auto-submit.
