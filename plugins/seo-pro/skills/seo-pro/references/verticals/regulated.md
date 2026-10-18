# Regulated and high-impact topics layer (practices Y1–Y16)

Covers sites that publish information or sell products where an error can cause personal, financial, legal or social harm: **health** (clinical services, treatments, medicines, devices, supplements, mental health, nutrition, apps), **finance** (banking, credit, investment, insurance, pensions, mortgages, crypto, tax), **legal** (firms, forms, rights information, claims, client acquisition) and other sensitive areas (safety, emergencies, immigration, employment, housing, education, public services, elections, child protection). Read `README.md` in this folder first; it extends core practices 39, 102–103, 106, 111, 147 and 157.

Research snapshot: **18 October 2026**. **Not medical, financial or legal advice**, and no substitute for local regulatory review. Rules are jurisdictional: record country, product, channel and date of every check.

**The thesis.** The goal isn't to "optimise YMYL" as a ranking trick. It's to publish information that is accurate, understandable, current, verifiable and fit for purpose; to show who is accountable for it; and to put controls in place so SEO never amplifies a wrong claim. Visibility never justifies lowering the standard of truth, safety or the person's freedom to decide.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**.

## Contents
- Concepts to get right
- Classify by intent and risk: Y1–Y2
- Editorial governance: Y3–Y5
- Evidence and safe writing: Y6–Y8
- Sector rules: Y9–Y11
- Technical SEO and decision design: Y12–Y13
- Generative AI in YMYL: Y14
- Lifecycle, corrections and measurement: Y15–Y16
- Myths · 90-day sequence · publication checklist · sources

---

## Concepts to get right

- **YMYL** ("Your Money or Your Life") is Google's conceptual category for topics that can affect health, financial stability, safety or society. It's not a tag you add to a page or a filter with a published score.
- **E-E-A-T** (experience, expertise, authoritativeness, trust) is a framework. Google says it isn't a specific ranking factor, though its systems give more weight to signals aligned with strong E-E-A-T on high-impact topics. **Trust** is the centre.
- **Quality Rater Guidelines** guide human raters who help evaluate whether Google's systems work; raters don't set rankings and their ratings aren't used directly to rank pages.
- **Credentials** must be real and relevant; transparency doesn't replace accuracy.
- **A disclaimer** states scope and limits; it doesn't neutralise false information, misleading advertising, licensed advice or an interface that pushes a harmful decision.

---

## Classify by intent and risk

### Y1. Risk comes from the decision the reader can take — Critical
- **How:** before keyword research, classify each page by the decision it may induce, and agree an internal scale (low / medium / high / critical) — never presented as a Google classification:

| Type | Example | Usual risk | Minimum control |
|---|---|---|---|
| Educational definition | "What APR means", "what migraine is" | Low–moderate | Reliable source, date, plain language |
| General guidance | "When to see a doctor about persistent pain", "how to compare mortgages" | Moderate–high | Expert review, limits, escalation signals |
| Product/action recommendation | "Best supplement for X", "invest in this asset", "file this claim" | High | Evidence and advertising rules, conflicts, professional review, alternatives and risks |
| Personalisation or calculation | Policy selector, symptom checker, dose calculator, credit eligibility | High | Functional validation, case tests, limits, security, regulatory review |
| Acquisition in a vulnerable moment | Urgent treatment, debt, accident, immigration, crisis | Very high | Ethical/legal review, no pressure, emergency and official resources first |
| User story / testimonial | Clinical case, client review, investment story | High | Consent, privacy, disclosure, never used as general evidence |

  Risk rises with severity, urgency, scale, irreversibility, vulnerable audiences, technical complexity, lower user understanding and commercial incentive.
- **Verify:** every high-risk URL has a risk level in the inventory.

### Y2. A responsibility record per URL or page group — High
- **How:** record purpose and intent; audience and jurisdiction; risk level; author; reviewer; business owner; evidence base; commercial conflict; review date and triggers; who can pause, correct or `noindex` unsafe content.

---

## Editorial governance

