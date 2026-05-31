# Workflow: Entity-EAV Mapper

## Purpose
Map every entity in the niche using the Entity-Attribute-Value (EAV) framework
as defined by Koray Tuğberk GÜBÜR. The goal is not to list entities — it is to
achieve Topical Coverage through proper EAV structuring.

## Critical Rules From the Course Material

**Entity stuffing does NOT increase Topical Coverage.**
**Attribute stuffing does NOT increase Topical Coverage.**

Coverage requires:
1. The entity is DEFINED — not just mentioned
2. The entity is CONNECTED to related entities through its attributes
3. The macro-context of the document MATCHES the query context for this entity
4. The attribute depth is SUFFICIENT — not surface-level descriptors

Example of INSUFFICIENT coverage:
- "The battery has good quality and long life" → no coverage
- "The battery type affects performance" → no coverage

Example of SUFFICIENT coverage:
- Entity: Battery | Attribute: Chemistry | Values: LiFePO4, NCA, NMC, LTO, LiPo, NiFe, Zn-Air, NaNiCl
- Entity: Battery | Attribute: Voltage | Values: operating voltage, charging voltage, peak voltage,
  nominal voltage, display voltage, motor voltage, voltage regulator, voltage stability
- Entity: Battery | Attribute: Durability | Values: vibration resistance, water exposure tolerance,
  shock resistance, overcharge protection, cycle life (number), humidity range, temperature range (min/max)

AND: All these attributes must be connected BACK to each other and to the central entity.
Covering durability without connecting it back to the battery's chemistry type
dilutes topical consolidation even if the information is individually accurate.

## Context Matters for Every Entity

The same entity produces different EAV maps depending on Source Context.

Example: "Country" entity
- For a Visa Consultancy: attributes processed = visa requirements, processing time,
  application procedures, consulate locations, document checklist
- For a Real Estate Consultancy: attributes processed = property laws, foreign ownership rules,
  climate impact on property value, infrastructure, investment zones

The attribute values ARE the same (country has all these attributes). But which ones
belong in MAIN CONTENT vs SUPPLEMENTARY CONTENT depends on Source Context.

## Inputs
- `central_entity` — Primary entity of the content network
- `source_context` — How the brand monetizes (determines which attributes are primary)
- `niche` — Industry context
- `scraped_content` — Existing site content if auditing
- `competitor_entities` — Entities found on competitor sites

## Execution Steps

### Step 1 — Entity Classification
For every entity discovered, classify it:
- **Central Entity**: appears in EVERY part of the content network
- **Core Entities**: appear in Core Section — directly connected to main attribute
- **Outer Entities**: appear in Outer Section — connected to minor attributes
- **Bridge Entities**: entities that connect Core and Outer Sections (Contextual Bridges)

Entity Types (for Schema.org and query processing):
- Brand, Product, Person, Place, Concept, Process, Feature, Material, Event, Organization

### Step 2 — Attribute Mapping Per Entity
For each entity:

1. Identify ALL relevant attributes — not just the obvious ones
   Think at the same depth as the battery example:
   - What are the technical specifications?
   - What are the performance characteristics?
   - What are the durability/reliability factors?
   - What are the materials/composition factors?
   - What are the compatibility/relationship factors?
   - What are the comparative factors vs alternatives?

2. For each attribute, determine:
   - Is this a MAIN attribute (belongs in Core Section per Source Context)?
   - Is this a MINOR attribute (belongs in Outer Section)?
   - Which document in the topical map should own this attribute's macro-context?

3. Identify DERIVED attributes:
   What additional attributes emerge from the main attribute?
   Example: Main attribute "quality" → derived: durability, reliability, performance rating,
   warranty coverage, maintenance requirements, failure modes

### Step 3 — Value Assignment
For each Entity-Attribute pair:

1. Assign SPECIFIC, VERIFIABLE factual values — not vague descriptors
   - NOT "high quality battery" → this is not a value
   - YES "LiFePO4 chemistry, 48V, 20Ah, 1000+ cycle life" → these are values

2. Flag missing values: Which attributes exist but have no specific values yet?
   These are content creation targets.

3. Identify value conflicts: Is contradictory information present across sources?
   Flag these for resolution.

### Step 4 — Entity Connection Mapping
Map how entities connect to each other:

1. Which entities share attributes? (Co-occurrence relationships)
2. Which entity is most PROMINENT — appears in the most connection paths?
3. Where are the DISCONNECTED attributes?
   (An attribute of Entity A that has no connection back to Entity B — even though
   it should. These disconnections dilute topical consolidation.)

4. Identify the ASSOCIATION WEAKNESS:
   Example from course material: Processing "20 Facts about Lithium Iron Phosphate"
   without connecting it to "Electric Scooter Battery" is a weak association because
   the search engine has no query sequences, paths, or documents that mention these
   two together. The association chain must be built:
   Electric Scooter → Battery → Battery Materials → Lithium Iron Phosphate

5. Build the anchor text variation map:
   The Central Entity ALWAYS appears in anchor texts with a SYNONYM value.
   Map all valid synonyms for each entity for internal linking.

### Step 5 — Schema.org Alignment
For each entity, define:
- Primary Schema.org type
- Key properties that correspond to the mapped attributes
- Relationships to other Schema.org types
- Which attributes translate to structured data markup opportunities

### Step 6 — EAV Coverage Score
For each entity, score attribute completeness:
- 0-30%: Entity is mentioned but not defined or connected
- 31-60%: Main attributes covered, derived attributes missing
- 61-85%: Good coverage, some value specificity gaps
- 86-100%: Full coverage — defined, connected, specific values, contextually placed

## Output Schema
```json
{
  "mapped_at": "",
  "central_entity": "",
  "source_context": "",
  "entities": [
    {
      "name": "",
      "type": "",
      "classification": "central|core|outer|bridge",
      "prominence_score": 0,
      "eav_coverage_score": 0,
      "attributes": [
        {
          "attribute": "",
          "attribute_type": "main|derived|minor",
          "section": "core|outer",
          "values": [
            {
              "value": "",
              "is_specific": true,
              "is_verifiable": true,
              "missing": false
            }
          ],
          "connected_to_attributes": [],
          "completeness_score": 0
        }
      ],
      "entity_connections": [
        {
          "connected_entity": "",
          "connection_type": "",
          "association_strength": "strong|medium|weak",
          "association_chain": []
        }
      ],
      "disconnected_attributes": [],
      "schema_type": "",
      "anchor_text_variations": []
    }
  ],
  "knowledge_graph_summary": {
    "total_entities": 0,
    "central_entity_coverage": 0,
    "overall_coverage_score": 0,
    "disconnection_risks": [],
    "critical_gaps": []
  }
}
```

## Self-Improvement Notes
After each run, document:
- Were there attributes that consistently lacked specific values across niches?
- Which entity types most often had disconnection risks?
- Were there niches where the association chain required more intermediate steps?
