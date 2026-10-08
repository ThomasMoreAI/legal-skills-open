---
name: entrevista-inicial-fiscal-521-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin fiscal. Aprende tu práctica y escribe CLAUDE.md a partir de tus obligaciones tributarias, procedimientos en curso y estrategia de planificación fiscal. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin fiscal", "onboarding fiscal", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/fiscal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: tax
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: últimas declaraciones fiscales relevantes, actas de inspección, consultas vinculantes DGT.
4. Extraer: régimen fiscal, obligaciones periódicas, procedimientos abiertos, estrategia de planificación.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/fiscal:entrevista-inicial
```

```
/fiscal:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Fiscal

## Propósito

Aprender cómo funciona *esta* práctica fiscal — qué forma jurídica tiene el contribuyente, qué impuestos le afectan, qué obligaciones periódicas gestiona, qué procedimientos tiene abiertos y qué planificación aplica. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica fiscal varía radicalmente según el tipo de contribuyente. Un autónomo en estimación directa simplificada tiene poco en común con un grupo fiscal consolidado. La entrevista identifica cuál es este antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`fiscal` es para quien gestiona obligaciones tributarias: declaraciones periódicas, planificación fiscal, procedimientos con la AEAT, recursos ante el TEAC/TEAR.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan la forma jurídica, el régimen fiscal y las obligaciones principales, con valores sensatos en todo lo demás. **15 minutos** añade el calendario completo de obligaciones, procedimientos en curso, estrategia de planificación y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil fiscal (forma jurídica, régimen, obligaciones periódicas, procedimientos, planificación), un calendario de obligaciones y análisis de consultas. Esta entrevista aprende cómo trabajas realmente — tus impuestos, tus plazos, tus procedimientos — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1 (contexto fiscal básico). Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes las últimas declaraciones del IS o del IVA? Pégalas o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo de la LIS, la LIRPF o la LIVA, o un plazo de la LGT, comprobar antes de escribirlo.

## La entrevista

### Apertura

> Voy a ayudarte con obligaciones tributarias, planificación fiscal, procedimientos con la AEAT y recursos ante los Tribunales Económico-Administrativos. Antes de nada, necesito saber qué tipo de contribuyente estamos hablando. Diez minutos.
>
> Después te pediré tres cosas: tus últimas declaraciones relevantes, algún acta de inspección si la hay, y consultas vinculantes de la DGT que hayas utilizado.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a fiscalista o asesor fiscal** — letrado/a, asesor fiscal colegiado, economista con práctica tributaria.
> 2. **Profesional no jurídico con acceso a asesor** — director financiero, controller, contable que consulta con asesoría fiscal.
> 3. **Profesional sin acceso regular a asesor fiscal** — autónomo, empresario que gestiona su fiscalidad.

Si es 2 o 3, explicar una vez: los outputs serán investigación para revisión profesional.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Contexto fiscal (3-4 min)

> **Cuál es la forma jurídica del contribuyente?** Este es el punto de partida — determina el impuesto principal, el régimen y las obligaciones.
>
> - Persona física (autónomo, profesional liberal)
> - Sociedad limitada (SL / SLU)
> - Sociedad anónima (SA)
> - Grupo fiscal consolidado (art. 55-75 LIS)
> - Comunidad de bienes / sociedad civil
> - Asociación / fundación
> - Otro (descríbelo)

Pausa. Después:

> **Régimen fiscal aplicable:**
> - **Impuesto sobre Sociedades:** régimen general, pyme (art. 101 LIS), empresa de reducida dimensión, ZEC, régimen especial de entidades sin ánimo de lucro?
> - **IRPF** (si persona física): estimación directa normal, simplificada, estimación objetiva (módulos)?
> - **IVA:** régimen general, simplificado, recargo de equivalencia, grupo de entidades, exento (art. 20 LIVA)?
>
> Actividades económicas (epígrafes IAE): cuáles?
> Delegación de la AEAT a la que pertenecéis?

### Parte 2: Obligaciones periódicas (3-4 min)

> **Qué modelos presentáis y con qué periodicidad?** Esto alimenta el calendario de obligaciones del plugin. Confirma los que apliquen:
>
> **IVA:**
> - Modelo 303 (trimestral/mensual)
> - Modelo 390 (resumen anual)
> - SII (Suministro Inmediato de Información) — estáis obligados o acogidos voluntariamente?
>
> **Retenciones:**
> - Modelo 111 (retenciones trabajo/profesionales, trimestral/mensual)
> - Modelo 115 (retenciones alquileres)
> - Modelo 123 (retenciones rendimientos capital mobiliario)
> - Modelos resumen anual: 190, 180, 193
>
> **Impuesto principal:**
> - Modelo 200/202 (IS — pago fraccionado y declaración anual)
> - Modelo 100 (IRPF)
>
> **Informativas:**
> - Modelo 347 (operaciones con terceros > 3.005,06 euros)
> - Modelo 349 (operaciones intracomunitarias)
> - Modelo 720 (bienes en el extranjero) — ojo: régimen sancionador declarado parcialmente inconstitucional por TJUE
> - Modelo 232 (operaciones vinculadas)

