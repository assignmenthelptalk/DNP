#!/usr/bin/env python3
"""
Tool: discover_entities.py
Job: Discover and map all entities using Koray Tuğberk GÜBÜR's EAV framework.
     Entity stuffing does NOT increase topical coverage.
     This tool discovers entities with their attributes and specific values —
     and maps how entities connect to each other through those attributes.
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
Entity-Attribute-Value (EAV) framework from holisticseo.digital.

You understand these exact definitions:

TOPICAL COVERAGE: Cannot be increased by stuffing entities or attributes.
Coverage requires:
- The entity is DEFINED (not just mentioned)
- The entity is CONNECTED to related entities via its attributes
- The macro-context of the document MATCHES the query context
- The attribute DEPTH is sufficient with specific, verifiable values

EAV DEPTH REQUIREMENT: Think at the depth of this example:
To cover "battery" for electric scooters you need:
- Chemistry types: LiFePO4, NCA, NMC, LTO, LiPo, NiFe, Zn-Air, NaNiCl
- Voltage types: operating, charging, peak, nominal, display, motor, regulator, stability
- Durability: vibration, water exposure, shock, overcharge, cycle life, humidity, temperature min/max
- And ALL of these must be connected BACK to each other and back to the central entity

"Battery quality is high" = NOT coverage.
"LiFePO4 chemistry, 48V, 20Ah, 1000+ cycle life" = coverage.

SOURCE CONTEXT DETERMINES ATTRIBUTE PRIORITY:
The same entity produces different EAV maps depending on Source Context.
"Country" for a Visa Consultancy: visa requirements, processing time, consulate locations
"Country" for a Real Estate Consultancy: property laws, foreign ownership, climate effects

Return ONLY valid JSON. No preamble. No markdown fences."""


def discover_entities(central_entity: str, niche: str, source_context: str,
                      scraped_content: dict = None) -> dict:
    """Discover entities using exact EAV framework from Koray's methodology."""
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        content_context = ""
        if scraped_content and scraped_content.get("heading_structure"):
            headings = scraped_content["heading_structure"]
            content_context = f"""
Existing site heading structure:
H1s: {', '.join(headings.get('h1', [])[:10])}
H2s: {', '.join(headings.get('h2', [])[:20])}
H3s: {', '.join(headings.get('h3', [])[:20])}
"""

        prompt = f"""Discover and map all entities for this niche using the EAV framework.

Central Entity: {central_entity}
Niche: {niche}
Source Context (how the brand monetizes): {source_context}
{content_context}

For each entity provide:
1. Entity name and type (Brand/Product/Person/Place/Concept/Process/Material/Feature)
2. Classification: central | core (main attribute related) | outer (minor attribute related) | bridge
3. Prominence score (1-10, how central to the content network?)
4. ALL relevant attributes — go deep, not surface-level
   For each attribute:
   - attribute name
   - attribute_type: main (from Source Context) | derived (from main) | minor (Outer Section)
   - section: core | outer
   - specific verifiable VALUES (not vague descriptors)
   - which other attributes this connects to
   - completeness score (0-100)
5. Entity connections: which other entities does this connect to, and through which attributes?
   Include the full association chain (A connects to B through attribute X connects to C through Y)
6. Disconnected attributes: attributes that exist but have no connection to other entities
7. Schema.org type
8. Anchor text variations (Central Entity always appears with synonym values in anchors)

Return this exact JSON structure:
{{
  "discovered_at": "{datetime.now().isoformat()}",
  "central_entity": "{central_entity}",
  "niche": "{niche}",
  "source_context": "{source_context}",
  "entities": [
    {{
      "name": "",
      "type": "",
      "classification": "central|core|outer|bridge",
      "prominence_score": 0,
      "eav_coverage_score": 0,
      "attributes": [
        {{
          "attribute": "",
          "attribute_type": "main|derived|minor",
          "section": "core|outer",
          "values": [
            {{
              "value": "",
              "is_specific": true,
              "is_verifiable": true
            }}
          ],
          "connected_to_attributes": [],
          "completeness_score": 0
        }}
      ],
      "entity_connections": [
        {{
          "connected_entity": "",
          "connection_through_attribute": "",
          "association_chain": [],
          "association_strength": "strong|medium|weak"
        }}
      ],
      "disconnected_attributes": [],
      "schema_type": "",
      "anchor_text_variations": []
    }}
  ],
  "knowledge_graph_summary": {{
    "total_entities": 0,
    "overall_coverage_score": 0,
    "disconnection_risks": [],
    "critical_gaps": []
  }}
}}"""

        print(f"[discover_entities] Mapping EAV for: {central_entity} | Context: {source_context}")

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
        return {"error": f"JSON parse error: {str(e)}", "raw_response": response_text[:500]}
    except Exception as e:
        return {"error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Discover entities using EAV framework")
    parser.add_argument("central_entity", help="Primary entity of the content network")
    parser.add_argument("--niche", required=True, help="Industry/niche context")
    parser.add_argument("--source-context", required=True,
                        help="How the brand monetizes (determines core vs outer attributes)")
    parser.add_argument("--scraped-content", help="Path to scraped content JSON", default=None)
    parser.add_argument("--output", help="Output JSON file path", default=None)
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not found in .env file")
        sys.exit(1)

    scraped = None
    if args.scraped_content:
        with open(args.scraped_content, "r", encoding="utf-8") as f:
            scraped = json.load(f)

    result = discover_entities(
        args.central_entity, args.niche, args.source_context, scraped
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"[discover_entities] Saved to {args.output}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
