---
name: entrevista-inicial-startups-3696-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de startups — aprende la fase, estructura societaria, pacto de accionistas, equity, rondas y equipo de tu startup y escribe el perfil de práctica en CLAUDE.md. Úsalo en la primera ejecución, cuando CLAUDE.md no exista o tenga marcadores pendientes, o cuando el usuario diga "configurar startups", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: pacto social, pacto de accionistas, cap table, contratos de empleados. Leer todos los que se proporcionen.
4. Extraer: estructura societaria, cláusulas del pacto, distribución de equity, régimen laboral.
5. Migración: si existe un CLAUDE.md poblado en la ruta cache pero no en config, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integrations`

Re-ejecuta la verificación de integraciones y actualiza `## Integraciones disponibles`. No repite la entrevista.

```
/startups:entrevista-inicial
```

```
/startups:entrevista-inicial --check-integrations
```

---

# Entrevista Inicial: Startups

## Propósito

Aprender cómo está estructurada *esta* startup — en qué fase se encuentra, cómo está organizada societariamente, si tiene pacto de accionistas, cómo gestiona el equity y las rondas, y qué situación tiene con el equipo. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` para que todos los skills lean desde la misma base.

Cada startup es distinta. Una S.A. recién constituida con dos socios no tiene nada en común con una startup en Serie A con 50 empleados y tres rondas cerradas. La entrevista determina en qué punto está antes de todo lo demás.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → saludar y ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Comprobar el perfil de empresa compartido

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo, confirmar en una línea, saltar preguntas de empresa.
- **Si no existe:** Hacer las preguntas de empresa, escribir perfil compartido, continuar con preguntas específicas.

## Antes de empezar la entrevista

> **`startups` es para quienes trabajan con startups: constitución, pactos de accionistas, equity, rondas de inversión, equipo.** ¿No es tu área? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu rol, la fase de la startup y si hay sociedad constituida (S.A. o S. de R.L.), con valores por defecto en el resto. **15 minutos** añade el pacto de accionistas, la cap table, el historial de rondas y la situación del equipo.
>
> ¿Rápido o completo? (Puedes ampliar con `/startups:entrevista-inicial --completo`.)

Esperar a que el usuario elija.

## Después de elegir rápido o completo

> "Este módulo mantiene tu perfil de startup (estructura societaria, pacto de accionistas, equity, rondas, equipo). La entrevista aprende cómo está tu startup realmente y lo escribe en un archivo de texto plano. Todo se puede cambiar después."
>
> "La configuración se construye solo desde tus respuestas y los documentos semilla. No lee tu historial de Claude ni otras conversaciones."
>
> "¿Listo?"

**Ruta rápida:** Parte 0 (rol) + fase de la startup + sociedad constituida sí/no. Config con `[POR DEFECTO]`. Cerrar: "Hecho. Ejecuta `/startups:entrevista-inicial --completo` cuando quieras."

**Ruta completa:** flujo completo abajo.

## Ritmo de la entrevista

- **Asumir que la respuesta existe en algún sitio.** Pacto social, pacto de accionistas, cap table — pedir enlace o pegado antes de hacer teclear.
- **2-3 preguntas por turno máximo**, contando subpartes.
- **Pausar para respuestas reales.** Documentos semilla, detalles del pacto — "Esta necesita respuesta escrita — espero."
- **Para documentos semilla:** "Pega el contenido, comparte ruta o URL, o di 'saltar por ahora.'"
- **Antes de escribir el perfil:** listar huecos, preguntar si rellenar ahora o dejar pendiente.
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

**Verificar hechos legales.** Tasa única anual de la sociedad, plazos de inscripción en el Registro Público, agente residente obligatorio — verificar antes de escribir.

## La entrevista

### Apertura

> Voy a ayudarte con la estructura societaria, pactos de accionistas, equity, rondas de inversión y gestión del equipo. Antes necesito saber en qué punto está tu startup. Diez minutos.
>
> Después te pediré que me enseñes el pacto social, el pacto de accionistas si lo hay, la cap table y algún contrato de empleado tipo. Aprenderé más de esos documentos que de cualquier descripción.

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién va a usar este módulo en el día a día?
>
> 1. **Fundador/CEO** — estoy montando o dirigiendo la startup.
> 2. **Abogado de startups** — asesoro a startups (in-house o externo).
> 3. **Inversionista** — evalúo startups para invertir.

Esto cambia el enfoque de los resultados:
- **Fundador:** framing práctico, orientado a decisión, con alertas de "consulta con tu abogado" antes de pasos con consecuencias jurídicas.
- **Abogado:** framing técnico-jurídico completo, redacción directa de documentos.
- **Inversionista:** framing de due diligence, detección de banderas rojas.

Si es fundador sin abogado:

> Puedes usar todo el módulo. Dos cosas cambian: (1) enmarco los resultados como investigación, no como asesoramiento, (2) pauso antes de pasos con consecuencias jurídicas — firmar pactos, modificar el pacto social, emitir equity. Un abogado mercantilista unas horas en los momentos clave suele ser más barato que el error.

#### ¿Qué hay conectado?

Verificar integraciones disponibles (almacenamiento, Slack, tareas programadas). Reportar estado real.

### Parte 1: La Startup

> "Cuéntame de la startup. Pega un enlace a la web o al pitch deck, o dame la versión de un párrafo."

- **Fase:** ¿En qué momento estáis?
  - Ideación (solo una idea)
  - Pre-seed (MVP, primeros usuarios)
  - Seed (producto lanzado, primeros ingresos o métricas)
  - Serie A (crecimiento, equipo formado)
  - Growth (escalando)
- **Sector:** ¿Qué sector? (Tech, fintech, healthtech, deeptech, marketplace, SaaS, otro.)
- **Modelo de negocio:** ¿Cómo ganáis o pensáis ganar dinero? (SaaS, marketplace, transaccional, licencia, hardware, servicios.)

### Parte 2: Estructura Societaria

*(Esto alimenta todos los skills que trabajan con la sociedad — sin saber cómo está constituida, no se puede redactar nada.)*

> "¿Tenéis sociedad constituida (S.A. o S. de R.L.)?"

- **Sociedad constituida:** Sí/No. Si sí:
  - **Forma jurídica:** S.A. o S. de R.L.
  - **Denominación social y RUC.**
  - **Capital social / capital autorizado:** ¿Cuánto? ¿Acciones emitidas y pagadas?
  - **Socios/accionistas:** ¿Cuántos? Porcentajes aproximados.
  - **Junta directiva / administración:** ¿Quiénes son los directores y dignatarios (S.A.) o administradores (S. de R.L.)?
  - **Agente residente:** ¿Qué abogado o firma?
  - **Fecha de constitución.**
- **Si no:** ¿Pensáis constituir? ¿S.A., S. de R.L., otro? ¿Algún motivo para no haberlo hecho aún?
- **Vesting:** ¿Los socios fundadores tienen vesting o reverse vesting? ¿Con cliff? ¿Plazo?

Si la fase es ideación y no hay sociedad: "No es imprescindible constituir antes de validar la idea, pero ten en cuenta que sin sociedad no hay personalidad jurídica separada — los socios responden con su patrimonio personal de lo que hagan como 'empresa'. El momento habitual es cuando entra dinero externo o cuando firmáis contratos relevantes."

### Parte 3: Pacto de Accionistas

*(Esto alimenta `/startups:pacto-accionistas` — las cláusulas actuales son el punto de partida para cualquier modificación o negociación.)*

> "¿Tenéis pacto de accionistas? Pega el contenido o comparte ruta."

- **Existe:** Sí/No. Si sí:
  - **Cláusulas principales:** ¿Qué cubre? (Dedicación, no competencia, vesting, drag-along, tag-along, anti-dilución, valoración, derecho de adquisición preferente, cláusula de punto muerto/deadlock, régimen de salida.)
  - **Firmantes:** ¿Todos los accionistas? ¿Incluye inversionistas?
  - **Fecha:** ¿Cuándo se firmó? ¿Se ha actualizado?
- **Si no:** "¿Sois más de un socio? Si sí, un pacto de accionistas no es obligatorio pero es el documento más importante que puede tener una startup con varios fundadores. Sin él, cualquier desacuerdo se resuelve con las reglas por defecto de la Ley 32 de 1927 y el pacto social, que raramente son las que queréis."

### Parte 4: Equity e Incentivos

*(Esto alimenta `/startups:equity` — el plan actual y la cap table son la base para cualquier simulación o nueva emisión.)*

> "¿Cómo está distribuido el equity? Si tienes cap table, pégala o comparte ruta."

- **Distribución actual:** Porcentajes de los socios principales.
- **Stock options / phantom shares:** ¿Tenéis un plan de incentivos? ¿De qué tipo?
  - Stock options: ¿aprobadas en junta? ¿Con qué valoración de ejercicio?
  - Phantom shares: ¿liquidación ligada a evento (venta, salida a bolsa)?
  - Warrants, SAR, otros.
- **Pool de opciones:** ¿Hay un pool reservado? ¿Qué porcentaje del capital?
- **Vesting de opciones/phantoms:** ¿Plazo estándar? ¿Cliff? ¿Aceleración por cambio de control?

Si no hay plan: "Si tenéis empleados clave sin equity, un plan de phantom shares es la forma más limpia — no requiere emitir acciones ni ir al notario cada vez. ¿Quieres que te ayude a diseñar uno?"

### Parte 5: Rondas de Inversión

*(Esto alimenta `/startups:ronda` — el historial de financiación y los términos anteriores condicionan cualquier ronda futura.)*

> "¿Habéis levantado inversión? Cuéntame el historial."

- **Historial de financiación:** ¿Cuántas rondas? Para cada una:
  - Tipo (FFF, pre-seed, seed, Serie A, deuda convertible, SAFE.)
  - Importe (USD.)
  - Valoración (pre-money.)
  - Inversionistas principales.
  - Instrumento (emisión de acciones, nota convertible, SAFE adaptado.)
- **Próxima ronda prevista:** ¿Estáis levantando? ¿Cuándo? ¿Objetivo de importe?
- **Inversionistas actuales:** ¿Tienen derechos especiales? (Anti-dilución, preferencia de liquidación, puestos en la junta directiva, veto.)
- **Régimen de valores:** ¿La colocación podría calificar como oferta pública sujeta a la SMV? ¿Se ha verificado alguna exención de oferta privada?

Si no han levantado: "¿Estáis financiando con recursos propios (bootstrapping) o pensáis levantar? Si vais a levantar, el momento de preparar la documentación es antes de hablar con inversionistas, no después."

### Parte 6: Equipo

*(Esto alimenta `/startups:equipo` — el régimen laboral, los contratos y la zona condicionan las contrataciones y los despidos.)*

> "¿Cuánta gente sois y cómo estáis organizados?"

- **Empleados:** ¿Cuántos? ¿Con contrato laboral?
- **Pasantes:** ¿Tenéis pasantes? ¿A través de universidad/convenio?
- **Contratistas independientes:** ¿Trabajáis con colaboradores externos? ¿Cuántos? (Alerta de relación laboral encubierta si es relevante.)
- **Régimen laboral:** ¿Aplica el Código de Trabajo general o un régimen especial de zona (SEM, Panamá Pacífico, Ciudad del Saber)?
- **Fundadores como trabajadores:** ¿Los fundadores cobran salario? ¿Están inscritos en la CSS?
- **Teletrabajo:** ¿Tenéis acuerdo de teletrabajo? (Ley 126 de 2020.)
- **Personal extranjero:** ¿Hay empleados extranjeros? ¿Con permiso de trabajo y visa? (Recordar la proporción de trabajadores nacionales exigida [verificar].)

### Parte 7: Documentos semilla

> Quiero ver cuatro cosas:
>
> 1. **Pacto social.** El de la escritura de constitución (o la última modificación). Aprenderé la estructura de gobierno, objeto social, régimen de transmisión de acciones.
>
> 2. **Pacto de accionistas.** Si existe. Aprenderé las cláusulas, quién firmó, qué derechos tienen los inversionistas.
>
> 3. **Cap table.** La distribución actual del capital. Aprenderé las rondas pasadas, la dilución y los compromisos.
>
> 4. **Contratos de empleados tipo.** Uno o dos representativos. Aprenderé el modelo, las cláusulas de confidencialidad/PI, las condiciones.

**Cómo leer los documentos semilla:**

**Pacto social:** Extraer objeto social, junta directiva, régimen de transmisión de acciones, mayorías reforzadas. Comparar con lo que el usuario ha dicho.

**Pacto de accionistas:** Mapear cada cláusula. Deltas con el pacto social son interesantes — "el pacto dice drag-along pero el pacto social no lo refleja — ¿es ejecutable?"

**Cap table:** Verificar que los porcentajes suman 100%. Extraer dilución por ronda. Identificar derechos especiales de inversionistas.

**Contratos:** Extraer modelo (indefinido, por tiempo definido, por obra), cláusulas de PI/confidencialidad/no competencia, condiciones económicas.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica: Startups

*Escrito por la entrevista inicial el [FECHA]. Edita este archivo directamente.*

---

## Quiénes somos

*Datos de empresa de `perfil-empresa.md` — edita allí para cambiar en todos los módulos.*

**Startup:** [Nombre]
**Fase:** [Ideación / Pre-seed / Seed / Serie A / Growth]
**Sector:** [PENDIENTE]
**Modelo de negocio:** [PENDIENTE]

---

## Quién usa esto

**Rol:** [Fundador / Abogado de startups / Inversionista]
**Contacto letrado:** [PENDIENTE]

---

## Integraciones disponibles

| Integración | Estado | Alternativa |
|---|---|---|
| Almacenamiento | [PENDIENTE] | Documentos locales |
| Slack | [PENDIENTE] | Notificaciones en línea |
| Tareas programadas | [PENDIENTE] | Recordatorios manuales |

---

## Estructura Societaria

**Sociedad constituida:** [Sí/No]
**Forma jurídica:** [S.A. / S. de R.L.]
**Denominación y RUC:** [PENDIENTE]
**Capital social / autorizado:** [PENDIENTE]
**Socios/accionistas:** [lista con porcentajes]
**Junta directiva / administración:** [PENDIENTE]
**Agente residente:** [PENDIENTE]
**Fecha constitución:** [PENDIENTE]
**Vesting fundadores:** [Sí — detalles / No / PENDIENTE]

---

## Pacto de Accionistas

**Existe:** [Sí/No]
**Firmantes:** [PENDIENTE]
**Fecha:** [PENDIENTE]
**Cláusulas principales:**

| Cláusula | Estado | Detalle |
|---|---|---|
| Dedicación exclusiva | [Sí/No] | |
| No competencia | [Sí/No] | |
| Vesting / reverse vesting | [Sí/No] | |
| Drag-along | [Sí/No] | |
| Tag-along | [Sí/No] | |
| Anti-dilución | [Sí/No] | |
| Derecho adquisición preferente | [Sí/No] | |
| Deadlock | [Sí/No] | |
| Régimen de salida | [Sí/No] | |

---

## Equity e Incentivos

**Distribución actual:** [cap table resumida]
**Plan de incentivos:** [Stock options / Phantom shares / Ninguno / PENDIENTE]
**Pool reservado:** [% / No / PENDIENTE]
**Vesting estándar:** [PENDIENTE]

---

## Rondas de Inversión

| Ronda | Importe (USD) | Valoración pre | Instrumento | Inversionistas principales |
|---|---|---|---|---|
| [PENDIENTE] | | | | |

**Próxima ronda:** [PENDIENTE]
**Régimen de valores (SMV):** [Oferta privada / verificar exención / PENDIENTE]
**Derechos especiales inversionistas:** [PENDIENTE]

---

## Equipo

**Empleados:** [N]
**Pasantes:** [N]
**Contratistas independientes:** [N]
**Régimen laboral:** [Código de Trabajo / régimen especial de zona / PENDIENTE]
**Fundadores en planilla:** [Sí/No — inscritos en CSS]
**Acuerdo teletrabajo:** [Sí/No/PENDIENTE]

---

## Escalación

| Tipo | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Contratación empleado | [fundador/RRHH] | [abogado] | Cláusulas PI, no competencia |
| Modificación pacto social | [abogado] | [junta] | Siempre |
| Ronda de inversión | [CEO] | [abogado + board] | Siempre |
| Conflicto entre socios | — | [abogado + mediador] | Siempre |
| Inspección de MITRADEL | — | [abogado laboral] | Siempre |

---

## Documentos semilla

| Documento | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Pacto social | [PENDIENTE] | | |
| Pacto de accionistas | [PENDIENTE] | | |
| Cap table | [PENDIENTE] | | |
| Contratos empleados | [PENDIENTE] | | |

---

## Resultados

**Carpeta de resultados:** [PENDIENTE]
**Convención de nombres:** [PENDIENTE]

**Encabezado de documentos de trabajo:**

- Si el rol es Abogado: `PRIVILEGIADO Y CONFIDENCIAL — TRABAJO PROFESIONAL`
- Si el rol es Fundador/Inversionista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/startups:entrevista-inicial --redo`*
```

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

> **Esto es lo que hago bien en startups:**
>
> - **Revisar o redactar un pacto de accionistas** — Cláusula por cláusula, adaptado a vuestra fase. Prueba: `/startups:pacto-accionistas`
> - **Diseñar un plan de equity** — Stock options o phantom shares, con simulación de dilución. Prueba: `/startups:equity`
> - **Preparar una ronda** — Term sheet, documentación, cap table pro-forma. Prueba: `/startups:ronda`
> - **Revisar contratos de equipo** — Empleados, contratistas, cláusulas de PI. Prueba: `/startups:equipo`
> - **Constituir la sociedad** — Checklist y documentación. Prueba: `/startups:constitucion`
>
> **Mi sugerencia:** Si tenéis pacto de accionistas, ejecuta `/startups:pacto-accionistas` para una revisión — es donde están los problemas que no se ven hasta que explotan.

1. **Mostrar resumen.** "Esto es lo que he entendido. Revisa la cap table y el pacto — ¿lo tengo bien?"
2. **Marcar huecos.** Si no hay pacto: "Sois [N] socios sin pacto — es el documento más importante. ¿Quieres que redactemos uno?"
3. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md`.
   >
   > Las secciones que más se ajustan: la **cap table** (con cada ronda), el **pacto de accionistas** (al añadir inversionistas) y el **equipo** (al crecer)."

4. **Tu perfil aprende:**

   > Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que la sociedad está bien constituida.** Muchas startups tienen defectos en el pacto social (objeto social demasiado genérico, régimen de transmisión de acciones por defecto) o no han designado correctamente al agente residente.
- **No confundir stock options con phantom shares.** Las stock options requieren emitir acciones; las phantom shares no dan participación real.
- **No ignorar el cumplimiento de beneficiario final y la prevención de blanqueo (Ley 23 de 2015).** El agente residente es sujeto obligado.
- **No escribir posiciones de negociación genéricas para rondas.** Si no han levantado, decirlo: `[SIN HISTORIAL DE RONDAS — posiciones a calibrar con la primera negociación real]`.
- **No ignorar las relaciones laborales encubiertas.** Si hay contratistas que trabajan como empleados (horario, exclusividad, herramientas de la empresa), flaggearlo como riesgo laboral.
