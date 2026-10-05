---
name: compliance-checklist-abdelstark
title: View full checklist for a tier
description: Use when the user needs to track EU AI Act compliance obligations, wants to see what requirements apply to their risk tier, needs to check compliance progress, or asks about specific Article requirements. Triggers on questions about compliance tracking, obligation checklists, Article 9-15 requirements, GPAI obligations, or compliance status.
author: AbdelStark
author_url: https://github.com/AbdelStark/eu-ai-act-toolkit/tree/main/skills/compliance-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

You are helping a user track and manage their EU AI Act compliance obligations. Use the @eu-ai-act/sdk or the `eu-ai-act` CLI to retrieve checklists, track progress, and generate compliance reports.

## Determine the Risk Tier

Before showing a checklist, you need the user's risk tier. Either:
- Ask the user directly: "What risk tier has your AI system been classified as?"
- If they don't know, use the classify-ai-system skill first to determine it
- Accept one of: prohibited, high-risk, gpai-systemic, gpai, limited, minimal

The toolkit contains 92 total checklist items across 6 tiers:
- **high-risk**: 61 items (Articles 9-15, 26, 72-73)
- **gpai-systemic**: 10 items (Article 55 + systemic risk obligations)
- **gpai**: 9 items (Article 53 transparency & documentation)
- **limited**: 6 items (Article 50 transparency obligations)
- **minimal**: 4 items (voluntary codes of conduct, basic transparency)
- **prohibited**: 2 items (cease deployment, notify authorities)

## Using the SDK

```typescript
import { getChecklist, calculateScore, countProgress } from '@eu-ai-act/sdk';

// Get all obligations for a tier
const checklist = getChecklist('high-risk');

// Each item has:
// {
//   id: 'hr-rm-001',
//   article: 'Article 9',
//   category: 'risk-management',
//   text: 'Establish a risk management system',
//   description: 'A risk management system shall be established, implemented, documented and maintained...',
//   required: true
// }

// Track progress with completed item IDs
const completed = ['hr-rm-001', 'hr-rm-002', 'hr-dg-001'];
const score = calculateScore('high-risk', completed);
// { percentage: 4.9, completed: 3, total: 61 }

const progress = countProgress('high-risk', completed);
// { completed: 3, remaining: 58, total: 61, byCategory: { 'risk-management': { completed: 2, total: 12 }, ... } }
```

## Using the CLI

```bash
# View full checklist for a tier
npx eu-ai-act checklist high-risk

# JSON output for programmatic use
npx eu-ai-act checklist high-risk --json

# Check current compliance status (reads from .eu-ai-act.json in project root)
npx eu-ai-act status

# Export a compliance report
npx eu-ai-act report --format md
npx eu-ai-act report --format json
```

The CLI tracks state in a `.eu-ai-act.json` file in the project root. This file stores the system classification, completed checklist items, and metadata.

## Presenting the Checklist

Show checklist items grouped by category. The main categories for high-risk systems are:

1. **risk-management** (Article 9) — Risk identification, analysis, evaluation, mitigation, testing
2. **data-governance** (Article 10) — Training data quality, bias examination, data relevance, completeness
3. **documentation** (Article 11, Annex IV) — Technical documentation covering system design, development, capabilities, limitations
4. **record-keeping** (Article 12) — Automatic logging of system operations, traceability
5. **transparency** (Article 13) — Instructions for use, system capabilities, limitations, human oversight info
6. **human-oversight** (Article 14) — Human-in-the-loop measures, ability to override, monitoring capabilities
7. **accuracy-robustness-cybersecurity** (Article 15) — Accuracy levels, resilience to errors, security measures
8. **post-market-monitoring** (Articles 72-73) — Ongoing monitoring plan, incident reporting, corrective actions
9. **registration** (Article 49) — EU database registration
10. **quality-management** (Article 17) — Quality management system documentation

For GPAI tiers, categories include:
- **model-documentation** — Technical documentation of model capabilities
- **transparency** — Downstream provider information obligations
- **copyright** — Copyright law compliance, training data documentation
- **systemic-risk** (gpai-systemic only) — Model evaluation, adversarial testing, incident reporting, cybersecurity

## Filtering and Searching

Help the user filter the checklist:
- By article: "Show me all Article 10 requirements" — filter items where article === 'Article 10'
- By category: "What data governance items do I need?" — filter by category === 'data-governance'
- By completion status: "What's left to do?" — show items not in the completed set
- By required flag: "What's mandatory vs recommended?" — filter by required === true

## Tracking Progress

When the user marks items as complete:
1. Record the item ID
2. Use calculateScore() to show updated percentage
3. Use countProgress() to show per-category breakdown
4. Encourage the user to update their .eu-ai-act.json file or use `npx eu-ai-act status` to persist progress

## Report Generation

When the user needs to share compliance status:
- `npx eu-ai-act report --format md` generates a Markdown compliance report
- `npx eu-ai-act report --format json` generates a machine-readable JSON report
- Reports include: system info, classification, completion percentage, item-by-item status, timestamps

## Important Notes

- Checklist items map directly to EU AI Act articles — always provide the article reference
- Required items are legally mandated; non-required items are best practices
- Enforcement dates vary by tier — remind users of their applicable deadline
- This tool provides informational guidance only and does not constitute legal advice
