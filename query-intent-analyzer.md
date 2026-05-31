# Workflow: Query Intent Analyzer

## Purpose
Analyze query semantics using Koray Tuğberk GÜBÜR's Represented vs Representative
Query framework. Map how search engines interpret queries and identify the full range
of user needs a web document must satisfy.

## Core Concept: Represented vs Representative Queries

This is NOT the same as "seed queries" and "tail queries."
This is NOT "short-tail vs long-tail keywords."

**Represented Query**: The exact terms the user types into the search bar.
**Representative Query**: How the search engine actually interprets those terms —
the meaning the search engine assumes the user wants.

Search engines do NOT give full relevance weight to the literal terms in the search bar.
The relevance of search bar terms is DISTRIBUTED based on representative queries primarily.

Examples:
- Represented query: "board vision" / "vision board" → Different SERPs despite similar meaning,
  because the search engine builds different contextual connections for each phrasing
- Represented query: "cancer" → Representative queries include "learn cancer,"
  "go to cancer treatment," "compare cancer treatment methods," "find cancer treatment center"
  → The document must satisfy ALL possible interpretations of this single-word query

The Semantic Distance between represented and representative queries changes continuously.
During and after Broad Core Algorithm Updates (BCAUs), SERP characteristics and
ranking source types change significantly as these distances shift.

## What This Analysis Must Determine

For every topic in the topical map:
1. What does the user actually TYPE? (represented query)
2. What does the SEARCH ENGINE think the user wants? (representative queries)
3. How far apart are these interpretations? (semantic distance score)
4. What is the FULL RANGE of possible and related search activities behind this query?
5. What MAJOR query needs must Main Content satisfy 100%?
6. What MINOR query needs should Supplementary Content touch?
7. Which content document in the topical map best serves each query cluster?

## Inputs
- `central_entity` — Primary entity of the content network
- `source_context` — Brand monetization purpose (determines query priority)
- `topical_map` — Output from topical-map-builder (provides topic nodes)
- `competitor_data` — Top ranking competitor pages

## Execution Steps

### Step 1 — Collect and Pair Queries

For each topic node in the topical map:

1. Identify the represented queries — actual search terms users type
   These come from: Google Autocomplete, People Also Ask, Related Searches,
   keyword research, search console data (if URL provided)

2. Infer the representative queries — how the search engine interprets each
   Ask: If this query went to the search engine, what would the search engine
   assume the user is looking for? What are the 3-5 most likely interpretations?

3. Measure Semantic Distance (0-10):
   - 0-2: Literal interpretation — search engine takes the query at face value
     Example: "LiFePO4 battery specs" → semantic distance is low
   - 3-5: Moderate interpretation — search engine fills in context
     Example: "battery life" → could mean phone battery, EV battery, flashlight
   - 6-8: High interpretation — search engine radically transforms the query intent
     Example: "cancer" → becomes a full medical information + treatment hub
   - 9-10: The search engine's interpretation may have little relation to literal terms
     Example: "vision board" vs "board vision" produce different SERPs entirely

### Step 2 — Classify Intent and Query Distribution

For each query cluster, classify the DISTRIBUTION of probabilities:

Koray's key insight: For a query like "movie 20" the distribution could be:
"best 20 movies," "movies for 20-year-olds," "the movie called 20," "movies from the 20s."
The web document must DISTRIBUTE its contextual flow to satisfy all likely interpretations.

Intent types in the distribution:
- Informational: user wants to learn (highest semantic distance potential)
- Navigational: user wants to find a specific page (very low semantic distance)
- Commercial: user is researching before buying
- Transactional: user wants to take action
- Investigational: user is comparing options

Do NOT assign a single intent type to a query if the search engine distributes
probabilities across multiple interpretations. Map the full distribution instead.

### Step 3 — Map Possible and Related Search Activities

For each cluster, define the full range of search activities behind the query.

This is where you think about real-world behavior:
- What is the user's END GOAL (not just their immediate query)?
- What is the SEQUENCE of searches the user will perform?
- What ACTION in the real world does this search lead to?
- Can this page enable the user to complete their end goal, or will they need to
  click to another source?

Important: If the page cannot enable the end goal (e.g., a calculator page without
a calculator, a loan comparison page without an application), it cannot rank for
highly commercial or transactional queries regardless of content quality.

### Step 4 — Assign Major and Minor Query Needs

For each cluster, separate:

**Major Query Needs** → Must be satisfied 100% in Main Content
- The primary interpretation the search engine assigns
- The core information the user cannot leave without
- The need that, if unsatisfied, creates a pogo-stick behavior (negative historical data)

**Minor Query Needs** → Touched in Supplementary Content, not overprocessed in Main Content
- Secondary interpretations
- Related search activities that are not the primary goal
- If over-processed in Main Content, they DILUTE the macro-context and reduce relevance

### Step 5 — Predicate and Sequence Analysis

Predicates signal the overall context for every query cluster.
"Yell" annotates a different context from "shout" — and ALL surrounding word
sequence probabilities change.

For each cluster:
1. What predicates appear in represented queries? (how, make, best, compare, fix, buy)
2. Do these predicates match the Source Context and Central Search Intent?
3. Are there predicate conflicts? (informational predicates on a transactional page?)
4. What question formats dominate? (What is X? How to X? Is X better than Y?)
5. What are the first words of likely paragraph openings — do they answer directly?

### Step 6 — Identify Contextual Flow Implications

Each query cluster's semantic distance and representative query distribution
has implications for the Contextual Flow of the document that targets it:

1. High semantic distance queries need a document that distributes contextual
   coverage across multiple interpretations from macro-context to micro-contexts
2. Low semantic distance queries need a tightly focused document with clear
   macro-context and minimal supplementary dilution
3. Queries with multiple equal-weight representative queries need careful
   Contextual Coverage balancing (no single interpretation should dominate)

### Step 7 — BCAU Risk Assessment

The Semantic Distance between queries changes continuously.
During Broad Core Algorithm Updates:
- SERP characteristics change
- The ranking web source types change
- Topics that were Core may shift toward Outer Section relevance

Flag any clusters where:
- A recent BCAU has likely shifted the representative query interpretation
- The current content targets an old interpretation
- Content Configuration (reconfiguration of topical maps) is needed

## Output Schema
```json
{
  "analyzed_at": "",
  "central_entity": "",
  "source_context": "",
  "query_clusters": [
    {
      "cluster_name": "",
      "topical_map_node": "",
      "topical_map_section": "core|outer",
      "represented_queries": [],
      "representative_queries": [],
      "semantic_distance_score": 0,
      "intent_distribution": {
        "informational": 0,
        "navigational": 0,
        "commercial": 0,
        "transactional": 0,
        "investigational": 0
      },
      "major_query_needs": [],
      "minor_query_needs": [],
      "possible_search_activities": [],
      "real_world_end_goal": "",
      "page_component_required": "",
      "predicate_distribution": [],
      "question_formats": [],
      "contextual_flow_implication": "",
      "contextual_coverage_risk": "",
      "bcau_risk": "low|medium|high",
      "content_gaps": [],
      "priority": "high|medium|low"
    }
  ],
  "total_clusters": 0,
  "high_semantic_distance_clusters": [],
  "bcau_risk_flags": [],
  "content_configuration_needed": []
}
```

## Self-Improvement Notes
After each run, document:
- Were there niches where semantic distance was consistently underestimated?
- Which query types had the most complex representative query distributions?
- Were there cases where BCAU had already shifted the representative query interpretation
  and the current content was targeting an outdated interpretation?
