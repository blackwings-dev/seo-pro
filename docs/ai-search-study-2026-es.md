---
title: "SEO para motores de inteligencia artificial"
subtitle: "Estudio crítico, guía estratégica y protocolo de medición"
version: "1.0"
research_cutoff: "2026-10-18"
language: "es"
scope: "Google AI Search, Bing/Copilot, ChatGPT Search, Perplexity y Claude con búsqueda web"
---

# SEO para motores de inteligencia artificial

## Estudio crítico, guía estratégica y protocolo de medición

**Fecha de corte: 18 de octubre de 2026.** Este documento estudia cómo mejorar la posibilidad de que páginas y marcas sean descubiertas, recuperadas, citadas y elegidas por superficies de búsqueda con IA. Reúne políticas de producto, documentación técnica, investigación académica y estudios de proveedores; distingue lo demostrado de lo plausible y de lo que sigue siendo incierto.

> **Tesis:** la estrategia más defendible consiste en hacer que una fuente sea accesible, pertinente, fiable y útil para una necesidad real; después, medir por separado si los sistemas la recuperan, la citan, envían visitas y generan resultados de negocio. No existe una técnica universal que garantice una mención o una cita en todos los motores de IA.

“SEO para IA”, “GEO” (Generative Engine Optimization), “AEO” (Answer Engine Optimization) y “C-SEO” se usan con significados variables. En esta guía son etiquetas de trabajo, no disciplinas con definiciones consensuadas ni una promesa de que haya un algoritmo único que optimizar.

## 1. Alcance y método

### 1.1 Qué cubre

El foco son las experiencias que buscan o recuperan contenido de la web para responder y, a veces, incluir enlaces: Google AI Overviews y AI Mode; Bing y Microsoft Copilot; ChatGPT Search; Perplexity; y Claude cuando usa búsqueda o recuperación web. Los nombres, interfaces, regiones, modelos y mecanismos cambian. La documentación de cada producto es la fuente para sus controles publicados; no se presupone que una conducta observada en un producto se aplique a todos los demás.

La guía no equipara estas superficies con los modelos que responden únicamente desde conocimiento aprendido, con bases privadas conectadas por una empresa, ni con sistemas internos de recomendación. Tampoco trata el tráfico de IA como sustituto automático del SEO convencional.

### 1.2 Jerarquía de evidencia

| Nivel | Tipo de evidencia | Qué permite concluir | Qué no permite concluir |
|---|---|---|---|
| **A — Primaria y operativa** | Documentación, política o herramienta oficial de una plataforma | Qué declara la plataforma, qué control publica y qué datos ofrece | La fórmula completa del sistema, ni que una recomendación mejore el ranking |
| **B — Experimental revisada** | Artículo revisado por pares o benchmark académico con método descrito | Qué ocurrió bajo las condiciones del experimento | Que el efecto se reproduzca en cualquier sitio, país, motor, consulta o periodo |
| **C — Prepublicación o estudio no revisado** | Preprint, experimento temprano o análisis reproducible aún sin revisión formal | Hipótesis y resultados iniciales que merecen atención | Consenso científico o certeza causal general |
| **D — Observacional/comercial** | Datos de proveedor, panel, logs, análisis de SERP o estudio de mercado | Asociaciones y patrones dentro de una muestra definida | Causalidad, representatividad universal o equivalencia con datos internos de los motores |
| **E — Práctica profesional** | Casos, recomendaciones de consultores y experiencia aplicada | Ideas de diagnóstico y ejecución | Regla oficial del buscador o efecto promedio universal |

La documentación oficial es primaria para explicar el funcionamiento que declara el proveedor, pero no es una auditoría independiente. Los estudios de GEO suelen probar técnicas en bancos de prueba, consultas acotadas o contextos donde el documento ya está disponible para el modelo; eso no siempre evalúa si el motor encontraría esa página en la web abierta. Los preprints más recientes se identifican como tales. La bibliografía incluye tanto fuentes normativas como trabajos con limitaciones.

### 1.3 Límites del estudio

- Los sistemas de recuperación, selección, ranking y generación son parcialmente propietarios y pueden cambiar sin aviso.
- Una respuesta puede variar por consulta, país, idioma, hora, modo, sesión, experimento de producto y modelo. Una comprobación manual es una observación situada, no un ranking estable.
- No se tiene acceso a los registros internos de los motores ni a los datos privados de todos los propietarios web.
- Las métricas de citas de plataformas y proveedores usan definiciones y universos distintos; no se deben sumar como si fueran una medida común.
- Los datos más recientes disponibles al corte pueden estar en vista previa o prepublicación. El lector debe volver a comprobar políticas, documentación y herramientas antes de cambiar controles del sitio.

## 2. Modelo mental: de la página a la respuesta

Para diagnosticar, separa estas etapas:

