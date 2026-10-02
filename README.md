# DNP Capstone Project Help

Source for [dnpcapstoneproject.help](https://www.dnpcapstoneproject.help), an academic support site for Doctor of Nursing Practice (DNP) students. It covers the capstone project (PICOT question through final manuscript) across all 13 specialisation tracks, plus related coursework.

The site is a static [Astro](https://astro.build) build deployed on Vercel. Its content structure comes from a separate semantic SEO workspace (`semantic-seo-workflow`, see [SEO workflow](#seo-workflow)).

## Stack

| Area | Choice |
|---|---|
| Framework | Astro 6 (static output, TypeScript) |
| Node | >= 22.12.0 |
| Sitemap | `@astrojs/sitemap`, tiered priorities set in [astro.config.mjs](astro.config.mjs) |
| Hosting | Vercel ([vercel.json](vercel.json)): build `npm run build`, output `dist` |
| Third-party | Tawk.to live chat, Ahrefs Analytics (homepage), WhatsApp float button |

## Quick start

```bash
npm install
npm run dev        # http://localhost:4321
npm run build      # outputs to dist/
npm run preview    # serve the production build
```

## How the site is built

The homepage and the inner pages use two different paths.

**Homepage.** [src/pages/index.astro](src/pages/index.astro) assembles section components (Hero, StatsBar, Mission, About, QualificationsGrid, HowItWorks, FAQ, FinalCTA and so on) from [site-config.json](site-config.json), inside [src/layouts/Layout.astro](src/layouts/Layout.astro). The layout adds the social share sidebar, WhatsApp button, Tawk.to and analytics.

**Inner pages.** [src/pages/[...slug].astro](src/pages/[...slug].astro) generates one static page per entry in [content.json](content.json) (about 52 pages). For each entry it:

1. Reads the metadata: `slug`, `tier`, `metaTitle`, `metaDescription`, `h1`, `intro`, `relatedPages`, `contextualQuestion`.
2. Loads the body HTML from `src/content/pages/<slug>.html`.
3. Renders both through [ServicePage.astro](src/components/ServicePage.astro) with the shared Header and Footer.
4. Sets the canonical URL to `https://www.dnpcapstoneproject.help/<slug>/` (www host, trailing slash).

A page appears on the site only if it has a `content.json` entry. The matching HTML file is optional, and without one the page renders with an empty body.

### Branding

Colours, fonts, nav links, hero copy and CTAs are in [site-config.json](site-config.json). The colours become CSS variables, such as `--color-primary` (#1A4D6E) and `--color-accent` (#E67E22). Change them there rather than in components.

## Project structure

```
.
├── astro.config.mjs        # site URL, sitemap tiers and priorities
├── content.json            # metadata for every inner page
├── site-config.json        # homepage copy, nav, colours, fonts
├── vercel.json             # build settings + legacy 308 redirects
├── public/
│   ├── images/             # header_<slug>.webp, one per page
│   ├── infographics/       # SVG infographics
│   ├── robots.txt          # allows all, points to sitemap-index.xml
│   └── favicon.svg
└── src/
    ├── components/         # homepage sections, ServicePage, Header, Footer, share sidebar
    ├── content/pages/      # body HTML for each inner page
    ├── data/socialLinks.ts # share-button definitions
    ├── layouts/Layout.astro
    └── pages/              # index.astro and [...slug].astro
```

## Content architecture

Pages follow a topical map with a Core section (the main attributes of the central entity) and an Outer section (supporting topics that pass trust to the Core). The sitemap tiers in [astro.config.mjs](astro.config.mjs) mirror that structure.

| Tier | Pages | Priority | Changefreq |
|---|---|---|---|
| Home | `/` | 1.0 | weekly |
| T1 core components | capstone help, proposal, PICOT, literature review, IRB, implementation plan, data analysis, manuscript | 0.9 | weekly |
| T1C examples | 50 project ideas, 60 PICOT examples, capstone examples | 0.85 | weekly |
| T2 project types and tracks | QI, EBP implementation, program evaluation, policy change; FNP, PMHNP, AGACNP, CRNA, nurse executive, population health, informatics | 0.8 | monthly |
| T2C/T2D | BSN and MSN capstone; discussion board, PowerPoint, admission essay, letter of intent | 0.75 | monthly |
| University | Grand Canyon, Aspen, Walden, Capella | 0.7 | monthly |
| Outer | DNP vs PhD, AACN Essentials, EBP frameworks, PICOT explained, review types, IRB protocol, statistics, APA 7 | 0.65 | monthly |
| Other | any page not listed above | 0.6 | monthly |
| Utility | about, contact, services, FAQ, samples, policies, orders | 0.5 | yearly |

Notes:

- `lastmod` is set to the build date for every page.
- `thank-you` and `orders/signup` are excluded from the sitemap.
- **Adding a page to a tier:** add its slug to the matching `Set` in [astro.config.mjs](astro.config.mjs). A slug in no set gets the default 0.6.

## On-page conventions

- **Meta titles** use `Keyword | DNP Help`, kept under 60 characters. The keyword is the page's target phrase, with no descriptive tail. The brand is the logo text; to change it, find and replace ` | DNP Help` in [content.json](content.json).
- **Homepage link.** Every inner page links to `/` in the first paragraph of its body HTML (`src/content/pages/<slug>.html`). Use natural anchor text such as "DNP capstone project help", not "click here".
- **Footer.** [Footer.astro](src/components/Footer.astro) is deliberately minimal to keep link equity on the homepage: the logo (home), email, WhatsApp, and Privacy Policy and Terms & Conditions links. Do not add service, resource or specialty links back to it. Navigation to those pages comes from the header, body content and `relatedPages`.

## Adding a page

1. Add an entry to [content.json](content.json) with the slug, tier, meta fields (`metaTitle` as `Keyword | DNP Help`), H1, intro and related pages.
2. Write the body HTML at `src/content/pages/<slug>.html`, with a homepage link in the first paragraph. Use `<section class="main-content">` with `h2` sections, as the existing pages do.
3. Add a header image at `public/images/header_<slug>.webp`.
4. Add the slug to the right tier set in [astro.config.mjs](astro.config.mjs).
5. Link to it from related pages, and link back from the new page's `relatedPages`.
6. Run `npm run build` and check the output.

## Redirects

[vercel.json](vercel.json) holds about 135 permanent redirects, issued as real 308s at the edge. They map legacy WordPress-era URLs (old service slugs, course-code pages such as `dnp890-dnp-practicum`, university course pages) to current pages. Redirects do not live in Astro config, which would emit meta-refresh pages instead of 308s. Add new ones to `vercel.json`.

## SEO workflow

Content planning for this site is done in a separate workspace, `semantic-seo-workflow`, built on Koray Tuğberk GÜBÜR's Holistic SEO methodology. Its README describes the WAT framework: Workflows (SOPs in `workflows/`), Agent (Claude), Tools (Python and PowerShell in `tools/`).

This site's planning data is in `client_data/dnp-assignment-help/`:

| Artifact | Purpose |
|---|---|
| `topical_map.json` | Central entity (*DNP Academic Assignment*), source context, topical border, Core and Outer sections, coverage gaps, coverage score |
| `publishing_schedule.json` | 28 pages over 20 weeks (1 June to 18 October 2026) at 2 pages per week: Core first, then Outer, then track and project-type pages |
| `page-briefs/` | 28 numbered briefs (`01-dnp-capstone-project-help.md` and so on), one per page, used to write the content |
| `input-images/`, `home-images/` | Source images for the header generator |

**Source context.** DNP assignment help and expert writing. The capstone is the highest-value service, and coursework help is the volume driver.

### Workflow, brief to published page

1. **Topical map** (`workflows/topical-map-builder.md`) defines the Core and Outer sections.
2. **Page brief** (`workflows/page-gpt-workflow.md`) produces a brief in `page-briefs/`.
3. **Write** (`workflows/writer-gpt-workflow.md`) turns the brief into the body HTML in `src/content/pages/`.
4. **Link** (`workflows/linking-gpt-workflow.md`) sets the internal linking, which feeds `relatedPages` in `content.json`.
5. **Images** go through `tools/images/generate_header.py` with a per-client config, producing the 1200×420 WebP headers in `public/images/`. Infographics follow `workflows/infographic-svg-skill.md`.
6. **Audit** (`workflows/seo-audit-workflow.md`) is rerun after publishing.

### Writing rules

The methodology defines coverage strictly: a topic is covered only if it is defined, connected to related attributes, and matched to the query context. Entity stuffing and one page per keyword do not count. Keep the central entity in anchor text and use synonyms.

## Known issues

- **Orphaned pages.** The cookie policy and refund policy pages are published and in the sitemap, but the footer no longer links to them. Consider linking them from the Terms page, or restoring a footer link if cookie-consent rules require it.
- **Favicon.** `site-config.json` and the layouts reference `/favicon.ico` and `/apple-touch-icon.png`. Only `favicon.svg` is in `public/`.
- **Tracking scripts.** Tawk.to is on every page, but Ahrefs Analytics is only in [Layout.astro](src/layouts/Layout.astro) (the homepage), not on inner pages. Confirm whether that is intended.
- **Tier labels.** The `tier` value in `content.json` is separate from the sitemap sets in `astro.config.mjs`, and the two can drift.
- **Schedule.** The publishing schedule lists 28 pages, but the site has about 52, which also include utility, university, example and policy pages. The brief set is not the full page inventory.

## Deployment

Pushes build on Vercel with `npm run build`. Before merging, confirm the build passes, check that `dist/sitemap-index.xml` is generated, and spot-check any new or changed redirects against the live URL.
