---
name: procedimiento
title: /procedimiento
description: Procedimiento administrativo — guía a través del procedimiento administrativo común. Cubre plazos (art. 21 LPAC), silencio administrativo (arts. 24-25), recursos administrativos (arts. 112-126) con árbol de decisión para alzada, reposición y revisión extraordinaria. Usar cuando el usuario diga "me han notificado una resolución", "recurso administrativo", "silencio", "plazo para recurrir", "procedimiento administrativo".
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/administrativo/skills/procedimiento
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: regulatory
language: es
---

# /procedimiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de administración, historial.
2. Identificar la fase del procedimiento y el tipo de acto.
3. Analizar plazos, opciones de recurso y silencio.
4. Generar informe con árbol de decisión.

```
/administrativo:procedimiento
Hemos solicitado una licencia de actividad hace 4 meses y no hemos recibido
respuesta. ¿Qué podemos hacer?
```

---

## Propósito

El procedimiento administrativo común (LPAC 39/2015) rige la relación del ciudadano y las empresas con la Administración. Los plazos son estrictos, el silencio administrativo tiene efectos jurídicos concretos y elegir mal el recurso puede cerrar vías. Este skill guía cada paso del procedimiento y ayuda a elegir la vía de impugnación correcta.

---

## Fases del procedimiento administrativo

### 1. Iniciación (arts. 54-69 LPAC)

| Tipo | Características |
|---|---|
| **De oficio** (art. 58) | Por acuerdo del órgano competente, denuncia, petición de otro órgano |
| **A solicitud del interesado** (art. 66) | Modelo normalizado; subsanación de 10 días si incompleta (art. 68) |

### 2. Instrucción (arts. 75-85 LPAC)

Alegaciones, prueba, informes, audiencia al interesado (art. 82 — trámite de audiencia de 10-15 días).

### 3. Resolución (arts. 87-92 LPAC)

**Plazo máximo para resolver y notificar:** El que establezca la norma reguladora del procedimiento. Si no dice nada: **3 meses** (art. 21.3 LPAC).

**Obligación de resolver expresamente** — art. 21.1 LPAC: la Administración está obligada a dictar resolución expresa y a notificarla en todos los procedimientos.

---

## Silencio administrativo (arts. 24-25 LPAC)

### Procedimientos iniciados a solicitud del interesado (art. 24)

| Regla | Efecto |
|---|---|
| **Regla general** | **Silencio positivo** — la solicitud se entiende estimada |
| **Excepciones (silencio negativo)** | Cuando una norma con rango de ley o derecho UE establezca lo contrario; transferencia de facultades sobre dominio público o servicio público; procedimientos de impugnación de actos y disposiciones; ejercicio del derecho de petición (art. 29 CE) |

### Procedimientos iniciados de oficio (art. 25)

| Tipo | Efecto del silencio |
|---|---|
| **Susceptibles de producir efectos favorables** | Silencio negativo (desestimación) |
| **Susceptibles de producir efectos desfavorables (sancionadores, caducidad)** | Caducidad del procedimiento |

---

## Recursos administrativos (arts. 112-126 LPAC)

### Árbol de decisión

```
¿Contra qué acto se recurre?
│
├── Acto que NO pone fin a la vía administrativa
│   └── RECURSO DE ALZADA (art. 121-122 LPAC)
│       ├── Plazo: 1 mes (acto expreso) / 3 meses (silencio)
│       ├── Ante: órgano superior jerárquico
│       └── Resolución: 3 meses; silencio = desestimación
│
├── Acto que SÍ pone fin a la vía administrativa
│   ├── RECURSO POTESTATIVO DE REPOSICIÓN (art. 123-124 LPAC)
│   │   ├── Plazo: 1 mes (acto expreso) / 3 meses (silencio)
│   │   ├── Ante: mismo órgano que dictó el acto
│   │   ├── Resolución: 1 mes; silencio = desestimación
│   │   └── Tras resolución → contencioso-administrativo
│   │
│   └── RECURSO CONTENCIOSO-ADMINISTRATIVO (directamente)
│       └── Plazo: 2 meses (acto expreso) / 6 meses (silencio)
│
└── Actos firmes en vía administrativa
    └── RECURSO EXTRAORDINARIO DE REVISIÓN (art. 125-126 LPAC)
        ├── Causas tasadas (error de hecho, documentos nuevos, sentencia firme, falsedad)
        ├── Plazo: 4 años (error de hecho) / 3 meses (resto de causas)
        └── Ante: mismo órgano que dictó el acto
```

