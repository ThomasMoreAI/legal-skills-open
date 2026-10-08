---
name: alta-autonomo-jaimebs2
title: Alta como Autónomo — Tutorial Paso a Paso
description: 'Use when the user asks how to become self-employed (autónomo) in Spain — the step-by-step process from zero to first invoice. Covers: getting digital ID (Cl@ve, certificado digital), registering with the tax agency (alta censal, Modelo 036/037, choosing IAE code), registering with Social Security (RETA via Import@ss), flat-rate quota (tarifa plana), municipal opening notice, first obligations (invoicing, bookkeeping), document checklist, estimated first-year cost, and capitalising unemployment benefit (pago único). This skill is about the PROCESS of becoming autónomo — for ongoing tax obligations once already registered, use fiscalidad-autonomos. Triggers on: ''hacerme autónomo'', ''darme de alta como autónomo'', ''cómo ser autónomo'', ''alta autónomo paso a paso'', ''tarifa plana autónomos'', ''Import@ss alta'', ''cuánto cuesta ser autónomo'', ''requisitos autónomo'', ''primer año autónomo'', ''capitalización desempleo'', ''pago único autónomos'', ''alta RETA'', ''alta censal
  autónomo'', ''emprender como autónomo'', ''autónomo por primera vez'', ''pasos para ser autónomo''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/emprendimiento/alta-autonomo
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

# Alta como Autónomo — Tutorial Paso a Paso

Guía práctica y cronológica para darse de alta como trabajador autónomo
(persona física con actividad económica) en España. Desde cero hasta
emitir tu primera factura.

> **Diferencia con `fiscalidad-autonomos`**: esta skill cubre el
> **proceso de alta** (cómo convertirte en autónomo). La skill
> `fiscalidad-autonomos` cubre las **obligaciones fiscales continuas**
> una vez ya estás dado de alta (IVA, IRPF, calendario fiscal, etc.).

> Esta skill orienta sobre los trámites de alta. **No sustituye
> asesoramiento profesional ni realiza trámites.**

---

## 1. Antes de empezar: documentación previa

### Requisitos básicos

- Ser mayor de 18 años.
- Tener NIE o DNI en vigor.
- No estar inhabilitado para ejercer la actividad.
- Si eres extranjero no comunitario: permiso de trabajo por cuenta
  propia.

### Decidir tu actividad

Antes de darte de alta, ten claro:

1. **Qué actividad vas a realizar** — necesitarás elegir un epígrafe
   del IAE (Impuesto de Actividades Económicas).
2. **Si necesitas licencia de actividad** (local físico, hostelería,
   etc.) → consulta la skill **licencias-actividad**.
3. **Si necesitas colegiación** — algunas profesiones reguladas la
   exigen (abogados, médicos, arquitectos…).
4. **Si necesitas seguro de responsabilidad civil** — obligatorio en
   algunas actividades, recomendable en casi todas.

---

## 2. Paso 1 — Obtener identificación digital

Para hacer los trámites online (muy recomendable), necesitas
identificación electrónica. Hay dos opciones principales:

### Cl@ve

Sistema de identificación del gobierno. Dos modalidades:

- **Cl@ve PIN**: código temporal por app o SMS. Sirve para trámites
  puntuales.
- **Cl@ve permanente**: usuario y contraseña reutilizable.

**Cómo registrarse**:
- Presencialmente en oficinas de la AEAT, Seguridad Social o
  ayuntamientos adheridos.
- Por videollamada.
- Con carta de invitación (si tienes DNI electrónico).

URL: `https://clave.gob.es`

### Certificado digital (FNMT)

Certificado electrónico emitido por la Fábrica Nacional de Moneda y
Timbre. Más potente que Cl@ve — permite todos los trámites.

**Pasos**:
1. Solicitar online en `https://www.sede.fnmt.gob.es/certificados/persona-fisica`
2. Acreditar identidad: presencialmente en oficina de registro o con
   DNI electrónico.
3. Descargar e instalar el certificado en tu navegador.

**Consejo**: obtener el certificado digital antes de empezar los
trámites de alta ahorra mucho tiempo.

Para más detalle → skill **certificado-digital** y skill **clave**.

---

## 3. Paso 2 — Alta en Hacienda (AEAT)

El primer trámite fiscal: la **declaración censal** mediante el
Modelo 036 o 037.

