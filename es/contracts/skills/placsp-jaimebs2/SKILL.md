---
name: placsp-jaimebs2
title: PLACSP — Datos de contratación pública vía datos.gob.es
description: 'Use when the user asks specifically about Spanish public sector contracting — contracts awarded by the State (contratación pública), tenders (licitaciones), major contracts (contratos mayores) by year, minor contracts (contratos menores), awards (adjudicaciones), or any dataset of the Plataforma de Contratación del Sector Público (PLACSP). PLACSP does not expose a queryable REST catalog at contrataciondelestado.es; instead, discover and download its datasets through the national open data catalog datos.gob.es. Triggers on: ''PLACSP'', ''plataforma contratación'', ''plataforma de contratación del sector público'', ''licitaciones'', ''contratos Estado'', ''contratos sector público'', ''contratos mayores'', ''contratos menores'', ''adjudicaciones'', ''anuncios licitación'', ''contratación pública''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/placsp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# PLACSP — Datos de contratación pública vía datos.gob.es

La **Plataforma de Contratación del Sector Público** (`contrataciondelestado.es`)
es el canal oficial donde se publican los contratos del Estado y otros
organismos públicos españoles. **No expone una API REST pública con catálogo
consultable**: los volcados oficiales son ficheros ATOM mensuales muy
pesados, poco prácticos para consultas puntuales.

En su lugar, los datasets de PLACSP están indexados en el catálogo nacional
`datos.gob.es`, que sí ofrece una API abierta bien documentada y permite
filtrar por título.

Esta skill sigue siempre el mismo patrón:

1. Buscar por título en `datos.gob.es` con la ruta `/title/{texto}`.
2. Revisar los `items[].distribution[]` devueltos.
3. Elegir la distribución con formato útil (CSV > JSON > XLSX > ATOM).
4. Descargar con `WebFetch` la `accessURL` real.

**Nunca** inventar URLs de `contrataciondelestado.es` ni scrapear el portal
web. Solo usar `accessURL` extraídas de la respuesta del catálogo.

## Solapamiento con `transparencia`

La skill `transparencia` también descubre datasets de PLACSP (entre otros
ámbitos). La diferencia:

- **`placsp`** (esta skill) → uso específico para contratación pública del
  Estado: contratos mayores, contratos menores, licitaciones, adjudicaciones.
- **`transparencia`** → uso genérico para el Portal de Transparencia:
  además de PLACSP cubre subvenciones, altos cargos, retribuciones, agendas
  institucionales, registro de transparencia.

Si la pregunta es **exclusivamente** sobre contratos públicos, esta skill
es más directa. Si mezcla contratación con subvenciones u otros datos de
transparencia, usar `transparencia`.

## Base URL

```
https://datos.gob.es/apidata/catalog/dataset
```

Siempre añadir `?_format=json`. WebFetch con GET y header
`Accept: application/json`.

> ⚠️ El parámetro `?q={texto}` **NO** funciona — devuelve 400. Hay que usar
> la ruta `/title/{texto}`.

## Operaciones

### 1. PLACSP global (búsqueda canónica)

```
GET https://datos.gob.es/apidata/catalog/dataset/title/PLACSP?_pageSize=10&_format=json
```

Es la búsqueda más directa: muchos publishers etiquetan sus datasets con la
abreviatura `PLACSP` en el título. Devuelve nombres como:

- *Contratos Mayores. 2024 - (PLACSP)*
- *Contratos Mayores. 2025 - (PLACSP)*

Usar esta consulta primero cuando el usuario menciona explícitamente
"PLACSP" o "Plataforma de Contratación del Sector Público".

### 2. Contratos mayores por año

```
GET https://datos.gob.es/apidata/catalog/dataset/title/contratos%20mayores?_pageSize=10&_format=json
```

`contratos mayores` debe ir URL-encoded (`contratos%20mayores`). Devuelve
datasets como:

- *Contratos Mayores. 2024 - (PLACSP)*
- *Contratos Mayores. 2025 - (PLACSP)*
- *UCM-Licitaciones de Contratos Mayores*
- *Estadística del número de contratos mayores por tipo y ejercicio*

> Si el usuario pide un año concreto, filtrar `items[]` por título que
> contenga ese año (`2023`, `2024`, …). Si no encuentra el año exacto,
> avisar y ofrecer el ejercicio disponible más próximo.

