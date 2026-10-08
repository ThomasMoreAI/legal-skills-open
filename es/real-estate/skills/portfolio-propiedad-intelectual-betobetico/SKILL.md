---
name: portfolio-propiedad-intelectual-betobetico
title: Propósito
description: Rastrea el estado de registros de PI, fechas de renovación y tasas de mantenimiento pendientes
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/portfolio
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

## Propósito

Esta skill gestiona el portfolio de activos de propiedad intelectual e industrial de una empresa o cliente. Rastrea el estado de registros, fechas de renovación, tasas de mantenimiento y acciones pendientes para marcas, patentes y diseños.

## Instrucciones

### Paso 1 — Cargar inventario de activos

1. Leer el registro de activos de PI proporcionado por el usuario.
2. Clasificar cada activo por tipo:
   - **Marcas**: nacionales (OEPM), europeas (EUIPO), internacionales (OMPI/Madrid).
   - **Patentes**: nacionales (OEPM), europeas (OEP), PCT.
   - **Modelos de utilidad**: OEPM.
   - **Diseños industriales**: OEPM, EUIPO (diseño comunitario registrado).
   - **Nombres de dominio**: .es, .com, .eu, otros.
   - **Derechos de autor**: registros en el Registro de la Propiedad Intelectual.

### Paso 2 — Calcular fechas clave

**Marcas:**
- Duración: 10 años desde la solicitud.
- Renovación: solicitar en los 6 meses anteriores al vencimiento (o 6 meses de gracia con recargo).
- OEPM y EUIPO: renovaciones por períodos de 10 años.

**Patentes:**
- Duración máxima: 20 años desde la solicitud.
- Anualidades: pago anual de tasas de mantenimiento (a partir del 3er año en OEPM).
- Plazo de pago: en los 3 meses anteriores al vencimiento de la anualidad.

**Diseños:**
- OEPM: 5 años, renovable por períodos de 5 años hasta máx. 25 años.
- EUIPO: 5 años, renovable hasta máx. 25 años.

**Modelos de utilidad:**
- Duración: 10 años desde la solicitud.
- Anualidades desde el 3er año.

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
| [nombre] | [tipo] | [nº registro] | [renovación/anualidad] | [fecha] | [EUR] |

### Inventario completo

| Activo | Tipo | Registro | Clases/Reivindicaciones | Territorio | Vigencia | Estado | Próxima acción |
|--------|------|----------|-------------------------|------------|----------|--------|----------------|
| [nombre] | [tipo] | [nº] | [detalle] | [territorio] | [hasta fecha] | [estado] | [acción y fecha] |

### Presupuesto estimado de tasas (próximos 12 meses)

| Activo | Acción | Fecha | Tasa estimada |
|--------|--------|-------|---------------|
| [nombre] | [tipo] | [fecha] | [EUR] |
| **TOTAL** | | | **[EUR]** |
```

## Referencias normativas

- **Ley de Marcas 17/2001**: art. 32 (duración), art. 33 (renovación).
- **Ley de Patentes 24/2015**: arts. 56-58 (duración y mantenimiento).
- **Ley 20/2003**: Protección jurídica del diseño industrial — arts. 43-46.
- **Reglamento (UE) 2017/1001**: Marca de la Unión Europea — arts. 52-53.
- **Reglamento (CE) 6/2002**: Diseño comunitario — arts. 12-13.
- **Convenio de Múnich (CPE)**: Patente europea — arts. 63, 86.

## Guardrails

- **NO** presenta solicitudes de renovación ni paga tasas.
- **NO** accede a bases de datos oficiales (OEPM, EUIPO, OMPI) — trabaja con datos proporcionados.
- **NO** valora la conveniencia de mantener o abandonar un activo.
- **NO** estima con precisión las tasas — proporciona rangos orientativos.
- **ESCALAR** si un activo estratégico está en período de gracia o próximo a caducar.
- **AVISAR** si faltan datos para calcular fechas de renovación (fecha de solicitud, territorio).
- **AVISAR** si se detectan activos sin responsable asignado.
