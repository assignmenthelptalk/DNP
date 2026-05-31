# LinkingGPT — Linking Instructions
**Client:** Tupate Studio
**Date:** 2026-03-18
**Methodology:** Koray Tuğberk GÜBÜR — holisticseo.digital
**Mode:** Mode A (CMS Direct Edit — instructions for implementor)

---

## PRE-FLIGHT FINDINGS SUMMARY

- **Total pages in site map:** 38
- **Published pages:** 0 (all planned — no written-content files exist yet)
- **Orphan pages:** 14 (pages with 0 incoming links)
- **Broken links in briefs:** 6 (linking to pages not in site map)
- **Slug mismatches:** 1 (GBP page slug inconsistency across 2 briefs)
- **Anchor overcrowding:** "website design Kenya" used by 34 pages → must diversify
- **Status:** Links are planned in briefs. Implementation happens AFTER pages are written and published.

---

## CRITICAL ISSUES — FIX BEFORE PUBLISHING

### ISSUE 1 — Slug Mismatch: Google Business Profile Page

**Problem:** Briefs for `/seo-services-kenya` (Page 02) and `/local-seo-kenya` (Page 04) both reference `/google-business-profile-kenya` as destination, but the actual published slug will be `/google-business-profile-optimisation-kenya`.

**Fix:** In both briefs' written content and in the CMS, ensure these links point to `/google-business-profile-optimisation-kenya`.

| Source Page | Current Anchor | Wrong Target | Correct Target |
|---|---|---|---|
| /seo-services-kenya | Google Business Profile optimization Kenya | /google-business-profile-kenya | /google-business-profile-optimisation-kenya |
| /local-seo-kenya | Google Business Profile optimization Kenya | /google-business-profile-kenya | /google-business-profile-optimisation-kenya |

---

### ISSUE 2 — Broken Links (Targets Don't Exist)

These 6 links appear in briefs pointing to pages NOT in the topical map. Do NOT publish these links as-is. Replace with redirects to the closest existing Core Section page.

| Source Page | Broken Anchor | Broken Target | Replacement Target | Replacement Anchor |
|---|---|---|---|---|
| /landing-page-design-kenya | conversion rate optimization Kenya | /conversion-rate-optimization-kenya | /seo-services-kenya | search visibility Kenya |
| /industrial-machinery-website-design-kenya | B2B website design Kenya | /b2b-website-design-kenya | /website-design-kenya | professional website Kenya |
| /medical-clinic-dental-website-design-kenya | healthcare website design Kenya | /healthcare-website-design-kenya | /website-design-kenya | Kenyan business website |
| /law-firm-accountancy-website-design-kenya | professional services website design Kenya | /professional-services-website-design-kenya | /website-design-kenya | custom-built website Kenya |
| /restaurant-hotel-website-design-kenya | hospitality website design Kenya | /hospitality-website-design-kenya | /website-design-kenya | website design for Kenyan businesses |
| /school-college-website-design-kenya | educational website design Kenya | /educational-website-design-kenya | /website-design-kenya | professional website Kenya |

---

### ISSUE 3 — Anchor Text Mismatch: Technical SEO Page

Multiple pages use anchor "technical SEO Kenya" → `/technical-seo-audit-kenya`, but the correct anchor synonym is "Technical SEO Audit Kenya" or a synonym variant. The key issue: some briefs may have written `/technical-seo-kenya` (non-existent) as the destination.

**Affected pages:** 06, 11, 13, 16
**Fix:** Use `/technical-seo-audit-kenya` as destination. Use anchor variant from list below:
- "Technical SEO Audit Kenya" (preferred)
- "website technical audit Kenya"
- "SEO health check Kenya"
- "website crawl audit Kenya"

---

## PRIORITY 1 — ORPHAN PAGE FIXES

These pages have ZERO incoming links. They receive no trust signal. Fix immediately upon publishing.

### CRITICAL: Core Tier 1 Orphans

#### FIX-01: /website-redesign-kenya (Core Tier 1 — HIGH COMMERCIAL INTENT)

No page currently links to the Website Redesign page. This is a Core Tier 1 commercial page with zero incoming trust.

**Add incoming links FROM:**