1. **Acceso:** el sistema puede solicitar la URL; robots, firewall, autenticación, geobloqueos, errores HTTP o renderizado no lo impiden.
2. **Descubrimiento:** conoce la URL mediante enlaces, rastreo, sitemap, feeds, una búsqueda o una petición de usuario.
3. **Procesamiento e indexación:** obtiene contenido legible, interpreta la página, idioma, entidad, fecha y relaciones. Que un bot descargue una página no prueba que se haya indexado.
4. **Recuperación:** ante una consulta, el sistema obtiene páginas, datos u otras fuentes que considera candidatas. Puede reformular la pregunta o ejecutar búsquedas auxiliares.
5. **Selección y generación:** decide qué material usa para redactar. El modelo también puede responder con conocimiento previo, sin recuperar una página propia del dominio.
6. **Cita y presentación:** puede incluir un enlace, una atribución, una mención de marca, una tarjeta o ninguna de ellas. Una mención no equivale a una cita a la web del negocio.
7. **Visita e impacto:** el usuario puede abrir el enlace, recordarlo, buscar la marca después, realizar una conversión o no hacer nada. La cita sola no demuestra ninguna de esas conductas.

Por tanto, “el bot puede rastrear el sitio” es una condición de acceso, no una estrategia completa. “La IA me mencionó” tampoco identifica automáticamente la URL usada ni su papel en la respuesta.

## 3. Hallazgos principales

### 3.1 No hay un único motor de respuesta

Google declara que sus experiencias de IA en Search se apoyan en los sistemas de búsqueda y en páginas indexadas y aptas para aparecer como fragmento. OpenAI, Anthropic y Perplexity publican agentes y controles con funciones distintas. Microsoft ha añadido herramientas propias para observar citas en Copilot y experiencias de Bing. Esas diferencias hacen inadecuada una receta técnica universal.

### 3.2 La base de SEO sigue siendo el punto de partida con mayor respaldo

Para Google, la guía oficial de optimización para funciones de IA indica que no se necesita un marcado especial ni un archivo específico para ser elegible; la página debe cumplir las condiciones normales de Search, estar indexada y ser apta para un fragmento. Esto no prueba que el SEO tradicional por sí solo garantice citas en ChatGPT, Claude o Perplexity, pero sí descarta la idea de que Google exija una nueva capa de “AI SEO” técnica.

### 3.3 Los controles de rastreo tienen objetivos distintos

OpenAI separa `OAI-SearchBot` (búsqueda) de `GPTBot` (posible uso para entrenamiento) y de `ChatGPT-User` (peticiones iniciadas por personas). Anthropic separa `Claude-SearchBot`, `ClaudeBot` y `Claude-User`. Perplexity documenta `PerplexityBot` y `Perplexity-User`. Una decisión de publicación debe considerar objetivo, derechos, licencias, privacidad y modelo de negocio, no copiar un bloque de robots.txt de otra empresa.

Google-Extended regula ciertos usos del contenido para productos de IA; Google afirma que no afecta a la inclusión en Search ni al ranking. Bloquear un agente de entrenamiento no es lo mismo que excluir una página de búsqueda.

### 3.4 El acceso no obliga al motor a citar

Permitir un crawler puede ser necesario para una modalidad concreta, pero no garantiza que se rastree cada URL, se indexe, se recupere en una consulta o se cite. A la inversa, una respuesta puede contener una mención aprendida o un enlace a una página distinta de la que el propietario esperaba.

### 3.5 Las tácticas de “GEO” tienen evidencia desigual

El trabajo inicial de GEO en KDD 2024 reportó mejoras de hasta el 40% en una métrica de visibilidad de su benchmark. Ese porcentaje no significa un 40% más de citas, tráfico, conversiones o visibilidad real universal: la métrica y el contexto experimental limitan su interpretación. En NeurIPS 2025, C-SEO Bench encontró que muchos métodos de reescritura evaluados fueron poco eficaces o dañaron el ranking del documento, mientras que las estrategias SEO tradicionales que elevaban la probabilidad de que la fuente entrara en el contexto fueron más eficaces en ese banco de pruebas.

Dos preprints de octubre de 2026 apuntan a mecanismos importantes, aún provisionales. Uno mide variación y vulnerabilidad de citas tras publicación de contenido en plataformas públicas; el otro, con dos mercados comerciales y cientos de miles de citas, atribuye más variación a qué páginas recupera el motor que a propiedades de página. Son resultados de sus muestras y plataformas, no una fórmula de optimización ni una justificación para sembrar contenido artificial.

### 3.6 La medición está mejorando, pero no es todavía una medida común

Google Search Console ofrece desde agosto de 2026 informes de visibilidad en experiencias generativas de Search y Discover. Bing Webmaster Tools tiene AI Performance en vista previa y ha añadido análisis de temas. Ambas herramientas mejoran la observación de sus propios productos; sus impresiones, consultas de grounding o citas no equivalen por sí solas a posición, cuota global, visitas, calidad editorial o ingresos.

