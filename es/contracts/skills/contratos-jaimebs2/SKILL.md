---
name: contratos-jaimebs2
title: Tipos de contratos de trabajo en España
description: 'Use when the user asks about types of employment contracts in Spain, the 2022 labour reform, permanent vs temporary contracts, training contracts, fixed-discontinuous contracts, trial periods, notice periods, dismissal compensation, or where to find official contract templates. Triggers on: ''tipos de contrato'', ''contrato indefinido'', ''contrato temporal'', ''contrato fijo-discontinuo'', ''contrato formativo'', ''contrato en prácticas'', ''contrato de formación'', ''reforma laboral 2022'', ''periodo de prueba'', ''contrato a tiempo parcial'', ''despido'', ''indemnización despido'', ''preaviso'', ''conversión temporal indefinido'', ''modelos de contrato SEPE'', ''contrato de trabajo'', ''RDL 32/2021'', ''Estatuto de los Trabajadores''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/laboral/contratos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# Tipos de contratos de trabajo en España

Guía completa sobre los contratos de trabajo vigentes tras la **reforma
laboral de 2022** (Real Decreto-ley 32/2021). La reforma simplificó
drásticamente la contratación, priorizando el contrato indefinido y
reduciendo la temporalidad.

> Esta skill orienta sobre tipos de contratos y derechos básicos.
> **No sustituye asesoramiento legal profesional.**

---

## 1. Marco legal

La normativa básica es el **Estatuto de los Trabajadores** (ET),
aprobado por Real Decreto Legislativo 2/2015 y modificado
sustancialmente por el **RDL 32/2021** (reforma laboral 2022).

URL del ET consolidado:
`https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430`

Principio general tras la reforma: **el contrato de trabajo se presume
indefinido**. La contratación temporal es la excepción y solo cabe en
los supuestos tasados por la ley.

---

## 2. Contrato indefinido

Es el contrato por defecto. No tiene fecha de finalización.

### 2.1 Indefinido ordinario

- **Duración**: sin límite temporal.
- **Jornada**: completa o parcial.
- **Periodo de prueba**: máximo 6 meses para técnicos titulados, 2 meses
  para el resto (3 meses en empresas de menos de 25 trabajadores).
- **Extinción por despido**:
  - Despido disciplinario procedente: 0 indemnización.
  - Despido objetivo procedente: 20 días/año trabajado (máximo 12
    mensualidades).
  - Despido improcedente: 33 días/año trabajado (máximo 24
    mensualidades).
- **Bonificaciones**: existen bonificaciones a la contratación indefinida
  para determinados colectivos (jóvenes, mayores de 45, personas con
  discapacidad, etc.). Consultar el SEPE.

### 2.2 Fijo-discontinuo

Contrato indefinido para trabajos de **naturaleza estacional** o
vinculados a contratas o subcontratas. El trabajador alterna periodos
de actividad y de inactividad.

- **Cuándo se usa**: campañas agrícolas, turismo, actividades de
  temporada, contratas que se repiten cíclicamente.
- **Derechos**: los mismos que un indefinido ordinario (antigüedad,
  indemnización por despido, etc.). Los periodos de inactividad computan
  como antigüedad.
- **Llamamiento**: la empresa debe llamar al trabajador cuando se inicie
  la actividad. El incumplimiento equivale a despido.
- **Orden de llamamiento**: según convenio colectivo o, en su defecto,
  antigüedad.

Tras la reforma 2022, el fijo-discontinuo absorbió muchos contratos que
antes eran temporales (obra y servicio, eventualidad estacional).

### 2.3 Indefinido adscrito a obra (construcción)

Específico del sector de la construcción. Es indefinido pero se vincula
a una obra concreta. Al finalizar la obra, la empresa debe ofrecer
recolocación; si no es posible, se extingue con indemnización del 7 %
sobre conceptos salariales.

---

## 3. Contratos temporales (post-reforma 2022)

La reforma eliminó el contrato de obra y servicio y el contrato
eventual por circunstancias del mercado. Solo quedan **dos causas** de
temporalidad:

### 3.1 Temporal por circunstancias de la producción

Para atender un **incremento ocasional e imprevisible** de la actividad
o oscilaciones que generen un desajuste temporal entre empleo estable y
el disponible.

