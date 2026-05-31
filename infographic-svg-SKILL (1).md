---
name: infographic-svg
description: Generate production-quality SVG infographics that embed directly into any web page — WordPress, Webflow, Shopify, Next.js, plain HTML, or any other stack. Replicates the Svalbardi.com illustrated infographic style — icon grids, annotated diagrams, stat callouts, comparison tables, human/entity silhouettes, and process flows. Read this skill before generating ANY infographic SVG. Every type has a precise template.
---

# SVG Infographic Skill

## What This Skill Produces

Inline SVG code that embeds directly into any web page or CMS.
No image upload required. No external dependencies. Search engines read the text.
Every infographic reinforces the Subject Entity and Object Entities of its section.

**Compatible with any web stack:**
- WordPress — paste into an HTML block
- Webflow — embed via HTML embed component
- Shopify — paste into section or page content
- Next.js / React — use as inline JSX or dangerouslySetInnerHTML
- Squarespace / Wix — paste into code block
- Plain HTML — paste directly into the `<body>`
- Any headless CMS — store as raw HTML field

The SVG is self-contained. It carries its own styles, fonts, and colors inline.
No CSS file, no JS file, no external image — just one block of code that works everywhere.

This skill replicates the Svalbardi.com infographic system:
- Illustrated icon grids (2×2, 3×2, 4×2)
- Annotated entity diagrams with callout lines
- Stat callouts (single large number inline)
- Side-by-side entity comparison with silhouettes
- Step-by-step process flows with icons
- Data comparison tables with color coding
- Inline definition cards (entity + attributes)

---

## Core Rules — Apply to Every SVG

**Rule 1 — Subject Entity in the largest text element**
The Subject Entity (the main entity of the section, not the page) must be the largest,
most visually dominant text in the SVG. Object Entities are supporting elements.

**Rule 2 — Alt text on every SVG**
Every SVG must have a `<title>` and `<desc>` element as the FIRST children of `<svg>`.
Format: `<title>[Subject Entity] — [main attribute] — [key value or context]</title>`
Never: `<title>infographic</title>` — too vague, no SEO value.

**Rule 3 — Real text, never paths for labels**
All labels, values, headings must be `<text>` elements — not converted to paths.
Search engines index SVG `<text>`. They do not index `<path>` shapes used as text.

**Rule 4 — Brand colors from business_profile.json**
Always check the client's `primary_color` and `secondary_color` before generating.
Default fallback only if profile not available: primary `#1B3A6B`, accent `#C9A84C`.

**Rule 5 — Section-level, not page-level**
Each infographic visualises ONE section's subject entity.
Never make a single "page summary" infographic. Make one per major section.
Placement: immediately after the section's H2, before the prose begins.

**Rule 6 — Specific EAV values only**
Every data point shown must be a specific, verifiable value.
NOT "high pass rate" → YES "95% pass rate"
NOT "fast delivery" → YES "delivered before your deadline"
NOT "expert writers" → YES "all writers hold CII Diploma or above"

**Rule 7 — viewBox for responsiveness**
Always use `viewBox` not fixed `width`/`height` on the root `<svg>`.
Any browser or CMS will scale it correctly with: `width="100%" style="max-width:800px"`

---

## Embed Wrapper — Works on Any Stack

Every SVG gets wrapped in a `<figure>` tag. This is standard HTML — it works
on WordPress, Webflow, Shopify, Next.js, plain HTML, or any other stack.

```html
<figure class="infographic-figure" style="text-align:center; margin: 2rem auto;">
  <svg viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg"
       width="100%" style="max-width:800px; display:block; margin:0 auto;"
       role="img" aria-labelledby="svg-title-[unique-id]">
    <title id="svg-title-[unique-id]">[Subject Entity] — [attribute] — [value/context]</title>
    <desc>[1-2 sentence description of what the infographic shows]</desc>
    <!-- SVG content here -->
  </svg>
  <figcaption style="font-size:0.85rem; color:#666; margin-top:0.5rem;">
    [Caption including represented query phrase]
  </figcaption>
</figure>
```

**Stack-specific notes:**
- **WordPress** — paste into an HTML block in the block editor
- **Webflow** — use an Embed element, paste the full `<figure>` block
- **Shopify** — paste into a Custom HTML section or liquid template
- **React / Next.js** — wrap in a component, replace `class` with `className`,
  or use `dangerouslySetInnerHTML` for the raw SVG string
- **Plain HTML** — paste directly inside `<body>` wherever the infographic appears
- **Headless CMS** — store the full `<figure>` block as a rich text or HTML field

