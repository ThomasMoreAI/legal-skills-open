---
name: alertas-4043-betobetico
title: /alertas
description: Alertas regulatorias (agente programado) — monitoriza la Gaceta Oficial de Panamá y los acuerdos de la SBP, la SMV y la UAF para detectar cambios normativos relevantes. Filtra por sector y umbral de materialidad configurados. Genera un digest con evaluación de relevancia. Usar para configurar o ejecutar bajo demanda diciendo "alertas regulatorias", "¿hay novedades?", "digest normativo".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/regulatorio/skills/alertas
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: regulatory
language: es
---

# /alertas

1. Cargar `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md` → sectores, umbrales de materialidad, fuentes, frecuencia.
2. Si `--configurar`: configurar las fuentes, sectores y frecuencia.
3. Si `--ejecutar` o sin flag: consultar fuentes y generar digest.
4. Filtrar por materialidad y sector.
5. Generar digest con evaluación de relevancia.

```
/regulatorio:alertas --ejecutar
```

---

## Propósito

El entorno regulatorio panameño es denso y disperso: Gaceta Oficial, acuerdos de la Superintendencia de Bancos, acuerdos y opiniones de la SMV, guías y tipologías de la UAF, resoluciones de otros supervisores sectoriales. Perderse una norma relevante es un riesgo real, sobre todo en materia de prevención de blanqueo. Este skill actúa como filtro inteligente: monitoriza las fuentes, evalúa la relevancia para la organización y genera un digest con solo lo que importa.

---

## Fuentes monitorizadas

| Fuente | URL base | Tipo | Frecuencia |
|---|---|---|---|
| **Gaceta Oficial de Panamá** | gacetaoficial.gob.pa [verificar] | Legislación nacional | Diaria |
| **Superintendencia de Bancos (SBP)** | superbancos.gob.pa [verificar] | Acuerdos, circulares | Semanal |
| **SMV** | supervalores.gob.pa [verificar] | Acuerdos, opiniones | Semanal |
| **UAF** | uaf.gob.pa [verificar] | Guías, tipologías, avisos | Semanal |
| **ANTAI** | antai.gob.pa [verificar] | Protección de datos | Semanal |
| **ACODECO** | acodeco.gob.pa [verificar] | Consumo y competencia | Semanal |
| **Otras autoridades sectoriales** | [según config] | [según sector] | [según config] |

Solo se monitorizan las fuentes configuradas en el perfil de práctica.

---

## Filtros

### Filtro por sector

Solo se incluyen normas que afecten a los sectores configurados en el perfil:
- [Según `~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md`]

### Filtro por materialidad

| Nivel | Criterio | Incluir en digest |
|---|---|---|
| **Alta** | Afecta directamente a la actividad; requiere acción | Siempre |
| **Media** | Relevante para el sector; puede requerir seguimiento | Siempre |
| **Baja** | Tangencialmente relevante; no requiere acción inmediata | Solo si se pide |
| **No material** | No afecta a los sectores configurados | Excluir |

---

## Evaluación de relevancia

Para cada norma detectada, evaluar:

1. **¿Afecta a nuestro sector?** — Según los sectores configurados
2. **¿Modifica obligaciones existentes?** — ¿Hay que cambiar algo?
3. **¿Crea obligaciones nuevas?** — ¿Hay que hacer algo nuevo?
4. **¿Tiene período transitorio?** — ¿Cuánto tiempo hay para adaptarse?
5. **¿Afecta a nuestras políticas internas?** — ¿Genera un gap?

---

## Formato del digest

```markdown
# Digest regulatorio — [Período]

**Fecha de generación:** [fecha]
**Período cubierto:** [desde — hasta]
**Sectores monitorizados:** [lista]

---

## Resumen

| Materialidad | Cantidad |
|---|---|
| Alta | [N] |
| Media | [N] |
| Baja | [N] |
| **Total relevantes** | **[N]** |

---

## Alertas de materialidad ALTA

### [Título de la norma]

| Campo | Detalle |
|---|---|
| **Referencia** | [tipo de norma, número, fecha, fuente] |
| **Publicación** | [Gaceta Oficial / acuerdo SBP / acuerdo SMV / guía UAF — fecha] |
| **Entrada en vigor** | [fecha] |
| **Período transitorio** | [si existe] |
| **Sector afectado** | [sector] |
| **Relevancia** | [2-3 frases: por qué importa] |
| **Impacto estimado** | [qué políticas/procedimientos afecta] |
| **Acción recomendada** | [Ej., Ejecutar `/regulatorio:diff` para analizar el impacto] |

---

## Alertas de materialidad MEDIA

[Formato más compacto: tabla resumen]

| # | Norma | Fecha | Sector | Relevancia | Acción |
|---|---|---|---|---|---|
| 1 | [referencia] | [fecha] | [sector] | [1 frase] | [Ej., Seguimiento] |

---

## Próxima ejecución programada

[Fecha y hora, si está configurado como agente programado]
```

---

## Configuración como agente programado

Si el entorno soporta tareas programadas:

| Parámetro | Valor |
|---|---|
| **Frecuencia** | [Diaria / Semanal / Quincenal] |
| **Día preferido** | [Lunes por la mañana, ej.] |
| **Canal de notificación** | [Email / Slack / inline] |
| **Destinatario** | [persona o equipo] |

Configurar con `/regulatorio:alertas --configurar`.

---

## Legislación de referencia

- Constitución Política de la República de Panamá (publicidad de normas) [verificar]
- Código Civil de Panamá (entrada en vigor de las leyes tras su promulgación en la Gaceta Oficial, salvo disposición contraria) [verificar]
- Ley 23 de 2015 y normativa sectorial según configuración (acuerdos de la SBP y de la SMV, guías de la UAF) [verificar]

---

## Lo que este skill NO hace

- No analiza en profundidad el impacto de cada norma — para eso, usar `/regulatorio:diff`.
- No propone redacciones de actualización — para eso, usar `/regulatorio:redaccion`.
- No accede a fuentes de pago (bases de datos legislativas premium) — trabaja con fuentes públicas.
