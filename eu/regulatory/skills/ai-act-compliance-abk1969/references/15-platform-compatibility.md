# Platform compatibility — Claude Code, Gemini CLI, OpenAI Codex

> Authoritative reference on how the `ai-act-compliance` skill activates
> across the three supported agent runtimes. The skill content
> (regulatory expertise, ISO anchors, references) is **identical** on every
> platform — only discovery and activation differ.

## Why this skill is portable by design

The `ai-act-compliance` skill is **decision-support / reference-grade**.
It declares (per `ssl.json`):

- `permission: filesystem.read` — only reads its own reference files
- `touches_sensitive_resources: false`
- **No** network access, **no** credentials, **no** code execution, **no**
  external tool calls

This minimal resource profile means the skill is **runtime-agnostic**:
nothing in the body depends on Claude-Code-specific tools (no `Bash`, no
`Edit`, no `WebFetch`). Any agent harness that can read Markdown and
follow a frontmatter-described skill can host it.

## Platform support matrix

| Runtime | Status | Discovery file | Install path | Notes |
|---|---|---|---|---|
| **Claude Code** | ✅ first-class | `SKILL.md` frontmatter | `~/.claude/skills/ai-act-compliance/` | Auto-trigger via `Skill` tool. Reload with `/reload-plugins`. |
| **Gemini CLI** | ✅ supported | `GEMINI.md` (root) + `SKILL.md` | `~/.gemini/skills/ai-act-compliance/` *(or platform default)* | Activated via `activate_skill` after Gemini reads `GEMINI.md` at session start. |
| **OpenAI Codex** | ✅ supported | `AGENTS.md` (root) + `SKILL.md` | `~/.agents/skills/ai-act-compliance/` *(per `superpowers:writing-skills` convention)* | Codex reads `AGENTS.md` at the project root and discovers the skill via the entry pointer. |
| GitHub Copilot CLI | 🟡 community | `AGENTS.md` + `references/copilot-tools.md` *(if added)* | `~/.copilot/skills/` *(varies)* | Markdown content portable; tool-name mapping not needed (no tool calls in this skill). |
| Cursor / other AGENTS-aware harnesses | 🟡 community | `AGENTS.md` | varies | Same as above. |

> 🟡 = the markdown content works, but the harness-side activation depends
> on third-party plumbing this repository does not own. Issue / PR
> welcome.

## Per-platform installation

### Claude Code

```bash
# Via skills.sh CLI
npx skills add abk1969/ai-act-skills@ai-act-compliance -g -y

# Manual (macOS / Linux)
git clone https://github.com/abk1969/ai-act-skills
cp -R ai-act-skills/skills/ai-act-compliance ~/.claude/skills/

# Manual (Windows PowerShell)
git clone https://github.com/abk1969/ai-act-skills
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.claude\skills\ai-act-compliance /E /I
```

Then in Claude Code:

```
/reload-plugins
```

The skill auto-triggers when the user's intent matches the `description`
field — e.g., "Is this AI system high-risk?", "What ISO 42001 control
covers art. 9?", "Do I need a FRIA?".

### Gemini CLI

```bash
# Manual install (macOS / Linux)
git clone https://github.com/abk1969/ai-act-skills
mkdir -p ~/.gemini/skills/
cp -R ai-act-skills/skills/ai-act-compliance ~/.gemini/skills/

# Manual install (Windows PowerShell)
git clone https://github.com/abk1969/ai-act-skills
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.gemini\skills" | Out-Null
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.gemini\skills\ai-act-compliance /E /I
```

Gemini CLI reads `GEMINI.md` at the root of the working directory at
session start. Once present, the skill becomes discoverable and Gemini
will invoke `activate_skill` when the user's question matches one of
the intent signatures (see `ssl.json` `intent_signature`).

### OpenAI Codex / AGENTS-aware harnesses

```bash
# Manual install (macOS / Linux)
git clone https://github.com/abk1969/ai-act-skills
mkdir -p ~/.agents/skills/
cp -R ai-act-skills/skills/ai-act-compliance ~/.agents/skills/

# Manual install (Windows PowerShell)
git clone https://github.com/abk1969/ai-act-skills
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
xcopy ai-act-skills\skills\ai-act-compliance $env:USERPROFILE\.agents\skills\ai-act-compliance /E /I
```

Codex follows the `AGENTS.md` convention: a top-level `AGENTS.md` at the
project root signals the skill location. The `superpowers:writing-skills`
guidance (Anthropic) explicitly notes:

> Personal skills live in agent-specific directories
> (`~/.claude/skills` for Claude Code, `~/.agents/skills/` for Codex).

Once installed, Codex reads the skill's `SKILL.md` frontmatter and
applies the same triggering logic as Claude Code.

## Tool-name mapping (not required for this skill)

Many cross-platform skills require a `references/copilot-tools.md` /
`references/codex-tools.md` mapping table because they invoke runtime
tools (`Bash`, `Read`, `Edit`, `Glob`). **This skill invokes none of
those** — its `control_flow_features.tool_calls` is `false` in
`ssl.json`. Verification:

```bash
# These greps return zero AI-Act-skill-mandated tool calls
grep -nE "Bash\(|Edit\(|Write\(|Read\(|WebFetch\(" SKILL.md references/*.md
```

The skill instructs the host LLM to **read** local reference files and
**cite** article + clause + control numbers in its output. Both
operations are universal across LLM runtimes — no tool translation is
needed.

If a downstream consumer wants to *automate* deliverable production
(e.g., generate an Annex IV `.docx` via `example-skills:docx`), that
automation lives outside this skill's scope and may add its own
tool-mapping requirements.

## Activation triggers (identical across platforms)

The skill auto-activates on any of the following user intents (full list
in `SKILL.md` § "When to invoke this skill" and `ssl.json`
`intent_signature`):

- "Is this AI system high-risk?"
- "What ISO 42001 control covers art. 9?"
- "Do I need a FRIA?"
- "How do I report a serious AI incident?"
- "Does art. 4 AI literacy apply to my org?"
- "Is fine-tuning a foundation model substantial modification?"
- "When does the GPAI systemic-risk regime kick in?"
- "Can I run my AI in an EU regulatory sandbox?"

The `description` field in `SKILL.md` frontmatter is the canonical
trigger source — every host runtime parses it.

## Verifying the install

After install on any platform:

1. **Frontmatter parse check** — open
   `<skill-dir>/ai-act-compliance/SKILL.md` and confirm the YAML
   frontmatter starts with `name: ai-act-compliance`.
2. **Reference file count** — confirm 15 reference files in
   `references/` (`01` through `15`).
3. **SSL manifest check** — `ssl.json` parses as JSON and contains
   `skill_id: SKILL_AI_ACT_COMPLIANCE`.
4. **Smoke test** — ask the host: *"Does the EU AI Act art. 4 AI
   literacy obligation apply to a SaaS deployer in France?"* The skill
   should activate and route the answer through scenes
   `S_PREPARE_SCOPE → S_ACQUIRE_FACTS → S_REASON_TIER →
   S_ACT_OBLIGATIONS → S_FINALIZE_REPORT`, citing **art. 4**, the
   **2025-02-02** effective date, and the relevant ISO/IEC 42001 Annex A
   controls.

## Output template — multi-platform compliance report

When a deployer or provider wants a single, portable compliance answer
that is reproducible across runtimes, the skill emits the following
shape (regardless of the host runtime):

```markdown
## EU AI Act compliance assessment

**System**: <name>
**Role**: [Provider | Deployer | Importer | Distributor | Auth. Rep]
**Tier**: [Unacceptable | High | Limited | Minimal]
**Pathway**: [Annex I | Annex III | Art. 50 | None]
**GPAI applicable**: [Yes | No] (systemic-risk: [Yes | No])

### Obligations (article + paragraph)
- [Provider] art. 9(2)(a) — RMS — ISO/IEC 42001 cl. 6.1.2 + A.6.1.2
- [Deployer] art. 26(5) — log retention — ISO/IEC 42001 cl. 8.4 + A.6.2.4
- ...

### Universal obligations
- [Both] art. 4 AI literacy — effective **2025-02-02** —
  ISO/IEC 42001 cl. 7.2 + A.4.3

### Substantial modification check (art. 25)
- [Yes / No] — rationale

### Deliverables
- Risk register (art. 9), Annex IV file (art. 11), DoC (art. 47),
  CE marking (art. 48), EU database registration (art. 49), FRIA
  (art. 27, deployer scope), PMM plan (art. 72), incident channel
  (art. 73)

### Effective dates (art. 113, post-Omnibus)
- 2025-02-02: art. 5 prohibitions + art. 4 AI literacy
- 2026-08-02: art. 50 transparency + Commission GPAI enforcement
- 2026-12-02: NCII/CSAM prohibition + end of art. 50(2) marking grace
- 2027-12-02: Annex III high-risk regime (deferred by 2026 AI Omnibus)
- 2028-08-02: Annex I product-safety pathway

### Legal disclaimer
*Decision-support output. Not legal advice. Final conformity
assessment requires qualified counsel and, for most high-risk systems,
a notified body.*

---
Generated by ai-act-compliance skill v2.0.0 — runtime-agnostic.
```

## Open issues / future work

- **CEN-CENELEC JTC 21 OJEU citations**: when EN ISO/IEC 42001 / 23894 /
  27090 are cited in OJEU, this skill will surface the art. 40
  presumption-of-conformity ladder. Tracked across all platforms.
- **GitHub Copilot CLI**: full first-class support pending stabilisation
  of the Copilot skill API. Markdown is already portable; the missing
  piece is the host-side `activate_skill` analogue.
- **Cursor**: same as Copilot — content portable, host-side
  discovery to be confirmed by the Cursor team.

If you adopt this skill on a runtime not listed above and it works,
please open a PR adding a row to the support matrix.

---

*This file is part of the `ai-act-compliance` skill v2.0.0. The skill's
regulatory content is identical across runtimes. Final conformity
assessment under EU Regulation 2024/1689 always requires qualified
counsel and, for most high-risk systems, a notified body.*