The `infographic-figure` class is purely a hook for optional custom CSS.
The SVG renders correctly with zero additional CSS.

---

## TYPE 1 — Icon Grid (2×2, 3×2, 4×2)

**When to use:** Sections listing multiple attributes, benefits, symptoms, or types of one entity.
Svalbardi uses this for "benefits of drinking water", "symptoms of overhydration", etc.
Each cell = one EAV triple: Entity → Attribute → Value shown visually.

**Subject Entity placement:** In the header bar, large and bold.
**Object Entities:** Each cell's icon + heading (the attributes of the subject entity).

**SVG viewBox:** `0 0 800 420` for 2×2, `0 0 800 560` for 3×2, `0 0 800 680` for 4×2

### Icon Grid Template (2×2 example — adapt for other sizes)

```svg
<svg viewBox="0 0 800 420" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="ig-title">
  <title id="ig-title">[Subject Entity] — [main attribute] — [context]</title>
  <desc>[What this grid shows and why it matters]</desc>

  <!-- Background -->
  <rect width="800" height="420" fill="#F8F9FC" rx="12"/>

  <!-- Header bar -->
  <rect width="800" height="64" fill="[primary_color]" rx="12"/>
  <rect y="52" width="800" height="12" fill="[primary_color]"/>
  <text x="400" y="40" text-anchor="middle" font-family="Georgia, serif"
        font-size="22" font-weight="bold" fill="white">
    [Subject Entity — Main Heading]
  </text>

  <!-- Accent line under header -->
  <rect y="64" width="800" height="3" fill="[accent_color]"/>

  <!-- CELL 1 — Top Left (x=20, y=80, w=370, h=155) -->
  <rect x="20" y="80" width="370" height="155" fill="white" rx="10"
        stroke="[accent_color]" stroke-width="1.5" stroke-opacity="0.3"/>
  <!-- Icon circle -->
  <circle cx="70" cy="140" r="30" fill="[primary_color]" opacity="0.12"/>
  <text x="70" y="148" text-anchor="middle" font-size="26">🔵</text>
  <!-- Replace emoji with relevant icon for content type -->
  <!-- Cell heading -->
  <text x="115" y="125" font-family="Georgia, serif" font-size="15"
        font-weight="bold" fill="[primary_color]">[Attribute Name]</text>
  <!-- Cell value/description — wrap at ~35 chars -->
  <text x="115" y="145" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[Specific value or short description]</text>
  <text x="115" y="162" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[continuation if needed]</text>
  <!-- Stat highlight (optional) -->
  <text x="115" y="218" font-family="Georgia, serif" font-size="28"
        font-weight="bold" fill="[accent_color]">[Key Stat]</text>
  <text x="190" y="218" font-family="Arial, sans-serif" font-size="12"
        fill="#666">[stat label]</text>

  <!-- CELL 2 — Top Right (x=410, y=80, w=370, h=155) -->
  <rect x="410" y="80" width="370" height="155" fill="white" rx="10"
        stroke="[accent_color]" stroke-width="1.5" stroke-opacity="0.3"/>
  <circle cx="460" cy="140" r="30" fill="[primary_color]" opacity="0.12"/>
  <text x="460" y="148" text-anchor="middle" font-size="26">🟡</text>
  <text x="505" y="125" font-family="Georgia, serif" font-size="15"
        font-weight="bold" fill="[primary_color]">[Attribute Name]</text>
  <text x="505" y="145" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[Specific value]</text>
  <text x="505" y="162" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[continuation]</text>

  <!-- CELL 3 — Bottom Left (x=20, y=248, w=370, h=155) -->
  <rect x="20" y="248" width="370" height="155" fill="white" rx="10"
        stroke="[accent_color]" stroke-width="1.5" stroke-opacity="0.3"/>
  <circle cx="70" cy="308" r="30" fill="[primary_color]" opacity="0.12"/>
  <text x="70" y="316" text-anchor="middle" font-size="26">🟢</text>
  <text x="115" y="293" font-family="Georgia, serif" font-size="15"
        font-weight="bold" fill="[primary_color]">[Attribute Name]</text>
  <text x="115" y="313" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[Specific value]</text>
  <text x="115" y="330" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[continuation]</text>

  <!-- CELL 4 — Bottom Right (x=410, y=248, w=370, h=155) -->
  <rect x="410" y="248" width="370" height="155" fill="white" rx="10"
        stroke="[accent_color]" stroke-width="1.5" stroke-opacity="0.3"/>
  <circle cx="460" cy="308" r="30" fill="[primary_color]" opacity="0.12"/>
  <text x="460" y="316" text-anchor="middle" font-size="26">🔴</text>
  <text x="505" y="293" font-family="Georgia, serif" font-size="15"
        font-weight="bold" fill="[primary_color]">[Attribute Name]</text>
  <text x="505" y="313" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[Specific value]</text>
  <text x="505" y="330" font-family="Arial, sans-serif" font-size="12"
        fill="#444">[continuation]</text>

  <!-- Footer -->
  <rect y="408" width="800" height="12" fill="[primary_color]" opacity="0.15" rx="0"/>
  <text x="400" y="418" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="10" fill="#999">[website URL]</text>
</svg>
```

