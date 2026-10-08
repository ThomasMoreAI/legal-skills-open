---
name: crear-empresa-jaimebs2
title: Crear una Empresa en España — Guía Paso a Paso
description: 'Use when the user asks about creating a company in Spain — choosing a legal form, the step-by-step incorporation process, or comparing business structures. Covers: legal forms compared (SL, SLU, SA, SLL, cooperativa, comunidad de bienes, sociedad civil), comparative table (minimum capital, partners, liability, taxation), step-by-step SL incorporation (name certificate, notary, tax registration, Commercial Registry), CIRCE and PAE fast-track, estimated costs (notary, registry, management), the 1-euro SL (Ley Crea y Crece), and post-incorporation obligations. This skill is about creating a company — for becoming self-employed (autónomo persona física) use alta-autonomo. Triggers on: ''crear empresa'', ''montar empresa'', ''constituir SL'', ''crear SL'', ''crear sociedad'', ''sociedad limitada'', ''sociedad anónima'', ''formas jurídicas España'', ''capital mínimo SL'', ''SL de 1 euro'', ''CIRCE'', ''PAE'', ''emprender empresa'', ''constituir sociedad'', ''registro mercantil empresa'',
  ''escritura pública empresa'', ''notario empresa'', ''NIF empresa'', ''empresa en España'', ''mejor forma jurídica''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/emprendimiento/crear-empresa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: corporate
language: es
---

# Crear una Empresa en España — Guía Paso a Paso

Guía completa para constituir una empresa en España: formas jurídicas,
proceso de constitución (especialmente la Sociedad Limitada), vía
telemática, costes y primeras obligaciones.

> **Diferencia con `alta-autonomo`**: esta skill cubre la creación de
> **sociedades mercantiles** (SL, SA, etc.). Si lo que quieres es ser
> autónomo persona física (sin crear empresa), consulta la skill
> **alta-autonomo**.

> Esta skill orienta sobre el proceso de creación de empresas. **No
> sustituye asesoramiento legal ni realiza trámites.**

---

## 1. Formas jurídicas en España

### Comparativa de las principales formas

| Forma jurídica | Capital mínimo | N.º socios | Responsabilidad | Impuesto principal |
|---|---|---|---|---|
| **Sociedad Limitada (SL/SRL)** | 1 € (desde Ley Crea y Crece) | 1+ (SLU si unipersonal) | Limitada al capital aportado | Impuesto de Sociedades (25 %) |
| **Sociedad Anónima (SA)** | 60.000 € (desembolsado 25 % mínimo) | 1+ | Limitada al capital aportado | Impuesto de Sociedades (25 %) |
| **Sociedad Limitada Laboral (SLL)** | 1 € | 2+ trabajadores + socios | Limitada al capital | Impuesto de Sociedades |
| **Sociedad Cooperativa** | Según estatutos | 3+ (1.er grado) | Limitada al capital | Impuesto de Sociedades (régimen especial, 20 %) |
| **Comunidad de Bienes (CB)** | Sin mínimo | 2+ | Ilimitada y solidaria | IRPF (atribución de rentas) |
| **Sociedad Civil (SC)** | Sin mínimo | 2+ | Ilimitada y subsidiaria | IRPF o Sociedades (según actividad) |
| **Autónomo (persona física)** | Sin mínimo | 1 | Ilimitada (patrimonio personal) | IRPF |

### La SL: la forma más habitual

La **Sociedad de Responsabilidad Limitada (SL)** es con diferencia la
forma jurídica más utilizada en España para empresas. Razones:

- **Responsabilidad limitada**: los socios solo responden hasta el
  capital aportado (su patrimonio personal queda protegido).
- **Capital mínimo de 1 €** desde la reforma de la Ley Crea y Crece
  (2022), aunque si el capital es inferior a 3.000 € se aplican
  restricciones (reserva legal del 20 % de beneficios hasta alcanzar
  3.000 €, y responsabilidad solidaria de los socios en caso de
  liquidación).
