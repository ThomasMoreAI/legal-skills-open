---
name: proteccion-datos-jaimebs2
title: Protección de Datos Personales — AEPD y RGPD
description: 'Use when the user asks about data protection in Spain: AEPD (Agencia Española de Protección de Datos), GDPR/RGPD, ARCO rights (access, rectification, erasure, objection, portability, restriction), how to file a complaint, obligations for businesses and self-employed, DPO, or the AEPD''s priority channel for urgent content removal. Triggers on: ''protección de datos'', ''AEPD'', ''RGPD'', ''GDPR'', ''LOPD'', ''LOPDGDD'', ''derechos ARCO'', ''derecho al olvido'', ''derecho de acceso'', ''derecho de rectificación'', ''derecho de supresión'', ''derecho de oposición'', ''portabilidad datos'', ''reclamación AEPD'', ''delegado protección datos'', ''DPO'', ''consentimiento datos'', ''política de privacidad'', ''tratamiento datos personales'', ''canal prioritario AEPD'', ''Facilita RGPD'', ''borrar mis datos''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/justicia/proteccion-datos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# Protección de Datos Personales — AEPD y RGPD

Guía completa sobre protección de datos en España: la AEPD, derechos
del ciudadano (acceso, rectificación, supresión, oposición,
portabilidad, limitación), cómo ejercerlos, reclamaciones, y
obligaciones de empresas y autónomos.

> Esta skill orienta sobre el marco general de la protección de datos.
> **No sustituye asesoramiento jurídico profesional ni tramita
> reclamaciones.**

---

## 1. Marco normativo

La protección de datos personales en España se rige por dos normas
principales:

### RGPD — Reglamento General de Protección de Datos (UE 2016/679)

- Norma europea de **aplicación directa** en España desde mayo de 2018.
- Establece los principios, derechos y obligaciones fundamentales.
- Aplica a toda organización que trate datos de personas en la UE.

### LOPDGDD — Ley Orgánica 3/2018

- **Complementa y desarrolla** el RGPD para España.
- Regula aspectos específicos: datos de fallecidos, menores (a partir de
  14 años pueden consentir), videovigilancia, exclusión publicitaria,
  etc.
- Incluye los **derechos digitales** (desconexión digital laboral,
  derecho a la intimidad en dispositivos digitales, testamento digital).

URL: `https://www.aepd.es`

---

## 2. La AEPD: Agencia Española de Protección de Datos

### Qué es

La AEPD es la **autoridad independiente** de control que vela por el
cumplimiento de la normativa de protección de datos en España.

### Qué hace

- **Atiende reclamaciones** de ciudadanos.
- **Investiga** posibles infracciones.
- **Sanciona** a empresas y organismos que incumplan (multas de hasta
  20 millones de euros o el 4 % de la facturación global).
- **Publica guías y herramientas** para facilitar el cumplimiento.
- **Promociona** la educación en privacidad.

### Canal prioritario

La AEPD tiene un **canal prioritario** para solicitar la retirada
urgente de contenido en internet que afecte gravemente a los derechos
de una persona:

- **Contenido sexual o violento** difundido sin consentimiento.
- **Acoso** en redes sociales.
- Especialmente orientado a menores y víctimas de violencia de género.

URL del canal prioritario: `https://www.aepd.es/canalprioritario`

---

## 3. Derechos del ciudadano

El RGPD reconoce a toda persona una serie de derechos sobre sus datos
personales. Se conocen coloquialmente como **derechos ARCO-POL**
(por sus iniciales):

### Derecho de acceso

- **Qué es**: saber si una organización trata tus datos y, en caso
  afirmativo, obtener una copia de ellos.
- **Información que debes recibir**: qué datos tienen, para qué los
  usan, a quién los ceden, cuánto tiempo los conservan.
- **Plazo**: la organización debe responder en **1 mes** (ampliable a
  3 meses si es complejo).

### Derecho de rectificación

- **Qué es**: corregir datos inexactos o completar datos incompletos.
- **Plazo**: 1 mes.

### Derecho de supresión ("derecho al olvido")

- **Qué es**: solicitar que borren tus datos personales.
- **Procede cuando**:
  - Los datos ya no son necesarios para la finalidad original.
  - Retiras el consentimiento.
  - Te opones al tratamiento y no hay motivos legítimos.
  - Los datos se trataron ilícitamente.
