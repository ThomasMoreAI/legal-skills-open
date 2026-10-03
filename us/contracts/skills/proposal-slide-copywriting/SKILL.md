---
name: proposal-slide-copywriting
title: Proposal Slide Copywriting Skill
description: Proposal deck slide copy constraints. Use for proposal slide headlines, body copy, RFP deck language, economy, hierarchy, and sequence rules for client engagement proposals.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/proposal-slide-copywriting
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Proposal Slide Copywriting Skill

Slides are not articles. Not bullets. Not summaries.
A slide is a single declarative moment in a conversation.

Proposal decks have specific section gravity: Understanding, Approach, Phases, Investment.
Every slide must earn its place in one of those arcs.

---

## Fundamental Rules

### 1. The Headline Carries the Argument
Remove all body text. Read only headlines in sequence.
If that tells the full story: done. If not: rewrite headlines.

Headlines are statements, questions, or provocations. Never topic labels.
❌ "Our Approach to the Engagement"
✅ "The Gap Isn't Capability: It's Alignment"

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

In a proposal deck, the sequence must also mirror the client's decision journey:
"Do they understand our situation? → Do they have a credible approach? → Can we afford it?"

---

## Word Economy

| Element | Target | Hard Limit |
|---------|--------|------------|
| Headline | 8-12 words | 15 words |
| Body text | 15-25 words | 35 words |
| Bullet items (if used) | 3-5 words each | 8 words |
| Max bullets | 3 | 5 |

---

## Banned on Proposal Slides

Slide titles that are just nouns:
`Overview, Introduction, Background, Our Approach, Our Services, Our Process, About Us, Next Steps, Conclusion, Summary, Key Takeaways`

Proposal-specific bans:
`Proven Methodology, Best-in-Class, Trusted Partner, World-Class, Seamless, Robust, Leverage, Synergy, Holistic, End-to-End`

Body text crimes:
- Nested bullets (sub-bullets)
- "We believe..." / "Our goal is to..." / "We are excited to..."
- Any sentence over 20 words
- Three sentences when one would do
- Em-dashes. Never. Use a period, comma, colon, or parentheses instead.

Structural crimes:
- More than 2 text zones per content slide
- Agenda slides
- Slides that exist only to transition
- Investment slides that bury the number

---

## The 10-Second Test
Show the slide for 10 seconds. Cover it. Ask: "what was the one thing?"
If they can't answer: rewrite.

---

## Proposal Section Context

**Understanding**: Show the client you've diagnosed their real problem, not the one they stated.
Headlines here should create mild discomfort: "You already know X. The real issue is Y."

**Approach**: Explain *how* you work, not *what* you deliver. The method is the differentiator.
Headlines here should create confidence: "We don't start with outputs. We start with the constraint."

**Phases**: Make the work feel concrete and sequenced. Each phase headline should name the outcome, not the activity.
❌ "Phase 1: Discovery"
✅ "Phase 1: Surface What's Actually Blocking Growth"

**Investment**: Never hedge. State the number clearly, then justify it in terms of value: not effort.
Headlines here should pre-empt the objection: "This Is What Focused Looks Like"

---

## Writing Sequence
1. Write all headlines first. Read in sequence. Fix until they tell the complete proposal story.
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

### JSON Apply Block (for bridge)

When pushing changes via the bridge, use this format:

```json
{
  "changes": [
    {
      "node_id": "123:456",
      "new_text": "Phase 1: Surface What's Actually Blocking Growth",
      "slide_name": "Phase 1"
    }
  ]
}
```

POST to `http://localhost:41234/api/changes`: the plugin will poll and apply.
