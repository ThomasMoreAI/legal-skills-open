---
name: case-briefs
title: Case Brief Generation
description: Generates structured case briefs from judicial opinions. Use when the user provides a court opinion and needs a case brief, case summary, or distillation of a judicial decision for legal research.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/case-briefs
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Case Brief Generation

Produces a structured case brief from a judicial opinion or case reporter entry. Extracts caption, procedural posture, facts, issues, holdings, reasoning, and significance into a standardized format.

## Quick Start

Given a court opinion, produce a brief with these six sections in order:

1. **Caption & Procedural Posture** — full case name, court, date, citation; how the case reached this court; lower court decision and basis for review
2. **Statement of Facts** — material facts chronologically; distinguish background, operative, and procedural facts; include only facts the court deemed relevant
3. **Issues Presented** — frame as precise yes/no or standard-identification questions; one issue per entry
4. **Holding & Disposition** — court's answer to each issue; narrow holding vs. broader principles; affirmed / reversed / remanded / other
5. **Reasoning & Analysis** — doctrines, statutes, precedents relied upon; analytical framework or test applied; concurrences and dissents with key departures
6. **Significance** — new precedent, clarification, or notable application; impact on future cases and practice

## Core Guidelines

- Use the opinion's exact language for legal standards, tests, and doctrines
- Mark direct quotations clearly
- Target 1–3 pages depending on complexity
- For multi-issue opinions, separate each issue with its own holding and reasoning
- Maintain objective, analytical tone throughout

## Pitfalls

- **Speculation on gaps**: if the source is incomplete on any element, note the limitation — never fill in missing details
- **Overbroad holdings**: state the narrow holding first, then any broader principle the court announced
- **Conflating facts and analysis**: keep the facts section purely factual; save legal characterization for reasoning
