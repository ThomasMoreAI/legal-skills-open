---
name: gdpr-compliance-vibeeval
title: GDPR Compliance
description: GDPR compliance - data subject rights, lawful basis, DPIA, privacy by design, breach notification, consent management, cross-border transfers, PII masking
author: vibeeval
author_url: https://github.com/vibeeval/vibecosystem/tree/main/skills/gdpr-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# GDPR Compliance

## Data Subject Rights

### Rights Overview

| Right | Article | SLA | Implementation |
|-------|---------|-----|----------------|
| Right of Access | Art. 15 | 30 gun | Data export endpoint |
| Right to Rectification | Art. 16 | 30 gun | Profile edit + audit trail |
| Right to Erasure | Art. 17 | 30 gun | Cascading delete + anonymize |
| Right to Restriction | Art. 18 | 30 gun | Processing flag on record |
| Right to Portability | Art. 20 | 30 gun | Machine-readable export (JSON/CSV) |
| Right to Object | Art. 21 | 30 gun | Opt-out mechanism |
| Automated Decision-Making | Art. 22 | 30 gun | Human review override |

### Data Subject Request Handler

```typescript
interface DSRRequest {
  id: string;
  type: 'access' | 'rectification' | 'erasure' | 'restriction' | 'portability' | 'objection';
  subjectId: string;
  verifiedIdentity: boolean;
  receivedAt: Date;
  deadline: Date;  // receivedAt + 30 gun
  status: 'received' | 'verified' | 'processing' | 'completed' | 'rejected';
  reason?: string;
}

async function handleDSR(request: DSRRequest): Promise<DSRResponse> {
  // Step 1: Identity verification ZORUNLU
  if (!request.verifiedIdentity) {
    return { status: 'rejected', reason: 'Identity not verified' };
  }

  // Step 2: Check deadline
  const daysRemaining = differenceInDays(request.deadline, new Date());
  if (daysRemaining <= 5) {
    await alertDPO({ type: 'dsr_deadline_approaching', request });
  }

  // Step 3: Process by type
  switch (request.type) {
    case 'access':
      return await generateDataExport(request.subjectId);
    case 'erasure':
      return await executeErasure(request.subjectId);
    case 'portability':
      return await generatePortableExport(request.subjectId, 'json');
    case 'rectification':
      return await updateSubjectData(request.subjectId, request.corrections);
    case 'restriction':
      return await restrictProcessing(request.subjectId);
    case 'objection':
      return await recordObjection(request.subjectId, request.reason);
  }
}
```

### Right to Erasure Implementation

```typescript
async function executeErasure(subjectId: string): Promise<ErasureResult> {
  const erasureLog: ErasureStep[] = [];

  await db.transaction(async (tx) => {
    // 1. Anonymize user record (yasal zorunluluklar haric)
    await tx.users.update({
      where: { id: subjectId },
      data: {
        email: `erased-${hash(subjectId)}@deleted.local`,
        name: 'Erased User',
        phone: null,
        address: null,
        dateOfBirth: null,
        deletedAt: new Date(),
      },
    });
    erasureLog.push({ table: 'users', action: 'anonymized' });

    // 2. Delete personal messages
    const deletedMessages = await tx.messages.deleteMany({
      where: { userId: subjectId },
    });
    erasureLog.push({ table: 'messages', action: 'deleted', count: deletedMessages.count });

    // 3. Delete sessions and tokens
    await tx.sessions.deleteMany({ where: { userId: subjectId } });
    await tx.refreshTokens.deleteMany({ where: { userId: subjectId } });
    erasureLog.push({ table: 'sessions', action: 'deleted' });

    // 4. Anonymize audit logs (log kaydi kalir, kisi bilgisi gider)
    await tx.auditLogs.updateMany({
      where: { actorId: subjectId },
      data: { actorId: 'erased', actorEmail: 'erased' },
    });
    erasureLog.push({ table: 'auditLogs', action: 'anonymized' });

    // 5. Notify third-party processors
    await notifyProcessors(subjectId, 'erasure');

    // 6. Record erasure for compliance
    await tx.erasureRecords.create({
      data: {
        subjectHash: hash(subjectId),
        erasedAt: new Date(),
        systems: erasureLog,
      },
    });
  });

  return { success: true, steps: erasureLog };
}
```

