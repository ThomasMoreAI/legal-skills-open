# 1er prompt — Puesta en marcha del repositorio preparado para IA **Normativa Educativa Canaria**

> Este archivo es el **prompt inicial** que debe ejecutarse en una sesión limpia con un agente capaz de crear ficheros y carpetas.
>
> Al terminar, el repositorio `ateeducacion/normativa_educativa_canaria` debe quedar preparado para recopilar, analizar, resumir, indexar y relacionar normativa educativa estatal y autonómica aplicable a Canarias, junto con currículos oficiales, en formatos **Markdown** y **YAML** fáciles de consultar por personas y por sistemas de inteligencia artificial.
>
> **No describas lo que harías. Hazlo.** Crea el repositorio, sus carpetas, plantillas, ejemplos, índices, schemas y `AGENTS.md`.

---

## 0. Objetivo real del repositorio

El repositorio `normativa_educativa_canaria` existe para tener una base documental **sencilla, rigurosa y preparada para IA** de normativa educativa y currículos.

Debe servir para:

1. guardar normativa educativa en formato estructurado;
2. crear resúmenes fieles en Markdown;
3. mantener metadatos en YAML;
4. enlazar siempre a fuentes oficiales;
5. registrar cuándo se consultó y cuándo se analizó cada norma;
6. relacionar normas entre sí;
7. separar norma vigente, modificada, derogada o pendiente de comprobar;
8. facilitar consultas por IA mediante índices, chunks y resúmenes trazables;
9. poder alimentar sistemas RAG, asistentes internos o agentes especializados;
10. incorporar con facilidad nuevas leyes, decretos, resoluciones, currículos o instrucciones.

Este repositorio **no sustituye las fuentes oficiales**. Cada resumen debe dejar claro que la fuente normativa válida es siempre BOE, BOC, Juriscan, Gobierno de Canarias, Ministerio de Educación u otra fuente pública competente.

---

## 1. Identidad del agente

Actúa como:

- **Documentalista normativo educativo.**
- **Analista de normativa educativa estatal y autonómica.**
- **Especialista en currículos LOMLOE.**
- **Diseñador de corpus documental para IA.**
- **Arquitecto de repositorios Markdown/YAML.**
- **Revisor de trazabilidad normativa.**

Tu misión es crear un repositorio usable por:

- docentes;
- equipos directivos;
- inspección educativa;
- personal técnico de administración educativa;
- agentes de inteligencia artificial;
- sistemas de búsqueda semántica;
- sistemas RAG.

---

## 2. Regla de oro

> **Todo dato normativo debe poder rastrearse hasta una fuente oficial.**

Está prohibido escribir frases como:

```text
La normativa exige...
La ley obliga...
El currículo establece...
````

si no se indica:

1. nombre de la norma;
2. artículo, disposición, anexo, apartado o página;
3. fuente oficial;
4. fecha de consulta;
5. ficha interna de fuente o norma.

Cuando falte evidencia:

* usa `[PENDIENTE]`;
* abre una pregunta `PREG-NNN`;
* no inventes;
* no rellenes con opinión.

Marcadores obligatorios:

```text
[HIPÓTESIS]       Afirmación razonable pendiente de comprobar.
[INTERPRETACIÓN] Lectura propia del equipo sobre un texto normativo.
[PENDIENTE]      Dato pendiente de verificar.
[OBSOLETO]       Contenido superado que se conserva por trazabilidad.
```

---

## 3. Fuentes iniciales

Durante la puesta en marcha deben registrarse estas fuentes iniciales.

```yaml
fuentes_iniciales:
  FTE-001:
    titulo: "Normativa educativa — Gobierno de Canarias"
    url: "https://www.gobiernodecanarias.org/educacion/web/servicios/normativa/"
    tipo: "portal-oficial"
    uso: "Entrada principal a normativa educativa autonómica, buscador, BOC, BOE y Juriscan."

  FTE-002:
    titulo: "Currículos de Educación Secundaria Obligatoria — Gobierno de Canarias"
    url: "https://www.gobiernodecanarias.org/educacion/web/secundaria/informacion/ordenacion-curriculo/curriculos-de-la-educacion-secundaria-obligatoria-eso/"
    tipo: "portal-curricular"
    uso: "Currículos LOMLOE de materias ESO, PDC, anexos y normativa relacionada."

  FTE-003:
    titulo: "Ordenación y currículo — Educación Secundaria — Gobierno de Canarias"
    url: "https://www.gobiernodecanarias.org/educacion/web/secundaria/informacion/ordenacion-curriculo/"
    tipo: "portal-curricular"
    uso: "Entrada general a ordenación y currículo de Secundaria."

  FTE-004:
    titulo: "Ordenación de la Educación Secundaria Obligatoria — Gobierno de Canarias"
    url: "https://www.gobiernodecanarias.org/educacion/web/secundaria/informacion/ordenacion-curriculo/ordenacion-de-la-educacion-secundaria-obligatoria-eso/index.html"
    tipo: "portal-curricular"
    uso: "Normativa de ordenación ESO, instrucciones de curso y normativa relacionada."

  FTE-005:
    titulo: "Ley Orgánica 2/2006, de Educación — texto consolidado BOE"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2006-7899"
    tipo: "normativa-estatal"
    uso: "Norma marco estatal."

  FTE-006:
    titulo: "Ley Orgánica 3/2020, LOMLOE"
    url: "https://www.boe.es/buscar/doc.php?id=BOE-A-2020-17264"
    tipo: "normativa-estatal"
    uso: "Ley modificadora de la LOE."

  FTE-007:
    titulo: "Real Decreto 217/2022, enseñanzas mínimas de ESO"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2022-4975"
    tipo: "normativa-estatal"
    uso: "Ordenación y enseñanzas mínimas de Educación Secundaria Obligatoria."

  FTE-008:
    titulo: "Ley 6/2014, Canaria de Educación no Universitaria"
    url: "https://www.boe.es/buscar/act.php?id=BOE-A-2014-9901"
    tipo: "normativa-autonomica"
    uso: "Marco educativo autonómico de Canarias."
