---
name: contencioso-3573-betobetico
title: /contencioso
description: Contencioso-administrativo — guía a través del recurso contencioso- administrativo contra actos de la Administración. Plazos, legitimación, medidas cautelares, costas. Usar cuando el usuario diga "recurso contencioso", "impugnar ante el juzgado", "la Administración no cumple", "me han denegado" o tras agotar la vía administrativa.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/administrativo/skills/contencioso
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: administrative
language: es
---

# /contencioso

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de administración, letrados.
2. Identificar el acto impugnado y la vía administrativa agotada.
3. Analizar legitimación, plazos, órgano competente y viabilidad.
4. Generar informe con estrategia procesal.

```
/administrativo:contencioso
El TEAR ha desestimado nuestra reclamación contra la liquidación de IBI.
Queremos ir al contencioso.
```

---

## Propósito

El recurso contencioso-administrativo (LJCA 29/1998) es la vía judicial de control de la actividad administrativa. Es el paso siguiente cuando la vía administrativa se ha agotado o cuando el acto pone fin directamente a dicha vía. Este skill guía la evaluación de viabilidad, plazos y estrategia del recurso.

---

## Presupuestos del recurso

### 1. Actividad administrativa impugnable (arts. 25-30 LJCA)

| Tipo | Ejemplo |
|---|---|
| Disposiciones generales de rango inferior a ley | Reglamentos, ordenanzas |
| Actos expresos y presuntos (silencio) | Resoluciones, liquidaciones, sanciones |
| Inactividad de la Administración | No ejecución de actos firmes (art. 29) |
| Vía de hecho | Actuación material sin cobertura jurídica (art. 30) |

### 2. Agotamiento de la vía administrativa

El recurso contencioso solo procede contra actos que pongan fin a la vía administrativa (art. 25.1 LJCA):

- Actos contra los que no cabe recurso de alzada
- Resoluciones de recursos de alzada
- Resoluciones de procedimientos sustitutivos
- Actos de órganos sin superior jerárquico

**Excepción:** contra la inactividad y la vía de hecho no se exige agotamiento previo (arts. 29-30 LJCA).

### 3. Legitimación (art. 19 LJCA)

- Personas físicas o jurídicas titulares de un derecho o interés legítimo
- Corporaciones, asociaciones, sindicatos, grupos afectados
- Administración del Estado contra actos de CCAA o EELL (y viceversa)
- Ministerio Fiscal en defensa de la legalidad
- Entidades de derecho público con interés legítimo

### 4. Plazos (art. 46 LJCA)

| Supuesto | Plazo |
|---|---|
| **Acto expreso** | **2 meses** desde notificación |
| **Silencio administrativo o acto presunto** | **6 meses** desde que se produzca el acto presunto |
| **Inactividad** | 2 meses desde la reclamación previa (art. 29.1) |
| **Vía de hecho** | 20 días desde requerimiento previo, o 10 días si no se requirió (art. 30) |
| **Disposición general** | 2 meses desde publicación |

**Los plazos son de caducidad — improrrogables.**

---

## Órgano competente (arts. 8-12 LJCA)

| Órgano | Competencia |
|---|---|
| **Juzgados de lo C-A** | Actos de EELL (salvo CCGG de Planeamiento); personal no funcionario; sanciones <60.000 EUR; extranjería |
| **Salas de lo C-A de los TSJ** | Actos de CCAA; actos de la AGE cuya competencia no sea de la AN; recursos contra actos de EELL de cuantía >60.000 EUR |
| **Audiencia Nacional** | Actos de ministros y secretarios de Estado (salvo los atribuidos a TSJ); actos de organismos estatales con competencia en todo el territorio |
| **Tribunal Supremo** | Disposiciones generales y actos del Consejo de Ministros y Comisiones Delegadas; actos del CGPJ |

---

## Medidas cautelares (arts. 129-136 LJCA)

