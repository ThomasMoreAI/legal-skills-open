---
name: investigacion-betobetico
title: /investigacion
description: 'Genera una hoja de ruta de investigación jurídica: legislación a consultar, áreas de jurisprudencia a buscar, términos de búsqueda para el Registro Judicial del Órgano Judicial y otras bases de datos. NO produce citas — produce pistas y direcciones de investigación. Usar cuando el usuario dice "necesito investigar", "hoja de ruta", "por dónde empiezo a buscar", "búsqueda jurisprudencial", o necesita planificar la investigación de un caso.'
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/clinica-juridica/skills/investigacion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: litigation
language: es
---

# /investigacion

1. Leer `~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md` — perfil del consultorio.
2. Cargar el memo de caso si existe.
3. Identificar las cuestiones a investigar.
4. Generar la hoja de ruta con fuentes y términos de búsqueda.

---

## Propósito

Producir una hoja de ruta de investigación jurídica que guíe al alumno hacia las fuentes correctas. NO produce citas ni jurisprudencia — produce las direcciones, los términos de búsqueda y las fuentes donde buscar. La investigación real la hace el alumno.

## ADVERTENCIA

> **Este skill NO cita jurisprudencia ni doctrina.** Las citas de una IA son poco fiables — pueden ser fabricadas, desactualizadas o mal contextualizadas. Lo que sí hace: te dice DÓNDE buscar, CON QUÉ términos, y QUÉ buscar exactamente. La investigación la haces tú en las fuentes primarias.

## Estructura de la hoja de ruta

### 1. Legislación a consultar

Para cada cuestión jurídica identificada:

| Norma | Artículos relevantes | Por qué consultarla | Dónde encontrarla |
|---|---|---|---|
| [norma] | [artículos] | [relevancia para el caso] | Gaceta Oficial (gacetaoficial.gob.pa), Órgano Judicial (organojudicial.gob.pa) |

### 2. Jurisprudencia a buscar

Para cada cuestión, generar estrategia de búsqueda en el Registro Judicial / buscador del Órgano Judicial:

| Cuestión | Tribunal objetivo | Términos de búsqueda | Tipo de resolución | Periodo |
|---|---|---|---|---|
| [cuestión] | [CSJ / Tribunal Superior / juzgado de circuito] | "[término 1]" AND "[término 2]" | Fallo / sentencia | Últimos 5 años |

**Estrategia de búsqueda en el Órgano Judicial (organojudicial.gob.pa):**

- Usar comillas para frases exactas.
- Combinar con AND, OR, NOT.
- Filtrar por tribunal: Corte Suprema de Justicia para doctrina general, Tribunal Superior del distrito judicial para criterios locales.
- Buscar primero fallos de la CSJ — si hay doctrina de la Sala correspondiente de la CSJ, es la referencia.
- Si no hay de la CSJ, buscar en el Tribunal Superior del distrito judicial del caso.
- Buscar también en tribunales de otros distritos judiciales para jurisprudencia menor.

### 3. Doctrina y comentarios

| Tema | Qué buscar | Dónde |
|---|---|---|
| [tema] | [tipo de comentario — monografía, artículo, manual] | Bibliotecas universitarias, repositorios académicos, revistas jurídicas panameñas |

### 4. Otras fuentes

| Fuente | Qué buscar | URL/Acceso |
|---|---|---|
| ANTAI (resoluciones) | Si hay componente de datos personales o transparencia | antai.gob.pa |
| Registro Público de Panamá | Si hay cuestión registral o societaria | registro-publico.gob.pa |
| DGI / Tribunal Administrativo Tributario | Si hay cuestión tributaria | dgi.mef.gob.pa |
| Defensoría del Pueblo | Si hay cuestión administrativa o de derechos humanos | defensoria.gob.pa |

## Formato de salida

```markdown
HOJA DE RUTA DE INVESTIGACIÓN — CONSULTORIO JURÍDICO

## Caso: [Referencia]
**Cuestiones a investigar:** [lista de cuestiones del memo]

---

### Legislación

| N.o | Norma | Artículos | Relevancia |
|---|---|---|---|
| 1 | [norma] | [arts.] | [para qué] |

### Búsquedas en el Órgano Judicial

| N.o | Cuestión | Búsqueda sugerida | Tribunal | Notas |
|---|---|---|---|---|
| 1 | [cuestión] | "[términos]" | [tribunal] | [qué buscar en las sentencias] |

### Doctrina

| N.o | Tema | Fuente sugerida | Qué buscar |
|---|---|---|---|
| 1 | [tema] | [base de datos / manual] | [tipo de comentario] |

### Otras fuentes

| N.o | Fuente | Búsqueda | Acceso |
|---|---|---|---|
| 1 | [fuente] | [qué buscar] | [URL] |

### Checklist de investigación

- [ ] Legislación: [norma 1] consultada y anotada
- [ ] Legislación: [norma 2] consultada y anotada
- [ ] Órgano Judicial: búsqueda [1] realizada — [N] resultados relevantes encontrados
- [ ] Doctrina: [fuente] consultada
- [ ] Hallazgos incorporados al memo de caso

---

**Qué hacer a continuación:**
1. **Buscar en el Órgano Judicial** — usa los términos sugeridos y filtra como se indica.
2. **Actualizar memo** — `/clinica-juridica:memo` con los hallazgos de la investigación.
3. **Consultar al supervisor** — si la investigación revela complejidad inesperada.
4. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **NO citar jurisprudencia.** Este skill produce pistas de investigación, no citas. Las citas las obtiene el alumno de las fuentes primarias.
- **Los términos de búsqueda son sugerencias.** El alumno debe adaptarlos y refinarlos según los resultados que encuentre.
- **Priorizar fuentes primarias.** Órgano Judicial, Gaceta Oficial, bases de datos oficiales. Los resúmenes de terceros (bufetes, blogs) son pistas, no fuentes.
- **La investigación es un proceso iterativo.** Lo que encuentre el alumno puede abrir nuevas líneas de investigación no previstas en esta hoja de ruta.
- **Señalar cuando la cuestión es novedosa.** Si no hay jurisprudencia clara, decirlo — "no encontrar nada" es un resultado de investigación válido que el supervisor necesita conocer.
