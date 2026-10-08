---
name: contratacion-administrativo-4074-betobetico
title: /contratacion
description: Contratación pública — revisa el pliego de cargos y la documentación de licitaciones públicas en Panamá. Comprueba criterios de evaluación, idoneidad del proponente, fianzas y plazos. Cubre el recurso ante el Tribunal Administrativo de Contrataciones Públicas (TACP). Usar cuando el usuario diga "licitación", "pliego de cargos", "contrato público", "PanamaCompra", "TACP" o adjunte documentación de licitación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/administrativo/skills/contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

# /contratacion

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de entidad, historial de licitaciones.
2. Obtener la documentación de la licitación.
3. Revisar contra los requisitos de la Ley 22 de 2006.
4. Generar informe de revisión.

```
/administrativo:contratacion
[adjuntar pliego de cargos del acto público de servicios de limpieza del municipio]
```

---

## Propósito

La contratación pública en Panamá se rige por la Ley 22 de 2006 y sus reformas, ordenadas en el Texto Único por la Ley 153 de 2020, administrada por la Dirección General de Contrataciones Públicas (DGCP) —ente rector que administra PanamaCompra; reglamento en el Decreto Ejecutivo 40 de 2018— a través del portal PanamaCompra. El pliego de cargos es la ley del acto de selección: define quién puede participar, cómo se evalúa, qué se exige y cómo se ejecuta. Un error en el pliego puede invalidar la licitación; un error en la propuesta puede descalificarla. Este skill revisa la documentación desde ambas perspectivas.

---

## Checklist de revisión del pliego de cargos

### 1. Objeto y tipo de contrato

| Aspecto | Verificar |
|---|---|
| **Tipo de contrato** | Obras / Servicios / Suministros / Consultoría / Concesión [verificar] |
| **Monto / cuantía** | ¿Se establece correctamente el monto y la partida presupuestaria? |
| **División en renglones** | ¿La estructura por renglones es coherente con el objeto? |
| **Procedimiento de selección** | Licitación pública / Licitación por mejor valor (y por mejor valor con evaluación separada) / Licitación abreviada / Licitación para convenio marco / Subasta en reversa / Subasta de bienes públicos / Contratación menor (el procedimiento excepcional, sin concurrencia, es figura aparte) (Texto Único de la Ley 22 de 2006) |

### 2. Idoneidad y requisitos del proponente

| Tipo | Requisitos |
|---|---|
| **Capacidad legal** | Existencia legal (sociedad inscrita en el Registro Público), poder del representante, paz y salvo de la DGI y de la CSS (Texto Único de la Ley 22 de 2006 y Decreto Ejecutivo 40 de 2018) |
| **Capacidad técnica** | Experiencia, equipo, personal, certificaciones exigidas en el pliego [verificar] |
| **Capacidad financiera** | Estados financieros, referencias bancarias, capital de trabajo [verificar] |
| **Registro de proponentes** | Inscripción vigente en el Registro de Proponentes del sistema PanamaCompra (art. 2 —glosario— del Texto Único de la Ley 22 de 2006) |

**Verificar:** ¿Los requisitos de idoneidad son proporcionales al objeto del contrato y no restringen indebidamente la participación?

### 3. Criterios de evaluación y adjudicación

| Aspecto | Verificar |
|---|---|
| **Metodología de evaluación** | ¿Mejor valor (técnica + precio) o menor precio? |
| **Criterios técnicos** | ¿Son claros, objetivos y ponderados? |
| **Criterio de precio** | ¿La fórmula de puntaje del precio es clara y no distorsiona? |
| **Ponderación** | ¿Se indica la ponderación de cada criterio? |
| **Subsanación** | ¿Qué requisitos son subsanables y cuáles descalifican? |

### 4. Fianzas

| Tipo | Importe | Cuándo |
|---|---|---|
| **Fianza de propuesta** | Porcentaje del valor de la propuesta según pliego [verificar] | Exigida para participar [verificar] |
| **Fianza de cumplimiento** | No menor del 10% del monto del contrato (salvo obras), con tope de B/.1,000,000.00 (art. 123 del Texto Único de la Ley 22 de 2006) | Al formalizar el contrato |
| **Fianza de pago anticipado / buen funcionamiento** | Según pliego | Si el pliego lo prevé [verificar] |

### 5. Plazos

