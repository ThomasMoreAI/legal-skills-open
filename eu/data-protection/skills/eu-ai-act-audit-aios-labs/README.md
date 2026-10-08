# EU AI Act Audit

Skill para [Claude Code](https://claude.com/claude-code) que audita cualquier proyecto de software para cumplimiento del **EU AI Act** (Reglamento (UE) 2024/1689).

> [English version](docs/README.en.md)

## Que hace

Escanea tu codebase, identifica sistemas de IA, clasifica su nivel de riesgo y produce un informe estructurado con:

- Sistemas de IA detectados (modelos, SDKs, APIs)
- Clasificacion de riesgo (prohibido, alto, limitado, minimo)
- Estado de cumplimiento articulo por articulo
- Hallazgos priorizados con referencias a `archivo:linea`
- Interseccion con RGPD (transferencias internacionales, politica de privacidad)
- Fuentes regulatorias consultadas online

## Instalacion

```bash
npx skills add aios-labs/eu-ai-act-audit
```

O manualmente: copia la carpeta a `~/.claude/skills/eu-ai-act-audit/`.

## Uso

En cualquier proyecto con Claude Code:

```
revisa si este proyecto cumple el AI Act 2026
```

```
audit this repo for EU AI Act compliance
```

```
cumple mi proyecto la ley de IA europea?
```

La skill se activa automaticamente cuando pides una auditoria completa de cumplimiento.

## Que audita

### Paso 1: Investigacion regulatoria
Busca online las ultimas guias del EU AI Office, Codigos de Practica y actualizaciones.

### Paso 2: Deteccion de sistemas de IA
Escanea `package.json`, `requirements.txt`, rutas API, middlewares, prompts de sistema, variables de entorno...

### Paso 3: Rol de la organizacion
Clasifica como **provider**, **deployer**, **importador** o **distribuidor**.

### Paso 4: Clasificacion de riesgo
Aplica el arbol de decision del Anexo III:

```
Practica prohibida (Art. 5)?
  SI -> No se puede desplegar
  NO -> En Anexo III?
    SI -> Riesgo significativo? -> ALTO RIESGO
    NO -> Interactua con personas / genera contenido? -> RIESGO LIMITADO (Art. 50)
         Otro -> RIESGO MINIMO
```

### Paso 5-8: Cumplimiento
Verifica obligaciones de transparencia (Art. 50), RGPD, salvaguardas tecnicas y accesibilidad.

## Formato del reporte

```markdown
# EU AI Act Compliance Audit — [Proyecto]

## 1. Sistemas de IA Identificados
## 2. Clasificacion de Riesgo
## 3. Estado de Cumplimiento (tabla articulo por articulo)
## 4. Hallazgos (alta / media / baja prioridad)
## 5. Resumen
## Fuentes
```

## Fechas clave

| Fecha | Obligacion |
|---|---|
| 2 feb 2025 | Alfabetizacion IA (Art. 4) y practicas prohibidas (Art. 5) — **ya en vigor** |
| 2 ago 2025 | Obligaciones GPAI (Capitulo V) |
| **2 ago 2026** | **Transparencia (Art. 50), sistemas de alto riesgo (Anexo III)** |
| 2 ago 2027 | Sistemas de alto riesgo en productos regulados (Anexo I) |

## Estructura

```
eu-ai-act-audit/
├── SKILL.md                         # Instrucciones de la skill (workflow de 8 pasos)
├── references/
│   ├── risk-classification.md       # Categorias del Anexo III + arbol de decision
│   └── high-risk-obligations.md     # Checklist completo para alto riesgo
├── evals/
│   └── evals.json                   # Casos de test
└── docs/
    └── README.en.md                 # English version
```

## Multas por incumplimiento

| Infraccion | Multa maxima |
|---|---|
| Practicas prohibidas | 35M EUR o 7% facturacion global |
| Sistemas de alto riesgo | 15M EUR o 3% facturacion global |
| Informacion incorrecta | 7.5M EUR o 1% facturacion global |

## Licencia

MIT
