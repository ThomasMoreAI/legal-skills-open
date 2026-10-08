---
name: entrevista-inicial-concursal-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin concursal. Aprende tu práctica y escribe CLAUDE.md a partir de tu rol habitual, tipos de proceso, experiencia y herramientas. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin concursal", "onboarding concursal", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/concursal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: bankruptcy
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: resolución de apertura del proceso concursal, inventario/lista de créditos, plan de reorganización.
4. Extraer: rol habitual, tipos de proceso, experiencia, herramientas.
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

# Entrevista Inicial: Derecho Concursal de Insolvencia (Panamá)

## Propósito

Aprender cómo funciona *esta* práctica concursal — si actúas como deudor, acreedor, administrador/restructurador del proceso o inversor en distressed. Qué tipos de proceso gestiona, cuánta experiencia tiene, qué herramientas usa. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica concursal varía radicalmente según el rol. Un abogado del administrador del proceso tiene necesidades completamente distintas a las de un acreedor financiero que busca maximizar su recuperación o a las de un inversor en situaciones de distressed. La entrevista identifica el perfil antes de nada.

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

> **`concursal` es para quien gestiona insolvencias bajo la Ley 12 de 2016: reorganización, liquidación, reconocimiento de créditos, compraventa de activos en distress.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el rol habitual y los tipos de proceso principales, con valores sensatos en todo lo demás. **15 minutos** añade tu experiencia detallada, herramientas, y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica concursal (rol, tipos de proceso, experiencia, herramientas). Esta entrevista aprende cómo trabajas realmente — desde qué lado actúas, qué tamaño de procesos gestionas, qué herramientas usas — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes una resolución de apertura de un proceso concursal o un plan de reorganización? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo de la Ley 12 de 2016, comprobarlo antes de escribirlo. Para cualquier número de artículo o plazo del que no haya certeza, usar referencia genérica y marcar `[verificar]`.

## La entrevista

### Apertura

> Voy a ayudarte con procesos concursales de insolvencia bajo la Ley 12 de 2016: reorganización, reconocimiento y graduación de créditos, liquidación y compraventa de activos en distress. Antes de nada, necesito saber desde qué lado actúas y qué tipo de procesos gestionas. Diez minutos.
>
> Después te pediré tres cosas: una resolución de apertura del proceso concursal, un inventario o lista de créditos, y un plan de reorganización si los tienes.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a idóneo especializado en insolvencia** — letrado/a especializado en concursal y reorganización.
> 2. **Profesional con acceso a letrado** — contador del proceso, auditor, director financiero que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — empresario en situación de insolvencia, acreedor individual.

Si es 2 o 3, explicar: los outputs serán investigación para revisión letrada. El derecho concursal tiene plazos procesales muy estrictos — se pausará antes de cualquier acción con consecuencias procesales.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Rol habitual (2-3 min)

> **Desde qué posición actúas habitualmente en procesos concursales?** Esto determina completamente cómo funciona el plugin — las prioridades, los plazos y la estrategia cambian radicalmente según el rol.
>
> - **Deudor** — asesoras a la empresa en situación de insolvencia o pre-insolvencia. Preparas solicitudes de reorganización o liquidación, negociáis el plan, gestionáis la fase de cumplimiento.
> - **Acreedor** — representas a acreedores (financieros, comerciales, trabajadores, públicos). Impugnas listas de créditos, votáis el plan, ejecutáis garantías.
> - **Administrador / restructurador del proceso** — eres administrador o restructurador designado [verificar] o formas parte de su equipo. Gestionáis el patrimonio, elaboráis inventario y lista de créditos, informes, propuestas de reorganización/liquidación.
> - **Inversor en distressed** — compras créditos, adquieres unidades productivas en liquidación, financias reorganizaciones.
> - **Varios roles** — actúas desde distintas posiciones según el asunto.
>
> Si actúas desde varios roles, cuál es el más frecuente?

Pausa. Después:

> **Cuál es tu ámbito geográfico habitual?** Los juzgados competentes varían.
> - Juzgados de Circuito del Circuito de Panamá?
> - Juzgados de otros circuitos (Colón, Chiriquí, etc.)?
> - Ámbito nacional?

### Parte 2: Tipos de proceso (2-3 min)

