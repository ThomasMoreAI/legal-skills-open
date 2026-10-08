---
name: entrevista-inicial-estudiante-derecho-3539-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de estudiante de Derecho — aprende tu universidad, curso, objetivos (grado, máster, oposiciones, acceso a la abogacía), método de estudio y asignaturas actuales. Escribe el perfil en CLAUDE.md para personalizar ejercicios, esquemas y simulacros. Úsalo en la primera ejecución, cuando CLAUDE.md no exista, o cuando el usuario diga "configurar estudiante", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/estudiante-derecho/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. No hay documentos semilla obligatorios, pero aceptar temarios, programas o apuntes si los ofrece.
4. Escribir `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

```
/estudiante-derecho:entrevista-inicial
```

---

# Entrevista Inicial: Estudiante de Derecho

## Propósito

Aprender quién es *este* estudiante — en qué universidad está, qué curso, qué quiere hacer (grado, máster, oposiciones, acceso a la abogacía), cómo estudia y en qué asignaturas necesita ayuda. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` para que los ejercicios, esquemas y simulacros se personalicen.

Cada estudiante es distinto. Un estudiante de 2.o de Grado preparando Civil no tiene nada en común con un graduado preparando oposiciones a judicatura. La entrevista lo determina antes de todo lo demás.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → saludar y ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Antes de empezar la entrevista

> **`estudiante-derecho` es para estudiantes de Derecho en España: esquemas, casos prácticos, simulacros de examen, preparación de oposiciones y acceso a la abogacía.** ¿No es tu caso? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu universidad, curso y objetivo principal. **10 minutos** añade asignaturas actuales, método de estudio, y si preparas oposiciones o acceso, los detalles específicos.
>
> ¿Rápido o completo?

Esperar.

## Después de elegir

> "Este módulo personaliza ejercicios, esquemas y simulacros según tu universidad, curso y objetivos. La entrevista aprende tu situación y la escribe en un archivo de texto plano. Todo se puede cambiar cuando avances de curso o cambies de objetivo."
>
> "¿Listo?"

**Ruta rápida:** universidad + curso + objetivo. Config con `[POR DEFECTO]`.

**Ruta completa:** flujo completo abajo.

## Ritmo de la entrevista

- **2-3 preguntas por turno máximo.**
- **Algunas son de selección rápida** (universidad, curso, objetivo). Otras necesitan respuesta (asignaturas, método).
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

## La entrevista

### Apertura

> Voy a ayudarte a estudiar Derecho de forma más eficiente — esquemas, casos prácticos, simulacros de examen, y si preparas oposiciones o el acceso, preparación específica. Primero necesito saber quién eres y qué estás haciendo. Cinco minutos.

### Parte 0: Quién eres

> "Cuéntame un poco de ti."

- **Universidad:** ¿En qué universidad estudias (o estudiaste)?
- **Curso actual:** ¿En qué curso estás? (1.o a 4.o de Grado, Máster de Acceso, Máster especializado, ya graduado.)
- **Especialización prevista:** ¿Tienes idea de qué rama te interesa? (Civil, penal, mercantil, laboral, administrativo, tributario, internacional, procesal, constitucional, otra.) Si no lo tienes claro, perfecto — es pronto.

### Parte 1: Objetivo

> "¿Qué quieres conseguir? Esto determina cómo personalizo los ejercicios."
>
> 1. **Grado** — estoy cursando el Grado en Derecho, quiero aprobar y aprender.
> 2. **Máster** — estoy en un máster (de acceso u otro).
> 3. **Oposiciones** — estoy preparando oposiciones o pienso prepararlas.
> 4. **Acceso a la abogacía** — estoy preparando el examen de acceso a la abogacía.
> 5. **Grado + oposiciones** — estudio el grado pero ya pienso en oposiciones.
> 6. **Grado + acceso** — estudio el grado y también quiero preparar el acceso.