- **Duración máxima**: 6 meses, ampliable hasta 1 año por convenio
  colectivo sectorial.
- **Variante previsible**: para situaciones ocasionales y previsibles de
  duración reducida y delimitada, máximo 90 días en el año natural (no
  continuados).

### 3.2 Temporal de sustitución

Para sustituir a un trabajador con derecho a reserva de puesto.

- **Supuestos**: IT, maternidad/paternidad, excedencia con reserva,
  vacaciones, cobertura temporal hasta incorporación del titular.
- **Duración**: la del derecho de reserva del sustituido.
- **Anticipación**: se puede celebrar hasta 15 días antes de que se
  produzca la ausencia para permitir el solape formativo.
- **Nombre y causa**: la causa de sustitución debe constar en el
  contrato.

### 3.3 Consecuencias del uso fraudulento

Si un contrato temporal no cumple los requisitos legales, se convierte
automáticamente en **indefinido**:

- Falta de causa o causa falsa.
- Encadenamiento de temporales que supere 18 meses en un periodo de 24
  meses en el mismo puesto (con el mismo o distinto trabajador).
- No dar de alta al trabajador en la Seguridad Social.

---

## 4. Contratos formativos

Dirigidos a la formación y cualificación de jóvenes. Hay dos
modalidades:

### 4.1 Contrato de formación en alternancia

Combina trabajo remunerado con formación reglada (FP, universidad,
certificados de profesionalidad).

- **Edad**: sin límite si se vincula a FP o certificados.
  Menores de 30 años para otros supuestos.
- **Duración**: mínimo 3 meses, máximo 2 años.
- **Jornada laboral**: primer año, máximo 65 % de la jornada del
  convenio; segundo año, máximo 85 %. El resto es formación.
- **Retribución**: la del convenio, en proporción al tiempo de trabajo
  efectivo. Nunca inferior al SMI en proporción.
- **Seguridad Social**: cotización reducida.
- **Sin horas extra ni periodo de prueba**.

### 4.2 Contrato para la obtención de práctica profesional

Para quienes han terminado estudios (título universitario, FP,
certificados) y quieren una primera experiencia en su profesión.

- **Plazo desde el título**: máximo 3 años (5 años para personas con
  discapacidad).
- **Duración**: mínimo 6 meses, máximo 1 año.
- **Retribución**: la del convenio para el puesto. Nunca inferior al SMI.
- **Periodo de prueba**: máximo 1 mes (salvo convenio).
- **Tutor**: la empresa debe asignar un tutor y elaborar un plan
  formativo.

---

## 5. Contrato a tiempo parcial

No es un tipo contractual autónomo, sino una modalidad que puede
aplicarse a indefinidos o temporales.

- **Definición**: jornada inferior a la de un trabajador a tiempo
  completo comparable.
- **Forma**: siempre por escrito, indicando el número de horas ordinarias
  y su distribución.
- **Horas complementarias**: pactadas o voluntarias, con límites legales
  (30 % de las horas ordinarias, ampliable al 60 % por convenio).
- **Derechos**: los mismos que un trabajador a tiempo completo, en
  proporción a la jornada (principio de igualdad de trato).
- **Horas extraordinarias**: prohibidas (salvo fuerza mayor).

---

## 6. Contrato de alta dirección

Regulado por el RD 1382/1985. Se rige por la voluntad de las partes
y, supletoriamente, por el derecho civil.

- **Quién**: personal con poderes de dirección general de la empresa.
- **No se rige por el ET** (salvo lo que expresamente remita).
- **Indemnización por desistimiento del empresario**: lo pactado en
  contrato o, en su defecto, 7 días de salario por año de servicio
  (máximo 6 mensualidades).

---

## 7. Periodo de prueba

Periodo inicial durante el cual cualquiera de las partes puede rescindir
el contrato sin preaviso, sin causa y sin indemnización.

| Tipo de trabajador | Duración máxima |
|---|---|
| Técnicos titulados | 6 meses |
| Resto de trabajadores | 2 meses (3 meses en empresas < 25 trabajadores) |
| Contrato para práctica profesional | 1 mes |
| Contrato de formación en alternancia | No se permite |
| Contrato temporal ≤ 6 meses | 1 mes (salvo convenio) |

