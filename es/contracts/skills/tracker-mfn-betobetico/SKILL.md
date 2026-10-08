---
name: tracker-mfn-betobetico
title: Tracker MFN / Side Letters
description: Matriz viva de side letters firmados, MFN activas, obligaciones contractuales con cada LP. Alertas si nueva concesión activa MFN dormido. Triggers en "tracker MFN", "matriz side letters", "obligaciones LP", "MFN check".
author: betobetico
author_url: https://github.com/betobetico/claude-para-servicios-financieros/tree/main/plugins/verticales/legal-fondos/skills/tracker-mfn
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: contracts
language: es
---

# Tracker MFN / Side Letters

## Paso 0
Carga perfil del usuario. El tracker es vivo — se actualiza tras cada nueva firma o evento.

## Paso 1 — Estructura de la matriz

```markdown
# Matriz Side Letters & MFN — {Fondo} — actualizado {fecha}

## LPs y commitments
| LP | Commitment | Categoría | Firma SL | MFN | Cierre |
|---|---|---|---|---|---|
| LP-001 (Fondo soberano X) | €50M | Anchor | Sí (12/01/2024) | Sí | 1er cierre |
| LP-002 (Pension Fund Y) | €30M | Institutional | Sí (15/02/2024) | Sí | 1er cierre |
| LP-003 (Family Office Z) | €5M | HNW | No | N/A | 1er cierre |
| LP-004 (Fund of Funds W) | €20M | FoF | Sí (10/03/2024) | No (rechazó) | 2do cierre |
| ... | | | | | |

## Side letters activas

### SL-001 — LP-001 (Fondo soberano X)
**Firmada:** 12/01/2024
**Vigente hasta:** Vida del fondo
**Concesiones:**
1. Fee discount: 1.5% gestión (vs 2% estándar) — duración fondo
2. Co-investment rights: prioridad hasta 50% del ticket del fondo en cada deal
3. Advisory board seat (LPAC)
4. Reporting personalizado: trimestral con desglose por geografía
5. MFN: tiene derecho a cualquier concesión más favorable hecha a otros LPs

**Coste anual estimado:** €750k en fees no facturados

### SL-002 — LP-002 (Pension Fund Y)
**Firmada:** 15/02/2024
**Concesiones:**
1. Fee discount: 1.75% gestión (vs 2%)
2. Reporting personalizado: ILPA template + KPIs ESG SFDR
3. ESG exclusions adicionales: sin tabaco, sin armas controvertidas, sin combustibles fósiles
4. MFN: tiene MFN

**Coste anual:** €150k fees + impacto operacional reporting + restricción universo inversión

### SL-003 — LP-004 (FoF W)
**Firmada:** 10/03/2024
**Concesiones:**
1. Capital call notice: 15 días (vs 10 estándar)
2. NO MFN (LP rechazó incluirlo a cambio de un fee discount mayor)

## Most Favoured Nation — Análisis cruzado

LPs con MFN activo: LP-001, LP-002

### Concesiones que activarían MFN si se ofrecen a un nuevo LP

| Concesión potencial | ¿Activa MFN de LP-001? | ¿Activa MFN de LP-002? | Notas |
|---|---|---|---|
| Fee discount <1.5% gestión | Sí (mejor que la suya) | Sí | LP-001 y LP-002 podrían pedir alinear |
| Fee discount 1.5%-1.75% | No (igual o peor) | Sí | LP-002 podría pedir alinear |
| Carry discount | Sí | Sí | Ambos quieren matching |
| Co-investment prioritario distinto | Posible — depende términos | No | Solo LP-001 tiene este derecho |
| Advisory board seat adicional | No (su seat no se diluye) | Posible si modifica governance | |
| Reporting más frecuente que mensual | No | Sí | LP-002 tiene mensual |

## Obligaciones del GP por LP

### LP-001
- [ ] Reporting trimestral con desglose geografía — próximo: {fecha}
- [ ] Notificar inversiones >€10M en 5 días
- [ ] LPAC convocada al menos trimestralmente
- [ ] Co-invest offer obligatoria cada deal >€20M

### LP-002
- [ ] Reporting mensual con KPIs ESG — próximo: {fecha}
- [ ] PAI Statement anual (SFDR) compartida
- [ ] Confirmación trimestral de cumplimiento exclusiones ESG

### LP-004
- [ ] Capital call notice 15 días (vs 10 estándar)
- [ ] Reporting anual ILPA estándar

## Tracker de eventos
| Fecha | Evento | LP afectado | Estado |
|---|---|---|---|
| 12/05/2024 | Reporting Q1 enviado LP-001 | LP-001 | ✅ |
| 15/05/2024 | Reporting M4 enviado LP-002 | LP-002 | ✅ |
| 22/05/2024 | LP-005 propone side letter con fee 1.5% + co-invest | LP-005 (nuevo) | ⚠️ Análisis MFN en curso |

## Alertas activas
- 🚨 **LP-005 propone side letter con fee 1.5%:** activaría MFN de LP-001 (igual) y LP-002 (mejor). Coste adicional estimado: €X. Decisión pendiente.
- 🟡 **Reporting Q2 a LP-001:** próximo deadline {fecha}. Empezar preparación.

## Histórico
{Lista cronológica de side letters firmadas, MFN activadas, renegociaciones}
```

