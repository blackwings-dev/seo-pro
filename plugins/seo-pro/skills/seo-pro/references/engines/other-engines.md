# Other search engines layer (practices W1–W12)

For markets and audiences where Google and Bing aren't the whole picture: **Yandex** (Russia), **Baidu** (mainland China), **Naver** (South Korea), **Seznam** (Czechia), the **IndexNow** network, and engines with their own or partly own index — **Brave Search**, **DuckDuckGo**, the **Ecosia/Qwant** European index, **Apple** (Applebot), **Mojeek**, **Kagi**. Read `README.md` in this folder first; the shared core applies to all of them, and this layer lists only what differs.

Research snapshot: **18 October 2026**. Several official consoles (Baidu Ziyuan, Naver Search Advisor, Seznam help) couldn't be fetched for this snapshot; facts from secondary sources are labelled *Supported* or *Unconfirmed* — verify in the console itself before a launch in those markets. Market shares are StatCounter (September 2026, all platforms), which is browser-based and undercounts in-app search.

Format: **Why** · **How** · **Avoid** · **Verify**.

## When this layer applies

| Market | Share (StatCounter, Sep 2026) | Read |
|---|---|---|
| Russia | Yandex ~70%, Google ~28% | W2–W3 |
| China (mainland) | Baidu ~47% (figures for others are unreliable; in-app search undercounted) | W4–W5 |
| South Korea | Google ~48%, Naver ~43% (Naver app undercounted) | W6 |
| Czechia | Google ~79%, Seznam ~15% | W7 |
| Global privacy/independent audiences | Brave, DuckDuckGo, Ecosia, Qwant, Mojeek, Kagi | W9–W11 |
| Apple devices (Siri, Spotlight, Safari suggestions) | — | W12 |

Sanctions, data-protection and content laws apply to some of these markets; marketing decisions there need legal review, not just SEO.

---

### W1. One IndexNow ping, seven engines — High · *Established*
- **How:** IndexNow participants listed at indexnow.org in 2026: **Bing, Yandex, Seznam, Naver, Yep, Internet Archive and Amazonbot**; a ping to one is shared with all. Google doesn't participate (B2 for implementation).
- **Verify:** key file at `/<key>.txt` (`seo_audit.py --indexnow-key`).

## Yandex

### W2. Yandex Webmaster and robots.txt specifics — High · *Established*
- **How:** verify in **Yandex Webmaster**; use `Clean-param` in robots.txt to tell Yandex which parameters to ignore (e.g. `Clean-param: utm_source&utm_medium&ref`) — a Yandex-only directive that complements canonicals (20). The old `Host` directive is gone from Yandex's documentation: choose the main mirror with 301 redirects and `rel=canonical`. Robot names are case-sensitive. Crawlers include **YandexBot** (main), YandexImages, YandexVideo, YandexMobileBot and YandexRenderResourcesBot; **YandexAdditional** reads robots.txt for Yandex's AI answers without indexing; some Yandex agents (e.g. YaDirectFetcher, YandexMetrika) ignore robots.txt. Verify Yandex bots by reverse DNS (`yandex.ru`, `yandex.net`, `yandex.com`) plus forward confirmation.
- **Avoid:** relying on `Host`; blocking YandexRenderResourcesBot from CSS/JS.

### W3. Yandex AI answers — Medium · *Supported*
- **Why:** **Yandex Neuro** (launched April 2024) combines YandexGPT with live search and cites sources, for users in Russia. Access for AI answers is governed through **YandexAdditional** in robots.txt.
- **How:** decide AI-answer access separately from indexing (A2 logic); measure in Yandex Webmaster and referrals.

## Baidu

### W4. Baidu basics — High · *Supported (official docs not retrievable for this snapshot)*
- **How:** register in **Baidu Ziyuan** (webmaster platform); let **Baiduspider** crawl; put critical content in **server HTML** — Baidu's JavaScript rendering is weaker than Google's (25, 127); use a Simplified Chinese site with `<html lang="zh-CN">`, ideally on its own domain or subdomain — Baidu isn't documented to support `hreflang`; write a real meta description; provide mobile versions with the mobile/PC relationship declared as Baidu requires.
- **Avoid:** relying on JS-rendered content, `hreflang` alone, or translated pages without localisation.

### W5. Hosting, ICP and Baidu AI search — High
- **How:** an **ICP filing** is legally required to host a site in mainland China; hosting in China and a `.cn` domain improve speed and local signals, but Baidu doesn't confirm them as ranking requirements — treat speed from mainland users as the measurable goal (CDN with mainland points of presence, no blocked third-party resources such as Google Fonts or Google-hosted scripts). Baidu now shows LLM answers in results and offers ERNIE in its app (ERNIE 5.0, November 2025); citation behaviour isn't documented for publishers.
- **Avoid:** loading resources from domains blocked in mainland China.

## Naver

### W6. Naver Search Advisor and the Naver ecosystem — High · *Supported*
- **How:** register in **Naver Search Advisor**; allow the **Yeti** crawler (blocking it removes you from Naver); submit changes through IndexNow (W1); expect Naver's own content (Blog, Cafe, Knowledge iN) to occupy much of the results — a presence there can complement the site, written with the same quality bar. **AI Briefing** (HyperCLOVA X, cited sources, rolled out to all users in May 2025) answers many queries directly.
- **Avoid:** assuming Google-only optimisation covers Korea.

## Seznam

