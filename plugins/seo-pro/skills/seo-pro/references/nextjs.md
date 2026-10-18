# Next.js implementation (App Router)

Before writing code, check the version in `package.json` (`next`) and consult the official docs if something doesn't line up: some APIs change between major versions (e.g. in Next 16 `middleware.ts` becomes `proxy.ts`, and `next/image`'s `priority` prop is replaced by `preload`). Examples are TypeScript for the App Router; on the Pages Router use `next/head` and `getServerSideProps`/`getStaticProps`, but recommend migrating.

## Contents
1. Centralised SEO configuration
2. Metadata (title, description, canonical, robots, Open Graph, hreflang)
3. sitemap.ts and robots.ts
4. JSON-LD
5. Performance: images, fonts, third-party scripts
6. Rendering and caching
7. Redirects, headers and 404s
8. Staging and preview environments
9. Final checks

---

## 1. Centralised SEO configuration

A single module prevents canonicals on different hosts, inconsistent brand names and relative URLs.

```ts
// src/lib/seo/config.ts
export const siteConfig = {
  url: process.env.NEXT_PUBLIC_SITE_URL ?? 'https://www.example.com', // no trailing slash
  name: 'Brand Name',
  shortName: 'Brand',
  locale: 'en_US',
  defaultTitle: 'Brand Name: value proposition',
  defaultDescription: 'A 140–160 character description with the value proposition.',
  twitter: '@brand',
  organization: {
    legalName: 'Brand Name Ltd',
    logo: '/logo-512.png',
    sameAs: ['https://www.linkedin.com/company/brand', 'https://github.com/brand'],
  },
} as const;

export const absoluteUrl = (path = '/') => new URL(path, siteConfig.url).toString();
```

`NEXT_PUBLIC_SITE_URL` must be the **canonical** production domain in production. In previews, don't point it at the preview domain (see §8).

## 2. Metadata

### Root layout

```ts
// src/app/layout.tsx
import type { Metadata, Viewport } from 'next';
import { siteConfig } from '@/lib/seo/config';

export const metadata: Metadata = {
  metadataBase: new URL(siteConfig.url),           // turns relative paths into absolute URLs
  title: { default: siteConfig.defaultTitle, template: `%s | ${siteConfig.shortName}` },
  description: siteConfig.defaultDescription,
  applicationName: siteConfig.name,
  openGraph: { type: 'website', siteName: siteConfig.name, locale: siteConfig.locale },
  twitter: { card: 'summary_large_image', site: siteConfig.twitter },
  robots: { index: true, follow: true, 'max-image-preview': 'large', 'max-snippet': -1 },
  // icons: prefer the file conventions app/icon.png, app/apple-icon.png, app/favicon.ico
};

export const viewport: Viewport = { width: 'device-width', initialScale: 1 };

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">{/* the real content language; dynamic with i18n */}
      <body>{children}</body>
    </html>
  );
}
```

### Dynamic pages

```ts
// src/app/blog/[slug]/page.tsx
import type { Metadata } from 'next';
import { notFound } from 'next/navigation';
import { getPost } from '@/lib/posts';

type Props = { params: Promise<{ slug: string }> }; // params is a Promise in Next 15+

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params;
  const post = await getPost(slug);
  if (!post) return {};
  return {
    title: post.seoTitle ?? post.title,                // the template appends "| Brand"
    description: post.seoDescription ?? post.excerpt,
    alternates: { canonical: `/blog/${slug}` },        // relative + metadataBase = absolute
    openGraph: {
      type: 'article',
      url: `/blog/${slug}`,
      title: post.title,
      description: post.excerpt,
      publishedTime: post.publishedAt,
      modifiedTime: post.updatedAt,
      images: [{ url: post.ogImage ?? `/blog/${slug}/opengraph-image`, width: 1200, height: 630 }],
    },
    robots: post.noindex ? { index: false, follow: true } : undefined,
  };
}

export default async function Page({ params }: Props) {
  const { slug } = await params;
  const post = await getPost(slug);
  if (!post) notFound(); // real 404, not a soft 404
  // ...
}
```

Rules:
- **A canonical on every indexable page** via `alternates.canonical`. For filtered listings, the canonical points to the version without sort/tracking parameters; paginated pages point to themselves.
- Use `React.cache()` or deduplicated `fetch` so you don't query the database twice (metadata + page).
- `title.absolute` when a page shouldn't get the brand suffix (e.g. the home page).
- Dynamic OG images with `opengraph-image.tsx` (`ImageResponse` from `next/og`) per route segment.
- From Next 15.2, metadata may be streamed to browsers; for known bots it stays in the `<head>` of the initial HTML. If in doubt, verify with `curl` using a Googlebot user agent.

