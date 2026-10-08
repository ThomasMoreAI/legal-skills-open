---
name: compliance-cl-lelemon-studio
title: compliance-cl — Motor de cumplimiento (Chile), multi-marco y self-service
description: Esta skill se usa cuando el usuario pide "armar el compliance", "cumplir la Ley 21.719", "preparar la protección de datos", "auditar datos personales", "generar política de privacidad / DPA / RAT / EIPD / consentimiento", "cumplir la ley de datos en Chile" o "modelo de prevención de delitos (Ley 21.595)". Audita un repo y genera, SIN abogado, toda la documentación de cumplimiento para un SaaS o empresa en Chile, contrastada contra el texto oficial de la ley. Cubre la Ley 21.719 (datos personales, vigencia dic-2026) y la 21.595 (delitos económicos, ya vigente), y es extensible a más marcos (packs).
author: Lelemon-studio
author_url: https://github.com/Lelemon-studio/compliance-cl
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cl
practice: data-protection
language: es
sources:
- title: Derechos Y Datos
  path: references/build/derechos-y-datos.md
- title: Index
  path: references/build/index.md
- title: Monitoreo
  path: references/build/monitoreo.md
- title: Seguridad
  path: references/build/seguridad.md
- title: Controls
  path: references/controls.md
- title: Cuando Acudir A Abogado
  path: references/cuando-acudir-a-abogado.md
- title: Instructivo Situaciones
  path: references/instructivo-situaciones.md
- title: Mapa Articulos 21719
  path: references/mapa-articulos-21719.md
- title: Output Model
  path: references/output-model.md
- title: Revisiones Periodicas
  path: references/revisiones-periodicas.md
---

# compliance-cl — Motor de cumplimiento (Chile), multi-marco y self-service

Auditar una aplicación contra uno o varios **packs** de ley, **resolver las decisiones** con el criterio
de la ley y **generar toda la documentación rellenada** (sin dejar tarea), dejando un **estado versionado**
en el repo que se re-corre en el tiempo. Objetivo: que un founder cumpla **solo**; el abogado es opcional
(ver `references/cuando-acudir-a-abogado.md`).

> **DISCLAIMER OBLIGATORIO** — No constituye asesoría legal (un software no asume la responsabilidad legal
> del usuario). Genera borradores fundados en la normativa chilena para cumplir sin abogado. Incluir este
> disclaimer al pie de cada documento legal generado.

## Modelo mental
- **Controles** = unidades reutilizables que satisfacen varios marcos a la vez. Catálogo + crosswalk:
  `references/controls.md`.
- **Packs** = una ley cada uno (`packs/<id>/pack.md`): obligaciones, controles que exige y documentos a
  generar. Hoy: `ley-21719`, `ley-21595`.
- **Estado** = el output vive en `<repo>/.compliance/` versionado por git. Formato: `references/output-model.md`.
- **Fuentes (verdad)** = textos OFICIALES en `sources/` (`FUENTES.md`). Toda afirmación legal cita
  **ley + artículo + archivo**; lo no verificable se marca `[verificar contra fuente oficial]`. NADA
  inventado. Numeración verificada: `references/mapa-articulos-21719.md`.

## Flujo

### Fase 0 — Encuadre (CUESTIONARIO: recoger todo para no dejar `[COMPLETAR]`)
Mostrar el disclaimer. Luego preguntar al usuario (con `AskUserQuestion` cuando aplique) y **registrar las
respuestas para rellenar los documentos**. No dejar placeholders salvo que el dato sea genuinamente
desconocido; en ese caso, proponer un **default sensato** y marcarlo.
Recoger:
1. Repo a auditar y **packs** a activar (default: `ley-21595` + `ley-21719`).
2. **Empresa:** razón social, RUT, domicilio, correo de contacto, tamaño, representante legal.
3. **Responsable de datos / encargado de prevención** designado (en micro suele ser el dueño).
4. Por flujo de datos: rol **responsable** vs **encargado**.
5. **Plazos de retención** por tipo de dato; si no los sabe, proponer defaults razonables.
6. ¿Tratan **datos sensibles** (salud, etc.)? ¿Usuarios en la **UE** (gatilla GDPR a futuro)?
Si ya existe `<repo>/.compliance/state.json`, leerlo: esta corrida es una re-evaluación.

### Fase 1 — Descubrimiento (leer el código, no asumir)
Recorrer el repo con Grep/Glob para levantar evidencia de cada control:
- Datos personales (esquemas/migraciones/modelos/formularios): `email|phone|telefono|rut|address|nombre|name|ip|lat|lng|password`; marcar **datos sensibles** específicos (salud, biométricos, menores).
- Proveedores externos y transferencias internacionales (`.env*`, `package.json`, configs): AWS, Google, Meta, etc.; marcar los que procesan fuera de Chile.
- Medidas técnicas: TLS, cifrado en reposo, hashing de password, MFA, logs/auditoría, segregación por tenant, secretos fuera del código, seudonimización, privacy-by-default.
- Gobernanza (no está en el código): tomarla del cuestionario; marcar `❓` lo no verificable por código.