```

Si una página enlaza a una fuente más precisa en BOE, BOC, Juriscan o PDF oficial, crea también la fuente final y relaciónala.

---

## 4. Principios del repositorio

Estos principios deben aparecer en `README.md`, `AGENTS.md` y `docs/metodologia/disciplina-evidencia.md`.

1. **Sencillez primero.** El repositorio debe ser fácil de leer, mantener y consultar.
2. **IA-friendly.** Todo contenido debe estar pensado para ser indexado, troceado y consultado por IA.
3. **Markdown para contenido narrativo.**
4. **YAML para metadatos estructurados.**
5. **Fuente oficial obligatoria.**
6. **Fecha de consulta obligatoria.**
7. **Fecha de análisis obligatoria cuando haya interpretación o resumen.**
8. **Estado de vigencia obligatorio.**
9. **Relaciones normativas explícitas.**
10. **No copiar normas completas si basta con resumen, cita y enlace oficial.**
11. **No mezclar normativa con recursos no normativos.**
12. **No borrar contenido histórico: marcar como derogado, obsoleto o sustituido.**
13. **Usar IDs estables y correlativos.**
14. **Todo resumen debe indicar que no sustituye la fuente oficial.**
15. **Todo índice debe ser legible por humanos y máquinas.**

---

## 5. IDs obligatorios

Usa estos prefijos:

```text
FTE-NNN      Fuente oficial o referencia.
NOR-NNN      Norma educativa.
CUR-NNN      Currículo o materia curricular.
AN-NNN       Nota de análisis.
REL-NNN      Relación entre normas.
CHUNK-NNNNN  Fragmento preparado para IA.
PREG-NNN     Pregunta abierta.
TAREA-NNN    Tarea.
DEC-NNNN     Decisión editorial.
```

Ejemplos:

```text
FTE-001
NOR-001
CUR-001
AN-001
REL-001
CHUNK-00001
PREG-001
TAREA-001
DEC-0001
```

Los IDs son correlativos y nunca se reutilizan.

---

## 6. Estructura de carpetas

Crea esta estructura:

```text
/
├── README.md
├── AGENTS.md
├── CLAUDE.md
├── TODO.md
├── status.yaml
├── index.md
├── schemas/
│   ├── fuente.schema.yaml
│   ├── norma.schema.yaml
│   ├── curriculum.schema.yaml
│   ├── relacion.schema.yaml
│   ├── analisis.schema.yaml
│   ├── chunk.schema.yaml
│   ├── pregunta.schema.yaml
│   └── tarea.schema.yaml
├── .agents/
│   └── skills/
│       ├── catalogacion-fuentes/SKILL.md
│       ├── analisis-normativo/SKILL.md
│       ├── control-vigencia/SKILL.md
│       ├── relaciones-normativas/SKILL.md
│       ├── analisis-curricular/SKILL.md
│       ├── preparacion-corpus-ia/SKILL.md
│       ├── control-calidad-documental/SKILL.md
│       ├── experto-lomloe-loe/SKILL.md
│       ├── experto-normativa-canaria/SKILL.md
│       ├── experto-eso/SKILL.md
│       ├── experto-primaria/SKILL.md
│       ├── experto-bachillerato/SKILL.md
│       ├── experto-formacion-profesional/SKILL.md
│       └── perfil-docente/SKILL.md
├── 00_gobierno-repositorio/
│   ├── metodologia/
│   ├── criterios/
│   └── glosario/
├── 01_fuentes/
│   ├── portales-oficiales/
│   ├── boe/
│   ├── boc/
│   ├── juriscan/
│   ├── gobierno-canarias/
│   ├── ministerio-educacion/
│   └── otras-fuentes-oficiales/
├── 02_normativa/
│   ├── estatal/
│   │   ├── leyes-organicas/
│   │   ├── reales-decretos/
│   │   ├── ordenes/
│   │   └── resoluciones/
│   ├── canarias/
│   │   ├── leyes/
│   │   ├── decretos/
│   │   ├── ordenes/
│   │   ├── resoluciones/
│   │   └── instrucciones/
│   ├── europea/
│   └── historica/
├── 03_curriculos/
│   ├── infantil/
│   ├── primaria/
│   ├── eso/
│   │   ├── materias/
│   │   ├── ambitos-pdc/
│   │   └── anexos/
│   ├── bachillerato/
│   ├── formacion-profesional/
│   └── regimen-especial/
├── 04_analisis/
│   ├── notas/
│   ├── comparativas/
│   ├── mapas-vigencia/
│   ├── mapas-curriculares/
│   └── sintesis/
├── 05_relaciones/
│   ├── normativa/
│   ├── curriculares/
│   └── grafos/
├── 06_indices/
│   ├── fuentes.yaml
│   ├── normativa.yaml
│   ├── curriculos.yaml
│   ├── relaciones.yaml
│   ├── analisis.yaml
│   ├── chunks.yaml
│   ├── preguntas.yaml
│   └── tareas.yaml
├── 07_corpus_ia/
│   ├── resumenes/
│   ├── chunks/
│   ├── prompts/
│   ├── preguntas-frecuentes/
│   └── exports/
├── 08_tareas/
│   ├── backlog/
│   ├── diario/
│   └── preguntas/
├── 09_decisiones-editoriales/
│   └── adr/
├── 10_plantillas/
│   ├── markdown/
│   └── yaml/
├── 11_calidad/
│   ├── validaciones/
│   ├── enlaces/
│   ├── vigencia/
│   └── informes/
└── docs/
    ├── guias/
    ├── metodologia/
    └── esquema-datos/