- **Fiscalidad**: tipo general del Impuesto de Sociedades del 25 %
  (15 % los dos primeros ejercicios con base imponible positiva para
  empresas de nueva creación).
- **Flexibilidad**: puede tener un solo socio (SLU — Sociedad
  Limitada Unipersonal).

### ¿SL o autónomo? Criterios de decisión

| Criterio | Autónomo | SL |
|---|---|---|
| **Responsabilidad** | Ilimitada (patrimonio personal) | Limitada al capital |
| **Coste de constitución** | Gratis (solo alta censal + RETA) | 400-1.500 € (notaría, registro…) |
| **Fiscalidad** | IRPF progresivo (19-47 %) | Sociedades 25 % (15 % primeros años) |
| **Administración** | Sencilla | Contabilidad mercantil, cuentas anuales |
| **Imagen** | — | Mayor percepción de solidez |
| **Recomendado si** | Ingresos bajos-medios, actividad simple | Ingresos altos, riesgo, varios socios |

**Regla práctica**: si los beneficios netos superan los 40.000-50.000 €
anuales, la SL suele ser fiscalmente más ventajosa (25 % fijo vs.
tipos progresivos del IRPF).

---

## 2. Proceso de constitución de una SL — Paso a paso

### Paso 1: Certificación negativa de nombre

Solicitar al **Registro Mercantil Central** un certificado de que el
nombre elegido para la sociedad no está ya registrado.

- Se puede solicitar online: `https://www.rmc.es`
- Se proponen hasta 5 nombres alternativos.
- Plazo de reserva: 6 meses (prorrogable).
- Coste: ~15-20 €.

### Paso 2: Apertura de cuenta bancaria y depósito del capital

- Abrir una cuenta bancaria a nombre de la **sociedad en
  constitución**.
- Depositar el capital social (mínimo 1 €, aunque lo habitual es
  3.000 € o más).
- El banco emite un **certificado de depósito** que necesitarás para
  la escritura.

### Paso 3: Redacción de estatutos

Los estatutos sociales regulan el funcionamiento de la sociedad:

- Denominación y objeto social.
- Domicilio social.
- Capital social y participaciones.
- Órgano de administración (administrador único, solidarios,
  mancomunados o consejo).
- Duración (generalmente indefinida).
- Régimen de transmisión de participaciones.

Se pueden usar **estatutos tipo** (más rápidos y baratos en notaría)
o estatutos personalizados.

### Paso 4: Escritura pública ante notario

Acudir a un notario con:
- Certificación negativa de nombre.
- Certificado de depósito bancario del capital.
- Estatutos sociales.
- DNI/NIE de todos los socios y administradores.

El notario otorga la **escritura de constitución**.

- Coste orientativo: 150-500 € (depende del capital y la complejidad).
- Directorio de notarías: `https://www.notariado.org`

### Paso 5: NIF provisional (AEAT)

- Solicitar el **NIF provisional** de la sociedad en la AEAT (Modelo
  036).
- Se obtiene con la escritura de constitución.
- Válido durante 6 meses, en los que se debe completar la inscripción
  registral.
- URL: `https://sede.agenciatributaria.gob.es`

Detalle del Modelo 036 (páginas, casillas, paso a paso por Sede AEAT) →
skill **fiscalidad-modelo-036**.

### Paso 6: Inscripción en el Registro Mercantil

- Presentar la escritura de constitución en el **Registro Mercantil
  Provincial** correspondiente al domicilio social.
- Plazo máximo: 2 meses desde el otorgamiento de la escritura.
- Una vez inscrita, la sociedad adquiere **plena personalidad
  jurídica**.
- Coste orientativo: 100-250 € (depende del capital).
- Portal: `https://www.registradores.org`

### Paso 7: NIF definitivo

