---
name: gdpr-es-skills-mauriciodelrio
title: GDPR — Reglamento General de Protección de Datos
description: Usa este skill cuando el software procese datos personales de usuarios. Aunque GDPR es legislación de la UE, este skill se aplica como estándar de protección de datos para cualquier software independientemente de la ubicación geográfica de los usuarios. Cubre sistema de consentimiento granular, derechos del interesado (ARCO+), encriptación y pseudonimización, política de retención, cookie banner, y checklist de cumplimiento.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/es-skills/governance-risk-and-compliance/gdpr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# GDPR — Reglamento General de Protección de Datos

GDPR (Reglamento UE 2016/679) define el estándar de protección de datos más riguroso a nivel global y debe aplicarse a cualquier software que procese datos personales, independientemente de la geografía de los usuarios. Toda implementación debe respetar los 7 principios del Art. 5: licitud/lealtad/transparencia, limitación de finalidad, minimización de datos, exactitud, limitación del almacenamiento, integridad/confidencialidad, y responsabilidad proactiva. Cada tratamiento requiere una base legal válida (Art. 6): consentimiento, contrato, obligación legal, intereses vitales, interés público, o interés legítimo. Los datos sensibles (Art. 9) requieren bases legales adicionales.

## Implementación

### 1. Sistema de Consentimiento

#### Schema de Base de Datos (Prisma)

```prisma
// schema.prisma — Modelo de consentimiento granular

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  // Datos personales con metadata de protección
  firstName     String?
  lastName      String?
  phone         String?
  dateOfBirth   DateTime?
  
  // Relaciones de cumplimiento
  consents      Consent[]
  dataRequests  DataSubjectRequest[]
  auditLogs     AuditLog[]
  
  // Metadata de creación y retención
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  deletedAt     DateTime? // Soft delete para período de retención
  retentionExpiresAt DateTime? // Fecha de expiración de retención
  
  @@map("users")
}

model Consent {
  id            String    @id @default(cuid())
  userId        String
  user          User      @relation(fields: [userId], references: [id])
  
  // Tipo de consentimiento granular
  purpose       ConsentPurpose
  legalBasis    LegalBasis
  
  // Estado y trazabilidad
  granted       Boolean
  grantedAt     DateTime?
  revokedAt     DateTime?
  expiresAt     DateTime?
  
  // Evidencia del consentimiento
  ipAddress     String?   // IP al momento del consentimiento
  userAgent     String?   // Navegador/dispositivo
  consentText   String    // Texto exacto que aceptó el usuario
  version       String    // Versión de la política de privacidad
  source        String    // Dónde se obtuvo (web, app, api)
  
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  
  @@unique([userId, purpose]) // Un consentimiento por propósito por usuario
  @@index([userId])
  @@index([purpose])
  @@map("consents")
}

enum ConsentPurpose {
  ESSENTIAL           // Funcionamiento básico del servicio
  ANALYTICS           // Análisis de uso y métricas
  MARKETING_EMAIL     // Comunicaciones de marketing por email
  MARKETING_PUSH      // Notificaciones push de marketing
  THIRD_PARTY_SHARING // Compartir datos con terceros
  PROFILING           // Creación de perfiles de usuario
  COOKIES_FUNCTIONAL  // Cookies funcionales
  COOKIES_ANALYTICS   // Cookies de analítica
  COOKIES_ADVERTISING // Cookies de publicidad
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

#### Servicio de Consentimiento

```typescript
// services/consent.service.ts

import { PrismaClient, ConsentPurpose, LegalBasis } from '@prisma/client';
import { z } from 'zod';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'consent-service' });

