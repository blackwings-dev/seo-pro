---
title: "Analítica y experimentación para SEO"
subtitle: "Instrumentación, atribución, cohortes, incrementalidad y alertas de cambios"
version: "1.0"
research_cutoff: "2026-10-18"
language: "es"
scope: "Medición orgánica en sitios web y aplicaciones, con énfasis en Google Search, GA4 y diseños causales"
---

# Analítica y experimentación para SEO

## Estudio independiente de investigación y manual operativo

**Fecha de corte: 18 de octubre de 2026.** SEO se suele evaluar con posiciones, clics o sesiones, pero ninguna de esas métricas responde por sí sola a la pregunta que normalmente importa: qué valor aportó el trabajo, qué cambió por la intervención y qué habría ocurrido sin ella.

Esta guía presenta un sistema de medición que combina datos de búsqueda, analítica de producto y negocio, cohortes, pruebas controladas y alertas. Distingue cuatro operaciones que a menudo se confunden: **observación** (qué pasó), **atribución** (a qué canal se asigna crédito), **predicción** (qué esperamos que pase) e **inferencia causal** (qué resultado adicional produjo una intervención frente a un contrafactual). Ninguna plataforma de analítica convierte automáticamente una correlación en causalidad.

## 1. Alcance, método y límites

### 1.1 Preguntas que debe responder un sistema SEO

1. ¿Los buscadores muestran y rastrean las páginas que queremos que descubran?
2. ¿Qué consultas, páginas, países, dispositivos y superficies aportan clics?
3. ¿Qué hacen las personas después de llegar desde búsqueda?
4. ¿Cuántos resultados relevantes para el negocio aparecen en la trayectoria, según una regla de atribución declarada?
5. ¿Qué grupos regresan, se suscriben, compran o generan valor con el tiempo?
6. ¿Una intervención SEO mejoró el resultado frente a lo que probablemente habría pasado sin ella?
7. ¿Cómo detectamos a tiempo pérdida de indexación, fallos de medición, caída de demanda o cambio de comportamiento?

### 1.2 Jerarquía de evidencia

- **Fuente del comportamiento dentro de cada sistema:** Search Console para la presencia en productos de Google; GA4, analítica propia o registros para interacciones observables dentro del sitio; CRM/comercio para ventas, leads cualificados y valor posterior.
- **Documentación de proveedor:** explica definiciones, procesamiento y limitaciones de su propio dato. No convierte ese dato en una medición universal.
- **Experimento aleatorizado bien diseñado:** mejor base para atribución causal cuando la unidad se puede asignar sin contaminar grupos.
- **Diseño cuasiexperimental:** difference-in-differences, series temporales interrumpidas, control sintético o grupos emparejados; útil cuando no se puede aleatorizar, pero depende de supuestos y diagnósticos.
- **Comparación antes/después o modelo de atribución:** describe cambios o distribuye crédito. Por sí solo no identifica qué habría pasado sin la intervención.

### 1.3 Límites y privacidad

Search Console y Analytics difieren en unidad de medida, cobertura, reglas de procesamiento, zonas horarias, privacidad y atribución. Search Console oculta consultas de bajo volumen o sensibles, limita filas y puede truncar resultados; no es un registro completo de todas las búsquedas. GA4 depende de etiquetas, consentimiento, navegador, identidad y modelado. CRM tampoco recoge automáticamente ingresos o cualificación de todos los canales.

En la Unión Europea y otros mercados regulados, la implementación de etiquetas, identificadores, consentimiento, importación de conversiones y retención debe revisarse con responsables de privacidad/legal según la normativa aplicable. Esta guía es metodológica, no asesoramiento jurídico. Diseña la medición con minimización de datos, propósito explícito, accesos limitados y agregación suficiente; no intentes reconstruir identidad individual a partir de señales incompletas.

## 2. Modelo mental: del resultado visible al valor

Un embudo de medición útil separa etapas:

| Etapa | Pregunta | Fuentes frecuentes | Métricas |
|---|---|---|---|
| Salud técnica | ¿Puede el motor acceder y procesar? | Logs, crawl, Search Console, monitor de disponibilidad | 4xx/5xx, latencia, URLs bloqueadas, cobertura, canonical |
| Visibilidad | ¿En qué búsquedas aparece el sitio? | Search Console; Bing Webmaster Tools | Impresiones, consultas, posición media, apariencia |
| Entrada | ¿Cuántas visitas llegan? | Search Console, analítica, logs | Clics, sesiones orgánicas, landing pages |
| Experiencia | ¿La página ayuda a completar una tarea? | Analítica de eventos, pruebas de UX | uso de buscador, interacción, retorno, engagement definido |
| Resultado | ¿Qué acción importante ocurre? | Analítica, CRM, ecommerce, suscripciones | lead, compra, margen, suscripción, retención |
| Incrementalidad | ¿Qué resultado adicional generó SEO? | Experimento o modelo causal + datos de negocio | lift neto frente a control, intervalo de incertidumbre |

