---
name: portfolio-propiedad-intelectual-3787-betobetico
title: Propósito
description: Rastrea el estado de registros de PI, fechas de renovación y tasas de mantenimiento pendientes
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/propiedad-intelectual/skills/portfolio
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

## Propósito

Esta skill gestiona el portfolio de activos de propiedad intelectual e industrial de una empresa o cliente. Rastrea el estado de registros, fechas de renovación, tasas de mantenimiento y acciones pendientes para marcas, patentes y diseños.

## Instrucciones

### Paso 1 — Cargar inventario de activos

1. Leer el registro de activos de PI proporcionado por el usuario.
2. Clasificar cada activo por tipo:
   - **Marcas**: nacionales (DIGERPI); internacionales por registro nacional en cada país (Panamá NO es parte del Protocolo de Madrid).
   - **Patentes**: nacionales (DIGERPI), internacionales (PCT).
   - **Modelos de utilidad**: DIGERPI.
   - **Diseños industriales**: DIGERPI.
   - **Nombres de dominio**: .pa, .com, otros.
   - **Derechos de autor**: registros en la Dirección Nacional de Derecho de Autor (DNDA) del Ministerio de Cultura — registro declarativo y optativo; la obra se protege desde su creación (Ley 64 de 2012; competencia traspasada al Ministerio de Cultura por la Ley 90 de 2019).

### Paso 2 — Calcular fechas clave

**Marcas:**
- Duración: 10 años contados desde la fecha de presentación de la solicitud (no desde la concesión), renovable indefinidamente por períodos iguales de 10 años (art. 109 de la Ley 35 de 1996).
- Renovación: se solicita en la ventana de 1 año antes del vencimiento, con período de gracia de 6 meses posteriores con recargo (arts. 110 y 205 de la Ley 35 de 1996).

**Patentes:**
- Duración máxima: 20 años improrrogables desde la presentación de la solicitud (art. 20 de la Ley 35 de 1996).
- Tasas de mantenimiento por quinquenios (cada 5 años), no anualidades (art. 207); la falta de pago, tras 6 meses de gracia con recargo, causa caducidad de pleno derecho.

**Diseños industriales:**
- 10 años, prorrogable una vez por 5 años adicionales (máx. 15 años) (arts. 79-80 de la Ley 35 de 1996).

**Modelos de utilidad:**
- 10 años improrrogables (art. 26 de la Ley 35 de 1996).

### Paso 3 — Evaluar estado

Para cada activo:
- **Vigente**: registro activo con todas las tasas al día.
- **Próxima renovación**: vence en los próximos 90 días.
- **En gracia**: período de gracia activo (con recargo).
- **Pendiente de pago**: tasa vencida sin pago registrado.
- **En trámite**: solicitud pendiente de resolución.
- **Caducado/Extinguido**: derecho perdido.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Portfolio de propiedad intelectual e industrial

**Titular:** [nombre/empresa]
**Fecha del informe:** [fecha]
**Total de activos:** [número]

### Resumen por tipo

| Tipo | Vigentes | En trámite | Próx. renovación (90d) | Caducados |
|------|----------|------------|------------------------|-----------|
| Marcas | [n] | [n] | [n] | [n] |
| Patentes | [n] | [n] | [n] | [n] |
| Diseños | [n] | [n] | [n] | [n] |
| Otros | [n] | [n] | [n] | [n] |

### Acciones urgentes (próximos 90 días)

| Activo | Tipo | Registro | Acción | Fecha límite | Tasa estimada |
|--------|------|----------|--------|--------------|---------------|
| [nombre] | [tipo] | [nº registro] | [renovación/anualidad] | [fecha] | [USD (B/.)] |

### Inventario completo

| Activo | Tipo | Registro | Clases/Reivindicaciones | Territorio | Vigencia | Estado | Próxima acción |
|--------|------|----------|-------------------------|------------|----------|--------|----------------|
| [nombre] | [tipo] | [nº] | [detalle] | [territorio] | [hasta fecha] | [estado] | [acción y fecha] |

### Presupuesto estimado de tasas (próximos 12 meses)

| Activo | Acción | Fecha | Tasa estimada |
|--------|--------|-------|---------------|
| [nombre] | [tipo] | [fecha] | [USD (B/.)] |
| **TOTAL** | | | **[USD (B/.)]** |
```

## Referencias normativas

- **Ley 35 de 1996** (propiedad industrial, mod. Ley 61 de 2012): duración (10 años, art. 109) y renovación de marcas (arts. 110 y 205).
- **Ley 35 de 1996**: duración y mantenimiento de patentes (20 años, art. 20; tasas por quinquenios, art. 207) y modelos de utilidad (10 años, art. 26).
- **Ley 35 de 1996**: protección y vigencia de los diseños industriales (10 años prorrogables una vez por 5 años, arts. 79-80).
- **Protocolo de Madrid**: Panamá NO es parte contratante; las marcas se gestionan por la vía nacional ante la DIGERPI o por registro nacional en cada país extranjero.
- **Tratado de Cooperación en materia de Patentes (PCT)**: solicitudes internacionales de patente.

## Guardrails

- **NO** presenta solicitudes de renovación ni paga tasas.
- **NO** accede a bases de datos oficiales (DIGERPI, OMPI) — trabaja con datos proporcionados.
- **NO** valora la conveniencia de mantener o abandonar un activo.
- **NO** estima con precisión las tasas — proporciona rangos orientativos.
- **ESCALAR** si un activo estratégico está en período de gracia o próximo a caducar.
- **AVISAR** si faltan datos para calcular fechas de renovación (fecha de solicitud, territorio).
- **AVISAR** si se detectan activos sin responsable asignado.
