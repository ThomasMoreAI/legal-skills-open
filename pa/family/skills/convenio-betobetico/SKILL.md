---
name: convenio-betobetico
title: /convenio
description: 'Genera una plantilla de convenio de divorcio por mutuo consentimiento o de regulación de guarda, crianza y comunicación, con todas las secciones habituales bajo el Código de la Familia de Panamá: guarda y crianza, régimen de comunicación y visitas, uso de la vivienda familiar, pensión alimenticia a los hijos, pensión alimenticia entre cónyuges y liquidación del régimen patrimonial del matrimonio. Adapta el contenido al perfil de práctica y a las posiciones habituales de la firma. Usar cuando el usuario dice "convenio de divorcio", "redacta un convenio", "divorcio por mutuo consentimiento", o necesita una plantilla.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/familia/skills/convenio
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: family
language: es
---

# /convenio

1. Leer `~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md` — perfil de práctica y posiciones habituales.
2. Recopilar datos de los cónyuges, menores e hijos mayores dependientes.
3. Determinar el régimen patrimonial del matrimonio aplicable.
4. Generar el convenio con las secciones propias del Código de la Familia de Panamá.
5. Ajustar a las posiciones habituales de la firma (si están configuradas).

---

## Propósito

Producir un borrador de convenio de divorcio por mutuo consentimiento completo que cumpla los requisitos del Código de la Familia de Panamá, adaptado a las circunstancias concretas de la pareja y a las posiciones habituales de la firma. Es un borrador — requiere revisión de abogado idóneo y, en mutuo consentimiento, la conformidad de ambas partes.

## Datos necesarios

- **Datos de los cónyuges:** nombres, cédula (o pasaporte/carné de residente si extranjero), domicilios, profesiones, ingresos netos mensuales.
- **Datos del matrimonio:** fecha, lugar de celebración, régimen patrimonial (capitulaciones o régimen legal supletorio).
- **Hijos menores de edad:** nombres, fechas de nacimiento, necesidades especiales.
- **Hijos mayores dependientes económicamente:** si los hay (p. ej. estudios).
- **Vivienda familiar:** propiedad (de quién), hipoteca pendiente, valor aproximado.
- **Otros bienes y deudas comunes:** vehículos, cuentas, inversiones, deudas.
- **Tipo de procedimiento:** divorcio por mutuo consentimiento o por causal (contencioso) ante el juzgado seccional de familia.

## Secciones habituales (Código de la Familia de Panamá)

### 1. Guarda y crianza

- **Guarda compartida:** distribución del tiempo (semanas alternas, 5-2-2-5, u otro modelo), domicilio de referencia del menor, decisiones ordinarias y extraordinarias.
- **Guarda exclusiva:** progenitor guardador, régimen de comunicación y visitas del no guardador.
- **Criterio rector:** interés superior del menor (principio recogido en el Código de la Familia).
- **Patria potestad:** ejercida por ambos progenitores salvo circunstancias excepcionales.

### 2. Régimen de comunicación y visitas

- Fines de semana alternos (viernes a domingo o jueves a lunes).
- Tarde intersemanal.
- Vacaciones: fin de año, Carnaval, Semana Santa, vacaciones escolares — reparto por mitades, años pares/impares.
- Días señalados: cumpleaños de los hijos, día del padre/madre, festividades nacionales.
- Comunicaciones telefónicas y telemáticas.

### 3. Uso de la vivienda familiar

- Atribución al progenitor guardador o a los hijos.
- Temporalidad — posibilidad de limitar temporalmente la atribución hasta la liquidación.
- Compensación por uso si la vivienda es de ambos o del no guardador.

### 4. Pensión alimenticia a los hijos

- Cuantía mensual por hijo, en balboas (B/.) / USD.
- Actualización periódica (índice de precios al consumidor u otro criterio).
- Gastos ordinarios incluidos.
- Gastos extraordinarios: clasificación y reparto.
- Forma de pago y cuenta de ingreso.
- Para cálculo detallado: `/familia:pensiones`.

### 5. Pensión alimenticia entre cónyuges

- Existencia de necesidad y posibilidad de prestarla.
- Cuantía y duración (temporal o indefinida).
- Criterios: dedicación a la familia, duración del matrimonio, edad, cualificación, estado de salud.
- Causas de extinción.

