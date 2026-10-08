---
name: arrendamiento-3187-betobetico
title: /arrendamiento
description: Revisor de arrendamiento — revisa un contrato de arrendamiento contra la LAU 29/1994 reformada. Distingue entre vivienda (Título II) y uso distinto (Título III). Comprueba duración, renta, actualización, fianza, obras y resolución. Marca cláusulas contrarias a la LAU (nulas en vivienda). Usar cuando el usuario diga "revisa este alquiler", "contrato de arrendamiento", "¿es legal esta cláusula del alquiler?", "LAU".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/inmobiliario/skills/arrendamiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# /arrendamiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual (arrendador/arrendatario).
2. Obtener el contrato.
3. Determinar tipo: vivienda (Título II LAU) vs uso distinto de vivienda (Título III LAU).
4. Revisar cláusula por cláusula contra la LAU.
5. Marcar cláusulas nulas (en vivienda) o de riesgo.

```
/inmobiliario:arrendamiento
[pegar el contrato de alquiler de vivienda]
```

---

## Propósito

La LAU (Ley 29/1994, reformada por RDL 7/2019 y Ley 12/2023 de Vivienda) establece un régimen imperativo para los arrendamientos de vivienda (Título II) — las cláusulas contrarias son nulas y se sustituyen por la norma legal. En arrendamientos de uso distinto (Título III), la autonomía de la voluntad es amplia. Distinguir correctamente el tipo de arrendamiento es el paso más importante.

---

## Paso 1: ¿Vivienda o uso distinto?

| Criterio | Vivienda (Título II) | Uso distinto (Título III) |
|---|---|---|
| **Destino** | Satisfacer necesidad permanente de vivienda del arrendatario | Local de negocio, oficina, almacén, temporada, garaje independiente |
| **Régimen** | Imperativo (art. 6 LAU) — irrenunciabilidad de derechos del arrendatario | Dispositivo — autonomía de voluntad (art. 4.3 LAU) |
| **Norma aplicable** | Título II LAU + supletoriamente CC | Voluntad de las partes → Título III LAU → CC |

**Arrendamientos de temporada:** son uso distinto de vivienda aunque el inmueble sea una vivienda (art. 3.2 LAU). Verificar que realmente es temporal y no un uso fraudulento para eludir el Título II.

---

## Revisión de arrendamiento de VIVIENDA (Título II LAU)

### Duración (art. 9-10 LAU, reforma RDL 7/2019 y Ley 12/2023)

| Aspecto | Norma | Verificar |
|---|---|---|
| **Duración mínima** | 5 años (persona física) / 7 años (persona jurídica) — art. 9 LAU | ¿El contrato respeta la prórroga obligatoria? |
| **Prórroga tácita** | 3 años adicionales si ninguna parte comunica la no renovación con 4 meses (arrendador) o 2 meses (arrendatario) de antelación — art. 10 LAU | ¿Se respetan los plazos de preaviso? |
| **Desistimiento del arrendatario** | Posible tras 6 meses, con 30 días de preaviso (art. 11 LAU); indemnización de 1 mes por año restante si se pactó | ¿Se ha pactado indemnización? |

### Renta (arts. 17-20 LAU)

| Aspecto | Norma | Verificar |
|---|---|---|
| **Renta inicial** | Libre (art. 17.1) — salvo zona de mercado residencial tensionado (Ley 12/2023) | ¿Aplica limitación de renta por zona tensionada? |
| **Actualización anual** | Solo si se pacta; límite: índice de referencia de IRAV (antes IPC/IGC) — art. 18 LAU tras Ley 12/2023 | ¿El índice pactado es conforme? |
| **Gastos generales e impuestos** | Repercutibles al arrendatario solo si se pacta (art. 20 LAU) | ¿Se ha pactado expresamente? |
| **Mejoras que incrementan renta** | Solo después del 5.o/7.o año (art. 19 LAU) | ¿Se pacta indebidamente antes? |

### Fianza (art. 36 LAU)

| Aspecto | Norma |
|---|---|
| **Fianza obligatoria** | 1 mensualidad (vivienda) — art. 36.1 |
| **Garantías adicionales** | Máximo 2 mensualidades adicionales (art. 36.5, reforma RDL 7/2019) cuando arrendador es persona jurídica → total máximo 3 meses |
| **Depósito** | En el organismo autonómico correspondiente (INCASOL, IVIMA, etc.) |
| **Actualización** | No se actualiza durante los 5/7 primeros años (art. 36.2) |

