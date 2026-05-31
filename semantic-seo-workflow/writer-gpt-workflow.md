# Workflow: WriterGPT — Semantic Content Writer

## Origin & Methodology
Built on Koray Tuğberk GÜBÜR's Holistic SEO methodology — holisticseo.digital
This workflow takes a PageGPT brief as input and writes the actual page content.
Every writing decision is grounded in Koray's exact definitions from the course material.

---

## Purpose
WriterGPT is the execution layer after PageGPT. PageGPT builds the structure.
WriterGPT fills that structure with semantically optimized, human-like content that:
- Satisfies Major Query Needs 100% in Main Content
- Applies Micro Semantics at the sentence level
- Separates Main Content from Supplementary Content correctly
- Uses the Contextual Flow sequence defined in the brief — never reorders it
- Writes with specific EAV depth (numbers, studies, institutions, not vague descriptors)
- Reads as authoritative, human, and natural — not robotic or AI-patterned

---

## Trigger Phrases
- "run WriterGPT for [client_name] — page brief: [page-slug]"
- "write the content for [page topic] using the brief"
- "generate content from this page brief"
- "WriterGPT for [client_name] [page type]"

---

## Client Data Root

All client paths in this workflow are resolved from a configurable client-data root:

- Preferred: `[CLIENT_DATA_ROOT]/[client_name]/...`
- Backward-compatible fallback: `client_data/[client_name]/...`

---

## Pre-Flight Checks

Before writing a single word:

1. Load the PageGPT brief from `[CLIENT_DATA_ROOT]/[client_name]/page-briefs/[page-slug]-brief.md`
   If no brief exists — STOP. Tell the user to run PageGPT first. Do not write without a brief.

2. Load `[CLIENT_DATA_ROOT]/[client_name]/business_profile.json`
   Confirm: Source Context, Central Entity, Central Search Intent, brand voice

3. Check the brief for:
   - Contextual Flow sequence (the ORDER of sections — must not be changed)
   - Main Content sections (macro-context — major query needs)
   - Contextual Border question (the transition point)
   - Supplementary Content sections (micro-contexts — minor query needs)
   - EAV depth per section (what specific values are required)
   - Micro Semantics notes (predicate choices, subject/object positioning)
   - Word count targets per section
   - Internal linking architecture (anchor texts, target pages)

4. Confirm the page type:
   Service Page / Blog Post / Product Page / Landing Page / Informational Page
   Each type has different tone, structure, and sentence opening rules.

5. Confirm the industry:
   Legal / Healthcare / Finance / Technical / General SEO & Blog
   Industry determines authority framing, compliance language, and E-E-A-T signals.

---

## Exact Concept Definitions Used In Writing

### What Makes a Sentence Semantically Correct

**Sequence Modeling (Micro Semantics)**
Word order changes relevance distribution.
"Teacher yelled students" → "teacher" carries the weight
"Students are yelled by Teacher" → "students" carry the weight
The predicate signals the overall context. "Yell" annotates differently from "shout."
All surrounding word sequence probabilities change with one predicate change.
Every sentence must be written with intentional subject/object/predicate positioning.

**First Sentence After Every Heading**
This is the most important sentence in any section.
It must DEFINE or ANSWER directly — never use rhetoric, never tease, never introduce without answering.
Following Koray's rule: the first word of a paragraph signals whether it answers or avoids.

**Define With "Is"**
Every entity introduced must be DEFINED — not just mentioned.
Use definitional sentence structures:
- "[Entity] is [definition with specific attributes and values]"
- "As defined by [authority source], [entity] is..."
- "[Entity], a [type] that [specific function/attribute], [value]..."

This applies Koray's core coverage rule: if you didn't DEFINE X, you didn't cover it.

**Numeric Values and Specificity**
Vague descriptors = not coverage. Specific values = coverage.
Every claim must be anchored to:
- A number, percentage, measurement, or duration
- A named study, university, institution, or researcher
- A specific attribute value (not "high quality" but "48V, 20Ah, LiFePO4")

Examples of correct specificity:
✅ "A study conducted at Peking University entitled 'Effects of Dehydration and Rehydration'
   followed 12 men who abstained from drinking water for 36 hours."
✅ "According to a study published in the European Journal of Nutrition, certain mineral
   waters rich in magnesium and sodium improve bowel movement frequency."
✅ "Physical performance, from a medical point of view, objectively measures whole body
   function related to mobility."
✅ "Asthma is a chronic respiratory disease, as it causes the airways to narrow and
   inflammation, as defined by Dr. Elizabeth Matsui, a renowned allergist and asthma expert."

❌ "Drinking water has many health benefits."
❌ "Studies show that hydration improves performance."
❌ "Water is good for the body in multiple ways."

