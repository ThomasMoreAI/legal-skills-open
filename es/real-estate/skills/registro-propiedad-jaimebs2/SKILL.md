---
name: registro-propiedad-jaimebs2
title: Vivienda --- Registro de la Propiedad
description: 'Use when the user asks about the Spanish Land Registry (Registro de la Propiedad): what it is and its purpose, nota simple (what it contains, how to request it, cost), property registration (compraventa, hipoteca, herencia), registral principles (fe pública registral, prioridad, tracto sucesivo, legalidad), difference between Catastro and Registro, certificación registral, or how to use the online portal. Triggers on: ''registro de la propiedad'', ''nota simple'', ''pedir nota simple'', ''nota simple online'', ''inscripción registro'', ''inscribir vivienda'', ''cargas vivienda'', ''cargas registro'', ''fe pública registral'', ''tracto sucesivo'', ''principio de prioridad'', ''registrador'', ''certificación registral'', ''catastro vs registro'', ''diferencia catastro registro'', ''sede registradores'', ''finca registral''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/vivienda/registro-propiedad
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# Vivienda --- Registro de la Propiedad

Guía completa sobre el Registro de la Propiedad en España: qué es,
cómo funciona, nota simple, inscripción de escrituras y principios
registrales.

> Esta skill orienta sobre conceptos y trámites registrales. **No
> sustituye asesoramiento jurídico profesional.**

---

## 1. Qué es el Registro de la Propiedad

El Registro de la Propiedad es una **institución del Estado** que da
publicidad oficial a la situación jurídica de los bienes inmuebles:
quién es su dueño, si tienen cargas (hipotecas, embargos) y otras
circunstancias relevantes.

### Para qué sirve

- **Seguridad jurídica**: quien compra confiando en lo que dice el
  Registro queda protegido (fe pública registral).
- **Publicidad**: cualquier persona puede conocer la situación de un
  inmueble.
- **Prioridad**: el primero que inscribe, prevalece frente a terceros.
- **Prevención de fraudes**: dobles ventas, cargas ocultas.

### Organización

- Hay más de 1.000 Registros de la Propiedad en España.
- Cada uno cubre un **distrito hipotecario** (zona geográfica).
- Están a cargo de **registradores de la propiedad**, funcionarios
  públicos seleccionados por oposición.
- El órgano directivo es la Dirección General de Seguridad Jurídica y
  Fe Pública (dependiente del Ministerio de Justicia).

URL: `https://www.registradores.org`

---

## 2. La nota simple informativa

La **nota simple** es el documento más solicitado del Registro. Es un
extracto que informa sobre la situación jurídica de una finca.

### Qué contiene

| Sección | Información |
|---|---|
| **Titularidad** | Nombre del propietario/s, porcentaje de propiedad, título de adquisición (compraventa, herencia, donación) |
| **Descripción de la finca** | Superficie, linderos, ubicación, referencia catastral |
| **Cargas y gravámenes** | Hipotecas (banco, importe, plazo), embargos, servidumbres, afecciones fiscales, condiciones resolutorias |
| **Notas marginales** | Expedición de certificaciones, procedimientos en curso |

### Cómo solicitarla

| Medio | Detalle | Plazo | Coste |
|---|---|---|---|
| **Online** | `https://sede.registradores.org` — con DNI electrónico, certificado digital o usuario registrado | Minutos a pocas horas | ~9,02 EUR + IVA |
| **Presencial** | Acudir al Registro de la Propiedad correspondiente | 1-3 días | ~9,02 EUR |
| **A través del notario** | Si se está preparando una escritura, el notario la solicita de oficio | Inmediato | Incluido en gastos de notaría |

### Quién puede pedir una nota simple

**Cualquier persona** con interés legítimo. En la práctica, se concede
a:
- Compradores potenciales.
- Propietarios.
- Bancos (para conceder hipotecas).
- Abogados y procuradores.
- Administradores de fincas.

### Nota simple vs. certificación registral

