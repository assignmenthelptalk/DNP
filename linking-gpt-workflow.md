# Workflow: LinkingGPT — Internal Link Architecture Builder

## Origin & Methodology
Built on Koray Tuğberk GÜBÜR's Holistic SEO methodology — holisticseo.digital
LinkingGPT runs AFTER pages are published. It reads all page briefs and written
content across the entire client site, builds the full internal linking map,
and implements or outputs precise linking instructions.

---

## Purpose
Internal links do three things in Koray's framework:
1. Signal to the search engine which page meets which search intent
2. Pass PageRank from Outer Section pages → Core Section pages
3. Build Contextual Bridges between topical map nodes

Without correct internal linking, the Outer Section CANNOT fulfill its purpose
of propagating trust and quality signals to the Core Section.
Without correct anchor texts, the Central Entity has no synonym distribution
across the content network.

This workflow automates all of that after publishing.

---

## Trigger Phrases
- "run LinkingGPT for [client_name]"
- "build the internal linking map for [client_name]"
- "implement internal links for [client_name]"
- "LinkingGPT — update links after publishing [page_name]"

---

## Client Data Root

All client paths in this workflow are resolved from a configurable client-data root:

- Preferred: `[CLIENT_DATA_ROOT]/[client_name]/...`
- Backward-compatible fallback: `client_data/[client_name]/...`

---

## Koray's Exact Internal Linking Rules (Built Into This Workflow)

### Rule 1 — Trust Flows Outer → Core
Outer Section pages MUST link TO Core Section pages.
This is how the Outer Section fulfills its only structural purpose.
Core Section pages do NOT need to link back to Outer Section pages.
The trust signal moves in ONE direction: Outer → Core.

### Rule 2 — Anchor Text Is Always a Central Entity Synonym
The Central Entity ALWAYS appears in anchor texts with a SYNONYM value.
Never use: "click here," "learn more," "read this," "find out," "this page"
Always use: a synonym of the Central Entity that is relevant to the TARGET page's
macro-context — not the SOURCE page's macro-context.

### Rule 3 — Main Content Gets Two Links Maximum
First internal link: placed in the first or second H2 section of Main Content
→ Anchor = Central Entity synonym most relevant to the current section
→ Target = the most topically adjacent Core Section page

Last internal link in Main Content: placed at or just before the Contextual Border
→ Anchor = Central Entity synonym with highest commercial intent signal
→ Target = the highest commercial intent Core Section page

### Rule 4 — Supplementary Content Carries the Majority of Links
Every Supplementary Content section should contain at least one internal link.
These links bridge to other topical map nodes — both Core and Outer.
Anchor texts here use Central Entity synonyms relevant to the TARGET page.

### Rule 5 — No Orphan Pages
Every published page must have at least ONE incoming internal link from another page.
Pages with no incoming links receive no trust signals and no contextual connection.
Identify and fix all orphan pages as part of every LinkingGPT run.

### Rule 6 — No Cannibalization Through Linking
Two pages must NEVER link to each other using the SAME anchor text.
If Page A links to Page B with anchor "divorce lawyer Nairobi,"
then Page B must NOT link back to Page A with the same anchor.
Anchor text variation must be maintained across the entire network.

### Rule 7 — Contextual Bridges Complement Hypertext
Not every connection needs a hypertext link.
Linkless bridges (consistent information alignment across documents) are equally
important. When two pages reference the same entity with consistent attribute
values but no hypertext link, that IS a contextual bridge.
LinkingGPT maps both linked and linkless bridges.

---

## Pre-Flight Checks

Before building any linking map:

1. Load ALL page briefs from `[CLIENT_DATA_ROOT]/[client_name]/page-briefs/`
   Build a list of every page: title, URL slug, topical map section, tier,
   primary entity, attribute focus, Central Entity synonyms used

2. Load ALL written content from `[CLIENT_DATA_ROOT]/[client_name]/written-content/`
   Scan each file for: existing internal links (are any already placed?),
   existing anchor texts, sections where links should go but don't exist yet

3. Load `[CLIENT_DATA_ROOT]/[client_name]/topical_map.json`
   Confirm the Core Section / Outer Section structure and tier assignments

4. Load `[CLIENT_DATA_ROOT]/[client_name]/content_network.json`
   Check the pre-planned internal linking architecture from the audit
   (This was planned BEFORE writing — now we verify it against actual content)

5. Load `[CLIENT_DATA_ROOT]/[client_name]/site_map.json` if it exists
   If it does not exist — CREATE IT now from the page briefs and written content
   (See Site Map Auto-Generation in Step 1 below)

6. Load `[CLIENT_DATA_ROOT]/[client_name]/business_profile.json`
   Confirm: Central Entity, Source Context, Central Search Intent,
   full list of Central Entity synonym values

---

## Execution Steps

### Step 1 — Auto-Generate or Update Site Map

If `site_map.json` does not exist, build it now from the page briefs:

For each page brief found in `[CLIENT_DATA_ROOT]/[client_name]/page-briefs/`:
Extract:
- page title (from Strategic Overview table in brief)
- url_slug (from Strategic Overview table)
- topical_map_section: core or outer
- topical_map_tier: tier_1, tier_2, tier_3
- primary_entity
- attribute_focus
- commercial_intent: high / medium / low
  (high = transactional/commercial page type,
   medium = informational with commercial connection,
   low = pure outer section informational)
- central_entity_synonyms: from the brief's internal linking architecture table
- status: published (if written content file exists) / planned (if only brief exists)

Save to `[CLIENT_DATA_ROOT]/[client_name]/site_map.json`

If `site_map.json` already exists, UPDATE it:
- Add any new pages from new briefs
- Update status from "planned" to "published" for pages with written content
- Add any new Central Entity synonyms found in written content

### Step 2 — Build the Full Link Opportunity Map

For EVERY possible page pair (Page A → Page B), evaluate:

**Should Page A link to Page B?**

Check these conditions:
1. Is Page A in the Outer Section and Page B in the Core Section?
   → YES: this is a trust propagation link. HIGH priority.
2. Does Page A's Supplementary Content process a micro-context that is
   Page B's macro-context?
   → YES: this is a Contextual Bridge link. HIGH priority.
3. Does Page A's Main Content reference an entity that Page B defines?
   → YES: this is a contextual definition link. MEDIUM priority.
4. Are Page A and Page B in the same topical map tier and section?
   → MAYBE: only link if the semantic relationship is strong.
   Linking same-tier pages too heavily dilutes individual page authority.
5. Does Page A already link to Page B?
   → If yes: check the anchor text. Is it a Central Entity synonym?
   If not — flag for anchor text correction.

**What anchor text should the link use?**

The anchor text must:
- Be a synonym value of the Central Entity
- Be relevant to the TARGET page's macro-context (not source page)
- NOT repeat an anchor text already used from Page A to any other page
- NOT repeat an anchor text already used by any other page linking to Page B

Pull synonym options from:
- `site_map.json` → `central_entity_synonyms` array for the TARGET page
- `business_profile.json` → full Central Entity synonym list
- The TARGET page's brief → anchor text variations in the Internal Linking section

**Where in the source page should the link be placed?**

Determine placement using the content structure:
- Is this the first or highest-priority link from this page?
  → Place in Main Content, first or second H2 section
- Is this a commercial intent target?
  → Place at or before the Contextual Border (last Main Content link)
- Is this a topical bridge to another macro-context?
  → Place in the Supplementary Content section whose micro-context
  connects to the target page's macro-context
- Is this an Outer → Core trust link?
  → Place in Supplementary Content of the Outer page

### Step 3 — Identify and Fix Orphan Pages

For every published page in the site map:
Count how many OTHER pages link TO it (incoming links).

If incoming link count = 0 → ORPHAN. Flag immediately.

For each orphan page, find the BEST source page:
- Which published page has a Supplementary Content section whose
  micro-context most closely matches the orphan page's macro-context?
- Which Outer Section page should be propagating trust to this Core page?

Add the orphan fix to the linking implementation plan.

### Step 4 — Check Anchor Text Cannibalization

Build a full anchor text usage matrix:

| Anchor Text | Used By (Source Page) | Points To (Target Page) |
|---|---|---|
| "divorce lawyer Nairobi" | /marriage-statistics | /divorce-lawyer-nairobi |
| "divorce lawyer Nairobi" | /child-custody | ← PROBLEM: same anchor, different page |

Flag any anchor text that:
- Points to two different pages (dilutes the relevance signal)
- Is used by more than 3 pages pointing to the same target
  (over-optimization risk — vary the synonyms)
- Is NOT a Central Entity synonym (replace with correct anchor)

### Step 5 — Map Linkless Contextual Bridges

Scan the written content of every page for:
- References to entities that are the primary entity of another page
  WITHOUT a hypertext link
- Consistent attribute-value pairs that appear across multiple pages
  about the same entity

These are existing linkless bridges. Document them:
```
Page A references [entity X] with [attribute Y = value Z]
Page B's macro-context IS [entity X]
→ Linkless bridge exists: Page A → Page B via [entity X]
→ No hypertext link needed here — bridge already exists
```

This prevents over-linking. If a strong linkless bridge already exists,
adding a hypertext link on top is optional, not required.

### Step 6 — Build the Implementation Plan

Produce a structured implementation plan with three priority levels:

**Priority 1 — Orphan Fixes** (do these first)
Every orphan page must receive at least one incoming link immediately.

**Priority 2 — Outer → Core Trust Links** (highest SEO impact)
All Outer Section pages that are NOT yet linking to Core Section pages.
These are the links that build Topical Authority over time.

**Priority 3 — Supplementary Content Contextual Bridges** (content completeness)
All Supplementary Content sections that should have links but don't yet.

For each planned link, specify exactly:
- Source page URL slug
- Source page section: main_content | contextual_border | supplementary_content
- Source page H2/H3 heading where link goes
- Approximate sentence or paragraph position
- Anchor text (Central Entity synonym)
- Target page URL slug
- Reason this link exists (trust propagation / contextual bridge / definition link)
- Priority: 1 / 2 / 3

