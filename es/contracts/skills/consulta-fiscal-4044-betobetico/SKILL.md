---
name: consulta-fiscal-4044-betobetico
title: /consulta
description: Consulta tributaria rápida — responde preguntas fiscales con referencia a legislación vigente y consultas vinculantes de la DGT cuando existan. Marca cuando la respuesta depende de interpretación o jurisprudencia pendiente. Usar cuando el usuario pregunte "¿cómo tributa...?", "¿puedo deducir...?", "consulta fiscal", "IVA de...", "retención de...".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/fiscal/skills/consulta
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# /consulta

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen fiscal, sector.
2. Recibir la consulta.
3. Analizar contra la normativa vigente.
4. Buscar consultas vinculantes de la DGT relevantes.
5. Emitir respuesta con citas.

```
/fiscal:consulta
¿Cómo tributa la venta de un local comercial por una sociedad a un particular?
¿IVA o ITP?
```

---

## Propósito

Las consultas tributarias del día a día necesitan respuestas rápidas, fundamentadas y con las citas correctas. Este skill responde citando siempre el artículo de ley aplicable y, cuando existe, la consulta vinculante de la DGT que soporta la interpretación. Marca explícitamente cuando la respuesta depende de interpretación o hay jurisprudencia contradictoria.

---

## Estructura de la respuesta

Toda respuesta incluye obligatoriamente:

1. **Respuesta directa** — 2-4 frases claras con la conclusión
2. **Artículo de ley** — siempre citar el artículo concreto de la norma (LIVA, LIS, LIRPF, LGT, LITPAJD, etc.)
3. **Consulta vinculante DGT** — si existe una consulta vinculante (V####-##) que respalde la posición, citarla con fecha y referencia
4. **Jurisprudencia** — si hay sentencias relevantes del TS, AN o TSJ
5. **Alertas** — marcar explícitamente cuando:
   - La respuesta depende de una interpretación discutible → `[interpretación — verificar]`
   - Hay jurisprudencia contradictoria → `[jurisprudencia dividida — verificar]`
   - Hay un cambio normativo reciente o pendiente → `[cambio normativo — verificar]`
   - La DGT ha cambiado de criterio → `[cambio de criterio DGT — verificar]`

---

## Áreas cubiertas

| Área | Normativa principal |
|---|---|
| IVA | LIVA (Ley 37/1992), RIVA (RD 1624/1992) |
| Impuesto sobre Sociedades | LIS (Ley 27/2014) |
| IRPF | LIRPF (Ley 35/2006), RIRPF (RD 439/2007) |
| ITP y AJD | LITPAJD (RDLeg 1/1993) |
| Procedimientos tributarios | LGT (Ley 58/2003) |
| Impuestos especiales | Ley 38/1992 |
| Aduanas | CAU (Rto. UE 952/2013) |
| Tributos locales | TRLHL (RDLeg 2/2004) |
| Fiscalidad internacional | CDI, LIRNR (RDLeg 5/2004) |

---

## Consultas vinculantes de la DGT

Las consultas vinculantes de la DGT (art. 89 LGT) son la interpretación oficial de la Administración. Son vinculantes para:
- Los órganos de la Administración tributaria encargados de la aplicación de los tributos
- NO son vinculantes para los tribunales

Al citar consultas:
- Referencia completa: V####-## de [fecha]
- Indicar si es criterio consolidado o ha habido cambio de criterio
- Si no existe consulta aplicable, indicarlo expresamente

---

## Formato de salida

```markdown
# Consulta tributaria

**Pregunta:** [la pregunta del usuario]
**Fecha:** [fecha]

---

## Respuesta

[2-4 frases con la conclusión clara]

---

## Fundamento

**Normativa:**
- [Ley] art. [X]: [contenido relevante]
- [Ley] art. [Y]: [si hay más de una norma aplicable]

**Consultas vinculantes DGT:**
- V####-## de [fecha]: [resumen de la conclusión de la consulta]
- [Si no hay consulta aplicable: "No se ha localizado consulta vinculante directamente aplicable"]

**Jurisprudencia:**
- [Si existe: STS/SAN/STSJ de [fecha], recurso [número]: resumen]
- [Si no: "Sin jurisprudencia relevante identificada"]

---

## Alertas

[Si aplica alguna de las marcas de verificación, incluirlas aquí.
Si no: "Sin alertas."]

---

## Ejemplo práctico

[Si ayuda a la comprensión: un ejemplo numérico concreto]
```

---

## Legislación de referencia

- LGT (Ley 58/2003) — arts. 88-89 (consultas tributarias escritas)
- LIVA (Ley 37/1992)
- LIS (Ley 27/2014)
- LIRPF (Ley 35/2006)
- LITPAJD (RDLeg 1/1993)
- LIRNR (RDLeg 5/2004)
- Base de datos de consultas vinculantes de la DGT (petete.tributos.hacienda.gob.es)

---

## Lo que este skill NO hace

- No sustituye una consulta vinculante formal ante la DGT — es una orientación profesional.
- No cubre fiscalidad de CCAA en detalle (solo remite a la normativa autonómica cuando aplica).
- No calcula cuotas — para eso, usar `/fiscal:revision` o una herramienta de cálculo.
