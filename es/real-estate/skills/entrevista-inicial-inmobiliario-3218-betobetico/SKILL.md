---
name: entrevista-inicial-inmobiliario-3218-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin inmobiliario. Aprende tu práctica y escribe CLAUDE.md a partir de tus operaciones habituales, posiciones en arrendamientos y gestión de propiedad horizontal. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin inmobiliario", "onboarding inmobiliario", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/inmobiliario/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: contratos de arrendamiento, escrituras de compraventa, estatutos de comunidad de propietarios.
4. Extraer: tipo de práctica, operaciones habituales, posiciones LAU, gestión de comunidades.
5. Migración: si existe un CLAUDE.md poblado en la ruta antigua de caché pero no en la ruta de configuración, copiarlo.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md`. Mostrar resumen. Ofrecer primera tarea.

## `--check-integraciones`

Re-ejecuta la comprobación de integraciones y actualiza `## Integraciones disponibles`. No re-entrevista.

```
/inmobiliario:entrevista-inicial
```

```
/inmobiliario:entrevista-inicial --check-integraciones
```

---

# Entrevista Inicial: Derecho Inmobiliario

## Propósito

Aprender cómo funciona *esta* práctica inmobiliaria — si es promotor, inversor, arrendador, administrador de fincas o asesor de particulares. Qué operaciones hace, qué posiciones toma en arrendamientos, cómo gestiona comunidades. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

