---
title: "SEO para noticias y publishers"
subtitle: "Estudio de investigación, estrategia editorial y guía operativa"
version: "1.0"
research_cutoff: "2026-10-18"
language: "es"
scope: "Medios informativos, publishers, revistas, medios locales y publicaciones digitales"
---

# SEO para noticias y publishers

## Estudio de investigación, estrategia editorial y guía operativa

**Fecha de corte: 18 de octubre de 2026.** Esta guía reúne documentación oficial de Google y Microsoft, investigación reciente sobre hábitos informativos y efectos de la búsqueda con IA, y prácticas editoriales y técnicas para medios. Distingue entre elegibilidad, rastreo, visibilidad, tráfico, relación con la audiencia e ingresos. No promete inclusión en Top Stories, Google News, Discover ni una posición determinada.

> **Tesis:** el SEO de un publisher es la coordinación entre periodismo que aporte información original y fiable, páginas rastreables y transparentes, distribución técnica correcta y un modelo de audiencia que no dependa de una sola plataforma. El éxito no se mide solo en clics: también importan lectores recurrentes, suscripciones, registro, confianza y valor editorial.

## 1. Alcance y método

### 1.1 Qué cubre

El estudio cubre Google Search y sus superficies de noticias (Top Stories, pestaña News), Google News, Discover, Bing/Microsoft Start y experiencias de búsqueda generativa que citan fuentes periodísticas. Incluye SEO de breaking news, periodismo de servicio, análisis y evergreen; arquitectura de secciones, páginas de artículo, noticias en vivo, paywall, sindicación, imágenes, sitemaps y medición.

El término **publisher** se usa para medios, redacciones, revistas y organizaciones que publican contenido informativo. Una página corporativa con una sección de blog no se convierte automáticamente en medio periodístico; tiene que ser útil y transparente para sus lectores y cumplir las políticas correspondientes a cada superficie.

### 1.2 Jerarquía de evidencia

| Nivel | Tipo | Qué permite afirmar | Qué no permite afirmar |
|---|---|---|---|
| **A — Fuente primaria** | Política, documentación o herramienta del buscador | Requisitos declarados, controles y métricas disponibles | Pesos algorítmicos completos o garantía de impresiones |
| **B — Investigación revisada / experimento** | Estudio académico publicado con método | Efectos observados bajo la muestra y condiciones del estudio | Generalización automática a todos los países, medios y consultas |
| **C — Preprint / estudio temprano** | Investigación en curso, aún sin revisión formal | Hipótesis nuevas que pueden orientar pruebas | Consenso científico ni causalidad universal |
| **D — Datos de industria / encuesta** | Panel de usuarios, proveedores de analítica o encuesta a líderes | Tendencias o percepciones de las muestras estudiadas | Métricas propias de cada publisher o predicción de su futuro |
| **E — Práctica editorial/técnica** | Recomendación de operación, UX o estándares profesionales | Un proceso más claro y verificable | Un factor oficial de ranking sin evidencia específica |

La documentación oficial describe lo que cada producto publica, no revela sus sistemas internos. El *Digital News Report* del Reuters Institute se basa en una encuesta online internacional de audiencias y no debe leerse como analítica de visitas. Los experimentos sobre AI Search pueden estimar efectos causales dentro de su configuración, pero la interfaz, los mercados, los temas y el comportamiento de producto cambian.

### 1.3 Límites

- Google News, Discover, Search y Microsoft Start son superficies distintas. No comparten elegibilidad, métricas ni necesariamente el mismo sistema de selección.
- Un artículo indexado no necesariamente aparecerá en News o Top Stories. Google tampoco garantiza que cada URL de un sitemap se publique o se clasifique.
- Una caída de tráfico coincidente con un cambio de producto no demuestra que ese cambio sea la única causa. Temporada, noticia, competencia, algoritmo, marca y medición también influyen.
- Las métricas de terceros dependen de sus paneles, sitios incluidos, mercados y definiciones. No son equivalentes a Search Console ni a la analítica del medio.
- Las reglas editoriales y de privacidad, copyright, protección de menores, contenido electoral y publicidad nativa varían por jurisdicción. Esta guía no sustituye asesoramiento legal ni la política editorial de la redacción.

## 2. Superficies y embudo de descubrimiento

Un publisher debe distinguir estos espacios:

| Superficie | Tipo de experiencia | Qué puede aportar | Cómo medirla |
|---|---|---|---|
| **Google Search: resultados web** | Búsqueda activa; noticia, fuente primaria, análisis o guía | Clics directos por consulta y página | Search Console, filtro Web y Search type cuando corresponda |
| **Top Stories / funciones de noticias** | Bloques de cobertura para consultas con intención informativa | Visibilidad temporal y clics a artículos | Search Console y revisión de SERP; no equivale a ranking web estable |
| **Pestaña News en Search** | Resultados en la pestaña News de Google Search | Clics e impresiones de búsqueda de noticias | Search Console, informe Performance de Search y tipo News |
| **Google News app / news.google.com** | Agregación y personalización de noticias | Lectores de producto News, posibles retornos o suscripciones | Informe News Performance de Search Console |
| **Google Discover** | Feed personalizado por intereses, no búsqueda explícita | Alcance incremental, a veces con picos de tráfico | Informe Discover en Search Console |
| **Bing News / Microsoft Start / Edge** | Noticias dentro de superficies Microsoft | Descubrimiento en otro ecosistema de búsqueda y distribución | Bing Webmaster Tools y analítica propia; Bing PubHub está retirado |
| **Chatbots y respuestas con IA** | Resumen conversacional con posibles citas | Mención, cita, referral o uso de contenido sin visita | Referencias etiquetadas cuando existan, logs y pruebas de consultas; datos incompletos |

