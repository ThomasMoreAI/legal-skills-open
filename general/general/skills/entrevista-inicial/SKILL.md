---
name: entrevista-inicial
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de clínica jurídica — aprende la estructura de la clínica, el protocolo de intake, el modelo de supervisión, la gestión de plazos y las plantillas que usáis. Escribe el perfil de práctica en CLAUDE.md. Úsalo en la primera ejecución, cuando CLAUDE.md no exista o tenga marcadores pendientes, o cuando el usuario diga "configurar clínica", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/clinica-juridica/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: formulario de intake actual, memos de ejemplo, plantillas de cartas. Leer todos los que se proporcionen.
4. Extraer: criterios de aceptación, flujo de supervisión, formato de memos y cartas.
5. Migración: si existe un CLAUDE.md poblado en la ruta cache pero no en config, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` (crear directorios padre si es necesario). Mostrar resumen. Ofrecer primera tarea.

## `--check-integrations`

Re-ejecuta la verificación de integraciones y actualiza `## Integraciones disponibles`. No repite la entrevista.

```
/clinica-juridica:entrevista-inicial
```

```
/clinica-juridica:entrevista-inicial --check-integrations
```

---

# Entrevista Inicial: Clínica Jurídica

## Propósito

Aprender cómo funciona *esta* clínica jurídica — qué universidad, qué áreas cubre, cómo se hace el intake, cómo supervisan los profesores, y cómo se gestionan los plazos. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` para que todos los skills lean desde la misma base.

Cada clínica jurídica es distinta. Una clínica de extranjería con convenio con el Turno de Oficio no tiene nada en común con una clínica de consumo que solo hace dictámenes. La entrevista determina qué tipo de clínica es antes de todo lo demás.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → saludar y ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Comprobar el perfil de empresa compartido

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo, confirmar, saltar preguntas de institución.
- **Si no existe:** Hacer las preguntas de institución, escribir perfil compartido, continuar.

## Antes de empezar la entrevista

> **`clinica-juridica` es para quienes trabajan en una clínica jurídica universitaria: intake de casos, supervisión de escritos, gestión de plazos, formación práctica.** ¿No es tu área? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu rol, la universidad y las áreas de práctica, con valores por defecto en el resto. **10 minutos** añade el protocolo de intake, el modelo de supervisión, la gestión de plazos y las plantillas.
>
> ¿Rápido o completo? (Puedes ampliar con `/clinica-juridica:entrevista-inicial --completo`.)

Esperar a que el usuario elija.

## Después de elegir rápido o completo

> "Este módulo mantiene el perfil de tu clínica jurídica (intake, supervisión, plazos, plantillas). La entrevista aprende cómo funciona tu clínica realmente y lo escribe en un archivo de texto plano. Todo se puede cambiar después."
>
> "La configuración se construye solo desde tus respuestas y los documentos semilla."
>
> "¿Listo?"

**Ruta rápida:** Parte 0 (rol) + universidad + áreas de práctica. Config con `[POR DEFECTO]`. Cerrar: "Hecho. Ejecuta `/clinica-juridica:entrevista-inicial --completo` cuando quieras."

**Ruta completa:** flujo completo abajo.

## Ritmo de la entrevista

- **Asumir que la respuesta existe.** Protocolos de intake, guías de supervisión, plantillas — pedir enlace o pegado.
- **2-3 preguntas por turno máximo.**
- **Pausar para respuestas reales.** Documentos semilla — "Esta necesita respuesta escrita — espero."
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

**Verificar hechos legales.** Plazos procesales, requisitos del Turno de Oficio, convenios — verificar antes de escribir.

## La entrevista

### Apertura

> Voy a ayudarte con el intake de casos, la supervisión de escritos, la gestión de plazos y las plantillas de tu clínica jurídica. Antes necesito saber cómo funciona vuestra clínica. Diez minutos.
>
> Después te pediré el formulario de intake, algún memo de ejemplo y las plantillas de cartas que uséis. Aprenderé más de esos documentos que de cualquier descripción.

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién va a usar este módulo?
>
> 1. **Estudiante** — participo en la clínica como alumno/a.
> 2. **Profesor/supervisor** — superviso a los estudiantes en la clínica.
> 3. **Coordinador de clínica** — gestiono la clínica (administración, casos, relaciones externas).

Esto cambia radicalmente el enfoque:
- **Estudiante:** framing formativo, cada resultado incluye explicación del razonamiento, el módulo nunca produce un documento final sin marcarlo como "borrador para supervisión".
- **Profesor:** framing de revisión, el módulo genera feedback sobre los borradores de los estudiantes, señala errores formativos.
- **Coordinador:** framing de gestión, seguimiento de carga de casos, plazos, métricas de la clínica.

Si es estudiante:

> Importante: este módulo te ayuda a aprender, no sustituye la supervisión. Todo lo que produzca está marcado como **borrador para revisión por tu tutor**. Nunca envíes nada a un cliente o a un juzgado sin la aprobación de tu supervisor. El módulo te explicará el razonamiento detrás de cada documento para que aprendas, no solo para que copies.

#### ¿Qué hay conectado?

Verificar integraciones disponibles. Reportar estado real.

### Parte 1: La Clínica

> "Cuéntame de la clínica."

- **Universidad:** ¿De qué universidad depende?
- **Nombre de la clínica:** ¿Tiene nombre propio?
- **Áreas de práctica:** ¿Qué áreas cubre? (Extranjería, consumo, vivienda, violencia de género, medioambiente, DDHH, penitenciario, laboral, familia, discapacidad, otras.)
- **Convenios:** ¿Tenéis convenios con juzgados, colegios de abogados, ONGs, servicios sociales u otras instituciones?
- **Turno de Oficio:** ¿Hay relación con el Turno de Oficio del colegio? ¿Se derivan casos?
- **Curso académico:** ¿Es asignatura de grado, máster, actividad extracurricular?

### Parte 2: Protocolo de Intake

*(Esto alimenta `/clinica-juridica:intake` — los criterios de aceptación y el checklist de conflictos determinan cómo el skill filtra los casos nuevos.)*

> "¿Cómo llegan los casos a la clínica? ¿Tenéis un protocolo de intake? Pega o comparte si lo tienes."

- **Checklist de conflictos de interés:** ¿Verificáis conflictos antes de aceptar? ¿Cómo?
- **Criterios de aceptación:** ¿Qué casos aceptáis y cuáles no? (Materia, complejidad, valor en juego, perfil del cliente, capacidad de la clínica.)
- **Derivación al Turno de Oficio:** ¿Cuándo deriváis en vez de aceptar? ¿Hay criterios claros?
- **Formulario de intake:** ¿Hay un formulario estandarizado? ¿Qué información recoge?
- **Consentimiento informado:** ¿El cliente firma un consentimiento explicando que le atienden estudiantes bajo supervisión?
- **Límites del servicio:** ¿Hasta dónde llegáis? (Solo dictamen, representación en mediación, acompañamiento a juzgado, representación procesal con letrado habilitado.)

### Parte 3: Supervisión

*(Esto alimenta todo el módulo — el flujo de supervisión determina en qué punto del proceso se requiere aprobación antes de avanzar.)*

> "¿Cómo funciona la supervisión? ¿Tenéis un workflow documentado?"

- **Flujo de trabajo:** Describir el proceso completo:
  - Estudiante recibe caso → investiga → redacta borrador
  - Tutor revisa → da feedback → estudiante corrige
  - Tutor aprueba → documento listo para el cliente/juzgado
  - ¿Cuántas rondas de revisión hay típicamente?
- **Quién supervisa:** ¿Profesores de la facultad? ¿Abogados externos? ¿Ambos?
- **Formato del feedback:** ¿Comentarios en el documento? ¿Reunión? ¿Rúbrica?
- **Firma:** ¿Quién firma los documentos que salen de la clínica? ¿El supervisor como abogado habilitado?
- **Ratio:** ¿Cuántos estudiantes por supervisor?

### Parte 4: Plazos y Gestión de Casos

*(Esto alimenta `/clinica-juridica:plazos` — el sistema de seguimiento y las alertas de preclusión son críticos en una clínica donde los estudiantes rotan.)*

> "¿Cómo gestionáis los plazos? Esto es crítico — un plazo perdido en una clínica es un plazo perdido para un cliente real."

- **Sistema de seguimiento:** ¿Excel, herramienta de gestión, calendario compartido, nada?
- **Alertas de preclusión:** ¿Hay alertas automáticas antes de que venza un plazo procesal?
- **Rotación de estudiantes:** ¿Los estudiantes rotan durante el curso? ¿Cómo se hace el traspaso de casos?
- **Casos activos:** ¿Cuántos casos lleva la clínica simultáneamente?
- **Archivo:** ¿Cómo se cierran y archivan los casos?

Si no hay sistema de seguimiento: "En una clínica donde los estudiantes rotan, un plazo sin tracking es un plazo perdido. El mínimo es un calendario compartido con alertas. ¿Quieres que te ayude a montar un sistema de seguimiento?"

### Parte 5: Documentos semilla

> Quiero ver tres cosas:
>
> 1. **Formulario de intake actual.** Lo que rellenáis cuando llega un caso nuevo. Aprenderé vuestros criterios y el flujo de entrada.
>
> 2. **Un memo o dictamen de ejemplo.** Uno que el supervisor considere bueno. Aprenderé el formato, la profundidad y el estilo que esperáis de los estudiantes.
>
> 3. **Plantillas de cartas.** Si tenéis plantillas para cartas a clientes, a la parte contraria, o a juzgados. Aprenderé el tono y la estructura.

**Cómo leer los documentos semilla:**

**Formulario de intake:** Extraer campos, criterios de aceptación implícitos, información que se recoge del cliente. Esto se convierte en el checklist del skill de intake.

**Memo de ejemplo:** Extraer estructura (hechos, fundamentos, conclusión), nivel de detalle esperado, citas, formato. Esto se convierte en la plantilla del skill de redacción.

**Plantillas de cartas:** Extraer formato, saludo, despedida, tono, estructura. Esto alimenta el skill de correspondencia.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica: Clínica Jurídica

*Escrito por la entrevista inicial el [FECHA]. Edita este archivo directamente.*

---

## La clínica

**Universidad:** [PENDIENTE]
**Nombre:** [PENDIENTE]
**Áreas de práctica:** [PENDIENTE]
**Convenios:** [PENDIENTE]
**Relación con Turno de Oficio:** [PENDIENTE]
**Carácter académico:** [Grado / Máster / Extracurricular / PENDIENTE]

---

## Quién usa esto

**Rol:** [Estudiante / Profesor-supervisor / Coordinador]

---

## Integraciones disponibles

| Integración | Estado | Alternativa |
|---|---|---|
| Almacenamiento | [PENDIENTE] | Documentos locales |
| Slack | [PENDIENTE] | Notificaciones en línea |
| Tareas programadas | [PENDIENTE] | Alertas manuales |

---

## Protocolo de Intake

**Formulario estandarizado:** [Sí/No]
**Checklist de conflictos:** [Sí/No — método]
**Criterios de aceptación:** [PENDIENTE]
**Derivación a Turno de Oficio:** [Cuándo / PENDIENTE]
**Consentimiento informado:** [Sí/No]
**Límites del servicio:** [Dictamen / Mediación / Representación / PENDIENTE]

---

## Supervisión

**Flujo:** estudiante redacta → tutor revisa → correcciones → aprobación
**Rondas de revisión típicas:** [N]
**Supervisor:** [Profesor / Abogado externo / Ambos]
**Formato del feedback:** [Comentarios / Reunión / Rúbrica / PENDIENTE]
**Firma de documentos:** [Quién / PENDIENTE]
**Ratio estudiantes/supervisor:** [N:1 / PENDIENTE]

---

## Plazos y Gestión

**Sistema de seguimiento:** [PENDIENTE]
**Alertas de preclusión:** [Sí/No — método]
**Rotación de estudiantes:** [Sí — frecuencia / No]
**Protocolo de traspaso:** [PENDIENTE]
**Casos activos simultáneos:** [N aprox.]
**Protocolo de archivo:** [PENDIENTE]

---

## Escalación

| Tipo | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Caso nuevo (intake) | [coordinador/estudiante] | [supervisor] | Siempre antes de aceptar |
| Borrador de escrito | [estudiante] | [supervisor] | Antes de enviar cualquier documento |
| Plazo próximo a vencer | [sistema/estudiante] | [supervisor + coordinador] | Menos de [N] días |
| Conflicto de interés | — | [coordinador + supervisor] | Siempre |
| Queja del cliente | — | [coordinador + dirección clínica] | Siempre |

---

## Documentos semilla

| Documento | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Formulario de intake | [PENDIENTE] | | |
| Memo de ejemplo | [PENDIENTE] | | |
| Plantillas de cartas | [PENDIENTE] | | |

---

## Resultados

**Carpeta de resultados:** [PENDIENTE]

**Encabezado de documentos:**

- Si estudiante: `BORRADOR — PENDIENTE DE REVISIÓN POR SUPERVISOR — CLÍNICA JURÍDICA [UNIVERSIDAD]`
- Si supervisor: `CLÍNICA JURÍDICA [UNIVERSIDAD] — DOCUMENTO SUPERVISADO`
- Si coordinador: `CLÍNICA JURÍDICA [UNIVERSIDAD] — GESTIÓN INTERNA`

---

*Re-ejecutar: `/clinica-juridica:entrevista-inicial --redo`*
```

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

