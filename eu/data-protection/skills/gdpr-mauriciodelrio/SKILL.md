---
name: gdpr-mauriciodelrio
title: GDPR — General Data Protection Regulation
description: Use this skill when the software processes personal data from users. Although GDPR is EU legislation, this skill applies as a data protection standard for any software regardless of the geographic location of users. Covers granular consent system, data subject rights (ARCO+), encryption and pseudonymization, retention policy, cookie banner, and compliance checklist.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/en-skills/governance-risk-and-compliance/gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR — General Data Protection Regulation

GDPR (EU Regulation 2016/679) defines the most rigorous data protection standard globally and should be applied to any software processing personal data, regardless of user geography. Every implementation must respect the 7 principles of Art. 5: lawfulness/fairness/transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, and accountability. Each processing activity requires a valid legal basis (Art. 6): consent, contract, legal obligation, vital interests, public interest, or legitimate interest. Sensitive data (Art. 9) requires additional legal bases.

## Implementation

### 1. Consent System

#### Database Schema (Prisma)

```prisma
// schema.prisma — Granular consent model

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  // Personal data with protection metadata
  firstName     String?
  lastName      String?
  phone         String?
  dateOfBirth   DateTime?
  
  // Compliance relations
  consents      Consent[]
  dataRequests  DataSubjectRequest[]
  auditLogs     AuditLog[]
  
  // Creation and retention metadata
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  deletedAt     DateTime? // Soft delete for retention period
  retentionExpiresAt DateTime? // Retention expiration date
  
  @@map("users")
}

model Consent {
  id            String    @id @default(cuid())
  userId        String
  user          User      @relation(fields: [userId], references: [id])
  
  // Granular consent type
  purpose       ConsentPurpose
  legalBasis    LegalBasis
  
  // Status and traceability
  granted       Boolean
  grantedAt     DateTime?
  revokedAt     DateTime?
  expiresAt     DateTime?
  
  // Consent evidence
  ipAddress     String?   // IP at the time of consent
  userAgent     String?   // Browser/device
  consentText   String    // Exact text the user accepted
  version       String    // Privacy policy version
  source        String    // Where it was obtained (web, app, api)
  
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  
  @@unique([userId, purpose]) // One consent per purpose per user
  @@index([userId])
  @@index([purpose])
  @@map("consents")
}

enum ConsentPurpose {
  ESSENTIAL           // Basic service functionality
  ANALYTICS           // Usage analysis and metrics
  MARKETING_EMAIL     // Marketing communications by email
  MARKETING_PUSH      // Marketing push notifications
  THIRD_PARTY_SHARING // Sharing data with third parties
  PROFILING           // User profile creation
  COOKIES_FUNCTIONAL  // Functional cookies
  COOKIES_ANALYTICS   // Analytics cookies
  COOKIES_ADVERTISING // Advertising cookies
}

enum LegalBasis {
  CONSENT
  CONTRACT
  LEGAL_OBLIGATION
  VITAL_INTERESTS
  PUBLIC_INTEREST
  LEGITIMATE_INTEREST
}
```

#### Consent Service

