---
name: hipaa-en-skills-mauriciodelrio
title: HIPAA — Health Insurance Portability and Accountability Act
description: Use this skill when the software processes, stores, or transmits Protected Health Information (PHI). Although HIPAA is U.S. legislation, this skill applies as a health data protection standard for any software regardless of the geographic location of users. Covers technical safeguards (RBAC access control, AES-256 encryption, audit trail), administrative and physical safeguards, breach notification, BAA with third parties, and compliance checklist.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/en-skills/governance-risk-and-compliance/hipaa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# HIPAA — Health Insurance Portability and Accountability Act

HIPAA defines the health information protection standard that should be applied to any software handling medical or patient data, regardless of user geography. It is structured in 5 rules: Privacy Rule (PHI use and disclosure), Security Rule (technical, administrative, and physical safeguards for ePHI), Breach Notification Rule (breach notification), Enforcement Rule (penalties), and Omnibus Rule (extension to Business Associates). PHI is any health information combined with any of the 18 HIPAA identifiers that can identify an individual.

## Implementation

### 1. The 18 HIPAA Identifiers

```typescript
// The 18 HIPAA identifiers that make data PHI
const HIPAA_IDENTIFIERS = [
  'name',                    // 1. Name
  'geographic_data',         // 2. Geographic data (smaller than state)
  'dates',                   // 3. Dates (except year) related to the individual
  'phone_number',            // 4. Phone numbers
  'fax_number',              // 5. Fax numbers
  'email',                   // 6. Email address
  'ssn',                     // 7. Social Security number
  'medical_record_number',   // 8. Medical record number
  'health_plan_id',          // 9. Health plan number
  'account_number',          // 10. Account numbers
  'certificate_license',     // 11. Certificate/license numbers
  'vehicle_identifiers',     // 12. Vehicle identifiers
  'device_identifiers',      // 13. Device identifiers
  'web_urls',                // 14. URLs
  'ip_address',              // 15. IP addresses
  'biometric_ids',           // 16. Biometric identifiers
  'face_photos',             // 17. Full face photos
  'unique_identifier',       // 18. Any other unique identifying number/code
] as const;
```

### 2. Technical Safeguards

#### Access Control (§164.312(a))

```prisma
// schema.prisma — HIPAA access control model

model HealthcareUser {
  id              String    @id @default(cuid())
  email           String    @unique
  passwordHash    String
  
  // Role-based access control
  role            HealthcareRole
  department      String?
  licenseNumber   String?   // Medical license number
  
  // MFA mandatory for PHI access
  mfaEnabled      Boolean   @default(true)
  mfaSecret       String?   // Encrypted
  
  // Session management
  sessions        UserSession[]
  
  // Auto-logoff for inactivity (§164.312(a)(2)(iii))
  lastActivityAt  DateTime  @default(now())
  sessionTimeout  Int       @default(900) // 15 minutes in seconds
  
  // Audit
  accessLogs      PHIAccessLog[]
  
  // Account status
  isActive        Boolean   @default(true)
  lockedAt        DateTime?
  failedAttempts  Int       @default(0)
  
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  @@map("healthcare_users")
}

enum HealthcareRole {
  PHYSICIAN           // Physician - full access to their patients' PHI
  NURSE               // Nurse - access to assigned patients' PHI
  LAB_TECHNICIAN      // Lab technician - access to lab results
  BILLING_STAFF       // Billing staff - access to billing data
  ADMIN               // System admin - no PHI access
  PATIENT             // Patient - access only to their own PHI
  RESEARCHER          // Researcher - access to de-identified data
}

model PatientRecord {
  id              String    @id @default(cuid())
  patientId       String
  patient         Patient   @relation(fields: [patientId], references: [id])
  
  // Clinical data (encrypted at rest)
  diagnosis       String    // Encrypted with AES-256
  treatment       String    // Encrypted
  medications     Json      // Encrypted
  labResults      Json?     // Encrypted
  notes           String?   // Encrypted
  
  // Access metadata
  sensitivityLevel PHISensitivity @default(STANDARD)
  
  // Break-the-glass: emergency access
  emergencyAccess  Boolean  @default(false)
  
  createdBy       String
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  // Full audit
  accessLogs      PHIAccessLog[]
  
  @@index([patientId])
  @@map("patient_records")
}

model Patient {
  id              String    @id @default(cuid())
  
  // Demographic data (all encrypted)
  mrn             String    @unique // Medical Record Number
  firstName       String    // Encrypted
  lastName        String    // Encrypted
  dateOfBirth     DateTime  // Encrypted
  ssn             String?   // Encrypted - only when necessary
  
  // Contact
  phone           String?   // Encrypted
  email           String?   // Encrypted
  address         Json?     // Encrypted
  
  // Health insurance
  insuranceProvider String?
  insurancePolicyId String? // Encrypted
  
  records         PatientRecord[]
  
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  @@map("patients")
}

enum PHISensitivity {
  STANDARD          // Standard PHI
  HIGHLY_SENSITIVE  // Mental health, substance abuse, HIV/AIDS
  RESTRICTED        // Psychotherapy notes (special protection)
}

// Mandatory audit trail — §164.312(b)
model PHIAccessLog {
  id              String    @id @default(cuid())
  
  userId          String
  user            HealthcareUser @relation(fields: [userId], references: [id])
  recordId        String?
  record          PatientRecord? @relation(fields: [recordId], references: [id])
  patientId       String?
  
  // Access detail
  action          PHIAction
  resource        String      // Type of resource accessed
  fieldsAccessed  String[]    // Specific fields accessed
  
  // Context
  reason          String?     // Reason for access
  isEmergency     Boolean     @default(false) // Break-the-glass
  
  // Technical metadata
  ipAddress       String
  userAgent       String
  sessionId       String
  
  // Result
  success         Boolean
  errorMessage    String?
  
  timestamp       DateTime    @default(now())
  
  @@index([userId])
  @@index([recordId])
  @@index([patientId])
  @@index([timestamp])
  @@index([action])
  @@map("phi_access_logs")
}

enum PHIAction {
  VIEW            // View PHI
  CREATE          // Create record with PHI
  UPDATE          // Modify PHI
  DELETE          // Delete PHI
  EXPORT          // Export PHI
  PRINT           // Print PHI
  SHARE           // Share PHI with another provider
  EMERGENCY_ACCESS // Emergency access (break-the-glass)
}
```