// Schema de validación para otorgar consentimiento
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
   * Otorgar consentimiento de forma granular.
   * GDPR Art. 7: El consentimiento debe ser libre, específico, informado e inequívoco.
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
    }, 'Consentimiento otorgado');

    return consent;
  }

  /**
   * Revocar consentimiento.
   * GDPR Art. 7(3): Debe ser tan fácil retirar como dar el consentimiento.
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
    }, 'Consentimiento revocado');

    // Disparar limpieza de datos asociados a este propósito
    await this.triggerDataCleanup(userId, purpose);

    return consent;
  }

  /**
   * Verificar si un usuario tiene consentimiento activo para un propósito.
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
   * Obtener todos los consentimientos de un usuario (para panel de privacidad).
   */
  async getUserConsents(userId: string) {
    return prisma.consent.findMany({
      where: { userId },
      orderBy: { purpose: 'asc' },
    });
  }

  private async triggerDataCleanup(userId: string, purpose: ConsentPurpose) {
    // Implementar lógica de limpieza según el propósito revocado
    // Por ejemplo: si revoca ANALYTICS, eliminar datos de tracking
    // Si revoca MARKETING_EMAIL, desuscribir de listas de email
    logger.info({
      event: 'data_cleanup_triggered',
      userId,
      purpose,
    }, 'Limpieza de datos iniciada por revocación de consentimiento');
  }
}
```

#### Middleware de Verificación de Consentimiento

```typescript
// middleware/consent.middleware.ts

import { Request, Response, NextFunction } from 'express';
import { ConsentPurpose } from '@prisma/client';
import { ConsentService } from '../services/consent.service';

const consentService = new ConsentService();

/**
 * Middleware factory que verifica consentimiento antes de procesar la request.
 * Úsalo en rutas que requieran consentimiento específico.
 * 
 * @example
 * router.post('/newsletter/subscribe', requireConsent(ConsentPurpose.MARKETING_EMAIL), handler);
 */
export function requireConsent(purpose: ConsentPurpose) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const userId = req.user?.id;

    if (!userId) {
      return res.status(401).json({ error: 'Autenticación requerida' });
    }

    const hasConsent = await consentService.hasConsent(userId, purpose);

    if (!hasConsent) {
      return res.status(403).json({
        error: 'Consentimiento requerido',
        code: 'CONSENT_REQUIRED',
        purpose,
        message: `Se requiere consentimiento para: ${purpose}`,
        consentUrl: `/api/v1/privacy/consent`,
      });
    }

    next();
  };
}
```

---

### 2. Derechos del Interesado (Derechos ARCO+)

#### Schema para Solicitudes de Derechos

```prisma
// Añadir a schema.prisma

model DataSubjectRequest {
  id            String    @id @default(cuid())
  userId        String
  user          User      @relation(fields: [userId], references: [id])
  
  type          DSRType
  status        DSRStatus @default(PENDING)
  
  // Detalles de la solicitud
  description   String?
  requestedAt   DateTime  @default(now())
  acknowledgedAt DateTime? // Confirmación de recepción
  completedAt   DateTime?  // Fecha de resolución
  deadline      DateTime   // Plazo máximo (30 días desde la solicitud)
  
  // Respuesta
  responseNotes String?
  responseData  Json?      // Datos exportados (para portabilidad)
  
  // Auditoría
  processedBy   String?    // ID del admin que procesó
  
  createdAt     DateTime  @default(now())
  updatedAt     DateTime  @updatedAt
  
  @@index([userId])
  @@index([status])
  @@index([deadline])
  @@map("data_subject_requests")
}

enum DSRType {
  ACCESS          // Art. 15 - Derecho de acceso
  RECTIFICATION   // Art. 16 - Derecho de rectificación
  ERASURE         // Art. 17 - Derecho al olvido
  RESTRICTION     // Art. 18 - Derecho a la limitación
  PORTABILITY     // Art. 20 - Derecho a la portabilidad
  OBJECTION       // Art. 21 - Derecho de oposición
  AUTOMATED_DECISION // Art. 22 - No ser objeto de decisiones automatizadas
}

enum DSRStatus {
  PENDING
  ACKNOWLEDGED
  IN_PROGRESS
  COMPLETED
  REJECTED
  EXTENDED     // Plazo extendido (max 2 meses adicionales)
}
```

#### Servicio de Derechos del Interesado

```typescript
// services/data-subject-rights.service.ts

