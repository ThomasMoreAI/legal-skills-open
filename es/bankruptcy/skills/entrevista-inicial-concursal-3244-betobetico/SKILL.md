---
name: entrevista-inicial-concursal-3244-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin concursal. Aprende tu práctica y escribe CLAUDE.md a partir de tu rol habitual, tipos de procedimiento, experiencia y herramientas. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin concursal", "onboarding concursal", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/concursal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: bankruptcy
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: auto de declaración de concurso, inventario/lista de acreedores, plan de reestructuración.
4. Extraer: rol habitual, tipos de procedimiento, experiencia, herramientas.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/concursal:entrevista-inicial
```

```
/concursal:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Derecho Concursal

## Propósito

Aprender cómo funciona *esta* práctica concursal — si actúas como deudor, acreedor, administración concursal o inversor en distressed. Qué tipos de procedimiento gestiona, cuánta experiencia tiene, qué herramientas usa. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica concursal varía radicalmente según el rol. Un abogado de la administración concursal tiene necesidades completamente distintas a las de un acreedor financiero que busca maximizar su recuperación o a las de un inversor en situaciones de distressed. La entrevista identifica el perfil antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`concursal` es para quien gestiona insolvencias: pre-concurso, concurso de acreedores, reestructuraciones, liquidaciones, compraventa de activos en distress.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el rol habitual y los tipos de procedimiento principales, con valores sensatos en todo lo demás. **15 minutos** añade tu experiencia detallada, herramientas, y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica concursal (rol, tipos de procedimiento, experiencia, herramientas). Esta entrevista aprende cómo trabajas realmente — desde qué lado actúas, qué tamaño de concursos gestionas, qué herramientas usas — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes un auto de declaración de concurso o un plan de reestructuración? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo del TRLC (RDL 1/2020, Texto Refundido de la Ley Concursal), comprobar antes de escribirlo. El TRLC ha sido modificado sustancialmente por la Ley 16/2022 de transposición de la Directiva de reestructuración.

## La entrevista

### Apertura

> Voy a ayudarte con procedimientos concursales: pre-concurso, reestructuraciones, concurso de acreedores, liquidación y compraventa de activos en distress. Antes de nada, necesito saber desde qué lado actúas y qué tipo de procedimientos gestionas. Diez minutos.
>
> Después te pediré tres cosas: un auto de declaración de concurso, un inventario o lista de acreedores, y un plan de reestructuración si los tienes.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a concursalista** — letrado/a especializado en insolvencia y reestructuración.
> 2. **Profesional con acceso a letrado** — economista de administración concursal, auditor, director financiero que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — empresario en situación de insolvencia, acreedor individual.

Si es 2 o 3, explicar: los outputs serán investigación para revisión letrada. El derecho concursal tiene plazos procesales muy estrictos — se pausará antes de cualquier acción con consecuencias procesales.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Rol habitual (2-3 min)

> **Desde qué posición actúas habitualmente en procedimientos concursales?** Esto determina completamente cómo funciona el plugin — las prioridades, los plazos y la estrategia cambian radicalmente según el rol.
>
> - **Deudor** — asesoras a la empresa en situación de insolvencia o pre-insolvencia. Preparas solicitudes de concurso, negociáis planes de reestructuración, gestionáis la fase de convenio o liquidación.
> - **Acreedor** — representas a acreedores (financieros, comerciales, trabajadores, públicos). Impugnas listas, votáis convenios, ejecutáis garantías.
> - **Administración concursal** — eres administrador concursal o formas parte de un equipo de AC. Gestionáis la masa, elaboráis inventario y lista de acreedores, informes, propuestas de convenio/liquidación.
> - **Inversor en distressed** — compras créditos concursales, adquieres unidades productivas en liquidación, financias reestructuraciones.
> - **Varios roles** — actúas desde distintas posiciones según el asunto.
>
> Si actúas desde varios roles, cuál es el más frecuente?

Pausa. Después:

> **Cuál es tu ámbito geográfico habitual?** Los juzgados de lo mercantil competentes varían.
> - Juzgados de lo Mercantil de [provincia(s)]?
> - Juzgados especializados (Madrid, Barcelona)?
> - Ámbito nacional?

### Parte 2: Tipos de procedimiento (2-3 min)

