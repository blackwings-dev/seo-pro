# Video and image search layer (practices V1–V14)

Covers **video** in Google Search (video results, Video mode, key moments, LIVE badges) and on **YouTube** (search and recommendations), and **images** in Google Images, Discover thumbnails and image provenance. Read `README.md` in this folder first; it extends core practices 13, 14, 58, 122, 129 and 146, Bing B22, publishers P5/P15 and e-commerce E11.

Research snapshot: **18 October 2026**, checked against Google Search Central (video and image docs, updates log) and YouTube Help. Google Lens has no dedicated optimisation guide and Bing's image guidance couldn't be confirmed in its current docs: for both, follow the general image practices below and don't promise Lens- or Bing-specific effects.

Format: **Why** · **How** · **Avoid** · **Verify**.

---

## Video in Google Search

### V1. Build real watch pages — Critical · *Established*
- **Why:** Google defines a **watch page** as a page whose main purpose is to show users a single video. The page must itself be indexed and perform in Search before its video is considered; since December 2023, **Video mode** only shows pages where the video is the main content. A blog post with a supporting embed isn't a watch page — it can still get a text result or an image result with a video badge.
- **How:** one watch page per important video with a unique title and description, the player prominent and not hidden behind other elements or interactions, and supporting text (summary, transcript, chapters) below.
- **Avoid:** lazy-loading the player behind a click with no crawlable video; dozens of videos on one page expecting each to rank.
- **Verify:** Search Console **Video indexing** report (indexed watch pages with an indexed video, and reasons others weren't); Performance filtered to *Videos*.

### V2. `VideoObject` markup — High · *Established*
- **How:** required `name`, `thumbnailUrl`, `uploadDate`; recommended `contentUrl` (preferred) or `embedUrl`, `description`, `duration` (ISO 8601), `expires`, `hasPart` (`Clip`), `interactionStatistic`, `ineligibleRegion` **or** `regionsAllowed` (never both), `publication` (`BroadcastEvent`) and `creator` (added to the docs in September 2026; `author` still supported). Values match the visible page.
- **Verify:** Rich Results Test; Video rich result report.

### V3. Thumbnails and fetchable files — High
- **How:** thumbnails in BMP, GIF, JPEG, PNG, WebP, SVG or AVIF, at least 60×30 px (larger is better), at a stable URL that Googlebot and Googlebot-Image can fetch (no robots.txt block, no login), mostly opaque. Let Google fetch the video file (`contentUrl`) where you can — key moments via `SeekToAction` and some features need it.
- **Avoid:** thumbnails behind hotlink protection that blocks Google (129); rotating thumbnail URLs.

### V4. Video sitemaps and preview controls — Medium
- **How:** a video sitemap where `<loc>` is the **watch page**, with `video:thumbnail_loc`, `video:content_loc` or `video:player_loc`, optional `video:expiration_date` and `video:restriction`; Google also reads structured data and Open Graph. Control previews with `max-video-preview:[seconds]` (0 = static image, −1 = no limit).

### V5. Key moments — Medium · *Established*
- **How:** either `Clip` (name, `startOffset`, `url`; `endOffset` recommended; all Search languages) or `SeekToAction` (a target URL containing `{seek_to_second_number}`; limited languages; Google must be able to fetch the video). Videos at least 30 seconds, working deep links, no two clips with the same start. Google prioritises publisher-set moments (markup or YouTube description timestamps); opt out with `nosnippet`.

### V6. Livestreams — Low (High for live publishers)
- **How:** `BroadcastEvent` in `publication` with `isLiveBroadcast`, `startDate` and `endDate` once it ends. Google's video docs say to use the **Indexing API** when a stream starts, ends or its markup changes — livestreams (`BroadcastEvent`) and job postings are the only uses the Indexing API allows (myths).

### V7. Video and SafeSearch — Medium
- **How:** sites hosting explicit video should let Googlebot fetch it and label it correctly; Google's June 2025 SafeSearch changes warned that blocking fetches of explicit video can hurt visibility, especially in Video mode. New crawlers `GoogleOther-Image` and `GoogleOther-Video` (May 2024) are for non-Search fetches — don't confuse them with Googlebot.

---

## YouTube

### V8. How YouTube ranks search results — High · *Established (YouTube Help)*
- **Why:** YouTube says search ranking rests on **relevance** (how well title, tags, description and video content match the query), **engagement** (e.g. watch time for that query) and **quality** (channels showing expertise, authoritativeness and trustworthiness), with weights varying by query; results can be personalised and placement can't be bought. Recommendations use viewing behaviour, likes, dislikes, subscriptions and feedback including satisfaction surveys.
- **How:** titles and descriptions that state the topic in the viewer's words (and match what the video delivers); a strong opening that earns watch time honestly; topical consistency across a channel; links between YouTube and the site (watch pages on the site can embed the same video, V1).
- **Avoid:** misleading titles or thumbnails — they may win clicks and lose watch time and trust.

### V9. Chapters, captions and languages — Medium
- **How:** chapters with the first timestamp at 00:00, at least three ascending timestamps and chapters of at least 10 seconds (automatic chapters aren't guaranteed and are unavailable with active strikes or some restricted content); upload or edit captions — auto-captions exist only in the default language; for multilingual reach, review **auto-dubbing** (on by default for eligible creators, labelled "auto-dubbed", not available over 120 minutes, for little/no speech or copyrighted content; creators can switch to manual publishing to review) and translated titles/descriptions. YouTube frames captions and dubbing as reaching a larger audience — not as ranking boosts.

### V10. Test & compare titles and thumbnails — Medium
- **How:** YouTube's **Test & compare** tests a title, thumbnail or both with up to three variants; the winner is chosen by **watch-time share**, not CTR; if there's no winner, the first variant is used. Desktop Studio with advanced features; not for Shorts, kids, mature, private or 18+ videos, scheduled Lives or Premieres until they convert. Shorts are uploads up to 3 minutes in square or vertical format.

### V11. AI disclosure on YouTube — High · *Established*
- **How:** disclose realistic altered or synthetic content with the "AI use" setting at upload. YouTube may label automatically (its own GenAI tools, C2PA metadata, manual review) and creators can't remove those labels. Not required for unrealistic content or minor edits (filters, colour, captions, upscaling, scripting). YouTube says disclosure alone doesn't limit reach or monetisation; repeatedly failing to disclose can lead to penalties, including removal from the Partner Program.

---

## Images

### V12. Google image best practices — High · *Established*
- **How:** images in `<img src>` (Google doesn't index CSS background images); a `src` fallback for `srcset`/`<picture>`; short descriptive filenames; images near relevant text and captions; descriptive `alt` — Google calls it the most important attribute — without keyword stuffing (58); a consistent URL for each image across the site (May 2025 guidance); supported formats BMP, GIF, JPEG, PNG, WebP, SVG and AVIF; image sitemaps may list CDN URLs on other domains; dimensions and responsive sizes for CLS and LCP (13, 14, 122).
- **Avoid:** text baked into images instead of HTML; lazy-loading the LCP image.

### V13. Preferred images, Discover and previews — High
- **How:** since March 2026 Google documents that it uses schema.org image markup (`primaryImageOfPage`, the main entity's `image`) **and** `og:image` to choose thumbnails for Search and Discover — pick a relevant, high-resolution, representative image; avoid generic logos, text-heavy images and extreme aspect ratios. Discover large previews need images at least 1,200 px wide and `max-image-preview:large` (P5). `max-image-preview` accepts `none`, `standard` or `large`.

### V14. Licensing and provenance metadata — Medium · *Established*
- **How:** for the **Licensable** badge in Google Images, add image license structured data (`contentUrl` plus at least one of `creator`, `creditText`, `copyrightNotice` or `license`; `license` is needed for the badge, `acquireLicensePage` recommended) or IPTC fields embedded in the file (Web Statement of Rights required, Licensor URL recommended); structured data wins if they conflict. For AI provenance, Google reads IPTC `DigitalSourceType` (`trainedAlgorithmicMedia`, `compositeWithTrainedAlgorithmicMedia`) and can extract **C2PA** metadata for *About this image* (how an image was created or edited with AI tools). Keep metadata through your image pipeline — many CDNs and optimisers strip it.
- **Avoid:** promising a visible "AI-generated" label in Search results; Google documents provenance in About this image.

---

## Myths

| Claim | Assessment | Practice |
|---|---|---|
| "YouTube tags matter a lot" | YouTube says tags play a minimal role in discovery (mainly misspellings); excessive tags breach spam policy | Title, thumbnail, description, content (V8) |
| "Embedding a YouTube video boosts your page's ranking" | No official support; a page where video is secondary isn't a watch page | Embed when it helps users; build watch pages for video search (V1) |
| "Captions and dubbing boost YouTube ranking" | Unconfirmed; YouTube says they reach more people | Do them for audience and accessibility (V9) |
| "Test & compare picks the highest-CTR thumbnail" | It uses watch-time share | Test honest variants (V10) |
| "AI disclosure reduces reach" | YouTube says it doesn't by itself | Disclose realistic synthetic content (V11) |
| "Google indexes CSS background images" | It indexes `<img src>` images | Use `<img>` for content images (V12) |

## Sources

Google (level A): [Video SEO best practices](https://developers.google.com/search/docs/appearance/video) · [Video is the main content (Dec 2023)](https://developers.google.com/search/blog/2023/12/video-is-the-main-content) · [Video structured data](https://developers.google.com/search/docs/appearance/structured-data/video) · [Robots meta tag (max-video-preview, max-image-preview)](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag) · [Google Images best practices](https://developers.google.com/search/docs/appearance/google-images) · [Image license metadata](https://developers.google.com/search/docs/appearance/structured-data/image-license-metadata) · [Discover](https://developers.google.com/search/docs/appearance/google-discover) · [Search documentation updates](https://developers.google.com/search/updates).

YouTube (level A): [How YouTube search works](https://support.google.com/youtube/answer/16090438) · [Recommendations](https://www.youtube.com/howyoutubeworks/recommendations/) · [Chapters](https://support.google.com/youtube/answer/9884579) · [Captions](https://support.google.com/youtube/answer/2734796) · [Auto-dubbing](https://support.google.com/youtube/answer/15569972) · [Test & compare](https://support.google.com/youtube/answer/16391400) · [Altered or synthetic content disclosure](https://support.google.com/youtube/answer/14328491) · [Tags](https://support.google.com/youtube/answer/146402).
