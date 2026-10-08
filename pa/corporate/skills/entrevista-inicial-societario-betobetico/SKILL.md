---
name: entrevista-inicial-societario-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu práctica societaria, los tipos de sociedad que manejas, tus áreas activas (M&A, secretaría de la junta directiva, cumplimiento registral, gestión de entidades) y tus formatos de documentos corporativos. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados-panama/tree/main/societario/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: pa
practice: corporate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — ejecutar solo la comprobación de integraciones del Parte 0. Al comprobar: solo reportar ✓ si una llamada MCP realmente respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego las partes específicas).
3. Documentos semilla: actas, informes de due diligence, estados financieros.
4. Extraer: estructura societaria, formatos de actas, checklist de DD, gobierno corporativo.
5. Migración: si existe un CLAUDE.md completo en `~/.claude/plugins/cache/claude-para-abogados/societario/*/CLAUDE.md` pero no en la ruta de config, copiarlo y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md` (creando directorios padre si es necesario).

---

## Propósito

La práctica societaria en Panamá abarca desde la constitución de una sociedad anónima o una fundación de interés privado hasta la gestión de la junta directiva de un grupo. Un secretario de la junta directiva vive en actas y certificaciones. Un abogado de M&A vive en due diligence y operaciones corporativas. Un gestor de entidades vive en el Registro Público y las obligaciones de mantenimiento. Esta entrevista descubre qué áreas son las tuyas y construye solo el perfil relevante.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → saludar y ofrecer retomar.
- **Contiene `[PLACEHOLDER]` pero sin pausa** → ofrecer empezar de cero o retomar.
- **Completo** → ya configurado; saltar salvo `--repetir`.

- `--repetir` — entrevista completa, sobrescribe todo
- `--verificar-integraciones` — solo recomprobar conectores

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`.

- **Si existe:** Leerlo. Confirmar: "Eres [nombre], [tipo de práctica], en [empresa], [sector], operando en [jurisdicciones]. ¿Correcto?" Si confirma, saltar preguntas de empresa.
- **Si no existe:** Hacer las preguntas de empresa, escribir el perfil compartido, y continuar con las específicas del plugin.

## Comprobación de ámbito de instalación

Si el directorio de trabajo está dentro de un proyecto, avisar sobre la limitación de lectura de archivos y pedir confirmación.

## Antes de empezar la entrevista

> **`societario` es para quienes trabajan en derecho de sociedades — constituciones, fundaciones de interés privado, M&A, secretaría de la junta directiva, cumplimiento registral y gestión de entidades.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, tipo de práctica y áreas activas, más valores por defecto para formatos de actas y checklist de DD. **15 minutos** añade tus formatos reales de actas y certificaciones, tu checklist de due diligence, tu estructura de gobierno corporativo y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu perfil de práctica societaria (tipos societarios, áreas activas, formatos de documentos corporativos), carpetas por operación, checklist de due diligence y calendario de cumplimiento registral. Aprende cómo trabajas tú. Todo se puede cambiar después."
>
> "¿Listo?"

**Perfil profesional nuevo.** Construido desde las respuestas del usuario y documentos que comparta. No lee historial personal ni conversaciones anteriores.

## Ritmo de la entrevista

- **Asume que la respuesta existe en algún sitio.** Pide enlace o documento antes de que teclee de memoria.
- **Tamaño de lote:** 2-3 preguntas máximo por turno, contando subpartes.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Para subidas:** "Pega el contenido, comparte una ruta, o di 'saltar por ahora.'"
- **Antes de escribir:** listar preguntas saltadas. Esperar confirmación.
- **Pausa y reanudación.** "Si necesitas parar, di 'pausa'." Escribir config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas de artículos (Ley 32 de 1927, Ley 25 de 1995, Código de Comercio de Panamá) antes de escribirlas en la configuración.

---

## La entrevista

### Apertura

> Voy a aprender cómo está organizada tu práctica societaria para que cada acta, cada informe de DD y cada certificación que genere salga como si la hubieras hecho tú — no como una plantilla genérica.

