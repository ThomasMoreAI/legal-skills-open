---
name: audit-transcription
title: Audit transcription
description: Flag and propose corrections for likely mistranscriptions in auto-transcribed meeting notes or audio transcripts. Use when the user says 'audit this transcript', 'fix the transcription', 'find mistranscriptions', or shares a noisy Granola/Whisper output and asks for cleanup.
author: nweii
author_url: https://github.com/nweii/agent-stuff/tree/master/skills/audit-transcription
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Audit transcription

## Posture

Auto-transcribed text is noisy in domain-specific ways. The user almost always knows what they actually said; you don't. **Your job is to flag, not to correct.** Every interpretation is a hypothesis until the user confirms it.

You will be wrong about some flags even when you're well-grounded in context. That's fine — it's expected. What's not fine is silently applying corrections the user hasn't seen.

## Workflow

### 1. Read the whole transcript before flagging anything

You can't tell what's mangled until you know the topic and shape. Skim end-to-end first.

### 2. Pull in domain context the user has documented

Before guessing at vocabulary, check what's actually in the user's world:

- Project notes, AGENTS.md / CLAUDE.md, glossaries
- Related notes the transcript references
- Recent commits, working logs, specs

If a transcribed proper noun doesn't match anything in their documented vocabulary, **don't substitute a similar-sounding name from your own knowledge** — flag it and ask.

### 3. Triage into three confidence tiers

| Tier | Example | What to do |
|------|---------|------------|
| **High — recurring vocabulary** | A phonetic mishearing of a domain term that appears throughout the transcript (e.g. a tool, product, or library name consistently rendered as a similar-sounding non-word) | Propose find/replace |
| **Medium — sentence-level gist** | A garbled clause whose meaning is recoverable from context | Propose your interpretation **as a question**: "I think you were saying X here — does that match?" |
| **Low — unrecoverable** | A sentence where multiple consecutive words are nonsense and the surrounding context doesn't pin down what was being said | Flag as garbled. Do not reconstruct. |

### 4. Surface flags as a list, not as edits

Show the user the triage grouped by tier. Wait for their pass:
- They will confirm some, correct others, and reject a few entirely.
- Treat each correction as a context update — apply it across the rest of the transcript before continuing.
- Don't argue. If the user says "that's not a word we use" about one of your guesses, drop it and don't relitigate.

### 5. Apply edits in-place only after confirmation

For high-confidence vocabulary: inline find/replace.

For medium/low-confidence stretches: wrap with a callout that preserves the original beneath the gist.

```markdown
> [!warning] Transcription note (Garbled)  
> gist: <one-paragraph reconstruction of what was being discussed>

<original garbled text left intact>
```

Never strip the raw transcript. The audit makes a noisy record readable; it doesn't replace it.

### 6. Annotate the file at the top

After edits, add a `## Transcription notes` section above the transcript with:

- A note that the transcript is auto-generated
- The recurring-vocab glossary (so future readers and agents don't re-derive it)
- Single-occurrence corrections that surprised you or that the user explicitly confirmed
- A pointer to the callout format used for unrecoverable passages

Update the frontmatter `description` to mention auto-transcription and the notes section.

## Anti-patterns

- **Don't guess at proper nouns from your own knowledge.** A name that sounds plausible to you may be invented. Flag, ask.
- **Don't rewrite garbled sentences with confident prose.** Even when you think you know what was said, write the gist as a hypothesis in a callout, not as edited dialogue.
- **Don't batch corrections without showing the user first.** Auto-mode does not override "wait for user confirmation on interpretive judgments."
- **Don't keep pushing a guess after the user corrects you.** The correction itself is information about how they think — incorporate it into how you flag the rest.
- **Don't claim you've recovered something you haven't.** If a clause is gone, mark it `[transcription unintelligible]` rather than fabricating.

## When the user is the only source of truth

If you can't ground a flag in any documented context — no glossary, no project notes, nothing in the codebase — say so explicitly when surfacing the flag. Frame it as "no idea what this is, and nothing in your notes resolves it" rather than producing a confident-sounding guess. The user will tell you, and that's the right division of labor.
