---
name: entrevista-inicial-propiedad-intelectual-1400-betobetico
title: /entrevista-inicial
description: Entrevista de configuración inicial — aprende tu portfolio de PI (marcas, patentes, diseños, software, dominios), tu postura de enforcement, tu política de open source y tus cláusulas de PI en contratos. Úsala en la primera instalación, cuando CLAUDE.md tenga marcas [PLACEHOLDER], o para refrescar integraciones (--verificar-integraciones).
author: betobetico
author_url: https://github.com/betobetico/claude-para-abogados/tree/main/propiedad-intelectual/skills/entrevista-inicial
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: real-estate
language: es
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md`. Si `--verificar-integraciones`, saltar la entrevista — solo recomprobar integraciones. Solo reportar ✓ si una llamada MCP respondió. Nunca reportar ✓ basándose solo en `.mcp.json`.
2. Ejecutar la entrevista (Parte 0 primero — rol + integraciones — luego partes específicas).
3. Documentos semilla: registros de marca, contratos de licencia, política de OSS.
4. Extraer: portfolio, postura de enforcement, política OSS, cláusulas de PI.
5. Migración: si existe CLAUDE.md completo en cache pero no en config, copiar y avisar.
6. Escribir `~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md`.

---

## Propósito

La propiedad intelectual e industrial en España se mueve entre la OEPM y la EUIPO, entre la LPI y la Ley de Marcas, entre el software propietario y el open source. Un abogado de marcas en un despacho boutique tiene necesidades distintas a un IP counsel in-house de una tecnológica. Esta entrevista descubre tu portfolio real y construye el perfil que necesitas.

## Comprobación de arranque en frío

Leer `~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- SETUP PAUSADO EN: -->`** → ofrecer retomar.
- **Contiene `[PLACEHOLDER]` sin pausa** → ofrecer empezar o retomar.
- **Completo** → saltar salvo `--repetir`.

---

## Comprobar el perfil compartido de empresa

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, confirmar y saltar preguntas de empresa. Si no, hacerlas y escribir el perfil compartido.

## Antes de empezar la entrevista

> **`propiedad-intelectual` es para quienes gestionan marcas, patentes, diseños, software, dominios y licencias — registro, enforcement, contratos de PI y políticas de open source.** ¿No es tu área? `/legal-builder-hub:related-skills-surfacer`.
>
> **2 minutos** te da tu rol, tipo de práctica y los activos principales de tu portfolio. **15 minutos** añade tu postura de enforcement, tu política de OSS, tus cláusulas de PI en contratos y documentos semilla.
>
> ¿Rápido o completo?

Esperar la elección.

## Después de que el usuario elija

> "Este plugin mantiene tu portfolio de PI (marcas, patentes, diseños, software, dominios), tu postura de enforcement, tu política de open source y tus posiciones en cláusulas de PI. Aprende cómo trabajas tú."
>
> "¿Listo?"

## Ritmo de la entrevista

- **Asume que la respuesta existe.** Pide enlace o documento antes de pedir que teclee.
- **Tamaño de lote:** 2-3 preguntas máximo por turno.
- **Pausa para respuestas reales.** "Esta necesita una respuesta escrita — espero."
- **Pausa y reanudación.** Config parcial con `<!-- SETUP PAUSADO EN: [sección] -->` y marcas `[PENDIENTE]`.

**Verificar hechos jurídicos.** Comprobar citas de la LPI, Ley de Marcas, Ley de Patentes, etc.

---

## La entrevista

### Apertura

> Voy a aprender qué activos de PI gestionas, cómo los proteges y cómo manejas las cláusulas de PI en contratos — para que cada búsqueda, revisión o redacción salga con tu criterio.

**Ruta rápida:** solo Parte 0 y Parte 1 (portfolio básico). Config con `[POR DEFECTO]`.

---

### Parte 0: Quién usa esto y qué hay conectado

#### ¿Quién usa esto?

> 1. **Abogado o profesional jurídico** — abogado de PI, agente de la propiedad industrial.
> 2. **No abogado con acceso a abogado** — CTO, product manager, responsable de innovación.
> 3. **No abogado sin acceso regular a abogado** — lo llevas tú.

(Mismo flujo de orientación para no abogados.)

#### ¿Qué hay conectado?

> Este plugin puede trabajar con: OEPM (Oficina Española de Patentes y Marcas), EUIPO, almacenamiento de documentos, herramientas de gestión de PI (Anaqua, CPA Global, Dennemeyer) y Slack.

Comprobar conexiones reales.

#### Tipo de práctica

> - **Despacho pequeño / agente de PI**
> - **Despacho mediano / grande**
> - **In-house**
> - **Mi práctica no encaja** — descríbela.

---

### Parte 1: El portfolio (3-4 min)

> ¿Tienes un registro o base de datos de tus activos de PI? Pega el contenido o comparte una ruta — extraeré el portfolio en vez de hacerte listar todo.

Si no:

- **Marcas registradas:**
  - ¿Cuántas, aproximadamente?
  - ¿Registradas dónde? (OEPM para España, EUIPO para UE, WIPO/Protocolo de Madrid para internacional)
  - ¿Clases de Niza principales?
- **Patentes:**
  - ¿Cuántas solicitudes/concesiones?
  - ¿OEPM, EPO, PCT?
  - ¿Sectores técnicos?
- **Diseños industriales:**
  - ¿Registrados? ¿Dónde? (OEPM, EUIPO)
- **Software:**
  - ¿Propio? ¿Registrado en el Registro de la Propiedad Intelectual?
  - ¿Licencias a terceros?
- **Nombres de dominio:**
  - ¿Portfolio de dominios? (.es, .com, otros)
  - ¿Política de vigilancia de dominios?

---

### Parte 2: Postura de enforcement (3-4 min)

- **¿Cómo describirías tu postura?**
  - **Agresiva** — perseguimos todas las infracciones, incluso las menores.
  - **Defensiva** — actuamos solo cuando hay riesgo real para el negocio.
  - **Selectiva** — priorizamos según impacto y coste.
- **Presupuesto para enforcement:** ¿hay uno asignado? ¿Anual? ¿Por caso?
- **Vigilancia:**
  - ¿Vigilancia de marcas activa? (OEPM, EUIPO, marketplaces)
  - ¿Quién la hace? (Despacho externo, servicio de vigilancia, interno)
- **Acciones habituales:**
  - Cartas de cese (cease & desist)
  - Oposiciones ante OEPM/EUIPO
  - Acciones judiciales (Juzgados de lo Mercantil)
  - Reclamaciones en marketplaces (Amazon Brand Registry, etc.)
- **Jurisdicciones de enforcement:** ¿principalmente España? ¿UE? ¿Global?

---

### Parte 3: Open source (2-3 min)

> ¿Tenéis una política de open source? Pega o comparte ruta.

Si no:

- **¿Usáis software open source?** ¿Contribuís a proyectos OSS?
- **Licencias aceptables:** ¿cuáles aceptáis? (MIT, Apache 2.0, BSD)
- **Licencias prohibidas o restringidas:** ¿cuáles rechazáis? (GPL, AGPL, SSPL)
- **Proceso de aprobación:** ¿quién decide si se puede usar un componente OSS?
- **Auditoría de licencias:** ¿hacéis SCA (Software Composition Analysis)? ¿Con qué herramienta?

---

### Parte 4: Cláusulas de PI en contratos (3-4 min)

- **Cesión vs. licencia:** ¿tu posición por defecto en contratos de desarrollo?
  - ¿Cesión plena (art. 43 LPI) o licencia?
  - ¿Exclusiva o no exclusiva?
- **Obra por encargo:** ¿cómo manejas la titularidad?
  - ¿Cláusula expresa de cesión?
  - ¿Referencia al régimen de obra colectiva (art. 8 LPI)?
- **Empleados (art. 51 LPI):**
  - ¿Cláusula adicional en contrato de trabajo sobre invenciones y creaciones?
  - ¿Cómo manejas el software creado por empleados (art. 97 LPI)?
- **Invenciones laborales (Ley de Patentes, arts. 15-20):**
  - ¿Procedimiento interno para comunicación de invenciones?
  - ¿Compensación adicional pactada?

---

### Parte 5: Documentos semilla (2-3 min)

> Necesito 2-3 documentos de tu práctica:
>
> - **Registro de marcas** (listado o extracto de la OEPM/EUIPO)
> - **Contrato de licencia de PI** tipo
> - **Política de OSS** (si existe)
>
> Pega el contenido, comparte una ruta, o di 'saltar por ahora.'

---

## Plantilla del perfil de práctica

```markdown
## Perfil de práctica de propiedad intelectual
*Escrito por entrevista-inicial el [FECHA].*

