---
name: entrevista-inicial-estudiante-derecho-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista inicial del módulo de estudiante de Derecho — aprende tu universidad, año, objetivos (licenciatura, posgrado, concursos de carrera judicial, idoneidad para la abogacía), método de estudio y asignaturas actuales. Escribe el perfil en CLAUDE.md para personalizar ejercicios, esquemas y simulacros. Úsalo en la primera ejecución, cuando CLAUDE.md no exista, o cuando el usuario diga "configurar estudiante", "onboarding", o quiera repetir la entrevista.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/estudiante-derecho/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: bankruptcy
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

Aprender quién es *este* estudiante — en qué universidad está, qué año, qué quiere hacer (licenciatura, posgrado, concursos de carrera judicial, idoneidad para la abogacía), cómo estudia y en qué asignaturas necesita ayuda. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` para que los ejercicios, esquemas y simulacros se personalicen.

Cada estudiante es distinto. Un estudiante de 2.o año preparando Civil no tiene nada en común con un graduado preparando un concurso de méritos para juez. La entrevista lo determina antes de todo lo demás.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → saludar y ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Antes de empezar la entrevista

> **`estudiante-derecho` es para estudiantes de Derecho en Panamá: esquemas, casos prácticos, simulacros de examen, preparación de concursos de la carrera judicial e idoneidad para la abogacía.** ¿No es tu caso? `/hub-constructor:buscador-skills`.
>
> **2 minutos** registra tu universidad, año y objetivo principal. **10 minutos** añade asignaturas actuales, método de estudio, y si preparas un concurso de carrera judicial o la idoneidad, los detalles específicos.
>
> ¿Rápido o completo?

Esperar.

## Después de elegir

> "Este módulo personaliza ejercicios, esquemas y simulacros según tu universidad, año y objetivos. La entrevista aprende tu situación y la escribe en un archivo de texto plano. Todo se puede cambiar cuando avances de año o cambies de objetivo."
>
> "¿Listo?"

**Ruta rápida:** universidad + año + objetivo. Config con `[POR DEFECTO]`.

**Ruta completa:** flujo completo abajo.

## Ritmo de la entrevista

- **2-3 preguntas por turno máximo.**
- **Algunas son de selección rápida** (universidad, año, objetivo). Otras necesitan respuesta (asignaturas, método).
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

## La entrevista

### Apertura

> Voy a ayudarte a estudiar Derecho de forma más eficiente — esquemas, casos prácticos, simulacros de examen, y si preparas un concurso de carrera judicial o la idoneidad, preparación específica. Primero necesito saber quién eres y qué estás haciendo. Cinco minutos.

### Parte 0: Quién eres

> "Cuéntame un poco de ti."

- **Universidad:** ¿En qué universidad estudias (o estudiaste)? (Universidad de Panamá, USMA, Universidad Latina, ULACIT, Universidad Católica Santa María La Antigua, otra.)
- **Año actual:** ¿En qué año estás? (1.o a 5.o de la Licenciatura, posgrado/maestría, ya graduado.)
- **Especialización prevista:** ¿Tienes idea de qué rama te interesa? (Civil, penal, comercial, laboral, administrativo, tributario, internacional, procesal, constitucional, marítimo, otra.) Si no lo tienes claro, perfecto — es pronto.

### Parte 1: Objetivo

> "¿Qué quieres conseguir? Esto determina cómo personalizo los ejercicios."
>
> 1. **Licenciatura** — estoy cursando la Licenciatura en Derecho, quiero aprobar y aprender.
> 2. **Posgrado** — estoy en un posgrado o maestría.
> 3. **Concursos de carrera judicial** — estoy preparando un concurso de méritos del Órgano Judicial o el Ministerio Público, o pienso prepararlo.
> 4. **Idoneidad para la abogacía** — me preparo para el ejercicio de la abogacía (idoneidad ante la CSJ).
> 5. **Licenciatura + concursos** — estudio la licenciatura pero ya pienso en concursos de carrera judicial.
> 6. **Licenciatura + idoneidad** — estudio la licenciatura y también quiero preparar el ejercicio de la abogacía.

Esto cambia radicalmente los ejercicios:
- **Licenciatura:** esquemas de asignaturas, casos prácticos tipo examen, tests de repaso.
- **Posgrado:** análisis más profundo, práctica profesional simulada.
- **Concursos de carrera judicial:** temas del programa, exposiciones cronometradas, tests tipo concurso.
- **Idoneidad:** simulacros de repaso integral, tests por materias, consolidación para la práctica.

### Parte 2: Asignaturas actuales

> "¿Qué asignaturas estás cursando ahora mismo? (O si es verano, las que cursarás el próximo cuatrimestre.) Esto me permite personalizar los ejercicios a lo que realmente estás estudiando."

Aceptar una lista libre. Para cada asignatura, registrar:
- Nombre de la asignatura.
- Profesor (opcional, puede influir en el enfoque).
- ¿Cómo es el examen? (Test, caso práctico, oral, desarrollo, mixto.)

Si está preparando un concurso de carrera judicial o la idoneidad y ya no cursa asignaturas: "¿En qué materias del programa estás ahora?" y tratar como equivalente.

### Parte 3: Método de estudio

> "¿Cómo estudias? Esto me ayuda a producir materiales que encajen con tu forma de trabajar."
>
> - **Esquemas** — ¿Haces esquemas? ¿Tipo mapa mental, esquema lineal, fichas?
> - **Fichas (flashcards)** — ¿Usas Anki u otro sistema de repetición espaciada?
> - **Casos prácticos** — ¿Practicas con casos? ¿De exámenes anteriores, del libro, inventados?
> - **Subrayado + lectura repetida** — el clásico.
> - **Otro** — cuéntame.

No juzgar el método. Adaptarse a lo que funcione para el estudiante.

### Parte 4: Si concursos de carrera judicial

*(Solo si el objetivo incluye concursos de la carrera judicial o el Ministerio Público.)*

> "¿A qué concurso te preparas (o piensas prepararte)?"
>
> 1. **Juez** — Municipal, de Circuito o Superior
> 2. **Magistrado** — tribunales superiores / CSJ
> 3. **Fiscal** — Ministerio Público
> 4. **Personero** — Ministerio Público a nivel municipal
> 5. **Defensor de Oficio**
> 6. **Secretario / Oficial Mayor** — personal del Órgano Judicial
> 7. **Otra** — especifica.

Después:
- **¿Tienes preparador?** Sí/No. Si sí, ¿individual o academia?
- **¿Es tu primer intento?** (Primero, segundo...) Si es la primera vez, decir: "El primer concurso es el que más desorienta — es normal. Los ejercicios que te proponga irán ajustándose a tu nivel."
- **¿Tienes las bases oficiales?** Pega o comparte. Si no: "Lo busco yo, pero confirma que sea la convocatoria vigente (Gaceta Oficial) [verificar]."

### Parte 5: Si idoneidad para la abogacía

*(Solo si el objetivo incluye la idoneidad para el ejercicio de la abogacía.)*

> "Sobre el ejercicio de la abogacía en Panamá:"

- **Plazos:** ¿Cuándo prevés tramitar la idoneidad ante la CSJ o iniciar tu práctica profesional?
- **Materias fuertes:** ¿En qué te sientes seguro?
- **Materias débiles:** ¿Qué te cuesta más? (Esto determina dónde concentrar los simulacros.)
- **¿Has hecho simulacros de repaso antes?**
- **¿Título de Licenciatura:** ¿Lo estás cursando ahora? ¿Lo has terminado? ¿Qué requisitos de idoneidad te faltan? [verificar]

## Plantilla del perfil de práctica

```markdown
# Perfil: Estudiante de Derecho

