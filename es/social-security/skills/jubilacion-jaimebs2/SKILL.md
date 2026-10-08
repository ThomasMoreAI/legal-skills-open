---
name: jubilacion-jaimebs2
title: Pensión de Jubilación en España
description: 'Use when the user asks about the Spanish retirement pension (pensión de jubilación): requirements, calculation, early retirement, active retirement, delayed retirement, minimum/maximum pension amounts, how to apply, or the transitional calendar to 2027. Triggers on: ''pensión jubilación'', ''jubilación anticipada'', ''jubilación activa'', ''jubilación demorada'', ''jubilación parcial'', ''calcular pensión'', ''edad jubilación'', ''años cotizados jubilación'', ''base reguladora jubilación'', ''complemento brecha género'', ''pensión mínima'', ''pensión máxima'', ''solicitar jubilación'', ''cuándo me puedo jubilar'', ''cuánto me queda de pensión'', ''contrato de relevo'', ''coeficientes reductores jubilación''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/seguridad-social-guia/jubilacion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: social-security
language: es
---

# Pensión de Jubilación en España

Guía completa sobre la pensión de jubilación del sistema de Seguridad Social
español: requisitos, cálculo, modalidades (anticipada, activa, demorada,
parcial), complementos y cómo solicitarla.

Para **datos estadísticos** sobre pensiones (número de pensionistas, pensión
media, gasto) consulta la skill **seguridad-social**. Para **cotizaciones**
(bases, tipos, cuotas) consulta **cotizaciones**. Para **vida laboral**
consulta **vida-laboral**.

> Esta skill orienta sobre requisitos y cálculo de la jubilación.
> **No sustituye asesoramiento profesional ni garantiza importes exactos.**
> Los parámetros están sujetos al periodo transitorio hasta 2027.

---

## 1. Requisitos generales

Para acceder a la pensión de jubilación contributiva se necesita:

### Edad

La edad ordinaria de jubilación depende de los años cotizados:

| Año | Edad con menos de 38 años y 6 meses cotizados | Edad con 38 años y 6 meses o más cotizados |
|---|---|---|
| 2024 | 66 años y 6 meses | 65 años |
| 2025 | 66 años y 8 meses | 65 años |
| 2026 | 66 años y 10 meses | 65 años |
| 2027 en adelante | **67 años** | **65 años** |

La progresión finaliza en 2027 con las edades definitivas: 67 años (regla
general) o 65 años (si se acreditan al menos 38 años y 6 meses de cotización).

### Periodo mínimo de cotización

- **15 años** de cotización efectiva.
- De esos 15 años, al menos **2 deben estar dentro de los 15 años
  inmediatamente anteriores** a la fecha de jubilación.
- Sin este mínimo no se genera derecho a pensión contributiva (podría
  accederse a una pensión no contributiva si se cumplen otros requisitos).

### Situación de alta o asimilada

Se debe estar en situación de alta en la Seguridad Social o en situación
asimilada al alta (desempleo involuntario, excedencia forzosa, etc.). También
existe la posibilidad de jubilarse sin estar en alta si se cumplen los 15 años
de cotización (jubilación desde situación de no alta).

---

## 2. Cálculo de la pensión

La pensión de jubilación se calcula en dos pasos:

### Paso 1 — Base reguladora

La base reguladora es la **media de las bases de cotización de los últimos
25 años** (300 meses), actualizadas con el IPC (salvo las de los 24 meses
inmediatamente anteriores, que se computan a su valor nominal).

```
Base reguladora = Suma de bases de cotización de 300 meses / 350
```

Se divide entre 350 (no entre 300) porque la pensión se paga en 14 pagas
al año (300 meses × 14/12 = 350).

**Lagunas de cotización**: si hay meses sin cotización en los últimos 25 años,
los primeros 48 meses se integran con la base mínima del Régimen General; el
resto, con el 50 % de dicha base mínima.

### Paso 2 — Porcentaje según años cotizados

Al resultado de la base reguladora se le aplica un porcentaje que depende
de los años cotizados:

| Años cotizados | Porcentaje |
|---|---|
| 15 años | 50 % |
| 16 años | 52,92 % |
| 17 años | 55,84 % |
| 18 años | 58,76 % |
| 19 años | 61,68 % |
| 20 años | 64,60 % |
| 21 años | 67,52 % |
| 25 años | 79,28 % |
| 30 años | 87,68 % |
| 35 años | 96,08 % |
| 36 años y 6 meses o más | **100 %** |

La escala es progresiva: 0,21 % por cada mes adicional entre los meses 1 y
49 a partir de los primeros 15 años; 0,19 % por cada mes adicional entre los
meses 50 y 209; después se mantiene hasta el 100 %.

### Ejemplo de cálculo

Un trabajador con base reguladora de 2.000 EUR y 35 años cotizados:

```
Pensión mensual = 2.000 × 96,08 % = 1.921,60 EUR (bruto, 14 pagas)
```

---

## 3. Pensión máxima y mínima

### Pensión máxima

La pensión máxima se fija cada año en los Presupuestos Generales del Estado.
En 2025: **3.267,60 EUR/mes** (14 pagas) = **45.746,40 EUR/año**.

### Pensiones mínimas

Dependen de la situación familiar del pensionista (con o sin cónyuge a cargo).
Se actualizan anualmente. Ejemplos orientativos (2025):

| Situación | Pensión mínima mensual (14 pagas) |
|---|---|
| Jubilación con 65 años, con cónyuge a cargo | ~1.033 EUR |
| Jubilación con 65 años, sin cónyuge | ~838 EUR |
| Jubilación con 65 años, con cónyuge no a cargo | ~795 EUR |

Si la pensión calculada es inferior al mínimo y los ingresos del pensionista
no superan cierto límite, se aplica un **complemento a mínimos** hasta
alcanzar la cuantía mínima.

---

## 4. Jubilación anticipada

### Anticipada involuntaria (por cese no voluntario)

- **Edad**: hasta 4 años antes de la edad ordinaria.
- **Cotización mínima**: 33 años.
- **Causa**: extinción del contrato por causa no imputable al trabajador
  (despido colectivo, objetivo, etc.).
- **Coeficientes reductores por trimestre de anticipación**:
  - Menos de 38,5 años cotizados: 1,875 % por trimestre.
  - 38,5 años o más cotizados: 1,625 % por trimestre.

### Anticipada voluntaria

- **Edad**: hasta 2 años antes de la edad ordinaria.
- **Cotización mínima**: 35 años.
- **Coeficientes reductores por trimestre de anticipación**:
  - Menos de 38,5 años cotizados: 3,26 % por trimestre.
  - Entre 38,5 y 41,5 años: 3,11 % por trimestre.
  - Entre 41,5 y 44,5 años: 2,96 % por trimestre.
  - 44,5 años o más: 2,81 % por trimestre.
- **Límite**: la pensión resultante no puede ser superior a la que
  correspondería a los 65 años con la misma cotización.

### Anticipada por actividad penosa/peligrosa

Ciertos colectivos (mineros, personal de vuelo, bomberos, Ertzaintza, policías
locales, etc.) tienen coeficientes reductores específicos que adelantan la
edad de jubilación.

---

## 5. Jubilación parcial y contrato de relevo

### Jubilación parcial

Permite compatibilizar una pensión parcial con un trabajo a tiempo parcial:

- **Sin contrato de relevo** (desde 2013): a partir de la edad ordinaria,
  con al menos 15 años cotizados. Se reduce la jornada entre un 25 % y un
  50 %.
- **Con contrato de relevo**: a partir de los 62-63 años (según año y
  cotización), con al menos 33 años cotizados y 6 años de antigüedad en la
  empresa. El relevista debe ser contratado al menos por la jornada reducida.

### Contrato de relevo

Contrato que celebra la empresa con un trabajador (relevista) para cubrir la
parte de jornada que deja el jubilado parcial. Puede ser indefinido o temporal
(con duración mínima según la modalidad).

---

## 6. Jubilación activa

Permite compatibilizar el cobro de una parte de la pensión con el trabajo
por cuenta propia o ajena:

### Requisitos

- Haber accedido a la jubilación al menos **1 año después** de la edad
  ordinaria.
- El porcentaje aplicable a la base reguladora debe alcanzar el **100 %**.

### Cuantía

- Se percibe el **50 % de la pensión** con carácter general.
- **100 % de la pensión** si el autónomo tiene al menos un trabajador por
  cuenta ajena contratado (incentivo introducido en 2022).

### Cotización

El jubilado activo sigue cotizando por un concepto de **solidaridad
intergeneracional** (cotización especial sin generación de nuevos derechos,
salvo el complemento de jubilación activa).

---

## 7. Jubilación demorada

Si se retrasa la jubilación más allá de la edad ordinaria habiendo alcanzado
el 100 % de la base reguladora, se aplican incentivos:

### Opciones (acumulables por periodos distintos)

| Incentivo | Detalle |
|---|---|
| **Porcentaje adicional** | 4 % por cada año completo de demora |
| **Cantidad a tanto alzado** | Pago único que varía según años cotizados y base reguladora |
| **Combinación** | Porcentaje adicional + tanto alzado, repartidos entre los años de demora |

Estos incentivos pueden elevar la pensión **por encima del límite máximo**
ordinario.

---

## 8. Complemento de brecha de género

Las mujeres (y hombres en algunos supuestos) con hijos que hayan visto
perjudicada su carrera de cotización reciben un complemento por cada hijo
(hasta 4), siempre que la pensión sea inferior a la del otro progenitor.

