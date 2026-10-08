# Diario — 2026-08-23: Resolución de avisos sobre copias locales (TAREA-092)

## Qué se ha hecho

- **Diagnóstico**: las 3 copias locales avisadas por el validador
  (NOR-017, NOR-018 y NOR-050) no contenían otra norma, sino solo la caché de
  navegación de la página del BOC: menús, «Mapa web» y párrafos `<p>`, sin una
  sola línea normativa. Las normas que declaraban ya habían sido retiradas como
  catalogación errónea (`DEC-0011`; `PREG-010`, `PREG-011`, `PREG-012`), y las
  normas reales que NOR-018 confundía (`NOR-076`, `NOR-077`) cuentan con ficha
  y copia local propia desde `PREG-011`.
- **Eliminación** de los tres `.txt` y de sus bloques `texto_plano_local` en
  `06_indices/textos-oficiales.yaml` (`estado_acceso` pasa a
  `enlace-oficial`, con `observaciones` que documentan la retirada). Las
  fichas NOR-017/018/050 se conservan marcadas (R9/R10); git conserva el
  historial de las copias.
- **Alineación de vigencia** en `06_indices/textos-oficiales.yaml`:
  NOR-017/018/050 pasan al estado de su ficha («No normativa — catalogación
  errónea…») y NOR-025 al rectificado por `PREG-012` («Vigente», tras quedar
  sin efecto la supuesta superación).
- **Validador**: nueva sección `TEXTOS-OFICIALES` que comprueba que cada
  `ruta_local` del índice resuelve a un fichero existente y que cada
  `estado_vigencia` coincide con el de la ficha normativa correspondiente.
  Verificado con prueba negativa en proceso (detecta ruta rota y vigencia
  divergente).

## IDs consumidos

- `TAREA-092`. No se crean otras entidades nuevas.

## Estado final

`python3 11_calidad/validar_corpus.py`: **0 errores · 0 avisos** — primera vez
que el corpus queda sin avisos desde que existen las comprobaciones de
correspondencia de copias.

## Publicación

Trabajado en la rama `feat/tarea-092-resolucion-avisos` e integrado vía pull
request.