**Ruta rápida:** solo Parte 0 y Parte 1 (tipos societarios). Config con `[POR DEFECTO]`. Cerrar con: "Listo. Valores por defecto para actas, DD y certificaciones. Ejecuta `/societario:entrevista-inicial --completa` cuando quieras."

**Ruta completa:** flujo completo.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> ¿Quién usará este plugin en el día a día?
>
> 1. **Abogado o profesional jurídico** — abogado, secretario del consejo, paralegal bajo supervisión.
> 2. **No abogado con acceso a abogado** — director financiero, gerente, asesor fiscal con abogado accesible.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados que en el patrón base.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: Registro Público en línea, almacenamiento de documentos (Google Drive, SharePoint, Box), herramientas de firma (DocuSign, Panamá firma electrónica) y Slack.

Comprobar conexiones reales, no solo configuración.

#### Tipo de práctica

> - **Despacho pequeño / ejercicio individual**
> - **Despacho mediano / grande**
> - **In-house**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: El despacho/empresa (2-3 min)

> ¿Tienes un organigrama societario, una tabla de entidades o un mapa de grupo? Pega el contenido o comparte una ruta — extraeré la estructura en vez de hacerte teclearla.

Si no:

- **Tipos societarios que manejas:** ¿cuáles de estos?
  - Sociedad Anónima (S.A.)
  - Sociedad de Responsabilidad Limitada (S. de R.L.)
  - Fundación de interés privado (Ley 25 de 1995)
  - Sociedades extranjeras redomiciliadas
  - Otros (sociedad civil, sociedad en comandita, empresa individual)
- **Sectores principales:** ¿en qué sectores operan tus clientes o tu empresa?
- **Número de entidades gestionadas:** ¿cuántas, aproximadamente?

---

### Parte 2: Áreas activas (3-4 min)

> ¿Cuáles de estas áreas forman parte de tu trabajo habitual? Más de una es normal. Dime los números que apliquen — solo configuro las que uses.
>
> 1. **M&A** — compraventas de acciones / cuotas de participación, fusiones, escisiones, aportaciones en especie.
> 2. **Secretaría de la junta directiva** — actas, certificaciones, convocatorias, libros sociales.
> 3. **Cumplimiento registral** — tasa única anual, nombramientos, reformas al pacto social, declaraciones ante la DGI.
> 4. **Gestión de entidades** — estructura de grupo, constituciones, fundaciones de interés privado, disoluciones, reestructuraciones societarias.

Registrar módulos activos. Proceder solo con los activos.

---

### Parte 3: Due diligence (4-5 min, si M&A activo)

> ¿Tienes una checklist estándar de due diligence o un informe de DD previo que pueda leer? Pega el contenido o comparte una ruta.

Si no:

- **Categorías de tu checklist:** ¿cómo la organizas? (Por área: societario, fiscal, laboral, contractual, regulatorio, litigios, propiedad intelectual, medioambiental)
- **Umbrales de materialidad:** ¿cuándo algo es material? (Todos los contratos / >X USD (B/.) / top N por facturación)
- **Formato de informe:** ¿narrativo, tabla de hallazgos, o híbrido?
- **Esquema de severidad:** ¿Rojo/Amarillo/Verde? ¿Alto/Medio/Bajo? ¿Otro?
- **¿Quién recibe el informe?** (Solo el equipo legal, el comprador/vendedor, el consejo)

---

### Parte 4: Gobierno corporativo (4-5 min, si secretaría de la junta directiva activa)

#### Actas

- **Formato de actas:** ¿narrativas detalladas, actas de acuerdo (solo decisiones), o híbridas?
- **Idioma:** ¿solo español, bilingüe español/inglés, otro?
- **Plazo de circulación** después de la junta/consejo
- **Proceso de aprobación:** ¿circuladas para comentarios, aprobadas en la siguiente reunión?

#### Certificaciones

- **Formato de certificación:** ¿formato libre o plantilla fija?
- **¿Quién certifica?** (Secretario, subsecretario, tesorero u otro dignatario)
- **¿Legitimación de firma notarial habitual?**

#### Libros sociales

