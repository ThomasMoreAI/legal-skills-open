---
name: convenio
title: /convenio
description: 'Genera una plantilla de convenio regulador para divorcio o separación, con todas las secciones obligatorias del art. 90 CC: guarda y custodia, régimen de visitas, uso de vivienda familiar, pensión de alimentos, pensión compensatoria y liquidación del régimen económico. Adapta el contenido al perfil de práctica y a las posiciones habituales del despacho. Usar cuando el usuario dice "convenio regulador", "redacta un convenio", "divorcio de mutuo acuerdo", o necesita una plantilla de convenio.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/familia/skills/convenio
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: family
language: es
---

# /convenio

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica y posiciones habituales.
2. Recopilar datos de los cónyuges, menores e hijos mayores dependientes.
3. Determinar el régimen económico matrimonial aplicable.
4. Generar el convenio con las secciones del art. 90 CC.
5. Ajustar a las posiciones habituales del despacho (si están configuradas).

---

## Propósito

Producir un borrador de convenio regulador completo que cumpla los requisitos del art. 90 CC, adaptado a las circunstancias concretas de la pareja y a las posiciones habituales del despacho. Es un borrador — requiere revisión letrada y, en mutuo acuerdo, la conformidad de ambas partes.

## Datos necesarios

- **Datos de los cónyuges:** nombres, DNI, domicilios, profesiones, ingresos netos mensuales.
- **Datos del matrimonio:** fecha, lugar de celebración, régimen económico (capitulaciones o legal supletorio), vecindad civil.
- **Hijos menores:** nombres, fechas de nacimiento, necesidades especiales.
- **Hijos mayores dependientes económicamente:** si los hay.
- **Vivienda familiar:** propiedad (de quién), hipoteca pendiente, valor aproximado.
- **Otros bienes y deudas comunes:** vehículos, cuentas, inversiones, deudas.
- **Tipo de procedimiento:** mutuo acuerdo (art. 777 LEC) o contencioso (art. 770 LEC).

## Secciones obligatorias (art. 90 CC)

### 1. Guarda y custodia

- **Custodia compartida:** distribución del tiempo (semanas alternas, 5-2-2-5, u otro modelo), domicilio de referencia del menor, decisiones ordinarias y extraordinarias.
- **Custodia exclusiva:** progenitor custodio, régimen de visitas del no custodio.
- **Criterio rector:** interés superior del menor (art. 2 LOPJM).
- **Patria potestad:** compartida salvo circunstancias excepcionales.

### 2. Régimen de visitas y comunicaciones

- Fines de semana alternos (viernes a domingo o jueves a lunes).
- Tarde intersemanal.
- Vacaciones: Navidad, Semana Santa, verano — reparto por mitades, años pares/impares.
- Días señalados: cumpleaños de los hijos, día del padre/madre, festividades locales.
- Comunicaciones telefónicas y telemáticas.

### 3. Uso de la vivienda familiar (art. 96 CC)

- Atribución al progenitor custodio o a los hijos (si custodia compartida, criterios del TS).
- Temporalidad — la jurisprudencia del TS tiende a limitar temporalmente la atribución.
- Compensación por uso si la vivienda es de ambos o del no custodio.

### 4. Pensión de alimentos (arts. 142-153 CC)

- Cuantía mensual por hijo.
- Actualización anual (IPC u otro índice).
- Gastos ordinarios incluidos.
- Gastos extraordinarios: clasificación y reparto.
- Forma de pago y cuenta de ingreso.
- Para cálculo detallado: `/familia:pensiones`.

### 5. Pensión compensatoria (art. 97 CC)

- Existencia de desequilibrio económico.
- Cuantía y duración (temporal o indefinida).
- Criterios del art. 97 CC: dedicación a la familia, duración del matrimonio, edad, cualificación, estado de salud.
- Causas de extinción.

### 6. Liquidación del régimen económico matrimonial

- Si **gananciales:** inventario de bienes gananciales y privativos, avalúo, propuesta de adjudicación.
- Si **separación de bienes:** división de bienes en copropiedad, compensación por trabajo doméstico (art. 1438 CC).
- Si **régimen foral:** aplicar normativa foral correspondiente (verificar vecindad civil).
- Puede incluirse en el convenio o tramitarse en pieza separada.

## Formato de salida

```markdown
BORRADOR — CONVENIO REGULADOR — REVISIÓN LETRADA OBLIGATORIA

> **Nota para el revisor**
> - **Régimen económico:** [gananciales / separación de bienes / foral — cuál]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar datos patrimoniales; confirmar régimen económico; revisar cálculo de pensiones; obtener conformidad de ambas partes.

## CONVENIO REGULADOR

D./D.a [nombre], con DNI [X], y D./D.a [nombre], con DNI [X], de común acuerdo y a los efectos previstos en el artículo 90 del Código Civil, otorgan el presente convenio regulador:

### PRIMERO. — Guarda y custodia
[Contenido adaptado a los datos y posiciones del despacho]

### SEGUNDO. — Régimen de visitas y comunicaciones
[Contenido]

### TERCERO. — Uso de la vivienda familiar
[Contenido]

### CUARTO. — Pensión de alimentos
[Contenido con cuantía, actualización y gastos extraordinarios]

### QUINTO. — Pensión compensatoria
[Contenido o "Las partes renuncian expresamente a la pensión compensatoria"]

### SEXTO. — Liquidación del régimen económico matrimonial
[Contenido según régimen aplicable]

### SÉPTIMO. — Ajuar doméstico
[Reparto]

### OCTAVO. — Seguros y planes de pensiones
[Si aplica]

### NOVENO. — Efectos fiscales
[Atribución de beneficios fiscales, tributación conjunta/individual]

En [ciudad], a [fecha].

[Firma] — [Firma]
```

## Referencias legislativas

- **CC arts. 90-101** — efectos de la nulidad, separación y divorcio.
- **CC art. 92** — guarda y custodia.
- **CC art. 93** — pensión de alimentos.
- **CC art. 96** — vivienda familiar.
- **CC art. 97** — pensión compensatoria.
- **CC arts. 142-153** — alimentos entre parientes.
- **CC art. 1438** — compensación por trabajo doméstico en separación de bienes.
- **LEC art. 777** — procedimiento de mutuo acuerdo.
- **LEC art. 770** — procedimiento contencioso.
- **LOPJM art. 2** — interés superior del menor.

## Guardarraíles

- **No asumir gananciales.** Verificar siempre vecindad civil y si hay capitulaciones. En Cataluña el supletorio es separación de bienes; en Aragón, consorcio conyugal.
- **El interés superior del menor prevalece siempre.** Por encima de las preferencias de las partes y de los defaults del despacho.
- **No presentar la custodia compartida como "lo normal".** Es una opción más — depende de las circunstancias del caso, la edad de los hijos y la capacidad de cooperación de los progenitores.
- **La renuncia a la pensión compensatoria debe ser informada.** Si hay desequilibrio evidente, advertir de las consecuencias de la renuncia.
- **No olvidar la compensación por trabajo doméstico (art. 1438 CC).** En separación de bienes, el cónyuge dedicado al hogar tiene derecho. Muchos lo olvidan.
- **Si hay indicios de violencia de género, PARAR.** No es un caso de convenio regulador ordinario — derivar a Juzgado de Violencia sobre la Mujer y recursos especializados.
