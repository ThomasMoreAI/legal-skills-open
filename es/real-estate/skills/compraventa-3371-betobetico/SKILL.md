---
name: compraventa-3371-betobetico
title: /compraventa
description: Compraventa inmobiliaria — revisa un contrato de compraventa de inmueble. Comprueba arras, cargas registrales (nota simple), condiciones suspensivas, escritura pública y fiscalidad (ITP vs IVA+AJD). Usar cuando el usuario diga "compraventa de piso", "revisar arras", "contrato de compraventa", "nota simple", "fiscalidad de la compra" o adjunte un contrato.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/inmobiliario/skills/compraventa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# /compraventa

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el contrato o la descripción de la operación.
3. Analizar la estructura de la operación (arras, condiciones, escritura).
4. Verificar cargas registrales si se facilita nota simple.
5. Determinar régimen fiscal.
6. Generar informe de revisión.

```
/inmobiliario:compraventa
Vamos a comprar un local comercial de segunda mano por 300.000 EUR.
El vendedor es una sociedad. Revisar la fiscalidad y el contrato de arras.
```

---

## Propósito

La compraventa inmobiliaria en España combina derecho civil (Código Civil), derecho hipotecario (Ley Hipotecaria), normativa fiscal (ITP/IVA/AJD) y práctica notarial/registral. Un error en cualquiera de estos ámbitos puede tener consecuencias graves: cargas ocultas, fiscalidad incorrecta, pérdida de arras o imposibilidad de inscripción. Este skill revisa cada aspecto de la operación.

---

## Estructura de la operación

### 1. Arras / contrato preparatorio

| Tipo de arras | Art. CC | Efecto |
|---|---|---|
| **Penitenciales** | Art. 1454 CC | Permiten desistir: comprador pierde las arras; vendedor devuelve el doble |
| **Confirmatorias** | Art. 1124 CC (interpretación jurisprudencial) | Señal de cumplimiento; no permiten desistir — incumplimiento → resolver + daños |
| **Penales** | Pacto expreso | Penalización por incumplimiento que no sustituye la obligación de cumplir (salvo pacto) |

**Clave:** si el contrato no especifica el tipo, la jurisprudencia las interpreta como **confirmatorias** (STS, interpretación restrictiva del art. 1454 CC). Es esencial que el tipo quede expresamente pactado.

**Verificar en el contrato de arras:**
- [ ] Tipo de arras expresamente indicado
- [ ] Importe y forma de pago
- [ ] Plazo para otorgar escritura pública
- [ ] Condiciones suspensivas (si las hay)
- [ ] Descripción del inmueble coincidente con el Registro
- [ ] Manifestación de cargas y gravámenes
- [ ] Situación posesoria (libre de ocupantes o no)
- [ ] Reparto de gastos (escritura, impuestos, registro, plusvalía)

### 2. Cargas registrales (nota simple)

Si se facilita nota simple, verificar:

| Aspecto | Verificar |
|---|---|
| **Titularidad** | ¿El vendedor es el titular registral? ¿Cotitularidad? |
| **Descripción** | ¿Coincide con la realidad (superficie, linderos, uso)? |
| **Cargas** | Hipotecas, embargos, anotaciones preventivas, servidumbres, arrendamientos inscritos |
| **Afecciones fiscales** | Afección real por ITP/IVA (4 años — art. 79 LGT) o plusvalía municipal (5 años) |
| **Limitaciones urbanísticas** | Fuera de ordenación, expediente de disciplina, afectaciones |
| **Régimen de propiedad horizontal** | Si procede: cuota de participación, anejos (garaje, trastero) |

**Cargas que deben cancelarse antes o en el acto de escritura:**
- Hipotecas → cancelación o subrogación
- Embargos → alzamiento o pago
- Anotaciones preventivas → verificar vigencia (4 años prorrogables)

### 3. Condiciones suspensivas habituales

- Obtención de financiación hipotecaria por el comprador
- Cancelación de cargas por el vendedor
- Obtención de licencia de primera ocupación (obra nueva)
- Certificado de eficiencia energética
- Cédula de habitabilidad (si aplica por CCAA)

### 4. Escritura pública e inscripción

| Paso | Verificar |
|---|---|
| **Escritura pública** | Obligatoria para inscripción registral; no para la validez del contrato (art. 1278 CC) pero sí para la oponibilidad frente a terceros |
| **Inscripción en el Registro** | Constitutiva para la hipoteca; declarativa para la propiedad (pero necesaria para la protección del art. 34 LH — fe pública registral) |
| **Medios de pago** | El notario debe identificar los medios de pago (art. 24 LN, art. 177 RN) — transferencia, cheque bancario |
| **Retención por plusvalía** | El comprador puede retener el importe de la plusvalía municipal si el vendedor no la ha pagado (art. 104 TRLHL) |