**Scaling for grid sizes:**
- 3×2 grid: add 6 cells, viewBox height = 560, row height = 155 each
- 4×2 grid: add 8 cells, viewBox height = 680, row height = 155 each
- Each row starts at: y=80 (row1), y=248 (row2), y=416 (row3), y=584 (row4)

**Icon selection rules:**
Use semantically relevant emoji that match the content entity:
- Medical/health: 🫀 🫁 🧠 💧 🩸 🦴 👁️ 🦷
- Process/action: ✅ ⚡ 🔄 📋 ✍️ 🕐 💳 📨
- Insurance/finance: 🛡️ 📊 📜 🏆 🔒 💰
- Education: 🎓 📚 ✏️ 🏅 📝 🔍
- Warning/symptoms: ⚠️ 🚨 ❌ 💢
Always prefer a specific emoji over a generic one. 💧 for water, 🫀 for heart, not ❤️

---

## TYPE 2 — Stat Callout (Inline Single Number)

**When to use:** After any sentence that contains a specific numeric value worth emphasising.
Svalbardi places these inline — not as separate sections. They break the wall of text visually.
Keep these compact — they are accent pieces, not full infographics.

**viewBox:** `0 0 800 140`

```svg
<svg viewBox="0 0 800 140" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="sc-title">
  <title id="sc-title">[Subject Entity] [attribute]: [value]</title>
  <desc>[One sentence explaining this statistic in context]</desc>

  <!-- Background -->
  <rect width="800" height="140" fill="[primary_color]" rx="10"/>

  <!-- Left accent block -->
  <rect width="12" height="140" fill="[accent_color]" rx="10"/>
  <rect x="8" width="8" height="140" fill="[accent_color]"/>

  <!-- Main stat — Subject Entity as the number -->
  <text x="130" y="85" font-family="Georgia, serif" font-size="64"
        font-weight="bold" fill="[accent_color]">[VALUE]</text>

  <!-- Label and context -->
  <text x="320" y="55" font-family="Georgia, serif" font-size="20"
        font-weight="bold" fill="white">[Attribute Label]</text>
  <text x="320" y="80" font-family="Arial, sans-serif" font-size="14"
        fill="white" opacity="0.85">[Context — what this value means]</text>
  <text x="320" y="100" font-family="Arial, sans-serif" font-size="14"
        fill="white" opacity="0.85">[continuation if needed]</text>

  <!-- Source/URL bottom right -->
  <text x="780" y="128" text-anchor="end" font-family="Arial, sans-serif"
        font-size="10" fill="white" opacity="0.5">[website URL]</text>
</svg>
```

---

## TYPE 3 — Side-by-Side Entity Comparison

**When to use:** Comparing two or three entities that share the same set of attributes.
Svalbardi uses human silhouettes for male vs female body water content.
For CII: Certificate vs Diploma vs ACII. For legal: Mediation vs Litigation.

**viewBox:** `0 0 800 480` for 2 entities, `0 0 800 480` for 3 entities (narrower columns)