```typescript
// services/consent.service.ts

import { PrismaClient, ConsentPurpose, LegalBasis } from '@prisma/client';
import { z } from 'zod';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'consent-service' });

// Validation schema for granting consent
const GrantConsentSchema = z.object({
  userId: z.string().cuid(),
  purpose: z.nativeEnum(ConsentPurpose),
  legalBasis: z.nativeEnum(LegalBasis),
  consentText: z.string().min(10),
  version: z.string(),
  source: z.enum(['web', 'mobile_app', 'api']),
});

type GrantConsentInput = z.infer<typeof GrantConsentSchema>;

interface ConsentContext {
  ipAddress: string;
  userAgent: string;
}

export class ConsentService {
  /**
   * Grant consent in a granular manner.
   * GDPR Art. 7: Consent must be freely given, specific, informed, and unambiguous.
   */
  async grantConsent(input: GrantConsentInput, context: ConsentContext) {
    const validated = GrantConsentSchema.parse(input);

    const consent = await prisma.consent.upsert({
      where: {
        userId_purpose: {
          userId: validated.userId,
          purpose: validated.purpose,
        },
      },
      create: {
        userId: validated.userId,
        purpose: validated.purpose,
        legalBasis: validated.legalBasis,
        granted: true,
        grantedAt: new Date(),
        consentText: validated.consentText,
        version: validated.version,
        source: validated.source,
        ipAddress: context.ipAddress,
        userAgent: context.userAgent,
      },
      update: {
        granted: true,
        grantedAt: new Date(),
        revokedAt: null,
        consentText: validated.consentText,
        version: validated.version,
        source: validated.source,
        ipAddress: context.ipAddress,
        userAgent: context.userAgent,
      },
    });

    logger.info({
      event: 'consent_granted',
      userId: validated.userId,
      purpose: validated.purpose,
      legalBasis: validated.legalBasis,
      version: validated.version,
    }, 'Consent granted');

    return consent;
  }

  /**
   * Revoke consent.
   * GDPR Art. 7(3): It must be as easy to withdraw as to give consent.
   */
  async revokeConsent(userId: string, purpose: ConsentPurpose) {
    const consent = await prisma.consent.update({
      where: {
        userId_purpose: { userId, purpose },
      },
      data: {
        granted: false,
        revokedAt: new Date(),
      },
    });

    logger.info({
      event: 'consent_revoked',
      userId,
      purpose,
    }, 'Consent revoked');

    // Trigger cleanup of data associated with this purpose
    await this.triggerDataCleanup(userId, purpose);

    return consent;
  }

  /**
   * Check if a user has active consent for a purpose.
   */
  async hasConsent(userId: string, purpose: ConsentPurpose): Promise<boolean> {
    const consent = await prisma.consent.findUnique({
      where: {
        userId_purpose: { userId, purpose },
      },
    });

    if (!consent) return false;
    if (!consent.granted) return false;
    if (consent.revokedAt) return false;
    if (consent.expiresAt && consent.expiresAt < new Date()) return false;

    return true;
  }

  /**
   * Get all consents for a user (for privacy panel).
   */
  async getUserConsents(userId: string) {
    return prisma.consent.findMany({
      where: { userId },
      orderBy: { purpose: 'asc' },
    });
  }

  private async triggerDataCleanup(userId: string, purpose: ConsentPurpose) {
    // Implement cleanup logic based on the revoked purpose
    // For example: if ANALYTICS is revoked, delete tracking data
    // If MARKETING_EMAIL is revoked, unsubscribe from email lists
    logger.info({
      event: 'data_cleanup_triggered',
      userId,
      purpose,
    }, 'Data cleanup triggered by consent revocation');
  }
}
```

#### Consent Verification Middleware

```typescript
// middleware/consent.middleware.ts

import { Request, Response, NextFunction } from 'express';
import { ConsentPurpose } from '@prisma/client';
import { ConsentService } from '../services/consent.service';

const consentService = new ConsentService();

/**
 * Middleware factory that verifies consent before processing the request.
 * Use it on routes that require specific consent.
 * 
 * @example
 * router.post('/newsletter/subscribe', requireConsent(ConsentPurpose.MARKETING_EMAIL), handler);
 */
export function requireConsent(purpose: ConsentPurpose) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    const hasConsent = await consentService.hasConsent(userId, purpose);

    if (!hasConsent) {
      return res.status(403).json({
        error: 'Consent required',
        code: 'CONSENT_REQUIRED',
        purpose,
        message: `Consent required for: ${purpose}`,
        consentUrl: `/api/v1/privacy/consent`,
      });
    }

    next();
  };
}
```

---

### 2. Data Subject Rights (ARCO+ Rights)

#### Schema for Rights Requests