### Modelo 037 vs. 036

| | Modelo 037 (simplificado) | Modelo 036 (completo) |
|---|---|---|
| **Para quién** | Autónomos persona física en estimación directa simplificada y régimen general de IVA | Todos los demás casos |
| **Cuándo usar 036** | — | Estimación directa normal, módulos, SII, operaciones intracomunitarias, varios locales |
| **Recomendación** | La mayoría de nuevos autónomos pueden usar el 037 | Usa el 036 si tu caso no encaja en el 037 |

Para el detalle de casillas, estructura del modelo por páginas y
supuestos de modificación posteriores (cambio de domicilio, alta en ROI,
cambio de régimen) → skill **fiscalidad-modelo-036**.

### Qué se decide en el alta censal

1. **Epígrafe del IAE**: código que identifica tu actividad.
   - Sección 1.ª: actividades empresariales (comercio, hostelería…).
   - Sección 2.ª: actividades profesionales (diseñadores, consultores,
     programadores…). Estas aplican retención de IRPF en factura.
   - Sección 3.ª: actividades artísticas.
   - Puedes tener más de un epígrafe si realizas varias actividades.

2. **Régimen de IRPF**:
   - Estimación directa simplificada (por defecto, la más habitual).
   - Estimación directa normal.
   - Estimación objetiva (módulos) — solo actividades incluidas en la
     Orden de Módulos anual.

3. **Régimen de IVA**:
   - General (por defecto).
   - Simplificado (módulos).
   - Recargo de equivalencia (comerciantes minoristas).

4. **Obligaciones periódicas**: modelos que vas a presentar (303 IVA,
   130/131 IRPF, etc.).

5. **Domicilio fiscal y local** afecto a la actividad (si existe).

### Cómo presentarlo

- **Online**: con certificado digital o Cl@ve en la Sede Electrónica
  de la AEAT.
- **Presencial**: en oficinas de la AEAT con cita previa.

URL: `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G322.shtml`

### Fecha del alta censal

El alta censal debe hacerse **antes de iniciar la actividad** (antes
de emitir la primera factura). El modelo permite indicar la fecha de
inicio de actividad.

---

## 4. Paso 3 — Alta en la Seguridad Social (RETA)

Después del alta en Hacienda (o simultáneamente), hay que darse de
alta en el Régimen Especial de Trabajadores Autónomos (RETA).

### Plazo

El alta en la Seguridad Social debe hacerse **dentro de los 60 días
anteriores al inicio de actividad**. Si se hace después, se considerará
alta fuera de plazo y no se podrá acceder a la tarifa plana.

### Cómo hacerlo: Import@ss

El trámite se hace online a través de **Import@ss**, el portal de la
Seguridad Social:

URL: `https://importass.seg-social.es`

Pasos en Import@ss:
1. Acceder con certificado digital o Cl@ve.
2. Seleccionar "Alta en trabajo autónomo".
3. Indicar la fecha de inicio de actividad (debe coincidir con el alta
   censal).
4. Elegir la base de cotización (desde 2023, sistema de cotización por
   ingresos reales).
5. Elegir mutua colaboradora (para IT, accidentes de trabajo y cese de
   actividad).
6. Indicar la actividad (CNAE) y el epígrafe del IAE.

### Tarifa plana para nuevos autónomos

Si es tu primera alta como autónomo (o han pasado más de 2 años desde
la última baja, o 3 si disfrutaste de tarifa plana anteriormente):

| Periodo | Cuota mensual (2024-2025) |
|---|---|
| Primeros 12 meses | 80 €/mes |
| Meses 13-24 | 80 €/mes (si ingresos netos < SMI) |

**Requisitos**:
- No haber estado de alta como autónomo en los 2 años anteriores (3 si
  se disfrutó antes de tarifa plana).
- Darse de alta en plazo (no fuera de plazo).
- No ser autónomo colaborador familiar.

La tarifa plana se solicita directamente al darse de alta en
Import@ss.

### Cotización por ingresos reales

Desde 2023, los autónomos cotizan en función de sus ingresos netos
reales. El sistema tiene 15 tramos con bases y cuotas distintas. Al
darte de alta eliges un tramo según tu previsión de ingresos, y al
final del año la Seguridad Social regulariza.

Para más detalle sobre cotización → skill **seguridad-social**.

---

## 5. Paso 4 — Comunicación al ayuntamiento (si procede)

