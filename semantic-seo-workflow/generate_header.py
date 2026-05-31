"""
generate_header.py  —  Svalbardi-style branded header image generator
Produces 1200×420 WebP headers with:
  • Client photo filling the right portion (from input_dir)
  • Decorative tiled border in brand colours around all edges
  • Dark branded text panel on the left with bold white uppercase title
  • Logo mark pinned to the bottom of the text panel
  • Soft gradient blend where panel meets photo

Usage: python generate_header.py
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ─── CLIENT CONFIG ────────────────────────────────────────────────────────────
CLIENT = {
    "brand":       (13,  43, 107),   # Navy   #0D2B6B  — border fill
    "accent":      (249, 115,  22),  # Orange #F97316  — diamond tiles + accents
    "panel":       (6,   18,  46),   # Deep navy        — text panel fill
    "logo_line1":  "BTEC",
    "logo_line2":  "Assignment Help",
    "input_dir":   r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\btec-assignment-help\images",
    "output_dir":  r"C:\Users\jobmu\my-second-projects\btec-assignment-help\public\images",
}

# ─── PAGES ───────────────────────────────────────────────────────────────────
PAGES = [
    # ── Phase 1 ──────────────────────────────────────────────────────────────
    {
        "slug":  "header_btec-assignment-help",
        "title": "BTEC\nASSIGNMENT\nHELP",
        "photo": "Screenshot_51.png",
    },
    {
        "slug":  "header_btec-national-assignment-help",
        "title": "BTEC NATIONAL\nASSIGNMENT\nHELP",
        "photo": "Screenshot_44.png",
    },
    {
        "slug":  "header_btec-hnc-assignment-help",
        "title": "BTEC HNC\nASSIGNMENT\nHELP",
        "photo": "Screenshot_46.png",
    },
    {
        "slug":  "header_btec-hnd-assignment-help",
        "title": "BTEC HND\nASSIGNMENT\nHELP",
        "photo": "Screenshot_50.png",
    },
    {
        "slug":  "header_btec-business-assignment-help",
        "title": "BTEC BUSINESS\nASSIGNMENT\nHELP",
        "photo": "Screenshot_40.png",
    },
    # ── Phase 2 ──────────────────────────────────────────────────────────────
    {
        "slug":  "header_btec-health-and-social-care-assignment-help",
        "title": "BTEC HEALTH AND\nSOCIAL CARE\nASSIGNMENT HELP",
        "photo": "Screenshot_37.png",
    },
    {
        "slug":  "header_btec-engineering-assignment-help",
        "title": "BTEC ENGINEERING\nASSIGNMENT HELP",
        "photo": "Screenshot_38.png",
    },
    {
        "slug":  "header_btec-it-assignment-help",
        "title": "BTEC IT\nASSIGNMENT HELP",
        "photo": "Screenshot_46.png",
    },
    {
        "slug":  "header_btec-sport-assignment-help",
        "title": "BTEC SPORT\nASSIGNMENT HELP",
        "photo": "Screenshot_42.png",
    },
    {
        "slug":  "header_btec-public-services-assignment-help",
        "title": "BTEC PUBLIC\nSERVICES\nASSIGNMENT HELP",
        "photo": "Screenshot_45.png",
    },
    {
        "slug":  "header_btec-assignment-grading-criteria-explained",
        "title": "BTEC ASSIGNMENT\nGRADING CRITERIA\nEXPLAINED",
        "photo": "Screenshot_51.png",
    },
    {
        "slug":  "header_how-to-achieve-distinction-in-btec-assignments",
        "title": "HOW TO ACHIEVE\nDISTINCTION IN\nBTEC ASSIGNMENTS",
        "photo": "Screenshot_40.png",
    },
    {
        "slug":  "header_btec-assignment-resubmission-guide",
        "title": "BTEC ASSIGNMENT\nRESUBMISSION\nGUIDE",
        "photo": "Screenshot_50.png",
    },
    {
        "slug":  "header_btec-assignment-brief-how-to-read-and-interpret-it",
        "title": "BTEC ASSIGNMENT\nBRIEF: HOW TO\nINTERPRET IT",
        "photo": "Screenshot_46.png",
    },
    {
        "slug":  "header_btec-childcare-and-early-years-assignment-help",
        "title": "BTEC CHILDCARE\nAND EARLY YEARS\nASSIGNMENT HELP",
        "photo": "Screenshot_37.png",
    },
]

# ─── LAYOUT CONSTANTS ─────────────────────────────────────────────────────────
W, H        = 1200, 420   # canvas size
BORDER      = 24          # border band thickness (px)
PANEL_W     = 450         # dark text panel width (inside border)
TILE        = 24          # border tile pitch


# ─── HELPERS ─────────────────────────────────────────────────────────────────

def get_font(size, bold=True):
    candidates = (
        [r"C:\Windows\Fonts\arialbd.ttf",   r"C:\Windows\Fonts\calibrib.ttf",
         r"C:\Windows\Fonts\verdanab.ttf",  r"C:\Windows\Fonts\trebucbd.ttf"]
        if bold else
        [r"C:\Windows\Fonts\arial.ttf",     r"C:\Windows\Fonts\calibri.ttf",
         r"C:\Windows\Fonts\verdana.ttf"]
    )
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


def fit_crop(img, w, h):
    """Center-crop image to exactly w × h."""
    iw, ih = img.size
    scale  = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img    = img.resize((nw, nh), Image.LANCZOS)
    x, y   = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def draw_diamond_tile(draw, cx, cy, radius, fill, dot):
    """Draw one diamond tile: filled diamond + white centre dot."""
    r = radius
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    draw.polygon(pts, fill=fill)
    d = max(2, radius // 4)
    draw.ellipse([(cx - d, cy - d), (cx + d, cy + d)], fill=dot)


def draw_border(draw, brand, accent):
    """Fill border bands and tile diamond motifs across them."""
    # Solid band fill
    draw.rectangle([(0, 0),        (W, BORDER)],       fill=brand)   # top
    draw.rectangle([(0, H-BORDER), (W, H)],             fill=brand)   # bottom
    draw.rectangle([(0, 0),        (BORDER, H)],        fill=brand)   # left
    draw.rectangle([(W-BORDER, 0), (W, H)],             fill=brand)   # right

    r   = TILE // 2 - 2          # diamond radius
    dot = (255, 255, 255)

    # Horizontal bands (top + bottom)
    half = TILE // 2
    for x in range(half, W, TILE):
        draw_diamond_tile(draw, x, BORDER // 2,     r, accent, dot)   # top
        draw_diamond_tile(draw, x, H - BORDER // 2, r, accent, dot)   # bottom

    # Vertical bands (left + right), skip corners
    for y in range(BORDER + half, H - BORDER, TILE):
        draw_diamond_tile(draw, BORDER // 2,     y, r, accent, dot)   # left
        draw_diamond_tile(draw, W - BORDER // 2, y, r, accent, dot)   # right


def panel_gradient(draw, px, py, pw, ph):
    """Add a right-edge gradient on the panel so it fades into the photo."""
    fade_w = 60
    for i in range(fade_w):
        alpha = int(255 * (1 - i / fade_w))
        x = px + pw - fade_w + i
        draw.rectangle([(x, py), (x + 1, py + ph)], fill=(6, 18, 46, alpha))


def generate(page, client):
    brand  = client["brand"]
    accent = client["accent"]
    panel  = client["panel"]

    inner_x = BORDER
    inner_y = BORDER
    inner_w = W - 2 * BORDER
    inner_h = H - 2 * BORDER

    # ── Background: photo fills right portion of inner area ──────────────────
    photo_x = inner_x + PANEL_W
    photo_w = inner_w - PANEL_W

    photo_src  = os.path.join(client["input_dir"], page["photo"])
    photo_img  = Image.open(photo_src).convert("RGB")
    photo_crop = fit_crop(photo_img, photo_w, inner_h)

    canvas = Image.new("RGB", (W, H), brand)
    canvas.paste(photo_crop, (photo_x, inner_y))

    draw = ImageDraw.Draw(canvas, "RGBA")

    # ── Dark text panel ───────────────────────────────────────────────────────
    draw.rectangle(
        [(inner_x, inner_y), (inner_x + PANEL_W, inner_y + inner_h)],
        fill=panel,
    )

    # Right-edge fade of panel into photo
    panel_gradient(draw, inner_x, inner_y, PANEL_W, inner_h)

    # Switch to RGB draw for crisp text
    draw = ImageDraw.Draw(canvas)

    # Accent top stripe across panel
    draw.rectangle(
        [(inner_x, inner_y), (inner_x + PANEL_W, inner_y + 6)],
        fill=accent,
    )

    # ── Title text ────────────────────────────────────────────────────────────
    title_font = get_font(38, bold=True)
    lines      = page["title"].split("\n")
    line_h     = 50
    tx         = inner_x + 32
    ty         = inner_y + 28

    for line in lines:
        # Subtle drop shadow
        draw.text((tx + 2, ty + 2), line, fill=(0, 0, 0), font=title_font)
        draw.text((tx,     ty),     line, fill=(255, 255, 255), font=title_font)
        ty += line_h

    # Short accent rule below title
    rule_y = ty + 10
    draw.rectangle([(tx, rule_y), (tx + 56, rule_y + 4)], fill=accent)

    # ── Logo block (bottom of panel) ─────────────────────────────────────────
    logo1_font = get_font(22, bold=True)
    logo2_font = get_font(13, bold=False)
    logo_y     = inner_y + inner_h - 64

    draw.text((tx, logo_y),      client["logo_line1"], fill=accent,          font=logo1_font)
    draw.text((tx, logo_y + 28), client["logo_line2"], fill=(190, 205, 230), font=logo2_font)

    # ── Decorative border (drawn last, over everything) ───────────────────────
    draw_border(draw, brand, accent)

    # ── Save ──────────────────────────────────────────────────────────────────
    os.makedirs(client["output_dir"], exist_ok=True)
    out_path = os.path.join(client["output_dir"], page["slug"] + ".webp")
    canvas.save(out_path, "WEBP", quality=92)
    print(f"  OK  {page['slug']}.webp")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Generating {len(PAGES)} header images...\n")
    for page in PAGES:
        generate(page, CLIENT)
    print(f"\nDone -> {CLIENT['output_dir']}")
