---
name: legal-compliance-everyone-needs-a-copilot
title: Legal Compliance Skill
description: Multi-framework compliance gap analysis. Use for GDPR, CCPA, ADA or WCAG, PCI-DSS, SOC 2, HIPAA, Colorado Privacy Act, Colorado AI Act, CJIS, applicability assessment, controls, and remediation plans.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/legal-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Legal Compliance Skill

Compliance analysis starts with applicability. Most frameworks do not apply to every engagement. The first question is always: does this framework apply here? The second question is: if it applies, where are the gaps?

---

## Framework Applicability Matrix

Apply this matrix to every new engagement. Check which frameworks trigger:

| Framework | Triggers When |
|-----------|--------------|
| GDPR | EU/EEA residents' personal data is processed |
| CCPA/CPRA | California residents' personal data is processed at scale |
| ADA / WCAG 2.1 | Deliverables are digital and accessible by government employees or public |
| PCI-DSS | Payment card data is in scope (rare for ENAC) |
| SOC 2 | ENAC stores or processes client data in cloud systems (vendor diligence) |
| HIPAA | Client touches health/human services, behavioral health, or insurance |
| Colorado Privacy Act (CPA) | Colorado residents' personal data is processed; any CO government engagement |
| Colorado AI Act (SB 24-205) | AI tools used in any CO engagement (effective Feb 1, 2026) |
| CJIS | Engagement touches sheriff, courts, DA, or any criminal justice system |

---

## Framework-by-Framework Analysis

### GDPR (EU General Data Protection Regulation)

**Typical ENAC applicability:** Low. Only triggers if a Colorado government client has operations processing EU resident data (e.g., an international workforce). Confirm scope before starting analysis.

**Key obligations if applicable:**
- Lawful basis for processing personal data (Article 6)
- Data subject rights: access, rectification, erasure, portability, objection
- Data Protection Impact Assessment for high-risk processing (Article 35)
- Data Processing Agreement with any processor (Article 28)
- Breach notification within 72 hours (Article 33)
- Data minimization and purpose limitation

**Gap checklist:**
- [ ] Lawful basis documented for each processing activity
- [ ] Privacy notice in place and accessible
- [ ] Data subject rights requests process exists
- [ ] DPAs executed with all processors
- [ ] Breach response plan in place

---

### CCPA / CPRA (California Consumer Privacy Act / Privacy Rights Act)

**Typical ENAC applicability:** Low. Only triggers if ENAC processes California residents' personal data at scale (>100K consumers/year or revenue from data sale). Unlikely for typical engagements.

**Key obligations if applicable:**
- Notice at collection
- Right to know, delete, correct, opt-out of sale
- Do Not Sell / Do Not Share obligations
- Service provider agreement (parallel to GDPR Article 28)

---

### ADA / WCAG 2.1 AA

**Typical ENAC applicability:** HIGH. Every deliverable submitted to a Colorado government entity.

**Key obligations:**
- **C.R.S. § 24-85-103:** All state and local government digital content must meet WCAG 2.1 AA.
- Adams County PSA §15: Accessibility compliance indemnification: ENAC is liable for inaccessible deliverables.

**WCAG 2.1 AA requirements for ENAC deliverables:**

| Principle | Key Requirements |
|-----------|----------------|
| Perceivable | Alt text for images; captions for audio/video; content viewable without color alone |
| Operable | All functions keyboard accessible; no seizure-inducing content |
| Understandable | Language identified; consistent navigation; error identification |
| Robust | Valid HTML/document structure; accessible name for all UI components |

**Document-specific checklist:**
- [ ] Heading hierarchy (H1 > H2 > H3, never skip levels, never use bold as a heading)
- [ ] Alt text for all images, charts, and graphics
- [ ] Logical reading order (check with Accessibility Checker in Word/Acrobat)
- [ ] Color contrast: 4.5:1 for normal text, 3:1 for large text (18pt or 14pt bold)
- [ ] No color as the only means of conveying meaning (e.g., red/green status without a shape or label)
- [ ] Linked text describes the destination (not "click here")
- [ ] Table headers identified as headers
- [ ] Document language specified in file properties

