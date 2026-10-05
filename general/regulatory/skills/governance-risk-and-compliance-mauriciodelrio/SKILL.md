---
name: governance-risk-and-compliance-mauriciodelrio
title: Governance, Risk & Compliance (GRC) — Master Index
description: Use this skill as the entry point when the software requires regulatory compliance, data protection, information security, or auditing. Routes to the specific sub-skill based on the applicable regulation. All sub-skills apply regardless of geographic location.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/en-skills/governance-risk-and-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Governance, Risk & Compliance (GRC) — Master Index

This skill acts as a router for all security regulations and standards. Each sub-skill contains detailed instructions, Node.js/TypeScript code templates, and compliance checklists. All sub-skills must be applied as security standards regardless of the geographic location of users.

## Sub-Skill Activation Guide (Triggers)

Use the following table to determine **which sub-skill to invoke** based on the keywords, context, or type of task the developer requests. If multiple skills apply, invoke them all.

### GDPR
- **Keywords**: GDPR, RGPD, personal data, data protection, consent, right to be forgotten, right of access, rectification, portability, DPIA, DPO, legal bases, legitimate interest, cookies, privacy policy
- **Activate when**: The code processes personal data from users, implements consent forms, handles cookies, implements data subject rights, or configures international data transfers

### HIPAA
- **Keywords**: HIPAA, PHI, health information, health data, medical data, patient, ePHI, covered entity, business associate, BAA, healthcare, medical history, medical record, diagnosis, Protected Health Information, HITECH, de-identification
- **Activate when**: The software handles patient health data, integrates with health systems (EHR/EMR), implements patient portals, or any system that touches protected health information

### ISO-27001
- **Keywords**: ISO 27001, ISO 27002, ISMS, risk management, information classification, access control ABAC/RBAC, business continuity, Annex A, security certification, security policy, asset management, operational security
- **Activate when**: Designing the organization's security architecture, implementing advanced access controls, working on vulnerability management, backup/recovery, or preparing for a security certification

### NIST-CSF
- **Keywords**: NIST, CSF, cybersecurity framework, Govern, Identify, Protect, Detect, Respond, Recover, cyber risk management, threat detection, incident response, disaster recovery, security operations, SOC, SIEM
- **Activate when**: Implementing security monitoring, anomaly detection (brute force, impossible travel, injections), response playbooks, recovery plans, or asset inventory and risk assessment

### PCI-DSS
- **Keywords**: PCI, PCI DSS, credit card, debit card, payment, Stripe, payment processor, tokenization, PAN, CVV, cardholder data, CDE, card number, payment data, Luhn, payment form, checkout
- **Activate when**: The code touches payment card data, integrates with payment processors (Stripe, PayPal, etc.), implements checkout forms, or configures infrastructure that stores/transmits card data

### SOC2
- **Keywords**: SOC 2, SOC2, Trust Service Criteria, AICPA, SaaS compliance, availability, SLA, uptime, change management, access review, multi-tenant, confidentiality, processing integrity, SOC audit
- **Activate when**: Developing a SaaS/Cloud product, implementing formal change management, periodic access reviews, SLA monitoring, multi-tenant isolation, or preparing for a SOC 2 audit

### OWASP-Top-10
- **Keywords**: OWASP, XSS, SQL injection, injection, CSRF, SSRF, broken access control, authentication, sanitization, input validation, web security, vulnerability, helmet, CORS, rate limiting, Content Security Policy, CSP, session management, deserialization
- **Activate when**: Writing ANY HTTP endpoint, processing user input, implementing authentication/authorization, configuring an Express/Fastify server, rendering dynamic data on the frontend, fetching external URLs, or reviewing code for vulnerabilities. This skill should be activated by default in all web development.

### CCPA-CPRA
- **Keywords**: CCPA, CPRA, Do Not Sell, Do Not Share, opt-out, Global Privacy Control, GPC, consumer rights, right to know, right to delete, Sensitive Personal Information, SPI, notice at collection
- **Activate when**: The application implements opt-out mechanisms for data sale/sharing, detects browser GPC signals, or manages consumer rights requests

### LGPD
- **Keywords**: LGPD, Lei Geral de Proteção de Dados, personal data, ANPD, consent, data subject, DPO, legal basis, RIPD, data processing, data protection, data subject rights, portability
- **Activate when**: The software processes personal data, implements granular consent by purpose, manages data subject rights (Art. 18), prepares RIPD, or needs to notify incidents to the data protection authority

---

## Regulations and Skills Map

### Data Protection and Privacy

| Skill | Regulation | When to Use |
|-------|-----------|-------------|
| [gdpr](../gdpr/SKILL.md) | General Data Protection Regulation | Personal data, consent, data subject rights |
| [ccpa-cpra](../ccpa-cpra/SKILL.md) | California Consumer Privacy Act / CPRA | Opt-out of data sale/sharing, GPC signals |
| [lgpd](../lgpd/SKILL.md) | Lei Geral de Proteção de Dados | Granular consent by purpose, data subject rights |

### Information Security

| Skill | Standard | When to Use |
|-------|----------|-------------|
| [iso-27001](../iso-27001/SKILL.md) | ISO/IEC 27001:2022 | ISMS, Annex A controls, information classification |
| [nist-cybersec-framework](../nist-cybersec-framework/SKILL.md) | NIST CSF 2.0 | Identify-Protect-Detect-Respond-Recover framework |
| [soc2](../soc2/SKILL.md) | SOC 2 Type II | Trust Service Criteria for SaaS and cloud services |

