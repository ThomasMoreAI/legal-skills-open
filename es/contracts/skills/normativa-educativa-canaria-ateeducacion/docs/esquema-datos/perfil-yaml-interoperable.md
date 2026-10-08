# Perfil YAML interoperable

## Propósito

Este perfil conserva Markdown/YAML como formato editorial y define qué subconjunto se puede transformar de forma determinista a JSON y JSON-LD. No crea un dialecto propio: aplica [YAML 1.2.2](https://yaml.org/spec/1.2.2/) y [JSON Schema 2020-12](https://json-schema.org/draft/2020-12), con esquemas públicos y validación automática.

## Reglas del perfil

| Aspecto | Regla | Motivo |
|---|---|---|
| Modelo de datos | Mapas con claves de texto, listas, cadenas, números, booleanos y `null`. | Coincide con el modelo de datos de JSON. |
| Fechas | Fecha civil ISO 8601 completa: `AAAA-MM-DD`. | Evita fechas parciales o interpretaciones dependientes del parser. |
| URI | URI absoluta en los campos declarados con `format: uri`. | Permite validar enlaces e identificadores antes de exportarlos. |
| Etiquetas YAML | No se admiten etiquetas personalizadas en el contenido canónico. | No tienen una conversión JSON portable. |
| Alias y anclas | Se pueden usar al editar; la salida generada contiene sus valores ya resueltos. | Conserva la ergonomía editorial sin trasladar semántica específica de YAML. |
| Claves duplicadas | No se admiten. | El resultado depende del parser y puede ocultar datos. |
| Orden | No transmite significado. | JSON-LD y los consumidores no deben depender del orden de claves. |
| Codificación | UTF-8. | Evita pérdidas y diferencias entre plataformas. |

## Contrato de validación

Cada familia documental tiene un esquema con `$id` público bajo `schemas/`. El validador aplica el vocabulario de JSON Schema 2020-12 y comprueba también los formatos `date` y `uri`.

Los cambios se clasifican así:

- Añadir una propiedad opcional es compatible hacia atrás.
- Añadir una propiedad a `required`, retirar un valor permitido o estrechar un patrón es potencialmente incompatible y exige migrar los datos en el mismo cambio.
- Una exportación generada nunca se edita manualmente: se regenera desde el YAML canónico y CI comprueba que esté actualizada.

## Capas publicadas

| Recurso | Estándar | Función |
|---|---|---|
| `datos/catalogo.jsonld` | Schema.org `Dataset` en JSON-LD | Descubrimiento del conjunto de datos y sus distribuciones. |
| `datos/legislacion.jsonld` | Schema.org `Legislation` en JSON-LD | Metadatos semánticos de las fichas normativas. |
| `datos/curriculos.jsonld` | Schema.org `LearningResource`/`Course` en JSON-LD | Metadatos semánticos de las fichas curriculares. |
| `datos/fuentes.jsonld` | Schema.org `WebPage` en JSON-LD | Metadatos semánticos de las fuentes oficiales. |
| `uri_eli` | ELI | Identificación jurídica oficial, solo cuando el publicador la confirma. |
| `datos/akoma-ntoso/` | OASIS LegalDocML Akoma Ntoso 1.0 | Pilotos de estructura del texto legal, separados del formato editorial. |

No se adopta YAML-LD como representación canónica. [YAML-LD](https://www.w3.org/community/reports/json-ld/CG-FINAL-yaml-ld-20231206/) permite expresar datos enlazados en YAML, pero es un informe final de un grupo comunitario, no una Recomendación del W3C. JSON-LD ofrece un ecosistema más consolidado para publicación semántica y es el formato recomendado por Google para los datos estructurados que admite.

## Mantenimiento

Después de cambiar una ficha normativa o esta capa de correspondencia:

```bash
python3 11_calidad/generar_interoperabilidad.py --write
python3 11_calidad/validar_corpus.py
python3 11_calidad/generar_interoperabilidad.py --check
```

La presencia de una URI con apariencia ELI no basta para añadir `uri_eli`: debe constar en la fuente oficial. Los identificadores internos `NOR-NNN` se mantienen para trazabilidad y no se presentan como identificadores jurídicos oficiales.