## Paso 2 — Actualización tras nueva firma

Cuando se firma una nueva side letter:
1. Añadir al listado
2. Re-ejecutar el análisis cruzado MFN
3. Si activa MFN: generar lista de LPs a notificar + comunicación

## Paso 3 — Pre-check antes de aceptar nueva concesión

Antes de firmar cualquier nueva side letter:

```markdown
## Pre-check: {Concesión propuesta a LP-X}

### Análisis MFN
- LP-001 tiene MFN: ¿esta concesión es más favorable que las suyas?
  - Concesión propuesta: {X}
  - Equivalente actual LP-001: {Y}
  - **Activa MFN: SÍ / NO**
- LP-002 tiene MFN: ...
- {repetir por cada LP con MFN}

### Impacto si todos los MFN se activan
- Fee discount adicional anual: €X
- Coste operacional adicional: €Y
- Impacto reputacional / gobernanza: ...

### Decisión recomendada
- ✅ Conceder — impacto MFN aceptable
- 🟡 Conceder con caveat — modificar términos para no activar MFN
- 🔴 No conceder — coste MFN excesivo
```

## Paso 4 — Reporting tracking

Genera dashboard de cumplimiento de obligaciones contractuales:

| LP | Obligación próxima | Fecha límite | Días restantes | Status |
|---|---|---|---|---|
| LP-001 | Reporting Q2 | 30/07/2024 | 12 | Pendiente |
| LP-002 | PAI Statement anual | 30/04/2024 | -5 | ⚠️ VENCIDA |

## Paso 5 — Outputs

1. **Matriz consolidada** (markdown + Excel para distribución a equipo)
2. **Análisis MFN** (cuando se evalúa nueva concesión)
3. **Tracking de obligaciones** (dashboard con próximos deadlines)
4. **Alertas** de incumplimientos / MFN activos
5. **Histórico** auditable

## Casos especiales

- **MFN sólo sobre economics** (no sobre governance): limitar análisis a fees y carry
- **MFN limitada por tamaño de commitment** (ejemplo: solo aplica si commitment ≥ €X): documentar restricciones
- **MFN con horizonte temporal** (solo activa por X meses post-firma): tracking de cuándo expira
- **MFN bilateral**: muy raro, pero ambos LPs pueden invocar matching mutuo
- **MFN para futuros fondos** (next fund MFN): tracking inter-fondo

## Cierre

> *Tracker matriz contractual. Mantener actualizado tras cada firma o evento material. Decisiones sobre nuevas concesiones requieren validación GC + Managing Partner + (si activa MFN material) Comité de Inversión. Toda comunicación a LPs sobre MFN debe coordinarse con IR/comunicación.*
