---
name: arrendamiento-betobetico
title: /arrendamiento
description: Revisor de arrendamiento — revisa un contrato de arrendamiento contra el régimen de arrendamientos panameño. Distingue entre arrendamiento de vivienda (régimen tutelado) y arrendamiento comercial/uso distinto. Comprueba duración, canon, actualización, depósito de garantía, mejoras y resolución. Marca cláusulas contrarias a la ley. Usar cuando el usuario diga "revisa este alquiler", "contrato de arrendamiento", "¿es legal esta cláusula del alquiler?", "arrendamiento".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/inmobiliario/skills/arrendamiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

# /arrendamiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual (arrendador/arrendatario).
2. Obtener el contrato.
3. Determinar tipo: arrendamiento de vivienda (régimen tutelado) vs arrendamiento comercial / uso distinto.
4. Revisar cláusula por cláusula contra la legislación de arrendamientos panameña.
5. Marcar cláusulas nulas o de riesgo.

```
/inmobiliario:arrendamiento
[pegar el contrato de alquiler de vivienda]
```

---

## Propósito

En Panamá los arrendamientos de vivienda están sujetos a un régimen tutelado regulado por la **Ley 93 de 1973** ("por la cual se dictan medidas sobre los arrendamientos"), modificada por la Ley 28 de 1974 y la Ley 259 de 2021, que fija reglas imperativas de protección al arrendatario; las cláusulas contrarias se tienen por no puestas. El órgano competente es la **Dirección General de Arrendamientos del MIVIOT**. Los arrendamientos comerciales o de uso distinto a vivienda también están alcanzados por la Ley 93 de 1973, y supletoriamente por el Código Civil de Panamá. Distinguir correctamente el tipo de arrendamiento es el paso más importante.

> **Nota sobre umbrales de canon:** Históricamente la Ley 93 de 1973 excluía los arrendamientos de vivienda con canon superior a B/.150/mes (Decreto Ejecutivo 294 de 1994), dejándolos a libre contratación. Sin embargo, el Decreto Ejecutivo 145 de 2020 suspendió ese umbral y facultó al MIVIOT a conocer de todos los contratos sin distinción de monto. Por tanto, no debe afirmarse un umbral fijo vigente sin más; los locales comerciales también están regulados por la Ley 93 de 1973 (verificar en el texto oficial).

---

## Paso 1: ¿Vivienda (régimen tutelado) o uso distinto?

| Criterio | Vivienda (régimen tutelado) | Uso distinto / comercial |
|---|---|---|
| **Destino** | Satisfacer necesidad de vivienda del arrendatario | Local comercial, oficina, depósito, temporada, estacionamiento independiente |
| **Régimen** | Imperativo (protección al arrendatario) — irrenunciabilidad de derechos (Ley 93 de 1973) | Dispositivo — autonomía de la voluntad (Ley 93 de 1973 + Código Civil de Panamá) |
| **Norma aplicable** | Ley 93 de 1973 (mod. Ley 28 de 1974 y Ley 259 de 2021) + supletoriamente Código Civil de Panamá | Ley 93 de 1973 y voluntad de las partes → Código Civil de Panamá |

**Arrendamientos de temporada / amueblados de corto plazo:** suelen quedar fuera del régimen tutelado de vivienda. Verificar que realmente es temporal y no un uso fraudulento para eludir la protección del arrendatario. [verificar]

---

## Revisión de arrendamiento de VIVIENDA (régimen tutelado)

### Duración y prórroga

| Aspecto | Norma | Verificar |
|---|---|---|
| **Duración mínima / prórroga** | Ley 93 de 1973 (verificar en el texto oficial) | ¿El contrato respeta la protección del arrendatario frente al desalojo? |
| **Renovación** | Según pacto y ley aplicable [verificar] | ¿Se respetan los plazos de preaviso? |
| **Desistimiento del arrendatario** | Según pacto y ley aplicable [verificar] | ¿Se ha pactado indemnización? |

### Canon de arrendamiento

| Aspecto | Norma | Verificar |
|---|---|---|
| **Canon inicial** | Libre fijación, salvo límites del régimen tutelado [verificar] | ¿Aplica algún tope o control de canon? |
| **Actualización** | Solo si se pacta, dentro de los límites legales [verificar] | ¿El criterio pactado es conforme? |
| **Moneda** | Balboas (B/.) / dólares estadounidenses (USD) | ¿El canon está expresado en B/. o USD? |
| **Gastos e impuestos** | Repercutibles al arrendatario solo si se pacta | ¿Se ha pactado expresamente? |

### Depósito de garantía

| Aspecto | Norma |
|---|---|
| **Depósito de garantía** | Un (1) mes de canon (art. 13 de la Ley 93 de 1973, mod. Ley 259 de 2021) |
| **Custodia del depósito** | Se consigna ante la Dirección General de Arrendamientos del MIVIOT (no lo retiene el arrendador); desde la Ley 259 de 2021 se canaliza por la banca estatal (art. 13 de la Ley 93 de 1973) |
| **Devolución** | Al término del contrato, con intereses, descontando daños o cánones pendientes (Ley 259 de 2021) |

