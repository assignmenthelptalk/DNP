# Page Brief: Technical SEO Audit Kenya

**Client:** Tupate Studio
**Date:** 2026-03-17
**Topical Map Position:** Core Section — Tier 2
**Attribute Focus:** Search Visibility — diagnosing and fixing technical barriers preventing Kenyan websites from ranking

---

## 1. PAGE IDENTITY

| Field | Value |
|-------|-------|
| **URL Slug** | `/technical-seo-audit-kenya` |
| **H1** | Technical SEO Audit for Kenyan Business Websites: Find and Fix What's Stopping Your Rankings |
| **Meta Title** | Technical SEO Audit Kenya \| Find Why You're Not Ranking \| Tupate Studio |
| **Meta Description** | Technical SEO audit for Kenyan business websites. Crawlability, Core Web Vitals, schema markup, indexation. We find what's stopping your rankings and fix it. Ksh 8,000/month. |
| **Target Word Count** | 2,400–2,900 words |
| **Content Type** | Service page (high-intent commercial + technical education) |
| **Priority** | HIGH — hub page that supports all SEO-related pages via internal links |

---

## 2. QUERY CONTEXT

### Represented Queries (what users type)
- SEO audit Kenya
- technical SEO audit Nairobi
- website SEO audit Kenya
- why is my website not ranking Kenya

### Representative Queries (how Google interprets them)
- "website technical issues preventing ranking Kenya"
- "Google Search Console errors Kenya"
- "Core Web Vitals audit Kenya"
- "crawlability issues website Kenya"
- "website indexation problems Kenya"
- "schema markup audit Kenya"
- "website speed audit Kenya"
- "SEO audit cost Kenya"
- "website not appearing on Google Kenya"

**Instruction:** This page captures high-intent "something is wrong" searches. The primary persona is a Kenyan business owner whose website is not ranking despite having a site — or whose rankings have dropped unexpectedly. The page must diagnose the problem, explain what a technical audit covers, and position Tupate Studio as the solution.

---

## 3. SOURCE CONTEXT CONNECTION

The technical SEO audit is both a standalone service and the entry point for Tupate Studio's SEO retainer. Every section reinforces:
> Technical issues block rankings → Tupate Studio identifies every technical barrier → fixes them systematically → website starts ranking → ongoing SEO retainer maintains technical health.

**Source Context N-grams:** "technical SEO," "SEO audit," "rankings," "Core Web Vitals," "Kenyan websites," "Google Search Console," "indexation," "schema markup."

---

## 4. CENTRAL ENTITY CONNECTION

**Central Entity:** Business Website (Kenya)
A technical SEO audit examines the technical health of the business website — its ability to be crawled, indexed, and ranked by Google. Frame every audit element as a property of the business website that either supports or undermines its Google performance.

---

## 5. MAIN CONTENT STRUCTURE

---

### H1: Technical SEO Audit for Kenyan Business Websites: Find and Fix What's Stopping Your Rankings

**Opening paragraph (60–80 words):**
Frame the problem: many Kenyan business websites have a fundamental technical reason they don't rank — and it has nothing to do with content or backlinks. Crawl errors, duplicate content, slow Core Web Vitals, broken schema markup, mobile usability failures — these are invisible to the business owner but fully visible to a technical SEO audit. Introduce Tupate Studio's audit as the diagnostic that finds and fixes these issues.

---

### H2: What a Technical SEO Audit Checks on a Kenyan Business Website

**Contextual directive:** Define the scope of a technical audit. Use a comprehensive list with explanations. This section builds trust by demonstrating systematic expertise.

**EAV depth required:**
- Entity: Technical SEO Audit
- Audit categories and what each covers:

**1. Crawlability**
- robots.txt: is Google blocked from crawling important pages? (Common error: robots.txt from staging that blocked all crawlers and was deployed to live site)
- XML sitemap: is it submitted to Google Search Console? Does it include all important pages? Are there 404 URLs in the sitemap?
- Crawl budget: for large sites (100+ pages), is Google wasting crawl budget on low-value pages (faceted search results, printer-friendly pages)?
- JavaScript rendering: does Google see the same content as users? SPAs (single-page applications) sometimes require JavaScript to render — Google may not crawl JS-heavy content correctly.