El embudo puede ser: **descubrimiento → rastreo → indexación → consideración/elegibilidad → selección en la superficie → impresión → clic → lectura/retorno → registro/suscripción/ingreso**. Una mejora en el primer paso no garantiza los siguientes. Una mención sin clic no es visita; una visita sin lectura no es atención; una impresión no es ingreso.

## 3. Hallazgos principales

### 3.1 Google ya no requiere “aprobación” manual para Google News

Google declara que los publishers no necesitan enviar su sitio para ser elegibles en las superficies de Google News: sus sistemas descubren contenido mediante tecnologías de Search y consideran el cumplimiento de políticas. Desde marzo de 2025, Google News genera automáticamente las páginas de publicaciones y dejó de usar las secciones, feeds RSS y ubicaciones web configuradas anteriormente en Publisher Center para crear esas páginas. Publisher Center sigue teniendo funciones específicas para productos como News Showcase y Reader Revenue Manager; no es el CMS ni una palanca general de ranking.

**Consecuencia:** no gastes recursos buscando una “aprobación Google News” como requisito técnico. Enfócate en crawlabilidad, políticas, transparencia, páginas de artículo y cobertura informativa original. Usa Publisher Center solo para funciones actuales que realmente necesites.

### 3.2 El sitemap de noticias ayuda a descubrir, no fuerza inclusión

El sitemap de noticias comunica artículos recientes y metadatos a Google. Google permite integrarlo en el sitemap general o mantener uno separado; la opción separada puede facilitar el seguimiento. La documentación recomienda incluir solo URLs creadas en los últimos dos días en la parte específica de News y actualizar el archivo conforme se publican artículos, en lugar de generar un nuevo sitemap por cada cambio. Google advierte que rastrea el sitemap de noticias con la misma frecuencia que el resto del sitio.

El sitemap no sustituye enlaces internos, políticas, indexación ni elegibilidad. Tampoco sirve para cambiar la fecha real de un artículo o relanzar artificialmente contenido antiguo.

### 3.3 NewsArticle schema es descriptivo, no requisito para Top Stories

Google afirma que no hay requisito de datos estructurados para ser elegible en Top Stories. `Article`, `NewsArticle` o `BlogPosting` pueden ayudar a Google a comprender título, autor, imagen y fechas, y quizá presentar mejor esos datos; no crean una posición ni hacen que una noticia sea noticia. El marcado tiene que corresponder al contenido visible y a la realidad editorial.

### 3.4 Transparencia editorial es una política explícita de Google News

Google News pide fechas y firmas claras; información sobre autores, publicación y publisher; información sobre la compañía o red detrás del medio; y datos de contacto. También exige que publicidad, patrocinio, afiliación o apoyo material se distingan claramente del periodismo independiente y que el contenido promocional no exceda el editorial en esas páginas.

Estas reglas sirven tanto para elegibilidad como para confianza de lectores. No deben reducirse a añadir un autor ficticio, una página vacía de “Sobre nosotros” o una fecha marcada sin historial de cambios.

### 3.5 URLs permanentes y páginas de artículo legibles son fundamentales

La guía técnica de Google News pide URLs únicas y permanentes para cada artículo. Las páginas de secciones deben mantener URLs estables, y los artículos tienen que poder descubrirse mediante enlaces HTML; los títulos y las horas de publicación deben ser reconocibles y el cuerpo no debe depender de JavaScript para hacerse visible al crawler. Si un medio cambia CMS, dominio o rutas, debe planificar redirecciones, canonicals y mapeo de URLs.

Una URL estable también preserva enlaces, compartidos, referencias, historial de correcciones y acumulación de señales. No republicar cada actualización de una historia bajo una URL nueva.

### 3.6 Discover no es una fuente de tráfico predecible

Discover se personaliza según actividad e intereses; puede mostrar contenido antiguo cuando siga siendo relevante. No requiere que el usuario escriba una consulta, y no es un feed que el publisher pueda programar. Google recomienda contenido oportuno, bien narrado o con perspectivas propias, títulos que describan el contenido, evitar clickbait/sensacionalismo y usar imágenes grandes y pertinentes. Las impresiones pueden fluctuar sin que exista una acción manual ni una causa única identificable.

### 3.7 Bing PubHub está retirado

La página oficial de directrices de Bing PubHub muestra un aviso explícito: **Bing PubHub está retirado**. Por tanto, las guías antiguas que recomiendan enviar la publicación a PubHub están desactualizadas. Los publishers deben verificar su sitio en Bing Webmaster Tools, mantener sitemaps y enlazado correctos, usar IndexNow para notificar URLs nuevas o modificadas a motores participantes y monitorizar Bing Search. IndexNow avisa de cambios; no garantiza rastreo, indexación, distribución en News ni posición.