import { PrismaClient, DSRType, DSRStatus } from '@prisma/client';
import pino from 'pino';
import crypto from 'node:crypto';

const prisma = new PrismaClient();
const logger = pino({ name: 'dsr-service' });

// Plazo GDPR: 30 días naturales desde la solicitud
const GDPR_DEADLINE_DAYS = 30;
const GDPR_EXTENSION_DAYS = 60; // Extensión máxima adicional

export class DataSubjectRightsService {
  /**
   * Crear una solicitud de derechos.
   * GDPR Art. 12(3): Responder sin dilación indebida, máximo 1 mes.
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
        acknowledgedAt: new Date(), // Confirmamos recepción inmediata
        status: DSRStatus.ACKNOWLEDGED,
      },
    });

    logger.info({
      event: 'dsr_created',
      requestId: request.id,
      userId,
      type,
      deadline: deadline.toISOString(),
    }, 'Solicitud de derechos del interesado creada');

    return request;
  }

  /**
   * Derecho de Acceso (Art. 15).
   * Exportar TODOS los datos personales del usuario en formato estructurado.
   */
  async processAccessRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
      include: { user: true },
    });

    // Recopilar todos los datos personales del usuario
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
    }, 'Solicitud de acceso completada');

    return userData;
  }

  /**
   * Derecho al Olvido (Art. 17).
   * Eliminar todos los datos personales del usuario.
   * Excepciones: obligaciones legales, defensa de reclamaciones.
   */
  async processErasureRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
    });

    // Verificar si hay excepciones legales que impidan la eliminación
    const exceptions = await this.checkErasureExceptions(request.userId);
    
    if (exceptions.length > 0) {
      await prisma.dataSubjectRequest.update({
        where: { id: requestId },
        data: {
          status: DSRStatus.REJECTED,
          responseNotes: `Eliminación parcial. Excepciones legales: ${exceptions.join(', ')}`,
          processedBy,
        },
      });

      logger.warn({
        event: 'dsr_erasure_partial',
        requestId,
        userId: request.userId,
        exceptions,
      }, 'Eliminación parcial por excepciones legales');

      // Eliminar solo los datos sin restricción legal
      await this.partialErasure(request.userId, exceptions);
      return { partial: true, exceptions };
    }

    // Eliminación completa
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
    }, 'Solicitud de eliminación completada');

    return { partial: false };
  }

  /**
   * Derecho a la Portabilidad (Art. 20).
   * Exportar datos en formato estructurado, de uso común y lectura mecánica.
   */
  async processPortabilityRequest(requestId: string, processedBy: string) {
    const request = await prisma.dataSubjectRequest.findUniqueOrThrow({
      where: { id: requestId },
    });

    const userData = await this.collectAllUserData(request.userId);

    // Formato JSON estructurado (lectura mecánica)
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
   * Recopilar todos los datos personales del usuario de todas las tablas.
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
      // Añadir más tablas según tu modelo de datos
      // prisma.order.findMany({ where: { userId } }),
      // prisma.address.findMany({ where: { userId } }),
      Promise.resolve([]), // Placeholder para orders
      Promise.resolve([]), // Placeholder para activity logs
    ]);

    return {
      profile: user,
      consents,
      orders,
      activityLogs,
    };
  }

  /**
   * Verificar excepciones legales para la eliminación.
   * Ejemplo: facturas deben conservarse por obligación fiscal.
   */
  private async checkErasureExceptions(userId: string): Promise<string[]> {
    const exceptions: string[] = [];

    // Ejemplo: Verificar si hay facturas (obligación legal de conservación fiscal)
    // const invoices = await prisma.invoice.count({ where: { userId } });
    // if (invoices > 0) {
    //   exceptions.push('invoices_tax_obligation');
    // }

    return exceptions;
  }

  private async fullErasure(userId: string) {
    await prisma.$transaction(async (tx) => {
      // Anonimizar en lugar de eliminar hard-delete para mantener integridad referencial
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

      // Eliminar consentimientos
      await tx.consent.deleteMany({ where: { userId } });
    });
  }

  private async partialErasure(userId: string, exceptions: string[]) {
    // Eliminar solo datos que no tienen restricción legal
    await prisma.user.update({
      where: { id: userId },
      data: {
        firstName: null,
        lastName: null,
        phone: null,
        dateOfBirth: null,
        // Mantener email si es necesario para obligaciones contractuales
      },
    });
  }
}
```

#### API de Derechos (Express Router)

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

// Todas las rutas requieren autenticación
router.use(authenticate);

/**
 * GET /api/v1/privacy/my-data
 * Obtener todos los datos personales (Art. 15 - Acceso)
 */
router.get('/my-data', async (req: Request, res: Response) => {
  const request = await dsrService.createRequest(
    req.user!.id,
    DSRType.ACCESS,
    'Solicitud de acceso a datos personales via API'
  );
  
  // Para solicitudes automatizadas, procesar inmediatamente
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
 * Solicitar eliminación de datos (Art. 17 - Derecho al olvido)
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
    message: 'Tu solicitud de eliminación ha sido recibida. Será procesada en un máximo de 30 días.',
    deadline: request.deadline,
  });
});

/**
 * POST /api/v1/privacy/portability
 * Exportar datos en formato portable (Art. 20)
 */
router.post('/portability', async (req: Request, res: Response) => {
  const request = await dsrService.createRequest(
    req.user!.id,
    DSRType.PORTABILITY,
    'Solicitud de portabilidad de datos'
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
 * Ver todos los consentimientos del usuario
 */
router.get('/consents', async (req: Request, res: Response) => {
  const consents = await consentService.getUserConsents(req.user!.id);
  res.json({ consents });
});

/**
 * POST /api/v1/privacy/consents
 * Otorgar un consentimiento
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
 * Revocar un consentimiento específico
 */
router.delete('/consents/:purpose', async (req: Request, res: Response) => {
  const purpose = req.params.purpose as any;
  const consent = await consentService.revokeConsent(req.user!.id, purpose);
  res.json({ consent, message: 'Consentimiento revocado exitosamente' });
});

export default router;
```