### Mejoras y reparaciones

| Tipo | Régimen |
|---|---|
| **Conservación (arrendador)** | Obligación del arrendador mantener el inmueble en estado de servir al uso pactado (Código Civil de Panamá) |
| **Mejoras (arrendador)** | Régimen según pacto y ley aplicable [verificar] |
| **Obras del arrendatario** | Sin consentimiento del arrendador: en principio prohibidas; verificar excepciones [verificar] |

### Resolución / desalojo

| Causa de resolución por arrendador | Causa de resolución por arrendatario |
|---|---|
| Falta de pago del canon [verificar] | Incumplimiento de reparaciones necesarias |
| Subarriendo no consentido | Perturbación del arrendador en el uso |
| Daños dolosos u obras no consentidas | |
| Uso distinto al pactado / actividades ilícitas | |

**Nota procesal:** El desalojo (desahucio / lanzamiento) en arrendamientos sujetos al régimen tutelado se tramita por vía gubernativa ante la Dirección General de Arrendamientos del MIVIOT, con reconsideración ante la propia Dirección y apelación ante el Ministro del MIVIOT antes de acudir a lo contencioso-administrativo (Ley 93 de 1973).

### Cláusulas nulas en vivienda (régimen tutelado)

**Se tienen por no puestas** las cláusulas que modifiquen en perjuicio del arrendatario las normas imperativas del régimen tutelado. Ejemplos habituales de cláusulas de riesgo:

- Renuncia anticipada del arrendatario a la protección frente al desalojo [verificar]
- Depósito de garantía superior al permitido por la ley [verificar]
- Repercusión de gastos de gestión o formalización al arrendatario cuando la ley no lo permite [verificar]
- Actualización de canon por encima del límite legal [verificar]
- Cláusulas de desalojo automático sin el debido proceso

---

## Revisión de arrendamiento de USO DISTINTO / COMERCIAL

En uso distinto, prima la autonomía de la voluntad bajo el Código Civil de Panamá. La revisión se centra en:

| Aspecto | Verificar |
|---|---|
| Duración y prórrogas | ¿Son razonables para el negocio? |
| Canon y actualización | Libre; ¿el criterio es claro y aplicable? ¿Moneda en B/. o USD? |
| Depósito de garantía | Libre pacto |
| Obras y mejoras | ¿Quién las asume? ¿Derecho de remoción al finalizar? |
| Cesión y subarriendo | ¿Se permite? Régimen según pacto y Código Civil de Panamá |
| Resolución anticipada | Causas pactadas; ¿penalización equilibrada? |
| Mejoras del local | ¿Quién paga la adecuación? ¿Reversión al arrendador? |

---

## Formato de salida

```markdown
# Revisión de arrendamiento: [Dirección del inmueble]

**Tipo:** [Vivienda (régimen tutelado) / Uso distinto - comercial]
**Arrendador:** [persona natural / jurídica]
**Fecha del contrato:** [fecha]
**Duración pactada:** [años]

---

## Resultado global

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Nula

---

## Detalle por cláusula

| # | Cláusula | Lo que dice el contrato | Norma aplicable | Riesgo | Observación |
|---|---|---|---|---|---|
| 1 | Duración | [Ej., 1 año sin prórroga] | Ley 93 de 1973 | Riesgo | Verificar protección del arrendatario |
| 2 | Depósito de garantía | [Ej., 3 cánones] | Art. 13 Ley 93 de 1973 (mod. Ley 259 de 2021) | Riesgo | El depósito es de un (1) mes y se consigna ante el MIVIOT |
| ... | ... | ... | ... | ... | ... |

---

## Cláusulas nulas (solo vivienda)

[Lista de cláusulas contrarias al régimen tutelado con consecuencia: se tienen por no puestas]

---

## Recomendaciones

[Ajustes recomendados para que el contrato sea conforme]
```

---

## Legislación de referencia

- Ley 93 de 1973 (mod. Ley 28 de 1974 y Ley 259 de 2021) — medidas sobre los arrendamientos
- Decreto Ejecutivo 145 de 2020 — suspensión del umbral de canon (sin distinción de monto)
- Código Civil de Panamá — supletorio en lo no previsto por la Ley 93 de 1973 (verificar en el texto oficial; no hay artículo de remisión expreso)
- MIVIOT (Ministerio de Vivienda y Ordenamiento Territorial) — Dirección General de Arrendamientos, autoridad competente en arrendamientos

---

## Lo que este skill NO hace

- No redacta contratos de arrendamiento desde cero — revisa los existentes.
- No determina si un canon queda dentro o fuera del régimen tutelado — indica cuándo verificarlo.
- No tramita la consignación del depósito de garantía ante la autoridad de vivienda.
