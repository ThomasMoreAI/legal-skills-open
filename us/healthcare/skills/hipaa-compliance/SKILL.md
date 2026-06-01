---
name: hipaa-compliance
title: HIPAA Compliance
description: HIPAA compliance - PHI protection, technical/administrative/physical safeguards, minimum necessary standard, BAA requirements, de-identification, access logging
author: vibeeval
author_url: https://github.com/vibeeval/vibecosystem/tree/main/skills/hipaa-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# HIPAA Compliance

## PHI (Protected Health Information) Identification

### What is PHI?

PHI = Individually identifiable health information transmitted or maintained in any form.

### 18 HIPAA Identifiers

| # | Identifier | Example | De-Identification Action |
|---|-----------|---------|-------------------------|
| 1 | Names | John Smith | Remove |
| 2 | Geographic data (< state) | 123 Main St, ZIP | Truncate ZIP to 3 digits |
| 3 | Dates (except year) | DOB, admission date | Generalize to year |
| 4 | Phone numbers | (555) 123-4567 | Remove |
| 5 | Fax numbers | (555) 123-4568 | Remove |
| 6 | Email addresses | john@example.com | Remove |
| 7 | SSN | 123-45-6789 | Remove |
| 8 | Medical record numbers | MRN-001234 | Replace with random ID |
| 9 | Health plan beneficiary # | BEN-98765 | Remove |
| 10 | Account numbers | ACC-12345 | Remove |
| 11 | Certificate/license # | LIC-54321 | Remove |
| 12 | Vehicle identifiers | VIN, plate # | Remove |
| 13 | Device identifiers | Serial #, IMEI | Remove |
| 14 | Web URLs | patient-portal.com/user/123 | Remove |
| 15 | IP addresses | 192.168.1.1 | Remove |
| 16 | Biometric identifiers | Fingerprint, voiceprint | Remove |
| 17 | Full-face photographs | Profile photo | Remove |
| 18 | Any unique identifying # | Custom patient ID | Replace with random |

### PHI Detection

```typescript
interface PHIDetectionResult {
  field: string;
  identifierType: string;
  confidence: 'high' | 'medium' | 'low';
  recommendation: 'encrypt' | 'remove' | 'truncate' | 'pseudonymize';
}

const PHI_PATTERNS: Record<string, RegExp> = {
  ssn: /\b\d{3}-\d{2}-\d{4}\b/,
  phone: /\b\(?(\d{3})\)?[-.\s]?\d{3}[-.\s]?\d{4}\b/,
  email: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/,
  mrn: /\bMRN[-\s]?\d{4,}\b/i,
  dob: /\b(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/\d{4}\b/,
  ip: /\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b/,
};

function scanForPHI(text: string): PHIDetectionResult[] {
  const results: PHIDetectionResult[] = [];
  for (const [type, pattern] of Object.entries(PHI_PATTERNS)) {
    if (pattern.test(text)) {
      results.push({
        field: type,
        identifierType: type,
        confidence: 'high',
        recommendation: 'encrypt',
      });
    }
  }
  return results;
}
```

## Technical Safeguards (164.312)

### Access Control (164.312(a))

```typescript
// Role-Based Access Control for PHI
interface HIPAARole {
  name: string;
  phiAccess: 'none' | 'minimum_necessary' | 'treatment' | 'admin';
  allowedOperations: ('read' | 'write' | 'delete' | 'export')[];
  requiresMFA: boolean;
}

const HIPAA_ROLES: Record<string, HIPAARole> = {
  receptionist: {
    name: 'Receptionist',
    phiAccess: 'minimum_necessary',
    allowedOperations: ['read'],
    requiresMFA: true,
  },
  nurse: {
    name: 'Nurse',
    phiAccess: 'treatment',
    allowedOperations: ['read', 'write'],
    requiresMFA: true,
  },
  physician: {
    name: 'Physician',
    phiAccess: 'treatment',
    allowedOperations: ['read', 'write'],
    requiresMFA: true,
  },
  admin: {
    name: 'System Admin',
    phiAccess: 'admin',
    allowedOperations: ['read', 'write', 'delete', 'export'],
    requiresMFA: true,
  },
  billing: {
    name: 'Billing Staff',
    phiAccess: 'minimum_necessary',
    allowedOperations: ['read'],
    requiresMFA: true,
  },
};

function enforceMinimumNecessary(
  role: HIPAARole,
  requestedFields: string[],
  allFields: string[]
): string[] {
  if (role.phiAccess === 'treatment') {
    return requestedFields; // Treatment = full access to relevant PHI
  }
  if (role.phiAccess === 'minimum_necessary') {
    // Only return non-clinical fields
    const nonClinicalFields = ['patientId', 'name', 'dob', 'insuranceId'];
    return requestedFields.filter((f) => nonClinicalFields.includes(f));
  }
  return [];
}
```