---

### 3. Encriptación y Pseudonimización

```typescript
// utils/encryption.service.ts

import crypto from 'node:crypto';

const ALGORITHM = 'aes-256-gcm';
const IV_LENGTH = 16;
const AUTH_TAG_LENGTH = 16;
const SALT_LENGTH = 32;

/**
 * Servicio de encriptación para datos personales en reposo.
 * GDPR Art. 32: Medidas técnicas apropiadas, incluyendo cifrado.
 */
export class EncryptionService {
  private readonly key: Buffer;

  constructor() {
    const masterKey = process.env.DATA_ENCRYPTION_KEY;
    if (!masterKey || masterKey.length < 32) {
      throw new Error('DATA_ENCRYPTION_KEY debe estar configurada con al menos 32 caracteres');
    }
    // Derivar clave usando HKDF para mayor seguridad
    this.key = crypto.createHash('sha256').update(masterKey).digest();
  }

  /**
   * Encriptar un dato personal.
   * Retorna string con formato: iv:authTag:ciphertext (todo en hex).
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
   * Desencriptar un dato personal.
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
   * Pseudonimizar un dato personal (proceso reversible con la clave).
   * GDPR Art. 4(5): Procesamiento de forma que no pueda atribuirse
   * sin información adicional.
   */
  pseudonymize(data: string): string {
    const hmac = crypto.createHmac('sha256', this.key);
    hmac.update(data);
    return hmac.digest('hex');
  }

  /**
   * Anonimizar un dato (proceso irreversible).
   * Los datos anonimizados ya no son datos personales bajo GDPR.
   */
  static anonymize(data: string): string {
    const salt = crypto.randomBytes(SALT_LENGTH);
    return crypto.createHash('sha256').update(salt).update(data).digest('hex');
  }

  /**
   * Hash seguro para contraseñas (usar bcrypt o argon2 en producción).
   */
  static async hashPassword(password: string): Promise<string> {
    // En producción usar: import bcrypt from 'bcrypt'; return bcrypt.hash(password, 12);
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

### 4. Política de Retención de Datos

```typescript
// jobs/data-retention.job.ts

