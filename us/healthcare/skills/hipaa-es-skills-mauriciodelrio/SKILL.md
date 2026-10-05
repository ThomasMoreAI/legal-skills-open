---
name: hipaa-es-skills-mauriciodelrio
title: HIPAA — Health Insurance Portability and Accountability Act
description: Usa este skill cuando el software procese, almacene o transmita información de salud protegida (PHI). Aunque HIPAA es legislación de EE.UU., este skill se aplica como estándar de protección de datos de salud para cualquier software independientemente de la ubicación geográfica de los usuarios. Cubre salvaguardas técnicas (control de acceso RBAC, encriptación AES-256, audit trail), administrativas y físicas, notificación de brechas, BAA con terceros, y checklist de cumplimiento.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/es-skills/governance-risk-and-compliance/hipaa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: es
---

# HIPAA — Health Insurance Portability and Accountability Act

HIPAA define el estándar de protección de información de salud que debe aplicarse a cualquier software que maneje datos médicos o de pacientes, independientemente de la geografía de los usuarios. Se estructura en 5 reglas: Privacy Rule (uso y divulgación de PHI), Security Rule (salvaguardas técnicas, administrativas y físicas para ePHI), Breach Notification Rule (notificación de brechas), Enforcement Rule (penalidades) y Omnibus Rule (extensión a Business Associates). PHI es cualquier información de salud combinada con alguno de los 18 identificadores HIPAA que pueda identificar a un individuo.

## Implementación

### 1. Los 18 Identificadores HIPAA

```typescript
// Los 18 identificadores HIPAA que hacen que los datos sean PHI
const HIPAA_IDENTIFIERS = [
  'name',                    // 1. Nombre
  'geographic_data',         // 2. Datos geográficos (menor a estado)
  'dates',                   // 3. Fechas (excepto año) relacionadas con el individuo
  'phone_number',            // 4. Números de teléfono
  'fax_number',              // 5. Números de fax
  'email',                   // 6. Dirección de email
  'ssn',                     // 7. Número de seguro social
  'medical_record_number',   // 8. Número de historia clínica
  'health_plan_id',          // 9. Número de plan de salud
  'account_number',          // 10. Números de cuenta
  'certificate_license',     // 11. Números de certificado/licencia
  'vehicle_identifiers',     // 12. Identificadores de vehículo
  'device_identifiers',      // 13. Identificadores de dispositivo
  'web_urls',                // 14. URLs
  'ip_address',              // 15. Direcciones IP
  'biometric_ids',           // 16. Identificadores biométricos
  'face_photos',             // 17. Fotos de rostro completo
  'unique_identifier',       // 18. Cualquier otro número/código identificador único
] as const;
```

### 2. Salvaguardas Técnicas (Technical Safeguards)

#### Control de Acceso (§164.312(a))

