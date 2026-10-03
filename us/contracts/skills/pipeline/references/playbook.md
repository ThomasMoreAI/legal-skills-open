You are entering the Pipeline Copilot content workflow.

Load these skill files before proceeding:
- `.claude/skills/narrative-workflow.md`
- `.claude/skills/pablo-presentation-voice.md`

## What /pipeline does

This command starts or resumes a content creation session. It governs the full pipeline from initial client thinking through final artifact: whether that's Figma Slides, a Word document, or Markdown.

## Pipeline Phases

```
Phase 0: Explore    (optional) Topic thinking, mental frameworks, ideas
Phase 1: @cs        Client brief: who, what, the ask, their fear, their language
Phase 2: @cmo       Positioning: market tension, contrarian angle, why now
Phase 3: @cco       Creative brief: hook, unspoken truths, the reframe
Phase 4: @cw        Copy: final content in Pablo's voice
Phase 5: Produce    Generate artifact (Figma Slides, Word doc, or Markdown)
```

## On Entry

1. Check if an argument was provided (client name, output type, or Figma URL).
2. If yes: acknowledge it, determine the right phase to start, and begin.
3. If no: ask: "What are we working on? Tell me the client name, what we're creating, or paste a Figma URL."
4. Determine the client folder: `docs/01-clients/{client}/`
5. State the current phase clearly before asking any questions.

## Phase 0: Explore (when the user wants to think first)

No agent persona. Collaborative thinking. Surface frameworks, challenge assumptions, find the angle.

Document to `docs/01-clients/{client}/01-thinking/00-exploration.md` as the conversation progresses.

When ready to move into structured work, invoke `/cs`.

## Navigation

The user moves between phases by invoking:
- `/cs` -> enter Phase 1
- `/cmo` -> enter Phase 2
- `/cco` -> enter Phase 3
- `/cw` -> enter Phase 4

Phases don't have to be sequential. The user can jump at any time.

## Phase 5: Produce

When copy is approved and ready to output:

**Figma Slides (decks, proposals, pitches):**
1. Bridge running: `pcopilot bridge start`
2. Open deck in Figma Slides -> run plugin -> Connect to CLI
3. Post changes: `pcopilot apply changes.json`
4. Plugin writes changes
5. Log what was applied in `05-apply-log.md`

**Word documents (alignments, SOWs, proposals):**
1. Final Markdown in `01-thinking/04-copy.md`
2. Generate: `pcopilot docx 04-copy.md --template alignment` (or `sow`)
3. Move output to `02-output/`

**Markdown only (case studies, testimonials):**
1. Write to `01-thinking/04-copy.md`
2. Copy final version to `02-output/` when approved

## Rules

- Never force a phase transition. The user decides when to move.
- Always state the current phase at the start of each response.
- Always document to the appropriate phase file as the conversation progresses.
- Never write final copy until Phase 3 (CCO creative brief) is complete.
- The pipeline is a guide, not a constraint.