```

Cada carpeta principal debe tener un `README.md` breve.

`CLAUDE.md` debe contener exactamente:

```text
@AGENTS.md
```

---

## 7. Qué va en cada capa

### `01_fuentes/`

Fichas de fuentes oficiales o portales de referencia.

Ejemplo:

```text
01_fuentes/boe/FTE-005-loe-texto-consolidado.md
```

### `02_normativa/`

Una ficha Markdown por norma.

Ejemplo:

```text
02_normativa/estatal/leyes-organicas/NOR-001-loe.md
```

### `03_curriculos/`

Fichas curriculares en YAML y Markdown.

Ejemplo:

```text
03_curriculos/eso/materias/CUR-001-biologia-geologia.yaml
03_curriculos/eso/materias/CUR-001-biologia-geologia.md
```

### `04_analisis/`

Notas de análisis, comparativas y síntesis.

Ejemplo:

```text
04_analisis/notas/AN-001-piramide-normativa-eso.md
```

### `05_relaciones/`

Relaciones estructuradas entre normas y currículos.

Ejemplo:

```text
05_relaciones/normativa/REL-001-lomloe-modifica-loe.yaml
```

### `06_indices/`

Índices principales del repositorio.

Deben ser YAML, con claves por ID, no listas anónimas.

### `07_corpus_ia/`

Contenido preparado para IA:

* resúmenes;
* chunks;
* preguntas frecuentes;
* prompts;
* exports JSON/YAML.

### `08_tareas/`

Tareas, diario y preguntas abiertas.

### `09_decisiones-editoriales/`

Decisiones sobre cómo se organiza el corpus.

Ejemplo:

```text
09_decisiones-editoriales/adr/DEC-0001-modelo-markdown-yaml.md
```

### `10_plantillas/`

Plantillas reutilizables.

### `11_calidad/`

Validaciones, comprobaciones de enlaces, vigencia y errores.

---

## 8. Formato de ficha de fuente

Crea plantilla:

```text
10_plantillas/markdown/plantilla-fuente.md
```

Contenido:

```markdown
---
id: FTE-XXX
titulo: ""
tipo_fuente: ""
autoridad: ""
url_oficial: ""
fecha_consulta: YYYY-MM-DD
fecha_analisis: null
estado_fuente: "Activa"
nivel_evidencia: "confirmado-fuente-primaria"
relacionadas: []
---

# FTE-XXX — Título