- **No procede** si los datos son necesarios por obligación legal
  (facturas, contratos), libertad de expresión o interés público.
- **Derecho al olvido en buscadores**: puedes pedir a Google, Bing,
  etc., que desindexen resultados que contengan tus datos y sean
  obsoletos o irrelevantes.

### Derecho de oposición

- **Qué es**: oponerte a que traten tus datos para una finalidad
  concreta.
- **Marketing**: tienes un derecho **absoluto** a oponerte al uso de
  tus datos para marketing directo (sin necesidad de justificación).
- Para otros tratamientos, la organización puede seguir tratando los
  datos si acredita motivos legítimos.

### Derecho a la portabilidad

- **Qué es**: recibir tus datos en un formato **estructurado, de uso
  común y lectura mecánica** (JSON, CSV...) y transmitirlos a otro
  responsable.
- Solo aplica a datos tratados con consentimiento o por contrato, y
  por medios automatizados.

### Derecho a la limitación del tratamiento

- **Qué es**: solicitar que los datos no se traten temporalmente
  (se "congelan") mientras se verifica su exactitud, se resuelve una
  reclamación o se ejerce un derecho.

---

## 4. Cómo ejercer tus derechos

### Paso 1 — Dirigirse al responsable del tratamiento

1. **Identificar** quién trata tus datos (la empresa, organismo o
   persona responsable).
2. **Enviar una solicitud** por escrito (email, formulario web, correo
   postal) indicando:
   - Nombre, apellidos, DNI/NIE.
   - Qué derecho ejerces.
   - Dirección para notificaciones.
   - Documentación acreditativa si es necesario.
3. El responsable debe responder en **1 mes** (ampliable a 3 si hay
   complejidad).
4. **Gratuito** (salvo solicitudes repetitivas o infundadas).

### Paso 2 — Reclamar ante la AEPD (si no te atienden)

Si el responsable no responde en plazo, deniega injustificadamente tu
solicitud o la respuesta es insatisfactoria:

1. Acceder a la **sede electrónica de la AEPD**:
   `https://sedeagpd.gob.es`
2. Presentar una **reclamación** (con certificado digital, Cl@ve o
   DNIe).
3. Adjuntar:
   - Copia de la solicitud al responsable.
   - Prueba de que se envió (acuse de recibo, email, etc.).
   - Respuesta recibida (si la hay).
4. La AEPD investigará y, si procede, requerirá al responsable o
   iniciará procedimiento sancionador.
5. **Gratuito** (no hay tasas para reclamar ante la AEPD).

---

## 5. Obligaciones de empresas y autónomos

Toda empresa o autónomo que trate datos personales debe cumplir con
el RGPD y la LOPDGDD:

### Principios fundamentales

- **Licitud**: base jurídica para tratar datos (consentimiento,
  contrato, obligación legal, interés legítimo, etc.).
- **Finalidad**: tratar datos solo para fines determinados y explícitos.
- **Minimización**: recoger solo los datos estrictamente necesarios.
- **Exactitud**: mantener los datos actualizados.
- **Limitación del plazo**: no conservar datos más tiempo del necesario.
- **Integridad y confidencialidad**: medidas de seguridad adecuadas.

### Registro de actividades de tratamiento

- Obligatorio para empresas con más de 250 empleados o que traten
  datos de riesgo.
- Recomendable para todos.
- Documento interno que describe qué datos se tratan, para qué, quién
  accede, plazos de conservación, etc.

### Consentimiento

- Debe ser **libre, específico, informado e inequívoco**.
- Para datos sensibles (salud, religión, orientación sexual): debe ser
  **explícito**.
- No vale el consentimiento tácito ni las casillas premarcadas.
- El responsable debe poder **demostrar** que obtuvo el consentimiento.

### Delegado de Protección de Datos (DPO)

Es obligatorio nombrar un DPO cuando:
- El responsable es una **autoridad u organismo público**.
- Se realizan tratamientos de **observación habitual y sistemática a
  gran escala** (videovigilancia masiva, tracking online).
- Se tratan a gran escala datos de **categorías especiales** (salud,
  biométricos, etc.).

