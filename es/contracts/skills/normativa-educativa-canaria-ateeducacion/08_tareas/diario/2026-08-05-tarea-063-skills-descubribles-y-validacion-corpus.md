# Diario — 2026-08-05: skills descubribles y validación automática del corpus (TAREA-063)

## Hecho

### Las skills del repositorio no las cargaba nadie

- Las catorce skills documentadas en `AGENTS.md` §14 existían en `.agents/skills/`, pero
  Claude Code sólo descubre skills en `.claude/skills/` (proyecto), `~/.claude/skills/`
  (personal) y plugins. Ninguna llegaba a cargarse.
- Solución: un enlace simbólico por skill en `.claude/skills/` apuntando a `.agents/skills/`.
  Claude Code sigue los enlaces y lee el `SKILL.md` del destino, así que se conserva la
  convención `.agents`, portable entre clientes, sin renunciar al descubrimiento.
- `.gitignore` pasa de ignorar `.claude/` entero a ignorar `.claude/*` con excepción de
  `.claude/skills/`.
- Reescritas las catorce descripciones. Eran infinitivos escuetos («Catalogar fuentes oficiales
  y crear fichas FTE trazables») sin términos de disparo. Ahora declaran qué hacen y cuándo
  usarlas, en tercera persona, y añaden `when_to_use` con frases de disparo. La descripción es
  el único texto que ve el modelo al decidir si carga una skill.
- La sección «Plantillas relacionadas» listaba las cinco plantillas del repositorio en las
  catorce skills, incluidas las que no aplican. Especializada en cada una.
- Ampliada `control-calidad-documental` con el procedimiento de validación; creada
  `publicacion-portal` para el portal de `docs/`.

### Los esquemas no los ejecutaba nada

- `schemas/` contiene ocho esquemas JSON Schema draft 2020-12 completos, con
  `additionalProperties: false` y listas `required` exigentes, que ningún script ni flujo de
  trabajo había ejecutado nunca. El control de §16.3 sólo comprobaba que el YAML parseara, cosa
  que una ficha puede cumplir incumpliendo su esquema o faltando en su índice.
- Creado `11_calidad/validar_corpus.py`: valida esquemas, coincidencia entre el `id` del
  frontmatter y el nombre del fichero, y cobertura de los índices en ambos sentidos.
- Creado `.github/workflows/validar-corpus.yml`, que lo ejecuta en cada push y pull request.

### Deriva entre esquemas y corpus

Primera ejecución: **1.103 errores**. Casi todos por esquemas desactualizados respecto a un
corpus que había crecido, no por defectos de las fichas:

- `temas` se validaba contra 18 etiquetas cerradas; el corpus usa más de cien y crece con cada
  norma. Pasa a validarse por forma (kebab-case).
- `estado_vigencia` no admitía el matiz que el corpus necesita. Pasa a exigir prefijo controlado
  seguido de texto libre, conservando la clasificación legible por máquina (R3).
- `texto_oficial` se rechazaba en 22 fichas: la §10 bis se incorporó al corpus y a las reglas,
  pero nunca a los esquemas.
- El esquema curricular describía sólo una de las dos formas de ficha que conviven hoy.
- `tarea.schema.yaml` exigía `siguiente_accion` en tareas ya cerradas.

Correcciones mecánicas del corpus, sin inventar dato alguno (R1):

- Siete fichas `REL` declaraban `fuente:` plano en vez del bloque `evidencia:` de §11.
  Convertidas con `localizacion: "[PENDIENTE]"` (R15), `fecha_registro` derivada del alta en git
  y `nivel_evidencia: pendiente-verificacion`.
- `PREG-004` y `PREG-005` no tenían frontmatter; añadido a partir del propio cuerpo de la ficha.
- Vocabulario unificado: `completo` → `completado`, `Finalizada` → `Hecha`,
  `normas_relacionadas` → `relacionadas`.

### Índices desactualizados

`FTE-075` a `FTE-077`, `NOR-068` a `NOR-070`, `REL-059`, `REL-060`, `TAREA-061` y `TAREA-062`
existían como ficha sin estar en su índice, incumpliendo R11. Proceden de `TAREA-061` y
`TAREA-062`, cuyo trabajo se integró sin completar el paso de índices. Cada entrada se ha
derivado de su propia ficha.

## Resultado

De 1.103 errores a **0 errores y 89 avisos**. Los avisos señalan campos recomendados ausentes
y quince entradas de `06_indices/tareas.yaml` cuya ficha nunca se creó: deuda documental
histórica que no se puede resolver sin reconstruir lo que se hizo.

## IDs consumidos

`TAREA-063`, `PREG-007`. No se han creado entidades `FTE`, `NOR`, `CUR`, `REL` ni `CHUNK`.

## Pendiente

- `PREG-007`: convergencia de las dos formas de ficha curricular y del valor de `etapa` para FP.
  Es decisión editorial; el esquema admite ambas formas mientras tanto.
- `TAREA-061` y `TAREA-062` siguen «En progreso» en su ficha aunque su trabajo está en `main`.
  No se han cerrado por no tocar tareas ajenas.
