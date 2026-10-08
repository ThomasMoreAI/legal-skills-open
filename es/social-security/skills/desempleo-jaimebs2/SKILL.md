---
name: desempleo-jaimebs2
title: Prestación por desempleo en España
description: 'Use when the user asks about unemployment benefits in Spain, how to claim unemployment (paro), contributory unemployment, unemployment subsidy, RAI (Renta Activa de Inserción), IMV (Ingreso Mínimo Vital), how long unemployment lasts, how much unemployment pays, capitalisation of unemployment (pago único), or obligations while receiving unemployment. Triggers on: ''desempleo'', ''prestación por desempleo'', ''paro'', ''cobrar el paro'', ''subsidio por desempleo'', ''RAI'', ''renta activa de inserción'', ''ingreso mínimo vital'', ''IMV'', ''duración del paro'', ''cuánto cobro de paro'', ''capitalización del desempleo'', ''pago único desempleo'', ''solicitar desempleo'', ''SEPE prestaciones'', ''renovar demanda'', ''sellar el paro'', ''demanda de empleo'', ''IPREM''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/laboral/desempleo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: social-security
language: es
---

# Prestación por desempleo en España

Guía completa sobre las prestaciones por desempleo: contributiva,
subsidio, RAI, IMV y capitalización. Requisitos, duración, cuantía
y cómo solicitar.

> Esta skill orienta sobre derechos y requisitos generales.
> **No sustituye asesoramiento profesional ni gestiona solicitudes.**

---

## 1. Visión general del sistema de protección por desempleo

España tiene un sistema escalonado de protección:

```
PROTECCIÓN POR DESEMPLEO
├── 1. Prestación contributiva (el "paro" principal)
├── 2. Subsidio por desempleo (nivel asistencial)
├── 3. Renta Activa de Inserción (RAI)
└── 4. Ingreso Mínimo Vital (IMV) — última red de seguridad
```

Cada nivel tiene requisitos distintos. Si no se accede al primero, se
puede acceder al siguiente.

URL principal del SEPE:
`https://www.sepe.es/HomeSepe/Personas/distributiva-prestaciones.html`

---

## 2. Prestación contributiva por desempleo

Es la protección principal. Se financia con las cotizaciones del
trabajador y la empresa durante el empleo.

### 2.1 Requisitos

- Estar **en situación legal de desempleo** (despido, fin de contrato,
  ERE/ERTE, etc. — no aplica si es baja voluntaria salvo excepciones).
- Estar **afiliado y en alta** (o situación asimilada) en la Seguridad
  Social.
- Haber cotizado un mínimo de **360 días** en los últimos 6 años.
- No haber cumplido la **edad de jubilación** (salvo excepciones).
- **Inscribirse como demandante de empleo** en el SEPE.
- **Solicitar la prestación** en los 15 días hábiles siguientes al cese.

### 2.2 Situación legal de desempleo

Se considera situación legal de desempleo, entre otros:

- Despido (procedente, improcedente o colectivo).
- Fin de contrato temporal.
- ERTE (suspensión o reducción de jornada).
- Resolución voluntaria por causas justificadas (traslado, modificación
  sustancial de condiciones, impago grave).
- Periodo de inactividad de fijos-discontinuos.

**NO es situación legal de desempleo**: dimisión voluntaria sin causa
justificada.

### 2.3 Duración

Depende de los días cotizados en los últimos 6 años:

| Días cotizados | Duración de la prestación |
|---|---|
| 360 – 539 | 120 días (4 meses) |
| 540 – 719 | 180 días (6 meses) |
| 720 – 899 | 240 días (8 meses) |
| 900 – 1.079 | 300 días (10 meses) |
| 1.080 – 1.259 | 360 días (12 meses) |
| 1.260 – 1.439 | 420 días (14 meses) |
| 1.440 – 1.619 | 480 días (16 meses) |
| 1.620 – 1.799 | 540 días (18 meses) |
| 1.800 – 1.979 | 600 días (20 meses) |
| 1.980 – 2.159 | 660 días (22 meses) |
| ≥ 2.160 | **720 días (24 meses)** — máximo |

### 2.4 Cuantía

- **Primeros 180 días**: 70 % de la base reguladora.
- **Resto de la prestación**: 50 % de la base reguladora.

La base reguladora se calcula como la media de las bases de cotización
por contingencias profesionales de los **últimos 180 días**.

**Topes mensuales (referencia 2025, vinculados al IPREM)**:

| Situación | Tope mínimo | Tope máximo |
|---|---|---|
| Sin hijos | 560,76 € | 1.225,80 € |
| Con 1 hijo | 749,28 € | 1.400,88 € |
| Con 2 o más hijos | 749,28 € | 1.575,96 € |

