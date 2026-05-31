# Workflow: SEO Audit (Master Orchestrator)

## Purpose
Full Holistic SEO audit based on Koray Tuğberk GÜBÜR's methodology.
Evaluates Topical Authority = Topical Coverage × Historical Data.
Produces a structured JSON data set and branded PDF report.

## Trigger Phrases
- "run an SEO audit for [URL or niche]"
- "analyze my website"
- "build a topical map for [niche/URL]"
- "do a full semantic SEO analysis"
- "check my topical authority"

## What You Must Establish Before Running Anything

Before calling any tool, answer these questions — they determine everything:

1. **Source Context**: How does this brand monetize? What is its purpose?
   What is the connection between the brand and its central entity?
   This is NOT the niche. It is HOW the brand operates within the niche.
   (Load from `business_profile.json` or ask the user directly)

2. **Central Entity**: What entity appears in EVERY part of this content network?
   What entity gives its main attributes to the Core Section and minor attributes
   to the Outer Section?

3. **Central Search Intent**: What is the unification of Source Context + Central Entity?
   This will appear site-wide in boilerplate, main content, and supplementary content.

4. **Main Attribute** (for Core Section): What is the MAIN attribute of the central entity
   that connects directly to the Source Context?
   Example: Affiliate for electric car chargers → main attribute = "quality"
   Example: Engineer for electric car chargers → main attribute = "production"

5. **Topical Border**: Where does this topical map begin and end?
   You cannot calculate Topical Coverage without defining this border first.

If any of these are unclear, ask the user before proceeding.

## Inputs Required
- `target` — Website URL and/or niche/topic keyword
- `client_name` — For saving data to `[CLIENT_DATA_ROOT]/[client_name]/`
- `business_profile` — Source Context + Central Entity (load from JSON or ask user)
- `competitors` — Optional list; auto-discovered if not provided

## Client Data Root

All client paths in this workflow are resolved from a configurable client-data root:

- Preferred: `[CLIENT_DATA_ROOT]/[client_name]/...`
- Backward-compatible fallback: `client_data/[client_name]/...`

## Pre-Flight Checklist
1. Load `[CLIENT_DATA_ROOT]/[client_name]/business_profile.json` if it exists
2. Check `[CLIENT_DATA_ROOT]/[client_name]/entity_map.json` — skip entity discovery if < 30 days old
3. Check `[CLIENT_DATA_ROOT]/[client_name]/topical_map.json` — skip rebuild if < 30 days old
4. Verify API keys are loaded from `.env`
5. Confirm brand assets exist in `brand_assets/`

## Execution Sequence

### Phase 1 — Discovery
**Goal: Understand the existing state of the source and the competitive landscape.**

Step 1: Call `scrape_website.py` (if URL provided)
- Extract: heading vectors (H1/H2/H3 site-wide), existing page structure,
  internal link patterns, site-wide N-grams, content types
- What to look for: Does the heading structure reflect the Central Entity and
  Source Context? Are headings used for structure or for design?
- What to check: Are Main Content and Supplementary Content clearly separated
  in the existing page layouts?

Step 2: Call `competitor_research.py`
- Find top 5 semantic competitors for this niche and Source Context
- Extract their topical borders, Core Section depth, Outer Section breadth
- Note: A semantic competitor is a site with the SAME Source Context
  targeting the SAME Central Entity. Not just any site in the niche.

Step 3: Call `discover_entities.py`
- Discover all entities with their attributes and values
- Remember: entity stuffing does NOT increase coverage
  Coverage requires defining, connecting, and contextualizing entities properly

### Phase 2 — Semantic Mapping
**Goal: Build the actual Topical Map based on exact definitions.**

Step 4: Run `entity-eav-mapper` workflow → produces `entity_map.json`
- Map every entity with ALL relevant attributes and SPECIFIC factual values
- Check: Are attributes connected back to each other? (Disconnected attributes
  dilute topical consolidation even if individually accurate)
- Check: For each attribute — is it a main attribute (Core) or minor attribute (Outer)?