La conexión de estas etapas sirve para localizar el problema y priorizar inversión. No asumas que cada fila es un embudo lineal: una persona puede descubrir, volver por otro canal, convertir semanas después o usar varios dispositivos.

## 3. Instrumentación: medir la acción, no solo la visita

### 3.1 Diseñar primero el contrato de medición

Antes de desplegar etiquetas, crear un diccionario que defina cada evento y cada métrica:

| Campo | Ejemplo de especificación |
|---|---|
| Nombre del evento | `generate_lead` o nombre recomendado pertinente |
| Descripción | Solicitud enviada correctamente, no solo botón pulsado |
| Momento de disparo | Confirmación del servidor o estado exitoso de la aplicación |
| Parámetros permitidos | `form_type`, `page_type`, `lead_category`; sin texto personal libre |
| ID de deduplicación | `lead_id` interno no identificable o token técnico conforme a política |
| Valor | Importe o valor esperado cuando esté definido, unidad y moneda explícitas |
| Fuente de verdad | CRM, plataforma de pedidos, backend o analítica |
| Propietario | Responsable de negocio/analítica/ingeniería |
| QA | Prueba de aceptación, evento esperado y condición de duplicación |
| Uso en decisiones | KPI principal, diagnóstico o solo exploratorio |

Usa nombres y parámetros estables entre versiones. Prefiere los eventos recomendados por GA4 cuando expresan la acción; crea eventos personalizados solo cuando no existe uno adecuado. Cambiar el significado de un evento existente rompe las comparaciones históricas: versiona los cambios y anota fecha y lógica.

### 3.2 Eventos orientados al negocio

Ejemplos a adaptar al modelo de negocio:

- **Ecommerce:** vista de lista y producto, carrito, inicio de checkout, compra confirmada, devolución, valor, moneda, artículos y cantidad. El backend/plataforma de pagos es la fuente de verdad de la venta; GA4 sirve para comportamiento y análisis, no para conciliar contabilidad.
- **Lead generation:** inicio de formulario, error, envío exitoso, llamada cualificada, lead aceptado y venta cerrada. Una impresión de formulario o un clic no equivalen a lead.
- **SaaS:** registro, activación (evento que representa valor real), uso recurrente, inicio y final de prueba, suscripción, expansión y cancelación. Alinear la ventana de cohorte con el ciclo de activación y venta.
- **Publisher:** registro, alta a newsletter, lectura comprometida con definición interna, muro, suscripción, renovación y baja; visitas de página no representan por sí solas relación duradera.
- **Servicio local:** clic para llamar, reserva, solicitud enviada y cita atendida; separar microconversiones de ventas confirmadas.

### 3.3 Reglas de calidad de eventos

- Disparar acciones de éxito después de confirmación, evitando que un doble clic, recarga o vuelta de pago cree dos compras/leads.
- En transacciones, incluir un identificador de transacción que permita detectar duplicados y conciliar con la plataforma.
- En ingresos, definir moneda, impuestos, descuentos, envío, reembolsos, valor bruto/neto y momento de reconocimiento.
- Validar parámetros, formatos, valores nulos y cambios de esquema en DebugView/Realtime, logs y reportes posteriores.
- Separar eventos del usuario de eventos automáticos/de infraestructura; no convertir cada interacción técnica en una “conversión”.
- Excluir entornos internos, QA y bots según criterios verificables, sin borrar tráfico legítimo.
- Comprobar que el consentimiento cambia la recogida según la configuración implementada; no interpretar modelado como observación directa.
- Documentar zona horaria, moneda, atribución, lookback y ventana de conversión.

### 3.4 Datos de búsqueda y analítica: unir sin confundir

Search Console describe lo ocurrido en resultados de Google antes del clic: impresiones, clics, consultas, páginas, país, dispositivo y tipo de búsqueda. Analytics describe actividad instrumentada después de la llegada. Una impresión no es una visita; un clic de Search Console no equivale necesariamente a una sesión de GA4. Las diferencias pueden venir de carga incompleta, consentimiento, bloqueadores, varias pestañas, zona horaria, procesamiento, redirecciones, canonical, límites y privacidad.

Compara primero tendencias y segmentos equivalentes, no igualdad exacta de totales. En Search Console, los datos de consulta pueden omitir consultas anonimizadas; filtrar por consulta o URL también puede cambiar los totales. GA4 modela parte de la actividad no observada bajo condiciones determinadas y los modelos de atribución pueden actualizarse después del evento. Señala estas diferencias en cada panel y no rellenes huecos con una falsa precisión.

### 3.5 Arquitectura de datos y conservación