*Escrito por la entrevista inicial el [FECHA]. Edita directamente o ejecuta --redo.*

---

## Quién soy

**Universidad:** [PENDIENTE]
**Año:** [PENDIENTE]
**Especialización interés:** [PENDIENTE / Sin decidir]

---

## Objetivo

**Principal:** [Licenciatura / Posgrado / Concursos de carrera judicial / Idoneidad / Combinado]

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

## Concursos de carrera judicial (si aplica)

**Cargo:** [Juez / Magistrado / Fiscal / Personero / Defensor de Oficio / Secretario u Oficial Mayor / Otro / N/A]
**Preparador:** [Sí — tipo / No / PENDIENTE]
**Intento:** [Primero / Segundo / N.o / PENDIENTE]
**Bases oficiales:** [Disponibles / PENDIENTE]

---

## Idoneidad para la abogacía (si aplica)

**Plazo previsto:** [PENDIENTE / N/A]
**Título de Licenciatura:** [Cursando / Completado / PENDIENTE / N/A]
**Materias fuertes:** [PENDIENTE]
**Materias débiles:** [PENDIENTE]
**Simulacros previos:** [Sí / No / PENDIENTE]

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
> - **Si concursos: exponer temas** — Práctica de exposición oral cronometrada. Prueba: `/estudiante-derecho:cantar`
> - **Si idoneidad: simulacro completo** — Simulacro de repaso integral para la práctica. Prueba: `/estudiante-derecho:simulacro-acceso`
>
> **Mi sugerencia:** Empieza con `/estudiante-derecho:esquema` de un tema que estés estudiando ahora — verás rápido si el formato te sirve.

1. **Resumen.** "Esto es lo que he entendido."
2. **Primera tarea según objetivo:**
   - Licenciatura: "¿Qué asignatura te genera más dudas ahora mismo?"
   - Concursos de carrera judicial: "¿En qué tema del programa estás? Te propongo un ejercicio."
   - Idoneidad: "¿Cuánto tiempo tienes para consolidar conocimientos? Te propongo un plan."
3. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md`.
   >
   > Actualízalo al cambiar de curso, de asignaturas o de objetivo. Ejecuta `--redo` para repetir la entrevista."

4. **Tu perfil aprende:**

   > Los ejercicios se adaptan conforme los usas. Si un test te sale fácil, el siguiente será más difícil. Si un esquema no te sirve, dime qué formato prefieres y lo ajusto.

## Modos de fallo

- **No asumir el nivel.** Un estudiante de 1.o no sabe lo que es una excepción procesal. Un aspirante a juez sí. Adaptar el lenguaje al año.
- **No sustituir al preparador.** Si tiene preparador del concurso, el módulo complementa, no compite. No contradecir el método del preparador sin que el estudiante lo pida.
- **No dar respuestas sin razonamiento.** El objetivo es que el estudiante aprenda, no que copie. Siempre explicar el porqué.
- **No inventar preguntas de examen.** Si el estudiante pide casos prácticos de una asignatura concreta, preguntar si tiene exámenes anteriores reales — son más útiles que los inventados.
- **No ignorar que el programa de cada concurso es específico.** El programa para juez no es el de fiscal. Usar las bases oficiales, no un programa genérico [verificar].
- **No confundir la idoneidad con los concursos de carrera judicial.** Son cosas distintas. La idoneidad habilita para ejercer la abogacía; los concursos de méritos seleccionan para cargos del Órgano Judicial o del Ministerio Público.