### 6. Liquidación del régimen patrimonial del matrimonio

- Si **sociedad de gananciales:** inventario de bienes comunes y propios, avalúo, propuesta de adjudicación.
- Si **separación de bienes:** división de bienes en copropiedad, compensación por trabajo doméstico si procede.
- Si **participación en las ganancias:** cálculo de las ganancias y del crédito de participación.
- Puede incluirse en el convenio o tramitarse en proceso separado.

## Formato de salida

```markdown
BORRADOR — CONVENIO DE DIVORCIO POR MUTUO CONSENTIMIENTO — REVISIÓN DE ABOGADO OBLIGATORIA

> **Nota para el revisor**
> - **Régimen patrimonial:** [gananciales / separación de bienes / participación — cuál]
> - **Elementos marcados [verificar]:** [N]
> - **Antes de actuar:** verificar datos patrimoniales; confirmar régimen patrimonial; revisar cálculo de pensiones; obtener conformidad de ambas partes.

## CONVENIO DE DIVORCIO POR MUTUO CONSENTIMIENTO

[Nombre], con cédula [X], y [nombre], con cédula [X], de común acuerdo y a los efectos previstos en el Código de la Familia de Panamá, otorgan el presente convenio:

### PRIMERO. — Guarda y crianza
[Contenido adaptado a los datos y posiciones de la firma]

### SEGUNDO. — Régimen de comunicación y visitas
[Contenido]

### TERCERO. — Uso de la vivienda familiar
[Contenido]

### CUARTO. — Pensión alimenticia a los hijos
[Contenido con cuantía en B/. / USD, actualización y gastos extraordinarios]

### QUINTO. — Pensión alimenticia entre cónyuges
[Contenido o "Las partes renuncian expresamente a la pensión alimenticia entre cónyuges"]

### SEXTO. — Liquidación del régimen patrimonial del matrimonio
[Contenido según régimen aplicable]

### SÉPTIMO. — Ajuar doméstico
[Reparto]

### OCTAVO. — Seguros y fondos de pensiones
[Si aplica]

### NOVENO. — Efectos fiscales
[Atribución de beneficios fiscales conforme a la legislación de la DGI, declaración del ISR]

En [ciudad], a [fecha].

[Firma] — [Firma]
```

## Referencias legislativas

- **Código de la Familia de Panamá** — efectos del divorcio y de la separación; nulidad del matrimonio. [verificar arts.]
- **Código de la Familia** — patria potestad, guarda y crianza. [verificar arts.]
- **Código de la Familia** — alimentos a los hijos y entre parientes. [verificar arts.]
- **Código de la Familia** — uso de la vivienda familiar. [verificar arts.]
- **Código de la Familia** — pensión alimenticia entre cónyuges. [verificar arts.]
- **Código de la Familia** — régimen patrimonial del matrimonio y compensación por trabajo doméstico. [verificar arts.]
- **Código Judicial de Panamá** — procedimiento de divorcio por mutuo consentimiento ante el juzgado seccional de familia. [verificar arts.]
- **Interés superior del menor** — principio rector recogido en el Código de la Familia.

## Guardarraíles

- **No asumir gananciales.** Verificar siempre si hay capitulaciones matrimoniales y cuál es el régimen pactado o el legal supletorio aplicable.
- **El interés superior del menor prevalece siempre.** Por encima de las preferencias de las partes y de los defaults de la firma.
- **No presentar la guarda compartida como "lo normal".** Es una opción más — depende de las circunstancias del caso, la edad de los hijos y la capacidad de cooperación de los progenitores.
- **La renuncia a la pensión alimenticia entre cónyuges debe ser informada.** Si hay necesidad evidente, advertir de las consecuencias de la renuncia.
- **No olvidar la compensación por trabajo doméstico.** En separación de bienes, el cónyuge dedicado al hogar puede tener derecho. Muchos lo olvidan. [verificar base legal]
- **Si hay indicios de violencia doméstica, PARAR.** No es un caso de convenio ordinario — derivar a las autoridades competentes (Ley 82 de 2013 sobre femicidio y violencia contra la mujer [verificar]) y a recursos especializados.