### 3.8 Las plataformas ya superan a las propiedades directas en el consumo global de noticias

El *Digital News Report 2026* del Reuters Institute señala que, por primera vez en su serie, redes sociales y redes de vídeo son la fuente de noticias más usada globalmente (54% de las audiencias encuestadas); el uso de webs y apps de medios disminuyó 12 puntos porcentuales desde 2020 en esa encuesta. Es un indicador de hábitos declarados en mercados internacionales, no una caída de tráfico de cada publisher ni una cuota de mercado. Justifica diversificar audiencia y formatos, no abandonar el SEO.

### 3.9 La evidencia sobre AI Search y referencias está creciendo, pero no cierra el debate

Un experimento de campo preregistrado de agosto de 2026, con 1.100 participantes con datos de comportamiento en Google Search, encontró que asignar a participantes a un modo AI Search redujo la proporción que hizo clic en sitios de noticias en la configuración estudiada. El artículo está en arXiv y todavía no debe presentarse como consenso revisado por pares; su experimento de producto no predice cada noticia, consulta, país o versión futura.

La conclusión editorial prudente es medir tanto las referencias como la presencia de la marca y la captación directa. No hay una optimización que fuerce al usuario a salir de la plataforma, ni una razón para declarar muerto el SEO de noticias.

## 4. Política editorial y confianza

### 4.1 Identidad y responsabilidad visibles

Cada artículo debe permitir responder quién informa, quién publica, qué organización está detrás, cómo contactar con el medio y qué política rige el trabajo. Mantén páginas útiles y actualizadas de:

- quiénes somos, propiedad y financiación;
- autores, editores y colaboradores con perfiles veraces;
- metodología, estándares editoriales y política de correcciones;
- contacto de redacción, denuncias/rectificaciones y derecho de respuesta;
- patrocinio, contenido comercial, afiliación y conflictos de interés;
- uso de IA editorial y controles humanos cuando sea relevante;
- políticas de privacidad, cookies y tratamiento de datos.

La firma puede ser de autor, equipo, agencia o corresponsal según el caso, siempre descrita con precisión. No atribuyas autoría a un periodista que no participó.

### 4.2 Fechas, actualizaciones y correcciones

Muestra fecha y hora de publicación cuando sean relevantes, con zona horaria clara para eventos en vivo. Si el artículo cambia sustancialmente, indica fecha de actualización y qué se modificó; conserva `datePublished` como fecha original y usa `dateModified` para un cambio real. Una corrección importante debe ser visible y explicar el error sin borrar la historia del cambio. Cambiar una fecha sin una modificación sustantiva puede confundir tanto a personas como a sistemas.

En historias que evolucionan, separa el hecho nuevo de la información previa, contextualiza incertidumbres y evita que un título antiguo contradiga el estado actual.

### 4.3 Titulares y previews

El titular debe describir la noticia y su núcleo informativo, no prometer algo que el artículo no contiene. Evita titulares ambiguos, truncados, clickbait, exageración, exceso de palabras clave y cambios de titular que alteren el hecho. El `<title>`, H1, metadatos sociales y el título visible deberían guardar coherencia; puede haber diferencias editoriales justificadas, pero no cuatro versiones contradictorias.

En Discover, Google pide evitar títulos e imágenes que exageren, oculten contexto esencial o manipulen morbo/indignación para elevar interacción. El CTR es útil para diagnosticar, pero no justifica sacrificar precisión.

### 4.4 Originalidad, atribución y sindicación

Distingue el reporteo original de notas de agencia, resúmenes, traducciones, comunicados, contenido licenciado y republicaciones. Atribuye fuentes, enlaces, imágenes y documentos de forma clara. Para sindicación de un artículo completo, coordina con socios si el contenido republicado debe bloquearse de indexación para ayudar a identificar la versión original, según la guía de Google News. No publiques varias URLs idénticas en el mismo dominio sin necesidad editorial.

La cobertura incremental (reescritura de una nota de prensa o de otra noticia con cambios mínimos) no reemplaza acceso a fuentes, reporteo, verificación, datos propios, contexto y valor para el lector.

### 4.5 Imágenes y media

Usa imágenes directamente relacionadas con la historia, con permisos y créditos correctos. Para Discover, Google recomienda imágenes grandes de al menos 1.200 píxeles de ancho, más de 300.000 píxeles totales y `max-image-preview:large` (o AMP) para optar a una vista previa grande; no garantiza aparecer. No uses logos genéricos como sustituto de imagen editorial. Verifica encuadre, contexto, pies de foto, autoría y etiquetas de contenido sintético/manipulado cuando la política editorial lo requiera.

Para video, audio, galerías y gráficos, crea una página accesible con texto contextual, transcripción o descripción cuando sea útil, y metadatos que correspondan al contenido realmente visible. No dependas de que Google interprete un video o un post social sin la explicación periodística que necesita el lector.

## 5. Arquitectura y SEO técnico de un publisher

### 5.1 Secciones permanentes y enlaces rastreables

