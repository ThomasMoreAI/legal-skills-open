---
id: TAREA-063
titulo: "Hacer descubribles las skills del repositorio y poner en marcha la validación automática del corpus"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-007, FTE-075, FTE-076, FTE-077, NOR-068, NOR-069, NOR-070, REL-059, REL-060, TAREA-061, TAREA-062]
---

# TAREA-063 — Skills descubribles y validación automática del corpus

## Objetivo

Resolver dos problemas detectados al auditar la configuración de agentes del repositorio:

1. Las catorce skills documentadas en `AGENTS.md` §14 existían en `.agents/skills/` pero
   ningún cliente las cargaba, porque Claude Code sólo descubre skills en `.claude/skills/`,
   `~/.claude/skills/` y plugins.
2. Los ocho esquemas de `schemas/` no los ejecutaba nada. El control previsto en §16.3 sólo
   comprobaba que el YAML parseara, cosa que una ficha puede cumplir incumpliendo su esquema.

## Trabajo realizado

### Skills

- Creados enlaces simbólicos en `.claude/skills/` hacia cada skill de `.agents/skills/`, de modo
  que Claude Code las descubra sin renunciar a la convención `.agents`, portable entre clientes.
- Ajustado `.gitignore` para versionar `.claude/skills/` manteniendo ignorado el resto de
  `.claude/`.
- Reescritas las descripciones de las catorce skills: antes eran infinitivos escuetos sin
  términos de disparo, que no bastan para que el modelo decida cargarlas. Ahora declaran qué
  hacen y cuándo usarlas, en tercera persona, y añaden `when_to_use` con frases de disparo.
- Especializada en cada skill la sección «Plantillas relacionadas», que antes listaba las cinco
  plantillas del repositorio en todas.
- Ampliada `control-calidad-documental` con el procedimiento de validación.
- Creada `publicacion-portal` para los cambios en `docs/` y su publicación.

### Validación del corpus

- Creado `11_calidad/validar_corpus.py`, que comprueba los esquemas de `schemas/`, la
  coincidencia entre el `id` del frontmatter y el nombre del fichero, y la cobertura de los
  índices de `06_indices/` en ambos sentidos.
- Creado `.github/workflows/validar-corpus.yml`, que lo ejecuta en cada push y cada pull request.
- Actualizado `AGENTS.md` §16.3 para sustituir la comprobación de parseo por el validador.

### Deriva corregida entre esquemas y corpus

La primera ejecución arrojó 1.103 errores. Casi todos eran esquemas desactualizados respecto a
un corpus que había crecido, no defectos de las fichas:

- `temas` se validaba contra una lista cerrada de 18 etiquetas cuando el corpus usa más de cien
  y crece con cada norma. Pasa a validarse por forma (kebab-case).
- `estado_vigencia` se validaba contra un enum que no admitía el matiz que el corpus necesita
  («Vigente con modificaciones; instrucción sexta modificada por NOR-070»). Pasa a exigir un
  prefijo controlado seguido de matiz libre, conservando la clasificación legible por máquina.
- `texto_oficial` se rechazaba en 22 fichas: la §10 bis de `AGENTS.md` se incorporó al corpus
  pero nunca a los esquemas.
- `etapas_afectadas` no admitía `todas` ni `ensenanzas-deportivas`.
- El esquema curricular describía sólo una de las dos formas de ficha que conviven hoy y
  declaraba `elementos` con listas de cadenas cuando contienen objetos.
- `tarea.schema.yaml` exigía `siguiente_accion` en tareas ya cerradas y no admitía el estado
  `En progreso`.
- `relacion.schema.yaml` exigía `observaciones`, que es metadato opcional.
- `fuente.schema.yaml` exigía campos que `AGENTS.md` §7 no pide para dar de alta una fuente.

### Correcciones mecánicas del corpus

- Siete fichas `REL` declaraban `fuente:` plano en lugar del bloque `evidencia:` que exige
  `AGENTS.md` §11. Convertidas, con `localizacion: "[PENDIENTE]"` (R15) al no constar el
  precepto exacto, `fecha_registro` derivada del alta en git y `nivel_evidencia:
  pendiente-verificacion`.
- `PREG-004` y `PREG-005` no tenían frontmatter. Añadido, derivado del propio cuerpo de la ficha.
- Unificado vocabulario: `estado_extraccion: completo` → `completado` (CUR-046, CUR-053);
  `estado: Finalizada` → `Hecha` (TAREA-011, TAREA-014, TAREA-015).
- `FTE-054` usaba `normas_relacionadas` en lugar de `relacionadas`.

### Índices

Incorporadas al índice las entidades que existían como ficha sin estar registradas, incumpliendo
R11: `FTE-075` a `FTE-077`, `NOR-068` a `NOR-070`, `REL-059`, `REL-060`, `TAREA-061` y
`TAREA-062`. Todas proceden de `TAREA-061` y `TAREA-062`, cuyo trabajo se integró sin cerrar el
paso de actualización de índices. Cada entrada se ha derivado de su propia ficha.

## Resultado

El validador pasa de 1.103 errores a **0 errores y 89 avisos**. Los avisos no bloquean:
señalan campos recomendados ausentes y quince entradas de `06_indices/tareas.yaml` cuya ficha
nunca se creó, que son deuda documental histórica y no se pueden resolver sin reconstruir lo
que se hizo.

## Pendiente para cierre

- `PREG-007` queda abierta: la convergencia de las dos formas de ficha curricular es una
  decisión editorial, no una corrección mecánica.
- `TAREA-061` y `TAREA-062` siguen marcadas «En progreso» en su propia ficha aunque su trabajo
  está integrado en `main`. No se ha modificado su estado por no cerrar tareas ajenas.

## Coordinación con trabajo paralelo

IDs consumidos en esta tarea: `TAREA-063` y `PREG-007`. No se han creado entidades `FTE`, `NOR`,
`CUR`, `REL` ni `CHUNK`. Las entradas de índice añadidas para `TAREA-061` y `TAREA-062`
reproducen literalmente lo que declaran sus fichas, sin alterar su contenido ni su estado.