- **¿Libro de actas y registro de acciones al día?** ¿Custodiados conforme al Código de Comercio?
- **Formato:** ¿digital o físico?
- **¿Quién los mantiene?** (Secretario, agente residente, firma externa)

> Sube 2-3 actas anteriores de juntas de accionistas o juntas directivas cerradas — nada activo. Quiero ver tu formato house: estructura, nivel de detalle, cómo redactas los acuerdos, cómo registras la asistencia.

De las actas semilla, extraer:
- Estructura y orden de secciones
- Formato de cabecera (sociedad, órgano, fecha, lugar)
- Registro de asistencia
- Profundidad de discusión
- Lenguaje de acuerdos (literal)
- Firma

---

### Parte 5: Documentos semilla (2-3 min)

> Además de las actas (si ya las compartiste), ¿puedes compartir alguno de estos?
>
> - **Informe de due diligence** de una operación cerrada
> - **Estados financieros** (balance general, estado de resultados)
> - **Certificación del secretario** de ejemplo
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica societaria
*Escrito por entrevista-inicial el [FECHA]. Áreas activas: [M&A | Secretaría de la junta directiva | Cumplimiento registral | Gestión de entidades]*

### Tipos societarios

| Tipo | Frecuencia | Notas |
|---|---|---|
| [PLACEHOLDER] | [alta/media/baja] | |

### Áreas activas

| Área | Estado | Notas |
|---|---|---|
| M&A | [activa/inactiva] | |
| Secretaría de la junta directiva | [activa/inactiva] | |
| Cumplimiento registral | [activa/inactiva] | |
| Gestión de entidades | [activa/inactiva] | |

### Due diligence (si activo)

**Categorías:** [PLACEHOLDER]
**Umbrales de materialidad:** [PLACEHOLDER]
**Formato de informe:** [PLACEHOLDER]
**Severidad:** [PLACEHOLDER]

### Gobierno corporativo (si activo)

**Formato de actas:** [PLACEHOLDER]
**Certificaciones:** [PLACEHOLDER]
**Libros sociales:** [PLACEHOLDER]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en práctica societaria:**
>
> - **Due diligence societaria** — checklist estructurada con tus categorías y umbrales. Prueba: `/societario:due-diligence`
> - **Redactar actas de junta directiva o de accionistas** — en tu formato house, con el nivel de detalle que usas. Prueba: `/societario:actas`
> - **Certificaciones del secretario** — desde plantillas aprendidas de tus documentos. Prueba: `/societario:certificacion`
> - **Calendario de cumplimiento registral** — qué hay que presentar y cuándo. Prueba: `/societario:cumplimiento-registral`
>
> **Mi sugerencia para empezar:** Si tienes una operación en curso, ejecuta `/societario:due-diligence` — verás si entiende tu checklist.

Conectar herramienta de investigación:

> "Antes de tu primer informe: conecta una herramienta de investigación jurídica."

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`. Todo se puede cambiar:
>
> - Edita el archivo directamente
> - `/societario:entrevista-inicial --repetir` para re-entrevista completa
> - `/societario:entrevista-inicial --verificar-integraciones` para recomprobar conectores
>
> Lo que más se ajusta: el formato de actas, los umbrales de DD y las categorías de checklist."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin:
>
> - Cuando una salida no encaje, suele ser una posición que ajustar.
> - Puedes decir "actualiza mi formato de actas" o "cambia mi umbral de materialidad" y el skill escribirá el cambio.
> - Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No asumas que todas las áreas están activas.** Un abogado de M&A no necesita configurar secretaría de la junta directiva.
- **No confundas tipos societarios.** Una S.A. (Ley 32 de 1927) y una S. de R.L. tienen regímenes diferentes. No mezcles.
- **No escribas formatos genéricos de actas.** Si el usuario te dio actas semilla, extrae su formato exacto.
- **No asumas régimen registral.** El Registro Público tiene plazos y requisitos específicos — verifica antes de escribir.
- **No pidas documentos semilla para áreas inactivas.**
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo. Quieres entender cómo trabaja el otro para ayudar de verdad.
