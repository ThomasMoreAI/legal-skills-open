---
id: DEC-0004
titulo: "Alcance editorial de extracción curricular"
estado: "Aceptada"
fecha: 2026-04-26
relacionadas: [PREG-002, CUR-001, CUR-023, NOR-003]
---

# DEC-0004 — Alcance editorial de extracción curricular

## Contexto

Las fichas curriculares `CUR-001` a `CUR-023` se crearon en estado pendiente sin fijar qué elementos curriculares se extraerían de cada decreto. La pregunta `PREG-002` solicitaba decidir el alcance editorial para competencias específicas, criterios de evaluación, saberes básicos, descriptores operativos y situaciones de aprendizaje.

## Decisión

Adoptar dos niveles de extracción coordinados:

1. **YAML estructurado obligatorio** por cada ficha curricular:
   - Competencias específicas (con su numeración oficial).
   - Criterios de evaluación asociados a cada competencia.
   - Saberes básicos por bloque.
   - Vinculación con descriptores operativos del perfil de salida.
2. **Markdown narrativo opcional**:
   - Síntesis breve por curso o por bloque.
   - Una situación de aprendizaje ejemplificadora por etapa, sólo cuando aparezca textualmente en la fuente oficial; nunca inventada.

Las orientaciones metodológicas y los recursos didácticos quedan fuera del alcance de la ficha curricular y se rigen por `DEC-0005`.

## Motivo

- Garantizar trazabilidad uno-a-uno con el decreto autonómico (`FTE-009` y posteriores) sin diluir el corpus con material no normativo.
- Mantener un nivel de detalle uniforme entre materias para que IA y personas usuarias puedan comparar fichas.
- Limitar el coste editorial a lo que aparece literalmente en la fuente, conforme a R1 y R7.

## Consecuencias

- Las fichas curriculares incompletas se mantendrán en `estado_extraccion: pendiente` hasta volcar los cuatro elementos YAML obligatorios.
- Las situaciones de aprendizaje copiadas o adaptadas que no aparezcan en fuente oficial deben marcarse como `[INTERPRETACIÓN]` o quedar excluidas.
- Los criterios e indicadores intermedios elaborados por terceros no se incorporan al corpus principal.

## Relación con IA

Los chunks IA derivados de currículos sólo se generarán a partir de los bloques YAML estructurados, evitando que el modelo mezcle texto normativo con orientaciones no oficiales.

## Revisión futura

Revisar tras completar la extracción de la primera materia (previsiblemente `CUR-001`) para validar que los cuatro bloques cubren las necesidades reales de consulta.