```prisma
// schema.prisma — Modelo para control de acceso HIPAA

model HealthcareUser {
  id              String    @id @default(cuid())
  email           String    @unique
  passwordHash    String
  
  // Control de acceso basado en roles
  role            HealthcareRole
  department      String?
  licenseNumber   String?   // Número de licencia médica
  
  // MFA obligatorio para acceso a PHI
  mfaEnabled      Boolean   @default(true)
  mfaSecret       String?   // Encriptado
  
  // Gestión de sesiones
  sessions        UserSession[]
  
  // Auto-logoff por inactividad (§164.312(a)(2)(iii))
  lastActivityAt  DateTime  @default(now())
  sessionTimeout  Int       @default(900) // 15 minutos en segundos
  
  // Auditoría
  accessLogs      PHIAccessLog[]
  
  // Estado de cuenta
  isActive        Boolean   @default(true)
  lockedAt        DateTime?
  failedAttempts  Int       @default(0)
  
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  @@map("healthcare_users")
}

enum HealthcareRole {
  PHYSICIAN           // Médico - acceso completo a PHI de sus pacientes
  NURSE               // Enfermera - acceso a PHI de pacientes asignados
  LAB_TECHNICIAN      // Técnico de laboratorio - acceso a resultados de lab
  BILLING_STAFF       // Personal de facturación - acceso a datos de facturación
  ADMIN               // Admin del sistema - sin acceso a PHI
  PATIENT             // Paciente - acceso solo a su propia PHI
  RESEARCHER          // Investigador - acceso a datos de-identificados
}

model PatientRecord {
  id              String    @id @default(cuid())
  patientId       String
  patient         Patient   @relation(fields: [patientId], references: [id])
  
  // Datos clínicos (encriptados en reposo)
  diagnosis       String    // Encriptado con AES-256
  treatment       String    // Encriptado
  medications     Json      // Encriptado
  labResults      Json?     // Encriptado
  notes           String?   // Encriptado
  
  // Metadatos de acceso
  sensitivityLevel PHISensitivity @default(STANDARD)
  
  // Break-the-glass: acceso de emergencia
  emergencyAccess  Boolean  @default(false)
  
  createdBy       String
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  // Auditoría completa
  accessLogs      PHIAccessLog[]
  
  @@index([patientId])
  @@map("patient_records")
}

model Patient {
  id              String    @id @default(cuid())
  
  // Datos demográficos (todos encriptados)
  mrn             String    @unique // Medical Record Number
  firstName       String    // Encriptado
  lastName        String    // Encriptado
  dateOfBirth     DateTime  // Encriptado
  ssn             String?   // Encriptado - solo cuando es necesario
  
  // Contacto
  phone           String?   // Encriptado
  email           String?   // Encriptado
  address         Json?     // Encriptado
  
  // Seguro médico
  insuranceProvider String?
  insurancePolicyId String? // Encriptado
  
  records         PatientRecord[]
  
  createdAt       DateTime  @default(now())
  updatedAt       DateTime  @updatedAt
  
  @@map("patients")
}

enum PHISensitivity {
  STANDARD          // PHI estándar
  HIGHLY_SENSITIVE  // Salud mental, abuso de sustancias, VIH/SIDA
  RESTRICTED        // Notas de psicoterapia (protección especial)
}

// Audit trail obligatorio — §164.312(b)
model PHIAccessLog {
  id              String    @id @default(cuid())
  
  userId          String
  user            HealthcareUser @relation(fields: [userId], references: [id])
  recordId        String?
  record          PatientRecord? @relation(fields: [recordId], references: [id])
  patientId       String?
  
  // Detalle del acceso
  action          PHIAction
  resource        String      // Tipo de recurso accedido
  fieldsAccessed  String[]    // Campos específicos accedidos
  
  // Contexto
  reason          String?     // Motivo del acceso
  isEmergency     Boolean     @default(false) // Break-the-glass
  
  // Metadatos técnicos
  ipAddress       String
  userAgent       String
  sessionId       String
  
  // Resultado
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
  VIEW            // Visualizar PHI
  CREATE          // Crear registro con PHI
  UPDATE          // Modificar PHI
  DELETE          // Eliminar PHI
  EXPORT          // Exportar PHI
  PRINT           // Imprimir PHI
  SHARE           // Compartir PHI con otro proveedor
  EMERGENCY_ACCESS // Acceso de emergencia (break-the-glass)
}
```

#### Servicio de Control de Acceso