**2. Indexation**
- Google Search Console Coverage report: how many pages are indexed vs how many exist? Why are some pages excluded?
- Canonical tags: are self-referencing canonicals in place? Are there conflicting canonicals pointing to wrong URLs?
- noindex tags: are there important pages with noindex accidentally set? (Common: staging site had noindex set, production still has it)
- Duplicate content: does the site serve the same content at multiple URLs? (www vs non-www, HTTP vs HTTPS, trailing slash vs no trailing slash — if all resolve without redirecting to one canonical version, duplicate content exists)
- Thin content pages: pages with under 200 words that provide no value — may drag down overall site quality score

**3. Core Web Vitals (CWV)**
- Largest Contentful Paint (LCP): time for main content to appear. Target: <2.5 seconds. Kenyan websites often fail due to un-optimized hero images and slow hosting server response (TTFB).
- Interaction to Next Paint (INP): time from user interaction to visual response. Target: <200ms. Fails due to heavy JavaScript blocking the main thread.
- Cumulative Layout Shift (CLS): unexpected visual instability. Target: <0.1. Fails due to images without dimensions, web fonts loading and shifting text, ads or embeds that push content.

**4. Mobile Usability**
- Google Search Console Mobile Usability report: lists specific pages with mobile errors
- Text too small to read: body text below 12px (Google penalizes)
- Clickable elements too close together: touch targets not meeting 44px minimum
- Content wider than screen: horizontal scrolling caused by fixed-width elements

**5. HTTPS and Security**
- SSL certificate: is HTTPS active and correctly configured? Mixed content errors (HTTPS page loading HTTP resources)?
- HSTS: HTTP Strict Transport Security header — forces browsers to always use HTTPS
- Security headers: Content Security Policy, X-Frame-Options — not direct ranking factors but protect site authority from being compromised

**6. Structured Data (Schema)**
- Schema types present and correct: LocalBusiness, Organization, Product, Article, FAQ, Breadcrumb
- Schema validation: Google's Rich Results Test — are there errors or warnings?
- Schema opportunities: which pages are missing schema that would benefit rankings or rich results?

**7. Internal Linking**
- Orphan pages: pages with no internal links pointing to them (Google cannot find them through normal crawling)
- Link equity flow: are the most important pages receiving the most internal links?
- Anchor text diversity: are internal links using descriptive anchor text or generic "click here"?

**8. Page Speed**
- Google PageSpeed Insights: mobile and desktop scores with specific failing elements
- TTFB (Time to First Byte): measures server response time. Kenyan shared hosting often has TTFB of 800ms–2s — this alone fails LCP targets before the page even starts loading.
- Render-blocking resources: CSS or JavaScript in `<head>` that delays page rendering

**Word count target:** 550–620 words (this is the core educational section — the heart of the page)

---

### H2: Core Web Vitals for Kenyan Websites: LCP, INP, and CLS Explained

**Contextual directive:** Deeper dive on Core Web Vitals specifically — the most important technical ranking factor for Google since June 2021. Many Kenyan business owners have heard "Core Web Vitals" but don't understand what it means.

**EAV depth required:**
- Why CWV matters for Kenya specifically: Google uses CWV as a "Page Experience" ranking signal. Sites that PASS all three CWV signals get a ranking boost. Sites that FAIL are at a disadvantage.
- LCP deep dive:
  - What it measures: when the largest content element (usually hero image or H1 headline) becomes visible
  - Kenya-specific causes of LCP failure: un-compressed hero images (800KB+ JPEGs), slow Kenyan hosting (TTFB >600ms), render-blocking JavaScript, no CDN
  - Fix: compress hero image to <150KB WebP, optimize server response time, use Cloudflare CDN with African edge node, defer non-critical JavaScript
- INP deep dive:
  - Replaced FID (First Input Delay) in March 2024
  - What it measures: total delay from click/tap to visual response — measured across ALL interactions on a page
  - Kenya failure causes: heavy JavaScript frameworks, analytics scripts blocking main thread, WordPress plugin JavaScript conflicts
  - Fix: reduce JavaScript payload, defer third-party scripts, use lightweight vanilla JS
