# CONTRATO DE IMPLEMENTACIÓN DE SISTEMAS DE AUTOMATIZACIÓN CON INTELIGENCIA ARTIFICIAL

En la Ciudad Autónoma de Buenos Aires, a los {{FECHA_LARGA}}, entre:

**{{PROVEEDOR_NOMBRE}}**, CUIT {{PROVEEDOR_CUIT}}, con domicilio en {{PROVEEDOR_DOMICILIO}}, en adelante **"EL PROVEEDOR"**;

y **{{CLIENTE_RAZON_SOCIAL}}**, CUIT {{CLIENTE_CUIT}}, con domicilio en {{CLIENTE_DOMICILIO}}, representada en este acto por {{CLIENTE_FIRMANTE}}, en su carácter de {{CLIENTE_FIRMANTE_CARGO}}, en adelante **"EL CLIENTE"**;

denominadas conjuntamente **"las Partes"**, quienes se reconocen capacidad legal suficiente para contratar y convienen celebrar el presente Contrato de Implementación, sujeto a las siguientes cláusulas.

---

## PRIMERA — DEFINICIONES

**"Sistema"**: la solución de automatización descripta en el Anexo I, en la configuración específica implementada para EL CLIENTE.

**"Componentes Base"**: las plantillas de flujos de trabajo, librerías de instrucciones (prompts), estructuras de integración, metodologías, patrones de arquitectura, scripts genéricos, documentación técnica y demás elementos de titularidad de EL PROVEEDOR, preexistentes al Contrato o desarrollados por éste con carácter general y reutilizable, que se utilizan para construir el Sistema.

**"Implementación Específica"**: la configuración, parametrización, adaptación e integración concreta de los Componentes Base a los sistemas, datos, procesos y necesidades de EL CLIENTE, conforme al Anexo I.

**"Componentes de IA"**: los modelos de lenguaje o de aprendizaje automático que intervienen en el Sistema y los roles que cumplen dentro del flujo, según se detallan en el Anexo I.

**"Plataformas de Terceros"**: los servicios, APIs, modelos, infraestructura y licencias provistos por terceros que el Sistema utiliza (entre otros, los identificados en el Anexo I).

**"Material del Cliente"**: la información, criterios, contenidos, bases de conocimiento, reglas de negocio y definiciones que EL CLIENTE entrega y valida y que se vuelcan en la configuración del Sistema.

**"Aceptación"**: el acto por el cual el Sistema se tiene por entregado conforme a la Cláusula OCTAVA.

---

## SEGUNDA — OBJETO

2.1. EL PROVEEDOR se obliga a diseñar, configurar, integrar, poner en marcha y entregar a EL CLIENTE el Sistema descripto en el Anexo I, que forma parte integrante e inseparable del presente.

2.2. La contratación es de carácter **llave en mano**. El Sistema se implementa íntegramente sobre infraestructura, cuentas y servicios de titularidad de EL CLIENTE. EL PROVEEDOR no retiene alojamiento, operación ni dependencia técnica alguna con posterioridad a la Aceptación, salvo que se contrate por separado un servicio de mantenimiento.

2.3. Producida la Aceptación y abonado el precio total, la relación contractual se agota, sin perjuicio de la garantía de la Cláusula NOVENA y de las cláusulas que expresamente subsisten conforme a la Cláusula VIGÉSIMA TERCERA.

---

## TERCERA — ALCANCE

3.1. **Alcance incluido.** EL PROVEEDOR prestará exclusivamente las tareas y entregables enumerados en el Anexo I.

3.2. **Alcance excluido.** Quedan expresamente fuera del objeto, salvo acuerdo posterior por escrito y presupuesto aparte:

a) el desarrollo de funcionalidades, integraciones, canales o automatizaciones no enumerados en el Anexo I;
b) la creación de contenidos, piezas creativas, campañas publicitarias o material comercial;
c) el costo de las Plataformas de Terceros, licencias, consumos de API, mensajería, publicidad o infraestructura;
d) la migración, depuración, normalización o corrección de datos preexistentes de EL CLIENTE;
e) la capacitación más allá de {{SESIONES_CAPACITACION}} sesión/es de traspaso;
f) la gestión comercial, el seguimiento o el cierre de las oportunidades, consultas o interacciones que el Sistema genere o procese;
g) la operación cotidiana del Sistema una vez entregado;
h) el soporte, mantenimiento, monitoreo o ajuste posterior al período de garantía;
i) {{EXCLUSIONES_ADICIONALES}}

