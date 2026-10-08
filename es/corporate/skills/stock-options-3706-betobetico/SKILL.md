---
name: stock-options-3706-betobetico
title: /stock-options
description: 'Estructura un plan de incentivos de equity: stock options (opciones sobre participaciones) y phantom shares (derechos económicos). Incluye régimen fiscal con la Ley de Startups (Ley 28/2022), vesting, cliff, good/bad leaver. Usar cuando el usuario dice "stock options", "phantom shares", "plan de incentivos", "equity para empleados", "opciones sobre participaciones", o quiere retener talento con equity.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/startups/skills/stock-options
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
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

### Stock options (opciones sobre participaciones)

- **Qué son:** derecho a adquirir participaciones de la sociedad a un precio fijado (strike price) en el futuro.
- **Ventaja:** alineación real de intereses — el beneficiario se convierte en socio.
- **Complejidad:** requiere ampliación de capital, modificación de estatutos, posibles problemas con derecho de suscripción preferente.
- **Riesgo:** dilución de los socios existentes.

### Phantom shares (derechos económicos)

- **Qué son:** derecho a recibir un pago equivalente al valor de un número determinado de participaciones en un evento de liquidez.
- **Ventaja:** no requiere ampliación de capital ni entrada en el capital social. El beneficiario no es socio.
- **Complejidad:** menor — es un contrato privado.
- **Limitación:** no hay derechos políticos (voto, información).

### SAR (Stock Appreciation Rights)

- Similar a phantom shares — derecho al incremento de valor, no al valor total.

## Estructura del plan

### Términos esenciales

| Término | Definición | Rango habitual |
|---|---|---|
| Pool | Porcentaje total reservado para incentivos | 10-15% del capital |
| Strike price | Precio de ejercicio de las opciones | Valor de la participación al momento de la concesión |
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

### Stock options — Régimen general (LIRPF art. 17)

- **Momento de tributación:** cuando se ejercen las opciones (adquisición de participaciones).
- **Calificación:** rendimiento del trabajo (diferencia entre valor de mercado y strike price).
- **Retención:** la empresa debe practicar retención a cuenta.
- **Tipo marginal:** hasta el 47% (según CCAA y tramo de renta).

### Stock options — Régimen Ley de Startups (Ley 28/2022 art. 13)

| Requisito | Detalle |
|---|---|
| Empresa emergente certificada por ENISA | Obligatorio |
| Exención | Hasta 50.000 EUR/año de rendimiento del trabajo en especie [verificar] |
| Diferimiento | La tributación se difiere al momento de la venta de las participaciones (no al ejercicio) |
| Plazo máximo de diferimiento | 10 años desde la entrega de las participaciones |
| Oferta generalizada | Si el plan se ofrece a todos los trabajadores en las mismas condiciones, la exención aplica sin límite |

### Phantom shares — Régimen fiscal

- **Momento de tributación:** cuando se cobra el pago.
- **Calificación:** rendimiento del trabajo.
- **Retención:** la empresa practica retención.
- **No hay beneficio fiscal especial** — tributan como nómina.

## Formato de salida

```markdown
BORRADOR — PLAN DE INCENTIVOS — REVISIÓN LETRADA Y FISCAL OBLIGATORIA

> **Nota para el revisor**
> - **Tipo de plan:** [stock options / phantom shares / mixto]
> - **Régimen fiscal aplicado:** [general / Ley de Startups — verificar requisitos ENISA]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar certificación ENISA si se aplica Ley de Startups; revisar con asesor fiscal; revisar con letrado mercantilista; adaptar a los estatutos de la sociedad.

## Plan de incentivos: [Nombre de la empresa]

### Resumen del plan

| Parámetro | Valor |
|---|---|
| Tipo | [stock options / phantom shares] |
| Pool total | [%] |
| Vesting | [periodo] |
| Cliff | [periodo] |
| Beneficiarios | [N] |
| Régimen fiscal | [general / Ley de Startups] |

### Estructura del plan

[Documento completo del plan con todas las cláusulas]

### Modelo de acuerdo individual

[Borrador de acuerdo individual para un beneficiario]

### Simulación fiscal

| Escenario | Valor opciones | Tributación | Neto beneficiario |
|---|---|---|---|
| Régimen general | [valor] | [impuestos] | [neto] |
| Ley de Startups (si aplica) | [valor] | [impuestos] | [neto] |

---

**Qué hacer a continuación:**
1. **Adaptar acuerdo individual** — personalizo para cada beneficiario.
2. **Verificar ENISA** — comprobar si la empresa tiene certificación de empresa emergente.
3. **Pacto de socios** — alinear el plan con el pacto de socios existente.
4. **Ronda de inversión** — `/startups:ronda` para asegurar que el plan es compatible con la ronda.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 28/2022** — Ley de fomento del ecosistema de las empresas emergentes (Ley de Startups), art. 13.
- **LIRPF (Ley 35/2006) arts. 17 y 42** — rendimientos del trabajo en especie.
- **LSC arts. 295-316** — ampliación de capital.
- **LSC art. 304** — derecho de suscripción preferente.

## Guardarraíles

- **El régimen de la Ley de Startups solo aplica a empresas con certificación ENISA.** No darlo por hecho — verificar siempre.
- **Las stock options requieren ampliación de capital.** Hay que prever en los estatutos y en el pacto de socios la reserva del pool. Los inversores suelen negociar quién soporta la dilución.
- **La valoración de las participaciones es clave y conflictiva.** El strike price debe reflejar el valor de mercado — una valoración artificialmente baja puede ser cuestionada por Hacienda.
- **No confundir consolidación (vesting) con ejercicio.** Las opciones se consolidan con el vesting pero solo se pueden ejercer en los eventos previstos.
- **Phantom shares tributan como nómina.** No hay ventaja fiscal — solo ventaja de simplicidad jurídica. No vender las phantoms como "fiscalmente eficientes".
- **Siempre coordinar con asesor fiscal.** La tributación de estos instrumentos es compleja y cambiante.