> Esta ficha describe una fuente oficial o referencia institucional. No sustituye la consulta directa de la fuente.

## Identificación

- **Autoridad:** 
- **URL oficial:** 
- **Fecha de consulta:** 
- **Tipo de fuente:** 

## Qué contiene

[PENDIENTE]

## Relevancia para el repositorio

[PENDIENTE]

## Normas o currículos enlazados

[PENDIENTE]

## Observaciones

[PENDIENTE]
```

---

## 9. Formato de ficha normativa

Crea plantilla:

```text
10_plantillas/markdown/plantilla-norma.md
```

Contenido:

```markdown
---
id: NOR-XXX
titulo: ""
nombre_corto: ""
tipo_norma: ""
ambito: ""
autoridad: ""
fecha_disposicion: null
fecha_publicacion: null
fecha_entrada_vigor: null
fecha_consulta: YYYY-MM-DD
fecha_analisis: YYYY-MM-DD
estado_vigencia: "Pendiente de verificación"
fuente_principal: FTE-XXX
url_oficial: ""
etapas_afectadas: []
temas: []
relaciones:
  desarrolla_a: []
  modificada_por: []
  modifica_a: []
  deroga_a: []
  derogada_por: []
  relacionada_con: []
nivel_evidencia: "confirmado-fuente-primaria"
---

# NOR-XXX — Título

> Este resumen no sustituye la consulta de la fuente oficial.

## 1. Identificación

- **Norma:** 
- **Nombre corto:** 
- **Ámbito:** 
- **Autoridad:** 
- **Fuente oficial:** 
- **Fecha de consulta:** 
- **Estado de vigencia:** 

## 2. Objeto de la norma

[PENDIENTE]

## 3. Ámbito de aplicación

[PENDIENTE]

## 4. Estructura

[PENDIENTE]

## 5. Artículos, disposiciones o anexos clave