```svg
<svg viewBox="0 0 800 480" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="comp-title">
  <title id="comp-title">[Entity A] vs [Entity B] — [attribute] comparison</title>
  <desc>[What is being compared and the key difference]</desc>

  <!-- Background -->
  <rect width="800" height="480" fill="#F8F9FC" rx="12"/>

  <!-- Header -->
  <rect width="800" height="64" fill="[primary_color]" rx="12"/>
  <rect y="52" width="800" height="12" fill="[primary_color]"/>
  <text x="400" y="40" text-anchor="middle" font-family="Georgia, serif"
        font-size="22" font-weight="bold" fill="white">
    [Entity A] vs [Entity B]
  </text>
  <rect y="64" width="800" height="3" fill="[accent_color]"/>

  <!-- Divider between columns -->
  <line x1="400" y1="80" x2="400" y2="460" stroke="[accent_color]"
        stroke-width="1.5" stroke-dasharray="6,4" stroke-opacity="0.4"/>

  <!-- === ENTITY A — LEFT COLUMN === -->
  <!-- Entity label -->
  <rect x="20" y="80" width="360" height="40" fill="[primary_color]" opacity="0.08" rx="8"/>
  <text x="200" y="106" text-anchor="middle" font-family="Georgia, serif"
        font-size="17" font-weight="bold" fill="[primary_color]">[Entity A Name]</text>

  <!-- Entity icon/silhouette -->
  <!-- For human silhouettes, use SVG path or large emoji -->
  <text x="200" y="210" text-anchor="middle" font-size="80">🧑</text>
  <!-- Replace with SVG body path for higher quality when content requires it -->

  <!-- Primary stat — largest number -->
  <text x="200" y="290" text-anchor="middle" font-family="Georgia, serif"
        font-size="52" font-weight="bold" fill="[accent_color]">[Value A]</text>
  <text x="200" y="315" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#555">[Attribute label]</text>

  <!-- Secondary attributes — 3 rows -->
  <rect x="40" y="335" width="320" height="34" fill="[primary_color]" opacity="0.06" rx="6"/>
  <text x="200" y="357" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 2]: <tspan font-weight="bold">[Value]</tspan></text>

  <rect x="40" y="374" width="320" height="34" fill="[primary_color]" opacity="0.03" rx="6"/>
  <text x="200" y="396" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 3]: <tspan font-weight="bold">[Value]</tspan></text>

  <rect x="40" y="413" width="320" height="34" fill="[primary_color]" opacity="0.06" rx="6"/>
  <text x="200" y="435" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 4]: <tspan font-weight="bold">[Value]</tspan></text>

  <!-- === ENTITY B — RIGHT COLUMN === -->
  <rect x="420" y="80" width="360" height="40" fill="[accent_color]" opacity="0.15" rx="8"/>
  <text x="600" y="106" text-anchor="middle" font-family="Georgia, serif"
        font-size="17" font-weight="bold" fill="[primary_color]">[Entity B Name]</text>

  <text x="600" y="210" text-anchor="middle" font-size="80">🧑</text>

  <text x="600" y="290" text-anchor="middle" font-family="Georgia, serif"
        font-size="52" font-weight="bold" fill="[accent_color]">[Value B]</text>
  <text x="600" y="315" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#555">[Attribute label]</text>

  <rect x="440" y="335" width="320" height="34" fill="[accent_color]" opacity="0.08" rx="6"/>
  <text x="600" y="357" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 2]: <tspan font-weight="bold">[Value]</tspan></text>

  <rect x="440" y="374" width="320" height="34" fill="[accent_color]" opacity="0.04" rx="6"/>
  <text x="600" y="396" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 3]: <tspan font-weight="bold">[Value]</tspan></text>

  <rect x="440" y="413" width="320" height="34" fill="[accent_color]" opacity="0.08" rx="6"/>
  <text x="600" y="435" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Attribute 4]: <tspan font-weight="bold">[Value]</tspan></text>

  <!-- Footer -->
  <text x="400" y="470" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="10" fill="#aaa">[website URL]</text>
</svg>
```

**For 3-entity comparison:** Divide width into thirds: col1 cx=133, col2 cx=400, col3 cx=667.
Add a second divider at x=533. Reduce font sizes by 2pt and secondary attributes to 2 rows.

---

## TYPE 4 — Annotated Entity Diagram

**When to use:** When a physical entity (body, product, system, document, building) has
multiple components that need individual labelling with values.
Svalbardi: organs labelled with their water percentage.
CII equivalent: CII Diploma structure labelled with modules, levels, pass marks.

**viewBox:** `0 0 800 500`

