---
name: contract-lifecycle-judicialmind
title: Contract Lifecycle Management
description: Contract lifecycle management skill. Use when the user needs to draft contracts, review agreements, extract obligations, analyze risk, redline documents, or manage contract workflows. Triggers on keywords like "contract", "agreement", "draft", "redline", "clause", "NDA", "MSA", "terms", "obligations", "contract review", "playbook".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/contract-lifecycle
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
sources:
- title: Clause Library
  path: references/clause-library.md
- title: Playbook Template
  path: references/playbook-template.md
- title: Risk Matrix
  path: references/risk-matrix.md
---

# Contract Lifecycle Management

This skill provides expert guidance for all phases of contract management from drafting through execution and renewal.

## Core Capabilities

### 1. Contract Drafting
- Template selection and customization
- Clause library management
- Version control best practices
- Collaborative drafting workflows

### 2. Contract Review & Redlining
- Risk identification
- Deviation from standard analysis
- Redline generation
- Negotiation strategy

### 3. Obligation Extraction
- Key date identification
- Performance obligations
- Payment terms
- Termination triggers

### 4. Risk Scoring
- Clause-by-clause risk analysis
- Industry-standard benchmarking
- Deviation flagging
- Severity classification

## Contract Types

### Commercial Agreements
| Type | Key Provisions | Risk Areas |
|------|----------------|------------|
| NDA/Confidentiality | Definition, term, exceptions | Carve-outs, remedies |
| MSA | Scope, SLAs, liability | Indemnity, IP |
| SaaS/License | Subscription, data, termination | Auto-renewal, data portability |
| Services | SOW, deliverables, acceptance | Change orders, warranties |
| Supply/Purchase | Quantity, price, delivery | Force majeure, warranties |

### Corporate Agreements
| Type | Key Provisions | Risk Areas |
|------|----------------|------------|
| Shareholder | Governance, transfer, exit | Drag-along, anti-dilution |
| Employment | Compensation, termination, IP | Non-compete, severance |
| Partnership | Contributions, distributions | Fiduciary, dissolution |
| Joint Venture | Structure, management, exit | Deadlock, IP ownership |

## Review Framework

### Systematic Review Process
```
┌─────────────────────────────────────────────────┐
│  1. Initial Scan                                 │
│     - Parties and effective date                 │
│     - Term and termination                       │
│     - Governing law and jurisdiction             │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  2. Risk Assessment                              │
│     - Indemnification scope                      │
│     - Liability caps and exclusions              │
│     - IP ownership and licenses                  │
│     - Data protection obligations                │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  3. Obligation Mapping                           │
│     - Performance requirements                   │
│     - Payment milestones                         │
│     - Reporting duties                           │
│     - Renewal/termination dates                  │
└─────────────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│  4. Negotiation Priorities                       │
│     - Must-have changes                          │
│     - Nice-to-have improvements                  │
│     - Acceptable as-is provisions                │
└─────────────────────────────────────────────────┘
```

## Key Clause Analysis

### Indemnification
**Standard Elements**:
- Scope of covered claims
- Notice requirements
- Control of defense
- Limitation tie-in

**Risk Factors**:
- [ ] Unlimited indemnity
- [ ] IP infringement without knowledge qualifier
- [ ] Third-party claims beyond customer's control
- [ ] No mutual indemnification

### Limitation of Liability
**Standard Structure**:
```
Exclusion of consequential damages
Cap on direct damages (typically 12 months fees)
Carve-outs (indemnity, IP, confidentiality, gross negligence)
```

**Risk Factors**:
- [ ] No cap on liability
- [ ] Asymmetric caps (higher exposure for one party)
- [ ] Broad carve-outs that swallow the cap
- [ ] No exclusion of consequential damages

### Intellectual Property
**Key Issues**:
- Pre-existing IP ownership
- Work product ownership
- License grants (scope, exclusivity, term)
- Background vs. foreground IP

### Termination
**Review Points**:
- Termination for convenience (notice period)
- Termination for cause (cure period)
- Effect of termination (survival, wind-down)
- Return/destruction of materials

## Risk Scoring Matrix

| Risk Level | Score | Action |
|------------|-------|--------|
| Critical | 5 | Must negotiate, escalate |
| High | 4 | Strongly recommend change |
| Medium | 3 | Request change |
| Low | 2 | Flag for awareness |
| Acceptable | 1 | No action needed |

### Scoring Criteria
- **Financial exposure**: Potential monetary impact
- **Legal risk**: Compliance, enforceability concerns
- **Operational impact**: Business disruption potential
- **Reputational risk**: Brand/relationship implications

## Playbook Integration

### Fallback Positions
For each risky clause, maintain:
1. **Preferred position**: Standard language
2. **Acceptable fallback**: Compromise language
3. **Walk-away point**: Non-negotiable threshold

### Approval Matrix
| Change Type | Approval Required |
|-------------|-------------------|
| Standard terms | Self-approve |
| Minor deviations | Legal lead |
| Material deviations | General counsel |
| Deal-specific terms | Business + Legal |

## Best Practices

### Drafting
- Start from approved templates
- Use defined terms consistently
- Include version control headers
- Maintain clause library with alternatives

### Review
- Use systematic checklist approach
- Compare against playbook positions
- Document all redlines with rationale
- Track negotiation history

### Execution
- Verify signature authority
- Confirm all exhibits attached
- Record effective dates
- Establish obligation tracking

## Integration with Other Skills

- **corporate-ma**: Transaction documents
- **due-diligence**: Contract review in M&A
- **compliance-tracking**: Regulatory requirements in contracts
- **e-discovery**: Contract-related disputes

## Reference Files

For detailed clause libraries and templates:
- `references/clause-library.md` - Standard clause alternatives
- `references/risk-matrix.md` - Detailed risk scoring guide
- `references/playbook-template.md` - Contract playbook format
