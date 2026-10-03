---
name: colorado-ai-act
title: Colorado AI Act Compliance Skill
description: Colorado AI Act compliance guide for ENAC. Use for AI governance, high-risk AI assessment, deployer obligations, human review checkpoints, government engagement AI disclosure, and Colorado SB 24-205 analysis.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/colorado-ai-act
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Colorado AI Act Compliance Skill

The Colorado AI Act (SB 24-205) is in effect. As of February 1, 2026, ENAC has compliance obligations for every government engagement where AI tools are used in ways that affect consequential decisions. This skill is the compliance guide.

---

## Key Facts

**Name:** Colorado Artificial Intelligence Act (SB 24-205)
**Effective date:** February 1, 2026: already in effect
**Enforcer:** Colorado Attorney General
**Civil penalties:** Up to $20,000 per violation; up to $100,000 per knowing or reckless violation
**Safe harbor:** A developer or deployer is not liable if they made reasonable efforts to comply, including developing and following a risk management policy

---

## Who Does the Act Cover

### Developers
Companies that create, code, produce, or intentionally and substantially modify a high-risk AI system.
**ENAC as developer?** Unlikely unless ENAC is building AI systems for clients. ENAC uses AI tools (Claude, etc.) but does not typically build them.

### Deployers
Companies that use a high-risk AI system in Colorado to make, or substantially assist in making, a consequential decision.
**ENAC as deployer?** YES: when ENAC uses AI tools (Claude API, other AI analysis tools) to make or substantially assist in making decisions that have material effects on individuals in the categories listed below.

---

## High-Risk AI System Definition

A high-risk AI system is one that makes or substantially assists in making a "consequential decision."

**Consequential decision** = a decision with a material effect on an individual's:
- Access to or the cost or terms of education or vocational training
- Employment or employment opportunities
- Essential government services
- Financial services (credit, insurance, housing, loans)
- Healthcare services
- Housing
- Legal services or processes
- Access to places of public accommodation

---

## ENAC Risk Assessment: Is Organizational Consulting High-Risk?

Apply this framework to every engagement scope at the start of the project.

### Scenario Analysis

**Scenario A: Likely Lower Risk:**
ENAC uses AI to synthesize interview responses, draft sections of a report, or organize findings into themes. A human consultant reviews, edits, validates, and presents the report. The client then makes its own decisions based on the report.

*Assessment:* AI is substantially assisting in producing a product that humans review. The AI is not making the consequential decision: the human consultant and client are. Lower risk if the human review is genuine and documented.

**Scenario B: Potentially High-Risk:**
ENAC uses AI to analyze employee survey data and produce staffing recommendations (who to keep, who to cut, which roles to restructure). These recommendations go directly to a government client's HR function and are used with limited human review to make employment decisions.

*Assessment:* AI is substantially assisting in making employment decisions. This is likely a high-risk use. Deployer obligations apply.

**Scenario C: Higher Risk:**
ENAC deploys an AI system that processes resident data and produces eligibility recommendations for a county social services program (e.g., which families qualify for assistance).

*Assessment:* Clearly high-risk. AI is substantially assisting in decisions about essential government services and financial services. Full deployer obligations apply; escalate to `@legal-ai-gov` and human counsel.

### ENAC's Default Posture

**Conservative:** Treat any AI-assisted analysis that affects personnel decisions or government service delivery as potentially high-risk until assessed otherwise. The safe harbor requires "reasonable efforts to comply": a conservative posture at the assessment stage is the foundation of that defense.

---

## Deployer Obligations Under the Colorado AI Act

If ENAC is a deployer using a high-risk AI system, these obligations apply:

### 1. Risk Management Program
Implement a risk management program that uses reasonable care to protect individuals from known or reasonably foreseeable risks of algorithmic discrimination.

**Recommended standard:** NIST AI RMF 1.0 (the Act specifically references it). ENAC's risk management program should document:
- How AI tools are used in client engagements
- How risks of algorithmic discrimination are identified and mitigated
- Human review checkpoints for all AI-assisted analysis
- Override mechanisms (humans can and do override AI findings)
- Annual review process

### 2. Impact Assessment
Conduct an impact assessment before deploying a high-risk AI system in a new context.

**Document for each high-risk use:**
- Description of the AI system and its purpose
- Categories of personal data used
- Potential risks of algorithmic discrimination
- Mitigation measures implemented
- Residual risk assessment
- Human oversight mechanisms

**Review annually** and whenever the AI system or its use materially changes.

### 3. Individual Notification
Notify individuals when a high-risk AI system is used to make or substantially assist in making a consequential decision about them.

**In an ENAC government engagement context:** If the engagement involves AI analysis that contributes to decisions affecting specific individuals (employees, residents, program participants), those individuals must be notified.

**Practical guidance:** Include AI disclosure in the engagement's communications to affected individuals, or in the deliverable document itself.

### 4. Meaningful Explanation
If requested, provide a meaningful explanation of the consequential decision, including the role AI played.