```svg
<svg viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="ann-title">
  <title id="ann-title">[Central Entity] — [attribute] breakdown with [specific values]</title>
  <desc>[What is being annotated and what the values mean]</desc>

  <!-- Background -->
  <rect width="800" height="500" fill="#F8F9FC" rx="12"/>

  <!-- Header -->
  <rect width="800" height="60" fill="[primary_color]" rx="12"/>
  <rect y="48" width="800" height="12" fill="[primary_color]"/>
  <text x="400" y="38" text-anchor="middle" font-family="Georgia, serif"
        font-size="21" font-weight="bold" fill="white">[Heading with Subject Entity]</text>
  <rect y="60" width="800" height="3" fill="[accent_color]"/>

  <!-- Central entity representation — center of diagram -->
  <!-- Use emoji, SVG shapes, or simplified illustration -->
  <!-- For a document/certificate: -->
  <rect x="300" y="90" width="200" height="260" fill="white" rx="8"
        stroke="[primary_color]" stroke-width="2"/>
  <rect x="310" y="100" width="180" height="20" fill="[primary_color]" opacity="0.15" rx="3"/>
  <text x="400" y="115" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="[primary_color]" font-weight="bold">[Entity Name]</text>
  <!-- Add internal structure lines to represent entity components -->
  <line x1="320" y1="135" x2="480" y2="135" stroke="#ddd" stroke-width="1"/>
  <line x1="320" y1="155" x2="460" y2="155" stroke="#ddd" stroke-width="1"/>
  <line x1="320" y1="175" x2="470" y2="175" stroke="#ddd" stroke-width="1"/>
  <line x1="320" y1="195" x2="450" y2="195" stroke="#ddd" stroke-width="1"/>
  <line x1="320" y1="215" x2="465" y2="215" stroke="#ddd" stroke-width="1"/>

  <!-- CALLOUT 1 — Left side annotation -->
  <!-- Callout line from entity point to label box -->
  <line x1="300" y1="135" x2="220" y2="135" stroke="[accent_color]" stroke-width="1.5"/>
  <line x1="220" y1="135" x2="160" y2="110" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="300" cy="135" r="4" fill="[accent_color]"/>
  <!-- Label box -->
  <rect x="20" y="95" width="145" height="50" fill="[primary_color]" rx="6"/>
  <text x="92" y="115" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[accent_color]">[Component Value]</text>
  <text x="92" y="133" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="white">[Component Label]</text>

  <!-- CALLOUT 2 — Left side annotation -->
  <line x1="300" y1="175" x2="210" y2="175" stroke="[accent_color]" stroke-width="1.5"/>
  <line x1="210" y1="175" x2="160" y2="185" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="300" cy="175" r="4" fill="[accent_color]"/>
  <rect x="20" y="160" width="145" height="50" fill="[primary_color]" rx="6"/>
  <text x="92" y="180" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[accent_color]">[Component Value]</text>
  <text x="92" y="198" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="white">[Component Label]</text>

  <!-- CALLOUT 3 — Left side annotation -->
  <line x1="300" y1="215" x2="200" y2="240" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="300" cy="215" r="4" fill="[accent_color]"/>
  <rect x="20" y="225" width="145" height="50" fill="[primary_color]" rx="6"/>
  <text x="92" y="245" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[accent_color]">[Component Value]</text>
  <text x="92" y="263" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="white">[Component Label]</text>

  <!-- CALLOUT 4 — Right side annotation -->
  <line x1="480" y1="145" x2="560" y2="120" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="480" cy="145" r="4" fill="[accent_color]"/>
  <rect x="560" y="95" width="145" height="50" fill="[accent_color]" rx="6"/>
  <text x="632" y="115" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[primary_color]">[Component Value]</text>
  <text x="632" y="133" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="[primary_color]">[Component Label]</text>

  <!-- CALLOUT 5 — Right side annotation -->
  <line x1="480" y1="185" x2="570" y2="190" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="480" cy="185" r="4" fill="[accent_color]"/>
  <rect x="570" y="165" width="145" height="50" fill="[accent_color]" rx="6"/>
  <text x="642" y="185" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[primary_color]">[Component Value]</text>
  <text x="642" y="203" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="[primary_color]">[Component Label]</text>

  <!-- CALLOUT 6 — Right side annotation -->
  <line x1="480" y1="225" x2="565" y2="255" stroke="[accent_color]" stroke-width="1.5"/>
  <circle cx="480" cy="225" r="4" fill="[accent_color]"/>
  <rect x="570" y="235" width="145" height="50" fill="[accent_color]" rx="6"/>
  <text x="642" y="255" text-anchor="middle" font-family="Georgia, serif"
        font-size="12" font-weight="bold" fill="[primary_color]">[Component Value]</text>
  <text x="642" y="273" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="[primary_color]">[Component Label]</text>

  <!-- Bottom label for the central entity -->
  <text x="400" y="375" text-anchor="middle" font-family="Georgia, serif"
        font-size="16" font-weight="bold" fill="[primary_color]">[Central Entity Name]</text>
  <text x="400" y="395" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="12" fill="#666">[Main attribute descriptor]</text>

  <!-- Footer -->
  <text x="400" y="490" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="10" fill="#aaa">[website URL]</text>
</svg>
```

**Callout placement rules:**
- Maximum 6 callouts (3 left, 3 right) — more creates visual noise
- Left callouts: entity points at x=300, labels end at x=165
- Right callouts: entity points at x=480, labels start at x=560
- Vertical spacing between callouts: minimum 65px
- Circle dots at connection point: r=4, fill=[accent_color]

