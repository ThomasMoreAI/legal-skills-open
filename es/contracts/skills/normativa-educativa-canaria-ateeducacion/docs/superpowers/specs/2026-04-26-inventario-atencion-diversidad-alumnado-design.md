# Diseño de Especificación: Inventario de Atención a la Diversidad y Alumnado

- **Fecha:** 2026-04-26
- **Tarea relacionada:** TAREA-016
- **Estado:** Pendiente de revisión del usuario

## 1. Objetivo
Sistematizar la normativa canaria vigente en materia de inclusión educativa, atención a la diversidad (NEAE, NEE, altas capacidades) y procesos de admisión/escolarización del alumnado. Se incluirán las resoluciones de instrucciones de curso para los periodos 24/25, 25/26 y 26/27.

## 2. Alcance
- Catalogación de 2 Decretos base (Diversidad y Admisión).
- Catalogación de 3 Órdenes de desarrollo (NEAE, Diversidad Básica, Admisión).
- Catalogación de 4 Resoluciones de instrucciones anuales (3 de Diversidad, 1 de Admisión reciente).
- Actualización de índices de fuentes, normativa y relaciones.

## 3. Arquitectura de Información

### 3.1. Fuentes (01_fuentes/)
Se crearán fichas de fuente para los boletines y portales identificados:
- **FTE-027:** Decreto 25/2018 (Diversidad) - BOC 2018/046
- **FTE-028:** Decreto 9/2022 (Admisión) - BOC 2022/020
- **FTE-029:** Orden 7 de junio de 2007 (Diversidad Básica) - BOC 2007/124
- **FTE-030:** Orden 13 de diciembre de 2010 (NEAE) - BOC 2010/250
- **FTE-031:** Orden 3 de marzo de 2022 (Admisión Procedimiento) - BOC 2022/049
- **FTE-032:** Resolución 261/2024 (Instrucciones Diversidad 24/25)
- **FTE-033:** Resolución 327/2025 (Instrucciones Diversidad 25/26)
- **FTE-034:** Resolución 584/2026 (Instrucciones Diversidad 26/27)
- **FTE-035:** Resolución 5 de febrero de 2026 (Admisión 26/27) - BOC 2026/031

### 3.2. Fichas Normativas (02_normativa/)
Se implementará el **Enfoque Individual** para las resoluciones:
- **NOR-024:** Decreto 25/2018
- **NOR-025:** Decreto 9/2022
- **NOR-026:** Orden 7 de junio de 2007
- **NOR-027:** Orden 13 de diciembre de 2010
- **NOR-028:** Orden 3 de marzo de 2022
- **NOR-029:** Res. Instrucciones Diversidad 24/25
- **NOR-030:** Res. Instrucciones Diversidad 25/26
- **NOR-031:** Res. Instrucciones Diversidad 26/27 (Vigente)
- **NOR-032:** Res. Admisión 26/27 (Vigente)

## 4. Relaciones (05_relaciones/)
Se definirán los siguientes vínculos:
- `NOR-024` (Decreto) -> Desarrolla -> `NOR-004` (Ley Canaria)
- `NOR-026`, `NOR-027` -> Desarrollan -> `NOR-024`
- `NOR-029`, `NOR-030`, `NOR-031` -> Instrucciones de -> `NOR-024` y `NOR-026`
- `NOR-028` -> Desarrolla -> `NOR-025`
- `NOR-032` -> Calendario de -> `NOR-025`

## 5. Validación
- Cada ficha debe cumplir con el esquema YAML correspondiente.
- Se verificará que las resoluciones 26/27 se marquen como "Vigentes" y las anteriores como "Históricas/Superadas" si procede (aunque se mantengan para análisis evolutivo).
- El índice `06_indices/normativa.yaml` debe reflejar todas las nuevas entradas.
