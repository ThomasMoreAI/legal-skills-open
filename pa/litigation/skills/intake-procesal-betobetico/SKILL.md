---
name: intake-procesal-betobetico
title: Propósito
description: Realiza la apertura estructurada de un nuevo asunto procesal con ficha, cronología inicial y registro
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

## Propósito

Esta skill estructura la apertura de un nuevo asunto procesal. Crea la ficha del asunto con todos los campos necesarios, genera una cronología inicial y registra los datos de contacto y seguimiento. Diseñada para estandarizar el alta de nuevos asuntos en el despacho.

## Instrucciones

### Paso 1 — Recopilar datos del asunto

Solicitar al usuario la siguiente información:

**Datos generales:**
- Nombre del asunto / referencia interna.
- Cliente (nombre, cédula o RUC, datos de contacto).
- Contraparte(s) (nombre, cédula o RUC si se conoce).
- Tipo de asunto: demandante / demandado / consulta / preventivo.

**Datos procesales:**
- Jurisdicción: civil, laboral, contencioso-administrativo, penal, comercial.
- Proceso: ordinario, sumario, oral, ejecutivo, laboral, etc.
- Tribunal (si ya está determinado).
- Número de expediente / entrada (si existe).
- Cuantía (determinada / indeterminada).

**Equipo:**
- Abogado responsable (idóneo).
- Abogado externo (si aplica).
- Apoderado judicial.
- Perito (si aplica).

**Estado inicial:**
- Fase actual: preinicial, demanda presentada, contestación pendiente, etc.
- Próximo término o acción.
- Documentación recibida.

### Paso 2 — Verificar completitud

Comprobar que están todos los campos mínimos:
- Cliente y contraparte identificados.
- Jurisdicción y tipo de proceso.
- Abogado responsable asignado.
- Al menos un hecho o documento de partida.

### Paso 3 — Generar cronología inicial

Con los datos disponibles, crear las primeras entradas de la línea temporal:
- Fecha de los hechos principales.
- Fecha de recepción del encargo.
- Próximas fechas clave (términos, audiencias).

### Paso 4 — Generar ficha del asunto

## Formato de salida

```markdown
## Ficha de apertura de asunto

**Referencia:** [código interno]
**Fecha de apertura:** [fecha]

### Datos generales

| Campo | Valor |
|-------|-------|
| Nombre del asunto | [nombre] |
| Cliente | [nombre — cédula/RUC] |
| Contraparte | [nombre — cédula/RUC] |
| Posición | [demandante / demandado] |
| Jurisdicción | [civil/laboral/contencioso/penal/comercial] |
| Proceso | [tipo] |
| Tribunal | [nombre y distrito judicial] |
| Nº de expediente | [número o "pendiente"] |
| Cuantía | [importe en B/. o "indeterminada"] |

### Equipo

| Rol | Nombre | Contacto |
|-----|--------|----------|
| Abogado responsable | [nombre] | [email/tel] |
| Abogado externo | [nombre] | [email/tel] |
| Apoderado judicial | [nombre] | [email/tel] |

### Cronología inicial

| # | Fecha | Hecho | Fuente |
|---|-------|-------|--------|
| 1 | [fecha] | [hecho] | [documento] |

### Próximas acciones

| Acción | Plazo | Responsable | Estado |
|--------|-------|-------------|--------|
| [acción] | [fecha] | [nombre] | Pendiente |

### Documentación recibida

| # | Documento | Fecha recepción | Origen |
|---|-----------|-----------------|--------|
| 1 | [nombre] | [fecha] | [quién lo entregó] |

### Datos de facturación

| Campo | Valor |
|-------|-------|
| Tipo de encargo | [iguala / hora / éxito / mixto] |
| Presupuesto estimado | [importe en B/. o "por definir"] |
| Provisión de fondos | [importe en B/. o "pendiente"] |

### Notas iniciales

[Observaciones del abogado responsable sobre el asunto]
```

## Referencias normativas

- **Código Judicial de Panamá**: requisitos de la demanda (para preparar la futura estrategia) [verificar].
- **Constitución Política de Panamá**: derecho al debido proceso y acceso a la justicia [verificar].
- **Código de Ética y Responsabilidad Profesional del Abogado**: conflicto de intereses y deber de diligencia [verificar].
- **Ley 81 de 2019** (protección de datos personales): tratamiento de datos de las partes [verificar].

## Guardrails

- **NO** abre asuntos en sistemas de gestión del despacho — genera la ficha para que el usuario la introduzca.
- **NO** verifica conflictos de intereses — eso es responsabilidad del despacho.
- **NO** factura ni gestiona provisiones de fondos.
- **NO** contacta a apoderados judiciales ni peritos.
- **AVISAR** si faltan datos mínimos obligatorios para completar la ficha.
- **AVISAR** si no se ha asignado abogado responsable.
- **ESCALAR** si el asunto tiene un término procesal inminente (< 10 días hábiles).
