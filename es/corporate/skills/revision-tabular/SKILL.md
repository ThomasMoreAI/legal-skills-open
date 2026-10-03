---
name: revision-tabular
title: Propósito
description: Genera una tabla de revisión documental de due diligence con una fila por documento y citas normativas
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/societario/skills/revision-tabular
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: en
---

## Propósito

Esta skill procesa los documentos de un data room virtual (VDR) para generar una tabla de revisión de due diligence. Cada documento se convierte en una fila con categorización, hallazgos clave, nivel de riesgo y referencia normativa. Diseñada para la fase de revisión documental de operaciones de M&A, inversión o financiación.

## Instrucciones

### Paso 1 — Indexar documentos

1. Leer la lista de documentos proporcionados por el usuario.
2. Clasificar cada documento en una categoría:
   - Societario (escrituras, estatutos, actas, poderes)
   - Contratos (mercantiles, laborales, financieros)
   - Laboral (plantilla, convenios, litigios laborales)
   - Fiscal (declaraciones, actas inspección, certificados)
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
- Documentos obligatorios por ley que no aparecen (ej. cuentas anuales, libros de actas).
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

- **LSC** (RDL 1/2010): Ley de Sociedades de Capital — estructura societaria, órganos, cuentas.
- **RRM** (RD 1784/1996): Reglamento del Registro Mercantil — inscripciones obligatorias.
- **Código de Comercio**: arts. 25-49 (contabilidad), arts. 116-174 (sociedades).
- **LIS** (Ley 27/2014): Impuesto sobre Sociedades — obligaciones fiscales.
- **ET** (RDL 2/2015): Estatuto de los Trabajadores — documentación laboral.
- **LME** (Ley 3/2009): Modificaciones estructurales de sociedades mercantiles.

## Guardrails

- **NO** emite opinión legal sobre la operación — solo documenta hallazgos.
- **NO** valora la conveniencia comercial de la transacción.
- **NO** accede a registros públicos — trabaja exclusivamente con documentos proporcionados.
- **ESCALAR** si se detectan más de 3 documentos de riesgo ALTO en una misma categoría.
- **ESCALAR** si faltan documentos obligatorios por ley (cuentas anuales, escritura de constitución).
- **AVISAR** si los documentos proporcionados están incompletos o son ilegibles.