### 3. Contratos menores

```
GET https://datos.gob.es/apidata/catalog/dataset/title/contratos%20menores?_pageSize=10&_format=json
```

Devuelve datasets como:

- *Contratos Menores* (varios publishers)
- *Relación de contratos menores por trimestre*
- *Contratos menores adjudicados*

> Los contratos menores los publican muchas administraciones locales y
> autonómicas (ayuntamientos, universidades, diputaciones) como volcados
> propios. Indicar siempre el `publisher` para que el usuario entienda el
> alcance territorial.

### 4. Licitaciones activas, anuncios y adjudicaciones

```
GET https://datos.gob.es/apidata/catalog/dataset/title/licitaciones?_pageSize=10&_format=json
```

Devuelve datasets como:

- *Licitaciones Publicadas 2021 / 2022 / …*
- *Anuncios licitaciones*
- *Adjudicaciones licitaciones*
- *Licitaciones de los organismos públicos del proyecto NextProcurement*

Si el usuario pide específicamente *adjudicaciones*, también probar:

```
GET https://datos.gob.es/apidata/catalog/dataset/title/adjudicaciones?_pageSize=10&_format=json
```

## Estructura de respuesta

```
result.items[]
  .title                       → string o lista de { _value, _lang }
  .identifier                  → identificador interno
  .publisher                   → URL del publisher (DIR3)
  ._about                      → URL canónica del dataset en datos.gob.es
  .distribution[]              → array (o objeto) de distribuciones
    .accessURL                 → URL real de descarga (CSV, JSON, XLSX, ATOM)
    .format._value             → "text/csv", "application/json", "application/atom+xml", ...
    .byteSize                  → tamaño aproximado en bytes
    .title                     → nombre legible de la distribución
```

> `distribution` puede venir como objeto (1 sola) o como array. Tratar
> siempre como lista.
> `title` puede venir como string, objeto `{_value, _lang}` o lista de
> objetos. Si es lista, preferir `_lang == "es"`.

## Workflow recomendado

```
1. GET /title/{termino}?_pageSize=10&_format=json
2. Filtrar result.items[] por títulos realmente relacionados con
   contratación pública (descartar agendas, subvenciones, etc.)
3. Para cada candidato, iterar distribution[]
4. Elegir formato más útil (CSV > JSON > XLSX > ATOM > PDF)
5. WebFetch a esa accessURL para descargar los datos
6. Si el fichero es muy grande (byteSize > ~5 MB), avisar antes al usuario
   — los volcados ATOM mensuales de PLACSP pueden superar 100 MB
7. Indicar siempre al usuario el publisher del dataset (Estado, CCAA,
   ayuntamiento, universidad) para que entienda el alcance
```

## Errores comunes

- **400 Bad Request**: estás usando `?q=` en vez de `/title/`.
- **0 items**: el término es demasiado específico — probar sinónimos
  (`contratos mayores` → `PLACSP`, `licitaciones` → `anuncios`,
  `adjudicaciones` → `adjudicación`).
- **HTML en vez de JSON**: olvidaste `?_format=json`.
- **Volcado ATOM gigantesco**: los ficheros mensuales de PLACSP completos
  son enormes. Si el usuario solo quiere consultar un puñado de contratos,
  preferir un dataset CSV/JSON anual ya recortado.
- **Confundir ámbito estatal con autonómico/local**: muchos datasets de
  contratación los publica una CCAA, ayuntamiento o universidad concreta.
  Leer siempre el `publisher` antes de generalizar a "España".

## Cuándo NO usar esta skill

- Si el usuario pregunta también por **subvenciones**, **altos cargos** o
  **agendas** → **transparencia** (cubre PLACSP además de eso).
- Si pregunta por la **ley de contratos del sector público** o una norma
  concreta (Ley 9/2017) → **boe**.
- Si pregunta por **paro registrado** o "contratos laborales" del SEPE →
  **sepe** (ojo: "contratos registrados" del SEPE ≠ "contratos del sector
  público" de PLACSP).
- Si necesita presentar una **oferta real** a una licitación → no es
  posible desde esta skill: redirigir a `https://contrataciondelestado.es`.
- Si pregunta por un dataset genérico no relacionado con contratación →
  **datos-gob-es**.