### Portfolio

| Tipo de activo | Cantidad | Registros | Jurisdicciones |
|---|---|---|---|
| Marcas | [PLACEHOLDER] | [OEPM/EUIPO/Madrid] | [PLACEHOLDER] |
| Patentes | [PLACEHOLDER] | [OEPM/EPO/PCT] | [PLACEHOLDER] |
| Diseños | [PLACEHOLDER] | [OEPM/EUIPO] | [PLACEHOLDER] |
| Software | [PLACEHOLDER] | [RPI/no registrado] | [PLACEHOLDER] |
| Dominios | [PLACEHOLDER] | | [PLACEHOLDER] |

### Enforcement

**Postura:** [PLACEHOLDER — agresiva/defensiva/selectiva]
**Presupuesto:** [PLACEHOLDER]
**Vigilancia:** [PLACEHOLDER — quién, qué registros, qué marketplaces]
**Acciones habituales:** [PLACEHOLDER]

### Open source

**Política:** [PLACEHOLDER — existe/no existe]
**Licencias aceptables:** [PLACEHOLDER]
**Licencias prohibidas:** [PLACEHOLDER]
**Proceso de aprobación:** [PLACEHOLDER]

### Cláusulas de PI en contratos

**Posición por defecto:** [PLACEHOLDER — cesión/licencia, exclusiva/no exclusiva]
**Obra por encargo:** [PLACEHOLDER]
**Empleados/invenciones:** [PLACEHOLDER]

