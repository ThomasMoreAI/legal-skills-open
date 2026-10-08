---
name: entrevista-inicial-procesal-3636-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu portfolio de asuntos judiciales, tus jurisdicciones activas, tus tipos de proceso habituales, tu relación con apoderados judiciales y tu estilo house de escritos. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/procesal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — solo recomprobar integraciones. Solo reportar ✓ si una llamada MCP respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego partes específicas).
3. Documentos semilla: demandas recientes, escritos tipo.
4. Extraer: portfolio de asuntos, estilo house, formato de escritos.
5. Migración: si existe CLAUDE.md completo en cache pero no en config, copiar y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md`.

---

## Propósito

La práctica procesal en Panamá tiene un ecosistema propio: el Órgano Judicial y su sistema de notificaciones, apoderados judiciales, jurisdicciones separadas (civil, penal, laboral, contencioso, comercial), términos procesales que no perdonan y un estilo de escrito judicial que varía mucho entre despachos. Un litigante civil en la ciudad de Panamá escribe diferente a un laboralista en Colón o a un penalista en David. Esta entrevista descubre tu práctica real y construye un perfil que refleje cómo litigas tú.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → ofrecer retomar.
- **Contiene `[PLACEHOLDER]` sin pausa** → ofrecer empezar o retomar.
- **Completo** → saltar salvo `--repetir`.

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, confirmar y saltar preguntas de empresa. Si no, hacerlas y escribir el perfil compartido.

## Antes de empezar la entrevista

> **`procesal` es para quienes litigan — demandas, contestaciones, recursos, ejecuciones y concursos en cualquier jurisdicción panameña.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, jurisdicciones activas y tipos de proceso. **15 minutos** añade tu estilo house de escritos, tu relación con apoderados judiciales, tu formato de citas jurisprudenciales y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica procesal (jurisdicciones, tipos de proceso, estilo house), plantillas de escritos, calendario de términos y registro de asuntos. Aprende cómo litigas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas del Código Judicial de Panamá, Código de Trabajo, Ley 38 de 2000, etc.

---

## La entrevista

### Apertura

> Voy a aprender cómo litigas — en qué jurisdicciones, qué tipos de proceso, cómo estructuras tus escritos y cómo citas la jurisprudencia — para que cada demanda, contestación o recurso que prepare suene como si lo hubieras escrito tú.

**Ruta rápida:** solo Parte 0 y Parte 1 (jurisdicciones y asuntos). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado litigante (idóneo), apoderado judicial, asistente legal procesal.
> 2. **No abogado con acceso a abogado** — director jurídico que coordina litigios externos.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: el sistema de notificaciones del Órgano Judicial, el buscador de jurisprudencia del Órgano Judicial / Registro Judicial, almacenamiento de documentos, herramientas de gestión de asuntos y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho pequeño / ejercicio individual**
> - **Despacho mediano / grande**
> - **In-house (coordinación de litigios externos)**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Portfolio de asuntos (3-4 min)

> ¿Tienes un listado de asuntos abiertos o un sistema de gestión de expedientes? Pega el contenido o comparte ruta.

Si no:

- **Jurisdicciones activas:** ¿en cuáles litigas habitualmente?
  - Civil (Juzgados de Circuito, Tribunales Superiores, Corte Suprema de Justicia)
  - Penal (Sistema Penal Acusatorio: Juzgados de Garantías, Tribunales de Juicio; Corte Suprema de Justicia)
  - Laboral (Juntas de Conciliación y Decisión, Juzgados de Trabajo, Tribunal Superior de Trabajo)
  - Contencioso-administrativo (Sala Tercera de la Corte Suprema de Justicia)
  - Comercial (jurisdicción civil/comercial según cuantía y materia)
- **Número de asuntos abiertos:** ¿cuántos, aproximadamente?
- **Distritos judiciales habituales:** ¿dónde litigas más? (Panamá, Colón, Chiriquí, otros)
- **¿Eres demandante o demandado habitualmente?** ¿O ambos?

---

### Parte 2: Tipos de procedimiento habituales (3-4 min)

- **¿Cuáles de estos manejas habitualmente?**
  - Proceso ordinario (según cuantía, Código Judicial de Panamá) [verificar]
  - Proceso sumario / oral (Código Judicial de Panamá) [verificar]
  - Proceso ejecutivo (Código Judicial de Panamá) [verificar]
  - Ejecución de títulos judiciales y extrajudiciales
  - Proceso concursal de insolvencia (Ley 12 de 2016)
  - Contencioso-administrativo (Sala Tercera de la CSJ)
  - Proceso laboral (Código de Trabajo de Panamá) [verificar]
  - Proceso penal (Sistema Penal Acusatorio: investigación, intermedia, juicio oral) [verificar]
  - Medidas cautelares
  - Otros (describe)
- **Cuantías habituales:** ¿rango típico (en B/.)?
- **Materias más frecuentes:** ¿reclamaciones de cantidad, responsabilidad civil, impugnaciones, otros?

---

### Parte 3: Despachos externos y apoderados judiciales (2-3 min)

- **Apoderados judiciales:**
  - ¿Trabajas con apoderados/corresponsales fijos en otros distritos? ¿Nombres o despachos?
  - ¿Quién elige al apoderado? (El cliente, tú, el despacho corresponsal lo asigna)
  - ¿Cómo te comunicas con ellos? (Email, plataforma, teléfono)
- **Abogados externos:**
  - ¿Coordinas abogados externos en otras plazas? ¿Cuáles?
  - ¿Cómo gestionas la relación? (Informes periódicos, acceso a expediente, reuniones)
- **Notificaciones del Órgano Judicial:**
  - ¿Quién gestiona las notificaciones judiciales? (Tú, apoderado, equipo administrativo)
  - ¿Frecuencia de revisión? (Diaria, varias veces al día)

---

### Parte 4: Estilo house (4-5 min)

> ¿Tienes una demanda o escrito tipo que pueda ver? Pega el contenido o comparte ruta — prefiero ver tu estilo real antes de preguntar sobre él.

Si no:

- **Formato de demandas:**
  - ¿Estructura? (Hechos numerados, fundamentos de derecho por bloques, parte petitoria)
  - ¿Extensión habitual? (Concisa / detallada / depende)
  - ¿Nivel de citas doctrinales? (Mínimas / moderadas / extensas)
- **Citas de jurisprudencia:**
  - ¿Cómo citas los fallos? (Sala, fecha, número de registro judicial / ponente)
  - ¿Citas con referencia a magistrado ponente?
  - ¿Usas bases de datos específicas? (Buscador del Órgano Judicial / Registro Judicial, vLex, otras)
  - ¿Prefieres citar la Corte Suprema de Justicia, Tribunales Superiores, o mix?
- **Recursos habituales:**
  - ¿Qué recursos interpones con más frecuencia? (Reconsideración, apelación, casación ante la CSJ, hecho)
  - ¿Formato específico para recursos?
- **Cautelas de estilo:**
  - ¿Usas fórmulas de cortesía específicas? ("Al Honorable Juez, con el debido respeto...")
  - ¿Formato de la petición / parte petitoria? (Tradicional, directo)

De los escritos semilla, extraer:
- Estructura general y orden de secciones
- Encabezado (datos del tribunal, partes, número de expediente)
- Estilo de hechos (narrativo vs. esquemático)
- Nivel de detalle en fundamentos de derecho
- Formato de la parte petitoria
- Formato de citas jurisprudenciales (Sala, fecha, registro judicial)
- Fórmulas de cortesía y cierre
- Peticiones accesorias habituales

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 escritos de asuntos cerrados:
>
> - **Demanda tipo** (la que mejor represente tu estilo)
> - **Escrito tipo** (contestación, recurso, o escrito de trámite)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica procesal
*Escrito por entrevista-inicial el [FECHA].*

### Portfolio de asuntos

**Jurisdicciones activas:**
| Jurisdicción | Frecuencia | Distritos judiciales |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [PLACEHOLDER] |

**Asuntos abiertos:** [PLACEHOLDER]
**Posición habitual:** [PLACEHOLDER — demandante/demandado/ambos]

### Tipos de proceso

| Tipo | Frecuencia | Cuantía habitual | Materia |
|---|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [PLACEHOLDER] | [PLACEHOLDER] |

### Apoderados judiciales y externos

**Apoderados/corresponsales habituales:** [PLACEHOLDER]
**Abogados externos en otras plazas:** [PLACEHOLDER]
**Gestión de notificaciones del Órgano Judicial:** [PLACEHOLDER — quién y frecuencia]

### Estilo house

**Estructura de demanda:** [PLACEHOLDER]
**Extensión habitual:** [PLACEHOLDER]
**Citas jurisprudenciales:** [PLACEHOLDER — Sala, registro judicial, bases de datos]
**Tribunales preferidos para citas:** [PLACEHOLDER]
**Recursos habituales:** [PLACEHOLDER]
**Fórmulas de cortesía:** [PLACEHOLDER]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en práctica procesal:**
>
> - **Redactar una demanda** — en tu estilo house, con hechos, fundamentos y petición. Prueba: `/procesal:demanda`
> - **Analizar un requerimiento recibido** — con términos, opciones y riesgos. Prueba: `/procesal:requerimiento-recibido`
> - **Calendario de términos procesales** — qué vence y cuándo. Prueba: `/procesal:plazos`
> - **Triaje de una demanda recibida** — plazos de contestación y excepciones. Prueba: `/procesal:requerimiento-recibido`
>
> **Mi sugerencia para empezar:** Si tienes un escrito pendiente, ejecuta `/procesal:demanda` — verás si entiende tu estilo.

Conectar herramienta de investigación:

> "Antes de tu primer escrito: conecta una herramienta de investigación jurídica (buscador del Órgano Judicial / Registro Judicial, vLex). Sin ella, marcaré cada cita como no verificada."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/procesal:entrevista-inicial --repetir` para re-entrevista completa
> - `/procesal:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: el estilo house (cuando tu escritura evoluciona), las jurisdicciones activas y el formato de citas."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No confundas jurisdicciones.** Civil, penal, laboral y contencioso-administrativo se rigen por cuerpos distintos (Código Judicial de Panamá, Código de Trabajo, Ley 38 de 2000).
- **No asumas términos.** Cada tipo de proceso tiene términos diferentes. Verifica siempre.
- **No inventes jurisprudencia.** Si no puedes verificar un fallo contra el buscador del Órgano Judicial / Registro Judicial o una base de datos, márcalo como `[modelo — verificar]`.
- **No ignores el régimen de representación judicial.** La actuación ante los tribunales se realiza por medio de apoderado judicial (abogado idóneo); verifica las reglas de poder del Código Judicial.
- **No escribas en estilo genérico.** Si el usuario te dio escritos semilla, usa su estilo exacto.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo.
