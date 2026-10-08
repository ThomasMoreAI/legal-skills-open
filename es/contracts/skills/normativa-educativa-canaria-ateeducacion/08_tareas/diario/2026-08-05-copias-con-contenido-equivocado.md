# Diario — 2026-08-05: trece copias locales contienen otra norma

## El hallazgo

Se lanzó una rama de diagnóstico para buscar más copias locales con el anexo ausente, el problema
que ya habían tenido Primaria e Infantil. Encontró algo peor: **trece copias no contienen la
norma que declaran**. Su cabecera R16 es correcta —título y URL— pero el cuerpo es otra
disposición por completo.

La más grave es `NOR-044`, la Orden de evaluación y promoción, que es **la norma más citada del
corpus**: su copia local contiene una resolución del Hospital Ntra. Sra. de Candelaria sobre
carrera profesional del personal sanitario. Verificado de forma independiente: el fichero
menciona «carrera profesional» 28 veces y «Candelaria» 7.

Otras: el ROC de los CIFP contiene el Plan Insular de Ordenación de La Gomera; los comedores
escolares, la Ley de la Agencia Canaria de Desarrollo Sostenible; la Ley de Función Pública
Canaria, una resolución de 1987 de la Diputación Provincial de Almería que ni siquiera es de
Canarias.

El patrón apunta a que la exportación original tomó el ítem equivocado del sumario del boletín.
Nada lo detectaba: los ficheros están bien codificados, tienen cabecera y su tamaño es plausible.

## Verificación cruzada

El diagnóstico venía de un agente, así que lo comprobé por otra vía: una comprobación que
contrasta las palabras significativas del título declarado contra el cuerpo del fichero. Marca
doce ficheros, once de ellos coincidentes con la lista del agente. Dos métodos independientes,
prácticamente el mismo resultado.

El único que solo detectaba mi método, `CUR-043`, resultó falso positivo: su cabecera abreviaba
«CCSS» donde el cuerpo escribe «Ciencias Sociales». Corregida la cabecera con el nombre completo.

## Qué se ha hecho

Las trece copias llevan ahora una línea `ADVERTENCIA DE CONTENIDO` en su cabecera que dice qué
contienen realmente y que no deben usarse para cita ni búsqueda.

El validador incorpora el tipo `CORRESPONDENCIA` con un matiz deliberado: **si la copia lleva la
marca, avisa; si no la lleva, es error**. Así la deuda conocida no bloquea el trabajo, pero una
contaminación nueva sí lo haría. Comprobado retirando la marca de `NOR-044`: pasa a error.

La re-exportación de las trece queda en `TAREA-084`, con prioridad crítica y `NOR-044` primero.

## Una advertencia sobre mi propio trabajo de hoy

Al fusionar `NOR-044` y `NOR-048` usé como una de las dos señales que sus copias locales eran
idénticas byte a byte. Lo eran, pero **ambas estaban contaminadas**: comparé dos ficheros
erróneos. La fusión sigue siendo correcta por las otras evidencias —misma fecha de disposición y
misma fuente, y el título de `NOR-048` declaraba ser un aspecto de la orden— pero esa señal valía
menos de lo que pensé. Conviene tenerlo presente: la comprobación de desdoblamientos por
contenido idéntico puede dar falsos positivos mientras haya copias contaminadas.

## El resto de la tanda

- **Infantil cerrado.** Re-exportado su anexo, el texto pasa de 405 a 4.084 líneas. Al verificar
  contra él aparecieron errores de la transcripción manual previa: una competencia con una frase
  del criterio mezclada, otra truncada, y un área que tiene cinco competencias y no cuatro. Las
  tres fichas quedan completas.
- **Religión.** Localizada la fuente real —Resolución de 21 de junio de 2022, BOE-A-2022-10452—
  y catalogada como `FTE-079` y `NOR-072`. Pero el contenido que `CUR-033` ya tenía **no coincide
  con ella**: seis competencias que son paráfrasis, cuatro bloques de saberes frente a tres
  reales, dos criterios por ciclo frente a doce. No se ha corregido: es decisión editorial si se
  re-extrae o si ese contenido viene de otra fuente sin identificar.

El corpus queda en **57 fichas curriculares completadas y 1 parcial**, que es `CUR-033`.

## IDs consumidos

`FTE-079`, `NOR-072`, `TAREA-084`.
