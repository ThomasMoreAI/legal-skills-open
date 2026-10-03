---
name: derechos
title: /derechos
description: Respondedor de derechos ARCO-POL — recibe una solicitud de ejercicio de derechos (acceso, rectificación, supresión, oposición, portabilidad, olvido, limitación) y genera el acuse de recibo y la respuesta sustantiva. Verifica identidad, evalúa excepciones y respeta el plazo de 1 mes del art. 12.3 RGPD. Usar cuando el usuario diga "ha llegado un derecho", "solicitud de acceso", "quieren que borremos sus datos" o pegue una solicitud.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/privacidad/skills/derechos
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /derechos

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → proceso ARCO-POL (canales, verificación de identidad, SLA, responsable).
2. Clasificar el derecho ejercido.
3. Verificar identidad del interesado.
4. Evaluar excepciones y límites al derecho.
5. Generar acuse de recibo + respuesta sustantiva como borradores.
6. Registrar la solicitud según el proceso interno.

**Antes de pegar la solicitud:** la solicitud contiene datos personales del interesado. No almacenar el nombre del interesado en nombres de archivo. Redactar lo que no sea necesario.

```
/privacidad:derechos
[pegar la solicitud del interesado]
```

---

## Propósito

Los derechos de los interesados tienen plazos legales estrictos (1 mes, prorrogable 2 meses más por complejidad — art. 12.3 RGPD), un proceso definido y muchos puntos donde se puede cometer un error: verificación insuficiente, excepción no documentada, plazo vencido. Este skill guía cada paso y genera los borradores de respuesta.

---

## Flujo de trabajo

### Paso 1: Clasificar el derecho

Identificar qué derecho ejerce el interesado:

| Derecho | Artículo RGPD | Artículo LOPDGDD | Contenido |
|---|---|---|---|
| **Acceso** | Art. 15 | Art. 13 | Copia de datos + información sobre el tratamiento |
| **Rectificación** | Art. 16 | Art. 14 | Corregir datos inexactos o incompletos |
| **Supresión (olvido)** | Art. 17 | Art. 15 | Eliminar datos (con excepciones) |
| **Oposición** | Art. 21 | Art. 18 | Cesar un tratamiento concreto |
| **Portabilidad** | Art. 20 | Art. 17 | Datos en formato estructurado y legible por máquina |
| **Limitación** | Art. 18 | Art. 16 | Suspender el tratamiento mientras se resuelve una disputa |

Si la solicitud combina derechos ("borra mis datos y antes dame una copia"), tratar como solicitudes vinculadas.

### Paso 2: Verificar identidad

Según el método configurado en `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md`.

Opciones habituales:
- **Solicitud desde sesión autenticada** → identidad confirmada
- **Email coincidente con registros** → suficiente para solicitudes de bajo riesgo
- **Verificación adicional** → para supresión o datos sensibles: DNI/NIE, pregunta de seguridad

**Calibrar al riesgo.** Sobre-verificar convierte el proceso en barrera (mal visto por la AEPD). Infra-verificar puede entregar datos a quien no corresponde.

Si no se puede verificar identidad, generar respuesta solicitando verificación. El plazo **no se suspende** salvo que la AEPD haya indicado lo contrario — responder pidiendo verificación dentro de los primeros días.

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

- **Supresión** — excepciones del art. 17.3 RGPD: obligación legal de conservar (facturación 4 años CC, fiscal 4 años LGT, blanqueo 10 años Ley 10/2010), ejercicio de defensa de reclamaciones, interés público
- **Portabilidad** — solo datos proporcionados por el interesado y tratados por medios automatizados con base en consentimiento o contrato (art. 20.1 RGPD)
- **Oposición** — el responsable puede acreditar motivos legítimos imperiosos que prevalezcan (art. 21.1 RGPD), salvo marketing directo (cese obligatorio, art. 21.3)

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
- Nuestra fecha objetivo de respuesta es [fecha — máximo 1 mes desde recepción,
  art. 12.3 RGPD]. Si la solicitud es compleja, podremos ampliar el plazo 2 meses
  adicionales, informándole antes de que venza el primer mes (art. 12.3 RGPD).
- No se aplica ninguna tasa a esta solicitud.

[Si falta verificación de identidad:]
**Para verificar su identidad,** por favor [paso concreto — ej., remita copia de
DNI/NIE al email dpd@empresa.com].

Para cualquier consulta, contacte con [datos de contacto del DPO / responsable].

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
| [Ej., Registros fiscales] | Obligación legal de conservación | Art. 17.3.b RGPD; art. 30 LGT |

**Sus otros derechos:** Puede ejercer [otros derechos] a través de [canal].
Si no está conforme, puede reclamar ante la AEPD (www.aepd.es).

[Firmante]
```

### Paso 6: Registrar

Documentar: fecha de recepción, fecha de verificación, fecha de respuesta, qué se facilitó/suprimió, excepciones aplicadas, quién gestionó.

---

## Plazos

| Concepto | Plazo | Base legal |
|---|---|---|
| Respuesta al interesado | **1 mes** desde recepción | Art. 12.3 RGPD |
| Prórroga por complejidad | **+2 meses** (informar en el 1.er mes) | Art. 12.3 RGPD |
| Gratuidad | Gratuito salvo solicitud manifiestamente infundada o excesiva | Art. 12.5 RGPD |
| Solicitudes repetitivas | Puede cobrarse canon razonable o negarse | Art. 12.5 RGPD |

---

## Disparadores de escalado

- El interesado es (o puede ser) demandante, periodista o representante legal
- El alcance es inusual ("todas las comunicaciones internas sobre mí")
- Existe un litigation hold sobre los datos del interesado
- El interesado impugna una respuesta previa
- La AEPD está en copia o se menciona procedimiento sancionador

---

## Legislación de referencia

- RGPD arts. 12-22 (derechos de los interesados)
- LOPDGDD arts. 12-18 (ejercicio de derechos en España)
- Guía de la AEPD sobre el ejercicio de derechos
- Criterios de la AEPD sobre verificación de identidad

---

## Lo que este skill NO hace

- No consulta directamente los sistemas — guía el proceso y genera los borradores.
- No decide excepciones en casos dudosos — las marca con `[revisión]`.
- No envía la respuesta — borrador para revisión humana y envío por el responsable.