Organiza el sitio en secciones estables por área editorial, tema, región y formato. Google News dice que URLs cambiantes de secciones dificultan identificar lo nuevo. Enlaza artículos desde portada, secciones, temas relacionados y contenidos explicativos mediante `<a href>` accesibles; no dependas exclusivamente de botones, enlaces dentro de JavaScript o imágenes sin texto.

Una estructura útil podría ser:

```text
/pais/tema/ (sección o landing editorial estable)
/pais/tema/slug-del-articulo/ (URL permanente)
/autor/nombre/ (perfil de autor)
/temas/entidad-o-tema/ (archivo curado cuando aporta valor)
```

Es solo un patrón ilustrativo. El valor está en la estabilidad, la claridad y el enlazado, no en que las palabras de la URL coincidan con una plantilla concreta.

### 5.2 Breaking news y live blogs

Para coberturas en vivo, usa una URL permanente para la página principal y mantén el contenido legible, ordenado cronológicamente y con hora por actualización. Diferencia el comienzo del live blog de actualizaciones posteriores. Enlaza a reportajes, antecedentes, fuentes primarias y otras piezas de la cobertura. Evita crear un nuevo artículo/URL por cada breve actualización si puede consolidarse en una cobertura continua.

Si una actualización cambia sustancialmente la noticia, considera publicar una pieza nueva cuando haya una necesidad editorial nueva; enlaza a la cobertura anterior y deja clara la relación. No reescribas el mismo artículo como si cada edición fuera un nuevo hecho.

### 5.3 Canonical, duplicados y archivos

Establece canonical coherente para versiones de impresión, parámetros, páginas móviles, AMP heredado si sigue en uso, republicaciones y formatos de newsletter. No canonicalices una noticia a una home o categoría genérica. Los archivos de etiquetas/autor deben ser indexables solo si ofrecen una página útil, única y mantenida; un archivo que repite títulos y snippets sin organización editorial puede no merecer indexación.

Evita páginas vacías por filtros, búsquedas internas indexables de combinaciones infinitas, etiquetas redundantes o URLs por paginación que pierdan enlaces. Mantén una política consistente para paginación de secciones, agregados de autor y temas.

### 5.4 Migraciones y cambios de CMS

Antes de cambiar dominio, rutas, sistema de paywall o CMS:

1. Exporta URLs y métricas por artículo.
2. Diseña un mapa 1:1 de redirecciones hacia la pieza equivalente.
3. Conserva fechas originales, autor, canonical y datos estructurados.
4. Prueba renderizado, robots, sitemap, enlaces internos, imágenes y acceso del crawler en staging.
5. Mantén artículo y archivo indexables en una sola URL preferida.
6. Monitoriza errores, indexación, clics, Discover y News por tipo de página.

Una migración puede alterar el rendimiento aunque el texto sea el mismo. No combines cambio de CMS, rediseño, fusión editorial, paywall y cambio de URL sin aislar riesgos cuando se pueda.

## 6. Google News, News sitemap y datos estructurados

### 6.1 Google News: elegibilidad y descubrimiento

Google descubre noticias algorítmicamente y no requiere una presentación manual del dominio para que sea considerado. Cumple las políticas de News, comprueba rastreo/indexación con Search Console y asegura que cada artículo tenga URL dedicada, permanente y legible. El cumplimiento habilita consideración; no garantiza aparecer o mantener visibilidad.

### 6.2 News sitemap

Usa un News sitemap para artículos recientes si es operativo para el medio:

- mantenerlo actualizado al publicar;
- incluir artículos de los últimos dos días en los campos de News;
- retirar artículos antiguos de la sección News o quitarles los metadatos News, manteniendo sus URLs en el sitemap general si siguen activas;
- usar nombre de publicación e idioma tal como define la especificación;
- no generar un sitemap por cada artículo;
- enviar el sitemap en Search Console y revisar errores.

Si el CMS publica a gran escala, automatiza validación XML y compara el sitemap con el inventario de artículos publicados. Un sitemap que enumera URLs con `noindex`, 404, redirects, canonical a otra página o páginas vacías crea señales contradictorias.

### 6.3 `NewsArticle` / `Article` structured data

Puede ser útil para declarar `headline`, `image`, `datePublished`, `dateModified` y `author`. El marcado debe describir el artículo visible, usar URLs de imagen accesibles, personas reales y fechas verdaderas. No es requisito de elegibilidad para Top Stories y no garantiza rich results.

Comprueba con Rich Results Test y el informe de datos estructurados de Search Console. Inspecciona HTML servido y renderizado: si la entidad/cuerpo solo aparece tras una interacción no reproducible, la implementación es frágil.

### 6.4 News sitemap versus sitemap general

El sitemap general comunica URLs canónicas que el medio quiere que se descubran; el sitemap News añade metadatos de publicaciones recientes. No sustituyen enlaces internos ni un inventario editorial sólido. IndexNow puede notificar a Bing y otros motores participantes de cambios; no debe confundirse con el News sitemap de Google ni con una garantía de indexación.

## 7. Discover: oportunidad con variabilidad

### 7.1 Qué hacer

