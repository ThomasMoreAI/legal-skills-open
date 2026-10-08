# Diario — 2026-08-05: cierre de la deuda del monitor

## Punto de partida

`TAREA-086` quedaba con 35 documentos identificados y sin fichar, y con una decisión pendiente
sobre nueve PDF que la Consejería publica fuera del BOC.

## Lo catalogado

Veinticuatro normas más, con fuente, copia local del PDF firmado y doce relaciones nuevas.

**El corpus cubre por primera vez los cinco grados del sistema de FP.** Faltaban los **Grados C**
(Certificados Profesionales) y **B** (Certificados de Competencia): los cubren las siete
resoluciones de 25 de febrero de 2026, que se reparten las familias profesionales.

Faltaban también dos ofertas completas: la **Formación Profesional Adaptada** y la **formación
dual**. Y la cadena estatal que sostiene todo lo anterior, empezando por el RD 658/2024, que
modifica el RD 659/2023 catalogado esta misma jornada. Sin él, esa ficha habría quedado mostrando
una redacción que ya no es la vigente.

Hay un tipo de hallazgo que se repite y conviene nombrar: **fichas que declaraban en su texto una
modificación cuyo destino no existía en el corpus**. `NOR-074` decía sustituir anexos de dos
resoluciones ausentes; ahora son `NOR-094` y `NOR-096`, y `REL-081` y `REL-082` cierran la
afirmación. Es exactamente el mismo patrón que apareció ayer con `NOR-075`.

## La decisión sobre los documentos del portal

`DEC-0012` fija el criterio: **no decide el canal de publicación, sino el contenido**. Se cataloga
lo que es resolución con parte dispositiva y alcance general; se rechaza el acto singular, el
extracto de una norma ya catalogada y el documento de una etapa normativa sustituida.

Aplicado: cuatro se catalogan y cinco no. Los tres de «Estructura modular y horaria» resultaron
ser los anexos V, VI y VII de `NOR-081` —llevan impreso el pie `boc-a-2024-226-3747`—, así que se
registran como accesos directos en esa ficha en lugar de duplicarse como normas.

La tentación era catalogar sólo lo del boletín, que es lo que tiene publicidad oficial. Pero buena
parte de lo que un centro aplica a diario —admisión a cursos de especialización, autorización de
la modalidad bilingüe, coordinación de familias profesionales— vive precisamente en esos
documentos. Un corpus que los ignore describe el marco jurídico, no la realidad de los centros. El
riesgo de confundir su rango se resuelve marcándolo, y las cuatro fichas lo llevan visible.

## Dos arreglos en la herramienta

**El identificador de las URL antiguas.** Quedaba una disposición señalada como pendiente que sí
estaba catalogada: `NOR-100`. Su URL en el snapshot usa el esquema antiguo del BOC, donde el
último tramo es la posición dentro del boletín y no el número de disposición, así que no contiene
el identificador. El informe lo resuelve ahora leyéndolo del sumario.

**Las exclusiones razonadas.** `descartados.yaml` recoge lo que no procede catalogar, con motivo
escrito y decisión que lo respalda. Sin eso, el informe repetiría en cada ejecución los mismos
cinco documentos descartados hasta convertirse en ruido que nadie lee, y entonces dejaría de
servir para lo único que importa.

## Estado

El informe de deuda queda en **cero disposiciones sin catalogar**, del BOC y del BOE. Lo que
queda son 25 páginas de portal, que son navegación, y las cinco exclusiones documentadas.

## Deuda que esta tanda deja anotada

Las fichas nuevas citan normas que el corpus todavía no tiene: los Reales Decretos de cada título
de FP, el RD 278/2023 de calendario de implantación, los RD 499/2024 y 500/2024, el Decreto
156/1996 de ordenación de la FP específica canaria y el Decreto 84/2024 del Reglamento Orgánico de
la Consejería.

No se abre tarea por ello. Son referencias de fundamento, no normas que otra ficha declare
modificar, que era el criterio de urgencia que ha guiado estas dos tandas.

## IDs consumidos

`FTE-094` a `FTE-117`, `NOR-087` a `NOR-110`, `REL-075` a `REL-086`, `DEC-0012`.
