---
id: PREG-013
titulo: "El BOC no publica permalink ELI en las disposiciones autonómicas consultadas"
estado: "Resuelta"
fecha_registro: 2026-08-22
relacionadas: [NOR-005, NOR-043, NOR-047, TAREA-087]
---

# PREG-013 — El BOC no publica permalink ELI

## Contexto

El BOE muestra un «Permalink ELI» en las fichas consolidadas y en muchos documentos originales.
Esa es la evidencia usada para rellenar `uri_eli` en las normas estatales y en las leyes
canarias republicadas en el BOE.

Las disposiciones autonómicas cuya fuente principal es el BOC no muestran ese permalink. La
consulta de 2026-08-22 a `https://www.gobiernodecanarias.org/boc/2023/058/001.html` (Decreto
30/2023, `NOR-005`) no contiene ninguna URI `eli`.

## Qué falta confirmar

Si el Boletín Oficial de Canarias, Juriscan o el Gobierno de Canarias publican identificadores
ELI para decretos, órdenes y resoluciones autonómicas, y dónde constan de forma oficial.

## Fuente o evidencia necesaria

Confirmación en una página oficial del BOC, de Juriscan o del registro ELI español
(`elidata.es`) que identifique de forma expresa la URI de una disposición autonómica canaria
no republicada en el BOE.

## Respuesta (2026-08-23)

**El Gobierno de Canarias no tiene implantado un dominio ELI propio**, y el BOC ni Juriscan
publican permalinks ELI. Evidencia consultada:

1. **Registro nacional** (`elidata.es`): la jurisdicción `es-cn` (Comunidad Autónoma de Canarias)
   está registrada en el MDR (`https://www.elidata.es/mdr/authority/jurisdiction/1/`), pero en el
   directorio «Acceda a legislación» Canarias **no aparece con proyecto ELI propio**, al
   contrario que las CCAA adheridas.
2. **Patrones probados sin éxito**: `gobiernodecanarias.org/eli/...` y `sede.gobiernodecanarias.org/eli/`
   devuelven 404; la página BOC del Decreto 30/2023 solo incluye metadatos Dublin Core, sin ELI;
   la ficha Juriscan ofrece únicamente su identificador interno `ficha.jsp?id=NNNNN`.
3. **Cobertura parcial vía BOE**: la base «Todo el Derecho» del BOE asigna URIs
   `https://www.boe.es/eli/es-cn/{tipo}/{aaaa}/{mm}/{dd}/{número}` a parte de la normativa
   canaria (p. ej., la Ley 6/2014: `https://www.boe.es/eli/es-cn/l/2014/07/25/6`, que ya usa
   `NOR-004`). Cobertura muy incompleta: para decretos de 2023 solo figura abril, y las órdenes
   no aparecen como categoría. El Decreto 30/2023 (`NOR-005`) **no tiene URI ELI en boe.es**.

## Consecuencia práctica para el corpus

- Para normas canarias publicadas en el BOC, los identificadores trazables son la URL canónica
  del BOC y, cuando exista, la ficha JurisCan; no debe construirse ninguna URI
  `gobiernodecanarias.org/eli/...`.
- Las URIs `boe.es/eli/es-cn/...` se añaden caso por caso solo con verificación individual de su
  existencia real (como ya se hace en `NOR-004`).
- Si Canarias implanta ELI en el futuro, revisar este campo en todo el corpus autonómico.