```typescript
// services/hipaa-access-control.service.ts

import { PrismaClient, HealthcareRole, PHISensitivity, PHIAction } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'hipaa-access-control' });

/**
 * Matriz de permisos HIPAA: Define qué roles pueden realizar qué acciones.
 * Principio de Mínimo Necesario (Minimum Necessary Rule - §164.502(b)):
 * Solo acceso a la PHI mínima necesaria para la función laboral.
 */
const ACCESS_MATRIX: Record<HealthcareRole, {
  allowedActions: PHIAction[];
  allowedSensitivity: PHISensitivity[];
  requiresPatientAssignment: boolean;
}> = {
  PHYSICIAN: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE, PHIAction.UPDATE, PHIAction.EXPORT, PHIAction.SHARE],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE, PHISensitivity.RESTRICTED],
    requiresPatientAssignment: true, // Solo pacientes asignados
  },
  NURSE: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE, PHIAction.UPDATE],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE],
    requiresPatientAssignment: true,
  },
  LAB_TECHNICIAN: {
    allowedActions: [PHIAction.VIEW, PHIAction.CREATE],
    allowedSensitivity: [PHISensitivity.STANDARD],
    requiresPatientAssignment: false, // Acceso por tipo de resultado
  },
  BILLING_STAFF: {
    allowedActions: [PHIAction.VIEW],
    allowedSensitivity: [PHISensitivity.STANDARD],
    requiresPatientAssignment: false,
  },
  ADMIN: {
    allowedActions: [], // Sin acceso a PHI
    allowedSensitivity: [],
    requiresPatientAssignment: false,
  },
  PATIENT: {
    allowedActions: [PHIAction.VIEW, PHIAction.EXPORT],
    allowedSensitivity: [PHISensitivity.STANDARD, PHISensitivity.HIGHLY_SENSITIVE],
    requiresPatientAssignment: false, // Solo su propia PHI
  },
  RESEARCHER: {
    allowedActions: [PHIAction.VIEW],
    allowedSensitivity: [PHISensitivity.STANDARD], // Solo datos de-identificados
    requiresPatientAssignment: false,
  },
};

export class HIPAAAccessControlService {
  /**
   * Verificar si un usuario tiene permiso para acceder a un registro de PHI.
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

    // Verificar si la cuenta está activa
    if (!user.isActive || user.lockedAt) {
      await this.logAccess({ ...params, success: false, errorMessage: 'Cuenta inactiva o bloqueada' });
      return { allowed: false, reason: 'Cuenta inactiva o bloqueada' };
    }

    // Verificar sesión timeout (auto-logoff §164.312(a)(2)(iii))
    const inactiveSeconds = (Date.now() - user.lastActivityAt.getTime()) / 1000;
    if (inactiveSeconds > user.sessionTimeout) {
      await this.logAccess({ ...params, success: false, errorMessage: 'Sesión expirada por inactividad' });
      return { allowed: false, reason: 'Sesión expirada por inactividad' };
    }

    const permissions = ACCESS_MATRIX[user.role];

    // Break-the-glass: acceso de emergencia
    if (params.isEmergency) {
      logger.warn({
        event: 'emergency_access',
        userId: params.userId,
        patientId: params.patientId,
        role: user.role,
      }, '⚠️ ACCESO DE EMERGENCIA (Break-the-glass)');
      
      await this.logAccess({ ...params, success: true, isEmergency: true });
      return { allowed: true, reason: 'Emergency access (break-the-glass)' };
    }

    // Verificar acción permitida
    if (!permissions.allowedActions.includes(params.action)) {
      await this.logAccess({
        ...params,
        success: false,
        errorMessage: `Acción ${params.action} no permitida para rol ${user.role}`,
      });
      return {
        allowed: false,
        reason: `Tu rol (${user.role}) no tiene permiso para ${params.action}`,
      };
    }

    // Verificar sensibilidad del registro
    if (params.recordId) {
      const record = await prisma.patientRecord.findUnique({
        where: { id: params.recordId },
      });

      if (record && !permissions.allowedSensitivity.includes(record.sensitivityLevel)) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: `Nivel de sensibilidad ${record.sensitivityLevel} no permitido`,
        });
        return {
          allowed: false,
          reason: `No tienes acceso a registros con nivel de sensibilidad ${record.sensitivityLevel}`,
        };
      }
    }

    // Verificar asignación de paciente (si aplica)
    if (permissions.requiresPatientAssignment) {
      const isAssigned = await this.isPatientAssigned(params.userId, params.patientId);
      if (!isAssigned) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: 'Paciente no asignado al profesional',
        });
        return { allowed: false, reason: 'Este paciente no está asignado a tu cuidado' };
      }
    }

    // Pacientes solo pueden acceder a su propia PHI
    if (user.role === 'PATIENT') {
      const isOwnData = await this.isOwnPatientData(params.userId, params.patientId);
      if (!isOwnData) {
        await this.logAccess({
          ...params,
          success: false,
          errorMessage: 'Intento de acceso a PHI de otro paciente',
        });
        return { allowed: false, reason: 'Solo puedes acceder a tu propia información de salud' };
      }
    }

    // Acceso permitido
    await this.logAccess({ ...params, success: true });

    // Actualizar última actividad
    await prisma.healthcareUser.update({
      where: { id: params.userId },
      data: { lastActivityAt: new Date() },
    });

    return { allowed: true, reason: 'Acceso autorizado' };
  }

  /**
   * Registrar todo acceso (exitoso o fallido) a PHI.
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
    // Implementar verificación de asignación paciente-proveedor
    // Esto depende de tu modelo de datos específico
    return true; // Placeholder
  }

  private async isOwnPatientData(userId: string, patientId: string): Promise<boolean> {
    // Verificar que el userId corresponde al patientId
    return true; // Placeholder
  }
}
```

