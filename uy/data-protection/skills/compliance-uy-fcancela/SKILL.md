---
name: compliance-uy-fcancela
title: compliance-uy — Motor de cumplimiento (Uruguay), multi-marco y self-service
description: Esta skill se usa cuando el usuario pide "armar el compliance", "cumplir la Ley 18.331", "preparar la protección de datos", "auditar datos personales", "generar política de privacidad / DPA / RAT / DPIA / consentimiento", "inscribir bases en la URCDP", "cumplir la ley de datos en Uruguay" o "prevención de lavado de activos (Ley 19.574)". Audita un repo y genera, SIN abogado, toda la documentación de cumplimiento para un SaaS o empresa en Uruguay, contrastada contra el texto oficial de la ley. Cubre la Ley 18.331 (protección de datos personales, con sus reformas de la Ley 19.670 y el Decreto 64/020) y la Ley 19.574 (prevención de LA/FT, para sujetos obligados), y es extensible a más marcos (packs).
author: fcancela
author_url: https://github.com/fcancela/compliance-uy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: uy
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
- title: Mapa Articulos 18331
  path: references/mapa-articulos-18331.md
- title: Mapa Articulos 19574
  path: references/mapa-articulos-19574.md
- title: Output Model
  path: references/output-model.md
- title: Revisiones Periodicas
  path: references/revisiones-periodicas.md
---

# compliance-uy — Motor de cumplimiento (Uruguay), multi-marco y self-service

Auditar una aplicación contra uno o varios **packs** de ley, **resolver las decisiones** con el criterio
de la ley y **generar toda la documentación rellenada** (sin dejar tarea), dejando un **estado versionado**
en el repo que se re-corre en el tiempo. Objetivo: que un founder cumpla **solo**; el abogado es opcional
(ver `references/cuando-acudir-a-abogado.md`).

> **DISCLAIMER OBLIGATORIO** — No constituye asesoría legal (un software no asume la responsabilidad legal
> del usuario). Genera borradores fundados en la normativa uruguaya para cumplir sin abogado. Incluir este
> disclaimer al pie de cada documento legal generado.

## Modelo mental
- **Controles** = unidades reutilizables que satisfacen varios marcos a la vez. Catálogo + crosswalk:
  `references/controls.md`.
- **Packs** = una ley/marco cada uno (`packs/<id>/pack.md`): obligaciones, controles que exige y documentos a
  generar. Hoy: `ley-18331` (datos), `ley-19574` (LA/FT).
- **Estado** = el output vive en `<repo>/.compliance/` versionado por git. Formato: `references/output-model.md`.
- **Fuentes (verdad)** = textos OFICIALES en `sources/` (`FUENTES.md`, de IMPO). Toda afirmación legal cita
  **ley/decreto + artículo + archivo**; lo no verificable se marca `[verificar contra fuente oficial]`. NADA
  inventado. Numeración verificada: `references/mapa-articulos-18331.md` y `references/mapa-articulos-19574.md`.

## Flujo

### Fase 0 — Encuadre (CUESTIONARIO: recoger todo para no dejar `[COMPLETAR]`)
Mostrar el disclaimer. Luego preguntar al usuario (con `AskUserQuestion` cuando aplique) y **registrar las
respuestas para rellenar los documentos**. No dejar placeholders salvo que el dato sea genuinamente
desconocido; en ese caso, proponer un **default sensato** y marcarlo.
Recoger:
1. Repo a auditar y **packs** a activar (default: `ley-18331`; activar `ley-19574` **solo si la empresa es
   sujeto obligado** — ver Fase 2).
2. **Empresa:** razón social, RUT, domicilio, correo de contacto, tamaño, representante legal.
3. **Responsable de datos / Delegado (DPO)** designado (en micro suele ser el dueño).
4. Por flujo de datos: rol **responsable** vs **encargado**.
5. **Plazos de retención** por tipo de dato; si no los sabe, proponer defaults razonables.
6. ¿Tratan **datos sensibles** (Art. 4 lit. E)? ¿Más de **35.000 personas**? (gatilla DPO + DPIA). ¿Hacen
   **perfiles** o tratan datos de **menores**? ¿Usuarios/transferencias **fuera de Uruguay**?
7. **¿La empresa es "sujeto obligado" de LA/FT?** (Ley 19.574 arts. 12-13 — ver el test del pack `ley-19574`).
Si ya existe `<repo>/.compliance/state.json`, leerlo: esta corrida es una re-evaluación.