Define qué herramienta es fuente de verdad para cada métrica. Si necesitas análisis de largo plazo, cohortes de usuario, combinación con CRM o un historial de más detalle que el disponible en informes estándar, diseña exportación a un almacén de datos y copias agregadas de Search Console cuando corresponda. Valida coste, retención, frescura, esquema, tratamiento de consentimiento y permisos. La exportación tampoco restaura información que nunca se recogió o se suprimió.

En GA4, la retención de datos de usuario y eventos que afecta a exploraciones es configurable y está limitada (la documentación consultada indica hasta 14 meses en propiedades estándar); algunas métricas agregadas de informes tienen reglas diferentes. Configura la retención deliberadamente y verifica el comportamiento actual de la propiedad antes de depender de cohortes históricas.

## 4. Métricas SEO: definiciones, denominadores y diagnóstico

### 4.1 Métricas de búsqueda

- **Impresiones:** exposición medida por la definición de cada reporte/superficie; no representa demanda total del mercado.
- **Clics:** interacción con un resultado de Google, con reglas por tipo de resultado.
- **CTR:** clics ÷ impresiones; cambia por consulta, posición, dispositivo, SERP, marca y composición de resultados. No se interpreta aislado.
- **Posición media:** agregación de posiciones observadas según las reglas de Search Console; no equivale a una posición única y estable para todas las personas.
- **Cobertura/indexación:** estados de URL informados por Search Console; no es un KPI de tráfico ni la proporción exacta de todo el contenido elegible.
- **Share de clics / visibilidad estimada:** requiere proveedor/modelo externo; documentar cobertura y supuestos.

### 4.2 Métricas de producto/negocio

Utiliza resultados con denominadores claros: ingresos orgánicos, margen de contribución, compras, leads cualificados, pipeline, activación, suscripciones, retención, reembolso, coste de servicio y tiempo hasta conversión. Un KPI SEO principal debe estar influenciable por SEO, ser medible con estabilidad razonable y conectar con un resultado de negocio.

Como guardrails, observa métricas que no deben empeorar: calidad de lead, tasa de devolución, velocidad, satisfacción, ingresos por usuario, errores de compra, cancelación y páginas no orgánicas afectadas. Una intervención puede aumentar visitas y reducir valor por usuario.

### 4.3 Segmentar antes de promediar

Reporta al menos por:

- query: marca/no marca y grupos de intención;
- URL y plantilla: producto, categoría, artículo, landing, ubicación, documentación;
- tipo de búsqueda/superficie, país/idioma y dispositivo;
- página nueva vs histórica, tipo de conversión y cliente nuevo/recurrente;
- tipo de intervención y fecha de despliegue.

El total agregado puede ocultar que una plantilla gana mientras otra pierde. Define los grupos antes de mirar el resultado cuando sea posible; si se crean tras observarlo, marca el análisis como exploratorio para controlar la selección de hallazgos.

## 5. Atribución: crédito no significa causalidad

### 5.1 Qué es la atribución

Un modelo de atribución distribuye crédito entre interacciones de una trayectoria. GA4 ofrece modelos como basado en datos y último clic de canales disponibles según el reporte/configuración actual. El resultado depende de identidad observable, ventanas, canales incluidos, configuración, consentimientos y modelado.

**Atribución responde:** “Con esta regla, ¿qué canal recibe crédito por la conversión observada o modelada?”

**Causalidad responde:** “¿Cuánto habría cambiado la conversión si no hubiéramos realizado esta intervención?”

La segunda pregunta necesita comparación válida o supuestos contrafactuales. Una conversión atribuida a orgánico no demuestra que SEO la causara: algunas personas habrían comprado de todos modos, quizá por marca, email, venta presencial, demanda existente o retorno directo.

### 5.2 Modelo de reporting recomendado

Presenta varias vistas, cada una con propósito y límites:

1. **Demanda y presencia:** impresiones, consultas, clics y posición de Search Console.
2. **Adquisición de sesiones:** landing pages orgánicas y sesiones/usuarios de analítica.
3. **Atribución de resultados:** key events/conversiones y revenue bajo el modelo declarado; preferir más de un modelo cuando la decisión dependa de él.
4. **Resultado de negocio conciliado:** pedidos, leads aceptados o margen desde sistemas transaccionales, segmentado con la regla disponible.
5. **Incrementalidad:** estimación experimental/cuasi experimental, separada visualmente de la atribución de plataforma.

No sumes cifras de herramientas distintas. No declares “SEO generó X” si la cifra es solo crédito de último clic o un modelo propietario; escribe “GA4 asigna X a orgánico bajo [modelo/ventana]”.

### 5.3 Atribución de canal y tráfico de marca

Las búsquedas de marca suelen incluir conocimiento previo; separarlas ayuda a distinguir captura de demanda existente de descubrimiento no marcado. La frontera no siempre es limpia: una persona puede descubrir la marca en búsqueda no marcada y regresar después por búsqueda de marca. Atribuir todo el segundo paso al canal de entrada o todo a marca puede sobrevalorar una etapa y ocultar el recorrido.

