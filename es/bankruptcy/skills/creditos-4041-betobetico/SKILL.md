---
name: creditos-4041-betobetico
title: /creditos
description: 'Clasifica créditos concursales según las categorías del TRLC: privilegio especial (art. 270), privilegio general (art. 280), ordinarios (art. 284) y subordinados (art. 281). Ayuda a preparar la comunicación e insinuación de créditos y a verificar la lista de acreedores. Usar cuando el usuario dice "clasifica este crédito", "insinuación de créditos", "comunicación de créditos", "lista de acreedores", o revisa un inventario de créditos concursales.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/concursal/skills/creditos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: bankruptcy
language: es
---

# /creditos

1. Leer `~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md` — perfil de práctica.
2. Recopilar datos de los créditos a clasificar.
3. Aplicar las reglas de clasificación del TRLC.
4. Producir la clasificación con fundamentación.
5. Si procede, preparar modelo de comunicación/insinuación.

---

## Propósito

Clasificar créditos concursales en sus categorías legales y, cuando el usuario lo necesite, preparar la documentación para la comunicación o insinuación de créditos ante la administración concursal. La clasificación correcta es crítica: determina el orden de pago, el derecho de voto en el convenio y la cuota de liquidación.

## Categorías de créditos (TRLC arts. 269-296)

### Créditos contra la masa (art. 242 TRLC)

No son créditos concursales — se pagan a su vencimiento con preferencia. Incluyen:

- Créditos salariales de los últimos 30 días antes de la declaración (hasta el doble del SMI).
- Costes del procedimiento concursal.
- Créditos por obligaciones nacidas tras la declaración de concurso.
- Alimentos del deudor y personas a su cargo.

### Créditos con privilegio especial (art. 270 TRLC)

Vinculados a un bien o derecho concreto:

| Tipo | Fundamento | Límite |
|---|---|---|
| Créditos garantizados con hipoteca | Art. 270.1.o TRLC | Hasta el valor de la garantía |
| Créditos garantizados con prenda | Art. 270.2.o TRLC | Hasta el valor del bien pignorado |
| Créditos garantizados con anticresis | Art. 270.3.o TRLC | Hasta el valor del inmueble |
| Créditos refaccionarios | Art. 270.4.o TRLC | Sobre el bien refaccionado |
| Arrendamientos financieros (leasing) | Art. 270.5.o TRLC | Cuotas pendientes + valor residual |
| Créditos con reserva de dominio | Art. 270.6.o TRLC | Sobre el bien vendido |

### Créditos con privilegio general (art. 280 TRLC)

Se cobran antes que los ordinarios sobre la masa activa sin afectación a bien concreto:

| Tipo | Fundamento |
|---|---|
| Créditos salariales (no contra la masa) hasta el triple del SMI x n.o de días pendientes | Art. 280.1.o TRLC |
| Indemnizaciones por extinción de contrato laboral | Art. 280.2.o TRLC |
| Retenciones tributarias y de SS debidas por el concursado | Art. 280.3.o TRLC |
| Créditos tributarios y de SS hasta el 50% de su importe | Art. 280.4.o TRLC |
| Créditos por responsabilidad civil extracontractual | Art. 280.5.o TRLC |
| Créditos del acreedor instante (25% de su crédito) | Art. 280.6.o TRLC |

### Créditos ordinarios (art. 284 TRLC)

Todos los que no son privilegiados ni subordinados. Es la categoría residual.

### Créditos subordinados (art. 281 TRLC)

Se cobran después de todos los demás:

| Tipo | Fundamento |
|---|---|
| Comunicados tardíamente (tras el plazo del art. 255) | Art. 281.1.o TRLC |
| Contractualmente subordinados | Art. 281.2.o TRLC |
| Intereses (salvo los garantizados con privilegio especial) | Art. 281.3.o TRLC |
| Multas y sanciones | Art. 281.4.o TRLC |
| Créditos de personas especialmente relacionadas (art. 283) | Art. 281.5.o TRLC |
| Créditos derivados de rescisión concursal a favor del demandado | Art. 281.6.o TRLC |

## Personas especialmente relacionadas (art. 283 TRLC)

