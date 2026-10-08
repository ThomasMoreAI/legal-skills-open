---
name: entrevista-inicial-fiscal-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin fiscal. Aprende tu práctica y escribe CLAUDE.md a partir de tus obligaciones tributarias, procedimientos en curso y estrategia de planificación fiscal. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin fiscal", "onboarding fiscal", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/fiscal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: tax
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: últimas declaraciones fiscales relevantes, resoluciones de alcance de la DGI, criterios o consultas de la DGI.
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

Aprender cómo funciona *esta* práctica fiscal — qué forma jurídica tiene el contribuyente, qué tributos le afectan, qué obligaciones periódicas gestiona, qué procedimientos tiene abiertos y qué planificación aplica. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

La práctica fiscal varía radicalmente según el tipo de contribuyente. Una persona natural asalariada tiene poco en común con una sociedad bajo régimen SEM o una empresa de la Zona Libre de Colón. La entrevista identifica cuál es este antes de nada. Y en Panamá, lo primero siempre es el **principio de territorialidad**: solo tributa la renta de fuente panameña.

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

> **`fiscal` es para quien gestiona obligaciones tributarias: declaraciones periódicas, planificación fiscal, procedimientos con la DGI, recursos ante el Tribunal Administrativo Tributario (TAT).** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan la forma jurídica, el régimen fiscal y las obligaciones principales, con valores sensatos en todo lo demás. **15 minutos** añade el calendario completo de obligaciones, procedimientos en curso, estrategia de planificación y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil fiscal (forma jurídica, régimen, obligaciones periódicas, procedimientos, planificación), un calendario de obligaciones y análisis de consultas. Esta entrevista aprende cómo trabajas realmente — tus tributos, tus plazos, tus procedimientos — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1 (contexto fiscal básico). Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes las últimas declaraciones del ISR o del ITBMS? Pégalas o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo del Código Fiscal, una norma de ITBMS o un plazo de procedimiento, comprobar antes de escribirlo.

## La entrevista

### Apertura

> Voy a ayudarte con obligaciones tributarias, planificación fiscal, procedimientos con la DGI y recursos ante el Tribunal Administrativo Tributario. Antes de nada, necesito saber qué tipo de contribuyente estamos hablando y cuál es la fuente de sus rentas (panameña o extranjera). Diez minutos.
>
> Después te pediré tres cosas: tus últimas declaraciones relevantes, alguna resolución de alcance de la DGI si la hay, y los criterios o consultas de la DGI que hayas utilizado.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a tributarista o contador público autorizado (CPA)** — letrado/a idóneo, CPA con práctica tributaria.
> 2. **Profesional no jurídico con acceso a asesor** — director financiero, controller, contador que consulta con asesoría fiscal.
> 3. **Profesional sin acceso regular a asesor fiscal** — empresario que gestiona su propia fiscalidad.

Si es 2 o 3, explicar una vez: los outputs serán investigación para revisión profesional.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Contexto fiscal (3-4 min)

> **Cuál es la forma jurídica del contribuyente?** Este es el punto de partida — determina el tributo principal, el régimen y las obligaciones.
>
> - Persona natural (asalariado, profesional independiente)
> - Sociedad anónima (S.A. — Ley 32 de 1927)
> - Sociedad de responsabilidad limitada (S. de R.L.)
> - Fundación de interés privado (Ley 25 de 1995)
> - Empresa bajo régimen de zona especial (SEM, Ciudad del Saber, ZLC, Panamá Pacífico)
> - Asociación / entidad sin fines de lucro
> - Otro (descríbelo)

Pausa. Después:

> **Régimen fiscal aplicable:**
> - **ISR:** régimen general, CAIR (si ingresos gravables > 1,5 millones B/.), no contribuyente, régimen de zona especial? [verificar]
> - **ITBMS:** contribuyente ordinario, agente de retención, no obligado, operaciones exentas?
> - **Fuente de las rentas:** ¿toda fuente panameña, o hay renta de fuente extranjera (no gravada)? ¿Operaciones de reexportación / servicios al exterior?
>
> Actividad económica principal: cuál?
> ¿Tenéis RUC y aviso de operación al día?

### Parte 2: Obligaciones periódicas (3-4 min)

> **Qué declaraciones presentáis y con qué periodicidad?** Esto alimenta el calendario de obligaciones del plugin. Confirma las que apliquen:
>
> **ITBMS:**
> - Formulario 430 (declaración mensual) [verificar]
> - Retenciones de ITBMS (si sois agente de retención) [verificar]
>
> **Retenciones del ISR:**
> - Planilla 03 (retenciones sobre salarios) [verificar]
> - Retención a no residentes / pagos al exterior gravados de fuente panameña
> - Retención sobre dividendos y complementario [verificar]
>
> **Impuesto principal:**
> - Formulario 1 (declaración jurada del ISR — jurídicas o naturales) [verificar]
> - Estimada del ISR y CAIR [verificar]
>
> **Otras:**
> - Tasa única de sociedades / fundaciones [verificar]
> - Planilla de la Caja de Seguro Social (CSS)
> - Informe de precios de transferencia (informe 930) si hay partes relacionadas [verificar]

