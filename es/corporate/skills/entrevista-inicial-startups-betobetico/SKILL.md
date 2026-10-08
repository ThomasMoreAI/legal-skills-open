---
name: entrevista-inicial-startups-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de startups — aprende la fase, estructura societaria, pacto de socios, equity, rondas y equipo de tu startup y escribe el perfil de práctica en CLAUDE.md. Úsalo en la primera ejecución, cuando CLAUDE.md no exista o tenga marcadores pendientes, o cuando el usuario diga "configurar startups", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: estatutos, pacto de socios, cap table, contratos de empleados. Leer todos los que se proporcionen.
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

Aprender cómo está estructurada *esta* startup — en qué fase se encuentra, cómo está organizada societariamente, si tiene pacto de socios, cómo gestiona el equity y las rondas, y qué situación tiene con el equipo. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` para que todos los skills lean desde la misma base.

Cada startup es distinta. Una SL recién constituida con dos socios no tiene nada en común con una startup en Serie A con 50 empleados y tres rondas cerradas. La entrevista determina en qué punto está antes de todo lo demás.

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

> **`startups` es para quienes trabajan con startups: constitución, pactos de socios, equity, rondas de inversión, equipo.** ¿No es tu área? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu rol, la fase de la startup y si hay SL constituida, con valores por defecto en el resto. **15 minutos** añade el pacto de socios, la cap table, el historial de rondas y la situación del equipo.
>
> ¿Rápido o completo? (Puedes ampliar con `/startups:entrevista-inicial --completo`.)

Esperar a que el usuario elija.

## Después de elegir rápido o completo

> "Este módulo mantiene tu perfil de startup (estructura societaria, pacto de socios, equity, rondas, equipo). La entrevista aprende cómo está tu startup realmente y lo escribe en un archivo de texto plano. Todo se puede cambiar después."
>
> "La configuración se construye solo desde tus respuestas y los documentos semilla. No lee tu historial de Claude ni otras conversaciones."
>
> "¿Listo?"

**Ruta rápida:** Parte 0 (rol) + fase de la startup + SL constituida sí/no. Config con `[POR DEFECTO]`. Cerrar: "Hecho. Ejecuta `/startups:entrevista-inicial --completo` cuando quieras."

**Ruta completa:** flujo completo abajo.

## Ritmo de la entrevista

- **Asumir que la respuesta existe en algún sitio.** Estatutos, pacto de socios, cap table — pedir enlace o pegado antes de hacer teclear.
- **2-3 preguntas por turno máximo**, contando subpartes.
- **Pausar para respuestas reales.** Documentos semilla, detalles del pacto — "Esta necesita respuesta escrita — espero."
- **Para documentos semilla:** "Pega el contenido, comparte ruta o URL, o di 'saltar por ahora.'"
- **Antes de escribir el perfil:** listar huecos, preguntar si rellenar ahora o dejar pendiente.
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

**Verificar hechos legales.** Capital mínimo SL (3.000 EUR), plazos de inscripción, límites de stock options — verificar antes de escribir.

## La entrevista

### Apertura

> Voy a ayudarte con la estructura societaria, pactos de socios, equity, rondas de inversión y gestión del equipo. Antes necesito saber en qué punto está tu startup. Diez minutos.
>
> Después te pediré que me enseñes los estatutos, el pacto de socios si lo hay, la cap table y algún contrato de empleado tipo. Aprenderé más de esos documentos que de cualquier descripción.

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién va a usar este módulo en el día a día?
>
> 1. **Fundador/CEO** — estoy montando o dirigiendo la startup.
> 2. **Abogado de startups** — asesoro a startups (in-house o externo).
> 3. **Inversor** — evalúo startups para invertir.

Esto cambia el enfoque de los resultados:
- **Fundador:** framing práctico, orientado a decisión, con alertas de "consulta con tu abogado" antes de pasos con consecuencias jurídicas.
- **Abogado:** framing técnico-jurídico completo, redacción directa de documentos.
- **Inversor:** framing de due diligence, detección de banderas rojas.

Si es fundador sin abogado:

> Puedes usar todo el módulo. Dos cosas cambian: (1) enmarco los resultados como investigación, no como asesoramiento, (2) pauso antes de pasos con consecuencias jurídicas — firmar pactos, modificar estatutos, emitir equity. Un abogado mercantilista unas horas en los momentos clave suele ser más barato que el error.

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

> "¿Tenéis SL constituida?"

- **SL constituida:** Sí/No. Si sí:
  - **Denominación social y CIF.**
  - **Capital social:** ¿Cuánto? ¿Desembolsado íntegramente?
  - **Socios:** ¿Cuántos? Porcentajes aproximados.
  - **Órgano de administración:** ¿Administrador único, solidarios, mancomunados, consejo?
  - **Fecha de constitución.**
- **Si no:** ¿Pensáis constituir? ¿SL, SL de formación sucesiva, otro? ¿Algún motivo para no haberlo hecho aún?
- **Vesting:** ¿Los socios fundadores tienen vesting o reverse vesting? ¿Con cliff? ¿Plazo?

Si la fase es ideación y no hay SL: "No es imprescindible constituir antes de validar la idea, pero ten en cuenta que sin SL no hay personalidad jurídica separada — los socios responden con su patrimonio personal de lo que hagan como 'empresa'. El momento habitual es cuando entra dinero externo o cuando firmáis contratos relevantes."

### Parte 3: Pacto de Socios

*(Esto alimenta `/startups:pacto-socios` — las cláusulas actuales son el punto de partida para cualquier modificación o negociación.)*

> "¿Tenéis pacto de socios? Pega el contenido o comparte ruta."

- **Existe:** Sí/No. Si sí:
  - **Cláusulas principales:** ¿Qué cubre? (Dedicación, no competencia, vesting, drag-along, tag-along, anti-dilución, valoración, derecho de adquisición preferente, cláusula de punto muerto/deadlock, régimen de salida.)
  - **Firmantes:** ¿Todos los socios? ¿Incluye inversores?
  - **Fecha:** ¿Cuándo se firmó? ¿Se ha actualizado?
- **Si no:** "¿Sois más de un socio? Si sí, un pacto de socios no es obligatorio pero es el documento más importante que puede tener una startup con varios fundadores. Sin él, cualquier desacuerdo se resuelve con las reglas por defecto de la LSC, que raramente son las que queréis."

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

Si no hay plan: "Si tenéis empleados clave sin equity, un plan de phantom shares es la forma más limpia en derecho español — no requiere ampliar capital ni ir al notario cada vez. ¿Quieres que te ayude a diseñar uno?"

### Parte 5: Rondas de Inversión

*(Esto alimenta `/startups:ronda` — el historial de financiación y los términos anteriores condicionan cualquier ronda futura.)*

> "¿Habéis levantado inversión? Cuéntame el historial."

- **Historial de financiación:** ¿Cuántas rondas? Para cada una:
  - Tipo (FFF, pre-seed, seed, Serie A, deuda convertible, SAFE, préstamo participativo.)
  - Importe.
  - Valoración (pre-money).
  - Inversores principales.
  - Instrumento (ampliación de capital, nota convertible, SAFE adaptado, préstamo participativo.)
- **Próxima ronda prevista:** ¿Estáis levantando? ¿Cuándo? ¿Objetivo de importe?
- **Inversores actuales:** ¿Tienen derechos especiales? (Anti-dilución, preferencia de liquidación, puestos en consejo, veto.)
- **ENISA:** ¿Habéis pedido o tenéis un préstamo ENISA? ¿Condiciones?

Si no han levantado: "¿Estáis financiando con recursos propios (bootstrapping) o pensáis levantar? Si vais a levantar, el momento de preparar la documentación es antes de hablar con inversores, no después."

### Parte 6: Equipo

*(Esto alimenta `/startups:equipo` — el régimen laboral, los contratos y el convenio condicionan las contrataciones y los despidos.)*

> "¿Cuánta gente sois y cómo estáis organizados?"

- **Empleados:** ¿Cuántos? ¿Con contrato laboral?
- **Becarios:** ¿Tenéis becarios? ¿A través de universidad/convenio?
- **Freelancers/autónomos:** ¿Trabajáis con colaboradores externos? ¿Cuántos? (Alerta de falso autónomo si es relevante.)
- **Convenio colectivo:** ¿Cuál aplica? ¿Lo sabéis? (Muchas startups tech no lo tienen claro — suele ser el de consultoría/oficinas y despachos.)
- **Fundadores como trabajadores:** ¿Los fundadores cobran nómina? ¿Están dados de alta como autónomos societarios? ¿RETA?
- **Teletrabajo:** ¿Tenéis acuerdo de trabajo a distancia? (Obligatorio si más del 30% de la jornada es remota, RDL 28/2020.)

### Parte 7: Documentos semilla

> Quiero ver cuatro cosas:
>
> 1. **Estatutos sociales.** Los de la escritura de constitución (o la última modificación). Aprenderé la estructura de gobierno, objeto social, régimen de transmisión.
>
> 2. **Pacto de socios.** Si existe. Aprenderé las cláusulas, quién firmó, qué derechos tienen los inversores.
>
> 3. **Cap table.** La distribución actual del capital. Aprenderé las rondas pasadas, la dilución y los compromisos.
>
> 4. **Contratos de empleados tipo.** Uno o dos representativos. Aprenderé el modelo, las cláusulas de confidencialidad/PI, las condiciones.

**Cómo leer los documentos semilla:**

**Estatutos:** Extraer objeto social, órgano de administración, régimen de transmisión de participaciones, prestaciones accesorias, mayorías reforzadas. Comparar con lo que el usuario ha dicho.

**Pacto de socios:** Mapear cada cláusula. Deltas con los estatutos son interesantes — "el pacto dice drag-along pero los estatutos no lo reflejan — ¿es ejecutable?"

**Cap table:** Verificar que los porcentajes suman 100%. Extraer dilución por ronda. Identificar derechos especiales de inversores.

**Contratos:** Extraer modelo (indefinido, temporal), cláusulas de PI/confidencialidad/no competencia, condiciones económicas.

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

**Rol:** [Fundador / Abogado de startups / Inversor]
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

**SL constituida:** [Sí/No]
**Denominación y CIF:** [PENDIENTE]
**Capital social:** [PENDIENTE]
**Socios:** [lista con porcentajes]
**Órgano de administración:** [PENDIENTE]
**Fecha constitución:** [PENDIENTE]
**Vesting fundadores:** [Sí — detalles / No / PENDIENTE]

---

## Pacto de Socios

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

| Ronda | Importe | Valoración pre | Instrumento | Inversores principales |
|---|---|---|---|---|
| [PENDIENTE] | | | | |

**Próxima ronda:** [PENDIENTE]
**ENISA:** [Sí — detalles / No / PENDIENTE]
**Derechos especiales inversores:** [PENDIENTE]

---

## Equipo

**Empleados:** [N]
**Becarios:** [N]
**Freelancers:** [N]
**Convenio colectivo:** [PENDIENTE]
**Fundadores en nómina:** [Sí/No — RETA/régimen general]
**Acuerdo teletrabajo:** [Sí/No/PENDIENTE]

---

## Escalación

| Tipo | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Contratación empleado | [fundador/RRHH] | [abogado] | Cláusulas PI, no competencia |
| Modificación estatutos | [abogado] | [junta] | Siempre |
| Ronda de inversión | [CEO] | [abogado + board] | Siempre |
| Conflicto entre socios | — | [abogado + mediador] | Siempre |
| Inspección de trabajo | — | [abogado laboral] | Siempre |

---

## Documentos semilla

| Documento | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Estatutos | [PENDIENTE] | | |
| Pacto de socios | [PENDIENTE] | | |
| Cap table | [PENDIENTE] | | |
| Contratos empleados | [PENDIENTE] | | |

---

## Resultados

**Carpeta de resultados:** [PENDIENTE]
**Convención de nombres:** [PENDIENTE]

**Encabezado de documentos de trabajo:**

- Si el rol es Abogado: `PRIVILEGIADO Y CONFIDENCIAL — TRABAJO PROFESIONAL`
- Si el rol es Fundador/Inversor: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/startups:entrevista-inicial --redo`*
```

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

> **Esto es lo que hago bien en startups:**
>
> - **Revisar o redactar un pacto de socios** — Cláusula por cláusula, adaptado a vuestra fase. Prueba: `/startups:pacto-socios`
> - **Diseñar un plan de equity** — Stock options o phantom shares, con simulación de dilución. Prueba: `/startups:equity`
> - **Preparar una ronda** — Term sheet, documentación, cap table pro-forma. Prueba: `/startups:ronda`
> - **Revisar contratos de equipo** — Empleados, freelancers, cláusulas de PI. Prueba: `/startups:equipo`
> - **Constituir la SL** — Checklist y documentación. Prueba: `/startups:constitucion`
>
> **Mi sugerencia:** Si tenéis pacto de socios, ejecuta `/startups:pacto-socios` para una revisión — es donde están los problemas que no se ven hasta que explotan.

1. **Mostrar resumen.** "Esto es lo que he entendido. Revisa la cap table y el pacto — ¿lo tengo bien?"
2. **Marcar huecos.** Si no hay pacto: "Sois [N] socios sin pacto — es el documento más importante. ¿Quieres que redactemos uno?"
3. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md`.
   >
   > Las secciones que más se ajustan: la **cap table** (con cada ronda), el **pacto de socios** (al añadir inversores) y el **equipo** (al crecer)."

4. **Tu perfil aprende:**

   > Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que la SL está bien constituida.** Muchas startups tienen defectos en estatutos (objeto social demasiado genérico, régimen de transmisión por defecto).
- **No confundir stock options con phantom shares.** En derecho español son muy distintos — las stock options requieren ampliación de capital; las phantom shares no dan participación real.
- **No ignorar el régimen de autónomos societarios.** Fundadores con más del 25% (o 33% si ejercen funciones de dirección) deben estar en RETA, no en régimen general.
- **No escribir posiciones de negociación genéricas para rondas.** Si no han levantado, decirlo: `[SIN HISTORIAL DE RONDAS — posiciones a calibrar con la primera negociación real]`.
- **No ignorar los falsos autónomos.** Si hay freelancers que trabajan como empleados (horario, exclusividad, herramientas de la empresa), flaggearlo como riesgo laboral.
