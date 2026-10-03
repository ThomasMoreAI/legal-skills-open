---
name: regimen-economico
title: /regimen-economico
description: Analiza el régimen económico matrimonial aplicable a una pareja, considerando vecindad civil, capitulaciones matrimoniales y derechos forales. Determina las consecuencias para la liquidación patrimonial. Usar cuando el usuario dice "qué régimen económico aplica", "liquidación de gananciales", "separación de bienes", "régimen foral", o necesita determinar el régimen antes de un divorcio o liquidación.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/familia/skills/regimen-economico
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: family
language: es
---

# /regimen-economico

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica.
2. Recopilar datos del matrimonio y vecindad civil.
3. Determinar el régimen aplicable.
4. Explicar las consecuencias para la liquidación.
5. Producir el informe.

---

## Propósito

Determinar con certeza qué régimen económico matrimonial rige un matrimonio concreto, explicar sus consecuencias patrimoniales y orientar sobre el proceso de liquidación. Es fundamental acertar en esto antes de redactar un convenio regulador o plantear una liquidación.

## Datos necesarios

- **Fecha del matrimonio.**
- **Lugar de celebración.**
- **Vecindad civil de cada cónyuge al momento del matrimonio** — este es el dato clave.
- **Capitulaciones matrimoniales** — si existen, cuándo se otorgaron, qué régimen pactaron.
- **Cambios de vecindad civil posteriores** — residencia continuada de 10 años o declaración ante el Registro Civil (art. 14.5 CC).
- **Nacionalidad** — si algún cónyuge es extranjero, aplicar normas de DIPr (Reglamento UE 2016/1103).

## Determinación del régimen aplicable

### Paso 1: Comprobar capitulaciones

Si hay capitulaciones matrimoniales (art. 1325 CC) — el régimen es el pactado. Fin del análisis.

### Paso 2: Determinar vecindad civil

| Cónyuge A | Cónyuge B | Régimen supletorio |
|---|---|---|
| Vecindad civil común | Vecindad civil común | Gananciales (art. 1316 CC) |
| Vecindad civil catalana | Vecindad civil catalana | Separación de bienes (art. 232-1 CCCat) |
| Vecindad civil aragonesa | Vecindad civil aragonesa | Consorcio conyugal (CDFA arts. 210 y ss.) |
| Vecindad civil balear | Vecindad civil balear | Separación de bienes (Compilación Baleares) |
| Vecindad civil navarra | Vecindad civil navarra | Conquistas (Ley 82 Fuero Nuevo) |
| Vecindad civil vizcaína | Vecindad civil vizcaína | Comunicación foral (Ley 5/2015 DCPV) |
| Vecindad civil gallega | Vecindad civil gallega | Gananciales con particularidades (Ley 2/2006) |

### Paso 3: Si las vecindades son distintas

En defecto de capitulaciones, se aplican las reglas del art. 9.2 CC (en su redacción aplicable según la fecha del matrimonio):

1. Ley personal común al tiempo de contraer matrimonio.
2. Ley personal o de residencia habitual de cualquiera de ellos, elegida en documento antes del matrimonio.
3. Ley de residencia habitual común inmediatamente posterior al matrimonio.
4. Ley del lugar de celebración.

**Atención a la fecha del matrimonio:** las reglas del art. 9.2 CC han cambiado. Para matrimonios anteriores a la reforma de 1990, las reglas eran distintas (se aplicaba la ley del marido).

### Paso 4: Si hay elemento internacional

- **Matrimonios entre ciudadanos UE (desde 29/01/2019):** Reglamento (UE) 2016/1103.
- **Matrimonios anteriores o con terceros estados:** art. 9.2 CC + convenios bilaterales.

## Regímenes — Características y liquidación

### Gananciales (CC arts. 1344-1410)

- **Bienes gananciales:** adquiridos a título oneroso durante el matrimonio, rendimientos del trabajo, frutos de bienes privativos y gananciales.
- **Bienes privativos:** los aportados al matrimonio, los adquiridos a título gratuito (herencia, donación), los de carácter personalísimo.
- **Liquidación:** inventario (activo y pasivo ganancial) -> avalúo -> pago de deudas -> división por mitad del remanente.

### Separación de bienes (CC arts. 1435-1444)

