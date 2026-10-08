# Issues iniciales para GitHub

Copiá cada bloque como un issue nuevo. Etiquetas sugeridas entre [corchetes].

## 1. Incorporar textos oficiales íntegros a `/sources` [normativa][P1]
Descargar de IMPO/Parlamento/gub.uy los textos vigentes de Ley 18.331, Decreto 414/009,
Ley 19.670 (arts. 37-40), Decreto 64/020 y guías URCDP, y colocarlos junto a sus `.md`.
**Aceptación:** cada `sources/*.md` tiene su archivo oficial asociado y fecha de consulta.

## 2. Fijar numeración del bloque de derechos (arts. 12-16) [normativa][P1]
Resolver la discrepancia de numeración (información/acceso/rectificación/comunicación) contra
el texto consolidado de IMPO y quitar las marcas `[verificar numeración]` donde se confirme.
**Aceptación:** numeración verificada y citada con fuente en `sources/ley-18331.md`.

## 3. Confirmar Resoluciones URCDP 63/2023 y 70/2023 [normativa][P1]
Verificar texto, vigencia y alcance (transferencias internacionales, Marco UE-EEUU) y el
listado de países con nivel adecuado.
**Aceptación:** C-10 y `matriz-proveedores-transferencias.md` citan resoluciones verificadas.

## 4. Confirmar umbral de DPO por "grandes volúmenes" [normativa][P2]
Verificar el criterio vigente de la URCDP para el art. 40 de la Ley 19.670.
**Aceptación:** C-13 y `sources/ley-19670-arts-37-40.md` sin `[verificar]` en el umbral.

## 5. Validador de cédula de identidad uruguaya [detección][P2]
Heurística con dígito verificador para distinguir CI real de números cualquiera.
**Aceptación:** la skill detecta campos de CI y reduce falsos positivos.

## 6. Heurísticas por framework [detección][P2]
Añadir patrones para Django, Rails, Laravel, Next.js, Spring (modelos, migraciones, forms).
**Aceptación:** detección de datos personales en al menos 3 frameworks sobre repos de prueba.

## 7. Inferencia de transferencias por región cloud [detección][P3]
Mapear regiones (`us-east-1`, `europe-west`, etc.) a "sale de Uruguay".
**Aceptación:** C-10 propone país/región estimada por proveedor.

## 8. Script de empaquetado `.skill` [tooling][P2]
Empaquetar el repo como skill instalable en Claude Code.
**Aceptación:** `make package` produce un `.skill` instalable.

## 9. GitHub Action: verificación de citas [tooling][P2]
Action que falle si una afirmación normativa en `references/`, `packs/` o `templates/` no
cita `sources/...` o no está marcada `[verificar contra fuente oficial]`.
**Aceptación:** PRs sin cita o marca fallan el check.

## 10. Repos sintéticos de prueba [tests][P2]
Crear repos de ejemplo (SaaS, e-commerce, salud) para evaluar la skill de punta a punta.
**Aceptación:** al menos 3 repos sintéticos con salida esperada documentada.

## 11. Pack sector salud [cobertura][P3]
Extender con datos de salud (Ley 18.331 art. 19) y normativa sanitaria aplicable.
**Aceptación:** `packs/salud/pack.md` con controles específicos y fuentes.

## 12. Guía de inscripción de bases ante la URCDP [docs][P3]
Paso a paso del trámite de registro (Ley 18.331 art. 6; Decreto 414/009).
**Aceptación:** documento con enlaces oficiales y requisitos.
