---
name: contratacion-startups-4019-betobetico
title: /contratacion
description: 'Guía para las primeras contrataciones de una startup en Panamá: tipos de contrato del Código de Trabajo, coste real (cuotas CSS, décimo tercer mes), alternativas (contratistas independientes, pasantes) y riesgos (relación laboral encubierta). Usar cuando el usuario dice "contratar empleados", "primer empleado", "coste de contratación", "Código de Trabajo", "contratista independiente", o necesita orientación sobre sus primeras contrataciones.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
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

Orientar a startups en sus primeras contrataciones, explicando las opciones legales del Código de Trabajo de Panamá, los costes reales y los riesgos de cada alternativa. Es una guía — la formalización requiere asesor laboral.

## Tipos de contrato laboral (Código de Trabajo de Panamá)

### Contrato por tiempo indefinido

- **Modalidad estándar** cuando la relación es permanente.
- **Periodo de prueba:** hasta 3 meses [verificar], durante los cuales la relación puede terminar sin indemnización.
- **Estabilidad:** tras 2 años de servicio continuo, el trabajador adquiere estabilidad reforzada [verificar].
- **Indemnización por despido injustificado:** prima de antigüedad e indemnización según años de servicio conforme al Código de Trabajo [verificar tablas].

### Contrato por tiempo definido

- **Para quién:** labores de naturaleza temporal o por un plazo determinado.
- **Duración máxima:** 1 año [verificar], renovable dentro de los límites legales; superado el límite o si la labor es permanente, se presume indefinido.

### Contrato por obra determinada

- **Para quién:** ejecución de una obra o proyecto específico.
- **Termina:** al concluir la obra.

### Pasantía / práctica profesional

- **Para quién:** estudiantes o recién graduados, vinculada a un programa formativo.
- **Requisito:** convenio con el centro educativo y contenido formativo real; si no, hay riesgo de relación laboral encubierta.

## Régimen laboral aplicable

| Situación de la empresa | Régimen aplicable | Notas |
|---|---|---|
| Empresa ordinaria en Panamá | Código de Trabajo de Panamá | Régimen general; MITRADEL como autoridad laboral |
| Empresa en régimen SEM | Normas laborales especiales del régimen SEM [verificar] | Algunas reglas migratorias y de personal extranjero son específicas |
| Empresa en Panamá Pacífico | Régimen laboral especial de la zona [verificar] | Flexibilidad en ciertas materias [verificar] |
| Empresa en Ciudad del Saber | Código de Trabajo con facilidades migratorias para personal extranjero [verificar] | |

**Importante:** el salario mínimo se fija por decreto según región y actividad — verificar el salario mínimo vigente aplicable [verificar].

## Coste real de un empleado

| Concepto | Cálculo orientativo |
|---|---|
| Salario bruto anual | [SBA] |
| Cuota patronal CSS (Caja de Seguro Social) | SBA x ~12.25% [verificar porcentaje vigente] |
| Seguro Educativo (cuota patronal) | SBA x 1.5% [verificar] |
| Riesgos profesionales (CSS) | Según actividad [verificar] |
| Décimo tercer mes | 1 mes adicional repartido en 3 partidas (abril, agosto, diciembre) [verificar] |
| **Coste total empresa** | **SBA + cuotas patronales + décimo tercer mes** |

### Ejemplo: desarrollador junior (Ciudad de Panamá)

| Concepto | Importe orientativo [verificar] |
|---|---|
| Salario bruto mensual | USD 1,200-2,000 |
| Cuota patronal CSS + seguro educativo (~13.75%) | proporcional |
| Décimo tercer mes | 1 salario adicional al año |
| Coste total empresa | salario + cuotas patronales + décimo |

**Nota:** los porcentajes de CSS y seguro educativo cambian — verificar las tasas patronales vigentes.

## Alternativas al contrato laboral

### Contratista independiente

| Ventaja | Riesgo |
|---|---|
| Sin cuota patronal CSS | **Relación laboral encubierta** — si hay subordinación y dependencia económica, es relación laboral y aplica el Código de Trabajo |
| Flexibilidad | Reclasificación: el trabajador puede reclamar prestaciones laborales, cuotas CSS retroactivas y sanciones de MITRADEL |
| Factura por servicios | El contratista puede reclamar laboralidad en cualquier momento |