#### Access Control Service

```typescript
// services/hipaa-access-control.service.ts

import { PrismaClient, HealthcareRole, PHISensitivity, PHIAction } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'hipaa-access-control' });

/**
 * HIPAA permissions matrix: Defines what roles can perform what actions.
 * Minimum Necessary Rule (§164.502(b)):
 * Only access the minimum PHI necessary for the job function.
 */
const ACCESS_MATRIX: Record<HealthcareRole, {
  allowedActions: PHIAction[];
  allowedSensitivity: PHISensitivity[];
  requiresPatientAssignment: boolean;
}> = {
  PHYSICIAN: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE, PHIAction.UPDATE, PHIAction.EXPORT, PHIAction.SHARE],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE, PHISensitivity.RESTRICTED],
    requiresPatientAssignment: true, // Only assigned patients
  },
  NURSE: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE, PHIAction.UPDATE],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE],
    requiresPatientAssignment: true,
  },
  LAB_TECHNICIAN: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE],
    allowedSensitivity: [PHISensitivity.STANDARD],
    requiresPatientAssignment: false, // Access by result type
  },
  BILLING_STAFF: {
    allowedActions: [PHIAction.VIEW],
    allowedSensitivity: [PHISensitivity.STANDARD],
    requiresPatientAssignment: false,
  },
  ADMIN: {
    allowedActions: [], // No PHI access
    allowedSensitivity: [],
    requiresPatientAssignment: false,
  },
  PATIENT: {
    allowedActions: [PHIAction.VIEW, PHIAction.EXPORT],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE],
    requiresPatientAssignment: false, // Only their own PHI
  },
  RESEARCHER: {
    allowedActions: [PHIAction.VIEW],
    allowedSensitivity: [PHISensitivity.STANDARD], // Only de-identified data
    requiresPatientAssignment: false,
  },
};

export class HIPAAAccessControlService {
  /**
   * Verify if a user has permission to access a PHI record.
   */
  async checkAccess(params: {
    userId: string;
    patientId: string;
    recordId?: string;
    action: PHIAction;
    fieldsRequested: string[];
    reason?: string;
    isEmergency?: boolean;
    ipAddress: string;
    userAgent: string;
    sessionId: string;
  }): Promise<{ allowed: boolean; reason: string }> {
    const user = await prisma.healthcareUser.findUniqueOrThrow({
      where: { id: params.userId },
    });

    // Check if the account is active
    if (!user.isActive || user.lockedAt) {
      await this.logAccess({ ...params, success: false, errorMessage: 'Account inactive or locked' });
      return { allowed: false, reason: 'Account inactive or locked' };
    }

    // Check session timeout (auto-logoff §164.312(a)(2)(iii))
    const inactiveSeconds = (Date.now() - user.lastActivityAt.getTime()) / 1000;
    if (inactiveSeconds > user.sessionTimeout) {
      await this.logAccess({ ...params, success: false, errorMessage: 'Session expired due to inactivity' });
      return { allowed: false, reason: 'Session expired due to inactivity' };
    }

    const permissions = ACCESS_MATRIX[user.role];

    // Break-the-glass: emergency access
    if (params.isEmergency) {
      logger.warn({
        event: 'emergency_access',
        userId: params.userId,
        patientId: params.patientId,
        role: user.role,
      }, '⚠️ EMERGENCY ACCESS (Break-the-glass)');
      
      await this.logAccess({ ...params, success: true, isEmergency: true });
      return { allowed: true, reason: 'Emergency access (break-the-glass)' };
    }

    // Check allowed action
    if (!permissions.allowedActions.includes(params.action)) {
      await this.logAccess({
        ...params,
        success: false,
        errorMessage: `Action ${params.action} not allowed for role ${user.role}`,
      });
      return {
        allowed: false,
        reason: `Your role (${user.role}) does not have permission for ${params.action}`,
      };
    }

    // Check record sensitivity
    if (params.recordId) {
      const record = await prisma.patientRecord.findUnique({
        where: { id: params.recordId },
      });

      if (record && !permissions.allowedSensitivity.includes(record.sensitivityLevel)) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: `Sensitivity level ${record.sensitivityLevel} not allowed`,
        });
        return {
          allowed: false,
          reason: `You do not have access to records with sensitivity level ${record.sensitivityLevel}`,
        };
      }
    }

    // Check patient assignment (if applicable)
    if (permissions.requiresPatientAssignment) {
      const isAssigned = await this.isPatientAssigned(params.userId, params.patientId);
      if (!isAssigned) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: 'Patient not assigned to the professional',
        });
        return { allowed: false, reason: 'This patient is not assigned to your care' };
      }
    }

    // Patients can only access their own PHI
    if (user.role === 'PATIENT') {
      const isOwnData = await this.isOwnPatientData(params.userId, params.patientId);
      if (!isOwnData) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: 'Attempt to access another patient\'s PHI',
        });
        return { allowed: false, reason: 'You can only access your own health information' };
      }
    }

    // Access allowed
    await this.logAccess({ ...params, success: true });

    // Update last activity
    await prisma.healthcareUser.update({
      where: { id: params.userId },
      data: { lastActivityAt: new Date() },
    });

    return { allowed: true, reason: 'Access authorized' };
  }

  /**
   * Log all access (successful or failed) to PHI.
   * HIPAA §164.312(b) — Audit Controls
   */
  private async logAccess(params: {
    userId: string;
    patientId: string;
    recordId?: string;
    action: PHIAction;
    fieldsRequested: string[];
    reason?: string;
    isEmergency?: boolean;
    ipAddress: string;
    userAgent: string;
    sessionId: string;
    success: boolean;
    errorMessage?: string;
  }) {
    await prisma.pHIAccessLog.create({
      data: {
        userId: params.userId,
        recordId: params.recordId,
        patientId: params.patientId,
        action: params.action,
        resource: 'patient_record',
        fieldsAccessed: params.fieldsRequested,
        reason: params.reason,
        isEmergency: params.isEmergency ?? false,
        ipAddress: params.ipAddress,
        userAgent: params.userAgent,
        sessionId: params.sessionId,
        success: params.success,
        errorMessage: params.errorMessage,
      },
    });
  }

  private async isPatientAssigned(userId: string, patientId: string): Promise<boolean> {
    // Implement patient-provider assignment verification
    // This depends on your specific data model
    return true; // Placeholder
  }

  private async isOwnPatientData(userId: string, patientId: string): Promise<boolean> {
    // Verify that the userId corresponds to the patientId
    return true; // Placeholder
  }
}
```

