---
name: contratacion-startups-betobetico
title: /contratacion
description: 'Guía para las primeras contrataciones de una startup: tipos de contrato, convenio colectivo aplicable, coste real, alternativas (autónomos, becarios) y riesgos (falso autónomo). Usar cuando el usuario dice "contratar empleados", "primer empleado", "coste de contratación", "convenio colectivo", "falso autónomo", o necesita orientación sobre sus primeras contrataciones.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /contratacion

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de la empresa y el perfil a contratar.
3. Analizar opciones de contratación.
4. Calcular coste real.
5. Producir la guía con recomendación.

---

## Propósito

Orientar a startups en sus primeras contrataciones, explicando las opciones legales, los costes reales y los riesgos de cada alternativa. Es una guía — la formalización requiere asesor laboral o gestoría.

## Tipos de contrato laboral

### Contrato indefinido

- **Modalidad estándar** tras la reforma laboral de 2022 (RDL 32/2021).
- **Periodo de prueba:** hasta 6 meses (titulados) o 2 meses (resto), salvo convenio.
- **Bonificaciones:** variable según la normativa vigente — verificar en SEPE [verificar].
- **Indemnización por despido:** 33 días/año (máx. 24 mensualidades) si procedente; 20 días/año si objetivo; nulo si improcedente (33 días/año con readmisión o indemnización).

### Contrato de formación en alternancia (art. 11.2 ET)

- **Para quién:** personas entre 16 y 30 años, vinculado a formación reglada.
- **Duración:** mínimo 3 meses, máximo 2 años.
- **Retribución:** no inferior al SMI proporcional al tiempo de trabajo efectivo (mínimo 65% el primer año, 85% el segundo).
- **Cotización SS:** tarifa plana reducida [verificar importe vigente].

### Contrato formativo para obtención de práctica profesional (art. 11.3 ET)

- **Para quién:** titulados universitarios o FP, dentro de los 3 años siguientes a la titulación (5 años si discapacidad).
- **Duración:** mínimo 6 meses, máximo 1 año.
- **Retribución:** la del convenio; en defecto, no inferior al SMI.

### Contrato temporal (limitado tras reforma 2022)

- **Solo dos causas:** circunstancias de la producción (art. 15.2 ET) o sustitución (art. 15.3 ET).
- **Duración máxima:** 6 meses (ampliable a 12 por convenio) para circunstancias de la producción.
- **Fraude:** si no hay causa real, se presume indefinido.

## Convenio colectivo aplicable

| Actividad de la empresa | Convenio probable | Notas |
|---|---|---|
| Desarrollo de software / TIC | XVII Convenio Colectivo Estatal de Empresas de Consultoría y Estudios de Mercado | El más habitual para startups tech |
| Comercio electrónico | Convenio de comercio del ámbito territorial | Según actividad principal |
| Marketing / publicidad | Convenio de empresas de publicidad | |
| Otro | Según actividad principal de la empresa (CNAE) | Consultar en el RM |

**Importante:** el convenio se determina por la actividad principal de la empresa, no por la función del trabajador. Una startup de software aplica el convenio de consultoría a todos sus empleados, incluidos los de administración o marketing.

## Coste real de un empleado

| Concepto | Cálculo orientativo |
|---|---|
| Salario bruto anual | [SBA] |
| Seguridad Social empresa (~30%) | SBA x 0,30 |
| **Coste total empresa** | **SBA x 1,30 aprox.** |
| Otros costes | Prevención de riesgos, formación, seguros |

### Ejemplo: desarrollador junior (Madrid, 2025)

| Concepto | Importe orientativo [verificar] |
|---|---|
| Salario bruto anual | 24.000-30.000 EUR |
| SS empresa (~30%) | 7.200-9.000 EUR |
| Coste total empresa | 31.200-39.000 EUR |
| Salario neto mensual (14 pagas) | ~1.500-1.800 EUR |

## Alternativas al contrato laboral

### Autónomo (colaborador externo)

