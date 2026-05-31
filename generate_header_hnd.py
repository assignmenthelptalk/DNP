"""
generate_header_hnd.py — HND Assignment Help header images
Produces 1200×420 WebP headers for all 9 HND pages (Phase 1 + Phase 2).
Brand: charcoal #1F2937 + rose red #F43F5E (HND assignment help)
"""

from PIL import Image, ImageDraw, ImageFont
import os

CLIENT = {
    "brand":       (31,  41,  55),   # Charcoal  #1F2937  — border fill
    "accent":      (244, 63,  94),   # Rose red  #F43F5E  — diamond tiles + accents
    "panel":       (17,  24,  39),   # Very dark charcoal  — text panel fill
    "logo_line1":  "HND",
    "logo_line2":  "Assignment Help",
    "input_dir":   r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\hnd-assignment-help\input images",
    "output_dir":  r"C:\Users\jobmu\my-second-projects\hnd-assignment-help\public\images",
}

PAGES = [
    # ── Phase 1 ──────────────────────────────────────────────────────────────
    {
        "slug":  "header_hnd-assignment-help",
        "title": "HND\nASSIGNMENT\nHELP",
        "photo": "Screenshot_1.png",
    },
    {
        "slug":  "header_hnd-business-assignment-help",
        "title": "HND BUSINESS\nASSIGNMENT\nHELP",
        "photo": "Screenshot_2.png",
    },
    {
        "slug":  "header_hnd-computing-assignment-help",
        "title": "HND COMPUTING\nASSIGNMENT\nHELP",
        "photo": "Screenshot_3.png",
    },
    {
        "slug":  "header_hnd-engineering-assignment-help",
        "title": "HND ENGINEERING\nASSIGNMENT\nHELP",
        "photo": "Screenshot_4.png",
    },
    {
        "slug":  "header_hnd-health-social-care-assignment-help",
        "title": "HND HEALTH AND\nSOCIAL CARE\nASSIGNMENT HELP",
        "photo": "Screenshot_5.png",
    },
    # ── Phase 2 ──────────────────────────────────────────────────────────────
    {
        "slug":  "header_hnd-assignment-grading-criteria",
        "title": "HND ASSIGNMENT\nGRADING CRITERIA\nEXPLAINED",
        "photo": "Screenshot_55.png",
    },
    {
        "slug":  "header_hnd-how-to-achieve-distinction",
        "title": "HOW TO ACHIEVE\nDISTINCTION IN\nHND ASSIGNMENTS",
        "photo": "Screenshot_6.png",
    },
    {
        "slug":  "header_hnd-assignment-resubmission",
        "title": "HND ASSIGNMENT\nRESUBMISSION\nGUIDE",
        "photo": "Screenshot_7.png",
    },
    {
        "slug":  "header_hnd-managing-successful-business-project",
        "title": "HND BUSINESS\nRESEARCH PROJECT\nUNIT 6 / 12",
        "photo": "Screenshot_8.png",
    },
]

W, H        = 1200, 420
BORDER      = 24
PANEL_W     = 450
TILE        = 24


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
    iw, ih = img.size
    scale  = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img    = img.resize((nw, nh), Image.LANCZOS)
    x, y   = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def draw_diamond_tile(draw, cx, cy, radius, fill, dot):
    r = radius
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
        draw.rectangle([(x, py), (x + 1, py + ph)], fill=(17, 24, 39, alpha))


def generate(page, client):
    brand  = client["brand"]
    accent = client["accent"]
    panel  = client["panel"]

    inner_x = BORDER
    inner_y = BORDER
    inner_w = W - 2 * BORDER
    inner_h = H - 2 * BORDER

    photo_x = inner_x + PANEL_W
    photo_w = inner_w - PANEL_W

    photo_src  = os.path.join(client["input_dir"], page["photo"])
    photo_img  = Image.open(photo_src).convert("RGB")
    photo_crop = fit_crop(photo_img, photo_w, inner_h)

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
    draw.text((tx, logo_y + 28), client["logo_line2"], fill=(180, 190, 210), font=logo2_font)

    draw_border(draw, brand, accent)

    os.makedirs(client["output_dir"], exist_ok=True)
    out_path = os.path.join(client["output_dir"], page["slug"] + ".webp")
    canvas.save(out_path, "WEBP", quality=92)
    print(f"  OK  {page['slug']}.webp")


if __name__ == "__main__":
    print(f"Generating {len(PAGES)} HND header images...\n")
    for page in PAGES:
        generate(page, CLIENT)
    print(f"\nDone -> {CLIENT['output_dir']}")
