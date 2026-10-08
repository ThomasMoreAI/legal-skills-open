---
name: antecedentes-penales-jaimebs2
title: Certificado de Antecedentes Penales
description: 'Use when the user asks about the criminal record certificate (certificado de antecedentes penales) in Spain: how to request it online or in person, what it is used for (employment, public exams, adoption, nationality, travel), sexual offence certificate (delitos de naturaleza sexual) required for working with minors, cancellation of criminal records, or requirements from the Ministry of Justice. Triggers on: ''antecedentes penales'', ''certificado de penales'', ''certificado antecedentes'', ''delitos sexuales certificado'', ''registro central de penados'', ''cancelación antecedentes'', ''penales para trabajar'', ''penales para oposiciones'', ''penales para nacionalidad'', ''Ministerio de Justicia certificado'', ''antecedentes penales online'', ''penales para adopción'', ''penales para visado'', ''trabajar con menores certificado''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/tramites/antecedentes-penales
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: criminal
language: es
---

# Certificado de Antecedentes Penales

Guía completa sobre el certificado de antecedentes penales en España:
qué es, para qué se necesita, cómo solicitarlo (online y
presencialmente), el certificado de delitos de naturaleza sexual y la
cancelación de antecedentes.

> Esta skill orienta sobre el trámite. **No emite certificados ni
> accede al Registro Central de Penados.** La solicitud se realiza a
> través de la sede electrónica del Ministerio de Justicia o
> presencialmente.

---

## 1. Qué es el certificado de antecedentes penales

Es un documento oficial emitido por el **Registro Central de Penados y
Rebeldes** (dependiente del Ministerio de Justicia) que certifica si
una persona tiene o no condenas penales inscritas.

### Para qué se pide

- **Empleo**: muchas empresas lo solicitan al contratar, especialmente
  en sectores regulados (seguridad privada, banca, transporte, etc.).
- **Oposiciones y empleo público**: requisito habitual para acceder a
  la función pública.
- **Adopción**: nacional e internacional.
- **Nacionalidad española**: es documento obligatorio en el expediente.
- **Visados y viajes**: algunos países lo exigen para visados de
  residencia o trabajo (EE.UU., Canadá, Australia, etc.).
- **Residencia en el extranjero**: consulados y embajadas lo piden.
- **Licencias y permisos**: armas, explosivos, etc.
- **Trámites de extranjería**: renovación de permisos, arraigo, etc.

---

## 2. Cómo solicitar el certificado

### Online (sede electrónica del Ministerio de Justicia)

La forma más rápida. El certificado se obtiene al momento en formato
PDF firmado electrónicamente.

**URL**: `https://sede.mjusticia.gob.es/es/tramites/certificado-antecedentes`

**Requisitos**:
- Certificado digital, Cl@ve permanente o DNI electrónico.
- Ser mayor de edad o representante legal de un menor.

**Pasos**:
1. Acceder a la sede electrónica del Ministerio de Justicia.
2. Seleccionar "Certificado de Antecedentes Penales".
3. Identificarse con certificado digital o Cl@ve.
4. Rellenar el formulario (datos personales, finalidad).
5. Descargar el certificado en PDF (inmediato).

**Coste**: gratuito.

### Presencialmente

Se puede solicitar en:
- **Oficinas de atención al ciudadano del Ministerio de Justicia**
  (Madrid: C/ de la Bolsa, 8).
- **Gerencias Territoriales del Ministerio de Justicia** en cada
  comunidad autónoma.
- **Oficinas de registro** de cualquier administración pública
  (ventanilla única).

**Documentación**:
- DNI, NIE o pasaporte en vigor.
- Formulario de solicitud (disponible en las oficinas o descargable).

**Plazo**: 3-5 días hábiles. Se recoge en la misma oficina o se envía
por correo.

**Coste**: gratuito.

### Por correo postal

Se puede enviar la solicitud por correo ordinario a:
Registro Central de Penados y Rebeldes
Ministerio de Justicia
C/ de la Bolsa, 8
28012 Madrid

Adjuntar fotocopia compulsada del DNI/NIE y formulario cumplimentado.
El certificado se devuelve por correo. Plazo: 10-15 días.

---

## 3. Certificado de delitos de naturaleza sexual