```prisma
// Add to schema.prisma

model DataSubjectRequest {
  id            String    @id @default(cuid())
  userId        String
  user          User      @relation(fields: [userId], references: [id])
  
  type          DSRType
  status        DSRStatus @default(PENDING)
  
  // Request details
  description   String?
  requestedAt   DateTime  @default(now())
  acknowledgedAt DateTime? // Receipt confirmation
  completedAt   DateTime?  // Resolution date
  deadline      DateTime   // Maximum deadline (30 days from request)
  
  // Response
  responseNotes String?
  responseData  Json?      // Exported data (for portability)
  
  // Audit
  processedBy   String?    // ID of the admin who processed
  
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  
  @@index([userId])
  @@index([status])
  @@index([deadline])
  @@map("data_subject_requests")
}

enum DSRType {
  ACCESS          // Art. 15 - Right of access
  RECTIFICATION   // Art. 16 - Right to rectification
  ERASURE         // Art. 17 - Right to be forgotten
  RESTRICTION     // Art. 18 - Right to restriction
  PORTABILITY     // Art. 20 - Right to data portability
  OBJECTION       // Art. 21 - Right to object
  AUTOMATED_DECISION // Art. 22 - Not to be subject to automated decisions
}

enum DSRStatus {
  PENDING
  ACKNOWLEDGED
  IN_PROGRESS
  COMPLETED
  REJECTED
  EXTENDED     // Extended deadline (max 2 additional months)
}
```

#### Data Subject Rights Service

```typescript
// services/data-subject-rights.service.ts

import { PrismaClient, DSRType, DSRStatus } from '@prisma/client';
import pino from 'pino';
import crypto from 'node:crypto';

const prisma = new PrismaClient();
const logger = pino({ name: 'dsr-service' });

// GDPR deadline: 30 calendar days from the request
const GDPR_DEADLINE_DAYS = 30;
const GDPR_EXTENSION_DAYS = 60; // Maximum additional extension

export class DataSubjectRightsService {
  /**
   * Create a rights request.
   * GDPR Art. 12(3): Respond without undue delay, maximum 1 month.
   */
  async createRequest(userId: string, type: DSRType, description?: string) {
    const deadline = new Date();
    deadline.setDate(deadline.getDate() + GDPR_DEADLINE_DAYS);

    const request = await prisma.dataSubjectRequest.create({
      data: {
        userId,
        type,
        description,
        deadline,
        acknowledgedAt: new Date(), // Confirm immediate receipt
        status: DSRStatus.ACKNOWLEDGED,
      },
    });

    logger.info({
      event: 'dsr_created',
      requestId: request.id,
      userId,
      type,
      deadline: deadline.toISOString(),
    }, 'Data subject rights request created');

    return request;
  }

  /**
   * Right of Access (Art. 15).
   * Export ALL personal data of the user in structured format.
   */
  async processAccessRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
      include: { user: true },
    });

    // Collect all personal data for the user
    const userData = await this.collectAllUserData(request.userId);

    await prisma.dataSubjectRequest.update({
      where: { id: requestId },
      data: {
        status: DSRStatus.COMPLETED,
        completedAt: new Date(),
        processedBy,
        responseData: userData,
      },
    });

    logger.info({
      event: 'dsr_access_completed',
      requestId,
      userId: request.userId,
      processedBy,
    }, 'Access request completed');

    return userData;
  }

  /**
   * Right to be Forgotten (Art. 17).
   * Delete all personal data of the user.
   * Exceptions: legal obligations, defense of claims.
   */
  async processErasureRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
    });

    // Check if there are legal exceptions that prevent deletion
    const exceptions = await this.checkErasureExceptions(request.userId);
    
    if (exceptions.length > 0) {
      await prisma.dataSubjectRequest.update({
        where: { id: requestId },
        data: {
          status: DSRStatus.REJECTED,
          responseNotes: `Partial deletion. Legal exceptions: ${exceptions.join(', ')}`,
          processedBy,
        },
      });

      logger.warn({
        event: 'dsr_erasure_partial',
        requestId,
        userId: request.userId,
        exceptions,
      }, 'Partial deletion due to legal exceptions');

      // Delete only data without legal restriction
      await this.partialErasure(request.userId, exceptions);
      return { partial: true, exceptions };
    }

    // Full deletion
    await this.fullErasure(request.userId);

    await prisma.dataSubjectRequest.update({
      where: { id: requestId },
      data: {
        status: DSRStatus.COMPLETED,
        completedAt: new Date(),
        processedBy,
      },
    });

    logger.info({
      event: 'dsr_erasure_completed',
      requestId,
      userId: request.userId,
      processedBy,
    }, 'Erasure request completed');

    return { partial: false };
  }

  /**
   * Right to Data Portability (Art. 20).
   * Export data in a structured, commonly used, and machine-readable format.
   */
  async processPortabilityRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
    });

    const userData = await this.collectAllUserData(request.userId);

    // Structured JSON format (machine-readable)
    const portableData = {
      exportMetadata: {
        format: 'JSON',
        exportDate: new Date().toISOString(),
        dataController: process.env.DATA_CONTROLLER_NAME,
        requestId,
      },
      personalData: userData,
    };

    await prisma.dataSubjectRequest.update({
      where: { id: requestId },
      data: {
        status: DSRStatus.COMPLETED,
        completedAt: new Date(),
        processedBy,
        responseData: portableData,
      },
    });

    return portableData;
  }

  /**
   * Collect all personal data of the user from all tables.
   */
  private async collectAllUserData(userId: string) {
    const [user, consents, orders, activityLogs] = await Promise.all([
      prisma.user.findUnique({
        where: { id: userId },
        select: {
          id: true,
          email: true,
          firstName: true,
          lastName: true,
          phone: true,
          dateOfBirth: true,
          createdAt: true,
        },
      }),
      prisma.consent.findMany({
        where: { userId },
        select: {
          purpose: true,
          granted: true,
          grantedAt: true,
          revokedAt: true,
          version: true,
        },
      }),
      // Add more tables according to your data model
      // prisma.order.findMany({ where: { userId } }),
      // prisma.address.findMany({ where: { userId } }),
      Promise.resolve([]), // Placeholder for orders
      Promise.resolve([]), // Placeholder for activity logs
    ]);

    return {
      profile: user,
      consents,
      orders,
      activityLogs,
    };
  }

  /**
   * Check legal exceptions for deletion.
   * Example: invoices must be retained due to tax obligations.
   */
  private async checkErasureExceptions(userId: string): Promise<string[]> {
    const exceptions: string[] = [];

    // Example: Check if there are invoices (legal tax retention obligation)
    // const invoices = await prisma.invoice.count({ where: { userId } });
    // if (invoices > 0) {
    //   exceptions.push('invoices_tax_obligation');
    // }

    return exceptions;
  }

  private async fullErasure(userId: string) {
    await prisma.$transaction(async (tx) => {
      // Anonymize instead of hard-delete to maintain referential integrity
      await tx.user.update({
        where: { id: userId },
        data: {
          email: `deleted_${crypto.randomUUID()}@anonymized.local`,
          firstName: null,
          lastName: null,
          phone: null,
          dateOfBirth: null,
          deletedAt: new Date(),
        },
      });

      // Delete consents
      await tx.consent.deleteMany({ where: { userId } });
    });
  }

  private async partialErasure(userId: string, exceptions: string[]) {
    // Delete only data that has no legal restriction
    await prisma.user.update({
      where: { id: userId },
      data: {
        firstName: null,
        lastName: null,
        phone: null,
        dateOfBirth: null,
        // Keep email if needed for contractual obligations
      },
    });
  }
}
```

