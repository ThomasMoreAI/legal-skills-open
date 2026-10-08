# Submission Drafting — a Claude Code Skill

A multi-agent [Claude Code](https://claude.com/claude-code) **skill** for persuasive writing, modelled on Chester Porter QC's *The Gentle Art of Persuasion*. It turns a brief or a draft into a piece that moves a **specific reader** to a conclusion the way Porter persuaded a tribunal: by courtesy, undisputed fact, and frank pre-emptive concession — never by force.

> ⚠️ **Not legal advice.** This skill is a drafting aid. Where a document has legal consequences (a Calderbank offer, a letter of demand), have it reviewed by a qualified practitioner before it is sent.

## What it does

The skill is register-general — the reader may be an opponent's solicitor, a regulator, a board, a client, a counterparty, or the reader of an essay. It runs as an orchestrated, multi-agent pass:

1. **Stage 1 — Orchestration.** The Lead Strategist ("Smiling Funnel-Web") decomposes the brief into a persuasion goal and weighted subgoals, hardens the frame (Frame Challenger + Issue Spotter passes), and confirms it with the user.
2. **Stage 0 — Legal intelligence** *(conditional)*. Where a load-bearing point turns on law, the orchestrator runs the [`australian-legal-research`](https://github.com/acor8826/claude-australian-legal-research) method to build a verified authorities pack before drafting.
3. **Stage 2 — Diverge-converge.** It dispatches Fact Finder and Devil's Advocate as parallel subagents, builds the **funnel** (Diplomat pass, then Plain Speaker pass), runs the Porter gate plus a release-blocking citation check, and cycles until the piece passes.

### The persuasion roster

| Agent | Role |
|---|---|
| **Lead Strategist — "Smiling Funnel-Web"** | The orchestrator: frames the goal, decomposes, converges, builds the funnel, makes the final call |
| **Fact Finder** | Verifies facts, strips hyperbole, sequences the fact base chronologically |
| **Devil's Advocate** | Maps every objection the reader could raise, each with its disarming concession |
| **Diplomat** | The register pass: courtesy, charm, humility; aggression rewritten into reasonable queries |
| **Plain Speaker** | The clarity pass: jargon and friction removed so the logic lands first time |

Every agent reads `references/porter-method.md` — Porter's doctrines distilled into nine operational rules — before writing anything.

## Installation

Clone this repo straight into your Claude Code skills directory:

```bash
# Personal (all projects)
git clone https://github.com/acor8826/claude-submission-drafting.git \
  ~/.claude/skills/submission-drafting
```

Or, for a single project, copy this folder into that project's `.claude/skills/` directory.

Claude Code auto-discovers any folder containing a `SKILL.md`, so once `submission-drafting/SKILL.md` is in a skills directory it is available.

**Optional companion:** Stage 0 (legal intelligence) works best with the [`australian-legal-research`](https://github.com/acor8826/claude-australian-legal-research) skill installed alongside; without it the skill still runs, but load-bearing legal points cannot be verified against primary sources.

## Usage

Once installed, the skill triggers automatically on persuasive-drafting requests, or you can invoke it explicitly. Triggers include:

- "make this more persuasive", "win over the reader", "anticipate objections"
- "draft a persuasive letter / email / board paper"
- "Calderbank offer", "letter of demand"
- any mention of Chester Porter or the funnel-web

## Repository layout

```
submission-drafting/
├── SKILL.md                        # Skill definition + orchestration architecture
└── references/
    ├── porter-method.md            # Porter's doctrines as nine operational rules
    ├── agent-lead-strategist.md    # Per-agent briefs …
    ├── agent-fact-finder.md
    ├── agent-devils-advocate.md
    ├── agent-diplomat.md
    ├── agent-plain-speaker.md
    ├── frame-hardening.md          # Frame Challenger + Issue Spotter passes
    ├── legal-intelligence.md       # Stage-0 bridge to australian-legal-research
    ├── porter-gate.md              # The release-blocking quality gate
    └── templates.md                # Subagent prompt + output templates
```

## License

[MIT](./LICENSE)
