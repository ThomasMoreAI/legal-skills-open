# AGENTS.md — ai-act-compliance (skill-level mirror)

> Skill-level pointer for **AGENTS-aware** runtimes (OpenAI Codex,
> Copilot CLI, Cursor, AGENTS.md-conventional harnesses) that load
> skills from a per-skill directory rather than a project root.

## Skill metadata

| Field | Value |
|---|---|
| `skill_id` | `ai-act-compliance` |
| `entry` | [`SKILL.md`](./SKILL.md) |
| `manifest` | [`ssl.json`](./ssl.json) (SSL-1.0, arXiv:2604.24026) |
| `version` | 2.0.0 |
| `license` | MIT |
| `repository` | <https://github.com/abk1969/ai-act-skills> |
| `permission` | `filesystem.read` (own reference files only) |
| `touches_sensitive_resources` | `false` |
| `tool_calls` | `false` (this skill performs only textual reasoning + reference reads) |

## Activation

Read [`SKILL.md`](./SKILL.md) — its YAML frontmatter `description`
field is the canonical trigger source. Use the typed scene graph in
`SKILL.md` § "Workflow — SSL scene structure" (entry
`S_PREPARE_SCOPE`).

For the 14 sample intent signatures and the full machine-readable
scheduling/structural/logical view, see [`ssl.json`](./ssl.json).

## Tool-name mapping

**None required.** This skill issues no tool calls. It instructs the
host model to read local Markdown references and produce
citation-grade text. Both are runtime-universal.

## Multi-platform reference

The full activation matrix and per-platform install instructions live
in
[`references/15-platform-compatibility.md`](./references/15-platform-compatibility.md).

## Legal notice

Decision-support only — not legal advice. Final EU AI Act conformity
assessment requires qualified counsel and, for most high-risk systems,
a notified body.
