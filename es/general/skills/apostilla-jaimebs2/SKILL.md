---
name: apostilla-jaimebs2
title: Apostilla de La Haya y Legalización de Documentos
description: 'Use when the user asks about the Hague Apostille (Apostilla de La Haya) in Spain: how to apostille a document, which documents need apostille, where to get it (notarial, judicial, administrative), consular legalisation for non-Hague countries, sworn translations (traducción jurada), list of sworn translators, or differences between apostille and legalisation. Triggers on: ''apostilla'', ''Apostilla de La Haya'', ''apostillar documento'', ''legalización consular'', ''traducción jurada'', ''traductor jurado'', ''legalizar documento'', ''apostilla notarial'', ''apostilla título'', ''documento para el extranjero'', ''Convenio de La Haya'', ''apostilla partida de nacimiento'', ''intérprete jurado'', ''MAEC traducción'', ''legalización cadena''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/tramites/apostilla
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# Apostilla de La Haya y Legalización de Documentos

Guía completa sobre la apostilla de documentos en España, la
legalización consular para países no firmantes del Convenio de La Haya
y las traducciones juradas.

> Esta skill orienta sobre el proceso. **No realiza apostillas ni
> legalizaciones.** Los trámites se gestionan en los organismos
> competentes según el tipo de documento.

---

## 1. Qué es la Apostilla de La Haya

La Apostilla es un sello o certificado que se coloca sobre un
documento público para que tenga **validez legal en otro país**
firmante del Convenio de La Haya de 5 de octubre de 1961 (Convenio
suprimiendo la exigencia de legalización de documentos públicos
extranjeros).

### Para qué sirve

Sustituye a la antigua cadena de legalizaciones consulares. Un
documento apostillado en España es reconocido directamente en
cualquiera de los más de **120 países** miembros del Convenio.

### Qué documentos se apostillan

Solo **documentos públicos**:
- Partidas de nacimiento, matrimonio, defunción.
- Certificados de antecedentes penales.
- Títulos académicos y certificados de notas.
- Escrituras notariales (poderes, compraventas, etc.).
- Resoluciones judiciales.
- Documentos administrativos (certificados de la Seguridad Social,
  empadronamiento, etc.).

**No se apostillan** documentos privados (contratos entre particulares,
facturas, cartas).

---

## 2. Dónde apostillar en España

El organismo competente depende del **tipo de documento**:

### Documentos notariales

- **Dónde**: Colegios Notariales (Decanatos) o Tribunales Superiores
  de Justicia (TSJ) de la comunidad autónoma.
- **Ejemplos**: poderes notariales, escrituras, actas notariales,
  testimonios de legitimación de firmas.

### Documentos judiciales

- **Dónde**: Tribunal Superior de Justicia (TSJ) de la comunidad
  autónoma donde se emitió el documento, o Letrado de la Administración
  de Justicia.
- **Ejemplos**: sentencias, autos, certificaciones de juzgados.

### Documentos del Registro Civil

- **Dónde**: Ministerio de Justicia — Subdirección General de
  Cooperación Jurídica Internacional.
- **Ejemplos**: partidas de nacimiento, matrimonio, defunción.
- **URL**: `https://sede.mjusticia.gob.es`

### Documentos administrativos

- **Dónde**: depende del organismo emisor.
  - Documentos de la Administración General del Estado: Ministerio de
    Justicia o el propio ministerio emisor.
  - Documentos autonómicos: órgano designado por la comunidad autónoma.
  - Títulos universitarios oficiales: Ministerio de Educación (o
    universidad para títulos propios, si aplica).

### Documentos académicos

- **Títulos universitarios oficiales**: Ministerio de Educación,
  Formación Profesional y Deportes.
- **Títulos de FP y bachillerato**: Ministerio de Educación o
  consejerías autonómicas.
- **Certificados de notas**: la universidad o centro que los emitió
  (con firma legitimada) y luego apostilla según corresponda.

---

## 3. Legalización consular (países NO firmantes del Convenio de La Haya)

Para países que **no son parte** del Convenio de La Haya (algunos
países de Asia, África, etc.), el documento debe seguir la **cadena
completa de legalización**:

### Cadena de legalización

1. **Autenticación del documento** por el organismo emisor (si no está
   ya autenticado).
2. **Ministerio de Justicia**: legaliza la firma del funcionario o
   notario.
3. **Ministerio de Asuntos Exteriores, Unión Europea y Cooperación
   (MAEC)**: legaliza la firma del Ministerio de Justicia.
   URL: `https://sede.exteriores.gob.es`
4. **Consulado o Embajada** del país de destino en España: legaliza la
   firma del MAEC.

### Plazos y costes

- Cada paso puede tardar **varios días a varias semanas**.
- El MAEC y el Ministerio de Justicia suelen tardar 2-5 días hábiles.
- Los consulados tienen sus propios plazos y tasas.

