---
name: entrevista-inicial-betobetico
title: 'Entrevista inicial'
description: Ejecuta la entrevista de configuración inicial del plugin de derecho de familia. Aprende tu práctica y escribe CLAUDE.md a partir de tu tipo de asuntos, posiciones habituales en convenios reguladores y baremos de pensiones. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin de familia", "onboarding familia", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/familia/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: family
language: en
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: convenios reguladores, sentencias de familia, propuestas de medidas.
4. Extraer: tipo de práctica, régimen económico habitual, posiciones en convenios, baremos de pensiones.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/familia:entrevista-inicial
```

```
/familia:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Derecho de Familia

## Propósito

Aprender cómo funciona *esta* práctica de familia — si hace principalmente mutuo acuerdo o contencioso, qué regímenes económicos maneja, cómo estructura convenios reguladores, qué baremos aplica. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica de familia varía mucho según el perfil. Un abogado que tramita divorcios de mutuo acuerdo tiene necesidades distintas a quien litiga custodias contenciosas o a quien trabaja en mediación familiar. Y el régimen económico matrimonial cambia completamente la liquidación: gananciales en territorio común no tiene nada que ver con separación de bienes en Cataluña o el consorcio conyugal aragonés. La entrevista identifica el perfil antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`familia` es para quien gestiona asuntos de derecho de familia: divorcios, separaciones, medidas paterno-filiales, convenios reguladores, liquidaciones de régimen económico, mediación.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el tipo de práctica y los regímenes económicos habituales, con valores sensatos en todo lo demás. **15 minutos** añade tus posiciones habituales en convenios, baremos de pensiones y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica de familia (tipo de asuntos, regímenes económicos, posiciones en convenios, baremos de pensiones). Esta entrevista aprende cómo trabajas realmente — tus asuntos típicos, tus posiciones, tus criterios — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes un convenio regulador tipo? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo del CC (arts. 90-106 sobre efectos del divorcio, arts. 1315 y ss. sobre régimen económico) o de legislación foral, comprobar antes de escribirlo.
- **Sensibilidad especial.** El derecho de familia toca situaciones personales delicadas. Si el usuario es una parte (no un profesional), extremar el cuidado. Si hay violencia de género, señalar recursos y derivar a profesional especializado.

## La entrevista

### Apertura

> Voy a ayudarte con asuntos de familia: divorcios, medidas paterno-filiales, convenios reguladores, liquidaciones de régimen económico. Antes de nada, necesito saber qué tipo de práctica de familia llevas. Diez minutos.
>
> Después te pediré tres cosas: un convenio regulador representativo, una sentencia de familia que consideres buena referencia, y una propuesta de medidas si haces contencioso.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a de familia** — letrado/a especializado en derecho de familia.
> 2. **Profesional con acceso a letrado** — mediador familiar, trabajador social, psicólogo que colabora con abogado/a en asuntos de familia.
> 3. **Profesional sin acceso regular a letrado** — particular gestionando su propio divorcio o asunto de familia.

Si es 2 o 3, explicar: los outputs serán investigación para revisión letrada. En familia los plazos y las consecuencias de los acuerdos son especialmente relevantes — se pausará antes de cualquier paso con consecuencias jurídicas.

Si es 3 y hay indicios de violencia de género: señalar el 016 (teléfono contra la violencia de género), los servicios de orientación jurídica gratuita del colegio de abogados, y el derecho a asistencia jurídica gratuita inmediata (art. 20 LO 1/2004).

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Tipo de práctica (2-3 min)

> **Qué tipo de asuntos de familia gestionas con más frecuencia?** Puedes seleccionar varios:
>
> - **Mutuo acuerdo** — divorcios, separaciones y medidas consensuadas. Volumen mensual?
> - **Contencioso** — divorcios contenciosos, disputas de custodia, modificación de medidas. Volumen?
> - **Mediación familiar** — eres mediador/a o deriváis a mediación? Con qué frecuencia funciona?
> - **Violencia de género** — llevas asuntos con componente de violencia? Juzgados de Violencia sobre la Mujer?
> - **Parejas de hecho** — regulación autonómica aplicable?
> - **Filiación** — reclamaciones/impugnaciones de filiación?
> - **Adopción / acogimiento** — tramitáis adopciones?
> - **Sustracción internacional de menores** (Convenio de La Haya 1980) — experiencia?
>
> Cuál es tu ratio aproximado mutuo acuerdo vs. contencioso?