| Source Page | Section | Heading Location | Anchor Text | Rationale |
|---|---|---|---|---|
| /website-design-kenya | Supplementary Content | SUPP H2: Types of Business Websites | "website redesign Kenya" | Design page naturally bridges to redesign service |
| /corporate-website-design-kenya | Supplementary Content | SUPP H2: When to Upgrade a Corporate Site | "business website redesign Kenya" | Corporate sites need redesign context |
| /website-maintenance-services-kenya | Main Content | H2: When Maintenance Isn't Enough | "website modernisation Kenya" | Maintenance → redesign is natural progression |
| /sme-digital-adoption-kenya | Supplementary Content | SUPP H2: Getting a First or Better Website | "revamp your business website Kenya" | Outer → Core trust propagation |

**Implementation instructions (Mode A):**
```
FILE: /website-design-kenya-content.md
SECTION: Supplementary Content → SUPP H2: E-commerce Website Design for Kenyan Online Businesses
PARAGRAPH: Last paragraph of this supplementary section
INSERT AFTER: "[last sentence of e-commerce design section]"
LINK: <a href="/website-redesign-kenya">website redesign Kenya</a>
CONTEXT: "If your existing business website needs modernisation rather than a new build, our [website redesign Kenya] service migrates your ranking history safely while delivering modern performance standards."
```

---

#### FIX-02: /corporate-website-design-kenya (Core Tier 1 — HIGH COMMERCIAL INTENT)

**Add incoming links FROM:**

| Source Page | Section | Heading Location | Anchor Text | Rationale |
|---|---|---|---|---|
| /website-design-kenya | Supplementary Content | SUPP H2: Types of Business Websites (Types table) | "corporate website design Kenya" | Primary design page links to corporate sub-type |
| /law-firm-accountancy-website-design-kenya | Supplementary Content | SUPP section | "corporate website for Kenyan businesses" | Legal/accounting firms need corporate sites |
| /online-business-growth-strategies-kenya | Supplementary Content | SUPP section | "established business website Kenya" | Outer → Core trust |
| /branding-logo-design-kenya | Supplementary Content | SUPP section | "corporate website Kenya" | Brand identity connects to corporate presence |

---

### HIGH: Core Tier 2 Orphans (Niche Pages)

These 7 Core Tier 2 niche pages all have zero incoming links. They MUST receive at least one incoming link each — preferably from the primary `/website-design-kenya` page (via supplementary content Types of Websites table) AND from a relevant Outer Section page.

#### FIX-03: /custom-built-website-vs-wordpress-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Supplementary Content | "custom-built vs WordPress Kenya" |
| /website-maintenance-services-kenya | Supplementary Content | "custom website vs WordPress for businesses" |
| /custom-web-development-kenya | Supplementary Content | "why custom over WordPress in Kenya" |

---

#### FIX-04: /industrial-machinery-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "industrial machinery website Kenya" |
| /corporate-website-design-kenya | Supplementary Content | "industrial B2B website Kenya" |
| /kenya-digital-economy-ict-landscape | Supplementary Content | "industrial sector website Kenya" |

---

#### FIX-05: /medical-clinic-dental-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "medical clinic website Kenya" |
| /local-seo-kenya | Supplementary Content | "dental clinic website Kenya" |
| /google-business-profile-optimisation-kenya | Supplementary Content | "healthcare website design Kenya" |

---

#### FIX-06: /law-firm-accountancy-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "law firm website Kenya" |
| /corporate-website-design-kenya | Supplementary Content | "professional services website Kenya" |
| /local-seo-kenya | Supplementary Content | "accountancy website Kenya" |

---

#### FIX-07: /real-estate-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "real estate website Kenya" |
| /ecommerce-website-development-kenya | Supplementary Content | "property listing website Kenya" |
| /kenya-ecommerce-market-overview | Supplementary Content | "real estate website Kenya" |

---

#### FIX-08: /restaurant-hotel-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "restaurant website Kenya" |
| /local-seo-kenya | Supplementary Content | "hotel website Kenya" |
| /digital-marketing-services-kenya | Supplementary Content | "hospitality website design Kenya" |

---

#### FIX-09: /school-college-website-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Main Content (Types table H3) | "school website Kenya" |
| /sme-digital-adoption-kenya | Supplementary Content | "educational website Kenya" |
| /branding-logo-design-kenya | Supplementary Content | "college website Kenya" |

---

### MEDIUM: Outer Section Orphans

These Outer Section pages have zero incoming links. They cannot propagate trust to Core Section pages if they themselves receive no trust. Fix with cross-Outer links and a Core Section bridge.

#### FIX-10: /branding-logo-design-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Supplementary Content | "branding and logo design Kenya" |
| /corporate-website-design-kenya | Supplementary Content | "brand identity Kenya" |
| /digital-marketing-services-kenya | Main Content | "logo design Kenya" |

