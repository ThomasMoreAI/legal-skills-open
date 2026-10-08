# Diario — 2026-08-05: una ficha por norma (DEC-0010)

## Hecho

`PREG-009` había dejado abierto si el desdoblamiento de una norma en varias fichas por etapa era
deliberado o duplicación. Resuelto: **una norma, una ficha**.

Antes de decidir busqué el patrón en todo el corpus por dos señales independientes —fichas que
comparten `fecha_disposicion` y `fuente_principal`, y copias locales con contenido idéntico— y
aparecieron **exactamente dos casos**, confirmados por ambas:

- Resolución conjunta 73/2025: `NOR-046` + `NOR-049`, ya fusionadas.
- Orden de 31 de mayo de 2023 sobre evaluación y promoción: `NOR-044` + `NOR-048`.

## Por qué no era inocuo

El segundo caso repite el patrón del primero, y con la misma clase de deriva. `NOR-048` se
delataba en su propio título —«Evaluación en Educación Infantil (**según** Orden de 31 de mayo de
2023)»— y además declaraba mal sus metadatos: `tipo_norma: resolucion-administrativa` y autoridad
«Dirección General de Ordenación», cuando la norma es una orden autonómica de la Consejería.

Es lo mismo que pasó con `NOR-049`, solo que allí llegó más lejos: acabó apuntando a `FTE-051`,
una fuente que describía un documento **que no existe**. Cuando una ficha duplicada necesita
metadatos propios, alguien acaba inventándolos.

Ese es el argumento de `DEC-0010`. La ventaja del desdoblamiento es real —quien busca «evaluación
en Infantil» encuentra antes una ficha titulada así que un apartado— pero se paga con duplicación
de contenido, metadatos que divergen y fuentes que se fabrican para justificar la segunda ficha.
La navegación por etapa se resuelve con `etapas_afectadas`, que ya existe y es filtrable.

## Fusión

Como en el caso anterior, las fichas no eran idénticas: `NOR-048` traía su análisis de evaluación
en Infantil —observación directa, promoción automática, informe de etapa—, conservado como
apartado 3 de `NOR-044`. Fusionar no es borrar.

`NOR-044` amplía además sus relaciones con `NOR-047`, y su fichero y copia local pierden el
«primaria» del nombre. `FTE-047` y `NOR-047`, que citaban a la retirada, se reapuntan.

## Prevención

El validador incorpora el tipo `DESDOBLAMIENTOS`, que avisa por las dos señales. Comprobado
recreando artificialmente un desdoblamiento: lo detecta por ambas vías y vuelve a cero al
retirarlo.

Es aviso y no error a propósito: puede haber casos legítimos —una norma y su corrección de
errores publicadas el mismo día desde la misma fuente— que piden mirar antes de fusionar.

## IDs consumidos

`DEC-0010`, `TAREA-083`. `NOR-048` retirado y no reutilizable.
