---
name: portfolio-procesal-4149-betobetico
title: Propósito
description: Genera un dashboard del portfolio de asuntos procesales con distribución de riesgo, plazos y costes
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/portfolio
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

## Propósito

Esta skill genera una vista consolidada (dashboard) del portfolio de asuntos procesales activos. Muestra la distribución de riesgo, próximos términos, asuntos inactivos y resumen de costes. Diseñada para reuniones de seguimiento del departamento legal o comité de dirección.

## Instrucciones

### Paso 1 — Cargar registro de asuntos

1. Leer el registro de asuntos proporcionado (fichas de intake, base de datos, listado).
2. Filtrar asuntos activos (excluir archivados y cerrados).
3. Verificar que cada asunto tiene los datos mínimos: referencia, cliente, jurisdicción, fase, riesgo, cuantía.

### Paso 2 — Clasificar y agregar

**Por jurisdicción:**
- Civil, laboral, contencioso-administrativo, penal, comercial.

**Por posición:**
- Demandante, demandado, preventivo/consulta.

**Por fase:**
- Preinicial, primera instancia, apelación, casación (CSJ), ejecución.

**Por riesgo:**
- ALTO, MEDIO, BAJO (según última evaluación del briefing o del abogado).

**Por actividad:**
- Activo (última actuación < 30 días).
- Normal (30-90 días).
- Inactivo / stale (> 90 días sin actividad).

### Paso 3 — Identificar alertas

- Asuntos con términos en los próximos 15 días.
- Asuntos inactivos > 90 días (stale matters).
- Asuntos de riesgo ALTO sin briefing actualizado.
- Asuntos con coste acumulado superior al presupuesto.
- Asuntos sin abogado responsable asignado.

### Paso 4 — Generar dashboard

## Formato de salida

```markdown
## Estado del portfolio procesal

**Fecha del informe:** [fecha]
**Asuntos activos:** [número]
**Cuantía total en riesgo:** [importe en B/.]

---

### Resumen ejecutivo

[3-4 frases con los datos más relevantes del portfolio]

### Distribución por riesgo

| Riesgo | Asuntos | Cuantía en riesgo | % del total |
|--------|---------|-------------------|-------------|
| ALTO | [n] | [B/.] | [%] |
| MEDIO | [n] | [B/.] | [%] |
| BAJO | [n] | [B/.] | [%] |

### Distribución por jurisdicción

| Jurisdicción | Asuntos | Demandante | Demandado |
|-------------|---------|------------|-----------|
| Civil | [n] | [n] | [n] |
| Laboral | [n] | [n] | [n] |
| Contencioso | [n] | [n] | [n] |
| Penal | [n] | [n] | [n] |
| Comercial | [n] | [n] | [n] |

### Próximos términos (15 días)

| Asunto | Acción | Fecha límite | Responsable | Riesgo |
|--------|--------|--------------|-------------|--------|
| [ref] | [acción] | [fecha] | [nombre] | [nivel] |

### Asuntos inactivos (>90 días)

| Asunto | Última actividad | Días inactivo | Fase | Responsable |
|--------|------------------|---------------|------|-------------|
| [ref] | [fecha] | [n] | [fase] | [nombre] |

### Resumen económico

| Concepto | Importe |
|----------|---------|
| Cuantía total en riesgo (demandado) | [B/.] |
| Cuantía total reclamada (demandante) | [B/.] |
| Honorarios devengados (período) | [B/.] |
| Provisión para costas estimada | [B/.] |
| Presupuesto consumido vs. estimado | [%] |

### Top 5 asuntos por cuantía

| # | Asunto | Cuantía | Posición | Riesgo | Fase |
|---|--------|---------|----------|--------|------|
| 1 | [ref] | [B/.] | [pos] | [nivel] | [fase] |

### Alertas

| Tipo | Asunto | Detalle | Acción requerida |
|------|--------|---------|------------------|
| Término inminente | [ref] | [detalle] | [acción] |
| Stale matter | [ref] | [días] sin actividad | Revisar estado |
| Sin responsable | [ref] | [detalle] | Asignar abogado |
| Sobrecoste | [ref] | [% sobre presupuesto] | Revisar presupuesto |
```

## Referencias normativas

- Normativa procesal panameña aplicable a cada asunto individualmente (Código Judicial de Panamá) [verificar].
- **Código de Ética y Responsabilidad Profesional del Abogado**: deber de diligencia y seguimiento de asuntos [verificar].
- **Ley 81 de 2019** (protección de datos personales): tratamiento de datos en el registro de asuntos [verificar].

## Guardrails

- **NO** toma decisiones sobre asuntos individuales — solo presenta datos agregados.
- **NO** cierra ni archiva asuntos.
- **NO** modifica datos de asuntos individuales.
- **NO** factura ni emite presupuestos.
- **NO** comparte datos de un cliente con otro (los briefings de portfolio deben filtrarse por cliente si es para reunión con cliente).
- **ESCALAR** si hay más de 3 asuntos de riesgo ALTO simultáneamente.
- **ESCALAR** si hay asuntos sin abogado responsable asignado.
- **AVISAR** si los datos de algún asunto están desactualizados (último briefing > 60 días).
- **AVISAR** si la cuantía total en riesgo supera umbrales del despacho (si están configurados).
