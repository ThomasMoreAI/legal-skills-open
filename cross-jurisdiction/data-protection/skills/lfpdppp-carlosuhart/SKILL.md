---
name: lfpdppp-carlosuhart
title: LFPDPPP — Auditoría de Cumplimiento (México)
description: Audita un sitio web frente a la Ley Federal de Protección de Datos Personales en Posesión de los Particulares (LFPDPPP — México, 2010) y su Reglamento. Detecta el sector automáticamente. Produce informe de cumplimiento con score, tabla de estado por artículo e issues priorizados con cuantificación de sanciones. Sub-skill del orquestador /privacidad — también invocable directamente.
author: carlosuhart
author_url: https://github.com/carlosuhart/seo-audit-skills/tree/main/skills/lfpdppp
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: es
---

# LFPDPPP — Auditoría de Cumplimiento (México)

## Uso

```
/lfpdppp https://ejemplo.com.mx
/lfpdppp https://ejemplo.com.mx --docx
```

Sin `--docx` el output es Markdown interno. Con `--docx` genera informe
ejecutivo en formato Word.

---

## Marco normativo

- **LFPDPPP**: Ley Federal de Protección de Datos Personales en Posesión de los
  Particulares. Publicada en DOF el 5 de julio de 2010. En vigor desde 2010.
  Solo aplica a **particulares** (personas físicas y morales del sector privado).
  El sector público se rige por la Ley General de Protección de Datos Personales
  en Posesión de Sujetos Obligados (LGPDPPSO, 2017) — fuera del scope de esta skill.
- **Reglamento LFPDPPP**: publicado en DOF el 21 de diciembre de 2011.
- **Lineamientos del Aviso de Privacidad**: publicados en DOF el 17 de enero de 2013.
- **INAI** (Instituto Nacional de Transparencia, Acceso a la Información y Protección
  de Datos Personales): autoridad de control. Web: inai.org.mx
- **Ámbito (Art. 2)**: aplica a personas físicas y morales de carácter privado que
  lleven a cabo el tratamiento de datos personales, con operaciones en México o
  dirigidas a titulares en México.

---

## Nota sobre el aviso de privacidad

En México, el documento de cumplimiento principal se denomina **aviso de privacidad**
(no "política de privacidad"). Existen tres tipos según el Reglamento y los Lineamientos:

| Tipo | Cuándo usar | Contenido |
|------|-------------|-----------|
| **Integral** | Recabación directa, suficiente espacio | Todos los elementos del Art. 16 |
| **Simplificado** | Recabación en formularios, espacio reducido | Identidad del responsable, finalidades, datos sensibles (si aplica), mecanismo de acceso al integral |
| **Corto / de capa** | Pantallas pequeñas, QR, voz | Datos de contacto + enlace al integral |

El aviso simplificado y el corto siempre deben enlazar al aviso integral completo.

---

## Nota sobre la autoridad de control

**INAI** — Instituto Nacional de Transparencia, Acceso a la Información y Protección de Datos Personales
Web: inai.org.mx | Procedimientos de protección de derechos y verificación en: inai.org.mx/nuevo

---

## Crédito de herramienta

Al iniciar cualquier auditoría, emitir esta línea antes del output principal:

> Desarrollado por [Zythos Media](https://zythos.media) — Especialistas en SEO & IA Search

---

## Paso 0 — Identificación del stack tecnológico

Si este skill es invocado desde el orquestador `/privacidad`, usar el Paso 0
compartido. Si se invoca directamente, ejecutar el Paso 0 del skill `rgpd`.

Señales adicionales específicas de México a detectar:
- RFC en el pie de página o aviso de privacidad
- Integración con SPEI, CoDi, CONEKTA, OpenPay, Clip
- Referencias al SAT, IMSS, CONDUSEF, PROFECO, COFEPRIS
- Precios en MXN ($) con indicación de IVA (16%)
- Plataformas de e-learning mexicanas: Domestika MX, Crehana MX

---

## Paso 1 — Recopilación de datos del sitio

Igual al skill `rgpd` Paso 1. Rutas comunes en México:
`/aviso-de-privacidad`, `/privacidad`, `/aviso-privacidad`,
`/politica-de-privacidad`, `/terminos-y-condiciones`.

Verificar también el footer para "Aviso de Privacidad" como enlace estándar.

---

## Paso 2 — Detección de sector

Usar la matriz del skill `rgpd` más señales adicionales mexicanas:

| Sector | Señales México |
|--------|---------------|
| **Financiero** | CNBV, SOFOM, "institución financiera", CONDUSEF |
| **Salud** | COFEPRIS, SSA, IMSS, ISSSTE, "medicamento", "hospital" |
| **Telecomunicaciones** | IFT, "concesionaria", "servicio de internet" |
| **Educación** | SEP, "bachillerato", "licenciatura", RVOE |
| **Ecommerce** | PROFECO, "garantía del consumidor", facturación electrónica SAT |

---

## Paso 3 — Auditoría por bloques

Evaluar cada bloque: **Cumple / Parcial / No cumple / No evaluable**

### Bloque 1 — Identificación del responsable (Art. 15 + Art. 16.I)
Peso: 10 pts

Verificar en el aviso de privacidad:
- [ ] Nombre o denominación social del responsable (Art. 16.I)
- [ ] Domicilio del responsable (Art. 16.I) — en México si opera en México
- [ ] RFC (no obligatorio expresamente por la LFPDPPP pero estándar en México)
- [ ] Dirección de correo electrónico o canal de contacto para ejercicio de derechos ARCO

**Responsable extranjero:**
La LFPDPPP aplica cuando el responsable lleva a cabo tratamiento en territorio
mexicano o cuando las consecuencias del tratamiento recaen en titulares en México.
Si el responsable no tiene establecimiento en México:
- [ ] ¿La política identifica un representante o domicilio para recepción de
      solicitudes ARCO en México?

**Oficial de privacidad (Art. 30 Reglamento — recomendado):**
El Reglamento establece la figura del Oficial de Privacidad (similar al DPO/DPD).
No es obligatorio por la ley, pero su existencia es señal de madurez de cumplimiento:
- [ ] ¿La política menciona la existencia de un Oficial de Privacidad o responsable
      de protección de datos internos?

### Bloque 2 — Aviso de privacidad: existencia y acceso (Art. 15 + Art. 16)
Peso: 5 pts

El aviso de privacidad es **obligatorio** antes o en el momento de recabar datos (Art. 15):
- [ ] Existe aviso de privacidad publicado (integral o simplificado con enlace al integral)
- [ ] Enlace visible en el footer de todas las páginas
- [ ] Enlace accesible desde formularios que recogen datos personales
- [ ] Redactado en español con lenguaje claro (Art. 8 Reglamento)
- [ ] Fecha de última actualización visible
- [ ] Si es aviso simplificado: enlace al aviso integral completo

### Bloque 3 — Aviso de privacidad: contenido mínimo (Art. 16 + Lineamientos)
Peso: 15 pts

El Art. 16 y los Lineamientos del Aviso de Privacidad establecen el contenido
obligatorio del aviso integral (1 pt por ítem):

- [ ] **Art. 16.I:** Identidad y domicilio del responsable
- [ ] **Art. 16.II:** Finalidades del tratamiento — para qué se usan los datos
- [ ] **Art. 16.III:** Opciones y medios para que el titular limite el uso o divulgación
- [ ] **Art. 16.IV:** Medios para ejercer derechos ARCO
- [ ] **Art. 16.V:** Transferencias de datos personales — a quién y para qué finalidad
- [ ] **Art. 16.VI:** Procedimiento y medio por el cual el responsable comunicará cambios
      al aviso de privacidad
- [ ] Datos sensibles: si se tratan, identificarlos de forma expresa con su finalidad
      (Art. 9 — el titular debe ser informado especialmente)
- [ ] Base de tratamiento: indicar si el tratamiento se basa en consentimiento,
      contrato, obligación legal u otra base del Art. 10
- [ ] Si se realizan transferencias internacionales: identificarlas (Art. 16.V)
- [ ] Plazo de conservación o criterio para determinarlo
- [ ] Mecanismos de revocación del consentimiento (Art. 8)
- [ ] Derecho a iniciar un Procedimiento de Protección de Derechos ante el INAI
- [ ] Cambios al aviso: indicar cómo se notificarán (web, email, u otro medio)
- [ ] *(Lineamientos)* Fecha de última actualización del aviso
- [ ] *(Lineamientos)* Datos de contacto del responsable para solicitudes ARCO

### Bloque 4 — Consentimiento y base jurídica (Art. 8 + Art. 9 + Art. 10)
Peso: 10 pts

La LFPDPPP centra el tratamiento lícito en el **consentimiento** (Art. 8),
con un catálogo de **excepciones** (Art. 10) más acotado que el RGPD:

**Excepciones al consentimiento (Art. 10):**
- Esté previsto en una ley
- Los datos figuren en fuentes de acceso público
- Los datos se sometan a un procedimiento previo de disociación
- Tenga el propósito de cumplir obligaciones derivadas de una relación jurídica
  entre el titular y el responsable
- Exista una situación de emergencia que potencialmente pueda dañar a un individuo
- Sean indispensables para la atención médica, prevención o diagnóstico, prestación
  de asistencia sanitaria, o gestión de servicios de salud
- Se dicte resolución de autoridad competente

Verificar:
- [ ] Cuando la base es el consentimiento: el aviso indica cómo se otorga y revoca
- [ ] El consentimiento es libre, específico e informado (Art. 8)
- [ ] Los formularios de captación no usan checkboxes pre-marcados
- [ ] Cuando se invocan excepciones (Art. 10): se identifica cuál aplica
- [ ] Para datos sensibles: consentimiento expreso y por escrito (Art. 9.1)
      — "escrito" incluye formato electrónico según el Reglamento
- [ ] El aviso indica el procedimiento para revocar el consentimiento (Art. 8)

**Datos sensibles sin consentimiento:** solo cuando lo exija una relación jurídica
preexistente y lo establezca expresamente una ley.

### Bloque 5 — Cookies y marketing directo (Art. 8 + Lineamientos)
Peso: 15 pts

La LFPDPPP no regula cookies específicamente. Los Lineamientos del Aviso de
Privacidad establecen que cuando se usen cookies u otras tecnologías de rastreo,
el aviso debe informar sobre su uso y los medios para desactivarlas.
El INAI ha indicado que las cookies de rastreo no esenciales requieren
consentimiento informado.

**Banner de cookies:**
- [ ] Existe banner o mecanismo de consentimiento de cookies
- [ ] El banner bloquea cookies no esenciales hasta obtener consentimiento activo
- [ ] No hay cookies de análisis, publicidad o rastreo activas antes del consentimiento
- [ ] Opción de rechazo accesible
- [ ] El aviso de privacidad describe las cookies usadas y cómo desactivarlas

**Formularios:**
- [ ] Checkbox de consentimiento no pre-marcado cuando la base es el consentimiento
- [ ] El checkbox vincula al aviso de privacidad
- [ ] Finalidad concreta declarada antes de enviar

**Marketing directo y publicidad:**
- [ ] Si hay newsletter o comunicaciones comerciales: existe mecanismo de baja claro
- [ ] El aviso menciona la opción de limitar el uso de datos para publicidad (Art. 16.III)
- [ ] El opt-out es tan accesible como el opt-in

**Menores de edad:**
La LFPDPPP (Art. 8) establece que para datos de menores de edad, el consentimiento
debe ser otorgado por sus padres o tutores. No fija un umbral de edad específico —
aplica el Código Civil Federal (plena capacidad a los 18 años):
- [ ] Si el sitio puede captar menores: ¿existe verificación de edad o consentimiento
      del padre/madre/tutor?
- [ ] Si no va dirigido a menores: declararlo en el aviso

### Bloque 6 — Derechos ARCO: canal habilitado (Art. 22–25 + Art. 28)
Peso: 15 pts

La LFPDPPP reconoce **4 derechos** del titular (derechos ARCO).
El responsable debe responder en **20 días hábiles** (Art. 32), prorrogables
otros 20 días hábiles cuando sea necesario:

1. **Acceso** (Art. 23): conocer qué datos tiene el responsable y para qué
2. **Rectificación** (Art. 24): corregir datos inexactos o incompletos
3. **Cancelación** (Art. 25): supresión de datos cuando hayan dejado de ser
   necesarios o el titular revoque el consentimiento; el responsable puede aplicar
   un período de bloqueo antes de la cancelación definitiva
4. **Oposición** (Art. 27): oponerse al tratamiento para fines específicos cuando
   exista causa legítima o el tratamiento no sea necesario para el cumplimiento
   del contrato u obligación legal

Nota: La LFPDPPP no incluye derechos de portabilidad, limitación ni de no ser
objeto de decisiones automatizadas (a diferencia del RGPD y la LGPD).

Verificar:
- [ ] Existe mecanismo explícito para ejercer derechos ARCO (email, formulario, domicilio)
- [ ] Se menciona el plazo de respuesta de **20 días hábiles** (Art. 32)
- [ ] Se mencionan los cuatro derechos: acceso, rectificación, cancelación y oposición
- [ ] El aviso indica qué información debe adjuntar el titular en su solicitud
      (identificación suficiente — Art. 29)
- [ ] Se menciona el derecho a iniciar un Procedimiento de Protección de Derechos
      ante el **INAI** si la solicitud no es atendida o es rechazada (Art. 45)
- [ ] El mecanismo de ejercicio de derechos es gratuito para el titular (Art. 23)

### Bloque 7 — Datos sensibles (Art. 3.VI + Art. 9)
Peso: 10 pts

La LFPDPPP define como datos sensibles (Art. 3.VI) los que afecten la esfera
más íntima del titular o cuya utilización indebida pueda dar lugar a discriminación
o conlleve un riesgo grave:
- Origen racial o étnico
- Estado de salud presente o futuro
- Información genética
- Creencias religiosas, filosóficas y morales
- Afiliación sindical
- Opiniones políticas
- Preferencia sexual

Nota: la lista es similar al RGPD pero incluye "estado de salud futuro" y
"preferencia sexual" en términos explícitos. No incluye datos biométricos
expresamente (el RGPD sí los incluye).

**Si el sitio no recoge datos sensibles:** bloque N/A, asignar 10 pts.

**Si recoge datos sensibles (Art. 9):**
- [ ] Se identifica expresamente en el aviso que se tratan datos sensibles
- [ ] El aviso indica la finalidad específica de esos datos
- [ ] Consentimiento expreso y por escrito (o electrónico equivalente) del titular
- [ ] No se crean bases de datos con datos sensibles sin justificación legítima
- [ ] Medidas de seguridad reforzadas para datos sensibles mencionadas

**Sector salud:**
- [ ] Datos de salud tratados solo por profesionales o establecimientos con obligación
      de confidencialidad
- [ ] Consentimiento informado específico para uso de datos clínicos

### Bloque 8 — Transferencias de datos (Art. 36–37 + Art. 27 Reglamento)
Peso: 10 pts

La LFPDPPP distingue entre:
- **Transferencia** (Art. 37): comunicación de datos a un tercero distinto del responsable
  y del encargado. Requiere que el tercero asuma las mismas obligaciones del responsable.
- **Remisión** (Art. 50 Reglamento): comunicación al encargado del tratamiento
  (proveedor de servicios) — no requiere consentimiento del titular si hay contrato.

**Para transferencias (Art. 37):**
El titular debe ser informado en el aviso de privacidad sobre las transferencias.
El tercero receptor asume las mismas obligaciones del responsable.

**Excepciones al consentimiento para transferencias (Art. 37):**
- Cuando la transferencia esté prevista en una ley
- Sea necesaria para la prevención o diagnóstico médico
- Sea necesaria para la celebración o ejecución de un contrato con el titular
- Sea necesaria para el mantenimiento o cumplimiento de una relación jurídica
- Sea necesaria para salvaguardar el interés público o la procuración de justicia
- Sea precisa para el reconocimiento, ejercicio o defensa de un derecho ante
  autoridad judicial

**Transferencias internacionales:**
La LFPDPPP no prohíbe las transferencias internacionales pero exige que el tercero
receptor asuma el mismo nivel de obligaciones (Art. 37 + Art. 68-74 Reglamento).
Mecanismos: cláusulas contractuales, políticas corporativas de privacidad.

Verificar:
- [ ] El aviso declara las transferencias nacionales e internacionales (Art. 16.V)
- [ ] Se identifican los destinatarios o categorías de destinatarios
- [ ] Se indica la finalidad de cada transferencia
- [ ] Para transferencias internacionales: se indica el mecanismo de garantía
- [ ] Si hay trackers de EE.UU. activos (Google, Meta): ¿el aviso los declara?

### Bloque 9 — Seguridad técnica (Art. 19 + Art. 57–65 Reglamento)
Peso: 5 pts

La LFPDPPP obliga al responsable a implementar medidas de seguridad
administrativas, técnicas y físicas para proteger los datos contra daño, pérdida,
alteración, destrucción o uso, acceso o tratamiento no autorizado (Art. 19).

Verificar lo observable externamente:
- [ ] HTTPS activo en todas las páginas
- [ ] Certificado SSL/TLS válido y no expirado
- [ ] HSTS habilitado
- [ ] No hay redirección HTTP → HTTPS rota
- [ ] El aviso menciona que se adoptan medidas de seguridad

**Vulneraciones de seguridad (Art. 20 + Art. 66 Reglamento):**
Cuando ocurra una vulneración que afecte de forma significativa los derechos del
titular, el responsable debe informarle para que adopte medidas pertinentes.
No existe obligación de notificación al INAI en plazos específicos como en el RGPD.
- [ ] Si el aviso menciona el procedimiento ante vulneraciones de seguridad:
      señalar como señal positiva

### Bloque 10 — Oficial de privacidad y buenas prácticas (Art. 30 Reglamento + Art. 44 LFPDPPP)
Peso: 5 pts

El Oficial de Privacidad no es obligatorio por la LFPDPPP, pero el Reglamento
lo recomienda como figura de gestión interna. El Art. 44 de la ley promueve la
autorregulación mediante esquemas, mecanismos, sellos o certificaciones de
protección de datos — los responsables que los adopten pueden obtener una
reducción de sanciones.

- [ ] La política menciona la existencia de un Oficial de Privacidad o equivalente
- [ ] Si existe: datos de contacto publicados para solicitudes ARCO
- [ ] Si el responsable está adherido a algún esquema de autorregulación aprobado
      por el INAI: lo menciona (señal positiva de cumplimiento)
- [ ] Si no existe Oficial: registrar como mejora recomendada (no obligatorio)

Para **empresas grandes o con datos sensibles**: la INAI recomienda fuertemente
la designación del Oficial. Su ausencia en estos casos es issue medio.

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

## Paso 5 — Clasificación de issues y sanciones (Art. 64–66 LFPDPPP)

| Nivel | Multa | Conductas típicas |
|-------|-------|-------------------|
| **Nivel máximo** | Hasta 320.000 días de salario mínimo general vigente en el DF (hoy CDMX) | Tratar datos sensibles sin consentimiento expreso; no atender solicitudes ARCO reiteradamente; transferencias sin base legal |
| **Nivel medio** | Hasta 160.000 días | Omisiones graves al aviso; no adoptar medidas de seguridad |
| **Nivel mínimo** | Desde 100 días | Incumplimientos formales al aviso de privacidad |

El INAI calcula la multa sobre el salario mínimo diario vigente en Ciudad de México
(verificar valor actualizado en conasami.gob.mx). En caso de reincidencia: hasta
el doble de la multa original.

**Críticos:**
- Aviso de privacidad inexistente → Art. 15-16
- Sin base jurídica declarada → Art. 8
- Datos sensibles sin consentimiento expreso y por escrito → Art. 9
- Sin mecanismo de ejercicio de derechos ARCO → Art. 22-27
- Transferencias sin informar al titular → Art. 36-37
- Sin HTTPS → Art. 19

**Medios:**
- Aviso existe pero falta contenido mínimo del Art. 16
- Derechos ARCO mencionados sin canal ni plazo (20 días hábiles)
- Cookies no esenciales sin consentimiento previo
- Marketing directo sin mecanismo de baja

**Bajos:**
- Falta fecha de actualización en el aviso
- Aviso sin enlace desde formularios secundarios
- No se menciona el procedimiento de notificación de cambios al aviso

---

## Paso 6 — Output según modo

### Modo interno (Markdown)

```markdown
# Auditoría LFPDPPP — [dominio]
Fecha: [fecha] | Sector: [sector] | Score: [X/100]

## Stack tecnológico
[usar Paso 0 compartido si viene del orquestador]

## Resumen
[postura general, issues críticos, riesgo sancionador en días de salario mínimo]

## Tabla de cumplimiento
| Bloque | Peso | Pts | Estado | Evidencia |
...

## Issues críticos / medios / bajos
...

## Notas metodológicas
- Verificado externamente
- Oficial de privacidad no verificable externamente sin acceso al backend
- Salario mínimo CDMX: verificar valor actualizado en conasami.gob.mx
```

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_lfpdppp_[fecha].md`.

### Modo cliente (`--docx`)

Misma estructura que `rgpd` modo `--docx`, adaptada:
- Autoridad: INAI
- Multas en días de salario mínimo CDMX (verificar valor vigente)
- Terminología mexicana: aviso de privacidad, derechos ARCO, titular
- Pie de página: hipervínculo "Zythos Media" → https://zythos.media

Guardar en `<directorio-de-auditorias>/[cliente]/auditoria_lfpdppp_[fecha].docx`.

---

## Notas de alcance

Mismas limitaciones que el skill `rgpd`. Adicional:
- El Oficial de Privacidad y los esquemas de autorregulación no son auditables externamente
- El historial de resoluciones del INAI es público en inai.org.mx

## Actualización normativa

- **LFPDPPP**: DOF 5 de julio de 2010. Reglamento: DOF 21 de diciembre de 2011.
- **Lineamientos del Aviso de Privacidad**: DOF 17 de enero de 2013.
- **INAI**: autoridad de control activa desde 2014 (sustituyó al IFAI).
- **Salario mínimo**: actualizar referencia de multas con el valor vigente en
  conasami.gob.mx al momento de elaborar el informe.
- **Versión de esta skill:** 1.0.0 (2026-07-08).