**Represented and Representative Queries in Main Content**
The macro-context heading must include the represented query language.
The body of the section must satisfy all probable representative query interpretations.
Example: A section on "benefits of drinking water" must also satisfy:
"benefits of hydration," "benefits of drinking water in the morning,"
"benefits of drinking a lot of water" — all within the same macro-context flow.

**Contextual Coverage Balance**
No single sub-context should dominate the page.
If one attribute is processed too heavily, it dilutes the prominence of others.
Each H2 section should have proportional coverage relative to its query weight.

**Internal Links — Placement Rules**
Main Content: first internal link appears early, anchored to a synonym of the Central Entity
Main Content: last internal link in Main Content = highest commercial intent target
Supplementary Content: majority of internal links sit here
Anchor text must ALWAYS use synonym values of the Central Entity — never generic text

---

## Execution Steps

### Step 1 — Read the Brief Completely
Do not start writing until you have read every section of the PageGPT brief.
Extract and confirm:
- H1 (do not change this)
- Contextual Flow sequence (do not reorder)
- EAV depth notes per section
- Micro Semantics notes (predicates, subject/object positioning)
- Word count targets
- Internal links with anchor texts
- FAQ questions

### Step 2 — Establish the Macro-Context Opening

Write the introduction following these rules:

**Rule 1**: H1 is already defined in the brief — use it exactly as written.

**Rule 2**: First paragraph after H1 must:
- Define the Central Entity or page topic immediately using "is" structure
- Include the represented query naturally in the first 1-2 sentences
- Anchor the macro-context so the search engine understands the page's dominant context
- Contain a numeric value, study reference, or authoritative source in the first paragraph
- Include the brand image signal (position the brand as the authority on this topic)

**Rule 3**: The opening paragraph sets the Contextual Vector for the entire page.
If the macro-context is wrong here, the entire page's relevance is compromised.

**Example opening structure**:
"[Entity] is [definition with specific attribute + value], as [authority source] defines it.
[Represented query phrase] has been shown to [specific outcome with numeric value],
according to [named institution or researcher]. In this [page type], we will [what user gets]
based on [evidence/methodology]."

### Step 3 — Write Main Content Sections

For each H2/H3 in the Main Content section of the brief:

**Sentence 1 after heading** — must define or answer directly.
Apply "Define with is":
"[Topic of this section] is [definition]" or
"[Entity] [predicate] [specific attribute with value]"

**Body of section** — apply in this order:
1. Define the entity/concept introduced in the heading
2. Give the specific attribute(s) from the EAV depth notes in the brief
3. Assign specific verifiable values — numbers, studies, institutions
4. Connect this attribute BACK to the central entity and macro-context
5. Use the predicate specified in the Micro Semantics notes of the brief
6. Vary sentence length: mix short declarative sentences with longer explanatory ones
7. Use the subject/object positioning from the brief's micro semantics notes

