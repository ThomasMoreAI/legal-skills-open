---
name: entrevista-inicial-inmobiliario-betobetico
title: /entrevista-inicial
description: Ejecuta la entrevista de configuración inicial del plugin inmobiliario. Aprende tu práctica y escribe CLAUDE.md a partir de tus operaciones habituales, posiciones en arrendamientos y gestión de propiedad horizontal. Usar en la primera ejecución, cuando CLAUDE.md no existe o tiene placeholders, o cuando el usuario dice "configura el plugin inmobiliario", "onboarding inmobiliario", o quiere re-ejecutar.
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/inmobiliario/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: real-estate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` — si está poblado y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista descrito abajo.
3. Documentos semilla: contratos de arrendamiento, escrituras de compraventa, reglamentos de copropiedad de propiedad horizontal.
4. Extraer: tipo de práctica, operaciones habituales, posiciones en arrendamientos, gestión de propiedad horizontal.
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

Aprender cómo funciona *esta* práctica inmobiliaria — si es promotor, inversor, arrendador, administrador de propiedad horizontal o asesor de particulares. Qué operaciones hace, qué posiciones toma en arrendamientos, cómo gestiona las propiedades horizontales. Escribirlo en `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` para que todos los demás skills lean desde el mismo entendimiento.

El derecho inmobiliario en Panamá tiene muchas caras. Un promotor que hace obra nueva tiene poco en común con una administradora de propiedades horizontales, o con un despacho que asesora a arrendatarios en conflictos de arrendamiento. La entrevista identifica el perfil antes de nada.

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
> **2 minutos** te dan el tipo de práctica y las operaciones principales, con valores sensatos en todo lo demás. **15 minutos** añade tus posiciones en arrendamientos, gestión de propiedad horizontal, y documentos semilla.
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
- **Verificar datos legales.** Si el usuario cita la Ley 284 de 2022 (propiedad horizontal), la Ley 93 de 1973 (arrendamientos) o el Código Civil de Panamá, comprobar antes de escribirlo. Los arrendamientos se rigen por la Ley 93 de 1973 (mod. Ley 28 de 1974 y Ley 259 de 2021); la Ley 284 de 2022 y los porcentajes de mayorías deben verificarse en su texto vigente — no asumir artículos de memoria.

## La entrevista

### Apertura

> Voy a ayudarte con operaciones inmobiliarias: compraventas, arrendamientos, propiedad horizontal, obra nueva. Antes de nada, necesito saber qué tipo de práctica inmobiliaria es esta. Diez minutos.
>
> Después te pediré tres cosas: un contrato de arrendamiento tipo, una escritura representativa y un reglamento de copropiedad si gestionas propiedad horizontal.

### Parte 0: Quién usa esto y qué hay conectado

#### Quién usa esto

> Quién va a usar este plugin en el día a día?
>
> 1. **Abogado/a inmobiliarista idóneo** — abogado/a especializado en derecho inmobiliario panameño.
> 2. **Profesional con acceso a abogado** — administrador de propiedad horizontal, corredor de bienes raíces, gestor que consulta con asesoría jurídica.
> 3. **Profesional sin acceso regular a abogado** — propietario, arrendador, inversor que gestiona esto por su cuenta.

Si es 2 o 3, explicar: los outputs serán investigación para revisión de un abogado idóneo.

#### Qué hay conectado

> Este plugin puede trabajar con: almacenamiento documental, Slack/Teams y tareas programadas. Déjame comprobar qué conectores tienes.

Comprobar cada conector. Reportar resultados.

### Parte 1: Tipo de práctica (2-3 min)

> **Cuál es tu perfil en el sector inmobiliario?** Puedes seleccionar varios:
>
> - **Promotor/constructor** — promoción inmobiliaria, obra nueva, incorporación al régimen de propiedad horizontal
> - **Inversor inmobiliario** — compra para rentabilidad (alquiler o reventa), fondos inmobiliarios
> - **Particular** — compraventa de vivienda propia, asesoramiento a compradores/vendedores
> - **Propiedad horizontal** — administración de PH, gestión de copropiedades
> - **Arrendador** — propietario que alquila viviendas o locales
> - **Arrendatario** — defensa de inquilinos, negociación de contratos de arrendamiento
> - **Despacho generalista** — de todo un poco
>
> Cuál es la operación más frecuente en tu práctica? Y la de mayor cuantía?

### Parte 2: Operaciones habituales (2-3 min)

> **Qué tipo de operaciones gestionas con más frecuencia?**
>
> - **Compraventa** — vivienda, local, terreno, finca? Volumen mensual/anual?
>   - Due diligence registral (Registro Público) y catastral (ANATI): la haces sistemáticamente?
>   - Arras / promesa de compraventa: penitenciales o confirmatorias? Cuál es tu posición habitual?
>   - Retención de la ganancia de capital por el comprador: cómo la gestionas?
>
> - **Arrendamiento de vivienda** (régimen tutelado) — cuántos contratos al año?
>
> - **Arrendamiento comercial / uso distinto** — locales, oficinas, depósitos?
>
> - **Obra nueva** — declaraciones de obra nueva, incorporación a propiedad horizontal, permisos de ocupación?
>
> - **Otros** — opciones de compra, derechos de superficie, permutas, cesiones, fideicomisos de garantía?

### Parte 3: Arrendamientos — Posiciones habituales (3-4 min)

> **Si trabajas con arrendamientos, necesito conocer tus posiciones habituales.** Esto alimenta los skills de revisión y redacción de contratos. Si no trabajas con arrendamientos, saltamos esta parte.
>
> **Arrendamiento de vivienda (régimen tutelado):**
> - **Duración:** Qué periodo obligatorio pactáis? [verificar el mínimo legal aplicable]
> - **Renovación / prórroga:** Intentáis limitar la prórroga cuando actuáis como arrendador?
> - **Canon:** Cómo fijáis el canon inicial? En B/. o USD? Conocéis si el inmueble queda dentro o fuera del régimen tutelado por su cuantía? (El umbral histórico de B/.150/mes quedó suspendido por el DE 145 de 2020; el MIVIOT conoce de todos los contratos — verificar en el texto oficial)
> - **Actualización del canon:** Qué criterio usáis y dentro de qué límite legal? [verificar]
> - **Depósito de garantía:** El depósito legal es de un (1) mes de canon y se consigna ante la Dirección General de Arrendamientos del MIVIOT (art. 13 Ley 93 de 1973, mod. Ley 259 de 2021). Lo consignáis así?
> - **Mejoras del arrendatario:** Posición sobre obras de conservación y mejora?
> - **Resolución / desalojo:** Causas habituales que invocáis como arrendador? Cómo gestionáis el impago?
>
> **Arrendamiento comercial / uso distinto:**
> - **Duración pactada habitual?** Periodo obligatorio + opciones de prórroga?
> - **Canon:** Fijo, variable según facturación, mixto?
> - **Cesión y subarriendo:** Posición? Lo permitís con condiciones o lo prohibís?
> - **Obras:** Quién paga la adecuación del local?
>
> Si tenéis un contrato de arrendamiento tipo, pégalo o comparte ruta — aprenderé más del contrato que de las respuestas.

### Parte 4: Propiedad horizontal (2-3 min)

> **Gestionas propiedades horizontales?** Si no, saltamos.
>
> Si sí:
> - **Cuántas PH gestionas?**
> - **Tipo de PH** — residencial, comercial, mixta, macroproyecto?
> - **Tipo de incidencias más habituales:**
>   - Morosidad de cuotas (Ley 284 de 2022) — procedimiento de cobro? Volumen?
>   - Obras y mejoras sobre bienes comunes — frecuencia de conflictos con las mayorías?
>   - Actividades molestas / uso indebido de unidades — las habéis invocado?
>   - Alquiler de corto plazo / turístico — os afecta? Habéis modificado el reglamento para limitarlo?
>   - Accesibilidad — solicitudes frecuentes?
>
> - **Asambleas:** Preparáis convocatorias y actas? Cuál es la problemática más habitual (quórum, mayorías, impugnación)?
>
> Si tenéis el reglamento de copropiedad de una PH tipo, pégalo o comparte ruta.

### Parte 5: Documentos semilla (3-4 min)

> Quiero ver tres cosas:
>
> 1. **Un contrato de arrendamiento representativo** — vivienda o local, el que mejor refleje vuestra práctica. Aprenderé vuestras cláusulas, vuestro estilo y vuestras posiciones reales.
>
> 2. **Una escritura representativa** — compraventa, obra nueva, incorporación a propiedad horizontal. Me enseña cómo estructuráis las operaciones.
>
> 3. **Reglamento de copropiedad** — si gestionáis propiedad horizontal. Aprenderé las particularidades de las PH que administráis.

**Cómo leer los documentos semilla:**

**Contrato de arrendamiento:** Mapear cada cláusula contra las posiciones declaradas. Deltas son interesantes — "dijiste que pedís 2 cánones de depósito, pero tu contrato tipo dice 3."

**Escritura:** Extraer la estructura de la operación, las condiciones suspensivas o resolutorias, los gravámenes inscritos, la distribución de gastos.

**Reglamento de copropiedad:** Identificar las limitaciones de uso, las mayorías especiales, los coeficientes de participación y cualquier cláusula no estándar.

## Plantilla del perfil de práctica

```markdown
# Perfil de Práctica — Derecho Inmobiliario