El convenio colectivo puede establecer duraciones distintas (nunca
superiores a las legales para temporales).

- Debe pactarse **por escrito**.
- Durante el periodo de prueba, el trabajador tiene los mismos derechos
  y obligaciones que cualquier otro (salario, Seguridad Social, etc.).
- Es nulo el periodo de prueba si el trabajador ya ha desempeñado las
  mismas funciones en la empresa.

---

## 8. Preaviso y extinción

### Preaviso

- **Dimisión del trabajador**: el plazo de preaviso es el que establezca
  el convenio o la costumbre del lugar. Si no se especifica, se suelen
  aplicar 15 días.
- **Despido objetivo**: la empresa debe preavisar con **15 días**.
- **Fin de contrato temporal**: si la duración supera 1 año, la parte que
  no renueva debe preavisar con **15 días**.
- **Despido disciplinario**: no requiere preaviso.

### Indemnizaciones por extinción

| Causa | Indemnización |
|---|---|
| Despido disciplinario procedente | 0 |
| Despido objetivo procedente | 20 días/año (máx. 12 mensualidades) |
| Despido improcedente (indefinido) | 33 días/año (máx. 24 mensualidades) |
| Fin de contrato temporal | 12 días/año trabajado |
| Despido colectivo (ERE) | 20 días/año (máx. 12 mensualidades) |

Los días se calculan por año de servicio, prorrateando los periodos
inferiores al año por meses.

---

## 9. Conversión de temporal a indefinido

Un contrato temporal se convierte en indefinido cuando:

1. Se supera la duración máxima legal sin denuncia (fin) expresa.
2. Se encadenan contratos temporales que suman más de **18 meses en un
   periodo de 24**, en el mismo puesto con la misma empresa (o grupo).
3. El contrato temporal no cumple los requisitos de causa (fraude de ley).
4. No se da de alta al trabajador en la Seguridad Social transcurrido un
   periodo igual al del periodo de prueba.

La empresa debe comunicar al trabajador por escrito su condición de
fijo en los 10 días siguientes.

---

## 10. Modelos oficiales de contrato

El SEPE pone a disposición los **modelos oficiales** de contrato de
trabajo, que deben usarse para la comunicación de la contratación:

URL: `https://www.sepe.es/HomeSepe/empresas/Contratos-de-trabajo.html`

Todos los contratos deben comunicarse al SEPE en los **10 días hábiles**
siguientes a su celebración. La comunicación se realiza a través de
**Contrat@**:

URL: `https://www.sepe.es/HomeSepe/empresas/comunica-contratacion.html`

---

## 11. Resumen rápido: tipos de contrato post-reforma

```
INDEFINIDOS (la norma):
  ├── Indefinido ordinario (tiempo completo o parcial)
  ├── Fijo-discontinuo (actividad estacional o contratas)
  └── Indefinido adscrito a obra (construcción)

TEMPORALES (la excepción — solo 2 causas):
  ├── Circunstancias de la producción (máx. 6 meses / 1 año por convenio)
  └── Sustitución (duración del derecho de reserva)

FORMATIVOS:
  ├── Formación en alternancia (trabajo + estudios, máx. 2 años)
  └── Obtención de práctica profesional (post-título, máx. 1 año)

OTROS:
  ├── A tiempo parcial (modalidad aplicable a cualquier tipo)
  └── Alta dirección (fuera del ET, regulación especial)
```

---

## Cuándo NO usar esta skill

- Si pregunta por **prestación por desempleo** (paro, subsidio,
  capitalización) → **laboral-desempleo**.
- Si pregunta por **cómo leer una nómina** o salario mínimo →
  **laboral-nominas**.
- Si pregunta por **ERE o ERTE** → **laboral-ere-erte**.
- Si pregunta por **convenios colectivos** o REGCON →
  **laboral-convenios**.
- Si pregunta por **Inspección de Trabajo** o denuncias laborales →
  **laboral-inspeccion**.
- Si pregunta por **estadísticas de paro** o empleo registrado →
  **sepe**.
- Si pregunta por **cotizaciones a la Seguridad Social** →
  **seguridad-social**.
- Si pregunta por **obligaciones fiscales del autónomo** →
  **fiscalidad-autonomos**.
- Si pregunta por el **texto de una ley** concreta → **boe**.
