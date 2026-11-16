---
description: Generate JSON-LD for a page or page type from what the page really contains, with TODO markers instead of invented data
argument-hint: <url or page type, e.g. https://example.com/product/x | Product | LocalBusiness>
---

Create structured data (JSON-LD) for `$ARGUMENTS` with the **seo-pro** skill. Load the skill first and follow practice 59 in `references/phase-2-content.md`, plus the vertical reference that matches the page type (`verticals/ecommerce.md`, `verticals/local.md`, `verticals/publishers.md`, `verticals/saas-services.md`) and `references/nextjs.md` or `references/other-stacks.md` for where the markup goes in the project.

Hard rule: **never invent data.** Ratings, review counts, prices, availability, addresses, phone numbers, opening hours, authors and dates are used only if they are visible on the page or provided by the user. Anything missing becomes a `"TODO: ..."` value and is listed at the end; a TODO value must never ship, so say that the block is not ready until they are resolved.

1. **Find the source of truth.**
   - If `$ARGUMENTS` is a URL, fetch it (`curl -s URL`) and read the title, headings, visible text, images, prices and any JSON-LD already present. Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/seo_audit.py" URL --render` when the content may only exist after JavaScript.
   - If it is a page type, ask for the real business data you need, or read it from the project's code or content; do not fill gaps with plausible values.
2. **Choose the types** that match the page's main content and that Google still supports for rich results (FAQ results were retired in 2026; do not add them expecting a rich result). Prefer one connected `@graph` with stable `@id`s over loose blocks. Do not mark up content that is not visible on the page.
3. **Write the JSON-LD**, using the framework's native place for it in this project (read the stack reference first). Use absolute URLs and ISO 8601 dates.
4. **Validate against the page**: for each type, list the required and recommended properties and mark each as `from the page`, `from the user` or `TODO`. Check that every value matches what a visitor sees. Parse the JSON to confirm it is valid.
5. Report: the block, the property table, the TODO list, and the checks to run (Rich Results Test, schema.org validator, then the seo-pro auditor on the live URL after deploy). State that markup makes a page eligible for a rich result and does not guarantee one.
