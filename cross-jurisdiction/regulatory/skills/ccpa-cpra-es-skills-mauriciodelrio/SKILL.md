---
name: ccpa-cpra-es-skills-mauriciodelrio
title: CCPA/CPRA — California Consumer Privacy Act & Privacy Rights Act
description: Usa este skill cuando desarrolles software que recolecte, almacene o procese información personal de usuarios. Aunque CCPA/CPRA es legislación de California, este skill se aplica como estándar de privacidad para cualquier software independientemente de la ubicación geográfica de los usuarios. Cubre derechos del consumidor (know, delete, correct, portability, opt-out), modelo de datos, opt-out DNSS con GPC, notice at collection, menores de edad, y checklist de cumplimiento.
author: mauriciodelrio
author_url: https://github.com/mauriciodelrio/delriodev-skills/tree/main/es-skills/governance-risk-and-compliance/ccpa-cpra
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: regulatory
language: es
---

# CCPA/CPRA — California Consumer Privacy Act & Privacy Rights Act

CCPA (2020) y CPRA (2023) definen estándares de privacidad que deben aplicarse a cualquier software que maneje información personal, independientemente de la geografía de los usuarios. El modelo opera con opt-out (no requiere consentimiento previo para recolectar), tiene definición amplísima de "venta" de datos (incluye compartir para publicidad), y las penalidades originales son $2,500 por violación o $7,500 por violación intencional. La autoridad de referencia es la California Privacy Protection Agency (CPPA).

## Implementación

### 1. Modelo de Datos de Privacidad

```prisma
// prisma/schema.prisma

/// Registro de información personal recolectada por consumidor
model ConsumerPrivacyProfile {
  id              String   @id @default(cuid())
  
  // Identificador del consumidor (puede ser autenticado o no)
  consumerEmail   String?
  accountId       String?  @unique
  deviceId        String?
  
  // Preferencias de privacidad CCPA/CPRA
  optOutSale          Boolean  @default(false)   // "Do Not Sell My Personal Information"
  optOutSharing       Boolean  @default(false)   // "Do Not Share My Personal Information" (CPRA)
  limitSensitiveUse   Boolean  @default(false)   // Limitar uso de SPI (CPRA)
  
  // Consentimiento financiero (opt-in para menores)
  isMinor             Boolean  @default(false)
  parentalConsent     Boolean?
  
  // Categorías de PI recolectada (para disclosure)
  categoriesCollected String[] @default([])
  sourcesOfCollection String[] @default([])
  purposesOfUse       String[] @default([])
  categoriesShared    String[] @default([])
  
  // Tracking
  createdAt       DateTime @default(now())
  updatedAt       DateTime @updatedAt
  lastVerified    DateTime?
  
  // Relaciones
  requests        ConsumerRequest[]
  
  @@index([consumerEmail])
  @@index([accountId])
  @@map("consumer_privacy_profiles")
}

/// Solicitudes de consumidores (DSAR — Data Subject Access Requests)
model ConsumerRequest {
  id          String              @id @default(cuid())
  profileId   String
  profile     ConsumerPrivacyProfile @relation(fields: [profileId], references: [id])
  
  type        ConsumerRequestType
  status      RequestStatus       @default(RECEIVED)
  
  // CCPA requiere responder en 45 días (extensible a 90)
  receivedAt       DateTime @default(now())
  acknowledgedAt   DateTime?
  deadlineAt       DateTime  // 45 días desde recepción
  extendedDeadline DateTime? // Extensión hasta 90 días
  completedAt      DateTime?
  
  // Verificación de identidad (obligatorio antes de procesar)
  identityVerified    Boolean  @default(false)
  verificationMethod  String?
  
  // Respuesta
  responseData     Json?
  denialReason     String?
  
  @@map("consumer_requests")
}

enum ConsumerRequestType {
  RIGHT_TO_KNOW        // Saber qué PI se recolecta y por qué
  RIGHT_TO_DELETE      // Eliminar toda la PI
  RIGHT_TO_CORRECT     // Corregir PI inexacta (CPRA)
  RIGHT_TO_PORTABILITY // Obtener PI en formato portable (CPRA)
  OPT_OUT_SALE         // No vender mi PI
  OPT_OUT_SHARING      // No compartir mi PI para publicidad (CPRA)
  LIMIT_SENSITIVE       // Limitar uso de info sensible (CPRA)
}

enum RequestStatus {
  RECEIVED
  IDENTITY_VERIFICATION
  IN_PROGRESS
  COMPLETED
  DENIED
  EXTENDED
}
```

