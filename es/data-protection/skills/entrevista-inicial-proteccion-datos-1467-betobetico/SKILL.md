---
name: entrevista-inicial-proteccion-datos-1467-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de protección de datos — aprende cómo funciona tu programa de privacidad (DPD, RAT, EIPD, brechas, auditorías) y escribe el perfil de práctica en CLAUDE.md. Úsalo en la primera ejecución, cuando CLAUDE.md no exista o tenga marcadores pendientes, o cuando el usuario diga "configurar protección de datos", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/proteccion-datos/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: data-protection
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: RAT actual, EIPD realizadas, protocolo de brechas, informes de auditoría. Leer todos los que se proporcionen.
4. Extraer: estructura del RAT, metodología EIPD, protocolo de brechas, programa de auditoría.
5. Migración: si existe un CLAUDE.md poblado (sin marcadores `[PENDIENTE]`) en `~/.claude/plugins/cache/claude-para-abogados/proteccion-datos/*/CLAUDE.md` pero no en la ruta de config, copiarlo y mostrar al usuario lo migrado.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integrations`

Re-ejecuta la verificación de integraciones (almacenamiento de documentos, Slack, tareas programadas) y actualiza `## Integraciones disponibles` en `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md`. No repite la entrevista.

Al verificar: solo reportar como conectado (checkmark) si una llamada MCP real tuvo éxito. Conectores configurados pero no probados se marcan con un circulo y una instrucción breve. Nunca reportar como conectado basándose solo en `.mcp.json`.

```
/proteccion-datos:entrevista-inicial
```

```
/proteccion-datos:entrevista-inicial --check-integrations
```

---

# Entrevista Inicial: Protección de Datos

## Propósito

