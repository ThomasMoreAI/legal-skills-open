# Rule Engine — Diseño (v2)

Objetivo

Motor híbrido para inferencia jurídica que combine:
- Reglas declarativas (DSL)
- Encadenamiento hacia adelante (forward chaining)
- Búsquedas y consultas (backward chaining)

Paradigma y tipos de regla

- Qualification rules: clasificación legal
- Obligation rules: generación de deberes
- Sanction rules: consecuencias
- Validation rules: comprobaciones de cumplimiento

DSL de ejemplo

rule: despido_injustificado
when:
  event.type == "despido"
  AND event.facts.justified == false
then:
  classify(event, "despido_injustificado")
  create_obligation("indemnizacion", actor="empleador")
  reference_norm("norm:mx:lft:art48")

Ejecución

1. Ingesta de hechos → normalización (LegalEvent)
2. Enriquecimiento: enlazar actores, normas y conceptos
3. Matching de reglas y agenda scheduler
4. Inferencia iterativa y resolución de conflictos
5. Salida: clasificaciones, obligaciones y explicación

Conflict resolution

Prioridad (stack):
1. Constitucional
2. Leyes federales
3. Leyes estatales
4. Reglamentos
5. Jurisprudencia (según obligatoriedad)

Explanation Engine

Cada decisión debe incluir justificación estructurada:

{
  "result": "despido_injustificado",
  "justification": [
    {
      "rule": "despido_injustificado",
      "facts_used": ["event:despido"],
      "norms": ["norm:mx:lft:art48"]
    }
  ]
}

Pruebas

- Unit: corrección de reglas
- Integration: cadenas de inferencia
- Regression: actualizaciones normativas

