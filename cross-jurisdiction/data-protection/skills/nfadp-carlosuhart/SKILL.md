---
name: nfadp-carlosuhart
title: nFADP / revDSG — Auditoría de Cumplimiento (Suiza)
description: Audita un sitio web frente a la nueva Ley Federal de Protección de Datos Personales de Suiza (nFADP / revDSG — en vigor desde el 1 de septiembre de 2023). Detecta el sector automáticamente. Produce informe de cumplimiento con score, tabla de estado por artículo e issues priorizados con cuantificación de sanciones en CHF. Sub-skill del orquestador /privacidad — también invocable directamente.
author: carlosuhart
author_url: https://github.com/carlosuhart/seo-audit-skills/tree/main/skills/nfadp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# nFADP / revDSG — Auditoría de Cumplimiento (Suiza)

## Uso

```
/nfadp https://ejemplo.ch
/nfadp https://ejemplo.ch --docx
```

---

## Marco normativo

- **nFADP** (new Federal Act on Data Protection): Bundesgesetz über den Datenschutz
  (DSG) en alemán · Loi fédérale sur la protection des données (LPD) en francés ·
  Legge federale sulla protezione dei dati (LPD) en italiano.
  En vigor desde el **1 de septiembre de 2023**. Reemplaza la ley anterior de 1992.
- **Ordenanza sobre la Protección de Datos (OPDa)**: reglamento de desarrollo,
  también en vigor desde el 1 de septiembre de 2023.
- **FDPIC** (Federal Data Protection and Information Commissioner):
  Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter (EDÖB) en alemán ·
  Préposé fédéral à la protection des données et à la transparence (PFPDT) en francés.
  Web: edoeb.admin.ch

Suiza **no es** miembro de la UE ni del EEE. La nFADP es derecho suizo independiente,
aunque está fuertemente inspirada en el RGPD. La UE tiene decisión de adecuación
para Suiza (flujo UE → Suiza permitido). Suiza considera adecuados los países de la
UE/EEE y otros listados por el FDPIC.

⚠️ **Diferencia crítica respecto al RGPD:** Las sanciones de la nFADP son **penales**
y recaen sobre las **personas físicas** responsables (no sobre la empresa).
El máximo es **CHF 250.000** por persona física infractora. No existe multa
administrativa directa a la empresa equivalente al Art. 83 RGPD.

---

## Paso 0 — Stack tecnológico

Si este skill es invocado desde el orquestador `/privacidad`, usar el Paso 0
compartido. Si se invoca directamente, ejecutar el Paso 0 del skill `rgpd`.

Señales adicionales específicas de Suiza:
- TLD `.ch`
- CHF (Fr. / CHF) como moneda
- MWST / TVA / IVA (IVA suizo) en precios
- Referencias al FDPIC / EDÖB / PFPDT
- Cantones suizos mencionados en el contenido o domicilio
- Número de UID (Unternehmens-Identifikationsnummer) en el pie de página

---

## Paso 1 — Recopilación de datos del sitio

Igual al skill `rgpd` Paso 1. Rutas comunes en Suiza:
- DE: `/datenschutz`, `/datenschutzerklarung`
- FR: `/protection-des-donnees`, `/confidentialite`
- IT: `/protezione-dei-dati`
- EN: `/privacy`, `/privacy-policy`

---

## Paso 2 — Detección de sector

Usar la matriz del skill `rgpd`. Señales adicionales suizas:

| Sector | Señales Suiza |
|--------|--------------|
| **Financiero** | FINMA, "banco suizo", "gestión patrimonial", CHF |
| **Farmacéutico** | Swissmedic, "Zulassung", "autorisation" |
| **Salud** | "Krankenkasse", LAMAL, "assurance maladie", "assicurazione malattie" |
| **Seguros** | FINMA, "Versicherung", "assurance" |

---

## Paso 3 — Auditoría por bloques

