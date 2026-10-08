---
id: TAREA-081
titulo: "Re-exportar el anexo curricular del Decreto 196/2022 de Infantil desde el PDF oficial"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [NOR-047, FTE-050, TAREA-079, TAREA-077]
siguiente_accion: "Descargar boc-a-2022-212-3215.pdf y extraer el anexo con pdftotext -layout, como se hizo en TAREA-077."
---

# TAREA-081 — Re-exportar el anexo curricular de Infantil

## Problema

`07_corpus_ia/textos-completos/texto-oficial-NOR-047-decreto-196-2022-infantil.txt` **no contiene
las tablas de bloques competenciales**: en su lugar hay un marcador «Ver anexo en las páginas
NNN-NNN del documento / Descargar». Es el mismo problema que tenía Primaria y que resolvió
`TAREA-077`.

Se detectó al ejecutar `TAREA-079`, que tuvo que transcribir los enunciados leyendo directamente
el PDF oficial página a página. Eso funcionó para las once competencias, pero deja sin base local
la transcripción de `criterios_evaluacion` y `saberes_basicos`, que sigue pendiente.

## Qué hacer

Lo mismo que `TAREA-077`, que sirve de guion probado:

1. Descargar `https://sede.gobiernodecanarias.org/boc/boc-a-2022-212-3215.pdf`.
2. Extraer con `pdftotext -layout`, que es lo que preserva la disposición en dos columnas del
   bloque competencial: enunciado a la izquierda y códigos de descriptor a la derecha.
3. Comprobar que el resultado contiene «Competencia específica» y los enunciados. Ojo: en
   Infantil **no hay códigos de descriptor** (`DEC-0009`), así que ese contador no sirve como
   prueba; usa el número de competencias.
4. Sustituir la copia local conservando la cabecera R16 y actualizando URL y fechas.
5. Registrar la nueva procedencia en `06_indices/textos-oficiales.yaml`.
6. Validar con `python3 11_calidad/validar_corpus.py`.

## Después

Desbloquea el cierre de `TAREA-079`: con la copia local completa se pueden transcribir
literalmente los criterios de evaluación y los saberes básicos de las tres fichas de Infantil.

## Comprobación general pendiente

Dos de tres decretos curriculares tenían el anexo ausente en su copia local. Conviene revisar los
97 ficheros de `07_corpus_ia/textos-completos/` en busca del mismo marcador «Ver anexo en las
páginas», que indica una copia incompleta aunque esté bien codificada.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-081`. Solo se modifica una copia local de texto y su entrada de índice.

## Resultado (2026-08-05)

Re-exportado desde el PDF oficial de 102 páginas con `pdftotext -layout`. El texto pasa de **405
a 4.084 líneas** y aparecen las 36 competencias específicas con sus enunciados y criterios; los
seis marcadores «Ver anexo en las páginas…» desaparecen. Retiradas las cabeceras y pies repetidos
sin tocar el contenido normativo.