### 3.7 La cita no es el objetivo final de un negocio

El resultado que justifica una inversión puede ser una venta, una solicitud cualificada, una visita, una reducción de soporte o una mejora de confianza. El objetivo debe definirse antes de seleccionar la métrica. Una empresa puede decidir que no le conviene abrir ciertos contenidos a ciertos usos aunque ello reduzca alguna oportunidad de presencia.

## 4. Comparativa de plataformas y controles publicados

| Plataforma/superficie | Señales y controles documentados a la fecha de corte | Herramientas de observación | Matiz esencial |
|---|---|---|---|
| **Google AI Overviews / AI Mode / Search generativo** | Googlebot y elegibilidad normal de Search; Google-Extended para determinados usos de IA fuera de la inclusión en Search. | Search Console: informe de impresiones, páginas, país, dispositivo y fecha para experiencias generativas. | No se requiere marcado especial, archivo `llms.txt` ni longitud de página específica para las funciones de IA de Search. Estar indexada no garantiza aparecer. |
| **Bing / Microsoft Copilot** | Bing Webmaster Tools, prácticas normales de descubrimiento e indexación; consultar las guías vigentes de Bing para directivas actuales. | AI Performance (vista previa): citas, páginas citadas, consultas de grounding; Topics Portfolio (beta) y métricas relacionadas. | Los datos son específicos del entorno Bing/Microsoft y se describen como direccionales; cita no es ranking ni tráfico. |
| **ChatGPT Search** | `OAI-SearchBot` para presencia en resultados de Search; `GPTBot` para uso potencial en entrenamiento; `ChatGPT-User` para acciones dirigidas por usuarios. | Analítica propia: OpenAI publica `utm_source=chatgpt.com` como posible marcador de referencia; no ofrece al propietario web un informe universal de citas comparable a GSC. | Los ajustes son independientes; robots.txt puede tardar alrededor de 24 horas en reflejarse. El agente de usuario de petición no gestiona la elegibilidad en Search. |
| **Perplexity** | `PerplexityBot` para descubrimiento y enlaces de búsqueda; `Perplexity-User` para recuperar páginas a petición del usuario. | Logs, analítica/referrer y comprobaciones manuales del producto. La documentación lista rangos IP para verificación de bots/WAF. | Perplexity indica que la recuperación iniciada por el usuario generalmente ignora robots.txt. Protege contenido privado con autenticación, no con robots.txt. |
| **Claude con búsqueda web** | `Claude-SearchBot` para mejorar resultados de búsqueda, `ClaudeBot` para entrenamiento potencial y `Claude-User` para solicitudes de usuarios. | Logs del servidor y auditoría manual; sin informe público universal de citas comparable a GSC. | Anthropic documenta respeto a robots.txt y soporte de `Crawl-delay`; comprueba la política vigente por producto y región. |

