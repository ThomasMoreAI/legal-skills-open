---
name: revision-tabular-betobetico
title: Propósito
description: Genera una tabla de revisión documental de due diligence con una fila por documento y citas normativas
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/revision-tabular
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

## Propósito

Esta skill procesa los documentos de un data room virtual (VDR) para generar una tabla de revisión de due diligence. Cada documento se convierte en una fila con categorización, hallazgos clave, nivel de riesgo y referencia normativa. Diseñada para la fase de revisión documental de operaciones de M&A, inversión o financiación.

## Instrucciones

### Paso 1 — Indexar documentos

1. Leer la lista de documentos proporcionados por el usuario.
2. Clasificar cada documento en una categoría:
   - Societario (pacto social, escrituras públicas, actas, poderes)
   - Contratos (mercantiles, laborales, financieros)
   - Laboral (planilla, convenciones colectivas, litigios laborales)
   - Fiscal (declaraciones de renta, requerimientos de la DGI, paz y salvo)
   - Regulatorio (licencias, autorizaciones, permisos)
   - Litigios (demandas, sentencias, arbitrajes)
   - Propiedad intelectual (registros, licencias, cesiones)
   - Inmobiliario (títulos, arrendamientos, cargas)

### Paso 2 — Analizar cada documento

Para cada documento:

1. Identificar tipo y fecha del documento.
2. Extraer hallazgos clave (hechos relevantes, cifras, obligaciones).
3. Evaluar nivel de riesgo: ALTO / MEDIO / BAJO / INFORMATIVO.
4. Citar la norma aplicable (artículo concreto).
5. Anotar si falta algún documento relacionado.

### Paso 3 — Detectar ausencias

- Documentos esperados según el índice del VDR que no están.
- Documentos obligatorios por ley que no aparecen (ej. pacto social, libros de actas, registro de acciones).
- Versiones desactualizadas de documentos que deberían estar vigentes.

### Paso 4 — Generar tabla

## Formato de salida

```markdown
## Revisión tabular de due diligence

**Operación:** [nombre]
**Fecha de revisión:** [fecha]
**Documentos analizados:** [número]
**Documentos pendientes:** [número]

### Tabla de revisión

| # | Documento | Categoría | Fecha | Hallazgos clave | Riesgo | Referencia normativa | Notas |
|---|-----------|-----------|-------|------------------|--------|----------------------|-------|
| 1 | [nombre]  | [cat]     | [fecha] | [hallazgo]     | [nivel] | [norma art. X]      | [nota] |

### Resumen por categoría

| Categoría | Docs revisados | Riesgo alto | Riesgo medio | Pendientes |
|-----------|----------------|-------------|--------------|------------|
| [cat]     | [n]            | [n]         | [n]          | [n]        |

### Documentos ausentes

| Documento esperado | Categoría | Obligatoriedad | Impacto |
|--------------------|-----------|----------------|---------|
| [nombre]           | [cat]     | Legal/Recomendado | [detalle] |
```

## Referencias normativas

- **Ley 32 de 1927**: sobre sociedades anónimas — estructura societaria, órganos, acciones.
- **Ley 25 de 1995**: sobre fundaciones de interés privado.
- **Código de Comercio de Panamá**: comerciantes, contabilidad y obligaciones mercantiles.
- **Código Fiscal de Panamá**: Impuesto sobre la Renta (ISR) — declaración jurada hasta el 31 de marzo (art. 710), bajo principio de territorialidad.
- **Código de Trabajo de Panamá**: documentación laboral.
- **Ley 23 de 2015**: prevención de blanqueo de capitales — sujetos obligados.

## Guardrails

- **NO** emite opinión legal sobre la operación — solo documenta hallazgos.
- **NO** valora la conveniencia comercial de la transacción.
- **NO** accede al Registro Público ni a otros registros — trabaja exclusivamente con documentos proporcionados.
- **ESCALAR** si se detectan más de 3 documentos de riesgo ALTO en una misma categoría.
- **ESCALAR** si faltan documentos obligatorios por ley (pacto social, escritura de constitución).
- **AVISAR** si los documentos proporcionados están incompletos o son ilegibles.
