# Roadmap

Estado: **v0.1 (semilla)**. Lo que sigue es tentativo y abierto a la comunidad.

## v0.1 — Semilla (actual)
- [x] Motor `SKILL.md`
- [x] Catálogo de 14 controles (`references/controls.md`)
- [x] Pack Ley 18.331 (`packs/ley-18331/pack.md`)
- [x] 10 plantillas + `state.schema.json`
- [x] Fuentes oficiales indexadas (`/sources`)
- [x] Ejemplo de salida

## v0.2 — Verificación normativa
- [ ] Descargar e incorporar a `/sources` los textos íntegros oficiales.
- [ ] Resolver y fijar la numeración del bloque de derechos (arts. 12-16) contra IMPO.
- [ ] Confirmar Resoluciones URCDP 63/2023 y 70/2023 y listado de países con nivel adecuado.
- [ ] Confirmar umbral de "grandes volúmenes" para DPO.

## v0.3 — Detección
- [ ] Validador de cédula de identidad uruguaya (dígito verificador).
- [ ] Mejorar heurísticas por framework (Django, Rails, Laravel, Next.js, Spring).
- [ ] Detección de regiones cloud para inferir transferencias.

## v0.4 — Empaquetado y CI
- [ ] Script de empaquetado `.skill`.
- [ ] Tests/ejemplos de regresión sobre repos sintéticos.
- [ ] GitHub Action que valide que cada afirmación normativa tenga cita.

## v0.5 — Cobertura ampliada
- [ ] Pack de sector salud (Ley 18.331 art. 19 + normativa sanitaria).
- [ ] Pack laboral (tratamiento de datos de empleados).
- [ ] Guía de inscripción de bases ante la URCDP paso a paso.

## Futuro
- [ ] Modo "diff": re-auditar y mostrar cambios entre ejecuciones.
- [ ] Exportar `state.json` a tablero/markdown navegable.
