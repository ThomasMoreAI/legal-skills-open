---
id: DEC-0005
titulo: "Tratamiento documental de orientaciones y recursos no normativos"
estado: "Aceptada"
fecha: 2026-04-26
relacionadas: [PREG-003, FTE-001, DEC-0002, DEC-0004]
---

# DEC-0005 — Tratamiento documental de orientaciones y recursos no normativos

## Contexto

Los portales oficiales (`FTE-001` y derivados) enlazan junto a la normativa una capa amplia de orientaciones, guías metodológicas, ejemplificaciones y recursos didácticos que no son norma jurídica. La pregunta `PREG-003` requería decidir qué tratamiento dar a esos materiales para no incumplir la regla R8 (no mezclar normas con orientaciones no normativas).

## Decisión

1. **Excluir** del corpus normativo (`02_normativa/`), curricular (`03_curriculos/`) y de chunks IA (`07_corpus_ia/`) cualquier orientación, guía, infografía o recurso didáctico no normativo.
2. **Catalogar** los recursos relevantes únicamente como fichas de fuente con `tipo_fuente: orientacion-no-normativa` dentro de `01_fuentes/`, sin asignarles ID `NOR-NNN` ni `CUR-NNN`.
3. **Permitir referenciar** estas fichas desde análisis (`04_analisis/`) y relaciones (`05_relaciones/`) cuando aporten contexto, marcando el texto derivado como `[INTERPRETACIÓN]` si se incorpora a un análisis.
4. **No generar chunks IA** a partir de orientaciones; los chunks se reservan a normativa y currículo oficial conforme a `DEC-0002` y `DEC-0004`.

## Motivo

- Cumplir R8 evitando que IA o personas usuarias confundan orientaciones con obligaciones normativas.
- Conservar trazabilidad de los recursos relevantes sin elevarlos a la categoría de norma.
- Mantener el corpus IA homogéneo y auditable.

## Consecuencias

- Será necesario crear un nuevo `tipo_fuente: orientacion-no-normativa` en futuras revisiones de plantillas y validaciones.
- Las orientaciones citadas en análisis deberán aparecer claramente identificadas como no normativas.
- Algunos materiales útiles para profesorado quedarán fuera del corpus principal; podrán recogerse en una posible carpeta de recursos en una fase posterior.

## Relación con IA

Reduce el riesgo de respuestas IA que mezclen recomendaciones metodológicas con prescripciones normativas, manteniendo separación clara en el corpus indexado.

## Revisión futura

Revisar cuando se publique la decisión de crear o no una sección específica de recursos didácticos no normativos en el repositorio.