**Tools:** Microsoft Accessibility Checker (Word, PowerPoint), Adobe Acrobat Accessibility Check, WebAIM Contrast Checker.

---

### HIPAA (Health Insurance Portability and Accountability Act)

**Typical ENAC applicability:** MEDIUM. Triggers when engagement scope includes county health/human services, behavioral health, insurance, or any system containing Protected Health Information (PHI).

**Key threshold:** Is ENAC a Business Associate (BA)? If ENAC accesses, uses, or discloses PHI on behalf of a Covered Entity, a Business Associate Agreement (BAA) is required before the engagement begins.

**Required if applicable:**
- Sign a BAA with the covered entity before engaging with PHI
- Implement minimum necessary access controls
- Report HIPAA breaches within 60 days of discovery
- Restrict PHI use to only what is specified in the BAA

**Gap checklist:**
- [ ] BAA executed before any PHI access
- [ ] PHI access limited to minimum necessary
- [ ] PHI transmission encrypted
- [ ] Breach notification process in place
- [ ] PHI included in engagement-end disposal plan

**Action:** Escalate to human counsel for HIPAA engagements before proceeding.

---

### Colorado Privacy Act (CPA): C.R.S. 6-1-1301

**Typical ENAC applicability:** MEDIUM-HIGH. Applies when ENAC processes personal data of Colorado residents. Most government engagements involve some PII from interviews, assessments, or data analysis.

**Key obligations:**
- Notice of data processing
- Data minimization
- Data subject rights (access, deletion, correction, portability, opt-out of targeted advertising)
- Data protection assessment for high-risk processing (profiling, selling data, sensitive data)
- Processor agreements with vendors who process personal data on ENAC's behalf

**Gap checklist:**
- [ ] Privacy notice provided to individuals whose data is processed
- [ ] Data minimization: only collect what is needed
- [ ] Processor agreements with AI vendors and cloud services
- [ ] Data subject rights response process exists
- [ ] Data protection assessment completed for high-risk activities
- [ ] Retention and disposal schedule defined

---

### Colorado AI Act (SB 24-205)

**Effective February 1, 2026.** See `colorado-ai-act` skill for full compliance guide.

**Quick applicability check:**
- Is ENAC using AI tools in this engagement? Yes (assume yes unless no AI used)
- Is this a high-risk AI use? Assess per the Act's consequential decision definition
- Are Deployer obligations met? Risk management program, impact assessment, disclosure

---

### CJIS Security Policy (FBI Criminal Justice Information Services)

**Typical ENAC applicability:** LOW but CRITICAL when triggered. Triggers when engagement touches sheriff, courts, DA, probation, parole, or any system that accesses CHRI (Criminal History Record Information).

**Action:** Do not start any engagement in CJIS scope without escalating to human counsel. CJIS compliance requires a formal security program, background checks, and specific technical controls that go far beyond typical consulting practice.

**Gap checklist:**
- [ ] CJIS scope confirmed or excluded before engagement start
- [ ] CJIS Security Policy Addendum signed if in scope
- [ ] Personnel security screening completed (fingerprinting may be required)
- [ ] Technical controls: encryption, access control, audit logging
- [ ] Legal counsel review completed

---

## Compliance Output Structure

1. **Applicability matrix**: Which frameworks apply to this engagement, and why
2. **Framework-by-framework gap analysis**: For each applicable framework: current state, gaps, remediation steps
3. **Critical escalations**: HIPAA and CJIS items requiring human counsel before proceeding
4. **Compliance calendar**: Annual renewal obligations (WCAG, CPA, CO AI Act impact assessment)
5. **Vendor compliance status**: AI tools and cloud services cleared for applicable frameworks

---

## Anti-Generic Rules

- NEVER start a HIPAA-scope engagement without a BAA
- NEVER start a CJIS-scope engagement without human counsel review
- NEVER skip WCAG for Colorado government deliverables: it is a legal requirement and an indemnification risk
- NEVER assume GDPR does not apply without confirming the client's data scope
- NEVER conflate Colorado Privacy Act with CCPA: they are different laws with different thresholds
