---
name: entrevista-inicial-administrativo-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin de derecho administrativo. Aprende tu práctica y escribe CLAUDE.md a partir de tus procedimientos habituales, experiencia en contratación pública y contencioso-administrativo. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin administrativo", "onboarding administrativo", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/administrativo/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: administrative
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: resoluciones administrativas, pliegos de contratación, recursos recientes.
4. Extraer: relación con administraciones, tipos de procedimiento, experiencia en contratación pública, asuntos contenciosos.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/administrativo:entrevista-inicial
```

```
/administrativo:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Derecho Administrativo

## Propósito

Aprender cómo funciona *esta* práctica de derecho administrativo — con qué administraciones se relaciona, qué procedimientos gestiona, si hace contratación pública, qué contenciosos lleva. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

El derecho administrativo en España es enormemente amplio. Un abogado que gestiona licencias urbanísticas tiene poco en común con uno que impugna sanciones de la CNMC o que licita contratos públicos. La entrevista identifica el perfil antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`administrativo` es para quien gestiona procedimientos administrativos, contratación pública, recursos ante la Administración y contencioso-administrativo.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan las administraciones con las que te relacionas y los procedimientos principales, con valores sensatos en todo lo demás. **15 minutos** añade tu experiencia en contratación pública, asuntos contenciosos en curso y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica administrativa (administraciones, procedimientos, contratación pública, contencioso-administrativo). Esta entrevista aprende cómo trabajas realmente y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes alguna resolución administrativa o pliego reciente? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo de la LPAC (Ley 39/2015), la LRJSP (Ley 40/2015), la LCSP (Ley 9/2017) o la LJCA (Ley 29/1998), comprobar antes de escribirlo.

## La entrevista

### Apertura

> Voy a ayudarte con procedimientos administrativos, contratación pública, recursos ante la Administración y contencioso-administrativo. Antes de nada, necesito saber con qué administraciones te relacionas y qué tipo de asuntos gestionas. Diez minutos.
>
> Después te pediré tres cosas: una resolución administrativa representativa, unos pliegos si haces contratación pública, y un recurso reciente.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a administrativista** — letrado/a especializado en derecho público.
> 2. **Profesional con acceso a letrado** — responsable de licitaciones, gestor administrativo, técnico de administración que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — gestionas esto por tu cuenta.

Si es 2 o 3, explicar: los outputs serán investigación para revisión letrada; se pausará antes de pasos con consecuencias jurídicas (presentación de recursos, interposición de contencioso).

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Relación con la Administración (2-3 min)

> **Con qué niveles de la Administración te relacionas habitualmente?** Esto determina la normativa procedimental y los órganos de recurso.
>
> - **AGE** (Administración General del Estado) — ministerios, organismos autónomos, entidades públicas empresariales. Cuáles?
> - **CCAA** (Comunidades Autónomas) — cuáles? Qué consejerías?
> - **EELL** (Entidades Locales) — ayuntamientos, diputaciones. Cuáles?
>
> Con qué frecuencia interactúas con cada nivel? (Diaria, semanal, mensual, puntual)
>
> Usáis sede electrónica habitualmente? Tenéis certificado digital / Cl@ve para la gestión?

Pausa. Después:

> **En qué ámbito material se concentra tu práctica administrativa?** (Puedes seleccionar varios)
> - Urbanismo y ordenación del territorio
> - Medio ambiente
> - Sanidad
> - Educación
> - Energía
> - Telecomunicaciones
> - Transportes e infraestructuras
> - Función pública / empleo público
> - Otro (descríbelo)

### Parte 2: Procedimientos habituales (2-3 min)

> **Qué tipo de procedimientos administrativos gestionas con más frecuencia?**
>
> - **Autorizaciones y licencias** — urbanísticas, ambientales, de actividad, sectoriales. Cuáles?
> - **Procedimientos sancionadores** — en qué materias? Habéis tenido sanciones recientes?
> - **Subvenciones y ayudas** — solicitud, justificación, reintegro. Con qué administración?
> - **Expropiaciones** — como beneficiario, como expropiado?
> - **Responsabilidad patrimonial** de la Administración — reclamaciones en curso?
> - **Procedimientos de revisión de oficio** — los habéis instado o sufrido?
>
> Para los procedimientos que más gestionas:
> - Plazos típicos de resolución real (no el legal, el real)
> - Silencio administrativo: positivo o negativo en tus procedimientos habituales?
> - Recursos habituales: alzada, reposición, o directamente contencioso?

