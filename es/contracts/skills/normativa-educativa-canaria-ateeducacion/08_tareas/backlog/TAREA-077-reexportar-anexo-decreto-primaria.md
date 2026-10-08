---
id: TAREA-077
titulo: "Re-exportar el anexo curricular del Decreto 211/2022 de Primaria desde el PDF oficial"
estado: "Hecha"
prioridad: "Alta"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [NOR-043, FTE-046, TAREA-067, TAREA-076]
siguiente_accion: "Descargar el PDF oficial del Decreto 211/2022 y extraer el anexo curricular a texto plano."
---

# TAREA-077 — Re-exportar el anexo curricular de Primaria

## Problema

`07_corpus_ia/textos-completos/texto-oficial-NOR-043-decreto-211-2022-primaria.txt` **no contiene
el currículo**. Los bloques competenciales se publican en el BOC como anexo en PDF o imagen, y la
conversión desde el HTML los sustituyó por un marcador. Comprobación: cero apariciones de códigos
de descriptor (`CCL1`, `STEM4`…) en todo el fichero.

Eso deja `TAREA-067` sin materia prima: las 10 fichas curriculares de Primaria no se pueden
completar sin una copia utilizable.

## Qué hacer

1. Localizar el PDF oficial del Decreto 211/2022 en el BOC (`FTE-046`,
   `https://www.gobiernodecanarias.org/boc/2022/231/001.html`) y su anexo curricular.
2. Extraer el texto con `pdftotext` conservando la codificación, y comprobar que aparecen los
   enunciados de competencias y los códigos de descriptor.
3. Sustituir o complementar la copia local, manteniendo la cabecera con URL oficial, fecha de
   consulta, fecha de exportación y la advertencia de R16.
4. Registrar el cambio en `06_indices/textos-oficiales.yaml`.
5. Ejecutar `python3 11_calidad/validar_corpus.py` para confirmar que no hay doble encodeo.

## Comprobar de paso

Si el decreto de Primaria tenía este problema, conviene revisar si otras copias locales sufren lo
mismo: un fichero puede estar bien codificado y aun así no contener el anexo. Una comprobación
posible es contar códigos de descriptor en los textos de decretos curriculares y avisar si son
cero.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-077`. No se modifican fichas del corpus, solo copias locales de texto.

## Resultado (2026-08-05)

El PDF oficial del BOC (`boc-a-2022-231-3533.pdf`, 346 páginas) sí contiene los anexos
curriculares. Re-exportado con `pdftotext -layout`, la copia local pasa de **cero a 2.938
códigos de descriptor**. Se retiraron las cabeceras y pies repetidos de cada página sin alterar
el contenido normativo, y la cabecera R16 se actualizó con la URL del PDF y las fechas.

`06_indices/textos-oficiales.yaml` recoge la nueva procedencia.
