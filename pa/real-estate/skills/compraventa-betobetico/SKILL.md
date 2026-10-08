---
name: compraventa-betobetico
title: /compraventa
description: Compraventa inmobiliaria — revisa un contrato de compraventa de inmueble bajo derecho panameño. Comprueba arras, gravámenes inscritos (certificado del Registro Público), condiciones suspensivas, escritura pública y fiscalidad (ITBI, ganancia de capital). Usar cuando el usuario diga "compraventa de apartamento", "revisar arras", "contrato de compraventa", "certificado del Registro Público", "fiscalidad de la compra" o adjunte un contrato.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/inmobiliario/skills/compraventa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

# /compraventa

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el contrato o la descripción de la operación.
3. Analizar la estructura de la operación (arras, condiciones, escritura).
4. Verificar gravámenes inscritos si se facilita certificado del Registro Público.
5. Determinar régimen fiscal.
6. Generar informe de revisión.

```
/inmobiliario:compraventa
Vamos a comprar un local comercial de segunda mano por 300.000 USD.
El vendedor es una sociedad anónima. Revisar la fiscalidad y el contrato de arras.
```

---

## Propósito

La compraventa inmobiliaria en Panamá combina derecho civil (Código Civil de Panamá), inscripción registral (Registro Público de Panamá), administración de tierras y catastro (ANATI), normativa fiscal (ITBI, ganancia de capital, ITBMS cuando aplica) y práctica notarial. Un error en cualquiera de estos ámbitos puede tener consecuencias graves: gravámenes ocultos, fiscalidad incorrecta, pérdida de arras o imposibilidad de inscripción. Este skill revisa cada aspecto de la operación.

---

## Estructura de la operación

### 1. Arras / contrato de promesa de compraventa

| Tipo de arras | Base legal | Efecto |
|---|---|---|
| **Penitenciales / de desistimiento** | Art. 1224 del Código Civil de Panamá | Permiten desistir: comprador pierde las arras; vendedor las devuelve dobladas |
| **Confirmatorias** | Categoría doctrinal / jurisprudencial (sin texto legal expreso) | Señal de cumplimiento; no permiten desistir — incumplimiento → resolver + daños |
| **Penales** | Pacto expreso (cláusula penal) | Penalización por incumplimiento que no sustituye la obligación de cumplir (salvo pacto) |

**Clave:** el art. 1224 del Código Civil de Panamá recoge únicamente las arras penitenciales / de desistimiento (rescindir perdiéndolas o devolviéndolas dobladas); las arras confirmatorias son una categoría doctrinal/jurisprudencial, no de texto legal expreso. No confundir con el art. 1221, que regula la promesa de compraventa. Si el contrato no especifica el tipo, debe interpretarse conforme al Código Civil de Panamá y la intención de las partes; es esencial que el tipo quede expresamente pactado. En Panamá es habitual instrumentar la operación mediante un **contrato de promesa de compraventa**.

**Verificar en el contrato de promesa / arras:**
- [ ] Tipo de arras expresamente indicado
- [ ] Importe y forma de pago (en B/. o USD)
- [ ] Plazo para otorgar la escritura pública
- [ ] Condiciones suspensivas (si las hay)
- [ ] Descripción del inmueble coincidente con el Registro Público (finca, tomo/rollo, documento/folio o folio real)
- [ ] Manifestación de gravámenes y limitaciones
- [ ] Situación posesoria (libre de ocupantes o no)
- [ ] Reparto de gastos (escritura, impuestos, registro, ganancia de capital)

### 2. Gravámenes inscritos (certificado del Registro Público)

Si se facilita certificado del Registro Público, verificar:

| Aspecto | Verificar |
|---|---|
| **Titularidad** | ¿El vendedor es el titular registral? ¿Cotitularidad? Si es sociedad anónima, ¿quién la representa? |
| **Descripción** | ¿Coincide con la realidad (superficie, linderos, uso)? Concordancia con el catastro de ANATI |
| **Gravámenes** | Hipotecas, anticresis, embargos, secuestros, servidumbres, arrendamientos inscritos |
| **Afectaciones / limitaciones** | Patrimonio familiar, prohibiciones de enajenar, fideicomisos, afectaciones urbanísticas |
| **Régimen de propiedad horizontal** | Si procede: coeficiente de participación, anexos (estacionamiento, depósito) bajo la Ley 284 de 2022 |

