# Workflow: Content Network Builder

## Definition
A Semantic Content Network is a collection of connected web documents that are
semantically optimized for a topic. Its quality affects the rankings of the web source
for ALL topics it covers — not just the individual pages.

Non-quality pages make other quality pages rank lower.
The entire network's health determines individual page performance.

## Purpose
Design a cohesive content network with:
- Correct Main Content / Supplementary Content architecture per page
- Optimized Contextual Flow (ordering) per page
- Internal linking architecture that propagates trust from Outer → Core Section
- Contextual Bridges (linkless and linked) between topical map nodes
- Publication frequency recommendation (Momentum)

## Inputs
- `topical_map` — Output from topical-map-builder
- `entity_map` — Output from entity-eav-mapper
- `query_clusters` — Output from query-intent-analyzer
- `existing_urls` — Current site pages (if auditing an existing site)

## Execution Steps

### Step 1 — Content Node Classification

For each node in the topical map, classify the page structure:

**Main Content** (required for every page):
- What is the macro-context of this page? (single dominant context)
- Which MAJOR query needs must Main Content satisfy 100%?
- Which entities and attributes belong in Main Content?
  (Primary entity + main attributes + specific values — full EAV depth)
- What is the contextual flow ORDER of main content sections?
  (Wrong order = wrong relevance distribution)
- What are the heading vectors? (H1, H2s that process the macro-context)
- Remember: Main Content contains MINIMAL internal links (only if inside macro-context)

**Supplementary Content** (required for every page):
- Which MINOR query needs belong here?
- Which micro-contexts and minor entities get processed here?
- Which OTHER macro-contexts does Supplementary Content bridge to?
  (Supplementary always processes topics WITH a connection to another macro-context)
- Where do the majority of internal links sit?
- Which Contextual Bridges (linkless + linked) belong here?

**Contextual Border** (required for every page):
- Where exactly does Main Content end and Supplementary Content begin?
- What is the grouper question that provides the SLOW TRANSITION?
  (Not a hard stop — a question that deepens the main context while opening side-topics)

### Step 2 — Contextual Flow Design Per Page

The ORDER of sections determines relevance. Apply this per page:

1. Identify the heaviest context (must appear earliest in the document)
2. Design the progression from macro-context → contextual border → micro-contexts
3. Check: Does the sequence mirror how the search engine distributes query intent?
4. Check: Does any section overweight its contextual coverage and dilute others?
   (One context taking 80% of the page dilutes everything else)
5. Check: Is each section's coverage appropriate for Passage Indexing?
   (Each section should be self-contained enough to rank independently as a passage)

### Step 3 — Internal Linking Architecture

Apply Koray's exact rules:

**Rule 1: Trust flows from Outer Section → Core Section**
Outer Section pages must link TO Core Section pages.
This is how the Outer Section fulfills its purpose: propagating trust signals.

**Rule 2: Anchor text must use Central Entity synonym values**
The Central Entity ALWAYS appears in anchor texts with a SYNONYM value.
Map all anchor text variations per entity for every link.
Never use generic anchors like "click here" or "learn more."

**Rule 3: Internal links in Main Content only if inside the macro-context**
If an internal link falls outside the macro-context of the main content section,
it belongs in the Supplementary Content section — not the Main Content.

**Rule 4: Supplementary Content carries the majority of internal links**
This is by design — supplementary content's job is to provide neighborhood cohesion
and bridge to other topical map nodes.

**Rule 5: Contextual Bridges complement hypertext links**
Not every connection needs a hypertext link. Linkless contextual bridges
(consistent information aligned across documents) are equally important for
propagating topical proximity signals.

For each link in the network:
- Source page and section (Main Content or Supplementary Content)
- Target page
- Anchor text (synonym value of Central Entity or connected entity)
- Intent signalled by this link
- Contextual validity: does this link fall within the correct section?

### Step 4 — Contextual Bridge Mapping

Map all Contextual Bridges in the content network:

**Linked Bridges** (hypertext):
- From which Outer Section node → to which Core Section node
- Anchor text (Central Entity synonym)
- What query path does this bridge serve?