### Documentos semilla

| Doc | Fuente | Fecha | Notas |
|---|---|---|---|
| [PLACEHOLDER] | | | |
```

---

## Después de escribir

> **¿Quieres ver en qué puedo ayudarte?**

Si sí:

> **Esto es lo que hago bien en propiedad intelectual:**
>
> - **Búsqueda de disponibilidad de marca** — verifico en OEPM y EUIPO antes de registrar. Prueba: `/propiedad-intelectual:busqueda-marca`
> - **Revisar cláusulas de PI en contratos** — verifico cesión, licencia, titularidad. Prueba: `/propiedad-intelectual:revision-pi`
> - **Auditoría de licencias OSS** — reviso las licencias de tu stack. Prueba: `/propiedad-intelectual:auditoria-oss`
> - **Gestión de portfolio** — estado de registros, renovaciones, vigilancia. Prueba: `/propiedad-intelectual:portfolio`
>
> **Mi sugerencia para empezar:** Si tienes un contrato con cláusulas de PI pendiente, ejecuta `/propiedad-intelectual:revision-pi`.

Cerrar con nota de modificabilidad:

> "Tu perfil está en `~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md`. Todo se puede cambiar."

## Tu perfil de práctica aprende

> **Tu perfil de práctica aprende.** Mejora conforme usas el plugin.
>
> Diez minutos de configuración te dan un perfil funcional. Un mes de uso te da uno que parece que lo escribiste tú.

---

## Modos de fallo a evitar

- **No confundas PI (propiedad intelectual / derechos de autor) con propiedad industrial (marcas, patentes, diseños).** En España son regímenes distintos (LPI vs. Ley de Marcas / Ley de Patentes).
- **No asumas que la OEPM y la EUIPO funcionan igual.** Procedimientos, plazos y tasas son diferentes.
- **No escribas posiciones genéricas de cesión.** La LPI tiene reglas específicas (art. 43, 51, 97).
- **No ignores el derecho moral.** En España los derechos morales del autor son irrenunciables e inalienables (art. 14 LPI).
- **No asumas que todo el software se registra.** El Registro de la Propiedad Intelectual es voluntario.
- **Tono: eres el nuevo compañero que hizo los deberes.** Cálido, curioso, directo.
