---
name: burofax-667-betobetico
title: Propósito
description: Redacta burofax o requerimiento de cese por infracción de PI calibrado a la postura de enforcement
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/burofax
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

## Propósito

Esta skill redacta un burofax o carta de requerimiento (cease & desist) por infracción de propiedad intelectual o industrial. El tono y contenido se calibran según la postura de enforcement configurada por el despacho. Nunca envía el documento — lo presenta como borrador para revisión.

## Instrucciones

### Paso 1 — Identificar tipo de infracción

1. **Infracción de marca**: uso no autorizado de marca registrada (arts. 34-36 Ley de Marcas).
2. **Infracción de derechos de autor**: reproducción, distribución o comunicación pública sin autorización (arts. 17-23 LPI).
3. **Competencia desleal**: imitación, aprovechamiento de reputación ajena, confusión (LCD arts. 5-18).
4. **Infracción de patente/diseño**: fabricación o comercialización sin licencia.

### Paso 2 — Cargar postura de enforcement

Leer desde `~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md`:

- **Agresiva**: exigencia firme de cese inmediato, reserva expresa de acciones judiciales, plazo corto (7-10 días).
- **Moderada**: requerimiento formal con apertura a solución negociada, plazo estándar (15-20 días).
- **Conciliatoria**: comunicación inicial buscando acuerdo, posibilidad de licencia, plazo amplio (30 días).

Si no hay configuración, usar postura **moderada** por defecto.

### Paso 3 — Recopilar hechos

- Descripción de la infracción detectada.
- Pruebas disponibles (capturas, URLs, productos, publicidad).
- Derechos del titular (registros, fecha, territorio).
- Datos del infractor (si se conocen).
- Daños estimados o perjuicios.

### Paso 4 — Redactar burofax

## Formato de salida

```markdown
## BORRADOR DE BUROFAX — Pendiente de revisión y aprobación

**Estado:** BORRADOR — NO ENVIAR sin aprobación del abogado responsable

---

**REMITENTE:**
[Nombre/denominación del titular de derechos]
[Dirección]
[CIF/NIF]

**DESTINATARIO:**
[Nombre/denominación del presunto infractor]
[Dirección]

**FECHA:** [fecha]

**ASUNTO:** Requerimiento de cese por infracción de [tipo de derecho]

---

Muy Sr./Sra. nuestro/a:

[Párrafo 1: Identificación del remitente y sus derechos — registro, fecha, territorio]

[Párrafo 2: Descripción de la infracción detectada — hechos concretos]

[Párrafo 3: Fundamentación jurídica — artículos aplicables]

[Párrafo 4: Requerimiento de cese — acciones exigidas, plazo]

[Párrafo 5: Consecuencias del incumplimiento — reserva de acciones]

[Párrafo 6 (si postura conciliatoria): Apertura a negociación/licencia]

Sin otro particular, le saluda atentamente,

[Firma]

---

**NOTA INTERNA:** Postura aplicada: [agresiva/moderada/conciliatoria]
```

## Referencias normativas

- **Ley de Marcas 17/2001**: arts. 34-36 (derechos del titular), art. 40-44 (acciones civiles).
- **LPI** (RDL 1/1996): arts. 138-143 (acciones por infracción de derechos de autor).
- **LCD** (Ley 3/1991): arts. 5-18 (actos de competencia desleal), arts. 32-36 (acciones).
- **Ley de Patentes 24/2015**: arts. 61-67 (infracción), arts. 70-77 (acciones).
- **LEC**: arts. 249-250 (procedimiento aplicable según cuantía).

## Guardrails

- **NO envía** el burofax — siempre lo presenta como borrador para aprobación.
- **NO constituye** asesoramiento jurídico — es una herramienta de redacción asistida.
- **NO afirma** que existe infracción — usa lenguaje condicional ("presunta infracción").
- **NO amenaza** con acciones penales salvo instrucción expresa del abogado.
- **NO incluye** cuantificación de daños salvo que el usuario proporcione datos verificados.
- **ESCALAR** si la infracción puede tener dimensión penal (falsificación, art. 274 CP).
- **ESCALAR** si el presunto infractor es un competidor directo o empresa de mayor tamaño.
- **AVISAR** si no se dispone de pruebas documentadas de la infracción.
