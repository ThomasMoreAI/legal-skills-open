---
name: incentivos-4037-betobetico
title: /incentivos
description: 'Mapea los incentivos fiscales disponibles para startups y empresas de base tecnológica en España: Ley de Startups (Ley 28/2022), deducciones por I+D+i (art. 35 LIS), patent box (art. 23 LIS), deducción por inversión en empresa nueva (art. 68.1 LIRPF). Genera una tabla de incentivos aplicables con requisitos y beneficio estimado. Usar cuando el usuario dice "incentivos fiscales", "Ley de Startups", "deducciones I+D", "patent box", "beneficios fiscales para startups", o quiere optimizar la carga fiscal de su empresa.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/incentivos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

# /incentivos

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de la empresa.
3. Evaluar cada incentivo aplicable.
4. Producir la tabla de incentivos con requisitos y beneficio.

---

## Propósito

Identificar todos los incentivos fiscales aplicables a una startup o empresa innovadora en España, verificar el cumplimiento de requisitos y estimar el beneficio fiscal. Es una herramienta de orientación — la aplicación concreta requiere asesor fiscal.

## Incentivos disponibles

### 1. Ley de Startups (Ley 28/2022) — Empresa emergente

| Beneficio | Detalle | Requisito |
|---|---|---|
| Tipo reducido IS | 15% (en lugar del 25%) durante los primeros 4 ejercicios con base imponible positiva | Certificación ENISA como empresa emergente |
| Diferimiento stock options | Tributación diferida al momento de venta (no al ejercicio) | Empleados de empresa emergente certificada |
| Exención stock options | Hasta 50.000 EUR/año exentos como rendimiento en especie [verificar importe vigente] | Plan ofrecido en condiciones generales |
| Autónomos con pluriactividad | Compatibilidad del trabajo por cuenta ajena con la actividad emprendedora | Alta en RETA + trabajo por cuenta ajena |
| Nómadas digitales | Régimen especial IRNR para trabajadores desplazados | Requisitos del art. 93 LIRPF reformado |

**Requisitos para ser empresa emergente (art. 3 Ley 28/2022):**

- Creada en los últimos 5 años (7 en biotech, energía, industriales).
- No cotizada ni distribuir dividendos.
- Sede social o establecimiento permanente en España.
- El 60% de la plantilla con contrato laboral en España.
- Proyecto innovador y escalable (certificado por ENISA).
- Facturación anual < 10 M EUR.
- No surgida de concentración empresarial.

### 2. Deducción por I+D+i (art. 35 LIS)

| Concepto | Deducción | Límite |
|---|---|---|
| Investigación y desarrollo (I+D) | 25% de gastos del ejercicio (42% si superan la media de los 2 años anteriores) | Cuota del IS |
| Gastos de personal investigador | 17% adicional | Acumulable |
| Innovación tecnológica (IT) | 12% de gastos | Cuota del IS |
| Monetización (art. 39.2 LIS) | Si no se puede aplicar por insuficiencia de cuota, se puede solicitar el abono (con descuento del 20%) | 1 M EUR/año para I+D, 1 M EUR para IT |

**Diferencia I+D vs. IT:**
- **I+D:** avance significativo en el campo científico o tecnológico (novedad objetiva).
- **IT:** avance para la empresa, aunque ya exista en el mercado (novedad subjetiva).

### 3. Patent box (art. 23 LIS)

| Concepto | Beneficio |
|---|---|
| Activos intangibles cedidos | Reducción del 60% de la renta neta procedente de la cesión |
| Activos: patentes, modelos de utilidad, know-how registrado, software registrado | |
| Requisito: que el cedente haya creado al menos el 25% del intangible | |

### 4. Deducción por inversión en empresa nueva (art. 68.1 LIRPF)

| Concepto | Beneficio |
|---|---|
| Deducción para el inversor (business angel) | 50% de la inversión en empresa nueva [verificar] |
| Base máxima de deducción | 100.000 EUR/año [verificar] |
| Requisitos: empresa de nueva creación, participación < 40%, mantener 3-12 años | |
| Mejora Ley de Startups: 50% (vs. 30% anterior) y 100.000 EUR (vs. 60.000 EUR anterior) | |