### Step 7 — Implementation

LinkingGPT implements links in ONE of two modes depending on how you publish:

---

#### Mode A — CMS Direct Edit (WordPress, Webflow, etc.)
If you publish through a CMS, LinkingGPT outputs:

For each link to add, generate the exact HTML anchor tag:
```html
<a href="/target-page-slug">anchor text synonym here</a>
```

And the exact sentence context it goes into:
```
FILE: [CLIENT_DATA_ROOT]/[client]/written-content/[page-slug]-content.md
SECTION: Supplementary Content → H2: [heading text]
PARAGRAPH: [first/second/third paragraph of that section]
INSERT AFTER: "[exact phrase from the paragraph that precedes the link]"
LINK: <a href="/divorce-lawyer-nairobi">matrimonial lawyer</a>
```

Save the full output to:
`[CLIENT_DATA_ROOT]/[client_name]/linking-plan/linking-instructions-[date].md`

---

#### Mode B — Direct File Edit (Claude Code modifies written content files)
Claude Code opens each written content `.md` file and directly inserts the links:

For each link in the implementation plan:
1. Open `[CLIENT_DATA_ROOT]/[client_name]/written-content/[source-page]-content.md`
2. Find the exact section and paragraph using the placement instructions
3. Insert the markdown link: `[anchor text synonym](URL)`
4. Verify the surrounding context still reads naturally
5. Save the file

After all edits are complete:
6. Re-scan all files to confirm no orphan pages remain
7. Confirm no anchor text cannibalization exists
8. Update `site_map.json` with the new link counts

---

### Step 8 — Generate the Linking Report

Save to: `[CLIENT_DATA_ROOT]/[client_name]/reports/linking-report-[date].md`

```markdown
# LinkingGPT Report — [Client Name]
Date: [date]
Methodology: Koray Tuğberk GÜBÜR — holisticseo.digital

## Summary
- Total pages analyzed: [n]
- Total links added: [n]
- Orphan pages fixed: [n]
- Anchor text corrections: [n]
- Linkless bridges documented: [n]

## Trust Flow Map
[Visual text map showing Outer → Core link paths]

## Link Matrix
| Source Page | Section | Anchor Text | Target Page | Priority |
|---|---|---|---|---|
[full table of all links added]

## Anchor Text Usage Map
| Anchor Text | Used N Times | Points To |
|---|---|---|
[full anchor text inventory]

## Linkless Bridges Documented
[list of all linkless contextual bridges found]

## Remaining Gaps
[pages that still need more incoming links]
[planned pages not yet published — link slots reserved]

## Next Run Triggers
Run LinkingGPT again when:
- [ ] A new page is published
- [ ] A page brief is updated with new supplementary content sections
- [ ] A Broad Core Algorithm Update shifts semantic distances
  (some links may need anchor text reconfiguration)
```

---

## Output Files

```
[CLIENT_DATA_ROOT]/[client_name]/
├── site_map.json                          ← updated with all published pages
├── linking-plan/
│   ├── linking-instructions-[date].md    ← exact placement instructions
│   └── anchor-text-matrix-[date].md      ← full anchor text inventory
└── reports/
    └── linking-report-[date].md          ← summary report
```

---

## How LinkingGPT Fits the Full Workflow

```
1. SEO Audit         → topical_map.json + content_network.json
                       (planned link architecture)

2. PageGPT           → page-briefs/[page]-brief.md
                       (link slots defined per page)

3. WriterGPT         → written-content/[page]-content.md
                       (content written, links as placeholders)

4. PUBLISH PAGES     → pages go live on site

5. LinkingGPT        → reads all briefs + content + topical map
                       builds site_map.json
                       implements all links
                       fixes orphans
                       outputs linking report
```

Run LinkingGPT:
- After every batch of new pages is published
- After a site-wide content configuration update
- After a Broad Core Algorithm Update (anchor text may need reconfiguration)
- Any time a new page is added that creates new link opportunities

---

## Restrictions — Non-Negotiable

- **Never invent a URL** — only link to pages that exist in site_map.json
- **Never use generic anchor text** — every anchor must be a Central Entity synonym
- **Never place more than 2 links in Main Content** — first + last only
- **Never create reciprocal links with the same anchor text** — always vary synonyms
- **Never link two same-tier pages heavily** — dilutes individual page authority
- **Never skip orphan fixes** — an orphan page has zero trust signal regardless of content quality
- **Never over-link a single target** — if 5+ pages already link to a Core page
  with the same anchor, vary the synonyms or skip the link
- **Always update site_map.json after every run** — the map must reflect the live state

---

## Self-Improvement Notes

After each run, document:
- Were there pages where the Outer → Core trust flow was blocked?
- Which anchor texts were most commonly misused (generic vs synonym)?
- Were there niches where linkless bridges were stronger than hypertext links?
- Did any Broad Core Algorithm Update require anchor text reconfiguration?
- Were there page types where the Main Content / Supplementary Content
  separation made linking placement unclear?