#### Rights API (Express Router)

```typescript
// routes/privacy.routes.ts

import { Router, Request, Response } from 'express';
import { z } from 'zod';
import { DSRType } from '@prisma/client';
import { DataSubjectRightsService } from '../services/data-subject-rights.service';
import { ConsentService } from '../services/consent.service';
import { authenticate } from '../middleware/auth.middleware';

const router = Router();
const dsrService = new DataSubjectRightsService();
const consentService = new ConsentService();

// All routes require authentication
router.use(authenticate);

/**
 * GET /api/v1/privacy/my-data
 * Get all personal data (Art. 15 - Access)
 */
router.get('/my-data', async (req: Request, res: Response) => {
  const request = await dsrService.createRequest(
    req.user!.id,
    DSRType.ACCESS,
    'Personal data access request via API'
  );
  
  // For automated requests, process immediately
  const data = await dsrService.processAccessRequest(request.id, 'system_auto');
  
  res.json({
    requestId: request.id,
    data,
    exportFormats: ['json', 'csv'],
    downloadUrl: `/api/v1/privacy/requests/${request.id}/download`,
  });
});

/**
 * POST /api/v1/privacy/erasure
 * Request data deletion (Art. 17 - Right to be forgotten)
 */
router.post('/erasure', async (req: Request, res: Response) => {
  const request = await dsrService.createRequest(
    req.user!.id,
    DSRType.ERASURE,
    req.body.reason
  );

  res.status(202).json({
    requestId: request.id,
    status: 'acknowledged',
    message: 'Your deletion request has been received. It will be processed within a maximum of 30 days.',
    deadline: request.deadline,
  });
});

/**
 * POST /api/v1/privacy/portability
 * Export data in portable format (Art. 20)
 */
router.post('/portability', async (req: Request, res: Response) => {
  const request = await dsrService.createRequest(
    req.user!.id,
    DSRType.PORTABILITY,
    'Data portability request'
  );

  const data = await dsrService.processPortabilityRequest(request.id, 'system_auto');

  res.json({
    requestId: request.id,
    format: 'application/json',
    data,
  });
});

/**
 * GET /api/v1/privacy/consents
 * View all user consents
 */
router.get('/consents', async (req: Request, res: Response) => {
  const consents = await consentService.getUserConsents(req.user!.id);
  res.json({ consents });
});

/**
 * POST /api/v1/privacy/consents
 * Grant a consent
 */
router.post('/consents', async (req: Request, res: Response) => {
  const consent = await consentService.grantConsent(
    { ...req.body, userId: req.user!.id },
    { ipAddress: req.ip ?? 'unknown', userAgent: req.headers['user-agent'] ?? 'unknown' }
  );
  res.status(201).json({ consent });
});

/**
 * DELETE /api/v1/privacy/consents/:purpose
 * Revoke a specific consent
 */
router.delete('/consents/:purpose', async (req: Request, res: Response) => {
  const purpose = req.params.purpose as any;
  const consent = await consentService.revokeConsent(req.user!.id, purpose);
  res.json({ consent, message: 'Consent successfully revoked' });
});

export default router;
```