---

### 2. Encriptación de PHI (§164.312(a)(2)(iv) y §164.312(e)(1))

```typescript
// services/phi-encryption.service.ts

import crypto from 'node:crypto';
import pino from 'pino';

const logger = pino({ name: 'phi-encryption' });

const ALGORITHM = 'aes-256-gcm';
const IV_LENGTH = 12; // Recomendado para GCM
const AUTH_TAG_LENGTH = 16;

/**
 * Servicio de encriptación específico para PHI.
 * HIPAA requiere encriptación en reposo y en tránsito para ePHI.
 * 
 * §164.312(a)(2)(iv): Encriptación en reposo
 * §164.312(e)(1): Encriptación en tránsito
 * 
 * Usa AES-256-GCM con autenticación (protege integridad + confidencialidad).
 */
export class PHIEncryptionService {
  private readonly masterKey: Buffer;
  private readonly keyVersion: string;

  constructor() {
    const keyEnv = process.env.PHI_ENCRYPTION_KEY;
    if (!keyEnv) {
      throw new Error('PHI_ENCRYPTION_KEY es obligatoria para cumplimiento HIPAA');
    }

    this.masterKey = Buffer.from(keyEnv, 'hex');
    this.keyVersion = process.env.PHI_KEY_VERSION ?? 'v1';

    if (this.masterKey.length !== 32) {
      throw new Error('PHI_ENCRYPTION_KEY debe ser exactamente 256 bits (64 caracteres hex)');
    }
  }

  /**
   * Encriptar un campo de PHI individual.
   * Retorna: keyVersion:iv:authTag:ciphertext (todo en base64)
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

    // Formato: version:iv:tag:ciphertext
    return [
      this.keyVersion,
      iv.toString('base64'),
      authTag.toString('base64'),
      encrypted.toString('base64'),
    ].join(':');
  }

  /**
   * Desencriptar un campo de PHI.
   */
  decryptField(encryptedData: string): string {
    const [version, ivB64, tagB64, ciphertextB64] = encryptedData.split(':');

    // Verificar versión de clave (para rotación de claves)
    if (version !== this.keyVersion) {
      logger.warn({
        event: 'key_version_mismatch',
        expected: this.keyVersion,
        found: version,
      }, 'Versión de clave no coincide — considerar re-encriptación');
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
   * Encriptar un objeto completo de PHI (múltiples campos).
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
   * Desencriptar un objeto completo de PHI.
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
          logger.error({ field: String(field) }, 'Error desencriptando campo PHI');
        }
      }
    }

    return decrypted;
  }

  /**
   * De-identificar datos según el método Safe Harbor de HIPAA.
   * Elimina los 18 identificadores definidos por HIPAA.
   * Los datos de-identificados ya no son PHI.
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

    // Generalizar fechas: solo mantener el año
    if (deIdentified.dateOfBirth instanceof Date) {
      deIdentified.birthYear = (deIdentified.dateOfBirth as Date).getFullYear();
      delete deIdentified.dateOfBirth;
    }

    // Generalizar ubicación: solo mantener los primeros 3 dígitos del ZIP si población > 20,000
    if (typeof deIdentified.zipCode === 'string') {
      deIdentified.zipPrefix = (deIdentified.zipCode as string).substring(0, 3);
      delete deIdentified.zipCode;
    }

    return deIdentified;
  }
}
```