### ¿Cuándo es necesario?

- Si vas a abrir un **local abierto al público** (tienda, oficina con
  atención al público, taller, restaurante…).
- Si tu actividad requiere **licencia de actividad o declaración
  responsable**.

### Tipos de trámite

- **Declaración responsable**: para actividades inocuas (oficinas,
  pequeño comercio sin impacto ambiental). Se presenta y se puede
  empezar a operar de inmediato.
- **Licencia de actividad**: para actividades clasificadas (molestas,
  insalubres, nocivas o peligrosas). Requiere proyecto técnico y
  aprobación previa.

Para detalle → skill **licencias-actividad**.

### Si trabajas desde casa

Si trabajas desde casa sin atención al público, generalmente **no
necesitas** licencia de actividad ni comunicación al ayuntamiento.
Verifica con tu ayuntamiento, ya que algunos tienen regulación
específica para actividades domiciliarias.

---

## 6. Paso 5 — Primeras obligaciones

Una vez dado de alta, tus obligaciones inmediatas son:

### Facturación

- Emitir factura por cada operación con todos los datos obligatorios.
- Numeración correlativa sin saltos.
- Conservar facturas emitidas y recibidas durante 4 años.

### Libros registro

Según tu régimen, deberás llevar:
- Libro de ingresos.
- Libro de gastos.
- Libro de bienes de inversión.
- Libros registro de facturas emitidas y recibidas (IVA).

### Impuestos trimestrales

Cada trimestre (abril, julio, octubre, enero) deberás presentar:
- **Modelo 303**: IVA.
- **Modelo 130/131**: pago fraccionado del IRPF.
- Otros modelos si corresponde (111, 115).

Para detalle completo de obligaciones fiscales → skill
**fiscalidad-autonomos**.

### Cuota de autónomos

Pago mensual a la Seguridad Social. Se domicilia y se cobra el último
día hábil de cada mes.

---

## 7. Checklist completo del alta

```
ANTES DE EMPEZAR:
  □ DNI/NIE en vigor
  □ Decidir actividad y epígrafe IAE
  □ Comprobar si necesitas colegiación
  □ Comprobar si necesitas licencia de actividad

IDENTIFICACIÓN DIGITAL (hacer primero):
  □ Obtener certificado digital FNMT
     o registrarse en Cl@ve

ALTA EN HACIENDA:
  □ Presentar Modelo 036 o 037
  □ Elegir epígrafe IAE
  □ Elegir régimen de IRPF
  □ Elegir régimen de IVA
  □ Indicar obligaciones periódicas
  □ Indicar fecha de inicio de actividad
  □ ¿Vas a comprar/vender a proveedores o clientes de la UE?
    → Solicitar alta en ROI en el mismo 036 (casilla 130 + 582/584)
    → Ver fiscalidad-modelo-036 y fiscalidad-operaciones-intracomunitarias

ALTA EN SEGURIDAD SOCIAL:
  □ Alta en RETA vía Import@ss
  □ Solicitar tarifa plana (si corresponde)
  □ Elegir mutua colaboradora
  □ Elegir base de cotización inicial

AYUNTAMIENTO (si procede):
  □ Declaración responsable o licencia de actividad

DESPUÉS DEL ALTA:
  □ Abrir cuenta bancaria separada (recomendado)
  □ Contratar seguro de responsabilidad civil (si procede)
  □ Empezar a llevar los libros registro
  □ Facturar correctamente
  □ Reservar 30-35 % de cada factura para impuestos y SS
```

---

## 8. Cuánto cuesta ser autónomo el primer año

Estimación orientativa de costes fijos el primer año (sin contar la
propia actividad):

| Concepto | Coste orientativo |
|---|---|
| Cuota de autónomos (tarifa plana, 12 meses × 80 €) | ~960 €/año |
| Cuota de autónomos (sin tarifa plana, base mínima) | ~3.500-4.000 €/año |
| Gestoría / asesoría fiscal (si contratas una) | 50-150 €/mes |
| Certificado digital FNMT | Gratuito |
| Seguro de responsabilidad civil | Variable (100-500 €/año según actividad) |
| Licencia de actividad (si procede) | Variable (100-1.000+ € según municipio y actividad) |

**Coste mínimo con tarifa plana**: unos **80 €/mes** si gestionas tú
mismo los impuestos. Con gestoría, unos **130-230 €/mes**.

