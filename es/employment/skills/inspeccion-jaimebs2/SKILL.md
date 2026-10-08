---
name: inspeccion-jaimebs2
title: Inspección de Trabajo y Seguridad Social (ITSS)
description: 'Use when the user asks about the Spanish Labour Inspectorate (Inspección de Trabajo, ITSS), how to file a labour complaint, workplace violations, labour sanctions, unpaid wages, undeclared work, workplace safety violations, anonymous complaints, or the inspection process. Triggers on: ''inspección de trabajo'', ''ITSS'', ''denuncia laboral'', ''denunciar empresa'', ''denunciar a mi jefe'', ''impago de salario'', ''horas extra no pagadas'', ''economía sumergida'', ''trabajo en negro'', ''sin contrato'', ''acoso laboral denuncia'', ''riesgos laborales denuncia'', ''sanción laboral'', ''infracción laboral'', ''buzón de denuncias'', ''garantía de indemnidad'', ''represalias denuncia''.'
author: jaimebs2
author_url: https://github.com/jaimebs2/OpenSpain/tree/main/openspain/skills/laboral/inspeccion
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: employment
language: es
---

# Inspección de Trabajo y Seguridad Social (ITSS)

Guía completa sobre la Inspección de Trabajo: qué es, cómo presentar
una denuncia, motivos habituales, proceso inspector, sanciones y
protección del denunciante.

> Esta skill es puramente informativa. **No automatiza ni tramita
> denuncias.** No sustituye asesoramiento legal profesional.

---

## 1. Qué es la Inspección de Trabajo

La **Inspección de Trabajo y Seguridad Social (ITSS)** es el organismo
público encargado de **vigilar el cumplimiento de la normativa laboral,
de Seguridad Social y de prevención de riesgos laborales** en España.

Depende del **Ministerio de Trabajo y Economía Social**.

URL oficial: `https://www.mites.gob.es/itss/web/index.html`

### Funciones principales

- Vigilar el cumplimiento de la legislación laboral y de Seguridad Social.
- Investigar denuncias de trabajadores y ciudadanos.
- Realizar visitas de inspección a centros de trabajo.
- Levantar actas de infracción y proponer sanciones.
- Mediar y arbitrar en conflictos laborales.
- Informar y asesorar a empresas y trabajadores.
- Perseguir el empleo irregular (economía sumergida).

---

## 2. Motivos habituales de denuncia

### 2.1 Impago o irregularidades salariales

- No pagar el salario en la fecha pactada.
- Pagar menos que lo fijado en convenio o por debajo del SMI.
- No pagar horas extraordinarias.
- No abonar complementos del convenio (nocturnidad, antigüedad, etc.).
- Pagar parte del salario "en negro" (sin reflejo en nómina).

### 2.2 Contratación irregular

- Trabajar sin contrato.
- No dar de alta en la Seguridad Social.
- Usar un contrato temporal sin causa real (fraude de ley).
- Trabajadores autónomos que realmente son empleados ("falso autónomo").
- Jornada real superior a la del contrato (parcial ficticio).

### 2.3 Jornada y descansos

- Superar la jornada máxima (40 horas semanales de media anual).
- No respetar los descansos (12 horas entre jornadas, día y medio
  semanal, vacaciones).
- No registrar la jornada (obligatorio desde 2019 — RDL 8/2019).
- Horas extraordinarias forzosas o por encima del límite legal (80/año).

### 2.4 Prevención de riesgos laborales

- Falta de evaluación de riesgos.
- No proporcionar equipos de protección individual (EPI).
- Condiciones inseguras en el centro de trabajo.
- Falta de formación en prevención.
- No tener plan de prevención ni servicio de prevención.

### 2.5 Discriminación y acoso

- Discriminación por sexo, edad, discapacidad, origen, orientación
  sexual, etc.
- Acoso sexual o por razón de sexo.
- Acoso laboral (mobbing).
- Falta de plan de igualdad (obligatorio para empresas ≥ 50 trabajadores).

### 2.6 Otros motivos

- Despido irregular.
- Incumplimiento del convenio colectivo.
- Cesión ilegal de trabajadores.
- Infracciones en materia de extranjería (trabajadores sin permiso).
- No respetar derechos de los representantes de los trabajadores.

---

