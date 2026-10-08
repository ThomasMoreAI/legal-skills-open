# Referencia técnica · Extracción y verificación de citas

## Patrones de búsqueda (regex)

### Normativas

#### Leyes

- `Ley N°\s*\d+(?:\.\d+)?` — "Ley N° 27043" o "Ley N° 23.654"
- `Ley\s+\d+` — "Ley 27043" (sin punto/N°)
- `\b(Ley|DECRETO|Resolución|Ordenanza|Disposición)\s+N°?\s*(\d+(?:[/-]\d+)?(?:/\d{4})?)`

#### Decretos

- `Decreto\s+N°\s*\d+(?:[/-]\d+)?(?:/\d{4})?` — "Decreto N° 1234/2023"
- `D\.?\s*N°\s*\d+` — "D.N. 1234"
- `Decreto-Ley\s+N°\s*\d+` — "Decreto-Ley N° 20744"

#### Resoluciones (administrativas)

- `Resolución\s+N°\s*\d+(?:[/-]\d+)?(?:/\d{4})?` — "Resolución N° 456/2023"
- `Res\.?\s+N°\s*\d+` — "Res. N° 456"

#### Artículos (referencias puras)

- `Art\.\s*\d+(?:,?\s*(?:inc|párr\.?|apartado|literal|punto)\s+[a-z\d)]+)?` — "Art. 15", "Art. 15, inc. a)"
- `Artículo\s+\d+` — "Artículo 15"

### Jurisprudenciales

#### Fallos CSJN/Corte Suprema

- `Fallos\s+(?:T\.)?\s*\d+\s*:\s*\d+` — "Fallos T.340:1313" o "Fallos 340:1313"
- `CSJN\s*,?\s*Fallos.*?\d+:\d+` — "CSJN, Fallos 340:1313"

#### Cámara Nacional / Provincial

- `Cámara\s+(?:Nacional|Provincial)\s+(?:de|del?)\s+[\w\s]+(?:,\s*\d+/\d+)?` — "Cámara Nacional de Apelaciones en lo Civil, 123/2023"
- `C\.?A\.?\s*[\w]*\s*,?\s*\d+/\d+` — "C.A. Civil, 456/2022"

#### Juzgados

- `Juzgado\s+(?:de|en)\s+[\w\s]+(?:,\s*\d+/\d+)?` — "Juzgado de Familia, 789/2021"

#### Tribunal de referencia incompleta (RIESGO)

- `[Tt]ribunal\s+\d+` — "Tribunal 15" (INCOMPLETO, REQUIERE VERIFICACIÓN)

### Doctrina (opcional)

- `(?:Prof|Dr|Dr\.|Dra|Doctora|Profesor|Autora?)\s+[A-Z][a-z]+\s+[A-Z][a-z]+(?:\s*\(.*?\d{4}\))?` — "Prof. García López (2015)"
- `[\w\s]+\s*,\s*[\w\s]*\s*[\[\(]20\d{2}[\]\)]` — "Fernández Arroyo [2018]"

## Estructura de extracción

```python
def extraer_citas(texto_escrito: str) -> List[Cita]:
    """
    Extrae todas las citas de un escrito.

    Args:
        texto_escrito: El contenido del escrito como string

    Returns:
        Lista de objetos Cita con:
        - texto: la cita tal como aparece en el escrito
        - tipo: 'normativa' | 'jurisprudencia' | 'doctrina' | 'indeterminada'
        - normalizacion: forma estándar para búsqueda en tabla
        - linea: línea del escrito donde aparece
        - seccion: sección del escrito (si está numerada)
        - marca_pendiente: bool (True si lleva 🔲)
    """
    citas = []
    lineas = texto_escrito.split('\n')

    for i, linea in enumerate(lineas, 1):
        # Extraer normativas
        for match in re.finditer(REGEX_NORMATIVAS, linea):
            cita = Cita(
                texto=match.group(),
                tipo='normativa',
                normalizacion=normalizar_normativa(match.group()),
                linea=i,
                seccion=extraer_seccion_parrafo(i, texto_escrito),
                marca_pendiente='🔲' in linea
            )
            citas.append(cita)

        # Extraer jurisprudenciales
        for match in re.finditer(REGEX_JURISPRUDENCIA, linea):
            cita = Cita(
                texto=match.group(),
                tipo='jurisprudencia',
                normalizacion=normalizar_jurisprudencia(match.group()),
                linea=i,
                seccion=extraer_seccion_parrafo(i, texto_escrito),
                marca_pendiente='🔲' in linea
            )
            citas.append(cita)

    return citas
```

## Normalización de citas

Para cruzar contra la tabla de fuentes, normalizar:

### Normativas

- "Ley N° 27043" → "Ley 27043"
- "Ley 27.043" → "Ley 27043"
- "Art. 15, Ley N° 27043" → ["Art. 15", "Ley 27043"]
- "Artículo 15" → "Art. 15"

### Jurisprudenciales

