---
name: ronda-betobetico
title: /ronda
description: Revisa term sheets y pactos de inversión (SHA) para rondas de financiación. Analiza cláusulas clave, identifica risk flags y orienta la negociación. Cubre ampliaciones de capital, notas convertibles y SAFE. Usar cuando el usuario dice "ronda de inversión", "term sheet", "pacto de inversión", "SHA", "nota convertible", "SAFE", "vamos a levantar capital", o revisa documentación de una ronda.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/ronda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

# /ronda

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Identificar el tipo de instrumento (equity, convertible, SAFE).
3. Analizar cada cláusula clave.
4. Señalar risk flags.
5. Producir el informe de revisión.

---

## Propósito

Revisar documentación de rondas de inversión (term sheets, pactos de inversión/SHA, notas convertibles, SAFE) identificando cláusulas clave, risk flags y puntos de negociación. El informe es un borrador de análisis — la negociación final requiere letrado mercantilista.

## Instrumentos de inversión

### Ampliación de capital (equity directo)

- El inversor suscribe participaciones nuevas al precio acordado.
- Requiere acuerdo de junta general.
- Se formaliza en escritura pública e inscripción en el RM.
- Ref: LSC arts. 295-316.

### Nota convertible (préstamo convertible)

- Préstamo que se convierte en participaciones en la siguiente ronda.
- Términos clave: cap de valoración, descuento, tipo de interés, plazo de vencimiento.
- No requiere valoración inmediata de la empresa.

### SAFE (Simple Agreement for Future Equity)

- Similar a la nota convertible pero sin ser un préstamo (sin interés ni vencimiento).
- Se convierte en participaciones en un evento futuro (ronda cualificada, venta, IPO).
- Adaptación al derecho español: requiere cuidado — no existe regulación específica.

## Cláusulas clave del term sheet / SHA

| Cláusula | Descripción | Risk flags |
|---|---|---|
| **Valoración pre-money** | Valor de la empresa antes de la inversión | Valoración baja = mayor dilución para fundadores |
| **Valoración post-money** | Pre-money + inversión | Verificar que el cálculo es correcto |
| **Liquidation preference** | Preferencia del inversor en caso de liquidación/venta | Participating preferred = doble dip = muy desfavorable para fundadores |
| **Anti-dilución** | Protección del inversor ante rondas a la baja (down rounds) | Full ratchet = muy agresivo; weighted average = estándar de mercado |
| **Tag-along** | Derecho del inversor a vender junto con los fundadores | Estándar — protege al minoritario |
| **Drag-along** | Derecho del mayoritario a obligar a todos a vender | Verificar umbral (75%? 80%?) y precio mínimo |
| **Vesting de fundadores** | Los fundadores consolidan sus participaciones en el tiempo | Habitual; verificar que el cliff no es excesivo |
| **Board seats** | Composición del consejo de administración | Verificar que los fundadores mantienen control operativo |
| **Derechos de información** | Qué información debe dar la empresa al inversor | Exceso = carga administrativa; mínimo = legítimo |
| **Derecho de suscripción preferente (pro-rata)** | Derecho del inversor a participar en futuras rondas | Estándar |
| **Cláusulas de no competencia** | Restricciones para los fundadores | Verificar duración y ámbito — excesivas son nulas |
| **Key person** | Condiciones vinculadas a la permanencia de personas clave | Verificar consecuencias de salida |
| **Materias reservadas** | Decisiones que requieren aprobación del inversor | Listas largas = pérdida de control operativo |

## Valoración — Conceptos

| Concepto | Fórmula |
|---|---|
| Valoración pre-money | Acordada entre partes |
| Valoración post-money | Pre-money + importe invertido |
| Porcentaje del inversor | Inversión / Post-money |
| Dilución de fundadores | Porcentaje pre-ronda - porcentaje post-ronda |
| Precio por participación | Pre-money / n.o de participaciones pre-inversión |

## Risk flags — Checklist

| Flag | Descripción | Severidad |
|---|---|---|
| Participating preferred | El inversor cobra su preferencia Y participa pro-rata del resto | Alta |
| Full ratchet anti-dilución | Ajuste total en down round — devastador para fundadores | Alta |
| Drag-along con umbral bajo | < 75% permite a una minoría forzar la venta | Alta |
| Vesting acelerado solo para inversores | Asimetría injustificada | Media |
| Lista larga de materias reservadas | Bloqueo operativo de la empresa | Alta |
| Liquidation preference > 1x | El inversor cobra 2x o 3x antes que nadie | Muy alta |
| No hay cap en nota convertible | Conversión a cualquier valoración — el inversor se beneficia sin límite | Alta |
| SAFE sin eventos de conversión claros | Indefinición jurídica — conflicto futuro | Alta |

## Formato de salida

```markdown
BORRADOR — REVISIÓN DE RONDA DE INVERSIÓN — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Instrumento:** [ampliación de capital / nota convertible / SAFE]
> - **Risk flags identificados:** [N]
> - **Antes de actuar:** revisar con letrado mercantilista; validar valoración con asesor financiero; no firmar sin revisión completa del SHA y estatutos.

## Revisión: [Ronda X de Empresa Y]

### Resumen de la operación

| Parámetro | Valor |
|---|---|
| Tipo de instrumento | [tipo] |
| Importe de la ronda | [importe] |
| Valoración pre-money | [importe] |
| Valoración post-money | [importe] |
| Dilución fundadores | [%] |
| Inversor(es) | [nombres] |

### Análisis por cláusula

| Cláusula | Términos propuestos | Mercado habitual | Risk flag | Comentario |
|---|---|---|---|---|
| [cláusula] | [términos] | [estándar] | [sí/no] | [análisis] |

### Risk flags

[Detalle de cada risk flag con explicación y recomendación]

### Puntos de negociación sugeridos

1. [Punto 1 — qué pedir y por qué]
2. [Punto 2]
3. [Punto N]

---

**Qué hacer a continuación:**
1. **Negociar** — preparo contrapropuesta con los puntos de negociación.
2. **Revisar SHA completo** — si solo he visto el term sheet, necesito el SHA.
3. **Simular dilución** — tabla de capitalización pre y post ronda.
4. **Stock options** — `/startups:stock-options` para alinear el plan de incentivos con la ronda.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **LSC arts. 295-316** — ampliación de capital.
- **LSC art. 304** — derecho de suscripción preferente.
- **LSC art. 308** — exclusión del derecho de suscripción preferente.
- **CC arts. 1254 y ss.** — obligaciones y contratos (para notas convertibles y SAFE).

## Guardarraíles

- **No firmar un term sheet como si no fuera vinculante.** Aunque se diga "no vinculante", las cláusulas de exclusividad, confidencialidad y costes suelen ser vinculantes.
- **La valoración no es lo único que importa.** Un term sheet con buena valoración pero liquidation preference 2x participating preferred puede ser peor que uno con valoración inferior y 1x non-participating.
- **El SAFE en derecho español no tiene regulación propia.** Hay que encajarlo como contrato atípico — verificar la validez de cada cláusula.
- **Derecho de suscripción preferente (art. 304 LSC).** Si no se excluye expresamente en los estatutos o en la junta, los socios existentes tienen derecho preferente a suscribir las nuevas participaciones.
- **No confundir dilución económica con dilución de control.** Materias reservadas y composición del consejo pueden ser más relevantes que el porcentaje de participación.
- **Siempre derivar a letrado mercantilista para la negociación y ejecución.**