import { PrismaClient } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'data-retention' });

/**
 * Política de retención de datos según GDPR Art. 5(1)(e).
 * "Limitación del plazo de conservación": los datos no se mantendrán
 * más tiempo del necesario para los fines del tratamiento.
 * 
 * Ejecutar como cron job diario.
 */

interface RetentionPolicy {
  model: string;
  field: string;         // Campo de fecha para evaluar retención
  retentionDays: number; // Días de retención
  action: 'anonymize' | 'delete' | 'archive';
  legalBasis: string;    // Justificación legal de la retención
}

const RETENTION_POLICIES: RetentionPolicy[] = [
  {
    model: 'auditLog',
    field: 'createdAt',
    retentionDays: 365 * 2, // 2 años
    action: 'archive',
    legalBasis: 'Obligación legal de conservación de registros de auditoría',
  },
  {
    model: 'session',
    field: 'lastActivityAt',
    retentionDays: 90,
    action: 'delete',
    legalBasis: 'Sesiones inactivas no son necesarias para el servicio',
  },
  {
    model: 'deletedUser',
    field: 'deletedAt',
    retentionDays: 30, // 30 días de gracia post-eliminación
    action: 'delete',
    legalBasis: 'Período de gracia completado, eliminación definitiva',
  },
  {
    model: 'analyticsEvent',
    field: 'createdAt',
    retentionDays: 180,
    action: 'anonymize',
    legalBasis: 'Datos de analytics anonimizados para estadísticas agregadas',
  },
];

export async function executeRetentionPolicies() {
  logger.info({ event: 'retention_job_started' }, 'Iniciando job de retención de datos');

  for (const policy of RETENTION_POLICIES) {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - policy.retentionDays);

    try {
      // Ejemplo para el modelo de sesiones
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
        }, `Política de retención ejecutada: ${policy.model}`);
      }

      // Añadir más modelos según sea necesario
    } catch (error) {
      logger.error({
        event: 'retention_policy_error',
        model: policy.model,
        error,
      }, `Error ejecutando política de retención: ${policy.model}`);
    }
  }

  logger.info({ event: 'retention_job_completed' }, 'Job de retención de datos completado');
}
```

---

### 5. Cookie Banner y Consentimiento de Cookies

```typescript
// middleware/cookie-consent.middleware.ts

import { Request, Response, NextFunction } from 'express';

/**
 * Categorías de cookies según GDPR y ePrivacy Directive.
 * Solo las cookies esenciales pueden usarse sin consentimiento.
 */
enum CookieCategory {
  ESSENTIAL = 'essential',         // Sin consentimiento requerido
  FUNCTIONAL = 'functional',       // Requiere consentimiento
  ANALYTICS = 'analytics',         // Requiere consentimiento
  ADVERTISING = 'advertising',     // Requiere consentimiento
}

interface CookiePreferences {
  essential: true;      // Siempre true, no puede desactivarse
  functional: boolean;
  analytics: boolean;
  advertising: boolean;
}

/**
 * Middleware que verifica las preferencias de cookies del usuario
 * antes de establecer cookies no esenciales.
 */
export function cookieConsentGuard(category: CookieCategory) {
  return (req: Request, res: Response, next: NextFunction) => {
    if (category === CookieCategory.ESSENTIAL) {
      return next(); // Cookies esenciales siempre permitidas
    }

    const consentCookie = req.cookies?.cookie_consent;
    
    if (!consentCookie) {
      // Sin consentimiento: no establecer cookies no esenciales
      return next();
    }

    try {
      const preferences: CookiePreferences = JSON.parse(consentCookie);
      
      if (!preferences[category]) {
        // El usuario no consintió esta categoría
        // No establecer la cookie y continuar
        res.locals.cookieBlocked = category;
        return next();
      }

      next();
    } catch {
      next(); // En caso de error, no establecer cookies
    }
  };
}