- Publicar contenido oportuno, bien contado o con perspectiva original.
- Usar título y preview fieles a lo que el lector encontrará.
- Añadir una imagen editorial pertinente, de calidad y suficientemente grande.
- Implementar `max-image-preview:large` si el medio permite previews amplias.
- Mantener author, publisher, `datePublished`/`dateModified` y contenido identificables.
- Revisar políticas específicas de Discover y manual actions.
- Analizar resultados por tema, audiencia, dispositivo, fecha y tipo de artículo.

### 7.2 Qué no prometer

No hay formato que garantice Discover, calendario que se pueda forzar ni una frecuencia que asegure impresiones. Un artículo evergreen puede aparecer porque es pertinente para una persona, aunque sea antiguo. Un pico y una caída no prueban por sí solos una penalización. Evita convertir toda noticia en una pieza de alto impacto emocional solo porque la superficie es personalizada.

### 7.3 Diagnóstico

Si Discover cae, revisa a la vez:

- errores técnicos, indexabilidad, canonical y cambios de plantilla;
- tema, competencia, estacionalidad, agotamiento de interés y volumen de publicación;
- título, imagen y calidad del preview;
- políticas, acciones manuales y problemas de seguridad;
- mezcla de fuentes y distribución de impresiones por landing;
- datos de Analytics y Search Console, separando la superficie Discover de Search.

Las métricas de Search Console describen rendimiento registrado por Google, no lectores únicos ni suscripciones.

## 8. Suscripciones, paywall y monetización

### 8.1 Paywall sin cloaking accidental

Si parte del contenido está limitado a suscriptores, deja claro al lector qué es gratuito y qué requiere acceso. Google recomienda marcar correctamente contenido paywalled para distinguirlo de cloaking; usa la implementación y propiedades estructuradas vigentes, como `isAccessibleForFree` y selectores de contenido, según corresponda. No presentes una versión completa a Googlebot y una página completamente distinta a los usuarios sin indicación de paywall.

Evalúa el modelo: meter, freemium, registro, suscripción dura, membresía o licencia B2B. El tratamiento SEO depende de la política de acceso, valor que se muestra antes del registro, indexación permitida y política de cookies. Un paywall no es solo una configuración técnica: afecta adquisición, conversión, retención, experiencia y acuerdos con plataformas.

### 8.2 Qué medir

- impresiones/clics a artículos gratuitos y paywalled;
- usuario anónimo → registro → suscriptor;
- conversión por temática, autor, formato y canal;
- churn y retención de cohortes adquiridas por búsqueda;
- ingreso por visita y valor de lector, junto con coste de adquisición;
- páginas consumidas antes de suscribirse y páginas de retorno;
- relación entre referral, newsletter, push, tráfico directo y suscripción.

No maximices sesiones si la estrategia necesita suscripciones de lectores fieles. Evalúa la contribución de búsqueda a audiencias propias y el efecto en retención.

### 8.3 Publicidad, afiliación y contenido comercial

Distingue contenido editorial, patrocinado, afiliado, sindicado y generado por usuario. Google News prohíbe presentar contenido patrocinado como editorial independiente sin disclosure claro. Los artículos comerciales deben tener utilidad y transparencia; no camufles páginas de terceros dentro de secciones editoriales para aprovechar la reputación del medio.

## 9. SEO editorial: antes y después de publicar

### 9.1 Antes de publicar

1. Identifica la necesidad informativa: qué sucedió, dónde, cuándo y qué pregunta intenta resolver el lector.
2. Comprueba si ya existe una URL canónica del tema: artículo inicial, actualización, live blog, guía o explicador.
3. Decide formato por función editorial, no por keyword: breaking, análisis, preguntas y respuestas, cronología, mapa, visualización o entrevista.
4. Verifica datos, citas, documentos, imágenes, derechos, contexto y riesgo de daño.
5. Prepara headline, descripción, imagen social, firma, hora, sección, canonical y enlaces relacionados.
6. Identifica enlaces a cobertura anterior y fuentes primarias para que el artículo no quede aislado.

### 9.2 Al publicar

- Publica en URL dedicada y estable con respuesta HTTP correcta.
- Asegura que H1, title, cuerpo y fechas aparezcan en HTML legible.
- Incluye enlace desde sección/portada y sitemap.
- Envío de News sitemap e IndexNow donde corresponda.
- Verifica imagen, `og:image`, meta robots, canonical, `NewsArticle` y paywall.
- Comprueba móvil, anuncios/intersticiales, velocidad y accesibilidad.

### 9.3 Después de publicar

- Actualiza si hay información nueva; conserva historial y hora.
- Corrige errores de forma visible y conserva la URL.
- Añade contexto y enlaces de seguimiento.
- Revisa Search Console: indexación, Search, News y Discover por separado.
- Analiza consultas, titulares que atraen clics, permanencia/lectura, newsletters y conversión.
- Consolida artículos solapados solo con una justificación editorial y un mapa de redirección claro.

## 10. Bing y distribución en Microsoft

Bing PubHub ya no es un proceso activo de admisión. La página oficial muestra que está retirado, por lo que un publisher debe ignorar tutoriales antiguos que digan “envía tu sitio a PubHub”.