Desde 2015 (Ley Orgánica 1/1996, modificada por la LO 8/2015), toda
persona que trabaje o vaya a trabajar en **actividades que impliquen
contacto habitual con menores** debe acreditar no tener antecedentes
por delitos sexuales.

### Quién debe solicitarlo

- Profesores, monitores, entrenadores deportivos.
- Personal de centros de menores, campamentos, ludotecas.
- Cuidadores, au pairs, personal doméstico que atienda menores.
- Voluntarios en actividades con menores.
- Cualquier profesional que trabaje habitualmente con menores.

### Cómo solicitarlo

Se solicita **en el mismo trámite** que el certificado de antecedentes
penales general, pero marcando la casilla correspondiente.

**Online**: en la sede electrónica, al solicitar el certificado de
antecedentes penales se puede marcar "Certificado de Delitos de
Naturaleza Sexual". Se obtiene un único documento que incluye ambos.

**URL**: `https://sede.mjusticia.gob.es/es/tramites/certificado-antecedentes`

### Qué refleja

El certificado indica si la persona tiene o no inscripciones en el
**Registro Central de Delincuentes Sexuales** por:
- Delitos contra la libertad e indemnidad sexual.
- Trata de seres humanos con fines de explotación sexual.

### Validez

No hay un plazo de validez establecido legalmente, pero la mayoría de
entidades lo aceptan con una antigüedad máxima de **3 meses**.

---

## 4. Cancelación de antecedentes penales

Los antecedentes penales **no son permanentes**. Se pueden cancelar
cuando se cumplen ciertos requisitos (art. 136 del Código Penal):

### Requisitos para la cancelación

1. **Haber cumplido o extinguido la pena** (incluidas responsabilidades
   civiles, salvo insolvencia declarada).
2. **Haber transcurrido un plazo** sin delinquir de nuevo:

| Pena impuesta | Plazo de cancelación |
|---|---|
| Penas leves | 6 meses |
| Penas que no excedan de 12 meses y por delito imprudente | 2 años |
| Resto de penas menos graves | 3 años |
| Penas graves | 5 años |

3. **No haber delinquido de nuevo** durante ese plazo.

### Cómo solicitar la cancelación

- **Automática**: el Ministerio de Justicia cancela de oficio si se
  cumplen los requisitos. En la práctica puede tardar.
- **A instancia de parte**: el interesado puede solicitar la
  cancelación en la sede electrónica o presencialmente.

URL: `https://sede.mjusticia.gob.es/es/tramites/cancelacion-antecedentes`

---

## 5. Antecedentes penales de extranjeros

### Extranjeros residentes en España

Pueden solicitar el certificado de antecedentes penales español de la
misma forma que los ciudadanos españoles (online o presencialmente).

### Antecedentes penales del país de origen

Para ciertos trámites (nacionalidad, adopción internacional), además
del certificado español, se pide el certificado de antecedentes del
**país de origen**. Este se solicita en el consulado o embajada del
país correspondiente y generalmente debe estar:
- **Apostillado** (si el país es firmante del Convenio de La Haya) o
  **legalizado** (si no lo es).
- **Traducido** por traductor jurado si no está en español.

Para información sobre apostilla y legalización, consulta las skills
**apostilla** y **legalizacion-documentos**.

---

## 6. Datos prácticos

| Aspecto | Detalle |
|---|---|
| **Organismo** | Ministerio de Justicia — Registro Central de Penados |
| **Coste** | Gratuito |
| **Validez del certificado** | Sin plazo legal; la entidad receptora suele exigir máximo 3 meses |
| **Plazo online** | Inmediato (PDF firmado) |
| **Plazo presencial** | 3-5 días hábiles |
| **Identificación online** | Certificado digital, Cl@ve permanente o DNIe |
| **Sede electrónica** | `https://sede.mjusticia.gob.es/es/tramites/certificado-antecedentes` |

---

## Cuándo NO usar esta skill

- Si pregunta por **apostilla o legalización** de un certificado de
  penales extranjero → **apostilla** o **legalizacion-documentos**.
- Si pregunta sobre **nacionalidad española** (proceso completo) →
  **extranjeria-nacionalidad**.
- Si necesita **cita previa** en algún organismo → **cita-previa**.
- Si pregunta por **oposiciones o empleo público** (no solo el
  certificado) → skill correspondiente de educación o empleo.
- Si pregunta por el **texto del Código Penal** → **boe**.