*Generado por la entrevista inicial en [FECHA]. Editar este archivo directamente.*

---

## Quiénes somos

[Empresa/Despacho] opera en el sector inmobiliario como [perfil: promotor/inversor/particular/administrador de PH/arrendador].
Operaciones principales: [tipos]. Zona geográfica: [provincia/distrito/corregimiento].
El equipo cuenta con [N] personas. [Responsable: nombre].
La escalación va a [nombre].

---

## Quién usa este plugin

**Rol:** [Abogado/a idóneo | Profesional con acceso a abogado | Profesional sin acceso a abogado]
**Contacto del abogado:** [Nombre / despacho / N/A]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental | [verificado/no] | Resultados guardados localmente |
| Slack / Teams | [verificado/no] | Alertas inline |
| Tareas programadas | [verificado/no] | Calendario bajo demanda |

---

## Tipo de práctica

**Perfiles activos:** [promotor / inversor / particular / PH / arrendador / arrendatario]
**Operación más frecuente:** [tipo]
**Operación de mayor cuantía:** [tipo]
**Zona geográfica principal:** [provincia/distrito]

---

## Operaciones habituales

| Tipo | Subtipo | Volumen anual | Cuantía media | Notas |
|---|---|---|---|---|
| Compraventa | [vivienda/local/terreno] | [número] | [B/. o USD] | |
| Arrendamiento vivienda | | [número] | [canon medio] | |
| Arrendamiento comercial | [local/oficina/depósito] | [número] | [canon medio] | |
| Obra nueva | | [número] | | |
| [otro] | | [número] | | |