---

#### FIX-11: /kenya-ecommerce-market-overview

| Source Page | Section | Anchor Text |
|---|---|---|
| /ecommerce-website-development-kenya | Supplementary Content | "Kenya e-commerce market" |
| /mpesa-payment-integration-websites | Supplementary Content | "e-commerce market in Kenya" |
| /online-business-growth-strategies-kenya | Main Content | "Kenya online retail landscape" |

---

#### FIX-12: /kenya-digital-economy-ict-landscape

| Source Page | Section | Anchor Text |
|---|---|---|
| /seo-services-kenya | Supplementary Content | "Kenya digital economy" |
| /website-design-kenya | Supplementary Content | "Kenya ICT landscape" |
| /sme-digital-adoption-kenya | Main Content | "digital economy Kenya overview" |

---

#### FIX-13: /sme-digital-adoption-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /website-design-kenya | Supplementary Content | "SME digital adoption Kenya" |
| /local-seo-kenya | Supplementary Content | "small business digital Kenya" |
| /online-business-growth-strategies-kenya | Supplementary Content | "SMEs going online Kenya" |

---

#### FIX-14: /social-media-marketing-integration-kenya

| Source Page | Section | Anchor Text |
|---|---|---|
| /digital-marketing-services-kenya | Supplementary Content | "social media marketing Kenya" |
| /website-design-kenya | Supplementary Content | "social media integration Kenya" |
| /content-marketing-kenya | Supplementary Content | "social media content Kenya" |

---

## PRIORITY 2 — OUTER → CORE TRUST LINKS

All Outer Section pages must link TO Core Section pages. Current state and gaps:

### Outer Tier 1 Pages (Trust Propagation — HIGHEST SEO IMPACT)

| Outer Page | Currently Links To Core | Missing Core Links | Priority |
|---|---|---|---|
| /mpesa-payment-integration-websites | /website-design-kenya ✓, /ecommerce-website-development-kenya ✓, /custom-ecommerce-development-kenya ✓ | /local-seo-kenya (M-Pesa for local businesses) | Add |
| /digital-marketing-services-kenya | /website-design-kenya ✓, /seo-services-kenya ✓ | /local-seo-kenya, /ecommerce-website-development-kenya | Add |
| /online-business-growth-strategies-kenya | /website-design-kenya ✓, /seo-services-kenya ✓ | /website-redesign-kenya (growth = modernize old sites too) | Add |

**Implementation — Missing Outer Tier 1 Links:**

```
FILE: /mpesa-payment-integration-websites-content.md
SECTION: Supplementary Content → Final SUPP H2
INSERT: "For local service businesses collecting M-Pesa deposits and booking fees,
[local SEO Kenya] ensures customers find your payment-enabled website on Google Maps
before they visit or call."
LINK: <a href="/local-seo-kenya">local SEO Kenya</a>

FILE: /digital-marketing-services-kenya-content.md
SECTION: Supplementary Content
INSERT REFERENCE: E-commerce dimension of digital marketing
LINK: <a href="/ecommerce-website-development-kenya">e-commerce website Kenya</a>
ANCHOR: "e-commerce website Kenya"

FILE: /online-business-growth-strategies-kenya-content.md
SECTION: Supplementary Content
INSERT: "Businesses with outdated websites lose customers at the first impression —
a [website modernisation Kenya] project is often the fastest growth lever available."
LINK: <a href="/website-redesign-kenya">website modernisation Kenya</a>
```

---

### Outer Tier 2 Pages — Trust Links Status

| Outer Page | Links To Core | Status |
|---|---|---|
| /domain-registration-kenya | /website-design-kenya ✓ | OK — 1 Core link |
| /web-hosting-kenya | /website-design-kenya ✓ | OK — 1 Core link |
| /google-ads-kenya | /website-design-kenya ✓, /seo-services-kenya ✓, /landing-page-design-kenya ✓ | GOOD |
| /content-marketing-kenya | /website-design-kenya ✓, /seo-services-kenya ✓, /content-strategy-kenyan-websites ✓ | GOOD |
| /branding-logo-design-kenya | /website-design-kenya ✓ | NEEDS ADDITIONAL — add /corporate-website-design-kenya |
| /website-analytics-reporting-kenya | /website-design-kenya ✓, /seo-services-kenya ✓ | OK |
| /kenya-ecommerce-market-overview | /ecommerce-website-development-kenya ✓, /custom-ecommerce-development-kenya ✓, /mpesa-payment-integration-websites ✓ | GOOD |
| /kenya-digital-economy-ict-landscape | /website-design-kenya ✓, /seo-services-kenya ✓ | OK |
| /sme-digital-adoption-kenya | /website-design-kenya ✓, /google-business-profile-optimisation-kenya ✓ | OK |
| /kenya-data-protection-act-website-compliance | /website-design-kenya ✓ | OK |
| /social-media-marketing-integration-kenya | /website-design-kenya ✓ | Minimal — add /digital-marketing-services-kenya |
| /38 already accounted for above | | |

