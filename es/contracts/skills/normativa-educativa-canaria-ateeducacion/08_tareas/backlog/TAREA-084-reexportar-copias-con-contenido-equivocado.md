---
id: TAREA-084
titulo: "Re-exportar las trece copias locales que contienen una norma distinta de la que declaran"
estado: "Hecha"
prioridad: "Crítica"
tipo: "corpus-ia"
responsable: "@.agents/skills/preparacion-corpus-ia"
fecha_creacion: 2026-08-05
fecha_actualizacion: 2026-08-05
fecha_cierre: 2026-08-05
relacionadas: [NOR-044, NOR-028, NOR-050, NOR-060, TAREA-074, TAREA-077, TAREA-081, TAREA-085, PREG-010, PREG-011, PREG-012]
siguiente_accion: null
---

# TAREA-084 — Copias locales con contenido equivocado

## Hallazgo

Al revisar los 96 textos locales buscando anexos ausentes apareció un problema **más grave que
el que se buscaba**: trece copias no contienen la norma que declaran. Su cabecera R16 es
correcta —título y URL— pero el cuerpo es **otra disposición por completo**.

El patrón apunta a que la exportación original tomó el ítem equivocado del sumario del boletín,
probablemente `001.html` en vez del anuncio concreto.

Nada lo detectaba: los ficheros están bien codificados, tienen su cabecera y su tamaño es
plausible. Quien los usara para citar o para RAG estaría citando otra norma.

## Los trece

| Ficha | Debería contener | Contiene realmente |
| --- | --- | --- |
| `NOR-044` | Orden 31-05-2023, evaluación y promoción | Resolución del Hospital Ntra. Sra. de Candelaria sobre carrera profesional sanitaria |
| `NOR-050` | Orden 29-05-2023, procedimientos NEAE | Orden de subvenciones por las erupciones volcánicas de La Palma |
| `NOR-012` | Decreto 112/2011, ROC de los CIFP | Decreto 97/2011, Plan Insular de Ordenación de La Gomera |
| `NOR-013` | Orden 22-05-2011, Inspección | Decreto 131/2011 sobre intensidades de protección de la dependencia |
| `NOR-011` | Decreto 52/2009, Reglamento de la Inspección | Corrección de errores del Decreto 35/2009 sobre la RPT de Economía |
| `NOR-017` | Orden 28-07-2014, escuelas infantiles | Resolución de subvenciones a Cofradías de Pescadores |
| `NOR-018` | Orden 1-09-2010, desarrollo del ROC en IES | Resolución de la Academia Canaria de Seguridad |
| `NOR-034` | Orden 24-04-2009, comedores escolares | Ley 3/2009 de la Agencia Canaria de Desarrollo Sostenible |
| `NOR-035` | Orden 2-08-2006, transporte escolar | Resolución de 1-08-2006 sobre período vacacional y permisos |
| `NOR-023` | Resolución 16-06-2020, permisos y licencias | Resolución de convalidación del Decreto ley 9/2020 (COVID-19) |
| `NOR-019` | Ley 2/1987, Función Pública Canaria | Resolución de 1987 de la Diputación Provincial de Almería |
| `NOR-060` | RD 1074/2012, Técnico Superior en Integración Social | Resolución de la Universidad Carlos III sobre un máster |
| `NOR-028` | Orden 10-02-2016, aulas enclave | Cáscara del BOC: faltan íntegros los anexos, que **son** la norma (116 páginas) |

**`NOR-044` es prioridad máxima**: es la norma de evaluación más citada del corpus.

## Mitigación aplicada

Las trece copias llevan ya una línea `ADVERTENCIA DE CONTENIDO` en su cabecera que dice qué
contienen realmente y que no deben usarse para cita ni búsqueda. El validador las reporta como
aviso mientras esa marca esté presente, y como **error** si falta: así una contaminación nueva no
pasaría inadvertida.

## Qué hacer

