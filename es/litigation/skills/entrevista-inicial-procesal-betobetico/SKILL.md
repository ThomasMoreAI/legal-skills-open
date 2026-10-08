---
name: entrevista-inicial-procesal-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu portfolio de asuntos judiciales, tus jurisdicciones activas, tus tipos de procedimiento habituales, tu relación con procuradores y tu estilo house de escritos. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/procesal/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
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

La práctica procesal en España tiene un ecosistema propio: LexNET, procuradores obligatorios, jurisdicciones separadas (civil, penal, social, contencioso, mercantil), plazos procesales que no perdonan y un estilo de escrito judicial que varía mucho entre despachos. Un litigante civil en Madrid escribe diferente a un laboralista en Barcelona o un penalista en Sevilla. Esta entrevista descubre tu práctica real y construye un perfil que refleje cómo litgas tú.

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

> **`procesal` es para quienes litigan — demandas, contestaciones, recursos, ejecuciones y concursos en cualquier jurisdicción española.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, jurisdicciones activas y tipos de procedimiento. **15 minutos** añade tu estilo house de escritos, tu relación con procuradores, tu formato de citas jurisprudenciales y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica procesal (jurisdicciones, tipos de procedimiento, estilo house), plantillas de escritos, calendario de plazos y registro de asuntos. Aprende cómo litgas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas de LEC, LECrim, LRJS, LJCA, etc.

---

## La entrevista

### Apertura

> Voy a aprender cómo litgas — en qué jurisdicciones, qué tipos de procedimiento, cómo estructuras tus escritos y cómo citas la jurisprudencia — para que cada demanda, contestación o recurso que prepare suene como si lo hubieras escrito tú.

**Ruta rápida:** solo Parte 0 y Parte 1 (jurisdicciones y asuntos). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado litigante, procurador, paralegal procesal.
> 2. **No abogado con acceso a abogado** — director jurídico que coordina litigios externos.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: LexNET, CENDOJ (buscador de jurisprudencia), almacenamiento de documentos, herramientas de gestión de asuntos (Wolters Kluwer, Lefebvre) y Slack.

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

- **Jurisdicciones activas:** ¿en cuáles litgas habitualmente?
  - Civil (Juzgados de Primera Instancia, Audiencia Provincial)
  - Penal (Juzgados de Instrucción, Penal, Audiencia Provincial, Audiencia Nacional)
  - Social (Juzgados de lo Social, TSJ)
  - Contencioso-administrativo (Juzgados de lo C-A, TSJ, Audiencia Nacional)
  - Mercantil (Juzgados de lo Mercantil)
- **Número de asuntos abiertos:** ¿cuántos, aproximadamente?
- **Partidos judiciales habituales:** ¿dónde litgas más? (Madrid, Barcelona, otros)
- **¿Eres demandante o demandado habitualmente?** ¿O ambos?

---

### Parte 2: Tipos de procedimiento habituales (3-4 min)

- **¿Cuáles de estos manejas habitualmente?**
  - Juicio ordinario (>6.000 euros, LEC art. 249)
  - Juicio verbal (hasta 6.000 euros, LEC art. 250)
  - Procedimiento monitorio (LEC arts. 812 ss.)
  - Ejecución de títulos judiciales y extrajudiciales
  - Procedimiento concursal (TRLC)
  - Contencioso-administrativo (ordinario, abreviado)
  - Procedimiento laboral (LRJS)
  - Procedimiento penal (diligencias previas, juicio oral, juicio rápido)
  - Medidas cautelares
  - Otros (describe)
- **Cuantías habituales:** ¿rango típico?
- **Materias más frecuentes:** ¿reclamaciones de cantidad, responsabilidad civil, impugnaciones, otros?

---

### Parte 3: Despachos externos y procuradores (2-3 min)

- **Procuradores:**
  - ¿Trabajas con procuradores fijos? ¿Nombres o despachos de procuraduría?
  - ¿Quién elige al procurador? (El cliente, tú, el despacho de procuraduría lo asigna)
  - ¿Cómo te comunicas con procuraduría? (Email, plataforma, teléfono)
- **Abogados externos:**
  - ¿Coordinas abogados externos en otras plazas? ¿Cuáles?
  - ¿Cómo gestionas la relación? (Informes periódicos, acceso a expediente, reuniones)
