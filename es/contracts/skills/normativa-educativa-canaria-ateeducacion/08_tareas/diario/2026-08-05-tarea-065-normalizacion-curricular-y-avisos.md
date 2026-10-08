# Diario — 2026-08-05: normalización curricular y recalibrado de avisos (TAREA-065)

## Hecho

### Dos fallos de índice que nadie veía

Investigando las 15 entradas huérfanas de `06_indices/tareas.yaml` aparecieron dos entradas más
con la `ruta` mal: `TAREA-025` apuntaba a un nombre de fichero inexistente y **`TAREA-055`
apuntaba a la ficha de `TAREA-054`**. El validador no lo detectaba porque solo comprobaba que el
ID estuviera presente.

Se añaden dos comprobaciones:

- Cada `ruta` del índice resuelve y su nombre corresponde al ID de la entrada.
- Campos espejo: si índice y ficha discrepan en `estado_extraccion`, `etapa`, `materia`,
  `norma_base` o `fuente`, es error y manda la ficha.

La segunda destapó de inmediato una discrepancia real: `06_indices/curriculos.yaml` daba
`norma_base: NOR-060` a `CUR-053` mientras la ficha y `TAREA-037` decían `NOR-058`. `NOR-058` es
el RD 289/2023 que actualiza el título de Integración Social; `NOR-060` es el RD 1074/2012 del
que vienen los módulos comunes. Corregido el índice y registrado `NOR-060` como
`relacionada_con` para no perder el vínculo.

### Los 89 avisos, cubo a cubo

- **35 de `fecha_analisis`**: no eran deuda. R5 solo la exige cuando hay análisis. Sale de los
  campos recomendados.
- **22 de `relacionadas`**: computadas por inversión —quién declara esa fuente en
  `fuente_principal`, `fuente` o `evidencia.fuente`—. 13 reciben referencias, 9 reciben `[]`.
- **15 de `nivel_evidencia`**: antes de asignarlo se comprobaron las 15 URL oficiales. **11
  resuelven** y pasan a `confirmado-fuente-primaria`. **4 devuelven 404** (`FTE-045`, `FTE-048`,
  `FTE-049`, `FTE-051`) y pasan a `pendiente-verificacion` con `estado_fuente: Pendiente de
  verificación`. Esas cuatro necesitan que se localice su ubicación actual.
- **2 de `temas`**: `NOR-022` y `NOR-023` etiquetadas con vocabulario ya en uso.
- **15 huecos de índice**: comprobado en el historial de git que ninguna de esas fichas existió
  jamás. Se marcan `ficha: null` con comentario. El hueco pasa a ser explícito en lugar de un
  descuido, y no se fabrica una ficha para taparlo (R1).

### La normalización curricular

Las 32 fichas de la Forma B se migran al contenedor único `elementos`, con `bloques_saberes`
renombrado a `saberes_basicos`. Los metadatos que faltaban —`url_oficial`, `fecha_consulta`,
`estado_vigencia`— se derivan de la `FTE` y la `NOR` que la propia ficha ya declaraba, que es la
convención que seguían las fichas completas.

La transformación se hizo sobre el texto, no reserializando el YAML, para que el diff fuera
mínimo y revisable; cada fichero se verificó comparando el resultado con el original para
garantizar que ninguna lista de contenido se alteró.

Al medir contra `DEC-0004` apareció algo que `PREG-007` no contemplaba: **las 8 fichas de FP
declaraban `completado` con 1 de los 4 elementos obligatorios**. No están incompletas. La FP se
ordena por módulos profesionales con resultados de aprendizaje según la LOFP 3/2022, y los
cuatro elementos de `DEC-0004` —pensados para el régimen general LOMLOE— no le aplican.

`DEC-0007` recoge las tres cosas: contenedor único, dos modelos de contenido según el tipo de
enseñanza, y `parcial` como estado intermedio explícito entre `pendiente` y `completado`.

## Resultado

El validador pasa de 0 errores y 89 avisos a **0 errores y 0 avisos**, con tres comprobaciones
más que antes no existían. El esquema curricular vuelve a exigir `url_oficial`,
`fecha_consulta`, `estado_vigencia` y `observaciones` a las 58 fichas, y las 58 los cumplen.

Reparto real de la extracción curricular: 18 fichas de ESO completas, 8 de FP completas según su
modelo, 32 parciales a la espera de descriptores operativos.

## IDs consumidos

`TAREA-065` a `TAREA-069`, `DEC-0007`. Ninguna entidad `FTE`, `NOR`, `CUR`, `REL` o `CHUNK`
nueva.

## Pendiente

- `TAREA-066` a `TAREA-069`: descriptores operativos de 32 fichas, por etapa.
- Localizar la ubicación actual de las 4 fuentes cuya URL oficial devuelve 404.