### W7. Seznam — Medium · *Supported*
- **How:** register in Seznam's webmaster tool, let **SeznamBot** crawl (Seznam rolled out a new indexing robot; check the current user-agent string in its help), and use IndexNow (W1). Czech-language content, local links and Czech business listings matter as for any local market (136).

### W8. Market-specific listings and maps — Medium
- **How:** local businesses in these markets need the local map and listing platforms (Yandex Business/Maps, Baidu Maps, Naver Place, Mapy.cz from Seznam) alongside Google Business Profile, governed from one master record (`../verticals/local.md` L16, L18).

## Independent and alternative indexes

### W9. Brave Search — Medium · *Established*
- **How:** Brave runs an independent index with no fallback to another engine and sells it as an API (used for AI grounding). Its crawler has **no distinct user agent** and won't crawl what Googlebot can't: robots.txt rules for Googlebot effectively apply; use `noindex` to keep pages out. Brave also uses data from opt-in Web Discovery Project users.
- **Avoid:** trying to block Brave separately in robots.txt; blocking Googlebot also removes you from Brave.

### W10. DuckDuckGo, Yahoo and the European index (Ecosia, Qwant) — Medium
- **How:** DuckDuckGo's links come mostly from Bing plus its own crawler (**DuckDuckBot**) and indexes; Yahoo results are Bing-powered — so the Bing layer covers them (B1–B24). **EUSP**, the Ecosia–Qwant joint venture, builds its own European index (brand **Staan**): most Ecosia traffic in France and, since July 2026, a growing share in Germany is served from it, with a self-service API since June 2026. For French and German audiences, keep the site crawlable by non-Google/Bing crawlers and check server logs for their bots before blocking unknown agents in the WAF (A7).
- **Avoid:** WAF rules that only allow Googlebot and Bingbot.

### W11. Mojeek and Kagi — Low
- **How:** **Mojeek** is a fully independent UK index (crawler **MojeekBot**, 9+ billion pages in 2025). **Kagi** is a paid meta-search engine combining its own small indexes with major providers; it documents no crawler. Nothing special to do beyond the shared core and not blocking legitimate crawlers.

### W12. Apple: Applebot and Applebot-Extended — Medium · *Established*
- **How:** **Applebot** crawls for Spotlight, Siri and Safari features and its data may also ground Siri answers and train Apple models; **Applebot-Extended** doesn't crawl — disallowing it in robots.txt opts content out of Apple foundation-model training **without** affecting Apple search features. Decide it like other training agents (A2).
- **Avoid:** blocking Applebot when you only meant to opt out of training.

---

## Myths

| Claim | Assessment | Practice |
|---|---|---|
| "Yandex still needs the `Host` directive" | Removed from Yandex docs | 301 + canonical (W2) |
| "hreflang handles China" | Baidu isn't documented to support it | Separate zh-CN site with `lang`, localised (W4) |
| "You must host in China to rank on Baidu" | ICP is a legal requirement for China hosting; ranking effect isn't confirmed | Measure speed from the mainland (W5) |
| "Block every bot except Googlebot and Bingbot" | Hides you from Yandex, Naver, Seznam, EUSP, Mojeek and AI answer engines | Per-bot decisions, verified by UA and IP/DNS (A2, A7) |
| "You can block Brave in robots.txt" | Brave has no distinct UA and follows Googlebot rules | `noindex` if needed (W9) |

## Sources

Official (level A): [Yandex robots.txt](https://yandex.com/support/webmaster/en/controlling-robot/robots-txt.html) · [Yandex canonical/mirrors](https://yandex.com/support/webmaster/en/robot-workings/canonical.md) · [Yandex robots and verification](https://yandex.com/support/webmaster/en/robot-workings/check-yandex-robots.html) · [Yandex Neuro launch](https://yandex.com/company/news/16-04-2024) · [IndexNow participating engines](https://www.indexnow.org/searchengines.json) · [Naver AI Briefing](https://www.navercorp.com/en/story/storyDetail?seq=32526) · [DuckDuckGo result sources](https://duckduckgo.com/duckduckgo-help-pages/results/sources) · [EUSP](https://eu-searchperspective.com/) · [Ecosia — EUSP Germany rollout](https://blog.ecosia.org/eusp-germany-rollout/) · [Brave Search API](https://brave.com/search/api/) · [Brave Search crawler](https://search.brave.com/help/brave-search-crawler) · [About Applebot](https://support.apple.com/en-us/119829) · [Kagi search sources](https://help.kagi.com/kagi/search-details/search-sources.html) · [Mojeek](https://www.mojeek.com/about/).

Secondary (levels B–C, verify in the consoles): [Chinafy — Baidu technical SEO](https://www.chinafy.com/blog/technical-seo-checklist-for-baidu) · [Naver crawlers (51Degrees)](https://51degrees.com/blog/naver-crawlers-2026) · [Seznam new robot (Lupa.cz)](https://www.lupa.cz/tiskove-zpravy/seznam-cz-dokoncil-nasazeni-noveho-vyhledavaciho-robota/) · [Baidu AI in search (KrASIA)](https://kr-asia.com/baidu-integrates-ai-into-search-as-rivals-pursue-superapp-ambitions) · [Staan self-service API (onlinemarketing.de)](https://onlinemarketing.de/seo/europaeische-search-api-staan-jetzt-als-self-service) · [StatCounter search engine market share](https://gs.statcounter.com/search-engine-market-share).