---

## 4. Traducción jurada

Cuando un documento apostillado o legalizado debe presentarse en un
país cuyo idioma oficial no es el español, generalmente se necesita
una **traducción jurada**.

### Qué es una traducción jurada

Es una traducción oficial realizada por un **traductor-intérprete
jurado** nombrado por el Ministerio de Asuntos Exteriores (MAEC).
Tiene validez legal y lleva la firma, sello y certificación del
traductor.

### Quién puede realizar traducciones juradas

Solo los **traductores-intérpretes jurados** habilitados por el MAEC.
Se obtiene el título mediante:
- Examen convocado por el MAEC.
- Reconocimiento de cualificaciones profesionales (ciudadanos de la
  UE con habilitación equivalente en su país).

### Lista oficial de traductores jurados

El MAEC publica un listado de traductores-intérpretes jurados
por idioma y provincia:

`https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx`

### Diferencia entre traducción jurada y traducción certificada

| | Traducción jurada | Traducción certificada |
|---|---|---|
| **Quién la hace** | Traductor-intérprete jurado (habilitado por MAEC) | Cualquier traductor profesional |
| **Validez legal** | Plena validez ante administraciones y tribunales | Valor informativo; algunas entidades la aceptan |
| **Sello y firma** | Sello oficial del traductor jurado + firma | Firma del traductor + declaración de fidelidad |
| **Cuándo se exige** | Documentos oficiales para la Administración española o extranjera | Documentos internos de empresas, comunicaciones, etc. |

### Coste orientativo

No hay tarifas oficiales fijas. Cada traductor establece sus precios.
Como orientación:
- Página estándar (unas 250 palabras): 25-50 EUR.
- Documentos con formato complejo (tablas, sellos): suplemento.
- Urgencia: recargo habitual del 30-50 %.

---

## 5. Proceso completo: ejemplo práctico

### Ejemplo: título universitario español para trabajar en Argentina

Argentina es firmante del Convenio de La Haya, por lo que basta con
apostilla (no legalización consular):

1. Obtener el título original del Ministerio de Educación (o de la
   universidad si es título propio).
2. **Apostillar** el título en el Ministerio de Educación (títulos
   oficiales) o en el organismo correspondiente.
3. Si Argentina exige el documento en otro idioma, **no aplica** en
   este caso (ambos países son hispanohablantes).
4. Presentar el documento apostillado en Argentina.

### Ejemplo: certificado de nacimiento español para China

China **no es firmante** del Convenio de La Haya, por lo que requiere
legalización consular completa:

1. Obtener la partida de nacimiento del Registro Civil.
2. **Ministerio de Justicia**: legaliza la firma del encargado del
   Registro Civil.
3. **MAEC**: legaliza la firma del Ministerio de Justicia.
4. **Consulado de China en España**: legaliza la firma del MAEC.
5. **Traducción jurada** al chino por un traductor habilitado.

---

## 6. Convenios bilaterales especiales

Algunos países tienen convenios bilaterales con España que **eximen de
apostilla o legalización**:

| País / Convenio | Efecto |
|---|---|
| Francia, Italia, Portugal, Alemania y otros (Convenio de Atenas, 1977) | Documentos del Registro Civil exentos de legalización |
| Países UE (Reglamento 2016/1191) | Documentos públicos de la UE exentos de apostilla para ciertos usos (nacimiento, matrimonio, defunción, etc.). Formularios multilingües opcionales |
| Iberoamérica (Convenio de La Paz, 1984) | Simplificación para documentos de Registro Civil entre países firmantes |

**Importante**: estos convenios no cubren todos los tipos de documentos.
Conviene verificar caso por caso.

---

## 7. Datos prácticos

| Aspecto | Detalle |
|---|---|
| **Apostilla — coste** | Gratuita en la mayoría de organismos. Algunos TSJ cobran tasa judicial |
| **Apostilla — plazo** | 1-5 días hábiles según organismo |
| **Legalización MAEC** | 2-5 días hábiles |
| **Sede MAEC** | `https://sede.exteriores.gob.es` |
| **Sede Ministerio de Justicia** | `https://sede.mjusticia.gob.es` |
| **Lista traductores jurados** | `https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx` |

---

## Cuándo NO usar esta skill

- Si pregunta por el **proceso completo de legalización de documentos
  extranjeros en España** (no españoles para el exterior) →
  **legalizacion-documentos**.
- Si pregunta sobre **homologación de títulos** extranjeros en España →
  skill de homologación de títulos.
- Si pregunta sobre **nacionalidad española** → **extranjeria-nacionalidad**.
- Si pregunta por el **certificado de antecedentes penales** (no su
  apostilla) → **antecedentes-penales**.
- Si pregunta por el **NIE o permiso de residencia** →
  **extranjeria-nie**.