| Ventaja | Riesgo |
|---|---|
| Sin coste de SS empresa | **Falso autónomo** — si hay dependencia y ajenidad, es relación laboral encubierta |
| Flexibilidad | Sanción ITSS: conversión en indefinido + cotizaciones retroactivas + sanción administrativa |
| Factura + IVA | El autónomo puede reclamar laboralidad en cualquier momento |

**Indicios de falso autónomo (jurisprudencia ITSS y TS):**
- Horario fijo impuesto por la empresa.
- Uso de medios de la empresa (ordenador, oficina, email corporativo).
- Integración en la estructura organizativa.
- Un solo cliente (la empresa).
- No poder rechazar encargos.

### Becario

| Requisito | Detalle |
|---|---|
| Convenio con centro educativo | Obligatorio — sin convenio no hay beca válida |
| Vinculación a formación | La beca debe tener contenido formativo real |
| Tutor en la empresa | Obligatorio |
| Bolsa/ayuda | No obligatoria legalmente pero recomendable |
| Cotización SS | Obligatoria desde RDL 2/2023 [verificar] |

**Riesgo:** si no hay contenido formativo real, es relación laboral encubierta.

## Formato de salida

```markdown
BORRADOR — GUÍA DE CONTRATACIÓN — REVISIÓN LABORAL OBLIGATORIA

> **Nota para el revisor**
> - **Perfiles analizados:** [N]
> - **Convenio colectivo identificado:** [nombre]
> - **Elementos marcados [verificar]:** [N — salarios, bonificaciones y costes pueden haber cambiado]
> - **Antes de actuar:** verificar convenio colectivo aplicable; comprobar bonificaciones vigentes en SEPE; confirmar costes de SS actualizados; consultar con asesor laboral.

## Guía de contratación: [Nombre de la empresa]

### Recomendación por perfil

| Perfil | Tipo recomendado | Coste estimado/año | Observaciones |
|---|---|---|---|
| [perfil] | [tipo contrato] | [coste] | [notas] |

### Convenio colectivo aplicable

**[Nombre del convenio]** — categorías profesionales, salarios mínimos por categoría, jornada.

### Coste detallado

[Tabla con desglose por perfil]

### Riesgos identificados

[Falso autónomo, contratos temporales sin causa, etc.]

---

**Qué hacer a continuación:**
1. **Redactar contrato** — preparo borrador de contrato laboral.
2. **Alta en SS** — checklist de trámites de alta.
3. **Stock options** — `/startups:stock-options` para plan de incentivos del equipo.
4. **Plan de coste a 12 meses** — proyección de coste de plantilla.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **ET (RDL 2/2015)** — Estatuto de los Trabajadores.
- **RDL 32/2021** — reforma laboral (limitación temporalidad).
- **Art. 11 ET** — contratos formativos.
- **Art. 15 ET** — contratación temporal.
- **LGSS (RDL 8/2015)** — cotización a la Seguridad Social.
- **Ley 31/1995** — prevención de riesgos laborales.
- **XVII Convenio de Consultoría** — BOE, el más habitual para startups TIC.

## Guardarraíles

- **El riesgo de falso autónomo es real y costoso.** La ITSS es cada vez más activa. No recomendar la contratación de autónomos cuando la relación tiene indicios claros de laboralidad.
- **La reforma de 2022 limitó la temporalidad.** No recomendar contratos temporales sin causa real — la presunción es de indefinido.
- **El convenio colectivo fija mínimos.** No se puede pagar por debajo del convenio aunque el empleado acepte.
- **Los costes de SS cambian.** Marcar `[verificar]` en todo porcentaje y cifra de cotización.
- **El alta RETA de socios con >25% es obligatoria.** No es opcional y genera un coste mensual significativo (~300 EUR/mes mínimo [verificar]).
- **Siempre derivar a asesor laboral/gestoría para la formalización.** Un contrato mal hecho puede ser más costoso que el ahorro de no pagar asesoramiento.
