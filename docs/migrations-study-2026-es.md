---
title: "Migraciones SEO y cambios de plataforma"
subtitle: "Estudio de investigación y manual operativo para rediseños, cambios de CMS, dominios y arquitectura"
version: "1.0"
research_cutoff: "2026-10-18"
language: "es"
scope: "Sitios web, publishers, ecommerce, servicios y organizaciones con tráfico orgánico"
---

# Migraciones SEO y cambios de plataforma

## Estudio de investigación y manual operativo

**Fecha de corte: 18 de octubre de 2026.** Una migración puede cambiar el dominio, las rutas, el CMS, la infraestructura, las plantillas, el contenido o varias de estas piezas a la vez. El término se usa a menudo para todo el proyecto, pero cada modificación altera señales distintas y exige controles distintos.

Este estudio convierte la documentación oficial de Google y Microsoft en un proceso de preparación, lanzamiento y recuperación. Incluye cambios de dominio y URL, HTTPS, alojamiento y CDN, CMS, rediseños, arquitectura, internacionalización, consolidación de sitios y cambios de plataforma de comercio electrónico. Distingue entre migración técnica, migración de contenido y transformación de producto. No promete que el tráfico o las posiciones permanezcan iguales: ningún checklist puede garantizarlo.

## 1. Alcance, método y límites

### 1.1 Qué significa “migración”

En este documento, una migración es un cambio que puede afectar la forma en que una página se identifica, se sirve, se enlaza, se representa o se mide. Puede ser:

| Clase | Ejemplos | ¿Cambian las URL visibles? | Riesgo SEO típico |
|---|---|---:|---|
| Infraestructura | Hosting, servidor, CDN, DNS, WAF | No necesariamente | Errores HTTP, latencia, bloqueos de bots, caída de disponibilidad |
| Protocolo y host | HTTP a HTTPS, www a no-www, dominio nuevo, subdominio | Sí | Pérdida de continuidad de URLs, redirecciones incompletas, certificados |
| Rutas y arquitectura | Reorganización de directorios, taxonomía, slugs | Sí | Mapeo incompleto, enlaces rotos, cambio de intención o jerarquía |
| Plataforma/CMS | WordPress a headless, Magento a Shopify, CMS propietario | A veces | Cambios en renderizado, metadatos, canonicals, paginación, facetas, contenido |
| Diseño y plantillas | Rediseño, navegación, componentes, renderizado JavaScript | Puede que no | Contenido omitido, enlaces no rastreables, títulos o datos estructurados alterados |
| Contenido | Recorte, reescritura, actualización, consolidación o eliminación | Puede que no | Pérdida de relevancia, cobertura temática, enlaces o utilidad |
| Consolidación/cambio de marca | Fusión de dominios, adquisición, separación de productos | Sí o no | Redirecciones sin equivalencia, pérdida de contexto, señales mezcladas |
| Medición y consentimiento | Nueva analítica, CMP, etiquetas, arquitectura de eventos | No | Datos no comparables que ocultan fallos o simulan caídas |

Google distingue explícitamente entre mover un sitio con cambios de URL y cambiar el alojamiento manteniendo las URL. También recomienda, siempre que sea razonable, no combinar el cambio de dominio, CMS y diseño en un único paso. Una migración sin cambio de URL sigue siendo un cambio de SEO si rompe rastreo, respuesta, contenido, indexabilidad o medición.

### 1.2 Jerarquía de evidencia

1. **Documentación primaria vigente:** Google Search Central, Search Console Help y documentación oficial de Bing Webmaster Tools.
2. **Principios técnicos comprobables:** semántica HTTP, códigos de estado, DNS, HTML servido, enlaces, sitemaps, analítica y logs.
3. **Experiencia de implementación:** útil para organizar inventarios y pruebas, pero no prueba que una técnica produzca una ganancia de ranking.
4. **Estimaciones de impacto:** dependen de la web, la escala, el historial, el mercado, la estacionalidad y la calidad del mapeo. Se presentan como rangos de riesgo, nunca como resultado garantizado.

### 1.3 Límites

- Los buscadores procesan URL por URL y no existe un plazo universal para completar la transición. Google indica que un sitio mediano puede tardar varias semanas o más; los sitios grandes pueden tardar más.
- Una variación temporal de visibilidad puede ocurrir aunque la migración esté correctamente implementada. Una caída que continúa o empeora exige diagnóstico; no debe normalizarse sin evidencia.
- Un rediseño puede mejorar UX y negocio sin mejorar rankings. También puede mantener posiciones mientras empeora conversión, medición o accesibilidad.
- Los sistemas de búsqueda no exponen todos sus datos ni garantizan indexación, transferencia de señales, ranking o tráfico.

## 2. Hallazgos ejecutivos