Evaluar: **Cumple / Parcial / No cumple / No evaluable**

### Bloque 1 — Identificación del responsable (Art. 19 nFADP)
Peso: 10 pts

La nFADP protege únicamente datos de **personas físicas** (Art. 2). Las personas
jurídicas están excluidas del ámbito de protección.

Verificar en la declaración de protección de datos (Datenschutzerklärung):
- [ ] Nombre o razón social del responsable del tratamiento
- [ ] Domicilio o sede del responsable
- [ ] Datos de contacto (email o formulario) para ejercicio de derechos
- [ ] UID (número de identificación de empresa) — no obligatorio pero habitual en Suiza
- [ ] Si el responsable no tiene domicilio en Suiza pero trata datos de titulares en Suiza
      (Art. 3 nFADP): ¿designa un representante en Suiza?

### Bloque 2 — Declaración de protección de datos: existencia y acceso (Art. 19 nFADP)
Peso: 5 pts

La nFADP obliga a informar al titular cuando se recogen datos (Art. 19):
- [ ] Existe declaración de protección de datos publicada
- [ ] Enlace visible en el footer de todas las páginas
- [ ] Enlace accesible desde formularios que recogen datos
- [ ] Redactada en el idioma principal del sitio (DE / FR / IT / EN)
- [ ] Fecha de última actualización visible

### Bloque 3 — Declaración de protección de datos: contenido mínimo (Art. 19 nFADP)
Peso: 15 pts

El Art. 19 establece la obligación de informar sobre (1 pt por ítem):

- [ ] **Art. 19.2(a):** Identidad y datos de contacto del responsable
- [ ] **Art. 19.2(b):** Finalidad del tratamiento
- [ ] **Art. 19.2(c):** Destinatarios o categorías de destinatarios si se comunican datos
- [ ] **Art. 19.2(d):** País de destino en transferencias internacionales (si aplica)
- [ ] **Art. 19.2(e):** Existencia de decisiones individuales automatizadas (si aplica)
      y la lógica utilizada (Art. 21)
- [ ] **Art. 19.3:** Si los datos no se recogen directamente del titular: también la
      fuente de los datos
- [ ] Categorías de datos tratados
- [ ] Períodos de conservación o criterios para determinarlos
- [ ] Derechos del titular: acceso, rectificación, eliminación, portabilidad,
      oposición a decisiones automatizadas
- [ ] Procedimiento para ejercer derechos y plazo de respuesta (30 días — Art. 25)
- [ ] Uso de cookies y tecnologías de rastreo
- [ ] Derecho a reclamar ante el **FDPIC**
- [ ] Si se realizan transferencias internacionales: países y garantías adoptadas
- [ ] Si existe asesor de protección de datos (Art. 10): datos de contacto
- [ ] Información sobre tratamiento de datos de menores si aplica

### Bloque 4 — Principios de tratamiento y licitud (Art. 6 nFADP)
Peso: 10 pts

La nFADP no exige una "base jurídica" explícita para cada tratamiento de la misma
forma que el RGPD. El tratamiento es lícito si respeta los principios del Art. 6
y no viola las prohibiciones de los Arts. 30-31 (datos sensibles):

**Principios del Art. 6:**
- [ ] **Licitud**: el tratamiento respeta el derecho y la buena fe
- [ ] **Proporcionalidad**: los datos tratados son adecuados y necesarios para la finalidad
- [ ] **Finalidad**: los datos se recogen para una finalidad determinada y reconocible;
      no se tratan posteriormente de forma incompatible (Art. 6.3)
- [ ] **Exactitud**: los datos son exactos y actualizados (Art. 6.5)
- [ ] **Seguridad**: medidas técnicas y organizativas apropiadas (Art. 8)

**Justificación del tratamiento de datos sensibles (Art. 31) si aplica:**
- [ ] Consentimiento del titular
- [ ] Obligación legal o necesidad de derechos legales
- [ ] Interés preponderante público o privado
- [ ] Datos publicados voluntariamente por el titular