## Lawful Basis for Processing

| Basis | Article | When to Use | Example |
|-------|---------|-------------|---------|
| Consent | Art. 6(1)(a) | Optional processing, marketing | Newsletter signup |
| Contract | Art. 6(1)(b) | Necessary for service delivery | Order processing |
| Legal obligation | Art. 6(1)(c) | Required by law | Tax records |
| Vital interests | Art. 6(1)(d) | Life-threatening situations | Emergency contact |
| Public interest | Art. 6(1)(e) | Public authority tasks | Government services |
| Legitimate interest | Art. 6(1)(f) | Business need, balanced with rights | Fraud prevention |

### Lawful Basis Checklist

- [ ] Documented lawful basis for EACH processing activity
- [ ] Records of Processing Activities (RoPA) maintained
- [ ] Legitimate Interest Assessment (LIA) for Art. 6(1)(f)
- [ ] Special category data has Art. 9 basis
- [ ] Children's data has parental consent (Art. 8)

## Data Protection Impact Assessment (DPIA)

### When Required (Art. 35)

- Automated decision-making with legal effects
- Large-scale processing of sensitive data
- Systematic monitoring of public areas
- New technology with high privacy risk
- Large-scale profiling

### DPIA Template

```markdown
## Data Protection Impact Assessment

**Project:** [proje adi]
**Date:** [tarih]
**DPO Review:** [evet/hayir]

### 1. Processing Description
- What data: [veri turleri]
- Why: [amac]
- How: [islem yontemi]
- Who: [erisim kimlerde]
- How long: [saklama suresi]

### 2. Necessity & Proportionality
- Lawful basis: [hukuki dayanak]
- Data minimization: [minimum veri mi?]
- Purpose limitation: [amac sinirli mi?]
- Storage limitation: [saklama suresi uygun mu?]

### 3. Risk Assessment
| Risk | Likelihood | Impact | Severity | Mitigation |
|------|-----------|--------|----------|------------|
| Unauthorized access | [L/M/H] | [L/M/H] | [L/M/H] | [onlem] |
| Data breach | [L/M/H] | [L/M/H] | [L/M/H] | [onlem] |
| Purpose creep | [L/M/H] | [L/M/H] | [L/M/H] | [onlem] |

### 4. Measures
- [ ] Encryption at rest and in transit
- [ ] Access controls (RBAC)
- [ ] Audit logging
- [ ] Data minimization applied
- [ ] Retention policy configured
- [ ] Pseudonymization where possible

### 5. DPO Sign-off
Date: [tarih] | Approved: [evet/hayir]
```

## Privacy by Design Patterns

### Data Minimization

```typescript
// YANLIS: Tum veriyi topla
const user = await db.users.findUnique({
  where: { id },
  // Returns everything including SSN, DOB, etc.
});

// DOGRU: Sadece gerekli alanlari sec
const user = await db.users.findUnique({
  where: { id },
  select: {
    id: true,
    name: true,
    email: true,
    // SSN, DOB, etc. secilmez
  },
});
```

### PII Masking

```typescript
function maskPII(data: Record<string, unknown>): Record<string, unknown> {
  const piiFields: Record<string, (val: string) => string> = {
    email: (v) => v.replace(/^(.{2}).*(@.*)$/, '$1***$2'),
    phone: (v) => v.replace(/^(.{3}).*(.{2})$/, '$1*****$2'),
    ssn: (v) => `***-**-${v.slice(-4)}`,
    creditCard: (v) => `****-****-****-${v.slice(-4)}`,
    ip: (v) => v.replace(/\.\d+$/, '.xxx'),
    name: (v) => `${v.charAt(0)}${'*'.repeat(v.length - 1)}`,
  };

  return Object.fromEntries(
    Object.entries(data).map(([key, value]) => {
      const masker = piiFields[key];
      if (masker && typeof value === 'string') {
        return [key, masker(value)];
      }
      return [key, value];
    })
  );
}
```

