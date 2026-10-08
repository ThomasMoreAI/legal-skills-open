---
name: regimen-economico-betobetico
title: /regimen-economico
description: Analiza el régimen patrimonial del matrimonio aplicable a una pareja bajo el Código de la Familia de Panamá, considerando las capitulaciones matrimoniales, el régimen legal supletorio y, en su caso, el elemento internacional. Determina las consecuencias para la liquidación patrimonial. Usar cuando el usuario dice "qué régimen económico aplica", "liquidación de gananciales", "separación de bienes", "participación en las ganancias", o necesita determinar el régimen antes de un divorcio o liquidación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/familia/skills/regimen-economico
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: family
language: es
---

# /regimen-economico

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica.
2. Recopilar datos del matrimonio.
3. Determinar el régimen aplicable.
4. Explicar las consecuencias para la liquidación.
5. Producir el informe.

---

## Propósito

Determinar con certeza qué régimen patrimonial del matrimonio rige un matrimonio concreto bajo el Código de la Familia de Panamá, explicar sus consecuencias patrimoniales y orientar sobre el proceso de liquidación. Es fundamental acertar en esto antes de redactar un convenio de divorcio o plantear una liquidación.

## Datos necesarios

- **Fecha del matrimonio.**
- **Lugar de celebración.**
- **Nacionalidad y residencia de cada cónyuge al momento del matrimonio.**
- **Capitulaciones matrimoniales** — si existen, cuándo se otorgaron, qué régimen pactaron.
- **Cambios posteriores de régimen** — si las partes modificaron el régimen mediante escritura pública. [verificar requisitos en el Código de la Familia]
- **Elemento internacional** — si algún cónyuge es extranjero o el matrimonio se celebró fuera de Panamá, valorar las normas de derecho internacional privado panameño (Código de Bustamante / Código de Derecho Internacional Privado de Panamá, Ley 61 de 2015).

## Determinación del régimen aplicable

### Paso 1: Comprobar capitulaciones

Si hay capitulaciones matrimoniales válidas — el régimen es el pactado por las partes. Fin del análisis. [verificar art. del Código de la Familia sobre capitulaciones]

### Paso 2: Régimen legal supletorio

A falta de capitulaciones, rige el régimen legal supletorio previsto en el Código de la Familia de Panamá. [verificar — confirmar cuál es el régimen supletorio actual: sociedad de gananciales o participación en las ganancias]

| Situación | Régimen aplicable |
|---|---|
| Matrimonio sin capitulaciones | Régimen legal supletorio del Código de la Familia |
| Matrimonio con capitulaciones de separación de bienes | Separación de bienes |
| Matrimonio con capitulaciones de participación | Participación en las ganancias |

### Paso 3: Si hay elemento internacional

- **Cónyuge extranjero o matrimonio celebrado fuera de Panamá:** aplicar las normas de conflicto del derecho internacional privado panameño (Código de Bustamante; Código de Derecho Internacional Privado de Panamá [verificar]) para determinar la ley aplicable a los efectos patrimoniales del matrimonio.
- **Atención a la fecha del matrimonio:** verificar la norma de conflicto vigente al momento de la celebración.

## Regímenes — Características y liquidación

### Sociedad de gananciales (Código de la Familia) [verificar arts.]

- **Bienes gananciales (comunes):** adquiridos a título oneroso durante el matrimonio, rendimientos del trabajo, frutos de bienes propios y comunes.
- **Bienes propios (privativos):** los aportados al matrimonio, los adquiridos a título gratuito (herencia, donación), los de carácter personalísimo.
- **Liquidación:** inventario (activo y pasivo común) -> avalúo -> pago de deudas -> división por mitad del remanente.

### Separación de bienes (Código de la Familia) [verificar arts.]

- Cada cónyuge es titular de sus bienes.
- Bienes en copropiedad: se dividen según las cuotas.
- **Compensación por trabajo doméstico:** el cónyuge que contribuyó al hogar puede tener derecho a compensación, según el régimen y las circunstancias. [verificar base legal en el Código de la Familia]

### Participación en las ganancias (Código de la Familia) [verificar arts.]

- Durante el matrimonio funciona como separación de bienes.
- A la disolución, cada cónyuge adquiere derecho a participar en las ganancias obtenidas por el otro.
- **Liquidación:** cálculo del patrimonio inicial y final de cada cónyuge -> determinación de las ganancias -> crédito de participación.

## Formato de salida

```markdown
BORRADOR — ANÁLISIS DE RÉGIMEN PATRIMONIAL DEL MATRIMONIO — REVISIÓN DE ABOGADO OBLIGATORIA

> **Nota para el revisor**
> - **Datos aportados:** [qué datos se proporcionaron]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar existencia de capitulaciones en el Registro Público de Panamá; confirmar el régimen legal supletorio vigente al momento del matrimonio; si hay elemento internacional, verificar la norma de conflicto aplicable.

## Régimen patrimonial del matrimonio: [Nombres de los cónyuges]

### Datos del matrimonio

| Dato | Valor |
|---|---|
| Fecha de matrimonio | [fecha] |
| Lugar de celebración | [lugar] |
| Nacionalidad / residencia cónyuge A | [dato] |
| Nacionalidad / residencia cónyuge B | [dato] |
| Capitulaciones | [sí/no — fecha y contenido] |

### Régimen aplicable

**[Nombre del régimen]** — [fundamentación jurídica]

### Consecuencias para la liquidación

[Explicación práctica de qué bienes son comunes y propios, cómo se liquida, qué derechos especiales existen]

### Pasos para la liquidación

1. [Paso 1]
2. [Paso 2]
3. [Paso N]

---

**Qué hacer a continuación:**
1. **Inventario de bienes** — preparo el inventario de bienes comunes y propios.
2. **Convenio de divorcio** — `/familia:convenio` con el régimen ya determinado.
3. **Liquidación detallada** — propuesta de adjudicación de bienes.
4. **Verificar capitulaciones** — necesito confirmación del Registro Público.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Código de la Familia de Panamá** — régimen patrimonial del matrimonio. [verificar arts.]
- **Código de la Familia** — capitulaciones matrimoniales y su modificación. [verificar arts.]
- **Código de la Familia** — régimen legal supletorio. [verificar art.]
- **Código de la Familia** — sociedad de gananciales, separación de bienes y participación en las ganancias. [verificar arts.]
- **Código de la Familia** — compensación por trabajo doméstico. [verificar art.]
- **Código de Derecho Internacional Privado de Panamá** (Ley 61 de 2015) y Código de Bustamante — régimen patrimonial con elemento internacional. [verificar]

## Guardarraíles

- **Verificar siempre las capitulaciones.** Se inscriben en el Registro Público de Panamá. Sin capitulaciones, rige el régimen legal supletorio.
- **Confirmar cuál es el régimen legal supletorio vigente.** No darlo por sentado: verificar el Código de la Familia y la fecha del matrimonio. [verificar]
- **La fecha del matrimonio importa.** Las normas pueden haber cambiado; comprobar el régimen y la norma de conflicto vigentes al momento de la celebración.
- **No aplicar derecho extranjero sin confirmar la norma de conflicto.** Si hay cónyuge extranjero o celebración fuera de Panamá, determinar primero la ley aplicable conforme al derecho internacional privado panameño.
- **No confundir derechos sucesorios con derechos en la liquidación inter vivos.** La liquidación del régimen patrimonial es distinta de la sucesión por causa de muerte.