### ¿Qué actos ponen fin a la vía administrativa? (art. 114 LPAC)

- Resoluciones de recursos de alzada
- Resoluciones de procedimientos de impugnación sustitutivos
- Actos de los órganos que carecen de superior jerárquico (ministros, secretarios de Estado, alcaldes en municipios de régimen común...)
- Los que una ley determine expresamente

---

## Plazos clave

| Concepto | Plazo | Base legal |
|---|---|---|
| Resolución del procedimiento (regla general) | 3 meses | Art. 21.3 LPAC |
| Subsanación de solicitud | 10 días | Art. 68 LPAC |
| Trámite de audiencia | 10-15 días | Art. 82 LPAC |
| Recurso de alzada (acto expreso) | 1 mes | Art. 122 LPAC |
| Recurso de alzada (silencio) | 3 meses | Art. 122 LPAC |
| Recurso de reposición (acto expreso) | 1 mes | Art. 124 LPAC |
| Recurso de reposición (silencio) | 3 meses | Art. 124 LPAC |
| Contencioso-administrativo (acto expreso) | 2 meses | Art. 46 LJCA |
| Contencioso-administrativo (silencio) | 6 meses | Art. 46 LJCA |

---

## Notificaciones (arts. 40-46 LPAC)

- Notificación electrónica obligatoria para: personas jurídicas, entidades sin personalidad, profesionales colegiados, empleados públicos (art. 14.2 LPAC)
- Notificación en sede electrónica: si no se accede en 10 días naturales, se entiende rechazada (art. 43.2 LPAC)
- Publicación en BOE/tablón: cuando no se pueda practicar la notificación personal

---

## Formato de salida

```markdown
# Procedimiento administrativo

**Tipo de acto:** [resolución / silencio / requerimiento / notificación]
**Administración actuante:** [AGE / CCAA / EELL / organismo autónomo]
**Fecha de notificación/silencio:** [fecha]
**Plazo para actuar:** [fecha límite — CRÍTICO]

---

## Situación procesal

[Resumen: en qué fase estamos, qué ha pasado, qué opciones hay]

---

## Plazos

| Concepto | Plazo | Fecha límite | Estado |
|---|---|---|---|
| [Ej., Recurso de alzada] | 1 mes | [fecha] | Pendiente |

---

## Opciones de recurso

| Opción | Plazo | Ante quién | Ventajas | Inconvenientes |
|---|---|---|---|---|
| Alzada | 1 mes | Superior jerárquico | Preceptivo si no agota vía | Resuelve la propia Administración |
| Reposición | 1 mes | Mismo órgano | Rápido; potestativo | Mismo órgano revisa |
| Contencioso | 2 meses | TSJ / AN | Juez independiente | Más lento y costoso |

---

## Recomendación

[Análisis razonado de la mejor opción]

---

## Silencio administrativo

**¿Ha transcurrido el plazo para resolver?** [Sí/No]
**Efecto del silencio:** [Positivo / Negativo — con base legal]
```

---

## Legislación de referencia

- LPAC (Ley 39/2015) — Procedimiento Administrativo Común
- LRJSP (Ley 40/2015) — Régimen Jurídico del Sector Público
- LJCA (Ley 29/1998) — Jurisdicción Contencioso-Administrativa
- CE art. 103 (principios de la Administración), art. 106 (control judicial)

---

## Lo que este skill NO hace

- No redacta el recurso administrativo — identifica la vía y la estrategia.
- No presenta escritos ante la Administración — genera el análisis para decisión.
- No cubre procedimientos sectoriales con regulación propia (tributario, urbanístico, sancionador específico) — remite al skill correspondiente.
