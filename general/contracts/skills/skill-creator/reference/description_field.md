# Writing the Description Field

The frontmatter `description` field is the single most important line in a skill. It is what the model uses to decide whether to load this skill into a given chat. A strong description is the difference between a skill that gets used reliably and one that sits unused in the library.

## What the description field is for

When a user opens a chat, LQ.AI loads available skills' descriptions into the model's context. The model reads the descriptions and decides which skills are relevant. If a skill's description doesn't clearly say *when* to apply the skill, the model won't trigger it — even if the skill itself would be perfect for the task.

## The "Use when..." pattern

Strong descriptions begin with explicit trigger language:

- *"Use when..."*
- *"Use this skill when..."*
- *"Apply when the user..."*
- *"For situations where..."*

This signals to the model that the description is a routing instruction, not just a feature description. The model is reading dozens of skill descriptions; the ones that read like routing instructions get used.

## Anatomy of a strong description

A strong description does three things in one paragraph:

1. **States the trigger conditions** (when to apply).
2. **Names what the skill does** (what to apply).
3. **Mentions the domain or document type** when applicable (where to apply).

Length: aim for 200–400 characters. Long descriptions get truncated in some runtimes. Short descriptions don't give the model enough signal.

## Strong examples

These descriptions are well-written. Note the structure: trigger → action → domain.

> "Use when the user uploads or pastes a non-disclosure agreement and asks for a review, redline, or risk assessment. Identifies unusual provisions, missing standard protections, and one-sided terms; produces a structured report with cited references to specific clauses."

> "Use when the user asks for action items, deadlines, or follow-ups derived from a client alert, regulatory bulletin, or memo. Extracts time-sensitive obligations, distinguishes mandatory from advisory items, and produces a checklist organized by deadline."

> "Use when the user wants to convert technical legal language into plain English for a business audience — board members, sales teams, or non-legal stakeholders. Preserves substantive meaning while removing jargon, qualifying clauses, and unnecessary hedging."

> "Use when the user uploads a Data Processing Agreement and asks whether it complies with GDPR Article 28 processor obligations. Checks for required terms (purpose limitation, sub-processor approval, security measures, audit rights, breach notification, return/deletion), flags gaps, and suggests language to add."

## Weak examples and why

These descriptions are too vague, too generic, or written in the wrong voice.

> "Reviews NDAs."

Too short, no trigger language, no domain detail. The model has no way to decide when to load this versus a generic "Contract Review" skill.

> "I help you review your NDA documents and find issues that you should be aware of as a lawyer reviewing a non-disclosure agreement for your business."

Wrong voice (first-person, addressing the user). The model reads this and gets confused about whose voice to adopt. Descriptions describe the skill in third person.

> "An advanced AI-powered solution leveraging cutting-edge natural language processing to deliver enterprise-grade contract intelligence for modern legal teams."

Marketing copy, not routing instruction. Tells the model nothing about when to apply.

> "Skill for contracts."

Too generic. Will collide with every other contract-related skill in the library.

## Common pitfalls

**The "personality" pitfall.** Don't describe the skill as a persona ("Acts as a senior partner reviewing..."). Describe what it does.

**The "feature list" pitfall.** Don't enumerate every capability ("Reviews, redlines, comments, summarizes, compares, classifies..."). Pick the primary action; the workflow section can list everything.

**The "marketing" pitfall.** Don't sell the skill ("Best-in-class NDA review with cutting-edge AI"). Describe it.

**The "user-instruction" pitfall.** Don't write instructions to the user in the description ("Upload your NDA and the skill will review it"). Write descriptions about the skill, for the model.

## Quick test

Before finalizing a description, ask: *"If a user typed a single sentence in the chat, what sentence would make me — the model — load this skill?"* The description should make that match obvious.

If you can't answer that question clearly, the description is too vague. Rewrite it.
