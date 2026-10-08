---
name: entrevista-inicial-administrativo-3752-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin de derecho administrativo. Aprende tu práctica y escribe CLAUDE.md a partir de tus procedimientos habituales, experiencia en contratación pública y contencioso-administrativo. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin administrativo", "onboarding administrativo", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/administrativo/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: administrative
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: resoluciones administrativas, pliegos de contratación, recursos recientes.
4. Extraer: relación con administraciones, tipos de procedimiento, experiencia en contratación pública, asuntos contenciosos.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/administrativo:entrevista-inicial
```

```
/administrativo:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Derecho Administrativo

## Propósito

Aprender cómo funciona *esta* práctica de derecho administrativo — con qué administraciones se relaciona, qué procedimientos gestiona, si hace contratación pública, qué contenciosos lleva ante la Sala Tercera de la CSJ. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

El derecho administrativo en Panamá es enormemente amplio. Un abogado que gestiona permisos de construcción tiene poco en común con uno que impugna sanciones de la ASEP o que licita contratos públicos en PanamaCompra. La entrevista identifica el perfil antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`administrativo` es para quien gestiona procedimientos administrativos, contratación pública, recursos ante la Administración y contencioso-administrativo.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan las administraciones con las que te relacionas y los procedimientos principales, con valores sensatos en todo lo demás. **15 minutos** añade tu experiencia en contratación pública, asuntos contenciosos en curso y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica administrativa (administraciones, procedimientos, contratación pública, contencioso-administrativo). Esta entrevista aprende cómo trabajas realmente y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes alguna resolución administrativa o pliego reciente? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo de la Ley 38 de 2000, de la Ley 22 de 2006 de contratación pública o del Código Judicial (jurisdicción contencioso-administrativa), comprobar antes de escribirlo.

## La entrevista

### Apertura

> Voy a ayudarte con procedimientos administrativos, contratación pública, recursos en la vía gubernativa y demandas ante la Sala Tercera de lo Contencioso-Administrativo de la CSJ. Antes de nada, necesito saber con qué administraciones te relacionas y qué tipo de asuntos gestionas. Diez minutos.
>
> Después te pediré tres cosas: una resolución administrativa representativa, un pliego de cargos si haces contratación pública, y un recurso reciente.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a administrativista idóneo/a** — abogado especializado en derecho público.
> 2. **Profesional con acceso a abogado** — responsable de licitaciones, gestor administrativo, funcionario que consulta con asesoría legal.
> 3. **Profesional sin acceso regular a abogado** — gestionas esto por tu cuenta.

Si es 2 o 3, explicar: los outputs serán investigación para revisión por abogado idóneo; se pausará antes de pasos con consecuencias jurídicas (presentación de recursos, interposición de demanda contenciosa).

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Relación con la Administración (2-3 min)

> **Con qué niveles de la Administración te relacionas habitualmente?** Esto determina la normativa procedimental y los órganos de recurso.
>
> - **Gobierno Central** — ministerios y sus direcciones. Cuáles?
> - **Entidades autónomas y semiautónomas** — ASEP, ACP, ATTT, MINSA, ANATI, MiAmbiente, etc. Cuáles?
> - **Municipios** — alcaldías, concejos municipales. Cuáles?
>
> Con qué frecuencia interactúas con cada nivel? (Diaria, semanal, mensual, puntual)
>
> Usáis el portal PanamaCompra o trámites en línea habitualmente?

Pausa. Después:

> **En qué ámbito material se concentra tu práctica administrativa?** (Puedes seleccionar varios)
> - Urbanismo y construcción
> - Ambiente
> - Salud
> - Educación
> - Energía
> - Telecomunicaciones
> - Transporte e infraestructura
> - Función pública / carrera administrativa
> - Otro (descríbelo)

### Parte 2: Procedimientos habituales (2-3 min)

> **Qué tipo de procedimientos administrativos gestionas con más frecuencia?**
>
> - **Permisos y licencias** — de construcción, ambientales, de operación, sectoriales. Cuáles?
> - **Procedimientos sancionadores** — en qué materias? Habéis tenido sanciones recientes?
> - **Subsidios y ayudas** — solicitud, justificación, reintegro. Con qué administración?
> - **Expropiaciones** — como beneficiario, como expropiado?
> - **Responsabilidad patrimonial del Estado** — reclamaciones en curso?
> - **Revocatoria o anulación de oficio de actos** — las habéis instado o sufrido?
>
> Para los procedimientos que más gestionas:
> - Plazos típicos de resolución real (no el legal, el real)
> - Silencio administrativo (regla general en Panamá: negativo): cómo opera en tus procedimientos habituales?
> - Recursos habituales: reconsideración, apelación, o directamente a la Sala Tercera tras agotar la vía gubernativa?

