---
name: checklist-cierre-ma
title: Propósito
description: Rastrea condiciones precedentes, consentimientos y documentos pendientes para el cierre de una operación M&A
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/societario/skills/checklist-cierre
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: es
---

## Propósito

Esta skill gestiona la checklist de cierre (closing checklist) de una operación de M&A. Rastrea el estado de cada condición precedente, consentimiento de terceros y documento pendiente de entrega. Diseñada para mantener visibilidad sobre el progreso hacia el cierre de la operación.

## Instrucciones

### Paso 1 — Extraer condiciones del SPA

1. Leer el contrato de compraventa (SPA) o el listado de condiciones precedentes proporcionado.
2. Identificar todas las condiciones de cierre:
   - **Condiciones precedentes (CPs)**: autorizaciones, consentimientos, certificados.
   - **Documentos de cierre**: escrituras, poderes, certificados, cartas.
   - **Consentimientos de terceros**: cambio de control, waiver de socios, autorización regulatoria.
   - **Acciones previas al cierre**: reorganizaciones, distribuciones, cancelaciones.

### Paso 2 — Asignar responsable y plazo

Para cada elemento:

1. **Responsable**: quién debe completarlo (comprador, vendedor, target, asesores, notario, registrador).
2. **Plazo**: fecha límite o condición temporal (ej. "antes del cierre", "5 días tras firma").
3. **Dependencias**: si un elemento depende de otro previo.

### Paso 3 — Clasificar estado

- **Pendiente**: no iniciado.
- **En curso**: trabajo en progreso, con detalle de próximo paso.
- **Completado**: entregado y conforme.
- **Bloqueado**: depende de un elemento que no avanza — indicar cuál.
- **Renunciado**: la parte beneficiaria ha renunciado a la condición (waiver).

### Paso 4 — Generar checklist

## Formato de salida

```markdown
## Checklist de cierre — [Nombre de la operación]

**Fecha de firma del SPA:** [fecha]
**Fecha prevista de cierre (longstop):** [fecha]
**Días hasta longstop:** [n]
**Estado general:** [n]/[total] completados

### Resumen de progreso

| Estado | Número | Porcentaje |
|--------|--------|------------|
| Completado | [n] | [%] |
| En curso | [n] | [%] |
| Pendiente | [n] | [%] |
| Bloqueado | [n] | [%] |

### Condiciones precedentes

| # | Condición | Responsable | Plazo | Estado | Notas |
|---|-----------|-------------|-------|--------|-------|
| CP-1 | [descripción] | [parte] | [fecha] | [estado] | [detalle] |

### Consentimientos de terceros

| # | Consentimiento | Tercero | Responsable | Estado | Notas |
|---|----------------|---------|-------------|--------|-------|
| C-1 | [descripción] | [nombre] | [parte] | [estado] | [detalle] |

### Documentos de cierre

| # | Documento | Responsable | Estado | Notas |
|---|-----------|-------------|--------|-------|
| D-1 | [descripción] | [parte] | [estado] | [detalle] |

### Elementos bloqueados

| Elemento | Bloqueado por | Acción requerida | Responsable |
|----------|---------------|------------------|-------------|
| [ref]    | [ref]         | [acción]         | [parte]     |

### Próximos pasos

[Lista priorizada de acciones para avanzar hacia el cierre]
```

## Referencias normativas

- **LME** (Ley 3/2009): Transformaciones, fusiones y escisiones.
- **LSC arts. 21-23**: Escritura y estatutos — formalidades de constitución y modificación.
- **CC arts. 1445-1537**: Compraventa — aplicable supletoriamente.
- **Ley 15/2007 (LDC)**: Control de concentraciones (CNMC) si aplica.
- **Ley 19/2003**: Régimen de inversiones exteriores si hay componente internacional.
- **RRM**: Inscripción de la transmisión de participaciones/acciones.

## Guardrails

- **NO** ejecuta ninguna acción de cierre — solo rastrea el estado.
- **NO** contacta a terceros ni envía solicitudes de consentimiento.
- **NO** redacta documentos de cierre — para eso usar la skill de acuerdo-social u otras específicas.
- **NO** valora si las condiciones precedentes se han cumplido sustantivamente — solo el estado formal.
- **ESCALAR** si quedan menos de 15 días para el longstop con elementos bloqueados.
- **ESCALAR** si una condición precedente regulatoria (CNMC, inversiones exteriores) está pendiente.
- **AVISAR** si no se proporciona fecha de longstop o fecha de firma.
