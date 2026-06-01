---
name: legal-researcher-varunk130
title: Legal Researcher
description: 'Surface relevant case law, statutes, and regulatory frameworks for legal questions. Use when: find case law, legal precedent, statutory reference, regulatory framework, GDPR requirements, CCPA compliance, employment law, contract law research.'
author: varunk130
author_url: https://github.com/varunk130/ai-legal-team-agent/tree/main/skills/legal-researcher
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Researcher

Identify relevant case law, statutory references, and regulatory frameworks applicable to a legal question or document. Surfaces precedents and compliance requirements.

## Output
Save to `outputs/legal-research-[topic]-[YYYY-MM-DD].md`

## When to Use
- You need to understand which regulations apply to a contract or business practice
- You want to know relevant case law precedents for a legal position
- You're assessing compliance requirements for a new product or market
- You need statutory references to support a legal argument

## What You'll Get

| Output | Description |
|--------|-------------|
| **Regulatory Landscape** | Applicable laws and regulations with relevance scoring |
| **Key Requirements** | Specific compliance obligations per regulation |
| **Case Law References** | Relevant precedents with outcomes and applicability |
| **Compliance Checklist** | Actionable items to achieve/maintain compliance |
| **Jurisdiction Notes** | Differences across applicable jurisdictions |

## Process

### Step 1: Define the Question
I'll ask:
> "What legal question or document do you need researched? Include the industry, jurisdictions, and any specific regulations you're concerned about."

### Step 2: Map Regulatory Landscape
I'll identify all applicable frameworks:
- **Privacy**: GDPR, CCPA/CPRA, HIPAA, state privacy laws
- **Financial**: SOX, Dodd-Frank, SEC regulations, PCI-DSS
- **Employment**: FLSA, ADA, Title VII, state employment laws
- **Industry-Specific**: FDA, FTC, FINRA, FERPA
- **International**: Cross-border data transfer, local contract law

### Step 3: Surface Key Requirements
For each applicable regulation:
- Core obligations and prohibitions
- Required documentation or disclosures
- Enforcement mechanisms and penalties
- Recent enforcement actions or guidance changes

### Step 4: Find Relevant Precedents
I'll identify case law that:
- Directly addresses the legal question
- Establishes relevant standards or tests
- Shows enforcement trends
- Highlights common pitfalls

### Step 5: Build Compliance Checklist
Actionable items organized by:
- **Critical** - Must address immediately (legal exposure)
- **Important** - Should address within 30 days
- **Advisory** - Best practices for risk reduction

## Example: GDPR Compliance for SaaS

**Input:** "We're a US SaaS company with EU customers. What do we need for GDPR?"

**Sample Output:**
| Requirement | Status Needed | Priority |
|---|---|---|
| Data Processing Agreement (Art. 28) | Required for all EU customer contracts | 🔴 Critical |
| Lawful basis for processing (Art. 6) | Documented per data type | 🔴 Critical |
| Data Subject Rights (Arts. 15-22) | Process for access, deletion, portability | 🟡 Important |
| Data Protection Impact Assessment (Art. 35) | Required if high-risk processing | 🟡 Important |
| Cross-border transfer mechanism (Art. 46) | SCCs or adequacy decision | 🔴 Critical |
| Data breach notification (Art. 33) | 72-hour process documented | 🟡 Important |

> ⚠️ Research output is for informational purposes. Not legal advice. Verify with qualified counsel.
