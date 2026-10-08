# Diario — 2026-08-05: mojibake en los textos oficiales y literalidad de las fichas parciales

## Hecho

Al extender a las 32 fichas parciales la comprobación de literalidad que `TAREA-072` estrenó
con las completas, ninguna competencia de Primaria ni de Infantil aparecía en su decreto. Antes
de atribuirlo a las fichas se revisó el texto de contraste, y ahí estaba el problema.

### 33 de 97 copias locales estaban dobles-codificadas

`ANEXO 1` figuraba como `ANEXOÂ 1`, y `Competencia específica` no aparecía **ni una vez** en los
decretos de Primaria e Infantil porque estaba escrito `Competencia especÃ­fica`. Un tercio del
material que alimenta la búsqueda y el RAG del corpus era parcialmente inservible sin que nada
lo detectara.

Los ficheros son mixtos: la cabecera de exportación —con URL oficial, fecha de consulta y la
advertencia de R16— estaba sana, y solo el cuerpo llegó dañado, así que revertir el fichero
entero fallaba. `11_calidad/reparar_mojibake.py` repara solo los tramos con la firma del daño y
únicamente si decodifican limpio como UTF-8.

Resultado: 33 ficheros reparados, cero mojibake en los 97. `Competencia específica` pasa de 0 a
52 apariciones en Primaria y de 0 a 12 en Infantil. Detalle en `TAREA-074`.

### La `descripcion` de las fichas parciales es un resumen

Con los textos ya sanos, la comprobación sigue dando que la mayoría de las 201 competencias no
reproducen el decreto. Verificado caso a caso, `CUR-037` competencia 1:

- Ficha: «…incorporando actividades físicas y deportivas en las rutinas diarias para mejorar la
  calidad de vida.»
- Decreto: «…seleccionando e incorporando intencionalmente…»

Arranca con la redacción oficial y a partir de ahí resume. Solo 9 de 201 coinciden en doce
palabras o más.

No es un defecto nuevo: es la otra cara de que estas fichas sean parciales. Pero importa,
porque un RAG que cite una de ellas estaría citando una paráfrasis como si fuera el texto de la
norma. Se anota en `PREG-008` y se amplía el alcance de `TAREA-066` a `TAREA-069`: al
desbloquearse habrá que sustituir `descripcion` por el enunciado literal y renombrar el campo a
`enunciado_oficial`.

## Cautela sobre el método

El reparto exacto (9 literales, 29 que empiezan literales y resumen, 52 que solo coinciden en el
arranque, 111 sin coincidencia) es menos fiable en Primaria e Infantil, cuyos decretos tienen
otra estructura y donde no se ha localizado el bloque competencial. El hecho cualitativo sí está
verificado.

## IDs consumidos

`TAREA-074`.

## Pendiente

- El validador no comprueba la codificación de las copias locales. Convendría añadirlo, y
  revisar el proceso de exportación que introdujo el daño.
- `PREG-008` acumula ya cinco problemas distintos; conviene resolverla antes de seguir tocando
  fichas curriculares.
