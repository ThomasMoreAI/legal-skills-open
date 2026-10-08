---
name: entrevista-inicial-consumo-3335-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu modelo de negocio B2C, tus condiciones generales, tu proceso de aprobación de marketing y tu gestión de reclamaciones de consumo bajo la Ley 45 de 2007. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/consumo/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

El derecho de consumo en Panamá tiene como norma central la Ley 45 de 2007, aplicada por la ACODECO, y convive con el Código de Comercio y una regulación sectorial intensa. Un ecommerce B2C tiene preocupaciones distintas a un marketplace, y un negocio presencial distinto a uno online. Esta entrevista descubre tu modelo y construye el perfil que necesitas para que cada revisión de condiciones, aprobación de campaña y respuesta a reclamación refleje tu realidad.

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

> **`consumo` es para quienes trabajan con consumidores y usuarios — condiciones generales, marketing, reclamaciones, retracto y cumplimiento de la Ley 45 de 2007.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, modelo de negocio y canales de venta. **15 minutos** añade tus condiciones generales reales, tu proceso de aprobación de marketing, tu gestión de reclamaciones y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica de consumo en Panamá (modelo de negocio, condiciones generales, proceso de marketing, reclamaciones), plantillas de documentos y checklist de cumplimiento de la Ley 45 de 2007. Aprende cómo trabajas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas de la Ley 45 de 2007, reglamentación de la ACODECO y Código de Comercio.

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
- **Provincias principales donde operáis:** (Relevante por la jurisdicción de las oficinas regionales de la ACODECO)
- **¿Operáis en zonas económicas especiales?** (Zona Libre de Colón, Ciudad del Saber, Panamá Pacífico — pueden activar reglas específicas) [verificar]
- **¿Vendéis a otros países (exportación / venta transfronteriza)?** (Puede activar obligaciones adicionales)

---

### Parte 2: Condiciones generales (4-5 min)

> ¿Tienes las condiciones generales de contratación actuales? Pega o comparte ruta — las reviso y extraigo las cláusulas clave en vez de preguntarte una a una.

Si no:

- **Plantilla actual:** ¿tenéis condiciones generales redactadas? ¿Cuándo se actualizaron por última vez?
- **Cláusulas sensibles:**
  - **Retracto (Ley 45 de 2007):** ¿plazo legal estándar o ampliado? ¿Excepciones aplicadas? ¿Mecanismo de retracto incluido?
  - **Garantías (Ley 45 de 2007):** ¿plazo de garantía legal de bienes y de contenidos/servicios digitales?
  - **Limitación de responsabilidad:** ¿posición?
  - **Resolución de disputas:** ¿conciliación/arbitraje ante la ACODECO, mediación, tribunales?
  - **Precio y modificaciones:** ¿cómo se comunican cambios de precio en suscripciones?
- **Cumplimiento formal:**
  - ¿Información al consumidor completa (Ley 45 de 2007)?
  - ¿Confirmación clara del pedido con obligación de pago? [verificar]
  - ¿Confirmación de contrato en soporte duradero?
- **¿Quién redactó las condiciones actuales?** (Interno, despacho externo, plantilla)

---

### Parte 3: Marketing (3-4 min)

- **Tipos de claims habituales:**
  - Claims de precio / descuento (el precio anterior anunciado debe ser real, Ley 45 de 2007)
  - Claims medioambientales / greenwashing
  - Claims de salud (si aplica)
  - Comparativa con competidores (Ley 45 de 2007)
- **Proceso de aprobación de marketing:**
  - ¿Quién aprueba las campañas desde el punto de vista legal? (Jurídico, compliance, externo)
  - ¿Hay checklist de revisión?
  - ¿Plazo habitual de revisión?
- **Influencers y redes sociales:**
  - ¿Trabajáis con influencers? ¿Tenéis contratos tipo?
  - ¿Seguís buenas prácticas de identificación de publicidad en redes?
  - ¿Cumplís con la obligación de identificar contenido publicitario? (Ley 45 de 2007)
- **Email marketing / comunicaciones comerciales:**
  - ¿Consentimiento previo del consumidor? ¿Tratamiento de datos conforme a la Ley 81 de 2019?
  - ¿Sistema de baja / opt-out?

---

### Parte 4: Reclamaciones (3-4 min)

- **Libro de quejas / canal de reclamaciones:**
  - ¿Tenéis un canal de reclamaciones disponible en establecimientos presenciales? [verificar]
  - ¿Proceso interno de gestión?