## 3. Cómo presentar una denuncia

### 3.1 Buzón de la Inspección de Trabajo (online)

El canal más habitual. Se accede desde:

URL: `https://oeitss.mites.gob.es/buzonitss/`

Permite presentar denuncias con certificado digital, Cl@ve o DNI
electrónico. También existe la posibilidad de presentar comunicaciones
sin identificación (buzón de lucha contra el fraude laboral).

### 3.2 Presencialmente

En las Inspecciones Provinciales de Trabajo (hay una en cada capital
de provincia). Se puede pedir cita previa o ir directamente en horario
de atención.

### 3.3 Por correo postal

Dirigiendo un escrito a la Inspección Provincial de Trabajo
correspondiente al centro de trabajo denunciado.

### 3.4 Contenido de la denuncia

La denuncia debe incluir:

1. **Datos del denunciante**: nombre, DNI, dirección (se mantienen
   confidenciales frente a la empresa).
2. **Datos de la empresa denunciada**: nombre o razón social, dirección
   del centro de trabajo, CIF si se conoce.
3. **Hechos**: descripción clara y detallada de la irregularidad.
4. **Fecha**: cuándo ocurrieron o empezaron los hechos.
5. **Pruebas** (si se tienen): nóminas, contratos, horarios, mensajes,
   fotografías, testimonios.

---

## 4. Anonimato y confidencialidad

### ¿Es anónima la denuncia?

- **No es anónima**: la denuncia se presenta con identificación del
  denunciante.
- **Sí es confidencial**: la ITSS **no revela la identidad del
  denunciante** a la empresa inspeccionada. La visita de inspección se
  presenta como una actuación de oficio.
- **Buzón de fraude**: existe un buzón específico para comunicar
  irregularidades de forma anónima (sin identificación), pero no genera
  obligación de actuación inmediata — la Inspección valora si inicia
  investigación.

### Garantía de indemnidad

El trabajador que denuncia está protegido por la **garantía de
indemnidad**: cualquier represalia (despido, sanción, cambio de
condiciones) por haber denunciado se considera **nula**.

Si la empresa toma represalias:

- El despido es **nulo** (readmisión obligatoria + salarios de
  tramitación).
- Cualquier sanción o perjuicio es anulable.
- El trabajador puede a su vez denunciar la represalia.

---

## 5. Proceso de inspección

### 5.1 Fases

```
DENUNCIA
  ↓
VALORACIÓN (la ITSS decide si actúa)
  ↓
VISITA DE INSPECCIÓN (sin previo aviso)
  ↓
ACTUACIONES (requerimientos, actas)
  ↓
RESOLUCIÓN (archivo o sanción)
```

### 5.2 Visita de inspección

- El inspector se presenta en el centro de trabajo **sin previo aviso**.
- Tiene **libre acceso** a cualquier parte del centro de trabajo,
  documentación y trabajadores.
- Puede solicitar: nóminas, contratos, registro de jornada, evaluación
  de riesgos, libro de matrícula, partes de alta/baja, etc.
- Puede **entrevistar** a trabajadores en privado (sin presencia del
  empresario).
- Puede requerir la presencia de los representantes de los trabajadores.

### 5.3 Posibles resultados

| Resultado | Qué significa |
|---|---|
| **Archivo** | No se detecta infracción o las pruebas son insuficientes |
| **Requerimiento** | Se da un plazo a la empresa para corregir la irregularidad |
| **Acta de infracción** | Se inicia expediente sancionador con propuesta de multa |
| **Acta de liquidación** | Se reclaman cuotas no ingresadas a la Seguridad Social |
| **Acta de obstrucción** | Si la empresa impide la labor inspectora |

### 5.4 Plazos

- La ITSS no tiene un plazo legal obligatorio para realizar la visita
  tras la denuncia. Puede tardar semanas o meses.
- Las infracciones laborales **prescriben** a los 3 años (graves y muy
  graves) o 1 año (leves) desde la comisión de los hechos.
- Las infracciones en materia de Seguridad Social prescriben a los 4 años.

---

## 6. Infracciones y sanciones

La Ley sobre Infracciones y Sanciones en el Orden Social (LISOS)
clasifica las infracciones en tres niveles:

### 6.1 Infracciones leves