### Audit Controls (164.312(b))

```typescript
interface HIPAAAuditLog {
  id: string;
  timestamp: string;
  userId: string;
  userRole: string;
  action: 'view' | 'create' | 'update' | 'delete' | 'export' | 'print';
  patientId: string;
  resourceType: string;          // 'medical_record', 'lab_result', 'prescription'
  resourceId: string;
  accessReason: string;          // 'treatment', 'payment', 'operations'
  ipAddress: string;
  userAgent: string;
  sessionId: string;
  success: boolean;
  details?: string;
}

async function logPHIAccess(entry: HIPAAAuditLog): Promise<void> {
  // HIPAA requires immutable, tamper-evident logs
  // Minimum 6 yil retention
  await auditStore.append({
    ...entry,
    integrity: computeHMAC(entry),
  });

  // Alert on suspicious access patterns
  if (await isAnomalousAccess(entry)) {
    await alertSecurityTeam({
      type: 'suspicious_phi_access',
      entry,
      reason: 'Anomalous access pattern detected',
    });
  }
}

async function isAnomalousAccess(entry: HIPAAAuditLog): Promise<boolean> {
  const recentAccess = await auditStore.getRecent(entry.userId, '1h');
  // Flag: >50 records in 1 hour (potential data exfiltration)
  if (recentAccess.length > 50) return true;
  // Flag: access outside business hours
  const hour = new Date(entry.timestamp).getHours();
  if (hour < 6 || hour > 22) return true;
  // Flag: accessing patient not in user's care
  if (entry.accessReason === 'treatment') {
    const isAssigned = await isPatientAssigned(entry.userId, entry.patientId);
    if (!isAssigned) return true;
  }
  return false;
}
```

### Integrity Controls (164.312(c))

```typescript
// Data integrity verification for PHI
import { createHash } from 'crypto';

interface IntegrityRecord {
  recordId: string;
  hash: string;
  algorithm: 'sha256';
  computedAt: Date;
}

function computeRecordHash(record: Record<string, unknown>): string {
  const canonical = JSON.stringify(record, Object.keys(record).sort());
  return createHash('sha256').update(canonical).digest('hex');
}

async function verifyIntegrity(recordId: string): Promise<boolean> {
  const record = await db.medicalRecords.findUnique({ where: { id: recordId } });
  const storedHash = await db.integrityRecords.findUnique({ where: { recordId } });

  if (!record || !storedHash) return false;

  const currentHash = computeRecordHash(record);
  return currentHash === storedHash.hash;
}
```

### Transmission Security (164.312(e))

```typescript
// TLS enforcement for PHI transmission
import https from 'https';
import fs from 'fs';

const tlsOptions: https.ServerOptions = {
  key: fs.readFileSync(process.env.TLS_KEY_PATH!),
  cert: fs.readFileSync(process.env.TLS_CERT_PATH!),
  minVersion: 'TLSv1.2',       // HIPAA minimum
  ciphers: [
    'TLS_AES_256_GCM_SHA384',
    'TLS_CHACHA20_POLY1305_SHA256',
    'ECDHE-RSA-AES256-GCM-SHA384',
  ].join(':'),
  honorCipherOrder: true,
};

// End-to-end encryption for PHI in transit between systems
function encryptPHIForTransmission(phi: string, recipientPublicKey: string): string {
  const symmetricKey = randomBytes(32);
  const encryptedData = encryptAES256GCM(phi, symmetricKey);
  const encryptedKey = publicEncrypt(recipientPublicKey, symmetricKey);
  return JSON.stringify({ encryptedData, encryptedKey: encryptedKey.toString('base64') });
}
```

