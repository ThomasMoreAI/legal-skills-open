---
id: FTE-056
titulo: "Buscador de enseñanzas del Gobierno de Canarias"
tipo_fuente: "catalogo-administrativo"
autoridad: "Consejería de Educación, Formación Profesional, Actividad Física y Deportes - Gobierno de Canarias"
url_oficial: "https://www.gobiernodecanarias.org/educacion/centroseducativos/buscador-ensenanzas/"
fecha_consulta: 2026-04-26
fecha_analisis: 2026-04-26
estado_fuente: "Activa"
nivel_evidencia: "confirmado-fuente-primaria"
relacionadas: [FTE-009, FTE-046, FTE-050]
---

# FTE-056 — Buscador de enseñanzas del Gobierno de Canarias

> Esta ficha describe una fuente oficial o referencia institucional. No sustituye la consulta directa de la fuente.

## Identificación

- **Autoridad:** Consejería de Educación, Formación Profesional, Actividad Física y Deportes - Gobierno de Canarias.
- **URL oficial:** <https://www.gobiernodecanarias.org/educacion/centroseducativos/buscador-ensenanzas/>
- **Fecha de consulta:** 2026-04-26.
- **Tipo de fuente:** catálogo administrativo de enseñanzas, estudios y módulos/áreas/materias asociados.

## Qué contiene

El buscador permite consultar fichas oficiales por enseñanza y estudio (`idEstudio`). En las fichas de Infantil, Primaria, ESO, Diversificación Curricular y Bachillerato LOMLOE, el apartado de módulos/áreas/materias muestra un código interno entre corchetes junto a la denominación administrativa.

Ejemplos confirmados en la consulta de 2026-04-26:

- `idEstudio=8440`: 3º Educación Secundaria Obligatoria (LOMLOE), con códigos como `BIG` para Biología y Geología, `MUS` para Música, `SGN` para Segunda Lengua Extranjera (Francés), `SGA` para Segunda Lengua Extranjera (Alemán) y `EUP` para Educación Plástica, Visual y Audiovisual.
- `idEstudio=8448`: 2º BAC Modalidad de Ciencias y Tecnología (LOMLOE), con `BIO` para Biología, `GAO` para Geología y Ciencias Ambientales, `FIC` para Física y `QUI` para Química.

## Relevancia para el repositorio

Esta fuente se usa para documentar los códigos administrativos de áreas, materias y módulos que aparecen en la oferta de enseñanzas del Gobierno de Canarias. Estos códigos no sustituyen a las denominaciones oficiales de los currículos publicados en BOC, pero sirven para:

- desambiguar abreviaturas usadas en fichas y listados internos;
- distinguir códigos por etapa, curso y modalidad;
- evitar inferir códigos no confirmados por fuente oficial;
- detectar diferencias relevantes, por ejemplo `BIG` para Biología y Geología en ESO frente a `BIO` para Biología en 2º Bachillerato.

## Normas o currículos enlazados

- `FTE-009` — Decreto 30/2023, currículo de ESO y Bachillerato en Canarias.
- `FTE-046` — Decreto 211/2022, currículo de Educación Primaria en Canarias.
- `FTE-050` — Decreto 196/2022, currículo de Educación Infantil en Canarias.
- [03_curriculos/codigos-materias-canarias.md](../../03_curriculos/codigos-materias-canarias.md)
- [03_curriculos/codigos-materias-canarias.yaml](../../03_curriculos/codigos-materias-canarias.yaml)

## Observaciones

La fuente tiene naturaleza administrativa. Si una denominación curricular del BOC difiere de la denominación del buscador, debe prevalecer la norma curricular para análisis normativo y debe conservarse el código del buscador solo como metadato trazable.