**Indicios de relación laboral encubierta (Código de Trabajo y criterio de MITRADEL):**
- Horario fijo impuesto por la empresa.
- Uso de medios de la empresa (equipo, oficina, correo corporativo).
- Integración en la estructura organizativa.
- Un solo cliente (la empresa) y dependencia económica.
- Subordinación jurídica (recibe órdenes e instrucciones).

### Pasante / practicante

| Requisito | Detalle |
|---|---|
| Convenio con centro educativo | Recomendable — sin programa formativo real hay riesgo de laboralidad |
| Vinculación a formación | El programa debe tener contenido formativo real |
| Tutor en la empresa | Recomendable |
| Estipendio | No siempre obligatorio, pero habitual [verificar] |

**Riesgo:** si no hay contenido formativo real y el pasante hace trabajo ordinario, es relación laboral encubierta.

## Formato de salida

```markdown
BORRADOR — GUÍA DE CONTRATACIÓN — REVISIÓN LABORAL OBLIGATORIA

> **Nota para el revisor**
> - **Perfiles analizados:** [N]
> - **Régimen laboral identificado:** [Código de Trabajo / régimen especial de zona]
> - **Elementos marcados [verificar]:** [N — salarios, cuotas CSS y costes pueden haber cambiado]
> - **Antes de actuar:** verificar régimen laboral aplicable; comprobar tasas vigentes de CSS y seguro educativo; confirmar salario mínimo aplicable; inscribir a la empresa como patrono en la CSS; consultar con asesor laboral.

## Guía de contratación: [Nombre de la empresa]

### Recomendación por perfil

| Perfil | Tipo recomendado | Coste estimado/año (USD) | Observaciones |
|---|---|---|---|
| [perfil] | [tipo contrato] | [coste] | [notas] |

### Régimen laboral aplicable

**[Código de Trabajo / régimen especial]** — categorías, salario mínimo aplicable, jornada (44 horas semanales [verificar]).

### Coste detallado

[Tabla con desglose por perfil, incluyendo cuotas patronales CSS y décimo tercer mes]

### Riesgos identificados

[Relación laboral encubierta, contratos por tiempo definido sin causa, etc.]

---

**Qué hacer a continuación:**
1. **Redactar contrato** — preparo borrador de contrato laboral conforme al Código de Trabajo.
2. **Inscripción patronal en CSS** — checklist de trámites de alta.
3. **Stock options** — `/startups:stock-options` para plan de incentivos del equipo.
4. **Plan de coste a 12 meses** — proyección de coste de plantilla en USD.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Código de Trabajo de Panamá** — relación laboral, tipos de contrato, despido, prestaciones.
- **Ley de la Caja de Seguro Social (CSS)** — cuotas obrero-patronales [verificar].
- **Ley del décimo tercer mes** — Ley 15 de 1971 [verificar].
- **Ley 126 de 2020** — teletrabajo.
- **Decreto de salario mínimo vigente [verificar]** — MITRADEL.

## Guardarraíles

- **El riesgo de relación laboral encubierta es real y costoso.** MITRADEL puede reclasificar al contratista; no recomendar contratistas independientes cuando hay subordinación y dependencia económica.
- **El contrato por tiempo definido tiene límites.** No recomendar contratos por tiempo definido para labores permanentes — se presume indefinido.
- **El décimo tercer mes es obligatorio.** Es un coste adicional que muchos fundadores olvidan presupuestar.
- **Las cuotas de CSS y seguro educativo cambian.** Marcar `[verificar]` en todo porcentaje y cifra de cotización.
- **Inscripción patronal en la CSS antes de contratar.** No es opcional; contratar sin inscribir genera multas y responsabilidad.
- **El salario mínimo se fija por decreto y varía por región y actividad.** No pagar por debajo del mínimo aplicable aunque el trabajador acepte.
- **Siempre derivar a asesor laboral para la formalización.** Un contrato mal hecho puede ser más costoso que el ahorro de no pagar asesoramiento.