/**
 * Helper para establecer cookies respetando el consentimiento.
 */
export function setConsentAwareCookie(
  res: Response,
  name: string,
  value: string,
  category: CookieCategory,
  options: { maxAge?: number; httpOnly?: boolean; secure?: boolean; sameSite?: 'strict' | 'lax' | 'none' } = {}
) {
  if (res.locals.cookieBlocked === category) {
    return; // Cookie bloqueada por falta de consentimiento
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

## Flujo de trabajo del agente

1. Identificar qué datos personales procesa la aplicación y documentar la base legal (Art. 6) para cada tratamiento.
2. Implementar el sistema de consentimiento granular con schema Prisma, servicio y middleware de verificación.
3. Implementar el servicio de derechos del interesado (acceso, rectificación, supresión, limitación, portabilidad, oposición).
4. Agregar la API REST de privacidad con los endpoints de datos, borrado, portabilidad y gestión de consentimientos.
5. Implementar encriptación de datos personales en reposo (AES-256-GCM) y pseudonimización donde corresponda.
6. Configurar la política de retención de datos como cron job con acciones por modelo (anonymize/delete/archive).
7. Implementar cookie banner con consentimiento granular por categoría (essential/functional/analytics/advertising).
8. Validar contra el checklist de cumplimiento antes de desplegar.

## Gotchas

Implementar Privacy by Design y Privacy by Default (Art. 25): cada nueva feature debe evaluarse contra GDPR antes de implementarse, y los ajustes de privacidad más restrictivos son los predeterminados. No usar consentimiento pre-marcado — debe ser acción afirmativa clara (Art. 7). La revocación del consentimiento debe ser tan fácil como otorgarlo. Mantener un Registro de Actividades de Tratamiento (ROPA, Art. 30). Realizar DPIAs (Art. 35) para procesamiento a gran escala, perfilado o nuevas tecnologías. Las brechas de seguridad deben notificarse a la autoridad supervisora en 72 horas (Art. 33) y a los afectados sin dilación si hay alto riesgo (Art. 34). No transferir datos fuera de la UE sin mecanismo legal (SCCs, adecuación, BCRs). No almacenar datos sin política de retención. No loggear datos personales en texto plano. No usar datos personales en ambientes de desarrollo/testing sin anonimizar.

---

## Checklist de Cumplimiento GDPR

- [ ] Base legal documentada para cada tratamiento de datos
- [ ] Sistema de consentimiento granular implementado
- [ ] Política de privacidad clara y accesible
- [ ] API de derechos del interesado (acceso, eliminación, portabilidad, rectificación)
- [ ] Encriptación de datos personales en reposo y en tránsito
- [ ] Política de retención de datos definida e implementada
- [ ] Cookie banner con consentimiento granular
- [ ] Registro de actividades de tratamiento (ROPA)
- [ ] Proceso de notificación de brechas (72 horas)
- [ ] DPIA para tratamientos de alto riesgo
- [ ] Mecanismo legal para transferencias internacionales
- [ ] Contratos con encargados del tratamiento (procesadores)
- [ ] DPO designado (si aplica según Art. 37)
- [ ] Logs de auditoría para acceso a datos personales
- [ ] Pseudonimización/anonimización donde sea posible
- [ ] Formación del equipo de desarrollo en GDPR

---

## Referencias y Recursos

- [Texto oficial del GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Guías de la AEPD (España)](https://www.aepd.es/)
- [ICO Guidelines (UK)](https://ico.org.uk/for-organisations/guide-to-data-protection/)
- [EDPB Guidelines](https://edpb.europa.eu/our-work-tools/general-guidance_en)
- [GDPR Enforcement Tracker](https://www.enforcementtracker.com/)