---

### 2. PHI Encryption (§164.312(a)(2)(iv) and §164.312(e)(1))

```typescript
// services/phi-encryption.service.ts

import crypto from 'node:crypto';
import pino from 'pino';

const logger = pino({ name: 'phi-encryption' });

const ALGORITHM = 'aes-256-gcm';
const IV_LENGTH = 12; // Recommended for GCM
const AUTH_TAG_LENGTH = 16;

/**
 * PHI-specific encryption service.
 * HIPAA requires encryption at rest and in transit for ePHI.
 * §164.312(a)(2)(iv): Encryption at rest
 * §164.312(e)(1): Encryption in transit
 * 
 * Uses AES-256-GCM with authentication (protects integrity + confidentiality).
 */
export class PHIEncryptionService {
  private readonly masterKey: Buffer;
  private readonly keyVersion: string;

  constructor() {
    const keyEnv = process.env.PHI_ENCRYPTION_KEY;
    if (!keyEnv) {
      throw new Error('PHI_ENCRYPTION_KEY is mandatory for HIPAA compliance');
    }

    this.masterKey = Buffer.from(keyEnv, 'hex');
    this.keyVersion = process.env.PHI_KEY_VERSION ?? 'v1';

    if (this.masterKey.length !== 32) {
      throw new Error('PHI_ENCRYPTION_KEY must be exactly 256 bits (64 hex characters)');
    }
  }

  /**
   * Encrypt an individual PHI field.
   * Returns: keyVersion:iv:authTag:ciphertext (all in base64)
   */
  encryptField(plaintext: string): string {
    const iv = crypto.randomBytes(IV_LENGTH);
    const cipher = crypto.createCipheriv(ALGORITHM, this.masterKey, iv, {
      authTagLength: AUTH_TAG_LENGTH,
    });

    const encrypted = Buffer.concat([
      cipher.update(plaintext, 'utf8'),
      cipher.final(),
    ]);
    const authTag = cipher.getAuthTag();

    // Format: version:iv:tag:ciphertext
    return [
      this.keyVersion,
      iv.toString('base64'),
      authTag.toString('base64'),
      encrypted.toString('base64'),
    ].join(':');
  }

  /**
   * Decrypt a PHI field.
   */
  decryptField(encryptedData: string): string {
    const [version, ivB64, tagB64, ciphertextB64] = encryptedData.split(':');

    // Check key version (for key rotation)
    if (version !== this.keyVersion) {
      logger.warn({
        event: 'key_version_mismatch',
        expected: this.keyVersion,
        found: version,
      }, 'Key version mismatch — consider re-encryption');
    }

    const iv = Buffer.from(ivB64, 'base64');
    const authTag = Buffer.from(tagB64, 'base64');
    const ciphertext = Buffer.from(ciphertextB64, 'base64');

    const decipher = crypto.createDecipheriv(ALGORITHM, this.masterKey, iv, {
      authTagLength: AUTH_TAG_LENGTH,
    });
    decipher.setAuthTag(authTag);

    const decrypted = Buffer.concat([
      decipher.update(ciphertext),
      decipher.final(),
    ]);

    return decrypted.toString('utf8');
  }

  /**
   * Encrypt a complete PHI object (multiple fields).
   */
  encryptPHIObject<T extends Record<string, unknown>>(
    data: T,
    fieldsToEncrypt: (keyof T)[]
  ): T {
    const encrypted = { ...data };

    for (const field of fieldsToEncrypt) {
      const value = data[field];
      if (value !== null && value !== undefined) {
        const stringValue = typeof value === 'string' ? value : JSON.stringify(value);
        (encrypted as Record<string, unknown>)[field as string] = this.encryptField(stringValue);
      }
    }

    return encrypted;
  }

  /**
   * Decrypt a complete PHI object.
   */
  decryptPHIObject<T extends Record<string, unknown>>(
    data: T,
    fieldsToDecrypt: (keyof T)[]
  ): T {
    const decrypted = { ...data };

    for (const field of fieldsToDecrypt) {
      const value = data[field];
      if (typeof value === 'string' && value.includes(':')) {
        try {
          (decrypted as Record<string, unknown>)[field as string] = this.decryptField(value);
        } catch {
          logger.error({ field: String(field) }, 'Error decrypting PHI field');
        }
      }
    }

    return decrypted;
  }

  /**
   * De-identify data using HIPAA's Safe Harbor method.
   * Removes the 18 identifiers defined by HIPAA.
   * De-identified data is no longer PHI.
   */
  static deIdentify(record: Record<string, unknown>): Record<string, unknown> {
    const IDENTIFIERS_TO_REMOVE = [
      'firstName', 'lastName', 'name', 'fullName',
      'address', 'city', 'zipCode', 'state',
      'phone', 'fax', 'email',
      'ssn', 'socialSecurityNumber',
      'mrn', 'medicalRecordNumber',
      'healthPlanId', 'insurancePolicyId',
      'accountNumber', 'licenseNumber',
      'vehicleId', 'deviceId',
      'ipAddress', 'url',
      'biometricId', 'photo',
    ];

    const deIdentified = { ...record };

    for (const identifier of IDENTIFIERS_TO_REMOVE) {
      if (identifier in deIdentified) {
        delete deIdentified[identifier];
      }
    }

    // Generalize dates: only keep the year
    if (deIdentified.dateOfBirth instanceof Date) {
      deIdentified.birthYear = (deIdentified.dateOfBirth as Date).getFullYear();
      delete deIdentified.dateOfBirth;
    }

    // Generalize location: only keep the first 3 ZIP digits if population > 20,000
    if (typeof deIdentified.zipCode === 'string') {
      deIdentified.zipPrefix = (deIdentified.zipCode as string).substring(0, 3);
      delete deIdentified.zipCode;
    }

    return deIdentified;
  }
}
```

