---
id: DEC-0010
titulo: "Una ficha normativa por norma: la etapa no desdobla fichas"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [PREG-009, NOR-044, NOR-046, FTE-049, FTE-051, TAREA-083]
---

# DEC-0010 — Una ficha normativa por norma

## Contexto

El corpus contenía dos casos de una misma norma descrita por **dos fichas `NOR` distintas**,
desdobladas por etapa:

| Norma | Fichas | Copias locales |
| --- | --- | --- |
| Resolución conjunta 73/2025 (instrucciones de organización y funcionamiento 25-26) | `NOR-046` «IOF Primaria» y `NOR-049` «IOF Infantil» | idénticas byte a byte |
| Orden de 31 de mayo de 2023 (evaluación y promoción) | `NOR-044` «Evaluación y Promoción» y `NOR-048` «Evaluación Infantil» | idénticas byte a byte |

El desdoblamiento no es inocuo. Produjo cuatro problemas concretos, todos detectados al
investigar `PREG-009`:

1. **Una fuente inventada.** `NOR-049` apuntaba a `FTE-051`, una ficha que describía una
   «Resolución de 20 de junio de 2025, IOF Escuelas Infantiles» **que no existe**. La norma real
   era la 73/2025, ya catalogada como `FTE-049`, a la que sí apuntaba `NOR-046`.
2. **Metadatos divergentes.** `NOR-048` declaraba `tipo_norma: resolucion-administrativa` y una
   autoridad distinta de la real, cuando la norma es una orden autonómica de la Consejería. Su
   propio título lo delataba: «Evaluación en Educación Infantil (**según** Orden de 31 de mayo de
   2023)».
3. **Alcance mal declarado.** `NOR-046` decía dirigirse a «los centros que imparten Educación
   Primaria» y `etapas_afectadas: [primaria]`, cuando la resolución se dirige a **todos** los
   centros públicos no universitarios: su articulado menciona Formación Profesional 63 veces,
   Infantil 32, Primaria 26, Secundaria 25, Bachillerato 14 y personas adultas 9.
4. **Copias locales duplicadas**, con el consiguiente coste y el riesgo de que una se actualice y
   la otra no.

## Decisión

**Una norma, una ficha `NOR`.** La identidad de la ficha es la norma, no la etapa a la que se
aplica.

La dimensión de etapa se expresa en `etapas_afectadas`, que ya existe y es filtrable, y en el
cuerpo de la ficha mediante apartados por etapa cuando el análisis lo requiera. Así lo hacen
ahora `NOR-046` —apartado 4 para Infantil— y `NOR-044` —apartado 3 para Infantil—.

Corolarios:

- Dos fichas no pueden compartir `fecha_disposicion` y `fuente_principal` describiendo el mismo
  documento. Si ocurre, una de las dos sobra.
- Una copia local de texto por norma. Dos ficheros con el mismo contenido señalan un
  desdoblamiento.
- Al fusionar, **se conserva el análisis específico** de la ficha retirada como apartado de la
  superviviente: el desdoblamiento es un error de modelado, no de contenido.
- El identificador de la ficha retirada **no se reutiliza** (R10) y la fusión se documenta en la
  superviviente.

## Consecuencias

- `NOR-049` fusionada en `NOR-046` y `NOR-048` en `NOR-044`. Ambos identificadores quedan
  retirados. Las fichas que los citaban se reapuntaron a las supervivientes.
- Los ficheros y sus copias locales pierden el nombre de etapa: `NOR-046-resolucion-iof-25-26.md`
  y `NOR-044-orden-evaluacion-31-mayo-2023.md`.
- `FTE-051`, que solo existía para dar fuente a `NOR-049`, queda marcada como catalogación
  errónea, sin referencias vivas.
- El validador incorpora una comprobación que detecta el patrón antes de que se consolide
  (`TAREA-083`).

## Alternativa descartada

**Mantener el desdoblamiento por comodidad de consulta.** Una persona que busque «evaluación en
Infantil» encuentra antes una ficha titulada así que un apartado dentro de una ficha general. Es
una ventaja real, pero se paga con duplicación de contenido, metadatos que divergen y fuentes que
se inventan para justificar la segunda ficha —que es exactamente lo que pasó—. La navegación por
etapa se resuelve con `etapas_afectadas` y con el índice, no duplicando entidades.

## Revisión futura

Si el portal público llega a necesitar vistas por etapa, se generan desde `etapas_afectadas` en
el momento de publicar, no duplicando fichas en el corpus.