Usa el filtro de marca de Search Console si está disponible en la propiedad y período, pero recuerda que el filtrado de consultas omite consultas anonimizadas, por lo que la fracción es aproximada. Mantén una clasificación propia transparente para cohortes de consultas y registra variantes, errores ortográficos, marcas de producto y consultas ambiguas.

## 6. Cohortes: adquisición, retorno y valor a lo largo del tiempo

### 6.1 Definir la cohorte

Una cohorte agrupa entidades que comparten una condición inicial. Para SEO, ejemplos:

- usuarios cuya primera visita observable fue orgánica;
- usuarios que aterrizaron por primera vez en una plantilla o grupo de intención;
- usuarios adquiridos durante una semana/mes y país;
- leads originados por una landing orgánica y posteriormente cualificados en CRM;
- clientes cuyo primer producto o alta vino de una página orgánica determinada.

Define: unidad (usuario, sesión, lead, cuenta, pedido), fecha de entrada, criterio de adquisición, evento de retorno, ventana, métrica y exclusiones. No mezcles cohorte de primera adquisición con canal de la sesión que convierte.

### 6.2 Métricas de cohorte

| Resultado | Denominador | Ejemplo de lectura |
|---|---|---|
| Retorno D7/W4/M3 | Miembros de cohorte elegibles | Proporción que vuelve en período definido |
| Activación | Nuevas cuentas/leads elegibles | Proporción que completa el hito de valor dentro de ventana |
| Conversión acumulada | Usuarios o leads de cohorte | Proporción que convierte hasta un tiempo desde adquisición |
| Ingreso acumulado | Miembros de cohorte | Revenue observado o reconocido hasta mes N |
| Margen/LTV | Clientes elegibles | Valor económico neto con supuestos explícitos de retención/coste |
| Tiempo a resultado | Usuarios/leads elegibles | Mediana/percentiles hasta primera compra, cualificación o suscripción |

La ventana adecuada depende del ciclo de compra. Un SaaS B2B con seis meses de venta no debe evaluarse con la retención de una app de uso diario; un ecommerce de compra ocasional no debe tratar cada semana como fallo de retención.

### 6.3 Buenas prácticas y trampas

- Comparar cohortes equivalentes por temporada, mercado, dispositivo y producto; controlar cambios en precios, promoción, inventario y onboarding.
- Separar usuarios nuevos de recurrentes y evitar inferir que `first user source` equivale a causa exclusiva del valor vitalicio.
- Considerar cohortes censuradas: las adquisiciones recientes aún no han tenido tiempo de convertir; usar edad de cohorte/curvas de supervivencia, no comparar acumulados incompletos.
- Reportar cantidad y tamaño de cohorte, tasas y valor absoluto; no esconder muestras pequeñas detrás de porcentajes llamativos.
- Si se usa GA4 Cohort Exploration, conocer su unidad/criterios y límites: la ayuda indica que las cohortes usan datos de dispositivo, no User-ID, y que hay límites de cohortes/dimensiones.
- Para cohortes que requieren ID persistente entre fuentes, diseñar el join en CRM/warehouse con base legal, seguridad, calidad y política de minimización apropiadas; no esperar que la exploración estándar haga esa unión.

## 7. Incrementalidad: medir lo que SEO añadió

### 7.1 La pregunta contrafactual

El efecto incremental de una intervención es la diferencia entre resultado observado con intervención y resultado que la misma unidad habría tenido sin ella. Ese segundo resultado no se observa directamente. El diseño de evaluación intenta estimarlo.

La ecuación simple de diferencia en diferencias es:

```text
Efecto estimado = (Tratamiento_después − Tratamiento_antes)
                 − (Control_después − Control_antes)
```

Se interpreta causalmente solo si los grupos habrían seguido tendencias comparables sin el tratamiento y no sufren shocks distintos relevantes, entre otros supuestos. Una prueba de tendencias previas ayuda a diagnosticar, pero no demuestra por sí sola el supuesto.

### 7.2 Diseños, de más a menos concluyentes

