---
name: creditos-betobetico
title: /creditos
description: 'Clasifica créditos del proceso concursal según el régimen de prelación de la Ley 12 de 2016 y del Código Civil de Panamá: créditos con garantía real / privilegio especial, créditos privilegiados o preferentes (laborales, fiscales, CSS), ordinarios y subordinados. Ayuda a preparar la comunicación y reconocimiento de créditos y a verificar la lista de créditos. Usar cuando el usuario dice "clasifica este crédito", "reconocimiento de créditos", "comunicación de créditos", "lista de créditos", o revisa un inventario de créditos.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/concursal/skills/creditos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: bankruptcy
language: es
---

# /creditos

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de los créditos a clasificar.
3. Aplicar las reglas de prelación de la Ley 12 de 2016 y del Código Civil de Panamá.
4. Producir la clasificación con fundamentación.
5. Si procede, preparar modelo de comunicación/reconocimiento.

---

## Propósito

Clasificar los créditos del proceso concursal en sus categorías legales y, cuando el usuario lo necesite, preparar la documentación para la comunicación o reconocimiento de créditos ante el administrador del proceso. La clasificación correcta es crítica: determina el orden de pago, el derecho de voto en la reorganización y la cuota en la liquidación.

## Categorías de créditos (Ley 12 de 2016 y Código Civil de Panamá [verificar])

### Créditos de administración del proceso

No son créditos concursales en sentido estricto — se atienden con preferencia por estar vinculados al propio proceso [verificar]. Suelen incluir:

- Honorarios del administrador/restructurador/liquidador del proceso.
- Gastos y costas del proceso concursal.
- Créditos por obligaciones nacidas tras la apertura del proceso para la continuidad de la actividad.

### Créditos con garantía real / privilegio especial

Vinculados a un bien o derecho concreto:

| Tipo | Fundamento | Límite |
|---|---|---|
| Créditos garantizados con hipoteca | Código Civil de Panamá [verificar] | Hasta el valor de la garantía |
| Créditos garantizados con prenda | Código Civil / Ley de prenda mercantil [verificar] | Hasta el valor del bien pignorado |
| Créditos garantizados con anticresis | Código Civil de Panamá [verificar] | Hasta el valor del inmueble |
| Créditos con garantía mobiliaria registrada | Legislación de garantías mobiliarias [verificar] | Sobre el bien gravado |
| Créditos con reserva de dominio | Código de Comercio / Código Civil | Sobre el bien vendido |

### Créditos privilegiados / preferentes

Se cobran antes que los ordinarios sobre el patrimonio del deudor sin afectación a un bien concreto [verificar]:

| Tipo | Fundamento |
|---|---|
| Salarios, prestaciones e indemnizaciones laborales (incluido décimo tercer mes) | Código de Trabajo de Panamá [verificar] |
| Cuotas adeudadas a la CSS (Caja de Seguro Social) | Régimen de la CSS [verificar] |
| Créditos fiscales (DGI — Dirección General de Ingresos) | Código Fiscal de Panamá [verificar] |
| Otros créditos con privilegio legal | Código Civil de Panamá [verificar] |

*Nota: el orden de prelación entre los créditos laborales, de la CSS y fiscales debe verificarse en cada caso conforme al Código de Trabajo, el régimen de la CSS y el Código Fiscal.*

### Créditos ordinarios / comunes

Todos los que no son privilegiados ni subordinados. Es la categoría residual [verificar].

### Créditos subordinados / postergados

Se cobran después de todos los demás [verificar]:

| Tipo | Fundamento |
|---|---|
| Comunicados tardíamente (fuera del plazo de reconocimiento) | Ley 12 de 2016 |
| Contractualmente subordinados | Código Civil / Ley 12 de 2016 |
| Intereses (salvo los amparados por garantía real) | Ley 12 de 2016 |
| Multas y sanciones | Ley 12 de 2016 |
| Créditos de personas vinculadas al deudor | Ley 12 de 2016 |

## Personas vinculadas al deudor (Ley 12 de 2016)

- **Con persona natural:** cónyuge, conviviente, ascendientes, descendientes, hermanos [verificar].
- **Con persona jurídica:** socios/accionistas con participación relevante, dignatarios y directores, sociedades del mismo grupo [verificar].

## Flujo de clasificación

Para cada crédito:

1. **Identificar al acreedor** — nombre, relación con el deudor.
2. **Determinar el origen** — contractual, laboral, fiscal, CSS, extracontractual, otro.
3. **Comprobar si hay garantía real** — hipoteca, prenda, garantía mobiliaria, reserva de dominio.
4. **Verificar si es persona vinculada** al deudor [verificar].
5. **Comprobar si se comunicó en plazo** (plazo de reconocimiento de la Ley 12 de 2016).
6. **Clasificar** aplicando las reglas en orden: administración del proceso > garantía real/privilegio especial > privilegiado/preferente > ordinario > subordinado [verificar].
7. **Señalar créditos mixtos** — un crédito hipotecario puede ser garantía real hasta el valor de la garantía y ordinario por el resto.

## Formato de salida

```markdown
BORRADOR — CLASIFICACIÓN DE CRÉDITOS — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Créditos analizados:** [N]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** confirmar importes actualizados; verificar garantías en el Registro Público de Panamá; comprobar plazos de comunicación de la Ley 12 de 2016.

## Clasificación de créditos: [Proceso concursal de X]

| N.o | Acreedor | Importe (USD/B/.) | Origen | Garantía | Clasificación | Fundamento | Notas |
|---|---|---|---|---|---|---|---|
| 1 | [nombre] | [importe] | [origen] | [sí/no — tipo] | [categoría] | [norma — verificar] | [verificar] |

### Resumen por categorías

| Categoría | N.o de créditos | Importe total | % del pasivo |
|---|---|---|---|
| Administración del proceso | [N] | [importe] | [%] |
| Garantía real / privilegio especial | [N] | [importe] | [%] |
| Privilegiados / preferentes | [N] | [importe] | [%] |
| Ordinarios / comunes | [N] | [importe] | [%] |
| Subordinados | [N] | [importe] | [%] |

---

**Qué hacer a continuación:**
1. **Preparar comunicación de créditos** — modelo de escrito de comunicación/reconocimiento ante el administrador del proceso.
2. **Impugnar la lista** — si la clasificación del administrador no coincide, preparo escrito de impugnación.
3. **Calcular mayorías para la reorganización** — con la clasificación, calculo las mayorías necesarias.
4. **Plan de reorganización** — `/concursal:plan` con los créditos ya clasificados.
5. **Otra cosa** — dime qué necesitas.
```

## Modelo de comunicación de créditos

Cuando el usuario lo solicite, generar un escrito de comunicación/reconocimiento con:

- Datos del acreedor (incluida cédula o RUC).
- Identificación del proceso concursal y juzgado.
- Importe del crédito (en USD/balboas), origen y fecha.
- Clasificación propuesta con fundamentación jurídica.
- Documentación justificativa adjunta (facturas, contratos, títulos, etc.).
- Plazo: el plazo de comunicación/reconocimiento de créditos que fije la Ley 12 de 2016 desde la apertura del proceso y su publicación [verificar].

## Referencias legislativas

- **Ley 12 de 2016** — proceso concursal de insolvencia; reconocimiento, graduación y prelación de créditos [verificar].
- **Código Civil de Panamá** — prelación y graduación general de créditos [verificar].
- **Código de Trabajo de Panamá** — créditos laborales (salarios, prestaciones, décimo tercer mes) [verificar].
- **Régimen de la CSS** — Caja de Seguro Social, cuotas adeudadas [verificar].
- **Código Fiscal de Panamá** — créditos tributarios (DGI) [verificar].
- **Plazo de comunicación de créditos** — Ley 12 de 2016.

## Guardarraíles

- **La clasificación depende de los hechos.** Si falta información sobre garantías o relación con el deudor, marcar `[verificar — clasificación provisional]`.
- **No inventar números de artículo ni el orden exacto de prelación.** El régimen de prelación panameño combina Ley 12 de 2016, Código Civil, Código de Trabajo, régimen de la CSS y Código Fiscal: usar referencia a la norma + `[verificar]` cuando no haya certeza.
- **Los créditos mixtos son frecuentes.** Un crédito hipotecario es garantía real solo hasta el valor de la garantía — el exceso es ordinario.
- **El plazo de comunicación es preclusivo.** Si se pasa, el crédito puede quedar subordinado o no reconocido [verificar]. Advertir siempre del plazo.
- **Persona vinculada no es insulto — es categoría legal.** Explicar las consecuencias sin dramatizar.
- **Nunca afirmar que la clasificación del administrador del proceso es incorrecta sin analizar sus fundamentos.** Señalar discrepancias para que el abogado las valore.