### Y3. Roles and separation of duties — Critical
- **How:** for high-risk pages, at least: editor/owner (purpose, clarity, maintenance); domain expert (technical accuracy); compliance/legal/regulatory (claims, disclosures, jurisdiction, acquisition); SEO/product (architecture, discovery, measurement — never overrides a safety decision); operations (prices, availability and support are real); a publication approver who resolves disagreements and records the decision. One person may hold several roles in a small organisation, but critical review needs an independent check where potential harm is significant (`../playbooks/governance.md` G2).
- **Avoid:** an automatic "reviewed by" that pretends independence.

### Y4. Minimum editorial flow — High
1. Classify risk, intent, jurisdiction, user group and likely action (Y1).
2. Brief with the real question, primary sources and content limits.
3. Separate facts, interpretation, general advice, advertising and calls to action.
4. Write with proportional evidence; record sources per relevant claim with access date.
5. Review by the right expert; second review by compliance when needed.
6. Comprehension test: read as a non-expert — what decision does the whole page suggest?
7. Web QA: content, metadata, structured data, links, accessibility and CTA match the approved version.
8. Publish with authorship, review, date, scope, conflicts and correction channel visible as fits the page type.
9. Watch incidents, policy/evidence changes and real user feedback.
10. Review, correct, archive, redirect or retire; keep a change log with reasons.

### Y5. A claims ledger — High
- **How:** for commercial or high-impact content, an internal table: ID · public claim · type (efficacy / safety / legal / performance / price) · evidence and URL · population/product/country · reviewer · limitations · status and date. Include claims in the title, meta description, images, testimonials, FAQs, schema, ads, CTAs and potential snippets. A footer disclaimer doesn't fix the net impression of an absolute headline.

---

## Evidence and safe writing

### Y6. Claim and proof in proportion — Critical
- **How:** before publishing, check what is stated and what inference it invites; whether evidence matches the product, service, population and outcome described; design quality, comparator, size, duration and limits; contradictory guidance and how it's resolved; practical (not just statistical) relevance; whether association, prediction and causation are distinguished; whether someone could substitute the content for a consultation, treatment, advice or urgent help. Typical source order: current official rules and warnings → recognised professional guidelines and consensus → systematic reviews and original studies → experts interpreting the body of evidence → individual experiences (as experience, not proof) → commercial content with conflicts declared.
- **Example rule (US):** the FTC's Health Products Compliance Guidance requires health claims to be backed by competent and reliable scientific evidence. In the EU and Spain, check rules on health advertising, medicines, medical devices, food/supplements and regional rules.

### Y7. Write uncertainty without losing clarity — High
- **How:** say what is known and not known; avoid absolutes ("cures", "guaranteed", "no risk", "suitable for everyone") unless specifically permitted and proven; define who it applies to, when it doesn't and which signs need professional attention; explain technical terms; don't hide a contraindication in a collapsed accordion; cite sources next to important claims; don't call a single exploratory study or a testimonial "proven"; no images, badges or percentages that convey more certainty than the text.

### Y8. Verifiable authors, reviewers and sources — Critical
- **How:** name and role of author and reviewer; degree, specialty, body, licence and jurisdiction where they exist, without inflation; scope of the review (medical, legal, financial accuracy — not individual advice); editorial policy, funding, affiliate links, conflicts and sponsorship; publication date and date of substantive review; sources and method for comparisons, calculators, surveys or product tests; contact, corrections and complaints (102, 103, 157). Link current primary sources in the right jurisdiction.
- **Avoid:** invented professionals, expert accounts, "peer-reviewed" claims, awards, associations or quotes; using a professional as decoration without their approval and disclosure of the relationship.

---

## Sector rules