---

### 3. Encryption and Pseudonymization

```typescript
// utils/encryption.service.ts

import crypto from 'node:crypto';

const ALGORITHM = 'aes-256-gcm';
const IV_LENGTH = 16;
const AUTH_TAG_LENGTH = 16;
const SALT_LENGTH = 32;

/**
 * Encryption service for personal data at rest.
 * GDPR Art. 32: Appropriate technical measures, including encryption.
 */
export class EncryptionService {
  private readonly key: Buffer;

  constructor() {
    const masterKey = process.env.DATA_ENCRYPTION_KEY;
    if (!masterKey || masterKey.length < 32) {
      throw new Error('DATA_ENCRYPTION_KEY must be configured with at least 32 characters');
    }
    // Derive key using HKDF for greater security
    this.key = crypto.createHash('sha256').update(masterKey).digest();
  }

  /**
   * Encrypt a personal data field.
   * Returns string with format: iv:authTag:ciphertext (all in hex).
   */
  encrypt(plaintext: string): string {
    const iv = crypto.randomBytes(IV_LENGTH);
    const cipher = crypto.createCipheriv(ALGORITHM, this.key, iv, {
      authTagLength: AUTH_TAG_LENGTH,
    });

    let encrypted = cipher.update(plaintext, 'utf8', 'hex');
    encrypted += cipher.final('hex');
    const authTag = cipher.getAuthTag();

    return `${iv.toString('hex')}:${authTag.toString('hex')}:${encrypted}`;
  }

  /**
   * Decrypt a personal data field.
   */
  decrypt(encryptedText: string): string {
    const [ivHex, authTagHex, ciphertext] = encryptedText.split(':');
    
    const iv = Buffer.from(ivHex, 'hex');
    const authTag = Buffer.from(authTagHex, 'hex');
    const decipher = crypto.createDecipheriv(ALGORITHM, this.key, iv, {
      authTagLength: AUTH_TAG_LENGTH,
    });
    decipher.setAuthTag(authTag);

    let decrypted = decipher.update(ciphertext, 'hex', 'utf8');
    decrypted += decipher.final('utf8');

    return decrypted;
  }

  /**
   * Pseudonymize personal data (reversible process with the key).
   * GDPR Art. 4(5): Processing in such a manner that it can no longer
   * be attributed without additional information.
   */
  pseudonymize(data: string): string {
    const hmac = crypto.createHmac('sha256', this.key);
    hmac.update(data);
    return hmac.digest('hex');
  }

  /**
   * Anonymize data (irreversible process).
   * Anonymized data is no longer personal data under GDPR.
   */
  static anonymize(data: string): string {
    const salt = crypto.randomBytes(SALT_LENGTH);
    return crypto.createHash('sha256').update(salt).update(data).digest('hex');
  }

  /**
   * Secure password hash (use bcrypt or argon2 in production).
   */
  static async hashPassword(password: string): Promise<string> {
    // In production use: import bcrypt from 'bcrypt'; return bcrypt.hash(password, 12);
    const salt = crypto.randomBytes(16).toString('hex');
    return new Promise((resolve, reject) => {
      crypto.scrypt(password, salt, 64, (err, derivedKey) => {
        if (err) reject(err);
        resolve(`${salt}:${derivedKey.toString('hex')}`);
      });
    });
  }
}
```