---

### 3. HIPAA Audit Middleware

```typescript
// middleware/hipaa-audit.middleware.ts

import { Request, Response, NextFunction } from 'express';
import pino from 'pino';

const logger = pino({
  name: 'hipaa-audit',
  // HIPAA requires tamper-proof logs
  // In production, send to a SIEM or immutable storage
  redact: {
    paths: [
      'req.headers.authorization',
      'body.password',
      'body.ssn',
      '*.ssn',
    ],
    censor: '[PHI-REDACTED]',
  },
});

/**
 * HIPAA audit middleware.
 * Logs all interactions with the system that involve PHI.
 * 
 * §164.312(b): "Implement hardware, software, and/or procedural mechanisms
 * that record and examine activity in information systems that contain or use ePHI."
 */
export function hipaaAuditMiddleware(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();

  // Capture the original response body
  const originalSend = res.send.bind(res);
  
  res.send = function (body: any) {
    const duration = Date.now() - startTime;

    logger.info({
      event: 'http_request',
      audit: {
        timestamp: new Date().toISOString(),
        userId: req.user?.id ?? 'anonymous',
        userRole: req.user?.role ?? 'unknown',
        sessionId: req.session?.id,
        action: `${req.method} ${req.route?.path ?? req.path}`,
        resource: req.originalUrl,
        sourceIp: req.ip,
        userAgent: req.headers['user-agent'],
        statusCode: res.statusCode,
        duration,
        // Do not log the response body if it contains PHI
        containsPHI: isPHIRoute(req.path),
      },
    }, `${req.method} ${req.originalUrl} ${res.statusCode} ${duration}ms`);

    return originalSend(body);
  };

  next();
}

/**
 * Determine if a route may contain PHI.
 */
function isPHIRoute(path: string): boolean {
  const phiPatterns = [
    '/patients',
    '/records',
    '/diagnos',
    '/treatment',
    '/medication',
    '/lab-result',
    '/clinical',
  ];

  return phiPatterns.some(pattern => path.toLowerCase().includes(pattern));
}

/**
 * Middleware for auto-logoff due to inactivity.
 * HIPAA §164.312(a)(2)(iii): "Implement electronic procedures that terminate
 * an electronic session after a predetermined time of inactivity."
 */
export function sessionTimeoutMiddleware(timeoutSeconds: number = 900) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (!req.session?.lastActivity) {
      req.session.lastActivity = Date.now();
      return next();
    }

    const elapsed = (Date.now() - req.session.lastActivity) / 1000;

    if (elapsed > timeoutSeconds) {
      logger.info({
        event: 'session_timeout',
        userId: req.user?.id,
        inactiveSeconds: elapsed,
      }, 'Session terminated due to inactivity');

      req.session.destroy((err) => {
        if (err) logger.error({ err }, 'Error destroying session');
      });

      return res.status(440).json({
        error: 'Session expired',
        code: 'SESSION_TIMEOUT',
        message: 'Your session has expired due to inactivity. Please log in again.',
      });
    }

    req.session.lastActivity = Date.now();
    next();
  };
}
```

