---
name: incapacidad-jaimebs2
title: Incapacidad Temporal y Permanente
description: 'Use when the user asks about temporary disability (incapacidad temporal / baja médica) or permanent disability (incapacidad permanente) in the Spanish Social Security system: sick leave, how long it lasts, who pays, disability grades, benefits, medical tribunal (EVI/INSS), review process, or work compatibility. Triggers on: ''baja médica'', ''baja laboral'', ''incapacidad temporal'', ''IT'', ''parte de baja'', ''quién paga la baja'', ''cuánto cobro de baja'', ''incapacidad permanente'', ''gran invalidez'', ''incapacidad absoluta'', ''incapacidad total'', ''incapacidad parcial'', ''tribunal médico'', ''EVI'', ''INSS incapacidad'', ''grados de invalidez'', ''revisión de grado'', ''alta médica'', ''mutua baja'', ''contingencia común'', ''accidente laboral''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/seguridad-social-guia/incapacidad
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: social-security
language: es
---

# Incapacidad Temporal y Permanente

Guía completa sobre las prestaciones de incapacidad temporal (baja médica)
e incapacidad permanente en el sistema de Seguridad Social español: quién
paga, cuánto se cobra, duración, grados de incapacidad permanente,
procedimiento y compatibilidad con el trabajo.

Para **cómo afecta la baja a la nómina** consulta **laboral-nominas**.
Para **cotizaciones** consulta **cotizaciones**.
Para **datos estadísticos** de la Seguridad Social consulta
**seguridad-social**.

> Esta skill orienta sobre derechos y procedimientos de incapacidad.
> **No sustituye asesoramiento médico ni jurídico.**

---

## 1. Incapacidad temporal (IT) — Baja médica

La incapacidad temporal es la situación en la que un trabajador no puede
desempeñar su trabajo por enfermedad o accidente y recibe asistencia
sanitaria de la Seguridad Social.

### Tipos de contingencia

| Tipo | Causa | Ejemplo |
|---|---|---|
| **Contingencia común** | Enfermedad común o accidente no laboral | Gripe, operación quirúrgica, depresión |
| **Contingencia profesional** | Accidente de trabajo o enfermedad profesional | Caída en obra, exposición a amianto |

La contingencia determina quién paga, cuánto y desde cuándo.

---

## 2. Requisitos para cobrar la IT

### Contingencia común

- Estar en **alta** o situación asimilada al alta.
- Tener **cotizados al menos 180 días** en los 5 años inmediatamente
  anteriores a la baja.

### Contingencia profesional

- Estar en **alta** (o alta de pleno derecho).
- **No se exige** periodo mínimo de cotización.

### Autónomos

Los autónomos también tienen derecho a la IT, pero deben estar al corriente
en el pago de cuotas. Desde 2019, la cobertura de IT por contingencia
profesional y cese de actividad es obligatoria para todos los autónomos.

---

## 3. Cuánto se cobra de baja

### Por contingencia común

| Periodo | Porcentaje de la base reguladora | Quién paga |
|---|---|---|
| Días 1–3 | **0 %** (no se cobra) | — |
| Días 4–15 | **60 %** | Empresa |
| Días 16–20 | **60 %** | INSS/Mutua (pago delegado por empresa) |
| Día 21 en adelante | **75 %** | INSS/Mutua (pago delegado por empresa) |

**Nota**: muchos convenios colectivos mejoran estos porcentajes. Algunos
complementan hasta el 100 % del salario desde el primer día.

### Por contingencia profesional (accidente de trabajo / enfermedad profesional)

| Periodo | Porcentaje | Quién paga |
|---|---|---|
| Día del accidente | **100 %** (salario íntegro) | Empresa |
| Día siguiente en adelante | **75 %** | Mutua (pago delegado por empresa) |

### Base reguladora de la IT

- **Contingencia común**: base de cotización por contingencias comunes del
  mes anterior a la baja, dividida entre el número de días del mes.
- **Contingencia profesional**: base de cotización por contingencias
  profesionales del mes anterior, incluyendo la prorrata de horas
  extraordinarias de los 12 meses anteriores.

### Autónomos

- La base reguladora es la base por la que cotizan en el RETA.
- No existe el concepto de "empresa que paga los primeros días".
- Desde el día 4 (contingencia común) o desde el día siguiente al accidente
  (contingencia profesional), paga la mutua.

