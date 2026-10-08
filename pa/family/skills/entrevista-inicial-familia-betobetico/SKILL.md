---
name: entrevista-inicial-familia-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin de derecho de familia. Aprende tu práctica y escribe CLAUDE.md a partir de tu tipo de asuntos, posiciones habituales en convenios de divorcio y criterios de pensiones. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin de familia", "onboarding familia", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/familia/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: family
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: convenios de divorcio, sentencias de familia, propuestas de medidas.
4. Extraer: tipo de práctica, régimen patrimonial habitual, posiciones en convenios, criterios de pensiones.
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

Aprender cómo funciona *esta* práctica de familia — si hace principalmente divorcios por mutuo consentimiento o contenciosos, qué regímenes patrimoniales maneja, cómo estructura convenios de divorcio, qué criterios aplica a las pensiones. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica de familia varía mucho según el perfil. Un abogado que tramita divorcios por mutuo consentimiento tiene necesidades distintas a quien litiga guardas contenciosas o a quien trabaja en mediación familiar. Y el régimen patrimonial del matrimonio cambia completamente la liquidación: la sociedad de gananciales no tiene nada que ver con la separación de bienes o con la participación en las ganancias. La entrevista identifica el perfil antes de nada.

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

> **`familia` es para quien gestiona asuntos de derecho de familia: divorcios, separaciones, procesos de guarda y crianza, convenios de divorcio, liquidaciones de régimen patrimonial, mediación.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el tipo de práctica y los regímenes patrimoniales habituales, con valores sensatos en todo lo demás. **15 minutos** añade tus posiciones habituales en convenios, criterios de pensiones y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica de familia (tipo de asuntos, regímenes patrimoniales, posiciones en convenios, criterios de pensiones). Esta entrevista aprende cómo trabajas realmente — tus asuntos típicos, tus posiciones, tus criterios — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes un convenio de divorcio tipo? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo del Código de la Familia (efectos del divorcio, régimen patrimonial, alimentos, guarda y crianza), comprobar antes de escribirlo.
- **Sensibilidad especial.** El derecho de familia toca situaciones personales delicadas. Si el usuario es una parte (no un profesional), extremar el cuidado. Si hay violencia doméstica, señalar recursos y derivar a profesional especializado.

## La entrevista

### Apertura

> Voy a ayudarte con asuntos de familia: divorcios, procesos de guarda y crianza, convenios de divorcio, liquidaciones de régimen patrimonial. Antes de nada, necesito saber qué tipo de práctica de familia llevas. Diez minutos.
>
> Después te pediré tres cosas: un convenio de divorcio representativo, una sentencia de familia que consideres buena referencia, y una propuesta de medidas si haces contencioso.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a de familia** — abogado/a idóneo/a especializado en derecho de familia.
> 2. **Profesional con acceso a abogado** — mediador familiar, trabajador social, psicólogo que colabora con abogado/a en asuntos de familia.
> 3. **Profesional sin acceso regular a abogado** — particular gestionando su propio divorcio o asunto de familia.

Si es 2 o 3, explicar: los outputs serán investigación para revisión de abogado idóneo. En familia los plazos y las consecuencias de los acuerdos son especialmente relevantes — se pausará antes de cualquier paso con consecuencias jurídicas.

Si es 3 y hay indicios de violencia doméstica: señalar la línea de atención del Ministerio de Desarrollo Social / Instituto Nacional de la Mujer (INAMU) [verificar], y los servicios de orientación jurídica gratuita (defensoría / consultorios jurídicos).

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Tipo de práctica (2-3 min)

> **Qué tipo de asuntos de familia gestionas con más frecuencia?** Puedes seleccionar varios:
>
> - **Mutuo consentimiento** — divorcios, separaciones y medidas consensuadas. Volumen mensual?
> - **Contencioso** — divorcios por causal, disputas de guarda, modificación de medidas. Volumen?
> - **Mediación familiar** — eres mediador/a o derivas a mediación? Con qué frecuencia funciona?
> - **Violencia doméstica** — llevas asuntos con componente de violencia? (Ley 82 de 2013 sobre femicidio y violencia contra la mujer [verificar])
> - **Uniones de hecho** — reconocimiento de uniones de hecho conforme al Código de la Familia?
> - **Filiación** — reclamaciones/impugnaciones de paternidad?
> - **Adopción** — tramitas adopciones (Ley 46 de 2013)?
> - **Sustracción internacional de menores** (Convenio de La Haya 1980) — experiencia?
>
> Cuál es tu ratio aproximado mutuo consentimiento vs. contencioso?

Pausa. Después:

> **En qué circuito / juzgado seccional de familia trabajas habitualmente?** (p. ej. juzgados seccionales de familia de Panamá, San Miguelito, Colón, Chiriquí)?
> Los criterios judiciales varían de un juzgado a otro — conocer los tuyos me ayuda a calibrar.

### Parte 2: Régimen patrimonial del matrimonio (2-3 min)

