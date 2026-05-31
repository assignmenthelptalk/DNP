# Linking GPT Workflow — Tupate Studio Internal Link Injection

## Purpose
Systematically review all HTML pages for Tupate Studio and inject or fix internal links based on the `supplementary_bridges_to` relationships defined in the topical map. This workflow ensures every page fulfils its contextual bridge obligations within the semantic content network, passing relevance and PageRank through correct supplementary and contextual-border sections.

## WAT Framework Context
- **W (Workflow):** This file
- **A (Agent):** Claude Code executing the process
- **T (Tools):** Read, Edit, Write tools operating on HTML files

---

## Inputs Required
- Topical map: `[CLIENT_DATA_ROOT]/[client]/topical_map.json`
- HTML pages directory: `[CLIENT_DATA_ROOT]/[client]/pages/`
- Business profile: `[CLIENT_DATA_ROOT]/[client]/business_profile.json`
- Topic → URL slug mapping (provided at session start)

---

## Step 1 — Read the Topical Map
Read `topical_map.json` in full (chunk if >10,000 tokens). Extract for every topic:
- `topic` (name)
- `supplementary_bridges_to` array
- `bridge_to_core` description (for outer section topics without `supplementary_bridges_to`)
- `contextual_bridges` array entries (outer section directional bridges)

---

## Step 2 — Build Link Assignment Map
Create a table mapping each HTML filename → required outbound link targets:

| HTML file | Bridge targets (topic names) | Target URLs |
|---|---|---|
| website-design-kenya.html | SEO Services in Kenya, Mobile-First Website Design Kenya, E-commerce Website Development Kenya | /seo-services-kenya, /mobile-first-website-design-kenya, /ecommerce-website-development-kenya |
| … | … | … |

For outer section topics without `supplementary_bridges_to`, derive bridge targets from:
1. `contextual_bridges` entries where `from_node` matches the page's topic
2. `bridge_to_core` narrative description

---

## Step 3 — Process Each Page
For each HTML file in sequence:

### 3a — Read the file
Read the full HTML file.

### 3b — Inventory existing links
Identify all `<a href="...">` tags already present. Note their `href` values and location (main-content, supplementary, contextual-border, FAQ).

### 3c — Determine missing bridges
Compare existing hrefs against required bridge URLs. Mark each bridge as:
- **Already present** — skip
- **Missing** — must inject

### 3d — Inject missing links
**Location rules (strictly enforced):**
- Primary injection zone: `<section class="supplementary">` paragraphs
- Secondary zone: `<div class="contextual-border">` paragraph — maximum 1 link
- Main content: **Do not add links unless the bridge topic is directly discussed in that section**

**Injection method:**
1. Scan supplementary section paragraphs for any sentence that discusses or mentions the bridge topic
2. If found: wrap the most relevant noun phrase or the topic name with `<a href="/slug">anchor text</a>`
3. If not found: append a short bridging sentence to the most relevant supplementary paragraph that naturally introduces the link. Keep to 1–2 sentences. Match the page's writing style (professional, Kenya-specific, no generic phrasing).

**Anchor text rules:**
- Use the topic name adapted to flow naturally (e.g., "SEO services in Kenya", "local SEO for your Kenyan business", "technical SEO audit")
- Never use generic anchors like "click here" or "learn more"
- Never repeat the same anchor text for different URLs

**Hard limits:**
- Maximum 5–6 total internal links per page (count all links including pre-existing ones)
- No duplicate links to the same URL
- Do not create a "Related links" list or "See also" section

### 3e — Save the updated file
Write the modified HTML back to the same file path using Edit tool (preserving all other content exactly).

---

## Step 4 — Compile Linking Report
After processing all pages, write a report to `[CLIENT_DATA_ROOT]/[client]/reports/linking-report.md` containing:

```markdown
# Linking Report — [Client Name]
**Date:** [YYYY-MM-DD]
**Pages processed:** [N]

## Summary
- Total links added: [N]
- Pages with all bridges already present: [list]
- Pages updated: [list]

## Page-by-Page Detail

### [page-filename].html
- **Required bridges:** topic A → /url-a, topic B → /url-b
- **Added:** `<a href="/url-a">anchor text</a>` in [section name], line ~[N]
- **Skipped (already present):** /url-b
```

---

## Linking Rules Reference

### Where Links Belong
| Section | Link density | Notes |
|---|---|---|
| `<section class="supplementary">` | Majority of links | Primary zone for contextual bridges |
| `<div class="contextual-border">` | Max 1 link | Only to the primary bridge target |
| `<section class="main-content">` | Minimal — do not add | Only if bridge topic is in that section's macro-context |
| `<section class="faq">` | None | Do not inject links into FAQ schema sections |

