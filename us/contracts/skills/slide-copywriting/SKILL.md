---
name: slide-copywriting
title: Slide Copywriting Skill
description: Slide copywriting constraints and ENAC voice rules. Use for slide headlines, deck copy, presentation text, concise body copy, headline sequences, and visual storytelling.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/slide-copywriting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Slide Copywriting Skill

Slides are not articles. Not bullets. Not summaries.
A slide is a single declarative moment in a conversation.

---

## Fundamental Rules

### 1. The Headline Carries the Argument
Remove all body text. Read only headlines in sequence.
If that tells the full story: done. If not: rewrite headlines.

Headlines are statements, questions, or provocations. Never topic labels.
❌ "Our Approach to Home Services"
✅ "You're Not in the Home Services Business Anymore"

### 2. One Idea Per Slide
Can't name the single idea in 6 words → split the slide.
Two slides share the same idea → merge them.

### 3. Body Text Is Evidence Only
Body text does one of two things:
- Adds a specific detail that makes the headline land harder
- Creates a question the next slide answers

Never explains the headline. If the headline needs explaining → rewrite the headline.

### 4. The Sequence Is the Argument
Each slide's headline creates a question. The next slide's headline answers it.
Read each consecutive pair as Q&A. If it doesn't work: fix sequence or headlines.

---

## Word Economy

| Element | Target | Hard Limit |
|---------|--------|------------|
| Headline | 8-12 words | 15 words |
| Body text | 15-25 words | 35 words |
| Bullet items (if used) | 3-5 words each | 8 words |
| Max bullets | 3 | 5 |

---

## Banned on Slides

Slide titles that are just nouns:
`Overview, Introduction, Background, Our Approach, Our Services, Our Process, About Us, Next Steps, Conclusion, Summary, Key Takeaways`

Body text crimes:
- Nested bullets (sub-bullets)
- "We believe..." / "Our goal is to..."
- Any sentence over 20 words
- Three sentences when one would do
- Em-dashes. Never. Use a period, comma, colon, or parentheses instead.

Structural crimes:
- More than 2 text zones per content slide
- Agenda slides
- Slides that exist only to transition

---

## The 10-Second Test
Show the slide for 10 seconds. Cover it. Ask: "what was the one thing?"
If they can't answer: rewrite.

---

## Writing Sequence
1. Write all headlines first. Read in sequence. Fix until they tell the complete story.
2. Add body text only where the headline creates a gap.
3. Apply word counts. Cut to limits.
4. Read aloud. If you stumble: rewrite.
5. AI sniff test: could ChatGPT have written this? If yes: rewrite.

---

## Delivery Format

```
**SLIDE [N]: [Slide Name]**
Headline: [exact text]
Body: [exact text, or "none"]
Node IDs: [headline_node_id], [body_node_id]
```

Always include node IDs from the extracted deck data so changes apply directly to Figma Slides.
