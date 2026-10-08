---
name: legalizacion-documentos-jaimebs2
title: Legalización de Documentos Extranjeros en España
description: 'Use when the user asks about legalising foreign documents for use in Spain: how to validate a foreign degree, birth certificate, marriage certificate, or other official document in Spain, the legalisation chain, sworn translations for the Spanish administration, which documents need translation and which do not, or the MAEC list of sworn translators. This skill focuses on bringing foreign documents INTO Spain (the reverse direction of the apostilla skill). Triggers on: ''legalizar documento extranjero'', ''documento extranjero España'', ''validar documento extranjero'', ''traducción jurada para España'', ''legalización documentos España'', ''cadena de legalización'', ''documento legalizado'', ''MAEC legalización'', ''traer documentos del extranjero'', ''registro civil documento extranjero'', ''inscripción matrimonio extranjero'', ''certificado extranjero España'', ''traducir documento para España''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/tramites/legalizacion-documentos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# Legalización de Documentos Extranjeros en España

Guía completa sobre cómo dar validez legal en España a documentos
emitidos en el extranjero: proceso de legalización, apostilla,
traducciones juradas y casos prácticos.

> Esta skill orienta sobre el proceso. **No realiza legalizaciones
> ni traducciones.** Los trámites se gestionan en los organismos
> competentes.

---

## 1. Cuándo se necesita legalizar un documento extranjero

Un documento público emitido en el extranjero (certificado de
nacimiento, título académico, sentencia judicial, certificado de
antecedentes, etc.) generalmente necesita ser **legalizado** para que
la Administración española lo acepte como válido.

### Escenarios habituales

- **Inscripción de nacimiento extranjero** en el Registro Civil
  español.
- **Inscripción de matrimonio celebrado en el extranjero**.
- **Solicitud de nacionalidad española**: certificados de nacimiento,
  matrimonio, antecedentes penales del país de origen.
- **Homologación de títulos académicos** extranjeros.
- **Trámites de extranjería**: reagrupación familiar, arraigo,
  renovación de permisos.
- **Registro de defunción** en España de un fallecimiento en el
  extranjero.
- **Poderes notariales** otorgados en el extranjero.

---

## 2. Tres vías según el país de origen

El proceso depende de si el país emisor del documento es:

### A) País firmante del Convenio de La Haya

Si el país es firmante del Convenio de La Haya (más de 120 países),
basta con que el documento lleve la **Apostilla de La Haya** emitida
por la autoridad competente del país de origen.

**Proceso**:
1. Obtener el documento original en el país de origen.
2. Apostillar el documento en la autoridad competente del país emisor.
3. Traducir al español por traductor jurado (si el documento no está
   en español).
4. Presentar en la Administración española.

### B) País con convenio bilateral de exención

Algunos países tienen convenios bilaterales con España que **eximen
de legalización**:

| Convenio | Países | Documentos exentos |
|---|---|---|
| **Convenio de Atenas (1977)** | Francia, Italia, Alemania, Portugal, Bélgica, Luxemburgo, Países Bajos, Turquía, Austria, etc. | Documentos del Registro Civil |
| **Reglamento UE 2016/1191** | Todos los países de la UE | Documentos públicos para ciertos usos (nacimiento, matrimonio, defunción, capacidad matrimonial, domicilio, nacionalidad). Formularios multilingües opcionales |
| **Convenio de La Paz (1984)** | Varios países iberoamericanos | Documentos del Registro Civil |

**Importante**: estos convenios no cubren todos los tipos de
documentos. Los títulos académicos, por ejemplo, generalmente necesitan
apostilla aunque exista convenio bilateral para documentos civiles.

### C) País sin convenio (legalización consular completa)

Si el país no es firmante del Convenio de La Haya ni tiene convenio
bilateral, el documento necesita la **cadena completa de legalización**:

1. **Autoridad local** del país emisor: autentica el documento.
2. **Ministerio de Asuntos Exteriores** del país emisor: legaliza la
   firma de la autoridad local.
3. **Consulado o Embajada de España** en el país emisor: legaliza la
   firma del Ministerio de Asuntos Exteriores.
4. **Ministerio de Asuntos Exteriores de España (MAEC)**: legaliza la
   firma del consulado español (en algunos casos se omite este paso).

URL del MAEC: `https://sede.exteriores.gob.es`

---

## 3. Traducción jurada

### Cuándo es necesaria

Todo documento en idioma distinto del español (castellano) que se
presente ante la Administración española debe ir acompañado de una
**traducción jurada** al español.

### Excepciones

- Documentos en **portugués**: algunos procedimientos aceptan
  documentos en portugués sin traducción (especialmente entre España
  y Portugal por convenios bilaterales, y en algunos registros civiles
  para documentos de países lusófonos).
- Documentos con **formulario multilingüe** del Reglamento UE
  2016/1191: no necesitan traducción si se adjunta el formulario en
  español.
- Comunidades autónomas con **lengua cooficial**: los documentos en
  catalán, euskera, gallego o valenciano son válidos sin traducción
  ante las administraciones de esas comunidades.

