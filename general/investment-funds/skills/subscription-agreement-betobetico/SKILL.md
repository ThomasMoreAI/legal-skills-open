---
name: subscription-agreement-betobetico
title: Subscription Agreement
description: Generación / revisión de subscription agreements para LPs — cláusulas estándar + checks pre-firma (KYC/AML, idoneidad, FATCA/CRS). Triggers en "subscription agreement", "subscription docs", "contrato suscripción LP".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/subscription-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: investment-funds
language: es
---

# Subscription Agreement

## Paso 0
Carga perfil. Para cada LP nuevo, requiere coordinación con `operaciones:kyc-parser` y `operaciones:kyc-reglas`.

## Paso 1 — Inputs

- LP suscriptor: nombre, tipo (persona física / jurídica / trust), jurisdicción, CIF/TIN
- Vehículo al que se suscribe
- Commitment: importe en EUR
- Clase de participación (si multi-clase)
- Es primer cierre o cierre adicional
- Documentación KYC recibida

## Paso 2 — Estructura del Subscription Agreement

```markdown
# Subscription Agreement

**Fondo:** {Vehículo}
**Gestora:** {SGEIC}
**Fecha de suscripción:** {fecha}

## 1. Datos del Inversor
- Razón social / Nombre: ...
- Forma jurídica: ...
- CIF/NIF/TIN: ...
- Domicilio: ...
- País de residencia fiscal: ...
- Representante autorizado: ...

## 2. Compromiso
- Importe comprometido: EUR {X}
- Clase: {A, B, C, founder, etc.}
- Modalidad de aportación: capital calls según LPA

## 3. Manifestaciones del Inversor (reps & warranties)
[Standard reps:]
- Capacidad legal y autorización
- Categoría de inversor (institucional / profesional / minorista cualificado)
- Origen lícito de los fondos
- No estar en listas de sanciones
- Conocimiento de los riesgos
- No actuar por cuenta de terceros (o si sí, identificación del UBO)

## 4. Aceptación del LPA
- Adhesión al LPA del fondo
- Confirmación de haber recibido y leído: LPA, folleto (si aplica), KID PRIIPs (si aplica), materiales de marketing

## 5. Fiscalidad
### 5.1 FATCA / CRS
- Clasificación FATCA del inversor: ...
- Formulario W-8/W-9 o equivalente: aportado
- Información CRS: aportada

### 5.2 Otros
- Retención fiscal aplicable
- Tax forms locales

## 6. Side Letter
- ¿Hay side letter? Sí/No
- Si sí: identificada en anexo

## 7. Notificaciones
- Datos contacto para capital calls, distribuciones, reporting
- Cuentas bancarias del Inversor para distribuciones

## 8. Firma
- Por el Inversor: {firmante autorizado}
- Aceptación por la Gestora: {apoderado}
```

## Paso 3 — Checks pre-firma obligatorios

| Check | Status | Owner |
|---|---|---|
| KYC completo (documentos + verificación identidad) | ✅/⚠️/❌ | Operaciones |
| AML screening (PEP, sanciones, jurisdicción) | ✅/⚠️/❌ | Compliance |
| Categorización MiFID | ✅/⚠️/❌ | Comercial / GC |
| FATCA classification + W-8/W-9 | ✅/❌ | LP + Compliance |
| CRS classification | ✅/❌ | LP + Compliance |
| Origen de fondos justificado | ✅/⚠️/❌ | Operaciones |
| UBO identificado (si LP es jurídica) | ✅/❌ | Operaciones |
| Side letter (si aplica) firmada en paralelo | N/A o ✅ | GC |

**Si cualquier check no es ✅ → bloquear firma y resolver primero.**

## Paso 4 — Coordinación con operaciones

Ejecuta o referencia:
- `/operaciones:kyc-parser` para extracción de datos del LP
- `/operaciones:kyc-reglas` para evaluación rules-grid

Si los outputs anteriores muestran riesgo **Alto** o **Inaceptable**, NO firmar el subscription agreement — escalar a comité de aceptación.

## Paso 5 — Outputs

1. **Subscription Agreement** (borrador completo, listo para revisión + firma)
2. **Checklist de checks pre-firma** (status por check)
3. **Side Letter** (si aplica) — vincular o redactar con `side-letter`
4. **Email para el LP** con docs adjuntos para firma electrónica
5. **Entrada en sistema legal** (formato JSON o markdown para CRM/DMS)

## Casos especiales

- **LP profesional reconocido (gestora institucional)**: process más ágil, menos disclosures
- **LP HNW / Family Office**: reps adicionales sobre estructuras (trust, holding, fundación), UBO real
- **LP no residente fiscal España**: foco en treaty benefits, withholding y CRS
- **LP corporativo cotizado**: posible disclosure pública del commitment
- **LP en jurisdicción de alto riesgo (GAFI grey list)**: diligencia reforzada, posible bloqueo
- **LP con cuenta nominee / custodio**: identificar beneficiario final

## Cierre

> *Subscription Agreement. Firma final requiere: (1) todos los checks ✅, (2) firma del LP, (3) aceptación de la Gestora por apoderado, (4) entrada en el libro de partícipes. Cualquier desviación de proceso requiere aprobación del GC y posiblemente del Comité de Aceptación.*
