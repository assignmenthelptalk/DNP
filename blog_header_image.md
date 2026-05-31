---
name: blog-header-image
description: >
  Generate polished, publication-quality blog header images as HTML/SVG artifacts — matching the editorial style of premium blogs like Svalbardi.com. Use this skill whenever the user wants to create a blog banner, article header image, featured image, hero image for a post/page, or any visual header that pairs a background photo with a styled title overlay. Trigger even if the user just says "make a blog image", "create a header for my article", "I need a featured image", or "build an image like this" while showing a blog screenshot. Always use this skill for blog/article image generation — don't attempt it without reading this skill first.
---

# Blog Header Image Skill

Creates high-quality, editorial-style blog header images as self-contained HTML files — ready to screenshot, export, or embed. Modeled after premium publication headers (e.g., Svalbardi, National Geographic, NYT Cooking).

---

## Step 1: Gather Inputs

Before building, collect (or infer from context):

| Input | Notes |
|---|---|
| **Title** | Main headline — required |
| **Subtitle** | Optional tagline or category line |
| **Images** | Single URL string OR Array of 2-4 URLs for split grids |
| **Brand/logo** | Optional — URL or SVG path |
| **Color scheme** | Primary + accent (default: dark overlay + white text) |
| **Style** | See style profiles below |
| **Dimensions** | Default: 960×480px (2:1 ratio), common for blog featured images |

If background image is missing, use a beautiful CSS gradient that suits the topic.

---

## Step 2: Choose a Style Profile

Match the style to the brand/topic. Ask if unclear.

### A. `editorial` (default — like Svalbardi)
- Dark semi-transparent panel behind title (not full overlay)
- Decorative geometric border (SVG pattern or CSS)
- Uppercase bold title, lighter subtitle
- Logo top-right inside the border frame
- Teal/navy/forest color palette typical; adapt to brand

### B. `magazine`
- Full-bleed image, title at bottom third
- Large serif display font, white with text-shadow
- Thin colored rule above title
- Optional category badge top-left

### C. `minimal`
- Split layout: 60% image / 40% solid color panel
- Clean sans-serif typography
- Single accent color
- Lots of white space

### D. `bold`
- Full overlay (60% opacity dark)
- Giant centered title, all caps
- Bright accent underline or highlight
- High contrast

### E. `nature/wellness`
- Soft gradient overlay (green/blue tones)
- Rounded decorative frame
- Organic shapes or leaf motifs in SVG

### F. `split-grid`
- Asymmetric or symmetric grid of 2, 3, or 4 images
- 2px "gap" between images (often white or brand-accented)
- Floating centered title panel with strong backdrop-blur
- Best for "roundup" posts, comparisons, or multi-faceted topics

---

## Step 3: Build the HTML Artifact

Create a **single self-contained HTML file** at `/mnt/user-data/outputs/blog-header.html`.

