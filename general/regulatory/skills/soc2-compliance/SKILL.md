---
name: soc2-compliance
title: SOC2 Type II Compliance
description: SOC2 Type II compliance - Trust Service Criteria, access controls, audit logging, change management, incident response, evidence collection
author: vibeeval
author_url: https://github.com/vibeeval/vibecosystem/tree/main/skills/soc2-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# SOC2 Type II Compliance

## Trust Service Criteria (TSC)

### 1. Security (Common Criteria - CC)

| Control | Requirement | Implementation |
|---------|-------------|----------------|
| CC1.1 | COSO principles | Documented security policies |
| CC2.1 | Information communication | Security awareness training |
| CC3.1 | Risk assessment | Annual risk assessment process |
| CC5.1 | Control activities | Technical + administrative controls |
| CC6.1 | Logical access | RBAC, MFA, least privilege |
| CC6.2 | Auth mechanisms | SSO, password policy, key rotation |
| CC6.3 | Access revocation | Automated deprovisioning |
| CC7.1 | Threat detection | IDS/IPS, SIEM, vulnerability scanning |
| CC7.2 | System monitoring | Real-time alerting, log aggregation |
| CC7.3 | Incident evaluation | Severity classification, escalation |
| CC7.4 | Incident response | Documented IR plan, tabletop exercises |
| CC8.1 | Change management | PR review, CI/CD gates, rollback plan |
| CC9.1 | Risk mitigation | Business continuity, DR plan |

### 2. Availability (A)

- [ ] SLA definitions (99.9%, 99.99%)
- [ ] Uptime monitoring (health checks, synthetic monitoring)
- [ ] Disaster recovery plan tested annually
- [ ] Capacity planning documented
- [ ] Failover procedures tested
- [ ] Backup verification (restore tests quarterly)

### 3. Processing Integrity (PI)

- [ ] Input validation on all data entry points
- [ ] Data processing accuracy checks
- [ ] Error handling and correction procedures
- [ ] Output reconciliation
- [ ] Transaction logging with checksums

### 4. Confidentiality (C)

- [ ] Data classification policy (Public, Internal, Confidential, Restricted)
- [ ] Encryption at rest (AES-256)
- [ ] Encryption in transit (TLS 1.2+)
- [ ] Key management procedures (rotation, revocation)
- [ ] Confidential data access logging
- [ ] NDA tracking for third parties

### 5. Privacy (P)

- [ ] Privacy notice published
- [ ] Consent collection mechanism
- [ ] Data subject request handling (30 gun)
- [ ] Data retention and disposal schedule
- [ ] Third-party data sharing agreements

## Access Control Checklist

### Authentication

```typescript
// MFA enforcement middleware
async function requireMFA(req: Request, res: Response, next: NextFunction) {
  const user = req.user;
  if (!user) return res.status(401).json({ error: 'Unauthenticated' });

  if (!user.mfaVerified) {
    await auditLog({
      action: 'auth.mfa.required',
      actor: user.id,
      resource: req.path,
      result: 'blocked',
    });
    return res.status(403).json({ error: 'MFA verification required' });
  }
  next();
}
```

### Authorization (RBAC)

```typescript
interface Permission {
  resource: string;
  action: 'read' | 'write' | 'delete' | 'admin';
}

interface Role {
  name: string;
  permissions: Permission[];
}

function checkPermission(user: User, resource: string, action: string): boolean {
  const role = getRoleByName(user.role);
  const hasPermission = role.permissions.some(
    (p) => p.resource === resource && p.action === action
  );

  auditLog({
    action: `authz.${action}.${hasPermission ? 'granted' : 'denied'}`,
    actor: user.id,
    resource,
  });

  return hasPermission;
}
```

### Access Review Checklist

- [ ] Quarterly access reviews for all systems
- [ ] Terminated employee access revoked within 24 hours
- [ ] Privileged access requires manager approval
- [ ] Service account inventory maintained
- [ ] API key rotation schedule (90 gun max)
- [ ] SSH key inventory and rotation