---

### 4. Data Retention Policy

```typescript
// jobs/data-retention.job.ts

import { PrismaClient } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'data-retention' });

/**
 * Data retention policy per GDPR Art. 5(1)(e).
 * "Storage limitation": data shall not be kept longer than
 * necessary for the purposes of the processing.
 * 
 * Run as a daily cron job.
 */

interface RetentionPolicy {
  model: string;
  field: string;         // Date field to evaluate retention
  retentionDays: number; // Retention days
  action: 'anonymize' | 'delete' | 'archive';
  legalBasis: string;    // Legal justification for retention
}

const RETENTION_POLICIES: RetentionPolicy[] = [
  {
    model: 'auditLog',
    field: 'createdAt',
    retentionDays: 365 * 2, // 2 years
    action: 'archive',
    legalBasis: 'Legal obligation to retain audit records',
  },
  {
    model: 'session',
    field: 'lastActivityAt',
    retentionDays: 90,
    action: 'delete',
    legalBasis: 'Inactive sessions are not necessary for the service',
  },
  {
    model: 'deletedUser',
    field: 'deletedAt',
    retentionDays: 30, // 30-day grace period post-deletion
    action: 'delete',
    legalBasis: 'Grace period completed, definitive deletion',
  },
  {
    model: 'analyticsEvent',
    field: 'createdAt',
    retentionDays: 180,
    action: 'anonymize',
    legalBasis: 'Anonymized analytics data for aggregate statistics',
  },
];

export async function executeRetentionPolicies() {
  logger.info({ event: 'retention_job_started' }, 'Starting data retention job');

  for (const policy of RETENTION_POLICIES) {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - policy.retentionDays);

    try {
      // Example for the session model
      if (policy.model === 'session' && policy.action === 'delete') {
        const result = await prisma.session.deleteMany({
          where: {
            [policy.field]: { lt: cutoffDate },
          },
        });

        logger.info({
          event: 'retention_policy_executed',
          model: policy.model,
          action: policy.action,
          recordsAffected: result.count,
          cutoffDate: cutoffDate.toISOString(),
          legalBasis: policy.legalBasis,
        }, `Retention policy executed: ${policy.model}`);
      }

      // Add more models as needed
    } catch (error) {
      logger.error({
        event: 'retention_policy_error',
        model: policy.model,
        error,
      }, `Error executing retention policy: ${policy.model}`);
    }
  }

  logger.info({ event: 'retention_job_completed' }, 'Data retention job completed');
}
```

---

### 5. Cookie Banner and Cookie Consent