### Parte 3: Contratación pública (3-4 min)

> **Trabajas en contratación pública?** Si la respuesta es no, saltamos esta parte.
>
> Si sí:
> - **Desde qué lado?** Licitador (empresa), poder adjudicador, o ambos?
> - **Perfil del contratante habitual** — con qué órganos de contratación trabajas más?
> - **Tipos de contratos** — obras, servicios, suministros, concesiones, mixtos?
> - **Cuantía habitual** — menor (< 15.000/40.000 euros), por debajo del umbral armonizado, armonizados?
> - **Procedimientos** — abierto, restringido, negociado, diálogo competitivo, asociación para la innovación?
>
> Experiencia con recursos:
> - **TACRC** (Tribunal Administrativo Central de Recursos Contractuales) — habéis interpuesto o defendido recursos especiales en materia de contratación?
> - **Órganos autonómicos equivalentes** (TARCJA en Andalucía, OARC en País Vasco, etc.) — cuáles?
> - Ratio de éxito aproximado? Criterios que más os afectan?
>
> Tienes algún pliego (PCAP + PPT) reciente que pueda ver? Pégalo o comparte ruta.

### Parte 4: Contencioso-administrativo (2-3 min)

> **Llevas asuntos contencioso-administrativos?** Si la respuesta es no, saltamos esta parte.
>
> Si sí:
> - **Jurisdicción habitual** — Juzgados de lo Contencioso-Administrativo, Salas de TSJ, Audiencia Nacional, Tribunal Supremo?
> - **Materias más frecuentes** — urbanismo, tributario (si no lo lleva el plugin fiscal), sanciones, contratación, responsabilidad patrimonial, extranjería, otro?
> - **Volumen** — cuántos asuntos en curso aproximadamente?
> - **Medidas cautelares** — las solicitáis con frecuencia? Ratio de éxito?
> - **Extensión de efectos** (art. 110 LJCA) — la usáis?
> - **Casación** — habéis preparado o interpuesto recursos de casación ante el TS? Conocéis el sistema de admisión por interés casacional (art. 88-89 LJCA)?
>
> Hay algún asunto contencioso en curso que sea especialmente relevante o de referencia?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Una resolución administrativa representativa** — favorable o desfavorable, la que mejor refleje vuestra práctica habitual. Aprenderé vuestro estilo de argumentación y los tipos de asuntos que gestionáis.
>
> 2. **Pliegos de contratación** — si hacéis contratación pública, un PCAP + PPT reciente. Aprenderé vuestras cláusulas habituales y vuestra posición en las mesas de contratación.
>
> 3. **Un recurso reciente** — administrativo o contencioso. Me enseña cómo argumentáis y qué criterios utilizáis.

**Cómo leer los documentos semilla:**

**Resolución administrativa:** Extraer el procedimiento, los fundamentos de derecho citados, el sentido del fallo. Identificar las normas procesales aplicadas.

**Pliegos:** Mapear los criterios de adjudicación, las condiciones especiales de ejecución, las cláusulas de penalización y modificación. Comparar con las posiciones declaradas en la entrevista.

**Recurso:** Extraer la estructura argumentativa, los fundamentos de derecho, la jurisprudencia citada. Aprender el estilo.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Administrativo

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] gestiona asuntos de derecho administrativo en [ámbitos materiales].
Relación principal con [AGE/CCAA/EELL — cuáles]. El equipo cuenta con [N] personas.
[Responsable: nombre]. La escalación va a [nombre].

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

## Relación con la Administración

| Nivel | Administraciones concretas | Frecuencia | Ámbito material |
|---|---|---|---|
| AGE | [ministerios/organismos] | [frecuencia] | [materia] |
| CCAA | [comunidades/consejerías] | [frecuencia] | [materia] |
| EELL | [ayuntamientos/diputaciones] | [frecuencia] | [materia] |