- **LexNET:**
  - ¿Quién gestiona las notificaciones de LexNET? (Tú, procurador, equipo administrativo)
  - ¿Frecuencia de revisión? (Diaria, varias veces al día)

---

### Parte 4: Estilo house (4-5 min)

> ¿Tienes una demanda o escrito tipo que pueda ver? Pega el contenido o comparte ruta — prefiero ver tu estilo real antes de preguntar sobre él.

Si no:

- **Formato de demandas:**
  - ¿Estructura? (Hechos numerados, fundamentos de derecho por bloques, suplico)
  - ¿Extensión habitual? (Concisa / detallada / depende)
  - ¿Nivel de citas doctrinales? (Mínimas / moderadas / extensas)
- **Citas de jurisprudencia:**
  - ¿Formato ECLI? (Ejemplo: ECLI:ES:TS:2024:1234)
  - ¿Citas con referencia a ponente?
  - ¿Usas bases de datos específicas? (CENDOJ, Westlaw, Aranzadi, vLex)
  - ¿Prefieres citar Tribunal Supremo, Audiencias Provinciales, TSJ, o mix?
- **Recursos habituales:**
  - ¿Qué recursos interpones con más frecuencia? (Apelación, casación, suplicación, contencioso)
  - ¿Formato específico para recursos?
- **Cautelas de estilo:**
  - ¿Usas fórmulas de cortesía específicas? ("Al Juzgado con el debido respeto...")
  - ¿Formato de suplico? (Tradicional, directo)

De los escritos semilla, extraer:
- Estructura general y orden de secciones
- Encabezado (datos del juzgado, partes, número de autos)
- Estilo de hechos (narrativo vs. esquemático)
- Nivel de detalle en fundamentos de derecho
- Formato de suplico/petitum
- Formato de citas jurisprudenciales (ECLI, referencia)
- Fórmulas de cortesía y cierre
- Otrosíes habituales

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
| Jurisdicción | Frecuencia | Partidos judiciales |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [PLACEHOLDER] |

**Asuntos abiertos:** [PLACEHOLDER]
**Posición habitual:** [PLACEHOLDER — demandante/demandado/ambos]

### Tipos de procedimiento

| Tipo | Frecuencia | Cuantía habitual | Materia |
|---|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [PLACEHOLDER] | [PLACEHOLDER] |

### Procuradores y externos

**Procuradores habituales:** [PLACEHOLDER]
**Abogados externos en otras plazas:** [PLACEHOLDER]
**Gestión de LexNET:** [PLACEHOLDER — quién y frecuencia]

### Estilo house

**Estructura de demanda:** [PLACEHOLDER]
**Extensión habitual:** [PLACEHOLDER]
**Citas jurisprudenciales:** [PLACEHOLDER — formato ECLI, bases de datos]
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
> - **Redactar una demanda** — en tu estilo house, con hechos, fundamentos y suplico. Prueba: `/procesal:demanda`
> - **Buscar jurisprudencia** — con formato ECLI, filtrada por tribunal y materia. Prueba: `/procesal:jurisprudencia`
> - **Calendario de plazos procesales** — qué vence y cuándo. Prueba: `/procesal:plazos`
> - **Preparar un recurso** — apelación, casación o suplicación en tu formato. Prueba: `/procesal:recurso`
>
> **Mi sugerencia para empezar:** Si tienes un escrito pendiente, ejecuta `/procesal:demanda` o `/procesal:recurso` — verás si entiende tu estilo.

Conectar herramienta de investigación:

> "Antes de tu primer escrito: conecta una herramienta de investigación jurídica (CENDOJ, Aranzadi, vLex). Sin ella, marcaré cada cita como no verificada."

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

- **No confundas jurisdicciones.** Civil, penal, social, contencioso y mercantil tienen leyes procesales distintas (LEC, LECrim, LRJS, LJCA).
- **No asumas plazos.** Cada tipo de procedimiento tiene plazos diferentes. Verifica siempre.
- **No inventes jurisprudencia.** Si no puedes verificar una sentencia contra CENDOJ o una base de datos, márcala como `[modelo — verificar]`.
- **No ignores la obligatoriedad de procurador.** Es obligatorio en la mayoría de procedimientos (LEC art. 23), con excepciones (monitorio <2.000, verbal <2.000, juicio cambiario).
- **No escribas en estilo genérico.** Si el usuario te dio escritos semilla, usa su estilo exacto.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo.