Step 5: Call `build_topical_map.py` → produces `topical_map.json`
Core Section must include:
- Source Context united with Central Search Intent
- Main attribute of central entity (from Source Context)
- Derived attributes of the main attribute
- Macro semantics: site-wide N-grams, question formats, predicate distributions
- Micro semantics: sequence modeling targets, entity-object relations

Outer Section must include:
- Minor attributes of the central entity
- Topics that propagate trust/signals TO the Core Section
- Contextual bridges (linkless connections between topical map nodes)
- Each outer section topic must connect back to the Core Section

Step 6: Run `query-intent-analyzer` workflow → produces `query_clusters.json`
- Map represented queries (what users actually type)
- Map representative queries (how the search engine interprets them)
- Analyze the semantic distance between them
- Note: The web document must satisfy ALL possible interpretations of a query,
  not just the literal terms in the search bar

### Phase 3 — Analysis and Scoring
**Goal: Calculate Topical Authority = Topical Coverage × Historical Data**

Step 7: Call `score_topical_authority.py`
Topical Coverage score checks:
- Has the topical border been defined?
- Are entities defined (not just mentioned)?
- Are entities connected to each other?
- Do macro-contexts match query contexts?
- Is the depth of attribute coverage sufficient?

Historical Data signals to check (from scraped site if URL provided):
- Publication frequency — does the site publish consistently?
- Content configuration — has the site been updating content to match changed
  semantic distances?
- Quality of content network — do low-quality pages dilute high-quality ones?

Step 8: Call `analyze_serp_intent.py`
- Identify gaps between current coverage and required coverage
- Find represented vs representative query gaps
- Flag Contextual Flow issues (wrong ordering of topics)
- Identify Contextual Coverage issues (one context overwhelming others)

Step 9: Run `content-network-builder` workflow → produces `content_network.json`
- Plan Main Content and Supplementary Content structure per page
- Design internal linking architecture (from Outer → Core Section)
- Plan Contextual Bridges (linkless and linked)
- Define publication frequency recommendation (Momentum)

### Phase 4 — Report Generation

Step 10: Call `generate_seo_pdf.py` → produces branded PDF report

## Output Files
- `[CLIENT_DATA_ROOT]/[client_name]/reports/seo-audit-[date].pdf`
- `[CLIENT_DATA_ROOT]/[client_name]/topical_map.json`
- `[CLIENT_DATA_ROOT]/[client_name]/entity_map.json`
- `[CLIENT_DATA_ROOT]/[client_name]/query_clusters.json`
- `[CLIENT_DATA_ROOT]/[client_name]/content_network.json`

## PDF Report Sections
1. Executive Summary — Topical Authority score, top 3 immediate actions
2. Business Profile — Source Context, Central Entity, Central Search Intent
3. Topical Map — Core Section (main attribute + derived attributes) +
   Outer Section (minor attributes, trust propagation plan)
4. EAV Analysis — Entity definitions, attribute depth, value completeness,
   connection gaps
5. Query Analysis — Represented vs Representative query clusters, semantic distance
   scores, coverage gaps per query context
6. Content Network Plan — Main Content / Supplementary Content structure,
   internal linking architecture, Contextual Bridge plan
7. Competitor Comparison — Topical Coverage and Core Section depth vs top 5 rivals
8. Prioritized Action Plan — Ordered by Vastness / Depth / Momentum impact

## Error Handling
- Scraping blocked → use cached data, flag and continue with available data
- No competitors found → broaden Source Context definition, retry with niche-level search
- PDF generation fails → save raw JSON report and flag issue
- API rate limited → exponential backoff, batch requests
- Topical Border unclear → STOP and ask user to clarify Source Context + Central Entity
  before proceeding. Everything downstream depends on this.

## Self-Improvement Notes
After every run, document:
- Was the Source Context correctly identified from the start?
- Did the topical border definition match what the user expected?
- Which competitor sources blocked scraping?
- Were there niches where the Outer Section required deeper expansion than expected?
- Did any content nodes have unclear Main Content vs Supplementary Content assignments?
