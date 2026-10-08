---
name: company-formation-danielmc09
title: Company Formation
description: '[JURISDICTION] Arma el mapa de pasos para constituir una empresa en la jurisdiccion declarada, con fuentes oficiales, costos, tiempos y lo que no se pudo verificar. Usar cuando se va a formalizar un negocio en un pais concreto.'
author: Danielmc09
author_url: https://github.com/Danielmc09/jurisdiction-latam/tree/main/jurisdiction-kit/skills/company-formation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: corporate
language: es
---

# Company Formation

Un mapa con fuentes. **No un instructivo.**

## Advertencia obligatoria en toda salida

> Esto no es asesoría legal ni contable. Es una guía de investigación con
> fuentes oficiales para llegar preparado a un profesional local. Los
> trámites cambian y varían por ciudad, sector y tipo societario. Verifica
> cada paso en la fuente oficial antes de ejecutarlo.

## Requiere

- `jurisdiction-research` corrido para esa jurisdicción
- **La capa territorial `packs/<iso>/<municipio>.md`**
- El sector, si el negocio declaró uno: `sectors/<iso>/<sector>.md`

### `[CRÍTICO]` Constituir es un trámite local

De las siete áreas de abajo, **al menos cuatro son competencia municipal o
departamental**: el registro mercantil, los impuestos locales, la apertura
de establecimiento y las licencias del sector.

**Si la capa territorial no existe o está vacía, dilo antes de empezar.**
Un mapa de constitución construido solo con la norma nacional le sirve a
nadie: cada paso ocurre ante una entidad local, con su tarifa y su tiempo.

Por cada paso, declara de qué nivel viene la fuente:

```
Nivel: nacional | departamental | municipal
```

## Las siete áreas

1. **Tipo societario** — opciones, responsabilidad, socios mínimos, capital
   mínimo, cuál se usa más para negocios digitales pequeños
2. **Registro mercantil** — **capa territorial**: qué cámara, documentos,
   costo, tiempo, renovación
3. **Identificación tributaria** — cómo se obtiene, qué régimen elegir, qué
   obligaciones dispara cada uno
4. **Obligaciones fiscales periódicas** — nacionales y **locales**: qué se
   declara, cada cuánto, desde qué umbral
5. **Facturación** — si la electrónica es obligatoria, desde cuándo, qué
   proveedor se requiere
6. **Seguridad social y laboral** — qué aplica si eres el único, y qué
   cambia al contratar a la primera persona
7. **Licencias del sector** — del pack sectorial. **Suele ser competencia
   municipal**: verifica el nivel antes de afirmarlo

## Formato por paso

```
### Paso N · <nombre>
Qué es:      <una línea>
Ante quién:  <entidad>
Requisitos:  <lista>
Costo:       <monto> · <moneda> · <año> · [CADUCA]
Tiempo:      <estimado> · fuente
Fuente:      <URL oficial>
Verificado:  <fecha>
Confianza:   ALTA (oficial) | MEDIA (secundaria) | BAJA (no verificado)
```

## Secciones obligatorias al final

```
## Lo que NO pude verificar
- <tema> · PREGUNTAR A: <contador | abogado | cámara de comercio>

## Lo que varía por ciudad o municipio
- <tema> · verificar localmente

## Preguntas para el profesional
1. ...
```

## Regla de completitud — la más importante

**Nunca presentes el mapa como completo.** Cierra siempre con:

> Este mapa cubre los pasos que pude verificar en fuentes oficiales. **No
> garantiza ser exhaustivo.** Los requisitos varían por sector, municipio y
> tipo societario. Confírmalo con un contador o abogado local antes de
> ejecutar.

Un mapa que se presenta como completo y tiene huecos hace más daño que uno
que declara sus límites.

## Guardrails

Aplican los de `CLAUDE.md`. Los críticos aquí:

- **Una norma se registra en el nivel que le corresponde.** Si un requisito
  es municipal, no lo presentes como nacional
- **Los huecos se declaran.** La sección de lo no verificado nunca va vacía
- **No se recomienda, se expone**

## Qué NO hacer

- No recomiendes un tipo societario. **Expón opciones y diferencias**
- No des consejos de optimización tributaria
- No estimes costos sin fuente
- No omitas la sección de lo no verificado. Si está vacía, sospecha de tu
  propia investigación
- No conviertas esto en un "constituye tu empresa en 5 pasos"