### Core HTML Template

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  /* === RESET & BASE === */
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { width: 960px; height: 480px; overflow: hidden; font-family: sans-serif; }

  /* === CONTAINER === */
  .header {
    position: relative;
    width: 960px;
    height: 480px;
    overflow: hidden;
  }

  /* === BACKGROUND / GRID === */
  .bg, .grid-container {
    position: absolute; inset: 0;
    overflow: hidden;
  }
  .bg {
    background-image: url('[IMAGE_URL]');
    background-size: cover;
    background-position: center;
    filter: brightness(0.85);
  }

  .grid-container {
    display: grid;
    gap: 2px;
    background: white; /* Gap color */
  }
  .grid-2nd { grid-template-columns: 1fr 1fr; }
  .grid-3rd-hero { grid-template-columns: 1.6fr 1fr; grid-template-rows: 1fr 1fr; }
  .grid-3rd-hero .grid-item:first-child { grid-row: span 2; }
  .grid-4th { grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; }

  .grid-item {
    background-size: cover;
    background-position: center;
    filter: brightness(0.9);
  }

  /* === DECORATIVE BORDER (editorial style) === */
  .border-frame {
    position: absolute; inset: 12px;
    border: 1px solid rgba(255,255,255,0.25);
    pointer-events: none;
  }

  /* === TITLE PANEL === */
  .title-panel {
    position: absolute;
    top: 40px; left: 40px; right: 160px;
    background: rgba(20, 60, 60, 0.78);
    padding: 28px 36px;
    backdrop-filter: blur(8px);
    z-index: 10;
  }

  /* Centered variant for Split Grids */
  .title-panel.centered {
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    right: auto;
    width: 80%;
    max-width: 650px;
    text-align: center;
    box-shadow: 0 20px 50px rgba(0,0,0,0.3);
  }

  /* === TYPOGRAPHY === */
  .title {
    font-family: 'Cinzel', 'Trajan Pro', Georgia, serif;
    font-size: 32px;
    font-weight: 700;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    line-height: 1.25;
    margin-bottom: 8px;
  }

  .subtitle {
    font-family: 'Cinzel', Georgia, serif;
    font-size: 14px;
    font-weight: 400;
    color: rgba(255,255,255,0.8);
    text-transform: uppercase;
    letter-spacing: 0.15em;
  }

  /* === LOGO AREA === */
  .logo-area {
    position: absolute;
    top: 40px; right: 40px;
    width: 80px;
    text-align: center;
    color: white;
  }

  /* === DECORATIVE PATTERN (corner motifs) === */
  .corner-tl, .corner-tr, .corner-bl, .corner-br {
    position: absolute;
    width: 40px; height: 40px;
    opacity: 0.5;
  }
  .corner-tl { top: 12px; left: 12px; }
  .corner-tr { top: 12px; right: 12px; transform: scaleX(-1); }
  .corner-bl { bottom: 12px; left: 12px; transform: scaleY(-1); }
  .corner-br { bottom: 12px; right: 12px; transform: scale(-1); }