**ENAC's requirement:** Document which findings in each deliverable were AI-assisted so that a meaningful explanation can be provided if requested.

### 5. Human Review and Override
Provide individuals the ability to seek human review of a consequential decision made by a high-risk AI system.

**ENAC's mechanism:** All AI-assisted analysis is reviewed and validated by a qualified human consultant. The deliverable represents the consultant's judgment, not the AI's output. Document this clearly in every engagement.

### 6. Annual Impact Assessment Review
Review impact assessments at least annually and after any material change to the high-risk AI system.

---

## Required Proposal AI Disclosure Language

Include in every proposal to a Colorado government client. Customize as needed based on the specific AI use in the engagement.

**Standard version:**
> "This engagement utilizes AI-assisted analysis tools to support research, data synthesis, and report drafting. All AI-generated analysis is reviewed, validated, and approved by qualified human consultants before inclusion in any deliverable or recommendation. Human judgment governs all findings and recommendations. [ENAC's full legal name] complies with the Colorado Artificial Intelligence Act (SB 24-205) and maintains a risk management program consistent with NIST AI RMF 1.0."

**Enhanced version (for higher-risk engagements):**
> "This engagement utilizes AI-assisted analysis tools to support [specific use: e.g., organizational data synthesis, interview transcript analysis, benchmarking]. ENAC has conducted an impact assessment of this AI use consistent with the Colorado Artificial Intelligence Act (SB 24-205). All AI-generated analysis is reviewed, validated, and approved by qualified human consultants before inclusion in any deliverable or recommendation. Human judgment governs all findings, recommendations, and actions arising from this engagement. Individuals may request a human review of any recommendation or finding. ENAC maintains a risk management program consistent with NIST AI RMF 1.0."

---

## GSA GSAR 552.239-7001 Federal Watch

For engagements involving federal grant funding (HUD, FEMA, HHS, DOL, DOE, DOT flowing through Colorado state or local government):

**The issue:** A proposed federal acquisition regulation clause (GSA GSAR 552.239-7001, published in draft March 2026) attempts to vest the federal government with ownership of all AI inputs and outputs for work performed on federally-funded contracts. This would include ENAC's AI-generated analysis and, potentially, the prompts and configurations used to produce it.

**Current status (as of May 2026):** Not yet finalized. Monitor acquisition.gov for final rule publication.

**If this clause appears in any RFP or contract:**
- Do not sign without escalating to `@legal-ip` and human counsel
- The clause directly conflicts with ENAC's Background IP carve-out for AI system configurations and prompts
- Assess whether the engagement can be structured to avoid triggering the clause (e.g., deliverables only, no AI tool access to the government)

**Interim strategy:** For any federally-funded contract, ensure the contract does not assign AI-generated analysis to the client beyond the deliverables themselves. Background IP (including prompts and configurations) must remain with ENAC.

---

## AI Vendor Terms Verification

Before using any AI tool on a government engagement, confirm the following. Review annually.

| Vendor | Check | Status |
|--------|-------|--------|
| Anthropic / Claude API | Data not used for model training | Confirmed in API terms (2024+): re-verify annually |
| Anthropic / Claude API | US-based data processing | Confirm current terms |
| Anthropic / Claude API | Government data processing permitted | Confirm commercial terms |
| Figma (collaboration) | Data handling for government content | Confirm Figma Enterprise terms |
| Any new AI tool | Data residency, training data use, government permissions | Verify before first use |

**Documentation requirement:** Record vendor clearance status in the engagement file. Update when vendor terms change.

---

## Internal Documentation Requirements

For every engagement using AI tools, maintain this documentation in the engagement file:

```
Engagement: [Name]
Date range: [Start] to [End]
Colorado AI Act applicability: [High-risk / Lower risk / Assessment rationale]

AI Tools Used:
- Tool: [Name and version]
  Purpose: [What it was used for]
  Data processed: [Types of data: no PII in this record]
  Vendor clearance confirmed: [Yes / Date]

Human Review Checkpoints:
- [Deliverable name]: reviewed by [initials] on [date]
- [Deliverable name]: reviewed by [initials] on [date]

Impact Assessment:
- Completed: [Yes/No/Date]
- High-risk determination: [Yes/No]
- Mitigation measures: [Brief description]
- Residual risk: [Acceptable/Escalated]

AI Disclosure:
- Included in proposal: [Yes/No]
- Version used: [Standard/Enhanced]
- Individual notification required: [Yes/No: if yes, confirm how handled]

Annual review date: [Date]
```

---

## Anti-Generic Rules

- NEVER start a post-February-2026 government engagement without completing the Colorado AI Act applicability assessment
- NEVER include AI disclosure in a proposal as boilerplate without confirming the specific AI use matches the disclosure language
- NEVER use an AI vendor on a government engagement without confirming vendor terms are cleared
- NEVER accept a GSA GSAR 552.239-7001 clause (or substantially similar language) without escalating to human counsel
- NEVER skip the impact assessment for engagements where AI is used to assist decisions about employment or government services