---

### 3. Middleware de Auditoría HIPAA

```typescript
// middleware/hipaa-audit.middleware.ts

import { Request, Response, NextFunction } from 'express';
import pino from 'pino';

const logger = pino({
  name: 'hipaa-audit',
  // HIPAA requiere que los logs sean a prueba de manipulaciones
  // En producción, enviar a un SIEM o almacenamiento inmutable
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
 * Middleware de auditoría HIPAA.
 * Registra todas las interacciones con el sistema que involucren PHI.
 * 
 * §164.312(b): "Implement hardware, software, and/or procedural mechanisms
 * that record and examine activity in information systems that contain or use ePHI."
 */
export function hipaaAuditMiddleware(req: Request, res: Response, next: NextFunction) {
  const startTime = Date.now();

  // Capturar el body original de la respuesta
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
        // No loggear el body de la respuesta si contiene PHI
        containsPHI: isPHIRoute(req.path),
      },
    }, `${req.method} ${req.originalUrl} ${res.statusCode} ${duration}ms`);

    return originalSend(body);
  };

  next();
}

/**
 * Determinar si una ruta puede contener PHI.
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
 * Middleware para auto-logoff por inactividad.
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
      }, 'Sesión terminada por inactividad');

      req.session.destroy((err) => {
        if (err) logger.error({ err }, 'Error destruyendo sesión');
      });

      return res.status(440).json({
        error: 'Sesión expirada',
        code: 'SESSION_TIMEOUT',
        message: 'Tu sesión ha expirado por inactividad. Por favor, inicia sesión nuevamente.',
      });
    }

    req.session.lastActivity = Date.now();
    next();
  };
}
```

---

### 4. Notificación de Brechas (Breach Notification Rule)

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
 * Servicio de notificación de brechas HIPAA.
 * 
 * Plazos obligatorios:
 * - Individuos afectados: sin demora injustificada, máximo 60 días
 * - HHS (si > 500 afectados): sin demora injustificada, máximo 60 días
 * - HHS (si < 500 afectados): hasta 60 días después del fin del año calendario
 * - Medios de comunicación (si > 500 en un estado): sin demora injustificada
 */
export class HIPAABreachNotificationService {
  async reportBreach(breach: BreachDetails) {
    logger.fatal({
      event: 'phi_breach_detected',
      ...breach,
    }, '🚨 BRECHA DE PHI DETECTADA');

    // 1. Evaluación de riesgo (4 factores)
    const riskAssessment = this.assessRisk(breach);

    if (riskAssessment.requiresNotification) {
      // 2. Notificar al equipo de seguridad interno inmediatamente
      await this.notifySecurityTeam(breach, riskAssessment);

      // 3. Iniciar proceso de notificación
      if (breach.numberOfAffected > 500) {
        await this.notifyHHS(breach); // Health and Human Services
        await this.notifyMedia(breach); // Medios si > 500 en un estado
      }

      // 4. Preparar notificaciones individuales
      await this.prepareIndividualNotifications(breach);
    }

    // 5. Documentar todo
    await this.documentBreach(breach, riskAssessment);

    return riskAssessment;
  }