1. **Clasificar el cambio antes de planificarlo.** Cambio de infraestructura sin cambio de URL y cambio de URL son rutas distintas en la guía de Google y en la implementación.
2. **El mapa URL antigua → destino es el artefacto central cuando cambian URLs.** Se construye con sitemaps, CMS, analítica, Search Console, backlinks y logs, no solo con un crawl del sitio actual.
3. **Una redirección debe conservar la intención y el contenido equivalente.** Enviar todo a la home crea una mala experiencia y puede ser interpretado como soft 404. Si no hay sustituto razonable, 404/410 puede ser la respuesta correcta.
4. **Los redirects permanentes deben ser directos y mantenerse.** Google recomienda 301/308 del lado servidor cuando es posible, evitar cadenas y conservar redirecciones al menos un año; desde la perspectiva de las personas, puede ser conveniente mantenerlas indefinidamente.
5. **La nueva web debe estar lista antes de cambiar el tráfico.** El entorno de pruebas tiene que protegerse; el sitio de producción nuevo debe estar rastreable cuando se hace el cambio y no conservar accidentalmente `noindex` o bloqueos de robots.
6. **Cambiar varias capas simultáneamente hace más difícil atribuir problemas.** Aislar dominio, CMS, diseño y reescritura editorial reduce ambigüedad y facilita una reversión parcial.
7. **Las redirecciones no sustituyen la migración interna.** Menús, enlaces contextuales, canonicals, hreflang, sitemap, feeds, recursos y campañas deben apuntar a destinos finales.
8. **La medición debe tener una línea base comparable.** Guardar datos por URL, plantilla, directorio, dispositivo y país permite detectar qué segmento perdió cobertura o rendimiento.
9. **Change of Address se usa solo en cambios elegibles de dominio/subdominio.** No corresponde a HTTP→HTTPS, www↔no-www ni cambio de rutas dentro del mismo dominio. La guía oficial actualizada en agosto de 2026 pide tramitar todas las variantes verificadas del dominio antiguo.
10. **La migración se completa cuando el usuario, los rastreadores y la organización llegan al mismo destino correcto.** Rankings por sí solos no prueban que redirecciones, conversiones, indexación y medición funcionen.

## 3. Marco para decidir el tipo y el momento

### 3.1 Matriz de alcance

Antes de aprobar calendario o presupuesto, anotar para cada dimensión si cambia, cómo se comprobará y quién responde:

| Dimensión | Antes | Después | Cambio | Responsable | Control de salida |
|---|---|---|---|---|---|
| Dominio / hostname |  |  | Sí/No |  | DNS, TLS, variantes, Change of Address si aplica |
| Protocolo |  |  | Sí/No |  | HTTP→HTTPS, certificado y una sola versión canónica |
| URL/ruta |  |  | Sí/No |  | Mapa, respuesta y destino por URL antigua |
| CMS/servidor |  |  | Sí/No |  | HTML, headers, renderizado, estabilidad |
| Navegación/arquitectura |  |  | Sí/No |  | Enlaces, niveles, breadcrumbs, páginas huérfanas |
| Contenido y metadatos |  |  | Sí/No |  | Cobertura, títulos, canonicals, robots y datos estructurados |
| Internacionalización |  |  | Sí/No |  | Hreflang recíproco, idiomas, geotargeting relevante |
| Analítica/consentimiento |  |  | Sí/No |  | Eventos, atribución, zona horaria, consentimiento y QA |
| Negocio/operación |  |  | Sí/No |  | Formularios, checkout, login, suscripción, feeds y API |

### 3.2 Riesgo: impacto × probabilidad × capacidad de detección

Prioriza controles por el coste de que el fallo ocurra y por lo tarde que se detectaría. Los cambios con más riesgo suelen combinar: gran proporción de URLs con demanda o backlinks, equivalencias editoriales débiles, reglas de redirección generadas con comodines, dependencia de JavaScript para contenido principal, producción de millones de parámetros, baja capacidad de monitorización y falta de acceso al dominio anterior.

Clasifica URLs por valor y sensibilidad, al menos en:

- Entradas con más clics, impresiones y conversiones orgánicas.
- URL con enlaces externos o tráfico de referencia relevante.
- Productos, categorías, artículos, páginas de servicio y páginas locales que generan ingresos o leads.
- Páginas estacionales y contenidos con ciclos de demanda previsibles.
- Páginas legales, de soporte, login, checkout y recursos descargables que no deben romperse aunque no tengan tráfico orgánico.

No asumas que las URL con poco tráfico actual son prescindibles: pueden tener enlaces valiosos, ser estacionales o estar afectadas por una incidencia previa.

## 4. Inventario de partida y línea base

### 4.1 Fuentes del inventario

Ninguna fuente contiene todas las URL existentes o relevantes. Combina:

1. Exportación completa del CMS y base de datos, incluidas páginas publicadas, archivadas y entradas con metadatos.
2. Sitemaps actuales y cualquier sitemap histórico disponible.
3. Crawl de HTML, enlaces, canonicals, status codes, robots, hreflang, metadatos, paginación e imágenes.
4. Search Console: rendimiento por página, consultas, países y dispositivos; informe de indexación; sitemaps; enlaces externos; inspección de muestras.
5. Analítica: landing pages orgánicas, conversión, ingresos/leads y eventos, con comparaciones interanuales y estacionales.
6. Logs de servidor/CDN: URL visitadas por personas y bots, códigos, latencia y errores. Verifica identidad del bot cuando se use para decisiones sensibles.
7. Backlinks: URL enlazada, dominio de referencia, contexto y visitas de referral. Herramientas externas ofrecen estimaciones y no son el registro completo.
8. Datos comerciales: catálogo y variantes, inventario, redirecciones de campañas, enlaces de app, feeds, PDFs y contenido servido por sistemas externos.