---

## Posiciones en arrendamiento de vivienda (régimen tutelado)

| Cláusula | Posición habitual | Notas |
|---|---|---|
| Duración | [periodo] | [verificar mínimo legal] |
| Renovación / prórroga | [posición] | |
| Canon inicial | [criterio] | Umbral de cuantía suspendido (DE 145 de 2020): el MIVIOT conoce de todos los contratos (verificar en el texto oficial) |
| Actualización del canon | [criterio] | [verificar límite legal] |
| Depósito de garantía | [1 mes de canon] | Consignación ante la Dirección General de Arrendamientos del MIVIOT (art. 13 Ley 93 de 1973, mod. Ley 259 de 2021) |
| Obras arrendatario | [posición] | |
| Resolución por impago | [procedimiento] | |

---

## Posiciones en arrendamiento comercial / uso distinto

| Cláusula | Posición habitual | Notas |
|---|---|---|
| Duración | [periodo obligatorio + opciones] | |
| Canon | [fijo/variable/mixto] | |
| Cesión/subarriendo | [permitido con condiciones / prohibido] | |
| Obras de adecuación | [quién paga] | |

---

## Propiedad horizontal (Ley 284 de 2022)

**PH gestionadas:** [número]
**Tipo:** [residencial / comercial / mixta / macro]
**Incidencias más frecuentes:** [morosidad / obras / uso indebido / corto plazo / accesibilidad]

### Procedimientos habituales en PH

