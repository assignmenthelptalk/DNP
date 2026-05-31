"""
generate_header_pgce.py — PGCE Assignment Help header images
Produces 1200×420 WebP headers for all 15 PGCE pages.
Brand: deep indigo #312E81 + amber #FBBF24
Source image: single 1408×768 Gemini-generated 3×3 classroom scene grid.
Different crop zones are used per page to create visual variety.
"""

from PIL import Image, ImageDraw, ImageFont
import os

CLIENT = {
    "brand":       (49,  46,  129),   # Deep indigo  #312E81 — border fill
    "accent":      (251, 191, 36),    # Amber/gold   #FBBF24 — diamond tiles + accents
    "panel":       (30,  27,  105),   # Darker indigo #1E1B69 — text panel fill
    "logo_line1":  "PGCE",
    "logo_line2":  "Assignment Help",
    "input_img":   r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\pgce-assignment-help\input images\Gemini_Generated_Image_eneaxzeneaxzenea.png",
    "output_dir":  r"C:\Users\jobmu\my-second-projects\pgce-assignment-help\public",
}

# Source image is a 3×3 grid of 9 classroom scenes (1408×768).
# zone = (x0_frac, y0_frac, x1_frac, y1_frac) — fractional crop of source before fit_crop.
# Grid reference (approximate):
#   Col1 x: 0.00–0.33  Col2 x: 0.33–0.67  Col3 x: 0.67–1.00
#   Row1 y: 0.00–0.33  Row2 y: 0.33–0.67  Row3 y: 0.67–1.00
#
# Scene map:
#   R1C1 – Primary classroom (teacher + young children at tables)
#   R1C2 – Lecture hall (student with laptop)
#   R1C3 – PE / sports hall (basketball)
#   R2C1 – Teacher 1:1 with young child (SEN / inclusion)
#   R2C2 – Art / design / craft class
#   R2C3 – Teacher at desk with older student (FE / assessment)
#   R3C1 – Teacher presenting to class (board / screen)
#   R3C2 – Professional group discussion around table
#   R3C3 – Children outdoors / garden learning

