# Equivalents in other stacks

Quick table of where each piece is implemented. Check the official docs for the project's exact version.

| Piece | Static HTML / Vite SPA | Astro | WordPress | Nginx | Apache (.htaccess) | Cloudflare | Vercel / Netlify (any framework) |
|---|---|---|---|---|---|---|---|
| Title, description, canonical | `<head>` of each page | `<head>` in the layout via props; `Astro.url` for the canonical | Yoast / Rank Math / SEOPress | — | — | — | — |
| Sitemap | Generate at build time (script) | `@astrojs/sitemap` | The SEO plugin (or core `/wp-sitemap.xml`) | — | — | — | — |
| robots.txt | File in `public/` | `public/robots.txt` or a `robots.txt.ts` endpoint | SEO plugin or a physical file | `location = /robots.txt` | Physical file | AI-bot settings in the dashboard (review them, 37) | File in `public/` |
| JSON-LD | `<script type="application/ld+json">` | Same, in layout/page | SEO plugin + filters to extend | — | — | — | — |
| 301 redirects | — (needs a server) | `redirects` in `astro.config` (static output emits meta refresh; better at the host) | Redirection plugin or the SEO plugin | `return 301 https://…$request_uri;` | `Redirect 301 /old /new` or `RewriteRule … [R=301,L]` | Redirect Rules / Bulk Redirects | `vercel.json` `redirects` / `_redirects` |
| Security headers and X-Robots-Tag | — | At the host | Plugin or server | `add_header … always;` | `Header set …` | Transform Rules (response headers) | `vercel.json` `headers` / `_headers` |
| Compression | — | At the host | Server/CDN | `gzip on;` / brotli module | `mod_deflate` / `mod_brotli` | Automatic | Automatic |
| Optimised images | Export AVIF/WebP at build time | `astro:assets` (`<Image>`, `<Picture>`) | Plugin (ShortPixel, Imagify) or CDN | — | — | Cloudflare Images / Polish | The provider's image optimisation |
| Rendering for bots | **Risk:** a Vite/CRA SPA serves empty HTML. Move to SSG/SSR (Astro, Next, Nuxt, SvelteKit) or prerender indexable routes | SSG by default (ideal) | Server-rendered (OK) | — | — | — | — |

## Notes per stack

**Pure SPA (React/Vue with Vite or CRA):** the highest-risk case for SEO (practice 25). Options from least to most robust: prerender public routes at build time (e.g. Vike, `react-snap`); split the public part into a static site (Astro) and keep the app on an `app.` subdomain; or migrate to a framework with SSR. Google no longer recommends "dynamic rendering" (serving different HTML to bots).

**WordPress:** use a single SEO plugin (never two: they duplicate tags). Disable indexing of author/date/tag archives if they add nothing, `noindex` on internal search, keep plugins to a minimum (performance and security), page caching (WP Rocket, LiteSpeed Cache or the host's) + CDN. Check that "Discourage search engines from indexing this site" (Settings → Reading) is unticked in production.

**Nginx (base snippet):**
```nginx
server {
  listen 80; server_name example.com www.example.com;
  return 301 https://www.example.com$request_uri;           # one hop to the canonical host
}
server {
  listen 443 ssl http2; server_name example.com;
  return 301 https://www.example.com$request_uri;
}
server {
  listen 443 ssl http2; server_name www.example.com;
  add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
  add_header X-Content-Type-Options "nosniff" always;
  add_header Referrer-Policy "strict-origin-when-cross-origin" always;
  location ~* \.(?:css|js|woff2|avif|webp|png|jpg|svg)$ { expires 1y; add_header Cache-Control "public, immutable"; }
  location ~* \.pdf$ { add_header X-Robots-Tag "noindex" always; }
}
```

**Apache (.htaccess):**
```apache
RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^ https://www.example.com%{REQUEST_URI} [R=301,L]
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\.pdf$">Header set X-Robots-Tag "noindex"</FilesMatch>
</IfModule>
```

**Cloudflare:** watch out for "Bot Fight Mode", WAF rules and "Block AI bots": check that Googlebot and Bingbot get a 200 (Security → Events) and that AI blocking matches the decision from practice 37. Enable Crawler Hints/IndexNow if you want automatic notifications to Bing.