> **Qué regímenes patrimoniales del matrimonio ves con más frecuencia?** Esto es fundamental para las liquidaciones.
>
> Bajo el Código de la Familia de Panamá:
> - **Sociedad de gananciales** — bienes comunes los adquiridos a título oneroso durante el matrimonio [verificar arts.]
> - **Separación de bienes** — pactada en capitulaciones; cada cónyuge conserva sus bienes [verificar arts.]
> - **Participación en las ganancias** — cada cónyuge participa en las ganancias del otro a la disolución [verificar arts.]
>
> Importante: el **régimen legal supletorio** (a falta de capitulaciones) lo fija el Código de la Familia — confírmalo según la fecha del matrimonio. [verificar]
>
> Cuáles ves tú en tu práctica? Gestionas liquidaciones de sociedad de gananciales regularmente?
> Ves matrimonios con elemento internacional (cónyuge extranjero, celebración fuera de Panamá)?

### Parte 3: Convenio de divorcio — Posiciones habituales (3-4 min)

> **Si trabajas con convenios de divorcio (mutuo consentimiento o contenciosos), necesito conocer tus posiciones habituales.** Esto alimenta los skills de redacción y revisión. Si solo haces contencioso, adaptaremos a propuestas de medidas.
>
> **Guarda y crianza:**
> - **Posición habitual** — guarda compartida, exclusiva materna, exclusiva paterna, según caso? Cuál es tu posición por defecto?
> - **Criterios que priorizas** — edad de los menores, distancia entre domicilios, disponibilidad laboral, opinión del menor?
> - **Distribución del tiempo** — semanas alternas, reparto 5-2-2-5, otro modelo? Cuál propones habitualmente?
> - **Régimen de comunicación y visitas** para el progenitor no guardador (si guarda exclusiva) — fines de semana alternos + intersemanal? Vacaciones escolares?
>
> **Vivienda familiar:**
> - **Posición habitual** — atribuir al guardador, venta, uso temporal hasta liquidación?
> - **Si guarda compartida** — uso alterno, venta, compensación?
>
> **Pensiones:**
> - **Pensión alimenticia a los hijos** — cómo la calculas? Qué criterios de proporcionalidad aplicas?
> - **Pensión alimenticia entre cónyuges** — temporal o indefinida? Qué criterios priorizas?
> - **Gastos extraordinarios** — cómo los clasificas? Qué lista usas de ordinarios vs. extraordinarios?

Pausa:

> Si tienes un convenio de divorcio tipo o una propuesta de medidas, pégalo o comparte ruta — aprenderé más de ahí que de las respuestas.

### Parte 4: Criterios de pensión alimenticia (2 min)

> **Qué criterios usas para calcular la pensión alimenticia a los hijos?**
>
> - **Principio de proporcionalidad** — proporción a las necesidades del alimentista y al caudal del alimentante. Cómo lo operativizas? [verificar art. del Código de la Familia]
> - **Mínimo de subsistencia** — qué importe consideras mínimo en tu plaza, en balboas (B/.)?
> - **Gastos de vivienda** — los incluyes en la pensión o los tratas por separado?
>
> **Para la pensión alimenticia entre cónyuges:**
> - **Criterios que priorizas** — duración del matrimonio, dedicación a la familia, edad, cualificación profesional, estado de salud, patrimonio?
> - **Duración habitual** — temporal (cuántos años sueles proponer?) o indefinida? En qué casos cada una?
> - **Cuantía** — qué porcentaje de la diferencia de ingresos sueles proponer?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Un convenio de divorcio representativo** — el que mejor refleje cómo trabajas. Aprenderé tu estructura, tu estilo y tus posiciones reales.
>
> 2. **Una sentencia de familia de referencia** — de tus juzgados habituales si es posible. Me enseña los criterios que aplican tus jueces.
>
> 3. **Una propuesta de medidas** — si haces contencioso. Me enseña cómo argumentas y qué pides.

**Cómo leer los documentos semilla:**

**Convenio de divorcio:** Mapear cada cláusula (guarda, comunicación y visitas, vivienda, pensión a los hijos, pensión entre cónyuges, gastos extraordinarios, liquidación de régimen) contra las posiciones declaradas. Deltas son interesantes.

**Sentencia:** Extraer los criterios del juez: cómo valora la guarda compartida, qué peso da a cada factor, cómo calcula las pensiones. Esto calibra las expectativas del plugin para ese juzgado.

**Propuesta de medidas:** Extraer la estructura argumentativa, las peticiones, los fundamentos de derecho. Aprender el estilo.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho de Familia

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Firma] practica derecho de familia en [circuito / juzgado seccional].
Tipo de práctica principal: [mutuo consentimiento / contencioso / mediación / mixto].
El equipo cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a | Profesional con acceso a abogado | Profesional sin acceso a abogado]
**Contacto de abogado idóneo:** [Nombre / firma / N/A]

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
| Mutuo consentimiento | [número] | [%] |
| Contencioso | [número] | [%] |
| Mediación | [número] | [%] |
| Violencia doméstica | [número] | [%] |
| Otros (filiación, adopción, etc.) | [número] | [%] |

**Juzgados habituales:** [Juzgado Seccional de Familia n.o X de [ciudad/circuito]]
**Criterios judiciales locales relevantes:** [notas]