- Cada cónyuge es titular de sus bienes.
- Bienes en copropiedad: se dividen según las cuotas.
- **Compensación por trabajo doméstico (art. 1438 CC):** el cónyuge que contribuyó al hogar tiene derecho a compensación. Criterio del TS: proporcional al enriquecimiento del otro.

### Consorcio conyugal aragonés (CDFA arts. 210 y ss.)

- Similar a gananciales pero con diferencias relevantes: bienes consorciales, bienes privativos, gestión del patrimonio.
- **Viudedad foral:** derecho de usufructo universal al cónyuge sobreviviente. No confundir con la liquidación inter vivos.

### Conquistas navarras (Fuero Nuevo Ley 82 y ss.)

- Bienes de conquista: adquiridos a título oneroso durante el matrimonio.
- Gestión conjunta.
- Liquidación similar a gananciales.

### Comunicación foral vizcaína (Ley 5/2015 DCPV)

- Todos los bienes se comunican al disolverse el matrimonio.
- Régimen muy amplio: incluye bienes aportados al matrimonio.
- Aplicable solo en tierra llana vizcaína — no en todo el País Vasco.

## Formato de salida

```markdown
BORRADOR — ANÁLISIS DE RÉGIMEN ECONÓMICO MATRIMONIAL — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Datos aportados:** [qué datos se proporcionaron]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar vecindad civil en el Registro Civil; comprobar existencia de capitulaciones en el Registro de la Propiedad (Sección 4.a); si hay elemento internacional, verificar normativa aplicable.

## Régimen económico matrimonial: [Nombres de los cónyuges]

### Datos del matrimonio

| Dato | Valor |
|---|---|
| Fecha de matrimonio | [fecha] |
| Lugar de celebración | [lugar] |
| Vecindad civil cónyuge A | [vecindad] |
| Vecindad civil cónyuge B | [vecindad] |
| Capitulaciones | [sí/no — fecha y contenido] |

### Régimen aplicable

**[Nombre del régimen]** — [fundamentación jurídica]

### Consecuencias para la liquidación

[Explicación práctica de qué bienes son comunes y privativos, cómo se liquida, qué derechos especiales existen]

### Pasos para la liquidación

1. [Paso 1]
2. [Paso 2]
3. [Paso N]

---

**Qué hacer a continuación:**
1. **Inventario de bienes** — preparo el inventario de bienes comunes y privativos.
2. **Convenio regulador** — `/familia:convenio` con el régimen ya determinado.
3. **Liquidación detallada** — propuesta de adjudicación de bienes.
4. **Verificar vecindad civil** — necesito confirmación del Registro Civil.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **CC arts. 1315-1444** — régimen económico matrimonial.
- **CC art. 9.2** — ley aplicable a los efectos del matrimonio.
- **CC art. 14** — vecindad civil.
- **CC art. 1316** — gananciales como supletorio en derecho común.
- **CC art. 1438** — compensación por trabajo doméstico.
- **CCCat Libro II (Ley 25/2010)** — régimen económico matrimonial catalán.
- **CDFA (DL 1/2011 de Aragón) arts. 210 y ss.** — consorcio conyugal.
- **Compilación de Baleares (DL 79/1990)** — separación de bienes.
- **Fuero Nuevo de Navarra (Ley 1/1973) Ley 82 y ss.** — conquistas.
- **Ley 5/2015 de Derecho Civil Vasco** — comunicación foral.
- **Ley 2/2006 de Derecho Civil de Galicia** — particularidades.
- **Reglamento (UE) 2016/1103** — régimen económico matrimonial internacional.

## Guardarraíles

- **La vecindad civil es el dato clave.** Sin ella, no se puede determinar el régimen. Insistir hasta obtenerla.
- **No confundir residencia con vecindad civil.** Se puede residir en Barcelona con vecindad civil común (y aplicar gananciales).
- **Verificar siempre las capitulaciones.** Se consultan en el Registro de la Propiedad, Sección 4.a (Registro Civil desde 2024 para los nuevos).
- **La fecha del matrimonio importa.** Las reglas de conflicto del art. 9.2 CC han cambiado varias veces.
- **No aplicar derecho foral sin confirmar vecindad civil foral.** Un aragonés de nacimiento que lleva 15 años en Madrid puede haber adquirido vecindad civil común.
- **La viudedad foral aragonesa NO es liquidación del régimen.** No confundir derechos sucesorios con derechos en la liquidación inter vivos.