Esto cambia radicalmente los ejercicios:
- **Grado:** esquemas de asignaturas, casos prácticos tipo examen, tests de repaso.
- **Máster:** análisis más profundo, práctica profesional simulada.
- **Oposiciones:** temas del programa, cantados cronometrados, tests tipo oposición.
- **Acceso:** simulacros del examen de acceso, tests por materias, análisis de convocatorias.

### Parte 2: Asignaturas actuales

> "¿Qué asignaturas estás cursando ahora mismo? (O si es verano, las que cursarás el próximo cuatrimestre.) Esto me permite personalizar los ejercicios a lo que realmente estás estudiando."

Aceptar una lista libre. Para cada asignatura, registrar:
- Nombre de la asignatura.
- Profesor (opcional, puede influir en el enfoque).
- ¿Cómo es el examen? (Test, caso práctico, oral, desarrollo, mixto.)

Si está preparando oposiciones o acceso y ya no cursa asignaturas: "¿En qué materias del programa estás ahora?" y tratar como equivalente.

### Parte 3: Método de estudio

> "¿Cómo estudias? Esto me ayuda a producir materiales que encajen con tu forma de trabajar."
>
> - **Esquemas** — ¿Haces esquemas? ¿Tipo mapa mental, esquema lineal, fichas?
> - **Fichas (flashcards)** — ¿Usas Anki u otro sistema de repetición espaciada?
> - **Casos prácticos** — ¿Practicas con casos? ¿De exámenes anteriores, del libro, inventados?
> - **Subrayado + lectura repetida** — el clásico.
> - **Otro** — cuéntame.

No juzgar el método. Adaptarse a lo que funcione para el estudiante.

### Parte 4: Si oposiciones

*(Solo si el objetivo incluye oposiciones.)*

> "¿A qué oposición te preparas (o piensas prepararte)?"
>
> 1. **Judicatura** — Carrera Judicial
> 2. **Fiscalía** — Carrera Fiscal
> 3. **Abogacía del Estado**
> 4. **Notarías**
> 5. **Registros** — Registros de la Propiedad y Mercantiles
> 6. **Letrados de la Administración de Justicia** (antes Secretarios Judiciales)
> 7. **TAC** — Técnicos de la Administración Civil del Estado
> 8. **Otra** — especifica.

Después:
- **¿Tienes preparador?** Sí/No. Si sí, ¿individual o academia?
- **¿Por qué vuelta vas?** (Primera, segunda, tercera...) Si es primera vez, decir: "La primera vuelta es la más larga y la que más desorienta — es normal. Los ejercicios que te proponga irán ajustándose a tu nivel."
- **¿Tienes el programa oficial?** Pega o comparte. Si no: "Lo busco yo, pero confirma que sea el vigente."

### Parte 5: Si acceso a la abogacía

*(Solo si el objetivo incluye el acceso.)*

> "Sobre el examen de acceso a la abogacía:"

- **Fecha del examen:** ¿Cuándo es la próxima convocatoria que vas a presentarte? (Suele ser en junio/julio.)
- **Materias fuertes:** ¿En qué te sientes seguro?
- **Materias débiles:** ¿Qué te cuesta más? (Esto determina dónde concentrar los simulacros.)
- **¿Has hecho simulacros antes?** ¿De qué convocatoria?
- **¿Máster de acceso:** ¿Lo estás cursando ahora? ¿Lo has terminado?

## Plantilla del perfil de práctica