---

## Regímenes patrimoniales habituales

| Régimen | Frecuencia | Base legal | Notas |
|---|---|---|---|
| Sociedad de gananciales | [frecuencia] | Código de la Familia [verificar arts.] | |
| Separación de bienes | [frecuencia] | Código de la Familia [verificar arts.] | |
| Participación en las ganancias | [frecuencia] | Código de la Familia [verificar arts.] | |

**Liquidaciones de gananciales:** [frecuencia] gestiones al año
**Conflictos habituales en liquidación:** [tipos]

---

## Posiciones en convenio de divorcio

### Guarda y crianza

| Aspecto | Posición habitual | Notas |
|---|---|---|
| Modalidad por defecto | [compartida / exclusiva / caso a caso] | |
| Distribución tiempo (compartida) | [modelo] | |
| Régimen comunicación/visitas (exclusiva) | [modelo] | |
| Criterios priorizados | [lista] | |

### Vivienda familiar

| Escenario | Posición | Notas |
|---|---|---|
| Guarda exclusiva | [atribuir al guardador / venta / temporal] | |
| Guarda compartida | [uso alterno / venta / compensación] | |

### Pensiones

| Tipo | Método cálculo | Posición habitual | Notas |
|---|---|---|---|
| A los hijos | [proporcionalidad / criterio propio] | [rango habitual en B/.] | Mínimo de subsistencia: [importe] |
| Entre cónyuges | [criterio] | [temporal X años / indefinida / según caso] | |

### Gastos extraordinarios

**Clasificación:** [lista de ordinarios vs. extraordinarios que usa el usuario]
**Consentimiento previo:** [posición sobre necesidad de acuerdo previo para extraordinarios]

---

## Criterios de pensión

**Método de cálculo:** [proporcionalidad / criterio propio]
**Consideración en juzgados habituales:** [notas]
**Mínimo de subsistencia en plaza:** [importe en B/.]
**Pensión entre cónyuges — duración habitual:** [rango]
**Pensión entre cónyuges — cuantía habitual:** [criterio]

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Mutuo consentimiento rutinario | [responsable] | [nombre] | Patrimonio > [umbral en B/.], menores en riesgo |
| Contencioso guarda | [responsable] | [nombre] | Siempre si hay violencia |
| Violencia doméstica | — | [especialista + dirección] | Siempre |
| Sustracción internacional | — | [especialista + dirección] | Siempre |
| Liquidación > [cuantía en B/.] | [responsable] | [nombre] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Convenio de divorcio | [ruta] | [fecha] | [tipo] |
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

1. **Mostrar el resumen.** "Esto es lo que he entendido. Las posiciones en convenio y los criterios de pensiones son las partes a revisar con más cuidado — un cálculo de pensión con criterios incorrectos propaga el error a todos los convenios."

2. **Proponer primeras tareas:**
   - "Quieres que redacte un convenio de divorcio para un caso concreto?"
   - "Quieres que calcule una pensión alimenticia según el criterio de proporcionalidad?"
   - "Quieres que revise un convenio de divorcio contra tus posiciones habituales?"
   - Si hace contencioso: "Quieres que redacte una propuesta de medidas para un caso?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/familia:entrevista-inicial --redo` para re-entrevista completa
   > - `/familia:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: las **posiciones en convenio** (según la jurisprudencia de tus juzgados evoluciona), los **criterios de pensiones**, y el **régimen patrimonial** (según cambia la normativa o la composición de tu cartera de clientes)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir gananciales.** Verificar siempre si hay capitulaciones matrimoniales y cuál es el régimen legal supletorio vigente al momento del matrimonio según el Código de la Familia.
- **Confirmar el régimen legal supletorio.** No darlo por sentado: depende del Código de la Familia y de la fecha del matrimonio. [verificar]
- **No dar por hecho criterios de pensión vinculantes.** En Panamá no hay tablas oficiales; la cuantía se fija por proporcionalidad. Preguntar siempre los criterios del juzgado habitual del usuario.
- **No ignorar la violencia doméstica.** Si hay indicios, el asunto cambia completamente de naturaleza jurídica (medidas de protección, Ley 82 de 2013). No tratar como un divorcio ordinario.
- **No escribir posiciones genéricas en convenios.** Si el usuario no ha tramitado muchos divorcios, decirlo: `[POSICIONES NO CONSOLIDADAS — poca experiencia en convenios. Tratar como puntos de partida.]`
- **No olvidar el interés superior del menor.** En todo lo que afecte a menores, el criterio rector es el interés superior del menor (principio del Código de la Familia). Esto prevalece sobre las posiciones de las partes y sobre cualquier default del plugin.
- **No confundir pensión a los hijos con pensión entre cónyuges.** La de los hijos es irrenunciable; la pensión entre cónyuges es disponible. Diferentes fundamentos, diferentes criterios, diferentes consecuencias de impago.
- **No olvidar la compensación por trabajo doméstico.** En separación de bienes, el cónyuge que se dedicó al hogar puede tener derecho a compensación. [verificar base legal en el Código de la Familia]
