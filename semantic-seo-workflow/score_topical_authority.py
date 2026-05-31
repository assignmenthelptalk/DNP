#!/usr/bin/env python3
"""
Tool: score_topical_authority.py
Job: Score Topical Authority using Koray Tuğberk GÜBÜR's exact formula.
     Topical Authority = Topical Coverage × Historical Data
     Historical Data = quality user engagement (NOT domain age, NOT time)
     Topical Coverage = defined, connected, contextually matched, deep EAV
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
Topical Authority formula from holisticseo.digital.

EXACT FORMULA: Topical Authority = Topical Coverage × Historical Data

TOPICAL COVERAGE — scored on these EXACT rules:
1. Is the topical border DEFINED? (Cannot calculate coverage without it)
2. Are entities DEFINED — not just mentioned? (mention ≠ coverage)
3. Are entities CONNECTED to each other through their attributes?
4. Does the macro-context of each document MATCH the query context?
5. Is the attribute depth SUFFICIENT with specific, verifiable values?
   ("battery quality" = not coverage | "LiFePO4 48V 1000+ cycles" = coverage)
6. Are attributes connected BACK to each other?
   (Isolated attribute mentions dilute topical consolidation)

HISTORICAL DATA — NOT domain age, NOT time. Quality user engagement:
- Fresh historical data > older historical data
- Non-quality engagement (low-quality session logs) DEMOTES a website
- Current rankings reflect historical data from at least 6 months ago
- Signals that count: clicks, hover-overs, impressions, query session logs,
  text-selects, clickless searches, even rankings at position 94
- Non-quality pages in the network make quality pages rank lower

SEMANTIC COMPETITOR: A site with the SAME Source Context targeting the SAME Central Entity.
Not just any site in the same niche.

BROAD CORE ALGORITHM UPDATE (BCAU) RISK:
Semantic distances between queries change after BCAUs.
Content targeting old representative query interpretations loses rankings.

CONTENT CONFIGURATION: The ongoing process of optimizing relevance and responsiveness
continuously according to changed semantic distances. Required when query semantics shift.

Return ONLY valid JSON. No preamble. No markdown fences."""