| | Nota simple | Certificación registral |
|---|---|---|
| **Valor jurídico** | Informativo | Prueba fehaciente en juicio |
| **Contenido** | Extracto | Contenido completo (puede incluir historial) |
| **Firma** | Del registrador | Del registrador con fe pública |
| **Coste** | ~9 EUR | ~25-50 EUR |
| **Para qué** | Compraventa, información general | Procedimientos judiciales, herencias |

---

## 3. Inscripción de escrituras

### Qué se inscribe

Se inscriben en el Registro los **títulos públicos** (escrituras
notariales, mandamientos judiciales) que afectan a derechos reales
sobre inmuebles:

- **Compraventa** de una vivienda.
- **Hipoteca** (constitución, cancelación).
- **Herencia** (adjudicación de inmuebles).
- **Donación** de un inmueble.
- **División horizontal** (creación de pisos/locales en un edificio).
- **Obra nueva** (declaración de una construcción).
- **Embargo** (anotación preventiva por mandamiento judicial).
- **Servidumbres** (de paso, luces, vistas).

### Proceso de inscripción

1. El notario remite **copia electrónica** de la escritura al Registro
   (desde 2007, esto es prácticamente inmediato).
2. El registrador **califica** el documento: verifica que cumple todos
   los requisitos legales (principio de legalidad).
3. Si es correcto, lo **inscribe** y devuelve la escritura con nota
   de despacho.
4. Si hay defectos, emite una **calificación negativa** que puede
   recurrirse (ante la DGSJFP o tribunales).

### Plazos

- **Asiento de presentación**: se practica el mismo día que entra el
  documento. Da prioridad (quien presenta primero, inscribe primero).
- **Calificación e inscripción**: plazo legal de **15 días hábiles**
  desde la presentación.
- **Vigencia del asiento de presentación**: 60 días hábiles
  (prorrogables si hay defectos subsanables).

### Aranceles registrales

Los aranceles están regulados por el **RD 1427/1989**. Dependen del
valor del inmueble o de la operación:

| Valor del inmueble | Arancel orientativo de inscripción |
|---|---|
| Hasta 6.010 EUR | 24,04 EUR |
| De 6.010 a 30.050 EUR | 1,75 ‰ |
| De 30.050 a 60.101 EUR | 1,25 ‰ |
| De 60.101 a 150.253 EUR | 0,75 ‰ |
| De 150.253 a 601.012 EUR | 0,30 ‰ |
| Más de 601.012 EUR | 0,20 ‰ |

Arancel máximo por inscripción: **2.181,67 EUR** (salvo excepciones).

---

## 4. Principios registrales

Los principios registrales son las reglas fundamentales que rigen el
funcionamiento del Registro:

### Fe pública registral (art. 34 LH)

El tercero que adquiere de buena fe confiando en el contenido del
Registro queda protegido, aunque luego resulte que el transmitente no
era el verdadero dueño.

**Requisitos**: adquisición de buena fe, a título oneroso, de persona
que aparece en el Registro como titular, e inscripción de su derecho.

### Principio de prioridad (art. 17 LH)

El que primero inscribe, prevalece. Si se presentan dos títulos
incompatibles, se inscribe el que llegó primero al Registro.

### Tracto sucesivo (art. 20 LH)

Para inscribir una transmisión, el transmitente debe figurar como
titular en el Registro. No se puede "saltar" eslabones de la cadena.

**Ejemplo**: para inscribir una venta de A a B, A debe estar inscrito
como propietario. Si A heredó pero no inscribió la herencia, primero
hay que inscribir la herencia.

### Principio de legalidad (art. 18 LH)

El registrador califica la legalidad de los documentos presentados:
verifica identidad, capacidad, forma, contenido y concordancia con el
Registro.

### Principio de legitimación (art. 38 LH)

Se presume que los derechos inscritos **existen y pertenecen** a su
titular en la forma determinada por el asiento. Esta presunción puede
destruirse, pero mientras no se demuestre lo contrario, el Registro
hace fe.

### Principio de especialidad

Cada finca tiene su propia **hoja registral** (folio real). En esa
hoja se inscriben todas las operaciones relativas a esa finca de forma
individualizada.

