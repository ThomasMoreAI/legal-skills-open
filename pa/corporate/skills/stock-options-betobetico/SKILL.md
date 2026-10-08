---
name: stock-options-betobetico
title: /stock-options
description: 'Estructura un plan de incentivos de equity: stock options (opciones sobre acciones) y phantom shares (derechos económicos). Incluye régimen fiscal panameño (ISR, principio de territorialidad), vesting, cliff, good/bad leaver. Usar cuando el usuario dice "stock options", "phantom shares", "plan de incentivos", "equity para empleados", "opciones sobre acciones", o quiere retener talento con equity.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/startups/skills/stock-options
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

# /stock-options

1. Leer `~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md` — perfil de práctica.
2. Determinar el tipo de plan más adecuado.
3. Estructurar el plan con sus cláusulas esenciales.
4. Analizar el tratamiento fiscal.
5. Producir el borrador del plan.

---

## Propósito

Estructurar un plan de incentivos basado en equity que sea legal, fiscalmente eficiente y alineado con los intereses de la empresa y los beneficiarios. El plan es un borrador — requiere revisión letrada y fiscal.

## Tipos de planes

### Stock options (opciones sobre acciones)

- **Qué son:** derecho a adquirir acciones de la sociedad a un precio fijado (strike price) en el futuro.
- **Ventaja:** alineación real de intereses — el beneficiario se convierte en accionista.
- **Complejidad:** requiere emisión de nuevas acciones (dentro del capital autorizado o mediante aumento), eventual modificación del pacto social.
- **Riesgo:** dilución de los accionistas existentes.

### Phantom shares (derechos económicos)

- **Qué son:** derecho a recibir un pago equivalente al valor de un número determinado de acciones en un evento de liquidez.
- **Ventaja:** no requiere emisión de acciones ni entrada en el capital social. El beneficiario no es accionista.
- **Complejidad:** menor — es un contrato privado.
- **Limitación:** no hay derechos políticos (voto, información).

### SAR (Stock Appreciation Rights)

- Similar a phantom shares — derecho al incremento de valor, no al valor total.

## Estructura del plan

### Términos esenciales

| Término | Definición | Rango habitual |
|---|---|---|
| Pool | Porcentaje total reservado para incentivos | 10-15% del capital |
| Strike price | Precio de ejercicio de las opciones | Valor de la acción al momento de la concesión |
| Vesting | Periodo de consolidación del derecho | 4 años |
| Cliff | Periodo mínimo antes de consolidar nada | 1 año (consolida 25% al cumplir el cliff) |
| Vesting mensual post-cliff | Consolidación gradual tras el cliff | 1/48 mensual |
| Ventana de ejercicio | Plazo para ejercer las opciones tras consolidar | 90 días tras salida (variable) |
| Good leaver | Salida voluntaria o involuntaria sin causa | Conserva opciones consolidadas |
| Bad leaver | Salida por incumplimiento grave o competencia desleal | Pierde todas las opciones (consolidadas y no consolidadas) |
| Evento de liquidez | Cuándo se pueden hacer efectivas | Venta de la empresa, salida a bolsa, ronda secundaria |
| Aceleración | Consolidación anticipada ante un evento | Single/double trigger en caso de venta de la empresa |

### Cláusulas del acuerdo individual

| Cláusula | Contenido |
|---|---|
| Partes | La empresa y el beneficiario |
| Tipo de plan | Stock options / phantom shares / SAR |
| N.o de opciones/phantoms | Cantidad asignada |
| Strike price | Precio de ejercicio (o N/A para phantoms) |
| Calendario de vesting | Cliff + vesting mensual |
| Condiciones de ejercicio | Evento de liquidez, ventana de ejercicio |
| Good/bad leaver | Definición y consecuencias |
| No transmisibilidad | Las opciones no se pueden ceder |
| Fiscalidad | Información sobre tributación |
| Confidencialidad | Sobre la existencia y términos del plan |

## Tratamiento fiscal

### Stock options — Régimen general (ISR, Código Fiscal)

- **Momento de tributación:** según la legislación panameña, cuando se materializa el beneficio para el trabajador [verificar momento exacto].
- **Calificación:** remuneración del trabajo (diferencia entre valor de mercado y strike price) sujeta a ISR si es renta de fuente panameña.
- **Retención:** la empresa, como agente de retención, debe practicar la retención de ISR que corresponda [verificar].
- **Principio de territorialidad:** solo tributan en Panamá las rentas de fuente panameña; el trabajo prestado en el exterior puede quedar fuera del ISR panameño [verificar].