**First internal link** in Main Content:
Place the first internal link in the first or second H2 section
Anchor text = Central Entity synonym value (from the brief's internal linking table)

**Section transitions**:
End each H2 section with a sentence that bridges naturally to the next section's context
This is not a hard stop — it is a slow contextual transition (Koray's Contextual Flow rule)

**What to avoid**:
❌ Starting a paragraph with "Additionally," "Furthermore," "Moreover," "In conclusion"
❌ Sentences that tease without answering ("There are many reasons why...")
❌ Vague claims without numeric anchors ("research shows," "experts say")
❌ Repeating the heading text in the first sentence verbatim
❌ Stacking multiple internal links in Main Content sections

### Step 4 — Write the Contextual Border Section

This is the transition between Main Content and Supplementary Content.
It is the grouper question from the brief — written as a heading + short section.

Rules:
- The heading IS the grouper question (H2 phrased as a question)
- The body of this section deepens the macro-context while OPENING toward side-topics
- It is NOT a hard break — it is a slow transition
- It mentions the supplementary topics ahead without abandoning the main context
- Word count: shorter than Main Content sections — this is a bridge, not a destination
- Place the last Main Content internal link here or in the section immediately before

### Step 5 — Write Supplementary Content Sections

For each H2 in the Supplementary Content section of the brief:

**Key difference from Main Content**:
Supplementary Content processes micro-contexts AND always connects them to ANOTHER
macro-context (bridging to other topical map nodes).

Rules:
- Each section touches a minor query need — do not over-process it
- Each section must maintain a connection back to the page's macro-context
- Each section must bridge to another topical map node (defined in the brief)
- Internal links are placed HERE — most of the page's linking happens in this section
- Use Contextual Bridges (linkless information alignment) where defined in the brief
- Passage Indexing readiness: each supplementary section must be self-contained
  enough to rank independently as a passage

**Anchor text rule**: Always use synonym values of the Central Entity.
Never use "click here," "learn more," or generic phrases.

### Step 6 — Write the FAQ Section

Rules from Koray's course:
- FAQ answers must NOT repeat Main Content
- Each question targets a NEW representative query variant — one the Main Content
  does not directly address
- Each answer must be self-contained (Passage Indexing — can rank independently)
- Answers should be 40-80 words: direct, complete, no padding
- Use the question formats specified in the brief
- Structure: Question → Define/Answer directly in sentence 1 → Expand with specific value → Close

### Step 7 — Apply AI-Natural Writing Patterns

To ensure content reads as human-authored:

**Sentence variation**:
- Mix short sentences (8-12 words) with medium (18-25 words) and occasional long (30-40 words)
- Never use the same sentence structure twice in a row
- Vary paragraph length: 2-sentence paragraphs mixed with 4-5 sentence paragraphs

**Natural transitions**:
- Use contextual transitions that grow FROM the previous sentence's meaning
- Not: "Additionally, water also helps..." (additive without connection)
- Yes: "This mechanism explains why [X], which in turn affects [Y]..." (causal connection)

**Avoid AI-detectable patterns**:
❌ Starting consecutive sentences with the same word
❌ Using "It is important to note that..." / "It is worth mentioning..."
❌ Lists of 3 items with parallel structure in every paragraph
❌ Ending sections with summary sentences that restate what was just said
❌ Overusing em-dashes, colons, and semicolons in decorative ways
   **Em-dash hard rule**: maximum 1 em-dash per 300 words. Every em-dash must earn its place.
   Before writing an em-dash, ask: does a period, comma, or colon work here instead?
   - ` — This/There/They/It/The` after an independent clause → write a new sentence with a period
   - ` — which/who/whose/that` → use a comma (relative clause)
   - ` — not/never/rather/instead` → use a comma (contrast)
   - ` — [lowercase word]` → use a comma (continuation)
   - ` — [definition/clarification]` → use a colon
   Em-dashes are a known AI-signature pattern. Exceeding the limit is a quality failure.

**Use storytelling anchors**:
- Named researchers, institutions, case subjects (12 men at Peking University)
- Specific scenarios that ground abstract concepts
- Cause-effect chains: "When X occurs, Y results because Z"
- Conditional framing where appropriate: "In patients with X, Y increases by Z%"

**Predicate variety**:
Use Koray's predicate principle — different predicates signal different contexts.
Vary predicates deliberately:
- Not: "Water helps... Water supports... Water aids..."
- Yes: "Water regulates... Hydration triggers... Fluid intake determines..."

### Step 8 — Industry-Specific Rules

**Legal Content**:
- Every claim must reference a specific law, statute, case, or legal definition
- Use neutral tone: "Under [Act/Section], [entity] is defined as..."
- Avoid phrases that constitute legal advice: "You should," "You must"
- Replace with: "In accordance with [law]," "Legal practitioners advise that..."
- Define every legal term on first use with its formal definition

**Healthcare & Medical Content**:
- Follow E-E-A-T: every claim attributed to a named doctor, institution, or study
- Use: "As defined by Dr. [Name], a [specialty]..." / "According to [Institution] research..."
- Avoid unverified claims: no survival rates, treatment outcomes without citation
- Use precise medical terminology on first use + plain language explanation
- Structure: condition definition → mechanism → clinical evidence → patient context

**Finance & Business Content**:
- Anchor every figure to a source: "[X]% according to [Institution] [Year] report"
- Use compliance-safe language: "This is not financial advice. Consult a qualified..."
- Define financial instruments formally on first use
- Use conditional framing: "In scenarios where [X], investors typically see [Y]"

**Technical & Engineering Content**:
- Use precise terminology — never approximate when exact values exist
- Structure: component → specification → function → performance parameter → tolerance
- Tables or structured lists acceptable for specifications (this is Main Content exception)
- Define acronyms on first use: "LiFePO4 (Lithium Iron Phosphate)"

**General SEO & Blog Content**:
- Conversational but authoritative — write as a subject matter expert talking to a peer
- Use "you" and "your" to maintain reader connection
- Anchor authority through specificity, not credential claims
- Open loops early, close them precisely

---

## Output Format

Save to: `[CLIENT_DATA_ROOT]/[client_name]/written-content/[page-slug]-content.md`

```markdown
# [H1 from brief — unchanged]

[Opening paragraph — defines entity, anchors macro-context, includes numeric value]

---

## MAIN CONTENT

### [H2 from brief]
[Body — define with "is", specific EAV values, study/institution anchor, predicate from brief]
[Internal link 1: [anchor text — Central Entity synonym] → [target page]]

#### [H3 from brief if applicable]
[Body — deeper attribute + specific value, connects back to H2 context]

### [H2 from brief]
[Body]

[...continue all Main Content H2s in exact Contextual Flow order from brief...]

---

## [CONTEXTUAL BORDER — Grouper Question as H2]
[Short bridging section — deepens macro-context, opens toward supplementary topics]
[Last Main Content internal link: [anchor text] → [target page]]

---

## SUPPLEMENTARY CONTENT

### [H2 from brief]
[Body — micro-context, connected to another macro-context node, internal links here]
[Internal link: [anchor text] → [target page]]

### [H2 from brief]
[Body]

[...continue all Supplementary Content H2s...]

---

## Frequently Asked Questions

**[Question from brief]**
[Answer — self-contained, 40-80 words, defines directly, specific value]

**[Question from brief]**
[Answer]

[...continue all FAQ questions from brief...]

---

*Word count: [actual count]*
*Page type: [type]*
*Central Entity: [entity]*
*Topical Map Section: [Core/Outer] — [Tier]*
```

---

## Quality Checklist Before Finalizing

Run through this before saving:

**Macro Semantics**
- [ ] H1 unchanged from brief
- [ ] Represented query appears naturally in opening paragraph
- [ ] All representative query variants covered across Main Content sections
- [ ] Site-wide N-grams consistent with Source Context (loaded from business_profile.json)
- [ ] Heading vectors read coherently as a list (tells the full story top-to-bottom)

**EAV Depth**
- [ ] Every entity introduced is DEFINED with "is" structure
- [ ] Every attribute has a SPECIFIC verifiable value (no vague descriptors)
- [ ] Attributes are connected BACK to each other and to the Central Entity
- [ ] At least one named study/institution/researcher per major section

**Contextual Structure**
- [ ] Contextual Flow sequence matches the brief exactly — no sections reordered
- [ ] Main Content sections contain minimal internal links (first + last only)
- [ ] Contextual Border is present as a gradual transition — not a hard section break
- [ ] Supplementary Content carries the majority of internal links
- [ ] Each Supplementary Content section bridges to another topical map node

**Micro Semantics**
- [ ] First sentence after every heading defines or answers directly
- [ ] Predicates match the brief's Micro Semantics notes
- [ ] Subject/object positioning applied as specified in brief
- [ ] No two consecutive paragraphs use the same sentence opening structure

**Internal Linking**
- [ ] First internal link in Main Content uses Central Entity synonym anchor
- [ ] Last internal link in Main Content targets highest commercial intent page
- [ ] All anchor texts use synonym values — no generic anchors
- [ ] Supplementary Content contains majority of links

**AI-Natural Patterns**
- [ ] Sentence length varies throughout — no uniform rhythm
- [ ] No AI-signature phrases ("It is important to note," "Furthermore," "Moreover")
- [ ] Em-dash count ≤ 1 per 300 words — replace excess with period/comma/colon per the em-dash rule above
- [ ] Transitions are causal/contextual — not additive
- [ ] FAQ answers are self-contained and do not repeat Main Content

**Industry Compliance**
- [ ] Legal: no unauthorized advice, all claims referenced to statute or case
- [ ] Healthcare: all claims attributed to named source, E-E-A-T signals present
- [ ] Finance: figures sourced, compliance language included
- [ ] Technical: precise terminology, acronyms defined on first use

---

## Restrictions — Non-Negotiable

From Koray's course definitions:

- **Never reorder the Contextual Flow** — the ORDER of sections is the SEO decision
- **Never write a heading then fail to define** — the first sentence must answer
- **Never use vague descriptors** — "good quality," "many benefits," "various studies"
  are not coverage. Specific values only.
- **Never stuff keywords** — mentioning the represented query 20 times ≠ coverage
- **Never write FAQ answers that repeat Main Content** — they must extend into
  NEW representative query variants
- **Never place internal links randomly in Main Content** — first link + last link only,
  both using Central Entity synonym anchors
- **Never break the Main Content / Supplementary Content separation** —
  supplementary micro-contexts do not belong in main content
- **Never use the same predicate consecutively** — predicate variety signals
  contextual richness to the search engine

---

## Self-Improvement Notes

After each piece of content is published and indexed, evaluate:
- Did the page rank for its represented query?
- Did it capture featured snippets or PAA positions? (Responsiveness signals)
- Which FAQ answers ranked as independent passages? (Passage Indexing success)
- Were there sections where the Contextual Coverage was imbalanced?
- Did any sections use vague descriptors that should have had specific values?
- Did the Contextual Border successfully transition to Supplementary Content
  without disrupting the page's topical consolidation?
- Update this workflow with findings after each evaluation cycle