> Los topes se actualizan anualmente. Se calculan como porcentajes del
> IPREM (Indicador Público de Renta de Efectos Múltiples).

### 2.5 Cotización durante el desempleo

Mientras se cobra la prestación contributiva, el SEPE cotiza a la
Seguridad Social por el beneficiario (contingencias comunes y
profesionales). Este tiempo computa para futuras prestaciones y para
la jubilación.

---

## 3. Subsidio por desempleo

Nivel asistencial para quienes no acceden a la prestación contributiva
o la han agotado.

### 3.1 Modalidades

| Modalidad | Requisitos principales |
|---|---|
| **Agotamiento de prestación contributiva** | Haber agotado la prestación, tener responsabilidades familiares (o ser mayor de 45), rentas < 75 % SMI |
| **Cotización insuficiente** | Haber cotizado entre 90 y 359 días (no alcanza los 360 para la contributiva), tener responsabilidades familiares |
| **Mayores de 52 años** | Haber agotado prestación o subsidio anterior, tener 52+ años, cumplir requisito de cotización para jubilación (excepto edad) |
| **Emigrantes retornados** | Haber trabajado en el extranjero y retornar a España |
| **Liberados de prisión** | Haber estado en prisión > 6 meses y no tener derecho a prestación contributiva |
| **Revisión por incapacidad** | Haber sido declarado apto tras incapacidad permanente |

### 3.2 Cuantía

- **80 % del IPREM mensual**: aproximadamente **480 €/mes** (2025).
- Duración variable según modalidad (6, 18, 21, 24, 30 meses o hasta
  la jubilación para mayores de 52).

### 3.3 Requisitos comunes

- Estar inscrito como demandante de empleo.
- No tener rentas propias superiores al **75 % del SMI** mensual
  (excluida la parte proporcional de pagas extras).
- Estar en situación legal de desempleo.

---

## 4. Renta Activa de Inserción (RAI)

Programa para personas con especial dificultad de inserción laboral.

### Requisitos

- Estar inscrito como demandante de empleo **ininterrumpidamente** 12
  meses o más.
- No tener derecho a prestación contributiva ni subsidio.
- No tener rentas superiores al 75 % del SMI.
- Pertenecer a alguno de estos colectivos:
  - Desempleados mayores de 45 años.
  - Víctimas de violencia de género o doméstica.
  - Personas con discapacidad ≥ 33 %.
  - Emigrantes retornados mayores de 45 años.

### Cuantía y duración

- **80 % del IPREM mensual** (~480 €/mes).
- **11 meses** de duración.
- Se puede cobrar un máximo de **3 veces** en la vida (con un año de
  carencia entre cada una).

---

## 5. Ingreso Mínimo Vital (IMV)

Última red de protección social para hogares en riesgo de pobreza.
No es técnicamente una prestación por desempleo, sino una prestación
de la Seguridad Social.

### Características

- **Quién lo gestiona**: INSS (Instituto Nacional de la Seguridad
  Social), no el SEPE.
- **Requisitos**: residencia legal en España ≥ 1 año, ingresos del hogar
  por debajo del umbral, tener entre 23 y 65 años (o ser menor con hijos
  a cargo), no ser beneficiario de otras prestaciones incompatibles.
- **Cuantía (2025, orientativa)**:
  - Adulto individual: ~604 €/mes.
  - Se incrementa por cada miembro adicional del hogar.
  - Complemento de infancia.
- **Solicitud**: sede electrónica de la Seguridad Social o presencialmente.
- **Compatible** con el empleo (con reducción progresiva).

URL: `https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/72702`

---

## 6. Capitalización del desempleo (pago único)

Permite cobrar la prestación contributiva de golpe para **emprender una
actividad por cuenta propia** o incorporarse a una cooperativa/sociedad
laboral.

### Requisitos

- Tener reconocida la prestación contributiva con al menos **3 meses
  pendientes**.
- No haber capitalizado en los 4 años anteriores.
- Presentar una **memoria del proyecto** de actividad.
- Iniciar la actividad en el **mes siguiente** a la resolución.

### Modalidades

1. **Pago único**: para la aportación al capital social de una
   cooperativa/sociedad laboral o para la inversión necesaria para
   iniciar actividad como autónomo.
2. **Subvención de cuotas**: se destina la prestación pendiente al pago
   de las cuotas de autónomos mensuales.
3. **Combinación**: parte como pago único y parte como subvención de
   cuotas.

### Solicitud

En el SEPE, con el modelo oficial. Se recomienda pedir cita previa.

URL: `https://www.sepe.es/HomeSepe/autonomos/capitaliza-tu-prestacion.html`

---

## 7. Cómo solicitar la prestación por desempleo

### Plazo

