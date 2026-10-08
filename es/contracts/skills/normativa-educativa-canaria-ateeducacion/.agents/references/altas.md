# Altas del corpus

Ábrelo cuando vayas a crear una ficha, un chunk, una relación o una entrada de índice. Una consulta que no crea entidades no lo necesita.

## Ficha de fuente

1. Asignar ID `FTE-NNN` correlativo.
2. Completar autoridad, URL oficial, tipo de fuente y fecha de consulta.
3. Describir qué contiene y su relevancia.
4. Enlazar normas o currículos relacionados.
5. Registrar la fuente en `06_indices/fuentes.yaml`.

El skill es `catalogacion-fuentes`.

## Ficha normativa

1. Asignar ID `NOR-NNN` correlativo.
2. Registrar fuente principal, ámbito, tipo de norma y estado de vigencia.
3. Redactar objeto, ámbito, estructura, relaciones e impacto en Canarias.
4. Añadir resumen breve, dudas abiertas y fuentes.
5. Actualizar `06_indices/normativa.yaml` y las relaciones.

El skill es `analisis-normativo`.

## Ficha curricular

1. Asignar ID `CUR-NNN` correlativo.
2. Registrar etapa, materia o ámbito, fuente y fecha de consulta.
3. Mantener `estado_extraccion` actualizado.
4. Separar YAML estructurado y Markdown narrativo.
5. Reflejar cualquier duda en `PREG-NNN`.

El skill es `analisis-curricular`.

## Chunks y textos rápidos

1. Crear `CHUNK-NNNNN` breve, con fuente, localización y fechas.
2. No mezclar hechos e interpretación. Si la hay, marcar `[INTERPRETACIÓN]`.
3. Registrar el chunk en `06_indices/chunks.yaml`.
4. Una copia local de texto completo lleva URL oficial, fecha de consulta, fecha de exportación y la advertencia de que no sustituye la fuente oficial.
5. Registrarla en `06_indices/textos-oficiales.yaml`. No usarla como prueba única si la fuente oficial es más reciente.

El skill es `preparacion-corpus-ia`.

## Relaciones

Crea un `REL-NNN` en YAML con tipo, origen, destino, evidencia, fecha y nivel de evidencia. Actualiza `06_indices/relaciones.yaml`. El skill es `relaciones-normativas`.

## Índices y vigencia

Cada entidad nueva entra en su índice en el mismo cambio. Si no se puede confirmar la vigencia en la fuente oficial, el estado es `Pendiente de verificación` y se abre una pregunta. El skill de vigencia es `control-vigencia`.
