# EU AI Act Audit

A [Claude Code](https://claude.com/claude-code) skill that audits any software project for **EU AI Act** (Regulation (EU) 2024/1689) compliance.

> [Version en espanol](../README.md)

## What it does

Scans your codebase, identifies AI systems, classifies their risk level, and produces a structured report with:

- AI systems detected (models, SDKs, APIs)
- Risk classification (prohibited, high, limited, minimal)
- Article-by-article compliance status
- Prioritized findings with `file:line` references
- GDPR intersection checks (international transfers, privacy policy)
- Regulatory sources consulted online

## Installation

```bash
npx skills add aios-labs/eu-ai-act-audit
```

Or manually: copy the folder to `~/.claude/skills/eu-ai-act-audit/`.

## Usage

In any project with Claude Code:

```
audit this repo for EU AI Act compliance
```

```
revisa si este proyecto cumple el AI Act 2026
```

```
what do we need for AI Act before August 2026?
```

The skill triggers automatically when you request a full compliance audit.

## What it audits

### Step 1: Regulatory research
Searches online for the latest EU AI Office guidance, Codes of Practice, and enforcement updates.

### Step 2: AI system discovery
Scans `package.json`, `requirements.txt`, API routes, middleware, system prompts, environment variables...

### Step 3: Organization role
Classifies as **provider**, **deployer**, **importer**, or **distributor**.

### Step 4: Risk classification
Applies the Annex III decision tree:

```
Prohibited practice (Art. 5)?
  YES -> Must not be deployed
  NO -> In Annex III?
    YES -> Significant risk of harm? -> HIGH-RISK
    NO -> Interacts with people / generates content? -> LIMITED RISK (Art. 50)
         Other -> MINIMAL RISK
```

### Steps 5-8: Compliance checks
Verifies transparency obligations (Art. 50), GDPR, technical safeguards, and accessibility.

## Report format

```markdown
# EU AI Act Compliance Audit — [Project Name]

## 1. AI Systems Identified
## 2. Risk Classification
## 3. Compliance Status (article-by-article table)
## 4. Findings (high / medium / low priority)
## 5. Summary
## Sources
```

## Key dates

| Date | Obligation |
|---|---|
| Feb 2, 2025 | AI literacy (Art. 4) and prohibited practices (Art. 5) — **already in force** |
| Aug 2, 2025 | GPAI obligations (Chapter V) |
| **Aug 2, 2026** | **Transparency (Art. 50), high-risk systems (Annex III)** |
| Aug 2, 2027 | High-risk systems in regulated products (Annex I) |

## Structure

```
eu-ai-act-audit/
├── SKILL.md                         # Skill instructions (8-step workflow)
├── references/
│   ├── risk-classification.md       # Annex III categories + decision tree
│   └── high-risk-obligations.md     # Full high-risk compliance checklist
├── evals/
│   └── evals.json                   # Test cases
└── docs/
    └── README.en.md                 # This file
```

## Non-compliance fines

| Violation | Maximum fine |
|---|---|
| Prohibited practices | 35M EUR or 7% global turnover |
| High-risk systems | 15M EUR or 3% global turnover |
| Incorrect information | 7.5M EUR or 1% global turnover |

## License

MIT