### Stock options — Consideraciones para startups en Panamá

| Aspecto | Detalle |
|---|---|
| No hay régimen especial tipo "Ley de Startups" | A diferencia de otras jurisdicciones, no existe una exención específica para stock options de empresas emergentes [verificar] |
| Estructura del plan | Conviene documentar el plan y los acuerdos individuales con asesoría fiscal para determinar el momento y la base de tributación |
| Regímenes especiales | Si la empresa opera bajo SEM, Ciudad del Saber o Panamá Pacífico, revisar el tratamiento específico de remuneraciones del personal en esos regímenes [verificar] |
| CSS | La remuneración en especie puede tener implicaciones de cuotas a la Caja de Seguro Social [verificar] |

### Phantom shares — Régimen fiscal

- **Momento de tributación:** cuando se cobra el pago.
- **Calificación:** remuneración del trabajo sujeta a ISR (si es renta de fuente panameña).
- **Retención:** la empresa practica la retención de ISR que corresponda.
- **No hay beneficio fiscal especial** — tributan como remuneración.

## Formato de salida

```markdown
BORRADOR — PLAN DE INCENTIVOS — REVISIÓN LETRADA Y FISCAL OBLIGATORIA

> **Nota para el revisor**
> - **Tipo de plan:** [stock options / phantom shares / mixto]
> - **Régimen fiscal aplicado:** [general ISR — verificar momento de tributación y territorialidad]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** revisar con asesor fiscal panameño; revisar con abogado mercantilista; verificar implicaciones de CSS; adaptar al pacto social de la sociedad.

## Plan de incentivos: [Nombre de la empresa]

### Resumen del plan

| Parámetro | Valor |
|---|---|
| Tipo | [stock options / phantom shares] |
| Pool total | [%] |
| Vesting | [periodo] |
| Cliff | [periodo] |
| Beneficiarios | [N] |
| Régimen fiscal | [ISR general / régimen especial de zona] |

### Estructura del plan

[Documento completo del plan con todas las cláusulas]

### Modelo de acuerdo individual

[Borrador de acuerdo individual para un beneficiario]

### Simulación fiscal

| Escenario | Valor opciones | Tributación (ISR) | Neto beneficiario |
|---|---|---|---|
| Renta de fuente panameña | [valor] | [impuestos] | [neto] |
| Renta de fuente extranjera (territorialidad) | [valor] | [impuestos] | [neto] |

---

**Qué hacer a continuación:**
1. **Adaptar acuerdo individual** — personalizo para cada beneficiario.
2. **Verificar régimen de zona** — comprobar si la empresa opera bajo SEM, Ciudad del Saber o Panamá Pacífico.
3. **Pacto de accionistas** — alinear el plan con el pacto de accionistas existente.
4. **Ronda de inversión** — `/startups:ronda` para asegurar que el plan es compatible con la ronda.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Código Fiscal de Panamá** — Impuesto sobre la Renta (ISR); principio de territorialidad [verificar].
- **Ley 32 de 1927** — sociedades anónimas (emisión de acciones).
- **Código de Trabajo de Panamá** — remuneración del trabajo y régimen del trabajador [verificar].
- **Normativa de la CSS** — cuotas sobre remuneraciones en especie [verificar].

## Guardarraíles

- **No existe un régimen panameño de exención de stock options tipo "Ley de Startups".** No prometer exenciones que no estén en la legislación — verificar siempre el tratamiento con asesor fiscal.
- **Las stock options requieren emitir acciones.** Hay que prever en el pacto social y en el pacto de accionistas la reserva del pool. Los inversionistas suelen negociar quién soporta la dilución.
- **La valoración de las acciones es clave y conflictiva.** El strike price debe reflejar el valor de mercado — una valoración artificialmente baja puede ser cuestionada por la DGI.
- **No confundir consolidación (vesting) con ejercicio.** Las opciones se consolidan con el vesting pero solo se pueden ejercer en los eventos previstos.
- **Phantom shares tributan como remuneración.** No hay ventaja fiscal — solo ventaja de simplicidad jurídica. No vender las phantoms como "fiscalmente eficientes".
- **Siempre coordinar con asesor fiscal.** La tributación de estos instrumentos bajo el ISR panameño y el principio de territorialidad es compleja — verificar cada caso.