**Gravámenes que deben cancelarse antes o en el acto de escritura:**
- Hipotecas → cancelación o subrogación
- Embargos / secuestros → levantamiento o pago
- Anotaciones / medidas cautelares → verificar vigencia [verificar]

### 3. Condiciones suspensivas habituales

- Obtención de financiación hipotecaria por el comprador
- Cancelación de gravámenes por el vendedor
- Obtención del permiso de ocupación (obra nueva)
- Paz y salvo de impuesto de inmueble y de cuotas de propiedad horizontal
- Concordancia de la finca con el catastro de ANATI

### 4. Escritura pública e inscripción

| Paso | Verificar |
|---|---|
| **Escritura pública** | Otorgada ante notario; necesaria para la inscripción en el Registro Público y la oponibilidad frente a terceros |
| **Inscripción en el Registro Público** | Entre las partes la transferencia se perfecciona por la escritura pública; frente a terceros se perfecciona con la inscripción (publicidad y prioridad registral) — arts. 1753-1762 del Código Civil de Panamá (en particular art. 1762) |
| **Medios de pago** | Identificación de los medios de pago conforme a la prevención de blanqueo (Ley 23 de 2015, arts. 22 y ss.; promotores y agentes/corredores son sujetos obligados no financieros supervisados por la Superintendencia de Sujetos No Financieros, con reportes a la UAF) — transferencia, cheque de gerencia |
| **Retención por ganancia de capital** | El comprador retiene el 3% del mayor entre el valor de venta y el catastral como adelanto de la ganancia de capital del vendedor (Formulario 107) y lo entera ante la DGI (art. 701 del Código Fiscal y Decreto Ejecutivo 170 de 1993) |

---

## Fiscalidad de la compraventa

### Impuestos principales en Panamá

| Concepto | Impuesto | Notas |
|---|---|---|
| **Transferencia de inmueble** | **ITBI** — Impuesto de Transferencia de Bienes Inmuebles | Tarifa del 2% sobre el mayor entre (i) el valor de la escritura y (ii) el valor catastral de adquisición + mejoras + 5% del valor catastral por cada año transcurrido; a cargo del vendedor (Formulario 106); requisito para inscribir (art. 701, lit. g, del Código Fiscal — Ley 106 de 1974) |
| **Ganancia de capital** | Impuesto sobre la ganancia de capital | 10% sobre la ganancia, con retención anticipada del 3% del mayor entre el valor de venta y el catastral (la retiene el comprador, Formulario 107); el vendedor puede optar por el 3% como definitivo o pedir devolución del excedente (art. 701 del Código Fiscal y Decreto Ejecutivo 170 de 1993). **Promotores / giro ordinario:** tarifa única y definitiva del 3,75% sobre el mayor entre valor de enajenación y catastral; vivienda nueva con escala progresiva 0,5%-2,5% (4,5% comercial) |
| **ITBMS** | Impuesto de Transferencia de Bienes Muebles y Servicios | No grava la transferencia de inmuebles (art. 1057-V del Código Fiscal); verificar su incidencia en servicios asociados |

**Principio de territorialidad:** la fiscalidad panameña grava la renta de fuente panameña; la ganancia por la venta de inmuebles situados en Panamá es de fuente panameña. [verificar]

### Otros impuestos y obligaciones

| Concepto | Sujeto pasivo | Notas |
|---|---|---|
| **Impuesto de inmueble** | Titular del inmueble | Anual; verificar exoneraciones (p. ej. patrimonio familiar tributario / vivienda principal) y que esté al día (paz y salvo) [verificar] |
| **Paz y salvo nacional (DGI)** | Vendedor | Para inscribir se requieren el paz y salvo del impuesto de inmueble (DGI) y el paz y salvo municipal, más la acreditación del pago del ITBI (Formulario 106) y del 3% de ganancia de capital (Formulario 107) |
| **Cuotas de propiedad horizontal** | Vendedor (al corriente) | Certificación de no adeudo de la administración (Ley 284 de 2022) |

