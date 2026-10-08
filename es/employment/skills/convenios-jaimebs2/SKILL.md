---
name: convenios-jaimebs2
title: Convenios colectivos en España
description: 'Use when the user asks about collective bargaining agreements (convenios colectivos) in Spain, how to find which agreement applies, REGCON (the public registry), the hierarchy of agreements, ultraactivity, what a convenio regulates, or how collective agreements are published. Triggers on: ''convenio colectivo'', ''convenios colectivos'', ''REGCON'', ''qué convenio me aplica'', ''registro de convenios'', ''negociación colectiva'', ''ultraactividad'', ''convenio de empresa'', ''convenio sectorial'', ''tablas salariales convenio'', ''buscar convenio'', ''ámbito del convenio'', ''jornada convenio'', ''vacaciones convenio'', ''clasificación profesional convenio'', ''salario convenio''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/laboral/convenios
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

# Convenios colectivos en España

Guía completa sobre los convenios colectivos: qué son, cómo saber cuál
te aplica, dónde buscarlos (REGCON), jerarquía, ultraactividad y
contenido habitual.

> Esta skill orienta sobre el sistema de negociación colectiva.
> **No sustituye asesoramiento legal profesional.**

---

## 1. Qué es un convenio colectivo

Un convenio colectivo es un **acuerdo negociado** entre los
representantes de los trabajadores (sindicatos o comités de empresa) y
los empresarios (o sus asociaciones) que regula las condiciones de
trabajo y empleo en un ámbito determinado.

Tiene **fuerza de ley** para las partes incluidas en su ámbito de
aplicación: obliga tanto a empresas como a trabajadores, aunque no
hayan participado en la negociación.

### Marco legal

- **Estatuto de los Trabajadores** (ET), Título III (arts. 82-92):
  `https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430`
- Los convenios se publican en el **BOE** (ámbito estatal), el boletín
  oficial de la comunidad autónoma o el de la provincia, según su ámbito.

---

## 2. Tipos de convenios por ámbito

### 2.1 Convenio de empresa

- Negociado entre la dirección de una empresa y sus representantes de
  los trabajadores.
- Aplica solo a esa empresa (o a un centro de trabajo o grupo de
  empresas).
- Tras la reforma de 2012, tiene **prioridad aplicativa** en determinadas
  materias sobre el convenio sectorial.

### 2.2 Convenio sectorial

Negociado por sindicatos y asociaciones empresariales para un **sector
de actividad** (hostelería, metal, comercio, etc.).

| Ámbito | Ejemplo | Publicación |
|---|---|---|
| **Estatal** | Convenio colectivo estatal de hostelería | BOE |
| **Autonómico** | Convenio del metal de Cataluña | DOGC |
| **Provincial** | Convenio de hostelería de Madrid | BOCM |
| **Comarcal / local** | Convenio de la construcción de Bizkaia | BOB |

### 2.3 Acuerdo marco / acuerdo interprofesional

Pactos de nivel superior que fijan la estructura de la negociación
colectiva en un sector o a nivel intersectorial.

---

## 3. Jerarquía y prioridad aplicativa

Tras la reforma laboral de 2012 (Ley 3/2012) y la de 2022 (RDL 32/2021):

### Materias con prioridad del convenio de empresa

El convenio de empresa tiene **prioridad aplicativa** (no puede ser
desplazado por uno sectorial) en:

1. Cuantía del salario base y complementos salariales.
2. Compensación de horas extraordinarias y retribución de trabajo a
   turnos.
3. Horario, distribución del tiempo de trabajo, vacaciones y adaptación
   de la clasificación profesional.
4. Modalidades de contratación (dentro de los límites legales).
5. Medidas de conciliación.

### Materias donde el convenio sectorial prevalece

En el resto de materias no listadas, aplica la regla general: el
convenio de ámbito superior establece las condiciones mínimas que el
inferior puede mejorar.

### Reforma 2022: recuperación del convenio sectorial en subcontratación

La reforma laboral de 2022 estableció que a los trabajadores de empresas
contratistas y subcontratistas se les aplica el convenio del **sector de
la actividad desarrollada** (no el de la empresa contratista si es
inferior). Esto fue un cambio importante para evitar la precarización
vía subcontratación.

---

## 4. Qué regula un convenio colectivo

### Contenido habitual

| Materia | Qué establece |
|---|---|
| **Salarios** | Tablas salariales por categoría profesional, complementos, revisión salarial |
| **Jornada** | Horas anuales, distribución, jornada máxima semanal/diaria |
| **Vacaciones** | Duración (mínimo 30 días naturales por ley), periodo de disfrute |
| **Permisos y licencias** | Matrimonio, nacimiento, fallecimiento, mudanza, exámenes, etc. |
| **Clasificación profesional** | Grupos y niveles profesionales, funciones de cada categoría |
| **Periodo de prueba** | Duración según categoría (dentro de los límites legales) |
| **Horas extraordinarias** | Retribución o compensación con descanso |
| **Complementos** | Antigüedad, nocturnidad, toxicidad, transporte, dietas |
| **Régimen disciplinario** | Faltas leves, graves y muy graves, sanciones |
| **Igualdad** | Planes de igualdad, protocolo de acoso, medidas de conciliación |
| **Formación** | Permisos para formación, planes formativos |
| **Salud laboral** | Medidas adicionales de prevención de riesgos laborales |

### Contenido mínimo obligatorio

Todo convenio debe incluir (ET art. 85.3):

- Partes que lo conciertan.
- Ámbito personal, funcional, territorial y temporal.
- Procedimientos de resolución de discrepancias (inaplicación del convenio).
- Forma y plazo de denuncia.
- Comisión paritaria (composición, funciones, procedimientos).

---

## 5. REGCON — Registro de Convenios Colectivos