</style>
### Universal HTML Template

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  /* === RESET & BASE === */
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { width: 960px; height: 480px; overflow: hidden; font-family: sans-serif; background: #111; }

  /* === CONTAINER === */
  .header { position: relative; width: 960px; height: 480px; overflow: hidden; }

  /* === BACKGROUND / GRID === */
  .bg, .grid-container { position: absolute; inset: 0; }
  .bg {
    background-image: url('[IMAGE_URL]');
    background-size: cover; background-position: center;
    filter: brightness(0.8);
  }

  .grid-container { display: grid; gap: 2px; background: white; }
  .grid-2nd { grid-template-columns: 1fr 1fr; }
  .grid-3rd-hero { grid-template-columns: 1.6fr 1fr; grid-template-rows: 1fr 1fr; }
  .grid-3rd-hero .grid-item:first-child { grid-row: span 2; }
  .grid-4th { grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; }

  .grid-item { background-size: cover; background-position: center; filter: brightness(0.85); }

  /* === OVERLAYS & BORDERS === */
  .border-frame {
    position: absolute; inset: 12px;
    border: 1px solid rgba(255,255,255,0.2);
    pointer-events: none; z-index: 5;
  }

  .title-panel {
    position: absolute;
    top: 40px; left: 40px; right: 160px;
    background: rgba(15, 45, 45, 0.85);
    padding: 32px 40px;
    backdrop-filter: blur(12px);
    z-index: 20;
    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
  }

  .title-panel.centered {
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    right: auto; width: 85%; max-width: 650px; text-align: center;
  }

  /* === TYPOGRAPHY === */
  .title {
    font-family: '[DISPLAY_FONT]', serif;
    font-size: 34px; font-weight: 700; color: #fff;
    text-transform: uppercase; letter-spacing: 0.05em;
    line-height: 1.2; margin-bottom: 10px;
  }
  .subtitle {
    font-family: '[DISPLAY_FONT]', serif;
    font-size: 14px; font-weight: 400; color: rgba(255,255,255,0.7);
    text-transform: uppercase; letter-spacing: 0.2em;
  }

  .logo-area {
    position: absolute; top: 40px; right: 40px;
    z-index: 25; color: white; text-align: right;
  }
</style>
<link href="https://fonts.googleapis.com/css2?family=[FONT_NAME]:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
<div class="header">
  <!-- Use EITHER .bg OR .grid-container -->
  [BACKGROUND_HTML]

  <div class="border-frame"></div>

  <div class="title-panel [CENTERED_CLASS]">
    <div class="title">[TITLE]</div>
    <div class="subtitle">[SUBTITLE]</div>
  </div>

  <div class="logo-area">
    <div style="font-size:11px; letter-spacing:0.15em;">[BRAND]</div>
  </div>
</div>
</body>
</html>
```

---

## Step 4: Split Grid Variations (Logic)

When `style: split-grid` is chosen:
1. **Identify Count**: Count provided images (2, 3, or 4).
2. **Assign Class**:
   - 2 images -> `.grid-2nd`
   - 3 images -> `.grid-3rd-hero`
   - 4 images -> `.grid-4th`
3. **Populate Items**: Create `<div class="grid-item" style="background-image: url('...')"></div>` for each.
4. **Force Center**: Always use `.title-panel.centered` for balance unless the user specifies otherwise.

---

## Step 5: Decorative Border Patterns
... [Existing SVG pattern logic follows] ...

For the Svalbardi-style **geometric tiling border**, use this SVG pattern approach:

```html
<svg style="position:absolute;inset:0;width:100%;height:100%;pointer-events:none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <pattern id="geo" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
      <!-- Diamond/geometric tile -->
      <polygon points="15,0 30,15 15,30 0,15" fill="none" stroke="rgba(100,180,160,0.35)" stroke-width="0.8"/>
      <circle cx="15" cy="15" r="2" fill="rgba(100,180,160,0.25)"/>
    </pattern>
  </defs>
  <!-- Top strip -->
  <rect x="0" y="0" width="960" height="18" fill="url(#geo)"/>
  <!-- Bottom strip -->
  <rect x="0" y="462" width="960" height="18" fill="url(#geo)"/>
  <!-- Left strip -->
  <rect x="0" y="0" width="18" height="480" fill="url(#geo)"/>
  <!-- Right strip -->
  <rect x="942" y="0" width="18" height="480" fill="url(#geo)"/>
</svg>
```

---

## Step 5: Font Pairings by Style

| Style | Display Font | Body/Subtitle Font | Source |
|---|---|---|---|
| editorial | Cinzel | Cinzel (lighter weight) | Google Fonts |
| magazine | Playfair Display | Lato | Google Fonts |
| minimal | DM Serif Display | DM Sans | Google Fonts |
| bold | Bebas Neue | Barlow Condensed | Google Fonts |
| nature/wellness | Cormorant Garamond | Jost | Google Fonts |

Always load from Google Fonts CDN in the `<head>`.

---

## Step 6: Background Without a Photo

If no image URL is provided, generate a CSS gradient background suited to the topic:

| Topic | CSS Gradient |
|---|---|
| Water/ocean | `linear-gradient(135deg, #0f4c75 0%, #1b6ca8 40%, #2196a0 100%)` |
| Food/nutrition | `linear-gradient(135deg, #2d5a27 0%, #4a7c59 50%, #8fb996 100%)` |
| Fitness | `linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%)` |
| Wellness/spa | `linear-gradient(135deg, #667eea 0%, #764ba2 100%)` |
| Business | `linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)` |
| Travel | `linear-gradient(135deg, #f7971e 0%, #ffd200 100%)` |

Add a subtle `noise` texture overlay for depth:
```css
.bg::after {
  content: '';
  position: absolute; inset: 0;
  background-image: url("data:image/svg+xml,..."); /* noise SVG */
  opacity: 0.04;
}
```

---

## Step 7: Output & Export

1. Save the completed HTML to `/mnt/user-data/outputs/blog-header.html`
2. Tell the user: **"To export as WebP (recommended): open in browser → right-click → inspect → screenshot, OR use the `convert_headers.mjs` script with Playwright to batch-export as WebP (quality 85)."**
3. Optionally offer a **React artifact** version if the user wants an interactive editor to tweak title/colors.

---

## Quality Checklist

Before delivering, verify:
- [ ] Title is legible against the background (contrast ratio)
- [ ] Decorative border doesn't obscure content
- [ ] Font loads correctly (Google Fonts link present)
- [ ] Dimensions are exactly 960×480 (or requested size)
- [ ] No overflow / clipping issues
- [ ] Brand/logo placement feels intentional
- [ ] Overall aesthetic matches the requested style
- [ ] File is self-contained (no broken external dependencies except CDN fonts/images)

---

## Common Variations

**Square format (Instagram):** Change body/header dimensions to `600×600px`, center the title.

**Wide banner (Twitter/X):** `1500×500px`, title left-aligned with more breathing room.

**Tall format (Pinterest):** `800×1200px`, title in lower third with larger image showcase.

**Dark mode variant:** Swap panel to `rgba(255,255,255,0.12)`, use dark background + light text.