Guardar fecha, zona horaria, filtros y método de exportación. Search Console tiene límites de filas y su informe no es un censo completo de URL; por eso debe cruzarse con otras fuentes.

### 4.2 Campos del fichero maestro de URLs

Como mínimo:

| Campo | Uso |
|---|---|
| `old_url` | URL absoluta original normalizada, sin perder parámetros relevantes |
| `new_url` | Destino exacto, URL sin cambio o vacío si se elimina sin sustituto |
| `old_status` / `new_status` | Estado HTTP observado y esperado |
| `template` / `content_type` | Categoría, producto, artículo, autor, landing, PDF, etc. |
| `indexability` / `canonical` | Estado, directiva y canonical de cada versión |
| `clicks`, `impressions`, `conversions`, `revenue` | Línea base de búsqueda y negocio |
| `external_links`, `referral_visits` | Valor y prioridad de outreach |
| `mapping_reason` | Equivalencia, consolidación, retirada, sin reemplazo |
| `priority` / `owner` | Orden de QA y responsable |
| `test_result` / `last_checked` | Evidencia de producción y estado del control |

El fichero debe detectar duplicados, destinos no existentes, bucles, cadenas, redirecciones a otro idioma o país por defecto y destinos de intención diferente. Mantén separadas las decisiones editoriales (“se consolida”) de las reglas técnicas (“301 a X”).

### 4.3 Línea base comparable

Conservar datos de 8–16 semanas como mínimo cuando el ciclo lo permita y comparar también con el mismo periodo del año anterior en negocios estacionales. Registrar:

- clics, impresiones, CTR y posición media por tipo de búsqueda, URL y consulta;
- sesiones/usuarios orgánicos, landing page, engagement definido por el negocio, leads, transacciones e ingresos;
- cobertura: páginas válidas, excluidas, rastreadas no indexadas, errores y canonicals elegidos;
- rendimiento por plantilla: disponibilidad, LCP/INP/CLS de campo cuando haya volumen, errores 4xx/5xx y latencia;
- medios propios: marca, direct, email, referrals, suscripciones, app y campañas.

No mezclar en un gráfico “sesiones orgánicas” de analítica con clics de Search Console como si fueran la misma métrica. Consentimiento, modelado, zona horaria, definición de canal, atribución y cambios de etiquetas alteran los números.

## 5. Estrategia de URLs y equivalencias

### 5.1 Reglas de mapeo

- Si existe una página sucesora con contenido/intención equivalentes, redirigir la URL antigua directamente a esa sucesora.
- Si varias páginas se integran realmente en una página nueva que cubre su función, se pueden redirigir a esa página consolidada.
- Si no hay sustituto razonable y el contenido se elimina de forma permanente, devolver `404` o `410`; no inventar equivalencias.
- No redirigir grandes grupos de URL a la home o a una categoría genérica solo para evitar 404. Google advierte que redirecciones irrelevantes pueden confundir y tratarse como soft 404.
- Evitar redirecciones condicionales por user-agent, país o referente que den al rastreador otro destino que al usuario.
- Elegir una única versión canónica de dominio, protocolo, host, mayúsculas/minúsculas y slash final; consolidar variantes con una redirección permanente coherente.
- Asegurar que el destino responde `200`, es indexable cuando debe serlo, ofrece contenido principal y apunta a sí mismo con canonical.

### 5.2 Cuándo usar redirección y cuándo no

| Situación | Respuesta recomendada |
|---|---|
| URL cambiada permanentemente, contenido equivalente | 301 o 308 del lado servidor al destino final |
| URL temporalmente desplazada | 302/307 si la página original debe seguir siendo la versión preferida |
| Página retirada, sin reemplazo | 404 o 410 y enlaces internos actualizados |
| Contenido consolidado de verdad | Redirección a la nueva página consolidada, con equivalencia comprobable |
| URL duplicada que se conserva funcionalmente | Canonical coherente; no usarlo como sustituto de una mudanza permanente |
| Dominio viejo que no se controla | Resolver propiedad/hosting/acceso antes del lanzamiento; sin él no se pueden servir redirects fiables |

El 301/308 es una señal fuerte de canonicalización y Google indica que redirecciones permanentes no producen pérdida de PageRank. Esto no equivale a garantizar que cada consulta, ranking, usuario o conversión se transfiera uno a uno.

### 5.3 Parámetros, facetas y paginación

Una plataforma nueva puede cambiar de forma explosiva el número de URL indexables si expone filtros, orden, búsqueda interna, variantes, tracking o sesiones como URL rastreables. Antes de lanzar:

- define la política de indexación de cada familia de parámetros;
- conserva la URL indexable de categorías y productos que ya cumplen una función orgánica;
- evita que filtros sin demanda o sin contenido diferenciado generen miles de páginas indexables;
- confirma canonical, enlaces internos, sitemap y robots de forma coordinada;
- no bloquees con robots.txt páginas que necesiten ser rastreadas para leer un `noindex` o canonical;
- comprueba cómo representa la plataforma páginas siguientes, filtros y estados vacíos.

### 5.4 Internacionalización

Al mover hostnames, subdirectorios o dominios de país, actualiza `hreflang` con URL completas nuevas, códigos correctos y referencias recíprocas. Confirma que cada alternante responde y se canoniza a sí mismo. Evita redirecciones automáticas por IP o idioma que impidan elegir otra versión. Si se retiran mercados o idiomas, documenta su destino y continuidad de servicio; no mandes todas las regiones a una versión que no corresponde.

