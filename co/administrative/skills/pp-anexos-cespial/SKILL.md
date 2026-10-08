---
name: pp-anexos-cespial
title: pp-anexos — F3/F4 · Fábrica de documentos
description: Genera los anexos y formatos formales de la propuesta (carta de presentación, documento de consorcio/UT, manifestaciones de inhabilidades/SARLAFT, pacto de transparencia, compromiso del equipo, formato de experiencia, autorización de junta, confidencialidad) usando los datos reales del proponente seleccionado (proponente único / consorcio / unión temporal) tomados del roster. Respeta el formato oficial del pliego cuando existe y deriva a firma humana los que la requieren. Úsala en F3/F4 para producir el paquete documental sin trabajo manual repetitivo.
author: Cespial
author_url: https://github.com/Cespial/propuestas-secop/tree/main/skills/pp-anexos
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: co
practice: administrative
language: es
---

# pp-anexos — F3/F4 · Fábrica de documentos

Produce el paquete documental formal de la propuesta. Operacionaliza el catálogo de anexos
del playbook. Corre en F3 (junto a `pp-propuesta`) y se cierra en F4 con `pp-cierre`.
Lee siempre primero `references/SPEC.md`. Tono y estilo uniformes en todo texto generado.

## Al empezar

- Lee `00-estado/ESTADO.md`: convocante, proceso, deadline absoluto, cifras canónicas, P0.
- Resuelve `<id>` del proceso y `<WORKSPACE>` (SPEC §1). `$PLUGIN` = raíz del plugin.
- Confirma el **proponente seleccionado** y su figura jurídica en
  `02-investigacion/05_DICTAMEN_JURIDICO_PROPONENTE.md` (único / consorcio / UT) y el `%` de
  participación. El proponente es el que recomendó `pp-proponente`. Define qué anexos son aplicables.

## Insumos que LEE

- `references/anexos-catalogo.md` — catálogo, qué requiere firma, exemplars reutilizables.
- `references/roster/<empresa>.md` — NITs, reps. legales, matrículas, RUP, `[VERIFICAR]` de cada
  empresa del roster que conforma el proponente (ver `references/ficha-empresa.template.md`).
- `references/perfiles-equipo.template.md` — perfiles para las cartas de compromiso del equipo.
- `01-pliego/` — **formatos oficiales** del pliego (Word/PDF) y la lista exacta de anexos exigidos.
- `02-investigacion/05_DICTAMEN_JURIDICO_PROPONENTE.md` — figura, `%`, designación de líder.
- `02-investigacion/18_EXPERIENCIA.md` — contratos que acreditan experiencia (para el formato).

## Salidas que ESCRIBE

- `05-anexos/<AX-NN>_<nombre>.{docx,pdf}` — un archivo por anexo, numerado según el pliego.
- `05-anexos/firmar/` — copia de cada firmable, listo para rúbrica humana.
- `05-anexos/00_INDICE_ANEXOS.md` — índice con estado: generado / pendiente de firma / N/A justificado.
- Actualiza `00-estado/ESTADO.md`: lista de firmas pendientes como acción humana.

## Subagentes / skills / workflows que invoca

- Coordina con `pp-proponente` — define desde qué empresa o figura se presenta la oferta.
- Coordina con `pp-equipo` — las cartas de compromiso del equipo nacen de sus perfiles y CV-anexos.
- Coordina con `pp-cierre` — el ZIP final incluye solo los anexos exigidos por el pliego.

---

## 1. Regla de oro — formato oficial manda

- Si el pliego adjunta un **formato oficial** para un anexo, diligéncialo y suscríbelo tal cual.
  No suscribir el formato oficial, o reemplazarlo por uno propio, es **causal de rechazo**.
- Solo cuando el pliego **no** trae formato, genera uno propio desde el catálogo.
- Antes de generar nada: inventaría qué formatos oficiales hay en `01-pliego/` y mapéalos
  al catálogo. Lo que el pliego ya define, no se inventa.

```bash
ls -1 "<WORKSPACE>/01-pliego/" | grep -iE "formato|anexo|carta|minuta|modelo"
```

## 2. Selección de anexos aplicables

Recorre `references/anexos-catalogo.md §2` y marca, para este proceso:

- **Aplica** — el pliego lo exige o la figura lo requiere (p. ej. documento de consorcio).
- **N/A** — no aplica a esta figura/objeto; se justifica en el índice (no se omite en silencio).
- **Origen** — formato oficial del pliego (preferente) o template propio.

La figura jurídica decide: proponente único no lleva documento de consorcio; consorcio/UT sí,
con `%` de participación y designación de representante tomados del dictamen jurídico.

## 3. Diligenciamiento con datos reales — cero invención

Toma los datos del roster (`references/roster/<empresa>.md`). Nunca inventes NIT, matrícula ni
representante.

- Por cada empresa del proponente: NIT, matrícula mercantil, rep. legal y domicilio de su ficha
  en `references/roster/`.
- `%` de participación: del dictamen jurídico. Si no está cerrado, es **P0**, no se rellena a ojo.
- Todo dato no confirmado (EEFF, n.º de empleados, capital) va con `[VERIFICAR]` + dueño + fecha.

Anexos típicos y su dato crítico:

| Anexo | Dato que debe quedar correcto |
|---|---|
| Carta de presentación | proponente, proceso, vigencia de la oferta, tesis vinculante (≤ 8 palabras) |
| Documento de consorcio/UT | NITs, `%` participación, representante designado |
| Manifestación de inhabilidades e incompatibilidades | `Ley 80/1993 art. 8` |
| Pacto de transparencia / anticorrupción | declaración del rep. legal |
| Manifestación SARLAFT / listas restrictivas | OFAC/ONU, declaración del rep. legal |
| Confidencialidad y tratamiento de datos | `Ley 1581/2012` |
| Formato de experiencia | n.º contrato, objeto, valor en SMMLV, UNSPSC (de `18_EXPERIENCIA.md`) |
| Autorización del órgano directivo | cuantía autorizada (acta de junta/asamblea) |
| Cartas de compromiso del equipo | rol y dedicación por perfil (de `pp-equipo`) |

## 4. Reutilizar exemplars reales

Parte de los exemplars citados en `anexos-catalogo.md §3` cuando el pliego no trae formato.
No copies texto de propuestas previas al mismo cliente (estilo, §13): adapta estructura, no ADN.

- Plantilla editable de acuerdo de consorcio / unión temporal — base del documento de consorcio/UT.
- Cartas a directivo de aliado y carta aval/intención — base de los avales del aliado (p. ej. IES).
- Carta de descuento vinculante — solo si el pliego pide oferta económica vinculante en anexo.

## 5. Generación de archivos

Para cada anexo aplicable, produce el archivo en `05-anexos/` con el naming `<AX-NN>_<nombre>`,
donde `NN` sigue la numeración del pliego. Formato editable (DOCX) y, si el pliego pide carga
firmada, también PDF para imprimir/firmar.

- La carta de presentación y el documento de consorcio/UT llevan la **misma tesis** que la propuesta.
- Las cifras (SMMLV, valores, `%`) son idénticas a las **cifras canónicas** de `ESTADO.md`.
- Sin emojis, sin frases vacías, sin nombrar competidores.

## 6. Derivar firmables a acción humana

Todo anexo marcado `[firma]` en el catálogo requiere rúbrica del representante legal (o del
secretario de junta, o de cada profesional). Estos **no** los firma la skill:

- Copia cada firmable a `05-anexos/firmar/`.
- Regístralos en `00-estado/ESTADO.md` como acción humana pendiente: anexo, quién firma, soporte.
- Firmas múltiples (consorcio/UT): cada representante legal de las empresas del proponente firma
  el documento de consorcio.

## 7. Índice de anexos

Genera `05-anexos/00_INDICE_ANEXOS.md` con una fila por anexo del pliego:

- `AX-NN`, nombre, origen (oficial / propio), estado (**generado** / **pendiente de firma** / **N/A**),
  y para N/A la justificación de por qué no aplica.
- Es el puente con `pp-cierre`: el ZIP final empaca solo los anexos **exigidos por el pliego**.

## Al terminar

Actualiza `00-estado/ESTADO.md`: anexos generados, firmables en `05-anexos/firmar/` con
responsable de firma, `[VERIFICAR]` abiertos (EEFF, `%` de participación si falta),
y próximo paso. Reporta al usuario qué quedó listo y qué exige mano humana.