- Tras la inscripción registral, solicitar el **NIF definitivo** en
  la AEAT (Modelo 036).
- A partir de aquí la sociedad opera con su CIF definitivo.

### Paso 8: Alta en el IAE y obligaciones censales

- Modelo 036: declaración censal con los datos de actividad, régimen
  de IVA, epígrafes del IAE, obligaciones periódicas.
- Similar al alta censal de autónomos pero a nombre de la sociedad.
- Si la sociedad va a operar con proveedores/clientes de la UE, aquí
  se solicita también el **alta en el ROI** (casilla 130 + 582/584) →
  ver **fiscalidad-operaciones-intracomunitarias**.

### Paso 9: Alta en la Seguridad Social

- **Administradores y socios trabajadores**: alta en el RETA
  (régimen de autónomos) si poseen el 25 % o más del capital (o el
  33 % si no ejercen funciones de dirección) o si conviven con un
  socio que posea el 50 %.
- **Trabajadores por cuenta ajena**: alta en el Régimen General.
- Trámites a través de Import@ss: `https://importass.seg-social.es`

### Paso 10: Licencia de actividad (si procede)

Si la empresa va a operar en un local físico abierto al público →
consulta la skill **licencias-actividad**.

---

## 3. Vía telemática: CIRCE y PAE

### CIRCE (Centro de Información y Red de Creación de Empresas)

Sistema telemático que permite crear una SL (y otras formas) a
través de un proceso acelerado y unificado.

URL: `https://www.circe.es`

### PAE (Punto de Atención al Emprendedor)

Oficinas (presenciales y online) adheridas al sistema CIRCE donde un
asesor te guía por todo el proceso:

- Rellena el **Documento Único Electrónico (DUE)**.
- Coordina notaría, Registro Mercantil, AEAT y Seguridad Social.
- Puede reducir el plazo de constitución a **48 horas** usando
  estatutos tipo.

### Ventajas de CIRCE/PAE

- Proceso unificado (un solo punto de contacto).
- Más rápido que la vía tradicional.
- Costes reducidos si se usan estatutos tipo.
- Permite crear SL, SLNE, autónomos y emprendedores de
  responsabilidad limitada.

### Desventajas

- Menos flexibilidad en los estatutos.
- No todas las formas jurídicas están disponibles.
- Depende de la disponibilidad de los PAE en cada zona.

---

## 4. La SL de 1 euro (Ley Crea y Crece)

Desde la reforma de la Ley 18/2022 de Creación y Crecimiento de
Empresas (Ley Crea y Crece):

### Cambios principales

- **Capital mínimo de 1 €** para la SL (antes 3.000 €).
- Mientras el capital sea inferior a 3.000 €:
  - Reserva legal obligatoria del 20 % del beneficio (hasta alcanzar
    3.000 €).
  - Si la sociedad se liquida con deudas y capital < 3.000 €, los
    socios responden solidariamente hasta los 3.000 €.
- **Constitución online** obligatoria para todas las SL (aún en
  implantación progresiva).

### ¿Es recomendable constituir con 1 €?

- **Ventaja**: reduce la barrera de entrada.
- **Inconveniente**: las restricciones (reserva del 20 %, responsabilidad
  solidaria) hacen que en la práctica muchos emprendedores sigan
  constituyendo con 3.000 € para evitar complicaciones.
- **Consejo**: si puedes aportar 3.000 €, hazlo. Evitas las
  restricciones y transmites mayor solvencia.

---

## 5. Costes orientativos de constitución

| Concepto | Coste orientativo |
|---|---|
| Certificación negativa de nombre | 15-20 € |
| Notaría (escritura de constitución) | 150-500 € |
| Registro Mercantil (inscripción) | 100-250 € |
| Impuesto de Transmisiones Patrimoniales (ITP/OS) | Exento desde 2010 |
| Gestoría (si contratas una para todo el proceso) | 300-800 € |
| **Total orientativo (vía tradicional)** | **400-1.500 €** |
| **Total orientativo (vía CIRCE con estatutos tipo)** | **200-600 €** |