### Fase 2 — Evaluar controles y RESOLVER decisiones
Para cada control de `references/controls.md`: estado (✅/⚠️/❌/❓) + evidencia + remediación. Un control
se propaga a todos los marcos que lo exigen.
**Resolver las decisiones** (no dejarlas abiertas), citando el artículo:
- **DPO** (Art. 50): obligatorio solo para organismos públicos o datos sensibles a gran escala; si no,
  basta el responsable designado → dar el resultado.
- **EIPD** (Art. 15 ter): aplicar el test de `packs/ley-21719/templates/eipd.md`; si aplica un supuesto, es obligatoria.
- **Base de licitud** por flujo y **mecanismo de transferencia** (cláusulas modelo).

### Fase 3 — Generar TODA la documentación (rellenada)
Por cada pack activo, leer su `pack.md` y generar **todos** sus `templates/`, **rellenados con las
respuestas de Fase 0 y los hallazgos de Fase 1**. Para `ley-21719`: rat, política, consentimiento,
canal-derechos, dpa, anexo-transferencias, plan-respuesta-brechas, registro-vulneraciones, y eipd (si el
test la hace obligatoria). Para `ley-21595`: modelo-prevencion-delitos, código-etica, matriz-riesgos,
acta-encargado-prevencion, reglamento-canal-denuncias. Reemplazar todos los placeholders; usar
`[COMPLETAR: ...]` solo para lo realmente desconocido.

### Fase 4 — Escribir el estado versionado
Escribir en `<repo>/.compliance/` según `references/output-model.md`: `state.json` (controles + score por
marco), `docs/` (todo lo generado), `INSTRUCTIVO.md` (runbooks desde `references/instructivo-situaciones.md`)
y `RESUMEN.md` (postura, brechas priorizadas, **diff vs la corrida anterior**, y qué quedó resuelto solo +
el único insumo externo: supervisión anual del MPD). Sugerir commitear `.compliance/`.

### Fase 5 — Cierre y construcción
Reportar la postura por marco. Para cada hueco con remediación de código, **ofrecer construirlo** (esta
skill corre en Claude Code) siguiendo las **recetas de `references/build/`** (MFA, cifrado en reposo,
audit log + actor/IP, endpoints ARCO, consentimiento, retención): en una rama, con tests y los gates del
repo. Ofrecer también **montar el monitoreo** (`references/build/monitoreo.md`: secret scanning + HIBP +
alertas + watcher); la skill no vigila en vivo, pero deja el monitoreo instalado. Sugerir **agendar
re-corridas periódicas** (`references/revisiones-periodicas.md`) para detectar drift. Cerrar con UN siguiente paso.

## Reglas
- **Fuente de verdad = `sources/`.** Cita ley + artículo + archivo; `[verificar contra fuente oficial]` si
  no se confirma. Nunca basar una afirmación normativa en un blog.
- **Self-service:** rellenar todo desde el cuestionario; resolver las decisiones; no derivar al abogado lo
  que la skill puede entregar. El abogado es opcional (ver `references/cuando-acudir-a-abogado.md`).
- No inventar datos de la empresa ni normativa. `[COMPLETAR]` solo para lo desconocido; `❓` para lo no
  verificable por código.
- Distinguir responsable vs encargado en cada flujo.
- No prometer "cumplimiento garantizado/certificado". Insumos NO self-service: la **supervisión externa
  anual del MPD (21.595)**, la representación si hay fiscalización, y el **monitoreo/detección de
  filtraciones en tiempo real** (es un servicio aparte; la skill prepara el plan de respuesta y puede
  configurar alertas sobre el audit log, pero no hace vigilancia 24/7).

## Recursos
- `references/controls.md` — catálogo de controles + crosswalk.
- `references/output-model.md` — formato del estado `.compliance/`.
- `references/mapa-articulos-21719.md` — artículos verificados contra el texto oficial.
- `references/cuando-acudir-a-abogado.md` — por qué el abogado es opcional.
- `references/instructivo-situaciones.md` — runbooks (ARCO, brecha, fiscalización, calendario).
- `references/build/` — **recetas de construcción** (cómo implementar cada remediación: MFA, cifrado,
  audit log + actor/IP, ARCO, consentimiento, retención, monitoreo) con librerías verificadas. Ver
  `references/build/index.md`.
- `references/revisiones-periodicas.md` — automatizar la re-corrida (`/loop`, cron headless `claude -p`,
  `/schedule`) para detectar drift entre corridas.
- `packs/ley-21719/`, `packs/ley-21595/` — obligaciones + plantillas por marco.
- `sources/` — textos legales oficiales (ley 21.719 PDF/txt, cláusulas modelo, XML) + `FUENTES.md`.
  ⚠️ Para **retener** datos hace falta el **Código Tributario** y el **Código del Trabajo**, que NO se
  versionan acá (repo público, redistribución BCN sin confirmar): `FUENTES.md` trae el `curl` para bajarlos y
  los artículos ya verificados. Sin ellos una retención queda sin fundamento — la 21.719 remite a la
  obligación legal, pero la pone otra ley.
