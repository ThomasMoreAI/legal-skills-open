---
name: burofax-betobetico
title: Propósito
description: Redacta un requerimiento extrajudicial de cese por infracción de PI calibrado a la postura de enforcement
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/propiedad-intelectual/skills/burofax
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

## Propósito

Esta skill redacta una carta de requerimiento extrajudicial (cease & desist) por infracción de propiedad intelectual o industrial. El tono y contenido se calibran según la postura de enforcement configurada por el despacho. Nunca envía el documento — lo presenta como borrador para revisión.

## Instrucciones

### Paso 1 — Identificar tipo de infracción

1. **Infracción de marca**: uso no autorizado de marca registrada (Ley 35 de 1996 — derechos del titular; acción civil y medidas cautelares, arts. 167-172; prescribe a los 6 años, art. 168).
2. **Infracción de derechos de autor**: reproducción, distribución o comunicación pública sin autorización (Ley 64 de 2012).
3. **Competencia desleal**: imitación, aprovechamiento de reputación ajena, confusión (Ley 45 de 2007). Estos actos se ventilan ante los Juzgados de Circuito Civil especializados (art. 124.5 de la Ley 45 de 2007), mediante acción privada del comerciante afectado; la ACODECO solo conoce prácticas monopolísticas.
4. **Infracción de patente/diseño**: fabricación o comercialización sin licencia (Ley 35 de 1996).

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

### Paso 4 — Redactar el requerimiento

## Formato de salida

```markdown
## BORRADOR DE REQUERIMIENTO EXTRAJUDICIAL — Pendiente de revisión y aprobación

**Estado:** BORRADOR — NO ENVIAR sin aprobación del abogado responsable

---

**REMITENTE:**
[Nombre/denominación del titular de derechos]
[Dirección]
[Cédula / RUC]

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

- **Ley 35 de 1996** (propiedad industrial, mod. Ley 61 de 2012): derechos del titular de la marca y acciones por infracción — cese, indemnización, medidas para evitar la repetición, publicación de la sentencia y medidas cautelares inmediatas (arts. 167-172); la acción prescribe a los 6 años (art. 168). Medidas en frontera por la Aduana, incluida la Zona Libre de Colón (arts. 176-177; caución de hasta el 50% del avalúo, art. 171).
- **Ley 64 de 2012** (derecho de autor): acciones por infracción de derechos de autor y derechos conexos.
- **Ley 45 de 2007** (protección al consumidor y defensa de la competencia): actos de competencia desleal ante los Juzgados de Circuito Civil especializados (art. 124.5), por acción privada del afectado; la ACODECO solo conoce prácticas monopolísticas.
- **Ley 35 de 1996** (patentes y diseños): infracción y acciones disponibles. Las acciones civiles de PI se tramitan ante los Juzgados de Circuito Civil especializados (Ley 45 de 2007, arts. 124 y 127; definición de los procesos de propiedad industrial en el art. 181 de la Ley 35 de 1996).
- **Código Penal de Panamá**: falsificación de marca (art. 268, prisión 4-6 años); piratería de derecho de autor (arts. 262-266); delitos contra la propiedad industrial (arts. 267-273). Dimensión penal ante la Fiscalía Superior Especializada en PI.
- **Código Judicial de Panamá**: procedimiento aplicable a las acciones civiles por infracción de PI.

## Guardrails

- **NO envía** el requerimiento — siempre lo presenta como borrador para aprobación.
- **NO constituye** asesoramiento jurídico — es una herramienta de redacción asistida.
- **NO afirma** que existe infracción — usa lenguaje condicional ("presunta infracción").
- **NO amenaza** con acciones penales salvo instrucción expresa del abogado.
- **NO incluye** cuantificación de daños salvo que el usuario proporcione datos verificados.
- **ESCALAR** si la infracción puede tener dimensión penal: falsificación de marca (art. 268 del Código Penal), piratería de derecho de autor (arts. 262-266) y demás delitos contra la propiedad industrial (arts. 267-273).
- **ESCALAR** si el presunto infractor es un competidor directo o empresa de mayor tamaño.
- **AVISAR** si no se dispone de pruebas documentadas de la infracción.