  /**
   * Evaluación de riesgo de 4 factores del HHS.
   */
  private assessRisk(breach: BreachDetails) {
    // Factor 1: Naturaleza y extensión de la PHI
    // Factor 2: La persona no autorizada que usó la PHI
    // Factor 3: Si la PHI fue realmente adquirida o vista
    // Factor 4: Extensión de la mitigación del riesgo

    return {
      requiresNotification: true, // Presunción de brecha a menos que se demuestre bajo riesgo
      riskLevel: 'high' as const,
      notificationDeadline: new Date(Date.now() + 60 * 24 * 60 * 60 * 1000), // 60 días
      factors: {
        natureOfPHI: 'clinical_data',
        unauthorizedAccess: breach.unauthorizedEntity ?? 'unknown',
        phiAcquired: true, // Presunción conservadora
        mitigationEffectiveness: breach.mitigationActions.length > 0 ? 'partial' : 'none',
      },
    };
  }

  private async notifySecurityTeam(breach: BreachDetails, risk: any) {
    // Integrar con tu sistema de alertas (PagerDuty, Slack, email)
    logger.fatal({
      event: 'security_team_notified',
      breach: breach.natureOfBreach,
      affected: breach.numberOfAffected,
      riskLevel: risk.riskLevel,
    }, 'Equipo de seguridad notificado');
  }

  private async notifyHHS(breach: BreachDetails) {
    // En producción: enviar formulario al HHS breach portal
    logger.info({
      event: 'hhs_notification_prepared',
      affected: breach.numberOfAffected,
    }, 'Notificación al HHS preparada');
  }

  private async notifyMedia(breach: BreachDetails) {
    logger.info({ event: 'media_notification_required' }, 'Notificación a medios requerida (>500 afectados)');
  }

  private async prepareIndividualNotifications(breach: BreachDetails) {
    // Preparar cartas/emails de notificación a pacientes afectados
    logger.info({
      event: 'individual_notifications_prepared',
      count: breach.numberOfAffected,
    }, 'Notificaciones individuales preparadas');
  }

  private async documentBreach(breach: BreachDetails, risk: any) {
    // HIPAA requiere mantener documentación de brechas por 6 años
    logger.info({
      event: 'breach_documented',
      retainUntil: new Date(Date.now() + 6 * 365 * 24 * 60 * 60 * 1000).toISOString(),
    }, 'Brecha documentada para retención de 6 años');
  }
}
```

---

### 5. BAA (Business Associate Agreement) — Verificación Técnica

```typescript
// services/baa-compliance.service.ts

/**
 * Servicio para verificar que todos los servicios de terceros
 * tienen BAA firmado antes de procesar PHI.
 * 
 * HIPAA requiere un BAA con cualquier Business Associate
 * que acceda, mantenga, utilice o transmita PHI.
 */

interface BusinessAssociate {
  name: string;
  service: string;
  baaSignedDate: Date;
  baaExpiryDate: Date;
  contactEmail: string;
  dataProcessed: string[];
}

// Registro de Business Associates con BAA activo
const BUSINESS_ASSOCIATES: BusinessAssociate[] = [
  {
    name: 'AWS',
    service: 'Cloud Infrastructure (HIPAA eligible)',
    baaSignedDate: new Date('2024-01-15'),
    baaExpiryDate: new Date('2026-01-15'),
    contactEmail: 'compliance@example.com',
    dataProcessed: ['ePHI storage', 'ePHI processing', 'backups'],
  },
  // Añadir todos los terceros que manejan PHI
];

