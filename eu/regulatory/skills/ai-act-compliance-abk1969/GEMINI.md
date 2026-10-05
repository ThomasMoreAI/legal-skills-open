# GEMINI.md — ai-act-compliance (skill-level mirror)

> Skill-level activation pointer for **Gemini CLI**.

## Skill metadata

| Field | Value |
|---|---|
| `skill_id` | `ai-act-compliance` |
| `entry` | [`SKILL.md`](./SKILL.md) |
| `manifest` | [`ssl.json`](./ssl.json) (SSL-1.0, arXiv:2604.24026) |
| `activation_tool` | `activate_skill` |
| `version` | 2.0.0 |
| `license` | MIT |
| `repository` | <https://github.com/abk1969/ai-act-skills> |
| `permission` | `filesystem.read` (own reference files only) |
| `touches_sensitive_resources` | `false` |
| `tool_calls` | `false` |

## Activation

Gemini CLI reads [`SKILL.md`](./SKILL.md) frontmatter — the
`description` field is the canonical trigger source. When a user
question matches one of the 14 intent signatures listed in
[`ssl.json`](./ssl.json) `intent_signature`, call `activate_skill`
with `skill_id: "ai-act-compliance"` and follow the scene graph
defined in `SKILL.md` § "Workflow — SSL scene structure".

## Tool compatibility

**No translation needed.** This skill issues zero tool calls
(`control_flow_features.tool_calls: false` in `ssl.json`). Pure
reference-reading + citation-grade text emission.

## Multi-platform reference

[`references/15-platform-compatibility.md`](./references/15-platform-compatibility.md)
documents the full support matrix (Claude Code, Gemini CLI, Codex) +
per-platform install steps.

## Legal notice

Decision-support only — not legal advice. Final EU AI Act conformity
assessment requires qualified counsel and, for most high-risk systems,
a notified body.