### Parte 3: Contratación pública (3-4 min)

> **Trabajas en contratación pública?** Si la respuesta es no, saltamos esta parte.
>
> Si sí:
> - **Desde qué lado?** Proponente (empresa), entidad contratante, o ambos?
> - **Entidad contratante habitual** — con qué entidades o unidades de compra trabajas más?
> - **Tipos de contratos** — obras, servicios, suministros, consultoría, concesiones?
> - **Cuantía habitual** — contratación menor (por debajo del umbral legal [verificar]) o licitación pública?
> - **Procedimientos** — licitación pública, subasta en reverso, convenio marco, procedimiento excepcional?
>
> Experiencia con recursos:
> - **TACP** (Tribunal Administrativo de Contrataciones Públicas) — habéis interpuesto o defendido recursos en materia de contratación?
> - Experiencia con la DGCP y el portal PanamaCompra?
> - Ratio de éxito aproximado? Aspectos del pliego que más os afectan?
>
> Tienes algún pliego de cargos reciente que pueda ver? Pégalo o comparte ruta.

### Parte 4: Contencioso-administrativo (2-3 min)

> **Llevas asuntos contencioso-administrativos?** Si la respuesta es no, saltamos esta parte.
>
> Si sí:
> - **Tipo de demanda habitual** — plena jurisdicción (restablecimiento de derecho subjetivo) o nulidad (control objetivo de legalidad)?
> - **Materias más frecuentes** — urbanismo, tributario (si no lo lleva el plugin fiscal), sanciones, contratación, responsabilidad patrimonial, migración, otro?
> - **Volumen** — cuántos asuntos en curso aproximadamente ante la Sala Tercera?
> - **Suspensión provisional** — la solicitáis con frecuencia? Ratio de éxito?
> - **Procuraduría de la Administración** — cómo gestionáis su intervención y concepto en el proceso?
> - **Demandas de protección de derechos humanos** ante la Sala Tercera — las habéis usado? [verificar]
>
> Hay algún asunto contencioso en curso que sea especialmente relevante o de referencia?

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Una resolución administrativa representativa** — favorable o desfavorable, la que mejor refleje vuestra práctica habitual. Aprenderé vuestro estilo de argumentación y los tipos de asuntos que gestionáis.
>
> 2. **Pliego de cargos** — si hacéis contratación pública, un pliego de cargos reciente. Aprenderé vuestras cláusulas habituales y vuestra posición en los actos públicos.
>
> 3. **Un recurso reciente** — administrativo (vía gubernativa) o contencioso (Sala Tercera). Me enseña cómo argumentáis y qué criterios utilizáis.

**Cómo leer los documentos semilla:**

**Resolución administrativa:** Extraer el procedimiento, los fundamentos de derecho citados, el sentido de la parte resolutiva. Identificar las normas procesales aplicadas.

**Pliego de cargos:** Mapear los criterios de evaluación, las condiciones de ejecución, las cláusulas de multa y modificación. Comparar con las posiciones declaradas en la entrevista.