### hreflang (i18n)

```ts
alternates: {
  canonical: `/en/services`,
  languages: {
    'en': '/en/services',
    'es-ES': '/es/servicios',
    'x-default': '/en/services',
  },
},
```
Every language version must declare the same set (including itself). Set `<html lang>` from the `[locale]` segment.

## 3. sitemap.ts and robots.ts

```ts
// src/app/sitemap.ts
import type { MetadataRoute } from 'next';
import { absoluteUrl } from '@/lib/seo/config';
import { getAllPublishedPosts, getAllServices } from '@/lib/data';

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const [posts, services] = await Promise.all([getAllPublishedPosts(), getAllServices()]);
  return [
    { url: absoluteUrl('/'), lastModified: new Date('2026-10-01') }, // real date of the last meaningful change
    ...services.map((s) => ({ url: absoluteUrl(`/services/${s.slug}`), lastModified: s.updatedAt })),
    ...posts
      .filter((p) => !p.noindex)
      .map((p) => ({ url: absoluteUrl(`/blog/${p.slug}`), lastModified: p.updatedAt })),
  ];
}
```
- Only canonical, indexable, 200 URLs. Don't include `changeFrequency` or `priority` (Google ignores them).
- More than 50,000 URLs → split with `generateSitemaps()`.
- `lastModified` = the real content modification date, **not** `new Date()` on every entry.

```ts
// src/app/robots.ts
import type { MetadataRoute } from 'next';
import { siteConfig } from '@/lib/seo/config';

export default function robots(): MetadataRoute.Robots {
  const isProd = process.env.VERCEL_ENV === 'production' || process.env.APP_ENV === 'production';
  if (!isProd) return { rules: { userAgent: '*', disallow: '/' } }; // previews not crawlable
  return {
    rules: [
      { userAgent: '*', allow: '/', disallow: ['/api/', '/admin/', '/search'] },
      // Explicit AI decision (practice 37); example: allow search bots, block training bots
      { userAgent: ['GPTBot', 'CCBot'], disallow: '/' },
    ],
    sitemap: `${siteConfig.url}/sitemap.xml`,
    host: siteConfig.url,
  };
}
```
**Never** block `/_next/` (it holds the CSS and JS needed to render).

## 4. JSON-LD

A reusable component that escapes `<` to prevent injection:

```tsx
// src/components/seo/JsonLd.tsx
export function JsonLd({ data }: { data: Record<string, unknown> | Record<string, unknown>[] }) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, '\\u003c') }}
    />
  );
}
```

Typed generators (optional: the `schema-dts` package provides schema.org types):

```ts
// src/lib/seo/schema.ts
import { siteConfig, absoluteUrl } from './config';

export const organizationSchema = () => ({
  '@context': 'https://schema.org',
  '@type': 'Organization',
  '@id': absoluteUrl('/#organization'),
  name: siteConfig.name,
  legalName: siteConfig.organization.legalName,
  url: siteConfig.url,
  logo: absoluteUrl(siteConfig.organization.logo),
  sameAs: siteConfig.organization.sameAs,
});

export const websiteSchema = () => ({
  '@context': 'https://schema.org',
  '@type': 'WebSite',
  '@id': absoluteUrl('/#website'),
  url: siteConfig.url,
  name: siteConfig.name,
  publisher: { '@id': absoluteUrl('/#organization') },
  inLanguage: 'en',
});

export const articleSchema = (p: { slug: string; title: string; excerpt: string; image: string;
  publishedAt: string; updatedAt: string; author: { name: string; slug: string } }) => ({
  '@context': 'https://schema.org',
  '@type': 'BlogPosting',
  headline: p.title,
  description: p.excerpt,
  image: absoluteUrl(p.image),
  datePublished: p.publishedAt,
  dateModified: p.updatedAt,
  mainEntityOfPage: absoluteUrl(`/blog/${p.slug}`),
  author: { '@type': 'Person', name: p.author.name, url: absoluteUrl(`/authors/${p.author.slug}`) },
  publisher: { '@id': absoluteUrl('/#organization') },
});

export const breadcrumbSchema = (items: { name: string; path: string }[]) => ({
  '@context': 'https://schema.org',
  '@type': 'BreadcrumbList',
  itemListElement: items.map((it, i) => ({
    '@type': 'ListItem', position: i + 1, name: it.name, item: absoluteUrl(it.path),
  })),
});
```
Organization + WebSite on the home page (or in the root layout); Article and Breadcrumb on each article; Product/Offer on product pages. The data must match what's visible.

