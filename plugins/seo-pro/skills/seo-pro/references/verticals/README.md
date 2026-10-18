# Verticals: layers by business model

Engine layers (`../engines/`) say what changes **per search engine**. Vertical layers say what changes **per business model**: the surfaces, data and rules that only matter for some sites. They sit on top of the shared core (1–160) and the engine layers, never replace them, and use their own ID prefixes so nothing is renumbered.

| File | Business model | Practice IDs | Main surfaces |
|---|---|---|---|
| `local.md` | Businesses that serve customers in person: storefronts, service-area businesses, practitioners, chains, hybrids | L1–L22 | Google Business Profile, Google Maps / local pack, Bing Places, Apple Business (Apple Maps), directories and review sites |
| `ecommerce.md` | Online stores and marketplaces | E1–E24 | Organic category and product pages, Product snippets / Merchant listings, Google Merchant Center free listings, agentic-commerce channels |
| `saas-services.md` | SaaS, software, APIs and docs (S1–S8); lead generation and professional services (S9–S14) | S1–S14 | Solution and use-case pages, docs, integrations, comparisons, service pages, forms and CRM quality |
| `publishers.md` | Newsrooms, magazines, local media, digital publications | P1–P20 | Top Stories, News tab, Google News, Discover, Bing/Microsoft, AI answers citing journalism |
| `regulated.md` | Health, finance, legal and other high-impact (YMYL) topics, informational or commercial | Y1–Y16 | All surfaces; governs what may be claimed, reviewed and published |

A site can need more than one vertical (an omnichannel retailer needs local and e-commerce; a clinic needs local and regulated). New verticals get their own file and prefix (e.g. `marketplace.md` → K1…) plus a row here.

## When to read them

In step 1 of the workflow ("Understand the project") classify the business. Then:

- **Serves customers in person** (at an address or at theirs) → read `local.md`, starting with L1–L2 (model and eligibility) before touching any profile.
- **Sells online** → read `ecommerce.md`, starting with E1, E5 and E16 (page types, facets, catalogue reconciliation).
- **Sells software or a digital product** → read `saas-services.md` S1–S8; **sells services through enquiries** (consultancy, agency, installer, B2B) → S9–S14.
- **Publishes news or journalism** → read `publishers.md`, starting with P1, P8, P12–P13.
- **Touches health, money, legal rights, safety or other high-impact decisions** → read `regulated.md` (Y1–Y3 first) **in addition to** any other vertical: a clinic is local **and** regulated; a supplement store is e-commerce **and** regulated; a finance news site is a publisher **and** regulated.
- **None of these** (e.g. an informational or documentation site) → the core and engine layers are enough; put "local profiles" and "Merchant Center" under *What we will NOT do* unless they apply.

Whatever the vertical, the cross-cutting playbooks in `../playbooks/` (migrations, measurement, reputation, governance) apply when their situation arises.

## How verticals map onto engines

| Topic | Google | Bing / Microsoft | Apple | AI answer engines | Layer |
|---|---|---|---|---|---|
| Local listing | Google Business Profile | Bing Places for Business (can import from GBP) | Apple Business (formerly Apple Business Connect) | Read profiles, reviews and websites; Google Maps "Ask" answers from them | L2–L8, L18, B15 |
| Local Q&A | Profile Q&A removed (Dec 2025); AI "Ask" in Maps where available | — | — | Answer questions on the website | L8 |
| Local ranking model | Relevance, distance, prominence (no weights published) | Location listed among ranking parameters | Not published | Not published | L1–L5, B10, B11 |
| Product data on the page | `Product` / `Offer` / `ProductGroup`; Product snippets vs Merchant listings | Structured data read for understanding | — | Read crawlable pages; schema isn't a citation lever | E13, A12 |
| Product feed | Merchant Center: free listings across Google surfaces + Shopping ads | Microsoft Merchant Center: **ads only** (no documented organic catalogue surface) | — | ChatGPT product discovery via ACP feeds; Google UCP checkout (US early access) | E15, E20, E21 |
| News discovery | Automatic (no submission); News sitemap; Top Stories needs no markup; Preferred sources | Automatic (PubHub retired); IndexNow; Open Graph thumbnails | — | Decide search, training, user fetch and licensing per operator | P12–P14, P6, P18–P19 |
| Discover-style feeds | Discover (Feb 2026 Discover core update: local, less clickbait, in-depth expertise) | Microsoft Start / Edge feeds | — | — | P15 |
| High-impact topics | Systems weigh E-E-A-T-aligned signals more on YMYL; E-E-A-T isn't a ranking factor | Quality and credibility among ranking parameters | — | Summaries lose nuance; audit critical answers | Y1–Y16, B10 |
| Shipping & returns | Search Console settings or organization-level markup (Nov 2025); Merchant Center for feeds | Merchant Center (ads) | — | Consume whatever the page and feeds say | E14 |

## Conflict rule, applied to verticals

The engines' rule still decides (`../engines/README.md`): do both → stricter wins → user-facing truth wins → document the trade-off. In verticals, "user-facing truth" carries extra weight because the failure costs are direct: a wrong opening time sends a customer to a closed door; a wrong price in a feed or an AI agent's answer breaks the sale and can breach consumer law. When a tactic makes a listing, feed or page say something that isn't true for the customer, it loses.