### Fase 1 — Descubrimiento (leer el código, no asumir)
Recorrer el repo con Grep/Glob para levantar evidencia de cada control:
- Datos personales (esquemas/migraciones/modelos/formularios): `email|phone|telefono|cedula|ci|rut|address|domicilio|nombre|name|ip|lat|lng|password`; marcar **datos sensibles** específicos (salud, biométricos, menores).
- Proveedores externos y transferencias internacionales (`.env*`, `package.json`, configs): AWS, Google, Meta, etc.; marcar los que procesan **fuera de Uruguay**.
- Medidas técnicas: TLS, cifrado en reposo, hashing de password, MFA, logs/auditoría, segregación por tenant, secretos fuera del código, disociación/seudonimización, privacidad por diseño/defecto.
- Gobernanza (no está en el código): tomarla del cuestionario; marcar `❓` lo no verificable por código.

**Señales de alerta (benchmarks rápidos a chequear):**
- Formularios que capturan datos **sin checkbox de consentimiento** o con casilla **premarcada** (viola Art. 9 / Decreto 414/009 art. 6).
- Captura de datos **sin enlace a la política de privacidad** ni aviso del Art. 13 en el punto de captura.
- **Secretos/credenciales hardcodeados** en el código (registrar solo `archivo:línea`, **nunca** copiar el valor).
- Endpoints que exponen datos personales **sin autenticación** o sin segregación por tenant.
- Datos sensibles (salud, biométricos, menores) tratados sin el consentimiento reforzado del Art. 18.
- Proveedores fuera de Uruguay **sin** declaración de transferencia (Art. 23) ni DPA.

> **Límite de alcance (decírselo al usuario):** la skill audita el **código del repo**. La privacidad **no
> vive solo ahí**: también fluye por correo, WhatsApp, CRM, planillas, herramientas SaaS, formularios en
> papel y procesos manuales que el escaneo **no ve**. Esos canales quedan a cargo del responsable; la skill
> los incorpora al RAT por cuestionario, pero no puede verificarlos. Ver `SECURITY.md`.

### Fase 2 — Evaluar controles y RESOLVER decisiones
Para cada control de `references/controls.md`: estado (✅/⚠️/❌/❓) + evidencia + remediación. Un control
se propaga a todos los marcos que lo exigen.
**Resolver las decisiones** (no dejarlas abiertas), citando el artículo:
- **DPO** (Decreto 64/020 art. 10): obligatorio para entidades públicas, privadas que traten datos sensibles
  como giro principal, o que traten **+35.000 personas**; si no, lo asume el responsable → dar el resultado.
  El DPO es **una persona** (en micro/pyme puede ser el dueño), **no la skill ni un bot**: la skill ayuda a
  designarlo, documentar el acta y comunicarlo a la URCDP en 90 días (art. 14), pero el rol y la cultura
  interna los sostiene una persona. Comunicar la designación a la URCDP en **90 días**.
- **DPIA** (Decreto 64/020 art. 6): aplicar el test de `packs/ley-18331/templates/dpia.md`; si aplica un
  supuesto, es obligatoria.
- **Inscripción de bases en la URCDP** (Art. 29): siempre exigible → preparar el documento.
- **Base de licitud** por flujo (Art. 9) y **mecanismo de transferencia** (Art. 23).
- **¿Sujeto obligado de LA/FT?** (Ley 19.574 arts. 12-13): si **no** encuadra en ningún literal, **no activar**
  el pack `ley-19574` y decírselo. Si encuadra, activarlo.

### Fase 3 — Generar TODA la documentación (rellenada)
Por cada pack activo, leer su `pack.md` y generar **todos** sus `templates/`, **rellenados con las
respuestas de Fase 0 y los hallazgos de Fase 1**. Para `ley-18331`: rat, política, consentimiento,
canal-derechos, dpa, anexo-transferencias, plan-respuesta-brechas, registro-vulneraciones,
inscripcion-bases-urcdp, y dpia (si el test la hace obligatoria). Para `ley-19574` (solo si es sujeto
obligado): programa-prevencion-laft, matriz-riesgos, acta-oficial-cumplimiento,
procedimiento-debida-diligencia, procedimiento-ros, codigo-conducta. Reemplazar todos los placeholders; usar
`[COMPLETAR: ...]` solo para lo realmente desconocido.

