---
name: entrevista-inicial-regulatorio-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin de cumplimiento regulatorio. Aprende tu práctica y escribe CLAUDE.md a partir de tus políticas internas, fuentes normativas y proceso de gaps. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin regulatorio", "onboarding", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/regulatorio/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: biblioteca de políticas internas, fuentes normativas habituales, ejemplo de análisis de gaps. Leer todos.
4. Extraer: sectores regulados, supervisores relevantes, umbrales de materialidad, proceso de gaps.
5. Migración: si existe un CLAUDE.md poblado (sin marcadores `[PLACEHOLDER]`) en `~/.claude/plugins/cache/claude-para-abogados/regulatorio/*/CLAUDE.md` pero no en la ruta de configuración, copiarlo y mostrar al usuario lo migrado.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones disponibles (almacenamiento documental, Slack/Teams, tareas programadas, feeds BOE/DOUE) y actualiza `## Integraciones disponibles` en `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md`. No re-entrevista. Usar cuando conectes o desconectes un MCP y quieras que el plugin lo detecte sin repetir toda la configuración.

Al comprobar: solo reportar como verificado si una llamada MCP realmente tuvo éxito. Conectores configurados pero no probados se marcan con un indicador neutral y una indicación breve para confirmar. Nunca reportar verificado basándose solo en declaraciones de `.mcp.json`.

```
/regulatorio:entrevista-inicial
```