### What NOT to Do
- Do not create a "Related links" or "See also" list
- Do not add links to FAQ sections (schema markup)
- Do not duplicate any existing link URL
- Do not exceed 5–6 total internal links per page
- Do not add more than 3 new links to any single supplementary section
- Do not change any content except wrapping text in `<a>` tags or adding bridge sentences

---

## Topic → URL Slug Reference

| Topic Name | URL Slug |
|---|---|
| Website Design for Businesses in Kenya | /website-design-kenya |
| SEO Services in Kenya | /seo-services-kenya |
| E-commerce Website Development Kenya | /ecommerce-website-development-kenya |
| Local SEO for Kenyan Businesses | /local-seo-kenya |
| Business Website Redesign Kenya | /website-redesign-kenya |
| Corporate Website Design Kenya | /corporate-website-design-kenya |
| Custom-Built Website vs WordPress Kenya | /custom-website-vs-wordpress-kenya |
| Mobile-First Website Design Kenya | /mobile-first-website-design-kenya |
| Technical SEO Audit Kenya | /technical-seo-audit-kenya |
| Website Speed Optimization Kenya | /website-speed-optimisation-kenya |
| Custom Web Development Kenya | /custom-web-development-kenya |
| Custom E-commerce Development Kenya | /custom-ecommerce-development-kenya |
| On-Page SEO Services Kenya | /on-page-seo-kenya |
| Google Business Profile Optimization Kenya | /google-business-profile-kenya |
| SEO Keyword Research Kenya | /seo-keyword-research-kenya |
| Website Maintenance Services Kenya | /website-maintenance-kenya |
| Landing Page Design Kenya | /landing-page-design-kenya |
| Content Strategy for Kenyan Websites | /content-strategy-kenya |
| M-Pesa Payment Integration Kenya | /mpesa-payment-integration |
| Industrial Machinery Website Design Kenya | /industrial-machinery-website-design-kenya |
| Medical Clinic/Dental Website Design Kenya | /medical-clinic-dental-website-design-kenya |
| Law Firm/Accountancy Website Design Kenya | /law-firm-accountancy-website-design-kenya |
| Real Estate Website Design Kenya | /real-estate-website-design-kenya |
| Restaurant/Hotel Website Design Kenya | /restaurant-hotel-website-design-kenya |
| School/College Website Design Kenya | /school-college-website-design-kenya |
| Digital Marketing Services Kenya | /digital-marketing-kenya |
| Online Business Growth Kenya | /online-business-growth-kenya |
| Domain Registration Kenya | /domain-registration-kenya |
| Web Hosting Kenya | /web-hosting-kenya |
| Google Ads Kenya | /google-ads-kenya |
| Content Marketing Kenya | /content-marketing-kenya |
| Branding/Logo Design Kenya | /branding-logo-design-kenya |
| Website Analytics Kenya | /website-analytics-kenya |
| Kenya E-commerce Market Overview | /kenya-ecommerce-market |
| Kenya Digital Economy | /kenya-digital-economy |
| SME Digital Adoption Kenya | /sme-digital-adoption-kenya |
| Kenya Data Protection Act Compliance | /kenya-data-protection-act-compliance |
| Social Media Marketing Kenya | /social-media-marketing-kenya |
| Google Maps SEO Ranking Kenya | /seo-google-maps-ranking-kenya |

---

## Lessons Learned (updated after each run)

### Run 1 — 2026-03-22
- Outer section tier 2 and tier 3 topics in the topical map do not have `supplementary_bridges_to` arrays. Derive their bridge targets from `bridge_to_core` descriptions and `contextual_bridges` entries.
- The `website-design-kenya.html` page already had all 3 required bridges present (SEO Services, Mobile-First, E-commerce) before this run — confirm pre-existence before editing.
- Some pages use `<a href="/mobile-first-website-design-kenya">mobile-first website design</a>` mid-paragraph in main-content — this was pre-existing and counts toward the link budget.
- Always read the full supplementary section before injecting — existing prose may already name a bridge topic without linking it (easiest injection point).
- For outer section pages with no `supplementary_bridges_to`, use `contextual_bridges[].from_node` matching the page's topic to identify required outbound links.
- The `WooCommerce Kenya E-commerce Setup` bridge target on `ecommerce-website-development-kenya.html` has no matching page — skip this bridge (no URL available).
- Keep bridge sentences to Kenyan business register: professional, direct, no buzzword phrases like "unlock the power of" or "leverage synergies."