El derecho inmobiliario en España tiene muchas caras. Un promotor que hace obra nueva tiene poco en común con un administrador de fincas que gestiona comunidades, o con un despacho que asesora a arrendatarios en conflictos LAU. La entrevista identifica el perfil antes de nada.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md`:
- **No existe** -> iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** -> saludar y ofrecer retomar.
- **Contiene marcadores `[PLACEHOLDER]`** -> ofrecer empezar de cero o retomar.
- **Poblado** -> ya configurado; saltar salvo `--redo`.

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar en una línea. Si confirma, saltar preguntas de empresa.
- **Si no existe:** Preguntar datos de empresa, escribirlos en perfil compartido y continuar.

## Antes de empezar la entrevista

> **`inmobiliario` es para quien gestiona operaciones inmobiliarias: compraventas, arrendamientos, propiedad horizontal, obra nueva, due diligence inmobiliaria.** No es tu área? `/hub-constructor:buscador-skills-relacionados`.
>
> **2 minutos** te dan el tipo de práctica y las operaciones principales, con valores sensatos en todo lo demás. **15 minutos** añade tus posiciones LAU, gestión de comunidades, y documentos semilla.
>
> Rápido o completo?

Esperar elección.

## Tras elegir rápido o completo

> "Este plugin mantiene tu perfil de práctica inmobiliaria (tipo de práctica, operaciones, posiciones en arrendamientos, propiedad horizontal). Esta entrevista aprende cómo trabajas realmente — tus operaciones, tus posiciones, tu estilo — y lo escribe en un archivo de texto plano que el plugin lee cada vez."
>
> "Listo? Unas preguntas rápidas primero."

**Ruta rápida:** preguntar solo Parte 0 y Parte 1. Escribir con `[DEFAULT]`.

**Ruta completa:** el flujo completo.

## Ritmo de la entrevista

- **No más de 2-3 preguntas por turno**, contando subpartes.
- **Pedir documentos.** "Tienes un contrato de arrendamiento tipo? Pégalo o comparte ruta."
- **Pausa y reanudación.** Al pausar, escribir configuración parcial con `<!-- CONFIGURACIÓN PAUSADA EN: [sección] -->` y marcadores `[PENDIENTE]`.
- **Verificar datos legales.** Si el usuario cita un artículo de la LAU (Ley 29/1994), la LPH (Ley 49/1960) o la LH (Ley Hipotecaria), comprobar antes de escribirlo. La LAU ha sufrido múltiples reformas (RDL 7/2019, Ley 12/2023 de vivienda) — verificar qué versión aplica.

## La entrevista

### Apertura

> Voy a ayudarte con operaciones inmobiliarias: compraventas, arrendamientos, propiedad horizontal, obra nueva. Antes de nada, necesito saber qué tipo de práctica inmobiliaria es esta. Diez minutos.
>
> Después te pediré tres cosas: un contrato de arrendamiento tipo, una escritura representativa y unos estatutos de comunidad si gestionas propiedad horizontal.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a inmobiliarista** — letrado/a especializado en derecho inmobiliario.
> 2. **Profesional con acceso a letrado** — administrador de fincas, agente inmobiliario, gestor que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a letrado** — propietario, arrendador, inversor que gestiona esto por su cuenta.

Si es 2 o 3, explicar: los outputs serán investigación para revisión letrada.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Tipo de práctica (2-3 min)

> **Cuál es tu perfil en el sector inmobiliario?** Puedes seleccionar varios:
>
> - **Promotor/constructor** — promoción inmobiliaria, obra nueva, declaraciones de obra nueva y división horizontal
> - **Inversor inmobiliario** — compra para rentabilidad (alquiler o reventa), SOCIMI, fondos inmobiliarios
> - **Particular** — compraventa de vivienda propia, asesoramiento a compradores/vendedores
> - **Comunidad de propietarios** — administración de fincas, gestión de comunidades
> - **Arrendador** — propietario que alquila viviendas o locales
> - **Arrendatario** — defensa de inquilinos, negociación de contratos de arrendamiento
> - **Despacho generalista** — de todo un poco
>
> Cuál es la operación más frecuente en tu práctica? Y la de mayor cuantía?

### Parte 2: Operaciones habituales (2-3 min)

> **Qué tipo de operaciones gestionas con más frecuencia?**
>
> - **Compraventa** — vivienda, local, solar, finca rústica? Volumen mensual/anual?
>   - Due diligence registral y urbanística: la haces sistemáticamente?
>   - Arras: penitenciales (art. 1454 CC) o confirmatorias? Cuál es tu posición habitual?
>   - Condición resolutoria vs. hipoteca del vendedor: cuál usas?
>
> - **Arrendamiento de vivienda** (LAU, título II) — cuántos contratos al año?
>
> - **Arrendamiento de uso distinto de vivienda** (LAU, título III) — locales, oficinas, naves?
>
> - **Obra nueva** — declaraciones de obra nueva, divisiones horizontales, licencias de primera ocupación?
>
> - **Otros** — opciones de compra, derechos de superficie, permutas, cesiones, leaseback?

### Parte 3: Arrendamientos — Posiciones LAU (3-4 min)

> **Si trabajas con arrendamientos, necesito conocer tus posiciones habituales.** Esto alimenta los skills de revisión y redacción de contratos. Si no trabajas con arrendamientos, saltamos esta parte.
>
> **Arrendamiento de vivienda (Título II LAU + Ley 12/2023 de vivienda):**
> - **Duración:** 5 años persona física / 7 persona jurídica (art. 9 LAU). Pactáis algo distinto como periodo obligatorio?
> - **Prórroga tácita:** 3 años adicionales (art. 10 LAU). Intentáis limitar la prórroga cuando actuáis como arrendador?
> - **Renta:** Cómo fijáis la renta inicial? Conocéis si la zona está declarada como zona tensionada (Ley 12/2023)?
> - **Actualización de renta:** IPC, IRAV, índice limitado (art. 18 LAU post Ley 12/2023)? Cuál es vuestra posición?
> - **Fianza:** 1 mensualidad vivienda / 2 uso distinto (art. 36 LAU). Pedís garantías adicionales? Cuántas mensualidades?
> - **Obras del arrendatario:** Posición sobre obras de conservación (art. 21), mejora (art. 22) y del arrendatario (art. 23)?
> - **Resolución:** Causas habituales que invocáis como arrendador? Cómo gestionáis el impago?
>
> **Arrendamiento de uso distinto (Título III LAU):**
> - **Duración pactada habitual?** Periodo obligatorio + opciones de prórroga?
> - **Renta:** Renta fija, variable según facturación, mixta?
> - **Cesión y subarriendo:** Posición? Lo permitís con condiciones o lo prohibís?
> - **Obras:** Quién paga la adecuación del local?
> - **Indemnización por clientela** (art. 34 LAU) — la pactáis expresamente?
>
> Si tenéis un contrato de arrendamiento tipo, pégalo o comparte ruta — aprenderé más del contrato que de las respuestas.

### Parte 4: Propiedad horizontal (2-3 min)

> **Gestionas comunidades de propietarios?** Si no, saltamos.
>
> Si sí:
> - **Cuántas comunidades gestionas?**
> - **Tipo de comunidades** — residencial, comercial, mixta, macrocomunidad?
> - **Tipo de incidencias más habituales:**
>   - Morosidad (art. 21 LPH) — procedimiento monitorio? Volumen?
>   - Obras comunes (art. 10, 17 LPH) — frecuencia de conflictos con las mayorías?
>   - Actividades molestas/nocivas/insalubres/peligrosas (art. 7.2 LPH) — las habéis invocado?
>   - Pisos turísticos — os afecta? Habéis modificado estatutos para limitar el uso turístico?
>   - Accesibilidad (art. 10.1.b LPH) — solicitudes frecuentes?
>
> - **Juntas:** Preparáis convocatorias y actas? Cuál es la problemática más habitual (quórum, mayorías, impugnación)?
>
> Si tenéis los estatutos de una comunidad tipo, pégalos o comparte ruta.

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Un contrato de arrendamiento representativo** — vivienda o local, el que mejor refleje vuestra práctica. Aprenderé vuestras cláusulas, vuestro estilo y vuestras posiciones reales.
>
> 2. **Una escritura representativa** — compraventa, obra nueva, división horizontal. Me enseña cómo estructuráis las operaciones.
>
> 3. **Estatutos de comunidad** — si gestionáis propiedad horizontal. Aprenderé las particularidades de las comunidades que administráis.

**Cómo leer los documentos semilla:**

**Contrato de arrendamiento:** Mapear cada cláusula contra las posiciones declaradas. Deltas son interesantes — "dijiste que pedís 2 meses de garantía adicional, pero tu contrato tipo dice 3."

**Escritura:** Extraer la estructura de la operación, las condiciones suspensivas o resolutorias, las cargas registrales, la distribución de gastos.

**Estatutos:** Identificar las limitaciones de uso, las mayorías especiales, las cuotas de participación y cualquier cláusula no estándar.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Inmobiliario

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] opera en el sector inmobiliario como [perfil: promotor/inversor/particular/administrador/arrendador].
Operaciones principales: [tipos]. Zona geográfica: [CCAA/provincias].
El equipo cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a | Profesional con acceso a letrado | Profesional sin acceso a letrado]
**Contacto letrado:** [Nombre / despacho / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Calendario bajo demanda |

---

## Tipo de práctica

**Perfiles activos:** [promotor / inversor / particular / comunidades / arrendador / arrendatario]
**Operación más frecuente:** [tipo]
**Operación de mayor cuantía:** [tipo]
**Zona geográfica principal:** [CCAA/provincia]

---

## Operaciones habituales

| Tipo | Subtipo | Volumen anual | Cuantía media | Notas |
|---|---|---|---|---|
| Compraventa | [vivienda/local/solar] | [número] | [euros] | |
| Arrendamiento vivienda | | [número] | [renta media] | |
| Arrendamiento uso distinto | [local/oficina/nave] | [número] | [renta media] | |
| Obra nueva | | [número] | | |
| [otro] | | [número] | | |

---

## Posiciones LAU — Arrendamiento de vivienda

| Cláusula | Posición habitual | Notas |
|---|---|---|
| Duración | [periodo] | |
| Prórroga | [posición] | |
| Renta inicial | [criterio] | Zona tensionada: [sí/no] |
| Actualización renta | [índice] | |
| Fianza | [legal] + [garantía adicional meses] | |
| Obras arrendatario | [posición] | |
| Resolución por impago | [procedimiento] | |

---

## Posiciones LAU — Arrendamiento uso distinto

| Cláusula | Posición habitual | Notas |
|---|---|---|
| Duración | [periodo obligatorio + opciones] | |
| Renta | [fija/variable/mixta] | |
| Cesión/subarriendo | [permitido con condiciones / prohibido] | |
| Obras adecuación | [quién paga] | |
| Indemnización clientela | [pactada/excluida] | |

---

## Propiedad horizontal

**Comunidades gestionadas:** [número]
**Tipo:** [residencial / comercial / mixta / macro]
**Incidencias más frecuentes:** [morosidad / obras / actividades molestas / turístico / accesibilidad]

### Procedimientos habituales en comunidades

| Incidencia | Frecuencia | Procedimiento | Notas |
|---|---|---|---|
| Morosidad | [frecuencia] | [monitorio / ordinario] | |
| Obras comunes | [frecuencia] | [tipo de mayoría] | |
| [otra] | [frecuencia] | [procedimiento] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Arrendamiento rutinario | [responsable] | [nombre] | Impago > [meses], desahucio |
| Compraventa > [cuantía] | [responsable] | [nombre] | Siempre |
| Conflicto en comunidad | [responsable] | [nombre] | Demanda judicial |
| Obra nueva | — | [dirección + legal] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Contrato arrendamiento | [ruta] | [fecha] | [vivienda/local] |
| Escritura | [ruta] | [fecha] | [tipo operación] |
| Estatutos comunidad | [ruta] | [fecha] | [comunidad] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/inmobiliario:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Las posiciones LAU son las partes a revisar con más cuidado — un contrato redactado con posiciones incorrectas propaga el error a toda la cartera."

2. **Proponer primeras tareas:**
   - "Quieres que revise un contrato de arrendamiento contra tus posiciones?"
   - "Tienes alguna escritura de compraventa pendiente de revisar?"
   - "Quieres que compruebe si alguna de tus comunidades tiene problemas de mayorías pendientes?"
   - Si es arrendador: "Quieres que revise si tus contratos están adaptados a la Ley 12/2023 de vivienda?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/inmobiliario:entrevista-inicial --redo` para re-entrevista completa
   > - `/inmobiliario:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: las **posiciones LAU** (la Ley 12/2023 ha cambiado muchas reglas), las **operaciones habituales** (según evoluciona la cartera), y la **propiedad horizontal** (según cambian las comunidades gestionadas)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No confundir título II con título III de la LAU.** Vivienda habitual (título II) tiene normas imperativas que no aplican a uso distinto (título III, mayoritariamente dispositivo). Un contrato de local redactado como si fuera vivienda es un error grave.
- **No ignorar la Ley 12/2023 de vivienda.** Ha modificado la LAU sustancialmente: límites a la actualización de renta, zonas tensionadas, recargo de IBI a viviendas vacías, limitaciones a grandes tenedores. Preguntar siempre si las zonas donde opera el usuario están declaradas tensionadas.
- **No asumir el régimen económico matrimonial.** En compraventas, el régimen importa para la disposición del bien. En España hay múltiples regímenes forales (catalán, aragonés, balear, navarro, vasco) además de gananciales y separación de bienes.
- **No escribir posiciones LAU genéricas.** Si el usuario no ha negociado muchos arrendamientos, decirlo: `[POSICIONES NO CONSOLIDADAS — práctica con poco volumen de arrendamientos. Tratar como puntos de partida.]`
- **No olvidar la normativa autonómica.** Urbanismo es competencia autonómica. Cada CCAA tiene su ley del suelo y su normativa urbanística propia. Un consejo urbanístico sin preguntar la CCAA es un error.
- **No dar por hecho que la LPH no ha cambiado.** La LPH se ha modificado múltiples veces (RDL 7/2019, Ley 10/2022 de accesibilidad). Verificar la versión vigente antes de citar artículos.