- **Con persona física:** cónyuge, pareja de hecho, ascendientes, descendientes, hermanos.
- **Con persona jurídica:** socios con >10% (SL) o >5% (SA), administradores, sociedades del grupo.

## Flujo de clasificación

Para cada crédito:

1. **Identificar al acreedor** — nombre, relación con el deudor.
2. **Determinar el origen** — contractual, laboral, tributario, extracontractual, otro.
3. **Comprobar si hay garantía real** — hipoteca, prenda, reserva de dominio, leasing.
4. **Verificar si es persona especialmente relacionada** (art. 283 TRLC).
5. **Comprobar si se comunicó en plazo** (art. 255 TRLC — 1 mes desde publicación en el BOE).
6. **Clasificar** aplicando las reglas en orden: contra la masa > privilegio especial > privilegio general > ordinario > subordinado.
7. **Señalar créditos mixtos** — un crédito hipotecario puede ser privilegio especial hasta el valor de la garantía y ordinario por el resto.

## Formato de salida

```markdown
BORRADOR — CALIFICACIÓN DE CRÉDITOS — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Créditos analizados:** [N]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** confirmar importes actualizados; verificar garantías en el Registro de la Propiedad/Registro de Bienes Muebles; comprobar plazos de comunicación.

## Clasificación de créditos: [Concurso de X]

| N.o | Acreedor | Importe | Origen | Garantía | Clasificación | Fundamento | Notas |
|---|---|---|---|---|---|---|---|
| 1 | [nombre] | [importe] | [origen] | [sí/no — tipo] | [categoría] | [artículo TRLC] | [verificar] |

### Resumen por categorías

| Categoría | N.o de créditos | Importe total | % del pasivo |
|---|---|---|---|
| Contra la masa | [N] | [importe] | [%] |
| Privilegio especial | [N] | [importe] | [%] |
| Privilegio general | [N] | [importe] | [%] |
| Ordinarios | [N] | [importe] | [%] |
| Subordinados | [N] | [importe] | [%] |

---

**Qué hacer a continuación:**
1. **Preparar comunicación de créditos** — modelo de escrito de comunicación/insinuación ante la AC.
2. **Impugnar la lista** — si la clasificación de la AC no coincide, preparo escrito de impugnación.
3. **Calcular mayorías para convenio** — con la clasificación, calculo las mayorías necesarias.
4. **Plan de reestructuración** — `/concursal:plan` con los créditos ya clasificados.
5. **Otra cosa** — dime qué necesitas.
```

## Modelo de comunicación de créditos

Cuando el usuario lo solicite, generar un escrito de comunicación/insinuación con:

- Datos del acreedor.
- Identificación del concurso y juzgado.
- Importe del crédito, origen y fecha.
- Clasificación propuesta con fundamentación jurídica.
- Documentación justificativa adjunta (facturas, contratos, títulos, etc.).
- Plazo: 1 mes desde la publicación de la declaración de concurso en el BOE (art. 255 TRLC).

## Referencias legislativas

- **TRLC arts. 242-248** — créditos contra la masa.
- **TRLC arts. 269-296** — clasificación de créditos concursales.
- **Art. 270 TRLC** — privilegio especial.
- **Art. 280 TRLC** — privilegio general.
- **Art. 281 TRLC** — créditos subordinados.
- **Art. 283 TRLC** — personas especialmente relacionadas.
- **Art. 284 TRLC** — créditos ordinarios.
- **Art. 255 TRLC** — plazo de comunicación de créditos.

## Guardarraíles

- **La clasificación depende de los hechos.** Si falta información sobre garantías o relación con el deudor, marcar `[verificar — clasificación provisional]`.
- **Los créditos mixtos son frecuentes.** Un crédito hipotecario es privilegio especial solo hasta el valor de la garantía — el exceso es ordinario.
- **El plazo de comunicación es preclusivo.** Si se pasa, el crédito se clasifica como subordinado. Advertir siempre del plazo.
- **Persona especialmente relacionada no es insulto — es categoría legal.** Explicar las consecuencias sin dramatizar.
- **Nunca afirmar que la clasificación de la administración concursal es incorrecta sin analizar sus fundamentos.** Señalar discrepancias para que el letrado las valore.