| Plazo | Referencia |
|---|---|
| **Convocatoria y presentación de propuestas** | Plazo mínimo según la Ley 22 de 2006 publicado en PanamaCompra [verificar] |
| **Adjudicación** | Plazo del pliego tras el acto público [verificar] |
| **Formalización del contrato** | Plazo del pliego tras la adjudicación en firme [verificar] |
| **Refrendo de la Contraloría General de la República** | Requisito de perfeccionamiento/eficacia del contrato estatal (art. 93 del Texto Único de la Ley 22 de 2006) |

### 6. Modificaciones y prórrogas del contrato

- ¿Se prevén adendas o modificaciones en el pliego?
- ¿Se respetan los límites de variación del monto previstos en la Ley 22 de 2006? [verificar]
- ¿Se motiva debidamente y se obtiene el refrendo de la Contraloría? [verificar]

### 7. Subcontratación

- ¿Se limita la subcontratación? ¿En qué porcentaje?
- ¿Se exige autorización previa de la entidad contratante?

---

## Recurso ante el Tribunal Administrativo de Contrataciones Públicas (TACP)

| Aspecto | Detalle |
|---|---|
| **Órgano** | Tribunal Administrativo de Contrataciones Públicas (TACP), que resuelve el recurso de impugnación (art. 125 del Texto Único de la Ley 22 de 2006) |
| **Actos recurribles** | Adjudicación, declaratoria de deserción, rechazo de propuestas y actos que afecten la selección objetiva (art. 125 del Texto Único de la Ley 22 de 2006) |
| **Plazo** | 5 días hábiles desde la notificación del acto (art. 125 del Texto Único de la Ley 22 de 2006) |
| **Fianza de impugnación** | 10% (bienes/servicios) o 15% (obras) (art. 125 del Texto Único de la Ley 22 de 2006) |
| **Efecto** | Según lo previsto en el Texto Único de la Ley 22 de 2006 (puede suspender el procedimiento) [verificar] |
| **Vía posterior** | Demanda contencioso-administrativa ante la Sala Tercera de la CSJ |

---

## Formato de salida

```markdown
# Revisión de licitación: [Objeto del contrato]

**Entidad contratante:** [nombre]
**Tipo de contrato:** [obras / servicios / suministros / consultoría / concesión]
**Procedimiento:** [licitación pública / licitación por mejor valor / licitación abreviada / convenio marco / subasta en reversa / subasta de bienes públicos / contratación menor / procedimiento excepcional]
**Monto / cuantía:** [importe en B/. / USD]
**Plazo de presentación de propuestas:** [fecha]

---

## Resumen de la revisión

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Bloqueante

---

## Detalle por área

| # | Área | Hallazgo | Riesgo | Base legal | Acción |
|---|---|---|---|---|---|
| 1 | Idoneidad | [Ej., Exigencia desproporcionada] | Alto | Ley 22 de 2006 | Impugnar pliego |
| 2 | Evaluación | [Ej., Fórmula de precio distorsionante] | Medio | Ley 22 de 2006 | Solicitar aclaración |
| ... | ... | ... | ... | ... | ... |

---

## Viabilidad del recurso ante el TACP

**¿Procede recurso ante el TACP?** [Sí/No — Ley 22 de 2006]
**Plazo:** [fecha límite]
**Órgano:** Tribunal Administrativo de Contrataciones Públicas (TACP)
**Vía posterior:** Demanda contencioso-administrativa ante la Sala Tercera de la CSJ

---

## Recomendaciones para la propuesta

[Si se revisa desde la perspectiva del proponente: puntos a reforzar en la propuesta]
```

---

## Legislación de referencia

- Ley 22 de 2006 — Que regula la contratación pública
- Ley 153 de 2020 — Reformas a la Ley 22 de 2006
- Texto Único de la Ley 22 de 2006, ordenado por la Ley 153 de 2020 — texto vigente consolidado
- Decreto Ejecutivo 40 de 2018 — reglamento de la Ley 22 de 2006; la Dirección General de Contrataciones Públicas (DGCP) es el ente rector que administra el portal PanamaCompra
- Fallos y resoluciones del Tribunal Administrativo de Contrataciones Públicas (TACP)

---

## Lo que este skill NO hace

- No prepara la propuesta técnica ni la oferta económica — revisa el pliego de cargos y señala riesgos.
- No presenta el recurso ante el TACP — analiza la viabilidad.
- No cubre contratos del sector privado — solo contratación pública (Ley 22 de 2006).
