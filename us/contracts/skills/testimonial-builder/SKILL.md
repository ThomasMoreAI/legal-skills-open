---
name: testimonial-builder
title: Testimonial Builder
description: Build client testimonials from interview transcripts. Use for testimonial categories, transcript analysis, approval checkpoints, testimonial drafting, client voice, and proof narrative creation.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/testimonial-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Testimonial Builder

Three phases. One pause. Output is a Markdown file of full testimonials in the client's voice, ready to send for approval.

---

## How to Start

Say: *"Build testimonials for [Client Name]"* or *"Create testimonials from [Client]'s interviews."*

If the client name is not provided, ask for it before proceeding.

---

## Directory Conventions

| Purpose | Path |
|---------|------|
| Source interviews | `docs/00-resources/03-client-interviews/[Client]/` |
| Output testimonials | `docs/00-resources/04-testimonials/[Client]/testimonials.md` |

Both directories use the client's first name as the folder name (e.g., `Judith`, `Tim`).

---

## Phase 1: Transcript Analysis

### Step 1: Discover and clean files

```bash
ls docs/00-resources/03-client-interviews/[Client]/
```

List all files. Then run the transcript cleaner to strip timestamps, filler words, and re-group fragmented turns before reading:

```bash
python transcript_cleaner.py docs/00-resources/03-client-interviews/[Client]/ \
  --output-dir /tmp/transcripts-[client-lowercase]
```

Read the cleaned files from `/tmp/transcripts-[client-lowercase]/` instead of the originals. This reduces token usage by 8-12% for Gemini transcripts and re-groups fragmented speaker turns.

Optionally, to get only the client's lines for a focused first pass:

```bash
python transcript_cleaner.py docs/00-resources/03-client-interviews/[Client]/ \
  --speaker "[Full Client Name]" --output-dir /tmp/transcripts-[client-lowercase]-filtered
```

Note the date range covered by the files and whether tone shifts across sessions.

### Step 2: Extract raw material

While reading, capture:

- **Voice markers**: actual words and phrases the client uses (vocabulary, metaphors, rhythm, sentence structure)
- **Tone shifts**: does their tone change across sessions? Early sessions vs. later ones often differ
- **Hard outcomes**: specific numbers, metrics, named results they mention
- **Recurring themes**: topics they return to across multiple sessions
- **Sensitive content**: early internal friction, political tension, vulnerability: flag anything that may need client confirmation before publishing

### Step 3: Map testimonial categories

For each distinct theme, produce:

```
**Theme N: [Title]**
- Who this serves: (what type of prospect would respond to this)
- Core message: (one sentence)
- Key source quotes: (2-4 verbatim quotes from transcripts)
- Voice markers for this theme: (how they specifically speak about this topic)
- Overlap: (note if this theme overlaps with another)
- Sensitive content flag: (yes/no: if yes, note what needs confirmation)
```

Aim for 4-7 themes. Fewer strong ones beat many weak ones.

---

## Phase 2: Category Review (PAUSE: wait for user)

Present all themes using the format above. Then say:

> Here are [N] testimonial categories. A few overlap: I've flagged them above.
>
> Which would you like to combine, remove, or keep as-is before I write the full testimonials?

**Do not proceed to Phase 3 until the user has approved the final category set.**

Handle common responses:
- "Combine X and Y": merge them, confirm the combined scope before writing
- "Remove X": drop it, confirm before writing
- "Keep all": proceed as-is
- "Not sure about X": describe what that testimonial would be about in one sentence, let user decide

---

## Phase 3: Write Testimonials

### Writing rules

**Structure:**
- Minimum 2 paragraphs per testimonial
- Lead with the problem or context in the client's voice
- Close with outcome, impact, or principle they drew from it

**Voice:**
- Use the client's actual words, phrases, and metaphors verbatim
- Match their rhythm: if they speak in short declarative sentences, write that way; if they build layered arguments, reflect that
- Never invent language they did not use

**Hard rules: no exceptions:**
- No em dashes (—). Use a comma, semicolon, colon, or restructure the sentence
- No generic testimonial language: "game-changer," "transformed our business," "couldn't be happier," "blown away," "world-class"
- No effusiveness. Credibility comes from specificity, not enthusiasm
- Include hard numbers and metrics when the client mentioned them
- Do not soften or polish away the candor: honest observations are what make testimonials believable

**Sensitive content:**
- If a theme drew from early-session vulnerability or internal political friction, add a note after that testimonial:
  > *Note: This testimonial draws on candid observations from early sessions. Confirm with [Client] that they are comfortable surfacing this publicly before sending.*

### Save the file

Create the output directory if needed and save:

```
docs/00-resources/04-testimonials/[Client]/testimonials.md
```

Use this file structure:

```markdown
# [Full Name]: Testimonials
**Title:** [Title], [Company]
**Status:** Draft, pending [First Name]'s approval

---

## 1. [Theme Title]

[Testimonial text]

---

## 2. [Theme Title]

[Testimonial text]

---

[repeat for each testimonial]

---

*Drafted from interviews conducted [year(s)]. All testimonials written in [First Name]'s voice for their review and approval.*
```

---

## Quality Tests

Before delivering, verify each testimonial:

| Test | Question | If No |
|------|----------|-------|
| Voice | Would this person actually say this? | Replace invented phrases with their real ones |
| Specificity | Is there a real story, outcome, or number? | Add concrete detail from transcripts |
| Credibility | Does it sound earned, not performed? | Cut any effusive language |
| Distinctness | Could this be from any client? | Add their specific situation or language |
| Em dash check | Zero em dashes? | Replace with comma, colon, or restructure |

---

## Output to User

After saving, return:

- File path
- List of testimonial titles with one-sentence description of who each serves
- Any sensitive content flags that need Pablo's attention before sending

Keep the summary under 150 words.
