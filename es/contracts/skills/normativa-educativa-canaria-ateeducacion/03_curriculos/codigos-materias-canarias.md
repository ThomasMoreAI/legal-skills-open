---
id: COD-MAT-CANARIAS-001
titulo: "Codigos administrativos de areas y materias por etapa y nivel"
fuente_principal: FTE-056
fecha_consulta: 2026-04-26
fecha_analisis: 2026-04-26
estado: "documentado"
---

# Códigos administrativos de áreas y materias por etapa y nivel

> Este documento resume códigos administrativos extraídos del buscador oficial de enseñanzas del Gobierno de Canarias. No sustituye la consulta directa de la fuente oficial ni las denominaciones curriculares publicadas en BOC.

## Fuente y alcance

- **Fuente principal:** [FTE-056](../01_fuentes/portales-oficiales/FTE-056-buscador-ensenanzas-codigos-materias.md).
- **URL base:** <https://www.gobiernodecanarias.org/educacion/centroseducativos/buscador-ensenanzas/>
- **Fecha de consulta:** 2026-04-26.
- **Fichero estructurado:** [codigos-materias-canarias.yaml](codigos-materias-canarias.yaml).

El buscador publica fichas por `idEstudio`; dentro de cada ficha, las áreas, materias o módulos aparecen con un código entre corchetes. En esta versión se documentan Infantil, Primaria, Diversificación Curricular, ESO, Bachillerato y BACHIBAC LOMLOE. FP queda fuera de este documento porque se está revisando en paralelo.

## Aclaraciones rápidas

- `SGA` sale del buscador oficial y significa **Segunda Lengua Extranjera (Alemán)** en Primaria/ESO.
- `SGN` significa **Segunda Lengua Extranjera (Francés)** en Primaria/ESO.
- `MUS` significa **Música**.
- En ESO, **Biología y Geología** aparece como `BIG`, no como `BIO`.
- `BIO` aparece en Bachillerato para **Biología** de 2º BAC.
- `BIR` aparece en 1º BAC para **Biología, Geología y Ciencias ambientales**.
- `EUP` significa **Educación Plástica, Visual y Audiovisual**.

## Estudios consultados

| Etapa | idEstudio | Nivel |
| --- | ---: | --- |
| Infantil | 8424-8429 | Educación Infantil 1º a 6º LOMLOE |
| Primaria | 8430-8435 | Educación Primaria 1º a 6º LOMLOE |
| ESO | 8436-8437 | Diversificación Curricular 1º y 2º LOMLOE |
| ESO | 8438-8441 | Educación Secundaria Obligatoria 1º a 4º LOMLOE |
| Bachillerato | 8442-8455 | BAC y BACHIBAC por curso y modalidad LOMLOE |

## Lectura recomendada

Usar el YAML como catálogo de consulta por etapa y nivel. Para un análisis curricular, debe citarse además la norma curricular correspondiente (`FTE-009`, `FTE-046` o `FTE-050`) porque el buscador no sustituye al BOC.
