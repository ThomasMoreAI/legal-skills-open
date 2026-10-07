# adversarial-qc

An [OpenClaw](https://github.com/openclaw/openclaw) skill for structured adversarial quality control of AI-generated deliverables.

> **⚠️ Proof of concept.** This is an open-source demo showing how far multi-agent verification can take AI quality control. It improves output quality but does not guarantee correctness. The production version is whatever you make of it — fork it, bring your own checklists, harden it, make it yours. This repo exists to show what's possible.

## What it does

Two AI agents independently verify a deliverable against a checklist, without seeing each other's work. Their results are compared:

- **Both agree it's correct** → high confidence (green)
- **Both find the same error** → confirmed issue (red)  
- **They disagree** → flagged for human review (yellow)

Simple idea: if two independent reviewers catch the same thing, you can trust it. If they disagree, a human looks.

## Why

Single-agent AI output has blind spots. Asking the same model to "review its own work" catches surface errors but misses structural ones. Running two agents in parallel — especially on different models — catches significantly more.

Based on research from Du et al. (ICML 2024) and Khan et al. (ICML 2024 Best Paper) showing multi-agent verification improves factual accuracy from 48% to 76% in some settings.

## Features

- **Single-model or cross-model** — two agents on the same model (cheap) or two different providers (stronger)
- **3 depth levels** — quick (~$0.02), standard (~$0.10), deep (~$0.50)
- **17-item verification checklist** covering factual accuracy, logical consistency, source attribution, formatting, domain correctness
- **Pre-built checklists** for M&A due diligence, contract review, code review, and general use
- **QC certificate** — PDF audit trail with pass/fail/review for every item, both agents' evidence, and overall verdict
- **Configurable** — bring your own checklist for any domain

## Installation

### OpenClaw 

Send the link to this GitHub repo to your agent and ask it how to install it.



## Usage

Once installed, the skill triggers when you ask your agent to:
- "QC this report"
- "Review this before sending"  
- "Run adversarial check on this analysis"
- "Verify this deliverable"

Or configure it as a mandatory gate on all substantive output.

### Configuration

Set in `references/config.md`:
- **Mode**: `single` or `cross`
- **Depth**: `quick`, `standard`, or `deep`  
- **Output**: `certificate` (PDF), `inline` (text), or `both`
- **Models**: which models to use for each agent

## Structure

```
adversarial-qc/
├── SKILL.md                          # Main skill definition
├── references/
│   ├── checklist.md                  # 17-item verification checklist
│   ├── config.md                     # Configuration options
│   ├── certificate-template.md       # QC certificate format
│   └── custom-checklists.md          # Domain-specific checklists (legal, code, M&A)
└── README.md
```

## Cost

| Depth | Single-model | Cross-model |
|-------|-------------|-------------|
| Quick | ~$0.02-0.05 | ~$0.04-0.10 |
| Standard | ~$0.10-0.30 | ~$0.20-0.50 |
| Deep | ~$0.30-1.00 | ~$0.50-1.50 |

Costs assume Sonnet-tier models. Opus increases ~5-10x.

## Background

Built from lessons learned running adversarial AI debates over several months. The key insight: full multi-turn debates between AI agents are expensive and don't consistently outperform simpler methods (ICLR 2025 systematic review). Parallel independent verification — where two agents check the same work without interacting — captures most of the benefit at a fraction of the cost.

## License

MIT

## Author

Alexios van der Slikke-Kirillov