Pausa. Después:

> **En qué partido judicial trabajas habitualmente?** Juzgados de Primera Instancia / Juzgados de Familia (si los hay especializados en tu ciudad)?
> Los criterios judiciales varían mucho de un juzgado a otro — conocer los tuyos me ayuda a calibrar.

### Parte 2: Régimen económico matrimonial (2-3 min)

> **Qué regímenes económicos matrimoniales ves con más frecuencia?** Esto es fundamental para las liquidaciones.
>
> **Derecho común (Código Civil):**
> - **Sociedad de gananciales** (arts. 1344-1410 CC) — el más habitual en territorio común
> - **Separación de bienes** (arts. 1435-1444 CC) — pactada en capitulaciones
> - **Participación** (arts. 1411-1434 CC) — infrecuente en la práctica
>
> **Derechos forales:**
> - **Cataluña** — separación de bienes como régimen legal supletorio (art. 232-1 CCCat)
> - **Aragón** — consorcio conyugal (arts. 210 y ss. Código del Derecho Foral de Aragón)
> - **Baleares** — varía por isla: separación de bienes en Mallorca y Menorca, diferente en Ibiza-Formentera
> - **Navarra** — régimen de conquistas (Ley 82 del Fuero Nuevo)
> - **País Vasco** — comunicación foral de bienes en tierra llana vizcaína (Ley 5/2015)
> - **Galicia** — gananciales con particularidades (Ley 2/2006)
> - **Valencia** — régimen de separación de bienes (art. 1316 CC tras STC 82/2016)
>
> Cuáles ves tú en tu práctica? Con qué frecuencia te encuentras regímenes forales?
> Gestionas liquidaciones de sociedad de gananciales regularmente?

### Parte 3: Convenio regulador — Posiciones habituales (3-4 min)

> **Si trabajas con convenios reguladores (mutuo acuerdo o contenciosos), necesito conocer tus posiciones habituales.** Esto alimenta los skills de redacción y revisión. Si solo haces contencioso, adaptaremos a propuestas de medidas.
>
> **Custodia:**
> - **Posición habitual** — custodia compartida, exclusiva materna, exclusiva paterna, según caso? Cuál es tu posición por defecto?
> - **Criterios que priorizas** — edad de los menores, distancia entre domicilios, disponibilidad laboral, preferencia del menor (art. 92 CC)?
> - **Distribución del tiempo** — semanas alternas, reparto 5-2-2-5, otro modelo? Cuál propones habitualmente?
> - **Régimen de visitas** para el progenitor no custodio (si custodia exclusiva) — fines de semana alternos + inter-semanal? Vacaciones?
>
> **Vivienda familiar:**
> - **Posición habitual** — atribuir al custodio (art. 96 CC), venta, uso temporal hasta liquidación?
> - **Si custodia compartida** — uso alterno, venta, compensación?
>
> **Pensiones:**
> - **Pensión alimenticia** — cómo la calculas? Usas las tablas orientadoras del CGPJ? Otro método?
> - **Pensión compensatoria** (art. 97 CC) — temporal o indefinida? Qué criterios priorizas? Capitalizas?
> - **Gastos extraordinarios** — cómo los clasificas? Qué lista usas de ordinarios vs. extraordinarios?

Pausa:

> Si tienes un convenio regulador tipo o una propuesta de medidas, pégalo o comparte ruta — aprenderé más de ahí que de las respuestas.

### Parte 4: Baremos y criterios de pensión alimenticia (2 min)

