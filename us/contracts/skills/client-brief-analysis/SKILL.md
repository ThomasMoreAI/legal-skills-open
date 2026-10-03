---
name: client-brief-analysis
title: Client Brief Analysis Skill
description: Analyze new client context before creating client-facing work. Use for client briefs, intake questions, commercial framing, positioning inputs, decision-maker context, and pre-proposal thinking.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/client-brief-analysis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Client Brief Analysis Skill

Before any copy, any deck, any document: understand the client. The brief is the foundation. Bad brief, bad everything.

---

## The Goal

Surface what matters about this client before any creative work begins. This is not research for its own sake. Every question points toward: what are we actually trying to help them do, and what would make this client say yes?

---

## Six Questions to Answer (In Order)

These come from the CS (Chief of Sales) phase. Do not skip ahead.

**1. Who is in the room?**
Not job titles: decision authority. Who can say yes? Who can block it? Who is the champion internally?

**2. What decision do they need to make?**
Not "what do they need to hear." What specific decision are they facing? What happens if they make the wrong one?

**3. What is the ask?**
Scope, investment range, timeline expectation. As specific as the information allows.

**4. What have they tried before?**
If this is a recurring problem, what did they try? Why didn't it work? The answer to this shapes the approach more than anything else.

**5. What is their biggest fear?**
Not the stated risk: the unstated one. The thing they're worried about that they haven't said out loud.

**6. What exact phrases do they use?**
Their vocabulary, not ours. If they say "alignment," we say alignment. If they say "buy-in," we say buy-in. Their language in the brief becomes their language in the copy.

---

## Sources for Brief Analysis

These sources feed the brief. Read them before running the intake questions.

| Source | What to look for |
|--------|-----------------|
| Call notes | Their vocabulary, their fears, what they pushed back on |
| Intake documents | The stated problem and the stated ask |
| Past engagements | If a returning client, what worked and what didn't |
| Public sources | Industry context, news, financials if relevant |
| RFP or brief | Explicit requirements and implicit priorities |

---

## Documenting the Brief

Save to `docs/01-clients/{client}/01-thinking/01-brief.md`.

Structure:
```
## Client Brief

**Who's in the room:** [names, roles, decision authority]
**The decision:** [specific decision they need to make]
**The ask:** [scope, investment range, timeline]
**What they've tried:** [prior attempts and why they failed]
**Their biggest fear:** [the unstated one]
**Their language:** [actual phrases and vocabulary to use]
**Key tension:** [the thing nobody's said yet but everyone knows]
```

---

## The Key Tension

Before moving to positioning, name the key tension in one sentence. This is the thing the whole engagement will orbit around.

Format: "Everyone knows [X]. Nobody is saying [Y]."

If you can't complete that sentence: the brief isn't done yet.

---

## Moving to Positioning

When all six questions are answered and the key tension is named, the brief is complete.

Invoke `/cmo` to move to positioning.
