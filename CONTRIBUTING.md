# Contributing

Thanks for adding a skill. Skills are short Markdown files; you don't need to write any code.

## How to contribute

1. Fork the repository.
2. Add a folder `{country}/{practice}/skills/{slug}/` with a `SKILL.md` inside. Use the template below.
3. If the plugin `{country}/{practice}/` doesn't exist yet, also add `plugin.json`, `CLAUDE.md`, and `README.md` in its root (copy from `ru/arbitration/` as a reference).
4. Open a pull request. CI runs the schema, license, and version checks; a maintainer reviews and merges.

## `SKILL.md` template

```markdown
---
name: my-skill
description: One-paragraph description of what the skill does and when to use it (40–2000 chars). This shows up in the marketplace and in semantic discovery.
author: Your Name
author_url: https://github.com/yourhandle
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [tag-one, tag-two]
---

# Skill title

## When to apply

Triggers, example user prompts, what's out of scope.

## Algorithm

Step-by-step instructions for the orchestrator.

## Output contract

What the answer must contain (citations, disclaimer, etc.).
```

The canonical contract is [`schemas/skill-frontmatter.schema.json`](schemas/skill-frontmatter.schema.json).

## Rules CI enforces

- **License.** Must be one of: `Apache-2.0`, `MIT`, `BSD-3-Clause`, `BSD-2-Clause`, `CC0-1.0`, `CC-BY-4.0`. AGPL / GPL / CC-NC / CC-ND are rejected automatically.
- **`execution_mode`.** Must be `open` in this repository.
- **Path consistency.** `name` matches the folder name; `jurisdiction` and `practice` match the path.
- **Versioning.** `version` follows semver (`MAJOR.MINOR.PATCH`). Bump it on every change to `SKILL.md`.
- **References.** If you cite local source texts, put them under `references/` inside the skill folder and list them in the `sources` frontmatter array.

## Contribution license

By opening a pull request you license your contribution under [Apache License 2.0](LICENSE) (same as the repository).

## No exclusivity

You keep all rights to your skill and can publish it elsewhere — on Lawvable, in your own repository, in a private deployment — without notifying us.