3.3. **Pedidos fuera de alcance.** Toda solicitud no comprendida en el Anexo I se tramitará como encargo adicional, y su ejecución quedará sujeta a la aceptación previa y por escrito de alcance, plazo y precio. Ningún pedido fuera de alcance se entenderá incluido por el hecho de haber sido mencionado en reuniones, mensajes o propuestas comerciales previas.

---

## CUARTA — NATURALEZA DE LA OBLIGACIÓN

4.1. La obligación asumida por EL PROVEEDOR es una **obligación de medios y no de resultado**, en los términos del artículo 1252 del Código Civil y Comercial de la Nación. EL PROVEEDOR se compromete a ejecutar el Sistema con la diligencia profesional exigible y conforme al Anexo I.

4.2. EL PROVEEDOR **no garantiza** volumen alguno de ventas, ingresos, facturación, conversiones, clientes ni resultados comerciales de EL CLIENTE, por depender éstos de factores ajenos a su control, tales como el producto, el precio, el mercado, la capacidad de cierre y la gestión comercial de EL CLIENTE.

4.3. Los únicos indicadores garantizados son los expresamente identificados como tales en el Anexo I, limitados a métricas bajo control operativo de EL PROVEEDOR.

4.4. Las manifestaciones contenidas en propuestas comerciales, materiales de difusión, presentaciones o comunicaciones previas no integran el presente Contrato ni constituyen garantía de resultado, prevaleciendo en todos los casos lo establecido en este instrumento y su Anexo I.

---

## QUINTA — DESEMPEÑO DE LOS COMPONENTES DE IA

5.1. **Acciones determinísticas.** Las acciones automatizadas que no dependen de la interpretación de un modelo de IA (creación o actualización de registros, envío de notificaciones, agendamiento, disparo de flujos, escritura en sistemas de EL CLIENTE) deben ejecutarse conforme a lo previsto en el Anexo I. Su falla reiterada constituye defecto sujeto a la garantía de la Cláusula NOVENA.

5.2. **Umbral de desempeño de los Componentes de IA.** Respecto de los roles de los Componentes de IA que admiten verificación objetiva —clasificación de intención, extracción de datos y decisión del paso siguiente del flujo— las Partes acuerdan un umbral de desempeño esperado de **{{UMBRAL_IA}}%** de respuestas correctas.

5.3. **Medición.** El umbral se mide sobre una muestra representativa acordada entre las Partes, en condiciones normales de operación, durante el período de garantía. Un desempeño igual o superior al umbral constituye cumplimiento pleno. Los desvíos individuales por debajo del umbral no constituyen, por sí solos, defecto ni incumplimiento.

5.4. **Redacción de respuestas.** La calidad estilística, el tono y la formulación de las respuestas generadas por los Componentes de IA no admiten medición objetiva y quedan excluidos del umbral, rigiéndose exclusivamente por lo dispuesto en la Cláusula 5.7.

5.5. **Exclusión por dominio de conocimiento.** El Sistema opera sobre la base del Material del Cliente entregado y validado por EL CLIENTE conforme a la Cláusula 6.4. Las consultas, escenarios o situaciones no contemplados en dicho material, o para los cuales EL CLIENTE no haya provisto criterios, quedan excluidos de la medición del umbral y no constituyen defecto. La ampliación del Material del Cliente se tramitará conforme a la Cláusula 3.3.

5.6. **Exclusión por calidad del input.** Quedan excluidas de la medición del umbral y no constituyen defecto las interacciones originadas en entradas ambiguas, incompletas, ilegibles, contradictorias, redactadas en idioma distinto al previsto, fuera del formato esperado o ajenas al dominio para el que el Sistema fue configurado.

