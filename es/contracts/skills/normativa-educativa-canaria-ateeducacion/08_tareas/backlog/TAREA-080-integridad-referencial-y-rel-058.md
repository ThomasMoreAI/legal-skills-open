---
id: TAREA-080
titulo: "Añadir la comprobación de integridad referencial al validador y corregir REL-058"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [REL-058, FTE-075, NOR-046, NOR-068, PREG-009]
---

# TAREA-080 — Integridad referencial

## Motivo

Al fusionar `NOR-049` en `NOR-046` quedaron referencias colgadas apuntando a un
identificador retirado, y nada las detectaba. El validador comprobaba los esquemas, los
índices y la codificación, pero no que las entidades citadas por otras fichas existieran.

## Hallazgo inesperado: REL-058

La primera ejecución de la comprobación encontró **dos** identificadores rotos, no uno.
El segundo era `REL-058`, citado por `FTE-075` y por `TAREA-061`.

`REL-058` **sí existía**, pero guardada como `.md` cuando la convención del repositorio y
`AGENTS.md` §11 exigen YAML: es el único de los 57 ficheros de `05_relaciones/` con esa
extensión. Por eso escapaba a la vez al validador —cuyo patrón es `REL-*.yaml`— y a la
sincronización de índices de `TAREA-063`, que usaba el mismo patrón. Llevaba desde el
2026-07-20 sin figurar en `06_indices/relaciones.yaml`.

Su contenido era YAML válido, así que la corrección fue renombrar el fichero y añadir su
entrada al índice. Nada que reconstruir.

## Trabajo realizado

- `11_calidad/validar_corpus.py` incorpora el tipo `REFERENCIAS`: recorre los campos
  estructurados de relación —`relacionadas`, `fuente_principal`, `fuente`, `norma_base`,
  `origen`, `destino` y las seis claves de `relaciones`— y da error si citan una entidad
  que no existe como ficha.
- Solo mira campos estructurados, no la prosa: el cuerpo de una ficha menciona
  legítimamente identificadores retirados para dejar constancia histórica, como hacen
  `NOR-046` y `FTE-051` con `NOR-049`.
- `REL-058` renombrada a `.yaml` y registrada en el índice.
- Tres referencias colgadas a `NOR-049` reapuntadas a `NOR-046`, la ficha superviviente
  que describe la misma resolución: en `PREG-009`, `TAREA-055` y `TAREA-078`.

## Nota sobre los huecos de numeración

La comprobación también expuso que `REL-013`, `REL-014` y `REL-015` no existen ni como
ficha ni en el índice. Son huecos de numeración sin usar, legítimos por R10, que no
requieren acción: nadie los referencia.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-080`. No se crean entidades nuevas.