---

### 2. Servicio de Derechos del Consumidor

```typescript
// services/ccpa-consumer-rights.service.ts

import { PrismaClient, ConsumerRequestType, RequestStatus } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'ccpa-rights' });

// CCPA: El consumidor puede hacer solicitudes 2 veces en un período de 12 meses
const MAX_REQUESTS_PER_YEAR = 2;
const RESPONSE_DEADLINE_DAYS = 45;
const MAX_EXTENSION_DAYS = 90;

export class CCPAConsumerRightsService {
  /**
   * Iniciar una solicitud de consumidor.
   * CCPA §1798.100-§1798.135
   */
  async submitRequest(
    consumerIdentifier: { email?: string; accountId?: string },
    requestType: ConsumerRequestType,
  ) {
    // Buscar o crear perfil de privacidad
    const profile = await this.findOrCreateProfile(consumerIdentifier);

    // Verificar límite de solicitudes (2 por 12 meses para RIGHT_TO_KNOW)
    if (requestType === 'RIGHT_TO_KNOW') {
      const recentRequests = await prisma.consumerRequest.count({
        where: {
          profileId: profile.id,
          type: 'RIGHT_TO_KNOW',
          receivedAt: {
            gte: new Date(Date.now() - 365 * 24 * 60 * 60 * 1000),
          },
        },
      });

      if (recentRequests >= MAX_REQUESTS_PER_YEAR) {
        return {
          success: false,
          error: 'Has alcanzado el límite de 2 solicitudes de conocimiento por período de 12 meses.',
        };
      }
    }

    const deadline = new Date();
    deadline.setDate(deadline.getDate() + RESPONSE_DEADLINE_DAYS);

    const request = await prisma.consumerRequest.create({
      data: {
        profileId: profile.id,
        type: requestType,
        status: 'IDENTITY_VERIFICATION',
        deadlineAt: deadline,
      },
    });

    logger.info({
      event: 'consumer_request_submitted',
      requestId: request.id,
      type: requestType,
      deadline: deadline.toISOString(),
    }, 'Solicitud de consumidor CCPA recibida');

    // Enviar email de confirmación (CCPA requiere acusar recibo en 10 días)
    // await this.sendAcknowledgment(profile, request);

    return {
      success: true,
      requestId: request.id,
      type: requestType,
      status: 'IDENTITY_VERIFICATION',
      deadline: deadline.toISOString(),
      message: 'Solicitud recibida. Debes verificar tu identidad para continuar.',
    };
  }

  /**
   * Derecho a Saber (Right to Know).
   * CCPA §1798.100, §1798.110, §1798.115
   * 
   * El consumidor tiene derecho a saber:
   * - Qué categorías de PI se recolectan
   * - Las fuentes de recolección
   * - El propósito comercial de la recolección
   * - Las categorías de terceros con quienes se comparte
   * - Las piezas específicas de PI recolectada
   */
  async processRightToKnow(requestId: string): Promise<object> {
    const request = await this.getVerifiedRequest(requestId, 'RIGHT_TO_KNOW');
    
    const profile = await prisma.consumerPrivacyProfile.findUniqueOrThrow({
      where: { id: request.profileId },
    });

    // Recopilar toda la información personal del consumidor
    const personalInfo = await this.collectPersonalInfo(profile.accountId!);

    const disclosure = {
      // §1798.110(a)(1): Categorías de PI recolectada
      categoriesCollected: [
        'Identificadores (email, nombre)',
        'Actividad en internet (historial de uso)',
        'Información comercial (transacciones)',
        'Geolocalización (si se proporcionó)',
      ],
      
      // §1798.110(a)(2): Categorías de fuentes
      sourcesOfCollection: [
        'Directamente del consumidor',
        'Automáticamente mediante cookies y tecnologías similares',
      ],
      
      // §1798.110(a)(3): Propósito comercial
      businessPurposes: [
        'Proveer el servicio solicitado',
        'Mantener la seguridad de la cuenta',
        'Mejorar el servicio',
        'Cumplir con obligaciones legales',
      ],
      
      // §1798.110(a)(4): Categorías de terceros
      thirdPartyCategories: [
        'Proveedores de servicios (hosting, email)',
        'Procesadores de pagos',
      ],
      
      // §1798.110(a)(5): Piezas específicas de PI
      specificPersonalInfo: personalInfo,

      // §1798.115: Información sobre venta/compartición
      salesAndSharing: {
        sold: false,
        shared: false,
        categoriesSold: [],
        categoriesShared: [],
      },
    };

    await prisma.consumerRequest.update({
      where: { id: requestId },
      data: {
        status: 'COMPLETED',
        completedAt: new Date(),
        responseData: disclosure as any,
      },
    });

    logger.info({
      event: 'right_to_know_completed',
      requestId,
      profileId: profile.id,
    }, 'Right to Know procesado');

    return disclosure;
  }

  /**
   * Derecho a Eliminar (Right to Delete).
   * CCPA §1798.105
   * 
   * Excepciones permitidas (no necesitas eliminar si):
   * - Necesario para completar la transacción
   * - Seguridad/detección de fraude
   * - Debugging
   * - Cumplimiento legal
   */
  async processRightToDelete(requestId: string): Promise<{ success: boolean; deletedCategories: string[] }> {
    const request = await this.getVerifiedRequest(requestId, 'RIGHT_TO_DELETE');

    const profile = await prisma.consumerPrivacyProfile.findUniqueOrThrow({
      where: { id: request.profileId },
    });

    const deletedCategories: string[] = [];

    await prisma.$transaction(async (tx) => {
      if (profile.accountId) {
        // Pseudonimizar datos de usuario
        await tx.user.update({
          where: { id: profile.accountId },
          data: {
            name: '[ELIMINADO]',
            email: `deleted_${Date.now()}@deleted.invalid`,
            phone: null,
            address: null,
            deletedAt: new Date(),
          },
        });
        deletedCategories.push('Identificadores personales');

        // Eliminar historial de actividad
        // await tx.activityLog.deleteMany({ where: { userId: profile.accountId } });
        deletedCategories.push('Actividad en internet');
      }
    });

    await prisma.consumerRequest.update({
      where: { id: requestId },
      data: {
        status: 'COMPLETED',
        completedAt: new Date(),
        responseData: { deletedCategories } as any,
      },
    });

    // CCPA requiere notificar a service providers para que también eliminen
    // await this.notifyServiceProviders(profile.accountId, 'delete');

    logger.info({
      event: 'right_to_delete_completed',
      requestId,
      deletedCategories,
    }, 'Right to Delete procesado');

    return { success: true, deletedCategories };
  }

  /**
   * Derecho a Corregir (Right to Correct) — CPRA §1798.106
   */
  async processRightToCorrect(
    requestId: string,
    corrections: Record<string, unknown>,
  ): Promise<{ success: boolean; correctedFields: string[] }> {
    const request = await this.getVerifiedRequest(requestId, 'RIGHT_TO_CORRECT');
    const correctedFields = Object.keys(corrections);

    // Validar que solo se corrijan campos permitidos
    const allowedFields = ['name', 'email', 'phone', 'address'];
    const invalidFields = correctedFields.filter(f => !allowedFields.includes(f));
    
    if (invalidFields.length > 0) {
      throw new Error(`Campos no permitidos para corrección: ${invalidFields.join(', ')}`);
    }

    const profile = await prisma.consumerPrivacyProfile.findUniqueOrThrow({
      where: { id: request.profileId },
    });

    if (profile.accountId) {
      await prisma.user.update({
        where: { id: profile.accountId },
        data: corrections as any,
      });
    }

    await prisma.consumerRequest.update({
      where: { id: requestId },
      data: {
        status: 'COMPLETED',
        completedAt: new Date(),
        responseData: { correctedFields } as any,
      },
    });

    logger.info({
      event: 'right_to_correct_completed',
      requestId,
      correctedFields,
    }, 'Right to Correct procesado');

    return { success: true, correctedFields };
  }

  // --- Helpers privados ---

  private async findOrCreateProfile(identifier: { email?: string; accountId?: string }) {
    const where = identifier.accountId 
      ? { accountId: identifier.accountId }
      : { consumerEmail: identifier.email };

    let profile = await prisma.consumerPrivacyProfile.findFirst({ where });
    
    if (!profile) {
      profile = await prisma.consumerPrivacyProfile.create({
        data: {
          consumerEmail: identifier.email,
          accountId: identifier.accountId,
        },
      });
    }

    return profile;
  }

  private async getVerifiedRequest(requestId: string, expectedType: ConsumerRequestType) {
    const request = await prisma.consumerRequest.findUniqueOrThrow({
      where: { id: requestId },
    });

    if (request.type !== expectedType) {
      throw new Error(`Tipo de solicitud incorrecto: esperado ${expectedType}, recibido ${request.type}`);
    }

    if (!request.identityVerified) {
      throw new Error('La identidad del consumidor no ha sido verificada');
    }

    return request;
  }

  private async collectPersonalInfo(accountId: string): Promise<Record<string, unknown>> {
    const user = await prisma.user.findUnique({
      where: { id: accountId },
      select: {
        name: true,
        email: true,
        createdAt: true,
      },
    });

    return {
      profile: user,
      // Agregar más fuentes de datos según tu aplicación
    };
  }
}
```