5.7. **Naturaleza de la inteligencia artificial.** EL CLIENTE reconoce y acepta que los Componentes de IA son de naturaleza probabilística y que, aun operando sobre información correcta y entradas adecuadas, pueden producir respuestas inexactas, incompletas, sesgadas o inventadas. Esta circunstancia es inherente al estado del arte de la tecnología, se verifica en la totalidad de los sistemas de inteligencia artificial disponibles en el mercado —cuyos proveedores advierten expresamente que pueden cometer errores y recomiendan verificar la información— y **no constituye por sí sola defecto, falla ni incumplimiento** de EL PROVEEDOR.

5.8. **Supervisión humana.** EL CLIENTE asume la supervisión humana del Sistema y conserva en todo momento la responsabilidad exclusiva sobre las decisiones, acciones y consecuencias derivadas de su operación o adoptadas sobre la base de sus resultados. EL CLIENTE se obliga a verificar los resultados del Sistema antes de utilizarlos en decisiones comerciales, legales, contractuales, financieras o de cumplimiento normativo. Esta obligación subsiste sin límite temporal luego de la Aceptación.

5.9. **Remedio.** Verificado un desempeño inferior al umbral por causa imputable a la configuración realizada por EL PROVEEDOR, el único remedio consistirá en el ajuste de dicha configuración dentro del plazo de la Cláusula NOVENA, sin derecho a devolución, reducción de precio, compensación ni indemnización alguna.

---

## SEXTA — OBLIGACIONES DE EL CLIENTE

6.1. **Accesos.** EL CLIENTE se obliga a proveer, dentro del plazo de {{PLAZO_ACCESOS}} días corridos desde la firma, los accesos, credenciales, permisos, cuentas y habilitaciones detallados en el Anexo II, así como la información y los materiales necesarios para la ejecución.

6.2. **Interlocutor.** EL CLIENTE designa como interlocutor con capacidad de decisión a {{INTERLOCUTOR_NOMBRE}}, correo electrónico {{INTERLOCUTOR_EMAIL}}, cuyas comunicaciones escritas obligan a EL CLIENTE a los efectos de este Contrato.

6.3. **Cuentas y titularidad.** Las cuentas en Plataformas de Terceros son de titularidad exclusiva de EL CLIENTE, quien las contrata directamente, asume sus costos y acepta sus términos y condiciones de uso.

6.4. **Validación del material.** EL CLIENTE se obliga a revisar y validar por escrito el Material del Cliente y los criterios de operación del Sistema con anterioridad a la puesta en marcha. Dicha validación es condición de la Aceptación y constituye la base sobre la que se mide el desempeño conforme a la Cláusula QUINTA.

6.5. **Efecto de la falta de colaboración.** Si EL CLIENTE no proveyera lo necesario o no respondiera dentro de los {{PLAZO_SILENCIO}} días corridos desde el requerimiento escrito de EL PROVEEDOR, los plazos quedarán automáticamente suspendidos y prorrogados por el tiempo del retraso, sin responsabilidad para EL PROVEEDOR. Los importes ya devengados no serán reembolsables.

6.6. **Inactividad prolongada.** Transcurridos {{PLAZO_INACTIVIDAD}} días corridos de inactividad imputable a EL CLIENTE, EL PROVEEDOR podrá dar por entregada la fase correspondiente a todos sus efectos, incluido el de facturación, y emitir la factura por el saldo pendiente.

6.7. **Pagos.** EL CLIENTE se obliga a atender puntualmente los pagos conforme a la Cláusula UNDÉCIMA.

---

## SÉPTIMA — PLAZOS

7.1. El plazo estimado de ejecución es de {{PLAZO_EJECUCION}}, conforme al cronograma del Anexo I.

7.2. Los plazos se computan desde el momento en que EL CLIENTE haya provisto la totalidad de los accesos e información del Anexo II, y no desde la firma del Contrato.

7.3. Los plazos son estimaciones de buena fe y **no revisten carácter esencial**, salvo pacto expreso y por escrito respecto de un hito determinado. Todo retraso imputable a EL CLIENTE o a Plataformas de Terceros prorroga los plazos en igual medida.

---

## OCTAVA — ENTREGA Y ACEPTACIÓN

8.1. Comunicada por escrito la puesta a disposición del Sistema, EL CLIENTE dispondrá de {{PLAZO_ACEPTACION}} días corridos para validarlo o comunicar por escrito los defectos concretos y reproducibles que impidan su funcionamiento conforme al Anexo I.