## 6. Cambio de dominio, host o protocolo

### 6.1 Dominio o subdominio

Checklist específico:

1. Verifica propiedad del dominio viejo y nuevo en Search Console y en Bing Webmaster Tools.
2. Conserva todas las variantes de Search Console que correspondan: HTTP/HTTPS, www/no-www y subdominios usados.
3. Configura TLS y DNS para el dominio nuevo; mantén el dominio antiguo operativo para responder con las redirecciones.
4. Implementa redirecciones URL por URL o con reglas demostrablemente correctas, sin eliminar rutas que no coinciden.
5. Envía la herramienta **Cambio de dirección** de Search Console para movimientos elegibles entre dominios/subdominios. No aplica a cambio de protocolo, www/no-www en el mismo dominio o rutas dentro del mismo dominio.
6. Según la guía de Google actualizada en agosto de 2026, tramita solicitudes para todas las variantes verificadas del dominio antiguo, incluso subdominios y versiones www/no-www no activas, hacia el dominio nuevo correspondiente.
7. Añade sitemap nuevo, actualiza canonicals/enlaces/hreflang y monitoriza ambas propiedades.
8. Mantén las redirecciones al menos un año; considera su continuidad indefinida para visitantes, enlaces antiguos y servicios externos.

La herramienta Cambio de dirección comunica la mudanza y ayuda a procesarla; no reemplaza las redirecciones ni implementa el sitio nuevo por sí misma.

### 6.2 HTTP a HTTPS

- instala y valida certificados, cadena de confianza, renovaciones, subdominios y recursos;
- redirige HTTP a HTTPS en una sola etapa, conservando path y parámetros útiles;
- actualiza canonical, sitemap, enlaces internos, hreflang, feeds y referencias de recursos;
- elimina contenido mixto y valida callbacks, APIs y dominios de terceros;
- no uses Cambio de dirección, pues protocolo no es un cambio de dominio elegible.

### 6.3 WWW/no-WWW, mayúsculas y slash

Selecciona una convención estable y aplícala en una regla única. Prueba combinaciones de protocolo, host, mayúsculas, slash, query string y paths codificados. Evita que la normalización en CDN, aplicación y CMS genere cadena de varias etapas.

## 7. Cambios de hosting, servidor, CDN y DNS sin cambiar URLs

La guía de Google para hosting se aplica cuando la URL visible no cambia. Su proceso: preparar y probar el nuevo entorno, cambiar DNS, observar el tráfico antiguo y nuevo, y apagar el entorno anterior cuando se confirme que usuarios y Googlebot llegan correctamente.

### Antes del cambio

- hacer pruebas desde redes y regiones distintas, también IPv4/IPv6 si se usa;
- revisar DNS TTL con antelación y planificar la propagación; TTL bajo ayuda a acortar cachés, pero no permite controlar todos los resolvers;
- probar certificados, redirecciones, headers, compresión, caché, páginas 404/5xx, contenido y recursos críticos;
- revisar WAF, rate limit, bot management, CDN y reglas de geobloqueo para que no desafíen ni bloqueen rastreadores legítimos;
- mantener Search Console verification, analítica, CMP, sitemap, robots y archivos estáticos;
- disponer de capacidad suficiente: Google puede rastrear el nuevo entorno más de lo habitual durante una mudanza.

### Durante y después

- confirmar resolución DNS desde varias ubicaciones y proveedores;
- comparar logs del origen viejo y nuevo; verificar códigos reales con peticiones y renderizado;
- observar 5xx, timeouts, latencia, errores TLS, robots, páginas en blanco y recursos bloqueados;
- mantener el origen anterior mientras aún sirva peticiones legítimas o permita comparar;
- detenerlo solo cuando se compruebe que usuarios y bots relevantes reciben contenido correcto.

## 8. Cambio de CMS, ecommerce o arquitectura de renderizado

Una plataforma puede generar HTML distinto aunque las URL no cambien. La paridad debe comprobarse a nivel de plantilla y datos, no mediante una revisión visual superficial.

### 8.1 Paridad SEO de plantillas

Comparar en old vs staging/new:

| Elemento | Verificación |
|---|---|
| Estado HTTP | Páginas activas 200; retiradas 404/410; sin errores ni soft 404 |
| Indexación | `robots.txt`, meta robots, `X-Robots-Tag`, login y acceso al contenido |
| Canonical | URL absoluta correcta, sin dominio de staging, parámetros no deseados ni canonical cruzado accidental |
| Título y descripción | Contenido y unicidad esperada; no campos vacíos o variables literales |
| Encabezados y texto principal | Se conserva tema, especificaciones, disponibilidad, autoría, cuerpo y enlaces clave |
| Enlazado interno | Navegación renderizada como enlaces HTML y destinos finales válidos |
| Datos estructurados | JSON válido, datos visibles que coinciden con página y entidad correcta |
| Hreflang | Tags y sitemap usan dominios/paths nuevos y reciprocalidad válida |
| Sitemap | Solo URL canónicas, indexables y con respuesta final válida |
| Robots/recursos | Googlebot y Bingbot pueden acceder al contenido y los recursos necesarios |
| Renderizado | Contenido principal presente y usable en HTML servido/renderizado; sin dependencia rota de JS |
| Media | Imágenes, vídeos, PDFs y descargas mantienen URL o tienen mapa/redirección |
| UX/negocio | Búsqueda, filtros, carrito, checkout, formularios, login y consentimiento funcionan |