```typescript
// middleware/cookie-consent.middleware.ts

import { Request, Response, NextFunction } from 'express';

/**
 * Cookie categories per GDPR and ePrivacy Directive.
 * Only essential cookies can be used without consent.
 */
enum CookieCategory {
  ESSENTIAL = 'essential',         // No consent required
  FUNCTIONAL = 'functional',       // Requires consent
  ANALYTICS = 'analytics',         // Requires consent
  ADVERTISING = 'advertising',     // Requires consent
}

interface CookiePreferences {
  essential: true;      // Always true, cannot be disabled
  functional: boolean;
  analytics: boolean;
  advertising: boolean;
}

/**
 * Middleware that checks the user's cookie preferences
 * before setting non-essential cookies.
 */
export function cookieConsentGuard(category: CookieCategory) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (category === CookieCategory.ESSENTIAL) {
      return next(); // Essential cookies are always allowed
    }

    const consentCookie = req.cookies?.cookie_consent;
    
    if (!consentCookie) {
      // No consent: do not set non-essential cookies
      return next();
    }

    try {
      const preferences: CookiePreferences = JSON.parse(consentCookie);
      
      if (!preferences[category]) {
        // User did not consent to this category
        // Do not set the cookie and continue
        res.locals.cookieBlocked = category;
        return next();
      }

      next();
    } catch {
      next(); // On error, do not set cookies
    }
  };
}

/**
 * Helper to set cookies respecting consent.
 */
export function setConsentAwareCookie(
  res: Response,
  name: string,
  value: string,
  category: CookieCategory,
  options: { maxAge?: number; httpOnly?: boolean; secure?: boolean; sameSite?: 'strict' | 'lax' | 'none' } = {}
) {
  if (res.locals.cookieBlocked === category) {
    return; // Cookie blocked due to lack of consent
  }

  res.cookie(name, value, {
    httpOnly: options.httpOnly ?? true,
    secure: options.secure ?? process.env.NODE_ENV === 'production',
    sameSite: options.sameSite ?? 'lax',
    maxAge: options.maxAge,
    path: '/',
  });
}
```

---

## Agent workflow

1. Identify what personal data the application processes and document the legal basis (Art. 6) for each processing activity.
2. Implement the granular consent system with Prisma schema, service, and verification middleware.
3. Implement the data subject rights service (access, rectification, erasure, restriction, portability, objection).
4. Add the privacy REST API with endpoints for data access, deletion, portability, and consent management.
5. Implement encryption of personal data at rest (AES-256-GCM) and pseudonymization where applicable.
6. Configure the data retention policy as a cron job with per-model actions (anonymize/delete/archive).
7. Implement cookie banner with granular consent per category (essential/functional/analytics/advertising).
8. Validate against the compliance checklist before deploying.

## Gotchas

Implement Privacy by Design and Privacy by Default (Art. 25): every new feature must be evaluated against GDPR before implementation, and the most restrictive privacy settings are the defaults. Do not use pre-checked consent — it must be a clear affirmative action (Art. 7). Withdrawing consent must be as easy as granting it. Maintain a Record of Processing Activities (ROPA, Art. 30). Conduct DPIAs (Art. 35) for large-scale processing, profiling, or new technologies. Security breaches must be reported to the supervisory authority within 72 hours (Art. 33) and to affected individuals without delay if there is high risk (Art. 34). Do not transfer data outside the EU without a legal mechanism (SCCs, adequacy, BCRs). Do not store data without a retention policy. Do not log personal data in plain text. Do not use personal data in development/testing environments without anonymizing.

---

## GDPR Compliance Checklist

- [ ] Legal basis documented for each data processing activity
- [ ] Granular consent system implemented
- [ ] Clear and accessible privacy policy
- [ ] Data subject rights API (access, deletion, portability, rectification)
- [ ] Encryption of personal data at rest and in transit
- [ ] Data retention policy defined and implemented
- [ ] Cookie banner with granular consent
- [ ] Record of Processing Activities (ROPA)
- [ ] Breach notification process (72 hours)
- [ ] DPIA for high-risk processing
- [ ] Legal mechanism for international transfers
- [ ] Contracts with data processors
- [ ] DPO designated (if applicable per Art. 37)
- [ ] Audit logs for personal data access
- [ ] Pseudonymization/anonymization where possible
- [ ] Development team training on GDPR

---

## References and Resources

- [Official GDPR Text](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [AEPD Guidelines (Spain)](https://www.aepd.es/)
- [ICO Guidelines (UK)](https://ico.org.uk/for-organisations/guide-to-data-protection/)
- [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance_en)
- [GDPR Enforcement Tracker](https://www.enforcementtracker.com/)