---

## 5. Catastro vs. Registro de la Propiedad

Dos instituciones diferentes que tratan sobre inmuebles pero con
fines distintos:

| | Catastro | Registro de la Propiedad |
|---|---|---|
| **Depende de** | Ministerio de Hacienda (DG Catastro) | Ministerio de Justicia (DGSJFP) |
| **Finalidad** | Fiscal (base para IBI, ITP, etc.) | Seguridad jurídica (quién es dueño, qué cargas tiene) |
| **Inscripción** | Obligatoria (de oficio o por declaración) | Voluntaria (salvo hipotecas) |
| **Qué identifica** | Parcelas y construcciones (referencia catastral) | Fincas registrales (número de finca) |
| **Superficie** | Gráfica (medición del Catastro) | Jurídica (la que dice la escritura) |
| **Propiedad** | Indica "titularidad catastral" (no prueba propiedad) | Acredita propiedad con fe pública |
| **Valor** | Valor catastral (para impuestos) | No determina valor |

### Discrepancias habituales

Es frecuente que la superficie del Catastro y la del Registro no
coincidan (especialmente en fincas antiguas). Desde 2015 (Ley
13/2015), existe un procedimiento para **coordinar** Catastro y
Registro: se incorpora la representación gráfica catastral a la
inscripción registral.

Para consultar datos catastrales, ver skill **catastro**.

---

## 6. Registro online

El Colegio de Registradores ofrece servicios electrónicos a través
de su sede:

URL: `https://sede.registradores.org`

### Servicios disponibles online

- **Nota simple**: solicitar y recibir notas simples informativas.
- **Consulta de índices**: verificar en qué Registro está inscrita
  una finca.
- **Publicidad formal**: solicitar certificaciones.
- **Seguimiento de documentos**: consultar el estado de una
  inscripción en curso.
- **Registro de la Propiedad abierto** (interoperabilidad con
  notarías y organismos).

### Acceso

Se puede acceder con:
- DNI electrónico.
- Certificado digital (FNMT u otro reconocido).
- Usuario y contraseña registrado en el portal.

---

## 7. Resumen rápido

```
NOTA SIMPLE:
  ├── Qué contiene: titular, descripción, cargas
  ├── Online: sede.registradores.org (~9 EUR + IVA, minutos)
  ├── Presencial: en el Registro (~9 EUR, 1-3 días)
  └── Pedir siempre actualizada antes de comprar

INSCRIPCIÓN:
  ├── El notario envía copia electrónica al Registro
  ├── El registrador califica (15 días hábiles)
  ├── Asiento de presentación da prioridad desde el día 1
  └── Coste: arancel según valor del inmueble

PRINCIPIOS CLAVE:
  ├── Fe pública registral: el Registro protege al comprador de buena fe
  ├── Prioridad: primero que inscribe, prevalece
  ├── Tracto sucesivo: cadena ininterrumpida de titulares
  └── Legalidad: el registrador verifica todo documento

CATASTRO ≠ REGISTRO:
  ├── Catastro → fiscal (base para impuestos)
  └── Registro → jurídico (quién es dueño, qué cargas tiene)
```

---

## Cuándo NO usar esta skill

- Si necesita el **proceso de compraventa completo** (arras, escritura,
  gastos) --> **vivienda-compraventa**.
- Si necesita información sobre **hipotecas** (tipos, TAE, FEIN) -->
  **vivienda-hipotecas**.
- Si pregunta por **datos catastrales** (referencia catastral, valor
  catastral, consulta de inmuebles) --> **catastro**.
- Si pregunta por **comunidad de propietarios** -->
  **vivienda-comunidad-propietarios**.
- Si pregunta por **alquiler de vivienda** --> **vivienda-alquiler**.
- Si pregunta por **ITP, AJD o plusvalía** -->
  **fiscalidad-itp-ajd** o **fiscalidad-impuestos-locales**.
- Si pregunta por **herencias** (sucesiones, adjudicación) -->
  **fiscalidad-sucesiones-donaciones**.