```
/regulatorio:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Cumplimiento Regulatorio

## Propósito

Aprender cómo funciona *esta* práctica de cumplimiento regulatorio — qué sectores supervisa, qué supervisores le afectan, cómo monitoriza cambios normativos, qué umbral de materialidad aplica, y cómo gestiona los gaps. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

Las prácticas de cumplimiento regulatorio varían enormemente. Una entidad financiera supervisada por CNMV tiene poco en común con un operador energético regulado por la CNMC. La entrevista identifica cuál es esta antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar desde esa sección.
- **Contiene marcadores `[PLACEHOLDER]` pero sin comentario de pausa** -> la plantilla nunca se completó; ofrecer empezar de cero o retomar donde empiecen los placeholders.
- **Poblado (sin placeholders, sin comentario de pausa)** -> ya configurado; saltar salvo `--redo`.

La estructura de la plantilla está en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — usarla como andamiaje de secciones. Escribir el perfil de práctica completado en la ruta de configuración, creando directorios padre si es necesario.

Si existe un CLAUDE.md en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Mostrar confirmación en una línea: "Eres [nombre], [entorno de práctica], en [empresa], [sector], operando en [jurisdicciones]. Correcto? (O di 'actualizar' para cambiar el perfil compartido.)" Si confirma, saltar las preguntas de empresa e ir directamente a las específicas del plugin.
- **Si no existe:** Serás el primer plugin que este usuario configura. Tras la orientación, preguntar los datos de empresa y escribirlos en el perfil compartido (según la plantilla en `references/company-profile-template.md`), luego continuar con las preguntas específicas. Decir al usuario: "He guardado tu perfil de empresa — los demás plugins jurídicos lo leerán y se saltarán estas preguntas."

## Antes de empezar la entrevista

Mostrar el preámbulo de bifurcación — 3-4 líneas breves:

> **`regulatorio` es para quien gestiona el cumplimiento normativo: monitorización de cambios regulatorios, análisis de gaps, actualización de políticas internas, relación con supervisores.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el sector, los supervisores principales y las fuentes normativas básicas, con valores sensatos en todo lo demás. **15 minutos** añade tu biblioteca de políticas, umbrales de materialidad, proceso de gaps completo y documentos semilla.
>
> Rápido o completo? (Ampliar en cualquier momento con `/entrevista-inicial --redo`.)

Esperar a que el usuario elija antes de mostrar nada más.

## Tras elegir rápido o completo

Orientar antes de la primera pregunta:

> "Este plugin mantiene tu perfil de práctica regulatoria (sectores, supervisores, fuentes normativas, políticas internas, proceso de gaps), un registro de obligaciones y alertas normativas. Esta entrevista aprende cómo trabajas realmente — tus sectores, tus supervisores, tus fuentes, tus umbrales — y lo escribe en un archivo de texto plano que el plugin lee cada vez. Todo lo que respondas se puede cambiar después. Una vez hecho, los comandos del plugin funcionarán como tú trabajas, no como una plantilla genérica."
>
> "La configuración se construye desde tus respuestas y documentos semilla. No lee tu historial personal de Claude ni otras conversaciones."
>
> "Listo? Unas preguntas rápidas primero, luego profundizamos."

**Ruta rápida:** preguntar solo Parte 0 (rol, entorno, integraciones) y sectores regulados. Escribir la configuración con marcadores `[DEFAULT]` en todo lo demás. Cerrar con: "Hecho. Puedes empezar a usar los comandos. He usado valores por defecto sensatos para umbrales de materialidad, proceso de gaps y biblioteca de políticas. Cuando un resultado del skill no encaje, normalmente es un valor por defecto que deberías ajustar. Ejecuta `/regulatorio:entrevista-inicial --redo` en cualquier momento para hacer la entrevista completa."

**Ruta completa:** el flujo de entrevista completo descrito abajo.

## Ritmo de la entrevista

- **Presuponer que la respuesta existe en algún sitio.** Cuando una pregunta pide información que probablemente está escrita — lista de supervisores, inventario de políticas, procedimiento de gaps — pedir un enlace o un pegado antes de pedir que lo escriban de memoria. "Pega un enlace o un documento, o dame la versión corta" es la pregunta por defecto.
- **Tamaño del lote — contar subpartes.** "No preguntar más de 2-3 cuestiones por turno" significa 2-3 *preguntas contestables*. Una pregunta con 5 subpartes son 5 preguntas.

**Pausar para respuestas reales.** Algunas preguntas tienen respuestas rápidas de selección (sector, tipo de supervisor). Otras necesitan que el usuario escriba o suba un documento.

- **Preguntar y esperar.** Decir explícitamente: "Esta necesita una respuesta escrita — espero."
- **Para subidas de documentos semilla:** "Pega el contenido, comparte una ruta de archivo o URL, o di 'saltar por ahora.' Si saltas, marcaré el hueco en tu perfil."
- **Antes de escribir el perfil:** revisar la entrevista. Listar preguntas saltadas o con placeholders. Decir: "Antes de escribir tu perfil, esto queda pendiente: [lista]. Quieres completar algo ahora, o dejarlo como placeholder?"
- **Pausa y reanudación.** Decir al usuario al inicio: "Si necesitas parar, di 'pausa' y guardaré tu progreso. Ejecuta `/regulatorio:entrevista-inicial` de nuevo después y retomo donde lo dejamos." Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.

**Verificar datos legales del usuario.** Cuando el usuario cite un artículo, una ley, un plazo, un umbral o un número de registro, hacer una comprobación antes de escribirlo en la configuración. Si algo no cuadra, señalarlo.

## La entrevista

### Apertura

> Voy a ayudarte con la monitorización normativa, el análisis de gaps, la actualización de políticas y la gestión de relaciones con supervisores. Antes de nada, necesito saber qué tipo de práctica regulatoria es esta. Diez minutos.
>
> Después te pediré que me enseñes tres cosas: tu biblioteca de políticas internas, tus fuentes normativas habituales y un ejemplo de análisis de gaps que consideres bueno.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a o profesional jurídico** — letrado/a, responsable de cumplimiento con formación jurídica.
> 2. **Profesional no jurídico con acceso a letrado** — compliance officer, responsable de cumplimiento que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — gestionas esto por tu cuenta.

Si la respuesta es 2 o 3, explicar una vez: los outputs se enmarcarán como investigación para revisión letrada, no como conclusiones definitivas, y se pausará antes de pasos con consecuencias jurídicas.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental (Drive, SharePoint), Slack/Teams, tareas programadas y feeds de boletines oficiales (BOE, DOUE, autonómicos). Déjame comprobar qué conectores tienes configurados.

Comprobar cada conector con una llamada real, no solo la configuración. Reportar resultados.

### Parte 1: Sector y supervisores (2-3 min)

> **En qué sector o sectores regulados opera tu organización?** Este es el contexto más importante — el playbook de una entidad financiera supervisada por CNMV es completamente distinto al de un operador de telecomunicaciones supervisado por la CNMC.
>
> Selecciona los que apliquen:
> - Financiero (banca, valores, seguros)
> - Energía (electricidad, gas, petróleo)
> - Telecomunicaciones
> - Sanitario / farmacéutico
> - Alimentario
> - Medioambiental
> - Transporte
> - Otro (descríbelo)

Pausa. Después:

> **Qué supervisores son relevantes para tu práctica?** Marca los que apliquen:
> - **CNMC** (Comisión Nacional de los Mercados y la Competencia)
> - **CNMV** (Comisión Nacional del Mercado de Valores)
> - **Banco de España**
> - **DGS** (Dirección General de Seguros y Fondos de Pensiones)
> - **AEMPS** (Agencia Española de Medicamentos y Productos Sanitarios)
> - **AESAN** (Agencia Española de Seguridad Alimentaria y Nutrición)
> - **MITECO** (Ministerio para la Transición Ecológica)
> - **Otros** (especifica)
>
> Hay algún procedimiento abierto con algún supervisor? Inspecciones, expedientes sancionadores, requerimientos de información?

### Parte 2: Fuentes normativas (2-3 min)

> **De dónde sacas la información normativa que necesitas monitorizar?** Esto alimenta el skill de monitorización regulatoria.
>
> Fuentes habituales en España:
> - **BOE** (Boletín Oficial del Estado) — frecuencia de consulta?
> - **DOUE** (Diario Oficial de la Unión Europea) — solo cuando hay normativa UE directamente aplicable?
> - **Boletines autonómicos** — cuáles? (BOCM, DOGC, BOJA, etc.)
> - **Portales de supervisores** — web de CNMV, Banco de España, CNMC, etc.
> - **Bases de datos jurídicas** — Aranzadi, La Ley, vLex, EUR-Lex, etc.
> - **Alertas de despachos** — recibes alertas regulatorias de despachos externos?
> - **Asociaciones sectoriales** — alguna asociación que publique novedades relevantes?
>
> Con qué frecuencia revisas cambios normativos? Diaria, semanal, mensual?

### Parte 3: Biblioteca de políticas (2-3 min)

> **Tiene tu organización un inventario de políticas internas de cumplimiento?** Pega un enlace o describe la estructura.
>
> Para cada política relevante me interesa saber:
> 1. **Nombre y ámbito** (ej. "Política de prevención del blanqueo de capitales")
> 2. **Formato** (Word, PDF, wiki interna, otro)
> 3. **Responsable** (quién aprueba y mantiene la política)
> 4. **Última actualización**
> 5. **Normativa de referencia** (la ley o regulación que fundamenta la política)
>
> Si tienes un documento con el inventario completo, es más rápido que lo pegues o compartas.

### Parte 4: Umbral de materialidad (2 min)

> **Qué tipo de cambio normativo requiere acción inmediata vs. seguimiento rutinario?** Esto calibra las alertas del plugin.
>
> Ayúdame a definir tus umbrales:
> - **Acción inmediata** — ej. nueva obligación con plazo de cumplimiento < 6 meses, sanción tipificada, cambio que afecta directamente a una autorización vigente
> - **Seguimiento prioritario** — ej. proyecto de ley en tramitación parlamentaria avanzada, consulta pública de supervisor, directiva UE pendiente de transposición
> - **Seguimiento rutinario** — ej. doctrina administrativa, resoluciones de supervisores en sectores adyacentes, tendencias regulatorias europeas
>
> Hay algún tipo de cambio normativo que siempre escale, independientemente del sector? (ej. cambios en régimen sancionador, modificaciones de la LPAC)

### Parte 5: Proceso de gaps (3-4 min)

> **Cómo gestionáis el ciclo completo cuando se detecta un gap de cumplimiento?** Esto es el corazón del plugin. Necesito entender cada fase:
>
> 1. **Detección** — Cómo se identifica el gap? Monitorización normativa, inspección, auditoría interna, otro?
> 2. **Análisis** — Quién evalúa el impacto y la prioridad? Hay una matriz de riesgo?
> 3. **Propuesta** — Cómo se formula la propuesta de adaptación? Quién la redacta?
> 4. **Aprobación** — Quién aprueba? Comité de cumplimiento, consejo, dirección?
> 5. **Implementación** — Quién ejecuta? Plazos típicos? Cómo se hace seguimiento?
>
> Tienes algún ejemplo de análisis de gaps que consideres representativo de cómo trabajáis? Pégalo o comparte ruta — aprenderé más de eso que de lo que me cuentes.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Cumplimiento Regulatorio

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa] es una [tipo de entidad]. Operamos en los sectores [sectores].
El equipo de cumplimiento cuenta con [N] personas. [Responsable de cumplimiento: nombre o ninguno].
La escalación va a [nombre].

**Huella regulatoria:** [sectores regulados que aplican]
**Asuntos regulatorios abiertos:** [ninguno / lista]

---

## Quién usa este plugin

**Rol:** [Abogado/a | Profesional con acceso a letrado | Profesional sin acceso a letrado]
**Contacto letrado:** [Nombre / equipo / despacho externo / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Barrido bajo demanda |
| Feeds BOE/DOUE | [verificado/no] | Consulta manual |

---

## Sectores regulados y supervisores

| Sector | Supervisores | Normativa marco | Activo |
|---|---|---|---|
| [sector] | [supervisores] | [normativa] | [activo/no] |

---

## Fuentes normativas

| Fuente | Frecuencia consulta | Método (RSS/web/BD) | Notas |
|---|---|---|---|
| BOE | [frecuencia] | [método] | |
| DOUE | [frecuencia] | [método] | |
| [boletines autonómicos] | [frecuencia] | [método] | |
| [portales supervisores] | [frecuencia] | [método] | |

---

## Biblioteca de políticas internas

| Política | Ámbito | Formato | Responsable | Última actualización | Normativa base |
|---|---|---|---|---|---|
| [nombre] | [ámbito] | [formato] | [responsable] | [fecha] | [normativa] |

---

## Umbrales de materialidad

| Nivel | Criterio | Ejemplo | Acción |
|---|---|---|---|
| Acción inmediata | [criterio] | [ejemplo] | Alerta + análisis en 24h |
| Seguimiento prioritario | [criterio] | [ejemplo] | Análisis en 1 semana |
| Seguimiento rutinario | [criterio] | [ejemplo] | Revisión en próximo ciclo |

---

## Proceso de gaps

| Fase | Responsable | Plazo típico | Mecanismo |
|---|---|---|---|
| Detección | [responsable] | [plazo] | [mecanismo] |
| Análisis | [responsable] | [plazo] | [mecanismo] |
| Propuesta | [responsable] | [plazo] | [mecanismo] |
| Aprobación | [responsable] | [plazo] | [mecanismo] |
| Implementación | [responsable] | [plazo] | [mecanismo] |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Cambio normativo rutinario | [responsable] | [nombre] | Impacto en autorizaciones vigentes |
| Inspección de supervisor | — | [GC + cumplimiento] | Siempre |
| Expediente sancionador | — | [GC + dirección] | Siempre |
| Gap crítico detectado | [responsable] | [nombre] | Plazo < 3 meses o sanción grave |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Biblioteca de políticas | [ruta] | [fecha] | |
| Fuentes normativas | [ruta/enlace] | [fecha] | |
| Ejemplo de análisis de gaps | [ruta] | [fecha] | |

---

## Resultados

**Carpeta de resultados:** [ruta donde se guardan análisis de gaps, alertas normativas y revisiones]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/regulatorio:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Los umbrales de materialidad y el proceso de gaps son las partes a revisar con más cuidado."

2. **Proponer primeras tareas:**
   - "Quieres que haga un barrido del BOE de las últimas dos semanas contra tus sectores?"
   - "Tienes alguna política interna que necesite actualizarse por un cambio normativo reciente?"
   - "Quieres que analice un gap concreto que tengas pendiente?"

3. **Señalar huecos:** Si no pudo aportar la biblioteca de políticas o el ejemplo de análisis de gaps, indicarlo.

4. **Cerrar con la nota de "puedes cambiar todo después":**

   > "Tu perfil de práctica está en `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` — un archivo de texto plano que puedes leer y editar directamente. Lo que respondiste se puede cambiar:
   >
   > - Editar el archivo directamente para un cambio rápido
   > - Ejecutar `/regulatorio:entrevista-inicial --redo` para una re-entrevista completa
   > - Ejecutar `/regulatorio:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las tres secciones que la gente ajusta más: los **umbrales de materialidad** (según el equipo gana experiencia), las **fuentes normativas** (según cambian las suscripciones), y el **proceso de gaps** (según se formaliza o simplifica)."

