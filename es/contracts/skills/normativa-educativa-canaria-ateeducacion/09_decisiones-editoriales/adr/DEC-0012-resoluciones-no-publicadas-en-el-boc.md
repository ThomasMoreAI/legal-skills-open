---
id: DEC-0012
titulo: "Qué se hace con las resoluciones que la Consejería publica sólo en su portal"
estado: "Aceptada"
fecha: 2026-08-05
relacionadas: [NOR-071, NOR-081, NOR-107, NOR-108, NOR-109, NOR-110, TAREA-086, DEC-0010]
---

# DEC-0012 — Resoluciones publicadas fuera del BOC

## Contexto

El monitor del portal detecta, junto a las disposiciones del BOC y del BOE, **PDF que la
Consejería publica directamente en su web**: resoluciones numeradas de una dirección general,
instrucciones de organización, apéndices de resoluciones anteriores y extractos de anexos.

`TAREA-086` dejó nueve de esos documentos sin catalogar precisamente porque no estaba claro qué
son. La regla R8 prohíbe mezclar normas con orientaciones no normativas, y meterlos todos en
`02_normativa/` sin criterio habría sido incumplirla.

El corpus ya tenía un precedente sin doctrina: `NOR-071`, la Resolución conjunta n.º 24/2024
sobre el primer ciclo de Infantil, se catalogó desde un PDF del portal.

## Decisión

**No es el canal de publicación lo que decide, sino el contenido.** Un documento del portal se
cataloga como `NOR` cuando reúne las dos condiciones:

1. **Es una resolución dictada por un órgano con competencia**, con parte dispositiva y efectos
   sobre los centros o sobre el alumnado. No basta con que informe u oriente.
2. **Tiene alcance general**: se dirige a una categoría de destinatarios, no a personas o centros
   nombrados uno a uno.

Y se rechaza en tres casos:

| Caso | Qué se hace |
| --- | --- |
| **Acto administrativo singular** —nombramientos, designación de centros concretos, adjudicaciones— | No se cataloga. Se agota al ejecutarse y no forma parte del ordenamiento |
| **Extracto o copia parcial de una norma ya catalogada** | No se cataloga como norma nueva. Se registra como `url_anexo` de la ficha que corresponde |
| **Documento de una etapa normativa ya sustituida**, sin efecto sobre el marco vigente | No se cataloga; si alguien lo necesita, se anota en la ficha de la norma que lo sustituyó |

Cuando sí se cataloga, la ficha lo declara expresamente: el campo `texto_oficial.url_html` apunta
a la página del portal, `url_pdf` al documento, y la copia local advierte en su nota de extracción
que **no es una disposición publicada en el BOC**. Quien la cite debe saberlo.

## Por qué no se descartan sin más

La tentación es catalogar sólo lo que sale en el boletín, que es lo que tiene publicidad oficial.
Pero buena parte de lo que un centro canario aplica a diario —admisión a cursos de
especialización, autorización de la modalidad bilingüe, coordinación de familias profesionales—
vive exactamente en estos documentos. Un corpus que los ignore describe el marco jurídico y no la
realidad de los centros.

El riesgo de incluirlos es confundir su rango, y eso se resuelve marcándolo, no excluyéndolos.

## Aplicación a los nueve documentos de TAREA-086

**Se catalogan cuatro:**

- `NOR-107` — Resolución 492/2023, procedimiento de selección de la coordinación de familias
  profesionales, FOL e Idiomas.
- `NOR-108` — Resolución de 22 de septiembre de 2014, convalidación de los módulos de Lengua
  Extranjera (Inglés) del desarrollo curricular canario.
- `NOR-109` — Resolución 305/2025, admisión y desarrollo de los cursos de especialización de FP.
- `NOR-110` — Resolución 318/2025, autorización de la modalidad bilingüe en ciclos formativos.

**No se catalogan cinco, por motivo expreso:**

| Documento | Motivo |
| --- | --- |
| Resolución 722, designación de centros coordinadores de familias profesionales 2023/2024 | Acto singular: nombra centros y profesorado concretos para un curso ya terminado |
| `APENDICES_RESOLUCION_INSTRUCCIONES_LOE.pdf` | Apéndices de una resolución de 2012 para las enseñanzas de FP reguladas por la LOE, sustituidas por el sistema de la LOFP 3/2022 |
| `Estructura-modular-y-horaria-Grados-D-nivel-1.pdf` | Es el **Anexo V** de `BOC-A-2024-226-3747`, ya catalogado como `NOR-081` |
| `Estructura-modular-y-horaria-Grados-D-nivel-2-y-3.pdf` | Es el **Anexo VI** de la misma resolución |
| `Estructura-modular-y-horaria-Grados-E.pdf` | Es el **Anexo VII** de la misma resolución |

Los tres últimos se comprobaron abriendo el PDF: llevan impreso el pie `boc-a-2024-226-3747` y el
rótulo del anexo. Son extractos de comodidad que la Consejería publica para que un centro no tenga
que descargar las 220 páginas del boletín. Se registran en `NOR-081` como accesos directos a sus
anexos.

## Consecuencia para el monitor

`scan_normativa.py --pendientes` seguirá listando los cinco descartados mientras estén en el
snapshot, porque no tienen ficha. Es correcto: el informe dice qué no está catalogado, no qué
debería estarlo. La justificación de por qué no procede vive aquí y en `TAREA-086`.