| Diseño | Aplicación SEO | Fortaleza | Riesgo/supuesto clave |
|---|---|---|---|
| Aleatorización por URL/grupo de páginas | Actualización de títulos, enlazado, contenido o plantilla en una muestra aleatoria de URLs | Reduce confusión si grupos y medición son válidos | Interferencia por enlaces internos, cambios globales, canonicalización y heterogeneidad de páginas |
| Experimento aleatorizado por usuario | Experiencia de landing, CTA, navegación o CRO después del clic | Estima impacto de UX/conversión dentro de la población asignada | No estima necesariamente impacto de ranking/impresiones si Google ve variante o la exposición no está aleatorizada |
| Despliegue escalonado aleatorio | Implementar grupos en fases y sortear el orden | Todos reciben mejora; proporciona comparaciones temporales | El tiempo, la estacionalidad y los efectos de anticipación se confunden si el diseño es débil |
| Difference-in-differences / event study | Intervención sobre un grupo de URLs con control comparable | Aprovecha series históricas cuando no se puede sortear | Tendencias paralelas, ausencia de shocks diferenciales, cambios simultáneos y composición estable |
| Control sintético / serie temporal interrumpida | Un sitio, sección o mercado tratado con controles predictivos | Útil para intervención amplia sin unidad de control clara | Ajuste preintervención, estabilidad de relación, predictores no contaminados y ausencia de otros cambios concurrentes |
| Antes/después simple | Cambios operativos pequeños o monitorización inicial | Fácil y rápido | Confunde intervención con estacionalidad, demanda, competencia, SERP y actualizaciones |

En SEO, la unidad experimental suele ser grupo de páginas, categoría o cluster de consulta, no la persona: Google decide qué versión rastrea y expone. Evita dividir la misma plantilla o entidad de forma que páginas tratadas y control se pasen señales por enlaces, canonical o contenido duplicado. Si la intervención afecta todo el dominio (p. ej. arquitectura, plataforma, política de indexación), un control interno puede quedar contaminado; considera un control externo o una serie temporal y baja el nivel de certeza.

### 7.3 Protocolo de experimento SEO

1. **Hipótesis causal:** cambio concreto y mecanismo esperado (p. ej. mejorar enlaces internos a un conjunto comparable de páginas para aumentar descubrimiento/clics cualificados).
2. **Resultado primario:** uno, predefinido; por ejemplo clics orgánicos por URL elegible en ventana, conversiones cualificadas o margen. Elegirlo según mecanismo y latencia.
3. **Guardrails:** indexabilidad, 404/5xx, conversión, calidad, velocidad y páginas no tratadas.
4. **Unidad y población:** páginas elegibles; reglas de inclusión/exclusión fijadas antes de asignar.
5. **Asignación:** aleatoria cuando se pueda, estratificada por plantilla, tráfico basal, posición, edad, demanda, país y estacionalidad.
6. **Control:** conservar experiencia actual; prevenir cambios no planificados y registrar contaminación.
7. **Período pre y post:** suficiente para variabilidad y retraso de rastreo; definir cómo manejar fines de semana, estacionalidad, lanzamientos y updates.
8. **MDE y potencia:** definir el cambio mínimo que merecería el coste; estimar muestra/variabilidad antes de ejecutar. Si el tráfico es bajo, el resultado puede ser inconcluso; no cambiar la regla después de mirar los datos.
9. **Pre-registro:** guardar fecha, hipótesis, URLs, tratamiento, métricas, exclusiones, análisis, parada y quién decide.
10. **Análisis:** intención de tratar por asignación original; reportar efecto absoluto, relativo, intervalo de confianza/credibilidad, tamaño de muestra y supuestos.
11. **Decisión:** implementar, iterar o rechazar según umbral predefinido y guardrails. “No significativo” no prueba efecto cero; puede indicar falta de potencia.
12. **Replicación:** repetir en otro conjunto/periodo si la decisión afecta escala importante.

### 7.4 Errores que invalidan experimentos

- Elegir páginas “ganadoras” después de ver su rendimiento posterior.
- Cambiar varios elementos simultáneamente y atribuir el resultado a uno.
- Parar el test cuando el gráfico se ve favorable (peeking) o prolongarlo solo hasta conseguir significancia.
- No ajustar por estacionalidad, tendencias previas, actualizaciones, campañas, stock, noticias o cambios de SERP.
- Usar sesiones como denominador cuando el tratamiento cambia impresiones/clics; el tráfico condicionado al clic puede ser un resultado post-tratamiento.
- Contaminar el control mediante enlaces, plantillas compartidas, redirecciones, cambios del sitemap o cambios globales.
- Hacer muchos cortes y reportar solo el favorable (múltiples comparaciones).
- Confundir cambio estadísticamente detectable con efecto que compensa el coste o riesgo de implementación.

### 7.5 Ejemplo de decisión

Se actualizan breadcrumbs y enlaces contextuales en un grupo de 120 páginas de una plantilla. Emparejar o estratificar por clics e impresiones previos, antigüedad, intención y posición; asignar páginas comparables a tratamiento/control; congelar otras modificaciones en ambos grupos; medir impresiones y clics por URL (mecanismo SEO) y conversiones por landing (valor), junto a errores y canónicos (guardrails). Si cambian links a la vez en todo el sitio o hay una actualización global, documentar la contaminación y reducir confianza. El resultado puede ser “prometedor pero inconcluso”, no necesariamente éxito/fracaso binario.

## 8. Análisis de cambios y atribución temporal

Una línea que sube después de un despliegue no demuestra que el despliegue la causó. Investiga en este orden:

1. Marca fecha exacta de release, rollout, contenido, robots, CDN, consentimiento, tag manager y cambios de negocio.
2. Comprueba salud técnica primero: respuesta, indexación, canonical, sitemap, renderizado, logs y medición.
3. Separa Search, Discover, News, imágenes y vídeo cuando aplique; las superficies tienen demanda y comportamiento diferentes.
4. Descompón por página, consulta, plantilla, país, dispositivo y marca/no marca para localizar el origen matemático del total.
5. Compara contra periodo anterior y mismo periodo interanual; inspecciona días de semana, vacaciones, campañas, stock y demanda de categoría.
6. Revisa cambios de SERP, competencia y actualizaciones de ranking/documentación; correlación de fecha es contexto, no prueba.
7. Contrasta clics GSC con sesiones orgánicas y con resultados de CRM/ventas; diagnostica discrepancias antes de atribuirlas.
8. Para una afirmación causal, busca control experimental o contrafactual; si no existe, presenta el resultado como observacional con supuestos.

Search Console recomienda revisar consultas, páginas, países y dispositivos, usar comparación temporal pertinente y reconocer que cambios de demanda, competidores y eventos externos también alteran rendimiento. Para SEO, 16 meses de historial puede ayudar a observar estacionalidad anual, aunque hay que considerar cambios de producto y de medición.

## 9. Alertas: detectar cambios sin llenar de ruido

### 9.1 Capas de alertas

| Prioridad | Ejemplos | Canal y respuesta |
|---|---|---|
| P0 — disponibilidad/seguridad | Dominio caído, TLS expirado, 5xx general, robots bloqueando todo, hack/incidente | Página técnica inmediata; asignar guardia y comprobar desde fuera |
| P1 — pérdida de indexabilidad | `noindex` global, canonical al staging, sitemap inválido, caída de URLs válidas, 404 masivo | Aviso inmediato/día; reproducir y acotar páginas afectadas |
| P2 — cambio de visibilidad | Clics/impresiones por debajo del rango estacional, CTR o cobertura anómalos por plantilla | Alerta diaria/semanal con segmento y baseline |
| P3 — negocio y calidad | Caída de leads aceptados, ventas orgánicas, margen, activación o retorno | Alerta semanal/mensual adaptada al ciclo de conversión |
| P4 — oportunidad | Aumento de impresiones sin clic, queries emergentes, páginas que ganan visibilidad | Digest editorial/SEO; revisar muestra antes de actuar |

### 9.2 Diseño estadístico de una alerta

- Usa un baseline que contemple estacionalidad, día de semana y volumen esperado; umbral fijo de “−20 %” no sirve igual para 10 o 100.000 clics.
- Exige relevancia absoluta (número de clics, URLs o valor afectado) además de variación relativa.
- Añade persistencia, por ejemplo dos ventanas consecutivas para alertas no críticas, para reducir ruido; una caída técnica global no debe esperar confirmación estadística prolongada.
- Calcula el impacto por cohorte/plantilla y usa guardrails; no alertes en el total del sitio si varias secciones se mueven en direcciones opuestas.
- Define acción, propietario y tiempo objetivo en cada alerta. Una notificación sin responsable no es un sistema de alertas.
- Registra falso positivo, falso negativo, causa y resolución; recalibra límites con historial.
- Distingue alerta de anomalía (dato inusual) de alerta causal (no existe tal automatismo).

### 9.3 Herramientas y cobertura

GA4 ofrece Insights automáticos y condiciones personalizadas de anomalía con notificaciones en la interfaz y, opcionalmente, por email; su cadencia y conjunto de métricas dependen de la configuración. Search Console envía mensajes para eventos importantes y tiene reportes diagnósticos, pero no sustituye un sistema propio de alertas por página/valor. Complementa con:

- monitor externo de uptime, DNS, TLS, robots, sitemap y status de páginas clave;
- logs/observabilidad para respuestas 4xx/5xx, render y rastreo;
- GSC API o exportaciones para cambios desglosados, gestionando límites y retrasos;
- Bing Webmaster Tools y otras fuentes relevantes del mercado;
- seguimiento de transacciones/leads del backend y checks de caída de eventos;
- calendario de releases, campañas, inventario, publicaciones y cambios de consentimiento.

## 10. Tablero y gobierno de métricas

### 10.1 Vista ejecutiva

Una página para decisiones de dirección:

- clics orgánicos y visibilidad por mercado/superficie, con comparación estacional;
- ventas/leads/margen observados y atribuidos, etiquetados por metodología;
- tendencia incremental estimada y nivel de evidencia, cuando exista estudio válido;
- guardrails de calidad, experiencia y dependencia de marca;
- incidencias y cambios recientes relevantes.

### 10.2 Vista operativa