---

## Procedimientos habituales

| Tipo | Administración | Frecuencia | Silencio | Recurso habitual | Notas |
|---|---|---|---|---|---|
| [autorizaciones/sanciones/subvenciones/etc.] | [cuál] | [frecuencia] | [positivo/negativo] | [alzada/reposición/contencioso] | |

---

## Contratación pública

**Posición:** [licitador / poder adjudicador / ambos]
**Perfiles del contratante habituales:** [órganos]
**Tipos de contrato:** [obras/servicios/suministros/concesiones]
**Cuantía habitual:** [menor/sub-umbral/armonizado]
**Procedimientos habituales:** [abierto/restringido/negociado]

### Experiencia en recursos contractuales

| Órgano | Recursos interpuestos | Recursos defendidos | Ratio éxito aprox. |
|---|---|---|---|
| TACRC | [número] | [número] | [ratio] |
| [órgano autonómico] | [número] | [número] | [ratio] |

---

## Contencioso-administrativo

**Jurisdicción habitual:** [juzgados/TSJ sala/AN/TS]
**Materias:** [lista]
**Asuntos en curso:** [número aproximado]
**Medidas cautelares:** [frecuencia y ratio]
**Casación:** [experiencia]

### Asuntos en curso relevantes

| Asunto | Órgano | Materia | Estado | Notas |
|---|---|---|---|---|
| [referencia] | [órgano] | [materia] | [estado] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Procedimiento rutinario | [responsable] | [nombre] | Silencio negativo vencido, sanción > [umbral] |
| Recurso administrativo | [responsable] | [nombre] | Cuantía > [umbral] |
| Contencioso-administrativo | [responsable] | [nombre] | Siempre en casación |
| Contratación > umbral armonizado | — | [GC + dirección] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Resolución administrativa | [ruta] | [fecha] | [tipo procedimiento] |
| Pliegos contratación | [ruta] | [fecha] | [órgano] |
| Recurso reciente | [ruta] | [fecha] | [tipo y materia] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/administrativo:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Los procedimientos habituales y la experiencia en contratación pública son las partes a revisar con más cuidado."

2. **Proponer primeras tareas:**
   - "Quieres que revise un pliego de contratación en curso?"
   - "Tienes algún recurso administrativo pendiente de redactar?"
   - "Quieres que compruebe plazos de prescripción o caducidad en tus procedimientos abiertos?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/administrativo:entrevista-inicial --redo` para re-entrevista completa
   > - `/administrativo:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: los **procedimientos habituales** (según evoluciona la práctica), la **contratación pública** (según se acumula experiencia en recursos), y el **contencioso-administrativo** (según cambian los asuntos en curso)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que la LPAC aplica a todo.** Hay procedimientos especiales con normativa propia (tributario, Seguridad Social, extranjería, contratación pública). La LPAC es supletoria en muchos casos.
- **No confundir recurso de alzada con reposición.** Alzada es contra actos que no agotan la vía administrativa (art. 121 LPAC); reposición es potestativo contra actos que la agotan (art. 123 LPAC). Un error aquí tiene consecuencias de inadmisibilidad.
- **No dar por hecho que el silencio es positivo.** En derecho administrativo español el silencio es negativo por defecto en muchos procedimientos (art. 24.1 LPAC con excepciones). Verificar siempre la norma sectorial aplicable.
- **No ignorar los plazos de la LJCA.** El plazo para interponer recurso contencioso-administrativo es de 2 meses desde la notificación del acto (art. 46 LJCA), pero hay excepciones (actos presuntos: 6 meses; vía de hecho: 10-20 días). Los plazos son de caducidad e improrrogables.
- **No olvidar la legitimación.** En contencioso-administrativo la legitimación activa es más amplia que en otros órdenes (art. 19 LJCA), pero hay matices importantes (acción pública en urbanismo, legitimación de organizaciones).
- **No mezclar normativa estatal con autonómica.** Las CCAA tienen competencia normativa propia en muchas materias administrativas (urbanismo, medio ambiente, función pública). Preguntar siempre la CCAA relevante.
