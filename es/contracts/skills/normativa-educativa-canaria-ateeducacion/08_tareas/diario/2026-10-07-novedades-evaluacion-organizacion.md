# Revisión de novedades — 2026-10-07

## Alcance y evidencias

Consulta y análisis realizados el 7 de octubre de 2026. Se contrastó el PDF de instrucciones aportado por el usuario con el corpus, el listado oficial de normativa 2026 y las páginas oficiales de organización de centros y rúbricas de Infantil y ESO. Esta revisión se concentra en evaluación, organización general y CER; no certifica una revisión exhaustiva del BOE o de todas las convocatorias y actos individuales publicados desde agosto.

- `NOR-125` / `FTE-132`: instrucciones de evaluación y calificación firmadas el 6 de octubre; aplicación desde 2026-2027.
- `NOR-126` / `FTE-133`: rúbricas de Infantil y PDC, firma 2 de octubre, registro 5 de octubre. Copia local con resolución y ambos anexos. Publicación BOC pendiente en el portal; `PREG-014` sigue la vigencia formal.
- `NOR-127` / `FTE-134`: instrucciones generales de organización 73/2026, firma 27 de mayo, registro 28 de mayo; faltaban en el corpus.
- `NOR-128` / `FTE-135`: modificación 95/2026 de horas de innovación FP; registro 16 de julio.
- `NOR-129` / `FTE-136`: modificación 110/2026, de 28 de septiembre, sobre recogida excepcional de menores por hermanos menores.
- `NOR-130` / `FTE-137`: configuración CER, Orden de 6 de agosto, BOC 166 de 19 de agosto.
- `NOR-131` / `FTE-138`: modificación CER, Orden de 25 de septiembre, BOC 201 de 7 de octubre; mantiene al CEIP San Vicente en el CER Santa Cruz de La Palma.

Se registran `REL-092` a `REL-103`. `NOR-046` se conserva como histórica por referirse a 2025-2026; no se afirma derogación expresa. La relación con la nueva referencia anual se marca inferida.

## Otras publicaciones observadas

El listado oficial de normativa 2026 muestra también convenios municipales de escolarización temprana, llamamientos de interinos, declaraciones de interés educativo y convocatorias de proyectos como SUMA, CanSat y Tenencia responsable de mascotas. No se catalogan como regulación general de evaluación u organización en esta tarea. Sus textos completos no han sido analizados aquí.

## Limitación del monitor

`scan_normativa.py --dry-run` informa de 80 candidatas y 0 nuevas, aunque las páginas temáticas y el listado de 2026 contienen los documentos incorporados. Ese resultado no acredita ausencia de novedades: el monitor solo lee enlaces de las páginas configuradas, sin recorrer todas las páginas temáticas ni la paginación del listado anual. No se modifica el snapshot ni se descartan documentos para silenciarlos.

## Cierre

`TAREA-098`: fuentes y relaciones trazables, copias locales con aviso y fechas, inventario y exportaciones regenerados. El resumen no sustituye la fuente oficial. La publicación BOC de las rúbricas queda abierta en `PREG-014`.

## Comprobaciones de cierre

- Validador del corpus: 0 errores y 0 avisos.
- Inventario público y exportaciones interoperables: comprobaciones `--check` correctas.
- 61 XML conformes al XSD Akoma Ntoso 3.0.
- Hashes, fechas y advertencias comprobados en las siete copias nuevas; ambos anexos de rúbricas completos.
- Portada local comprobada en Chrome a 1280 y 320 px: sin desbordamiento horizontal ni errores de consola. El único cambio en HTML generado es la cobertura temporal del JSON-LD.