---

## PRIORITY 3 — SUPPLEMENTARY CONTENT CONTEXTUAL BRIDGES

These are high-opportunity links that complete the Contextual Bridge network between topical map nodes. Implement after Priority 1 and 2 are complete.

### Bridge 01: Local SEO → Niche Pages (underlinked)

The `/local-seo-kenya` page has only 2 incoming links (01 and 02). Niche pages for sectors that rely on local search should link to it:

| Add Link FROM | Anchor | Section |
|---|---|---|
| /medical-clinic-dental-website-design-kenya | "local SEO for clinics Kenya" | Supplementary Content |
| /restaurant-hotel-website-design-kenya | "local search ranking Kenya" | Supplementary Content |
| /law-firm-accountancy-website-design-kenya | "local SEO for law firms Kenya" | Supplementary Content |
| /google-ads-kenya | "local SEO vs Google Ads Kenya" | Supplementary Content |

---

### Bridge 02: Website Speed → Technical SEO (underlinked chain)

`/website-speed-optimisation-kenya` receives 3 links. It should also receive from:

| Add Link FROM | Anchor | Section |
|---|---|---|
| /website-redesign-kenya | "website speed Kenya" | Supplementary Content (already has a bridge via mobile-first) |
| /mobile-first-website-design-kenya | (already links → speed) | ✓ EXISTS |
| /on-page-seo-services-kenya | "page speed optimisation Kenya" | Supplementary Content |
| /google-ads-kenya | "landing page speed Kenya" | Supplementary Content (slow landing pages waste ad spend) |

---

### Bridge 03: GBP Optimisation → Local Niche Pages

`/google-business-profile-optimisation-kenya` (3 incoming) should receive from:

| Add Link FROM | Anchor | Section |
|---|---|---|
| /restaurant-hotel-website-design-kenya | "Google Business Profile for restaurants" | Supplementary Content |
| /medical-clinic-dental-website-design-kenya | "GBP for clinics Kenya" | Supplementary Content |
| /seo-keyword-research-kenya | "local search keywords Kenya" | Supplementary Content |

---

### Bridge 04: SEO Keyword Research → On-Page SEO (reinforcement)

`/seo-keyword-research-kenya` receives only 1 incoming link:

| Add Link FROM | Anchor | Section |
|---|---|---|
| /seo-services-kenya | "keyword research Kenya" | Supplementary Content (add to existing SUPP H2) |
| /content-strategy-kenyan-websites | "SEO keyword strategy Kenya" | Supplementary Content |
| /on-page-seo-services-kenya | (already links to keyword research) | ✓ EXISTS |

---

### Bridge 05: Content Strategy ↔ Content Marketing (bidirectional bridge)

| Source | Target | Anchor | Section |
|---|---|---|---|
| /content-marketing-kenya | /content-strategy-kenyan-websites | "content strategy Kenya" | Main Content ✓ EXISTS |
| /content-strategy-kenyan-websites | /content-marketing-kenya | "content marketing Kenya" | Main Content ✓ EXISTS |
| Add: /seo-services-kenya | /content-strategy-kenyan-websites | "website content strategy Kenya" | Supplementary Content |

---

## ANCHOR TEXT DIVERSIFICATION — URGENT

The anchor "website design Kenya" is used by **34 pages** pointing to `/website-design-kenya`. This exceeds the 5-page threshold for over-optimization. Outer Section pages (25–38) MUST use synonym anchors instead.

### Mandatory Anchor Replacements (Outer Section pages):