5. **Tu perfil de práctica aprende.** Cerrar con:

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins:
   >
   > - Cuando un resultado de un skill no encaje, normalmente es una posición que ajustar. El output te dirá cuál.
   > - Puedes decir "actualiza mi umbral de materialidad a X" o "cambia mi proceso de aprobación a Y" y el skill relevante escribirá el cambio.
   > - Ejecuta `/regulatorio:entrevista-inicial --redo <sección>` para re-entrevistar una parte, o edita el archivo de configuración directamente.
   >
   > Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que todos los sectores regulados aplican.** Muchas empresas creen que les afecta normativa sectorial que no les toca. Preguntar qué autorizaciones o licencias administrativas tienen realmente.
- **No dejar que se salte la pregunta del supervisor.** Si no está seguro, recorrer juntos: "Qué autorizaciones o licencias necesitáis para operar? El organismo que las otorga es vuestro supervisor."
- **No escribir un proceso de gaps genérico.** Si no tienen un proceso formalizado, decirlo en la configuración: `[PROCESO NO FORMALIZADO — este equipo gestiona gaps de forma ad hoc. Tratar como punto de partida, no como procedimiento establecido.]`
- **No confundir normativa estatal con autonómica.** Preguntar siempre en qué CCAA opera la organización — muchas obligaciones regulatorias tienen desarrollo autonómico distinto.
- **No asumir que las fuentes están automatizadas.** Muchas prácticas de cumplimiento en España siguen consultando el BOE manualmente. No dar por hecho que tienen feeds RSS o alertas configuradas.