- No exponer el calendario laboral.
- No informar al trabajador de sus condiciones.
- No entregar la nómina en el formato correcto.

**Sanción**: 70 € a 750 €.

### 6.2 Infracciones graves

- No dar de alta al trabajador en la Seguridad Social.
- Impago o retraso reiterado del salario.
- No registrar la jornada.
- Superar la jornada máxima.
- Incumplir la normativa de contratación temporal.
- No elaborar el plan de igualdad (si es obligatorio).

**Sanción**: 751 € a 7.500 €.

### 6.3 Infracciones muy graves

- Retenciones salariales indebidas.
- Acoso sexual o por razón de sexo.
- Discriminación.
- Represalias contra el trabajador que denuncia.
- Incumplimiento grave de prevención de riesgos que genere riesgo para
  la vida o salud.
- Empleo de menores en trabajos prohibidos.
- Cesión ilegal de trabajadores.

**Sanción**: 7.501 € a 1.000.000 € (las más graves en prevención de
riesgos con resultado de muerte o lesiones graves).

### 6.4 Recargo de prestaciones

Si un accidente de trabajo o enfermedad profesional se produce por
falta de medidas de seguridad, la empresa puede ser condenada a un
**recargo del 30 % al 50 %** sobre las prestaciones de la Seguridad
Social del trabajador afectado.

---

## 7. Otras vías de reclamación

La Inspección de Trabajo no es la única vía:

| Vía | Cuándo usar |
|---|---|
| **Inspección de Trabajo (ITSS)** | Incumplimiento de normativa laboral, SS o prevención |
| **Juzgado de lo Social** | Reclamación de cantidades, despido, modificación de condiciones |
| **SMAC / papeleta de conciliación** | Paso previo obligatorio a la demanda judicial (excepto despido) |
| **Defensor del Pueblo** | Quejas contra la administración |
| **Sindicato** | Asesoramiento, mediación, representación |

En muchos casos, se puede denunciar ante la ITSS **y** demandar ante
el Juzgado de lo Social al mismo tiempo — no son excluyentes.

---

## 8. Obligación de registro de jornada

Desde mayo de 2019 (RDL 8/2019), todas las empresas deben llevar un
**registro diario de la jornada** de cada trabajador (hora de entrada
y salida).

- **Conservación**: 4 años.
- **Acceso**: trabajadores, representantes, ITSS.
- **Infracción** por no registrar: **grave** (751 € a 7.500 €).

Este registro es una herramienta clave para demostrar horas extra no
pagadas o exceso de jornada.

---

## 9. Resumen rápido

```
¿IRREGULARIDAD LABORAL?
  ↓
OPCIONES:
  ├── Denuncia a Inspección de Trabajo (ITSS)
  │     ├── Online: buzón electrónico (con Cl@ve o certificado)
  │     ├── Presencial: Inspección Provincial
  │     └── La identidad del denunciante es CONFIDENCIAL
  │
  ├── Demanda en Juzgado de lo Social
  │     └── Previo: papeleta de conciliación (SMAC)
  │
  └── Ambas vías son compatibles

PROCESO DE INSPECCIÓN:
  ├── Visita sin previo aviso
  ├── Libre acceso a documentación
  └── Resultado: archivo, requerimiento o acta de infracción

SANCIONES:
  ├── Leves: 70 – 750 €
  ├── Graves: 751 – 7.500 €
  └── Muy graves: 7.501 – 1.000.000 €

PROTECCIÓN DEL DENUNCIANTE:
  └── Garantía de indemnidad → represalias = despido nulo
```

---

## Cuándo NO usar esta skill

- Si pregunta por **tipos de contrato** → **laboral-contratos**.
- Si pregunta por **cómo leer una nómina** → **laboral-nominas**.
- Si pregunta por **prestación por desempleo** → **laboral-desempleo**.
- Si pregunta por **ERE o ERTE** → **laboral-ere-erte**.
- Si pregunta por **convenios colectivos** → **laboral-convenios**.
- Si pregunta por **estadísticas de paro** registrado → **sepe**.
- Si pregunta por **cotizaciones a la Seguridad Social** →
  **seguridad-social**.
- Si pregunta por **obligaciones fiscales del autónomo** →
  **fiscalidad-autonomos**.
- Si pregunta por el **texto de una ley** concreta → **boe**.