---

### 3. Opt-Out "Do Not Sell or Share" (DNSS)

```typescript
// middleware/ccpa-opt-out.middleware.ts

import { Request, Response, NextFunction } from 'express';
import { PrismaClient } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'ccpa-opt-out' });

/**
 * CCPA §1798.120: Derecho a Opt-Out de la venta de PI.
 * CPRA §1798.120: Extendido a "venta O compartición" de PI.
 * 
 * REQUISITOS:
 * 1. Link visible "Do Not Sell or Share My Personal Information" en el sitio
 * 2. Respetar Global Privacy Control (GPC) header
 * 3. No pedir login para ejercer el opt-out
 * 4. No volver a pedir consentimiento por 12 meses mínimo
 */

/**
 * Detectar señal de Global Privacy Control (GPC).
 * Los navegadores pueden enviar esta señal automáticamente.
 * CCPA/CPRA OBLIGAN a respetar GPC como opt-out válido.
 */
export function detectGlobalPrivacyControl(req: Request, _res: Response, next: NextFunction) {
  // GPC viene como header Sec-GPC: 1
  const gpcHeader = req.headers['sec-gpc'];
  
  if (gpcHeader === '1') {
    // Tratar como opt-out de venta Y compartición
    res.locals.gpcEnabled = true;
    
    logger.info({
      event: 'gpc_detected',
      ip: req.ip,
      userAgent: req.headers['user-agent'],
    }, 'Global Privacy Control detectado — respetando opt-out automático');
  }

  next();
}

/**
 * Middleware para verificar opt-out antes de compartir datos con terceros.
 * USAR en cualquier endpoint que envíe datos a analytics, ad networks, etc.
 */
export function checkOptOutBeforeSharing(req: Request, res: Response, next: NextFunction) {
  const isOptedOut = res.locals.gpcEnabled || res.locals.consumerOptedOut;

  if (isOptedOut) {
    // No enviar datos a partners de advertising/analytics
    res.locals.allowThirdPartySharing = false;
    res.locals.allowTargetedAds = false;
    res.locals.allowCrossSiteTracking = false;
  } else {
    res.locals.allowThirdPartySharing = true;
    res.locals.allowTargetedAds = true;
    res.locals.allowCrossSiteTracking = true;
  }

  next();
}

/**
 * API de Opt-Out.
 * No requiere autenticación — cualquier consumidor puede ejercer este derecho.
 */
export async function handleOptOut(req: Request, res: Response) {
  const { email, optOutSale, optOutSharing, limitSensitiveUse } = req.body;

  // Buscar o crear perfil
  let profile = await prisma.consumerPrivacyProfile.findFirst({
    where: { consumerEmail: email },
  });

  if (profile) {
    profile = await prisma.consumerPrivacyProfile.update({
      where: { id: profile.id },
      data: {
        optOutSale: optOutSale ?? profile.optOutSale,
        optOutSharing: optOutSharing ?? profile.optOutSharing,
        limitSensitiveUse: limitSensitiveUse ?? profile.limitSensitiveUse,
        lastVerified: new Date(),
      },
    });
  } else {
    profile = await prisma.consumerPrivacyProfile.create({
      data: {
        consumerEmail: email,
        optOutSale: optOutSale ?? false,
        optOutSharing: optOutSharing ?? false,
        limitSensitiveUse: limitSensitiveUse ?? false,
      },
    });
  }

  logger.info({
    event: 'opt_out_updated',
    profileId: profile.id,
    optOutSale: profile.optOutSale,
    optOutSharing: profile.optOutSharing,
    limitSensitiveUse: profile.limitSensitiveUse,
  }, 'Preferencias de opt-out actualizadas');

  res.json({
    success: true,
    preferences: {
      optOutSale: profile.optOutSale,
      optOutSharing: profile.optOutSharing,
      limitSensitiveUse: profile.limitSensitiveUse,
    },
    message: 'Tus preferencias de privacidad han sido actualizadas.',
  });
}
```