Pausa. Después:

> **Hay alguna obligación que se os haya pasado o que hayáis presentado fuera de plazo recientemente?** Esto me ayuda a calibrar las alertas del calendario.

### Parte 3: Tributos municipales y otros (2-3 min)

> **En qué municipio o municipios operáis?** Los tributos municipales y las tasas varían.
>
> Tributos que os afectan:
> - **Impuesto de aviso de operación** — pagado y al día? [verificar]
> - **Impuesto de inmuebles** — tenéis inmuebles relevantes? ¿exoneración vigente? [verificar]
> - **Tasas y arbitrios municipales** — relevantes?
> - **Impuesto de timbre** — operaciones sujetas? [verificar]
>
> Operáis bajo algún régimen de zona especial (SEM, Ciudad del Saber, Zona Libre de Colón, Panamá Pacífico)? Si es así, los incentivos y exenciones cambian sustancialmente.

### Parte 4: Procedimientos (2-3 min)

> **Tenéis procedimientos abiertos con la DGI o el Tribunal Administrativo Tributario?** Esto me ayuda a entender vuestra exposición actual.
>
> - **Fiscalizaciones en curso** — alcance? Períodos afectados? Tributos?
> - **Resoluciones de alcance / liquidaciones adicionales** — alguna pendiente de resolución?
> - **Recursos de reconsideración** ante la DGI — cuántos, por qué conceptos, estado?
> - **Apelaciones ante el TAT** — en curso?
> - **Demandas contencioso-administrativas** ante la Sala Tercera de la CSJ — en curso?
> - **Procedimientos sancionadores** (morosidad, defraudación fiscal) — alguno abierto?
>
> Hay algún criterio de la DGI o fallo del TAT especialmente relevante para vuestra práctica? (ej. un criterio sobre la fuente de una renta o la deducibilidad de un gasto de vuestro sector)

### Parte 5: Planificación fiscal (2-3 min)

> **Qué instrumentos de planificación fiscal utilizáis o estáis considerando?** Esto alimenta el skill de análisis de oportunidades.
>
> - **Principio de territorialidad** — tenéis una segregación clara de renta de fuente panameña vs extranjera? ¿prorrateo de gastos correctamente documentado?
> - **Régimen de zona especial** (SEM, Ciudad del Saber, ZLC, Panamá Pacífico) — aplicáis incentivos? ¿cumplís los requisitos de elegibilidad? [verificar]
> - **Precios de transferencia** — tenéis estudio de PT e informe 930 con partes relacionadas? [verificar]
> - **Arrastre de pérdidas** — cuánto pendiente de aplicar? ¿dentro del límite anual? [verificar]
> - **Incentivos sectoriales** (turismo, agro, energía, forestal) — aplican? [verificar]
> - **CDI** — operáis con países con convenio para evitar la doble imposición? [verificar]
>
> Tenéis alguna planificación en marcha que queráis que el plugin tenga en cuenta?

### Parte 6: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Últimas declaraciones relevantes** — la última declaración jurada del ISR (formulario 1) y la última declaración del ITBMS (formulario 430). Me enseñan la realidad fiscal, no la teoría.
>
> 2. **Resoluciones de alcance de la DGI** — si las hay, la más reciente. Aprenderé qué criterios aplica la DGI a vuestro sector y qué ajustes habéis aceptado o recurrido.
>
> 3. **Criterios / consultas de la DGI** — los que hayáis utilizado en vuestra práctica. Me dicen qué cuestiones habéis tenido que resolver y qué criterio seguís.

**Cómo leer los documentos semilla:**

**Declaraciones:** Extraer cifras clave — renta gravable, tarifa efectiva, segregación de fuente extranjera, créditos de ITBMS, pérdidas aplicadas. Comparar con lo declarado en la entrevista.

**Resoluciones de alcance:** Identificar los ajustes propuestos, los aceptados y los recurridos. Extraer criterios de la DGI relevantes para el sector.

**Criterios DGI:** Mapear las cuestiones planteadas y los criterios obtenidos. Estos son precedentes que el plugin debe conocer.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Fiscal (Panamá)

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Contribuyente] es una [forma jurídica]. Régimen fiscal: [régimen ISR / CAIR / zona especial].
Actividad principal: [actividad]. RUC: [RUC]. Administración: DGI.
El equipo fiscal cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

**Municipio principal:** [municipio]
**Régimen de zona especial:** [SEM / Ciudad del Saber / ZLC / Panamá Pacífico / ninguno]
**Fuente de las rentas:** [solo panameña / panameña + extranjera no gravada]

---

## Quién usa este plugin