---

### 4. Breach Notification (Breach Notification Rule)

```typescript
// services/hipaa-breach-notification.service.ts

import pino from 'pino';

const logger = pino({ name: 'hipaa-breach-notification' });

interface BreachDetails {
  discoveredAt: Date;
  natureOfBreach: string;
  typesOfPHI: string[];
  numberOfAffected: number;
  affectedPatientIds: string[];
  unauthorizedEntity?: string;
  mitigationActions: string[];
  discoveredBy: string;
}

/**
 * HIPAA breach notification service.
 * 
 * Mandatory timelines:
 * - Affected individuals: without unreasonable delay, maximum 60 days
 * - HHS (if > 500 affected): without unreasonable delay, maximum 60 days
 * - HHS (if < 500 affected): up to 60 days after the end of the calendar year
 * - Media (if > 500 in a state): without unreasonable delay
 */
export class HIPAABreachNotificationService {
  async reportBreach(breach: BreachDetails) {
    logger.fatal({
      event: 'phi_breach_detected',
      ...breach,
    }, '🚨 PHI BREACH DETECTED');

    // 1. Risk assessment (4 factors)
    const riskAssessment = this.assessRisk(breach);

    if (riskAssessment.requiresNotification) {
      // 2. Notify internal security team immediately
      await this.notifySecurityTeam(breach, riskAssessment);

      // 3. Initiate notification process
      if (breach.numberOfAffected > 500) {
        await this.notifyHHS(breach); // Health and Human Services
        await this.notifyMedia(breach); // Media if > 500 in a state
      }

      // 4. Prepare individual notifications
      await this.prepareIndividualNotifications(breach);
    }

    // 5. Document everything
    await this.documentBreach(breach, riskAssessment);

    return riskAssessment;
  }

  /**
   * HHS 4-factor risk assessment.
   */
  private assessRisk(breach: BreachDetails) {
    // Factor 1: Nature and extent of the PHI
    // Factor 2: The unauthorized person who used the PHI
    // Factor 3: Whether the PHI was actually acquired or viewed
    // Factor 4: Extent to which the risk has been mitigated

    return {
      requiresNotification: true, // Presumption of breach unless low risk demonstrated
      riskLevel: 'high' as const,
      notificationDeadline: new Date(Date.now() + 60 * 24 * 60 * 60 * 1000), // 60 days
      factors: {
        natureOfPHI: 'clinical_data',
        unauthorizedAccess: breach.unauthorizedEntity ?? 'unknown',
        phiAcquired: true, // Conservative presumption
        mitigationEffectiveness: breach.mitigationActions.length > 0 ? 'partial' : 'none',
      },
    };
  }

  private async notifySecurityTeam(breach: BreachDetails, risk: any) {
    // Integrate with your alerting system (PagerDuty, Slack, email)
    logger.fatal({
      event: 'security_team_notified',
      breach: breach.natureOfBreach,
      affected: breach.numberOfAffected,
      riskLevel: risk.riskLevel,
    }, 'Security team notified');
  }

  private async notifyHHS(breach: BreachDetails) {
    // In production: submit form to HHS breach portal
    logger.info({
      event: 'hhs_notification_prepared',
      affected: breach.numberOfAffected,
    }, 'HHS notification prepared');
  }

  private async notifyMedia(breach: BreachDetails) {
    logger.info({ event: 'media_notification_required' }, 'Media notification required (>500 affected)');
  }

  private async prepareIndividualNotifications(breach: BreachDetails) {
    // Prepare notification letters/emails for affected patients
    logger.info({
      event: 'individual_notifications_prepared',
      count: breach.numberOfAffected,
    }, 'Individual notifications prepared');
  }

  private async documentBreach(breach: BreachDetails, risk: any) {
    // HIPAA requires maintaining breach documentation for 6 years
    logger.info({
      event: 'breach_documented',
      retainUntil: new Date(Date.now() + 6 * 365 * 24 * 60 * 60 * 1000).toISOString(),
    }, 'Breach documented for 6-year retention');
  }
}
```