- **Conciliación / arbitraje de consumo ante la ACODECO:**
  - ¿Participáis en la conciliación o el arbitraje de la ACODECO?
  - ¿En qué ámbito? (Oficina central / oficinas regionales)
  - ¿Límites? (Cuantía máxima, materias excluidas)
- **ACODECO (denuncias y mediaciones):**
  - ¿Habéis tenido mediaciones o denuncias ante la ACODECO?
  - ¿Cómo gestionáis las solicitudes de información de la ACODECO?
- **Sectores regulados:**
  - Si vendéis servicios financieros o sujetos a otra autoridad (Superintendencia de Bancos, etc.), ¿lo tenéis identificado?
- **Volumen de reclamaciones:** ¿cuántas al mes/trimestre?
- **Canal de reclamaciones:** ¿email, formulario web, teléfono, presencial?

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica:
>
> - **Condiciones generales de contratación** actuales
> - **Política de devoluciones / retracto** publicada
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
**Provincias principales:** [PLACEHOLDER]
**Zonas económicas especiales:** [PLACEHOLDER — sí/no, cuáles]
**Venta transfronteriza / exportación:** [PLACEHOLDER — sí/no]

### Condiciones generales

**Estado actual:** [PLACEHOLDER — vigentes/pendientes de actualización/inexistentes]
**Última actualización:** [PLACEHOLDER]
**Cláusulas clave:**

| Cláusula | Posición actual | Notas |
|---|---|---|
| Retracto | [PLACEHOLDER — plazo legal/ampliado/excepciones] [verificar] | |
| Garantías | [PLACEHOLDER — plazo legal bienes / digital] [verificar] | |
| Resolución de disputas | [PLACEHOLDER] | |
| Precio / modificaciones | [PLACEHOLDER] | |

### Marketing

**Proceso de aprobación:** [PLACEHOLDER]
**Claims habituales:** [PLACEHOLDER]
**Influencers:** [PLACEHOLDER — sí/no, contratos tipo]
**Email marketing:** [PLACEHOLDER — consentimiento / Ley 81 de 2019]

### Reclamaciones

**Volumen:** [PLACEHOLDER — reclamaciones/mes]
**Canal:** [PLACEHOLDER]
**Libro de quejas / canal de reclamaciones:** [PLACEHOLDER — disponible/no aplica]
**Conciliación / arbitraje ACODECO:** [PLACEHOLDER — participa/no participa]
**Denuncias ACODECO:** [PLACEHOLDER — historial/no]

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
> - **Revisar condiciones generales** — verifico cumplimiento de la Ley 45 de 2007, retracto, garantías, información al consumidor. Prueba: `/consumo:condiciones-generales`
> - **Aprobar una campaña de marketing** — reviso claims, descuentos y comparativas contra la Ley 45 de 2007. Prueba: `/consumo:claims`
> - **Revisar un lanzamiento** — checklist de cumplimiento antes de comercializar. Prueba: `/consumo:lanzamiento`
> - **Consulta rápida de consumo** — semáforo VERDE/AMARILLO/ROJO con fundamento. Prueba: `/consumo:consulta`
>
> **Mi sugerencia para empezar:** Si tienes condiciones generales pendientes de revisión, ejecuta `/consumo:condiciones-generales` — verás de inmediato si el plugin entiende tu modelo.

Conectar herramienta de investigación:

> "Antes de tu primera revisión: conecta una herramienta de investigación jurídica."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/consumo:entrevista-inicial --repetir` para re-entrevista completa
> - `/consumo:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: las condiciones generales (cuando cambian o se actualiza la Ley 45 de 2007 o su reglamentación), el proceso de marketing y las posiciones en reclamaciones."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No confundas la Ley 45 de 2007 con la regulación sectorial.** Servicios financieros, telecomunicaciones, salud y energía pueden tener autoridades y reglas propias además de la ACODECO.
- **No asumas un plazo único de retracto para todo.** Hay excepciones importantes [verificar]: productos personalizados, contenido digital ya descargado, bienes precintados, etc.
- **Verifica siempre el plazo y el régimen de garantía legal** conforme a la Ley 45 de 2007 antes de afirmar una cifra concreta [verificar].
- **No anuncies descuentos con un precio de referencia falso.** El precio anterior anunciado debe ser real y haber estado vigente (Ley 45 de 2007).
- **No escribas condiciones genéricas.** Si el usuario te dio sus condiciones, extrae su estilo y estructura.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. No eres un formulario — eres alguien que quiere entender cómo trabaja el otro para poder ayudar de verdad.