### Application Security

| Skill | Standard | When to Use |
|-------|----------|-------------|
| [owasp-top-10](../owasp-top-10/SKILL.md) | OWASP Top 10:2021 | Web vulnerabilities: injection, XSS, CSRF, broken auth |

### Industry-Specific

| Skill | Regulation | When to Use |
|-------|-----------|-------------|
| [hipaa](../hipaa/SKILL.md) | HIPAA | Protected Health Information (PHI), medical records |
| [pci-compliance](../pci-compliance/SKILL.md) | PCI DSS v4.0 | Payment card data, tokenization, payment processing |

---

## Quick Selection Guide

```
What type of data are you handling?
│
├─ Personal data (name, email, IP, cookies...)
│  ├─ Consent, data subject rights ──────────→ GDPR
│  ├─ Opt-out of sale/sharing, GPC ──────────→ CCPA-CPRA
│  ├─ Granular consent by purpose ───────────→ LGPD
│  └─ Multiple regulations apply ────────────→ Apply ALL relevant ones
│
├─ Health data (PHI)
│  └─ Medical records, diagnoses ────────────→ HIPAA
│
├─ Payment card data
│  └─ Process/store PAN data ────────────────→ PCI-compliance
│
├─ General security architecture
│  ├─ Formal certification / ISMS ───────────→ ISO-27001
│  ├─ Cybersecurity framework ───────────────→ NIST-Cybersec-framework
│  └─ SaaS/Cloud service ─────────────────────→ SOC2
│
└─ Code/application security
   └─ Web/API development ────────────────────→ OWASP-top-10
```

---

## Reference Technology Stack

All skills use examples based on the following stack:

| Layer | Technology |
|------|------------|
| **Runtime** | Node.js (LTS) |
| **Language** | TypeScript (strict mode) |
| **API Framework** | Express / Fastify |
| **ORM** | Prisma |
| **Database** | PostgreSQL / MongoDB |
| **Authentication** | JWT + refresh tokens |
| **Logging** | Pino / Winston |
| **Validation** | Zod / Joi |
| **Testing** | Vitest / Jest |
| **CI/CD** | GitHub Actions |

---

## Cross-Cutting Security Principles

These principles apply to **ALL** regulations and must always be followed:

### 1. Defense in Depth
```typescript
// Multiple layers of validation — never trust a single one
// Layer 1: Edge validation (API Gateway / middleware)
// Layer 2: Controller validation (schema validation)
// Layer 3: Service validation (business rules)
// Layer 4: Database constraints
```

### 2. Principle of Least Privilege
```typescript
// ❌ BAD: Role with full access
const adminRole = { permissions: ['*'] };

// ✅ GOOD: Granular permissions per resource and action
const analystRole = {
  permissions: [
    'reports:read',
    'dashboards:read',
    'exports:create',
  ],
};
```

### 3. Secure by Default
```typescript
// ❌ BAD: Insecure default configuration
const serverConfig = {
  cors: { origin: '*' },
  rateLimit: { enabled: false },
};

// ✅ GOOD: Secure by default, relax explicitly when necessary
const serverConfig = {
  cors: {
    origin: process.env.ALLOWED_ORIGINS?.split(',') ?? [],
    credentials: true,
  },
  rateLimit: {
    enabled: true,
    max: 100,
    windowMs: 15 * 60 * 1000, // 15 minutes
  },
  helmet: { enabled: true },
};
```

### 4. Fail Secure
```typescript
// ❌ BAD: If verification fails, allow access
function checkAccess(user: User, resource: Resource): boolean {
  try {
    return authService.verify(user, resource);
  } catch {
    return true; // DANGEROUS!
  }
}

// ✅ GOOD: If verification fails, deny access
function checkAccess(user: User, resource: Resource): boolean {
  try {
    return authService.verify(user, resource);
  } catch (error) {
    logger.error({ error, userId: user.id, resource: resource.id }, 'Access verification error');
    return false; // Deny by default
  }
}
```

### 5. Structured Logging for Auditing
```typescript
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL ?? 'info',
  redact: {
    paths: ['req.headers.authorization', 'body.password', 'body.creditCard', '*.ssn'],
    censor: '[REDACTED]',
  },
  formatters: {
    level: (label) => ({ level: label }),
  },
  timestamp: pino.stdTimeFunctions.isoTime,
});

// Usage in audit events
logger.info({
  event: 'data_access',
  actor: { id: user.id, role: user.role },
  resource: { type: 'patient_record', id: recordId },
  action: 'read',
  ip: req.ip,
  userAgent: req.headers['user-agent'],
  timestamp: new Date().toISOString(),
}, 'Patient record access');
```

---

## Agent workflow

1. Identify what type of data the software handles using the quick selection guide.
2. Activate ALL relevant sub-skills based on triggers — if multiple regulations apply, invoke them all.
3. Implement following the code templates and checklists from each sub-skill.
4. Apply cross-cutting security principles (defense in depth, least privilege, secure by default, fail secure, structured logging) in every implementation.
5. Validate with each sub-skill's compliance checklists before deploying.