- CLS deep dive:
  - What it measures: unexpected layout shifts (page jumping as elements load)
  - Kenya failure causes: images without width/height attributes (browser doesn't reserve space), web fonts loading and shifting text, YouTube embeds that resize, cookie consent banners that appear without reserved space
  - Fix: always set explicit image dimensions, preload critical fonts, use aspect-ratio CSS for all media elements
- How to check CWV: Google Search Console → Experience → Core Web Vitals (field data) + PageSpeed Insights (lab data). Both needed for full picture.

**Word count target:** 380–440 words

---

### H2: Crawlability and Indexation Issues That Kill Kenyan Website Rankings

**Contextual directive:** Cover the two most common critical technical issues that completely prevent rankings — these are "invisible" to business owners but obvious in a technical audit.

**EAV depth required:**
- Real Kenya examples:
  1. **robots.txt blocking**: web developer deployed staging site's robots.txt (`Disallow: /`) to production. Google could not crawl ANY page. Site ranked for nothing. Discovered only after 6 months of zero traffic growth.
  2. **noindex on all pages**: developer left `<meta name="robots" content="noindex">` on all pages. Google was told not to index the site. Business owner thought Google "just hadn't found" the site yet.
  3. **Non-canonical duplicates**: both www.site.co.ke and site.co.ke served content without redirecting to a single version. Google split ranking signal between two URLs.
  4. **HTTP vs HTTPS split**: site had moved to HTTPS but old HTTP URLs were not redirected. Backlinks still pointed to HTTP. PageRank not transferred.
- Crawl error types in Google Search Console and what each means:
  - 404 Not Found: page URL exists in sitemap or has links pointing to it, but returns 404. Kills link equity and causes indexation gaps.
  - Redirect error: redirect chain is broken or leads to another redirect (chain too long)
  - Server error (500): hosting server crashed when Google tried to crawl — page cannot be indexed
  - Soft 404: page returns 200 HTTP status but content says "not found" — Google confusion
- How Tupate Studio finds these: Screaming Frog SEO Spider (full site crawl), Google Search Console Coverage report, manual URL testing

**Word count target:** 320–380 words

---

### H2: Schema Markup for Kenyan Business Websites: Types and Implementation

**Contextual directive:** Schema markup is one of the most under-implemented SEO elements on Kenyan websites. Cover the types and their direct business impact.

**EAV depth required:**
- Entity: Schema Markup (Structured Data)
- What schema does: communicates content type and meaning to Google in a machine-readable format → enables Rich Results (star ratings, FAQ dropdowns, product prices in search results) → improves click-through rates
- Schema types for Kenyan businesses:
  1. **LocalBusiness**: tells Google the business name, address, phone, hours, category. Critical for local SEO. Service businesses: `LocalBusiness` (or sub-type like `MedicalBusiness`, `LegalService`, `Restaurant`)
  2. **Organization**: for corporate websites. Adds logo, social profiles, founding date.
  3. **Product**: for e-commerce pages. Adds price, availability, ratings to search results.
  4. **FAQPage**: adds expandable FAQ dropdowns in search results. High CTR impact. Easy to implement — every FAQ section should have this.
  5. **BreadcrumbList**: shows page hierarchy in search result URL (Home > Services > SEO Audit). Improves navigation context in SERPs.
  6. **Article / BlogPosting**: for blog content. Adds publish date, author.
  7. **Service**: for individual service pages — connects service to the LocalBusiness entity.
- Implementation method: JSON-LD in `<script type="application/ld+json">` tags — recommended by Google, cleanest implementation, no markup in HTML body required
- Validation: Google's Rich Results Test and Schema.org Validator
- Common errors found in Kenyan websites: incomplete LocalBusiness schema (missing opening hours, missing area served), conflicting schemas from multiple SEO plugins (common WordPress issue), malformed JSON (syntax errors that invalidate the entire schema block)

**Word count target:** 320–380 words

---

### H2: Website Speed Audit: How Hosting in Kenya Affects Your Google Scores

**Contextual directive:** Kenyan hosting quality is a major technical SEO issue. Cover the TTFB (server response time) problem specifically for Kenyan-hosted websites.

**EAV depth required:**
- Entity: Web Hosting Performance (Kenya)
- TTFB (Time to First Byte): the time from a browser request to the first byte of response from the server. Google's recommended TTFB: under 800ms. Good: under 200ms.
- Kenya shared hosting reality: many Kenyan hosting providers (Truehost, Sasahost, Kenya Website Experts) operate shared servers with 300–600 customers on one server. At peak times: TTFB of 1,500–3,000ms — this alone exceeds Google's LCP threshold before any content loads.
- Hosting tiers comparison for Kenya:
  - Shared hosting (Ksh 500–2,000/month): 300–2,000ms TTFB typical. Acceptable for very simple sites. Unacceptable for SEO-focused businesses.
  - VPS (Virtual Private Server) (Ksh 3,000–8,000/month): 100–400ms TTFB typical. Recommended for businesses running SEO campaigns.
  - Managed cloud (AWS, Google Cloud, DigitalOcean): 50–150ms TTFB from nearest region (Africa — Frankfurt or Johannesburg nodes). Best performance.
- CDN (Content Delivery Network): Cloudflare free tier serves cached content from edge nodes including African ones (Johannesburg, Nairobi) — reduces TTFB to 50–100ms for repeat visitors even on slow origin hosting. Recommended for all Kenyan websites.
- What the audit includes: TTFB measurement from Nairobi IP address, PageSpeed Insights score, GTmetrix report, hosting provider assessment with specific recommendation
- Tupate Studio's hosting recommendation: communicated during audit — we do not lock clients to specific hosting providers but will recommend upgrades when hosting is clearly causing ranking problems

**Word count target:** 320–380 words

---

### H2: Technical SEO Audit Report: What You Receive and What We Fix

**Contextual directive:** Describe the deliverable. Converts informed readers to paying clients by showing exactly what they get.

**EAV depth required:**
- Audit report contents:
  1. **Executive summary**: top 5 critical issues with estimated ranking impact (ranked by urgency)
  2. **Crawlability section**: robots.txt analysis, sitemap audit, crawl error list from Google Search Console
  3. **Indexation section**: indexed page count vs total pages, noindex audit, canonical audit, duplicate content list
  4. **Core Web Vitals section**: LCP, INP, CLS scores for top 10 pages; specific failing elements; priority fix list
  5. **Mobile usability section**: Google Search Console mobile errors; screenshots of mobile UX issues
  6. **Schema markup section**: current schema types, validation errors, missing schema opportunities
  7. **Speed audit section**: TTFB measurement, PageSpeed Insights scores, hosting assessment
  8. **Internal linking section**: orphan pages, link equity flow map, anchor text audit
  9. **Priority fix list**: ranked list of all issues, estimated effort and impact
- What Tupate Studio fixes after the audit:
  - Included in SEO retainer (Ksh 8,000/month): implementation of all fixes identified in audit
  - One-time audit only: audit report delivered (Ksh 5,000 one-time) — client implements fixes themselves or hires a developer
- Timeline: audit completed in 5–7 business days for websites up to 100 pages. Larger sites (100–500 pages): 10–14 business days.

**Word count target:** 280–340 words

---

## 6. CONTEXTUAL BORDER

**Border Question:**
> "After fixing technical issues, what on-page content optimization does a Kenyan website need to rank for competitive keywords?"

**Border treatment (60–80 words):** Answer: technical health is the prerequisite — but ranking for competitive Kenyan keywords also requires on-page content optimization (matching pages to representative queries), local SEO (for local intent searches), and content strategy (topical authority building). Bridge to SEO Services and On-Page SEO pages. Technical SEO is necessary but not sufficient — it is the foundation on which all other SEO work is built.

---

## 7. SUPPLEMENTARY CONTENT STRUCTURE

---

### SUPP H2: On-Page SEO After the Technical Foundation Is Fixed

**Key points:**
- Once technical issues are resolved: title tags, meta descriptions, heading hierarchy, content depth, internal linking architecture
- Internal link: "SEO Services in Kenya" → `/seo-services-kenya`

**Word count target:** 150–180 words

---

### SUPP H2: Mobile-First Design and Technical SEO: The Connection

**Key points:**
- Mobile usability errors in Google Search Console = direct ranking penalty
- Custom-built mobile-first sites have fewer technical SEO issues than WordPress responsive sites
- Internal link: "Mobile-First Website Design Kenya" → `/mobile-first-website-design-kenya`
- Internal link: "Custom-Built Website vs WordPress Kenya" → `/custom-website-vs-wordpress-kenya`

**Word count target:** 130–160 words

---

### SUPP H2: Technical SEO Audit FAQs

**FAQ entries (FAQPage schema):**
1. Q: What is included in Tupate Studio's technical SEO audit? A: [A full audit covering crawlability, indexation, Core Web Vitals, mobile usability, schema markup, internal linking, and hosting performance. You receive a written report with a prioritized fix list within 5–7 business days.]
2. Q: Why is my website not appearing on Google in Kenya? A: [The most common causes for Kenyan websites not appearing on Google: robots.txt accidentally blocking crawlers, noindex meta tag on all pages, site not submitted to Google Search Console, website too new (less than 3 months), or no pages targeting the specific queries you want to rank for.]
3. Q: How much does a technical SEO audit cost in Kenya? A: [A one-time technical audit report is Ksh 5,000. If you are on Tupate Studio's SEO retainer (Ksh 8,000/month), the audit is included and all identified fixes are implemented as part of the monthly service.]
4. Q: How often should a Kenyan website have a technical SEO audit? A: [A full technical audit should be done: at website launch, after any major website change (redesign, platform migration), after a Google Core Update if rankings dropped, and as part of an annual SEO health check. On the monthly retainer, we perform mini-audits monthly and a full audit quarterly.]
5. Q: Can you audit a WordPress website in Kenya? A: [Yes — we audit WordPress websites and any other website platform. We identify the issues; the fix recommendation may include migrating to custom-built code if WordPress's structural limitations are causing the technical problems (e.g., plugin conflicts, Core Web Vitals failure due to plugin overhead).]

---

## 8. INTERNAL LINKS

| Anchor Text | Destination Page | Location |
|---|---|---|
| SEO Services in Kenya | /seo-services-kenya | Supp H2: On-Page SEO section |
| Mobile-First Website Design Kenya | /mobile-first-website-design-kenya | Supp H2: Mobile design connection |
| Custom-Built Website vs WordPress Kenya | /custom-website-vs-wordpress-kenya | Supp H2: Mobile design connection |
| Website Redesign Kenya | /website-redesign-kenya | H2: Audit what we check (mention of pre-redesign audit) |
| Local SEO for Kenyan businesses | /local-seo-kenya | Contextual Border paragraph |

---

## 9. SCHEMA MARKUP

```json
{
  "@context": "https://schema.org",
  "@type": ["Service", "LocalBusiness"],
  "name": "Technical SEO Audit Kenya",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Tupate Studio",
    "url": "https://tupate.studio"
  },
  "serviceType": "Technical SEO Audit",
  "areaServed": { "@type": "Country", "name": "Kenya" },
  "offers": [
    {
      "@type": "Offer",
      "name": "One-time Technical SEO Audit Report",
      "priceCurrency": "KES",
      "price": "5000"
    },
    {
      "@type": "Offer",
      "name": "Monthly SEO Retainer (includes ongoing technical auditing)",
      "priceCurrency": "KES",
      "price": "8000"
    }
  ]
}
```

Also add: **FAQPage** schema on FAQ section, **BreadcrumbList** schema.

---

## 10. TECHNICAL SEO DIRECTIVES

- **Title tag:** `Technical SEO Audit Kenya | Find Why You're Not Ranking | Tupate Studio` (65 chars)
- **Meta description:** 148–155 chars, includes "audit," "Kenya," "Core Web Vitals," "rankings," price signal
- **URL:** `/technical-seo-audit-kenya`
- **H1:** Includes primary query "Technical SEO Audit" + "Kenyan" + outcome "Find and Fix"
- **This page is a hub page** — it receives internal links from all other SEO-adjacent pages and passes authority back to the SEO Services page

---

## 11. CONTEXTUAL COVERAGE DIRECTIVES

| Section | Coverage Weight | Reason |
|---|---|---|
| What a technical audit checks (full scope) | 22–25% | Core educational section — largest word count, most queries addressed |
| Core Web Vitals deep dive | 16–18% | Most important technical ranking factor — deserves full treatment |
| Crawlability and indexation | 13–15% | Most common critical issues found in Kenyan websites |
| Schema markup | 12–14% | Under-implemented in Kenya — high opportunity differentiation |
| Hosting and speed | 12–14% | Kenya-specific issue — shared hosting TTFB is unique local problem |
| Audit report deliverable | 10–12% | Conversion section |
| Supplementary sections | 10–12% | Contextual bridges |

---

## 12. CONTEXTUAL FLOW ORDER

1. What a technical audit covers (comprehensive scope — establishes authority and diagnoses the problem space)
2. Core Web Vitals (LCP, INP, CLS) — most important ranking technical factor — expanded treatment
3. Crawlability and indexation — most common "invisible" critical issues
4. Schema markup — under-utilized opportunity for Kenyan websites
5. Hosting and server speed — Kenya-specific TTFB problem
6. Audit report and deliverable — conversion section
7. Contextual Border
8. Supplementary: on-page SEO bridge → mobile design connection → FAQs

**Rationale:** Opens with the full diagnostic picture (establishes comprehensive expertise) → drills into the most important ranking factor (CWV) → addresses the most common critical failure (crawl/index) → covers the opportunity layer (schema) → addresses Kenya's specific infrastructure issue (hosting) → closes with the deliverable. Education → most critical → most common → opportunity → infrastructure → conversion.