---

## TYPE 5 — Process Flow (Horizontal Steps)

**When to use:** Any section explaining a sequence — how a service works, how to apply,
how a qualification is structured, how a process unfolds.
Svalbardi uses this for "how the body uses water" type process explanations.

**viewBox:** `0 0 800 300` for 3-4 steps, `0 0 800 380` for 5-6 steps

```svg
<svg viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="pf-title">
  <title id="pf-title">[Process name] — [number] steps — [context]</title>
  <desc>[What this process achieves and for whom]</desc>

  <!-- Background -->
  <rect width="800" height="300" fill="#F8F9FC" rx="12"/>

  <!-- Header -->
  <rect width="800" height="56" fill="[primary_color]" rx="12"/>
  <rect y="44" width="800" height="12" fill="[primary_color]"/>
  <text x="400" y="34" text-anchor="middle" font-family="Georgia, serif"
        font-size="20" font-weight="bold" fill="white">[Process heading]</text>
  <rect y="56" width="800" height="3" fill="[accent_color]"/>

  <!-- Horizontal connector line through all step circles -->
  <line x1="80" y1="155" x2="720" y2="155" stroke="[accent_color]"
        stroke-width="2" stroke-opacity="0.4"/>

  <!-- STEP 1 (cx=100 for 4 steps: 100, 300, 500, 700) -->
  <!-- Step circle -->
  <circle cx="100" cy="155" r="36" fill="[primary_color]"/>
  <circle cx="100" cy="155" r="32" fill="white"/>
  <!-- Step number -->
  <text x="100" y="147" text-anchor="middle" font-family="Georgia, serif"
        font-size="11" fill="[primary_color]" opacity="0.7">STEP</text>
  <text x="100" y="165" text-anchor="middle" font-family="Georgia, serif"
        font-size="18" font-weight="bold" fill="[primary_color]">1</text>
  <!-- Icon above circle (optional) -->
  <text x="100" y="116" text-anchor="middle" font-size="22">📋</text>
  <!-- Step heading below -->
  <text x="100" y="205" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[primary_color]">[Step Heading]</text>
  <!-- Step description — 2 lines max, ~16 chars each -->
  <text x="100" y="223" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 1]</text>
  <text x="100" y="238" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 2]</text>

  <!-- Arrow between step 1 and 2 -->
  <polygon points="168,149 168,161 182,155" fill="[accent_color]" opacity="0.7"/>

  <!-- STEP 2 (cx=300) -->
  <circle cx="300" cy="155" r="36" fill="[primary_color]"/>
  <circle cx="300" cy="155" r="32" fill="white"/>
  <text x="300" y="147" text-anchor="middle" font-family="Georgia, serif"
        font-size="11" fill="[primary_color]" opacity="0.7">STEP</text>
  <text x="300" y="165" text-anchor="middle" font-family="Georgia, serif"
        font-size="18" font-weight="bold" fill="[primary_color]">2</text>
  <text x="300" y="116" text-anchor="middle" font-size="22">💬</text>
  <text x="300" y="205" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[primary_color]">[Step Heading]</text>
  <text x="300" y="223" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 1]</text>
  <text x="300" y="238" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 2]</text>

  <polygon points="368,149 368,161 382,155" fill="[accent_color]" opacity="0.7"/>

  <!-- STEP 3 (cx=500) -->
  <circle cx="500" cy="155" r="36" fill="[accent_color]"/>
  <circle cx="500" cy="155" r="32" fill="white"/>
  <text x="500" y="147" text-anchor="middle" font-family="Georgia, serif"
        font-size="11" fill="[primary_color]" opacity="0.7">STEP</text>
  <text x="500" y="165" text-anchor="middle" font-family="Georgia, serif"
        font-size="18" font-weight="bold" fill="[primary_color]">3</text>
  <text x="500" y="116" text-anchor="middle" font-size="22">💳</text>
  <text x="500" y="205" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[primary_color]">[Step Heading]</text>
  <text x="500" y="223" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 1]</text>
  <text x="500" y="238" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 2]</text>

  <polygon points="568,149 568,161 582,155" fill="[accent_color]" opacity="0.7"/>

  <!-- STEP 4 (cx=700) — Final step highlighted -->
  <circle cx="700" cy="155" r="36" fill="[accent_color]"/>
  <circle cx="700" cy="155" r="32" fill="[primary_color]"/>
  <text x="700" y="147" text-anchor="middle" font-family="Georgia, serif"
        font-size="11" fill="white" opacity="0.7">STEP</text>
  <text x="700" y="165" text-anchor="middle" font-family="Georgia, serif"
        font-size="18" font-weight="bold" fill="white">4</text>
  <text x="700" y="116" text-anchor="middle" font-size="22">📨</text>
  <text x="700" y="205" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[primary_color]">[Step Heading]</text>
  <text x="700" y="223" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 1]</text>
  <text x="700" y="238" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="11" fill="#555">[Description line 2]</text>

  <!-- Footer -->
  <text x="400" y="290" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="10" fill="#aaa">[website URL]</text>
</svg>
```