**Privacidad por diseño y por defecto (Art. 7 nFADP):**
- [ ] El sistema / formulario recoge solo los datos necesarios para la finalidad
- [ ] La configuración de privacidad más protectora está activada por defecto
- [ ] Las opciones de suscripción a comunicaciones no están preseleccionadas

### Bloque 5 — Cookies, consentimiento y perfilado (Art. 6 + Art. 21 + DSG-Praxis)
Peso: 15 pts

La nFADP no regula cookies específicamente. El FDPIC ha indicado que las cookies
de rastreo no esenciales requieren consentimiento informado conforme al Art. 6.
La práctica suiza (DSG-Praxis) se alinea en este punto con el RGPD.

**Perfilado (Art. 5(f)) y perfilado de alto riesgo (Art. 5(g)):**
- **Perfilado**: cualquier tratamiento automatizado de datos para evaluar aspectos
  personales (comportamiento, preferencias, rendimiento, situación económica, etc.)
- **Perfilado de alto riesgo**: perfilado que conduce a combinar datos para evaluar
  aspectos esenciales de la personalidad → requiere consentimiento expreso o
  una de las justificaciones del Art. 31

**Banner de cookies:**
- [ ] Existe banner o CMP
- [ ] El banner bloquea cookies no esenciales hasta obtener consentimiento
- [ ] No hay cookies de análisis, publicidad o rastreo activas antes del consentimiento
- [ ] Opción de rechazo tan accesible como la aceptación
- [ ] Configuración granular por categoría
- [ ] El consentimiento es revocable fácilmente

**Formularios:**
- [ ] Checkbox de consentimiento no pre-marcado cuando aplica
- [ ] Finalidad concreta declarada antes de enviar

**Perfilado:**
- [ ] Si el sitio realiza perfilado: declarado en la Datenschutzerklärung (Art. 19.2(e))
- [ ] Si es perfilado de alto riesgo: consentimiento expreso o justificación Art. 31

**Marketing directo:**
- [ ] Existe mecanismo de baja de comunicaciones comerciales
- [ ] La declaración menciona el derecho de oposición al tratamiento para marketing

### Bloque 6 — Derechos del titular (Art. 25–32 nFADP)
Peso: 15 pts

La nFADP reconoce los siguientes derechos, con plazo de respuesta de **30 días**
(Art. 25.5), prorrogable hasta 3 meses con notificación:

1. **Derecho de acceso** (Art. 25): información sobre si se tratan sus datos y,
   en caso afirmativo, qué datos, con qué finalidad, conservación, destinatarios y
   origen; si hay decisiones automatizadas y la lógica empleada
2. **Derecho a la exactitud / rectificación** (Art. 32): corrección de datos inexactos
3. **Derecho de supresión** (Art. 32): eliminación de datos cuyo tratamiento sea
   contrario a los principios de la nFADP
4. **Derecho a la portabilidad** (Art. 28): recibir los datos en formato estructurado
   y de uso común; aplica cuando el tratamiento es automatizado y se basa en
   consentimiento o contrato
5. **Derecho a oponerse a decisiones individuales automatizadas** (Art. 21):
   incluido el perfilado de alto riesgo; el responsable debe comunicar la decisión
   y el titular puede solicitar revisión por persona física

Nota: la nFADP tiene menos derechos que el RGPD — no existe derecho explícito a
la limitación del tratamiento ni al olvido como tal (aunque la supresión cubre
parte de esta función).

Verificar:
- [ ] Existe mecanismo para ejercer derechos (email, formulario)
- [ ] Se menciona el plazo de **30 días** (prorrogable a 3 meses)
- [ ] Se mencionan los derechos: acceso, rectificación, supresión, portabilidad,
      oposición a decisiones automatizadas
