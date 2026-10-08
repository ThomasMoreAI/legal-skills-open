---
name: entrevista-inicial-consumo-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu modelo de negocio B2C, tus condiciones generales, tu proceso de aprobación de marketing y tu gestión de reclamaciones de consumo. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/consumo/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: consumer
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — solo recomprobar integraciones. Solo reportar ✓ si una llamada MCP respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego partes específicas).
3. Documentos semilla: condiciones generales, política de devoluciones.
4. Extraer: modelo B2C, condiciones generales, proceso de marketing, reclamaciones.
5. Migración: si existe CLAUDE.md completo en cache pero no en config, copiar y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md`.

---

## Propósito

El derecho de consumo en España es un campo donde el TRLGDCU (Real Decreto Legislativo 1/2007) convive con normativa autonómica, directivas europeas transpuestas y una regulación sectorial intensa. Un ecommerce B2C tiene preocupaciones distintas a un marketplace, y un negocio presencial distinto a uno online. Esta entrevista descubre tu modelo y construye el perfil que necesitas para que cada revisión de condiciones, aprobación de campaña y respuesta a reclamación refleje tu realidad.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → ofrecer retomar.
- **Contiene `[PLACEHOLDER]` sin pausa** → ofrecer empezar o retomar.
- **Completo** → saltar salvo `--repetir`.

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, confirmar y saltar preguntas de empresa. Si no, hacerlas y escribir el perfil compartido.

## Antes de empezar la entrevista

> **`consumo` es para quienes trabajan con consumidores y usuarios — condiciones generales, marketing, reclamaciones, desistimiento y cumplimiento del TRLGDCU.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, modelo de negocio y canales de venta. **15 minutos** añade tus condiciones generales reales, tu proceso de aprobación de marketing, tu gestión de reclamaciones y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica de consumo (modelo de negocio, condiciones generales, proceso de marketing, reclamaciones), plantillas de documentos y checklist de cumplimiento. Aprende cómo trabajas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas del TRLGDCU, LCD, LSSI, normativa autonómica.

---

## La entrevista

### Apertura

> Voy a aprender cómo es tu negocio de cara al consumidor — qué vendes, cómo lo vendes, qué condiciones pones y cómo gestionas las reclamaciones — para que cada revisión y cada documento que prepare encaje con tu modelo.

**Ruta rápida:** solo Parte 0 y Parte 1 (modelo de negocio). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado de consumo, compliance, legal ops.
> 2. **No abogado con acceso a abogado** — marketing, ecommerce manager, atención al cliente con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: plataformas de ecommerce (Shopify, WooCommerce, Prestashop), CRM, herramientas de atención al cliente (Zendesk, Freshdesk), almacenamiento de documentos y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho / consultoría**
> - **In-house (empresa B2C)**
> - **In-house (marketplace / plataforma)**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Modelo de negocio (3-4 min)

> ¿Tienes una descripción del modelo de negocio o la web de la empresa? Pega un enlace o describe el modelo — necesito entender qué vendéis, a quién y cómo.

- **Tipo de relación:**
  - **B2C directo** — vendéis al consumidor final
  - **B2B2C** — vendéis a empresas que revenden al consumidor
  - **Marketplace** — facilitáis transacciones entre vendedores y consumidores
  - **Otro** (describe)
- **Canales de venta:**
  - **Online** (web, app, redes sociales)
  - **Presencial** (tiendas, establecimientos)
  - **Mixto** (omnicanal)
- **¿Qué vendéis?** Bienes, servicios, contenido digital, suscripciones
- **Comunidades autónomas principales donde operáis:** (Esto importa — la normativa de consumo autonómica varía)
- **¿Vendéis a otros países de la UE?** (Esto activa obligaciones adicionales — Directiva Omnibus, Directiva de contenidos digitales)

---

### Parte 2: Condiciones generales (4-5 min)

> ¿Tienes las condiciones generales de contratación actuales? Pega o comparte ruta — las reviso y extraigo las cláusulas clave en vez de preguntarte una a una.

Si no:

- **Plantilla actual:** ¿tenéis condiciones generales redactadas? ¿Cuándo se actualizaron por última vez?
- **Cláusulas sensibles:**
  - **Desistimiento (art. 102 TRLGDCU):** ¿14 días estándar o ampliado? ¿Excepciones aplicadas? ¿Formulario de desistimiento incluido?
  - **Garantías:** ¿3 años (bienes, art. 120 TRLGDCU tras reforma 2022) o 2 años (contenidos/servicios digitales)?
  - **Limitación de responsabilidad:** ¿posición?
  - **Resolución de disputas:** ¿arbitraje de consumo, mediación, tribunales?
  - **Precio y modificaciones:** ¿cómo se comunican cambios de precio en suscripciones?
- **Cumplimiento formal:**
  - ¿Información precontractual completa (art. 97 TRLGDCU)?
  - ¿Botón de pedido con "pedido con obligación de pago" (art. 98 TRLGDCU)?
  - ¿Confirmación de contrato en soporte duradero?
- **¿Quién redactó las condiciones actuales?** (Interno, despacho externo, plantilla)

---

### Parte 3: Marketing (3-4 min)

- **Tipos de claims habituales:**
  - Claims de precio / descuento (cuidado con la Directiva Omnibus — precio anterior 30 días)
  - Claims medioambientales / greenwashing (Directiva de Empowerment del consumidor)
  - Claims de salud (si aplica)
  - Comparativa con competidores (LCD art. 10)
- **Proceso de aprobación de marketing:**
  - ¿Quién aprueba las campañas desde el punto de vista legal? (Jurídico, compliance, externo)
  - ¿Hay checklist de revisión?
  - ¿Plazo habitual de revisión?
- **Influencers y redes sociales:**
  - ¿Trabajáis con influencers? ¿Tenéis contratos tipo?
  - ¿Seguís las guías de Autocontrol sobre publicidad en redes?
  - ¿Cumplís con la obligación de identificar contenido publicitario?
- **Email marketing / comunicaciones comerciales:**
  - ¿Cumplimiento de LSSI (art. 21)? ¿Consentimiento previo?
  - ¿Sistema de baja / opt-out?

---

### Parte 4: Reclamaciones (3-4 min)

- **Hojas de reclamaciones:**
  - ¿Tenéis hojas de reclamaciones disponibles? (Obligatorio en establecimientos presenciales en la mayoría de CCAA)
  - ¿Proceso interno de gestión?
- **Arbitraje de consumo:**
  - ¿Estáis adheridos a la Junta Arbitral de Consumo?
  - ¿En qué ámbito? (Nacional, autonómico, municipal)
  - ¿Límites de adhesión? (Cuantía máxima, materias excluidas)
- **OMIC (Oficinas Municipales de Información al Consumidor):**
  - ¿Habéis tenido mediaciones a través de OMIC?
  - ¿Cómo gestionáis las solicitudes de información de OMIC?
- **Plataforma ODR europea:**
  - ¿Tenéis el enlace en vuestra web? (Obligatorio para comercio electrónico)
- **Volumen de reclamaciones:** ¿cuántas al mes/trimestre?
- **Canal de reclamaciones:** ¿email, formulario web, teléfono, presencial?

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica:
>
> - **Condiciones generales de contratación** actuales
> - **Política de devoluciones / desistimiento** publicada
> - **Plantilla de respuesta a reclamación** (si existe)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

De los documentos, extraer:
- Estructura y estilo de condiciones generales
- Formato de política de devoluciones
- Tono y estilo de respuestas a reclamaciones

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica de consumo
*Escrito por entrevista-inicial el [FECHA].*

### Modelo de negocio

**Tipo:** [PLACEHOLDER — B2C/B2B2C/marketplace]
**Canales:** [PLACEHOLDER — online/presencial/mixto]
**Producto/servicio:** [PLACEHOLDER]
**CCAA principales:** [PLACEHOLDER]
**Venta transfronteriza UE:** [PLACEHOLDER — sí/no]

### Condiciones generales

**Estado actual:** [PLACEHOLDER — vigentes/pendientes de actualización/inexistentes]
**Última actualización:** [PLACEHOLDER]
**Cláusulas clave:**

| Cláusula | Posición actual | Notas |
|---|---|---|
| Desistimiento | [PLACEHOLDER — 14 días/ampliado/excepciones] | |
| Garantías | [PLACEHOLDER — 3 años bienes / 2 años digital] | |
| Resolución de disputas | [PLACEHOLDER] | |
| Precio / modificaciones | [PLACEHOLDER] | |

### Marketing

**Proceso de aprobación:** [PLACEHOLDER]
**Claims habituales:** [PLACEHOLDER]
**Influencers:** [PLACEHOLDER — sí/no, contratos tipo]
**Email marketing:** [PLACEHOLDER — LSSI cumplimiento]

### Reclamaciones

**Volumen:** [PLACEHOLDER — reclamaciones/mes]
**Canal:** [PLACEHOLDER]
**Hojas de reclamaciones:** [PLACEHOLDER — disponibles/no aplica]
**Arbitraje de consumo:** [PLACEHOLDER — adherido/no adherido]
**ODR:** [PLACEHOLDER — enlace publicado/no]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en derecho de consumo:**
>
> - **Revisar condiciones generales** — verifico cumplimiento del TRLGDCU, desistimiento, garantías, información precontractual. Prueba: `/consumo:revision-condiciones`
> - **Aprobar una campaña de marketing** — reviso claims, descuentos, comparativas contra LCD y guías de Autocontrol. Prueba: `/consumo:revision-marketing`
> - **Responder a una reclamación** — con plantilla adaptada al canal y al tipo. Prueba: `/consumo:reclamacion`
> - **Auditar cumplimiento de consumo** — checklist de obligaciones por canal. Prueba: `/consumo:auditoria`
>
> **Mi sugerencia para empezar:** Si tienes condiciones generales pendientes de revisión, ejecuta `/consumo:revision-condiciones` — verás de inmediato si el plugin entiende tu modelo.

Conectar herramienta de investigación:

> "Antes de tu primera revisión: conecta una herramienta de investigación jurídica."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/consumo:entrevista-inicial --repetir` para re-entrevista completa
> - `/consumo:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: las condiciones generales (cuando cambian o se actualiza el TRLGDCU), el proceso de marketing y las posiciones en reclamaciones."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No confundas TRLGDCU con la normativa autonómica.** Cada comunidad autónoma tiene su propia ley de consumo con particularidades (hojas de reclamaciones, sanciones, mediación).
- **No asumas 14 días de desistimiento para todo.** Hay excepciones importantes (art. 103 TRLGDCU): productos personalizados, contenido digital ya descargado, bienes precintados, etc.
- **No olvides la reforma de garantías de 2022.** Bienes ahora tienen 3 años de garantía legal (art. 120 TRLGDCU).
- **No ignores la Directiva Omnibus.** Los descuentos deben mostrar el precio anterior de los últimos 30 días.
- **No escribas condiciones genéricas.** Si el usuario te dio sus condiciones, extrae su estilo y estructura.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. No eres un formulario — eres alguien que quiere entender cómo trabaja el otro para poder ayudar de verdad.