> **Qué tipos de proceso gestionas?** La Ley 12 de 2016 distingue principalmente:
>
> - **Proceso de reorganización** — dirigido a la recuperación de la empresa viable mediante un plan acordado con los acreedores. Cuántos has gestionado? Es tu vía habitual como primer paso?
> - **Proceso de liquidación** — realización del patrimonio para el pago a los acreedores. Has gestionado alguno?
> - **Solicitud voluntaria** (presentada por el deudor) — frecuencia?
> - **Solicitud a instancia de acreedor** — frecuencia? Desde qué lado?
> - **Insolvencia de persona natural** — gestionas estos supuestos? Verificar el ámbito subjetivo de la Ley 12 de 2016.
> - **Procesos de grupos de sociedades o vinculados** — los has gestionado? [verificar]
>
> Distinguir: en cuántos has terminado en reorganización exitosa y en cuántos en liquidación? Ratio aproximado?

### Parte 3: Experiencia (2 min)

> **Cuánta experiencia concursal tienes?** Esto calibra los defaults del plugin.
>
> - **Número aproximado de procesos concursales gestionados** en tu carrera
> - **Sectores principales** — inmobiliario, industrial, servicios, construcción, comercio, logística/Zona Libre, marítimo, otro?
> - **Tamaño habitual de los procesos:**
>   - Microempresa / pequeña empresa
>   - Mediana empresa
>   - Gran empresa
>   - Grupo de sociedades
> - **Asuntos especialmente relevantes o de referencia?** Sin nombres si prefieres, pero el tipo y tamaño me ayuda.

### Parte 4: Herramientas (2 min)

> **Qué herramientas usas en tu práctica concursal?**
>
> - **Software de gestión** — usas algún software específico? (sistema de notificaciones del Órgano Judicial, plataformas de administración del proceso, etc.)
> - **Portal del Órgano Judicial de Panamá** — con qué frecuencia lo consultas? Tienes acceso de usuario registrado?
> - **Registro Público de Panamá** — para verificar la situación societaria del deudor y las garantías inscritas? Con qué frecuencia?
> - **Bases de datos jurídicas** — Gaceta Oficial, Registro Judicial, repositorios de jurisprudencia de la Corte Suprema de Justicia? Cuáles usas?
> - **Herramientas de valoración** — para activos en liquidación, unidades productivas?
> - **Plataformas de subastas / remates judiciales** — cuáles usas?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Una resolución de apertura del proceso concursal** — me enseña qué tipo de procesos gestionas y cómo se estructuran en tu juzgado habitual.
>
> 2. **Un inventario y/o lista de créditos** — me enseña la complejidad de las masas que gestionas y cómo clasificas los créditos.
>
> 3. **Un plan de reorganización o propuesta de acuerdo** — me enseña cómo estructuras las soluciones y qué tipo de quitas/esperas propones habitualmente.

**Cómo leer los documentos semilla:**

**Resolución de apertura:** Extraer tipo de proceso (reorganización/liquidación), medidas adoptadas, designación de administrador/restructurador/liquidador, carácter de las facultades del deudor (supervisión vs. desapoderamiento) [verificar].

**Inventario/lista de créditos:** Analizar la composición del pasivo (créditos con garantía real, privilegiados, ordinarios, subordinados). Identificar la complejidad.

**Plan de reorganización/acuerdo:** Extraer la estructura de la propuesta (quitas, esperas, capitalización de deuda, dación en pago, continuación/liquidación). Identificar las posiciones habituales.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Concursal de Insolvencia (Panamá)

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] practica derecho concursal desde el rol de [deudor/acreedor/administrador-restructurador/inversor].
Ámbito geográfico: [juzgados habituales]. El equipo cuenta con [N] personas.
[Responsable: nombre]. La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a idóneo | Profesional con acceso a letrado | Profesional sin acceso a letrado]
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

**Posición principal:** [deudor / acreedor / administrador-restructurador del proceso / inversor distressed / varios]
**Posición secundaria:** [si aplica]
**Juzgados habituales:** [Juzgado de Circuito de [ciudad]]

---

## Tipos de proceso

