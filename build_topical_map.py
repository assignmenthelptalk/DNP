#!/usr/bin/env python3
"""
Tool: build_topical_map.py
Job: Build a structured Topical Map using Koray Tuğberk GÜBÜR's exact definitions.
     Topical Map = Core Section (main attribute of central entity + Source Context)
                 + Outer Section (minor attributes, propagates trust to Core)
     NOT a list of blog posts. NOT entity-attribute connections.
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
exact Topical Map framework from holisticseo.digital.

EXACT DEFINITIONS YOU MUST USE:

TOPICAL MAP: A content network design based on semantics for achieving the topical
authority state by including overall macro contexts and semantics with publication frequency.
Has exactly TWO sections: Core Section and Outer Section.
NOT a blog post list. NOT entity-attribute connections.

SOURCE CONTEXT: The purpose of the brand identity and how the brand monetizes.
Determines which attributes of the central entity belong in Core vs Outer Section.
The SAME central entity produces a COMPLETELY DIFFERENT topical map with a different Source Context.

CORE SECTION: The unification of Source Context with Central Search Intent.
Focuses on the MAIN ATTRIBUTE of the central entity — the attribute that comes from Source Context.
Example: Electric car charger AFFILIATE → main attribute = "quality" → derived: durability, charge time, maintenance
Example: Electric car charger ENGINEER → main attribute = "production" → derived: materials, designs, types
Example: Visa Consultancy → main attribute = "visa" under country context
Example: Divorce Lawyer → main attributes = "divorce" (mediation, trial, alimony) + "legal" (grounds, prenuptial)

OUTER SECTION: Focuses on MINOR attributes of the central entity.
Purpose: improve historical data, increase topical relevance, propagate trust TO Core Section.
Example: Visa Consultancy Outer = culture, geography, climate, language schools (NOT visa topics)
Example: Divorce Lawyer Outer = marriage statistics, relationship types, marriage dynamics

TOPICAL COVERAGE RULES:
- You CANNOT calculate coverage without first defining the topical BORDER
- Stuffing entities or opening new pages does NOT increase coverage
- Coverage requires: DEFINE the entity, CONNECT it to others, MATCH macro-context to query context
- Attribute depth must be SPECIFIC — not "battery quality" but chemistry types, voltage values, cycle life

TOPICAL AUTHORITY FORMULA: Topical Coverage × Historical Data
Historical Data = quality user engagement (not domain age, not time)

VASTNESS-DEPTH-MOMENTUM: Go wider + go deeper + go faster. If one is missing, increase another.

Return ONLY valid JSON. No preamble. No markdown fences."""


