# Normativa Educativa Canaria

Repositorio IA-friendly para recopilar, analizar, resumir, indexar y relacionar normativa educativa y currículos aplicables a Canarias.

[![Normativa Educativa Canaria para tu inteligencia artificial](docs/assets/img/og-image.jpg)](https://ateeducacion.github.io/normativa_educativa_canaria/assets/img/og-image.jpg)

> Los resúmenes de este repositorio no sustituyen la consulta de las fuentes oficiales.

## Propósito

- centralizar fuentes oficiales y fichas normativas en formatos legibles;
- mantener metadatos estructurados en YAML;
- preparar contenido trazable para búsqueda semántica, RAG y asistentes internos;
- separar normativa, currículos, análisis, relaciones, preguntas y tareas.

## Principios del repositorio

1. **Sencillez primero.**
2. **IA-friendly.**
3. **Markdown para contenido narrativo.**
4. **YAML para metadatos estructurados.**
5. **Fuente oficial obligatoria.**
6. **Fecha de consulta obligatoria.**
7. **Fecha de análisis obligatoria cuando haya interpretación o resumen.**
8. **Estado de vigencia obligatorio.**
9. **Relaciones normativas explícitas.**
10. **No copiar normas completas por defecto si basta con resumen, cita y enlace oficial; cuando haga falta lectura rápida, usar copia local trazable y subordinada a la fuente oficial.**
11. **No mezclar normativa con recursos no normativos.**
12. **No borrar contenido histórico: marcar como derogado, obsoleto o sustituido.**
13. **Usar IDs estables y correlativos.**
14. **Todo resumen debe indicar que no sustituye la fuente oficial.**
15. **Todo índice debe ser legible por humanos y máquinas.**

## Estructura principal

- `00_gobierno-repositorio/`: metodología, criterios editoriales y glosario operativo.
- `01_fuentes/`: fichas de fuentes oficiales.
- `02_normativa/`: fichas Markdown de normas.
- `03_curriculos/`: currículos en Markdown y YAML.
- `04_analisis/`: notas, comparativas y síntesis.
- `05_relaciones/`: relaciones normativas y curriculares.
- `06_indices/`: índices YAML del corpus.
- `07_corpus_ia/`: resúmenes y chunks para IA.
- `08_tareas/`: backlog, diario y preguntas abiertas.
- `09_decisiones-editoriales/`: ADRs del repositorio.
- `10_plantillas/`: plantillas reutilizables.
- `11_calidad/`: validaciones e informes.
- `docs/`: portal público, guías metodológicas y esquema de datos.
- `DESIGN.md`: sistema de diseño y reglas de experiencia de usuario del portal.

## Arranque rápido

- Índice principal: [index.md](index.md)
- Sistema de diseño del portal: [DESIGN.md](DESIGN.md)
- Gobierno del repositorio: [00_gobierno-repositorio/](00_gobierno-repositorio/)
- Fuentes: [06_indices/fuentes.yaml](06_indices/fuentes.yaml)
- Normativa: [06_indices/normativa.yaml](06_indices/normativa.yaml)
- Textos oficiales: [06_indices/textos-oficiales.yaml](06_indices/textos-oficiales.yaml)
- Currículos: [06_indices/curriculos.yaml](06_indices/curriculos.yaml)
- Códigos administrativos de áreas y materias: [03_curriculos/codigos-materias-canarias.md](03_curriculos/codigos-materias-canarias.md)
- Relaciones: [06_indices/relaciones.yaml](06_indices/relaciones.yaml)
- Preguntas abiertas: [06_indices/preguntas.yaml](06_indices/preguntas.yaml)

## Uso como contexto de IA

Vía rápida con un cliente compatible:

1. Use la **Skill de Experto en Normativa Canaria** para obtener el mejor rendimiento.
2. O proporcione la URL de este repositorio directamente a su asistente.

Para más detalle sobre prompts y ejemplos de uso, consulte el [Portal del Corpus](https://ateeducacion.github.io/normativa_educativa_canaria/).

## Estado actual del corpus

<!-- inventario-corpus:inicio -->
_Sección generada desde los índices canónicos; no se edita manualmente._

- Fuentes: **138** (FTE-001 a FTE-138, con posibles huecos reservados).
- Normativa: **129** (NOR-001 a NOR-131, con posibles huecos reservados).
- Currículos: **58** (CUR-001 a CUR-058, con posibles huecos reservados); bachillerato: 14, eso: 23, formacion-profesional: 8, infantil: 3, primaria: 10.
- Relaciones: **100** (REL-001 a REL-103, con posibles huecos reservados).
- Chunks IA: **22** (CHUNK-00001 a CHUNK-00022, con posibles huecos reservados).
- Tareas: **98**; Hecha: 98.
- Copias locales de textos oficiales: **139** (normativa: 102; currículos: 37).
- Inventario legible por máquinas: [docs/datos/inventario.json](docs/datos/inventario.json).
<!-- inventario-corpus:fin -->
