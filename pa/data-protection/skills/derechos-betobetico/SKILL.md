---
name: derechos-betobetico
title: /derechos
description: Respondedor de derechos del titular — recibe una solicitud de ejercicio de derechos (acceso, rectificación, cancelación/supresión, oposición, portabilidad) y genera el acuse de recibo y la respuesta sustantiva. Verifica identidad, evalúa excepciones y respeta el plazo de respuesta de la Ley 81 de 2019. Usar cuando el usuario diga "ha llegado un derecho", "solicitud de acceso", "quieren que borremos sus datos" o pegue una solicitud.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/privacidad/skills/derechos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: data-protection
language: es
---

# /derechos

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → proceso de derechos del titular (canales, verificación de identidad, SLA, responsable).
2. Clasificar el derecho ejercido.
3. Verificar identidad del titular.
4. Evaluar excepciones y límites al derecho.
5. Generar acuse de recibo + respuesta sustantiva como borradores.
6. Registrar la solicitud según el proceso interno.

**Antes de pegar la solicitud:** la solicitud contiene datos personales del titular. No almacenar el nombre del titular en nombres de archivo. Redactar lo que no sea necesario.

```
/privacidad:derechos
[pegar la solicitud del titular]
```

---

## Propósito

Los derechos del titular tienen plazos legales estrictos fijados en la Ley 81 de 2019 y su Decreto Ejecutivo 285 de 2021, un proceso definido y muchos puntos donde se puede cometer un error: verificación insuficiente, excepción no documentada, plazo vencido. Este skill guía cada paso y genera los borradores de respuesta.

---

## Flujo de trabajo

### Paso 1: Clasificar el derecho

Identificar qué derecho ejerce el titular:

| Derecho | Referencia | Contenido |
|---|---|---|
| **Acceso** | Art. 15 de la Ley 81 de 2019 | Copia de datos + información sobre el tratamiento |
| **Rectificación** | Art. 15 de la Ley 81 de 2019 | Corregir datos inexactos o incompletos |
| **Cancelación / Supresión** | Art. 15 de la Ley 81 de 2019 | Eliminar datos (con excepciones) |
| **Oposición** | Art. 15 de la Ley 81 de 2019 | Cesar un tratamiento concreto |
| **Portabilidad** | Art. 15 de la Ley 81 de 2019 | Datos en formato estructurado y legible por máquina |

Si la solicitud combina derechos ("borra mis datos y antes dame una copia"), tratar como solicitudes vinculadas.

### Paso 2: Verificar identidad

Según el método configurado en `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`.

Opciones habituales:
- **Solicitud desde sesión autenticada** → identidad confirmada
- **Email coincidente con registros** → suficiente para solicitudes de bajo riesgo
- **Verificación adicional** → para supresión o datos sensibles: cédula o pasaporte/carné de residente, pregunta de seguridad

**Calibrar al riesgo.** Sobre-verificar convierte el proceso en barrera (mal visto por la ANTAI). Infra-verificar puede entregar datos a quien no corresponde.

Si no se puede verificar identidad, generar respuesta solicitando verificación. El plazo **no se suspende** salvo que la ANTAI haya indicado lo contrario — responder pidiendo verificación dentro de los primeros días.

### Paso 3: Localizar los datos

Recorrer la lista de sistemas de `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`:

| Sistema | Consultado | Datos encontrados | Qué |
|---|---|---|---|
| Base de datos producción | | | |
| CRM | | | |
| Herramienta de soporte | | | |
| Email marketing | | | |
| Logs / analítica | | | |
| Copias de seguridad | | | (normalmente exentas de supresión) |
| Encargados de tratamiento | | | (pueden necesitar notificación) |

### Paso 4: Evaluar excepciones

**No toda solicitud procede íntegramente.** Para cada excepción, citar la norma:

- **Cancelación / Supresión** — excepciones de la Ley 81 de 2019: obligación legal de conservar (conservación contable y fiscal según el Código de Comercio y la legislación de la DGI; prevención de blanqueo conforme a la Ley 23 de 2015), ejercicio de defensa de reclamaciones, interés público
- **Portabilidad** — solo datos proporcionados por el titular y tratados por medios automatizados con base en consentimiento o relación contractual (Ley 81 de 2019)
- **Oposición** — el responsable puede acreditar causas legítimas que prevalezcan, salvo en marketing directo, donde el cese es obligatorio (Ley 81 de 2019)