**Step cx positions:**
- 3 steps: 133, 400, 667
- 4 steps: 100, 300, 500, 700
- 5 steps: 80, 240, 400, 560, 720
- 6 steps: viewBox width 900, cx: 75, 225, 375, 525, 675, 825

**Arrow midpoint formula:** Arrow polygon x = (cx_current + cx_next) / 2 ± 14

---

## TYPE 6 — Colour-Coded Comparison Table

**When to use:** Multiple entities, same attributes, need rapid visual scanning.
Best for qualification comparisons, pricing tiers, option selection pages.
Svalbardi uses this for animal vs human water percentages.

**viewBox:** `0 0 800 [64 + (n_rows × 52) + 40]`

```svg
<svg viewBox="0 0 800 428" xmlns="http://www.w3.org/2000/svg"
     width="100%" style="max-width:800px;" role="img" aria-labelledby="ct-title">
  <title id="ct-title">[Entity A] vs [Entity B] vs [Entity C] — [attribute] comparison</title>
  <desc>[What the table shows and the key takeaway]</desc>

  <!-- Background -->
  <rect width="800" height="428" fill="#F8F9FC" rx="12"/>

  <!-- Header -->
  <rect width="800" height="60" fill="[primary_color]" rx="12"/>
  <rect y="48" width="800" height="12" fill="[primary_color]"/>
  <text x="400" y="38" text-anchor="middle" font-family="Georgia, serif"
        font-size="20" font-weight="bold" fill="white">[Table Title]</text>
  <rect y="60" width="800" height="3" fill="[accent_color]"/>

  <!-- Column headers row -->
  <rect x="0" y="63" width="800" height="44" fill="[primary_color]" opacity="0.08"/>
  <!-- Attribute col header -->
  <text x="110" y="91" text-anchor="middle" font-family="Georgia, serif"
        font-size="14" font-weight="bold" fill="[primary_color]">Attribute</text>
  <!-- Entity col headers -->
  <text x="310" y="91" text-anchor="middle" font-family="Georgia, serif"
        font-size="14" font-weight="bold" fill="[primary_color]">[Entity A]</text>
  <text x="510" y="91" text-anchor="middle" font-family="Georgia, serif"
        font-size="14" font-weight="bold" fill="[primary_color]">[Entity B]</text>
  <text x="700" y="91" text-anchor="middle" font-family="Georgia, serif"
        font-size="14" font-weight="bold" fill="[primary_color]">[Entity C]</text>

  <!-- Column dividers -->
  <line x1="215" y1="63" x2="215" y2="428" stroke="#ddd" stroke-width="1"/>
  <line x1="415" y1="63" x2="415" y2="428" stroke="#ddd" stroke-width="1"/>
  <line x1="615" y1="63" x2="615" y2="428" stroke="#ddd" stroke-width="1"/>

  <!-- ROW 1 (y=107, alternating fill: even=white, odd=primary opacity 0.04) -->
  <rect x="0" y="107" width="800" height="52" fill="white"/>
  <text x="110" y="138" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[accent_color]">[Attribute 1]</text>
  <text x="310" y="138" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value A1]</text>
  <text x="510" y="138" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value B1]</text>
  <text x="700" y="138" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value C1]</text>

  <!-- ROW 2 -->
  <rect x="0" y="159" width="800" height="52" fill="[primary_color]" opacity="0.04"/>
  <text x="110" y="190" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[accent_color]">[Attribute 2]</text>
  <text x="310" y="190" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value A2]</text>
  <text x="510" y="190" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value B2]</text>
  <text x="700" y="190" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value C2]</text>

  <!-- ROW 3 -->
  <rect x="0" y="211" width="800" height="52" fill="white"/>
  <text x="110" y="242" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[accent_color]">[Attribute 3]</text>
  <text x="310" y="242" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value A3]</text>
  <text x="510" y="242" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value B3]</text>
  <text x="700" y="242" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value C3]</text>

  <!-- ROW 4 -->
  <rect x="0" y="263" width="800" height="52" fill="[primary_color]" opacity="0.04"/>
  <text x="110" y="294" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[accent_color]">[Attribute 4]</text>
  <text x="310" y="294" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value A4]</text>
  <text x="510" y="294" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value B4]</text>
  <text x="700" y="294" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value C4]</text>

  <!-- ROW 5 -->
  <rect x="0" y="315" width="800" height="52" fill="white"/>
  <text x="110" y="346" text-anchor="middle" font-family="Georgia, serif"
        font-size="13" font-weight="bold" fill="[accent_color]">[Attribute 5]</text>
  <text x="310" y="346" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value A5]</text>
  <text x="510" y="346" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value B5]</text>
  <text x="700" y="346" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="13" fill="#333">[Value C5]</text>

  <!-- Highlight row for recommended entity (optional — color the cell) -->
  <!-- Example: highlight Entity B column for rows 1-5 -->
  <!-- Add a rect over that column with accent color, low opacity, on top -->
  <rect x="415" y="107" width="200" height="260" fill="[accent_color]" opacity="0.08" rx="0"/>

  <!-- Footer -->
  <rect x="0" y="388" width="800" height="40" fill="[primary_color]" opacity="0.06" rx="0"/>
  <text x="400" y="413" text-anchor="middle" font-family="Arial, sans-serif"
        font-size="10" fill="#888">[website URL]</text>
</svg>
```

