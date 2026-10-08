---
name: fundacion-interes-privado-betobetico
title: Propósito
description: Asiste en la constitución, estructura y cumplimiento de fundaciones de interés privado conforme a la Ley 25 de 1995
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/fundacion-interes-privado
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: contracts
language: es
---

## Propósito

Esta skill asiste en el ciclo de vida de las fundaciones de interés privado panameñas (Ley 25 de 1995): constitución (acta fundacional / carta fundacional), definición de órganos (fundador, Consejo de Fundación, protector), beneficiarios, patrimonio y reglamentos, así como en el seguimiento de las obligaciones de mantenimiento. Es la figura típica de planificación patrimonial y sucesoria en Panamá, sin accionistas y con fines no lucrativos.

## Instrucciones

### Paso 1 — Identificar la acción

Determinar qué se solicita:

1. **Constituir**: preparar el borrador del acta fundacional y los elementos necesarios.
2. **Revisar**: analizar un acta fundacional o reglamento existente y detectar incidencias.
3. **Cumplimiento**: verificar el estado de las obligaciones de mantenimiento de la fundación.

### Paso 2 — Recopilar datos necesarios

Solicitar al usuario los datos según la acción:

- **Fundador**: nombre, cédula / pasaporte; puede ser persona natural o jurídica.
- **Nombre de la fundación**: debe incluir la palabra "Fundación" y no ser igual o similar al de otra preexistente (art. 5, numeral 1, Ley 25 de 1995).
- **Patrimonio inicial**: mínimo de USD 10.000 (B/. 10.000), expresable en cualquier moneda (art. 5, numeral 2, Ley 25 de 1995).
- **Domicilio** en Panamá y **agente residente** (abogado o firma de abogados en Panamá) (art. 5, numerales 4 y 5, Ley 25 de 1995).
- **Consejo de Fundación**: miembros (mínimo 3 si son personas naturales, o 1 si es persona jurídica) (art. 17, Ley 25 de 1995).
- **Beneficiarios**: identificación o forma de determinarlos (a menudo en reglamento privado).
- **Protector** (opcional): facultades de supervisión.
- **Objeto / fines**: no lucrativos; pueden incluir manutención y educación de beneficiarios.

### Paso 3 — Verificar requisitos legales

Comprobar conforme a la Ley 25 de 1995:

- **Patrimonio mínimo** de B/. 10.000 afectado a los fines de la fundación (art. 5, numeral 2, Ley 25 de 1995).
- **Acta fundacional**: puede otorgarse por documento privado con firma del fundador autenticada por notario o directamente ante notario (escritura pública) — la escritura pública no es la única vía (art. 4, Ley 25 de 1995). La **inscripción en el Registro Público confiere la personalidad jurídica** (art. 9, Ley 25 de 1995).
- **Órganos**: Consejo de Fundación válidamente designado (art. 17, Ley 25 de 1995).
- **Reglamento**: documento privado que regula beneficiarios y distribución (no necesariamente inscrito).
- **Agente residente** vigente.
- **Beneficiario final**: cumplimiento del registro de beneficiarios finales (Ley 129 de 2020, administrada por la SSNF; Decreto Ejecutivo 13 de 2022) y de la debida diligencia de la Ley 23 de 2015 (si la fundación es sujeto obligado o si interviene su agente residente).

### Paso 4 — Generar el documento o informe

Según la acción, redactar el borrador del acta fundacional, el informe de revisión o el calendario de cumplimiento.

## Formato de salida

```markdown
## Fundación de interés privado — [Acción]

**Fundación:** [nombre completo]
**Fundador:** [nombre]
**Patrimonio inicial:** [importe en USD / B/.]
**Agente residente:** [nombre]
**Fecha:** [fecha]

---

### Estructura

| Elemento | Detalle | Estado / Referencia |
|----------|---------|---------------------|
| Consejo de Fundación | [miembros] | Ley 25 de 1995, art. 17 |
| Protector | [nombre / no designado] | [opcional] |
| Beneficiarios | [identificación / reglamento] | [privado] |
| Reglamento | [sí / no] | [privado] |

### Obligaciones de mantenimiento

| Obligación | Plazo | Estado | Base legal |
|------------|-------|--------|------------|
| Tasa única anual | Anual (B/. 400.00) | [estado] | Código Fiscal, art. 318-A |
| Agente residente | Continuo | [estado] | Ley 25 de 1995, art. 5.5 |
| Libros / registros contables | Permanente | [estado] | Ley 52 de 2016 (ref. Ley 254 de 2021) |
| Beneficiario final | Según Ley 129 de 2020 | [estado] | Ley 129 de 2020 / Ley 23 de 2015 |

### Incidencias / Acciones recomendadas

[Lista de incidencias detectadas o acciones pendientes]
```

## Referencias normativas

- **Ley 25 de 1995**: sobre fundaciones de interés privado — constitución (arts. 4 y 9), nombre y patrimonio (art. 5), órganos (art. 17) y régimen sucesorio (art. 14). Esta ley **excluye expresamente la aplicación del Título II del Libro I del Código Civil** (art. 2), por lo que dicho código no se aplica supletoriamente en esa materia. En materia sucesoria, las disposiciones de la fundación **prevalecen sobre las legítimas hereditarias** (art. 14).
- **Ley 52 de 2016 (reformada por la Ley 254 de 2021)**: obligación de llevar registros contables y documentación de soporte de las fundaciones (no deriva del Código de Comercio).
- **Código Fiscal, art. 318-A**: tasa única anual de las fundaciones, B/. 400.00 anuales (verificar tarifa vigente con la DGI).
- **Ley 129 de 2020**: Sistema Privado y Único de Registro de Beneficiarios Finales de las Personas Jurídicas, administrado por la Superintendencia de Sujetos No Financieros (SSNF), reglamentada por el Decreto Ejecutivo 13 de 2022; el agente residente es el obligado a reportar.
- **Ley 23 de 2015**: prevención de blanqueo de capitales — debida diligencia y conocimiento del cliente y del beneficiario final por los sujetos obligados (incl. agentes residentes); UAF.

## Guardrails

- **NO** constituye ni inscribe la fundación ante el Registro Público — solo prepara borradores.
- **NO** asesora sobre la fiscalidad internacional del fundador o de los beneficiarios — escalar a fiscalista.
- **NO** certifica la validez del acta fundacional — requiere revisión del abogado idóneo y del notario.
- **NO** sustituye el reglamento privado, que debe redactarse según la voluntad del fundador.
- **ESCALAR** si la estructura busca eludir normas imperativas de sucesiones o de acreedores.
- **ESCALAR** si hay indicios de uso para blanqueo de capitales o evasión fiscal (Ley 23 de 2015).
- **AVISAR** si faltan datos esenciales (fundador, patrimonio, Consejo de Fundación o agente residente).