> **Qué tipos de procedimiento gestionas?** El TRLC (tras la reforma de la Ley 16/2022) distingue varios:
>
> - **Comunicación de apertura de negociaciones** (art. 583 TRLC, antiguo pre-concurso art. 5 bis) — cuántos has gestionado? Es una herramienta que uses habitualmente como primer paso?
> - **Planes de reestructuración** (Libro II, arts. 599 y ss. TRLC, nuevo tras Ley 16/2022) — has gestionado alguno? Con homologación judicial?
> - **Concurso voluntario** (solicitado por el deudor) — frecuencia?
> - **Concurso necesario** (solicitado por acreedores) — frecuencia? Desde qué lado?
> - **Concurso de persona natural** (incluido microempresa) — gestionas exoneración del pasivo insatisfecho (segunda oportunidad, arts. 486 y ss. TRLC)?
> - **Procedimiento especial de microempresas** (Libro III, arts. 685 y ss. TRLC, en vigor desde enero 2023) — lo has usado?
>
> Distinguir: en cuántos has terminado en convenio y en cuántos en liquidación? Ratio aproximado?

### Parte 3: Experiencia (2 min)

> **Cuánta experiencia concursal tienes?** Esto calibra los defaults del plugin.
>
> - **Número aproximado de concursos gestionados** en tu carrera
> - **Sectores principales** — inmobiliario, industrial, servicios, construcción, hostelería, retail, otro?
> - **Tamaño habitual de los concursos:**
>   - Microempresa (< 10 empleados, < 2M activo, < 2M cifra negocios)
>   - Pyme
>   - Gran empresa
>   - Grupo de sociedades (concurso conexo, art. 36 TRLC)
> - **Asuntos especialmente relevantes o de referencia?** Sin nombres si prefieres, pero el tipo y tamaño me ayuda.

### Parte 4: Herramientas (2 min)

> **Qué herramientas usas en tu práctica concursal?**
>
> - **Software de gestión concursal** — usas algún software específico? (LexNET para comunicaciones, plataformas de administración concursal, etc.)
> - **Registro Público Concursal** (https://www.publicidadconcursal.es) — con qué frecuencia lo consultas? Tienes acceso de usuario registrado?
> - **Registro de Acuerdos Extrajudiciales y de planes de reestructuración** — lo usas?
> - **Bases de datos jurídicas** — Aranzadi, La Ley, vLex, CENDOJ? Cuáles usas para jurisprudencia concursal?
> - **Herramientas de valoración** — para activos en liquidación, unidades productivas?
> - **Plataformas de subastas** — Portal de Subastas del BOE (subastas.boe.es), otras?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Un auto de declaración de concurso** — me enseña qué tipo de concursos gestionas y cómo se estructuran en tu juzgado habitual.
>
> 2. **Un inventario y/o lista de acreedores** — me enseña la complejidad de las masas que gestionas y cómo clasificas los créditos.
>
> 3. **Un plan de reestructuración o propuesta de convenio** — me enseña cómo estructuras las soluciones y qué tipo de quitas/esperas propones habitualmente.

**Cómo leer los documentos semilla:**

**Auto de declaración:** Extraer tipo de concurso, medidas adoptadas, nombramiento de AC, carácter de las facultades del deudor (intervención vs. suspensión).

**Inventario/lista de acreedores:** Analizar la composición del pasivo (créditos con privilegio especial, general, ordinarios, subordinados). Identificar la complejidad.

**Plan de reestructuración/convenio:** Extraer la estructura de la propuesta (quitas, esperas, capitalización de deuda, cesión de bienes, continuación/liquidación). Identificar las posiciones habituales.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Concursal

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] practica derecho concursal desde el rol de [deudor/acreedor/AC/inversor].
Ámbito geográfico: [juzgados habituales]. El equipo cuenta con [N] personas.
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

## Rol habitual

**Posición principal:** [deudor / acreedor / administración concursal / inversor distressed / varios]
**Posición secundaria:** [si aplica]
**Juzgados habituales:** [Mercantil n.o X de [ciudad]]

---

## Tipos de procedimiento

