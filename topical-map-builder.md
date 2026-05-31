# Workflow: Topical Map Builder

## Definition
A Topical Map is a content network design based on semantics for achieving the
topical authority state by including overall macro contexts and semantics with
publication frequency.

It has exactly TWO sections: Core Section and Outer Section.

This is NOT a list of blog post names. NOT connections between entities via attributes.
NOT a content calendar. NOT "topics in SEO."

The phrase "Topical Map" was coined first by Koray Tuğberk GÜBÜR.

## What Must Be True Before Building Anything

1. **Source Context is defined** — How does this brand monetize? What is its purpose?
   The Source Context determines which attributes of the Central Entity go into the
   Core Section and which go into the Outer Section.
   The SAME central entity produces a COMPLETELY DIFFERENT topical map depending
   on the Source Context.

2. **Central Entity is identified** — The entity that appears in EVERY sub-section
   of the content network: in main content/macro context AND supplementary content/micro context.

3. **Topical Border is defined** — You CANNOT calculate Topical Coverage without first
   defining where this topical map begins and ends.
   What is included? What is excluded? Where does a competitor's topical map change the border?

4. **Central Search Intent is established** — The unification of Source Context + Central Entity.
   This is what appears site-wide in boilerplate, headings, and content.

If any of these are missing, ask before building.

## Inputs
- `source_context` — How the brand monetizes + its brand purpose
- `central_entity` — The entity that appears throughout the entire content network
- `niche` — Broader industry context
- `existing_content` — List of existing URLs/topics (if auditing an existing site)
- `entity_map` — Output from entity-eav-mapper (if available)

## Execution Steps

### Step 1 — Establish the Topical Border
Before creating any topic nodes:

1. Define the topical border:
   - What is the outermost edge of this topical map?
   - At what point does a topic belong to a DIFFERENT topical map?
   - What would a competitor do to shift this border and shrink your coverage?
2. Example for "Divorce Lawyer":
   - INSIDE border: divorce (mediation, trial, property division, alimony, child custody),
     legal (grounds, prenuptial agreement, default judgement, emancipation, discovery)
   - OUTSIDE border: marriage (statistics, mistakes, types, dynamics, roles, functions)
     → These go in the Outer Section, NOT Core Section
3. The topical border determines what is Core vs Outer, and what is entirely excluded

### Step 2 — Build the Core Section
The Core Section = Source Context + Central Search Intent + MAIN ATTRIBUTE of Central Entity

Rules:
- The main attribute must come DIRECTLY from the Source Context
- Derived attributes flow from the main attribute
- All Core Section topics process the central entity through its MAIN attribute lens
- Macro semantics must be defined for the Core Section:
  - Site-wide N-grams that will appear across Core Section pages
  - Question formats that signal the query context
  - Predicate distributions (which action verbs signal the correct context)
  - First-word patterns in paragraphs (must answer, not use rhetoric)

Examples by Source Context:
| Source Context | Central Entity | Main Attribute (Core) | Derived Attributes |
|---|---|---|---|
| Electric car charger affiliate | Charger | Quality | Durability, charge time, maintenance |
| Electric car charger engineer | Charger | Production | Materials, designs, types |
| Visa Consultancy | Country | Visa processes | Application, requirements, processing time |
| Divorce Lawyer | Divorce | Legal process | Mediation, trial, property division, alimony |
| Pension Planning | Retirement | Financial independence | 401k, ROTH IRA, RMD, catch-up |

Core Section Tier Structure:
- **Tier 1 Topics**: Directly tied to the Central Entity through its MAIN attribute
  - These are the densest, most authoritative pages
  - Each must process the main attribute with FULL EAV depth
  - Macro-context must match the query context for each topic
- **Tier 2 Topics**: Process derived attributes of the main attribute
  - Each must be connected BACK to the main attribute
  - Cannot exist in isolation — must reinforce Core Section consolidation

Depth check for each Core topic: Does this topic define its entity? Connect it to related
entities? Match the macro-context to the query context? If no to any of these: not covered.

### Step 3 — Build the Outer Section
The Outer Section = MINOR attributes of the Central Entity

Rules:
- Focuses on attributes that are NOT the main attribute from Source Context
- Each Outer Section topic must have a linkless or linked connection back to Core Section
- The Outer Section's job is to propagate trust + quality signals TO the Core Section
  and improve overall historical data
- Outer Section topics process the central entity through its MINOR attribute lens
- The macro-context of an outer topic can be different from Core, BUT supplementary
  content must bridge BACK to the Core Section's context

