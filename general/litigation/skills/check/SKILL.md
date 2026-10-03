---
name: check
title: AI4L - Project Verification & Consistency Checking
description: Project Verification & Consistency Checking
author: forever-healthy
author_url: https://github.com/forever-healthy/AI4L/tree/main/.claude/skills/check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# AI4L - Project Verification & Consistency Checking

Handles consistency checking for all major files in the repo, including version numbers, item numbering, and overall consistency across files

### [project_files]

- `.claude/skills/er/SKILL.md`
- `.claude/skills/check/SKILL.md`

- `.claude/agents/er-auditor.md`
- `.claude/agents/er-creator.md`
- `.claude/agents/er-fixer.md`
- `.claude/agents/er-combiner.md`

- `AGENTS.md`
- `CLAUDE.md`
- `README.md`
- `CONTRIBUTING.md`

- `prompts/AI4L.md`
- `prompts/PERSONA.md`

- `.grok/rules/rules.md`

- `docs/Using-Chat-UI.md`
- `docs/Using-Claude-Desktop.md`
- `docs/Using-CLI-Environments.md`
- `docs/Lessons-Learned.md`
- `docs/Limitations.md`

- `docs/Examples.md`

## Version

* Check all [project_files] version numbers
* Use the version stated in the `VERSION` file in the project root as a reference.
* Make sure that all targets are consistent with it, including the version in the badges.
* Some files do not have badges, just the version in the text. Make sure those are consistent as well.
* If a file has no version, leave it as it is

## Consistency Checking

* Check all target files for consistency and completeness
* Check the numbering of all items and the item count in AI4L.md

# Reporting

* If there are any inconsistencies, report them and ask the user if you should fix them.
* Report what was fixed (if anything).
