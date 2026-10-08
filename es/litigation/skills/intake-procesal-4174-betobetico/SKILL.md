---
name: intake-procesal-4174-betobetico
title: Propósito
description: Realiza la apertura estructurada de un nuevo asunto procesal con ficha, cronología inicial y registro
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/procesal/skills/intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
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
- Cliente (nombre, CIF/NIF, datos de contacto).
- Contraparte(s) (nombre, CIF/NIF si se conoce).
- Tipo de asunto: demandante / demandado / consulta / preventivo.

**Datos procesales:**
- Jurisdicción: civil, social, contencioso-administrativo, penal, mercantil.
- Procedimiento: ordinario, verbal, monitorio, laboral, etc.
- Órgano judicial (si ya está determinado).
- Número de autos (si existe).
- Cuantía (determinada / indeterminada).

**Equipo:**
- Abogado responsable.
- Abogado externo (si aplica).
- Procurador.
- Perito (si aplica).

**Estado inicial:**
- Fase actual: preinicial, demanda presentada, contestación pendiente, etc.
- Próximo plazo o acción.
- Documentación recibida.

### Paso 2 — Verificar completitud

Comprobar que están todos los campos mínimos:
- Cliente y contraparte identificados.
- Jurisdicción y tipo de procedimiento.
- Abogado responsable asignado.
- Al menos un hecho o documento de partida.

### Paso 3 — Generar cronología inicial

Con los datos disponibles, crear las primeras entradas de la línea temporal:
- Fecha de los hechos principales.
- Fecha de recepción del encargo.
- Próximas fechas clave (plazos, audiencias).

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
| Cliente | [nombre — CIF/NIF] |
| Contraparte | [nombre — CIF/NIF] |
| Posición | [demandante / demandado] |
| Jurisdicción | [civil/social/contencioso/penal/mercantil] |
| Procedimiento | [tipo] |
| Órgano judicial | [nombre y localidad] |
| Nº de autos | [número o "pendiente"] |
| Cuantía | [importe o "indeterminada"] |

### Equipo

| Rol | Nombre | Contacto |
|-----|--------|----------|
| Abogado responsable | [nombre] | [email/tel] |
| Abogado externo | [nombre] | [email/tel] |
| Procurador | [nombre] | [email/tel] |

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
| Tipo de encargo | [igualado / hora / éxito / mixto] |
| Presupuesto estimado | [importe o "por definir"] |
| Provisión de fondos | [importe o "pendiente"] |

### Notas iniciales

[Observaciones del abogado responsable sobre el asunto]
```

## Referencias normativas

- **LEC arts. 399-400**: Requisitos de la demanda (para preparar la futura estrategia).
- **LOPJ art. 11**: Tutela judicial efectiva — plazos de acceso.
- **Código Deontológico de la Abogacía**: arts. sobre conflicto de intereses y deber de diligencia.
- Normativa de protección de datos (RGPD/LOPDGDD): tratamiento de datos de las partes.

## Guardrails

- **NO** abre asuntos en sistemas de gestión del despacho — genera la ficha para que el usuario la introduzca.
- **NO** verifica conflictos de intereses — eso es responsabilidad del despacho.
- **NO** factura ni gestiona provisiones de fondos.
- **NO** contacta a procuradores ni peritos.
- **AVISAR** si faltan datos mínimos obligatorios para completar la ficha.
- **AVISAR** si no se ha asignado abogado responsable.
- **ESCALAR** si el asunto tiene un plazo procesal inminente (< 10 días hábiles).
