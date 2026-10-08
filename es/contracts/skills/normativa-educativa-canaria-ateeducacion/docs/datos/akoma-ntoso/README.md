# Pilotos Akoma Ntoso

Los XML de este directorio son exportaciones técnicas y reproducibles de artículos delimitados de normas educativas. Su finalidad es probar la estructura, los identificadores FRBR y, cuando existe, la trazabilidad ELI.

El catálogo revisado vive en `11_calidad/akoma_ntoso_pilotos.yaml`. El generador `11_calidad/generar_interoperabilidad.py` es la única vía de edición de estos XML.

## Alcance y garantías

- Cada fichero incluye un artículo concreto; no representa el texto completo ni una consolidación jurídica.
- El contenido se contrasta con la copia local de consulta o con la publicación oficial citada en el catálogo de pilotos.
- Se ha validado localmente contra el XSD oficial de [Akoma Ntoso 3.0 / OASIS LegalDocML 1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part2-specs/schemas/akomantoso30.xsd).
- No sustituyen al BOE ni al BOC, no son publicación oficial y no deben utilizarse como fuente jurídica autónoma.
- La URI ELI solo aparece como `FRBRalias` cuando la ficha normativa tiene `uri_eli` confirmada por el publicador.

## Cobertura actual

60 porciones publicadas (2026-08-22), generadas desde
`11_calidad/akoma_ntoso_pilotos.yaml`:

| Norma | Porciones publicadas | Publicador |
|---|---|---|
| RD 217/2022 (ESO) — `NOR-003` | artículos 1, 2 y 3; DA 2.ª y 4.ª; DF 1.ª a 4.ª | BOE |
| Ley 6/2014 de Canarias — `NOR-004` | artículos 1, 2 y 3 | BOC |
| Decreto 30/2023 de Canarias (ESO y Bachillerato) — `NOR-005` | artículos 1, 2 y 3 | BOC |
| RD 243/2022 (Bachillerato) — `NOR-006` | artículos 1, 2 y 3; DA 2.ª, 4.ª y 5.ª; DF 1.ª a 5.ª | BOE |
| LOFP 3/2022 — `NOR-007` | artículos 1 y 2 (las 24 definiciones) | BOE |
| Decreto 81/2010 ROC — `NOR-009` | artículos 1 y 2 del Reglamento Orgánico (anexo) | BOC |
| Decreto 25/2018 atención a la diversidad — `NOR-024` | artículos 1 y 2 | BOC |
| Decreto 211/2022 Primaria — `NOR-043` | artículos 1, 2 y 3 | BOC |
| Decreto 196/2022 Infantil — `NOR-047` | artículos 1, 2 y 3 | BOC |
| RD 157/2022 Primaria — `NOR-079` | artículos 1, 2 y 3 | BOE |
| RD 659/2023 FP — `NOR-080` | artículos 1, 2 y 3; DA 1.ª a 4.ª, 7.ª, 9.ª, 10.ª, 12.ª, 13.ª, 18.ª, 20.ª a 22.ª; DF 5.ª, 7.ª y 8.ª | BOE |

Quedan excluidas las disposiciones largas o que modifican íntegramente
otras normas (p. ej., DF 1.ª a 4.ª del RD 659/2023). Todos los XML se
validan contra el XSD oficial en CI
(`11_calidad/validar_akoma_ntoso.py`).