- "Fallos T.340:1313" → "Fallos 340:1313"
- "CSJN, Fallos T.340:1313" → "CSJN, Fallos 340:1313"
- "C.A. Civil, 123/2023" → normalizar a "Cámara Nacional de Apelaciones en lo Civil, 123/2023"

## Búsqueda en tabla de fuentes

```python
def verificar_cita(cita: Cita, tabla_fuentes: List[Dict]) -> VerificacionResult:
    """
    Verifica si una cita existe en la tabla de fuentes.

    Returns:
        VerificacionResult(
            encontrada: bool,
            fila_tabla: Dict | None,  # Si encontrada
            uuid: str | None,
            url: str | None,
            estatus: '✅' | '🔴' | '🔲'  # ✅=verificada, 🔴=bloqueante, 🔲=pendiente
        )
    """
    normalizacion = cita.normalizacion

    # Búsqueda 1: exacta
    for fila in tabla_fuentes:
        if normalizar(fila['Norma/Fallo']) == normalizacion:
            return VerificacionResult(
                encontrada=True,
                fila_tabla=fila,
                estatus='✅' if not cita.marca_pendiente else '🔲'
            )

    # Búsqueda 2: parcial (p.ej., "Art. 15" dentro de "Ley 27043, Art. 15")
    for fila in tabla_fuentes:
        if normalizacion in normalizar(fila['Norma/Fallo']):
            # Confirmar que es la misma norma (mismo artículo, misma ley)
            return VerificacionResult(
                encontrada=True,
                fila_tabla=fila,
                estatus='✅'
            )

    # No encontrada
    if cita.marca_pendiente:
        return VerificacionResult(
            encontrada=False,
            estatus='🔲'  # Marcada deliberadamente como pendiente
        )
    else:
        return VerificacionResult(
            encontrada=False,
            estatus='🔴'  # BLOQUEANTE: cita sin verificación y sin marca
        )
```

## Flujo de auditoría (pseudocódigo)

```python
def auditar_escrito(
    ruta_escrito: str,
    ruta_tabla_fuentes: str
) -> ReporteAuditoria:

    # Paso 1: Leer
    escrito = leer_archivo(ruta_escrito)
    tabla_fuentes = parsear_tabla_fuentes(ruta_tabla_fuentes)

    # Paso 2: Extraer
    citas = extraer_citas(escrito)

    # Paso 4: Cruce
    resultados = []
    for i, cita in enumerate(citas, 1):
        verificacion = verificar_cita(cita, tabla_fuentes)
        resultados.append({
            'numero': i,
            'cita': cita.texto,
            'tipo': cita.tipo,
            'linea': cita.linea,
            'seccion': cita.seccion,
            'estatus': verificacion.estatus,
            'uuid': verificacion.uuid,
            'url': verificacion.url
        })

    # Paso 5-6: Clasificar
    bloqueantes = [r for r in resultados if r['estatus'] == '🔴']
    pendientes = [r for r in resultados if r['estatus'] == '🔲']
    verificadas = [r for r in resultados if r['estatus'] == '✅']

    # Paso 7: Generar reporte
    return ReporteAuditoria(
        escrito_auditado=ruta_escrito,
        timestamp=datetime.now(),
        resumen={
            'total': len(citas),
            'verificadas': len(verificadas),
            'bloqueantes': len(bloqueantes),
            'pendientes': len(pendientes)
        },
        tabla_completa=resultados,
        bloqueantes=bloqueantes,
        pendientes=pendientes,
        checksum_ok=(len(verificadas) + len(bloqueantes) + len(pendientes)) == len(citas)
    )
```

## Casos especiales y trampas

1. **Artículos huérfanos:** "Art. 15" sin indicación de a qué norma refiere.
   - ACCIÓN: buscar la norma anterior citada en el párrafo; si no existe, 🔴 bloqueante.

2. **Fallos parciales:** "Fallos 340" sin el segundo número.
   - ACCIÓN: 🔴 bloqueante; requiere "Fallos 340:1313" completo.

3. **Referencias genéricas:** "jurisprudencia pacífica", "consenso de la doctrina".
   - ACCIÓN: si está en escrito sin 🔲, es 🔴 bloqueante; pedir especificación.

4. **Citas modificadas:** "la Ley N° 27043, modificada por Decreto N° 456/2023".
   - ACCIÓN: ambas normas deben estar en tabla; verificar ambas.

5. **Citas en notas al pie:** mismo tratamiento que en el cuerpo del texto.

6. **URLs/UUIDs incompletos en tabla:** si la tabla tiene UUID pero URL está vacía.
   - ACCIÓN: 🟡 mejorable; completar en tabla (o dejar 🔲 si se va a verificar luego).

## Validación del reporte

Checksum: `verificadas + bloqueantes + pendientes = total_citas`

Si no coincide:

1. Rehacer extracción (paso 2) — algunos párrafos pueden tener múltiples citas.
2. Verificar que no haya citas duplicadas (mismo UUID en múltiples filas).
3. Confirmar que la tabla de fuentes está completa (sin cortes o mergings).