| Tipo | Experiencia | Frecuencia actual | Notas |
|---|---|---|---|
| Reorganización | [número] | [frecuencia] | |
| Liquidación | [número] | [frecuencia] | |
| Solicitud voluntaria | [número] | [frecuencia] | |
| Solicitud a instancia de acreedor | [número] | [frecuencia] | Desde lado [deudor/acreedor] |
| Insolvencia de persona natural | [número] | [frecuencia] | [verificar ámbito subjetivo] |
| Grupos / vinculados | [número] | [frecuencia] | |

**Ratio reorganización/liquidación:** [aproximado]

---

## Experiencia

**Procesos gestionados (carrera):** [número]
**Sectores principales:** [lista]
**Tamaño habitual:** [microempresa / pyme / gran empresa / grupo]

---

## Herramientas

| Herramienta | Uso | Frecuencia | Notas |
|---|---|---|---|
| Sistema de notificaciones del Órgano Judicial | Notificaciones judiciales | [frecuencia] | |
| Portal del Órgano Judicial | Consulta | [frecuencia] | Acceso registrado: [sí/no] |
| Registro Público de Panamá | Verificación societaria/garantías | [frecuencia] | |
| [base datos jurídica] | Jurisprudencia | [frecuencia] | |
| [plataforma de remates] | Subastas | [frecuencia] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Proceso rutinario | [responsable] | [nombre] | Patrimonio > [umbral] |
| Plan de reorganización | [responsable] | [nombre] | Siempre |
| Venta de unidad productiva | — | [dirección + legal] | Siempre |
| Conducta dolosa o fraudulenta | — | [GC + dirección] | Siempre |
| Responsabilidad de administradores | — | [GC + dirección] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Resolución de apertura | [ruta] | [fecha] | [tipo proceso] |
| Inventario/lista de créditos | [ruta] | [fecha] | [volumen] |
| Plan reorganización/acuerdo | [ruta] | [fecha] | [tipo propuesta] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/concursal:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. El rol habitual y los tipos de proceso son las partes más importantes — todo lo demás se construye desde ahí."

2. **Proponer primeras tareas:**
   - Si es deudor/administrador: "Quieres que analice la viabilidad de un proceso de reorganización para un caso concreto?"
   - Si es acreedor: "Quieres que revise una lista de créditos para comprobar la clasificación de tus créditos?"
   - Si es inversor: "Quieres que analice una oportunidad de adquisición de unidad productiva?"
   - General: "Quieres que revise los plazos concursales de un proceso en curso?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/concursal:entrevista-inicial --redo` para re-entrevista completa
   > - `/concursal:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: los **tipos de proceso** (la Ley 12 de 2016 sigue generando criterios jurisprudenciales), la **experiencia** (según gestionas más procesos), y las **herramientas** (según cambian los sistemas judiciales)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No confundir la reorganización con la liquidación.** Son dos procesos distintos con efectos, legitimación y trámites diferentes bajo la Ley 12 de 2016. Verificar siempre cuál cita el usuario.
- **No asumir que todos conocen la Ley 12 de 2016.** Sustituyó al régimen anterior de quiebra y concurso de acreedores del Código de Comercio; muchos profesionales aún razonan con el régimen previo. Preguntar experiencia real.
- **No inventar números de artículo ni plazos.** Para cualquier cita concreta de la Ley 12 de 2016 (artículo, plazo, mayoría) de la que no haya certeza, usar referencia genérica y marcar `[verificar]`.
- **No confundir garantía real con privilegio general.** La clasificación y prelación de créditos (Ley 12 de 2016 y Código Civil de Panamá) es fundamental y los errores se propagan a todo el proceso.
- **No olvidar los plazos concursales.** Son perentorios. El plazo para solicitar el proceso desde el conocimiento de la insolvencia es crítico [verificar] — su incumplimiento puede agravar la responsabilidad de los administradores.
- **No escribir experiencia inflada.** Si el profesional tiene poca experiencia concursal, decirlo en la configuración: `[EXPERIENCIA LIMITADA — pocos procesos concursales gestionados. El plugin ajustará las explicaciones y ofrecerá más contexto normativo.]`
- **No ignorar la responsabilidad de los administradores.** En cada proceso, preguntar si hay riesgo de conducta dolosa o fraudulenta y de responsabilidad por las deudas [verificar].