def score_topical_authority(topical_map: dict, entity_map: dict,
                             competitor_data: dict, query_clusters: dict = None) -> dict:
    """Score topical authority using the exact Topical Coverage × Historical Data formula."""
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        coverage_score = topical_map.get("topical_coverage_score", 0)
        topical_border = topical_map.get("topical_border_definition", "undefined")
        gaps = topical_map.get("coverage_gaps", [])
        vdm = topical_map.get("vastness_depth_momentum", {})

        entities = entity_map.get("entities", [])
        entity_coverage = entity_map.get("knowledge_graph_summary", {})

        competitors = competitor_data.get("competitors", [])

        query_context = ""
        if query_clusters:
            high_distance = query_clusters.get("high_semantic_distance_clusters", [])
            bcau_flags = query_clusters.get("bcau_risk_flags", [])
            config_needed = query_clusters.get("content_configuration_needed", [])
            query_context = f"""
High semantic distance clusters: {json.dumps(high_distance[:5])}
BCAU risk flags: {json.dumps(bcau_flags[:5])}
Content configuration needed: {json.dumps(config_needed[:5])}
"""

        prompt = f"""Score Topical Authority using the formula: Topical Authority = Topical Coverage × Historical Data

SOURCE DATA:

Topical Border Defined: {topical_border}
Current Topical Coverage Score: {coverage_score}/100
Coverage Gaps: {json.dumps(gaps[:10], indent=2)}
Vastness-Depth-Momentum State: {json.dumps(vdm, indent=2)}

Entity Map Summary:
Total Entities: {len(entities)}
Overall EAV Coverage: {entity_coverage.get('overall_coverage_score', 0)}/100
Disconnection Risks: {json.dumps(entity_coverage.get('disconnection_risks', [])[:5])}
Critical Gaps: {json.dumps(entity_coverage.get('critical_gaps', [])[:5])}

Competitors (semantic competitors = same Source Context, same Central Entity):
{json.dumps([{{
    'name': c.get('name', ''),
    'url': c.get('url', ''),
    'topical_coverage': c.get('topical_coverage', [])[:5],
    'threat_level': c.get('threat_level', '')
}} for c in competitors[:5]], indent=2)}
{query_context}

SCORE THESE DIMENSIONS:

1. TOPICAL COVERAGE SCORE (0-100)
Score based on the EXACT coverage rules:
- Is the topical border defined? (-20 if not)
- Are entities defined (not just mentioned)? Score the depth.
- Are entities connected to each other? Score the network strength.
- Do macro-contexts match query contexts? Check each topic node.
- Is attribute depth sufficient? Check for specific vs vague values.
- Are attributes connected back to each other? Check for isolation.

2. HISTORICAL DATA QUALITY SIGNALS (0-100)
Score based on observable signals from the content network:
- Is publication frequency consistent? (Momentum score)
- Are there non-quality pages diluting the network?
- Is Content Configuration happening? (Are pages updated when query semantics shift?)
- Are BCAU risk flags high? (Outdated representative query targeting = bad signal)

3. EAV DEPTH SCORE (0-100)
For each entity: how specific are the values?
Are attributes connected back to each other (not isolated)?
Is the association chain built correctly (A → attribute → B → attribute → C)?

4. SEMANTIC ALIGNMENT SCORE (0-100)
Do represented queries have matching representative query coverage?
Are major query needs satisfied in Main Content?
Are minor query needs correctly placed in Supplementary Content?

5. COMPETITIVE GAP ANALYSIS
Where do semantic competitors outperform?
Where is there an opportunity to build topical coverage they lack?
Which gaps in YOUR topical map, if filled, would most impact the BCAU outcomes?

6. OVERALL TOPICAL AUTHORITY SCORE (0-100)
Weighted composite: Coverage (40%) × Historical Signals (30%) + EAV (15%) + Semantic (15%)

7. PRIORITY ACTIONS BY VASTNESS-DEPTH-MOMENTUM
What should be done FIRST?
- Vastness: which topical border gaps to fill?
- Depth: which nodes need deeper EAV coverage?
- Momentum: what publication frequency is needed?

Return this exact JSON:
{{
  "scored_at": "{datetime.now().isoformat()}",
  "formula": "Topical Authority = Topical Coverage × Historical Data",
  "scores": {{
    "topical_coverage": 0,
    "historical_data_signals": 0,
    "eav_depth": 0,
    "semantic_alignment": 0,
    "overall_topical_authority": 0
  }},
  "coverage_analysis": {{
    "topical_border_status": "defined|undefined|partial",
    "entity_definition_score": 0,
    "entity_connection_score": 0,
    "macro_context_match_score": 0,
    "attribute_depth_score": 0,
    "attribute_connection_score": 0
  }},
  "historical_data_analysis": {{
    "publication_frequency_signal": "strong|moderate|weak",
    "network_dilution_risk": "high|medium|low",
    "content_configuration_status": "active|needed|not_started",
    "bcau_exposure_level": "high|medium|low"
  }},
  "competitor_comparison": [
    {{
      "competitor": "",
      "their_coverage_score": 0,
      "your_coverage_score": 0,
      "gap": 0,
      "gap_direction": "ahead|behind",
      "their_strengths": [],
      "your_opportunities": []
    }}
  ],
  "priority_gaps": [
    {{
      "topic": "",
      "gap_type": "undefined|disconnected|wrong_macro_context|shallow_depth|missing",
      "impact_score": 0,
      "section": "core|outer",
      "vastness_depth_momentum_category": "vastness|depth|momentum",
      "recommended_action": "create|expand|reconfigure|remove",
      "competitor_coverage": "none|partial|full"
    }}
  ],
  "quick_wins": [],
  "content_configuration_tasks": [],
  "vastness_depth_momentum_plan": {{
    "current_weakest": "vastness|depth|momentum",
    "recommended_priority": "",
    "publication_frequency_target": "",
    "estimated_authority_gain": {{
      "30_days": 0,
      "90_days": 0,
      "180_days": 0
    }}
  }}
}}"""

        print("[score_topical_authority] Calculating Topical Authority = Topical Coverage × Historical Data")

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
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
    parser = argparse.ArgumentParser(description="Score topical authority: Coverage × Historical Data")
    parser.add_argument("--topical-map", required=True, help="Path to topical map JSON")
    parser.add_argument("--entity-map", required=True, help="Path to entity map JSON")
    parser.add_argument("--competitor-data", required=True, help="Path to competitor data JSON")
    parser.add_argument("--query-clusters", help="Path to query clusters JSON", default=None)
    parser.add_argument("--output", help="Output JSON file path", default=None)
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)

    with open(args.topical_map, "r", encoding="utf-8") as f:
        topical_map = json.load(f)
    with open(args.entity_map, "r", encoding="utf-8") as f:
        entity_map = json.load(f)
    with open(args.competitor_data, "r", encoding="utf-8") as f:
        competitor_data = json.load(f)

    query_clusters = None
    if args.query_clusters:
        with open(args.query_clusters, "r", encoding="utf-8") as f:
            query_clusters = json.load(f)

    result = score_topical_authority(topical_map, entity_map, competitor_data, query_clusters)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[score_topical_authority] Saved to {args.output}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