## Audit Logging Requirements

### What to Log (ZORUNLU)

| Event Category | Examples | Retention |
|---------------|----------|-----------|
| Authentication | Login, logout, MFA, password reset | 1 yil |
| Authorization | Permission grants, denials, role changes | 1 yil |
| Data access | PII reads, exports, downloads | 1 yil |
| Data modification | Create, update, delete operations | 1 yil |
| System events | Config changes, deployments, restarts | 1 yil |
| Admin actions | User management, policy changes | 3 yil |

### Log Format

```typescript
interface AuditLogEntry {
  id: string;               // UUID
  timestamp: string;         // ISO 8601
  action: string;           // 'user.login.success'
  actor: {
    id: string;
    email: string;
    ip: string;
    userAgent: string;
  };
  resource: {
    type: string;           // 'user', 'document', 'config'
    id: string;
    name?: string;
  };
  result: 'success' | 'failure' | 'error';
  details?: Record<string, unknown>;
  correlationId?: string;   // Request tracing
}

async function writeAuditLog(entry: AuditLogEntry): Promise<void> {
  // Append-only, tamper-evident storage
  await auditStore.append({
    ...entry,
    hash: computeHash(entry),  // Chain hash for integrity
  });
}
```

### Anti-Patterns

| Anti-Pattern | Neden Yanlis | Dogru Yol |
|-------------|-------------|-----------|
| Logging PII in plaintext | Data exposure riski | Mask/hash sensitive fields |
| Mutable audit logs | Tampering riski | Append-only, immutable store |
| No correlation ID | Trace edilemez | Her request'e UUID ata |
| Missing failure logs | Saldiri tespiti zorlasiyor | Basarisiz denemeleri de logla |
| Client-side only logging | Manipule edilebilir | Server-side zorunlu |

## Change Management

### Change Request Template

```markdown
## Change Request

**Requester:** [isim]
**Date:** [tarih]
**Priority:** [P0-P3]
**Type:** [Standard | Emergency | Normal]

### Description
[Ne degisecek]

### Impact Assessment
- Affected systems: [liste]
- Affected users: [kac kisi, hangi roller]
- Risk level: [Low | Medium | High | Critical]
- Rollback plan: [nasil geri alinir]

### Approval
- [ ] Engineering lead
- [ ] Security review (High/Critical risk)
- [ ] Business owner (user-facing changes)

### Implementation
- [ ] Changes tested in staging
- [ ] Monitoring dashboards checked
- [ ] Rollback procedure verified
- [ ] Post-deployment verification
```

### CI/CD Gates

```yaml
# SOC2 compliant pipeline
deployment:
  stages:
    - lint-and-test
    - security-scan
    - code-review-approval    # Min 1 reviewer
    - staging-deploy
    - staging-verification
    - production-approval     # Manual gate
    - production-deploy
    - post-deploy-verification

  rules:
    - require_code_review: true
    - require_passing_tests: true
    - require_security_scan: true
    - no_direct_push_to_main: true
    - branch_protection: true
```

## Incident Response Plan

### Severity Classification

| Severity | Definition | Response Time | Examples |
|----------|-----------|--------------|---------|
| SEV-1 | Service down, data breach | 15 min | Production outage, unauthorized access |
| SEV-2 | Major degradation | 1 saat | Feature broken, performance issue |
| SEV-3 | Minor impact | 4 saat | Non-critical bug, cosmetic issue |
| SEV-4 | No user impact | Next business day | Internal tool issue |

### Response Workflow

```
1. DETECT    → Monitoring alert / user report
2. TRIAGE    → Classify severity, assign IC (Incident Commander)
3. CONTAIN   → Stop the bleeding (isolate, rollback, block)
4. ERADICATE → Root cause fix
5. RECOVER   → Restore normal operations
6. REVIEW    → Post-incident review within 48 saat
7. IMPROVE   → Action items tracked to completion
```