Cuantía orientativa (2025): **33,20 EUR/mes por hijo** (14 pagas).

Se aplica a pensiones de jubilación, incapacidad permanente y viudedad.

---

## 9. Cómo solicitar la jubilación

### Canales

| Canal | Detalle |
|---|---|
| **Import@ss** (web/app) | `https://importass.seg-social.es` — solicitud telemática con certificado digital, Cl@ve o DNIe |
| **Sede electrónica** | `https://sede.seg-social.gob.es` |
| **Presencial** | Centros de Atención e Información de la Seguridad Social (CAISS), con cita previa |
| **Teléfono** | 901 16 65 65 / 91 541 25 30 |

### Documentación habitual

- DNI/NIE en vigor.
- Documento de cese de actividad (si aplica).
- Certificado de empresa (los últimos 6 meses de bases de cotización).
- Declaración de situación familiar (para complementos a mínimos).
- Libro de familia o certificados de nacimiento de hijos (para complemento
  de brecha de género).

### Plazo

Se puede solicitar con hasta **3 meses de antelación** a la fecha prevista
de jubilación. Los efectos económicos se producen desde el día siguiente al
cese en el trabajo (o desde la solicitud si es posterior).

---

## 10. Simulador de pensión

La Seguridad Social ofrece un simulador online que estima la pensión futura
a partir de los datos de cotización reales del trabajador:

- **Acceso**: Import@ss → "Tu pensión de jubilación"
- **URL**: `https://importass.seg-social.es`
- **Requiere**: identificación electrónica (certificado digital, Cl@ve o
  DNIe).

El simulador es orientativo, no vinculante.

---

## 11. Calendario transitorio (hasta 2027)

Los principales parámetros de la jubilación se están adaptando
progresivamente:

| Parámetro | Antes | 2027 (definitivo) |
|---|---|---|
| Edad ordinaria (regla general) | 65 años | **67 años** |
| Edad con cotización larga | 65 años (con 35,5 años cotizados) | **65 años** (con 38,5 años) |
| Periodo de cálculo (base reguladora) | 15 años (180 meses) | **25 años** (300 meses) — ya en vigor |
| Años para el 100 % | 35 años | **36 años y 6 meses** |

Estos cambios provienen de la Ley 27/2011 y reformas posteriores (RDL 2/2023).

---

## 12. Pensión no contributiva de jubilación

Para personas mayores de 65 años que no alcanzan el periodo mínimo de
cotización (15 años):

- **Requisito**: residir en España al menos 10 años (2 de ellos
  inmediatamente anteriores a la solicitud).
- **Cuantía** (2025): ~7.399 EUR/año (íntegra), se reduce según ingresos y
  convivencia.
- **Gestión**: comunidades autónomas (no el INSS).

---

## Resumen rápido

```
PENSIÓN DE JUBILACIÓN — ESQUEMA
  ├── REQUISITOS
  │   ├── Edad: 67 años (o 65 con 38,5 años cotizados) — transitorio hasta 2027
  │   ├── Cotización mínima: 15 años (2 en los últimos 15)
  │   └── Alta o asimilada al alta
  │
  ├── CÁLCULO
  │   ├── Base reguladora = media últimos 25 años de cotización / 350
  │   └── Porcentaje = 50 % (15 años) → 100 % (36,5 años)
  │
  ├── MODALIDADES
  │   ├── Anticipada involuntaria: -4 años, 33 años cotizados
  │   ├── Anticipada voluntaria: -2 años, 35 años cotizados
  │   ├── Parcial: con contrato de relevo
  │   ├── Activa: 50 % pensión + trabajo (100 % si autónomo con empleados)
  │   └── Demorada: +4 % por año o tanto alzado
  │
  ├── COMPLEMENTOS
  │   ├── Brecha de género: ~33 EUR/mes por hijo
  │   └── A mínimos: si pensión < mínimo e ingresos bajos
  │
  └── SOLICITUD
      ├── Import@ss / Sede electrónica / CAISS presencial
      └── Hasta 3 meses de antelación
```

---

## Cuándo NO usar esta skill

- Si necesita **datos estadísticos de pensiones** (número de pensionistas,
  gasto, pensión media por CCAA) → **seguridad-social**.
- Si pregunta por **cotizaciones** (bases, tipos, cuotas de autónomos) →
  **cotizaciones**.
- Si pregunta por **cómo obtener la vida laboral** → **vida-laboral**.
- Si pregunta por **incapacidad temporal o permanente** →
  **incapacidad**.
- Si pregunta por **prestación de maternidad/paternidad** →
  **maternidad-paternidad**.
- Si pregunta por **obligaciones fiscales del autónomo** →
  **fiscalidad-autonomos**.
- Si pregunta por **nóminas y cómo se refleja la cotización** →
  **laboral-nominas**.
- Si pregunta por el **texto de una ley** de Seguridad Social → **boe**.
