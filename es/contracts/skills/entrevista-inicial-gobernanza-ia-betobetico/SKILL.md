---
name: entrevista-inicial-gobernanza-ia-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin de gobernanza de IA. Aprende tu práctica y escribe CLAUDE.md a partir de tu inventario de sistemas IA, clasificación de riesgo y contratos con proveedores. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin de IA", "onboarding gobernanza IA", o quiere re-ejecutar la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/gobernanza-ia/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: registro de sistemas IA, política de uso de IA, contrato con proveedor de IA. Leer todos.
4. Extraer: sistemas desplegados, clasificación de riesgo, posiciones contractuales, política de IA generativa.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones disponibles y actualiza `## Integraciones disponibles` en la configuración. No re-entrevista.

```
/gobernanza-ia:entrevista-inicial
```

```
/gobernanza-ia:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Gobernanza de IA

## Propósito

Aprender cómo *esta* organización gestiona la IA — qué sistemas tiene desplegados, cómo los clasifica, qué exige a los proveedores, qué política interna aplica a la IA generativa. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

El Reglamento Europeo de Inteligencia Artificial (AI Act, Reglamento (UE) 2024/1689) cambia radicalmente las obligaciones de las organizaciones. Pero la gobernanza real varía enormemente: una empresa que solo usa ChatGPT para marketing tiene poco en común con una que despliega modelos de scoring crediticio. La entrevista identifica cuál es esta antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar desde esa sección.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar los datos de empresa, escribirlos en el perfil compartido y continuar con las específicas del plugin.

## Antes de empezar la entrevista

> **`gobernanza-ia` es para quien gestiona la conformidad con el AI Act, la política interna de IA, la revisión de contratos con proveedores de IA y el registro de sistemas.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan los sistemas IA principales y la clasificación de riesgo básica, con valores sensatos en todo lo demás. **15 minutos** añade tu inventario completo, posiciones contractuales con proveedores, política de IA generativa y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de gobernanza de IA (inventario de sistemas, clasificaciones de riesgo, posiciones con proveedores, política interna), un registro de sistemas y evaluaciones de conformidad. Esta entrevista aprende cómo gestionas la IA realmente — tus sistemas, tus proveedores, tus políticas — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "La configuración se construye desde tus respuestas y documentos semilla. No lee tu historial personal."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1 (sistemas principales). Escribir con `[DEFAULT]` en lo demás.

**Ruta completa:** el flujo completo descrito abajo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos antes que descripciones.** "Tienes un inventario de sistemas IA? Pégalo o comparte ruta."
- **Pausa y reanudación.** Decir al inicio: "Si necesitas parar, di 'pausa' y guardaré tu progreso." Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo del AI Act o un plazo, comprobar antes de escribirlo.

## La entrevista

### Apertura

> Voy a ayudarte con la gobernanza de IA: clasificación de riesgo, registro de sistemas, revisión de contratos con proveedores de IA y política interna. Antes de nada, necesito saber cómo usáis la IA en vuestra organización. Diez minutos.
>
> Después te pediré tres cosas: vuestro registro de sistemas IA (o una lista informal), vuestra política de uso de IA (si existe), y un contrato con un proveedor de IA.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a o profesional jurídico** — letrado/a, responsable de cumplimiento, DPO con funciones de gobernanza IA.
> 2. **Profesional no jurídico con acceso a letrado** — CTO, responsable de innovación, data scientist que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — gestionas la gobernanza de IA por tu cuenta.

Si la respuesta es 2 o 3, explicar una vez: los outputs serán investigación para revisión letrada.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector con una llamada real. Reportar resultados.

### Parte 1: Uso de IA en la organización (3-4 min)

> **Qué sistemas de IA utiliza tu organización actualmente?** Este es el inventario base — todo lo demás depende de él.
>
> Para cada sistema que menciones necesito saber:
> 1. **Nombre y proveedor** (ej. "GPT-4 de OpenAI", "modelo propio de scoring", "Copilot de Microsoft")
> 2. **Estado** (en producción, en desarrollo, en fase de pruebas, descartado)
> 3. **Uso** (para qué se usa — clasificación de documentos, atención al cliente, decisiones automatizadas, generación de contenido, etc.)
> 4. **Datos que procesa** (datos personales, datos financieros, datos de salud, datos públicos, etc.)
> 5. **Quién lo usa** (departamento, número de usuarios)
>
> Si tenéis un inventario o registro formal, pégalo o comparte ruta — es mucho más rápido.

Pausa. Después:

> **Estáis desarrollando algún sistema de IA internamente?** Modelos propios, fine-tuning de modelos base, pipelines de ML en producción?

### Parte 2: Clasificación de riesgo (2-3 min)

> **Habéis clasificado vuestros sistemas según las categorías del AI Act?** El Reglamento (UE) 2024/1689 establece cuatro niveles: riesgo inaceptable (art. 5), alto riesgo (Anexo III), riesgo limitado (art. 50, obligaciones de transparencia) y riesgo mínimo.
>
> Para cada sistema que mencionaste:
> - Está clasificado? Quién hizo la clasificación?
> - Alguno cae en la categoría de alto riesgo del Anexo III? (ej. sistemas de scoring crediticio, selección de personal, identificación biométrica, evaluación educativa)
> - Alguno podría considerarse de riesgo inaceptable? (ej. scoring social, manipulación subliminal, explotación de vulnerabilidades)
>
> Tenéis un registro interno de clasificaciones? Es obligatorio para sistemas de alto riesgo (art. 49).

Pausa. Después:

> **Qué criterios internos usáis para decidir si un nuevo uso de IA necesita evaluación?** Tenéis un proceso de aprobación para nuevos despliegues de IA, o cada equipo decide por su cuenta?

### Parte 3: Proveedores de IA (2-3 min)

> **Cómo gestionáis la relación contractual con proveedores de IA?** Esto alimenta el skill de revisión de contratos.
>
> Me interesa saber:
> 1. **Quiénes son los proveedores principales** (OpenAI, Microsoft, Google, Amazon, proveedores nicho, etc.)
> 2. **Qué cláusulas son clave en vuestros contratos** — hay alguna que sea línea roja?
>    - Propiedad de los outputs
>    - Uso de datos para entrenamiento del modelo
>    - Garantías de conformidad con AI Act
>    - Auditoría y transparencia
>    - Localización de datos (dentro/fuera de la UE)
>    - Responsabilidad por outputs incorrectos o sesgados
> 3. **Proceso de revisión** — quién aprueba la contratación de un nuevo proveedor de IA? Hay un proceso formal o es ad hoc?
>
> Si tenéis un contrato tipo o un checklist de revisión, pégalo o comparte ruta.

### Parte 4: Política interna de IA generativa (2 min)

> **Tiene tu organización una política interna sobre el uso de IA generativa?** (ChatGPT, Copilot, Claude, Gemini, Midjourney, etc.)
>
> Si existe:
> - Qué cubre? (uso permitido, prohibido, condicionado)
> - Quién la aprobó? Cuándo fue la última actualización?
> - Se aplica a toda la organización o solo a ciertos departamentos?
> - Contempla: confidencialidad de datos introducidos, propiedad intelectual de outputs, verificación humana de resultados?
>
> Si no existe:
> - Hay alguna directriz informal o comunicación interna sobre el uso de IA generativa?
> - Quién debería aprobar una política así? (Dirección, comité de cumplimiento, CTO, etc.)
>
> Pega la política si la tienes, o dame la versión corta.

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas. Me dirán más que cualquier cosa que me cuentes:
>
> 1. **Registro de sistemas IA** — el inventario formal o informal de los sistemas de IA que usáis. Si no existe como documento, la lista que me diste antes sirve de base.
>
> 2. **Política de uso de IA** — la política interna sobre uso de IA generativa o IA en general, si existe. Me enseña qué habéis decidido como organización.
>
> 3. **Un contrato con un proveedor de IA** — el más representativo. Aprenderé vuestras posiciones contractuales reales, no las declaradas.

**Cómo leer los documentos semilla:**

**Registro de sistemas:** Extraer cada sistema, su clasificación de riesgo, su estado y los datos que procesa. Comparar con lo declarado en la entrevista.

**Política de uso:** Mapear las restricciones y permisos. Identificar lagunas respecto al AI Act.

**Contrato con proveedor:** Extraer las cláusulas clave. Identificar deltas con las posiciones declaradas — "dijiste que exigís que no usen datos para entrenamiento, pero el contrato con [proveedor] no tiene esa cláusula."

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Gobernanza de IA

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa] es una [tipo de entidad]. Usamos IA en [áreas principales].
El equipo de gobernanza IA cuenta con [N] personas. [Responsable: nombre o ninguno].
La escalación va a [nombre].

**Madurez en gobernanza IA:** [incipiente / en desarrollo / formalizada]
**Asuntos abiertos:** [ninguno / lista]

---

## Quién usa este plugin

**Rol:** [Abogado/a | Profesional con acceso a letrado | Profesional sin acceso a letrado]
**Contacto letrado:** [Nombre / equipo / despacho externo / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Barrido bajo demanda |

---

## Inventario de sistemas IA

| Sistema | Proveedor | Estado | Uso | Datos | Clasificación riesgo AI Act | Usuarios |
|---|---|---|---|---|---|---|
| [nombre] | [proveedor] | [producción/desarrollo/pruebas] | [uso] | [tipo datos] | [inaceptable/alto/limitado/mínimo/sin clasificar] | [depto] |

---

## Clasificación de riesgo

**Proceso de clasificación:** [quién clasifica, con qué criterios, frecuencia de revisión]
**Sistemas de alto riesgo (Anexo III):** [lista o ninguno]
**Registro en BD UE (art. 49):** [registrado / pendiente / no aplica]
**Criterios internos para evaluación de nuevos usos:** [descripción del proceso]

---

## Proveedores de IA — Posiciones contractuales

| Cláusula | Exigimos | Aceptable | Nunca aceptamos |
|---|---|---|---|
| Propiedad de outputs | [posición] | [fallback] | [línea roja] |
| Uso de datos para entrenamiento | [posición] | [fallback] | [línea roja] |
| Conformidad AI Act | [posición] | [fallback] | [línea roja] |
| Auditoría y transparencia | [posición] | [fallback] | [línea roja] |
| Localización de datos | [posición] | [fallback] | [línea roja] |
| Responsabilidad por outputs | [posición] | [fallback] | [línea roja] |

**Proceso de aprobación de nuevos proveedores:** [descripción]

---

## Política interna de IA generativa

**Estado:** [aprobada / borrador / informal / no existe]
**Alcance:** [toda la organización / departamentos específicos]
**Última actualización:** [fecha]
**Aprobada por:** [quién]

**Usos permitidos:** [lista]
**Usos prohibidos:** [lista]
**Usos condicionados:** [lista con condiciones]
**Reglas de confidencialidad:** [qué datos no pueden introducirse en herramientas de IA]
**Propiedad intelectual:** [posición sobre PI de outputs generados por IA]
**Verificación humana:** [cuándo se exige revisión humana de outputs de IA]

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Nuevo uso de IA (riesgo mínimo) | [responsable] | [nombre] | Si implica datos personales |
| Nuevo uso de IA (alto riesgo) | — | [GC + cumplimiento] | Siempre |
| Incidente con sistema IA | — | [GC + CTO + dirección] | Siempre |
| Nuevo proveedor de IA | [responsable] | [nombre] | Contrato > [umbral] |
| Requerimiento regulador sobre IA | — | [GC + dirección] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Registro de sistemas IA | [ruta] | [fecha] | |
| Política de uso de IA | [ruta] | [fecha] | |
| Contrato proveedor de IA | [ruta] | [fecha] | [proveedor] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/gobernanza-ia:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. El inventario de sistemas y la clasificación de riesgo son las partes a revisar con más cuidado — un sistema mal clasificado propaga errores a todos los outputs."

2. **Proponer primeras tareas:**
   - "Quieres que clasifique un sistema de IA concreto según el AI Act?"
   - "Quieres que revise un contrato con un proveedor de IA contra tus posiciones?"
   - "Quieres que analice los gaps de tu política de IA generativa respecto al AI Act?"
   - Si no hay registro formal: "Quieres que construya un registro de sistemas IA a partir de lo que me has contado?"

3. **Señalar huecos.** Si no hay registro formal de sistemas: "Estáis operando sin un registro formal de sistemas IA. El AI Act lo exige para sistemas de alto riesgo (art. 49). Quieres que te ayude a construir uno?"

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/gobernanza-ia:entrevista-inicial --redo` para re-entrevista completa
   > - `/gobernanza-ia:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: el **inventario de sistemas** (cada vez que desplegáis algo nuevo), las **posiciones con proveedores** (según negociáis más contratos), y la **política de IA generativa** (campo que evoluciona muy rápido)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Cuando un resultado no encaje, normalmente es una posición que ajustar. Un mes de uso te da un perfil que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que el AI Act aplica a todo.** Muchos usos de IA son de riesgo mínimo y no generan obligaciones específicas. No inflar artificialmente la clasificación de riesgo.
- **No confundir "deployer" con "provider" en terminología AI Act.** La mayoría de organizaciones son "deployers" (implantadores), no "providers" (proveedores). Las obligaciones son distintas.
- **No dar por hecho que existe una política de IA generativa.** La mayoría de organizaciones en España todavía no la tienen formalizada. Si no existe, señalarlo como gap pero no bloquearse.
- **No escribir posiciones contractuales genéricas.** Si el equipo no ha negociado muchos contratos con proveedores de IA, decirlo: `[POSICIONES NO CONSOLIDADAS — este equipo tiene poca experiencia negociando contratos de IA. Tratar como puntos de partida.]`
- **No olvidar la dimensión de protección de datos.** Gobernanza de IA y protección de datos se solapan (EIPD, base legal para tratamiento automatizado). Preguntar si el DPO está implicado en gobernanza IA.
- **No ignorar los plazos del AI Act.** Las obligaciones entran en vigor escalonadamente (febrero 2025 prácticas prohibidas, agosto 2025 IA de propósito general, agosto 2026 sistemas de alto riesgo). Señalar qué plazos son relevantes para esta organización.
