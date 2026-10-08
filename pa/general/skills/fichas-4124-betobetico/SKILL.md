---
name: fichas-4124-betobetico
title: /fichas
description: Genera y practica fichas de estudio (flashcards) con sistema Leitner de repetición espaciada. Categoriza por materia y tema. Permite generar fichas nuevas desde apuntes o practicar fichas existentes con el sistema de cajas. Usar cuando el usuario dice "fichas de estudio", "flashcards", "repaso con fichas", "genera fichas", "Leitner", o quiere estudiar con repetición espaciada.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/estudiante-derecho/skills/fichas
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: general
language: es
---

# /fichas

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Leer fichas existentes: `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/fichas.yaml`.
3. Ejecutar la acción solicitada.
4. Escribir fichas actualizadas.

---

## Propósito

Facilitar el aprendizaje mediante fichas de estudio con repetición espaciada (sistema Leitner). Las fichas sirven para memorizar conceptos clave, definiciones, artículos y reglas que el estudiante necesita tener disponibles de forma automática.

## Sistema Leitner

El sistema Leitner organiza las fichas en 5 cajas según el nivel de dominio:

| Caja | Frecuencia de repaso | Criterio para avanzar | Criterio para retroceder |
|---|---|---|---|
| Caja 1 | Cada sesión | Acertar 1 vez | — (fichas nuevas empiezan aquí) |
| Caja 2 | Cada 2 sesiones | Acertar 2 veces consecutivas | Fallar → Caja 1 |
| Caja 3 | Cada 4 sesiones | Acertar 2 veces consecutivas | Fallar → Caja 1 |
| Caja 4 | Cada 8 sesiones | Acertar 2 veces consecutivas | Fallar → Caja 2 |
| Caja 5 | Cada 16 sesiones | — (dominada) | Fallar → Caja 2 |

## Acciones

### Generar fichas

```
/estudiante-derecho:fichas generar [materia] [tema]
```

Genera fichas a partir de:
- Apuntes pegados por el estudiante.
- Un tema del programa indicado por número.
- Una sesión socrática o IRAC anterior.

**Tipos de fichas:**

| Tipo | Frente | Dorso | Ejemplo |
|---|---|---|---|
| Definición | Concepto | Definición + artículo | "Contrato de compraventa" → "Código Civil de Panamá, art. correspondiente: ... [verificar]" |
| Artículo | N.o de artículo | Contenido esencial | "Art. del Código Civil de Panamá sobre responsabilidad civil extracontractual [verificar]" → "Responsabilidad civil extracontractual: ..." |
| Regla | Enunciado de la regla | Explicación + excepciones | "Plazo de prescripción de la acción de responsabilidad civil extracontractual" → "[plazo según el Código Civil de Panamá] [verificar]" |
| Comparación | "Diferencia entre X e Y" | Tabla comparativa breve | |
| Caso | Supuesto breve | Solución + artículo | |

### Practicar fichas

```
/estudiante-derecho:fichas practicar [materia]
```

- Selecciona fichas según el sistema Leitner (prioriza Caja 1 y 2).
- Muestra el frente, espera la respuesta del estudiante.
- Evalúa: correcto / parcial / incorrecto.
- Mueve la ficha a la caja correspondiente.
- Al final de la sesión: resumen de rendimiento.

### Listar fichas

```
/estudiante-derecho:fichas listar [materia]
```

Muestra todas las fichas organizadas por materia, tema y caja.

## Formato de fichas (fichas.yaml)

```yaml
fichas:
  - id: F-001
    materia: "civil"
    tema: "Obligaciones y contratos"
    tipo: "definicion"
    frente: "Contrato de compraventa"
    dorso: "Código Civil de Panamá [verificar art.]: Por el contrato de compraventa uno de los contratantes se obliga a entregar una cosa determinada y el otro a pagar por ella un precio cierto."
    caja: 1
    sesiones_en_caja: 0
    aciertos_consecutivos: 0
    ultima_practica: null
```

## Formato de salida (sesión de práctica)

```markdown
## Sesión de fichas — [Materia]

**Fichas en esta sesión:** [N]
**Distribución:** Caja 1: [N] | Caja 2: [N] | Caja 3: [N] | Caja 4: [N] | Caja 5: [N]

---

### Ficha 1 / [N]

**[FRENTE]**

[Texto del frente de la ficha]

---

*Tu respuesta:* [el estudiante responde]

**[DORSO]**

[Texto del dorso]

**Resultado:** [Correcto / Parcial / Incorrecto]
**Movimiento:** [Caja X → Caja Y]

---

[Repetir para cada ficha]

### Resumen de la sesión

| Resultado | Cantidad | % |
|---|---|---|
| Correcto | [N] | [%] |
| Parcial | [N] | [%] |
| Incorrecto | [N] | [%] |

**Fichas dominadas (Caja 5):** [N] / [total]
**Áreas débiles:** [temas con más errores]

---

**Qué hacer a continuación:**
1. **Repasar errores** — repaso las fichas que has fallado.
2. **Generar más fichas** — sobre los temas donde fallas.
3. **Esquema** — `/estudiante-derecho:esquema` del tema con más errores.
4. **Siguiente sesión** — la próxima sesión incluirá [N] fichas según el calendario Leitner.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **Las fichas son para memorización, no para comprensión.** Si el estudiante no entiende un concepto, no sirve memorizarlo. Derivar a `/estudiante-derecho:socratico` o `/estudiante-derecho:esquema` primero.
- **No generar cientos de fichas de golpe.** Mejor 20 fichas bien hechas que 200 que nunca se practican. Sugerir 10-20 por sesión.
- **Evaluar con generosidad razonable.** Si el estudiante dice lo esencial aunque no sea literal, es correcto. Si omite un elemento clave, es parcial.
- **No inventar artículos.** Los números de artículo en las fichas deben ser correctos. Si no estás seguro, marcar `[verificar]`.
- **El sistema Leitner requiere constancia.** Si el estudiante no practica regularmente, advertir que la repetición espaciada solo funciona con regularidad.
- **Adaptar al nivel.** Fichas de primer año de derecho civil son distintas de fichas para concursos de la carrera judicial.