> **Qué criterios y herramientas usas para calcular la pensión alimenticia?**
>
> - **Tablas orientadoras del CGPJ** — las usas como referencia? Las consideran vinculantes tus juzgados habituales?
> - **Criterios del art. 146 CC** — proporción a las necesidades del alimentista y al caudal del alimentante. Cómo lo operativizas?
> - **Mínimo vital** — qué importe consideras mínimo vital en tu plaza?
> - **Gastos de vivienda** — los incluyes en la pensión o los tratas por separado?
>
> **Para la pensión compensatoria (art. 97 CC):**
> - **Criterios que priorizas** — duración del matrimonio, dedicación a la familia, edad, cualificación profesional, estado de salud, patrimonio?
> - **Duración habitual** — temporal (cuántos años sueles proponer?) o indefinida? En qué casos cada una?
> - **Cuantía** — qué porcentaje de la diferencia de ingresos sueles proponer?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Un convenio regulador representativo** — el que mejor refleje cómo trabajas. Aprenderé tu estructura, tu estilo y tus posiciones reales.
>
> 2. **Una sentencia de familia de referencia** — de tus juzgados habituales si es posible. Me enseña los criterios que aplican tus jueces.
>
> 3. **Una propuesta de medidas** — si haces contencioso. Me enseña cómo argumentas y qué pides.

**Cómo leer los documentos semilla:**

**Convenio regulador:** Mapear cada cláusula (custodia, visitas, vivienda, pensión alimenticia, compensatoria, gastos extraordinarios, liquidación de régimen) contra las posiciones declaradas. Deltas son interesantes.

**Sentencia:** Extraer los criterios del juez: cómo valora la custodia compartida, qué peso da a cada factor, cómo calcula las pensiones. Esto calibra las expectativas del plugin para ese juzgado.