export function verifyBAA(serviceName: string): boolean {
  const ba = BUSINESS_ASSOCIATES.find(
    b => b.service.toLowerCase().includes(serviceName.toLowerCase())
  );

  if (!ba) {
    throw new Error(
      `⚠️ VIOLACIÓN HIPAA: No existe BAA para el servicio "${serviceName}". ` +
      'No se puede enviar PHI a este servicio sin un BAA firmado.'
    );
  }

  if (ba.baaExpiryDate < new Date()) {
    throw new Error(
      `⚠️ BAA EXPIRADO para ${ba.name}. Renovar antes de continuar procesando PHI.`
    );
  }

  return true;
}
```

---

## Flujo de trabajo del agente

1. Identificar qué datos de salud procesa la aplicación y clasificar como PHI estándar, altamente sensible o restringido.
2. Implementar el modelo de datos con control de acceso RBAC, encriptación de campos PHI y audit trail completo.
3. Implementar el servicio de control de acceso con matriz de permisos por rol, principio de mínimo necesario y mecanismo break-the-glass.
4. Agregar encriptación AES-256-GCM para ePHI en reposo con versionado de claves y método de de-identificación Safe Harbor.
5. Implementar middleware de auditoría HIPAA para todas las rutas que manejen PHI y auto-logoff por inactividad.
6. Configurar el servicio de notificación de brechas con evaluación de riesgo de 4 factores y plazos de notificación.
7. Verificar que todos los servicios de terceros tengan BAA firmado y vigente antes de procesar PHI.
8. Validar contra el checklist de cumplimiento (técnico, administrativo, físico, BAs) antes de desplegar.

## Gotchas

Encriptar toda ePHI en reposo (AES-256) y en tránsito (TLS 1.2+) es obligatorio, no opcional. MFA es requerido para todo acceso a sistemas con PHI. El auto-logoff debe activarse después de 15 minutos de inactividad máximo (§164.312(a)(2)(iii)). El audit trail debe registrar quién accedió a qué PHI, cuándo, desde dónde, y si fue exitoso o fallido. El mecanismo break-the-glass para acceso de emergencia debe existir pero con logging exhaustivo. No enviar PHI por email sin encriptación. No usar servicios en la nube sin BAA firmado. No loggear PHI en texto plano en archivos de log. No copiar PHI a ambientes de desarrollo sin de-identificar mediante el método Safe Harbor (eliminar los 18 identificadores). No compartir credenciales de acceso — cada usuario debe tener ID único. No descartar hardware con PHI sin sanitización certificada. Las brechas deben notificarse a individuos afectados en máximo 60 días, y al HHS inmediatamente si afectan a más de 500 individuos. La documentación de brechas debe conservarse por 6 años.

---

## Checklist de Cumplimiento HIPAA

### Salvaguardas Técnicas
- [ ] Encriptación AES-256 para ePHI en reposo
- [ ] TLS 1.2+ para ePHI en tránsito
- [ ] Control de acceso basado en roles (RBAC)
- [ ] IDs de usuario únicos — sin cuentas compartidas
- [ ] Auto-logoff por inactividad (≤15 min)
- [ ] Mecanismo de acceso de emergencia (break-the-glass)
- [ ] Audit logs para todo acceso a ePHI
- [ ] Integridad de datos — mecanismos de detección de alteraciones

### Salvaguardas Administrativas
- [ ] Security Officer designado
- [ ] Privacy Officer designado
- [ ] Análisis de riesgos documentado
- [ ] Plan de gestión de riesgos
- [ ] Políticas y procedimientos de seguridad escritos
- [ ] Formación de la fuerza laboral
- [ ] Plan de contingencia (backup, recuperación, emergencia)
- [ ] Proceso de notificación de brechas

### Salvaguardas Físicas
- [ ] Control de acceso a instalaciones
- [ ] Estaciones de trabajo en ubicaciones seguras
- [ ] Políticas de uso de dispositivos móviles
- [ ] Sanitización de medios antes de descarte

### Business Associates
- [ ] BAA firmado con todos los proveedores que manejan PHI
- [ ] Inventario actualizado de Business Associates
- [ ] Revisión periódica de compliance de BAs

---

## Referencias y Recursos

- [Texto oficial de HIPAA](https://www.hhs.gov/hipaa/index.html)
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html)
- [HHS Breach Portal](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf)
- [NIST SP 800-66 (HIPAA Security Rule Implementation)](https://csrc.nist.gov/publications/detail/sp/800-66/rev-2/final)
- [OCR Enforcement Actions](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html)