- [ ] Se indica qué información debe adjuntar el titular (identificación)
- [ ] Se menciona el derecho a reclamar ante el **FDPIC** (edoeb.admin.ch)

### Bloque 7 — Datos sensibles y perfilado de alto riesgo (Art. 5(c) + Art. 22 nFADP)
Peso: 10 pts

**Datos sensibles (Art. 5(c)):**
- Opiniones o actividades religiosas, ideológicas, políticas o sindicales
- Datos de salud, esfera íntima u origen racial o étnico
- Datos genéticos
- Datos biométricos que identifiquen de forma unívoca a una persona física
- Datos sobre procedimientos y sanciones administrativos o penales
- Datos sobre medidas de asistencia social

Nota: lista similar al RGPD pero incluye datos sobre medidas de asistencia social
y procedimientos penales de forma explícita.

**Si el sitio no recoge datos sensibles ni realiza perfilado de alto riesgo:**
bloque N/A — asignar 10 pts.

**Si recoge datos sensibles o realiza perfilado de alto riesgo:**
- [ ] Identificados explícitamente en la declaración
- [ ] Consentimiento expreso del titular u otra justificación Art. 31
- [ ] Finalidad específica declarada
- [ ] Medidas de seguridad reforzadas mencionadas

**Evaluación de impacto sobre la protección de datos (EIPD — Art. 22 nFADP):**
Obligatoria cuando el tratamiento conlleva alto riesgo para la personalidad
o los derechos fundamentales del titular. Criterios: datos sensibles a gran
escala, perfilado de alto riesgo, monitorización sistemática de zonas públicas.
- [ ] Si aplica: ¿la declaración menciona la realización de EIPD?
- [ ] Si la EIPD revela riesgo residual elevado: ¿se consultó al FDPIC (Art. 23)?

### Bloque 8 — Transferencias internacionales (Art. 16–18 nFADP)
Peso: 10 pts

La nFADP permite transferencias a países con nivel de protección adecuado
reconocido por el Consejo Federal suizo (Art. 16). El FDPIC publica y mantiene
la lista. Países incluidos: todos los estados de la UE/EEE + varios más
(ver edoeb.admin.ch para la lista actualizada).

**Para transferencias a países sin nivel adecuado (Art. 16.2 + Art. 17):**
- Cláusulas contractuales tipo aprobadas por el FDPIC (o equivalentes)
- Normas corporativas vinculantes (BCR)
- Garantías específicas reconocidas (certificaciones, códigos de conducta)
- Consentimiento expreso del titular para la transferencia
- Necesidad para ejecutar un contrato con el titular

**EE.UU.:** Suiza tiene el Swiss-US Data Privacy Framework (DPF) en vigor.
Las organizaciones de EE.UU. certificadas bajo el DPF + extensión suiza
tienen nivel adecuado para transferencias desde Suiza.

Verificar:
- [ ] La declaración informa sobre transferencias internacionales (Art. 19.2(d))
- [ ] Se identifican los países o regiones de destino
- [ ] Se indica la garantía adoptada (adecuación suiza, DPF, SCCs suizas)
- [ ] Si hay trackers de EE.UU. activos: ¿se menciona el Swiss-US DPF o SCCs?

### Bloque 9 — Seguridad y notificación de brechas (Art. 8 + Art. 24 nFADP)
Peso: 5 pts

La nFADP exige medidas técnicas y organizativas apropiadas para garantizar la
seguridad de los datos según el riesgo (Art. 8).

- [ ] HTTPS activo en todas las páginas
- [ ] Certificado SSL/TLS válido y no expirado
- [ ] HSTS habilitado
- [ ] La declaración menciona que se adoptan medidas de seguridad

**Notificación de brechas (Art. 24 nFADP):**
Cuando una violación de seguridad probablemente conlleve un alto riesgo para
la personalidad o los derechos fundamentales del titular, el responsable debe
notificar al **FDPIC "lo antes posible"** (no existe el plazo de 72h del RGPD).
También debe notificar al titular si es necesario para su protección.
- [ ] La declaración menciona el procedimiento ante vulneraciones de seguridad