### Plazos orientativos

| Vía | Plazo habitual |
|---|---|
| Tradicional (notario + registro) | 2-4 semanas |
| CIRCE/PAE con estatutos tipo | 48 horas - 1 semana |
| CIRCE/PAE con estatutos personalizados | 1-3 semanas |

---

## 6. Obligaciones tras la constitución

Una vez constituida la sociedad, las obligaciones principales son:

### Obligaciones fiscales

- **Impuesto de Sociedades** (Modelo 200): declaración anual. Tipo
  general 25 %, reducido 15 % los dos primeros ejercicios con beneficio.
- **IVA trimestral** (Modelo 303) e IRPF retenciones (Modelos 111,
  115) si corresponde.
- **Modelo 349** si hay operaciones con la UE → ver
  **fiscalidad-operaciones-intracomunitarias**.
- **Facturación**: cumplir el RD 1619/2012, obligación progresiva de
  factura electrónica y VeriFactu desde 2026 → ver
  **fiscalidad-facturacion**.
- **Cuentas anuales**: depósito obligatorio en el Registro Mercantil
  dentro de los 7 meses siguientes al cierre del ejercicio.

### Obligaciones contables

- **Contabilidad mercantil**: libro diario, libro de inventarios y
  cuentas anuales, conforme al Plan General de Contabilidad.
- **Libros de actas**: registro de los acuerdos de la junta de socios.
- **Libro de socios**: registro de las participaciones.
- **Legalización de libros**: anual ante el Registro Mercantil.

### Obligaciones con la Seguridad Social

- Cotización de administradores y socios trabajadores (RETA).
- Cotización de trabajadores por cuenta ajena (Régimen General).

---

## 7. Recursos y enlaces útiles

| Recurso | URL |
|---|---|
| CIRCE (creación telemática de empresas) | `https://www.circe.es` |
| Colegio de Registradores (Registro Mercantil) | `https://www.registradores.org` |
| Registro Mercantil Central (certificación de nombre) | `https://www.rmc.es` |
| Consejo General del Notariado | `https://www.notariado.org` |
| Sede Electrónica AEAT | `https://sede.agenciatributaria.gob.es` |
| Import@ss (alta en Seguridad Social) | `https://importass.seg-social.es` |
| EUGO (ventanilla única de servicios) | `https://eugo.es` |
| Portal CIRCE — PAE | `https://www.circe.es/CIRCE.PAE.Web/guest/homePae` |

---

## Cuándo NO usar esta skill

- Si quieres ser **autónomo persona física** (sin crear empresa) →
  **alta-autonomo**.
- Si ya tienes empresa y preguntas por **obligaciones fiscales** del
  Impuesto de Sociedades → **fiscalidad-sociedades**.
- Si preguntas por **obligaciones fiscales de autónomos** (IVA, IRPF,
  calendario) → **fiscalidad-autonomos**.
- Si preguntas por **detalle del Modelo 036** (casillas, supuestos,
  ROI) → **fiscalidad-modelo-036**.
- Si preguntas por **operaciones intracomunitarias** (ROI/VIES,
  reverse charge, Modelo 349) → **fiscalidad-operaciones-intracomunitarias**.
- Si preguntas por **facturación** (datos obligatorios, VeriFactu,
  factura electrónica) → **fiscalidad-facturacion**.
- Si preguntas por **licencias de actividad y apertura** →
  **licencias-actividad**.
- Si preguntas por **datos del Registro Mercantil** (consulta de
  empresas existentes, actos registrales) → **borme**.
- Si preguntas por **cuotas de Seguridad Social** del administrador →
  **seguridad-social**.
- Si preguntas por el **certificado digital** o **Cl@ve** →
  **certificado-digital** / **clave**.