### Encryption at Rest

```typescript
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto';

const ALGORITHM = 'aes-256-gcm';

function encryptPII(plaintext: string, key: Buffer): EncryptedData {
  const iv = randomBytes(16);
  const cipher = createCipheriv(ALGORITHM, key, iv);
  const encrypted = Buffer.concat([cipher.update(plaintext, 'utf8'), cipher.final()]);
  const authTag = cipher.getAuthTag();

  return {
    ciphertext: encrypted.toString('base64'),
    iv: iv.toString('base64'),
    authTag: authTag.toString('base64'),
  };
}

function decryptPII(data: EncryptedData, key: Buffer): string {
  const decipher = createDecipheriv(
    ALGORITHM,
    key,
    Buffer.from(data.iv, 'base64')
  );
  decipher.setAuthTag(Buffer.from(data.authTag, 'base64'));
  return decipher.update(data.ciphertext, 'base64', 'utf8') + decipher.final('utf8');
}
```

## Data Breach Notification (72 Saat Kurali)

### Notification Workflow

```
0h    → Breach detected
       → Incident response team activated
       → Containment measures started

24h   → Impact assessment completed
       → Affected data subjects identified
       → Breach severity classified

48h   → Notification to DPA prepared
       → Data subject notification prepared (if high risk)

72h   → DEADLINE: DPA notification submitted (Art. 33)
       → Data subject notification sent if required (Art. 34)
```

### Breach Assessment

```typescript
interface BreachAssessment {
  detectedAt: Date;
  nature: string;                    // What happened
  categoriesAffected: string[];      // Data types exposed
  subjectsAffected: number;          // How many people
  likelyConsequences: string[];      // Potential harm
  measuresTaken: string[];           // Containment actions
  riskLevel: 'low' | 'medium' | 'high';
  notifyDPA: boolean;               // Required unless low risk
  notifySubjects: boolean;          // Required if high risk
  dpaNotificationDeadline: Date;    // detectedAt + 72h
}

function assessBreachRisk(breach: BreachAssessment): string {
  const highRiskFactors = [
    breach.categoriesAffected.includes('financial'),
    breach.categoriesAffected.includes('health'),
    breach.categoriesAffected.includes('credentials'),
    breach.subjectsAffected > 1000,
  ];
  const highRiskCount = highRiskFactors.filter(Boolean).length;

  if (highRiskCount >= 2) return 'high';
  if (highRiskCount >= 1) return 'medium';
  return 'low';
}
```

## Consent Management

### Consent Collection

```typescript
interface ConsentRecord {
  subjectId: string;
  purpose: string;           // 'marketing_email', 'analytics', 'profiling'
  granted: boolean;
  grantedAt: Date | null;
  revokedAt: Date | null;
  method: 'explicit_opt_in' | 'form' | 'api';
  version: string;           // Privacy policy version
  ip?: string;
  evidence: string;          // What they agreed to (exact text)
}

async function recordConsent(consent: ConsentRecord): Promise<void> {
  // Consent must be:
  // - Freely given (no pre-ticked boxes)
  // - Specific (per purpose)
  // - Informed (clear language)
  // - Unambiguous (affirmative action)
  await db.consents.create({ data: consent });
  await auditLog({
    action: `consent.${consent.granted ? 'granted' : 'revoked'}`,
    actor: consent.subjectId,
    resource: consent.purpose,
    details: { version: consent.version },
  });
}
```

### Consent Anti-Patterns

| Anti-Pattern | GDPR Violation | Dogru Yol |
|-------------|---------------|-----------|
| Pre-ticked checkboxes | Art. 7 - not freely given | Unchecked by default |
| Bundled consent | Art. 7 - not specific | Separate consent per purpose |
| Dark patterns (confusing UI) | Art. 7 - not informed | Clear, plain language |
| No withdrawal mechanism | Art. 7(3) - easy withdrawal | One-click unsubscribe |
| Consent wall (block access) | Art. 7 - not freely given | Allow access without consent |
| Implicit consent | Art. 4(11) - not unambiguous | Explicit opt-in required |