En España, la LOPDGDD amplía los supuestos: colegios profesionales,
centros educativos, aseguradoras, entidades financieras, empresas de
seguridad privada, etc.

### Evaluación de impacto (EIPD)

Obligatoria cuando el tratamiento entrañe un **alto riesgo** para los
derechos de las personas:
- Perfilado automatizado con efectos jurídicos.
- Tratamiento a gran escala de datos sensibles.
- Videovigilancia a gran escala.

### Notificación de brechas de seguridad

- Si hay una **violación de seguridad** que afecte a datos personales,
  el responsable debe notificarla a la AEPD en un plazo máximo de
  **72 horas**.
- Si hay alto riesgo para los afectados, también debe comunicarlo a
  los propios interesados.

---

## 6. Herramientas de la AEPD

La AEPD ofrece herramientas gratuitas para facilitar el cumplimiento:

### Facilita RGPD

- Para **empresas que tratan datos de bajo riesgo** (clientes,
  proveedores, empleados, datos de contacto).
- Genera la documentación mínima necesaria (cláusulas, registro,
  políticas) respondiendo un cuestionario online.
- URL: `https://www.aepd.es/guias-y-herramientas/herramientas/facilita-rgpd`

### Facilita Emprende

- Para **emprendedores y nuevas empresas**.
- Orientación paso a paso sobre qué obligaciones de protección de datos
  aplican según el tipo de negocio.

### Otras herramientas

- **GESTIONA-EIPD**: para realizar evaluaciones de impacto.
- **COMUNICA-Brecha RGPD**: para valorar si una brecha de seguridad
  debe comunicarse a los afectados.
- **Guías sectoriales**: sanidad, educación, videovigilancia, comunidades
  de propietarios, etc.

---

## 7. Sanciones

Las infracciones del RGPD se clasifican en:

| Tipo | Multa máxima | Ejemplos |
|---|---|---|
| Leves | Apercibimiento | No atender un derecho en plazo |
| Graves | Hasta 10 M€ o 2 % facturación global | No tener registro de actividades, no nombrar DPO cuando es obligatorio |
| Muy graves | Hasta 20 M€ o 4 % facturación global | Tratar datos sin base jurídica, vulnerar derechos de forma sistemática |

Las administraciones públicas no reciben multas económicas, sino
apercibimientos y medidas correctoras.

---

## 8. Resumen rápido

```
DERECHOS DEL CIUDADANO (ARCO-POL):
  ├── Acceso → saber qué datos tienen sobre ti
  ├── Rectificación → corregir datos incorrectos
  ├── Supresión → borrar tus datos ("derecho al olvido")
  ├── Oposición → que no usen tus datos (absoluto para marketing)
  ├── Portabilidad → recibir tus datos en formato reutilizable
  └── Limitación → congelar el tratamiento temporalmente

CÓMO EJERCERLOS:
  1. Solicitud al responsable del tratamiento (1 mes para responder)
  2. Si no responden → reclamación ante la AEPD (gratuita)

OBLIGACIONES EMPRESAS/AUTÓNOMOS:
  ├── Base jurídica para tratar datos
  ├── Registro de actividades de tratamiento
  ├── Consentimiento libre, específico, informado
  ├── DPO (si es obligatorio)
  ├── Evaluación de impacto (tratamientos de alto riesgo)
  └── Notificar brechas en 72 horas

HERRAMIENTAS AEPD:
  ├── Facilita RGPD → documentación básica automatizada
  ├── Facilita Emprende → para nuevos negocios
  └── Canal prioritario → retirada urgente de contenido
```

---

## Cuándo NO usar esta skill

- Si pregunta por **obligaciones fiscales de autónomos** (IVA, IRPF,
  modelos trimestrales) → **fiscalidad-autonomos**.
- Si pregunta por **cómo crear una empresa** (alta, formas jurídicas)
  → **emprendimiento-crear-empresa**.
- Si pregunta por el **texto del RGPD o la LOPDGDD** → **boe**.
- Si pregunta por **certificados del Registro Civil** → **registro-civil**.
- Si pregunta por **justicia gratuita** → **justicia-gratuita**.
- Si pregunta por **trámites de extranjería** → **extranjeria-nacionalidad**.