PAGES = [
    # ── Phase 1 ──────────────────────────────────────────────────────────
    {
        "slug":  "header_pgce-assignment-help",
        "title": "PGCE\nASSIGNMENT\nHELP",
        "zone":  (0.0, 0.0, 1.0, 1.0),   # Full image — all 9 scenes for the hub
    },
    {
        "slug":  "header_pgce-primary-assignment-help",
        "title": "PGCE PRIMARY\nASSIGNMENT\nHELP",
        "zone":  (0.0, 0.0, 0.38, 0.40),  # R1C1 — primary classroom with young children
    },
    {
        "slug":  "header_pgce-secondary-assignment-help",
        "title": "PGCE SECONDARY\nASSIGNMENT\nHELP",
        "zone":  (0.0, 0.63, 0.38, 1.0),  # R3C1 — teacher presenting to secondary class
    },
    {
        "slug":  "header_pgce-further-education-assignment-help",
        "title": "PGCE FURTHER\nEDUCATION\nASSIGNMENT HELP",
        "zone":  (0.64, 0.28, 1.0, 0.68), # R2C3 — teacher + adult learner at desk
    },
    {
        "slug":  "header_pgce-reflective-writing-help",
        "title": "PGCE REFLECTIVE\nWRITING\nHELP",
        "zone":  (0.30, 0.63, 0.70, 1.0), # R3C2 — professional group discussion
    },
    # ── Phase 2 ──────────────────────────────────────────────────────────
    {
        "slug":  "header_teachers-standards-in-pgce-assignments-explained",
        "title": "TEACHERS'\nSTANDARDS\nIN PGCE",
        "zone":  (0.25, 0.65, 0.67, 1.0), # R3C2 offset left — professionals around table
    },
    {
        "slug":  "header_pgce-assignment-referral-and-resubmission-guide",
        "title": "PGCE REFERRAL\n& RESUBMISSION\nGUIDE",
        "zone":  (0.63, 0.25, 1.0, 0.67), # R2C3 offset — one-on-one support/feedback
    },
    {
        "slug":  "header_pgce-subject-knowledge-audit-help",
        "title": "PGCE SUBJECT\nKNOWLEDGE\nAUDIT HELP",
        "zone":  (0.30, 0.0, 0.68, 0.38),  # R1C2 — student studying in lecture hall
    },
    {
        "slug":  "header_pgce-lesson-study-assignment-help",
        "title": "PGCE LESSON\nSTUDY\nASSIGNMENT HELP",
        "zone":  (0.0, 0.0, 0.42, 0.44),   # R1C1 wider — classroom teaching observation
    },
    # ── Phase 3 ──────────────────────────────────────────────────────────
    {
        "slug":  "header_pgce-behaviour-management-assignment-help",
        "title": "PGCE BEHAVIOUR\nMANAGEMENT\nASSIGNMENT HELP",
        "zone":  (0.0, 0.60, 0.42, 1.0),   # R3C1 wider — teacher managing class presentation
    },
    {
        "slug":  "header_pgce-assessment-for-learning-assignment-help",
        "title": "ASSESSMENT\nFOR LEARNING\nPGCE GUIDE",
        "zone":  (0.62, 0.26, 1.0, 0.70),  # R2C3 — desk-based assessment / feedback
    },
    {
        "slug":  "header_pgce-sen-and-inclusion-assignment-help",
        "title": "PGCE SEN AND\nINCLUSION\nASSIGNMENT HELP",
        "zone":  (0.0, 0.28, 0.37, 0.68),  # R2C1 — teacher 1:1 with child
    },
    {
        "slug":  "header_pgce-curriculum-design-assignment-help",
        "title": "PGCE CURRICULUM\nDESIGN\nASSIGNMENT HELP",
        "zone":  (0.30, 0.28, 0.68, 0.68), # R2C2 — art/design/craft class
    },
    # ── Phase 4 ──────────────────────────────────────────────────────────
    {
        "slug":  "header_pgce-secondary-english-assignment-help",
        "title": "PGCE SECONDARY\nENGLISH\nASSIGNMENT HELP",
        "zone":  (0.31, 0.01, 0.69, 0.37), # R1C2 — lecture hall / academic study
    },
    {
        "slug":  "header_pgce-secondary-maths-assignment-help",
        "title": "PGCE SECONDARY\nMATHS\nASSIGNMENT HELP",
        "zone":  (0.63, 0.63, 1.0, 1.0),   # R3C3 — outdoor/practical learning
    },
]

W, H        = 1200, 420
BORDER      = 24
PANEL_W     = 450
TILE        = 24


def get_font(size, bold=True):
    candidates = (
        [r"C:\Windows\Fonts\arialbd.ttf",  r"C:\Windows\Fonts\calibrib.ttf",
         r"C:\Windows\Fonts\verdanab.ttf", r"C:\Windows\Fonts\trebucbd.ttf"]
        if bold else
        [r"C:\Windows\Fonts\arial.ttf",    r"C:\Windows\Fonts\calibri.ttf",
         r"C:\Windows\Fonts\verdana.ttf"]
    )
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


def zone_crop(img, zone):
    """Pre-crop image to a fractional zone before fit_crop."""
    iw, ih = img.size
    x0 = int(zone[0] * iw)
    y0 = int(zone[1] * ih)
    x1 = int(zone[2] * iw)
    y1 = int(zone[3] * ih)
    x0, x1 = max(0, x0), min(iw, x1)
    y0, y1 = max(0, y0), min(ih, y1)
    return img.crop((x0, y0, x1, y1))