| Localización | Contenido | Relevancia |
| --- | --- | --- |
| [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |

## 6. Relación con otras normas

[PENDIENTE]

## 7. Impacto en Canarias

[PENDIENTE]

## 8. Resumen IA-friendly

[PENDIENTE]

## 9. Preguntas frecuentes

[PENDIENTE]

## 10. Dudas abiertas

[PENDIENTE]

## 11. Fuentes

- [FTE-XXX](ruta-relativa)
```

---

## 10. Formato de currículo

Crea plantilla YAML:

```text
10_plantillas/yaml/plantilla-curriculum.yaml
```

Contenido:

```yaml
id: CUR-XXX
titulo: ""
etapa: ""
materia: ""
ambito: null
cursos: []
norma_base: NOR-XXX
fuente: FTE-XXX
url_oficial: ""
fecha_consulta: YYYY-MM-DD
fecha_analisis: null
estado_extraccion: "Pendiente"
estado_vigencia: "Pendiente de verificación"
elementos:
  competencias_especificas: []
  criterios_evaluacion: []
  saberes_basicos: []
  descriptores_operativos: []
  situaciones_aprendizaje: []
relaciones:
  desarrolla_a: []
  relacionada_con: []
resumen_ia: ""
observaciones: null
```

Crea también plantilla Markdown:

```text
10_plantillas/markdown/plantilla-curriculum.md
```

Contenido:

```markdown
---
id: CUR-XXX
titulo: ""
tipo: "curriculum"
etapa: ""
materia: ""
norma_base: NOR-XXX
fuente: FTE-XXX
fecha_consulta: YYYY-MM-DD
fecha_analisis: null
estado_extraccion: "Pendiente"
---

# CUR-XXX — Título

> Este resumen curricular no sustituye el currículo oficial publicado por la administración competente.

## 1. Identificación

## 2. Norma base

## 3. Cursos afectados

## 4. Competencias específicas

[PENDIENTE]

## 5. Criterios de evaluación

[PENDIENTE]

## 6. Saberes básicos

[PENDIENTE]

## 7. Resumen IA-friendly

[PENDIENTE]

## 8. Relaciones

[PENDIENTE]

## 9. Fuente oficial

[PENDIENTE]
```

---

## 11. Formato de relación normativa

Crea plantilla:

```text
10_plantillas/yaml/plantilla-relacion.yaml
```

Contenido:

```yaml
id: REL-XXX
tipo_relacion: "modifica"
origen: NOR-XXX
destino: NOR-YYY
descripcion: ""
evidencia:
  fuente: FTE-XXX
  localizacion: ""
fecha_registro: YYYY-MM-DD
nivel_evidencia: "confirmado-fuente-primaria"
observaciones: null
```

Tipos permitidos:

```text
modifica
desarrolla
deroga
corrige
complementa
sustituye
aplica
interpreta
relaciona
```

---

## 12. Formato de chunk IA

Crea plantilla:

```text
10_plantillas/yaml/plantilla-chunk.yaml
```

Contenido:

```yaml
id: CHUNK-00001
origen_tipo: "norma"
origen_id: NOR-XXX
titulo: ""
texto: >
  Texto breve, autocontenido y trazable.
metadatos:
  ambito: ""
  etapa: []
  temas: []
  estado_vigencia: ""
  fuente: FTE-XXX
  url_oficial: ""
  fecha_consulta: YYYY-MM-DD
  fecha_analisis: YYYY-MM-DD
  localizacion: ""
relaciones:
  normas: []
  curriculos: []
  chunks_relacionados: []
uso_recomendado:
  - "rag"
  - "busqueda-semantica"
  - "preguntas-respuestas"
nivel_evidencia: "confirmado-fuente-primaria"
```

Reglas para chunks:

1. Cada chunk debe ser breve.
2. Cada chunk debe ser autocontenido.
3. Cada chunk debe indicar fuente.
4. No crear chunks sin fuente oficial.
5. No mezclar hechos e interpretación.
6. Si hay interpretación, marcar `[INTERPRETACIÓN]`.

---

## 13. Índices principales

Crea estos archivos:

```text
06_indices/fuentes.yaml
06_indices/normativa.yaml
06_indices/curriculos.yaml
06_indices/relaciones.yaml
06_indices/analisis.yaml
06_indices/chunks.yaml
06_indices/preguntas.yaml
06_indices/tareas.yaml
```

### `06_indices/fuentes.yaml`

```yaml
FTE-001:
  titulo: "Normativa educativa — Gobierno de Canarias"
  tipo_fuente: "portal-oficial"
  autoridad: "Gobierno de Canarias"
  url_oficial: "https://www.gobiernodecanarias.org/educacion/web/servicios/normativa/"
  fecha_consulta: 2026-04-25
  ruta: "01_fuentes/portales-oficiales/FTE-001-normativa-educativa-gobierno-canarias.md"
  estado_fuente: "Activa"
```

### `06_indices/normativa.yaml`

```yaml
NOR-001:
  titulo: "Ley Orgánica 2/2006, de Educación"
  nombre_corto: "LOE"
  tipo_norma: "ley-organica"
  ambito: "estatal"
  estado_vigencia: "Vigente con modificaciones"
  fuente_principal: FTE-005
  ruta: "02_normativa/estatal/leyes-organicas/NOR-001-loe.md"
  temas: [sistema-educativo, curriculo, evaluacion]
  etapas_afectadas: [infantil, primaria, eso, bachillerato, formacion-profesional]
```

### `06_indices/curriculos.yaml`

```yaml
CUR-001:
  titulo: "Biología y Geología — ESO Canarias"
  etapa: "eso"
  materia: "Biología y Geología"
  norma_base: NOR-XXX
  fuente: FTE-002
  ruta_yaml: "03_curriculos/eso/materias/CUR-001-biologia-geologia.yaml"
  ruta_md: "03_curriculos/eso/materias/CUR-001-biologia-geologia.md"
  estado_extraccion: "Pendiente"
```

---

## 14. Estados controlados

### Estado de vigencia

```text
Vigente
Vigente con modificaciones
Parcialmente vigente
Derogada
Derogada parcialmente
Sustituida
Histórica
Pendiente de verificación
No normativa
```

### Estado de extracción curricular

```text
Pendiente
En análisis
Extraído parcialmente
Extraído
Revisado
Obsoleto
```

### Nivel de evidencia

```text
confirmado-fuente-primaria
confirmado-fuente-secundaria-oficial
inferido
hipotesis
opinion-experta
```

### Ámbitos

```text
estatal
canarias
europeo
municipal
otro
```

### Etapas

```text
infantil
primaria
eso
bachillerato
formacion-profesional
educacion-adultos
regimen-especial
transversal
```

### Temas

```text
curriculo
ordenacion
evaluacion
promocion
titulacion
atencion-diversidad
inclusion
admision
escolarizacion
convivencia
organizacion-centros
funcion-docente
inspeccion
digitalizacion
familias
becas-ayudas
calendario-escolar
transporte-comedor
```

---

## 15. `AGENTS.md`

Crea un `AGENTS.md` con estas secciones:

1. Propósito del repositorio.
2. Qué debe hacer un agente antes de modificar el repositorio.
3. Regla de evidencia.
4. Estructura de carpetas.
5. Formato Markdown.
6. Formato YAML.
7. Cómo crear una ficha de fuente.
8. Cómo crear una ficha normativa.
9. Cómo crear una ficha curricular.
10. Cómo crear chunks para IA.
11. Cómo registrar relaciones.
12. Cómo actualizar índices.
13. Cómo comprobar vigencia.
14. Cuándo cargar cada skill.
15. Criterios de cierre de tarea.

Incluye estas reglas obligatorias:

```text
R1. No se crea contenido normativo sin fuente oficial.
R2. Todo resumen indica que no sustituye la fuente oficial.
R3. Toda norma tiene estado de vigencia.
R4. Toda ficha tiene fecha de consulta.
R5. Todo análisis tiene fecha de análisis.
R6. Toda relación normativa se registra en YAML.
R7. Todo contenido IA-friendly debe ser breve, trazable y fiel.
R8. No se mezclan normas con orientaciones no normativas.
R9. No se borran normas derogadas; se marcan.
R10. Los IDs son estables, correlativos y no se reutilizan.
R11. Los índices YAML se actualizan con cada nueva fuente, norma, currículo o chunk.
R12. Las dudas se registran como PREG-NNN.
R13. Las interpretaciones se marcan con [INTERPRETACIÓN].
R14. Las hipótesis se marcan con [HIPÓTESIS].
R15. Los datos pendientes se marcan con [PENDIENTE].
```

---

## 16. Skills mínimas

Crea estas skills:

### `catalogacion-fuentes`

Catalogar fuentes oficiales y crear `FTE-NNN`.

### `analisis-normativo`

Analizar normas y crear `NOR-NNN`.

### `control-vigencia`

Comprobar si una norma está vigente, modificada, derogada o pendiente.

### `relaciones-normativas`

Crear `REL-NNN` entre normas.

### `analisis-curricular`

Extraer y resumir currículos.

### `preparacion-corpus-ia`

Crear resúmenes, chunks y exports IA-friendly.

### `control-calidad-documental`

Validar estructura, enlaces, YAML, Markdown y trazabilidad.

### `experto-lomloe-loe`

Normativa básica estatal LOE/LOMLOE.

### `experto-normativa-canaria`

Normativa educativa autonómica canaria.

### `experto-eso`

ESO, ordenación, currículo, evaluación y PDC.

### `experto-primaria`

Infantil y Primaria.

### `experto-bachillerato`

Bachillerato.

### `experto-formacion-profesional`

Formación Profesional.

### `perfil-docente`

Revisar claridad y utilidad para profesorado.

Cada skill debe tener este formato:

```markdown
---
name: nombre-skill
description: Descripción breve y accionable.
license: CC-BY-4.0
compatibility: opencode
metadata:
  idioma: es
  ambito: normativa-educativa-canarias
  tipo: proceso | dominio | perfil
  version: "1.0"
  actualizado: 2026-04-25
---

# Nombre de la skill

## Rol

## Misión

## Cuándo cargarla

## Entradas esperadas

## Salidas esperadas

## Reglas de evidencia

## Anti-patrones

## Plantillas relacionadas
```

---

## 17. Ejemplos iniciales obligatorios

Crea estos ejemplos mínimos.

### Fuentes

```text
FTE-001 Normativa educativa Gobierno de Canarias
FTE-002 Currículos ESO Canarias
FTE-003 Ordenación y currículo Secundaria Canarias
FTE-004 Ordenación ESO Canarias
FTE-005 LOE BOE texto consolidado
FTE-006 LOMLOE BOE
FTE-007 RD 217/2022 BOE
FTE-008 Ley Canaria 6/2014
```

### Normas

```text
NOR-001 LOE
NOR-002 LOMLOE
NOR-003 RD 217/2022
NOR-004 Ley Canaria 6/2014
```

Si puedes confirmar durante la ejecución el decreto autonómico de currículo ESO/Bachillerato de Canarias y su fuente oficial final, crea también:

```text
NOR-005 Decreto autonómico de currículo ESO/Bachillerato Canarias
```

Si no puedes confirmarlo con fuente oficial final:

* crea `PREG-001`;
* no inventes la ficha normativa;
* deja una referencia pendiente desde `FTE-002`.

### Relaciones

```text
REL-001 LOMLOE modifica LOE
REL-002 RD 217/2022 desarrolla enseñanzas mínimas ESO
REL-003 Ley Canaria 6/2014 se relaciona con LOE/LOMLOE
```

### Currículos ESO iniciales

Crea fichas `CUR-NNN` con estado `Pendiente` para las materias ESO localizadas desde la página oficial de currículos.

Como mínimo:

```text
CUR-001 Biología y Geología
CUR-002 Cultura Clásica
CUR-003 Cultura y Ciudadanía Digital
CUR-004 Digitalización
CUR-005 Economía Personal y Social
CUR-006 Economía y Emprendimiento
CUR-007 Educación en Valores Cívicos y Éticos
CUR-008 Educación Física
CUR-009 Educación Plástica, Visual y Audiovisual
CUR-010 Expresión Artística
CUR-011 Filosofía
CUR-012 Física y Química
CUR-013 Formación y Orientación Personal y Profesional
CUR-014 Geografía e Historia
CUR-015 Historia y Geografía de Canarias
CUR-016 Latín
CUR-017 Lengua Castellana y Literatura
CUR-018 Lengua Extranjera
CUR-019 Matemáticas
CUR-020 Música
CUR-021 Segunda Lengua Extranjera
CUR-022 Tecnología
CUR-023 Tecnología y Digitalización
```

Crea también ámbitos PDC si aparecen en la fuente oficial:

```text
CUR-024 Ámbito Lingüístico y Social
CUR-025 Ámbito Científico-Tecnológico
CUR-026 Ámbito Práctico
```

### Análisis

```text
AN-001 Pirámide normativa ESO
AN-002 Inventario inicial de currículos ESO
AN-003 Criterios para distinguir norma, currículo, orientación y recurso
```

### Preguntas

```text
PREG-001 Fuente oficial final del decreto autonómico de currículo ESO/Bachillerato.
PREG-002 Nivel de detalle que se extraerá de cada currículo.
PREG-003 Tratamiento de orientaciones y recursos no normativos.
```

### Tareas

```text
TAREA-001 Puesta en marcha del repositorio
TAREA-002 Catalogar fuentes iniciales
TAREA-003 Crear fichas normativas iniciales
TAREA-004 Crear índice inicial de currículos ESO
TAREA-005 Preparar primeros chunks IA
TAREA-006 Revisar vigencia de normas iniciales
```

---

## 18. `status.yaml`

Crea este estado inicial:

```yaml
metadata:
  proyecto: "Normativa Educativa Canaria"
  repositorio: "ateeducacion/normativa_educativa_canaria"
  objetivo: "Corpus IA-friendly de normativa educativa y currículos en Markdown y YAML"
  fase_actual: "Fase 0 — Puesta en marcha"
  fecha_actualizacion: 2026-04-25
  agente_actual: "@.agents/skills/catalogacion-fuentes"

tareas:
  TAREA-001:
    titulo: "Puesta en marcha del repositorio"
    estado: "Hecha"
    prioridad: "Crítica"
    tipo: "puesta-en-marcha"
    responsable: "@.agents/skills/catalogacion-fuentes"
    fecha_creacion: 2026-04-25
    fecha_actualizacion: 2026-04-25
    relacionadas: [DEC-0001]
    siguiente_accion: null

  TAREA-002:
    titulo: "Catalogar fuentes iniciales"
    estado: "En curso"
    prioridad: "Alta"
    tipo: "catalogacion"
    responsable: "@.agents/skills/catalogacion-fuentes"
    fecha_creacion: 2026-04-25
    fecha_actualizacion: 2026-04-25
    relacionadas: [FTE-001, FTE-002, FTE-003, FTE-004]
    siguiente_accion: "Completar fuentes BOE, BOC o Juriscan finales"

  TAREA-003:
    titulo: "Crear fichas normativas iniciales"
    estado: "Pendiente"
    prioridad: "Alta"
    tipo: "analisis"
    responsable: "@.agents/skills/analisis-normativo"
    fecha_creacion: 2026-04-25
    fecha_actualizacion: 2026-04-25
    relacionadas: [NOR-001, NOR-002, NOR-003, NOR-004]
    siguiente_accion: "Crear fichas Markdown con resumen IA-friendly"

bloqueos: []

reglas:
  - "No crear contenido normativo sin fuente oficial."
  - "No borrar historial."
  - "Actualizar índices YAML con cada nueva entidad."
  - "Marcar toda duda como PREG-NNN."
```

---

## 19. `index.md`

Crea un índice principal en Markdown, no hace falta panel HTML complejo.

Debe tener:

```markdown
# Normativa Educativa Canaria

Repositorio IA-friendly de normativa educativa y currículos.

## Accesos principales

- [Fuentes](06_indices/fuentes.yaml)
- [Normativa](06_indices/normativa.yaml)
- [Currículos](06_indices/curriculos.yaml)
- [Relaciones](06_indices/relaciones.yaml)
- [Chunks IA](06_indices/chunks.yaml)
- [Preguntas abiertas](06_indices/preguntas.yaml)

## Normas iniciales

- LOE
- LOMLOE
- RD 217/2022
- Ley Canaria 6/2014

## Currículos iniciales

- ESO Canarias

## Advertencia

Los resúmenes de este repositorio no sustituyen la consulta de fuentes oficiales.
```

---

## 20. Corpus IA

En `07_corpus_ia/resumenes/`, crea:

```text
resumen-NOR-001-loe.md
resumen-NOR-002-lomloe.md
resumen-NOR-003-rd-217-2022.md
resumen-NOR-004-ley-canaria-educacion.md
```

Cada resumen debe tener:

```markdown
---
origen: NOR-XXX
tipo: "resumen-ia"
fuente: FTE-XXX
fecha_consulta: YYYY-MM-DD
fecha_analisis: YYYY-MM-DD
estado_vigencia: ""
---

# Resumen IA — NOR-XXX

> Este resumen no sustituye la fuente oficial.

## Qué regula

## A quién afecta

## Ideas clave

## Artículos o apartados importantes

## Relaciones con otras normas

## Posibles preguntas de usuario

## Respuesta breve recomendada para IA

## Fuente oficial
```

En `07_corpus_ia/chunks/`, crea al menos 5 chunks iniciales de ejemplo:

```text
CHUNK-00001-loe-objeto.yaml
CHUNK-00002-lomloe-modifica-loe.yaml
CHUNK-00003-rd217-eso.yaml
CHUNK-00004-ley-canaria-marco.yaml
CHUNK-00005-curriculos-eso-canarias.yaml
```

---

## 21. Decisiones editoriales iniciales

Crea:

```text
09_decisiones-editoriales/adr/DEC-0001-modelo-markdown-yaml.md
09_decisiones-editoriales/adr/DEC-0002-separacion-fuente-norma-curriculo-chunk.md
09_decisiones-editoriales/adr/DEC-0003-tratamiento-de-normas-pendientes-de-vigencia.md
```

Formato:

```markdown
---
id: DEC-0001
titulo: ""
estado: "Aceptada"
fecha: 2026-04-25
relacionadas: []
---

# DEC-0001 — Título

## Contexto

## Decisión

## Motivo

## Consecuencias

## Relación con IA

## Revisión futura
```

---

## 22. Validación

Crea schemas básicos en `schemas/`.

Todos deben usar:

```yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
additionalProperties: false
```

Crea guía:

```text
docs/guias/validacion.md
```

Con:

```bash
npx ajv-cli validate \
  --spec=draft2020 \
  -s schemas/norma.schema.yaml \
  -d 06_indices/normativa.yaml
```

---

## 23. Criterios de cierre

Una tarea solo pasa a `Hecha` si:

1. tiene fuente oficial;
2. tiene fecha de consulta;
3. tiene Markdown o YAML válido;
4. está enlazada desde un índice;
5. tiene ID correcto;
6. tiene relaciones si aplica;
7. tiene estado de vigencia si es norma;
8. tiene resumen IA si corresponde;
9. tiene preguntas abiertas si hay dudas;
10. aparece en el diario.

---

## 24. Entrega final obligatoria

Al terminar deben existir:

1. árbol de directorios completo;
2. `README.md`;
3. `AGENTS.md`;
4. `CLAUDE.md`;
5. `TODO.md`;
6. `status.yaml`;
7. `index.md`;
8. schemas básicos;
9. 14 skills;
10. plantillas Markdown/YAML;
11. fuentes `FTE-001` a `FTE-008`;
12. normas `NOR-001` a `NOR-004`;
13. relaciones `REL-001` a `REL-003`;
14. currículos ESO `CUR-001` a `CUR-023`;
15. ámbitos PDC `CUR-024` a `CUR-026` si aparecen en la fuente;
16. análisis `AN-001` a `AN-003`;
17. preguntas `PREG-001` a `PREG-003`;
18. tareas `TAREA-001` a `TAREA-006`;
19. chunks IA `CHUNK-00001` a `CHUNK-00005`;
20. índices YAML actualizados.

---

## 25. Criterio final de éxito

El repositorio debe permitir que una IA pueda responder preguntas como:

```text
¿Qué normativa regula la ESO en Canarias?
¿Qué relación hay entre LOMLOE y LOE?
¿Qué norma estatal establece las enseñanzas mínimas de ESO?
¿Qué currículos ESO están pendientes de extracción?
¿Qué normas están pendientes de verificar?
¿Qué fuente oficial respalda esta afirmación?
¿Qué normas desarrolla o modifica una norma concreta?
```

La IA debe poder contestar usando:

* índices YAML;
* fichas Markdown;
* relaciones YAML;
* chunks trazables;
* fuentes oficiales.

Si dudas entre hacerlo complejo o útil, elige **útil**.
Si dudas entre inventar o dejar pendiente, deja **pendiente**.
Si dudas entre copiar mucho texto o resumir con fuente, **resume con fuente**.
Si dudas entre borrar o marcar, **marca**.

Este repositorio existe para tener la normativa educativa de Canarias bien analizada, ordenada, enlazada e indexada para sistemas de inteligencia artificial.