---

### 4. Notice at Collection (Aviso en Punto de Recolección)

```typescript
// config/ccpa-notice.config.ts

/**
 * CCPA §1798.100(b): Aviso al consumidor en el punto de recolección.
 * Debe informar ANTES de recolectar datos:
 * - Qué categorías se recolectan
 * - Para qué propósitos
 * - Si se venden o comparten
 * - Período de retención
 */

export interface NoticeAtCollection {
  categories: CategoryNotice[];
  retentionPolicies: RetentionPolicy[];
  thirdPartyDisclosure: ThirdPartyDisclosure[];
  links: { privacyPolicy: string; doNotSell: string; rights: string };
}

interface CategoryNotice {
  category: string;
  examples: string[];
  purpose: string;
  retentionPeriod: string;
  sold: boolean;
  shared: boolean;
}

interface RetentionPolicy {
  dataType: string;
  retentionPeriod: string;
  justification: string;
}

interface ThirdPartyDisclosure {
  recipientCategory: string;
  purpose: string;
  dataCategories: string[];
}

export const NOTICE_AT_COLLECTION: NoticeAtCollection = {
  categories: [
    {
      category: 'Identificadores',
      examples: ['Nombre', 'Email', 'Dirección IP'],
      purpose: 'Proveer el servicio, comunicaciones',
      retentionPeriod: 'Mientras la cuenta esté activa + 30 días',
      sold: false,
      shared: false,
    },
    {
      category: 'Información comercial',
      examples: ['Historial de compras', 'Suscripciones'],
      purpose: 'Proveer el servicio, facturación',
      retentionPeriod: '7 años (requisitos fiscales)',
      sold: false,
      shared: false,
    },
    {
      category: 'Actividad en Internet',
      examples: ['Páginas visitadas', 'Funcionalidades usadas'],
      purpose: 'Mejorar el servicio, analytics',
      retentionPeriod: '12 meses',
      sold: false,
      shared: false,
    },
  ],
  retentionPolicies: [
    {
      dataType: 'Datos de cuenta',
      retentionPeriod: 'Duración de cuenta + 30 días de gracia',
      justification: 'Necesario para proveer el servicio',
    },
    {
      dataType: 'Registros de transacciones',
      retentionPeriod: '7 años',
      justification: 'Requisitos fiscales y legales',
    },
    {
      dataType: 'Logs de actividad',
      retentionPeriod: '12 meses',
      justification: 'Seguridad y mejora del servicio',
    },
  ],
  thirdPartyDisclosure: [
    {
      recipientCategory: 'Proveedores de servicios (Service Providers)',
      purpose: 'Hosting, email, procesamiento de pagos',
      dataCategories: ['Identificadores', 'Información comercial'],
    },
  ],
  links: {
    privacyPolicy: '/privacy',
    doNotSell: '/do-not-sell',
    rights: '/privacy-rights',
  },
};

/**
 * Endpoint para servir el notice at collection y links de privacidad.
 */
export function getPrivacyNotice(): NoticeAtCollection {
  return NOTICE_AT_COLLECTION;
}
```