def build_topical_map(central_entity: str, niche: str, source_context: str,
                      entity_map: dict = None, scraped_content: dict = None) -> dict:
    """Build a topical map using Koray's exact framework."""
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        entity_context = ""
        if entity_map and entity_map.get("entities"):
            entities = entity_map["entities"]
            core_entities = [e["name"] for e in entities if e.get("classification") in ["central", "core"]][:10]
            outer_entities = [e["name"] for e in entities if e.get("classification") == "outer"][:10]
            entity_context = f"""
Known Core Entities: {', '.join(core_entities)}
Known Outer Entities: {', '.join(outer_entities)}
EAV Coverage Score: {entity_map.get('knowledge_graph_summary', {}).get('overall_coverage_score', 'unknown')}
"""

        content_context = ""
        if scraped_content and scraped_content.get("heading_structure"):
            h1s = scraped_content["heading_structure"].get("h1", [])
            h2s = scraped_content["heading_structure"].get("h2", [])
            content_context = f"""
Existing site headings:
H1s (macro-contexts established): {', '.join(h1s[:8])}
H2s (context vectors in use): {', '.join(h2s[:15])}
"""

        prompt = f"""Build a complete Topical Map for this source.

Central Entity: {central_entity}
Niche: {niche}
Source Context (how the brand monetizes): {source_context}
{entity_context}
{content_context}

STEP 1 — Define the Topical Border:
What is included in this topical map? What is excluded?
Where does this topical map end and another begin?
What would a competitor do to shift this border and shrink your coverage?

STEP 2 — Build the Core Section:
What is the MAIN ATTRIBUTE of {central_entity} that connects to the Source Context?
What are the DERIVED attributes from the main attribute?
Build Tier 1 topics (directly tied to central entity through main attribute)
Build Tier 2 topics (derived attributes — must connect BACK to main attribute)

For each Core topic:
- macro_context: What is the single dominant context this page establishes?
- query_context_match: Does the macro-context match how the search engine interprets the query?
- eav_depth: What specific EAV depth does this topic require?
- suggested_h1: Write an H1 that processes the macro-context (not generic, not design)
- suggested_h2s: List H2s in correct Contextual Flow order (ORDER MATTERS — changes relevance)
- contextual_border_question: What grouper question transitions from Main → Supplementary Content?
- supplementary_bridges_to: Which other topical map nodes does this page's Supplementary Content bridge to?

Define Macro Semantics for the Core Section:
- site_wide_ngrams: What 2-3 word phrases should appear consistently across all Core pages?
- question_formats: What question structures signal the query context? (What is X? How to X?)
- predicate_distributions: What action verbs signal the correct context site-wide?

STEP 3 — Build the Outer Section:
Identify MINOR attributes of {central_entity} — attributes NOT covered in the Core Section.
These are topics that build historical data and propagate trust signals TO the Core Section.
Each Outer topic must have a linkless or linked connection back to Core Section.

For each Outer topic:
- Which minor attribute of the central entity does this process?
- How does this topic connect back to the Core Section (linked or linkless bridge)?
- What does this topic's Supplementary Content link to in the Core Section?

STEP 4 — Map Contextual Bridges:
For each bridge between topical map nodes:
- From which node → to which node
- Bridge type: linked (hypertext) or linkless (information alignment)
- If linked: what anchor text? (must use synonym value of central entity)

STEP 5 — Coverage Gap Analysis:
For each gap, specify:
- gap_type: undefined | disconnected | wrong_macro_context | shallow_depth
- NOT just "missing topic" — explain WHICH coverage rule is violated

STEP 6 — Vastness-Depth-Momentum Assessment:
Is the topical map wide enough? (Vastness)
Is each node covered with sufficient EAV depth? (Depth)
What publication frequency is needed? (Momentum)
Which of the three should be prioritized first?

Return this exact JSON:
{{
  "built_at": "{datetime.now().isoformat()}",
  "central_entity": "{central_entity}",
  "niche": "{niche}",
  "source_context": "{source_context}",
  "central_search_intent": "",
  "topical_border_definition": "",
  "topical_coverage_score": 0,
  "core_section": {{
    "main_attribute": "",
    "derived_attributes": [],
    "tier_1_topics": [
      {{
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
      }}
    ],
    "tier_2_topics": [],
    "macro_semantics": {{
      "site_wide_ngrams": [],
      "question_formats": [],
      "predicate_distributions": [],
      "heading_vector_pattern": ""
    }}
  }},
  "outer_section": {{
    "tier_1_topics": [],
    "tier_2_topics": [],
    "tier_3_topics": [],
    "contextual_bridges": [
      {{
        "from_node": "",
        "to_node": "",
        "bridge_type": "linked|linkless",
        "anchor_text": "",
        "bridge_description": ""
      }}
    ]
  }},
  "coverage_gaps": [
    {{
      "topic": "",
      "section": "core|outer",
      "gap_type": "undefined|disconnected|wrong_macro_context|shallow_depth",
      "priority": "high|medium|low",
      "reason": ""
    }}
  ],
  "vastness_depth_momentum": {{
    "vastness_assessment": "",
    "depth_assessment": "",
    "momentum_recommendation": "",
    "priority_recommendation": "vastness|depth|momentum"
  }}
}}"""

        print(f"[build_topical_map] Building topical map | Entity: {central_entity} | Context: {source_context}")

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=6000,
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
    parser = argparse.ArgumentParser(description="Build a topical map using Koray's exact framework")
    parser.add_argument("central_entity", help="Primary entity of the content network")
    parser.add_argument("--niche", required=True, help="Industry/niche context")
    parser.add_argument("--source-context", required=True,
                        help="How the brand monetizes — determines Core vs Outer attributes")
    parser.add_argument("--entity-map", help="Path to entity map JSON", default=None)
    parser.add_argument("--scraped-content", help="Path to scraped content JSON", default=None)
    parser.add_argument("--output", help="Output JSON file path", default=None)
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)

    entity_map = None
    if args.entity_map:
        with open(args.entity_map, "r", encoding="utf-8") as f:
            entity_map = json.load(f)

    scraped = None
    if args.scraped_content:
        with open(args.scraped_content, "r", encoding="utf-8") as f:
            scraped = json.load(f)

    result = build_topical_map(
        args.central_entity, args.niche, args.source_context, entity_map, scraped
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[build_topical_map] Saved to {args.output}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