```markdown
# Perfil: Estudiante de Derecho

*Escrito por la entrevista inicial el [FECHA]. Edita directamente o ejecuta --redo.*

---

## Quién soy

**Universidad:** [PENDIENTE]
**Curso:** [PENDIENTE]
**Especialización interés:** [PENDIENTE / Sin decidir]

---

## Objetivo

**Principal:** [Grado / Máster / Oposiciones / Acceso / Combinado]

---

## Asignaturas actuales

| Asignatura | Tipo de examen | Notas |
|---|---|---|
| [PENDIENTE] | | |

---

## Método de estudio

**Preferencias:** [Esquemas / Fichas / Casos prácticos / Lectura / Otro]
**Herramientas:** [Anki / Notion / Papel / Otro / PENDIENTE]

---

## Oposiciones (si aplica)

**Especialidad:** [Judicatura / Fiscalía / Notarías / Registros / Abogacía del Estado / LAJ / TAC / Otra / N/A]
**Preparador:** [Sí — tipo / No / PENDIENTE]
**Vuelta:** [Primera / Segunda / N.a / PENDIENTE]
**Programa oficial:** [Disponible / PENDIENTE]

---

## Acceso a la Abogacía (si aplica)

**Fecha examen:** [PENDIENTE / N/A]
**Máster de acceso:** [Cursando / Completado / PENDIENTE / N/A]
**Materias fuertes:** [PENDIENTE]
**Materias débiles:** [PENDIENTE]
**Simulacros previos:** [Sí — convocatoria / No / PENDIENTE]

---

## Resultados

**Carpeta:** [PENDIENTE]

**Encabezado:** `MATERIAL DE ESTUDIO — NO CONSTITUYE ASESORAMIENTO JURÍDICO`

---

*Re-ejecutar: `/estudiante-derecho:entrevista-inicial --redo`*
```

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

> **Esto es lo que hago bien para estudiantes de Derecho:**
>
> - **Generar esquemas** — Esquemas de temas adaptados a tu asignatura y formato. Prueba: `/estudiante-derecho:esquema`
> - **Crear casos prácticos** — Casos tipo examen con solución razonada. Prueba: `/estudiante-derecho:caso-practico`
> - **Simulacros de test** — Tests cronometrados por materia. Prueba: `/estudiante-derecho:test`
> - **Explicar conceptos** — Explicaciones claras de conceptos jurídicos complejos. Prueba: `/estudiante-derecho:explicar`
> - **Si oposiciones: cantar temas** — Práctica de exposición oral cronometrada. Prueba: `/estudiante-derecho:cantar`
> - **Si acceso: simulacro completo** — Simulacro del examen de acceso. Prueba: `/estudiante-derecho:simulacro-acceso`
>
> **Mi sugerencia:** Empieza con `/estudiante-derecho:esquema` de un tema que estés estudiando ahora — verás rápido si el formato te sirve.

1. **Resumen.** "Esto es lo que he entendido."
2. **Primera tarea según objetivo:**
   - Grado: "¿Qué asignatura te genera más dudas ahora mismo?"
   - Oposiciones: "¿En qué tema del programa estás? Te propongo un ejercicio."
   - Acceso: "¿Cuántos días faltan para el examen? Te propongo un plan."
3. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md`.
   >
   > Actualízalo al cambiar de curso, de asignaturas o de objetivo. Ejecuta `--redo` para repetir la entrevista."

4. **Tu perfil aprende:**

   > Los ejercicios se adaptan conforme los usas. Si un test te sale fácil, el siguiente será más difícil. Si un esquema no te sirve, dime qué formato prefieres y lo ajusto.

## Modos de fallo

- **No asumir el nivel.** Un estudiante de 1.o no sabe lo que es una excepción procesal. Un opositor sí. Adaptar el lenguaje al curso.
- **No sustituir al preparador.** Si tiene preparador de oposiciones, el módulo complementa, no compite. No contradecir el método del preparador sin que el estudiante lo pida.
- **No dar respuestas sin razonamiento.** El objetivo es que el estudiante aprenda, no que copie. Siempre explicar el porqué.
- **No inventar preguntas de examen.** Si el estudiante pide casos prácticos de una asignatura concreta, preguntar si tiene exámenes anteriores reales — son más útiles que los inventados.
- **No ignorar que el programa de oposiciones es específico.** El programa de judicatura no es el de notarías. Usar el programa oficial, no uno genérico.
- **No confundir el examen de acceso con las oposiciones.** Son cosas completamente distintas. El acceso es un test; las oposiciones son orales/escritas extensas.