### 8.2 Problemas frecuentes al cambiar CMS

- campos de SEO migrados a campos equivocados o que el CMS ignora;
- slugs con caracteres/acentos, codificación o normalización distinta;
- títulos repetidos por plantillas, breadcrumbs o sufijos duplicados;
- páginas que responden 200 con error, contenido vacío o texto de carga;
- JavaScript que oculta cuerpo, enlaces o metadata hasta una interacción;
- imágenes y PDFs que siguen con rutas antiguas sin redirección;
- staging indexado, producción con `noindex`, o `robots.txt` bloqueando toda la web;
- datos de inventario, precios, disponibilidad, autores o fechas desincronizados;
- paginación y filtros que cambian de patrones y multiplican URLs;
- etiquetas analíticas duplicadas, perdidas o bloqueadas por consentimiento.

### 8.3 Contenido y diseño

Un rediseño puede modificar el texto visible, orden, entidades, enlaces internos y propuesta de la página. Una auditoría de “paridad” debe distinguir:

- **Paridad técnica:** status, indexabilidad, canonical, sitemap, renderizado.
- **Paridad informativa:** tema, respuestas, atributos, entidades, evidencias y contexto.
- **Paridad de navegación:** rutas de descubrimiento, navegación, categorías, breadcrumbs y enlaces contextuales.
- **Paridad de conversión:** acciones y eventos que conectan tráfico orgánico con el objetivo de negocio.

Si se desea cambiar el contenido, documentar qué se retira, qué se conserva, qué se combina y por qué. No trasladar literalmente contenido obsoleto solo para preservar URL, ni reescribir a la vez todas las páginas prioritarias durante una mudanza de dominio si es posible separar esos cambios.

## 9. Plan de preparación, lanzamiento y recuperación

### Fase A — Descubrimiento y gobierno (T−8 a T−4 semanas)

1. Nombrar responsable de decisión, SEO, producto, ingeniería, infraestructura, analítica, contenido, QA y soporte.
2. Definir alcance exacto, dependencias, mercados, dominios y criterios de éxito/rollback.
3. Crear inventario de URL y baseline, clasificar por plantilla, valor orgánico y conversión.
4. Decidir si conviene separar dominio, CMS, diseño y limpieza editorial en lanzamientos distintos.
5. Obtener acceso al antiguo dominio, DNS, hosting, CMS, Search Console, Bing Webmaster y analítica.
6. Publicar un mapa aprobado, con dueño y explicación para excepciones; congelar nuevas reglas no revisadas cerca del lanzamiento.

### Fase B — Construcción y pruebas (T−4 a T−1)

1. Preparar staging no indexable mediante controles de acceso y/o `noindex`; usar robots.txt como control de rastreo, no como sustituto de autenticación ni de `noindex`.
2. Crawl de staging y comparación automatizada contra old site por plantilla.
3. Probar todas las reglas de redirección con muestras de cada patrón, además de todas las URLs de mayor valor.
4. Confirmar analytics y eventos con orden de datos, consentimiento y atribución probados.
5. Ensayar el despliegue y rollback con infraestructura realista; medir duración, propagación y responsables.
6. Definir tablero de lanzamiento con alertas: errores 5xx, tasa de 404, tráfico orgánico, pagos/leads, eventos y logs de bots.

### Fase C — Go/no-go

No lanzar si cualquiera de estos controles críticos falla:

- no existe un dueño accesible del dominio antiguo o no se puede servir redirección;
- los destinos de páginas prioritarias no existen o son irrelevantes;
- producción nueva contiene bloqueo global no previsto (`noindex`, robots, autenticación, firewall);
- TLS/DNS, checkout, formularios, login o analítica crítica no funcionan;
- sitemap y canonicals apuntan a staging o dominio equivocado;
- no existe un rollback operativo y no hay responsable con capacidad de activarlo.

### Fase D — Lanzamiento

1. Ejecutar en periodo de menor riesgo según ciclos de negocio; evitar días donde no haya soporte técnico/editorial.
2. Si es un hosting sin URL nueva, cambia DNS tras la prueba de paridad. Si cambian URLs, activar redirects y sitio nuevo de forma coordinada.
3. Confirmar en minutos: home, páginas de mayor valor, variantes de dominio, códigos, certificados, `robots.txt`, canonicals, sitemaps, Search Console, Bing y analítica.
4. Verificar que una muestra amplia de URLs antiguas redirige una vez al destino previsto; rastrear la lista completa automáticamente.
5. Actualizar sitemap y enviar el sitemap nuevo. En cambio elegible de dominio, enviar Change of Address en las variantes requeridas.
6. Actualizar enlaces internos, campañas, perfiles, feeds, integraciones y enlaces de propiedad propia.

### Fase E — Estabilización (primeras 72 horas y semanas siguientes)