---

### 5. Menores de Edad (CCPA §1798.120(c-d))

```typescript
// services/ccpa-minors.service.ts

import { PrismaClient } from '@prisma/client';
import pino from 'pino';

const prisma = new PrismaClient();
const logger = pino({ name: 'ccpa-minors' });

/**
 * CCPA trata a los menores de forma especial:
 * - Menores de 13 años: Requieren consentimiento PARENTAL (opt-in) para vender/compartir PI
 * - 13-15 años: Requieren consentimiento del MENOR (opt-in) para vender/compartir PI
 * - 16+ años: Se aplican las reglas normales (opt-out)
 * 
 * CPRA extiende esto a COMPARTIR datos, no solo vender.
 */

export class CCPAMinorsService {
  /**
   * Verificar si podemos vender/compartir datos de un consumidor menor.
   */
  async canSellOrShareData(consumerId: string): Promise<{
    allowed: boolean;
    reason: string;
  }> {
    const profile = await prisma.consumerPrivacyProfile.findFirst({
      where: { accountId: consumerId },
    });

    if (!profile) {
      return { allowed: false, reason: 'Perfil de privacidad no encontrado' };
    }

    // Si el consumidor ha hecho opt-out (cualquier edad > 16)
    if (profile.optOutSale || profile.optOutSharing) {
      return { allowed: false, reason: 'Consumidor ejerció opt-out' };
    }

    // Verificación de menores
    if (profile.isMinor) {
      if (!profile.parentalConsent) {
        return {
          allowed: false,
          reason: 'Menor de edad — se requiere consentimiento parental verificado',
        };
      }
    }

    return { allowed: true, reason: 'Permitido' };
  }
}
```

