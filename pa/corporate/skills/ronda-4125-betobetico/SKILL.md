---
name: ronda-4125-betobetico
title: /ronda
description: Revisa term sheets y pactos de inversión (SHA) para rondas de financiación. Analiza cláusulas clave, identifica risk flags y orienta la negociación. Cubre ampliaciones de capital, notas convertibles y SAFE. Usar cuando el usuario dice "ronda de inversión", "term sheet", "pacto de inversión", "SHA", "nota convertible", "SAFE", "vamos a levantar capital", o revisa documentación de una ronda.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/ronda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

Revisar documentación de rondas de inversión (term sheets, pactos de inversión/SHA, notas convertibles, SAFE) identificando cláusulas clave, risk flags y puntos de negociación. El informe es un borrador de análisis — la negociación final requiere abogado mercantilista.

## Instrumentos de inversión

### Emisión de acciones (equity directo)

- El inversionista suscribe acciones nuevas al precio acordado.
- Requiere acuerdo de junta de accionistas y, en su caso, junta directiva.
- Se formaliza y, si modifica el pacto social (p. ej. aumento de capital autorizado), se inscribe en el Registro Público.
- Ref: Ley 32 de 1927.

### Nota convertible (préstamo convertible)

- Préstamo que se convierte en acciones en la siguiente ronda.
- Términos clave: cap de valoración, descuento, tipo de interés, plazo de vencimiento.
- No requiere valoración inmediata de la empresa.

### SAFE (Simple Agreement for Future Equity)

- Similar a la nota convertible pero sin ser un préstamo (sin interés ni vencimiento).
- Se convierte en acciones en un evento futuro (ronda cualificada, venta, IPO).
- Adaptación al derecho panameño: requiere cuidado — no existe regulación específica; se encaja como contrato atípico al amparo de la libertad contractual del Código de Comercio y el Código Civil.

## Cláusulas clave del term sheet / SHA

| Cláusula | Descripción | Risk flags |
|---|---|---|
| **Valoración pre-money** | Valor de la empresa antes de la inversión | Valoración baja = mayor dilución para fundadores |
| **Valoración post-money** | Pre-money + inversión | Verificar que el cálculo es correcto |
| **Liquidation preference** | Preferencia del inversor en caso de liquidación/venta | Participating preferred = doble dip = muy desfavorable para fundadores |
| **Anti-dilución** | Protección del inversor ante rondas a la baja (down rounds) | Full ratchet = muy agresivo; weighted average = estándar de mercado |
| **Tag-along** | Derecho del inversor a vender junto con los fundadores | Estándar — protege al minoritario |
| **Drag-along** | Derecho del mayoritario a obligar a todos a vender | Verificar umbral (75%? 80%?) y precio mínimo |
| **Vesting de fundadores** | Los fundadores consolidan sus acciones en el tiempo | Habitual; verificar que el cliff no es excesivo |
| **Board seats** | Composición de la junta directiva | Verificar que los fundadores mantienen control operativo |
| **Derechos de información** | Qué información debe dar la empresa al inversor | Exceso = carga administrativa; mínimo = legítimo |
| **Derecho de suscripción preferente (pro-rata)** | Derecho del inversionista a participar en futuras rondas | Estándar |
| **Cláusulas de no competencia** | Restricciones para los fundadores | Verificar duración y ámbito — excesivas son nulas |
| **Key person** | Condiciones vinculadas a la permanencia de personas clave | Verificar consecuencias de salida |
| **Materias reservadas** | Decisiones que requieren aprobación del inversor | Listas largas = pérdida de control operativo |

## Valoración — Conceptos

| Concepto | Fórmula |
|---|---|
| Valoración pre-money | Acordada entre partes |
| Valoración post-money | Pre-money + importe invertido |
| Porcentaje del inversionista | Inversión / Post-money |
| Dilución de fundadores | Porcentaje pre-ronda - porcentaje post-ronda |
| Precio por acción | Pre-money / n.o de acciones pre-inversión |

## Risk flags — Checklist

| Flag | Descripción | Severidad |
|---|---|---|
| Participating preferred | El inversionista cobra su preferencia Y participa pro-rata del resto | Alta |
| Full ratchet anti-dilución | Ajuste total en down round — devastador para fundadores | Alta |
| Drag-along con umbral bajo | < 75% permite a una minoría forzar la venta | Alta |
| Vesting acelerado solo para inversionistas | Asimetría injustificada | Media |
| Lista larga de materias reservadas | Bloqueo operativo de la empresa | Alta |
| Liquidation preference > 1x | El inversionista cobra 2x o 3x antes que nadie | Muy alta |
| No hay cap en nota convertible | Conversión a cualquier valoración — el inversionista se beneficia sin límite | Alta |
| SAFE sin eventos de conversión claros | Indefinición jurídica — conflicto futuro | Alta |

## Formato de salida

```markdown
BORRADOR — REVISIÓN DE RONDA DE INVERSIÓN — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Instrumento:** [emisión de acciones / nota convertible / SAFE]
> - **Risk flags identificados:** [N]
> - **Antes de actuar:** revisar con abogado mercantilista; validar valoración con asesor financiero; no firmar sin revisión completa del SHA y el pacto social.

## Revisión: [Ronda X de Empresa Y]

### Resumen de la operación

| Parámetro | Valor |
|---|---|
| Tipo de instrumento | [tipo] |
| Importe de la ronda | [importe USD] |
| Valoración pre-money | [importe USD] |
| Valoración post-money | [importe USD] |
| Dilución fundadores | [%] |
| Inversionista(s) | [nombres] |

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

- **Ley 32 de 1927** — sociedades anónimas (emisión de acciones, junta de accionistas).
- **Código de Comercio de Panamá** — actos de comercio y libertad de pacto.
- **Código Civil de Panamá** — obligaciones y contratos (para notas convertibles y SAFE como contratos atípicos).
- **SMV (Superintendencia del Mercado de Valores)** — si la oferta de valores supera el ámbito privado y constituye oferta pública, puede requerir registro o exención ante la SMV [verificar].

## Guardarraíles

- **No firmar un term sheet como si no fuera vinculante.** Aunque se diga "no vinculante", las cláusulas de exclusividad, confidencialidad y costes suelen ser vinculantes.
- **La valoración no es lo único que importa.** Un term sheet con buena valoración pero liquidation preference 2x participating preferred puede ser peor que uno con valoración inferior y 1x non-participating.
- **El SAFE en derecho panameño no tiene regulación propia.** Hay que encajarlo como contrato atípico al amparo de la libertad contractual — verificar la validez de cada cláusula.
- **Derecho de suscripción preferente.** Verificar si el pacto social o el pacto de accionistas reconoce a los accionistas existentes un derecho preferente a suscribir las nuevas acciones [verificar].
- **Oferta de valores y SMV.** Una colocación amplia de acciones o instrumentos convertibles puede calificar como oferta pública sujeta a la Superintendencia del Mercado de Valores (SMV) — verificar si aplica alguna exención de oferta privada [verificar].
- **No confundir dilución económica con dilución de control.** Materias reservadas y composición de la junta directiva pueden ser más relevantes que el porcentaje de participación.
- **Siempre derivar a abogado mercantilista para la negociación y ejecución.**
