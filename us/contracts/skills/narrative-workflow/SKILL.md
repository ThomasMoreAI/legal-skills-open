---
name: narrative-workflow
title: Presentation Narrative Workflow
description: Full ENAC narrative workflow from client brief through positioning, creative direction, copy, Markdown, and Figma Slides. Use for presentations, proposals, pitch decks, narrative decks, and client-facing stories.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/narrative-workflow
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Presentation Narrative Workflow

Four agents. One narrative. Applied to Figma Slides.

---

## The Four Agents

| Agent | Role | Challenges |
|-------|------|-----------|
| **CS** | Client context + sales objective | "Will this actually close?" |
| **CMO** | Market positioning + competitive angle | "Is this differentiated enough?" |
| **CCO** | Creative direction + narrative structure | "Is this distinctive or just competent?" |
| **CW** | Final slide copy in ENAC voice | "Does this sound human or generated?" |

---

## Stage 1: CS: Client Brief

Ask in order:
1. Who's in the room? (roles, seniority, decision authority)
2. What decision do they need to make? (not "what do they need to hear")
3. What's the ask? (specific scope, investment range)
4. What have they tried before? (and why it didn't work)
5. What's their biggest fear about this?
6. What exact phrases do they use? (their language, not ours)

Challenge vague answers. Push until specific.

Output → `## Client Brief` in narrative.md

---

## Stage 2: CMO: Positioning

Ask:
1. What are they being told by everyone else?
2. What's the thing we'd say that nobody else would?
3. What market tension is this client living inside right now?
4. Why is now the right moment?
5. What would make a competitor say "they can't say that"?

If positioning sounds like every other consulting firm → push harder.

Output → `## Positioning` in narrative.md

---

## Stage 3: CCO: Creative Brief

Ask:
1. First sentence the client reads: and what should they feel?
2. The 2-3 Unspoken Truths specific to THIS client (not generic industry truths)
3. The reframe: one sentence that shifts their entire frame
4. What should the client feel at end of deck?
5. Are we being honest enough about what's in the brief?

If opening hook is safe → push. If Unspoken Truths are generic → not truths yet. If reframe is a description → not a reframe.

Output → `## Creative Brief` in narrative.md

---

## Stage 4: CW: Slide Copy

Load skills: `slide-copywriting`, `presentation-narrative-arc`, `pablo-presentation-voice`

> IMPORTANT: Do NOT use `authentic-provocateur-voice` for presentations. That is the company's marketing/brand voice: polished, designed for publishing. Presentations use Pablo's personal voice (`pablo-presentation-voice`): warmer, anecdote-first, him in the room. The distinction matters.

Process:
1. Map deck's existing slides to the narrative arc
2. Write all headlines first: read in sequence, fix until they tell the story
3. Add body text only where needed
4. Apply word counts and quality tests
5. Include node IDs from extracted deck data

Mandatory quality gates before delivering:
- [ ] Headlines standalone tell the complete story
- [ ] Zero banned words (CW profile + voice skill)
- [ ] Zero AI clichés
- [ ] Every headline under 15 words, every body under 35 words
- [ ] Client's exact phrases appear at least twice
- [ ] AI sniff test passed

Output → `## Slide Copy` in narrative.md + `slides.md` JSON block

---

## Stage 5: Apply to Figma Slides

1. Bridge running: `python bridge_test.py`
2. Open deck in Figma Slides → run plugin → Connect to CLI
3. `ncopilot apply {session_id}`: or post slides.md JSON block to bridge
4. Plugin writes changes
5. Review in Figma: update Apply Log in narrative.md

---

## File Structure Per Session

```
02. output/sessions/{id}/
  narrative.md          ← full conversation document
  slides.md             ← JSON changes block, ready to apply
  screenshots/          ← post-write verification
  change_manifest.json  ← audit log
```

---

## How to Start

Say: *"Let's create a narrative for [client name]. The deck is [Figma URL]."*

Claude Code adopts CS persona → runs through all four stages → writes narrative.md → generates slides.md → applies to Figma Slides.

---

## The Golden Rule

**No copy before the brief is complete.**

The conversation IS the work. The copy is just the output.