| Incidencia | Frecuencia | Procedimiento | Notas |
|---|---|---|---|
| Morosidad de cuotas | [frecuencia] | [vía de cobro Ley 284 de 2022] | [verificar] |
| Obras sobre bienes comunes | [frecuencia] | [tipo de mayoría] | [verificar] |
| [otra] | [frecuencia] | [procedimiento] | |

---

## Escalación

| Tipo de asunto | Gestiona | Escala a | Cuándo |
|---|---|---|---|
| Arrendamiento rutinario | [responsable] | [nombre] | Impago > [meses], desalojo |
| Compraventa > [cuantía] | [responsable] | [nombre] | Siempre |
| Conflicto en PH | [responsable] | [nombre] | Demanda judicial |
| Obra nueva | — | [dirección + legal] | Siempre |

---

## Documentos semilla

| Doc | Ubicación | Fecha revisión | Notas |
|---|---|---|---|
| Contrato arrendamiento | [ruta] | [fecha] | [vivienda/local] |
| Escritura | [ruta] | [fecha] | [tipo operación] |
| Reglamento de copropiedad | [ruta] | [fecha] | [PH] |

---

## Resultados

**Carpeta de resultados:** [ruta]
**Convención de nombres:** [patrón o "ad hoc"]

---

*Re-ejecutar: `/inmobiliario:entrevista-inicial --redo`*
```

## Tras escribir

1. **Mostrar el resumen.** "Esto es lo que he entendido. Las posiciones en arrendamiento son las partes a revisar con más cuidado — un contrato redactado con posiciones incorrectas propaga el error a toda la cartera."

2. **Proponer primeras tareas:**
   - "Quieres que revise un contrato de arrendamiento contra tus posiciones?"
   - "Tienes alguna escritura de compraventa pendiente de revisar?"
   - "Quieres que compruebe si alguna de tus PH tiene problemas de mayorías pendientes?"
   - Si es arrendador: "Quieres que revise si tus contratos cumplen el régimen tutelado de arrendamientos vigente en Panamá?"

3. **Señalar huecos.**

4. **Cerrar:**

   > "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md`. Lo que respondiste se puede cambiar:
   > - Editar directamente para un cambio rápido
   > - `/inmobiliario:entrevista-inicial --redo` para re-entrevista completa
   > - `/inmobiliario:entrevista-inicial --check-integraciones` para re-comprobar conexiones
   >
   > Las secciones que más se ajustan: las **posiciones en arrendamiento** (verificar el régimen tutelado vigente), las **operaciones habituales** (según evoluciona la cartera), y la **propiedad horizontal** (según cambian las PH gestionadas)."

5. **Tu perfil aprende:**

   > **Tu perfil de práctica aprende.** Mejora conforme usas los plugins. Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

## Modos de fallo

- **No confundir vivienda con uso distinto.** El arrendamiento de vivienda sujeto al régimen tutelado tiene normas imperativas de protección al arrendatario que no aplican al arrendamiento comercial (mayoritariamente dispositivo). Un contrato de local redactado como si fuera vivienda es un error grave. [verificar umbrales y alcance del régimen tutelado]
- **No asumir artículos del régimen de arrendamientos de memoria.** El marco aplicable es la Ley 93 de 1973 (mod. Ley 28 de 1974 y Ley 259 de 2021). El umbral histórico de canon (B/.150/mes, DE 294 de 1994) quedó suspendido por el DE 145 de 2020. Verificar el detalle de los artículos en el texto oficial.
- **No olvidar la retención de la ganancia de capital.** En compraventas, el comprador suele retener un porcentaje del precio como adelanto de la ganancia de capital del vendedor a enterar ante la DGI. Verificar tarifas vigentes.
- **No asumir el régimen de la propiedad.** Verificar la titularidad en el Registro Público (persona natural, sociedad anónima, fundación de interés privado, fideicomiso) y el régimen económico matrimonial cuando proceda (Código de la Familia de Panamá).
- **No dar por hecho que la Ley 284 de 2022 dice lo que crees.** Verificar quórums, mayorías y plazos en el texto vigente antes de citar artículos.
- **No olvidar la prevención de blanqueo.** Las operaciones inmobiliarias pueden estar sujetas a la Ley 23 de 2015 y obligaciones ante la UAF (sujetos obligados). Verificar la debida diligencia exigida.
```