El **REGCON** es el registro público del Ministerio de Trabajo donde se
inscriben todos los convenios colectivos. Es la herramienta principal
para buscar qué convenio aplica.

### Buscador público

URL: `https://expinterweb.mites.gob.es/regcon/pub/consultaPublicaCondec`

### Cómo buscar tu convenio

1. Accede al buscador del REGCON.
2. Filtra por:
   - **Tipo**: convenio, acuerdo, laudo arbitral.
   - **Ámbito territorial**: estatal, autonómico, provincial.
   - **Sector de actividad** (código CNAE o descripción).
   - **Texto libre**: nombre del convenio o del sector.
3. Descarga el texto completo del convenio.

### Consejos para encontrar tu convenio

- Si no sabes el sector, busca por el **código CNAE** de la empresa
  (aparece en el contrato de trabajo o en la vida laboral).
- Si hay duda entre dos convenios, el que aplica es el del **sector de
  actividad real** de la empresa (no su denominación social).
- Si la empresa tiene convenio propio, pregunta a los representantes de
  los trabajadores o a RRHH.

---

## 6. Ultraactividad

La **ultraactividad** es la vigencia del convenio colectivo una vez
que ha expirado su periodo de duración y no se ha negociado uno nuevo.

### Regla actual (tras reforma 2022)

La reforma laboral de 2022 modificó el artículo 86.3 del ET: cuando un
convenio colectivo pierde su vigencia y no se ha alcanzado un nuevo
acuerdo, **se mantienen las condiciones del convenio anterior
indefinidamente** hasta que se negocie uno nuevo.

Esto revirtió la reforma de 2012, que establecía un límite de 1 año
de ultraactividad (tras el cual se aplicaba el convenio de ámbito
superior).

### Implicaciones prácticas

- El convenio caducado sigue siendo plenamente aplicable.
- Las tablas salariales del convenio caducado se mantienen (aunque pueden
  quedar desactualizadas si no hay cláusula de revisión salarial).
- La empresa no puede reducir condiciones alegando que el convenio ha
  caducado.

---

## 7. Inaplicación del convenio (descuelgue)

Una empresa puede **dejar de aplicar** determinadas condiciones de un
convenio colectivo de ámbito superior cuando concurran causas ETOP
(económicas, técnicas, organizativas o de producción).

### Materias susceptibles de descuelgue

- Jornada de trabajo.
- Horario y distribución del tiempo.
- Régimen de trabajo a turnos.
- Sistema de remuneración y cuantía salarial.
- Sistema de trabajo y rendimiento.
- Funciones (movilidad funcional).
- Mejoras voluntarias de la Seguridad Social.

### Procedimiento

1. Periodo de consultas con los representantes (máximo 15 días).
2. Si hay acuerdo, se comunica a la autoridad laboral y a la comisión
   paritaria del convenio.
3. Si no hay acuerdo, se acude a la comisión paritaria y, en su caso,
   a los procedimientos de mediación (SIMA a nivel estatal) o a la
   CCNCC (Comisión Consultiva Nacional de Convenios Colectivos).

---

## 8. Publicación de convenios

| Ámbito | Dónde se publica |
|---|---|
| Estatal | BOE (Boletín Oficial del Estado) |
| Autonómico | Diario oficial de la comunidad autónoma (DOGC, BOJA, DOCV, etc.) |
| Provincial | Boletín oficial de la provincia (BOP) |

Todos los convenios, independientemente de su ámbito, se inscriben en
el REGCON.

Para buscar un convenio publicado en el BOE, se puede usar también:
`https://www.boe.es/legislacion/codigos/codigo.php?id=236`

---

## 9. Comisión paritaria

Todo convenio colectivo debe crear una **comisión paritaria** formada
por representantes de ambas partes (empresarial y sindical).

### Funciones

- Interpretar el convenio.
- Resolver discrepancias sobre su aplicación.
- Intervenir en la inaplicación del convenio (descuelgue).
- Conocer las reclamaciones antes de acudir a la vía judicial
  (trámite previo y preceptivo en muchos convenios).

---

## 10. Resumen rápido

```
CONVENIO COLECTIVO
├── Empresa (prioridad en salarios, horarios, etc.)
├── Sectorial estatal (BOE)
├── Sectorial autonómico (diario oficial CCAA)
└── Sectorial provincial (BOP)

CÓMO ENCONTRAR TU CONVENIO
├── 1. Busca en REGCON (buscador público del Ministerio)
├── 2. Filtra por sector CNAE y ámbito territorial
├── 3. Si la empresa tiene convenio propio, pregunta a RRHH
└── 4. En caso de duda, el que aplica es el del sector de actividad real

ULTRAACTIVIDAD (reforma 2022)
└── El convenio caducado sigue vigente indefinidamente hasta que se negocie uno nuevo

DESCUELGUE
├── Causas ETOP
├── Periodo de consultas
└── Si no hay acuerdo → mediación / CCNCC
```

---

## Cuándo NO usar esta skill

- Si pregunta por **tipos de contrato** → **laboral-contratos**.
- Si pregunta por **cómo leer una nómina** → **laboral-nominas**.
- Si pregunta por **prestación por desempleo** → **laboral-desempleo**.
- Si pregunta por **ERE o ERTE** → **laboral-ere-erte**.
- Si pregunta por **Inspección de Trabajo** o denuncias →
  **laboral-inspeccion**.
- Si pregunta por **estadísticas de paro** registrado → **sepe**.
- Si pregunta por **cotizaciones a la Seguridad Social** →
  **seguridad-social**.
- Si pregunta por **obligaciones fiscales del autónomo** →
  **fiscalidad-autonomos**.
- Si pregunta por el **texto de una ley** concreta → **boe**.
