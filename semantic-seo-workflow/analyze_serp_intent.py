#!/usr/bin/env python3
"""
Tool: analyze_serp_intent.py
Job: Analyze query semantics using Koray Tuğberk GÜBÜR's Represented vs
     Representative Query framework.
     NOT "seed queries and tail queries."
     NOT "short-tail vs long-tail keywords."
     Represented = what user types. Representative = what search engine interprets.
Uses: Anthropic API
"""

import os
import json
import sys
import argparse
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

SYSTEM_PROMPT = """You are a Semantic SEO expert applying Koray Tuğberk GÜBÜR's
Query Semantics framework from holisticseo.digital.

EXACT DEFINITIONS YOU MUST USE:

REPRESENTED QUERY: The exact terms the user types into the search bar.

REPRESENTATIVE QUERY: How the search engine actually interprets those terms.
Search engines do NOT give full relevance weight to literal search bar terms.
Relevance is distributed based on representative queries primarily.

Example: "board vision" and "vision board" produce different SERPs because the
search engine builds different contextual connections for each phrasing.

Example: Query "cancer" → representative queries include "learn cancer,"
"go to cancer treatment," "compare treatment methods," "find treatment center."
A web document must satisfy ALL possible interpretations — not just the literal query.

SEMANTIC DISTANCE (0-10):
0-2: Literal — search engine takes the query at face value
3-5: Moderate — search engine fills in context gaps  
6-8: High — search engine radically transforms query intent
9-10: The search engine's interpretation has little relation to literal terms

MAJOR QUERY NEEDS: Must be satisfied 100% in Main Content.
If unsatisfied → pogo-stick behavior → negative historical data → rankings lost.

MINOR QUERY NEEDS: Touched in Supplementary Content only.
If over-processed in Main Content → dilutes macro-context → reduces relevance.

HISTORICAL DATA: Not time. Quality user engagement (clicks, hover-overs, session logs).
If major query needs are unmet → non-quality historical data accumulates → rankings drop
6+ months later.

PREDICATE SIGNAL: The predicate (action verb) signals the overall context.
"Yell" annotates a different context from "shout" — ALL surrounding word sequence
probabilities change.

CONTEXTUAL COVERAGE: One context taking too much of a page dilutes all others.
The full distribution of probable interpretations must be reflected in content.

BCAU RISK: Broad Core Algorithm Updates shift semantic distances between queries.
Content targeting old representative query interpretations loses rankings.

Return ONLY valid JSON. No preamble. No markdown fences."""