8.2. Vencido dicho plazo sin observaciones escritas, el Sistema se tendrá por **aceptado tácitamente** a todos sus efectos.

8.3. Solo se admitirán como defecto los apartamientos verificables respecto del Anexo I. La Aceptación **no podrá condicionarse** a mejoras, preferencias estéticas, cambios de criterio, funcionalidades no pactadas ni al grado de satisfacción subjetiva de EL CLIENTE.

8.4. Subsanados los defectos comunicados en término, se reiniciará por única vez el plazo del punto 8.1 respecto exclusivamente de los puntos observados.

8.5. La Aceptación determina la entrega definitiva, el vencimiento del saldo de precio, el inicio del plazo de garantía y el momento a partir del cual opera la cesión prevista en la Cláusula DÉCIMA CUARTA.

---

## NOVENA — GARANTÍA

9.1. EL PROVEEDOR garantiza que el Sistema funcionará sustancialmente conforme al Anexo I durante **{{PLAZO_GARANTIA}}** contados desde la Aceptación.

9.2. Dentro de dicho plazo, EL PROVEEDOR corregirá sin cargo los defectos concretos y reproducibles imputables a su implementación, comunicados por escrito.

9.3. **Exclusiones de la garantía.** La garantía no cubre, y EL PROVEEDOR no responderá por, incidencias derivadas de:

a) modificaciones, ajustes, reconfiguraciones o intervenciones sobre el Sistema realizadas por EL CLIENTE, su personal o terceros no autorizados por EL PROVEEDOR;
b) cambios, actualizaciones, interrupciones, degradaciones, modificaciones de precios, políticas o condiciones de uso de las Plataformas de Terceros;
c) vencimiento, revocación, suspensión o pérdida de credenciales, tokens, licencias, suscripciones o cuentas de EL CLIENTE;
d) modificaciones en los sistemas, estructuras de datos, formatos o procesos de EL CLIENTE;
e) falta de pago de los servicios de terceros necesarios para la operación;
f) uso del Sistema para finalidades distintas de las previstas en el Anexo I;
g) los supuestos de exclusión previstos en las Cláusulas 5.5, 5.6 y 5.7;
h) caso fortuito o fuerza mayor.

9.4. La corrección del defecto constituye el **remedio único y exclusivo** de EL CLIENTE y agota la responsabilidad de EL PROVEEDOR por este concepto.

9.5. Vencido el plazo de garantía cesa toda obligación de corrección, soporte, monitoreo o mantenimiento a cargo de EL PROVEEDOR.

---

## DÉCIMA — SOPORTE POSTERIOR A LA GARANTÍA

10.1. Vencida la garantía, EL PROVEEDOR podrá prestar tareas de soporte, corrección, ajuste o ampliación a solicitud de EL CLIENTE, sujeto a disponibilidad y a conformidad previa por escrito sobre alcance y presupuesto.

10.2. Dichas tareas se facturarán a razón de **{{TARIFA_HORARIA}}** por hora, con un mínimo facturable de {{MINIMO_FACTURABLE}} hora/s por intervención.

10.3. EL PROVEEDOR podrá actualizar la tarifa horaria para trabajos posteriores, comunicándolo por escrito con anterioridad a la aceptación del encargo.

10.4. EL PROVEEDOR no asume obligación alguna de disponibilidad, tiempo de respuesta ni permanencia, salvo que se suscriba un contrato de mantenimiento por separado.

---

## UNDÉCIMA — PRECIO Y FORMA DE PAGO

11.1. El precio total por la implementación asciende a **{{PRECIO_TOTAL}}** ({{PRECIO_LETRAS}}), {{TRATAMIENTO_IMPOSITIVO}}.

11.2. El precio se abonará conforme al siguiente esquema:

{{ESQUEMA_PAGOS}}

11.3. El pago se efectuará mediante {{MEDIO_PAGO}}. Los gastos, comisiones y costos de la transacción son a cargo de EL CLIENTE.

11.4. {{CLAUSULA_MONEDA}}