## Cross-Border Data Transfer

### Transfer Mechanisms

| Mechanism | When to Use | Complexity |
|-----------|-------------|------------|
| Adequacy decision | EU-approved country (UK, Japan, etc.) | Low |
| Standard Contractual Clauses (SCCs) | US, India, etc. | Medium |
| Binding Corporate Rules (BCRs) | Intra-group transfers | High |
| Explicit consent | One-off transfers | Low |
| EU-US Data Privacy Framework | US companies certified | Medium |

### Transfer Impact Assessment (TIA)

```markdown
## Transfer Impact Assessment

**From:** [EU entity]
**To:** [Non-EU entity, country]
**Mechanism:** [SCC / BCR / Adequacy / Consent]

### Data Transferred
- Categories: [personal data types]
- Volume: [approximate records/month]
- Frequency: [continuous / batch / ad-hoc]

### Recipient Country Assessment
- Privacy laws: [adequacy level]
- Government access: [surveillance risk]
- Legal remedies: [available to EU subjects?]

### Supplementary Measures
- [ ] End-to-end encryption (keys retained in EU)
- [ ] Pseudonymization before transfer
- [ ] Access controls at destination
- [ ] Contractual prohibition on government disclosure
- [ ] Regular compliance audits
```

## Data Minimization & Retention

### Retention Policy

| Data Category | Retention Period | Legal Basis | After Expiry |
|--------------|-----------------|-------------|-------------|
| Active user data | Account lifetime | Contract | Anonymize |
| Inactive user data | 2 yil inactivity | Legitimate interest | Delete |
| Transaction records | 7 yil | Legal obligation (tax) | Archive encrypted |
| Marketing consent | Until revoked | Consent | Delete |
| Support tickets | 3 yil after resolution | Legitimate interest | Anonymize |
| Access logs | 1 yil | Legitimate interest | Delete |
| Analytics (aggregated) | Indefinite | Legitimate interest | N/A (no PII) |

### Automated Retention Enforcement

```typescript
async function enforceRetentionPolicies(): Promise<RetentionReport> {
  const report: RetentionReport = { deletedCount: 0, anonymizedCount: 0 };

  // Delete inactive accounts (2 yil)
  const inactiveThreshold = subYears(new Date(), 2);
  const inactiveUsers = await db.users.findMany({
    where: { lastActiveAt: { lt: inactiveThreshold }, deletedAt: null },
  });
  for (const user of inactiveUsers) {
    await executeErasure(user.id);
    report.deletedCount++;
  }

  // Anonymize old support tickets (3 yil)
  const ticketThreshold = subYears(new Date(), 3);
  const oldTickets = await db.tickets.updateMany({
    where: { resolvedAt: { lt: ticketThreshold }, anonymized: false },
    data: { userEmail: 'anonymized', userName: 'anonymized', anonymized: true },
  });
  report.anonymizedCount += oldTickets.count;

  // Delete old access logs (1 yil)
  const logThreshold = subYears(new Date(), 1);
  await db.accessLogs.deleteMany({
    where: { createdAt: { lt: logThreshold } },
  });

  return report;
}
```

## GDPR Compliance Checklist

### Organizational

- [ ] Data Protection Officer (DPO) appointed (if required)
- [ ] Records of Processing Activities (RoPA) maintained
- [ ] Privacy policy published and up to date
- [ ] Employee data protection training completed
- [ ] Vendor Data Processing Agreements (DPA) in place
- [ ] Data breach response plan documented and tested

### Technical

- [ ] Encryption at rest (AES-256) for PII
- [ ] Encryption in transit (TLS 1.2+)
- [ ] Access controls with least privilege
- [ ] Audit logging for all PII access
- [ ] Data subject request API/workflow
- [ ] Consent management system
- [ ] Automated retention enforcement
- [ ] PII inventory and data flow map
- [ ] Pseudonymization where applicable
- [ ] Backup encryption and access control