### 5. Otros incentivos

| Incentivo | Descripción | Ref |
|---|---|---|
| Bonificaciones en cuotas SS | Bonificaciones para empresas innovadoras que contratan personal investigador | RD 475/2014 |
| ZEC (Zona Especial Canarias) | Tipo IS del 4% para empresas en Canarias que cumplan requisitos | Ley 19/1994 |
| Reserva para inversiones en Canarias (RIC) | Reducción en base imponible por reinversión | Ley 19/1994 |
| Deducciones autonómicas IRPF | Varias CCAA tienen deducciones por inversión en startups | Variable por CCAA |

## Formato de salida

```markdown
BORRADOR — MAPA DE INCENTIVOS FISCALES — REVISIÓN FISCAL OBLIGATORIA

> **Nota para el revisor**
> - **Datos de la empresa:** [resumen]
> - **Incentivos evaluados:** [N]
> - **Elementos marcados [verificar]:** [N — especialmente importes y porcentajes que pueden haber cambiado]
> - **Antes de actuar:** verificar requisitos con asesor fiscal; comprobar vigencia de cada incentivo; solicitar informes vinculantes de la DGT si hay duda; certificar en ENISA si procede.

## Incentivos fiscales: [Nombre de la empresa]

### Resumen

| Incentivo | Aplicable | Beneficio estimado | Requisito pendiente |
|---|---|---|---|
| Ley de Startups (tipo IS 15%) | [sí/no/potencial] | [ahorro] | [requisito] |
| Stock options Ley de Startups | [sí/no/potencial] | [ahorro] | [requisito] |
| I+D+i (art. 35 LIS) | [sí/no/potencial] | [deducción] | [requisito] |
| Patent box (art. 23 LIS) | [sí/no/potencial] | [reducción] | [requisito] |
| Business angel (art. 68.1 LIRPF) | [sí/no/potencial] | [deducción inversores] | [requisito] |

### Análisis detallado por incentivo

[Para cada incentivo aplicable: requisitos, estado de cumplimiento, pasos para acceder, beneficio estimado]

### Plan de acción

| Acción | Responsable | Plazo | Prioridad |
|---|---|---|---|
| [acción] | [quién] | [cuándo] | [alta/media/baja] |

---

**Qué hacer a continuación:**
1. **Solicitar certificación ENISA** — si procede, preparo la documentación.
2. **Informe motivado I+D+i** — solicitar al CDTI para blindar la deducción.
3. **Plan de stock options** — `/startups:stock-options` optimizado fiscalmente.
4. **Consulta vinculante DGT** — si hay duda sobre la aplicación de algún incentivo.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 28/2022** — Ley de fomento del ecosistema de las empresas emergentes.
- **LIS (Ley 27/2014) art. 35** — deducciones por I+D+i.
- **LIS art. 23** — reducción por cesión de intangibles (patent box).
- **LIS art. 39.2** — monetización de deducciones I+D+i.
- **LIRPF (Ley 35/2006) art. 68.1** — deducción por inversión en empresa nueva.

## Guardarraíles

- **Los importes y porcentajes fiscales cambian.** Marcar `[verificar]` en toda cifra concreta — las reformas fiscales son frecuentes.
- **La certificación ENISA es requisito previo para los beneficios de la Ley de Startups.** Sin ella, no aplica ningún beneficio.
- **El informe motivado del CDTI blinda la deducción por I+D+i.** Sin él, Hacienda puede cuestionar la calificación como I+D o IT.
- **No confundir I+D con IT.** La deducción es diferente y los requisitos también. No todo desarrollo de software es I+D.
- **Patent box requiere que el intangible esté registrado.** Un know-how no registrado no accede al beneficio.
- **Siempre derivar a asesor fiscal.** La aplicación de incentivos fiscales requiere planificación fiscal profesional. Un error puede suponer devolución del incentivo + intereses + sanción.
