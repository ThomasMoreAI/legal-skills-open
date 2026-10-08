# Modelo de output — `.compliance/` versionado en el repo

El resultado NO son PDFs sueltos: es un **estado vivo** dentro del repo auditado, versionado
por git. Re-correr la skill compara contra el estado anterior y reporta avance/**drift**.

## Estructura escrita en `<repo>/.compliance/`
```
.compliance/
├── state.json        # estado de controles + score por marco (la "postura")
├── RESUMEN.md        # informe legible + diff vs corrida anterior + plan
└── docs/             # documentos generados por los packs activos
    ├── 21719-rat.md
    ├── 21719-politica-privacidad.md
    ├── 21719-dpa.md
    ├── 21719-plan-respuesta-brechas.md
    ├── 21595-modelo-prevencion-delitos.md
    ├── 21595-codigo-etica.md
    └── 21595-matriz-riesgos.md
```

## `state.json` (esquema)
```json
{
  "schema": 1,
  "generated_at": "[ISO-8601, pedir al sistema con `date`]",
  "git_commit": "[git rev-parse --short HEAD]",
  "company": { "razon_social": "...", "rut": "...", "tamano": "micro|pequena|mediana|grande" },
  "active_packs": ["ley-21595", "ley-21719"],
  "controls": {
    "sec-mfa": { "status": "pass|partial|fail|unknown", "evidence": "auth/mfa.ts:42", "remediation": "" },
    "data-derechos": { "status": "fail", "evidence": "", "remediation": "Agregar endpoint export+delete" }
  },
  "frameworks": {
    "ley-21719": { "score": 0.62, "controls_required": 14, "pass": 7, "partial": 2, "fail": 5 },
    "ley-21595": { "score": 0.40, "controls_required": 8, "pass": 2, "partial": 2, "fail": 4 }
  }
}
```
- `score` = (pass + 0.5·partial) / controls_required.
- Timestamp y commit reales: obtenerlos con Bash (`date -u +%FT%TZ`, `git rev-parse --short HEAD`),
  no inventarlos.

## Re-corrida (compliance vivo)
1. Si existe `state.json`, cárgalo como `previo`.
2. Tras evaluar, compara control a control:
   - **avance**: fail/partial/unknown → pass.
   - **drift**: pass → fail/partial (algo que cumplía dejó de cumplir).
3. En `RESUMEN.md`, sección "Cambios vs última corrida ([fecha previa])": lista avances y drift,
   y la variación de score por marco.

## Versionado
- git es el audit trail: cada corrida = un commit de `.compliance/`.
- Sugerir al usuario: `git add .compliance && git commit -m "compliance: snapshot [fecha]"`.
- Más adelante (productización), esto mismo corre en CI por release; aquí basta correr la skill.