El trabajo vigente consiste en:

- verificar la propiedad en Bing Webmaster Tools;
- mantener sitemap general correcto y monitorizar cobertura;
- enviar URLs nuevas/actualizadas por IndexNow cuando el CMS lo permita;
- asegurar páginas de artículo rastreables, enlaces HTML y metadatos claros;
- medir clicks e impresiones en Bing Webmaster Tools;
- observar si el contenido aparece en superficies actuales de Microsoft, sin inferir que un protocolo de notificación asegure presencia en Microsoft Start.

IndexNow transmite que una URL cambió a motores participantes. No informa al publisher de una selección editorial, no obliga a indexar y no sustituye sitemap.

## 11. Visibilidad en respuestas generativas y relación con crawlers

Los publishers deben separar acceso de búsqueda, uso para entrenamiento, peticiones del usuario y licencias. En OpenAI, Anthropic y Perplexity existen controles diferentes para algunos de esos casos. La decisión debe adoptarse con equipos editorial, legal, distribución, producto y tecnología: acceso puede aumentar posibilidades de descubrimiento, pero no garantiza atribución, referral o compensación.

Para Search generativo de Google, aplica controles de Google Search y sus reglas específicas disponibles; Google-Extended trata usos de ciertos productos de IA y no debe confundirse con aparecer en Search. Para ChatGPT Search, comprueba `OAI-SearchBot`; para Perplexity, `PerplexityBot`; para Anthropic, `Claude-SearchBot`; revisa roles actuales y políticas antes de cambiar robots o WAF.

Registra cada bot en logs, verifica IPs con datos oficiales y separa visitas humanas de crawls automatizados. Revisa volumen, caché, coste y derechos. No bloquees Googlebot de Search por querer limitar un crawler de entrenamiento si el negocio necesita mantener Search, salvo decisión expresa con análisis de consecuencias.

Las prácticas generales de claridad editorial (quién, qué, cuándo, fuentes, fecha, imágenes y documentos accesibles) ayudan a lectores y sistemas a entender contenido; no hay evidencia de un formato de texto universal que garantice citas de IA.

## 12. Medición: audiencia, visibilidad y sostenibilidad

### 12.1 Informes de Search Console

Google publica informes separados:

- **Search Performance:** resultados de Google Search; el tipo News permite revisar la pestaña News de Search.
- **News Performance:** datos de `news.google.com` y apps Google News para Android/iOS. No incluye la pestaña News de Search.
- **Discover Performance:** impresiones y clics en Discover, separado de búsqueda web.

Lee impresiones, clics, CTR, posición media, páginas, país, dispositivo y fecha junto al contexto de publicación. No sumes los informes sin revisar qué superficies se solapan y qué define cada reporte.

### 12.2 Tablero editorial

| Objetivo | Métricas sugeridas |
|---|---|
| Descubrimiento | URLs rastreadas/indexadas; tiempo de publicación a primera impresión; páginas no descubiertas |
| Presencia en Search | Clics/impresiones por tipo de consulta, artículo, sección, país y dispositivo |
| News / Top Stories | Informe News Performance; Search type News; cobertura manual documentada por consultas de prueba |
| Discover | Impresiones, clics, CTR, páginas, tema, formato, imagen y cohortes temporales |
| Calidad de audiencia | Lectura/atención cuando se mida bien, retorno, consumo de más de una pieza, newsletter/push opt-in |
| Suscripción | Registro, conversión, churn, retención, LTV, contribución asistida de búsqueda |
| Ingresos | Ingreso por sesión, yield publicitario, suscripción, afiliación claramente marcada, licencias |
| Resiliencia | Proporción de audiencia directa/propia frente a búsqueda, redes, agregadores y chatbots |
| Integridad | Correcciones, rectificaciones, fallos de enlaces, quejas, acciones manuales y contenido duplicado |

Define eventos y atribución con equipos de analítica. La sesión de Analytics puede no capturar el valor de una impresión, una cita o una búsqueda de marca posterior; tampoco atribuyas a SEO un aumento que viene de una noticia viral o campaña editorial.

### 12.3 Análisis de consultas y artículos

Agrupa por tipo informativo: breaking, servicio, directo, análisis, opinión, explicador, evergreen, local, deportes, finanzas, cultura. Compara ciclo de vida, no solo el día de publicación: el breaking puede tener pico de horas; un explicador quizá crezca después y genere lectores recurrentes.

Para cada artículo, revisa:

- impresiones y clics por query;
- cómo el buscador muestra el titular y la imagen;
- consultas relevantes no cubiertas o mal atendidas;
- CTR con posición y superficie comparables;
- lectores nuevos vs recurrentes;
- conversión, retorno y engagement;
- actualizaciones, referencias, enlaces externos y sindicación.

No uses un dashboard para incentivar volumen y velocidad a costa de verificación. La métrica debe servir a la misión editorial, no reemplazarla.

## 13. Riesgos y afirmaciones que conviene descartar