### Bloque 10 — Asesor de protección de datos y EIPD (Art. 10 + Art. 22–23 nFADP)
Peso: 5 pts

**Asesor de protección de datos (Datenschutzberater — Art. 10):**
Es **voluntario** para empresas privadas (a diferencia del DPD del RGPD que es
obligatorio en ciertos casos). Su designación puede ser considerada por el FDPIC
como señal de cumplimiento proactivo y relevante para la valoración de sanciones.

- [ ] ¿La declaración menciona la existencia de un asesor de protección de datos?
- [ ] Si existe: datos de contacto publicados
- [ ] Si no existe: es una mejora recomendada, no un issue (no obligatorio)

**Para organizaciones con tratamientos de alto riesgo:**
Si el responsable realiza EIPD (Art. 22) y esta revela riesgo residual elevado,
debe consultar al FDPIC previamente (Art. 23 — consulta previa).

---

## Paso 4 — Score global

```
Score = suma de puntos obtenidos / 100
```

| Rango | Interpretación |
|-------|---------------|
| 80–100 | Postura defensible |
| 60–79 | Riesgo moderado |
| 40–59 | Riesgo alto |
| 0–39 | Riesgo crítico |

---

## Paso 5 — Clasificación de issues y sanciones (Art. 60–66 nFADP)

⚠️ Las sanciones de la nFADP son **penales** y recaen sobre **personas físicas**
(directivos, responsables de protección de datos, empleados infractores) — no
directamente sobre la empresa. Multa penal de hasta **CHF 250.000** por persona
física. La empresa puede responder subsidiariamente si la investigación de la
persona responsable sería desproporcionada (Art. 64).

| Conducta sancionable | Máximo |
|---|---|
| Incumplir el deber de informar (Art. 19), no atender derechos del titular (Art. 25-32), no cumplir requisitos de transferencia internacional (Art. 16-17) | CHF 250.000 |
| Incumplir disposiciones de la OPDa sobre seguridad o EIPD | CHF 250.000 |

**Críticos:**
- Sin declaración de protección de datos → Art. 19
- Datos sensibles tratados sin justificación → Art. 31
- Sin mecanismo de ejercicio de derechos → Art. 25-32
- Transferencias internacionales a países sin adecuación sin garantías → Art. 16-17
- Sin HTTPS → Art. 8

**Medios:**
- Declaración existe pero falta contenido mínimo Art. 19
- Derechos mencionados sin canal ni plazo (30 días)
- Perfilado de alto riesgo no declarado → Art. 19.2(e) + Art. 21
- EIPD probable pero no mencionada → Art. 22
- Cookies no esenciales sin consentimiento previo

**Bajos:**
- Falta fecha de actualización
- Asesor de protección de datos no mencionado
- Headers de seguridad recomendados ausentes

---

## Paso 6 — Output según modo

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_nfadp_[fecha].md` o `.docx`.

Modo `--docx`: misma estructura que `rgpd`, adaptada:
- Autoridad: FDPIC (edoeb.admin.ch)
- Sanciones: multa penal CHF 250.000 contra persona física
- Idioma: adaptar terminología al idioma principal del sitio (DE/FR/IT/EN)
- Pie de página: hipervínculo "Zythos Media" → https://zythos.media

---

## Actualización normativa

- **nFADP**: en vigor desde el 1 de septiembre de 2023.
- **OPDa** (Ordenanza): en vigor desde el 1 de septiembre de 2023.
- **Swiss-US DPF**: operativo. Verificar estado en edoeb.admin.ch.
- **Lista de países con adecuación**: mantiene el FDPIC en edoeb.admin.ch.
- **Versión de esta skill:** 1.0.0 (2026-07-08).