### Post-Incident Review Template

```markdown
## Post-Incident Review

**Incident:** [INC-XXXX]
**Date:** [tarih]
**Duration:** [suresi]
**Severity:** [SEV-1/2/3/4]
**IC:** [isim]

### Timeline
- HH:MM - Event detected
- HH:MM - IC assigned
- HH:MM - Root cause identified
- HH:MM - Fix deployed
- HH:MM - Service restored

### Root Cause
[Detayli aciklama]

### Impact
- Users affected: [sayi]
- Duration: [sure]
- Data impact: [varsa]

### Action Items
- [ ] [Action 1] - Owner: [isim] - Due: [tarih]
- [ ] [Action 2] - Owner: [isim] - Due: [tarih]

### Lessons Learned
[Ne ogrendi]
```

## Evidence Collection Guide

### Continuous Evidence Collection

| Evidence Type | Source | Frequency | Tool |
|--------------|--------|-----------|------|
| Access reviews | IAM provider | Quarterly | Okta/Auth0 export |
| Change logs | Git, CI/CD | Continuous | GitHub audit log |
| Security scans | SAST/DAST | Per deploy | Snyk, SonarQube |
| Penetration tests | External auditor | Annual | Report PDF |
| Training records | LMS | Annual | Completion certs |
| Incident reports | Incident tracker | Per incident | PagerDuty, Jira |
| Backup tests | DR runbook | Quarterly | Restore verification |
| Uptime metrics | Monitoring | Continuous | Datadog, Grafana |
| Vulnerability patches | Dependency manager | Continuous | Dependabot, Renovate |

### Evidence Automation

```typescript
// Automated evidence collector
async function collectMonthlyEvidence(): Promise<EvidencePackage> {
  const [accessLogs, changeLog, securityScans, uptimeMetrics] = await Promise.all([
    fetchAccessReviewReport(),
    fetchGitChangeLog(),
    fetchSecurityScanResults(),
    fetchUptimeMetrics(),
  ]);

  return {
    period: getCurrentMonth(),
    accessReview: accessLogs,
    changeManagement: changeLog,
    securityScanning: securityScans,
    availability: uptimeMetrics,
    generatedAt: new Date().toISOString(),
  };
}
```

## Common SOC2 Findings & Fixes

| Finding | Risk | Fix |
|---------|------|-----|
| No MFA for admin accounts | High | Enable MFA for all privileged users |
| Missing access reviews | Medium | Implement quarterly review process |
| No encryption at rest | High | Enable disk/database encryption |
| Inadequate logging | Medium | Implement centralized audit logging |
| No change management | High | Require PR reviews, approval gates |
| Missing incident response plan | High | Document and test IR procedures |
| No vulnerability scanning | Medium | Add SAST/DAST to CI/CD |
| Shared service accounts | Medium | Individual accounts with RBAC |
| No backup verification | Medium | Quarterly restore tests |
| Missing security training | Low | Annual security awareness program |

## SOC2 Readiness Checklist

### Phase 1: Gap Assessment (2-4 hafta)

- [ ] Current state documentation
- [ ] Policy inventory
- [ ] Control gap identification
- [ ] Remediation roadmap

### Phase 2: Remediation (2-6 ay)

- [ ] Policies written and approved
- [ ] Technical controls implemented
- [ ] Monitoring and alerting configured
- [ ] Evidence collection automated
- [ ] Employee training completed

### Phase 3: Type I Audit (1-2 ay)

- [ ] Point-in-time assessment
- [ ] Control design evaluation
- [ ] Report received

### Phase 4: Type II Audit (6-12 ay observation)

- [ ] Operating effectiveness tested
- [ ] Evidence provided for observation period
- [ ] Exceptions documented and remediated
- [ ] Final report received