| Afirmación | Evaluación | Alternativa prudente |
|---|---|---|
| “Hay que solicitar aprobación de Google News.” | Desactualizado: Google descubre contenido y no requiere envío para elegibilidad; Publisher Center cambió. | Verificar indexación, políticas, transparencia y estructura. |
| “NewsArticle schema es obligatorio para Top Stories.” | Google dice explícitamente que no hay requisito de marcado. | Usarlo como ayuda de comprensión y datos, bien validado. |
| “Enviar sitemap de noticias fuerza inclusión.” | El sitemap ayuda a descubrir URLs recientes; no garantiza rastreo, indexación o ranking. | Mantenerlo correcto y enlazado, con páginas técnicamente sólidas. |
| “Discover es una fuente estable si publicas a diario.” | Personalización y demanda causan alta variabilidad; no hay frecuencia garantizada. | Diversificar, medir y concentrarse en historias útiles, oportunas y fieles. |
| “Cambiar la fecha hace que Google trate el artículo como nuevo.” | Puede inducir a error; no equivale a una actualización sustantiva. | Conservar fecha original y declarar cambios reales. |
| “Republicar cada noticia de agencia crea más URLs de SEO.” | Duplica contenido y puede ocultar el original o crear canibalización. | Añadir valor editorial o manejar sindicación con socios y canonical/noindex según el caso. |
| “Google Search manda un número fijo de clics a cada medio.” | No existe cuota garantizada; el referral varía por consulta, producto y marca. | Medir tendencias en el sitio propio y diversificar audiencia. |
| “Una cita de IA equivale a una visita o licencia.” | No; puede no producir clic, y crawling no constituye por sí mismo licencia. | Separar cita, referral, contrato, uso de contenido e ingresos. |
| “El SEO de noticias está muerto.” | La distribución cambia, pero las búsquedas y superficies de noticias siguen generando descubrimiento. | Tratar Search como un canal importante, no exclusivo. |
| “El SEO de noticias consiste en palabras clave.” | Es insuficiente; contexto, relevancia, frescura, autoridad y utilidad importan en un entorno editorial. | Priorizar reporteo, estructura, transparencia, técnica y experiencia del lector. |

## 14. Hoja de ruta de 90 días

No garantiza un crecimiento determinado. Ordena la auditoría y permite aprender.

### Días 1–15: inventario y línea base

- Inventariar secciones, plantillas, artículos, autores, archivos, tipos de contenido y paywall.
- Separar métricas de Search, News, Discover, Bing, social, email y tráfico directo.
- Revisar News sitemap, sitemap general, robots, canonicals, datos estructurados y logs.
- Capturar fuentes de tráfico, conversión, lectores recurrentes y suscripciones por sección.

### Días 16–35: eliminar bloqueos y ambigüedad

- Corregir URLs no permanentes, contenido no legible, enlaces inaccesibles y fechas ambiguas.
- Reforzar páginas de transparencia, perfiles, contacto, política editorial y disclosures.
- Validar noticias de pago, canonical/sindicación y estado de bots con partes interesadas.
- Retirar instructivos antiguos de PubHub o “aprobación Google News” del proceso operativo.

### Días 36–60: mejorar experiencia editorial y distribución

- Mejorar enlaces entre secciones, piezas de contexto, reportajes y actualizaciones en vivo.
- Definir estándares de headlines, fechas, correcciones, imágenes y marcados.
- Implementar News sitemap y proceso de IndexNow si encaja con tecnología y objetivos.
- Crear un grupo piloto para Discover/newsletter/registro, sin cambios masivos simultáneos.

### Días 61–90: medir valor y diversificar

- Comparar por tipo de artículo, tema, canal y cohortes.
- Estudiar referral de IA, crawls, costes, citas, atribución y decisiones de licencia/bloqueo.
- Analizar lectores que vuelven y convierten, no solo pageviews.
- Priorizar mejoras con efecto demostrable; documentar nulls y efectos adversos.
- Establecer un calendario trimestral de revisión de políticas de plataformas y datos.

## 15. Checklist ejecutiva

- [ ] El medio distingue Google Search, Google News, Top Stories, Discover y Bing/Microsoft.
- [ ] No depende de una aprobación manual obsoleta ni del Bing PubHub retirado.
- [ ] Las secciones tienen URLs estables y artículos en URLs únicas y permanentes.
- [ ] Artículos y titulares son legibles por crawler en HTML y enlazados con `<a href>`.
- [ ] Las fechas y firmas son claras, correctas y consistentes entre página y schema.
- [ ] Hay información real de autores, publisher, compañía, contacto y políticas.
- [ ] Patrocinios, afiliación, sindicación y material comercial se identifican.
- [ ] Correcciones y cambios sustantivos se explican sin reescribir la historia de publicación.
- [ ] News sitemap sigue el límite temporal y se actualiza correctamente.
- [ ] `NewsArticle`/`Article` se usa como marcado descriptivo, no como garantía de Top Stories.
- [ ] Descubrimiento, paywall y acceso de crawler reflejan la política editorial/legal elegida.
- [ ] Imágenes de Discover son relevantes, grandes y fieles; no se usa clickbait.
- [ ] Sindicación y duplicados tienen reglas documentadas con socios.
- [ ] Search, News, Discover, Bing, referrals de IA y tráfico propio se reportan por separado.
- [ ] El éxito incluye lectores recurrentes, conversión, confianza e ingresos, además de clics.
- [ ] La redacción no recibe incentivos de volumen que debiliten verificación o correcciones.