Para cada una, el procedimiento probado de `TAREA-077` y `TAREA-081`:

1. Localizar el PDF del anuncio concreto en el BOC o el BOE, **no** el sumario del día.
2. Extraer con `pdftotext -layout` y comprobar que el cuerpo corresponde al título.
3. Sustituir la copia conservando la cabecera R16, actualizando URL y fechas, y **retirando la
   línea de advertencia de contenido**.
4. Registrar la nueva procedencia en `06_indices/textos-oficiales.yaml`.
5. Validar: el fichero debe desaparecer de los avisos de `CORRESPONDENCIA`.

## Anexos accesorios ausentes

Seis copias más tienen ausente un anexo de carácter accesorio —formularios, modelos de acta— con
el articulado completo: `NOR-025`, `NOR-015`, `NOR-014`, `NOR-026`, `NOR-016` y `NOR-037`. No
comprometen la cita del articulado y quedan como trabajo de menor prioridad dentro de esta tarea.

## Coordinación con trabajo paralelo

IDs consumidos: `TAREA-084`. Solo se modifican copias locales de texto y su índice.

## Avance 2026-08-05 — causa localizada y ocho copias sustituidas

### La causa

La cabecera de estas copias apunta a una URL de la forma `/boc/AAAA/NNN/001.html`. Ese último
número **no es el número de la disposición**, sino su posición dentro del boletín. La exportación
original lo dejó casi siempre en `001`, de modo que se llevó la primera disposición del boletín
—cualquiera que fuese— en vez de la norma buscada. `NOR-044` es el ejemplo puro: pedía `002` y
la orden de evaluación estaba en `001`, así que se trajo la resolución del hospital que ocupaba
el segundo lugar.

En dos casos el número de boletín era además el equivocado (`NOR-023` estaba en el 132, no en el
131) y en uno el boletín declarado ni siquiera contiene disposiciones generales (`NOR-018`).

### La herramienta

Se añade `11_calidad/reexportar_texto_oficial.py`. En lugar de confiar en el ordinal, **localiza
la disposición por su título** dentro del sumario del boletín y extrae el texto del **PDF oficial
firmado**, no del HTML. Eso resuelve de paso el problema de los anexos publicados como imagen,
que la versión HTML omite.

Incorpora tres salvaguardas:

- Si el título no casa con ninguna disposición del boletín declarado, busca en el archivo del BOC
  a partir de la fecha que el propio título indica, localizando el boletín por búsqueda binaria
  sobre las fechas.
- Antes de escribir comprueba que el texto extraído habla de lo que dice el título. Esa
  comprobación evitó un falso positivo real en `NOR-017`, donde una resolución del mismo día
  sobre el Ayuntamiento de El Sauzal alcanzaba coincidencia suficiente por el juego de fechas.
- Al aplicar, sincroniza `06_indices/textos-oficiales.yaml` con la URL, el PDF, el hash y las
  fechas nuevas.

El sumario del BOC ha usado tres marcados distintos a lo largo de los años y el índice anual
otros tres; la herramienta los cubre todos, así que sirve para cualquier boletín desde 2006.

### Hecho

Ocho copias sustituidas desde su PDF firmado: `NOR-011`, `NOR-012`, `NOR-013`, `NOR-023`,
`NOR-028`, `NOR-034`, `NOR-035` y `NOR-044`. `NOR-044` pasa de 0 apariciones de «promoción» a 69.
`NOR-028`, cuyos anexos *son* la norma, pasa de cáscara a 6.734 líneas.

La corrección no se quedó en la copia local: la URL equivocada estaba también en el frontmatter
de las ocho fichas `NOR` y de cinco fichas `FTE`, y en dos índices. Todas apuntan ya a la
disposición correcta, y las ocho fichas `NOR` incorporan el bloque `texto_oficial` con el enlace
al PDF firmado.

