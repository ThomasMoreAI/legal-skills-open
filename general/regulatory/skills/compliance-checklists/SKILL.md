---
name: compliance-checklists
title: Compliance Checklists
description: Create operational checklists for legal, accessibility, privacy, platform, and product compliance obligations.
author: MRCalderon3D
author_url: https://github.com/MRCalderon3D/everything-game-dev-code/tree/main/skills/qa-release/compliance-checklists
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Compliance Checklists

## Purpose
Create operational checklists for legal, accessibility, privacy, platform, and product compliance obligations.

## Use When
- compliance requirements are spread across teams
- a launch checklist is incomplete
- a platform or market imposes new constraints

## Inputs
- platform rules
- data practices
- store policies
- accessibility scope

## Process
1. collect required compliance categories
2. turn each obligation into a reviewable checklist item
3. identify owners and evidence required to pass
4. track waivers or unresolved questions explicitly
5. review the checklist at milestone and release gates

## Outputs
- compliance checklist set
- evidence requirements
- owner map
- waiver tracking

## Quality Bar
- turns risk into explicit evidence and ownership
- keeps release blockers visible instead of implicit
- connects quality decisions to milestone and platform impact

## Common Failure Modes
- severity inflation or minimization without player-impact context
- treating waived risks as invisible
- submission checklists that are incomplete or stale

## Related Agents
- security-reviewer
- console-compliance-reviewer
- release-manager

## Related Commands
- cert-check
- release-check
- verify

## Notes
- Keep this skill aligned with the relevant rules layer and current project documentation.
- If engine-specific constraints materially change the workflow, hand off to the matching engine skill or engine-specific reviewer.