def fit_crop(img, w, h):
    iw, ih = img.size
    scale  = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img    = img.resize((nw, nh), Image.LANCZOS)
    x, y   = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def draw_diamond_tile(draw, cx, cy, radius, fill, dot):
    r   = radius
    pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
    draw.polygon(pts, fill=fill)
    d = max(2, radius // 4)
    draw.ellipse([(cx - d, cy - d), (cx + d, cy + d)], fill=dot)


def draw_border(draw, brand, accent):
    draw.rectangle([(0, 0),        (W, BORDER)],       fill=brand)
    draw.rectangle([(0, H-BORDER), (W, H)],             fill=brand)
    draw.rectangle([(0, 0),        (BORDER, H)],        fill=brand)
    draw.rectangle([(W-BORDER, 0), (W, H)],             fill=brand)

    r   = TILE // 2 - 2
    dot = (255, 255, 255)
    half = TILE // 2
    for x in range(half, W, TILE):
        draw_diamond_tile(draw, x, BORDER // 2,     r, accent, dot)
        draw_diamond_tile(draw, x, H - BORDER // 2, r, accent, dot)
    for y in range(BORDER + half, H - BORDER, TILE):
        draw_diamond_tile(draw, BORDER // 2,     y, r, accent, dot)
        draw_diamond_tile(draw, W - BORDER // 2, y, r, accent, dot)


def panel_gradient(draw, px, py, pw, ph):
    fade_w = 60
    for i in range(fade_w):
        alpha = int(255 * (1 - i / fade_w))
        x = px + pw - fade_w + i
        draw.rectangle([(x, py), (x + 1, py + ph)], fill=(30, 27, 105, alpha))


def generate(page, client, source_img):
    brand  = client["brand"]
    accent = client["accent"]
    panel  = client["panel"]

    inner_x = BORDER
    inner_y = BORDER
    inner_w = W - 2 * BORDER
    inner_h = H - 2 * BORDER

    photo_x = inner_x + PANEL_W
    photo_w = inner_w - PANEL_W

    # Zone-crop then fit-crop the source image
    zone_img   = zone_crop(source_img, page["zone"])
    photo_crop = fit_crop(zone_img.convert("RGB"), photo_w, inner_h)

    canvas = Image.new("RGB", (W, H), brand)
    canvas.paste(photo_crop, (photo_x, inner_y))

    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rectangle(
        [(inner_x, inner_y), (inner_x + PANEL_W, inner_y + inner_h)],
        fill=panel,
    )
    panel_gradient(draw, inner_x, inner_y, PANEL_W, inner_h)

    draw = ImageDraw.Draw(canvas)
    draw.rectangle(
        [(inner_x, inner_y), (inner_x + PANEL_W, inner_y + 6)],
        fill=accent,
    )

    title_font = get_font(38, bold=True)
    lines      = page["title"].split("\n")
    line_h     = 50
    tx         = inner_x + 32
    ty         = inner_y + 28

    for line in lines:
        draw.text((tx + 2, ty + 2), line, fill=(0, 0, 0), font=title_font)
        draw.text((tx,     ty),     line, fill=(255, 255, 255), font=title_font)
        ty += line_h

    rule_y = ty + 10
    draw.rectangle([(tx, rule_y), (tx + 56, rule_y + 4)], fill=accent)

    logo1_font = get_font(22, bold=True)
    logo2_font = get_font(13, bold=False)
    logo_y     = inner_y + inner_h - 64

    draw.text((tx, logo_y),      client["logo_line1"], fill=accent,          font=logo1_font)
    draw.text((tx, logo_y + 28), client["logo_line2"], fill=(200, 200, 230), font=logo2_font)

    draw_border(draw, brand, accent)

    os.makedirs(client["output_dir"], exist_ok=True)
    out_path = os.path.join(client["output_dir"], page["slug"] + ".webp")
    canvas.save(out_path, "WEBP", quality=92)
    print(f"  OK  {page['slug']}.webp")


if __name__ == "__main__":
    print(f"Loading source image...")
    source = Image.open(CLIENT["input_img"])
    print(f"Source: {source.size[0]}×{source.size[1]}, mode={source.mode}")
    print(f"\nGenerating {len(PAGES)} PGCE header images...\n")
    for page in PAGES:
        generate(page, CLIENT, source)
    print(f"\nDone -> {CLIENT['output_dir']}")