Fuentes primarias: [guía de Google sobre funciones de IA](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), [controles Google-Extended](https://developers.google.com/crawling/docs/crawling-indexing/google-extended), [Search Console generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports), [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/), [Bing Topics Portfolio beta](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/), [OpenAI crawlers](https://developers.openai.com/api/docs/bots), [Anthropic crawlers](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) y [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers).

### 4.1 Decisión sobre robots y firewalls

Antes de editar `robots.txt`, documenta por agente:

| Pregunta | Decisión que debe tomar el propietario |
|---|---|
| ¿Queremos que el contenido público pueda aparecer como fuente en búsqueda de esa plataforma? | Permitir el agente de búsqueda correspondiente, después de valorar licencias y negocio. |
| ¿Permitimos el uso para entrenamiento? | Tratarlo como decisión separada del descubrimiento en búsqueda, según las opciones documentadas de cada operador. |
| ¿Permitimos solicitudes desencadenadas por una persona? | Valorar el producto, el contenido y el riesgo de extracción; ciertos agentes pueden comportarse distinto de los crawlers automáticos. |
| ¿El WAF/CDN permite el acceso legítimo? | Verificar IP oficial y user-agent documentados en combinación; el user-agent puede falsificarse. |
| ¿Hay contenido privado? | Exigir autenticación y autorización en el servidor. `robots.txt` es público y no es un mecanismo de seguridad. |

No pegues una lista de agentes como solución universal. Los nombres, direcciones IP, productos y políticas cambian; comprueba los enlaces oficiales del proveedor y registra la fecha de revisión. Para verificar robots, valida reglas, subdominios, cabeceras HTTP, WAF, logs y respuestas reales, no solo el archivo de texto.

## 5. Qué está respaldado, qué es hipótesis y qué es mito

| Recomendación o afirmación | Evaluación | Aplicación prudente |
|---|---|---|
| Una página pública, indexable, rastreable, con respuesta útil y bien enlazada tiene más oportunidades de ser considerada por sistemas que dependen de búsqueda web. | **Fundamento sólido**, aunque no garantiza cita. | Resolver errores de rastreo, canonicals, renderizado, enlaces internos y calidad antes de tácticas específicas de IA. |
| Publicar investigación, datos, documentación y experiencia propios puede aportar información que no es intercambiable con páginas genéricas. | **Estrategia razonable**; el impacto depende de consulta y plataforma. | Publicar evidencia verificable, procedencia, método y límites. No inventar estudios ni estadísticas. |
| Organizar contenido con títulos precisos, términos definidos, tablas legibles y respuestas directas ayuda a las personas y puede facilitar extracción. | **Buena práctica editorial**; no es una palanca universal demostrada de citación. | Hacerlo por comprensión y accesibilidad; medir el resultado. No fragmentar de forma mecánica. |
| Añadir schema especial para aparecer en respuestas de IA. | **No respaldado como requisito universal**. Google dice que no hace falta marcado específico para AI Overviews/AI Mode. | Usar datos estructurados cuando correspondan a una función admitida y describan contenido visible y veraz. No venderlos como “hack GEO”. |
| Crear `llms.txt` para que Google cite mejor el sitio. | **No respaldado para Google Search**; Google declara que no lo usa como factor de visibilidad. Otros usos pueden ser decisiones de documentación o tooling fuera de Search. | No sustituir sitemap, robots, HTML legible o documentación. Si se publica, evaluar mantenimiento y objetivo concreto, sin prometer resultados. |
| Cada párrafo debe tener X palabras, las páginas han de medir X, o hay que “chunkear” todo en bloques de 300 palabras. | **Sin estándar universal demostrado**. | Estructurar según la tarea y al usuario. Mantener profundidad y contexto necesarios. |
| Mencionar la marca muchas veces, imitar preguntas de prompts o añadir listas de “mejores marcas”. | **No demostrado y arriesga calidad/manipulación**. | Trabajar intención real, claridad de entidad y fuentes auténticas. No fabricar comparativas ni testimonios. |
| Una cita en IA equivale a un backlink o a una posición en Google. | **Falso como equivalencia**. | Registrar la cita como evento distinto y atribuirle su superficie y consulta. |
| Un aumento de citas demuestra aumento de ventas. | **No demostrado**. | Conectar exposición con sesiones y conversiones, comparar periodos y reconocer tráfico oscuro y atribución incompleta. |
| El estudio GEO KDD 2024 garantiza hasta 40% más visibilidad. | **Lectura incorrecta de la cifra**. | El 40% es un resultado máximo relativo en la métrica y benchmark del trabajo, no un efecto general de negocio. |

## 6. Protocolo operativo de optimización

### Fase 1 — Fijar el objetivo y el universo

1. Define qué valor buscas: descubrimiento de marca, visita de referencia, lead, compra, soporte o inclusión en una fuente educativa.
2. Elige las superficies prioritarias según audiencia, idioma, mercado y modelo de negocio. No empieces “optimizando para todas las IA” si no sabes qué producto importa.
3. Selecciona preguntas que representen tareas reales de clientes: informativas, comparativas, transaccionales, locales y de soporte. Separa preguntas de marca y sin marca.
4. Conserva una línea base con fecha, país, idioma, producto, modo, consulta literal, URL citada y captura o enlace de la respuesta, respetando condiciones de uso.

### Fase 2 — Auditar el acceso técnico

- Comprueba respuestas HTTP: páginas importantes devuelven `200`, no redirecciones encadenadas, páginas vacías, errores intermitentes ni challenge de navegador para bots legítimos.
- Confirma que `robots.txt`, `noindex`, canonicals, autenticación, reglas del CDN/WAF y directivas por subdominio expresan la política deseada.
- Revisa que el contenido principal está presente en HTML renderizado y no depende de una acción que el crawler no pueda ejecutar. Comprueba navegación con enlaces HTML estándar.
- Mantén sitemaps XML, hreflang, canonicals e indexación limpios según la estrategia SEO normal. Sitemap e IndexNow notifican o facilitan descubrimiento; no garantizan indexación ni citas.
- Revisa logs del servidor para distinguir crawler de búsqueda, crawler de entrenamiento y petición de usuario; verifica las IP con datos publicados por la plataforma antes de confiar en un user-agent.
- Conserva datos sensibles detrás de controles de acceso reales. Robots.txt comunica preferencias a crawlers cooperativos; no oculta ni protege información.

### Fase 3 — Auditar contenido y fuentes

En páginas prioritarias, comprueba:

- **Necesidad concreta:** responde una pregunta, tarea o decisión que existe en el mercado; evita páginas creadas solo para capturar variantes artificiales.
- **Valor original:** experiencia directa, datos propios, documentación, comparaciones con método, imágenes propias o conocimiento difícil de sustituir.
- **Afirmaciones comprobables:** define términos, fecha, unidad, ámbito geográfico, fuente y condiciones cuando afectan a la interpretación.
- **Autoría y responsabilidad:** identifica autores, revisores, organización, experiencia pertinente y forma de contacto; corrige credenciales o biografías exageradas.
- **Transparencia:** describe limitaciones, conflictos de interés, metodología, fuentes, actualizaciones y políticas comerciales relevantes.
- **Claridad de entidades:** usa el nombre oficial de producto/empresa, variantes y relaciones con coherencia. No rellenes el texto con repeticiones de marca.
- **Accesibilidad de la evidencia:** coloca conclusiones y datos clave cerca del contexto que los explica; enlaza a fuentes primarias y deja claro qué afirmación respalda cada cita.
- **Mantenimiento:** corrige información caducada cuando cambia de verdad. Cambiar la fecha sin actualizar el contenido puede engañar.
- **Experiencia de lectura:** títulos descriptivos, estructura lógica, tablas semánticas cuando aporten comparación, texto visible, navegación clara y ausencia de intersticiales que impidan acceder al contenido.

Esto mejora la utilidad para personas y la posibilidad de que un sistema interprete una fuente. No se afirma que cada punto sea un factor directo de ranking generativo.

### Fase 4 — Mejorar la reputación sin manipularla

La selección de fuentes puede depender tanto de la recuperación como de la familiaridad del sistema con entidades, fuentes y páginas; la investigación reciente lo estudia, pero no permite una receta universal. Construye reputación mediante cobertura editorial genuina, colaboraciones transparentes, documentación pública útil, comunidad y referencias de terceros independientes. No compres publicaciones falsas, reseñas, citas académicas ni “menciones garantizadas por IA”. No publiques contenido diseñado para introducir conceptos ficticios en respuestas: además de dañar a usuarios, los experimentos recientes muestran que la contaminación de fuentes puede ser una vulnerabilidad del sistema.

### Fase 5 — Usar datos estructurados solo para su función válida

Aplica Schema.org cuando aporte un tipo admitido por un buscador o una aplicación concreta, con valores fieles a lo visible y elegible. Valida sintaxis y políticas de esa plataforma. El marcado puede ayudar a interpretar entidades o a habilitar resultados enriquecidos; no crea por sí solo reputación, no fuerza una cita y no corrige contenido insuficiente. La guía de Google para IA dice que no hace falta un marcado especial para sus funciones generativas.

### Fase 6 — Actualizar solo cuando exista una razón

Para precios, versiones, disponibilidad, horarios, normativas, especificaciones o estadísticas, muestra fecha de vigencia y actualiza cuando cambien. En temas atemporales, no simules frescura. Una publicación reciente puede ser importante en ciertas consultas sensibles al tiempo; no se ha demostrado que todo contenido nuevo gane siempre frente a contenido estable en todos los motores.

## 7. Medición reproducible

### 7.1 Construye un panel de consultas

Mantén un conjunto fijo de consultas representativas y anota su razón de inclusión. Estratifícalas por:

- intención (aprender, comparar, comprar, resolver una incidencia, encontrar un proveedor local);
- categoría y producto/servicio;
- etapa de decisión;
- idioma y mercado;
- consultas de marca, competidor y categoría;
- temas de alta sensibilidad o alto riesgo.

Para un sitio pequeño, empieza con un panel manejable que se pueda revisar manualmente; para un sitio grande, usa una muestra estratificada. No presentes el número del panel como tamaño estadísticamente suficiente sin cálculo y diseño muestral.

### 7.2 Registra cada observación

| Campo | Ejemplo de registro |
|---|---|
| Motor y superficie | ChatGPT Search; Google AI Mode; Bing Copilot |
| Fecha/hora y mercado | 2026-10-18; España; español |
| Consulta literal | Texto exacto usado |
| Modo/sesión | Web activada, sesión nueva, dispositivo; anotar si no se conoce el modelo |
| Resultado | Sin respuesta, respuesta con fuentes, resumen, lista, producto local |
| Evidencia propia | Dominio y URL exacta citada; fragmento o proposición atribuida |
| Papel de la fuente | Cita directa, apoyo contextual, mención sin enlace, enlace navegacional |
| Fidelidad | La URL respalda correctamente la afirmación: sí / parcialmente / no / no comprobable |
| Presentación | Posición aproximada, número de fuentes, prominencia; definición constante |
| Competidores y fuentes externas | Dominios, tipo de fuente, páginas relevantes |
| Resultado posterior | Clics, sesiones, leads, ventas u otro evento disponible |

Repite las observaciones en diferentes fechas y conserva resultados negativos. Si el producto permite enlace compartible, guárdalo; si no, conserva evidencia de forma compatible con sus condiciones. Evita automatizar scraping o enviar consultas masivas sin revisar términos y carga.

### 7.3 Métricas recomendadas (con definiciones propias)

1. **Accesibilidad:** porcentaje de URLs prioritarias que responden y son recuperables por el agente/superficie objetivo, medido con pruebas técnicas y logs.
2. **Cobertura de citas del panel:** ejecuciones elegibles del panel que citan al menos una URL propia / ejecuciones elegibles observadas. Es una métrica interna: publica denominador, periodo, motores y protocolo.
3. **Cobertura de páginas:** páginas propias citadas y distribución por sección, intención y motor.
4. **Cuota de citas dentro del panel:** citas propias / todas las citas registradas en ese panel y periodo. No equivale a cuota de mercado ni share of voice universal.
5. **Fidelidad de atribución:** proporción de citas en las que la página realmente respalda la proposición, evaluada con muestreo humano.
6. **Visibilidad oficial por plataforma:** impresiones/páginas del informe de Google Search Console o citas/consultas de grounding en Bing AI Performance, respetando el alcance y límites del producto.
7. **Visitas atribuibles:** sesiones etiquetadas o referidas desde productos de IA. En ChatGPT puede aparecer `utm_source=chatgpt.com`; analítica y privacidad pueden perder parte de la atribución. No asumas que todo el tráfico aparece con ese referrer.
8. **Resultado comercial:** ventas, leads cualificados, ingresos, retención, coste de soporte o valor de marca, según objetivo. Separa conversiones asistidas y directas y documenta la ventana de atribución.

No combines métricas de motores con definiciones distintas en un único “AI visibility score” sin documentar pesos, cobertura y sesgos. Un índice sintético sirve para seguimiento interno si sus componentes permanecen visibles; no es una medida objetiva de todo Internet.

### 7.4 Cómo probar un cambio

- Formula una hipótesis concreta: por ejemplo, “hacer visible la política de compatibilidad ayudará a que la página de soporte sea citada en consultas de versión”.
- Selecciona páginas comparables y un grupo que no se modifica, cuando sea posible.
- Cambia una variable sustantiva a la vez y registra el despliegue, URLs, fechas, contenido y eventos relevantes.
- Mantén un panel fijo y registra superficie, país, idioma, modo, sesión y fecha. Repite varias veces; un único resultado es demasiado frágil.
- Mira el paso del embudo afectado: primero acceso/indexación/recuperación, después cita, después tráfico y negocio. No atribuyas un efecto de citas a un cambio editorial si el crawler no llegó a la página.
- Considera estacionalidad, cambios de producto, actualizaciones de motor, campañas de marca, modificaciones de analítica y cambios en competidores.
- Acepta resultados nulos. Si la muestra es pequeña o no se puede controlar la exposición, informa que el hallazgo es direccional, no causal.

## 8. Priorización por tipo de sitio

| Tipo de sitio | Prioridades razonables | Riesgo de interpretación |
|---|---|---|
| **Editorial / medios** | Política de acceso por bot, derechos y licencias, autoría, fuentes primarias, datos y enlaces de referencia, medir impresiones/citas y tráfico. | Una cita puede sustituir una visita en ciertas tareas; separar valor de marca, tráfico y modelo de ingresos. |
| **Ecommerce** | Datos exactos de producto, precio, stock, envío y devolución; páginas accesibles; feeds y canales comerciales vigentes; comparación transparente. | No prometer que Product schema eleva citas. Una variación de precio o stock puede invalidar la respuesta generada. |
| **SaaS / documentación** | Documentación pública rastreable, versiones claras, ejemplos funcionales, límites y compatibilidad; enlaces entre producto, documentación y soporte. | Si una página está detrás de login o el código solo aparece en una app, el sistema puede no recuperar la evidencia. |
| **Local** | Nombre, dirección, teléfono, área, horario y servicios consistentes; perfiles oficiales; reseñas auténticas y políticas claras. | Horarios o disponibilidad incorrectos pueden causar daño directo; monitorizar cambios locales y respuestas erróneas. |
| **Salud, finanzas, legal y otros YMYL** | Credenciales verificables, revisión profesional, fuentes primarias, fecha, límites, procesos de corrección y cumplimiento normativo. | La síntesis automática puede perder matices. Auditar afirmaciones críticas y no tratar una cita como aval profesional. |
| **B2B / fabricantes** | Especificaciones, compatibilidad, certificaciones vigentes, fichas descargables con versión, casos verificables y vocabulario estable de entidad. | Los productos poco conocidos pueden no aparecer en respuestas basadas en familiaridad de marca; no manipular menciones. |

## 9. Riesgos y límites editoriales

- **Contenido fabricado para “alimentar” a la IA:** escala publicaciones sin valor y puede convertirse en abuso de contenido escalado o desinformación. Usa IA como herramienta editorial con revisión, autoría y responsabilidad humana.
- **Falsa prueba social:** no inventes reseñas, rankings, premios, estudios, citas de terceros ni “casos de éxito”. Una mención fabricada puede influir temporalmente en respuestas, pero degrada confianza y puede perjudicar a usuarios.
- **Pérdida de contexto:** respuestas resumidas pueden omitir condiciones, advertencias, excepciones y fechas. Comprueba lo que el sistema atribuye a la página.
- **Privacidad y derechos:** los controles de rastreo, entrenamiento, búsqueda y fetch no son idénticos. Revisa términos, acuerdos de licencia y normativa aplicable antes de abrir contenido sensible o licenciado.
- **Seguridad:** no uses robots.txt para proteger secretos; no confíes solo en el user-agent para permitir acceso a zonas sensibles. Usa autenticación, reglas WAF verificadas, limitación de tasa y registros.
- **Volatilidad:** las respuestas pueden cambiar incluso sin editar la web. Conserva historial, evita reaccionar a una sola muestra y prioriza problemas de usuario persistentes.
- **Sesgo de selección:** las plataformas pueden citar repetidamente un grupo limitado de dominios. Que una fuente sea citada no prueba su exactitud, independencia o calidad.

## 10. Hoja de ruta de 90 días

No es una promesa de crecimiento, sino una secuencia para producir evidencia interna.

### Días 1–15: definir y medir

- Elegir objetivo de negocio y superficies relevantes.
- Revisar políticas de bots, robots, WAF, privacidad y derechos.
- Fijar panel de consultas y capturar línea base.
- Configurar analítica/referrers y registrar límites de atribución.

### Días 16–35: reparar acceso y páginas prioritarias

- Corregir errores HTTP, bloqueos accidentales, canonicals, enlaces internos y renderizado.
- Asegurar que páginas prioritarias contienen texto legible y no quedan huérfanas.
- Corregir inconsistencias de datos de producto, negocio, autoría y fechas.
- No aplicar una renovación masiva de contenido sin auditoría de utilidad.

### Días 36–65: aportar evidencia original

- Priorizar un grupo pequeño de páginas con preguntas de alto valor.
- Añadir experiencia, metodología, fuentes, comparación real o datos propios donde falten.
- Mejorar claridad y navegación sin sacrificar matices.
- Mantener páginas comparables como referencia si el diseño lo permite.

### Días 66–90: revisar resultados y decidir

- Repetir consultas y auditorías técnicas con el mismo protocolo.
- Contrastar los informes oficiales de Search Console y Bing con logs y analítica.
- Revisar fidelidad de las citas, clics, leads y resultados de negocio.
- Documentar efectos nulos, positivos y adversos; detener cambios que solo aumentan menciones vacías.
- Ajustar la siguiente prueba a partir del cuello de botella observado.

## 11. Lista de comprobación ejecutiva

- [ ] El objetivo y las superficies prioritarias están definidos.
- [ ] La decisión sobre búsqueda, entrenamiento y peticiones de usuario se tomó por separado cuando la plataforma ofrece controles separados.
- [ ] `robots.txt`, `noindex`, canonicals, WAF, autenticación y subdominios reflejan la política real.
- [ ] Se verificaron logs y acceso de crawlers legítimos con IP/documentación oficial actual.
- [ ] Las páginas importantes son descubribles, enlazadas y legibles sin interacciones opacas.
- [ ] El contenido incorpora evidencia propia o valor diferencial cuando procede.
- [ ] Afirmaciones, precios, versiones, horarios y fechas sensibles están actualizados y contextualizados.
- [ ] Autores, entidades, fuentes y conflictos de interés se presentan con precisión.
- [ ] Schema y archivos auxiliares no se venden internamente como garantías de citación.
- [ ] Existe un panel fijo de consultas y se registran también resultados negativos.
- [ ] Las métricas distinguen rastreo, indexación, recuperación, cita, sesión y conversión.
- [ ] Las afirmaciones importantes generadas por IA se revisan por fidelidad, especialmente en áreas sensibles.
- [ ] Las tácticas de terceros se evalúan por método, fecha, muestra, interés comercial y posibilidad de réplica.

## 12. Conclusión

El trabajo de SEO para motores de IA no consiste en “escribir para el robot” ni en repetir una lista de hacks. Consiste en comprender qué superficies importan, permitir el acceso que el negocio acepta, mantener las páginas técnicamente recuperables, publicar información precisa que aporte valor y verificar con evidencia si los sistemas la encuentran y si esa visibilidad resulta útil.

Las fuentes más sólidas confirman que las plataformas tienen controles distintos y que Google no exige una capa técnica especial para sus funciones generativas de Search. La investigación experimental aporta hipótesis sobre estructura, recuperación, posición en contexto y selección de fuentes; sus resultados no deben convertirse en garantías universales. La estrategia responsable es construir fuentes que merezcan ser usadas, no fabricar señales para forzar una respuesta.

## 13. Bibliografía anotada

### Documentación y herramientas oficiales

1. **Google Search Central — [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features).** Requisitos de elegibilidad y reporte para experiencias de IA en Search.
2. **Google Search Central — [A guide to Google Search ranking systems and AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).** Orientación oficial que rechaza requisitos especiales de marcado o formatos para AI Overviews/AI Mode.
3. **Google Developers — [Google-Extended](https://developers.google.com/crawling/docs/crawling-indexing/google-extended).** Alcance del token de control para usos de IA; separación respecto a Search.
4. **Google Search Central — [Search Generative AI performance reports in Search Console](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports).** Informe de visibilidad publicado en junio de 2026 y disponible globalmente desde el 31 de agosto, según el anuncio.
5. **Google Search Central — [Robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro).** Alcance y límites de robots.txt; no es control de acceso.
6. **OpenAI Developers — [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots).** Agentes OAI-SearchBot, GPTBot y ChatGPT-User, funciones y control independiente.
7. **OpenAI Help Center — [Publishers and developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq).** Aparición en ChatGPT Search, acceso del crawler y atribución de referencia.
8. **Anthropic Help Center — [Does Anthropic crawl data from the web?](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler).** Diferencias entre ClaudeBot, Claude-User y Claude-SearchBot; política de robots.
9. **Perplexity Docs — [Perplexity Crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers).** PerplexityBot, Perplexity-User, robots y verificación de IP para WAF.
10. **Bing Webmaster Blog — [Introducing AI Performance in Bing Webmaster Tools](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/).** Alcance y métricas de cita en vista previa; datos no equivalentes a ranking.
11. **Bing Search Blog — [New AI Visibility Insights in Bing Webmaster Tools](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/).** Intenciones, temas, citation share y comparación, con límites de interpretación.
12. **Bing Webmaster Blog — [Topics Portfolio beta in AI Performance](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/).** Beta reciente de agrupación temática; el propio anuncio describe los datos como direccionales.
13. **Bing — [Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a).** Guía primaria de calidad y prácticas de Bing; comprobar la versión vigente.

### Investigación académica y estudios independientes

14. **Aggarwal et al. (KDD 2024), [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735), DOI [10.1145/3637528.3671900](https://doi.org/10.1145/3637528.3671900).** Trabajo fundacional y benchmark; el “hasta 40%” es una métrica experimental situada, no un incremento universal de tráfico o citas.
15. **Puerto et al. (NeurIPS 2025), [C-SEO Bench: Does Conversational SEO Work?](https://papers.neurips.cc/paper_files/paper/2025/hash/27aa3aeff0f8460a7b43d30fa6c5c032-Abstract-Datasets_and_Benchmarks_Track.html).** Benchmark multisitio y multimétodo; útil para evaluar límites de las técnicas de reescritura en sus tareas y dominios.
16. **Chen & Koudas (arXiv, 10 oct. 2026), [What Drives AI Citations?](https://arxiv.org/abs/2610.15033).** Preprint con 158.099 respuestas y 468.037 citas en dos mercados; plantea que la recuperación de páginas explica más variación que propiedades observables de página en su muestra. Aún no revisado por pares y no universalizable.
17. **Liu et al. (arXiv, 8 oct. 2026), [From Public Posts to AI-Search Citations](https://arxiv.org/abs/2610.11932).** Preprint de seguridad que evalúa concentración de fuentes y vulnerabilidad de sistemas ante contenido publicado en plataformas de baja barrera. Evidencia de riesgo, no táctica recomendada.
18. **[Optimizing Visibility in Generative Engines: A Critical Survey (2023–2026)](https://arxiv.org/abs/2607.14035).** Revisión de literatura reciente; subraya heterogeneidad de métricas y falta de evidencia causal duradera y transversal. Preprint, no revisión sistemática definitiva.
19. **Ahrefs (2026), [We Tracked 1,885 Pages Adding Schema. AI Citations Barely Moved](https://ahrefs.com/blog/schema-ai-citations/).** Estudio de proveedor con páginas tratadas y comparación; útil como señal sobre la hipótesis de schema, no revisión por pares ni prueba para todas las implementaciones.
20. **Marketing Science, [ChatGPT Referrals to E-Commerce Websites](https://doi.org/10.1287/mksc.2025.0489).** Estudio de tráfico referido en una muestra de sitios de ecommerce; el alcance de producto y periodo limita la generalización a otras plataformas.

### Cómo actualizar esta guía

Antes de cambiar robots, firewalls, datos estructurados o políticas editoriales, revisa la fuente primaria enlazada. Para la siguiente edición, registra qué cambió en cada producto, la fecha de consulta, el alcance geográfico, si el dato era público o beta y si la nueva evidencia fue revisada por pares. La versión presente es una síntesis a fecha de corte, no una garantía de políticas futuras.