11.5. El primer pago constituye condición de inicio de los trabajos. EL PROVEEDOR no está obligado a comenzar la ejecución hasta su acreditación efectiva.

---

## DUODÉCIMA — COSTOS DE TERCEROS

12.1. El precio **no incluye** el costo de las Plataformas de Terceros, licencias, suscripciones, consumos de API, tokens, mensajería, publicidad, hosting ni infraestructura, los que son contratados, asumidos y abonados directamente por EL CLIENTE.

12.2. Las variaciones en los precios, políticas, condiciones o disponibilidad de dichas plataformas no modifican el precio ni las obligaciones de EL PROVEEDOR, ni generan responsabilidad alguna a su cargo.

---

## DÉCIMA TERCERA — MORA

13.1. La mora se producirá de pleno derecho por el mero vencimiento de los plazos, sin necesidad de interpelación previa.

13.2. El retraso en cualquier pago faculta a EL PROVEEDOR a suspender inmediatamente la ejecución, previo aviso, sin que ello constituya incumplimiento de su parte ni prorrogue sus obligaciones.

13.3. Las sumas impagas devengarán un interés moratorio equivalente a {{INTERES_MORA}}, desde la mora y hasta su efectivo pago.

13.4. El retraso superior a {{DIAS_RESOLUCION}} días corridos faculta a EL PROVEEDOR a resolver el Contrato, conservando los importes devengados y sin que opere la cesión de derechos de la Cláusula DÉCIMA CUARTA.

---

## DÉCIMA CUARTA — PROPIEDAD INTELECTUAL

14.1. **Cesión de la Implementación Específica.** EL PROVEEDOR cede a EL CLIENTE, en forma total, irrevocable y **no exclusiva**, los derechos patrimoniales de propiedad intelectual sobre la Implementación Específica, comprendiendo las configuraciones, parametrizaciones, integraciones, instrucciones adaptadas y documentación de entrega desarrolladas para EL CLIENTE.

14.2. **Condición de la cesión.** La cesión opera de pleno derecho y en forma automática a partir del pago total del precio pactado. Hasta entonces, EL CLIENTE cuenta con una autorización de uso precaria y revocable, que cesa de pleno derecho ante la falta de pago.

14.3. **Retención de los Componentes Base.** EL PROVEEDOR **conserva la titularidad plena y exclusiva** sobre los Componentes Base, que no son objeto de cesión. EL PROVEEDOR conserva el derecho irrestricto de utilizarlos, modificarlos, reutilizarlos, licenciarlos y comercializarlos, en proyectos para terceros o de cualquier otro modo, sin limitación de tiempo, territorio ni destinatario, y sin obligación de compensación alguna a EL CLIENTE.

14.4. **Licencia sobre los Componentes Base.** EL PROVEEDOR otorga a EL CLIENTE una licencia perpetua, irrevocable, mundial, no exclusiva, intransferible y libre de regalías sobre los Componentes Base, en la medida necesaria para usar, operar, modificar, mantener y evolucionar el Sistema para su propio negocio. Esta licencia subsiste indefinidamente luego de la terminación del Contrato.

14.5. **Restricción.** EL CLIENTE no podrá revender, sublicenciar, distribuir ni ceder los Componentes Base a terceros en forma autónoma o separada del Sistema, ni utilizarlos para desarrollar u ofrecer servicios de automatización a terceros.

14.6. **Reserva de conocimiento.** Los conceptos, técnicas, metodologías, arquitecturas, ideas, procedimientos y experiencia adquiridos o perfeccionados por EL PROVEEDOR con motivo de la ejecución del Contrato permanecen libremente disponibles para su uso en otros proyectos, sin más límite que las obligaciones de confidencialidad de la Cláusula DÉCIMA SEXTA.

14.7. **Plataformas de Terceros.** Las Plataformas de Terceros no son objeto de cesión ni de licencia bajo este Contrato y se rigen por sus propios términos.

14.8. **Datos y contenidos de EL CLIENTE.** Los datos, marcas, contenidos e información aportados por EL CLIENTE, así como los resultados generados por el Sistema a partir de ellos, son y continuarán siendo de su exclusiva titularidad.