---

### 5. BAA (Business Associate Agreement) — Technical Verification

```typescript
// services/baa-compliance.service.ts

/**
 * Service to verify that all third-party services
 * have a signed BAA before processing PHI.
 * 
 * HIPAA requires a BAA with any Business Associate
 * that accesses, maintains, uses, or transmits PHI.
 */

interface BusinessAssociate {
  name: string;
  service: string;
  baaSignedDate: Date;
  baaExpiryDate: Date;
  contactEmail: string;
  dataProcessed: string[];
}

// Registry of Business Associates with active BAA
const BUSINESS_ASSOCIATES: BusinessAssociate[] = [
  {
    name: 'AWS',
    service: 'Cloud Infrastructure (HIPAA eligible)',
    baaSignedDate: new Date('2024-01-15'),
    baaExpiryDate: new Date('2026-01-15'),
    contactEmail: 'compliance@example.com',
    dataProcessed: ['ePHI storage', 'ePHI processing', 'backups'],
  },
  // Add all third parties that handle PHI
];

export function verifyBAA(serviceName: string): boolean {
  const ba = BUSINESS_ASSOCIATES.find(
    b => b.service.toLowerCase().includes(serviceName.toLowerCase())
  );

  if (!ba) {
    throw new Error(
      `⚠️ HIPAA VIOLATION: No BAA exists for service "${serviceName}". ` +
      'Cannot send PHI to this service without a signed BAA.'
    );
  }

  if (ba.baaExpiryDate < new Date()) {
    throw new Error(
      `⚠️ BAA EXPIRED for ${ba.name}. Renew before continuing to process PHI.`
    );
  }

  return true;
}
```

