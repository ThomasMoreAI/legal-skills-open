# Diario — 2026-08-23: Auditoría y normalización del corpus (TAREA-091)

## Qué se ha hecho

Auditoría documental completa (validador oficial + dos pasadas paralelas de
revisión) seguida de corrección en seis bloques, cada uno con commit propio:

- **Bloque A — datos de tareas**: corregida la entrada corrupta de `TAREA-069`
  en `status.yaml` (duplicaba título y `relacionadas` de TAREA-075); alineados
  los estados contradictorios de `TAREA-010` (ficha), `TAREA-089` y
  `TAREA-090` (`06_indices/tareas.yaml`); sustituidas en `relacionadas` las
  referencias a `NOR-048`/`NOR-049` (retirados por DEC-0010) por sus fusiones
  `NOR-044`/`NOR-046` en `status.yaml`, `06_indices/tareas.yaml` y
  `06_indices/preguntas.yaml`.
- **Bloque B**: anulados los `siguiente_accion` residuales de 13 tareas
  verificadas como completadas (TAREA-036, 064, 066-068, 070, 073, 077-079,
  081, 082 y 084). Se conservan los informativos de TAREA-029 y TAREA-051.
- **Bloque C**: eliminado el sangrado íntegro a 4 espacios de los 4 resúmenes
  IA (`resumen-NOR-001` a `NOR-004`); ahora cumplen AGENTS.md §5.1.
- **Bloque D**: migrados `CHUNK-00006` a `CHUNK-00022` del esquema ad-hoc
  (`contenido`, `<aviso>`) a `schemas/chunk.schema.yaml`, con metadatos
  resueltos desde `06_indices/normativa.yaml` y `06_indices/fuentes.yaml`.
  Casos especiales: `CHUNK-00008` anclado a FTE-005; `CHUNK-00014` marcado
  conforme a DEC-0011 con `nivel_evidencia: pendiente-verificacion`; el origen
  `TRANSVERSAL` de `CHUNK-00015` se normaliza a `NOR-005` (con las tres normas
  en `relaciones.normas`). `FTE-053` pasa a `estado_fuente: "Superada"` en su
  índice (ya estaba retirada por DEC-0011 pero el índice decía «Activa»).
- **Bloque E**: frontmatter nuevo para las 27 fichas curriculares `.md` que no
  lo tenían (Infantil, Primaria, Bachillerato), generado desde sus `.yaml`
  emparejados, y para el ADR `DEC-0006`.
- **Bloque F**: el validador cubre ahora los tres puntos ciegos que permitían
  que lo anterior pasara CI: valida los chunks contra su esquema y su índice
  (entidad CHUNK nueva), exige frontmatter válido en los 50 `.md` curriculares
  (`CURRICULARES-MD`) y detecta sangrado sistemático en resúmenes
  (`RESUMENES`). Verificado con pruebas negativas.

## IDs consumidos

- `TAREA-091`. No se crean otras entidades nuevas.

## Estado final

`python3 11_calidad/validar_corpus.py`: **0 errores · 3 avisos**. Los avisos
son los conocidos sobre copias locales de NOR-017/NOR-018/NOR-050 (ámbito de
TAREA-085 y DEC-0011). Única pregunta abierta del corpus: PREG-013.
