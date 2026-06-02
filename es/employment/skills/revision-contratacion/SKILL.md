---
name: revision-contratacion
title: Propósito
description: Revisa contratos de trabajo verificando cláusulas obligatorias y adecuación al tipo contractual
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/revision-contratacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

## Propósito

Esta skill revisa un contrato de trabajo individual, verifica que contiene todas las cláusulas obligatorias según el ET y la normativa aplicable, y comprueba que el tipo contractual elegido se ajusta a la situación descrita.

## Instrucciones

### Paso 1 — Identificar tipo de contrato

1. **Indefinido ordinario**: contrato por defecto (art. 15.1 ET).
2. **Fijo-discontinuo** (art. 16 ET): trabajos estacionales o vinculados a contratas.
3. **Temporal por circunstancias de la producción** (art. 15.2 ET): incremento ocasional e imprevisible, máx. 6 meses (ampliable a 12 por convenio).
4. **Temporal por sustitución** (art. 15.3 ET): sustitución de persona trabajadora con reserva de puesto.
5. **Contrato formativo para la obtención de práctica profesional** (art. 11.3 ET).
6. **Contrato de formación en alternancia** (art. 11.2 ET).

### Paso 2 — Verificar cláusulas obligatorias

Comprobar la presencia y corrección de:

| Cláusula | Base legal | Verificación |
|----------|------------|--------------|
| Identidad de las partes | Art. 8.5 ET, RD 1659/1998 | Datos completos |
| Fecha de inicio y duración | Art. 15 ET | Coherente con tipo |
| Domicilio de la empresa y centro de trabajo | RD 1659/1998 | Presente |
| Categoría o grupo profesional | Art. 22 ET | Conforme a convenio |
| Salario base y complementos | Art. 26 ET | ≥ SMI y convenio |
| Jornada y horario | Art. 34 ET | ≤ 40h/semana media anual |
| Vacaciones | Art. 38 ET | ≥ 30 días naturales |
| Período de prueba | Art. 14 ET | Dentro de límites legales/convenio |
| Convenio colectivo aplicable | Art. 2 RD 1659/1998 | Identificado |
| Plazo de preaviso para extinción | Convenio aplicable | Conforme |

### Paso 3 — Revisar cláusulas especiales

- **No competencia postcontractual** (art. 21.2 ET): máx. 2 años (técnicos), máx. 6 meses (resto); requiere compensación económica adecuada e interés industrial/comercial.
- **Permanencia** (art. 21.4 ET): máx. 2 años, requiere formación especializada a cargo del empresario.
- **Exclusividad** (art. 21.1 ET): plena dedicación con compensación económica.
- **Confidencialidad**: proporcionalidad y duración.
- **Teletrabajo**: si > 30% de jornada, requiere acuerdo individual (Ley 10/2021).

### Paso 4 — Verificar adecuación del tipo contractual

- El temporal tiene causa real y vigente.
- La duración se ajusta a los máximos legales.
- No hay indicios de uso fraudulento de la temporalidad (cadena de contratos, art. 15.5 ET).

## Formato de salida

```markdown
## Revisión de contrato de trabajo

**Tipo contractual:** [tipo]
**Trabajador:** [nombre]
**Puesto:** [denominación]
**Convenio aplicable:** [nombre del convenio]

### Verificación de cláusulas obligatorias

| Cláusula | Presente | Conforme | Observaciones |
|----------|----------|----------|---------------|
| [nombre] | [SÍ/NO] | [SÍ/NO/N/A] | [detalle] |

### Cláusulas especiales

| Cláusula | Presente | Validez | Riesgos |
|----------|----------|---------|---------|
| No competencia | [SÍ/NO] | [válida/dudosa/nula] | [detalle] |

### Adecuación del tipo contractual

[Valoración de si el tipo contractual es correcto para la situación descrita]

### Riesgos detectados

| Riesgo | Severidad | Consecuencia | Recomendación |
|--------|-----------|--------------|---------------|
| [riesgo] | [nivel] | [qué puede pasar] | [qué hacer] |
```

## Referencias normativas

- **ET arts. 8-21**: Forma, duración y modalidades del contrato.
- **ET art. 14**: Período de prueba.
- **ET art. 15**: Duración del contrato — reforma por RDL 32/2021.
- **ET art. 16**: Contrato fijo-discontinuo.
- **ET art. 21**: Pactos de no competencia, permanencia, exclusividad.
- **RD 1659/1998**: Información al trabajador sobre condiciones del contrato.
- **RD 1060/2022**: Tipos de contratos formativos.
- **Ley 10/2021**: Trabajo a distancia.

## Guardrails

- **NO** redacta contratos de trabajo — solo revisa los existentes.
- **NO** determina el convenio colectivo aplicable con certeza — sugiere el probable.
- **NO** calcula nóminas ni cotizaciones a la Seguridad Social.
- **ESCALAR** si el contrato temporal carece de causa o supera la duración máxima legal.
- **ESCALAR** si la cláusula de no competencia carece de compensación económica.
- **AVISAR** si no se identifica el convenio colectivo aplicable para verificar límites.