def analyze_serp_intent(central_entity: str, niche: str, source_context: str,
                        topical_map: dict = None, competitor_data: dict = None) -> dict:
    """Analyze query intent using Represented vs Representative Query framework."""
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        topics_context = ""
        if topical_map:
            core = topical_map.get("core_section", {})
            outer = topical_map.get("outer_section", {})
            core_topics = [t.get("topic", "") for t in core.get("tier_1_topics", [])[:10]]
            outer_topics = [t.get("topic", "") for t in outer.get("tier_1_topics", [])[:8]]
            topics_context = f"""
Core Section topics (main attribute focus): {', '.join(core_topics)}
Outer Section topics (minor attribute focus): {', '.join(outer_topics)}
Central Search Intent: {topical_map.get('central_search_intent', 'unknown')}
"""

        competitor_context = ""
        if competitor_data:
            competitors = competitor_data.get("competitors", [])
            competitor_context = f"Top competitor domains: {', '.join([c.get('url', '') for c in competitors[:5]])}"

        prompt = f"""Analyze query semantics for this content network using the
Represented vs Representative Query framework.

Central Entity: {central_entity}
Niche: {niche}
Source Context: {source_context}
{topics_context}
{competitor_context}

For EACH topic node in the topical map, and for the central entity overall:

1. REPRESENTED QUERIES: What exact terms do users type?
   Include: autocomplete variations, People Also Ask formats, related searches formats

2. REPRESENTATIVE QUERIES: How does the search engine ACTUALLY interpret these?
   For each represented query, what are the 3-5 most probable interpretations the
   search engine assigns? What is the DISTRIBUTION of these interpretations?

3. SEMANTIC DISTANCE (0-10): How far is the search engine's interpretation from the literal query?

4. INTENT DISTRIBUTION: What percentage of the query's weight goes to each intent type?
   (Informational / Navigational / Commercial / Transactional / Investigational)
   Sum must = 100%. Many queries have MIXED distributions — do not force a single label.

5. MAJOR QUERY NEEDS: What must Main Content satisfy 100%?
   If this is not satisfied, what pogo-stick behavior occurs?
   What negative historical data signal does this create?

6. MINOR QUERY NEEDS: What belongs in Supplementary Content only?
   What happens if these are over-processed in Main Content?
   (Answer: dilutes macro-context and reduces relevance)

7. POSSIBLE SEARCH ACTIVITIES: What is the user's real-world end goal?
   What sequence of searches will the user perform?
   What real-world action does this search lead to?

8. PAGE COMPONENT REQUIRED: Does satisfying this query require a specific
   functional component? (calculator, form, application, map, comparison table)
   If yes — what is it? Pages WITHOUT this component CANNOT rank for commercial queries.

9. PREDICATE ANALYSIS: What are the dominant predicates in represented queries?
   (how, make, best, compare, fix, buy, is, does, what, why)
   Do they match the Source Context? Are there predicate conflicts?

10. CONTEXTUAL FLOW IMPLICATION: Given the semantic distance and representative query
    distribution, how should the document's Contextual Flow be structured?
    Should it heavily favor one interpretation or distribute across several?

11. BCAU RISK: Is there evidence that a recent Broad Core Algorithm Update has
    shifted the representative query interpretation for this cluster?
    If so, what Content Configuration is needed?

Return this exact JSON:
{{
  "analyzed_at": "{datetime.now().isoformat()}",
  "central_entity": "{central_entity}",
  "source_context": "{source_context}",
  "query_clusters": [
    {{
      "cluster_name": "",
      "topical_map_node": "",
      "topical_map_section": "core|outer",
      "represented_queries": [],
      "representative_queries": [],
      "semantic_distance_score": 0,
      "intent_distribution": {{
        "informational": 0,
        "navigational": 0,
        "commercial": 0,
        "transactional": 0,
        "investigational": 0
      }},
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
    }}
  ],
  "total_clusters": 0,
  "high_semantic_distance_clusters": [],
  "bcau_risk_flags": [],
  "content_configuration_needed": []
}}"""

        print(f"[analyze_serp_intent] Mapping represented vs representative queries | Entity: {central_entity}")

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=5000,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}]
        )

        response_text = message.content[0].text.strip()
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]

        result = json.loads(response_text)
        return result

    except ImportError:
        return {"error": "anthropic library not installed. Run: pip install anthropic"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}"}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Analyze query intent using Represented vs Representative framework")
    parser.add_argument("central_entity", help="Primary entity of the content network")
    parser.add_argument("--niche", required=True, help="Industry/niche context")
    parser.add_argument("--source-context", required=True, help="How the brand monetizes")
    parser.add_argument("--topical-map", help="Path to topical map JSON", default=None)
    parser.add_argument("--competitor-data", help="Path to competitor data JSON", default=None)
    parser.add_argument("--output", help="Output JSON file path", default=None)
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)

    topical_map = None
    if args.topical_map:
        with open(args.topical_map, "r", encoding="utf-8") as f:
            topical_map = json.load(f)

    competitor_data = None
    if args.competitor_data:
        with open(args.competitor_data, "r", encoding="utf-8") as f:
            competitor_data = json.load(f)

    result = analyze_serp_intent(
        args.central_entity, args.niche, args.source_context, topical_map, competitor_data
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[analyze_serp_intent] Saved to {args.output}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
