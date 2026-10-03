---
name: brainstorming
title: Brainstorming
description: Collaborative design refinement through iterative questioning. Use for transforming ideas into detailed specifications before implementation. Based on obra/superpowers.
author: vamseeachanta
author_url: https://github.com/vamseeachanta/workspace-hub/tree/main/.agents/skills/_internal/workflows/brainstorming
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Brainstorming

## Overview

This skill guides collaborative dialogue to transform ideas into detailed design specifications before implementation begins. Through Socratic questioning and iterative refinement, it ensures shared understanding and prevents costly rework.

## Quick Start

1. **Understand context** - Examine project, ask clarifying questions
2. **Explore options** - Propose 2-3 approaches with trade-offs
3. **Refine design** - Validate section by section (200-300 words each)
4. **Document** - Write design to timestamped file
5. **Plan** - Optionally create implementation plan

## When to Use

- Starting new features or projects
- Clarifying ambiguous requirements
- Evaluating architectural decisions
- Designing APIs or interfaces
- Planning complex implementations
- Before writing any significant code

## The Brainstorming Process

### Phase 1: Understanding

**Goal:** Build complete picture of the problem space.

**Approach:**
- Examine project context first
- Ask one question at a time
- Use multiple-choice questions when feasible
- Focus on purpose, constraints, and success metrics

**Key questions:**
- What problem are we solving?
- Who are the users?
- What are the constraints?
- How will success be measured?
- What already exists?
### Phase 2: Exploration

**Goal:** Identify and evaluate solution approaches.

**Approach:**
- Propose 2-3 different approaches
- Present trade-offs for each
- Give reasoned recommendations
- Stay conversational, not prescriptive

**Option template:**
```
### Option A: [Name]

- Approach: [Description]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Best for: [Scenarios]
```
### Phase 3: Design Presentation

**Goal:** Create validated design specification.

**Approach:**
- Break into sections of 200-300 words
- Validate each section before proceeding
- Cover: architecture, components, data flow, error handling, testing
- Allow revisiting earlier decisions

**Section checklist:**
- [ ] Architecture overview

*See sub-skills for full details.*

## Key Principles

### YAGNI (You Aren't Gonna Need It)

Apply ruthlessly:
- Design only what's needed now
- Avoid speculative features
- Question every "nice to have"
- Defer complexity until required
### Single Question Per Message

- Prevents overwhelming stakeholders
- Ensures each point is addressed
- Maintains conversation flow
- Allows for course correction
### Incremental Validation

- Validate section by section
- Get explicit confirmation
- Allow reversals
- Build on confirmed foundations

## Question Templates

### Clarification

- "To clarify: [summary of understanding]. Is that correct?"
- "When you say [term], do you mean (a) [option1], (b) [option2], or (c) something else?"
### Trade-off Exploration

- "We could either [A] or [B]. [A] gives us [benefit] but [drawback]. [B] gives us [benefit] but [drawback]. Which matters more for this project?"
### Priority Assessment

- "Which is more important: [quality A] or [quality B]?"
- "If we had to choose between [option 1] and [option 2], which would you prefer?"
### Validation

- "Here's my understanding of [section]. Does this match your expectations?"
- "Before we move on, let me confirm: [summary]"

## Post-Design Actions

After validation:

1. **Document**
   - Write design to timestamped file
   - Include all decisions and rationale
   - Note any deferred decisions

2. **Plan (Optional)**
   - Use writing-plans skill for implementation
   - Break design into tasks
   - Estimate and prioritize

3. **Review (Optional)**
   - Share with stakeholders
   - Gather additional feedback
   - Incorporate changes

## Related Skills

- [writing-plans](../development/planning/writing-plans/SKILL.md) - Create implementation plans
- [sparc-workflow](../development/sparc-workflow/SKILL.md) - Development methodology
- [product-roadmap](../product/product-roadmap/SKILL.md) - Product planning

---

## Version History

- **1.0.0** (2026-01-19): Initial release adapted from obra/superpowers

## Sub-Skills

- [Best Practices](best-practices/SKILL.md)
- [Error Handling](error-handling/SKILL.md)
- [Metrics](metrics/SKILL.md)