---

## 4. Duración de la baja

### Plazos máximos

| Concepto | Plazo |
|---|---|
| Duración máxima inicial | **365 días** |
| Prórroga | **Hasta 180 días más** (total 545 días) si se prevé curación |
| Prórroga extraordinaria | **Hasta 180 días más** (total 730 días) para demora en calificación de IP |

### Proceso de control

| Actor | Función |
|---|---|
| **Médico de cabecera** | Emite el parte de baja, los partes de confirmación (semanales o según duración estimada) y el parte de alta |
| **INSS** | Puede emitir alta médica a los 365 días (o antes), incluso contra la opinión del médico |
| **Mutua** | Gestiona la prestación en contingencia profesional. Puede proponer alta al INSS |
| **Inspección médica (SPS)** | Puede emitir alta en los primeros 365 días |

### Partes de baja y confirmación

- **Parte de baja**: el médico indica una duración estimada (muy corta: < 5 días;
  corta: 5-30; media: 31-60; larga: > 61 días).
- **Partes de confirmación**: se emiten periódicamente según la duración
  estimada.
- **Parte de alta**: cuando el trabajador puede reincorporarse o se agota
  el plazo máximo.

---

## 5. Fin de la baja (alta médica)

### Quién puede dar el alta

- El **médico de cabecera** (servicio público de salud).
- El **INSS** (a partir del día 365, o antes si lo considera).
- La **inspección médica** del servicio autonómico de salud.
- La **mutua** solo puede proponer el alta al INSS (no emitirla
  directamente en contingencia común).

### Disconformidad con el alta

Si no estás de acuerdo con el alta médica emitida por el INSS:
1. Reclamar ante el INSS en **4 días hábiles**.
2. El INSS revisa y resuelve en 7 días.
3. Si se confirma el alta, se puede interponer reclamación previa y
   posterior demanda ante el Juzgado de lo Social.

---

## 6. Incapacidad permanente (IP)

Cuando las lesiones o limitaciones se estabilizan y no hay posibilidad de
curación, se evalúa la incapacidad permanente. Hay cuatro grados:

### Grados de incapacidad permanente

| Grado | Definición | Prestación |
|---|---|---|
| **Parcial** | Disminución ≥ 33 % del rendimiento en la profesión habitual, pero puede seguir ejerciéndola | Indemnización a tanto alzado = **24 mensualidades** de la base reguladora |
| **Total** | No puede realizar su profesión habitual, pero sí otra distinta | Pensión del **55 %** de la base reguladora (75 % si ≥ 55 años y dificultades de empleo) |
| **Absoluta** | No puede realizar ninguna profesión u oficio | Pensión del **100 %** de la base reguladora |
| **Gran invalidez** | Necesita asistencia de otra persona para actos esenciales de la vida | Pensión del **100 % + complemento** (mínimo 45 % de la base mínima de cotización + 30 % de la última base del trabajador) |

### Requisitos de cotización para la IP

Dependen de la edad y la contingencia:

- **Contingencia profesional**: no se exige cotización previa.
- **Contingencia común**:
  - Menores de 31 años: 1/3 del tiempo transcurrido entre los 16 años y la
    fecha del hecho causante.
  - 31 años o más: 1/4 del tiempo entre los 20 años y el hecho causante
    (mínimo 5 años), y al menos 1/5 debe estar en los 10 años anteriores.

### Base reguladora de la IP

Varía según contingencia y grado:
- **Contingencia común**: similar al cálculo de jubilación (media de bases
  de cotización de un periodo).
- **Contingencia profesional**: salario real del año anterior, incluyendo
  pagas extras y complementos.

---

## 7. Procedimiento para la incapacidad permanente

### Inicio del procedimiento

| Vía | Detalle |
|---|---|
| **De oficio por el INSS** | Al agotar los 545 días de IT (o 730), el INSS inicia expediente de IP |
| **A petición del trabajador** | Puede solicitar valoración al INSS o al Equipo de Valoración de Incapacidades (EVI) |
| **A petición de la mutua** | La mutua puede proponer al INSS la iniciación del expediente |
| **A petición del servicio de salud** | Cuando considera estabilizadas las lesiones |