### Y9. Health and wellbeing — Critical
- **Risks:** wrong diagnosis or treatment, abandoning care, wrong dose, false reassurance, delayed emergency care, cure claims, exposure of sensitive data.
- **Controls:** review by a clinician competent in the specific topic against current guidelines; state population, age, pregnancy, interactions, limits and when to seek professional or emergency care; separate general information from individual assessment, diagnosis or prescription; no testimonials or before/after as proof of efficacy; no prevent/treat/cure claims that can't be supported and aren't permitted; protect images, records and consent (anonymisation isn't infallible); emergency pages lead with the immediate action and official resources, before any monetisation; medical translations reviewed by an expert translator and a local professional (machine translation can invert a dose, frequency or negation). The WHO's credibility principles (science, objectivity, transparency, accountability) are useful editorial criteria, not an SEO algorithm.

### Y10. Finance, investment, credit and insurance — Critical
- **Risks:** capital loss, harmful debt, unsuitable sales, fraud, conflicts, investment recommendations disguised as education, selective performance.
- **Controls:** specify product, market, jurisdiction, date, eligibility, fees, conditions and material risks; separate historical data, assumption, simulation, forecast and guarantee — past performance is never a promise; disclose affiliate links, commissions, positions and sponsorship; review claims of return, safety, "no risk", approved credit or savings; don't bury risks in small print; no artificial urgency around volatile assets or vulnerable debt situations; calculators show assumptions, rates, dates and ranges, without false precision; check the provider's authorisation and registration and link official warnings.
- **Regulatory examples:** ESMA warns that public posts suggesting buying or selling instruments can be investment recommendations subject to objective-presentation and disclosure rules, and that "this isn't advice" doesn't settle the classification; ESMA's 2026 finfluencer factsheet and the CNMV's resources give EU/Spanish guidance; in the US the SEC Marketing Rule sets conditions for testimonials and endorsements by registered advisers. Don't extrapolate between regimes.

### Y11. Legal services and other sensitive areas — Critical
- **Legal risks:** wrong answer for the jurisdiction or facts, missed deadlines, false expectations, targeting vulnerable people, breaching confidentiality, confusing information with a lawyer–client relationship.
- **Legal controls:** state jurisdiction, effective date and area of law; cite current law and case law; say outcomes depend on facts and exceptions without using that as cover for vague content; never promise success, compensation, timing or results; protect privilege and client identity; state what a form does and doesn't create, how documents are protected and who responds; no pressure in accident, eviction, immigration, violence or dismissal contexts; check bar rules on advertising, testimonials, results, fees and rankings (in Spain, the Código Deontológico de la Abogacía Española 2019 requires objective, truthful and dignified advertising that preserves independence and professional secrecy).
- **Other areas:** insurance/fintech/crypto (licences, warnings, volatility; never present complex products as guaranteed deposits); pharmacy, devices and supplements (authorisation, permitted claims, labelling, sales channels); immigration and rights (country and validity, no false guarantees, official sources, no coercive acquisition); employment, housing and credit (discriminatory language, eligibility, automated criteria); safety and emergencies (current official instructions first, no monetisation interrupting critical action); children and education (age-appropriate language, consent, protect minors' data); civic and political topics (separate information, opinion, advertising and sponsorship; visible corrections).

---

## Technical SEO and decision design

### Y12. Indexing, snippets and structured data — High
- **How:** `title`, H1, meta description and Open Graph describe the real content and don't turn a limited claim into an absolute promise; main content and essential limitations in accessible HTML; canonical, hreflang, robots and sitemap reflect the approved version, language and country; dangerous outdated pages are updated, retired, redirected to a current guide or given the right status — not kept for traffic; no near-identical doorway pages per city or legal condition, and no acquisition pages for services not available locally; experimental calculators or landings with unvalidated claims stay out of the sitemap. Markup matches visible content and the real entity: don't add `MedicalWebPage`, `Physician`, `FinancialProduct`, `Review`, ratings or licences to fake eligibility or reputation — schema doesn't validate a claim, create a licence or guarantee rich results.

### Y13. Accessibility and decision design — High
- **How:** contrast, readable language, keyboard navigation, headings and form labels (35, 36); limits, risks, costs and requirements near the recommendation or CTA; no fake countdowns, misleading preselection, coerced consent, dark patterns or neutral-looking buttons that trigger a financial or medical action (111); alternatives and support easy to find; tools show version, assumptions, uncertainty range, sources and review date; urgent content never depends on cookies, registration or subscription.

---

## Y14. Generative AI in YMYL — Critical
- **Allowed as internal assistance:** classification, evidence summaries, glossaries, structural drafts, preliminary translation, link QA, detecting uncited claims — each reviewed by a competent person. AI is neither a primary source nor a professional reviewer.
- **Mandatory controls:** no sensitive or personal data in tools without authorisation, contract and assessment; check every citation (models invent studies, authors, laws, doses, dates and exceptions); compare against current primary sources in the right jurisdiction; control omissions, bias, ambiguity, negation, units and numbers; publish who is accountable and how it was reviewed — never attribute unreviewed text to a professional; keep model/process history where audit needs it; don't scale hundreds of pages behind a superficial review (scaled content abuse applies however the content is produced); ask whether it should be published, not only whether it can be produced.

---

## Lifecycle, corrections and measurement

### Y15. Risk-based review triggers and corrections — Critical
- **Triggers that force an early review:** a change in clinical guidance, law, regulation, price, eligibility, product or warning; new evidence; incidents, complaints, reported harm, product recalls or court decisions; a change of reviewer, licence, affiliation or commercial relationship; technical changes in calculators, forms, routing, payments, consent or providers; broken or replaced official links, a new translation or market; a sudden traffic spike to a crisis page that changes its real function. There's no universal interval: a calendar is a cadence, not permission to ignore an event.
- **Corrections:** a visible route and an owner for reports of factual errors or unsafe advice, impersonation or false licences, privacy issues, commercial/legal review, and pausing a CTA or page during investigation. When correcting, keep the date and a description of the change; make the correction visible and proportionate if decisions may have been affected; never hide a substantive error by changing `dateModified` or the publish date. For high-risk pages, version the editorial and published copies with reviewers, evidence, date and reason; for interactive tools, also code, parameters, tests and validation results.

### Y16. Balanced metrics and harmful-content incidents — High
- **Metrics:** discovery (impressions, clicks, queries, coverage); usefulness and safety (helpful/not helpful feedback, errors found, corrections, support escalations, accessibility, abandonment of critical steps, calculator failures, harm reports); business (valid conversions, qualified leads, contracted consultations, sales, retention); editorial quality (source freshness, review time, share of risky pages with a reviewer, valid official links, claims with evidence, errors by severity); trust (risk comprehension, complaints, resolution, sponsorship transparency).
- **Avoid perverse incentives:** paying authors or reviewers on rankings or conversion; optimising conversion rate without guardrails on complaints, refunds, cancellations, adverse outcomes or risk comprehension; creating automatic treatment or advice pages from query data.
- **Incident:** if a potentially harmful page becomes visible — assess harm and pause the claim/CTA; confirm facts with the responsible professional; correct or withdraw, checking caches, snippets, schema and feeds; show a notice if users may have relied on it; review ads, syndicated copies and external spread; find the root cause (brief, review, CMS, AI, incentives, supplier); document without naming people unnecessarily.

---

## Myths

| Claim or practice | Why it fails | Responsible criterion |
|---|---|---|
| "E-E-A-T is a score; get it to 90" | Not a specific ranking factor or public scale | Show experience, expertise, accountability and trust to people |
| "Add a doctor/lawyer to the page to rank" | Decorative credentials don't prove review or accuracy | A real, competent reviewer with explicit scope and accountability |
| "A disclaimer lets us recommend anything" | Doesn't change substance, impression or legal classification | Review claim, product, audience, context and obligations |
| "This patient/client story proves it works" | One experience isn't general efficacy | Present as individual experience, consented and disclosed |
| "Publish 500 pages, more volume converts" | At high risk, scale amplifies errors; may be scaled content abuse | Only differentiated, reviewed, maintainable content |
| "Update the date to signal freshness" | A false date misleads and breaks traceability | Update after substantive review; record what changed |
| "'Educational' or 'not advice' removes regulation" | Content can function as a recommendation by substance | Classify under local rules and how the audience reads it |
| "Third-party ads and widgets aren't our responsibility" | The site distributes their claims and impression | Review ads, affiliates, widgets and comments |
| "Schema makes Google trust the professional" | Schema describes; it doesn't accredit or rank | Accurate, visible, eligible markup only |
| "Rankings prove the advice is correct" | Ranking isn't clinical, legal or financial review | Expert review and safety have authority independent of traffic |

## 90-day sequence

- **Days 1–15 — map and controls:** inventory URLs, products, calculators, lead forms, testimonials, affiliates and social posts; classify by topic, jurisdiction, intent and risk; identify owners, authors, reviewers, claims and sources; prioritise urgency, treatment, investment, debt, litigation and irreversible decisions; create pause, correction and escalation mechanisms.
- **Days 16–35 — policy and evidence:** approve source hierarchy, review SLA, claims ledger and disclosures; review the highest-impact pages with relevant professionals; fix authors, credentials and undisclosed conflicts; remove absolute or outdated claims and repair primary-source links; check jurisdiction, eligibility, disclaimers, forms and CTAs.
- **Days 36–60 — experience and architecture:** make crisis/urgency pages help before they sell; place risks, costs and limits near the action; audit schema, metadata, indexing, translations, accessibility and local landings; reduce duplication and under-reviewed programmatic pages; test calculators, price changes and critical flows.
- **Days 61–90 — maintenance and measurement:** activate the review calendar and triggers; a dashboard for coverage, accuracy, complaints, corrections, conversion and guardrails; train SEO, content, PR, sales, support, affiliates and agencies; run a drill for a wrong claim or regulatory alert; publish editorial and corrections policies where they add transparency.

## Sensitive-page publication checklist

**Before writing**
- [ ] Purpose, audience, country, intent and likely action defined.
- [ ] Internal risk level and required reviewers set.
- [ ] Current official/primary sources identified.
- [ ] Commercial relationships, affiliate links, funding and conflicts declared.

**Editorial and professional review**
- [ ] Each relevant claim has evidence matching product, population, country and date.
- [ ] Title and CTA don't overstate the evidence or create false urgency.
- [ ] Data, risks, contraindications, limits and alternatives explained.
- [ ] Author and reviewer are real people with verifiable credentials and correct scope.
- [ ] Education, advertising, opinion and individual advice are separated.
- [ ] Applicable regulator, bar or country rules applied.

**Web QA and maintenance**
- [ ] Snippet, images, schema and visible content say the same.
- [ ] Critical pages and resources are accessible, readable and crawlable where appropriate.
- [ ] Contact, support, corrections and complaints route exist.
- [ ] Review date and triggers, owner and approved version recorded.
- [ ] CTA and conversion have guardrails for quality and potential harm.

## Sources

Google (level A): [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Search Quality Rater Guidelines](https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf) · [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies) · [Guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) · [Review snippet structured data](https://developers.google.com/search/docs/appearance/structured-data/review-snippet).

Health: [WHO — using the internet and media for health information](https://www.who.int/tools/your-life-your-health/how-to-find-and-use-health-information/using-the-internet-and-the-media-to-get-health-information) · [WHO/NAM — principles for credible health sources](https://www.who.int/teams/digital-health-and-innovation/digital-channels/phase-ii--global-principles-for-identifying-credible-sources-of-health-information-on-social-media) · [FTC Health Products Compliance Guidance](https://www.ftc.gov/business-guidance/resources/health-products-compliance-guidance).

Finance and legal: [ESMA — investment recommendations on social media](https://www.esma.europa.eu/document/warning-posting-investment-recommendation-social-media) · [ESMA finfluencers factsheet (2026)](https://www.esma.europa.eu/sites/default/files/2026-01/Finfluencers_factsheet_EN.pdf) · [CNMV investor portal](https://internet.cnmv.es/Portal/Inversor/Indice?lang=es) · [SEC — Investment Adviser Marketing](https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/investment-adviser-marketing) · [Código Deontológico de la Abogacía Española (2019)](https://www.abogacia.es/wp-content/uploads/2019/05/Codigo-Deontologico-2019.pdf).