---

## Fiscalidad de la compraventa

### ¿ITP o IVA + AJD?

| Supuesto | Impuesto | Tipo general |
|---|---|---|
| **Segunda transmisión** (vendedor particular o sociedad sin renuncia a exención) | **ITP** | 6%-11% según CCAA |
| **Primera transmisión** (promotor vende vivienda nueva) | **IVA + AJD** | IVA 10% (vivienda) / 21% (local, garaje no anejo) + AJD 0,5%-2% según CCAA |
| **Segunda transmisión con renuncia a exención de IVA** (B2B, art. 20.Dos LIVA) | **IVA + AJD** | IVA 21% + AJD; requiere que el comprador tenga derecho a deducir el IVA |

**Regla clave (art. 20.Uno.22 LIVA):** Las segundas y ulteriores entregas de edificaciones están exentas de IVA → tributan por ITP. Pero el sujeto pasivo puede **renunciar a la exención** si el adquirente es sujeto pasivo de IVA con derecho a deducción total. La renuncia debe ser expresa y constar en la escritura.

### Otros impuestos

| Impuesto | Sujeto pasivo | Plazo |
|---|---|---|
| **Plusvalía municipal (IIVTNU)** | Vendedor | 30 días hábiles desde la escritura |
| **IBI** | Quien sea titular a 1 de enero; repercusión prorrata habitual | Anual |
| **Ganancia patrimonial (IRPF/IS)** | Vendedor | Declaración correspondiente |

---

## Formato de salida

```markdown
# Revisión de compraventa inmobiliaria

**Inmueble:** [dirección, referencia catastral]
**Vendedor:** [persona física/jurídica]
**Comprador:** [persona física/jurídica]
**Precio:** [importe]
**Fecha de la operación:** [fecha prevista]

---

## Estructura de la operación

| Fase | Estado | Observaciones |
|---|---|---|
| Arras / contrato privado | [Firmado / Pendiente] | [tipo de arras, importe] |
| Due diligence registral | [Realizado / Pendiente] | [nota simple obtenida/pendiente] |
| Escritura pública | [Pendiente] | [notaría, fecha prevista] |
| Inscripción registral | [Pendiente] | |

---

## Cargas registrales

| Carga | Tipo | Estado | Acción |
|---|---|---|---|
| [Ej., Hipoteca Banco X] | Gravamen | Vigente | Cancelar en escritura |
| [Ej., Embargo AEAT] | Anotación | Vigente | Alzar antes de escritura |

---

## Fiscalidad

| Concepto | Régimen | Tipo | Importe estimado | Sujeto pasivo |
|---|---|---|---|---|
| [ITP / IVA] | [1.a transmisión / 2.a transmisión] | [X%] | [importe] | [comprador] |
| AJD | [si aplica] | [X%] | [importe] | [comprador] |
| Plusvalía municipal | IIVTNU | [estimación] | [importe] | [vendedor] |

---

## Hallazgos del contrato

| # | Cláusula | Observación | Riesgo | Recomendación |
|---|---|---|---|---|
| 1 | [Ej., Tipo de arras no especificado] | Se interpretarán como confirmatorias | Alto | Especificar expresamente |
| 2 | [Ej., Sin retención por plusvalía] | Riesgo de afección real | Medio | Incluir cláusula de retención |
| ... | ... | ... | ... | ... |

---

## Checklist pre-escritura

- [ ] Nota simple actualizada (48h antes de escritura)
- [ ] Certificado de eficiencia energética
- [ ] IBI al corriente / últimos recibos
- [ ] Certificado de deuda con la comunidad de propietarios (art. 9.1.e LPH)
- [ ] Cédula de habitabilidad / licencia de primera ocupación (según CCAA)
- [ ] Medios de pago preparados (transferencia / cheque bancario)
```

---

## Legislación de referencia

- Código Civil arts. 1445-1541 (compraventa), art. 1454 (arras penitenciales)
- Ley Hipotecaria (Decreto de 8 de febrero de 1946) — arts. 32-34 (fe pública registral)
- LIVA (Ley 37/1992) — art. 20.Uno.22 (exención segundas entregas), art. 20.Dos (renuncia)
- LITPAJD (RDLeg 1/1993) — ITP y AJD
- TRLHL (RDLeg 2/2004) — art. 104 (plusvalía municipal)
- LPH (Ley 49/1960) — art. 9.1.e (certificado de deuda)
- Normativa autonómica de ITP y AJD (tipos varían por CCAA)

---

## Lo que este skill NO hace

- No realiza la due diligence urbanística completa (licencias, planeamiento, situación urbanística) — marca cuándo es necesaria.
- No tramita la inscripción registral — indica los pasos.
- No calcula impuestos con precisión autonómica — indica el régimen aplicable y remite al cálculo específico por CCAA.