| Page | Current Anchor | Replace With |
|---|---|---|
| /mpesa-payment-integration-websites | "website design Kenya" | "professional website Kenya" |
| /digital-marketing-services-kenya | "website design Kenya" | "Kenyan business website" |
| /online-business-growth-strategies-kenya | "website design Kenya" | "business website Kenya" |
| /domain-registration-kenya | "website design Kenya" | "register domain for website Kenya" → actually link to /web-hosting-kenya instead — this is a stronger contextual bridge |
| /web-hosting-kenya | "website design Kenya" | "custom-built website Kenya" |
| /google-ads-kenya | "website design Kenya" | "website for Google Ads Kenya" |
| /content-marketing-kenya | "website design Kenya" | "content website Kenya" |
| /branding-logo-design-kenya | "website design Kenya" | "branded website Kenya" |
| /website-analytics-reporting-kenya | "website design Kenya" | "analytics-ready website Kenya" |
| /kenya-ecommerce-market-overview | (doesn't link to /website-design-kenya) | N/A |
| /kenya-digital-economy-ict-landscape | "website design Kenya" | "digital presence Kenya" |
| /sme-digital-adoption-kenya | "website design Kenya" | "SME website Kenya" |
| /kenya-data-protection-act-website-compliance | "website design Kenya" | "compliant website Kenya" |
| /social-media-marketing-integration-kenya | "website design Kenya" | "website and social media Kenya" |

### Similarly diversify "SEO services Kenya" anchor (used 10+ times):

| Page | Alternative Anchor |
|---|---|
| /content-marketing-kenya | "Kenya SEO" |
| /website-analytics-reporting-kenya | "search engine optimization Kenya" |
| /google-ads-kenya | "organic search Kenya" |
| /digital-marketing-services-kenya | "SEO for Kenyan businesses" |

---

## LINKLESS CONTEXTUAL BRIDGES (DO NOT ADD HYPERLINKS — THESE ALREADY EXIST)

The following topical connections are covered by consistent entity-attribute alignment across pages. No hypertext link is needed — these are valid contextual bridges:

| Page A | Page B | Shared Entity | Linkless Bridge |
|---|---|---|---|
| /website-design-kenya | /mobile-first-website-design-kenya | Mobile-first design | Both pages reference Safaricom 4G, 80% mobile users, LCP targets — consistent attributes |
| /ecommerce-website-development-kenya | /mpesa-payment-integration-websites | Daraja API | Both cover STK Push, Paybill, C2B API — same entity, consistent values |
| /seo-services-kenya | /technical-seo-audit-kenya | Core Web Vitals | Both pages reference LCP, INP, CLS with same values — linkless bridge exists |
| /local-seo-kenya | /google-business-profile-optimisation-kenya | GBP entity | Both describe the same GBP optimization attributes consistently |
| /website-redesign-kenya | /website-maintenance-services-kenya | Post-launch monitoring | Both reference 90-day monitoring, Google Search Console — consistent bridge |
| /kenya-digital-economy-ict-landscape | /sme-digital-adoption-kenya | Kenya digital economy context | Both reference same ICT statistics and Safaricom ecosystem |
| /kenya-data-protection-act-website-compliance | /ecommerce-website-development-kenya | KDPA and data collection | E-commerce brief covers KDPA compliance — linkless bridge via consistent attribute values |

---

## IMPLEMENTATION SEQUENCE

When pages are written and ready to publish, implement links in this order:

**Week 1 (Priority 1 — Orphan Fixes):**
1. Ensure /website-design-kenya supplementary content includes niche page links (types table → 6 niche pages)
2. Add incoming links to /website-redesign-kenya and /corporate-website-design-kenya
3. Fix all 6 broken link targets in niche briefs before writing

**Week 2 (Priority 2 — Outer → Core Trust Flow):**
4. Add missing Outer Tier 1 trust links (3 additions above)
5. Diversify anchor text on all Outer Section pages (14 anchor replacements)
6. Fix GBP slug mismatches in briefs 02 and 04

**Week 3+ (Priority 3 — Contextual Bridges):**
7. Add local SEO → niche sector links (4 additions)
8. Add speed/technical audit bridges (3 additions)
9. Add GBP → local niche links (3 additions)
10. Add keyword research incoming links (2 additions)

---

## RESTRICTIONS CHECKLIST

- [ ] Never link to pages not in site_map.json — all 6 broken links must be replaced
- [ ] Never use "click here", "learn more", "read this" as anchor text — all anchors are Central Entity synonyms
- [ ] Never place more than 2 links in Main Content per page
- [ ] Never repeat the same anchor from Page A to Page B that Page B uses to link back to Page A
- [ ] Diversify "website design Kenya" anchor — currently 34 pages use it (must reduce to < 10 with same text)
- [ ] Update site_map.json incoming_link_counts after each implementation batch
- [ ] Run orphan check after each batch — no page should have 0 incoming links by go-live