**15 días hábiles** desde la situación legal de desempleo. Si se
solicita fuera de plazo, se pierde un día de prestación por cada día
de retraso.

### Dónde

1. **Sede electrónica del SEPE** (con certificado digital, Cl@ve o
   DNI electrónico):
   `https://www.sepe.es/HomeSepe/Personas/distributiva-prestaciones.html`
2. **Cita previa** en oficina del SEPE:
   `https://www.sepe.es/HomeSepe/que-es-el-sepe/comunicacion-institucional/noticias/historico-de-noticias/2020/detalle-noticia.html?folder=/2020/Junio/&detail=cita-previa-702`

### Documentación necesaria

- DNI/NIE.
- Certificado de empresa (lo facilita el empleador al SEPE).
- Documento de situación legal de desempleo.
- Datos bancarios (cuenta a nombre del solicitante).
- Libro de familia (si alega cargas familiares).

---

## 8. Obligaciones del perceptor

Quien cobra prestación o subsidio debe:

1. **Renovar la demanda de empleo** (sellar el paro) en las fechas
   indicadas. Si no se renueva, se suspende la prestación.
2. **Acudir a las citaciones** del SEPE y de los servicios de empleo
   autonómicos.
3. **Aceptar una oferta de empleo adecuada** o participar en acciones de
   formación.
4. **Comunicar cualquier cambio**: inicio de trabajo, cambio de domicilio,
   variación de rentas o situación familiar.
5. **No rechazar** una oferta de empleo adecuada sin causa justificada.
6. **No trabajar por cuenta ajena o propia** sin comunicarlo (compatibilidad
   regulada).

El incumplimiento puede suponer **sanción** (suspensión o extinción de
la prestación).

---

## 9. Compatibilidad con trabajo

### Trabajo a tiempo parcial

La prestación es **compatible** con un trabajo a tiempo parcial. Se
reduce proporcionalmente.

### Trabajo por cuenta propia

- **Menores de 60 años**: pueden capitalizar o suspender la prestación.
- Programas específicos de compatibilidad para mayores de 52 años.

### ERTE

Durante un ERTE, el trabajador cobra prestación por desempleo por la
parte de jornada suspendida. No consume paro.

---

## 10. IPREM: referencia para las cuantías

El **IPREM** (Indicador Público de Renta de Efectos Múltiples) es el
índice de referencia para calcular topes y cuantías de prestaciones.
Sustituye al SMI como referencia desde 2004.

| Año | IPREM mensual | IPREM anual (12 pagas) | IPREM anual (14 pagas) |
|---|---|---|---|
| 2025 | 600,00 € | 7.200,00 € | 8.400,00 € |

> Se actualiza anualmente en la Ley de Presupuestos Generales del Estado.

---

## 11. Resumen rápido

```
¿TIENES 360+ DÍAS COTIZADOS EN 6 AÑOS?
  SÍ → Prestación contributiva (70/50 % base reguladora, 4-24 meses)
  NO ↓

¿TIENES 90-359 DÍAS + CARGAS FAMILIARES?
  SÍ → Subsidio por cotización insuficiente (80 % IPREM)
  NO ↓

¿HAS AGOTADO LA PRESTACIÓN + CARGAS/45+ AÑOS?
  SÍ → Subsidio por agotamiento (80 % IPREM, 18-30 meses)
  NO ↓

¿52+ AÑOS + COTIZACIÓN PARA JUBILACIÓN?
  SÍ → Subsidio mayores 52 (80 % IPREM, hasta jubilación)
  NO ↓

¿DIFICULTAD ESPECIAL + 12 MESES INSCRITO?
  SÍ → RAI (80 % IPREM, 11 meses, máx. 3 veces)
  NO ↓

¿HOGAR EN RIESGO DE POBREZA?
  SÍ → Ingreso Mínimo Vital (INSS, no SEPE)

¿QUIERES EMPRENDER?
  → Capitalización del desempleo (pago único)
```

---

## Cuándo NO usar esta skill

- Si pregunta por **estadísticas de paro registrado** por municipio,
  sexo o sector → **sepe**.
- Si pregunta por **tipos de contrato** o despido → **laboral-contratos**.
- Si pregunta por **cómo leer una nómina** → **laboral-nominas**.
- Si pregunta por **ERE o ERTE** (procedimiento, negociación) →
  **laboral-ere-erte**.
- Si pregunta por **convenios colectivos** → **laboral-convenios**.
- Si pregunta por **Inspección de Trabajo** → **laboral-inspeccion**.
- Si pregunta por **cotizaciones y afiliación** a la Seguridad Social →
  **seguridad-social**.
- Si pregunta por **obligaciones fiscales del autónomo** →
  **fiscalidad-autonomos**.
- Si pregunta por el **texto de una ley** concreta → **boe**.