Aprender cómo funciona *este* programa de protección de datos — quién es el DPD, cómo está el RAT, qué evaluaciones de impacto se han hecho, cómo se gestionan las brechas y cuál es el programa de auditoría. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` para que todos los demás skills lean desde la misma base.

Cada programa de protección de datos es distinto. Un hospital con datos de salud no tiene nada en común con una SaaS B2B. La entrevista determina qué tipo de organización es antes de todo lo demás.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → saludar y ofrecer retomar desde esa sección.
- **Contiene marcadores `[PENDIENTE]` pero sin comentario de pausa** → la plantilla nunca se completó; ofrecer empezar de cero o retomar.
- **Poblado (sin pendientes, sin pausa)** → ya configurado; saltar salvo `--redo`.

## Comprobar el perfil de empresa compartido

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea: "Eres [nombre], [entorno], en [empresa], [sector], operando en [jurisdicciones]. ¿Correcto? (Di 'actualizar' para cambiar el perfil compartido.)" Si confirma, saltar las preguntas de empresa e ir directo a las específicas del módulo.
- **Si no existe:** Serás el primer módulo que configure este usuario. Tras la orientación, hacer las preguntas de empresa y escribirlas en el perfil compartido, luego continuar con las preguntas específicas. Decir: "He guardado tu perfil de empresa — los otros módulos legales lo leerán y se saltarán estas preguntas."

## Antes de empezar la entrevista

Mostrar el preámbulo (3-4 líneas cortas):

> **`proteccion-datos` es para quienes gestionan el programa de protección de datos: RAT, EIPD, brechas, auditorías, comunicación con la AEPD.** ¿No es tu área? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu rol, si tienes DPD y las bases jurídicas principales, con valores por defecto en el resto. **15 minutos** añade el RAT completo, la metodología de EIPD, el protocolo de brechas y el programa de auditoría.
>
> ¿Rápido o completo? (Puedes ampliar en cualquier momento con `/proteccion-datos:entrevista-inicial --completo`.)

Esperar a que el usuario elija antes de continuar.

## Después de elegir rápido o completo

Orientar al usuario:

> "Este módulo mantiene tu perfil de práctica de protección de datos (DPD, RAT, EIPD, brechas, auditorías), y lo usa como referencia en cada tarea. La entrevista aprende cómo trabajas realmente y lo escribe en un archivo de texto plano. Todo lo que respondas se puede cambiar después. Una vez hecho, los comandos del módulo funcionarán como tú trabajas, no como una plantilla genérica."
>
> "La configuración se construye solo desde tus respuestas y los documentos semilla. No lee tu historial de Claude ni otras conversaciones."
>
> "¿Listo? Unas preguntas rápidas primero, luego profundizamos."

**Ruta rápida:** preguntar solo Parte 0 (rol, integraciones) y si hay DPD designado. Escribir config con marcadores `[POR DEFECTO]` en lo demás. Cerrar con: "Hecho. Puedes empezar a usar los comandos. He puesto valores por defecto para RAT, EIPD y brechas. Ejecuta `/proteccion-datos:entrevista-inicial --completo` cuando quieras hacer la entrevista completa."

**Ruta completa:** el flujo de entrevista completo descrito abajo.

## Ritmo de la entrevista

- **Asumir que la respuesta existe en algún sitio.** Cuando una pregunta pida información que probablemente esté documentada — RAT, protocolo de brechas, informe de auditoría — pedir un enlace o un pegado antes de pedir que lo teclee de memoria. "Pega un enlace o un documento, o dame la versión corta" es la petición por defecto.
- **Tamaño del lote — contar subpreguntas.** "Nunca más de 2-3 preguntas por turno" significa 2-3 *preguntas respondibles*, contando subpartes. Si no cabe en una pantalla, son demasiadas.
- **Pausar para respuestas reales.** Cuando una pregunta necesite más que una selección rápida: "Esta necesita una respuesta escrita — espero." No avanzar hasta que el usuario responda.
- **Para documentos semilla:** "Pega el contenido, comparte una ruta o URL, o di 'saltar por ahora.' Si saltas, lo marco como pendiente para que lo rellenes después."
- **Antes de escribir el perfil:** revisar la entrevista. Listar preguntas saltadas o con marcadores. Decir: "Antes de escribir tu perfil, esto queda abierto: [lista]. ¿Quieres rellenar algo ahora o dejarlo como pendiente?"
- **Pausa y reanudación.** Decir al usuario: "Si necesitas parar, di 'pausa' y guardaré tu progreso. Ejecuta `/proteccion-datos:entrevista-inicial` más tarde y retomaremos donde lo dejaste." Al pausar, escribir config parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.

**Verificar hechos legales.** Cuando el usuario cite una norma, plazo, umbral o número de registro, verificar antes de escribirlo en la config. Si hay conflicto: "Has dicho que el plazo es X; mi entendimiento es Y — ¿puedes confirmar cuál va en el perfil? `[premisa marcada — verificar]`"

## La entrevista

### Apertura

> Voy a ayudarte con el registro de actividades, evaluaciones de impacto, gestión de brechas y auditorías de protección de datos. Antes de hacer nada de eso, necesito saber cómo funciona tu programa. Diez minutos.
>
> Después te pediré que me enseñes cuatro cosas: tu RAT actual, alguna EIPD que hayas hecho, tu protocolo de brechas y tus informes de auditoría. Aprenderé más de esos documentos que de cualquier cosa que me cuentes.

### Parte 0: Quién usa esto y qué hay conectado

Tres preguntas rápidas antes de entrar en protección de datos. Configuran cómo funciona el módulo, no qué puede hacer.

#### ¿Quién usa esto?

> ¿Quién va a usar este módulo en el día a día? (Esto determina el encabezado de los documentos de trabajo y el marco de los resultados.)
>
> 1. **Abogado o profesional jurídico** — abogado, DPD con formación jurídica, responsable de privacidad bajo supervisión letrada.
> 2. **No jurista con acceso a abogado** — DPD no jurista, responsable de cumplimiento, consultor con abogado de referencia.
> 3. **No jurista sin acceso regular a abogado** — lo llevas tú solo.

Si la respuesta es 2 o 3, decir una vez:

> Puedes usar todas las funciones — RAT, EIPD, gestión de brechas, auditorías. Dos cosas cambian:
>
> 1. **Enmarco los resultados como investigación para revisión letrada**, no como dictámenes.
> 2. **Pauso antes de pasos con consecuencias legales** — comunicación a la AEPD, notificación de brechas a interesados. Te preguntaré si has consultado con un abogado.

Si la respuesta es 3, añadir:

> Si necesitas encontrar un abogado especializado en protección de datos: el Colegio de Abogados de tu provincia tiene servicio de orientación. La AEPD publica guías para responsables. Muchos despachos ofrecen una primera consulta gratuita.

#### ¿Qué hay conectado?

> Este módulo puede trabajar con: almacenamiento de documentos (Google Drive, SharePoint, Dropbox), Slack y tareas programadas. Voy a comprobar qué conectores tienes configurados.

Verificar qué está realmente conectado (no solo configurado). Para cada conector:
- Si se puede probar: reportar como conectado solo si responde.
- Si no se puede probar: marcar como "configurado pero no verificado".
- Nunca reportar como conectado basándose solo en la configuración.

> - (checkmark) [Integración] — conectado (verificado)
> - (circulo) [Integración] — configurado pero no verificado. Abre la configuración MCP para confirmar.
> - (cruz) [Integración] — no encontrado. [Función] usará [alternativa manual]. [Cómo conectar.]
>
> No necesitas todas. Las funciones principales funcionan solo con acceso a archivos.

### Parte 1: Delegado de Protección de Datos (DPD)

*(Esta información alimenta todos los skills que necesitan saber quién es el punto de contacto con la AEPD y cómo se estructura la supervisión.)*

> ¿Tenéis designado un Delegado de Protección de Datos?

- **DPD interno o externo:** ¿Es un empleado de la organización o un servicio externo?
- **Datos de contacto:** Nombre, email, si está publicado en la web y comunicado a la AEPD.
- **Comunicación con la AEPD:** ¿Ha habido comunicaciones previas? ¿Consultas previas? ¿Alguna inspección o procedimiento abierto?

Si no hay DPD designado: "¿Es obligatorio en vuestro caso? La designación es obligatoria para autoridades públicas, tratamientos a gran escala de categorías especiales, y observación habitual y sistemática a gran escala (art. 37 RGPD, art. 34 LOPDGDD). ¿Encajáis en alguno de estos supuestos? `[verificar obligatoriedad]`"

### Parte 2: Registro de Actividades de Tratamiento (RAT)

*(Esto alimenta los skills de evaluación de impacto, análisis de riesgos y auditoría — sin un RAT actualizado, todo se construye sobre arena.)*

> "¿Tenéis un Registro de Actividades de Tratamiento? Pega el contenido, comparte una ruta o URL, o dame la versión resumida."

- **Categorías de tratamiento actuales:** ¿Cuántas actividades hay registradas? ¿Están actualizadas?
- **Bases jurídicas principales:** ¿Cuáles usáis más? (Consentimiento, interés legítimo, ejecución contractual, obligación legal, interés vital, interés público.)
- **Plazos de conservación:** ¿Están definidos por actividad? ¿Hay una política general de retención?
- **Transferencias internacionales:** ¿Transferís datos fuera del EEE? ¿Con qué garantías? (Decisiones de adecuación, cláusulas contractuales tipo, BCR.)

Si no hay RAT: "El RAT es obligatorio para responsables con más de 250 empleados o que realicen tratamientos de riesgo (art. 30 RGPD). Incluso si no es obligatorio, es la base de todo lo demás. ¿Quieres que te ayude a construir uno desde cero?"

### Parte 3: Evaluaciones de Impacto (EIPD)

*(Esto alimenta `/proteccion-datos:eipd` — la estructura, profundidad y metodología que uses aquí es la plantilla por defecto para cada EIPD que generemos.)*

> "¿Habéis realizado evaluaciones de impacto en protección de datos?"

- **EIPD realizadas:** ¿Cuántas? ¿Para qué tratamientos? Pega una de ejemplo si puedes.
- **Metodología:** ¿Seguís la guía de la AEPD? ¿La metodología CNIL? ¿Otra propia?
- **Lista de la AEPD:** ¿Habéis revisado la lista de tratamientos que requieren EIPD obligatoria publicada por la AEPD? (Lista del art. 35.4 RGPD publicada por la AEPD.)
- **Umbrales:** ¿Qué desencadena una EIPD en vuestra organización? ¿Solo lo obligatorio o también análisis voluntarios?
- **Aprobación:** ¿Quién firma la EIPD? ¿Solo el DPD, un comité, dirección?

Si no han hecho EIPD: "¿Tenéis tratamientos de alto riesgo? Videovigilancia a gran escala, perfilado, datos de salud masivos, decisiones automatizadas con efectos jurídicos... Si la respuesta es sí, la EIPD es obligatoria. Si no estáis seguros, el primer paso es cruzar vuestro RAT con la lista de la AEPD."

### Parte 4: Gestión de Brechas de Seguridad

*(Esto alimenta `/proteccion-datos:brecha` — el protocolo, los tiempos de respuesta y el equipo de gestión determinan cómo el skill estructura la respuesta ante un incidente.)*

> "¿Tenéis un protocolo de gestión de brechas de seguridad de datos personales?"

- **Historial de incidentes:** ¿Ha habido brechas notificadas a la AEPD? ¿Cuántas? ¿Alguna notificada a los interesados?
- **Protocolo actual:** ¿Está documentado? Pega el contenido o comparte ruta. ¿Incluye las 72 horas del art. 33 RGPD?
- **Equipo de respuesta:** ¿Quién participa? (DPD, seguridad, dirección, comunicación, legal.) ¿Hay roles asignados?
- **Registro de brechas:** ¿Mantenéis el registro interno del art. 33.5 RGPD con todas las brechas, notificadas o no?
- **Comunicación a interesados:** ¿Tenéis plantillas? ¿Criterios para determinar cuándo es necesaria la comunicación del art. 34 RGPD?

Si no hay protocolo: "Las 72 horas del art. 33 RGPD empiezan a contar desde que tenéis conocimiento. Sin un protocolo preparado, esas 72 horas se gastan en decidir qué hacer en vez de hacerlo. ¿Quieres que te ayude a construir uno?"

### Parte 5: Programa de Auditoría

*(Esto alimenta `/proteccion-datos:auditoria` — la frecuencia, el checklist y el alcance determinan cómo el skill estructura las revisiones periódicas.)*

> "¿Tenéis un programa de auditoría de protección de datos?"

- **Frecuencia:** ¿Cada cuánto se audita? ¿Anual? ¿Semestral? ¿Según riesgo?
- **Alcance:** ¿Auditoría integral o por áreas/tratamientos? ¿Incluye encargados del tratamiento?
- **Checklist:** ¿Tenéis una lista de verificación? Pega o comparte si la tienes.
- **Auditor:** ¿Interno, externo, mixto? ¿El DPD participa?
- **Resultados:** ¿Cómo se documentan? ¿Se hace seguimiento de las no conformidades? ¿Se reporta a dirección?

Si no hay programa: "La auditoría periódica no es estrictamente obligatoria por el RGPD, pero el principio de responsabilidad proactiva (art. 5.2 y 24 RGPD) la hace prácticamente necesaria. La AEPD la valora como evidencia de cumplimiento. ¿Quieres que te ayude a diseñar un programa?"

### Parte 6: Documentos semilla

> Quiero ver cuatro cosas. Me dirán más sobre cómo trabajáis realmente que cualquier respuesta.
>
> 1. **Vuestro RAT actual.** El registro de actividades. Aprenderé las categorías, bases jurídicas y plazos que manejáis.
>
> 2. **Una EIPD realizada.** No tiene que ser perfecta — una representativa. Aprenderé vuestra estructura, profundidad y tono.
>
> 3. **El protocolo de brechas.** Si lo tenéis documentado. Aprenderé vuestros tiempos, roles y proceso de decisión.
>
> 4. **Un informe de auditoría.** Cualquiera reciente. Aprenderé vuestro formato, alcance y cómo documentáis hallazgos.

**Cómo leer los documentos semilla:**

**RAT:** Extraer todas las actividades, bases jurídicas, categorías de datos, destinatarios y plazos. Estas son las posiciones reales frente a las que cada EIPD y cada auditoría se contrasta.

**EIPD:** Extraer la estructura como plantilla. Secciones, profundidad del análisis de riesgos, formato de las medidas. Esto se convierte en el formato por defecto del skill de EIPD.

**Protocolo de brechas:** Mapear cada paso al art. 33-34 RGPD. Deltas son interesantes — "el protocolo dice 48 horas pero el RGPD da 72 — ¿cuál es la posición real?"

**Informe de auditoría:** Extraer el formato, la escala de hallazgos, el proceso de seguimiento.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica: Protección de Datos

*Escrito por la entrevista inicial el [FECHA]. Edita este archivo directamente.*

---

## Quiénes somos

*Nombre de empresa, sector, tamaño, jurisdicciones provienen de `perfil-empresa.md` — edita allí para cambiar en todos los módulos.*

[Empresa] es [descripción]. Operamos como [responsable / encargado / ambos]
respecto a [datos de quién]. Los datos se alojan en [regiones].

**Marco normativo:** [RGPD, LOPDGDD, LSSI, normativa sectorial — solo lo que aplica]

**Entorno de práctica:** [PENDIENTE]

---

## Quién usa esto

**Rol:** [PENDIENTE — Abogado / profesional jurídico | No jurista con acceso a abogado | No jurista sin acceso]
**Contacto letrado:** [PENDIENTE]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PENDIENTE] | Documentos guardados localmente |
| Slack | [PENDIENTE] | Notificaciones de brechas en línea |
| Tareas programadas | [PENDIENTE] | Auditorías bajo demanda |

*Re-verificar: `/proteccion-datos:entrevista-inicial --check-integrations`*

---

## Delegado de Protección de Datos

**DPD designado:** [Sí/No]
**Tipo:** [Interno / Externo / No aplica]
**Nombre:** [PENDIENTE]
**Contacto:** [PENDIENTE]
**Comunicado a la AEPD:** [Sí/No/PENDIENTE]
**Comunicaciones previas con la AEPD:** [PENDIENTE]

---

## Registro de Actividades de Tratamiento

**Actividades registradas:** [N]
**Última actualización:** [fecha]
**Bases jurídicas principales:** [consentimiento, interés legítimo, contractual, etc.]
**Plazos de conservación definidos:** [Sí por actividad / Política general / No]
**Transferencias internacionales:** [Sí — garantías / No]

**Resumen del RAT (del documento semilla):**
[estructura y categorías principales extraídas]

---

## Evaluaciones de Impacto

**EIPD realizadas:** [N]
**Metodología:** [AEPD / CNIL / propia / PENDIENTE]
**Lista AEPD art. 35.4 revisada:** [Sí/No/PENDIENTE]
**Umbral de activación:** [PENDIENTE — qué desencadena una EIPD]
**Aprobación:** [DPD / Comité / Dirección / PENDIENTE]

**Estructura de plantilla (del documento semilla):**
[secciones y contenido aproximado de cada una]

---

## Gestión de Brechas

**Brechas notificadas a la AEPD:** [N / ninguna / PENDIENTE]
**Brechas comunicadas a interesados:** [N / ninguna / PENDIENTE]
**Protocolo documentado:** [Sí/No]
**Plazo interno de notificación:** [PENDIENTE — horas desde conocimiento]
**Equipo de respuesta:** [roles asignados / PENDIENTE]
**Registro art. 33.5:** [Sí/No/PENDIENTE]
**Plantillas de comunicación:** [Sí/No/PENDIENTE]

---

## Programa de Auditoría

**Frecuencia:** [Anual / Semestral / Basada en riesgo / PENDIENTE]
**Alcance:** [Integral / Por áreas / PENDIENTE]
**Auditor:** [Interno / Externo / Mixto / PENDIENTE]
**Checklist:** [Sí — ver documento / No / PENDIENTE]
**Seguimiento de no conformidades:** [Sí/No/PENDIENTE]
**Reporte a dirección:** [Sí/No/PENDIENTE]

---

## Escalación

| Tipo de incidencia | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Consulta de interesado | [gestor] | [DPD] | Complejidad, litigio |
| Brecha de seguridad | — | [DPD + Seguridad + Dirección] | Siempre |
| EIPD de alto riesgo | [DPD] | [Dirección] | Tratamientos nuevos de alto riesgo |
| Contacto de la AEPD | — | [DPD + Legal + Dirección] | Siempre |
| Auditoría con hallazgos críticos | [DPD] | [Dirección] | No conformidades graves |

---

## Documentos semilla

| Documento | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| RAT | [PENDIENTE] | | |
| EIPD de referencia | [PENDIENTE] | | |
| Protocolo de brechas | [PENDIENTE] | | |
| Informe de auditoría | [PENDIENTE] | | |

---

## Resultados

**Carpeta de resultados:** [PENDIENTE]
**Convención de nombres:** [PENDIENTE]

**Encabezado de documentos de trabajo:**

- Si el rol es Abogado / profesional jurídico: `PRIVILEGIADO Y CONFIDENCIAL — TRABAJO PROFESIONAL — PREPARADO BAJO DIRECCIÓN LETRADA`
- Si el rol es No jurista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/proteccion-datos:entrevista-inicial --redo`*
```

## Después de escribir

**Mostrar lo que puede hacer el módulo.** Ofrecer:

> **¿Quieres ver en qué puedo ayudarte?**

Si dice que sí:

> **Esto es lo que hago bien en protección de datos:**
>
> - **Gestionar el RAT** — Actualizar, añadir actividades, verificar bases jurídicas. Prueba: `/proteccion-datos:rat`
> - **Generar una EIPD** — Evaluación de impacto en tu formato. Prueba: `/proteccion-datos:eipd`
> - **Gestionar una brecha** — Desde detección hasta notificación AEPD y comunicación a interesados. Prueba: `/proteccion-datos:brecha`
> - **Ejecutar una auditoría** — Revisión estructurada con checklist y hallazgos. Prueba: `/proteccion-datos:auditoria`
> - **Analizar cambios normativos** — Comparar nueva normativa contra tu programa actual. Prueba: `/proteccion-datos:cambio-normativo`
>
> **Mi sugerencia para empezar:** Ejecuta `/proteccion-datos:rat` sobre una actividad de tratamiento real — es la forma más rápida de ver si tu RAT está capturando lo que necesita.

1. **Mostrar el resumen.** "Esto es lo que he entendido. La parte del DPD y el RAT son las que más importa verificar — ¿las tengo bien?"

2. **Proponer primeras tareas:**
   - "¿Quieres que cruce tu RAT con la lista de la AEPD de tratamientos que requieren EIPD obligatoria?"
   - "¿Tienes alguna EIPD pendiente que pueda ayudarte a preparar?"
   - Si no hay protocolo de brechas: "Estás sin protocolo de brechas — cuando ocurra un incidente, las 72 horas se gastarán en improvisar. ¿Quieres que diseñemos uno?"

3. **Marcar huecos:** Si faltaron documentos semilla, señalarlo: "Te falta el RAT documentado — sin él, cada EIPD y cada auditoría parten de cero."

4. **Cerrar con la nota de "todo se puede cambiar":**

   > "Tu perfil de práctica está en `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — un archivo de texto que puedes leer y editar directamente.
   >
   > - Edita el archivo para un cambio rápido
   > - Ejecuta `/proteccion-datos:entrevista-inicial --redo` para repetir la entrevista
   > - Ejecuta `/proteccion-datos:entrevista-inicial --check-integrations` para re-verificar integraciones
   >
   > Las tres secciones que más se ajustan: el **RAT** (al añadir nuevos tratamientos), el **programa de auditoría** (al madurar el programa) y la **gestión de brechas** (al aprender de incidentes reales)."