- **0–2 h:** monitorización técnica continua; comprobar ruta, estado, canonical, robots y conversión en URLs prioritarias.
- **2–24 h:** revisar logs, 5xx, latencia, 404, cadenas, bot access, analítica y checkout/formularios.
- **Días 2–7:** rastrear redirecciones y enlaces, revisar reportes de Search Console, sitemaps e indexación; corregir errores de mapeo.
- **Semanas 2–8+:** observar transferencia de impresiones/clics entre conjuntos old/new, cobertura por plantilla, consultas, conversiones y resultados de servidor. El plazo varía por tamaño y frecuencia de rastreo.
- Mantener la redirección y medición en el dominio antiguo durante el periodo de transición; las notificaciones de sitemaps y herramientas ayudan a descubrir, pero no fuerzan indexación.

### Fase F — Retrospectiva

Documentar: qué cambió, qué falló, cuánto tardó en resolverse, páginas afectadas, impacto observado y qué controles habrían detectado antes el problema. Mantener el mapa, las reglas y el checklist como documentación de la arquitectura actual.

## 10. Monitorización y diagnóstico

### 10.1 KPI por nivel

| Nivel | Señales | Pregunta |
|---|---|---|
| Disponibilidad | 5xx, timeouts, TLS, DNS, latencia | ¿La web sirve respuestas estables? |
| Transporte | 3xx, 4xx, bucles, cadenas, destinos | ¿Cada URL antigua llega a su destino correcto? |
| Rastreo | Logs, Crawl Stats, robots, renderizado | ¿Los bots pueden pedir y procesar el nuevo sitio? |
| Indexación | Canonical elegida, sitemaps, páginas indexadas/excluidas | ¿Los motores reconocen las URL nuevas esperadas? |
| Visibilidad | Impresiones, consultas, clics, CTR y posición | ¿La demanda orgánica se transfiere por tipo de página? |
| Negocio | Leads, transacciones, ingresos, suscripciones | ¿La búsqueda genera el resultado esperado? |
| Experiencia | Core Web Vitals de campo, errores UX, búsqueda interna | ¿El usuario completa su tarea? |

### 10.2 Segmentación analítica

En un dominio nuevo, anota el lanzamiento y compara:

- URL antigua frente a su URL nueva por cohortes y páginas prioritarias;
- directorio, plantilla, idioma, dispositivo, país, marca/no marca y tipo de intención;
- clics e impresiones de Search Console, más sesiones y conversiones en analítica;
- semana actual, periodo previo y comparación estacional pertinente;
- tráfico directo/referral para detectar URLs externas o campañas rotas.

No interpretes un descenso en la propiedad antigua aislado: durante un traslado exitoso, lo esperable es que la actividad vieja baje y la nueva crezca gradualmente. Evalúa la suma old+new, la correspondencia y el negocio.

### 10.3 Síntoma → primera hipótesis

| Síntoma | Revisar primero |
|---|---|
| Muchas URL nuevas “Descubiertas, actualmente sin indexar” | Calidad/cobertura, enlaces internos, sitemap, respuesta/duplicación y capacidad de rastreo |
| Nuevo dominio no recibe impresiones y el viejo sigue activo | Redirects, canonical, enlaces, Change of Address aplicable, sitemap y variantes |
| Muchos 404 nuevos | Mapa de URL, slugs, parámetros, codificación y reglas de ruta |
| Sitemap con URL redirigidas o no canónicas | Sitemap de destino, canonicals, CMS y fecha de generación |
| Páginas válidas pero se desploman clics por plantilla | Comparar contenido, intención, title, indexabilidad, navegación, experiencia, consulta y demanda |
| Caída abrupta coincidente con lanzamiento | Robots/noindex, 5xx, DNS/TLS, canonical a staging, JS, WAF, etiquetas y redirecciones |
| Analytics cae pero Search Console no | Consentimiento, tag, canal, atribución, propiedad y huso horario |
| Search Console cae pero sesiones orgánicas se mantienen | Definiciones, canonical/property, tracking de URL, retrasos de reporte y otros motores |

Evita atribuir una caída automáticamente al “sandbox” o a una penalización. Busca evidencia en los datos y compara con actualizaciones, estacionalidad, cambios de SERP, demanda, competidores y problemas técnicos.

## 11. Rollback y recuperación

Un rollback no consiste necesariamente en “volver todo atrás”. Después de que algunas URL hayan sido rastreadas, revertir DNS, canonicals y redirects de forma incoherente puede alargar el problema. El plan debe establecer qué es reversible y qué requiere un nuevo movimiento.

Antes del lanzamiento, especificar:

- qué señales activan rollback (p. ej., pagos fallidos, 5xx sostenidos, bloqueos generalizados, destinos incorrectos a gran escala);
- el umbral y duración necesarios para evitar reaccionar a ruido normal;
- quién decide, quién ejecuta y quién comunica;
- si se restaura la plataforma antigua manteniendo el dominio nuevo o se revierte el DNS;
- qué pasa con formularios, pedidos, inventario, contenido publicado y eventos generados durante la ventana;
- cómo mantener redirects correctos y coherentes para usuarios y motores;
- cómo preservar logs, baseline y evidencia del incidente.

Si el problema afecta solo a una plantilla o patrón, una corrección acotada suele ser preferible a revertir todo el cambio. No prolongar el diagnóstico en producción si la web está caída o un bloqueo global es evidente.

## 12. Migraciones especiales

### 12.1 Rediseño sin cambio de URL

