# Diario — 2026-08-05: FTE-051 describía una resolución inexistente (PREG-009)

## Hecho

`TAREA-070` había establecido que la «Resolución de 20 de junio de 2025, IOF Escuelas
Infantiles» que declara `FTE-051` no aparece en ningún portal oficial. Faltaba decidir qué hacer,
y la decisión dependía de saber qué es realmente esa ficha.

**La prueba estaba dentro del corpus, no en el portal.** La copia local del texto de `NOR-049`
—la única ficha que referenciaba `FTE-051`— declara en su cabecera como URL de origen el PDF de
la Resolución 73/2025, su contenido lleva tres veces el sello «RESOLUCION - Nº: 73 / 2025», y su
cuerpo es **idéntico línea a línea** al de la copia de `NOR-046`, que ya apuntaba a `FTE-049`.

Dicho de otro modo: `NOR-046` y `NOR-049` son dos fichas de la misma resolución, desdobladas por
etapa, y una de ellas apuntaba a una fuente que nunca existió.

## Resuelto

- **`NOR-049` se reapunta a `FTE-049`** y se corrige su `url_oficial`, que estaba rota, al PDF
  oficial verificado.
- **`FTE-051` no se borra** (R9) ni se reutiliza su ID (R10). Pasa a `estado_fuente: "Superada"`,
  con `[CATALOGACIÓN ERRÓNEA]` al frente del título y la explicación completa en la ficha. Su
  `nivel_evidencia` pasa a `confirmado-fuente-primaria`, porque ahora sí hay evidencia primaria:
  la de que el documento no existe.
- Ya no queda ninguna referencia viva a `FTE-051`.

Se descartó reidentificarla como la Resolución 24/2024. Esa norma sí existe y el corpus no la
tiene, pero darle el ID de otra cosa haría que `FTE-051` significara algo distinto de lo que
significó. Se cataloga aparte en `TAREA-078`.

## Aparece una cuestión nueva

**Dos fichas normativas describen la misma resolución**, con contenido literal idéntico y dos
copias locales idénticas. Puede ser deliberado —la resolución tiene anexos por etapa y separarlas
facilita la consulta— o puede ser duplicación. Conviene decidirlo antes de que el patrón se
repita con las instrucciones de 2026-2027, que ya están publicadas. Queda anotado en `PREG-009`.

## IDs consumidos

`TAREA-078`. `PREG-009` queda resuelta.