## Administrative Safeguards (164.308)

### Checklist

- [ ] Security Officer designated
- [ ] Privacy Officer designated
- [ ] Risk analysis conducted (annual)
- [ ] Risk management plan documented
- [ ] Sanction policy for violations
- [ ] Information system activity review (regular)
- [ ] Workforce security procedures
- [ ] Security awareness training (annual)
- [ ] Security incident procedures
- [ ] Contingency plan (backup, DR, emergency mode)
- [ ] Evaluation (periodic compliance assessment)
- [ ] Business Associate Agreements (BAA) with all vendors

### Workforce Training Requirements

| Topic | Frequency | Audience |
|-------|-----------|----------|
| HIPAA overview | Annual | All staff |
| PHI handling procedures | Annual | PHI access staff |
| Security awareness | Annual + onboarding | All staff |
| Incident reporting | Annual | All staff |
| Phishing awareness | Quarterly | All staff |
| Role-specific PHI policies | Annual | Clinical staff |

## Physical Safeguards (164.310)

### Checklist

- [ ] Facility access controls (badge, biometric)
- [ ] Workstation use policy (screen lock, clean desk)
- [ ] Workstation security (cable locks, positioning)
- [ ] Device and media controls (disposal, reuse, movement)
- [ ] Visitor access logging
- [ ] Server room access restricted and logged
- [ ] Mobile device policy (encryption, remote wipe)

## Minimum Necessary Standard

### Implementation

```typescript
// Minimum Necessary middleware
function minimumNecessaryFilter(role: string, endpoint: string) {
  return (req: Request, res: Response, next: NextFunction) => {
    const fieldPermissions = getFieldPermissions(role, endpoint);

    // Override response to filter fields
    const originalJson = res.json.bind(res);
    res.json = (data: unknown) => {
      const filtered = filterFields(data, fieldPermissions);
      return originalJson(filtered);
    };

    next();
  };
}

// Field access matrix
const FIELD_PERMISSIONS: Record<string, Record<string, string[]>> = {
  receptionist: {
    '/api/patients': ['id', 'name', 'dob', 'phone', 'appointmentTime'],
    '/api/patients/:id': ['id', 'name', 'dob', 'phone', 'insuranceId'],
  },
  nurse: {
    '/api/patients': ['id', 'name', 'dob', 'vitals', 'medications', 'allergies'],
    '/api/patients/:id': ['*'], // Full treatment access
  },
  billing: {
    '/api/patients': ['id', 'name', 'insuranceId', 'billingCodes'],
    '/api/patients/:id': ['id', 'name', 'insuranceId', 'billingCodes', 'procedures'],
  },
};
```

### Exceptions to Minimum Necessary

| Scenario | Minimum Necessary Applies? |
|----------|--------------------------|
| Treatment (doctor-to-doctor) | NO - full PHI allowed |
| Patient's own request | NO - full access to own data |
| Required by law | NO - as required |
| Payment/billing | YES - only billing-relevant fields |
| Healthcare operations | YES - limit to necessary |
| Research (with authorization) | YES - de-identified preferred |

## Business Associate Agreement (BAA)

### Required BAA Provisions

```markdown
## BAA Checklist

- [ ] Permitted uses and disclosures of PHI defined
- [ ] BA will not use/disclose PHI beyond contract
- [ ] BA will implement appropriate safeguards
- [ ] BA will report security incidents and breaches
- [ ] BA will ensure subcontractors comply
- [ ] BA will make PHI available for patient access
- [ ] BA will make PHI available for amendment
- [ ] BA will provide accounting of disclosures
- [ ] BA will make internal practices available to HHS
- [ ] BA will return or destroy PHI at termination
- [ ] CE may terminate if BA violates terms
```

### Common BA Vendors Requiring BAA

| Vendor Type | Examples | PHI Exposure |
|------------|---------|-------------|
| Cloud hosting | AWS, GCP, Azure | Infrastructure |
| EHR systems | Epic, Cerner | Full PHI |
| Email (if PHI sent) | Google Workspace, M365 | Communication |
| Payment processing | Stripe (if health billing) | Billing PHI |
| Analytics (if PHI) | Custom analytics | Usage data |
| Backup services | Veeam, Backblaze | Full PHI |
| Shredding services | Iron Mountain | Physical PHI |

