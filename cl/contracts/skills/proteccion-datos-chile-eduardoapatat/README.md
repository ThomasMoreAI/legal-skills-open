# Protección de Datos Chile

[![skills.sh](https://skills.sh/b/eduardoapatat/proteccion-datos-chile)](https://skills.sh/eduardoapatat/proteccion-datos-chile)

Agent Skill para diseñar, implementar y revisar sistemas que tratan datos personales con nexo chileno, conforme a la Ley N.º 19.628 y su reforma por la Ley N.º 21.719.

No funciona sólo como revisor al final del proyecto: incorpora privacidad y seguridad desde requisitos, arquitectura y desarrollo, y también ayuda a auditar código, configuración, flujos, proveedores e incidentes con evidencia verificable.

## Cuándo se activa

Se activa por cualquiera de estas rutas:

1. el usuario pide expresamente aplicar o revisar la normativa chilena de protección de datos; o
2. concurren un **nexo con Chile** y un **tratamiento real o previsible de datos personales**.

El nexo puede surgir porque el responsable o encargado está en Chile, el producto se dirige al mercado chileno, ofrece bienes o servicios a personas en Chile, monitorea su comportamiento o queda sujeto al derecho chileno por otra causa relevante.

El tratamiento puede inferirse aunque no se mencione la palabra “privacidad”. Ejemplos: cuentas, RUT, pagos, despacho, soporte, cookies, IP vinculables, logs, imágenes, ubicación, biometría, analítica individual, perfiles, IA o datos laborales.

Una mención aislada de “Chile”, “mercado chileno” o “seguridad” no activa por sí sola el análisis completo. La skill realiza primero un cribado breve y sólo continúa si confirma ambos elementos.

- **Revisión base:** cualquier dato personal.
- **Revisión reforzada:** datos sensibles, salud, biometría, niños, niñas o adolescentes, geolocalización, solvencia, infracciones, vigilancia, perfiles, decisiones automatizadas, tratamiento masivo, IA, transferencias o incidentes.
- **Fuera de alcance:** datos irreversiblemente anónimos, sistemas sin datos de personas naturales ni nexo chileno, actividades estrictamente personales y ciberseguridad sin impacto en datos personales.

> [!NOTE]
> Un RUT asociado a una persona natural y una IP vinculable son normalmente datos personales, pero no son automáticamente datos sensibles. La clasificación depende del texto legal y del contexto.

## Qué hace

### Durante la construcción

- inventaría titulares, datos, finalidades y roles;
- cuestiona datos innecesarios y valores predeterminados invasivos;
- define fuente de licitud y evidencia por finalidad;
- diseña controles de acceso, aislamiento, trazabilidad, retención y eliminación;
- incorpora derechos de titulares en el modelo y las APIs;
- revisa proveedores, nube, países y subencargados;
- evalúa logs, telemetría, pruebas, respaldos e IA;
- determina si corresponde una evaluación de impacto;
- genera requisitos y pruebas de aceptación antes de producción.

### Durante una auditoría

- contrasta políticas con código, configuración y comportamiento efectivo;
- sigue los datos desde su recolección hasta su eliminación;
- detecta exposiciones, accesos indebidos y controles faltantes;
- separa vulnerabilidad técnica, incumplimiento jurídico e incidente;
- vincula cada hallazgo con evidencia, artículo, prioridad y remediación;
- marca como **no verificado** lo que no puede probarse.

### Ante un incidente

- prioriza contención y preservación de evidencia;
- delimita datos, personas, sistemas, terceros y países afectados;
- diferencia acceso posible, acceso confirmado, extracción, alteración, pérdida y destrucción;
- determina el régimen vigente en la fecha del hecho;
- analiza comunicaciones a autoridad o titulares sin importar plazos extranjeros automáticamente;
- relaciona la conducta con posibles infracciones sólo cuando hay evidencia suficiente.

La skill no ejecuta pruebas intrusivas ni explota vulnerabilidades sin autorización expresa.

## Resultado de una revisión

Cada hallazgo incluye:

| Campo | Contenido |
| --- | --- |
| Evidencia | Artefacto, componente o comportamiento observado. |
| Estado | Cumple, parcial, no cumple, no verificado o no aplica. |
| Régimen | Vigente, futuro confirmado, proyecto o buena práctica. |
| Norma | Ley, artículo y elemento aplicable. |
| Riesgo | Escenario, probabilidad, impacto y prioridad técnica. |
| Encaje jurídico | Confirmado, probable, posible o no determinado. |
| Corrección | Cambio concreto y responsable. |
| Prueba | Criterio de aceptación reproducible. |

La prioridad técnica no se equipara automáticamente con la categoría legal de una infracción.

## Estado normativo

La skill obliga a verificar fuentes oficiales antes de concluir y diferencia una fecha legal de una propuesta legislativa.

| Fecha | Estado verificado al 16-09-2026 |
| --- | --- |
| **1 de diciembre de 2026** | Fecha jurídicamente publicada para la entrada en vigencia de las modificaciones introducidas por la Ley N.º 21.719. |
| **1 de diciembre de 2027** | Fecha propuesta por el Boletín N.º 18.623-07; todavía no constituye derecho vigente. |

Al 16 de septiembre de 2026, el Boletín N.º 18.623-07 está en primer trámite constitucional en el Senado y tiene suma urgencia. El proyecto también contempla ajustes institucionales y transitorios, por lo que debe verificarse completo si avanza.

El Decreto N.º 662, publicado el 9 de septiembre de 2026, reglamenta los modelos voluntarios de prevención de infracciones previstos por la reforma. Su publicación no adelanta por sí sola la vigencia de todas las obligaciones reformadas.

Fuentes principales:

- [Ley N.º 19.628 vigente en LeyChile](https://www.bcn.cl/leychile/navegar?idNorma=141599)
- [Ley N.º 21.719 en el Diario Oficial](https://www.diariooficial.interior.gob.cl/publicaciones/2024/12/13/44023/01/2583630.pdf)
- [Ley N.º 21.719 consolidada en LeyChile](https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272)
- [Decreto N.º 662 sobre modelos de prevención](https://www.bcn.cl/leychile/navegar?idNorma=1227971)
- [Boletín N.º 18.623-07 en el Senado](https://portallegislativo.senado.cl/detalle-proyectos-ley/19307)
- [Texto del proyecto de modificación](https://www.camara.cl/verDoc.aspx?prmID=18854&prmTIPO=INICIATIVA)

## Instalación

```bash
npx skills add eduardoapatat/proteccion-datos-chile
```

El instalador permite seleccionar los agentes compatibles en los que se habilitará la skill.

## Ejemplos

### Construir un sistema desde cero

```text
Diseña el registro y la arquitectura de datos para un marketplace dirigido a Chile que usa RUT, dirección de despacho, pagos y analítica. Define controles y pruebas de aceptación antes de producción.
```

### Auditar una implementación

```text
Revisa este repositorio y su configuración de nube. Identifica dónde se procesan datos personales de usuarios chilenos, comprueba los controles y entrega hallazgos con evidencia y artículos aplicables.
```

### Biometría laboral

```text
Analiza y diseña de forma segura un control de asistencia con reconocimiento facial para trabajadores en Chile.
```

### Incidente

```text
Un bucket quedó accesible y contenía RUT, contratos y direcciones. Ayúdame a contener, preservar evidencia y determinar obligaciones conforme al régimen vigente en la fecha del incidente.
```

### SaaS e inteligencia artificial

```text
Evalúa una plataforma SaaS que procesa conversaciones de clientes chilenos en Estados Unidos y quiere reutilizarlas para mejorar un modelo de IA.
```

## Estructura

```text
proteccion-datos-chile/
├── SKILL.md
├── README.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    ├── activacion-en-sistemas.md
    ├── fuentes-oficiales.md
    ├── incidentes-y-sanciones.md
    ├── metodo-y-salidas.md
    ├── regimen-y-puntos-clave.md
    └── revision-de-sistemas.md
```

- `SKILL.md`: activación, modos, vigencia, flujo y reglas de evidencia.
- `activacion-en-sistemas.md`: detonante preciso, casos límite y ciclo de vida.
- `revision-de-sistemas.md`: método técnico-jurídico de construcción y auditoría.
- `incidentes-y-sanciones.md`: brechas, comunicaciones, infracciones y consecuencias.
- `regimen-y-puntos-clave.md`: mapa por artículos del régimen actual y reformado.
- `fuentes-oficiales.md`: jerarquía, enlaces, citas y control de actualidad.
- `metodo-y-salidas.md`: plantillas de entregables y estados de hallazgo.
- `agents/openai.yaml`: metadatos opcionales para interfaces compatibles de OpenAI.

## Por qué el repositorio no copia la ley completa

El repositorio mantiene un mapa estructurado y enlaces oficiales, no una copia integral como fuente principal. La Ley N.º 21.719 modifica la Ley N.º 19.628, ha recibido cambios posteriores y debe leerse en su versión consolidada por fecha. Una copia local puede quedar obsoleta y confundirse con derecho vigente.

Para uso sin internet puede conservarse una instantánea oficial fechada y marcada como histórica, pero la skill nunca debe presentarla como actual sin verificación.

## Alcance y limitaciones

La skill entrega análisis informativo, requisitos de diseño y apoyo para revisar evidencia. No sustituye la asesoría de un abogado habilitado en Chile, una auditoría integral de ciberseguridad ni una decisión de la autoridad.

> [!WARNING]
> Esta skill no certifica ni garantiza el cumplimiento de la Ley N.º 19.628, la Ley N.º 21.719 u otras normas, ni la ausencia de vulnerabilidades. Sus conclusiones dependen del alcance y de la evidencia examinada y deben contrastarse con la implementación efectiva —código, configuración, infraestructura, flujos, proveedores y operación—. Antes de producción, y especialmente ante datos sensibles, alto riesgo o un incidente, se recomienda revisión independiente jurídica, de privacidad y de seguridad.

## Mantenimiento

Actualiza conjuntamente `README.md`, `SKILL.md` y las referencias cuando:

- cambie el estado del Boletín N.º 18.623-07;
- se publique una modificación legal o reglamento;
- la Agencia dicte instrucciones o decisiones;
- cambie jurisprudencia relevante;
- se incorporen nuevas categorías, finalidades o tecnologías.

No cambies sólo la fecha de verificación: vuelve a comprobar el contenido y los enlaces oficiales.

## Licencia

Distribuida bajo licencia MIT. La licencia cubre el contenido original de la skill, no los textos legales ni documentos oficiales enlazados.
