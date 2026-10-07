# Wizard Mode

The default Skill Creator interaction is open conversation. Wizard mode is the fallback for users who are stuck or who explicitly ask for a structured walkthrough.

## When to switch into wizard mode

Switch when you observe:

- The user has said "I don't know" or equivalent to two consecutive open questions.
- The user asks "can you just walk me through it?" or "what do you need from me?"
- The user is producing one-word or one-line responses for several turns, suggesting they're not engaged with the conversational format.
- The user starts the session with "I want a structured walkthrough" or similar.

When switching, name it:

> "Let me switch to a structured walkthrough — I'll ask each question in order and you can answer as much or as little as you want for each one. Skip any question where you don't have a strong view; I'll fill in reasonable defaults and we can refine later."

This gives the user permission to skip and reduces the pressure of feeling like they need a "right answer" for every question.

## The wizard sequence

Ask these questions in this order. One per turn. Pause for the answer before moving on.

### 1. Name and one-line purpose

> "What should we call this skill, and what does it do in one sentence?"

If the user can't name it, suggest two or three options based on what you've inferred so far. ("Based on what you've told me, this might be 'NDA Risk Review' or 'Quick Contract Triage' — does either fit, or do you want something else?")

### 2. Trigger phrasings

> "Imagine you're in a chat and you want to use this skill. What might you type? Give me two or three examples."

These become the `trigger_examples` in the frontmatter. Push for variety — different ways the same intent might be phrased.

### 3. Required input

> "What does the skill need to do its job? A document? Some text? A URL?"

Often this is "a document." When it is, follow up: "What kind — PDF, Word, pasted text, all of those?"

### 4. Optional inputs

> "Are there things that, if the user provides them, would make the output better? For example, a jurisdiction, a perspective (which side of the deal), or specific positions to check?"

These become `inputs.optional`. Common ones: jurisdiction, perspective (party A vs. B), specific issues to focus on, the user's standard positions.

### 5. The workflow

> "Walk me through what the skill should do. Pretend you're explaining it to a junior associate who's never seen this kind of work — what are the steps, what should they look for, what's the order?"

This is the heart of the skill and the longest answer. Take notes. Ask follow-ups when the user mentions a criterion: "You said you'd flag anything below 1x annual fees — should I make that an explicit threshold, or is it judgment-based?"

### 6. Output format

> "When the skill is done, what does the output look like? A report? A checklist? A redlined document? What's at the top? What's the very first thing you'd want to see?"

Push for specificity. "A report" is not enough; "a one-paragraph executive summary, then a list of issues ranked by severity, then specific clause-by-clause comments" is enough.

### 7. Edge cases

> "Have you ever started reviewing a document and immediately known you weren't going to apply your usual review approach? What was wrong with it?"

This produces the refusal/flag conditions. Common ones: wrong document type, wrong jurisdiction, document too short to be meaningful, document in a language you don't read.

### 8. Examples

> "Can you give me one real example — even just from memory — of a time you did this kind of review? What was the document, what did you flag, what did the output look like?"

If the user can produce one, capture it. If they can't, sketch a hypothetical based on what they've told you and ask them to confirm or correct it. A skill without at least one example is incomplete.

### 9. Self-improvement

> "Do you want this skill to evolve over time? If yes, after each use it'll ask if there's anything you'd change, and update itself based on your feedback. If no, it stays exactly as we wrote it."

Default to off if the user is unsure. They can turn it on later by editing the skill.

### 10. Confirmation

Before drafting the SKILL.md, reflect everything back:

> "Here's what I have. The skill is called X. It triggers on phrases like Y and Z. It takes a document plus optional jurisdiction. It walks through these steps in this order. The output is shaped like A. It refuses or flags B. Self-improvement is on/off. Anything missing or wrong before I draft it?"

This gives the user one final review before the artifact gets written.

## After the wizard

After producing the SKILL.md, return to the standard close: a use suggestion and an offer to refine. The wizard's job is to get a v1.0.0 written; refinement happens through use.
