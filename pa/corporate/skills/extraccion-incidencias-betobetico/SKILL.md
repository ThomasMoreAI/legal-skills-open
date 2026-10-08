---
name: extraccion-incidencias-betobetico
title: Propósito
description: Extrae incidencias de due diligence clasificadas por categoría, severidad y recomendación
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/extraccion-incidencias
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

## Propósito

Esta skill analiza los documentos de un Virtual Data Room (VDR) y extrae incidencias organizadas por categoría jurídica. Cada incidencia incluye severidad, impacto estimado y recomendación. Aplica un umbral de materialidad configurable para filtrar hallazgos menores.

## Instrucciones

### Paso 1 — Cargar configuración

1. Leer umbral de materialidad desde `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`.
2. Si no existe, usar umbral por defecto: incidencias con impacto potencial > USD 50.000 (B/. 50.000) o que afecten a la continuidad del negocio.
3. Cargar categorías de análisis y criterios específicos del despacho.

### Paso 2 — Analizar documentos por categoría

Revisar los documentos agrupándolos en:

1. **Societario**: constitución, pacto social, actas, poderes, estructura accionarial.
2. **Contratos**: contratos materiales, cambio de control, restricciones de cesión.
3. **Laboral**: planilla, litigios, convención colectiva, altos directivos, planes de incentivos.
4. **Fiscal**: contingencias, fiscalizaciones de la DGI, pérdidas fiscales acumuladas, precios de transferencia.
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
| 1 | [descripción] | [nivel] | [USD/B/. o cualitativo] | [nivel] | [acción] |

### Incidencias menores (bajo umbral de materialidad)

| Categoría | Número | Descripción agrupada |
|-----------|--------|----------------------|
| [cat]     | [n]    | [resumen]            |

### Recomendaciones para el SPA

[Lista de cláusulas sugeridas para el contrato de compraventa]
```

## Referencias normativas

- **Ley 32 de 1927**: sobre sociedades anónimas — estructura, órganos, acciones.
- **Registro Público de Panamá**: inscripciones y publicidad registral.
- **Código de Comercio de Panamá**: contabilidad y obligaciones mercantiles.
- **Código de Trabajo de Panamá**: relaciones laborales y contingencias.
- **Código Fiscal de Panamá**: obligaciones y contingencias tributarias — declaración jurada de renta ISR hasta el 31 de marzo (art. 710); ITBMS.
- **Ley 25 de 1995**: fundaciones de interés privado.

## Guardrails

- **NO** cuantifica contingencias fiscales ni laborales con precisión — proporciona rangos orientativos.
- **NO** sustituye el informe de due diligence de un abogado idóneo — es herramienta de apoyo.
- **NO** accede al Registro Público ni a bases de datos externas.
- **NO** valora la operación comercialmente.
- **ESCALAR** si se detectan incidencias CRÍTICAS que puedan ser deal-breakers.
- **ESCALAR** si la documentación es insuficiente para evaluar una categoría completa.
- **AVISAR** si el umbral de materialidad no está configurado y se usa el valor por defecto.