Compara contenido servido, navegación, enlaces, encabezados, datos estructurados, imágenes, metadatos y comportamiento móvil antes y después. Una página puede conservar el path y perder contenido, enlaces internos o una respuesta útil por un cambio de plantilla.

### 12.2 Fusión de dominios y adquisiciones

No todas las URL de una empresa adquirida deben ir a la home del comprador. Construye equivalencias por intención y entidad, preserva páginas útiles, elimina contenido sin equivalente con respuesta adecuada y conserva una capa de contexto para explicar marcas, productos y entidades. Separa la integración legal/comercial de la equivalencia editorial y SEO.

### 12.3 Cambio de marca

Inventaría consultas de marca antigua y nueva, nombres de producto, perfiles sociales, backlinks, emails y campañas. Mantén redirecciones, actualiza referencias propias, conserva metadatos de identidad y monitoriza ambas familias de consultas. El cambio de nombre no convierte automáticamente las consultas de marca antigua en demanda de la nueva.

### 12.4 Ecommerce

Además de URL y producto, comparar IDs, variantes, categorías, stock, precios, moneda, impuestos, disponibilidad, reseñas, feeds, filtros, paginación y marcado de producto. Define el destino cuando un artículo se descataloga: alternativa equivalente, categoría relevante o 404/410, según el caso. La redirección indiscriminada a un producto distinto degrada la experiencia y puede romper relevancia.

### 12.5 Publishers

Preservar autoría, fecha, canonical, paginación y rutas de artículo; distinguir actualización sustantiva de cambio de fecha. Para notas en vivo y archivos, definir si la URL permanece, si se archiva o si se consolida; sostener enlaces internos y sitemaps de noticias conforme a las reglas de la plataforma. La política editorial y de derechos puede limitar la disponibilidad de algunas páginas.

## 13. Afirmaciones que conviene descartar

| Afirmación | Evaluación | Criterio correcto |
|---|---|---|
| “Un 301 conserva el 100 % del tráfico.” | No verificable y falsa como promesa. | Un redirect transmite una señal fuerte de mudanza; rendimiento depende del destino, contenido, demanda y procesamiento. |
| “Pon todos los redirects a la home para no perder autoridad.” | Mala práctica; destinos irrelevantes pueden ser soft 404. | Mapear equivalencias; 404/410 si no existe reemplazo. |
| “Con un plugin de migración ya está todo el SEO.” | El plugin solo implementa parte de la tarea. | Auditar el resultado servido, rutas, indexación, negocio y medición. |
| “El ranking bajará exactamente dos semanas.” | No hay calendario universal. | Medir por URL y segmento; Google indica varias semanas o más según escala y rastreo. |
| “La propiedad de Search Console migra sola.” | La verificación y datos pertenecen a propiedades específicas. | Verificar old/new y todas las variantes necesarias; enviar Change of Address solo si aplica. |
| “Si el staging está bloqueado por robots, producción será segura.” | La configuración puede copiarse por error y el robots no es control de acceso. | QA independiente de producción; staging protegido; lista explícita de directivas a retirar. |
| “No hace falta guardar el dominio viejo.” | Sin control del dominio puede ser imposible redirigir y proteger usuarios. | Mantener propiedad, DNS y servicio de redirección. |
| “El crawl del sitio actual es el inventario completo.” | Ignora URLs no enlazadas, eliminadas, externas o estacionales. | Cruzar CMS, sitemap, logs, analítica, Search Console y backlinks. |
| “Cambio de hosting es neutro para SEO.” | Solo si la experiencia técnica permanece estable. | Comparar disponibilidad, DNS, TLS, latencia, bots, contenido y respuesta. |

## 14. Hoja de ruta de referencia

El calendario depende de escala y organización; la siguiente secuencia no es una duración garantizada.

### Preparación

- Delimitar tipos de cambio, dominios, plataforma y equipos.
- Capturar baseline, inventario, logs, enlaces y conversiones.
- Construir y aprobar el mapa de URL y excepciones.
- Definir modelo de rutas canónicas, sitemaps, redirects, robots, hreflang y medición.
- Crear pruebas automáticas y plan de rollback.

### Validación

- Probar paridad de contenido y metadatos por plantilla.
- Probar reglas completas en lote: status, destino, cadenas, bucles y relevancia.
- Confirmar infraestructura, privacidad/consentimiento y procesos de negocio.
- Simular el lanzamiento y validar el dashboard.

### Lanzamiento

- Ejecutar con soporte y ventana de bajo riesgo.
- Validar técnicamente las URL de más valor.
- Enviar sitemap nuevo y Change of Address si el movimiento es elegible.
- Corregir enlaces propios y campañas, observar logs y conversiones.

### Seguimiento

- Resolver errores críticos inmediatamente.
- Revisar semanalmente el traspaso de indexación y rendimiento por cohorte.
- Actualizar backlinks prioritarios cuando sea viable.
- Mantener redirects y propiedad antigua durante el horizonte requerido.
- Documentar desviaciones, causa y decisión, no solo el resultado final.

## 15. Checklist de salida

### Alcance y gobernanza

- [ ] Se clasificó cada cambio: URL, dominio, infraestructura, CMS, diseño, contenido, analítica.
- [ ] Hay una persona responsable y un canal de escalado durante el lanzamiento.
- [ ] Se capturó baseline orgánico, comercial, técnico y de indexación.
- [ ] Se decidió qué cambios separar para mejorar atribución y reversibilidad.