---

## Agent workflow

1. Identify what health data the application processes and classify as standard PHI, highly sensitive, or restricted.
2. Implement the data model with RBAC access control, PHI field encryption, and complete audit trail.
3. Implement the access control service with per-role permission matrix, minimum necessary principle, and break-the-glass mechanism.
4. Add AES-256-GCM encryption for ePHI at rest with key versioning and Safe Harbor de-identification method.
5. Implement HIPAA audit middleware for all routes handling PHI and auto-logoff for inactivity.
6. Configure the breach notification service with 4-factor risk assessment and notification timelines.
7. Verify that all third-party services have a signed and current BAA before processing PHI.
8. Validate against the compliance checklist (technical, administrative, physical, BAs) before deploying.

## Gotchas

Encrypting all ePHI at rest (AES-256) and in transit (TLS 1.2+) is mandatory, not optional. MFA is required for all access to systems with PHI. Auto-logoff must activate after 15 minutes of inactivity maximum (§164.312(a)(2)(iii)). The audit trail must record who accessed what PHI, when, from where, and whether it was successful or failed. The break-the-glass mechanism for emergency access must exist but with exhaustive logging. Do not send PHI via unencrypted email. Do not use cloud services without a signed BAA. Do not log PHI in plain text in log files. Do not copy PHI to development environments without de-identifying using the Safe Harbor method (remove all 18 identifiers). Do not share access credentials — each user must have a unique ID. Do not discard hardware containing PHI without certified sanitization. Breaches must be reported to affected individuals within 60 days maximum, and to HHS immediately if more than 500 individuals are affected. Breach documentation must be retained for 6 years.

---

## HIPAA Compliance Checklist

### Technical Safeguards
- [ ] AES-256 encryption for ePHI at rest
- [ ] TLS 1.2+ for ePHI in transit
- [ ] Role-based access control (RBAC)
- [ ] Unique user IDs — no shared accounts
- [ ] Auto-logoff for inactivity (≤15 min)
- [ ] Emergency access mechanism (break-the-glass)
- [ ] Audit logs for all ePHI access
- [ ] Data integrity — alteration detection mechanisms

### Administrative Safeguards
- [ ] Designated Security Officer
- [ ] Designated Privacy Officer
- [ ] Documented risk analysis
- [ ] Risk management plan
- [ ] Written security policies and procedures
- [ ] Workforce training
- [ ] Contingency plan (backup, recovery, emergency)
- [ ] Breach notification process

### Physical Safeguards
- [ ] Facility access control
- [ ] Workstations in secure locations
- [ ] Mobile device usage policies
- [ ] Media sanitization before disposal

### Business Associates
- [ ] Signed BAA with all vendors that handle PHI
- [ ] Updated inventory of Business Associates
- [ ] Periodic BA compliance review

---

## References and Resources

- [Official HIPAA Text](https://www.hhs.gov/hipaa/index.html)
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [HHS Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf)
- [NIST SP 800-66 (HIPAA Security Rule Implementation)](https://csrc.nist.gov/publications/detail/sp/800-66/rev-2/final)
- [OCR Enforcement Actions](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html)