## De-Identification Methods

### Safe Harbor Method (164.514(b)(2))

```typescript
interface DeIdentifiedRecord {
  randomId: string;  // Not derived from original ID
  ageGroup: string;  // '>89' or age bucket
  zipCode3: string;  // First 3 digits (if population > 20K)
  diagnosisCode: string;
  procedureCode: string;
  // ALL 18 identifiers removed
}

function deIdentifySafeHarbor(record: PatientRecord): DeIdentifiedRecord {
  const age = calculateAge(record.dateOfBirth);

  return {
    randomId: generateRandomId(), // NOT derived from patient ID
    ageGroup: age > 89 ? '90+' : `${Math.floor(age / 10) * 10}-${Math.floor(age / 10) * 10 + 9}`,
    zipCode3: record.zipCode.substring(0, 3),
    diagnosisCode: record.diagnosisCode,
    procedureCode: record.procedureCode,
    // name: REMOVED
    // dob: REMOVED (age bucket only)
    // ssn: REMOVED
    // mrn: REMOVED
    // phone: REMOVED
    // email: REMOVED
    // address: REMOVED (zip3 only)
  };
}
```

### Expert Determination Method (164.514(b)(1))

```markdown
## Expert Determination Requirements

1. Apply statistical/scientific methods
2. Determine re-identification risk is "very small"
3. Document methods and results
4. Expert must have appropriate knowledge and experience
5. Re-identification risk typically < 0.04 (1 in 25)
```

## PHI Encryption Standards

### At Rest

```typescript
// Column-level encryption for PHI fields
import { createCipheriv, createDecipheriv, randomBytes, scryptSync } from 'crypto';

const ALGORITHM = 'aes-256-gcm';
const KEY = scryptSync(process.env.PHI_ENCRYPTION_KEY!, 'salt', 32);

function encryptPHIField(value: string): EncryptedField {
  const iv = randomBytes(16);
  const cipher = createCipheriv(ALGORITHM, KEY, iv);
  const encrypted = Buffer.concat([cipher.update(value, 'utf8'), cipher.final()]);
  return {
    data: encrypted.toString('base64'),
    iv: iv.toString('base64'),
    tag: cipher.getAuthTag().toString('base64'),
  };
}

function decryptPHIField(encrypted: EncryptedField): string {
  const decipher = createDecipheriv(
    ALGORITHM,
    KEY,
    Buffer.from(encrypted.iv, 'base64')
  );
  decipher.setAuthTag(Buffer.from(encrypted.tag, 'base64'));
  return decipher.update(encrypted.data, 'base64', 'utf8') + decipher.final('utf8');
}
```

### Key Management

- [ ] Encryption keys stored separately from data
- [ ] Key rotation schedule (annual minimum)
- [ ] Key access limited to security team
- [ ] Key backup and recovery procedure
- [ ] Key destruction procedure for decommissioned systems

## HIPAA Violation Penalties

| Tier | Description | Penalty Per Violation | Annual Maximum |
|------|-------------|----------------------|----------------|
| 1 | Did not know | $100 - $50,000 | $25,000 |
| 2 | Reasonable cause | $1,000 - $50,000 | $100,000 |
| 3 | Willful neglect (corrected) | $10,000 - $50,000 | $250,000 |
| 4 | Willful neglect (not corrected) | $50,000+ | $1,500,000 |

## Anti-Patterns

| Anti-Pattern | HIPAA Violation | Dogru Yol |
|-------------|----------------|-----------|
| PHI in logs/debug output | Minimum necessary | Filter PHI before logging |
| PHI in error messages | Minimum necessary | Generic error messages |
| Unencrypted PHI at rest | Technical safeguard | AES-256 encryption |
| Shared login credentials | Access control | Individual accounts + MFA |
| No audit trail | Audit controls | Immutable access logging |
| PHI in URL parameters | Transmission security | POST body + TLS |
| PHI in email (unencrypted) | Transmission security | Encrypted messaging or portal |
| No BAA with cloud vendor | Administrative safeguard | Execute BAA before use |
| No access expiration | Access control | Auto-expire + review |
| PHI on personal devices | Physical safeguard | MDM + encryption policy |