**Row height formula:** Each row = 52px. viewBox height = 64 (header) + 44 (col header) + (n_rows × 52) + 40 (footer)
**For yes/no values:** Replace text with ✓ (fill #4CAF50) or ✗ (fill #EF5350)
**For highlighted column:** Add `<rect>` overlay on that column with accent color opacity 0.08

---

## Pre-Generation Checklist

Before writing any SVG, answer these 6 questions:

1. **Which TYPE fits this section?**
   - List of attributes → Type 1 (Icon Grid)
   - Single important number → Type 2 (Stat Callout)
   - Two or three entities being compared with same attributes → Type 3 (Side-by-Side)
   - One entity with labelled components → Type 4 (Annotated Diagram)
   - Sequential steps → Type 5 (Process Flow)
   - Multiple entities in a table format → Type 6 (Comparison Table)

2. **What is the Subject Entity?**
   The main entity of THIS section (not the whole page).

3. **What are the Object Entities?**
   The surrounding context elements that set the macro-context for the subject.

4. **What is the alt text?**
   `[Subject Entity] — [main attribute] — [key value or context phrase]`

5. **What brand colors apply?**
   Check `business_profile.json` → `brand_assets.primary_color` and `secondary_color`

6. **Where does this infographic go on the page?**
   - Immediately after the section H2 (before prose) = reinforces macro-context
   - At the contextual border = bridges main and supplementary content
   - Within supplementary content = supports passage indexing

---

## Quality Standards — Match Svalbardi Level

**What makes Svalbardi's infographics work:**
1. Every infographic is section-level, not page-level
2. The title of each infographic contains the exact query phrase for that section
3. Values are always specific — never vague descriptors
4. The visual hierarchy is: value (largest) → label (medium) → context (smallest)
5. Consistent brand colors throughout — no rainbow of unrelated colors
6. Clean white space — elements are not crowded
7. The footer always contains the brand URL — every infographic is attributable

**Common mistakes to avoid:**
- Generic icons that don't match the content entity (graduation cap for insurance)
- Vague text values ("highly qualified" instead of "CII Diploma or above")
- Too many elements — maximum 8 data points per infographic
- Missing alt text or generic alt text ("infographic")
- Missing `<title>` and `<desc>` elements
- Text converted to paths (breaks search engine indexing)
- Colors that don't match the brand profile
- Infographic placed at the end of a section instead of the beginning

---

## Saving and Naming

Files saved to: `client_data/[client_name]/infographics/`

Naming convention: `[subject-entity-slug]-[type]-infographic.svg`
Examples:
- `cii-diploma-comparison-infographic.svg`
- `cii-assignment-process-steps-infographic.svg`
- `cii-certificate-stats-infographic.svg`
- `insurance-law-module-diagram-infographic.svg`

**Alt text for CMS media libraries** (copy from SVG `<title>`):
`[Subject Entity] — [attribute] — [value/context]`

This applies to any CMS that has a separate alt text field when uploading images.
If embedding inline SVG directly (no upload), the alt text lives inside the SVG
`<title>` element and is read automatically by search engines and screen readers.
