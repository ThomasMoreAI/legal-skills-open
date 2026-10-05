---
name: generate-compliance-docs-abdelstark
title: Generate a single template
description: Use when the user needs to generate EU AI Act compliance documentation, wants templates for technical documentation, risk management systems, data governance plans, human oversight plans, or declarations of conformity. Triggers on requests for compliance documents, Annex IV documentation, Article 9 risk management, Article 10 data governance, or Article 14 human oversight plans.
author: AbdelStark
author_url: https://github.com/AbdelStark/eu-ai-act-toolkit/tree/main/skills/generate-compliance-docs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

You are helping a user generate EU AI Act compliance documentation using templates from the @eu-ai-act/sdk or the `eu-ai-act` CLI. These templates provide structured Markdown documents with [TODO] placeholders that the user fills in with their system-specific details.

## Available Templates

The following templates are available:

1. **technical-documentation** (Annex IV) — Comprehensive technical documentation covering system description, design specifications, development methodology, training data, performance metrics, and limitations. Required for all high-risk AI systems.

2. **risk-management-system** (Article 9) — Risk management system plan including risk identification, analysis, evaluation, mitigation measures, residual risk assessment, and testing procedures. Required for high-risk AI systems.

3. **data-governance** (Article 10) — Data governance and management plan covering training/validation/test data practices, data quality measures, bias examination, data relevance assessment, and data gap analysis. Required for high-risk AI systems.

4. **human-oversight-plan** (Article 14) — Human oversight implementation plan detailing human-in-the-loop measures, override capabilities, monitoring procedures, operator training, and escalation protocols. Required for high-risk AI systems.

5. **monitoring-plan** (Articles 72-73) — Post-market monitoring plan covering ongoing performance monitoring, incident detection and reporting, corrective action procedures, and update/change management. Required for high-risk AI systems.

6. **declaration-of-conformity** (Article 47) — EU declaration of conformity document stating the AI system meets all applicable EU AI Act requirements. Required before placing a high-risk AI system on the market.

## Gather Required Inputs

Before generating any template, collect these inputs from the user:

**Required:**
- `systemName` — Name of the AI system (e.g., "Hiring Assistant v2")
- `provider` — Organization name of the AI system provider
- `intendedPurpose` — Description of what the AI system is designed to do

**Optional:**
- `version` — Version string of the AI system (defaults to "0.1.0")
- `date` — Date for the document (defaults to current date)

Ask the user for these values. Do not generate a template without at least the three required inputs.

## Using the SDK

```typescript
import { generateTemplate } from '@eu-ai-act/sdk';

// Generate a single template
const doc = generateTemplate('technical-documentation', {
  systemName: 'Hiring Assistant v2',
  provider: 'Acme Corp',
  intendedPurpose: 'Automated screening and ranking of job applicants based on CV analysis',
  version: '2.1.0',
  date: '2025-06-15',
});

// doc is a string containing Markdown with [TODO] placeholders
console.log(doc);

// Generate all templates for a high-risk system
const templateTypes = [
  'technical-documentation',
  'risk-management-system',
  'data-governance',
  'human-oversight-plan',
  'monitoring-plan',
  'declaration-of-conformity',
];

for (const type of templateTypes) {
  const content = generateTemplate(type, {
    systemName: 'Hiring Assistant v2',
    provider: 'Acme Corp',
    intendedPurpose: 'Automated screening and ranking of job applicants',
  });
  // Write each to a file
  fs.writeFileSync(`./compliance-docs/${type}.md`, content);
}
```

## Using the CLI

```bash
# Generate a single template
npx eu-ai-act generate conformity \
  --system "Hiring Assistant v2" \
  --provider "Acme Corp" \
  --purpose "Automated screening and ranking of job applicants" \
  --output declaration-of-conformity.md

# Generate a specific template type
npx eu-ai-act generate technical-documentation \
  --system "Hiring Assistant v2" \
  --provider "Acme Corp" \
  --purpose "Automated screening and ranking of job applicants" \
  --output technical-docs.md

# Generate ALL templates for a tier (bulk generation)
npx eu-ai-act generate --tier high-risk \
  --system "Hiring Assistant v2" \
  --provider "Acme Corp" \
  --purpose "Automated screening and ranking of job applicants" \
  --output ./compliance-docs/
```

Bulk generation with `--tier high-risk` creates all 6 templates in the output directory.

## Template Output Format

All templates are generated as Markdown files containing:
- A header with system name, provider, date, and version
- Structured sections matching the relevant Article requirements
- `[TODO]` placeholders where the user must fill in system-specific information
- Guidance notes explaining what information belongs in each section
- Cross-references to the applicable EU AI Act articles and recitals

Example placeholder: `[TODO: Describe the specific risks identified during risk assessment, including likelihood and severity ratings]`

## Recommending Templates by Tier

Based on the user's risk tier, recommend the appropriate templates:

- **high-risk**: Recommend generating ALL 6 templates. These are legally required under Articles 9-15, 47, and 72-73.
- **gpai / gpai-systemic**: Recommend technical-documentation for model card/documentation obligations under Articles 53/55.
- **limited**: Recommend technical-documentation for transparency documentation.
- **minimal**: No templates strictly required, but technical-documentation is a best practice.
- **prohibited**: No templates needed — the system should not be deployed.

## Explaining Each Template

When the user asks what a template covers, explain:

- **technical-documentation**: "This is required by Annex IV. It documents your system's general description, design, development process, training data, performance metrics, and known limitations. It's the single most important compliance document."
- **risk-management-system**: "Required by Article 9. It documents your process for identifying, analyzing, and mitigating risks throughout the AI system's lifecycle."
- **data-governance**: "Required by Article 10. It documents how you manage training, validation, and test data — including quality criteria, bias checks, and data relevance."
- **human-oversight-plan**: "Required by Article 14. It documents how humans can monitor, intervene, and override the AI system's decisions."
- **monitoring-plan**: "Required by Articles 72-73. It documents your post-market monitoring strategy including performance tracking, incident reporting, and corrective actions."
- **declaration-of-conformity**: "Required by Article 47. It's a formal declaration that your AI system meets all applicable EU AI Act requirements. Must be signed before placing the system on the market."

## After Generation

Once templates are generated, advise the user to:
1. Search for all `[TODO]` placeholders and fill them in with accurate, system-specific information
2. Have the documents reviewed by their legal and technical teams
3. Keep documents updated as the system evolves
4. Store documents for at least 10 years after the AI system is placed on the market (Article 18)
5. Make technical documentation available to national competent authorities upon request

This tool provides informational guidance and document templates only. It does not constitute legal advice. Consult a qualified legal professional for definitive EU AI Act compliance guidance.
