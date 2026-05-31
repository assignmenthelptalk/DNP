"""
generate_header_nebosh_phase2a.py — NEBOSH Phase 2A header images
Produces 1200×420 WebP headers for the 6 Phase 2A pages.
Brand: deep red #7C1D1D + orange #FB923C (NEBOSH assignment help)
"""

from PIL import Image, ImageDraw, ImageFont
import os

CLIENT = {
    "brand":       (124, 29,  29),   # Deep red  #7C1D1D
    "accent":      (251, 146, 60),   # Orange    #FB923C
    "panel":       (60,  10,  10),   # Darker red for text panel
    "logo_line1":  "NEBOSH",
    "logo_line2":  "Assignment Help",
    "input_dir":   r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\nebosh-assignment-help\input-images",
    "output_dir":  r"C:\Users\jobmu\my-second-projects\nebosh-assignment-help\public",
}

PAGES = [
    {
        "slug":  "header_nebosh-assignment-marking-criteria-explained",
        "title": "NEBOSH ASSIGNMENT\nMARKING CRITERIA\nEXPLAINED",
        "photo": "Screenshot_28.png",
    },
    {
        "slug":  "header_nebosh-how-to-pass-assignment-first-time",
        "title": "HOW TO PASS YOUR\nNEBOSH ASSIGNMENT\nFIRST TIME",
        "photo": "Screenshot_24.png",
    },
    {
        "slug":  "header_nebosh-ig1-assignment-model-answers",
        "title": "NEBOSH IG1\nMODEL ANSWERS\nDISTINCTION GRADE",
        "photo": "Screenshot_25.png",
    },
    {
        "slug":  "header_nebosh-ig2-practical-assessment-help",
        "title": "NEBOSH IG2\nPRACTICAL\nASSESSMENT HELP",
        "photo": "Screenshot_26.png",
    },
    {
        "slug":  "header_nebosh-assignment-word-count-requirements",
        "title": "NEBOSH ASSIGNMENT\nWORD COUNT\nREQUIREMENTS",
        "photo": "Screenshot_27.png",
    },
    {
        "slug":  "header_nebosh-assignment-referral-recovery",
        "title": "NEBOSH ASSIGNMENT\nREFERRAL RECOVERY\nGET BACK ON TRACK",
        "photo": "Screenshot_30.png",
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
        draw.rectangle([(x, py), (x + 1, py + ph)], fill=(60, 10, 10, alpha))


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
    draw.text((tx, logo_y + 28), client["logo_line2"], fill=(220, 180, 180), font=logo2_font)

    draw_border(draw, brand, accent)

    os.makedirs(client["output_dir"], exist_ok=True)
    out_path = os.path.join(client["output_dir"], page["slug"] + ".webp")
    canvas.save(out_path, "WEBP", quality=92)
    print(f"  OK  {page['slug']}.webp")


if __name__ == "__main__":
    print(f"Generating {len(PAGES)} NEBOSH Phase 2A header images...\n")
    for page in PAGES:
        generate(page, CLIENT)
    print(f"\nDone -> {CLIENT['output_dir']}")