Examples:
- Visa Consultancy Outer: country culture, language schools, geography, climate, religion
  (These are minor attributes of "country" — not visa-related)
- Divorce Lawyer Outer: marriage statistics, relationship types, marriage dynamics,
  marital roles (These are minor attributes of marriage/relationship context)
- Pension Planning Outer: Elder Law Attorney, Power of Attorney, Estate Planning,
  Gifting, Annuity, Medicaid, Retirement Community

Outer Section Tier Structure:
- **Tier 1 (Outer)**: Most directly connected minor attribute topics
- **Tier 2 (Outer)**: Supporting contextual topics that build neighborhood cohesion
- **Tier 3 (Outer)**: Deep contextual bridging topics that connect outer edges back to core

### Step 4 — Define Macro Semantics Site-Wide
For the ENTIRE topical map (not per page):

1. Site-wide N-grams: What 2-3 word phrases appear consistently across the site?
   These must reflect the Central Entity and Source Context.
2. Question formats: What question structures are used most? (What is X? How to X?
   Is X better than Y? Why does X happen?)
3. Predicate distributions: What action verbs dominate? Do they signal the right context?
4. Heading vector patterns: How are H1/H2/H3 constructed across the site?
   Do they reflect Contextual Flow or random content?

### Step 5 — Define Contextual Bridges
Map the connections BETWEEN topical map nodes:

1. Linked bridges: Hypertext connections from Outer Section → Core Section
   (This is how historical data and trust flow from outer to core)
2. Linkless bridges: Consistent information alignment across documents without links
   (Topical proximity signals without explicit anchor text)
3. Contextual Borders: Where does each page's Main Content end and Supplementary Content begin?
   What grouper question provides the transition?

### Step 6 — Coverage Gap Analysis
For each section of the topical map:

Evaluate using Koray's coverage rules:
- Is the entity DEFINED (not just mentioned)?
- Is the entity CONNECTED to related entities?
- Does the macro-context MATCH the query context?
- Is the attribute DEPTH sufficient?
  (Not "battery quality" but specific chemistry types, voltage values, cycle life numbers)
- Are attributes connected BACK to each other?
  (Isolated attribute mentions dilute context even if individually accurate)

Score Topical Coverage based on the topical border — what percentage of the border
is covered at sufficient depth?

### Step 7 — Vastness-Depth-Momentum Assessment
Evaluate the current state and what is missing:
- Vastness: Is the topical map wide enough? Are there missing nodes at the border?
- Depth: Is each node covered with sufficient EAV depth?
- Momentum: Is publication frequency fast enough to maintain indexation priority?

Recommendation: Which of the three to prioritize for THIS site's situation?

## Output Schema
```json
{
  "built_at": "",
  "central_entity": "",
  "source_context": "",
  "central_search_intent": "",
  "topical_border_definition": "",
  "topical_coverage_score": 0,
  "core_section": {
    "main_attribute": "",
    "derived_attributes": [],
    "tier_1_topics": [
      {
        "topic": "",
        "attribute_focus": "",
        "macro_context": "",
        "query_context_match": true,
        "eav_depth_required": "",
        "coverage_status": "missing|partial|covered",
        "priority": "high|medium|low",
        "suggested_h1": "",
        "suggested_h2s": [],
        "contextual_border_question": "",
        "supplementary_bridges_to": []
      }
    ],
    "tier_2_topics": [],
    "macro_semantics": {
      "site_wide_ngrams": [],
      "question_formats": [],
      "predicate_distributions": [],
      "heading_vector_pattern": ""
    }
  },
  "outer_section": {
    "tier_1_topics": [],
    "tier_2_topics": [],
    "tier_3_topics": [],
    "contextual_bridges": [
      {
        "from_node": "",
        "to_node": "",
        "bridge_type": "linked|linkless",
        "anchor_text": "",
        "bridge_description": ""
      }
    ]
  },
  "coverage_gaps": [
    {
      "topic": "",
      "section": "core|outer",
      "gap_type": "undefined|disconnected|wrong_macro_context|shallow_depth",
      "priority": "high|medium|low",
      "reason": ""
    }
  ],
  "vastness_depth_momentum": {
    "vastness_assessment": "",
    "depth_assessment": "",
    "momentum_recommendation": "",
    "priority_recommendation": ""
  }
}
```

## Self-Improvement Notes
After each run, document:
- Was the topical border well-defined from the start?
- Did the Source Context clearly indicate which attributes are core vs outer?
- Which niches required deeper Tier 3 outer expansion than expected?
- Were there cases where a competitor shifted the topical border mid-analysis?