- rendimiento por consulta, página, plantilla, país, dispositivo y tipo de resultado;
- cohortes orgánicas y curvas de retorno/activación/valor;
- cobertura, canonicals, sitemaps, errores, robots, Core Web Vitals y release markers;
- panel de experimentos: hipótesis, diseño, estado, muestra, resultado, confianza y decisión;
- salud de tracking: tasa de eventos por sesión/página, duplicados, ratio de compra vs backend y cobertura de consentimiento.

### 10.3 Contrato de métrica

Para cada KPI publicar nombre, pregunta, numerador, denominador, unidad, fuente, filtros, ventana, retraso, owner, cambio de definición, caveat y uso permitido. Ejemplo: “Conversiones orgánicas atribuidas” no es intercambiable con “ventas incrementales por SEO”.

## 11. Errores de interpretación que conviene descartar

| Afirmación | Corrección |
|---|---|
| “GA4 dice que SEO generó la venta.” | GA4 asigna crédito bajo un modelo, ventana e identidad disponibles; causalidad requiere comparación contrafactual. |
| “GSC y GA4 tienen que coincidir.” | Clics y sesiones tienen definiciones y cobertura distintas; compara tendencias y diagnostica discrepancias. |
| “Subieron clics, mejoró SEO.” | Puede ser demanda, SERP, marca, distribución, medición o estacionalidad; descompón y valida resultado. |
| “La posición media bajó, por eso perdimos tráfico.” | La métrica agrega consultas/URLs y no describe la misma cesta; analiza páginas y consultas con impresiones/clics. |
| “El porcentaje de retención de GA4 demuestra lealtad.” | Depende de identidad observable, definición de retorno, consentimiento y ventana; cotejar con CRM/producto. |
| “Una prueba sin p<0,05 demuestra que el cambio no funciona.” | Puede faltar potencia o duración; reporta intervalos, MDE y resultado inconcluso. |
| “Difference-in-differences elimina todos los factores externos.” | Solo bajo supuestos como tendencias paralelas y ausencia de shocks diferenciales relevantes. |
| “Una alerta de anomalía identifica la causa.” | Detecta una desviación; el diagnóstico causal es trabajo posterior. |
| “Más sesiones orgánicas siempre es mejor.” | No si cae calidad, margen, activación, conversión o experiencia. |

## 12. Hoja de ruta de 90 días

### Días 1–15: definiciones y diagnóstico

- Definir objetivos comerciales por tipo de página y funnel.
- Auditar consentimientos, tags, eventos, fuentes de verdad, zonas horarias, atribución y retención.
- Comparar GSC/GA4/backend y documentar discrepancias esperadas.
- Crear diccionario de eventos y contrato de KPI con responsables.

### Días 16–35: instrumentación y calidad

- Corregir eventos críticos y deduplicación; conciliar ecommerce/leads con sistemas de negocio.
- Crear grupos de marca/no marca e intención con reglas transparentes.
- Exportar y preservar datos agregados necesarios para comparaciones históricas/cohortes.
- Definir controles de privacidad, acceso, retención y QA de releases.

### Días 36–60: cohortes, paneles y alertas

- Analizar cohorts orgánicas por plantilla, intención, mercado y nuevo/recurrente.
- Construir vistas ejecutiva y operativa con métricas distintas por etapa.
- Crear alertas P0/P1 técnicas y P2/P3 de negocio con responsables y baselines.
- Revisar la latencia de conversión y la madurez de cohortes.

### Días 61–90: experimentación

- Seleccionar una intervención SEO acotada con muestra elegible y mecanismo explícito.
- Diseñar control, pre-registro, MDE, guardrails y regla de decisión.
- Ejecutar y documentar efecto, incertidumbre, contaminación y aprendizaje.
- Si la aleatorización no es viable, usar diseño cuasiexperimental con supuestos revisables y lenguaje prudente.

## 13. Checklist ejecutivo

- [ ] Cada métrica importante tiene definición, fuente, denominador y propietario.
- [ ] Separé GSC visibilidad/clics, analítica de sesiones y ventas/leads de la fuente de negocio.
- [ ] La implementación mide acciones confirmadas y evita duplicados.
- [ ] Conversión, key event y microconversión están etiquetados y usados de forma coherente.
- [ ] Consentimiento, modelado, privacidad, acceso y retención se consideran en el análisis.
- [ ] La atribución declara modelo, ventana, canal e identidad; no se presenta como causalidad.
- [ ] Las cohortes especifican unidad, fecha de entrada, retorno, ventana, censura y muestra.
- [ ] Las pruebas fijan hipótesis, unidad, control, resultado primario, guardrails y regla de parada.
- [ ] Los análisis antes/después incluyen comparación estacional y eventos concurrentes.
- [ ] Alertas distinguen emergencia técnica, cambio de visibilidad, valor de negocio y anomalía.
- [ ] Cada alerta tiene responsable y acción de respuesta.
- [ ] El panel muestra magnitud e incertidumbre, y no solo una variación porcentual.