| Tipo | Experiencia | Frecuencia actual | Notas |
|---|---|---|---|
| Comunicación art. 583 | [número] | [frecuencia] | |
| Plan de reestructuración (Libro II) | [número] | [frecuencia] | |
| Concurso voluntario | [número] | [frecuencia] | |
| Concurso necesario | [número] | [frecuencia] | Desde lado [deudor/acreedor] |
| Persona natural / segunda oportunidad | [número] | [frecuencia] | |
| Microempresas (Libro III) | [número] | [frecuencia] | |

**Ratio convenio/liquidación:** [aproximado]

---

## Experiencia

**Concursos gestionados (carrera):** [número]
**Sectores principales:** [lista]
**Tamaño habitual:** [microempresa / pyme / gran empresa / grupo]

---

## Herramientas

| Herramienta | Uso | Frecuencia | Notas |
|---|---|---|---|
| LexNET | Comunicaciones judiciales | [frecuencia] | |
| Registro Público Concursal | Consulta | [frecuencia] | Acceso registrado: [sí/no] |
| [software gestión] | [uso] | [frecuencia] | |
| [base datos jurídica] | Jurisprudencia | [frecuencia] | |
| Portal Subastas BOE | Subastas | [frecuencia] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Concurso rutinario | [responsable] | [nombre] | Masa activa > [umbral] |
| Plan de reestructuración | [responsable] | [nombre] | Siempre |
| Venta de unidad productiva | — | [dirección + legal] | Siempre |
| Calificación culpable | — | [GC + dirección] | Siempre |
| Responsabilidad de administradores | — | [GC + dirección] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Auto de declaración | [ruta] | [fecha] | [tipo concurso] |
| Inventario/lista acreedores | [ruta] | [fecha] | [volumen] |
| Plan reestructuración/convenio | [ruta] | [fecha] | [tipo propuesta] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/concursal:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. El rol habitual y los tipos de procedimiento son las partes más importantes — todo lo demás se construye desde ahí."

2. **Proponer primeras tareas:**
   - Si es deudor/AC: "Quieres que analice la viabilidad de una comunicación art. 583 para un caso concreto?"
   - Si es acreedor: "Quieres que revise una lista de acreedores para comprobar la clasificación de tus créditos?"
   - Si es inversor: "Quieres que analice una oportunidad de adquisición de unidad productiva?"
   - General: "Quieres que revise los plazos concursales de un procedimiento en curso?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/concursal:entrevista-inicial --redo` para re-entrevista completa
   > - `/concursal:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: los **tipos de procedimiento** (el nuevo Libro II y Libro III del TRLC están generando jurisprudencia nueva), la **experiencia** (según gestionas más concursos), y las **herramientas** (según cambian los sistemas judiciales)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No confundir el antiguo art. 5 bis con el actual art. 583 TRLC.** La comunicación de apertura de negociaciones del art. 583 TRLC (tras Ley 16/2022) tiene un régimen distinto al antiguo pre-concurso. Verificar qué norma cita el usuario.
- **No asumir que todos conocen el Libro II (planes de reestructuración).** Es relativamente nuevo (Ley 16/2022, transposición de la Directiva 2019/1023) y muchos profesionales aún no lo han utilizado. Preguntar experiencia real.
- **No ignorar el procedimiento especial de microempresas (Libro III).** En vigor desde enero 2023, con reglas procesales muy distintas al concurso ordinario. Si el deudor es microempresa, este procedimiento puede ser el adecuado.
- **No confundir privilegio especial con privilegio general.** La clasificación de créditos (arts. 269-283 TRLC) es fundamental y los errores se propagan a todo el procedimiento.
- **No olvidar los plazos concursales.** Son perentorios e improrrogables. El plazo de dos meses para solicitar concurso desde el conocimiento de la insolvencia (art. 5 TRLC) es especialmente crítico — su incumplimiento puede generar concurso necesario y calificación culpable.
- **No escribir experiencia inflada.** Si el profesional tiene poca experiencia concursal, decirlo en la configuración: `[EXPERIENCIA LIMITADA — pocas operaciones concursales gestionadas. El plugin ajustará las explicaciones y ofrecerá más contexto normativo.]`
- **No ignorar la responsabilidad de los administradores.** En cada concurso, preguntar si hay riesgo de calificación culpable (art. 441 TRLC) y de responsabilidad por deudas (art. 456 TRLC).