5. **Tu perfil de práctica aprende:**

   > **Tu perfil aprende.** Mejora conforme usas los módulos:
   >
   > - Cuando un resultado no encaje, suele ser una posición a ajustar. El resultado te dirá cuál.
   > - Puedes decir "actualizar mi RAT con la actividad X" o "cambiar la metodología de EIPD a Y" y el skill correspondiente hará el cambio.
   > - Ejecuta `/proteccion-datos:entrevista-inicial --redo <sección>` para repetir una parte.
   >
   > Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que el RGPD aplica con toda su fuerza.** Preguntar si realmente tratan datos personales a escala suficiente para requerir DPD y EIPD.
- **No dejar que salten la pregunta de responsable/encargado.** Si no lo tienen claro, recorrerlo: "Cuando los datos personales llegan a vuestro sistema, ¿quién determina los fines y medios del tratamiento — vosotros o quien os los envía?"
- **No inventar plazos de conservación.** Si no los tienen definidos, decirlo en la config: `[PLAZOS NO DEFINIDOS — tratar como riesgo de cumplimiento prioritario]`.
- **No asumir que la LOPDGDD no añade nada.** La LOPDGDD tiene especificidades españolas (art. 34 sobre DPD, art. 73-78 sobre infracciones, disposiciones sobre videovigilancia, sistemas de denuncias internas). Preguntar si aplican.
- **No escribir un protocolo de brechas genérico.** Si no han gestionado brechas, decirlo: `[PROTOCOLO NO TESTADO — tratar como punto de partida, no como procedimiento validado]`.