### Datos y mapeo

- [ ] Inventario combina CMS, crawl, sitemaps, Search Console, analytics, logs y backlinks.
- [ ] Cada URL importante tiene destino aprobado o decisión documentada 404/410.
- [ ] No hay destinos inexistentes, bucles, cadenas evitables o redirecciones genéricas.
- [ ] Imágenes, documentos, vídeos, feed y recursos se incluyeron en el plan.

### Sitio nuevo

- [ ] TLS, DNS, disponibilidad, firewall y capacidad validados.
- [ ] Producción no está bloqueada por `noindex`, robots o autenticación accidental.
- [ ] Canonicals, hreflang, enlaces, breadcrumbs y sitemaps apuntan a URL finales.
- [ ] Plantillas conservan el contenido principal, enlaces y funciones necesarias.
- [ ] Formularios, checkout, login, consentimiento y analítica verificados.

### Lanzamiento y seguimiento

- [ ] Search Console y Bing Webmaster Tools verifican las propiedades pertinentes.
- [ ] Change of Address se envía solo en migración elegible y para todas las variantes requeridas.
- [ ] Sitemaps nuevos enviados; no contienen staging, redirecciones ni noindex.
- [ ] Hay monitoreo de 3xx, 4xx, 5xx, canonical, indexación, logs y conversiones.
- [ ] Existe un rollback practicado con umbrales, responsables y decisiones de DNS/redirects.
- [ ] El dominio antiguo y sus redirecciones permanecerán activos el tiempo necesario.

## 16. Conclusión

Una migración SEO bien gestionada es una transferencia controlada de URL, contenido, accesibilidad, señales y capacidad de medir. La decisión clave no es “qué plugin usar”, sino qué cambia, qué debe conservarse, qué URL sustituye a cuál y cómo se probará en producción.

La guía más sólida es conservadora con los cambios simultáneos y rigurosa con las pruebas: inventario multifuente, mapa explícito, destinos pertinentes, redirects directos, paridad por plantilla, control del entorno, baseline de negocio y seguimiento old+new. Google advierte que puede haber fluctuación temporal y procesamiento de varias semanas o más; la investigación práctica debe detectar antes los errores técnicos y reducir la incertidumbre, no vender una garantía de rankings.

## 17. Fuentes anotadas

### Google Search Central y Search Console

1. **[Site Moves and Migrations](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).** Fuente principal para cambios de URL, mapeo, redirects, variantes de Search Console, Change of Address, sitemaps y monitorización. Actualizada el 20 de agosto de 2026.
2. **[Changing Your Web Hosting and SEO](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes).** Procedimiento para cambiar hosting/CDN sin cambiar URLs, verificación, DNS y cierre del entorno viejo.
3. **[Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects).** Semántica de redirects permanentes/temporales y preferencia por respuestas server-side.
4. **[How to Specify a Canonical URL](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).** Señales de canonicalización y uso de redirects, canonicals y sitemaps.
5. **[Troubleshoot Crawling Errors](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors).** Soft 404, códigos de error, cadenas de redirección y respuesta de rastreo.
6. **[Block Search Indexing with `noindex`](https://developers.google.com/search/docs/crawling-indexing/block-indexing).** Uso del `noindex` y requisito de que el crawler pueda rastrear la directiva.
7. **[Robots.txt Introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro).** Aclara que robots.txt controla rastreo y no garantiza la exclusión del índice.
8. **[Change of Address tool](https://support.google.com/webmasters/answer/9370220).** Condiciones y uso de la herramienta de Search Console para traslados elegibles.
9. **[Search documentation updates](https://developers.google.com/search/updates).** Registro del cambio de junio de 2026 que amplía la guía de Change of Address a variantes de dominio, www/no-www y subdominios.

### Microsoft Bing

10. **[Website Migration with Bing](https://blogs.bing.com/webmaster/2020/12/Website-Migration-with-Bing/).** Orientación oficial de migración y gestión de redirecciones en Bing; contrastar los detalles con la documentación vigente de Bing Webmaster Tools.
11. **[Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a).** Guía general sobre URLs movidas, redirects permanentes y URLs retiradas.
12. **[IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby).** Notificación de URL nuevas o actualizadas a motores participantes; mecanismo de descubrimiento, no garantía de indexación.

### Recursos de implementación complementarios

13. **[Aleyda Solis — SEO migration checklist](https://www.aleydasolis.com/en/seo/seo-migration-checklist/).** Checklist profesional complementario; útil para elaborar operaciones y QA, subordinado a documentación vigente de motores y evidencia del sitio.
14. **[Screaming Frog — Website migration guide](https://www.screamingfrog.co.uk/seo-spider/tutorials/website-migration-guide/).** Flujo de trabajo de rastreo y comparación pre/post; es una guía de implementación de herramienta, no especificación de Google.

### Revisión futura

Antes de reutilizar este estudio para una migración concreta, comprobar la versión actual de la documentación oficial, los límites de Search Console, la herramienta Cambio de dirección y las capacidades de Bing Webmaster Tools. Los requisitos específicos dependen de CMS, CDN, escala, mercados, catálogo, dominio y sistema de medición.
