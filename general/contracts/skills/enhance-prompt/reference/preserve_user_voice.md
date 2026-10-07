# Preserving User Voice

The single most common failure mode of prompt-rewriting tools is to "improve" the user's prompt into something the user did not ask for. This reference catalogs how to expand without overwriting.

## Why preservation matters

Users develop a feel for how the model responds to their prompts. When the system silently rewrites their input, the response stops mapping to what they typed. They learn to distrust the tool. Worse, the rewrite often discards information the user encoded in word choice — urgency, formality, scope, confidence, the seriousness of the question.

Enhance Prompt's value is *making implicit elements explicit*, not *replacing explicit elements with conventional ones*.

## What to preserve

**The user's substantive verbs and nouns.** "Help me figure out" is not the same as "Analyze." "Quick look" is not the same as "Comprehensive review." "Worried about" is not the same as "Identify risks in." Substituting changes meaning. Preserve verbatim.

**Hedging and qualification.** "I think this is probably fine but..." encodes the user's prior assessment. Do not flatten to "Review this contract."

**Casual or terse phrasing.** "lol" or "ugh, this one again" is the user's emotional state, which encodes information about their priors and time pressure. Don't strip it; you don't need to expand it either.

**User-stated constraints.** "in two paragraphs," "no legalese," "skip the boilerplate" — these are explicit constraints. Carry them through unchanged.

**Pronouns and references the user established.** If the user said "this contract" referring to a contract attached to the chat, the expansion should also say "this contract" — not "the attached contract" or "the document at issue."

**The user's level of detail.** A short prompt should yield a short expanded prompt. Do not pad. The user is signaling something about effort budget.

## What to add

The seven elements from the main SKILL.md (role, jurisdiction, audience, scope, output format, constraints, citation expectations) — *and only the ones that are missing and relevant.*

The test: read the original prompt and ask, "if I run this prompt against the model, what would the model assume that the user did not specify?" Surface those assumptions explicitly. That is the expansion.

## What to never add

- **Industry-standard answers smuggled into the prompt.** "Typically the standard term is 3 years" is an answer, not an expansion.
- **Jurisdiction-specific rules the user did not invoke.** If the user did not specify California, do not insert "considering California's restrictions on non-solicits." That is research the model should do *if* California is in scope, not a prompt instruction.
- **Risk assessments.** "This is a high-risk request, so be careful" inserts a risk frame that is the user's call.
- **Politeness padding.** "Please carefully consider" or "Take your time to think through" are noise.
- **Marketing or salesy language.** "Provide a comprehensive, world-class analysis" is not better than "review this."

## Handling vague prompts

When a prompt is genuinely vague — "thoughts?" or "what do you think" or "review this" with nothing else — the expansion should preserve the vagueness while adding the minimum scaffolding needed for a useful response.

Example transformation:

> *Original:* "Thoughts on this NDA?"
>
> *Expanded:* "As in-house counsel, share your initial thoughts on this NDA. Identify anything notable (favorable, unfavorable, unusual, or worth flagging) without conducting a full review. Output as brief bullets, not a memo. The output is a draft for human review."

Notice what was added: role, scope ("initial thoughts ... without a full review"), output format, default constraint. Notice what was *not* added: a perspective (the user did not specify), a severity rubric (out of scope for "thoughts"), specific issues to look for.

The expanded version is meaningfully more useful than the original, but it is the same prompt — just with the implicit elements made explicit.

## Handling prompts that mix tasks

Sometimes a prompt asks for two or three things at once: "summarize this and also flag any unusual provisions and tell me whether to sign." The expansion should preserve the multi-task structure, not collapse it. Each task may need its own minor expansion (audience for the summary, perspective for the flagging, format for the recommendation), but the structure stays.

## Handling prompts in a continuing conversation

When `chat_history` is provided, much of what would be "implicit" in a one-shot prompt has been established by prior turns. Do not re-establish.

Example: if the prior assistant turn was a contract review and the current user prompt is "what about the IP clause specifically," do not expand to "As in-house counsel, review the IP clause from [perspective]'s perspective..." The perspective is established. Just expand to clarify scope: "Focus on the IP clause specifically. Identify any provisions that warrant attention and explain why."

## Meta-test

Read the expanded prompt aloud. Does it still sound like the user? If you have flattened their voice into "AI assistant generic prompt voice," go back and restore the user's words.

Read the reasoning section. Does it explain *why each element was added*, in plain language the user will understand? If a bullet just says "added role and format," that is not reasoning — that is summary. The reasoning should explain the *value* of the addition: "Specifying you're operating as in-house counsel keeps the response in the right voice for your audience" is reasoning. "Added a role" is not.

Submit only when both pass.
