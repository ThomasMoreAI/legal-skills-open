---
name: contratacion-administrativo-betobetico
title: /contratacion
description: Contratación pública — revisa pliegos (PCAP, PPT) y documentación de licitaciones. Comprueba criterios de adjudicación, solvencia, garantías y plazos. Cubre el recurso especial ante el TACRC (art. 44 LCSP). Usar cuando el usuario diga "licitación", "pliego", "contrato público", "recurso especial", "TACRC", "LCSP" o adjunte documentación de licitación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/administrativo/skills/contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /contratacion

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de entidad, historial de licitaciones.
2. Obtener la documentación de la licitación.
3. Revisar contra los requisitos de la LCSP.
4. Generar informe de revisión.

```
/administrativo:contratacion
[adjuntar PCAP del contrato de servicios de limpieza del Ayuntamiento]
```

---

## Propósito

La contratación pública en España se rige por la LCSP 9/2017, que transpone las directivas europeas de contratación. Los pliegos (PCAP y PPT) son la ley del contrato: definen quién puede licitar, cómo se valora, qué se exige y cómo se ejecuta. Un error en los pliegos puede invalidar la licitación; un error en la oferta puede excluirla. Este skill revisa la documentación desde ambas perspectivas.

---

## Checklist de revisión de pliegos

### 1. Objeto y tipo de contrato (arts. 12-18 LCSP)

| Aspecto | Verificar |
|---|---|
| **Tipo de contrato** | Obras / Servicios / Suministros / Concesión de obras / Concesión de servicios |
| **Valor estimado** | ¿Se calcula correctamente? (art. 101 LCSP) ¿Incluye prórrogas y modificaciones previsibles? |
| **Lote/División en lotes** | ¿Se ha justificado la no división en lotes? (art. 99.3 LCSP — obligación de motivar) |
| **Procedimiento** | Abierto / Restringido / Negociado / Diálogo competitivo / Asociación para la innovación / Menor |

### 2. Solvencia (arts. 74-86 LCSP)

| Tipo | Requisitos |
|---|---|
| **Económica y financiera** (art. 87) | Volumen de negocio, seguros, patrimonio neto |
| **Técnica o profesional** (arts. 88-91) | Experiencia, equipos, personal, certificaciones |
| **Clasificación empresarial** | ¿Es obligatoria? (obras >500.000 EUR — art. 77; servicios: potestativa) |

**Verificar:** ¿Los requisitos de solvencia son proporcionales al objeto del contrato? (art. 74.2 LCSP)

### 3. Criterios de adjudicación (arts. 145-149 LCSP)

| Aspecto | Verificar |
|---|---|
| **Mejor relación calidad-precio** | ¿Se valoran criterios de calidad o solo precio? |
| **Criterios cuantificables por fórmulas** | ¿Las fórmulas son claras y no distorsionan? |
| **Criterios sujetos a juicio de valor** | ¿No superan los cuantificables automáticamente (salvo excepciones)? |
| **Ponderación** | ¿Se indica la ponderación de cada criterio? |
| **Criterios sociales y medioambientales** | ¿Se incluyen? (arts. 145.2, 148 LCSP) |
| **Ofertas anormalmente bajas** | ¿Se define el umbral? (art. 149 LCSP) |

### 4. Garantías (arts. 106-113 LCSP)

| Tipo | Importe | Cuándo |
|---|---|---|
| **Garantía provisional** | Hasta 3% del presupuesto base | Potestativa (art. 106) |
| **Garantía definitiva** | 5% del precio de adjudicación (IVA excluido) | Obligatoria salvo excepciones (art. 107) |
| **Garantía complementaria** | Hasta 5% adicional | Si el pliego lo prevé (art. 107.3) |

### 5. Plazos (arts. 156-165 LCSP)

| Plazo | Mínimo |
|---|---|
| **Presentación de ofertas (abierto)** | 35 días desde envío del anuncio (15 días si urgencia) |
| **Presentación de ofertas (restringido)** | 30 días desde invitación |
| **Adjudicación** | 2 meses desde apertura de ofertas (salvo prórroga motivada) |
| **Formalización** | 15 días hábiles desde notificación de adjudicación (si no hay recurso especial) |

### 6. Modificaciones del contrato (arts. 203-207 LCSP)

- ¿Se prevén modificaciones en el pliego? (art. 204)
- ¿Se respetan los límites de modificación no prevista? (art. 205 — <50% del precio)
- ¿Se motiva debidamente?

### 7. Subcontratación (art. 215 LCSP)

- ¿Se limita la subcontratación? ¿En qué porcentaje?
- ¿Se exige comunicación previa?
- Obligación de pago directo a subcontratistas (art. 216 LCSP)

---

## Recurso especial en materia de contratación (arts. 44-60 LCSP)

| Aspecto | Detalle |
|---|---|
| **Órgano** | TACRC (estatal) o tribunal autonómico equivalente |
| **Actos recurribles** | Anuncios de licitación, pliegos, actos de trámite cualificados, adjudicación, modificaciones, resolución |
| **Contratos susceptibles** | SARA (sujetos a regulación armonizada) + concesiones >5M EUR + determinados servicios sociales |
| **Plazo** | 15 días hábiles desde notificación del acto |
| **Efecto** | Suspensión automática si se recurre la adjudicación antes de formalizar (art. 53) |
| **Resolución** | 5 días hábiles (medidas provisionales) / plazo breve para el fondo |

---

## Formato de salida

```markdown
# Revisión de licitación: [Objeto del contrato]

**Órgano de contratación:** [nombre]
**Tipo de contrato:** [obras / servicios / suministros / concesión]
**Procedimiento:** [abierto / restringido / negociado / menor]
**Valor estimado:** [importe]
**Plazo de presentación:** [fecha]

---

## Resumen de la revisión

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Bloqueante

---

## Detalle por área

| # | Área | Hallazgo | Riesgo | Base legal | Acción |
|---|---|---|---|---|---|
| 1 | Solvencia | [Ej., Exigencia desproporcionada] | Alto | Art. 74.2 LCSP | Impugnar pliego |
| 2 | Adjudicación | [Ej., Fórmula de precio distorsionante] | Medio | Art. 146 LCSP | Solicitar aclaración |
| ... | ... | ... | ... | ... | ... |

---

## Viabilidad del recurso especial

**¿Es contrato SARA?** [Sí/No]
**¿Procede recurso especial?** [Sí/No — art. 44 LCSP]
**Plazo:** [fecha límite]
**Órgano:** [TACRC / tribunal autonómico]

---

## Recomendaciones para la oferta

[Si se revisa desde la perspectiva del licitador: puntos a reforzar en la oferta]
```

---

## Legislación de referencia

- LCSP (Ley 9/2017) — Ley de Contratos del Sector Público
- RGLCAP (RD 1098/2001) — Reglamento (parcialmente vigente)
- Directiva 2014/24/UE — contratación pública clásica
- Directiva 2014/23/UE — concesiones
- Resoluciones y doctrina del TACRC

---

## Lo que este skill NO hace

- No prepara la oferta técnica ni la proposición económica — revisa pliegos y señala riesgos.
- No presenta recurso especial ante el TACRC — analiza la viabilidad.
- No cubre contratos del sector privado — solo contratación pública (LCSP).
