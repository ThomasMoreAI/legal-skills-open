# Interoperabilidad jurídica

## Decisión de arquitectura

El formato editorial canónico del corpus continúa siendo Markdown/YAML. Es legible, versionable y ya está validado mediante esquemas e índices. Los estándares externos se incorporarán como capas de exportación generadas, sin duplicar manualmente la información ni sustituir la fuente jurídica oficial.

## Estándares aplicables

### ELI

El [Identificador Europeo de Legislación (ELI)](https://eur-lex.europa.eu/eli-register/about.html) es la referencia prioritaria para identificar legislación y publicar metadatos interoperables. La [especificación técnica española](https://www.elidata.es/documentacion_tecnica/especificacion_tecnica.php) contempla su aplicación gradual a la legislación estatal, autonómica y local.

ELI encaja con las fichas `NOR-NNN` como capa de identificación y metadatos. El campo opcional `uri_eli` registra únicamente identificadores confirmados por el organismo publicador; el generador no intenta deducirlos a partir del título o de otras fechas. En la práctica, el BOE publica un permalink ELI en la ficha consolidada o en el documento original. El BOC no ofrece ese permalink en las páginas consultadas.

### Akoma Ntoso

[Akoma Ntoso 1.0](https://docs.oasis-open.org/legaldocml/akn-core/v1.0/akn-core-v1.0.html) es un estándar XML para documentos jurídicos y parlamentarios. Sería adecuado como formato de exportación cuando se necesite representar con precisión la estructura completa del texto normativo, sus bloques y referencias.

No se adopta como formato de edición principal mientras el corpus mantenga fichas de análisis y copias de consulta, en vez de una edición XML estructural completa de cada disposición. Los [pilotos publicados](../datos/akoma-ntoso/README.md) limitan deliberadamente la prueba al artículo 1 de un conjunto reducido de normas y se validan contra el XSD oficial.

### Schema.org y JSON-LD

El corpus publica un catálogo `Dataset`, un grafo `Legislation`, un grafo `LearningResource`/`Course` de currículos y un grafo `WebPage` de fuentes mediante [Schema.org](https://schema.org/) y JSON-LD. Esta capa mejora el descubrimiento y ofrece un contrato semántico reutilizable. No convierte las fichas en fuentes oficiales ni implica que Google ofrezca un resultado enriquecido específico para legislación.

### llms.txt

[llms.txt](https://llmstxt.org/) facilita a modelos de lenguaje un mapa Markdown breve del contenido público. Es una capa de descubrimiento, no un estándar jurídico ni una fuente de verdad. La copia de la raíz debe apuntar a documentos canónicos y mantener su inventario generado desde `06_indices/`.

## Correspondencia prevista

| Campo interno | Destino interoperable | Regla |
|---|---|---|
| Identificador `NOR-NNN` | Identificador interno | Se conserva para trazabilidad; no se presenta como cita jurídica. |
| Denominación oficial | Metadato ELI de título | Se exporta literalmente desde la ficha validada. |
| Fechas de disposición y publicación | Metadatos ELI temporales | Se exportan solo cuando constan en la fuente oficial. |
| Tipo de norma y ámbito | Tipo de recurso y jurisdicción ELI | Requiere una tabla de correspondencias explícita y versionada. |
| URL oficial | URI de referencia | Se conserva; solo se marca como URI ELI si el publicador la ofrece como tal. |
| Texto completo estructurado | Akoma Ntoso | Se genera únicamente desde una extracción estructural verificada. |

## Implantación

1. El esquema normativo admite una URI ELI oficial verificada y valida fechas y URI.
2. `11_calidad/generar_interoperabilidad.py` transforma las fichas en `datos/legislacion.jsonld`, `datos/curriculos.jsonld`, `datos/fuentes.jsonld` y `datos/catalogo.jsonld`.
3. El catálogo `Dataset` se inserta también en la página pública para facilitar su descubrimiento.
4. CI comprueba que las exportaciones coincidan con las fichas canónicas.
5. Akoma Ntoso permanece en fase piloto: solo se publican porciones revisadas listadas en `11_calidad/akoma_ntoso_pilotos.yaml` (hoy, artículos 1 a 3 del núcleo curricular y de la ordenación de FP, disposiciones breves de los reales decretos estatales y artículos 1 y 2 del ROC y del Decreto 25/2018). Cada XML se valida contra el XSD oficial en CI.

## Salvaguardas

- No inventar identificadores ELI ni inferir que una URL oficial cumple ELI por su apariencia.
- Mantener Markdown/YAML como única fuente editorial hasta que una migración tenga cobertura, validación y reversibilidad demostradas.
- Generar las capas interoperables automáticamente y comprobar en CI que no estén desactualizadas.
- Conservar siempre el enlace a BOE, BOC o al portal institucional como referencia jurídica verificable.
