# Worked Example — Skipped Prompt

This example shows Enhance Prompt correctly *not* expanding a prompt because the skip conditions apply. The point of this example is to demonstrate restraint — Enhance Prompt's value comes as much from knowing when to do nothing as from knowing what to add.

## Input

```yaml
raw_input: "what about california"
attached_skills: []
attached_files: []
chat_history:
  - role: user
    content: "review this clause for enforceability concerns"
  - role: assistant
    content: |
      The clause has two enforceability concerns:
      1. The 5-year non-solicit period is unusually long...
      2. The geographic scope is unbounded...

      In Delaware, the 5-year duration would face heightened scrutiny but
      is not categorically unenforceable. The geographic scope is the
      bigger issue — Delaware courts typically require reasonable geographic
      limitation tied to the protectable interest...
jurisdiction: "Delaware"
```

## Skip-condition check

- Already well-structured? No — 4 words.
- Conversational or interpersonal? No — substantive.
- **Follow-up question continuing a prior task? Yes.** The prior assistant turn discussed enforceability of a non-solicit clause. The user's "what about california" is asking the same enforceability question for a different jurisdiction. The prior turn supplies all the context (the clause, the issue, the analysis framework); expansion would discard it by re-establishing context the conversation already has.
- Operational? Borderline — but the follow-up condition takes precedence.

Skip the expansion.

## Output

```yaml
expansion_applied: false

expanded_prompt: "what about california"

reasoning: []

skip_reason: "follow-up question continuing the prior turn's analysis; the chat history supplies the context that would otherwise need to be established"

preview_to_user: null
```

When `expansion_applied` is false, the application passes the original `raw_input` through to the model unchanged. The user does not see an Enhance Prompt review screen — the prompt is sent immediately.

## Why this matters

If Enhance Prompt had expanded this to:

> "As in-house counsel, analyze whether the 5-year non-solicit clause and unbounded geographic scope would be enforceable under California law. Identify the relevant statutes (including Cal. Bus. & Prof. Code §16600 generally), leading cases, and any meaningful exceptions..."

...the expansion would have:

1. **Substituted the model's judgment for the user's intent.** The user asked "what about california" — they want the brief continuation of the prior analysis pivoted to California. They did not ask for a comprehensive California-law primer.
2. **Discarded conversational momentum.** The prior turn's framework, the specific clause language, the user's level of engagement — all would have been displaced by a context-free expansion.
3. **Slowed the user down.** A short follow-up should be answered in seconds. Routing through Enhance Prompt's review screen for a follow-up is friction without value.
4. **Trained the user to distrust Enhance Prompt.** If Enhance Prompt expands every prompt regardless of context, users learn to disable it. If Enhance Prompt skips correctly, users learn to trust it.

## What this example demonstrates

- **Skip is a first-class output, not a fallback.** The skill's value includes knowing when to do nothing.
- **Chat history is consulted before expansion.** Without checking history, this prompt would look "vague" and trigger expansion. With history, it is a clear follow-up.
- **The skip_reason is specific and actionable.** "follow-up question continuing the prior turn's analysis" tells the application (and a developer reviewing logs) why this prompt was passed through. Generic "skipped" would be useless for tuning the skip conditions over time.
- **No reasoning bullets when there is nothing to explain.** The `reasoning` array is empty when `expansion_applied` is false. The `skip_reason` field carries the explanation instead.