---

## 9. Capitalización del desempleo (pago único)

Si estás cobrando prestación por desempleo y quieres hacerte autónomo,
puedes solicitar la **capitalización del desempleo** (pago único):

### Qué es

El SEPE te abona de una sola vez (o en pagos periódicos) la prestación
que te queda por cobrar, para que la inviertas en tu nueva actividad.

### Modalidades

- **Pago único**: para la inversión necesaria para iniciar la
  actividad (incluye la cuota de autónomos).
- **Abono mensual de cuotas**: el SEPE paga directamente tus cuotas
  de autónomos con cargo a la prestación pendiente.
- **Combinación de ambas**: parte como pago único para inversión y
  parte para cuotas.

### Requisitos principales

- Tener pendiente al menos 3 meses de prestación.
- No haber usado el pago único en los 4 años anteriores.
- Iniciar la actividad en el plazo de 1 mes desde la resolución.
- Solicitar la capitalización **antes** de darse de alta como
  autónomo.

### Dónde solicitarlo

En el SEPE (Servicio Público de Empleo Estatal):
`https://www.sepe.es`

---

## 10. Orden cronológico resumido

```
1. PREPARACIÓN
   ├── Decidir actividad y epígrafe IAE
   ├── Obtener certificado digital o Cl@ve
   └── Solicitar capitalización desempleo (si procede) ← ANTES del alta

2. ALTAS (mismo día o días consecutivos)
   ├── Alta en Hacienda (Modelo 036/037) ← primero
   └── Alta en Seguridad Social (RETA vía Import@ss) ← mismo día o siguiente

3. AYUNTAMIENTO (si procede)
   └── Declaración responsable o licencia de actividad

4. PUESTA EN MARCHA
   ├── Abrir cuenta bancaria profesional
   ├── Contratar seguro RC (si procede)
   ├── Empezar a facturar
   └── Llevar libros y reservar para impuestos
```

**Importante**: el alta en Hacienda y en la Seguridad Social deben ser
en la misma fecha o con muy pocos días de diferencia. La fecha de
inicio de actividad debe coincidir en ambas.

---

## 11. Recursos y enlaces útiles

| Recurso | URL |
|---|---|
| Import@ss (alta en Seguridad Social) | `https://importass.seg-social.es` |
| Alta censal AEAT (Modelo 036/037) | `https://sede.agenciatributaria.gob.es/Sede/procedimientoini/G322.shtml` |
| Portal Cl@ve | `https://clave.gob.es` |
| Certificado digital FNMT | `https://www.sede.fnmt.gob.es/certificados/persona-fisica` |
| Ventanilla Única Empresarial | `https://www.one.gob.es/` |
| SEPE (capitalización desempleo) | `https://www.sepe.es` |
| EUGO (ventanilla única de servicios) | `https://eugo.es` |

---

## Cuándo NO usar esta skill

- Si ya eres autónomo y preguntas por **obligaciones fiscales
  continuas** (IVA, IRPF, calendario, facturación) →
  **fiscalidad-autonomos**.
- Si preguntas por **detalle del Modelo 036** (casillas, supuestos de
  modificación, alta en ROI, navegación Sede AEAT) →
  **fiscalidad-modelo-036**.
- Si preguntas por **detalle del IVA** (cálculo del Modelo 303, tipos,
  exenciones) → **fiscalidad-iva**.
- Si preguntas por **detalle del IRPF** (Modelo 130/131, gastos
  deducibles) → **fiscalidad-irpf-autonomos**.
- Si preguntas por **operaciones con la UE** (ROI, VIES, reverse
  charge, Modelo 349) → **fiscalidad-operaciones-intracomunitarias**.
- Si preguntas por **facturación** (datos obligatorios, factura
  electrónica, VeriFactu) → **fiscalidad-facturacion**.
- Si preguntas por **cuotas de Seguridad Social, bases, tramos** →
  **seguridad-social**.
- Si preguntas por **crear una empresa** (SL, SA) en vez de ser
  autónomo persona física → **crear-empresa**.
- Si preguntas por **licencias de actividad y apertura** →
  **licencias-actividad**.
- Si necesitas el **certificado digital** o **Cl@ve** en detalle →
  **certificado-digital** / **clave**.
- Si preguntas por **datos del Registro Mercantil** → **borme**.
