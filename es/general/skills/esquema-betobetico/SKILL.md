---
name: esquema-betobetico
title: /esquema
description: Construye o amplía esquemas de estudio a partir de apuntes, manuales o temas del estudiante. Se adapta al formato preferido del estudiante (mapas conceptuales, esquemas jerárquicos, tablas comparativas). Usar cuando el usuario dice "esquema", "esquematiza", "organiza mis apuntes", "mapa conceptual", "resumen estructurado", o necesita organizar materia de estudio.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/estudiante-derecho/skills/esquema
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: general
language: es
---

# /esquema

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Identificar la materia, el tema y la fuente (apuntes, manual, tema de oposición).
3. Determinar el formato preferido.
4. Generar o ampliar el esquema.

---

## Propósito

Convertir material de estudio (apuntes, temas de manual, notas de clase) en esquemas estructurados que faciliten el aprendizaje y la retención. Se adapta al formato que mejor funcione para cada estudiante.

## Formatos disponibles

### 1. Esquema jerárquico (por defecto)

```
I. CONCEPTO PRINCIPAL
   A. Subconcepto 1
      1. Detalle
      2. Detalle
         a. Sub-detalle
   B. Subconcepto 2
```

Mejor para: temas con estructura lógica clara, preparación de oposiciones (temas orales).

### 2. Tabla comparativa

| Concepto | Tipo A | Tipo B | Tipo C |
|---|---|---|---|
| Definición | | | |
| Requisitos | | | |
| Efectos | | | |
| Plazo | | | |

Mejor para: comparar instituciones jurídicas (tipos de contratos, tipos de recursos, regímenes económicos).

### 3. Mapa conceptual (formato texto)

```
[Concepto central]
├── [Rama 1] → [Consecuencia]
│   ├── [Sub-rama] → [Detalle]
│   └── [Sub-rama] → [Detalle]
├── [Rama 2] → [Consecuencia]
└── [Rama 3] → [Consecuencia]
```

Mejor para: relaciones entre conceptos, visión de conjunto.

### 4. Ficha-resumen

```
TEMA: [nombre]
NORMA CLAVE: [artículos]
CONCEPTO: [definición en una línea]
REQUISITOS: [lista]
EFECTOS: [lista]
EXCEPCIONES: [lista]
JURISPRUDENCIA CLAVE: [referencia — verificar]
TRUCO DE EXAMEN: [lo que siempre preguntan]
```

Mejor para: repaso rápido, última hora antes del examen.

## Reglas de esquematización

- **Fidelidad al contenido.** El esquema refleja lo que dice el material del estudiante, no lo que la IA "sabe". Si el manual dice X y la IA cree que es Y, señalarlo como nota al margen — no corregir silenciosamente.
- **Jerarquía clara.** Lo más importante primero. Los detalles después. No todo tiene el mismo peso.
- **Brevedad.** Un esquema no es un resumen — es una estructura. Si una idea necesita 3 líneas, ponerla en un apartado aparte.
- **Referencias cruzadas.** Si un tema conecta con otro, señalarlo: "Ver también: [tema relacionado]".
- **Marcadores de examen.** Si algo es típico de examen (por experiencia del estudiante o por naturaleza del tema), marcarlo.

## Formato de salida

```markdown
## Esquema: [Materia] — [Tema]

**Fuente:** [manual / apuntes / tema de oposición]
**Formato:** [jerárquico / tabla / mapa / ficha]

---

[Esquema en el formato elegido]

---

**Conexiones con otros temas:**
- [tema relacionado 1] — [por qué conecta]
- [tema relacionado 2] — [por qué conecta]

**Puntos frecuentes de examen:**
- [punto 1]
- [punto 2]

---

**Qué hacer a continuación:**
1. **Ampliar** — profundizo en una sección concreta.
2. **Fichas** — `/estudiante-derecho:fichas` para generar fichas de estudio de este tema.
3. **Socrático** — `/estudiante-derecho:socratico` para poner a prueba lo estudiado.
4. **Otro tema** — esquematizo otro tema.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **No sustituir al estudio.** El esquema es una herramienta de organización, no un sustituto del estudio del material original.
- **No inventar contenido.** Si el estudiante pega sus apuntes, esquematizar lo que hay — no añadir materia que no está.
- **Respetar el manual/programa.** Si el estudiante sigue un manual concreto, usar la estructura de ese manual.
- **Señalar lagunas.** Si los apuntes del estudiante tienen un hueco evidente ("este tema no menciona las excepciones"), señalarlo.
- **No copiar textualmente el manual.** Esquematizar es reformular y estructurar, no copiar.
- **Adaptar al nivel.** Un esquema para un estudiante de primero es distinto de uno para un opositor.
