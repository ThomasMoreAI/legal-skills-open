# Diario — 2026-08-05: Primaria, Infantil, Bachillerato y la Resolución 24/2024

## Hecho

Segunda tanda en paralelo, esta vez toda con Sonnet por ser extracción y catalogación contra
fuente. Cinco ramas: re-exportación del anexo de Primaria encadenada con sus 10 fichas,
catalogación de la Resolución 24/2024, literalidad de Infantil y criterios de Bachillerato en
dos lotes.

## El anexo de Primaria estaba en el PDF, no en el HTML

`TAREA-077` confirmó la hipótesis: el PDF oficial del BOC, 346 páginas, sí contiene los anexos
curriculares. Re-exportado con `pdftotext -layout`, la copia local pasa de **cero a 2.938 códigos
de descriptor**.

Con eso, `TAREA-067` completó nueve de las diez fichas de Primaria. Los descriptores se mapean
**por ciclo** —«Primer ciclo», «Segundo ciclo», «Tercer ciclo»—, que es como los organiza el
decreto, y varían realmente entre ciclos en Educación Artística, Educación Física, Matemáticas y
Educación Emocional.

Dos comprobaciones que merecen mención. La primera, del propio agente: contrastó área por área el
número de competencias y de criterios extraídos contra lo que el decreto declara en su
introducción —«nueve competencias específicas… veinticuatro criterios de evaluación»—, y coincide
en las nueve. La segunda, mía: 56 de las 62 competencias se localizan literalmente en el texto
oficial, y las 6 restantes son las de `CUR-033`, que no se tocó.

Al contrastar aparecieron además dos erratas heredadas: los títulos de los bloques III a V de
saberes de `CUR-030` no correspondían al decreto, y a `CUR-032` le faltaba un bloque entero.

## Mi primera verificación estaba mal

Al comprobar la literalidad de Primaria salían 24 enunciados «no literales». No lo eran: el PDF
dispone el bloque competencial en **dos columnas** —enunciado a la izquierda, códigos a la
derecha— y `pdftotext -layout` las intercala línea a línea, de modo que «competencias clave.
Perfil de salida» aparece en mitad de la frase. Mi comprobación buscaba las doce primeras
palabras contiguas. Rehecha como búsqueda de subsecuencia, el resultado es el correcto.

Es el mismo patrón de la tanda anterior: los agentes reportan una discrepancia y la discrepancia
está en mi herramienta.

## Infantil: el mismo problema, resuelto de otra manera

`TAREA-079` descubrió que la copia local de Infantil **tampoco contiene las tablas** de bloques
competenciales: solo un marcador «Ver anexo en las páginas NNN-NNN». En vez de detenerse, el
agente descargó el PDF oficial y transcribió los once enunciados leyéndolo página a página,
después de que una primera lectura por lotes produjera un error de transcripción que él mismo
detectó y corrigió.

Las tres fichas siguen en `parcial`: falta transcribir criterios y saberes, y eso pide primero
re-exportar la copia local. Queda en `TAREA-081`.

**Dos de tres decretos curriculares tenían el anexo ausente.** Conviene revisar los 97 textos
locales buscando ese marcador: una copia puede estar bien codificada y aun así estar incompleta.

## Bachillerato y la Resolución 24/2024

Las siete fichas de Bachillerato que quedaban en `parcial` reciben sus criterios y saberes
íntegros, extraídos de los textos por materia, y pasan a `completado`. Los agentes documentaron
las normalizaciones ortotipográficas que aplicaron —espacios espurios antes de vocales
acentuadas, una «t» suelta, comas dobles— sin alterar contenido.

La Resolución Conjunta 24/2024 queda catalogada como `FTE-078` y `NOR-071`, con copia local y
cabecera R16. Es la norma a la que remite la 73/2025 para el primer ciclo de Infantil.

## Resultado

El corpus pasa de **38 fichas curriculares completadas y 20 parciales a 54 y 4**. Validador en 0
errores y 0 avisos.

Las cuatro parciales son las tres de Infantil, a la espera de `TAREA-081`, y `CUR-033`
(Religión), que no es un problema de trabajo sino de fuente: el Decreto 211/2022 delega ese
currículo en la jerarquía eclesiástica y se publica en el BOE. Además, el contenido que ya tenía
esa ficha no está trazado a ninguna `FTE`, lo que incumple R1. Queda en `TAREA-082`.

## IDs consumidos

`FTE-078`, `NOR-071`, `TAREA-081`, `TAREA-082`.
