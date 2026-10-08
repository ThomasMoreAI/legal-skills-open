---
name: entrevista-inicial-laboral-2851-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu práctica laboral, la convención colectiva aplicable, tus tipos de contrato, tu proceso de despido y tus políticas internas para que cada documento salga con tu criterio. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/laboral/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: employment
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — ejecutar solo la comprobación de integraciones. Solo reportar ✓ si una llamada MCP realmente respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego las partes específicas).
3. Documentos semilla: contratos tipo, avisos de despido, convención colectiva.
4. Extraer: convención aplicable, tipos de contrato, proceso de despido, políticas internas.
5. Migración: si existe un CLAUDE.md completo en `~/.claude/plugins/cache/claude-para-abogados/laboral/*/CLAUDE.md` pero no en config, copiarlo y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md` (creando directorios padre si es necesario).

---

## Propósito

La práctica laboral panameña está intensamente regulada por el Código de Trabajo y la normativa de MITRADEL y de la CSS. La convención colectiva aplicable (cuando existe) condiciona muchas condiciones — desde los tipos de contrato hasta los plazos de preaviso. Un abogado in-house de una empresa con 500 empleados y sindicato tiene necesidades completamente distintas a las de un despacho que lleva despidos para pymes. Esta entrevista descubre tu contexto real y construye un perfil que refleje tu práctica, no una genérica.

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

> **`laboral` es para quienes trabajan en derecho del trabajo y de la seguridad social — contratación, despidos, negociación colectiva, políticas internas y cumplimiento laboral.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, tipo de práctica, convención colectiva y tipos de contrato habituales, más valores por defecto. **15 minutos** añade tu proceso real de despido, tus plantillas de contrato, tus políticas internas y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica laboral (convención aplicable, tipos de contrato, proceso de despido, políticas internas), plantillas de documentos y calendario de obligaciones laborales. Aprende cómo trabajas tú. Todo se puede cambiar después."
>
> "¿Listo?"

**Perfil profesional nuevo.** Construido desde las respuestas del usuario únicamente.

## Ritmo de la entrevista

- **Asume que la respuesta existe en algún sitio.** Pide enlace o documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas del Código de Trabajo, normativa de MITRADEL y de la CSS, convención colectiva, etc.

---

## La entrevista

### Apertura

> Voy a aprender cómo funciona tu práctica laboral — qué convención aplica, cómo contratas, cómo despides y qué políticas tienes — para que cada aviso, informe o cálculo que haga encaje con tu realidad.

**Ruta rápida:** solo Parte 0 y Parte 1 (contexto laboral). Config con `[POR DEFECTO]`. Cerrar con: "Listo. Valores por defecto para contratación, despido y políticas. Ejecuta `/laboral:entrevista-inicial --completa` cuando quieras."

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién usará este plugin en el día a día?
>
> 1. **Abogado o profesional jurídico** — abogado laboralista idóneo, paralegal.
> 2. **No abogado con acceso a abogado** — RRHH, director de personas, administrador con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: almacenamiento de documentos (Google Drive, SharePoint), herramientas de RRHH y nóminas (Factorial, Personio, SAP SuccessFactors, software de planillas local) y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho pequeño / ejercicio individual**
> - **Despacho mediano / grande**
> - **In-house / departamento de RRHH**
> - **Asesor laboral**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: Contexto laboral (3-4 min)

> ¿Tienes la convención colectiva aplicable en formato digital? Pega el contenido o comparte una ruta — extraeré las categorías, tablas salariales y condiciones clave.

Si no:

- **Convención colectiva aplicable:** ¿aplica alguna? (Nombre completo y ámbito — empresa, sindicato)
- **Número de empleados:** ¿cuántos, aproximadamente?
- **Centros de trabajo:** ¿cuántos y dónde?
- **Representación laboral:** ¿hay sindicato, delegados de los trabajadores?
- **Sectores:** ¿qué actividad principal? (Esto condiciona la convención y la regulación sectorial; ten en cuenta regímenes especiales como Zona Libre de Colón, Ciudad del Saber, Panamá Pacífico o régimen SEM)

---

### Parte 2: Contratación (3-4 min)

> ¿Tienes plantillas de contrato de trabajo que uses habitualmente? Pega el contenido o comparte una ruta.

Si no:

- **Tipos de contrato habituales:** ¿cuáles usas más?
  - Por tiempo indefinido
  - Por tiempo definido
  - Por obra determinada
  - De aprendizaje / formación
  - Otros
- **Cláusulas especiales que incluyes habitualmente:**
  - Pacto de no competencia postcontractual
  - Cláusula de confidencialidad
  - Pacto de dedicación exclusiva
  - Período de prueba: ¿qué duración aplicas según el cargo?
- **Proceso de alta:** ¿quién gestiona la inscripción del trabajador en la CSS? (Interno, gestoría, despacho)

---

### Parte 3: Extinción (4-5 min)

> ¿Tienes un modelo de carta de despido o un proceso interno documentado? Pega o comparte ruta.

Si no:

- **Tipos de despido que manejas habitualmente:**
  - Despido por causa justificada disciplinaria (Código de Trabajo, art. 213, acápite A)
  - Despido por causa económica o de operación de la empresa (Código de Trabajo, art. 213, acápite C)
  - Despido de trabajador con fuero (maternidad, sindical) — requiere autorización judicial previa (Código de Trabajo, arts. 106 y 383)
  - Renuncia / mutuo acuerdo
  - Vencimiento de contrato por tiempo definido o por obra
  - Terminación en período de prueba
- **Proceso interno de despido:**
  - ¿Quién decide? (RRHH, dirección, jurídico)
  - ¿Se solicita autorización previa ante el juzgado o la Junta de Conciliación y Decisión cuando hay fuero?
  - ¿Se notifica o se solicita autorización a MITRADEL cuando aplica?
- **Cálculo de prestaciones:**
  - ¿Cómo calculas la indemnización y la prima de antigüedad? (Herramienta propia, hoja de cálculo, manual)
  - ¿Reconoces el despido injustificado habitualmente? ¿Cuándo?
  - ¿Ofreces acuerdos / transacciones? ¿Proceso habitual?
- **Conciliación administrativa (MITRADEL):**
  - ¿Quién asiste? (Abogado, el propio RRHH, ambos)
  - ¿Posición habitual en la audiencia de conciliación?

---

### Parte 4: Políticas internas (3-4 min)

> ¿Tienes un manual del empleado o handbook? Pega o comparte ruta — extraeré las políticas en vez de preguntarte una a una.

Si no:

- **¿Qué políticas internas tenéis?**
  - Manual del empleado / handbook
  - Reglamento interno de trabajo (aprobado por MITRADEL cuando aplica) [verificar]
  - Protocolo de prevención del hostigamiento y la discriminación (Ley 7 de 2018)
  - Acuerdo de teletrabajo (Ley 126 de 2020)
  - Política de protección de datos del trabajador (Ley 81 de 2019)
  - Política de seguridad y salud en el trabajo / riesgos profesionales
  - Canal de denuncias / whistleblowing
  - Código de conducta
  - Política de uso de herramientas digitales
- **¿Cuáles de estas están actualizadas?** ¿Cuáles necesitan revisión?
- **¿Quién las mantiene?** (RRHH, jurídico, consultoría externa)

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica — nada activo ni confidencial sensible:
>
> - **Contrato de trabajo tipo** (el que más uses)
> - **Aviso de despido** reciente (disciplinario o por causa económica)
> - **Convención colectiva** aplicable (o enlace a la Gaceta Oficial / registro de MITRADEL)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

De los documentos, extraer:
- Formato y estructura de contratos
- Estilo de redacción de avisos de despido
- Categorías y condiciones de la convención

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica laboral
*Escrito por entrevista-inicial el [FECHA].*

### Contexto laboral

**Convención colectiva:** [PLACEHOLDER]
**Empleados:** [PLACEHOLDER]
**Centros de trabajo:** [PLACEHOLDER]
**Representación laboral:** [PLACEHOLDER — sindicato/delegados/ninguna]

### Contratación

| Tipo de contrato | Frecuencia | Cláusulas especiales |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | [no competencia/confidencialidad/etc.] |

**Período de prueba por cargo:**
| Cargo | Duración |
|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] |

### Terminación

**Tipos habituales:** [PLACEHOLDER]
**Proceso interno:** [PLACEHOLDER]
**Reconocimiento de despido injustificado:** [PLACEHOLDER — cuándo y por qué]
**Conciliación (MITRADEL):** [PLACEHOLDER — quién asiste, posición habitual]

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
> - **Redactar un aviso de despido** — disciplinario o por causa económica, con los hechos que me des, en tu formato. Prueba: `/laboral:carta-despido`
> - **Calcular prestaciones** — indemnización por despido injustificado y prima de antigüedad, con antigüedad y salario base. Prueba: `/laboral:calculo-indemnizacion`
> - **Revisar un contrato de trabajo** — verifico que cumple con el Código de Trabajo y la convención aplicable. Prueba: `/laboral:revision-contrato`
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
> Lo que más se ajusta: la convención colectiva (cuando cambia), los tipos de contrato habituales y el proceso de despido."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin:
>
> - Cuando una salida no encaje, suele ser un dato de la convención que ajustar.
> - Puedes decir "actualiza mi convención" o "cambia mi proceso de despido" y el skill escribirá el cambio.
> - Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No asumas convención colectiva.** Pregunta siempre si aplica alguna. La convención puede mejorar muchos mínimos legales.
- **No confundas tipos de despido.** El despido por causa disciplinaria, el despido por causa económica y el despido de trabajador con fuero tienen requisitos, plazos y consecuencias distintos. Cita el Código de Trabajo con [verificar] cuando no estés seguro del artículo.
- **No escribas prestaciones genéricas.** Usa el salario base y la antigüedad reales, no aproximaciones; distingue siempre indemnización por despido injustificado y prima de antigüedad.
- **No inventes artículos del Código de Trabajo ni escalas de cálculo.** Si no estás seguro del número de artículo o de la fórmula vigente, márcalo con [verificar].
- **No pidas documentos semilla si el usuario dijo que no los tiene.** Señala el hueco y sigue.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. No eres un formulario — eres alguien que quiere entender cómo trabaja el otro para poder ayudar de verdad.