**Linkless Bridges** (information alignment):
- Which documents share consistent information about the same entity?
- Where is the same entity referenced across multiple documents without links?
- These create topical proximity signals between topical map nodes
- Flag any cases where linkless bridges are ABSENT but needed

**Bridge Content**:
- Are there topic nodes specifically designed to bridge macro-context to micro-contexts?
- Do these bridge nodes have their own Main Content (the bridge concept) and
  Supplementary Content (links to both the macro and micro nodes they connect)?

### Step 5 — Network Health Analysis

Evaluate the entire content network:

1. **Non-quality page identification**: Which pages dilute the network?
   - Pages with incorrect macro-context for their query
   - Pages that mix Main Content and Supplementary Content without separation
   - Pages targeting queries they cannot satisfy (missing functional components)
   - Pages with disconnected attributes that dilute topical consolidation

2. **Orphan risk**: Which pages have no incoming Contextual Bridges?
   Pages with no incoming links OR linkless connections receive no trust signals.

3. **Cannibalization risk**: Where do pages compete for the same macro-context?
   Two pages targeting the same represented query with the same macro-context
   dilute each other.

4. **Silo integrity**: Is trust flowing correctly from Outer → Core?
   Are there Core Section pages with no incoming links from Outer Section pages?

### Step 6 — Publication Schedule (Momentum)

Momentum = publication frequency for maintaining indexation priority.

Design the publication schedule based on Vastness-Depth-Momentum assessment:

1. What is currently MISSING that most impacts Topical Coverage?
   Publish these first — they close the most significant topical border gaps.

2. What is the minimum publication frequency to maintain indexation priority?
   This depends on: niche competition, historical data quality, current topical coverage.

3. What is the Content Configuration schedule?
   (Which existing pages need reconfiguration due to changed semantic distances?)
   Content Configuration = optimizing relevance and responsiveness continuously.

4. Publication order should follow this logic:
   - Core Section Tier 1 first (highest authority pages — establish the macro-context)
   - Core Section Tier 2 (build depth around derived attributes)
   - Outer Section (build Vastness + propagate trust to Core)
   - Bridge content (Contextual Bridges between nodes)

## Output Schema
```json
{
  "built_at": "",
  "content_network_summary": {
    "total_pages_recommended": 0,
    "new_pages_needed": 0,
    "pages_to_update": 0,
    "pages_to_remove": 0,
    "non_quality_pages_flagged": 0
  },
  "content_nodes": [
    {
      "title": "",
      "url_slug": "",
      "topical_map_section": "core|outer",
      "topical_map_tier": "",
      "status": "new|existing|update|remove",
      "primary_entity": "",
      "attribute_focus": "",
      "macro_context": "",
      "target_query_cluster": "",
      "major_query_needs_satisfied": [],
      "main_content_sections": [
        {
          "heading": "",
          "context_vector": "",
          "eav_depth": "",
          "contextual_weight": "heavy|medium|light",
          "order": 0
        }
      ],
      "contextual_border_question": "",
      "supplementary_content_sections": [
        {
          "heading": "",
          "micro_context": "",
          "bridges_to_macro_context": "",
          "internal_links": []
        }
      ],
      "internal_links_to": [
        {
          "target_page": "",
          "anchor_text": "",
          "content_section": "main|supplementary",
          "contextual_validity": true
        }
      ],
      "internal_links_from": [],
      "contextual_bridges": [
        {
          "bridge_type": "linked|linkless",
          "target_node": "",
          "description": ""
        }
      ],
      "page_component_required": "",
      "priority": "high|medium|low"
    }
  ],
  "network_health": {
    "non_quality_pages": [],
    "orphan_risks": [],
    "cannibalization_risks": [],
    "trust_flow_gaps": []
  },
  "publication_schedule": [
    {
      "week": 0,
      "pages": [],
      "rationale": "",
      "momentum_impact": ""
    }
  ],
  "vastness_depth_momentum_plan": {
    "current_state": "",
    "priority": "vastness|depth|momentum",
    "recommendation": ""
  }
}
```

## Self-Improvement Notes
After each run, document:
- Were there pages where Main Content / Supplementary Content separation was unclear?
- Which Contextual Bridges were missing and most impacted trust flow?
- Were there niches where the publication schedule needed higher initial momentum?
- Which non-quality pages most significantly diluted the network health?