### Obras (arts. 21-24 LAU)

| Tipo | Régimen |
|---|---|
| **Conservación (arrendador)** | Obligación del arrendador sin derecho a elevar renta (art. 21) |
| **Mejoras (arrendador)** | Puede elevar renta solo tras 5.o/7.o año; 3 meses de preaviso al arrendatario (art. 22) |
| **Obras del arrendatario** | Sin consentimiento del arrendador: prohibidas salvo adaptación para discapacidad (art. 24) |

### Resolución (art. 27 LAU)

| Causa de resolución por arrendador | Causa de resolución por arrendatario |
|---|---|
| Falta de pago de renta (art. 27.2.a) | No realización de reparaciones necesarias (art. 27.3.a) |
| Subarriendo no consentido (art. 27.2.c) | Perturbación del arrendador en el uso (art. 27.3.b) |
| Daños dolosos o realización de obras no consentidas (art. 27.2.d) | |
| Actividades molestas, insalubres, nocivas, peligrosas o ilícitas (art. 27.2.e) | |
| No destinar a vivienda permanente (art. 27.2.f) | |

### Cláusulas nulas en vivienda (art. 6 LAU)

**Son nulas y se tienen por no puestas** las cláusulas que modifiquen en perjuicio del arrendatario las normas del Título II (salvo las que la propia ley autorice). Ejemplos habituales de cláusulas nulas:

- Renuncia a la prórroga obligatoria de 5/7 años
- Fianza superior a 1 mes + 2 meses de garantía adicional (si arrendador PJ)
- Repercusión de gastos de formalización o gestión inmobiliaria al arrendatario cuando el arrendador es persona jurídica (art. 20.1 LAU)
- Actualización de renta por índice superior al permitido
- Renuncia al derecho de adquisición preferente sin constancia registral

---

## Revisión de arrendamiento de USO DISTINTO (Título III LAU)

En uso distinto, prima la autonomía de la voluntad. La revisión se centra en:

| Aspecto | Verificar |
|---|---|
| Duración y prórrogas | ¿Son las pactadas razonables para el negocio? |
| Renta y actualización | Libre; ¿el índice es claro y aplicable? |
| Fianza | 2 mensualidades obligatorias (art. 36.1 LAU); garantías adicionales libres |
| Obras y mejoras | ¿Quién las asume? ¿Derecho de remoción al finalizar? |
| Cesión y subarriendo | ¿Se permite? Régimen del art. 32 LAU |
| Resolución anticipada | Causas pactadas; ¿penalización equilibrada? |
| Indemnización por clientela | Art. 34 LAU — derecho a indemnización si no se renueva y el arrendatario tenía actividad comercial abierta al público |

---

## Formato de salida

```markdown
# Revisión de arrendamiento: [Dirección del inmueble]

**Tipo:** [Vivienda (Título II) / Uso distinto (Título III)]
**Arrendador:** [persona física / jurídica]
**Fecha del contrato:** [fecha]
**Duración pactada:** [años]

---

## Resultado global

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Nula

---

## Detalle por cláusula

| # | Cláusula | Lo que dice el contrato | Norma aplicable | Riesgo | Observación |
|---|---|---|---|---|---|
| 1 | Duración | [Ej., 1 año sin prórroga] | Art. 9 LAU | Nula | Mínimo 5/7 años de prórroga obligatoria |
| 2 | Fianza | [Ej., 3 meses + 3 de garantía] | Art. 36 LAU | Nula (si PJ) | Máximo 1+2 si arrendador PJ |
| ... | ... | ... | ... | ... | ... |

---

## Cláusulas nulas (solo vivienda)

[Lista de cláusulas contrarias al Título II LAU con consecuencia: se sustituyen por la norma legal]

---

## Recomendaciones

[Ajustes recomendados para que el contrato sea conforme]
```

---

## Legislación de referencia

- LAU (Ley 29/1994) de Arrendamientos Urbanos, reformada por:
  - RDL 7/2019, de 1 de marzo
  - Ley 12/2023, de 24 de mayo, por el derecho a la vivienda
- Código Civil arts. 1542-1582 (supletorio)
- Legislación autonómica sobre depósito de fianzas

---

## Lo que este skill NO hace

- No redacta contratos de arrendamiento desde cero — revisa los existentes.
- No determina si una zona es "mercado residencial tensionado" — indica cuándo verificarlo.
- No tramita el depósito de fianza en el organismo autonómico.
