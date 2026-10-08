# Esquema del Memory Store del despacho

El Memory Store se monta en `/mnt/memory/<nombre-store>/` dentro del
container del coordinador. Cada cita ya verificada en un asunto previo
se almacena como un fichero markdown con frontmatter.

## Estructura jerárquica (paths dentro del store)

```
jurisprudencia/
├── sts/
│   ├── 2024/
│   │   └── STS-1234-2024-Sala1.md
│   └── 2025/
├── stc/
├── stjue/
├── san/
├── stsj/<ccaa>/
└── sap/<provincia>/

normativa/
├── estatal/
│   ├── leyes/
│   ├── leyes-organicas/
│   ├── reales-decretos/
│   └── reglamentos/
└── europea/
    ├── reglamentos/
    └── directivas/

doctrina/
└── <autor-apellidos>/
```

## Contenido por entrada (frontmatter + cuerpo)

```yaml
---
tipo: STS                          # categoría
sala: Sala Primera                 # si aplica
ponente: "Apellidos, Nombre"
fecha: 2024-03-15
numero_recurso: 1234/2023
url_canonica: https://www.poderjudicial.es/...
verificado_por: <usuario>
verificado_fecha: 2026-04-22T10:30:00Z
ultima_revalidacion: 2026-05-08T14:00:00Z
asuntos_donde_aparece: [ASUNTO-2024-087, ASUNTO-2024-119]
holding_canonico: "..."            # resumen sustantivo
citas_literales_verificadas:
  - texto: "..."
    fj: "Fundamento Jurídico 3º"
  - texto: "..."
    fj: "Fundamento Jurídico 5º"
matizada_por: []                   # jurisprudencia posterior
superada_por: null
alertas: []
---

# Análisis sustantivo

[Texto libre del despacho sobre el holding, aplicabilidad histórica,
matices observados]
```

## Política

- Toda cita marcada `verificada` en un informe se incorpora.
- Toda entrada con más de 180 días sin revalidación: marca para revisión manual.
- Si jurisprudencia posterior matiza o supera: actualizar campos `matizada_por` o `superada_por`.
- Acceso: lectura libre por todos los agentes del workspace; escritura solo desde el flujo de verificación validado o desde edición humana explícita.

## Cómo consultarlo (desde el coordinador, en el container)

El store está montado como filesystem. El coordinador lo recorre con las
herramientas estándar:

```
glob /mnt/memory/jurisprudencia-verificada-despacho/jurisprudencia/sts/2024/*.md
read /mnt/memory/jurisprudencia-verificada-despacho/jurisprudencia/sts/2024/STS-1234-2024-Sala1.md
```

Para escribir una nueva entrada tras una verificación positiva:

```
write /mnt/memory/jurisprudencia-verificada-despacho/jurisprudencia/sts/2024/STS-XXXX-YYYY-SalaN.md
```

Cada escritura genera una `memory_version` inmutable; el audit trail es automático.
