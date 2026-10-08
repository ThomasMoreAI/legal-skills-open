---
name: entrevista-inicial-laboral-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu práctica laboral, el convenio colectivo aplicable, tus tipos de contrato, tu proceso de despido y tus políticas internas para que cada documento salga con tu criterio. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/laboral/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — ejecutar solo la comprobación de integraciones. Solo reportar ✓ si una llamada MCP realmente respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego las partes específicas).
3. Documentos semilla: contratos tipo, cartas de despido, convenio colectivo.
4. Extraer: convenio aplicable, tipos de contrato, proceso de despido, políticas internas.
5. Migración: si existe un CLAUDE.md completo en `~/.claude/plugins/cache/claude-para-abogados/laboral/*/CLAUDE.md` pero no en config, copiarlo y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md` (creando directorios padre si es necesario).

---

## Propósito

La práctica laboral española es intensamente regulada y cambiante. El convenio colectivo aplicable condiciona casi todo — desde los tipos de contrato hasta los plazos de preaviso y las cuantías de indemnización. Un abogado in-house de una empresa con 500 empleados y comité de empresa tiene necesidades completamente distintas a las de un despacho que lleva despidos para pymes. Esta entrevista descubre tu contexto real y construye un perfil que refleje tu práctica, no una genérica.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → saludar y ofrecer retomar.
- **Contiene `[PLACEHOLDER]` pero sin pausa** → ofrecer empezar o retomar.
- **Completo** → ya configurado; saltar salvo `--repetir`.

- `--repetir` — entrevista completa
- `--verificar-integraciones` — solo recomprobar conectores

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, confirmar y saltar preguntas de empresa. Si no, hacerlas y escribir el perfil compartido.

## Comprobación de ámbito de instalación

Avisar si el directorio de trabajo es de proyecto (no home).

## Antes de empezar la entrevista

> **`laboral` es para quienes trabajan en derecho del trabajo y de la Seguridad Social — contratación, despidos, negociación colectiva, políticas internas y cumplimiento laboral.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, tipo de práctica, convenio colectivo y tipos de contrato habituales, más valores por defecto. **15 minutos** añade tu proceso real de despido, tus plantillas de contrato, tus políticas internas y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica laboral (convenio aplicable, tipos de contrato, proceso de despido, políticas internas), plantillas de documentos y calendario de obligaciones laborales. Aprende cómo trabajas tú. Todo se puede cambiar después."
>
> "¿Listo?"

**Perfil profesional nuevo.** Construido desde las respuestas del usuario únicamente.

## Ritmo de la entrevista

- **Asume que la respuesta existe en algún sitio.** Pide enlace o documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas del ET, LRJS, convenio colectivo, etc.

---

## La entrevista

### Apertura

> Voy a aprender cómo funciona tu práctica laboral — qué convenio aplica, cómo contratas, cómo despides y qué políticas tienes — para que cada carta, informe o cálculo que haga encaje con tu realidad.

**Ruta rápida:** solo Parte 0 y Parte 1 (contexto laboral). Config con `[POR DEFECTO]`. Cerrar con: "Listo. Valores por defecto para contratación, despido y políticas. Ejecuta `/laboral:entrevista-inicial --completa` cuando quieras."

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién usará este plugin en el día a día?
>
> 1. **Abogado o profesional jurídico** — abogado laboralista, graduado social, paralegal.
> 2. **No abogado con acceso a abogado** — RRHH, director de personas, administrador con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: almacenamiento de documentos (Google Drive, SharePoint), herramientas de RRHH (Factorial, Personio, SAP SuccessFactors), nóminas (A3nom, Sage) y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho pequeño / ejercicio individual**
> - **Despacho mediano / grande**
> - **In-house / departamento de RRHH**
> - **Graduado social**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Contexto laboral (3-4 min)

> ¿Tienes el convenio colectivo aplicable en formato digital? Pega el contenido o comparte una ruta — extraeré las categorías, tablas salariales y condiciones clave.

Si no:

- **Convenio colectivo aplicable:** ¿cuál aplica? (Nombre completo y ámbito — sectorial, empresa, grupo)
- **Número de empleados:** ¿cuántos, aproximadamente?
- **Centros de trabajo:** ¿cuántos y dónde?
- **Representación laboral:** ¿hay comité de empresa, delegados de personal, sección sindical?
- **Sectores:** ¿qué actividad principal? (Esto condiciona el convenio y la regulación sectorial)

---

### Parte 2: Contratación (3-4 min)

> ¿Tienes plantillas de contrato de trabajo que uses habitualmente? Pega el contenido o comparte una ruta.

Si no:

- **Tipos de contrato habituales:** ¿cuáles usas más?
  - Indefinido ordinario
  - Indefinido fijo-discontinuo
  - Temporal por circunstancias de la producción (art. 15.2 ET)
  - Temporal por sustitución
  - Formativo (art. 11 ET) — en alternancia o para práctica profesional
  - Otros
- **Cláusulas especiales que incluyes habitualmente:**
  - Pacto de no competencia postcontractual (art. 21.2 ET)
  - Pacto de permanencia (art. 21.4 ET)
  - Cláusula de confidencialidad
  - Pacto de dedicación exclusiva
  - Periodo de prueba: ¿qué duración aplicas según categoría?
- **Proceso de alta:** ¿quién gestiona el alta en Seguridad Social? (Interno, gestoría, despacho)

---

### Parte 3: Extinción (4-5 min)

> ¿Tienes un modelo de carta de despido o un proceso interno documentado? Pega o comparte ruta.

Si no:

- **Tipos de despido que manejas habitualmente:**
  - Despido disciplinario (art. 54 ET)
  - Despido objetivo individual (art. 52 ET) — causas económicas, técnicas, organizativas, productivas
  - Despido colectivo / ERE (art. 51 ET)
  - Extinción por voluntad del trabajador (art. 50 ET)
  - No renovación de temporales
  - Desistimiento en periodo de prueba
- **Proceso interno de despido:**
  - ¿Quién decide? (RRHH, dirección, jurídico)
  - ¿Hay expediente contradictorio previo para representantes?
  - ¿Audiencia previa al delegado sindical?
- **Cálculo de indemnizaciones:**
  - ¿Cómo calculas? (Herramienta propia, hoja de cálculo, manual)
  - ¿Reconoces improcedencia habitualmente? ¿Cuándo?
  - ¿Ofreces acuerdos transaccionales? ¿Proceso habitual?
- **Conciliación previa (SMAC/CMAC):**
  - ¿Quién asiste? (Abogado, el propio RRHH, ambos)
  - ¿Posición habitual en acto de conciliación?

---

### Parte 4: Políticas internas (3-4 min)

> ¿Tienes un manual del empleado o handbook? Pega o comparte ruta — extraeré las políticas en vez de preguntarte una a una.

Si no:

- **¿Qué políticas internas tenéis?**
  - Manual del empleado / handbook
  - Protocolo de prevención del acoso (obligatorio)
  - Política de desconexión digital (art. 88 LOPDGDD)
  - Acuerdo de teletrabajo (Ley 10/2021)
  - Plan de igualdad (obligatorio >50 empleados)
  - Registro retributivo
  - Canal de denuncias / whistleblowing (Ley 2/2023)
  - Código de conducta
  - Política de uso de herramientas digitales
- **¿Cuáles de estas están actualizadas?** ¿Cuáles necesitan revisión?
- **¿Quién las mantiene?** (RRHH, jurídico, consultoría externa)

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica — nada activo ni confidencial sensible:
>
> - **Contrato de trabajo tipo** (el que más uses)
> - **Carta de despido** reciente (disciplinario u objetivo)
> - **Convenio colectivo** aplicable (o enlace al BOE/BORM/etc.)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

De los documentos, extraer:
- Formato y estructura de contratos
- Estilo de redacción de cartas de despido
- Categorías y condiciones del convenio

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica laboral
*Escrito por entrevista-inicial el [FECHA].*

### Contexto laboral

**Convenio colectivo:** [PLACEHOLDER]
**Empleados:** [PLACEHOLDER]
**Centros de trabajo:** [PLACEHOLDER]
**Representación laboral:** [PLACEHOLDER — comité/delegados/sección sindical/ninguna]

### Contratación

| Tipo de contrato | Frecuencia | Cláusulas especiales |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [no competencia/permanencia/etc.] |

**Periodo de prueba por categoría:**
| Categoría | Duración |
|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] |

### Extinción

**Tipos habituales:** [PLACEHOLDER]
**Proceso interno:** [PLACEHOLDER]
**Reconocimiento de improcedencia:** [PLACEHOLDER — cuándo y por qué]
**Conciliación:** [PLACEHOLDER — quién asiste, posición habitual]

### Políticas internas

| Política | Estado | Responsable | Última actualización |
|---|---|---|---|
| [PLACEHOLDER] | [vigente/pendiente/inexistente] | [PLACEHOLDER] | [PLACEHOLDER] |

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en práctica laboral:**
>
> - **Redactar una carta de despido** — disciplinario u objetivo, con los hechos que me des, en tu formato. Prueba: `/laboral:carta-despido`
> - **Calcular indemnizaciones** — por despido improcedente, objetivo, ERE, con antigüedad y salario regulador. Prueba: `/laboral:calculo-indemnizacion`
> - **Revisar un contrato de trabajo** — verifico que cumple con el ET y el convenio aplicable. Prueba: `/laboral:revision-contrato`
> - **Auditar políticas internas** — reviso si las políticas obligatorias están al día. Prueba: `/laboral:auditoria-politicas`
>
> **Mi sugerencia para empezar:** Si tienes un despido pendiente, ejecuta `/laboral:carta-despido` — verás si entiende tu proceso.

Conectar herramienta de investigación:

> "Antes de tu primer documento: conecta una herramienta de investigación jurídica."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/laboral:entrevista-inicial --repetir` para re-entrevista completa
> - `/laboral:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: el convenio colectivo (cuando cambia), los tipos de contrato habituales y el proceso de despido."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin:
>
> - Cuando una salida no encaje, suele ser un dato del convenio que ajustar.
> - Puedes decir "actualiza mi convenio" o "cambia mi proceso de despido" y el skill escribirá el cambio.
> - Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No asumas convenio colectivo.** Pregunta siempre cuál aplica. El convenio condiciona casi todo.
- **No confundas tipos de despido.** Disciplinario (art. 54), objetivo (art. 52) y colectivo (art. 51) tienen requisitos, plazos e indemnizaciones distintos.
- **No escribas indemnizaciones genéricas.** Usa el salario regulador y la antigüedad reales, no aproximaciones.
- **No olvides la reforma laboral de 2022.** Los contratos temporales cambiaron sustancialmente. Verifica que la información del usuario está actualizada.
- **No pidas documentos semilla si el usuario dijo que no los tiene.** Señala el hueco y sigue.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. No eres un formulario — eres alguien que quiere entender cómo trabaja el otro para poder ayudar de verdad.