Pausa. Después:

> **Hay alguna obligación que se os haya pasado o que hayáis presentado fuera de plazo recientemente?** Esto me ayuda a calibrar las alertas del calendario.

### Parte 3: Impuestos autonómicos y locales (2-3 min)

> **En qué Comunidad Autónoma operáis principalmente?** Los impuestos cedidos y la normativa autonómica varían mucho.
>
> Impuestos que os afectan:
> - **ITP y AJD** (Impuesto sobre Transmisiones Patrimoniales y Actos Jurídicos Documentados) — hacéis operaciones sujetas con frecuencia?
> - **Impuesto sobre Sucesiones y Donaciones** — relevante para la práctica?
> - **Plusvalía municipal** (IIVTNU) — ojo: régimen recalculado tras STC 182/2021 y RDL 26/2021
> - **IBI** — tenéis inmuebles relevantes?
> - **IAE** — exentos por cifra de negocios < 1M euros?
> - **ICIO** (Impuesto sobre Construcciones, Instalaciones y Obras) — relevante?
>
> Operáis en territorio foral (País Vasco, Navarra)? Si es así, la normativa es completamente distinta.

### Parte 4: Procedimientos (2-3 min)

> **Tenéis procedimientos abiertos con la AEAT o los Tribunales Económico-Administrativos?** Esto me ayuda a entender vuestra exposición actual.
>
> - **Inspecciones en curso** — alcance general o parcial? Ejercicios afectados? Inspector actuario?
> - **Actas firmadas** (conformidad, disconformidad, con acuerdo) — alguna pendiente de resolución?
> - **Reclamaciones ante TEAR/TEAC** — cuántas, por qué conceptos, estado?
> - **Recursos contencioso-administrativos** contra resoluciones del TEAC — en curso?
> - **Procedimientos sancionadores** — alguno abierto?
>
> Hay algún criterio administrativo o resolución del TEAC especialmente relevante para vuestra práctica? (ej. un criterio sobre la deducibilidad de un gasto específico de vuestro sector)

### Parte 5: Planificación fiscal (2-3 min)

> **Qué instrumentos de planificación fiscal utilizáis o estáis considerando?** Esto alimenta el skill de análisis de oportunidades.
>
> - **Operaciones vinculadas** — tenéis política de precios de transferencia? Documentación master file / local file?
> - **Deducciones I+D+i** (art. 35 LIS) — las aplicáis? Tenéis informes motivados vinculantes?
> - **Patent box** (art. 23 LIS) — ingresos por cesión de activos intangibles?
> - **Incentivos Ley de Startups** (Ley 28/2022) — aplica el tipo reducido del 15%? Stock options?
> - **Reserva de capitalización** (art. 25 LIS) — la aplicáis?
> - **Reserva de nivelación** (art. 105 LIS, solo pymes) — la aplicáis?
> - **BINs** (bases imponibles negativas) — cuánto pendiente de compensar?
> - **Reestructuraciones** — habéis hecho fusiones, escisiones, canjes bajo el régimen especial (cap. VII, título VII LIS)?
>
> Tenéis alguna planificación en marcha que queráis que el plugin tenga en cuenta?

### Parte 6: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Últimas declaraciones relevantes** — el último modelo 200 (IS) o 100 (IRPF), y el último 303 (IVA). Me enseñan la realidad fiscal, no la teoría.
>
> 2. **Actas de inspección** — si las hay, la más reciente. Aprenderé qué criterios aplica la AEAT a vuestro sector y qué ajustes habéis aceptado o recurrido.
>
> 3. **Consultas vinculantes DGT** — las que hayáis utilizado en vuestra práctica. Me dicen qué cuestiones habéis tenido que resolver y qué criterio seguís.

**Cómo leer los documentos semilla:**

**Declaraciones:** Extraer cifras clave — base imponible, tipo efectivo, deducciones aplicadas, BINs compensadas. Comparar con lo declarado en la entrevista.

**Actas de inspección:** Identificar los ajustes propuestos, los aceptados y los recurridos. Extraer criterios de la AEAT relevantes para el sector.

**Consultas DGT:** Mapear las cuestiones planteadas y los criterios obtenidos. Estos son precedentes que el plugin debe conocer.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Fiscal

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Contribuyente] es una [forma jurídica]. Régimen fiscal: [régimen IS/IRPF].
Actividades IAE: [epígrafes]. Delegación AEAT: [delegación].
El equipo fiscal cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

**CCAA principal:** [comunidad autónoma]
**Territorio foral:** [sí/no — cuál]

---

## Quién usa este plugin