## 16. Conclusión

El SEO para noticias y publishers no es una solicitud de inclusión ni un plugin. Es una capacidad editorial y técnica: publicar información original y verificable; hacer identificables el artículo, el autor y la organización; conservar URLs y fechas fiables; facilitar el rastreo; y distribuir el trabajo en distintas superficies sin perder relación directa con los lectores.

Google News no necesita una admisión manual, Google no exige `NewsArticle` para Top Stories y un sitemap no compra visibilidad. Discover es variable, Bing PubHub está retirado y los sistemas de IA pueden cambiar la relación entre exposición y referral. Lo defendible es medir cada canal con su propia definición, proteger la integridad editorial, tomar decisiones informadas sobre contenido y crawlers, y construir una audiencia que el publisher pueda servir directamente.

## 17. Bibliografía anotada

### Documentación de Google

1. **Google News Publisher Center — [Help Google News discover your web-crawled content](https://support.google.com/news/publisher-center/answer/9606634).** Elegibilidad automática, cumplimiento de políticas y diagnóstico de rastreo/indexación.
2. **Google News Publisher Center — [Google News policies](https://support.google.com/news/publisher-center/answer/6204050).** Transparencia, patrocinio y políticas específicas de News.
3. **Google News Publisher Center — [Technical guidelines](https://support.google.com/news/publisher-center/answer/9606708).** URLs, secciones, HTML, titulares y fechas.
4. **Google News Publisher Center — [Automatic publication pages](https://support.google.com/news/publisher-center/answer/15898024).** Retiro del flujo manual de páginas en Google News desde marzo de 2025.
5. **Google Search Central — [News sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap).** Actualización, ventana de dos días y límites.
6. **Google Search Central — [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article).** Uso y aclaración de que el marcado no es requisito para Top Stories.
7. **Google Search Central — [Discover and your website](https://developers.google.com/search/docs/appearance/google-discover).** Recomendaciones de imagen, headlines, contenido y políticas de Discover.
8. **Google Search Central — [Flexible sampling / paywalled content](https://developers.google.com/search/docs/appearance/flexible-sampling).** Marcado de contenido de suscripción y distinción respecto a cloaking.
9. **Google Search Console Help — [News Performance report](https://support.google.com/news/publisher-center/answer/10252664).** Alcance de Google News app y news.google.com frente a la pestaña News de Search.
10. **Google News Publisher Center — [Content that must be blocked from Google News](https://support.google.com/news/publisher-center/answer/9520026).** Casos de contenido republicado y originalidad/sindicación.
11. **Google Search Central — [Google News ranking](https://support.google.com/news/publisher-center/answer/9607025).** Descripción publicada de factores generales de selección y ranking, sin pesos.

### Documentación de Microsoft y otras plataformas

12. **Bing Webmaster Tools — [PubHub publisher guidelines](https://www.bing.com/webmasters/help/pubhub-publisher-guidelines-32ce5239).** Página oficial con aviso de retiro de Bing PubHub; las directrices históricas no son un proceso vigente de envío.
13. **Bing Webmaster Blog — [Sitemaps in AI-powered search](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/).** Sitemap e IndexNow como mecanismos de cobertura/notificación, no garantía de aparición.
14. **Bing Webmaster Tools — [AI Performance public preview](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/).** Métricas de citas para propiedades en superficies de Microsoft con límites propios.
15. **Google News Publisher Center — [Google News Showcase](https://support.google.com/news/publisher-center/answer/10018888).** Programa separado de licencias/curación para publishers participantes, con disponibilidad por mercado.

### Investigación de audiencia e impacto de IA

16. **Reuters Institute — [Digital News Report 2026: executive summary](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary).** Hábitos informativos online en mercados internacionales; encuesta de audiencias, no analítica de tráfico web.
17. **Reuters Institute — [Spain, Digital News Report 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/spain).** Contexto español; alcance de marca de noticias declarado por encuestados y datos de mercado.
18. **Reuters Institute — [Journalism, media, and technology trends and predictions 2026](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026).** Encuesta de líderes editoriales sobre prioridades y riesgos; expectativas de ejecutivos, no proyección causal.
19. **Wang et al. (arXiv, agosto 2026), [AI in Search Reduces Publisher Referrals Without Improving User Experience](https://arxiv.org/abs/2608.18352).** Experimento preregistrado con 1.100 datos de comportamiento; resultados de la interfaz y muestra probadas, aún preprint.
20. **Society of Professional Journalists — [SPJ Code of Ethics](https://www.spj.org/ethicscode.asp).** Marco profesional sobre verificación, independencia, transparencia, daño y correcciones; estándar ético, no documento SEO.

### Actualización futura

Al revisar este estudio, comprueba el estado de Publisher Center, PubHub, Search Console, IndexNow y las políticas de IA; actualiza ejemplos por país e idioma; y registra los cambios en comportamiento de audiencia con metodología. Para cualquier recomendación que afecte al paywall o a crawlers, incluye a dirección editorial, producto, tecnología y asesoría legal en la decisión.