## 14. Conclusión

La analítica SEO madura no intenta fabricar una cifra única para “el valor de SEO”. Construye una cadena auditable de mediciones: qué apareció en búsqueda, qué visitas llegaron, qué acciones se observaron, qué crédito asignó el modelo y qué efecto adicional puede sostener un diseño causal.

La atribución es útil para describir recorridos y planificar; cohortes muestran la calidad posterior de la adquisición; alertas reducen tiempo de detección; experimentos e inferencia cuasiexperimental ayudan a estimar incrementalidad. Su valor depende de instrumentación correcta, comparación justa, hipótesis previa y reporte honesto de incertidumbre. Si el diseño no separa causa y contexto, la conclusión correcta es “observamos un cambio compatible con la intervención”, no “demostramos que SEO lo causó”.

## 15. Bibliografía anotada

### Google Search y Analytics

1. **Google Search Central — [Using Search Console and Google Analytics data for SEO](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console).** Diferencias y usos complementarios de GSC y GA; incluye discrepancias entre clicks y sessions.
2. **Search Console Help — [About Search Console data](https://support.google.com/webmasters/answer/96568).** Retrasos, consultas anonimizadas, filas limitadas, zona horaria y límites de los informes.
3. **Search Console Help — [Performance report: advanced filtering and comparison](https://support.google.com/webmasters/answer/17011165).** Filtros y efecto de consultas/URL en totales.
4. **Search Console Help — [Evaluating performance changes](https://support.google.com/webmasters/answer/17010961).** La propia guía advierte que es difícil atribuir cambios a una edición concreta y sugiere comparar con periodos similares y contexto.
5. **Search Central — [Debug Google Search traffic drops](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops).** Diagnóstico segmentado, comparación estacional y superficies de búsqueda.
6. **Google Analytics Help — [Conversions vs. key events](https://support.google.com/analytics/answer/13965727).** Distinción actual entre key events para análisis de comportamiento y conversions asociadas a reporting/optimización publicitaria.
7. **Google Analytics Help — [Get started with attribution](https://support.google.com/analytics/answer/10596866).** Modelos y límites de asignación de crédito en informes de atribución.
8. **Google Analytics Help — [Cohort exploration](https://support.google.com/analytics/answer/9670133).** Criterios, granularidad, cálculo y límites de exploración de cohortes GA4.
9. **Google Analytics Help — [Configuration limits](https://support.google.com/analytics/answer/12229528).** Límites de exploración, muestreo y retención de datos configurables.
10. **Google Analytics for Developers — [Set up events](https://developers.google.com/analytics/devguides/collection/ga4/events).** Tipos de eventos, medición recomendada y depuración.
11. **Google Analytics for Developers — [Recommended events](https://developers.google.com/analytics/devguides/collection/ga4/reference/recommended-events).** Nombres y parámetros de evento estándar.
12. **Google Analytics for Developers — [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce).** Eventos y parámetros ecommerce, compra, moneda, valor y reembolso.
13. **Google Analytics Help — [Analytics Insights](https://support.google.com/analytics/answer/9443595).** Insights automáticos y reglas/anomalías personalizadas con notificaciones.
14. **Google Analytics Help — [Anomaly detection](https://support.google.com/analytics/answer/9517187).** Descripción del enfoque de detección de anomalías de Analytics Intelligence.
15. **Google Tag Platform — [Set up consent mode](https://developers.google.com/tag-platform/security/guides/consent).** Señales de consentimiento y comportamiento de etiquetas; no reemplaza el mecanismo de consentimiento del sitio.

### Métodos de inferencia causal

16. **Brodersen et al., Annals of Applied Statistics (2015), [Inferring causal impact using Bayesian structural time-series models](https://research.google/pubs/inferring-causal-impact-using-bayesian-structural-time-series-models/).** Método de serie temporal/control sintético y discusión de fortalezas y límites cuando no hay experimento aleatorizado.
17. **Callaway, Goodman-Bacon y Sant’Anna, American Economic Review, [Difference-in-Differences with a Continuous Treatment](https://www.aeaweb.org/articles?id=10.1257/aer.20240137).** Evidencia econométrica reciente sobre supuestos de tendencias paralelas e interpretación de estimadores.
18. **Roth et al., Journal of Econometrics, [What’s Trending in Difference-in-Differences?](https://www.sciencedirect.com/science/article/pii/S0304407623001318).** Síntesis de métodos DiD, múltiples periodos y problemas de pre-trends.

### Revisión futura

Antes de implantar esta guía, volver a comprobar la documentación vigente de GA4, Search Console, políticas de consentimiento, exportaciones, límites y definiciones de atribución. Cambios de producto pueden alterar nombres, ventanas, retención o disponibilidad de informes. En cada informe causal, incluir diseño, unidad, periodo, población, intervención, métrica primaria, supuestos, incertidumbre y limitaciones.