### Quién puede hacer traducciones juradas

Solo los **traductores-intérpretes jurados** habilitados por el MAEC,
o los que tengan reconocimiento equivalente en la UE.

Lista oficial de traductores jurados del MAEC:
`https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx`

### Traducciones realizadas en el extranjero

Las traducciones realizadas por traductores jurados de otros países
generalmente no son válidas directamente en España. Excepciones:

- Traducciones hechas por funcionarios consulares o diplomáticos
  españoles.
- Traducciones realizadas por traductores jurados de países de la UE
  con reconocimiento mutuo de cualificaciones.

Si la traducción se hizo en el extranjero y no cumple estos requisitos,
la Administración española puede exigir una nueva traducción jurada
por un traductor habilitado en España.

---

## 4. Proceso paso a paso: ejemplos prácticos

### Ejemplo 1: Certificado de nacimiento colombiano para nacionalidad española

Colombia es firmante del Convenio de La Haya:
1. Obtener certificado de nacimiento actualizado en Colombia.
2. **Apostillar** en Colombia (Ministerio de Relaciones Exteriores
   colombiano o entidades autorizadas).
3. El documento está en español → **no necesita traducción**.
4. Presentar ante el Registro Civil español con la solicitud de
   nacionalidad.

### Ejemplo 2: Título universitario marroquí para homologación en España

Marruecos no es firmante del Convenio de La Haya:
1. Obtener el título original en Marruecos.
2. **Legalización consular completa**:
   - Ministerio de Educación marroquí (autentica).
   - Ministerio de Asuntos Exteriores marroquí (legaliza).
   - Consulado de España en Marruecos (legaliza).
3. **Traducción jurada** al español (el título está en árabe/francés).
4. Presentar ante el Ministerio de Educación español para
   homologación.

### Ejemplo 3: Partida de matrimonio francesa para inscripción en España

Francia tiene Convenio de Atenas con España:
1. Obtener la partida de matrimonio en Francia (acte de mariage).
2. **Exenta de apostilla** para Registro Civil (Convenio de Atenas).
3. **Traducción jurada** al español (o formulario multilingüe UE).
4. Presentar ante el Registro Civil consular o en España.

---

## 5. Dónde presentar documentos extranjeros legalizados

| Trámite | Organismo | URL |
|---|---|---|
| Inscripción Registro Civil | Registro Civil Central o consular | `https://sede.mjusticia.gob.es` |
| Nacionalidad española | Registro Civil / Ministerio de Justicia | `https://sede.mjusticia.gob.es` |
| Homologación de títulos | Ministerio de Educación | `https://www.educacionfpydeportes.gob.es` |
| Trámites de extranjería | Oficina de Extranjería | `https://sede.administracionespublicas.gob.es` |
| Inscripción en la Seguridad Social | TGSS | `https://importass.seg-social.es` |

---

## 6. Preguntas frecuentes

**¿Cuánto cuesta legalizar un documento?**
La apostilla en el país de origen varía según el país (desde gratuita
hasta 50-100 EUR). Las tasas consulares españolas también varían. La
traducción jurada depende del traductor (orientativamente 25-50 EUR
por página estándar).

**¿Caduca la legalización o apostilla?**
No, la apostilla o legalización no caduca. Sin embargo, algunos
documentos (como el certificado de antecedentes penales) tienen una
validez temporal y se exige que sean recientes (generalmente menos de
3-6 meses).

**¿Puedo legalizar una fotocopia?**
No. La apostilla o legalización se realiza sobre el **documento
original** (o una copia oficial certificada por el organismo emisor).
Las fotocopias simples no son legalizables.

**¿Qué hago si el país de origen ya no existe (URSS, Yugoslavia, etc.)?**
Los documentos emitidos por estados desaparecidos son generalmente
válidos. Se apostillan o legalizan a través del estado sucesor que
controle el registro correspondiente.

---

## 7. Datos prácticos

| Aspecto | Detalle |
|---|---|
| **MAEC — Legalizaciones** | `https://sede.exteriores.gob.es` |
| **Ministerio de Justicia** | `https://sede.mjusticia.gob.es` |
| **Lista traductores jurados** | `https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Traductores-Interpretes-Jurados.aspx` |
| **Convenio de La Haya — países firmantes** | `https://www.hcch.net/es/instruments/conventions/status-table/?cid=41` |

---

## Cuándo NO usar esta skill

- Si pregunta por **apostillar un documento español para el
  extranjero** (dirección inversa) → **apostilla**.
- Si pregunta sobre **homologación de títulos** académicos extranjeros
  (el proceso educativo completo) → skill de homologación de títulos.
- Si pregunta sobre **nacionalidad española** (proceso completo) →
  **extranjeria-nacionalidad**.
- Si pregunta por el **NIE o permiso de residencia** →
  **extranjeria-nie**.
- Si pregunta por **antecedentes penales** (no su legalización) →
  **antecedentes-penales**.
- Si pregunta por el **texto de un convenio internacional** → **boe**.
