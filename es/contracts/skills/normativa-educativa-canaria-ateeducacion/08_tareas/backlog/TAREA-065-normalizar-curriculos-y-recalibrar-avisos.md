---
id: TAREA-065
titulo: "Normalizar las fichas curriculares, recalibrar los avisos del validador y cerrar los huecos de índice"
estado: "Hecha"
prioridad: "Alta"
tipo: "calidad-documental"
responsable: "@.agents/skills/control-calidad-documental"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [PREG-007, DEC-0007, TAREA-063, TAREA-066, TAREA-067, TAREA-068, TAREA-069]
---

# TAREA-065 — Normalización curricular y recalibrado de avisos

## Objetivo

Resolver lo que `TAREA-063` dejó abierto: la convergencia de las dos formas de ficha curricular
(`PREG-007`) y los 89 avisos del validador, y cerrar de paso los fallos de índice que salieron
al investigarlos.

## Trabajo realizado

### Rutas de índice y comprobación nueva

- Corregidas dos rutas erróneas en `06_indices/tareas.yaml`: `TAREA-025` apuntaba a un nombre de
  fichero inexistente y `TAREA-055` apuntaba **a la ficha de `TAREA-054`**.
- Añadida al validador la comprobación de que cada `ruta` del índice resuelve y su nombre
  corresponde al ID de la entrada. Sin ella el cruce anterior era indetectable.
- Añadida la comprobación de campos espejo: cuando el índice y la ficha discrepan en
  `estado_extraccion`, `etapa`, `materia`, `norma_base` o `fuente`, es error y manda la ficha.
  Esta comprobación destapó que `06_indices/curriculos.yaml` declaraba `norma_base: NOR-060`
  para `CUR-053` mientras la ficha y `TAREA-037` decían `NOR-058`.

### Divergencia de CUR-053

`NOR-058` es el Real Decreto 289/2023, que actualiza el título de Técnico Superior en
Integración Social; `NOR-060` es el Real Decreto 1074/2012, del que proceden los módulos comunes
recogidos en `modulos_comunes_base`. Se corrige el índice a `NOR-058` y se registra `NOR-060` en
`relaciones.relacionada_con` para no perder el vínculo.

### Vocabulario de etapa

`etapa: fp` unificado con `formacion-profesional` en 8 fichas y 8 entradas de índice. El alias
se retira del enum del esquema.

### Recalibrado de los avisos de FTE

- `fecha_analisis` sale de los campos recomendados: R5 solo la exige cuando hay análisis, y una
  fuente catalogada sin analizar legítimamente no la tiene (35 avisos).
- `relacionadas` computada por inversión: una fuente se relaciona con las entidades que la
  declaran en `fuente_principal`, `fuente` o `evidencia.fuente`. 13 fuentes reciben sus
  referencias y 9 reciben `[]`, que es lo correcto para una fuente que aún no usa nadie.
- `nivel_evidencia`: comprobadas las 15 URL oficiales antes de asignarlo. **11 resuelven** y
  reciben `confirmado-fuente-primaria`; **4 devuelven 404** (`FTE-045`, `FTE-048`, `FTE-049`,
  `FTE-051`) y pasan a `pendiente-verificacion` con `estado_fuente: Pendiente de verificación`.
- Etiquetadas las dos fichas `NOR` sin `temas` (`NOR-022` y `NOR-023`) con vocabulario ya en uso.

### Normalización curricular

Las 32 fichas de la Forma B se migran al contenedor único `elementos`, renombrando
`bloques_saberes` como `saberes_basicos`. Los metadatos ausentes se derivan de la `FTE` y la
`NOR` que la propia ficha declaraba. Se marcan `estado_extraccion: parcial` y se anota en
`observaciones` qué falta exactamente.

La transformación se hizo sobre el texto para que el diff fuera mínimo, y cada fichero se
verificó comparando el YAML resultante con el original: ninguna lista de contenido se alteró.

Al medir contra `DEC-0004` apareció un dato que no estaba en `PREG-007`: las 8 fichas de FP
declaraban `completado` con 1 de los 4 elementos obligatorios. No están incompletas — la FP se
ordena por módulos profesionales según la LOFP 3/2022 y los cuatro elementos no le aplican.
`DEC-0007` lo recoge.

### Huecos de índice

Las 15 entradas de `06_indices/tareas.yaml` cuya ficha nunca existió —comprobado en el historial
de git— se marcan con `ficha: null` y un comentario. El hueco pasa a ser explícito y el validador
deja de avisar. No se fabrican fichas para taparlo.

## Resultado

El validador pasa de **0 errores y 89 avisos** a **0 errores y 0 avisos**, con tres
comprobaciones nuevas que antes no existían: rutas de índice, campos espejo y huecos reconocidos.

`PREG-007` queda resuelta en `DEC-0007`.

## Pendiente

La extracción de los descriptores operativos que faltan en 32 fichas queda planificada por etapa
en `TAREA-066` (Bachillerato, 14), `TAREA-067` (Primaria, 10), `TAREA-068` (ESO, 5) y
`TAREA-069` (Infantil, 3).

Las 4 fuentes con URL rota necesitan que se localice su ubicación actual en el portal oficial.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-065` a `TAREA-069` y `DEC-0007`. No se han creado entidades `FTE`, `NOR`,
`CUR`, `REL` ni `CHUNK`: solo se han completado y corregido las existentes.