| Aspecto | Detalle |
|---|---|
| **Regla general** | Pueden adoptarse cuando la ejecución del acto pueda hacer perder la finalidad legítima del recurso (art. 130) |
| **Criterio** | Periculum in mora + ponderación de intereses (no solo fumus boni iuris) |
| **Suspensión** | La medida cautelar más habitual; también cabe adoptar medidas positivas |
| **Caución** | El tribunal puede exigir caución al solicitante (art. 133) |
| **Momento** | Puede solicitarse en cualquier estado del proceso, incluso antes de la interposición (medidas cautelarísimas — art. 135) |

---

## Procedimiento

### Procedimiento ordinario (arts. 45-77 LJCA)

1. **Interposición** del recurso (art. 45) — escrito de interposición + documento del acto
2. **Reclamación del expediente** administrativo (art. 48) — 20 días
3. **Demanda** (art. 52) — 20 días desde recepción del expediente
4. **Contestación** (art. 54) — 20 días
5. **Prueba** (art. 60) — si se solicita: 30 días (15 días para proponer + 15 para practicar)
6. **Conclusiones / vista** (art. 62-65) — 10 días para conclusiones escritas
7. **Sentencia** (art. 67) — 10 días desde conclusiones/vista

### Procedimiento abreviado (art. 78 LJCA)

Para asuntos de cuantía <30.000 EUR ante Juzgados de lo C-A:
- Demanda con la interposición
- Vista oral con prueba y conclusiones
- Sentencia en 10 días

---

## Costas (art. 139 LJCA)

| Regla | Detalle |
|---|---|
| **Primera instancia** | Vencimiento objetivo: cada parte paga las suyas salvo temeridad o mala fe, en cuyo caso se imponen al que litigó así |
| **Recursos** | Se imponen al recurrente si se desestima íntegramente (salvo que el caso presente serias dudas de derecho) |
| **Límite cuantitativo** | El tribunal fija un máximo de costas |

---

## Formato de salida

```markdown
# Viabilidad de recurso contencioso-administrativo

**Acto impugnado:** [descripción]
**Administración demandada:** [nombre]
**Fecha de notificación:** [fecha]
**Plazo para recurrir:** [fecha límite — CRÍTICO]

---

## Presupuestos procesales

| Presupuesto | Estado | Observaciones |
|---|---|---|
| Actividad impugnable | [Sí/No] | [tipo de acto] |
| Agotamiento vía administrativa | [Sí/No] | [vía seguida] |
| Legitimación | [Sí/Dudosa/No] | [fundamento] |
| Plazo | [Dentro/Fuera] | [fecha límite] |
| Órgano competente | [Juzgado/TSJ/AN/TS] | [base competencial] |

---

## Viabilidad del recurso

**Valoración:** [Alta / Media / Baja / Inviable]

[Análisis de fondo: fortalezas y debilidades de la posición]

---

## Medidas cautelares

**¿Procede solicitar suspensión?** [Sí/No]
**Fundamento:** [periculum in mora + ponderación de intereses]
**Caución estimada:** [si procede]

---

## Estrategia procesal

| Aspecto | Recomendación |
|---|---|
| Procedimiento | [Ordinario / Abreviado] |
| Medidas cautelares | [Solicitar / No solicitar] |
| Prueba clave | [qué prueba practicar] |
| Riesgo de costas | [valoración] |

---

## Costes estimados

| Concepto | Estimación |
|---|---|
| Tasa judicial (si procede) | [importe — si aplica] |
| Honorarios letrado | [rango según complejidad] |
| Procurador | [si preceptivo] |
| Pericial | [si necesaria] |
```

---

## Legislación de referencia

- LJCA (Ley 29/1998) — Ley reguladora de la Jurisdicción Contencioso-Administrativa
- LPAC (Ley 39/2015) — agotamiento de la vía administrativa
- LRJSP (Ley 40/2015) — responsabilidad patrimonial
- CE arts. 24 (tutela judicial), 106 (control judicial de la Administración)
- Ley 10/2012 — tasas judiciales (parcialmente vigente)

---

## Lo que este skill NO hace

- No redacta la demanda contencioso-administrativa — analiza la viabilidad y estrategia.
- No sustituye al procurador ni al abogado habilitado para actuar ante la jurisdicción.
- No cubre el recurso de casación contencioso-administrativo en detalle — señala cuándo puede proceder.
