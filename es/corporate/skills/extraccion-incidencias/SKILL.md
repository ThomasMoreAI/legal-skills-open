---
name: extraccion-incidencias
title: Propósito
description: Extrae incidencias de due diligence clasificadas por categoría, severidad y recomendación
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/societario/skills/extraccion-incidencias
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

## Propósito

Esta skill analiza los documentos de un Virtual Data Room (VDR) y extrae incidencias organizadas por categoría jurídica. Cada incidencia incluye severidad, impacto estimado y recomendación. Aplica un umbral de materialidad configurable para filtrar hallazgos menores.

## Instrucciones

### Paso 1 — Cargar configuración

1. Leer umbral de materialidad desde `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`.
2. Si no existe, usar umbral por defecto: incidencias con impacto potencial > 50.000 EUR o que afecten a la continuidad del negocio.
3. Cargar categorías de análisis y criterios específicos del despacho.

### Paso 2 — Analizar documentos por categoría

Revisar los documentos agrupándolos en:

1. **Societario**: constitución, estatutos, actas, poderes, estructura accionarial.
2. **Contratos**: contratos materiales, cambio de control, restricciones de cesión.
3. **Laboral**: plantilla, litigios, convenio, altos directivos, planes de incentivos.
4. **Fiscal**: contingencias, inspecciones, bases imponibles negativas, precios de transferencia.
5. **Regulatorio**: licencias, autorizaciones, cumplimiento sectorial.
6. **Litigios**: procedimientos activos, contingencias, provisiones.
7. **Propiedad intelectual**: titularidad, registros, licencias, software.

### Paso 3 — Clasificar cada incidencia

Para cada incidencia detectada:

1. **Descripción**: qué se ha encontrado (fáctico, sin opinión).
2. **Severidad**: CRÍTICA / ALTA / MEDIA / BAJA.
3. **Impacto**: cuantificado si es posible, cualitativo si no.
4. **Probabilidad**: alta / media / baja.
5. **Recomendación**: acción sugerida (declaración y garantía, indemnidad, condición precedente, ajuste de precio).

### Paso 4 — Filtrar por materialidad

Aplicar el umbral de materialidad:
- Incidencias por debajo del umbral se agrupan en "Incidencias menores".
- Incidencias por encima se detallan individualmente.

## Formato de salida

```markdown
## Informe de incidencias de due diligence

**Operación:** [nombre]
**Fecha:** [fecha]
**Umbral de materialidad:** [importe o criterio]

### Resumen ejecutivo

- Incidencias críticas: [n]
- Incidencias altas: [n]
- Incidencias medias: [n]
- Impacto total estimado: [rango]

### Incidencias por categoría

#### [Categoría]

| # | Incidencia | Severidad | Impacto | Probabilidad | Recomendación |
|---|------------|-----------|---------|--------------|---------------|
| 1 | [descripción] | [nivel] | [EUR o cualitativo] | [nivel] | [acción] |

### Incidencias menores (bajo umbral de materialidad)

| Categoría | Número | Descripción agrupada |
|-----------|--------|----------------------|
| [cat]     | [n]    | [resumen]            |

### Recomendaciones para el SPA

[Lista de cláusulas sugeridas para el contrato de compraventa]
```

## Referencias normativas

- **LSC** (RDL 1/2010): estructura, órganos, cuentas anuales.
- **RRM** (RD 1784/1996): inscripciones y publicidad registral.
- **Código de Comercio**: contabilidad y obligaciones mercantiles.
- **ET** (RDL 2/2015): relaciones laborales y contingencias.
- **LGT** (Ley 58/2003): obligaciones y contingencias tributarias.
- **LME** (Ley 3/2009): modificaciones estructurales.

## Guardrails

- **NO** cuantifica contingencias fiscales ni laborales con precisión — proporciona rangos orientativos.
- **NO** sustituye el informe de due diligence de un abogado — es herramienta de apoyo.
- **NO** accede a registros públicos ni bases de datos externas.
- **NO** valora la operación comercialmente.
- **ESCALAR** si se detectan incidencias CRÍTICAS que puedan ser deal-breakers.
- **ESCALAR** si la documentación es insuficiente para evaluar una categoría completa.
- **AVISAR** si el umbral de materialidad no está configurado y se usa el valor por defecto.
