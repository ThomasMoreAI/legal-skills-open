# Output language preference: auto
<!-- qwen-code:llm-output-language: auto -->

## Rule
Respond in the same language as the user's input.

## Exception
If the user **explicitly** requests a response in a specific language (e.g., "please reply in English"), switch to the user's requested language for the remainder of the conversation.

## Mixed-language input
If the user mixes languages, use the language that best matches the user's main request.

## Keep technical artifacts unchanged
Do **not** translate or rewrite:
- Code blocks, CLI commands, file paths, stack traces, logs, JSON keys, identifiers
- Exact quoted text from the user (keep quotes verbatim)

## Tool / system outputs
Raw tool/system outputs may contain fixed-format English. Preserve them verbatim, and if needed, add a short explanation in the user's language below.