14.9. **Garantía de titularidad.** EL PROVEEDOR declara contar con las facultades necesarias para realizar la cesión y otorgar la licencia previstas en esta cláusula. Su responsabilidad por reclamos de terceros vinculados a la propiedad intelectual queda sujeta a los límites de la Cláusula DÉCIMA NOVENA y no alcanza a reclamos derivados del Material del Cliente, de modificaciones no realizadas por EL PROVEEDOR, del uso del Sistema en combinación con elementos no provistos por éste, ni del uso en infracción del presente Contrato.

---

## DÉCIMA QUINTA — DIFUSIÓN Y CONTENIDO

15.1. EL CLIENTE **autoriza en forma irrevocable** a EL PROVEEDOR a difundir públicamente, con fines comerciales, educativos y de portfolio, en cualquier medio, formato y soporte —incluyendo sitio web, redes sociales, plataformas de video, presentaciones y materiales comerciales— información relativa al proyecto ejecutado, comprendiendo:

a) la mención de su denominación comercial y la utilización de su marca y logotipo a los fines de identificarlo como cliente;
b) la descripción del desarrollo realizado, su arquitectura, los flujos implementados, las herramientas y tecnologías utilizadas y la metodología aplicada;
c) la exhibición de material demostrativo del Sistema, incluyendo capturas, grabaciones y demostraciones funcionales;
d) los resultados y métricas obtenidos.

15.2. Dicha autorización **no requiere aprobación previa** de EL CLIENTE respecto de cada publicación, y EL CLIENTE **renuncia expresamente** a oponerse, objetar, requerir la remoción o reclamar por dicha difusión.

15.3. **Único límite.** EL PROVEEDOR se abstendrá de difundir credenciales, contraseñas, claves de acceso, tokens y datos personales identificables de terceros, adoptando las medidas razonables de ocultamiento a tal efecto.

15.4. La presente autorización subsiste sin límite temporal luego de la terminación del Contrato y prevalece sobre la Cláusula DÉCIMA SEXTA, que no será interpretada de modo que restrinja su ejercicio.

15.5. Nada de lo previsto en este Contrato limita el derecho de EL PROVEEDOR a producir y difundir contenido educativo, formativo o divulgativo sobre técnicas, arquitecturas, herramientas, patrones y Componentes Base de su titularidad, sin identificación de EL CLIENTE.

---

## DÉCIMA SEXTA — CONFIDENCIALIDAD

16.1. Cada Parte mantendrá la confidencialidad de la información no pública de la otra a la que acceda con motivo del Contrato, utilizándola exclusivamente para su ejecución.

16.2. La obligación subsiste durante {{PLAZO_CONFIDENCIALIDAD}} años desde la terminación. Se exceptúa la información pública, la conocida lícitamente con anterioridad, la desarrollada en forma independiente, la recibida de un tercero sin obligación de reserva y aquella cuya revelación sea requerida por autoridad competente.

16.3. Esta cláusula no alcanza a los Componentes Base ni al conocimiento reservado conforme a las Cláusulas 14.3 y 14.6, ni restringe la difusión autorizada por la Cláusula DÉCIMA QUINTA.

---

## DÉCIMA SÉPTIMA — DATOS PERSONALES

17.1. Cuando el Sistema trate datos personales, **EL CLIENTE reviste el carácter de responsable del tratamiento** y EL PROVEEDOR el de encargado, en los términos de la Ley 25.326 y su reglamentación.

17.2. EL CLIENTE garantiza que cuenta con base legal suficiente y con el consentimiento o la legitimación necesarios respecto de la totalidad de los datos personales que se incorporen al Sistema, y responde en forma exclusiva por la licitud de su origen, su finalidad y su tratamiento.

17.3. EL PROVEEDOR tratará los datos únicamente conforme a las instrucciones de EL CLIENTE y a los fines de la implementación, guardará confidencialidad y, concluida la ejecución, no conservará copias, salvo las necesarias para el cumplimiento de obligaciones legales.

17.4. Producida la Aceptación, el tratamiento queda íntegramente bajo control de EL CLIENTE, cesando toda intervención y responsabilidad de EL PROVEEDOR a ese respecto.

---

## DÉCIMA OCTAVA — TRANSPARENCIA EN EL USO DE IA