**Corrección adicional en `FTE-026`:** declaraba el boletín 131 cuando la resolución salió en el
132 —la fecha de publicación que `NOR-023` ya registraba lo confirmaba—, y declaraba
`relacionadas: [NOR-018]`, una norma sin ninguna relación con los permisos del profesorado. El
fichero pasa a llamarse `FTE-026-boc-2020-132-permisos.md`.

### Queda

Cinco copias que la búsqueda automática no resuelve, y que necesitan localización manual:

| Ficha | Situación |
| --- | --- |
| `NOR-017` | No está en el boletín declarado ni en los 90 siguientes con ese título |
| `NOR-018` | El boletín declarado sólo contiene anuncios; la orden está en otro |
| `NOR-050` | No aparece en el boletín declarado |
| `NOR-019` | La URL del BOE es de otra norma: apunta a una resolución de la Diputación de Almería |
| `NOR-060` | La URL del BOE tampoco corresponde al RD 1074/2012 |

## Cierre (2026-08-05)

### Las trece

Diez sustituidas desde su fuente oficial. Las otras tres **no eran un problema de exportación**:
las normas que declaran no existen. Se escalan a `TAREA-085` con `PREG-010`, `PREG-011` y
`PREG-012`.

| Estado | Fichas |
| --- | --- |
| Re-exportadas desde el PDF firmado del BOC | `NOR-011`, `NOR-012`, `NOR-013`, `NOR-023`, `NOR-028`, `NOR-034`, `NOR-035`, `NOR-044` |
| Re-exportadas desde el BOE con el identificador corregido | `NOR-019`, `NOR-060` |
| Escaladas: la norma no se localiza | `NOR-017`, `NOR-018`, `NOR-050` |

Dos mecanismos distintos, que conviene no confundir:

- **En el BOC**, la URL terminaba en la posición de la disposición dentro del boletín, casi
  siempre dejada en `001`. Se llevaba la primera disposición del boletín, fuera cual fuese.
- **En el BOE**, el identificador `BOE-A-` era directamente otro. La copia contenía exactamente
  la disposición de ese identificador falso, así que el error estaba en la ficha, no en la
  exportación. La advertencia que pusimos el 2026-08-05 decía «la cabecera es correcta»: valía
  para las once del BOC, no para estas dos.

### Los anexos accesorios

Cinco de las seis copias con anexos ausentes quedan completas al extraerlas del PDF:

| Ficha | Antes | Después |
| --- | ---: | ---: |
| `NOR-025` (Orden NEAE 2010) | 750 | 1.729 |
| `NOR-026` (Resolución NEAE 2011) | 742 | 1.689 |
| `NOR-014` | 544 | 722 |
| `NOR-037` | 382 | 459 |
| `NOR-016` | 224 | 266 |

Que `NOR-025` y `NOR-026` se completen importa especialmente: con `NOR-050` en cuarentena, son el
marco procedimental NEAE que hay que dar por vigente.

**`NOR-015` no se puede completar.** El PDF del BOC 2000/148 son 19 páginas escaneadas sin capa
de texto: `pdftotext` no extrae nada. La copia sigue procediendo del HTML, que omite los anexos
publicados como imagen. Recuperarlos exigiría OCR, y un texto normativo transcrito por OCR
introduce errores que no compensan. Queda anotado en la cabecera de la propia copia.

### Herramienta

`11_calidad/reexportar_texto_oficial.py` cubre los tres marcados de sumario que el BOC ha usado
desde 2006, los dos esquemas de URL, la búsqueda por archivo cuando el boletín declarado es el
equivocado y la sincronización del índice. Su modo `--auditar` contrasta la `url_oficial` de cada
ficha `NOR` contra el sumario de su boletín: es lo que descubrió las tres normas inexistentes y
tres enlaces más que apuntaban a otra disposición (`NOR-042`, `NOR-045`, `NOR-023`).

Con eso, de las 40 fichas `NOR` con URL de disposición del BOC, **37 contrastan correctamente** y
las 3 restantes son las de `TAREA-085`.