Cada excepción propuesta lleva nota: **"propuesta — requiere revisión por letrado antes de aplicarla."**

### Paso 5: Generar respuestas — DOS CARTAS

#### 5a — Acuse de recibo (enviar en 1-3 días)

```markdown
Asunto: Hemos recibido su solicitud de [derecho] — [Empresa] — [fecha]

Estimado/a [Nombre]:

Hemos recibido su solicitud de [acceso / rectificación / supresión / oposición /
portabilidad / limitación] con fecha [fecha de recepción].

**Su solicitud, según la entendemos:** [resumen en una frase].

**Próximos pasos:**
- Nuestra fecha objetivo de respuesta es [fecha — dentro de los 10 días hábiles
  desde la presentación de su solicitud, conforme al art. 16 de la Ley 81 de 2019].
- No se aplica ningún cargo a esta solicitud (suministro gratuito de información, art. 16 de la Ley 81 de 2019).

[Si falta verificación de identidad:]
**Para verificar su identidad,** por favor [paso concreto — ej., remita copia de
su cédula o pasaporte al email datos@empresa.com].

Para cualquier consulta, contacte con [datos de contacto del encargado de protección de datos / responsable].

[Firmante]
```

#### 5b — Respuesta sustantiva (antes de que venza el plazo)

Adaptar plantilla según el derecho ejercido. Estructura mínima:

```markdown
Asunto: Respuesta a su solicitud de [derecho] — [Empresa] — [fecha]

Estimado/a [Nombre]:

En relación con su solicitud de [derecho] recibida el [fecha]:

**Resultado:**
[Tabla con datos facilitados / rectificados / suprimidos / portados / limitados,
según proceda]

**Datos no incluidos / no suprimidos y motivo:**
| Categoría | Excepción aplicada | Base legal |
|---|---|---|
| [Ej., Registros fiscales/contables] | Obligación legal de conservación | Ley 81 de 2019; Código de Comercio / legislación de la DGI |

**Sus otros derechos:** Puede ejercer [otros derechos] a través de [canal].
Si no está conforme, puede reclamar ante la ANTAI.

[Firmante]
```

### Paso 6: Registrar

Documentar: fecha de recepción, fecha de verificación, fecha de respuesta, qué se facilitó/suprimió, excepciones aplicadas, quién gestionó.

---

## Plazos

| Concepto | Plazo | Base legal |
|---|---|---|
| Respuesta al titular | 10 días hábiles desde la presentación de la solicitud | Art. 16 de la Ley 81 de 2019 (Decreto Ejecutivo 285 de 2021, art. 15) |
| Prórroga por complejidad | No prevista en la norma panameña (no existe la prórroga general del RGPD) | Ley 81 de 2019 |
| Gratuidad | El suministro de información es gratuito (la excepción del RGPD por solicitudes "manifiestamente infundadas o excesivas" no está recogida en la Ley 81) | Art. 16 de la Ley 81 de 2019 |

---

## Disparadores de escalado

- El titular es (o puede ser) demandante, periodista o representante legal
- El alcance es inusual ("todas las comunicaciones internas sobre mí")
- Existe un litigation hold sobre los datos del titular
- El titular impugna una respuesta previa
- La ANTAI está en copia o se menciona procedimiento sancionador

---

## Legislación de referencia

- Ley 81 de 2019 — derechos del titular de los datos personales (art. 15: acceso, rectificación, cancelación/supresión, oposición y portabilidad; art. 16: plazo de 10 días hábiles y gratuidad)
- Decreto Ejecutivo 285 de 2021 — reglamento de ejercicio de derechos (art. 15)
- Guías y resoluciones de la ANTAI sobre el ejercicio de derechos
- Criterios de la ANTAI sobre verificación de identidad

---

## Lo que este skill NO hace

- No consulta directamente los sistemas — guía el proceso y genera los borradores.
- No decide excepciones en casos dudosos — las marca con `[revisión]`.
- No envía la respuesta — borrador para revisión humana y envío por el responsable.