**Propuesta de medidas:** Extraer la estructura argumentativa, las peticiones, los fundamentos de derecho. Aprender el estilo.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho de Familia

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] practica derecho de familia en [partido judicial].
Tipo de práctica principal: [mutuo acuerdo / contencioso / mediación / mixto].
El equipo cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a | Profesional con acceso a letrado | Profesional sin acceso a letrado]
**Contacto letrado:** [Nombre / despacho / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Calendario bajo demanda |

---

## Tipo de práctica

| Tipo de asunto | Volumen mensual | Porcentaje aprox. |
|---|---|---|
| Mutuo acuerdo | [número] | [%] |
| Contencioso | [número] | [%] |
| Mediación | [número] | [%] |
| Violencia de género | [número] | [%] |
| Otros (filiación, adopción, etc.) | [número] | [%] |

**Juzgados habituales:** [Juzgado de Primera Instancia / Familia n.o X de [ciudad]]
**Criterios judiciales locales relevantes:** [notas]

---

## Regímenes económicos habituales

| Régimen | Frecuencia | Derecho aplicable | Notas |
|---|---|---|---|
| Gananciales | [frecuencia] | CC arts. 1344-1410 | |
| Separación de bienes | [frecuencia] | CC arts. 1435-1444 / CCCat 232-1 / otro | |
| [foral] | [frecuencia] | [normativa] | |

**Liquidaciones de gananciales:** [frecuencia] gestiones al año
**Conflictos habituales en liquidación:** [tipos]

---

## Posiciones en convenio regulador

### Custodia

| Aspecto | Posición habitual | Notas |
|---|---|---|
| Modalidad por defecto | [compartida / exclusiva / caso a caso] | |
| Distribución tiempo (compartida) | [modelo] | |
| Régimen visitas (exclusiva) | [modelo] | |
| Criterios priorizados | [lista] | |

### Vivienda familiar

| Escenario | Posición | Notas |
|---|---|---|
| Custodia exclusiva | [atribuir al custodio / venta / temporal] | |
| Custodia compartida | [uso alterno / venta / compensación] | |

### Pensiones

| Tipo | Método cálculo | Posición habitual | Notas |
|---|---|---|---|
| Alimenticia | [tablas CGPJ / criterio propio / otro] | [rango habitual] | Mínimo vital: [importe] |
| Compensatoria | [criterio] | [temporal X años / indefinida / según caso] | |

### Gastos extraordinarios

**Clasificación:** [lista de ordinarios vs. extraordinarios que usa el usuario]
**Consentimiento previo:** [posición sobre necesidad de acuerdo previo para extraordinarios]

---

## Baremos y criterios

**Tablas CGPJ:** [las usa / referencia / no las usa]
**Consideración en juzgados habituales:** [vinculantes / orientativas / ignoradas]
**Mínimo vital en plaza:** [importe]
**Pensión compensatoria — duración habitual:** [rango]
**Pensión compensatoria — cuantía habitual:** [criterio]

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Mutuo acuerdo rutinario | [responsable] | [nombre] | Patrimonio > [umbral], menores en riesgo |
| Contencioso custodia | [responsable] | [nombre] | Siempre si hay violencia |
| Violencia de género | — | [especialista + dirección] | Siempre |
| Sustracción internacional | — | [especialista + dirección] | Siempre |
| Liquidación > [cuantía] | [responsable] | [nombre] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Convenio regulador | [ruta] | [fecha] | [tipo] |
| Sentencia de referencia | [ruta] | [fecha] | [juzgado] |
| Propuesta de medidas | [ruta] | [fecha] | [tipo asunto] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/familia:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Las posiciones en convenio y los baremos de pensiones son las partes a revisar con más cuidado — un cálculo de pensión con criterios incorrectos propaga el error a todos los convenios."

2. **Proponer primeras tareas:**
   - "Quieres que redacte un convenio regulador para un caso concreto?"
   - "Quieres que calcule una pensión alimenticia con las tablas CGPJ?"
   - "Quieres que revise un convenio regulador contra tus posiciones habituales?"
   - Si hace contencioso: "Quieres que redacte una propuesta de medidas para un caso?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/familia:entrevista-inicial --redo` para re-entrevista completa
   > - `/familia:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: las **posiciones en convenio** (según la jurisprudencia de tus juzgados evoluciona), los **baremos de pensiones** (las tablas CGPJ se actualizan), y el **régimen económico** (según cambia la normativa foral o la composición de tu cartera de clientes)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir gananciales.** En Cataluña el régimen legal supletorio es separación de bienes. En Aragón es el consorcio conyugal. En Baleares varía por isla. Preguntar siempre dónde se celebró el matrimonio y si hay capitulaciones.
- **No aplicar derecho común a territorio foral.** Las normas sobre régimen económico, legítimas, pactos sucesorios y otras instituciones son completamente distintas en cada derecho foral. Un convenio regulador con liquidación de gananciales en Cataluña es un error.
- **No dar por hecho que las tablas CGPJ son vinculantes.** Son orientadoras. Muchos juzgados no las aplican o las aplican con criterios propios. Preguntar siempre los criterios del juzgado habitual del usuario.
- **No ignorar la violencia de género.** Si hay indicios, el asunto cambia completamente de naturaleza jurídica (Juzgados de Violencia sobre la Mujer, medidas del art. 544 ter LECrim, orden de protección). No tratar como un divorcio ordinario.
- **No escribir posiciones genéricas en convenios.** Si el usuario no ha tramitado muchos divorcios, decirlo: `[POSICIONES NO CONSOLIDADAS — poca experiencia en convenios. Tratar como puntos de partida.]`
- **No olvidar el interés superior del menor.** En todo lo que afecte a menores, el criterio rector es el interés superior del menor (art. 2 LOPJM). Esto prevalece sobre las posiciones de las partes y sobre cualquier default del plugin.
- **No confundir pensión alimenticia con compensatoria.** La alimenticia es para los hijos (arts. 142-153 CC, irrenunciable); la compensatoria es entre cónyuges (art. 97 CC, disponible). Diferentes fundamentos, diferentes criterios, diferentes consecuencias de impago.
- **No ignorar la compensación por trabajo doméstico (art. 1438 CC / equivalentes forales).** En separación de bienes, el cónyuge que se dedicó al hogar tiene derecho a compensación. Es una cuestión que muchos olvidan y que los juzgados cada vez valoran más.
