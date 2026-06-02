---
name: legal-team-lead
title: Legal Team Lead
description: 'Orchestrate multi-agent legal document analysis. Use when: legal analysis, coordinate legal review, synthesize legal findings, document analysis report, combine compliance risk and strategy findings.'
author: varunk130
author_url: https://github.com/varunk130/ai-legal-team-agent/tree/main/skills/legal-team-lead
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Team Lead

Orchestrate a comprehensive legal document analysis by coordinating findings across compliance, contract terms, legal research, and strategic risk assessment - then synthesize into an executive report.

## Output
Save to `outputs/legal-analysis-[doc]-[YYYY-MM-DD].md`

## When to Use
- You have a legal document that needs multi-dimensional analysis
- You want a synthesized report combining compliance, risk, and strategy
- You need to present legal findings to non-legal stakeholders

## What You'll Get

| Section | Description |
|---------|-------------|
| **Executive Summary** | 3-paragraph overview of findings and urgency |
| **Compliance Assessment** | Regulatory adherence (GDPR, CCPA, SOX, employment law) |
| **Key Contract Terms** | Critical clauses extracted and categorized |
| **Risk Profile** | Severity-rated risks with financial exposure estimates |
| **Strategic Recommendations** | Prioritized action items with legal basis |
| **Redline Suggestions** | Specific proposed changes with before/after text |

## Process

### Step 1: Receive the Document
I'll ask:
> "Paste the legal document text or describe the contract/agreement you need analyzed. Include document type (NDA, SaaS agreement, employment contract, lease, etc.) and any specific concerns."

### Step 2: Classify Document Type
I'll identify:
- Document category (contract, agreement, policy, notice)
- Applicable regulatory frameworks
- Relevant jurisdictions
- Key parties and their roles

### Step 3: Coordinate Analysis
I'll run four analysis passes:
1. **Contract Analysis** - clause extraction, obligation mapping, defined terms
2. **Legal Research** - applicable statutes, case law, regulatory requirements
3. **Risk Assessment** - severity rating, financial exposure, likelihood
4. **Strategic Review** - negotiation leverage, recommended positions

### Step 4: Synthesize Findings
I'll combine all four analyses into a unified report with:
- Cross-referenced findings (where contract gaps create compliance risks)
- Prioritized action items (critical → important → advisory)
- Executive summary suitable for non-legal stakeholders

## Tips
1. **Include document type** - "This is a SaaS agreement" helps me apply the right frameworks
2. **Flag specific concerns** - "I'm worried about the IP clause" focuses the analysis
3. **Mention jurisdiction** - Different laws apply in different places

> ⚠️ This skill produces analysis for discussion purposes only. Not legal advice. Consult a qualified attorney for legal decisions.