18.1. Cuando el Sistema interactúe directamente con personas humanas, EL PROVEEDOR lo dejará configurado de modo que permita informar que la interacción se produce con un sistema de inteligencia artificial.

18.2. EL CLIENTE, en su carácter de responsable del despliegue frente a sus destinatarios, velará por que dicha información se exhiba efectivamente y por la licitud del uso del Sistema conforme a la normativa aplicable.

---

## DÉCIMA NOVENA — RESPONSABILIDAD

19.1. **Límite.** La responsabilidad total y acumulada de EL PROVEEDOR por cualquier concepto derivado del presente Contrato, cualquiera sea la naturaleza del reclamo, no excederá el **{{TOPE_RESPONSABILIDAD}}% del precio total efectivamente percibido**.

19.2. **Exclusión de daños indirectos.** EL PROVEEDOR no responderá en ningún caso por daños indirectos, lucro cesante, pérdida de chance, pérdida de negocio, pérdida de clientes, interrupción de la actividad, pérdida o corrupción de datos por causa ajena, daño a la imagen o reputación, ni por expectativas de facturación de EL CLIENTE.

19.3. **Supuestos excluidos de responsabilidad.** EL PROVEEDOR no responderá por los hechos comprendidos en las Cláusulas 5.5, 5.6, 5.7, 9.3 y VIGÉSIMA.

19.4. Las limitaciones precedentes no resultan aplicables en caso de dolo o culpa grave de EL PROVEEDOR, ni respecto de la responsabilidad que legalmente no pueda limitarse.

---

## VIGÉSIMA — FUERZA MAYOR Y DEPENDENCIA DE TERCEROS

20.1. Ninguna Parte responderá por el incumplimiento debido a caso fortuito o fuerza mayor ajenos a su control razonable. Los plazos se suspenderán mientras subsista la causa.

20.2. EL CLIENTE reconoce que el Sistema depende de Plataformas de Terceros cuya disponibilidad, calidad, funcionamiento, políticas y continuidad se encuentran fuera del control de EL PROVEEDOR. EL PROVEEDOR no responderá por su indisponibilidad, degradación, modificación, discontinuación, cambio de condiciones o de precios, ni por las restricciones de uso que dichos terceros impongan, las que EL CLIENTE se obliga a observar.

---

## VIGÉSIMA PRIMERA — TERMINACIÓN

21.1. El Contrato se extingue por el cumplimiento de las prestaciones, producida la Aceptación y abonado el precio total, sin perjuicio de la garantía y de las cláusulas de subsistencia.

21.2. Cualquiera de las Partes podrá resolver el Contrato ante incumplimiento grave de la otra no subsanado dentro de los {{PLAZO_SUBSANACION}} días corridos de la intimación escrita que describa concretamente el incumplimiento.

21.3. Resuelto el Contrato por causa imputable a EL PROVEEDOR, EL CLIENTE tendrá derecho a la devolución de la porción proporcional del precio abonada y no ejecutada, con el límite de la Cláusula DÉCIMA NOVENA, y sin derecho a indemnización adicional alguna.

21.4. Resuelto el Contrato por causa imputable a EL CLIENTE, EL PROVEEDOR conservará la totalidad de los importes devengados y no operará la cesión de la Cláusula DÉCIMA CUARTA.

21.5. La resolución deberá notificarse por medio fehaciente. No se admitirán comunicaciones resolutorias por mensajería instantánea.

---

## VIGÉSIMA SEGUNDA — DISPOSICIONES GENERALES

22.1. **Independencia.** Las Partes son contratantes independientes. Nada en este Contrato crea relación laboral, societaria, de agencia ni de representación.

22.2. **No solicitación.** Durante la vigencia y por {{PLAZO_NO_SOLICITACION}} meses posteriores, EL CLIENTE se abstendrá de contratar o vincular, directa o indirectamente, al personal o colaboradores afectados por EL PROVEEDOR a la ejecución, salvo autorización escrita.

22.3. **Cesión.** Ninguna Parte podrá ceder su posición contractual sin conformidad escrita de la otra.