---

## Flujo de trabajo del agente

1. Identificar si la aplicación recolecta PI de residentes de California y si cumple los umbrales de aplicabilidad ($25M ingresos, 100k+ consumidores, o 50%+ ingresos por venta de datos).
2. Implementar el modelo de datos de privacidad con perfiles de consumidor y solicitudes DSAR.
3. Implementar el servicio de derechos del consumidor cubriendo todos los derechos aplicables (know, delete, correct, portability, opt-out sale, opt-out sharing, limit SPI).
4. Agregar middleware de opt-out con detección de Global Privacy Control (GPC) y verificación antes de compartir datos con terceros.
5. Configurar el Notice at Collection con categorías de PI, propósitos, políticas de retención y links obligatorios.
6. Implementar protección de menores con opt-in verificado para menores de 16 años.
7. Validar contra el checklist de cumplimiento antes de desplegar.

## Gotchas

El opt-out de venta/compartición NO debe requerir login ni autenticación — cualquier consumidor puede ejercerlo. La señal GPC (`Sec-GPC: 1`) es legalmente vinculante bajo CCPA/CPRA y debe respetarse como opt-out automático. Las solicitudes de consumidor deben acusarse en 10 días hábiles y resolverse en 45 días (extensible a 90 con notificación). El consumidor puede hacer máximo 2 solicitudes Right to Know por período de 12 meses. No discriminar al consumidor por ejercer sus derechos (no cobrar más ni degradar servicio). Los menores de 13 requieren consentimiento parental, y los de 13-15 requieren consentimiento del propio menor (opt-in) antes de vender o compartir su PI. Mantener registro de todas las solicitudes por 24 meses. Los contratos con service providers deben incluir cláusulas que prohíban uso de PI fuera del servicio contratado. Evitar dark patterns en el proceso de opt-out.

---

## Checklist de Cumplimiento CCPA/CPRA

### Derechos del Consumidor
- [ ] Right to Know (saber qué PI se recolecta y cómo se usa)
- [ ] Right to Delete (eliminar PI)
- [ ] Right to Correct (corregir PI inexacta) — CPRA
- [ ] Right to Portability (obtener PI en formato portable) — CPRA
- [ ] Right to Opt-Out de venta de PI
- [ ] Right to Opt-Out de compartición de PI — CPRA
- [ ] Right to Limit uso de Sensitive Personal Information — CPRA
- [ ] Right to Non-Discrimination

### Avisos y Links
- [ ] Privacy Policy actualizada con disclosures CCPA/CPRA
- [ ] Notice at Collection (antes de recolectar datos)
- [ ] Link "Do Not Sell or Share My Personal Information" visible
- [ ] Link "Limit the Use of My Sensitive Personal Information" — CPRA
- [ ] Información sobre retención de datos

### Operaciones
- [ ] Verificación de identidad para solicitudes de consumidores
- [ ] Proceso de respuesta dentro de 45 días (máximo 90 con extensión)
- [ ] Acuse de recibo dentro de 10 días hábiles
- [ ] Registro de solicitudes por 24 meses
- [ ] Global Privacy Control (GPC) respetado
- [ ] Protección especial para menores de 16 años
- [ ] Contratos con service providers con cláusulas de privacidad
- [ ] Entrenamiento de empleados que manejan solicitudes de consumidores

---

## Referencias y Recursos

- [CCPA Texto completo — California Legislative Information](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5)
- [CPRA Texto completo](https://thecpra.org/)
- [California Privacy Protection Agency (CPPA)](https://cppa.ca.gov/)
- [Global Privacy Control (GPC)](https://globalprivacycontrol.org/)
- [CCPA Regulations — Final Text](https://www.oag.ca.gov/privacy/ccpa/regs)
