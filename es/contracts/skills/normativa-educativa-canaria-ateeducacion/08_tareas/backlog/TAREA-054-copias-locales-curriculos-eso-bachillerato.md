---
id: TAREA-054
titulo: "Publicar copias locales rápidas de currículos ESO y Bachillerato"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-04-27
fecha_actualizacion: 2026-04-27
relacionadas: [FTE-002, FTE-009, FTE-012, CUR-001, CUR-023, CUR-037, CUR-058, TAREA-053]
---

# TAREA-054 — Publicar copias locales rápidas de currículos ESO y Bachillerato

## Objetivo

Añadir copias locales rápidas en texto plano para los currículos de materias de ESO y Bachillerato ya registrados en el corpus, manteniendo trazabilidad con la fuente oficial y con `06_indices/textos-oficiales.yaml`.

## Criterios de cierre

- Publicar en `07_corpus_ia/textos-completos/` las copias locales rápidas de los currículos `CUR-001` a `CUR-023` y `CUR-037` a `CUR-058` de Bachillerato.
- Actualizar `06_indices/textos-oficiales.yaml` con el PDF oficial específico y la ruta local de cada copia.
- Reflejar la nueva cobertura en la documentación pública y en el seguimiento de tarea.
- Validar YAML y comprobar que todas las rutas locales declaradas existen.

## Resultado

- Publicadas 37 copias locales rápidas en `07_corpus_ia/textos-completos/` para los currículos `CUR-001` a `CUR-023` y `CUR-037` a `CUR-045`, `CUR-054` a `CUR-058`.
- Actualizado `06_indices/textos-oficiales.yaml` con PDF oficial específico, fecha de consulta 2026-04-27 y huella `sha256` de cada copia local.
- Actualizados `README.md`, `llms.txt` y `llms-full.txt` para reflejar la nueva cobertura: 40 copias locales rápidas trazables en total.

## IDs consumidos

- `TAREA-054`.

## Coordinación con trabajo paralelo

- La tarea consume `TAREA-054` y afecta a `06_indices/textos-oficiales.yaml`, `status.yaml`, `06_indices/tareas.yaml`, documentación de cobertura y `07_corpus_ia/textos-completos/`.
- No se prevé crear nuevos IDs de `FTE`, `NOR`, `CUR`, `REL`, `CHUNK`, `PREG` o `DEC`.