## 5. Performance

**Images** (`next/image`):
```tsx
import Image from 'next/image';
// Hero image (LCP): not lazy, high priority
<Image src={hero} alt="Real description" priority sizes="100vw" />          {/* Next ≤ 15 */}
// Next 16+: <Image ... preload /> (check the docs for your version)
// Everything else: lazy by default, always with width/height or fill + sizes
<Image src="/team.webp" alt="Support team at the office" width={800} height={533} sizes="(max-width: 768px) 100vw, 50vw" />
```
Set `images.formats: ['image/avif', 'image/webp']` in `next.config` and `remotePatterns` for external domains.

**Fonts** (`next/font`): self-hosts, subsets and adjusts metrics (prevents CLS).
```ts
import { Inter } from 'next/font/google';
const inter = Inter({ subsets: ['latin'], display: 'swap', variable: '--font-inter' });
```

**Third-party scripts** (`next/script`): analytics with `strategy="afterInteractive"`; chats, widgets and pixels with `strategy="lazyOnload"`. For GA4/GTM, `@next/third-parties`. Respect consent (don't load before acceptance).

**Less client JavaScript**: keep components as Server Components and add `'use client'` only on interactive leaves; `dynamic(() => import(...))` for heavy widgets below the fold. Analyse with `@next/bundle-analyzer`.

## 6. Rendering and caching

- Indexable content always rendered on the server (the App Router default). Check it isn't fetched on the client with `useEffect` + `fetch`.
- Rarely changing content: static with revalidation (`export const revalidate = 3600`, or tag-based revalidation with `revalidateTag` on publish). Known dynamic routes: `generateStaticParams`.
- Links with `next/link` (`<Link href>` renders a crawlable `<a href>`). Never navigation via `router.push` in an `onClick` as the only mechanism for content links.

## 7. Redirects, headers and 404s

```js
// next.config.mjs
/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: false, // pick a policy and never change it
  async redirects() {
    return [
      { source: '/old-services/:slug', destination: '/services/:slug', permanent: true }, // 308
      { source: '/:path*', has: [{ type: 'host', value: 'example.com' }], destination: 'https://www.example.com/:path*', permanent: true },
    ];
  },
  async headers() {
    return [
      {
        source: '/:path*',
        headers: [
          { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' },
          { key: 'X-Content-Type-Options', value: 'nosniff' },
          { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
          { key: 'Permissions-Policy', value: 'camera=(), microphone=(), geolocation=()' },
          { key: 'Content-Security-Policy', value: "frame-ancestors 'self'" },
        ],
      },
      { source: '/documents/:path*.pdf', headers: [{ key: 'X-Robots-Tag', value: 'noindex' }] },
    ];
  },
};
export default nextConfig;
```
- `permanent: true` returns **308** (equivalent to 301 for Google).
- Many redirects (hundreds or thousands): use Vercel bulk redirects or a map in `proxy.ts`/`middleware.ts` with O(1) lookup, not a giant array.
- Apex ↔ `www` redirection is better configured in the provider's domain settings (Vercel: "Redirect to") than in code.
- A useful `app/not-found.tsx` (search, main links) and `notFound()` in dynamic routes with no data. Check that non-existent URLs return **404**, not 200.
- For a full nonce-based CSP, follow the official Next.js guide (requires dynamic rendering).

## 8. Staging and previews

- Previews and staging **not indexable**: environment-aware `robots.ts` (§3) + `X-Robots-Tag: noindex` header on non-production environments + deployment protection (e.g. Vercel Deployment Protection).
- On every production deploy, check that `noindex` hasn't leaked through (practice 120: automated alert).
- `metadataBase` in previews: if it points to the production domain, canonicals of an indexed preview point to production (the lesser evil); never the other way round.

## 9. Final checks

```bash
npm run build && npm start &          # local production build
python3 "${CLAUDE_SKILL_DIR}/scripts/seo_audit.py" http://localhost:3000 --crawl 100
curl -s http://localhost:3000/ | grep -iE '<title|rel="canonical"|name="robots"|application/ld\+json'
curl -s http://localhost:3000/robots.txt
curl -s http://localhost:3000/sitemap.xml | head -20
curl -sI http://localhost:3000/does-not-exist | head -1   # must be 404
```
After deploying, repeat against the production domain and check URL Inspection in Search Console for 2–3 templates (home, listing, detail).