### Fase 4 — Escribir el estado versionado
Escribir en `<repo>/.compliance/` según `references/output-model.md`: `state.json` (controles + score por
marco), `docs/` (todo lo generado), `INSTRUCTIVO.md` (runbooks desde `references/instructivo-situaciones.md`)
y `RESUMEN.md` (postura, brechas priorizadas, **diff vs la corrida anterior**, y qué quedó resuelto solo).
Sugerir commitear `.compliance/`.

### Fase 5 — Cierre y construcción
Reportar la postura por marco. Para cada hueco con remediación de código, **ofrecer construirlo** (esta
skill corre en Claude Code) siguiendo las **recetas de `references/build/`** (MFA, cifrado en reposo,
audit log + actor/IP, endpoints de acceso/supresión, consentimiento, retención): en una rama, con tests y
los gates del repo. Ofrecer también **montar el monitoreo** (`references/build/monitoreo.md`: secret scanning
+ HIBP + alertas + watcher); la skill no vigila en vivo, pero deja el monitoreo instalado. Sugerir **agendar
re-corridas periódicas** (`references/revisiones-periodicas.md`) para detectar drift. Cerrar con UN siguiente paso.

## Reglas
- **Fuente de verdad = `sources/`.** Cita ley/decreto + artículo + archivo; `[verificar contra fuente oficial]`
  si no se confirma. Nunca basar una afirmación normativa en un blog.
- **No inventar derechos:** en Uruguay los derechos del titular son **acceso (Art. 14)** y **rectificación,
  actualización, inclusión o supresión (Art. 15)**. **No** existen portabilidad/oposición/bloqueo al estilo RGPD.
- **No confundir marcos con Chile:** Uruguay **NO** tiene responsabilidad penal de la persona jurídica. El pack
  `ley-19574` es **prevención de LA/FT para sujetos obligados**, no un "modelo de prevención de delitos" eximente.
- **Self-service:** rellenar todo desde el cuestionario; resolver las decisiones; no derivar al abogado lo que
  la skill puede entregar. El abogado es opcional (ver `references/cuando-acudir-a-abogado.md`).
- No inventar datos de la empresa ni normativa. `[COMPLETAR]` solo para lo desconocido; `❓` para lo no
  verificable por código.
- **Manejo de secretos:** si encontrás credenciales/secretos en el código, registralos como **ubicación**
  (`archivo:línea`) — **nunca** copies el valor a `.compliance/` ni a un documento. La remediación es rotarlos
  y moverlos a variables de entorno / gestor de secretos. La skill corre local; no exfiltra nada (ver `SECURITY.md`).
- **No prometer "cumplimiento garantizado" ni "te deja en regla".** La skill deja **borradores y un
  diagnóstico** que acercan al cumplimiento y dicen qué falta; la interpretación legal tiene zonas grises y la
  decisión final (human-in-the-loop) es del usuario.
- Distinguir responsable vs encargado en cada flujo.
- No prometer "cumplimiento garantizado/certificado". Insumos NO self-service: la auditoría independiente del
  programa de LA/FT (si aplica), la representación si hay inspección, y el **monitoreo en tiempo real** (es un
  servicio aparte; la skill prepara el plan de respuesta y puede configurar alertas, pero no vigila 24/7).

## Recursos
- `references/controls.md` — catálogo de controles + crosswalk.
- `references/output-model.md` — formato del estado `.compliance/`.
- `references/mapa-articulos-18331.md` / `mapa-articulos-19574.md` — artículos verificados contra el texto oficial.
- `references/cuando-acudir-a-abogado.md` — por qué el abogado es opcional.
- `references/instructivo-situaciones.md` — runbooks (habeas data, brecha 72h, inspección URCDP/SENACLAFT, ROS, calendario).
- `references/build/` — **recetas de construcción** (MFA, cifrado, audit log, acceso/supresión, consentimiento,
  retención, monitoreo) con librerías verificadas. Ver `references/build/index.md`.
- `references/revisiones-periodicas.md` — automatizar la re-corrida (`/loop`, cron headless `claude -p`,
  `/schedule`) para detectar drift entre corridas.
- `packs/ley-18331/`, `packs/ley-19574/` — obligaciones + plantillas por marco.
- `sources/` — textos legales oficiales (Ley 18.331, Decretos 414/009 y 64/020, Ley 19.670, Ley 19.574,
  Decreto 379/018) + `FUENTES.md`.