---

## Formato de salida

```markdown
# Revisión de compraventa inmobiliaria

**Inmueble:** [dirección, finca / folio real, corregimiento]
**Vendedor:** [persona natural / sociedad anónima]
**Comprador:** [persona natural / jurídica]
**Precio:** [importe en B/. o USD]
**Fecha de la operación:** [fecha prevista]

---

## Estructura de la operación

| Fase | Estado | Observaciones |
|---|---|---|
| Promesa de compraventa / arras | [Firmado / Pendiente] | [tipo de arras, importe] |
| Due diligence registral | [Realizado / Pendiente] | [certificado del Registro Público obtenido/pendiente] |
| Escritura pública | [Pendiente] | [notaría, fecha prevista] |
| Inscripción en el Registro Público | [Pendiente] | |

---

## Gravámenes inscritos

| Gravamen | Tipo | Estado | Acción |
|---|---|---|---|
| [Ej., Hipoteca Banco X] | Gravamen | Vigente | Cancelar en escritura |
| [Ej., Embargo] | Medida cautelar | Vigente | Levantar antes de escritura |

---

## Fiscalidad

| Concepto | Régimen | Tarifa | Importe estimado | Sujeto pasivo |
|---|---|---|---|---|
| ITBI | Transferencia de inmueble | 2% (Formulario 106; art. 701-g Código Fiscal) | [importe] | [vendedor] |
| Ganancia de capital | Retención anticipada | 3% del mayor entre valor de venta y catastral / 10% sobre ganancia (Formulario 107) | [importe] | [vendedor / retiene comprador] |
| Impuesto de inmueble | Paz y salvo | — | [al día] | [vendedor] |

---

## Hallazgos del contrato

| # | Cláusula | Observación | Riesgo | Recomendación |
|---|---|---|---|---|
| 1 | [Ej., Tipo de arras no especificado] | Ambigüedad sobre desistimiento | Alto | Especificar expresamente |
| 2 | [Ej., Sin retención por ganancia de capital] | Riesgo fiscal para el comprador | Medio | Incluir cláusula de retención |
| ... | ... | ... | ... | ... |

---

## Checklist pre-escritura

- [ ] Certificado del Registro Público actualizado (próximo a la fecha de escritura)
- [ ] Paz y salvo de impuesto de inmueble
- [ ] Paz y salvo nacional (DGI) del impuesto de inmueble y paz y salvo municipal del vendedor
- [ ] Certificación de no adeudo de cuotas de propiedad horizontal (Ley 284 de 2022)
- [ ] Permiso de ocupación (obra nueva) si aplica
- [ ] Medios de pago preparados (transferencia / cheque de gerencia) y cumplimiento de prevención de blanqueo (Ley 23 de 2015)
```

---

## Legislación de referencia

- Código Civil de Panamá — compraventa, arras (art. 1224), promesa de compraventa (art. 1221), derechos reales, hipoteca, inscripción (arts. 1753-1762, en particular 1762)
- Registro Público de Panamá — inscripción de la propiedad y gravámenes
- ANATI — catastro y administración de tierras
- ITBI — art. 701, lit. g) del Código Fiscal (Ley 106 de 1974); Formulario 106
- Ganancia de capital — art. 701 del Código Fiscal y Decreto Ejecutivo 170 de 1993; Formulario 107 (incl. régimen de promotores 3,75% y vivienda nueva 0,5%-2,5%)
- Art. 1057-V del Código Fiscal — el ITBMS no grava la transferencia de inmuebles
- Ley 284 de 2022 — propiedad horizontal (certificación de no adeudo)
- Ley 23 de 2015 (arts. 22 y ss.) — prevención de blanqueo; promotores y agentes/corredores como sujetos obligados no financieros (Superintendencia de Sujetos No Financieros, UAF)

---

## Lo que este skill NO hace

- No realiza la due diligence de uso de suelo / urbanística completa (permisos, planeamiento, situación urbanística) — marca cuándo es necesaria.
- No tramita la inscripción en el Registro Público — indica los pasos.
- No calcula impuestos con precisión definitiva — indica el régimen aplicable y remite al cálculo específico ante la DGI.
