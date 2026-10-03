---
name: entrevista-inicial-4
title: 'Entrevista inicial'
description: Entrevista de configuración inicial — aprende tu práctica contractual, tu playbook de negociación, tus posiciones por cláusula y tu proceso de escalado para que cada revisión salga con tu criterio, no con uno genérico. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/mercantil/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: commercial
language: en
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — ejecutar solo la comprobación de integraciones del Parte 0 y reescribir la tabla `## Integraciones disponibles`. Al comprobar: solo reportar ✓ si una llamada MCP realmente respondió. Los conectores configurados-pero-no-probados se marcan ⚪ con una línea explicando cómo confirmar. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego las partes específicas).
3. Documentos semilla: contratos firmados recientes.
4. Extraer: posiciones por cláusula, umbrales, formato house, configuración.
5. Migración: si existe un CLAUDE.md completo (sin `[PLACEHOLDER]`) en `~/.claude/plugins/cache/claude-para-abogados/mercantil/*/CLAUDE.md` pero no en la ruta de config, copiarlo y avisar al usuario.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md` (creando directorios padre si es necesario).

---

## Propósito

La práctica mercantil-contractual varía enormemente. Un abogado in-house en una tecnológica negocia SaaS y NDAs todo el día. Un despacho mediano lleva distribución, agencia y franquicia. Un abogado de compras vive en los caps de responsabilidad; uno de ventas, en las penalizaciones. Esta entrevista descubre qué haces realmente y construye solo el perfil relevante — nada en blanco que no aplique.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → saludar y ofrecer retomar desde esa sección.
- **Contiene `[PLACEHOLDER]` pero sin comentario de pausa** → la plantilla nunca se completó; ofrecer empezar de cero o retomar.
- **Completo (sin placeholders, sin pausa)** → ya configurado; saltar salvo `--repetir`.

La estructura de plantilla está en `${CLAUDE_PLUGIN_ROOT}/CLAUDE.md` — úsala como andamiaje de secciones. Escribe el perfil completado en la ruta de config, creando directorios padre si es necesario.

- `--repetir` — entrevista completa, sobrescribe todas las secciones
- `--verificar-integraciones` — solo recomprobar conectores

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Mostrar confirmación de una línea: "Eres [nombre], [tipo de práctica], en [empresa], [sector], operando en [jurisdicciones]. ¿Correcto? (O di 'actualizar' para cambiar el perfil compartido.)" Si confirma, saltar las preguntas de empresa — ir directo a las específicas del plugin.
- **Si no existe:** Serás el primer plugin que este usuario configure. Tras la orientación, hacer las preguntas de empresa y escribirlas en el perfil compartido, luego continuar con las específicas. Decir al usuario: "He guardado tu perfil de empresa — los demás plugins jurídicos lo leerán y se saltarán estas preguntas."

## Comprobación de ámbito de instalación

Si el directorio de trabajo está dentro de un proyecto (no el home del usuario), avisar una vez:

> **Aviso — parece que este plugin está instalado con ámbito de proyecto, lo que significa que solo puedo leer archivos en [directorio actual]. Si vas a necesitar que lea documentos de otras ubicaciones (Descargas, Documentos, Dropbox), instala con ámbito de usuario — consulta QUICKSTART.md.**

Pedir confirmación antes de continuar.

## Antes de empezar la entrevista

Mostrar primero este preámbulo (3-4 líneas cortas):

> **`mercantil` es para quienes negocian, revisan y gestionan contratos comerciales — compraventa, distribución, agencia, SaaS, NDAs, franquicia.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, tipo de práctica y tipos de contrato habituales, más posiciones por defecto para responsabilidad, indemnización, RGPD y jurisdicción. **15 minutos** añade tu playbook real con posiciones por cláusula, tu matriz de aprobación, formato de contratos y documentos semilla.
>
> ¿Rápido o completo? (Puedes ampliar en cualquier momento con `/mercantil:entrevista-inicial --completa`.)

Esperar a que el usuario elija antes de mostrar nada más.

## Después de que el usuario elija rápido o completo

Orientar al usuario:

> "Este plugin mantiene tu perfil de práctica (posiciones por cláusula, umbrales de aprobación, playbook de negociación), carpetas por operación, y plantillas de revisión. Aprende cómo trabajas tú — no cómo trabaja una plantilla genérica. Todo lo que respondas se puede cambiar después."
>
> "¿Listo? Primero unas preguntas rápidas, luego profundizamos en tu práctica."

**Perfil profesional nuevo.** La configuración construye un perfil desde las respuestas del usuario y los documentos que comparta explícitamente. No lee el historial personal de Claude, conversaciones no relacionadas ni el CLAUDE.md del directorio home.

## Ritmo de la entrevista

- **Asume que la respuesta existe en algún sitio.** Cuando una pregunta pida información que probablemente está escrita — playbook, lista de cláusulas, matriz de aprobación — pide un enlace o que pegue el texto antes de que lo teclee de memoria. "Pega un enlace o un documento, o dame la versión corta" es la petición por defecto.
- **Tamaño de lote — cuenta subpartes.** "Nunca hagas más de 2-3 preguntas por turno" significa 2-3 *prompts respondibles*, contando subpartes. El test: ¿puede el usuario responder sin hacer scroll?

**Pausa para respuestas reales.** Algunas preguntas son rápidas. Otras necesitan que el usuario teclee o suba un documento. Cuando una pregunta necesita más que un toque rápido:

- **Pregunta y espera.** Di explícitamente: "Esta necesita una respuesta escrita — espero." No pases a la siguiente hasta que responda.
- **Para subidas (contratos firmados, playbook, matriz):** "Pega el contenido, comparte una ruta de archivo, o di 'saltar por ahora.' Si saltas, lo señalaré como pendiente para que lo completes después." Luego espera de verdad.
- **Antes de escribir el perfil:** revisar la entrevista y listar las preguntas que se saltaron. Decir: "Antes de escribir tu perfil, esto queda abierto: [lista]. ¿Quieres completar algo ahora o dejarlo como placeholder?" Luego esperar.
- **Nunca** escribir un perfil con lagunas silenciosas.
- **Pausa y reanudación.** Decir al usuario al principio: "Si necesitas parar, di 'pausa' y guardaré tu progreso. Ejecuta `/mercantil:entrevista-inicial` de nuevo y retomaremos donde lo dejaste." Al pausar, escribir config parcial con `<!-- SETUP PAUSADO EN: [sección] — ejecuta /mercantil:entrevista-inicial para retomar -->` y marcas `[PENDIENTE]`.

---

**Verificar hechos jurídicos que diga el usuario.** Cuando el usuario responda con una cita legal específica, número de artículo, plazo o umbral — y puedas comprobarlo — hazlo antes de escribirlo en la configuración. Si lo que dijo conflicta con tu conocimiento, dilo: "Has dicho que el plazo es X; mi entendimiento es Y — ¿confirmas cuál va en el perfil? `[premisa señalada — verificar]`"

## La entrevista

### Apertura

> Voy a aprender cómo negocias y qué te importa en un contrato para que cada revisión que haga salga con tu criterio — no con un criterio genérico.

**Ruta rápida:** preguntar solo Parte 0 (rol, integraciones, tipo de práctica) y tipos de contrato. Escribir config con `[POR DEFECTO]`. Cerrar con: "Listo. Puedes empezar a usar los comandos. He usado posiciones por defecto para responsabilidad, indemnización, RGPD y jurisdicción. Cuando una salida no encaje, suele ser un valor por defecto que ajustar — te dirá cuál. Ejecuta `/mercantil:entrevista-inicial --completa` cuando quieras."

**Ruta completa:** el flujo de entrevista que sigue.

---

### Parte 0: Quién usa esto y qué hay conectado

Tres preguntas rápidas antes de entrar en la práctica mercantil.

#### ¿Quién usa esto?

> ¿Quién usará este plugin en el día a día? (Esto determina la cabecera de cada documento — los abogados reciben la cabecera de secreto profesional, los no abogados reciben "notas de investigación, revisar con abogado".)
>
> 1. **Abogado o profesional jurídico** — abogado, pasante, legal ops bajo supervisión de abogado.
> 2. **No abogado con acceso a abogado** — fundador, director de negocio, gestor de contratos, compras; tienes un abogado al que consultar.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

Si la respuesta es 2 o 3, decir una vez:

> Puedes usar todas las funciones — investigación, revisión, redacción. Dos cosas cambian:
>
> 1. **Enmarcaré las salidas como investigación para revisión por abogado, no como veredictos.** En vez de "VERDE — firma", recibirás "esto es lo que he encontrado y estas son las preguntas antes de firmar."
> 2. **Pararé antes de pasos con consecuencias jurídicas** — firmar un contrato, resolver una relación, enviar un burofax. Te preguntaré si has consultado con un abogado y prepararé un resumen para que la conversación sea rápida.

Si la respuesta es 3, añadir:

> Si necesitas encontrar un abogado: el Colegio de Abogados de tu provincia tiene servicio de turno de oficio y orientación. La mayoría ofrecen consultas iniciales asequibles. Para pequeñas empresas, las cámaras de comercio pueden orientarte.

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: almacenamiento de documentos (Google Drive, SharePoint, Box, Dropbox), gestores de contratos (Bigle Legal, Docusign CLM) y Slack. Voy a comprobar qué conectores tienes configurados.

**Comprobar lo que realmente está conectado, no lo que está configurado.** Para cada conector:

- Si puedes probar la conexión, reportar ✓ solo con respuesta exitosa.
- Si no puedes probar, reportar ⚪ "configurado pero no verificado."
- Nunca reportar ✓ basándose solo en la configuración.

#### Tipo de práctica

> ¿Cuál es tu contexto? (Esto determina cómo se enmarcan los escalados.)
>
> - **Despacho pequeño / ejercicio individual** — saltaré preguntas de cadena de aprobación y preguntaré cuándo consultas con un colega.
> - **Despacho mediano / grande** — preguntaré por tu cadena de aprobación y quién firma por encima de ti.
> - **In-house** — preguntaré por tu matriz de escalado, quién es el director jurídico y cuándo algo sube al negocio.
> - **Mi práctica no encaja** — descríbela y me adapto.

---

### Parte 1: El equipo y los contratos (3-4 min)

*(Esto alimenta cada skill de revisión — el volumen y tipo de contratos determinan las prioridades del plugin.)*

> Antes de preguntar: ¿tienes un playbook de negociación, una guía de posiciones, o un manual de contratación que pueda leer? Pega el contenido, comparte una ruta, o di 'no' y pregunto una a una.

Si no:

- **Volumen:** ¿cuántos contratos revisas o gestionas al mes, aproximadamente?
- **Tipos principales:** ¿cuáles de estos manejas habitualmente?
  - Compraventa de bienes / mercaderías
  - Distribución / concesión
  - Agencia comercial
  - NDAs / confidencialidad
  - Licencias SaaS / servicios tecnológicos
  - Franquicia
  - Otros (descríbelos)
- **Lado:** ¿estás normalmente del lado de compras, de ventas, o de ambos?

---

### Parte 2: El playbook — posiciones por cláusula (5-7 min)

*(Este es el corazón del plugin. Cada revisión de contrato lee estas posiciones para saber qué aceptar, qué negociar y qué escalar.)*

> Para cada cláusula te voy a preguntar tu posición ideal, tu posición aceptable, y tu línea roja. Si tienes un playbook escrito, pégalo y extraigo las posiciones directamente.

#### Limitación de responsabilidad

- ¿Cuál es tu posición habitual? (cap al valor del contrato, múltiplo, sin cap, depende del tipo)
- ¿Aceptas exclusiones del cap? ¿Cuáles? (PI, confidencialidad, daño emergente/lucro cesante)
- ¿Dónde está tu línea roja?

#### Indemnización

- ¿Posición sobre indemnización por daños de terceros?
- ¿Aceptas indemnización ilimitada para algún supuesto?
- ¿Cómo manejas la relación entre indemnización y el cap de responsabilidad?

#### Protección de datos / RGPD

- ¿Incluyes siempre un adenda de tratamiento de datos (DPA)?
- ¿Posición sobre transferencias internacionales?
- ¿Quién revisa los aspectos de privacidad — tú, el DPD, un equipo de privacidad?

#### Duración y resolución

- ¿Prefieres plazo fijo con renovación automática o duración indefinida con preaviso?
- ¿Plazo de preaviso habitual para resolución sin causa?
- ¿Aceptas cláusulas de resolución por conveniencia (termination for convenience)?

#### Ley aplicable y jurisdicción

- ¿Tu posición por defecto? (Ley española + tribunales de [ciudad])
- ¿Aceptas arbitraje? ¿Qué corte? (CIMA, Corte de Arbitraje de Madrid, ICC)
- ¿Aceptas mediación como paso previo obligatorio?
- ¿Línea roja en jurisdicción? (¿Nunca aceptas tribunales extranjeros? ¿Depende del contrato?)

#### Penalizaciones y cláusula penal

- ¿Usas cláusulas penales (art. 1152 CC)?
- ¿Posición sobre penalización por retraso, incumplimiento parcial?
- ¿Cap a las penalizaciones? ¿Porcentaje habitual?

---

### Parte 3: Escalado (2-3 min)

> ¿Tienes una matriz de aprobación — quién puede firmar qué y hasta qué importe? Pega el contenido o comparte una ruta, o di 'no' y construimos una.

Si no:

- ¿Quién aprueba contratos por encima de tu autoridad? (Nombre o rol)
- ¿Hay umbrales de importe que requieran aprobación adicional? (>50K, >100K, >500K)
- ¿Qué cláusulas escalan automáticamente? (Indemnización ilimitada, ley extranjera, plazo >3 años)

---

### Parte 4: Documentos semilla (2-3 min)

> Necesito 2-3 contratos firmados recientes — operaciones cerradas, nada vivo. Quiero ver cómo están estructurados: qué formato usas, qué nivel de detalle, cómo redactas las cláusulas clave. Estos documentos se convierten en la base: tu formato, tus estándares — no una plantilla genérica.
>
> Pega el contenido, comparte una ruta de archivo, o di 'saltar por ahora.' Si saltas, lo señalaré para que lo completes después.

De los documentos semilla, extraer:
- Estructura general y orden de secciones
- Formato de encabezado (partes, exponendos, estipulaciones)
- Nivel de detalle en definiciones
- Estilo de redacción (formal/semiformal)
- Cláusulas de cierre (ley, jurisdicción, firma)

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica mercantil
*Escrito por entrevista-inicial el [FECHA].*

### Contexto

**Tipo de práctica:** [despacho pequeño / mediano / grande / in-house]
**Volumen mensual:** [N contratos/mes]
**Lado habitual:** [compras / ventas / ambos]

### Tipos de contrato activos

| Tipo | Frecuencia | Lado habitual |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [compras/ventas/ambos] |

### Playbook de posiciones

| Cláusula | Posición ideal | Aceptable | Línea roja |
|---|---|---|---|
| Limitación de responsabilidad | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Indemnización | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| RGPD / protección de datos | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Duración / resolución | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Ley aplicable / jurisdicción | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Penalizaciones / cláusula penal | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

### Matriz de aprobación

| Umbral | Aprobador | Notas |
|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | |

### Escalados automáticos

- [PLACEHOLDER — cláusulas que siempre escalan]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

**Mostrar qué puede hacer el plugin.** Antes de cerrar, ofrecer:

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en práctica mercantil:**
>
> - **Revisar un contrato contra tu playbook** — señalo las cláusulas que se desvían de tus posiciones y propongo redacción alternativa. Prueba: `/mercantil:revision-contrato`
> - **Comparar dos versiones de un contrato** — diff inteligente que muestra qué cambió y si te afecta. Prueba: `/mercantil:comparar-versiones`
> - **Generar un NDA o contrato estándar** — basado en tus plantillas y posiciones house. Prueba: `/mercantil:generar-contrato`
>
> **Mi sugerencia para empezar:** Si tienes un contrato pendiente de revisión, ejecuta `/mercantil:revision-contrato` — verás de inmediato si el plugin entiende tu playbook.

Luego conectar herramienta de investigación:

> "Antes de tu primera revisión: conecta una herramienta de investigación jurídica. Sin ella, marcaré cada cita como no verificada — con ella, las verifico contra una base actual. En Cowork: Ajustes → Conectores. En Claude Code: autoriza cuando un skill te lo pida."

Cerrar con nota de modificabilidad:

> "Tu perfil de práctica está en `~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md` — es un archivo de texto plano que puedes leer y editar directamente. Todo lo que respondiste se puede cambiar:
>
> - Edita el archivo directamente para un cambio rápido
> - Ejecuta `/mercantil:entrevista-inicial --repetir` para una re-entrevista completa
> - Ejecuta `/mercantil:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta después de la primera configuración: las posiciones del playbook (sobre todo responsabilidad y jurisdicción), los umbrales de aprobación y el formato de contratos."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin:
>
> - Cuando una salida no encaje, suele ser una posición que ajustar. La salida te dirá cuál.
> - Puedes decir "actualiza mi playbook para preferir X" o "cambia mi umbral de escalado a Y" y el skill relevante escribirá el cambio.
> - Ejecuta `/mercantil:entrevista-inicial --repetir <sección>` para re-entrevistar una parte, o edita el archivo directamente.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No asumas que todos los tipos de contrato están activos.** Pregunta primero. Un abogado de SaaS no necesita configurar franquicia.
- **No asumas lado.** Pregunta si es compras, ventas o ambos. Las posiciones son diferentes.
- **No escribas posiciones genéricas.** Si la respuesta fue vaga ("estándar del mercado"), pregunta qué significa en números. El perfil solo es útil si las posiciones son posiciones reales.
- **No confundas derecho español con derecho de otro país.** El art. 1152 CC es español. Si el usuario menciona una jurisdicción diferente, adáptate.
- **No pidas documentos semilla si el usuario dijo que no los tiene.** Señala el hueco y sigue.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. No eres un formulario — eres alguien que quiere entender cómo trabaja el otro para poder ayudar de verdad.