**Recurso:** Extraer la estructura argumentativa, los fundamentos de derecho, la jurisprudencia citada. Aprender el estilo.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Administrativo

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] gestiona asuntos de derecho administrativo en [ámbitos materiales].
Relación principal con [Gobierno Central / entidades autónomas / municipios — cuáles]. El equipo cuenta con [N] personas.
[Responsable: nombre]. La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a idóneo/a | Profesional con acceso a abogado | Profesional sin acceso a abogado]
**Contacto del abogado:** [Nombre / despacho / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Calendario bajo demanda |

---

## Relación con la Administración

| Nivel | Administraciones concretas | Frecuencia | Ámbito material |
|---|---|---|---|
| Gobierno Central | [ministerios/direcciones] | [frecuencia] | [materia] |
| Entidades autónomas y semiautónomas | [ASEP/ATTT/MINSA/etc.] | [frecuencia] | [materia] |
| Municipios | [alcaldías/concejos] | [frecuencia] | [materia] |

---

## Procedimientos habituales

| Tipo | Administración | Frecuencia | Silencio | Recurso habitual | Notas |
|---|---|---|---|---|---|
| [permisos/sanciones/subsidios/etc.] | [cuál] | [frecuencia] | [negativo por defecto/positivo si norma especial] | [reconsideración/apelación/contencioso] | |

---

## Contratación pública

**Posición:** [proponente / entidad contratante / ambos]
**Entidades contratantes habituales:** [entidades]
**Tipos de contrato:** [obras/servicios/suministros/consultoría/concesiones]
**Cuantía habitual:** [contratación menor / licitación pública]
**Procedimientos habituales:** [licitación pública/subasta en reverso/convenio marco]

### Experiencia en recursos contractuales

| Órgano | Recursos interpuestos | Recursos defendidos | Ratio éxito aprox. |
|---|---|---|---|
| TACP | [número] | [número] | [ratio] |

---

## Contencioso-administrativo (Sala Tercera CSJ)

**Tipo de demanda habitual:** [plena jurisdicción / nulidad]
**Materias:** [lista]
**Asuntos en curso:** [número aproximado]
**Suspensión provisional:** [frecuencia y ratio]
**Procuraduría de la Administración:** [gestión de su intervención]

### Asuntos en curso relevantes

| Asunto | Órgano | Materia | Estado | Notas |
|---|---|---|---|---|
| [referencia] | [órgano] | [materia] | [estado] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Procedimiento rutinario | [responsable] | [nombre] | Silencio negativo vencido, sanción > [umbral] |
| Recurso administrativo | [responsable] | [nombre] | Cuantía > [umbral] |
| Contencioso-administrativo (Sala Tercera) | [responsable] | [nombre] | Siempre |
| Contratación pública por licitación | — | [GC + dirección] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Resolución administrativa | [ruta] | [fecha] | [tipo procedimiento] |
| Pliego de cargos | [ruta] | [fecha] | [entidad] |
| Recurso reciente | [ruta] | [fecha] | [tipo y materia] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/administrativo:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Los procedimientos habituales y la experiencia en contratación pública son las partes a revisar con más cuidado."

2. **Proponer primeras tareas:**
   - "Quieres que revise un pliego de contratación en curso?"
   - "Tienes algún recurso administrativo pendiente de redactar?"
   - "Quieres que compruebe plazos de prescripción o caducidad en tus procedimientos abiertos?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/administrativo:entrevista-inicial --redo` para re-entrevista completa
   > - `/administrativo:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: los **procedimientos habituales** (según evoluciona la práctica), la **contratación pública** (según se acumula experiencia en recursos), y el **contencioso-administrativo** (según cambian los asuntos en curso)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No asumir que la Ley 38 de 2000 aplica a todo.** Hay procedimientos especiales con normativa propia (tributario ante la DGI, contratación pública, migratorio, laboral). La Ley 38 de 2000 es de aplicación general y supletoria en muchos casos [verificar].
- **No confundir recurso de reconsideración con apelación.** La reconsideración se interpone ante el mismo funcionario de primera o única instancia que dictó el acto (art. 166.1 Ley 38 de 2000); la apelación, ante su inmediato superior (art. 166.2 Ley 38 de 2000). La resolución de la apelación (o la inexistencia de superior) es lo que agota la vía gubernativa (art. 200 Ley 38 de 2000). Un error aquí tiene consecuencias de inadmisibilidad.
- **No dar por hecho que el silencio es positivo.** En Panamá la regla general es el silencio administrativo NEGATIVO: transcurrido el plazo (general de 2 meses) sin decisión, la petición o recurso se entiende denegado, salvo norma especial que disponga lo contrario expresamente (arts. 156-157 Ley 38 de 2000). Verificar siempre la norma sectorial aplicable.
- **No ignorar los plazos del contencioso.** La demanda de plena jurisdicción ante la Sala Tercera está sujeta a un plazo de 2 meses desde la publicación, notificación o ejecución del acto (art. 42-B Ley 135 de 1943); la demanda de nulidad puede presentarse en cualquier tiempo (art. 42-A Ley 135 de 1943).
- **No olvidar el agotamiento de la vía gubernativa.** Es presupuesto para acudir a la Sala Tercera (art. 200 Ley 38 de 2000), salvo en las acciones de nulidad y demás excepciones legales.
- **No olvidar la intervención de la Procuraduría de la Administración.** En el proceso contencioso-administrativo emite concepto obligatorio (Ley 38 de 2000).