22.4. **Notificaciones.** Las comunicaciones se cursarán válidamente a los correos electrónicos {{PROVEEDOR_EMAIL}} y {{INTERLOCUTOR_EMAIL}}, y las de carácter fehaciente a los domicilios constituidos en el encabezamiento.

22.5. **Firma electrónica.** Las Partes reconocen expresamente la validez y eficacia probatoria de la firma electrónica y de la suscripción por medios digitales del presente y de sus anexos, renunciando a impugnarlos por el solo hecho de haberse instrumentado por dichos medios. El Contrato podrá suscribirse en ejemplares separados, que en conjunto constituirán un único instrumento.

22.6. **Integralidad.** El presente Contrato y sus Anexos constituyen el acuerdo íntegro entre las Partes y reemplazan toda negociación, propuesta, cotización o comunicación previa. Toda modificación deberá instrumentarse por escrito y ser suscripta por ambas Partes.

22.7. **Nulidad parcial.** La invalidez de una cláusula no afectará la validez de las restantes.

22.8. **Anexos.** Forman parte integrante e inseparable del presente el Anexo I (alcance técnico y métricas) y el Anexo II (accesos y credenciales requeridos).

---

## VIGÉSIMA TERCERA — SUBSISTENCIA

Subsisten a la terminación del Contrato, por cualquier causa, las Cláusulas QUINTA (5.8), DÉCIMA CUARTA, DÉCIMA QUINTA, DÉCIMA SEXTA, DÉCIMA SÉPTIMA, DÉCIMA NOVENA, VIGÉSIMA SEGUNDA y VIGÉSIMA CUARTA.

---

## VIGÉSIMA CUARTA — LEY APLICABLE Y JURISDICCIÓN

24.1. El presente Contrato se rige por las leyes de la República Argentina.

24.2. Para toda controversia derivada del presente, las Partes se someten a la competencia de los Tribunales Ordinarios en lo Comercial de la Ciudad Autónoma de Buenos Aires, con renuncia expresa a cualquier otro fuero o jurisdicción que pudiera corresponderles.

---

En prueba de conformidad, las Partes suscriben el presente en dos ejemplares de un mismo tenor y a un solo efecto, en el lugar y fecha indicados.

<br><br>

| | |
|---|---|
| _______________________ | _______________________ |
| **EL PROVEEDOR** | **EL CLIENTE** |
| {{PROVEEDOR_NOMBRE}} | {{CLIENTE_RAZON_SOCIAL}} |
| CUIT {{PROVEEDOR_CUIT}} | CUIT {{CLIENTE_CUIT}} |
| | {{CLIENTE_FIRMANTE}} — {{CLIENTE_FIRMANTE_CARGO}} |

---
---

# ANEXO I — ALCANCE TÉCNICO Y MÉTRICAS

## 1. Descripción del Sistema

{{DESCRIPCION_SISTEMA}}

## 2. Alcance incluido

{{ALCANCE_INCLUIDO}}

## 3. Entregables

{{ENTREGABLES}}

## 4. Integraciones y canales

{{INTEGRACIONES}}

## 5. Plataformas de Terceros utilizadas

{{PLATAFORMAS_TERCEROS}}

## 6. Componentes de IA y roles dentro del flujo

{{ROLES_IA}}

Los roles precedentes se encuentran sujetos al umbral de desempeño de la Cláusula 5.2, con las exclusiones de las Cláusulas 5.4, 5.5, 5.6 y 5.7.

## 7. Acciones determinísticas

{{ACCIONES_DETERMINISTICAS}}

## 8. Métricas garantizadas

{{METRICAS_GARANTIZADAS}}

## 9. Criterios de aceptación

{{CRITERIOS_ACEPTACION}}

## 10. Cronograma

{{CRONOGRAMA}}

---

# ANEXO II — ACCESOS Y CREDENCIALES REQUERIDOS

EL CLIENTE se obliga a proveer, dentro del plazo previsto en la Cláusula 6.1, los siguientes accesos:

{{ACCESOS_REQUERIDOS}}

**Interlocutor designado:** {{INTERLOCUTOR_NOMBRE}} — {{INTERLOCUTOR_EMAIL}}

La falta de provisión en término activa los efectos previstos en las Cláusulas 6.5 y 6.6.