**Rol:** [Abogado/a fiscalista | Profesional con acceso a asesor | Profesional sin acceso a asesor]
**Contacto asesor fiscal:** [Nombre / despacho / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Calendario bajo demanda |

---

## Régimen fiscal

**Forma jurídica:** [tipo]
**IS/IRPF:** [régimen aplicable, tipo impositivo]
**IVA:** [régimen, periodicidad, SII sí/no]
**Ejercicios abiertos a inspección:** [ejercicios no prescritos]

---

## Calendario de obligaciones

| Modelo | Concepto | Periodicidad | Plazo | Notas |
|---|---|---|---|---|
| 303 | IVA | [trimestral/mensual] | 20 del mes siguiente (30 enero 4T) | |
| 111 | Retenciones trabajo | [trimestral/mensual] | 20 del mes siguiente | |
| 200 | IS declaración anual | Anual | 25 días tras 6 meses cierre ejercicio | |
| [modelo] | [concepto] | [periodicidad] | [plazo] | |

---

## Impuestos autonómicos y locales

| Impuesto | Aplica | CCAA / municipio | Notas |
|---|---|---|---|
| ITP y AJD | [sí/no] | [CCAA] | [tipo autonómico] |
| Sucesiones y Donaciones | [sí/no] | [CCAA] | [bonificaciones autonómicas] |
| Plusvalía (IIVTNU) | [sí/no] | [municipio] | Post STC 182/2021 |
| IBI | [sí/no] | [municipio] | |
| IAE | [exento/obligado] | | Cifra negocios [cifra] |

---

## Procedimientos abiertos

| Tipo | Ejercicios/Concepto | Estado | Órgano | Cuantía | Notas |
|---|---|---|---|---|---|
| [inspección/acta/reclamación/recurso] | [detalle] | [estado] | [AEAT/TEAR/TEAC/TSJ/TS] | [euros] | |

---

## Planificación fiscal

| Instrumento | Estado | Detalle |
|---|---|---|
| Operaciones vinculadas | [aplica/no] | [documentación TP: sí/no] |
| Deducciones I+D+i | [aplica/no] | [informes motivados: sí/no] |
| Patent box | [aplica/no] | [detalle] |
| Ley Startups | [aplica/no] | [detalle] |
| Reserva capitalización | [aplica/no] | [importe] |
| Reserva nivelación | [aplica/no] | [importe] |
| BINs pendientes | [importe] | [ejercicios origen] |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Declaración periódica rutinaria | [responsable] | [nombre] | Discrepancia material |
| Requerimiento AEAT | [responsable] | [nombre] | Siempre |
| Inicio inspección | — | [GC + fiscal + dirección] | Siempre |
| Acta de disconformidad | — | [GC + fiscal] | Siempre |
| Planificación fiscal > [umbral] | [responsable] | [nombre] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Última declaración IS/IRPF | [ruta] | [fecha] | Ejercicio [año] |
| Acta de inspección | [ruta] | [fecha] | [concepto] |
| Consultas DGT | [ruta] | [fecha] | [referencias] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/fiscal:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. El calendario de obligaciones y los procedimientos abiertos son las partes a revisar con más cuidado."

2. **Proponer primeras tareas:**
   - "Quieres que revise si tenéis algún plazo fiscal próximo que requiera atención?"
   - "Quieres que analice una consulta vinculante de la DGT relevante para vuestro sector?"
   - "Tenéis algún acta de inspección que queráis que revise?"
   - Si hay BINs pendientes: "Quieres que analice la estrategia óptima de compensación de BINs?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/fiscal:entrevista-inicial --redo` para re-entrevista completa
   > - `/fiscal:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: el **calendario de obligaciones** (cuando cambian las periodicidades o se añaden modelos), los **procedimientos abiertos** (según se resuelven o abren nuevos), y la **planificación fiscal** (según cambia la estrategia o la normativa)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir el régimen fiscal.** Una SL no siempre está en régimen general de IS — puede ser pyme, puede tributar en territorio foral, puede estar en ZEC. Preguntar siempre.
- **No confundir obligaciones estatales con autonómicas.** El ITP lo gestiona la CCAA, no la AEAT. La plusvalía es municipal. No mezclar administraciones.
- **No dar por hecho que el SII aplica.** Solo es obligatorio para grandes empresas (volumen de operaciones > 6.010.121,04 euros), grupos de IVA e inscritos en REDEME. No asumir que todos lo tienen.
- **No olvidar la prescripción.** Los ejercicios prescritos (4 años, art. 66 LGT) no pueden ser objeto de comprobación salvo excepciones. Pero la prescripción se interrumpe — verificar si hay actos interruptivos.
- **No escribir un calendario con plazos genéricos.** Los plazos reales dependen de si es gran empresa (mensual) o no (trimestral), si está en SII, si es territorio foral. Personalizar siempre.
- **No ignorar la normativa foral.** Si el contribuyente opera en País Vasco o Navarra, la normativa fiscal es completamente distinta (Concierto/Convenio). No aplicar normativa estatal a contribuyentes forales.