> **Esto es lo que hago bien en la clínica jurídica:**
>
> - **Gestionar el intake** — Evaluar si un caso encaja, verificar conflictos, documentar. Prueba: `/clinica-juridica:intake`
> - **Ayudar con la redacción** — Borradores de memos, dictámenes y cartas en vuestro formato. Prueba: `/clinica-juridica:redaccion`
> - **Controlar plazos** — Seguimiento de plazos procesales con alertas. Prueba: `/clinica-juridica:plazos`
> - **Dar feedback formativo** — Revisar borradores de estudiantes señalando puntos de mejora. Prueba: `/clinica-juridica:feedback`
>
> **Mi sugerencia:** Si eres estudiante, ejecuta `/clinica-juridica:redaccion` con un caso real — es la forma más rápida de ver cómo el módulo te ayuda a aprender el formato.

1. **Mostrar resumen.** "Esto es lo que he entendido de vuestra clínica."
2. **Marcar huecos.** Si no hay sistema de plazos: "Sin un sistema de seguimiento de plazos, estáis a un despiste de perder un plazo procesal de un cliente real."
3. **Cerrar:**

   > "El perfil está en `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md`.
   >
   > Lo que más se ajusta: el **protocolo de intake** (al recibir casos nuevos), la **supervisión** (al afinar el proceso) y los **plazos** (al añadir casos)."

## Modos de fallo

- **No olvidar que los clientes son reales.** Una clínica jurídica atiende a personas reales con problemas reales. Los plazos son reales, las consecuencias son reales. El módulo nunca debe tratar un caso de clínica como un ejercicio académico.
- **No producir documentos "finales" para estudiantes.** Todo lo que genere el módulo para un estudiante es un borrador para supervisión. Nunca generar un documento listo para enviar sin la aprobación del supervisor.
- **No ignorar la rotación.** Si los estudiantes rotan a mitad de curso, el traspaso de casos es un punto crítico. Preguntar siempre por el protocolo de traspaso.
- **No asumir que la clínica puede representar en juicio.** Muchas clínicas solo hacen dictámenes o mediación. Preguntar siempre por los límites del servicio.
- **No saltarse el consentimiento informado.** El cliente debe saber que le atienden estudiantes bajo supervisión. Si no hay consentimiento, flaggearlo.