### Equipo de Valoración de Incapacidades (EVI)

- Órgano del INSS compuesto por un médico inspector, un médico del INSS,
  un inspector de trabajo y un funcionario del INSS.
- Evalúa las limitaciones del trabajador y emite un dictamen-propuesta
  con el grado de incapacidad (o la denegación).

### Resolución

- El **Director Provincial del INSS** resuelve el expediente basándose
  en el dictamen del EVI.
- Plazo: **135 días** desde el inicio del expediente.
- Si no resuelve en plazo, se entiende **desestimada** (silencio negativo).

### Recursos

1. **Reclamación previa** ante el INSS: **30 días** desde la notificación.
2. **Demanda ante el Juzgado de lo Social**: **30 días** desde la
   resolución de la reclamación previa.
3. **Recurso de suplicación** ante el TSJ si la cuantía supera cierto
   umbral.

---

## 8. Revisión de grado

La incapacidad permanente puede ser revisada:

- **Por mejoría o agravamiento** de las lesiones.
- **A petición del beneficiario**, del INSS o de la mutua.
- **Plazo**: a partir de los 2 años desde la resolución (o antes si se
  prevé mejoría).
- Puede suponer subir de grado, bajar de grado o extinguir la pensión.

---

## 9. Compatibilidad con el trabajo

| Grado | Compatible con trabajo |
|---|---|
| **Parcial** | Sí, puede seguir en su profesión habitual |
| **Total** | Sí, puede trabajar en otra profesión distinta a la habitual |
| **Absoluta** | Sí, pero con limitaciones y obligación de comunicarlo al INSS. El trabajo debe ser compatible con el estado del beneficiario |
| **Gran invalidez** | Mismas condiciones que la absoluta |

La pensión de IP total es compatible con el salario de otra profesión.
La de absoluta y gran invalidez es compatible con trabajo, pero el INSS
puede revisar la situación.

---

## 10. Prestaciones durante la IT — Casos especiales

### Recaída

Si se produce una nueva baja por la misma enfermedad en los **180 días
siguientes** al alta, se considera recaída (no nueva baja). Se acumula
al periodo anterior a efectos del cómputo de los 365/545 días.

### Baja durante el desempleo

Si el trabajador está cobrando la prestación por desempleo y cae enfermo:
- Cobra la prestación de IT con la misma cuantía que la prestación por
  desempleo.
- El periodo de IT no "consume" desempleo.

### Baja durante la maternidad/paternidad

La IT anterior a la prestación de nacimiento la interrumpe. Si la IT
surge durante la prestación de nacimiento, se cobra la de nacimiento
hasta que termine; después, la de IT.

---

## Resumen rápido

```
INCAPACIDAD TEMPORAL (BAJA MÉDICA)
  ├── Contingencia común: días 1-3 = 0 %, días 4-20 = 60 %, día 21+ = 75 %
  ├── Contingencia profesional: día accidente = 100 %, siguiente = 75 %
  ├── Duración máxima: 365 + 180 días (posible hasta 730)
  └── Alta: médico, INSS (a los 365 días), inspección

INCAPACIDAD PERMANENTE
  ├── Parcial: ≥ 33 % pérdida → indemnización (24 mensualidades)
  ├── Total: no puede ejercer su profesión → 55 % (o 75 %)
  ├── Absoluta: no puede trabajar en ningún oficio → 100 %
  ├── Gran invalidez: necesita asistencia → 100 % + complemento
  └── Procedimiento: INSS → EVI → dictamen → resolución → recurso
```

---

## Cuándo NO usar esta skill

- Si pregunta por la **pensión de jubilación** → **jubilacion**.
- Si pregunta por **cotizaciones** (bases, tipos, cuotas) →
  **cotizaciones**.
- Si pregunta por **cómo obtener la vida laboral** → **vida-laboral**.
- Si pregunta por **prestación de maternidad/paternidad** →
  **maternidad-paternidad**.
- Si necesita **datos estadísticos** de la Seguridad Social →
  **seguridad-social**.
- Si pregunta por **nóminas y cómo se refleja la baja** →
  **laboral-nominas**.
- Si pregunta por **contratos laborales** → **laboral-contratos**.
- Si pregunta por el **texto de una ley** → **boe**.