**Rol:** [Abogado/a tributarista | CPA | Profesional con acceso a asesor | Profesional sin acceso a asesor]
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
**ISR:** [régimen aplicable, tarifa, CAIR sí/no]
**ITBMS:** [régimen, periodicidad, agente de retención sí/no]
**Territorialidad:** [segregación de renta panameña vs extranjera]
**Períodos abiertos a fiscalización:** [períodos no prescritos]

---

## Calendario de obligaciones

| Formulario | Concepto | Periodicidad | Plazo | Notas |
|---|---|---|---|---|
| 430 | ITBMS | Mensual | 15 días siguientes al mes [verificar] | |
| 03 | Retenciones ISR salarios | Mensual | [plazo] [verificar] | |
| 1 | Declaración jurada ISR | Anual | 31 de marzo (prórroga 1 mes) [verificar] | |
| [formulario] | [concepto] | [periodicidad] | [plazo] | |

---

## Tributos municipales

| Tributo | Aplica | Municipio | Notas |
|---|---|---|---|
| Aviso de operación | [sí/no] | [municipio] | [2% capital, tope] [verificar] |
| Impuesto de inmuebles | [sí/no] | [ubicación] | [exoneración vigente] [verificar] |
| Tasas / arbitrios | [sí/no] | [municipio] | |

---

## Procedimientos abiertos

| Tipo | Períodos/Concepto | Estado | Órgano | Cuantía | Notas |
|---|---|---|---|---|---|
| [fiscalización/alcance/reconsideración/apelación] | [detalle] | [estado] | [DGI/TAT/Sala Tercera CSJ] | [B/.] | |

---

## Planificación fiscal

| Instrumento | Estado | Detalle |
|---|---|---|
| Territorialidad (segregación fuente) | [aplica/no] | [documentación de prorrateo] |
| Régimen de zona especial | [aplica/no] | [SEM / Ciudad del Saber / ZLC / Panamá Pacífico] |
| Precios de transferencia | [aplica/no] | [estudio PT / informe 930: sí/no] |
| Arrastre de pérdidas | [importe] | [períodos origen] |
| Incentivos sectoriales | [aplica/no] | [detalle] |
| CDI | [aplica/no] | [países] |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Declaración periódica rutinaria | [responsable] | [nombre] | Discrepancia material |
| Requerimiento DGI | [responsable] | [nombre] | Siempre |
| Inicio fiscalización | — | [legal + fiscal + dirección] | Siempre |
| Resolución de alcance | — | [legal + fiscal] | Siempre |
| Planificación fiscal > [umbral] | [responsable] | [nombre] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Última declaración ISR | [ruta] | [fecha] | Período [año] |
| Resolución de alcance DGI | [ruta] | [fecha] | [concepto] |
| Criterios DGI | [ruta] | [fecha] | [referencias] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/fiscal:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. El calendario de obligaciones, la segregación de fuente y los procedimientos abiertos son las partes a revisar con más cuidado."

2. **Proponer primeras tareas:**
   - "Quieres que revise si tenéis algún plazo fiscal próximo que requiera atención?"
   - "Quieres que analice un criterio de la DGI relevante para vuestro sector?"
   - "Tenéis alguna resolución de alcance que queráis que revise?"
   - Si hay pérdidas pendientes: "Quieres que analice la estrategia óptima de aplicación de pérdidas?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/fiscal:entrevista-inicial --redo` para re-entrevista completa
   > - `/fiscal:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: el **calendario de obligaciones** (cuando cambian las periodicidades o se añaden formularios), los **procedimientos abiertos** (según se resuelven o abren nuevos), y la **planificación fiscal** (según cambia la estrategia o la normativa)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir la fuente de la renta.** Lo primero en Panamá es el principio de territorialidad: la renta de fuente extranjera no tributa. Verificar siempre la fuente antes de aplicar el ISR.
- **No asumir el régimen fiscal.** Una S.A. no siempre está en régimen general — puede estar bajo CAIR, bajo régimen SEM, en Ciudad del Saber, Zona Libre de Colón o Panamá Pacífico. Preguntar siempre.
- **No confundir obligaciones nacionales con municipales.** El aviso de operación y muchas tasas son municipales, no de la DGI. No mezclar administraciones.
- **No dar por hecho que aplica el CAIR.** El Cálculo Alternativo del ISR solo aplica cuando los ingresos gravables superan 1.500.000 B/. [verificar]. No asumir que todos lo tienen.
- **No olvidar la prescripción.** Verificar el plazo de prescripción aplicable conforme al Código Fiscal y si hay actos que lo interrumpan. [verificar]
- **No escribir un calendario con plazos genéricos.** Los plazos reales dependen del régimen (general / zona especial), de la periodicidad de ITBMS y de si hay prórroga de la declaración jurada. Personalizar siempre.
- **No ignorar el régimen de zona especial.** Si el contribuyente opera bajo SEM, Ciudad del Saber, ZLC o Panamá Pacífico, las exenciones y obligaciones son distintas. No aplicar el régimen general por defecto.
