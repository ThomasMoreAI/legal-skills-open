# Diario — 2026-08-05: la re-exportación destapó algo peor que copias mal exportadas

## Lo que se buscaba

`TAREA-084` pedía re-exportar trece copias locales que contenían una norma distinta de la que
declaraban. Trabajo mecánico, en principio.

## La causa, que resultó ser trivial

Las cabeceras apuntaban a URL de la forma `/boc/AAAA/NNN/001.html`. Ese último número **no es el
número de la disposición**: es su posición dentro del boletín. La exportación original lo dejó
casi siempre en `001` y se llevó la primera disposición de cada boletín, fuera cual fuese.
`NOR-044` es el caso puro: pedía `002`, la orden de evaluación estaba en `001`, y se trajo la
resolución del hospital que ocupaba el segundo lugar.

En el BOE el mecanismo era otro: el identificador `BOE-A-` era directamente falso, así que la
copia contenía exactamente la disposición de ese identificador. El error estaba en la ficha, no
en la exportación. Conviene señalarlo porque la advertencia que pusimos por la mañana decía «la
cabecera es correcta», y para esas dos no lo era.

## La herramienta

`11_calidad/reexportar_texto_oficial.py` localiza la disposición **por su título** dentro del
sumario y extrae del PDF firmado, no del HTML. Eso resuelve de paso los anexos publicados como
imagen, que el HTML omite.

Tuvo que aprender más de lo previsto sobre el BOC: tres marcados distintos de sumario desde 2006,
tres formatos de índice anual, y un cambio de esquema de URL hacia 2025 —de posición a número de
disposición— que además dejó de publicarse en el sumario. También busca en el archivo cuando el
boletín declarado es el equivocado, localizando el boletín por búsqueda binaria sobre las fechas.

La salvaguarda que más sirvió fue la más simple: comprobar, antes de escribir, que el texto
extraído habla de lo que dice el título. Evitó un falso positivo real en `NOR-017`, donde una
resolución del mismo día sobre el Ayuntamiento de El Sauzal alcanzaba coincidencia suficiente por
puro juego de fechas.

## Lo que apareció debajo

Tres copias resistieron todos los métodos. Para descartar un fallo de la herramienta se
recorrieron **los sumarios de los 765 boletines** publicados en 2010, 2014 y 2023. Las normas no
existen:

- `NOR-017` declara una Orden de 2014 sobre organización de escuelas infantiles. En todo 2014
  sólo hay dos decretos que **crean** escuelas infantiles municipales. Su título coincide casi
  palabra por palabra con una orden de la Comunitat Valenciana.
- `NOR-018` toma la fecha de una orden real —la de 1 de septiembre de 2010, sobre los EOEP— y el
  objeto de otra —la de 9 de octubre de 2013, que sí desarrolla el Reglamento Orgánico—.
- `NOR-050` declara una orden de 2023 sobre procedimientos NEAE. En todo 2023 no hay ninguna
  disposición sobre NEAE salvo un extracto de convocatoria de ayudas.

Las tres estaban registradas como `confirmado-fuente-primaria`.

## Por qué esto es peor que una copia mal exportada

Una copia equivocada se detecta al leerla. Una ficha que describe una norma inexistente no se
detecta nunca desde dentro del corpus: tiene título verosímil, fechas coherentes, fuente asignada
y estado de vigencia. Y sostiene lo que se construya encima.

`NOR-050` lo demuestra. Sostiene `REL-048`, que declara que deroga los procedimientos de
`NOR-025`, la Orden de 13 de diciembre de 2010. Si la orden de 2023 no existe, `NOR-025` sigue
vigente y el corpus estaba afirmando lo contrario. Para un corpus normativo ese es el peor error
posible: no una laguna, sino una afirmación falsa sobre qué está en vigor. Las dos relaciones
citaban además localización concreta —«disposición derogatoria única»— de un texto que nadie
encuentra.

Nada se ha borrado. Las tres fichas pasan a `Pendiente de verificación`, `FTE-053` queda marcada
como catalogación errónea, las relaciones y el chunk quedan degradados, y `NOR-025` **no** se
toca. Abiertas `PREG-010`, `PREG-011` y `PREG-012`, y `TAREA-085` con prioridad crítica.

## La comprobación que faltaba

La auditoría que descubrió esto se ha dejado como modo `--auditar` de la herramienta: contrasta
la `url_oficial` de cada ficha `NOR` contra el sumario de su boletín. Encontró de paso tres
enlaces más que apuntaban a otra disposición del boletín correcto. De las 40 fichas con URL de
disposición del BOC, 37 contrastan bien y las 3 restantes son las de `TAREA-085`.

No se ha añadido al validador porque necesita red y el validador debe poder correr sin ella.

## El resto de la tanda

- **Religión.** `CUR-033` se re-extrae íntegramente desde el Anexo II del BOE: 6 competencias, 36
  criterios y 84 saberes, frente a las 6 paráfrasis, 6 criterios y 4 bloques que tenía. La
  literalidad se verificó carácter a carácter: 6 de 6, 31 de 36 y 81 de 84 coinciden, y los ocho
  restantes rompen exactamente donde el PDF intercala su marca de página. El corpus queda en 58
  fichas curriculares completadas y ninguna parcial.
- **Las tres resoluciones de FP** que `TAREA-064` arrastraba desde julio se identificaron
  cruzando el snapshot del monitor con el corpus: de sus 76 URL, exactamente tres se registraron
  el día de `TAREA-061` y no dejaban rastro. Catalogadas como `FTE-080` a `FTE-082` y `NOR-073` a
  `NOR-075`.
- **Anexos accesorios.** Cinco de las seis copias incompletas quedan completas al extraerlas del
  PDF. `NOR-025` pasa de 750 a 1.729 líneas y `NOR-026` de 742 a 1.689, lo que importa
  especialmente ahora que son el marco NEAE que hay que dar por vigente. `NOR-015` no se puede
  completar: su PDF de 2000 son 19 páginas escaneadas sin capa de texto.

## Un informe que no resistió la comprobación

Un agente informó de que el servidor del BOC le había servido, bajo el nombre de fichero
correcto, el PDF de otra resolución. Descargando la misma URL tres veces devuelve siempre el
documento correcto con idéntico hash. Lo que ocurrió es que los tres agentes trabajaban en
paralelo y el encargo les sugería a todos la misma ruta temporal: se pisaron el fichero entre
ellos. Queda anotado para que no se registre como un problema de integridad del BOC, que no lo
es.

## IDs consumidos

`FTE-080`, `FTE-081`, `FTE-082`, `NOR-073`, `NOR-074`, `NOR-075`, `PREG-010`, `PREG-011`,
`PREG-012`, `TAREA-085`.
