"""
generate_header_iosh.py — IOSH Assignment Help header images
Produces 1200×420 WebP headers for all IOSH Managing Safely pages.
Brand: dark teal #064E3B + amber #FBBF24

HOW TO USE
----------
1. Drop your grid image into: client_data/New-sites/iosh-assignment-help/input images/
2. Set GRID_COLS and GRID_ROWS below to match the grid dimensions of your image.
3. Run:  python generate_header_iosh.py
Pages are mapped to grid cells in reading order (left→right, top→bottom).
Override individual zones by adding "zone": (x0,y0,x1,y1) to any PAGES entry.
"""

from PIL import Image, ImageDraw, ImageFont
import os, glob

CLIENT = {
    "brand":       (6,   78,  59),    # Dark teal    #064E3B — border fill
    "accent":      (251, 191, 36),    # Amber        #FBBF24 — diamond tiles + accents
    "panel":       (3,   49,  37),    # Darker teal              — text panel fill
    "logo_line1":  "IOSH",
    "logo_line2":  "Assignment Help",
    "input_dir":   r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\iosh-assignment-help\input images",
    "output_dir":  r"C:\Users\jobmu\my-second-projects\iosh-assignment-help\public",
}

GRID_COLS = 3
GRID_ROWS = 4   # 12 cells for 11 pages (last cell unused)

PAGES = [
    {"slug": "header_iosh-assignment-help",                                          "title": "IOSH MANAGING\nSAFELY\nASSIGNMENT HELP"},
    {"slug": "header_iosh-managing-safely-project-help",                             "title": "IOSH MANAGING\nSAFELY PROJECT\nHELP"},
    {"slug": "header_iosh-managing-safely-risk-assessment-help",                     "title": "IOSH RISK\nASSESSMENT\nHELP"},
    {"slug": "header_iosh-managing-safely-hazard-identification-help",               "title": "IOSH HAZARD\nIDENTIFICATION\nHELP"},
    {"slug": "header_iosh-managing-safely-project-action-plan-help",                 "title": "IOSH PROJECT\nACTION PLAN\nHELP"},
    {"slug": "header_iosh-hierarchy-of-control-for-the-managing-safely-project",     "title": "IOSH HIERARCHY\nOF CONTROL\nGUIDE"},
    {"slug": "header_iosh-managing-safely-project-marking-criteria-explained",       "title": "IOSH MARKING\nCRITERIA\nEXPLAINED"},
    {"slug": "header_iosh-managing-safely-project-referral-and-resubmission-guide",  "title": "IOSH REFERRAL\n& RESUBMISSION\nGUIDE"},
    {"slug": "header_iosh-managing-safely-test-preparation",                         "title": "IOSH TEST\nPREPARATION\nGUIDE"},
    {"slug": "header_how-to-achieve-a-high-score-in-the-iosh-managing-safely-project","title": "HOW TO ACHIEVE\nHIGH SCORE\nIOSH PROJECT"},
    {"slug": "header_iosh-managing-safely-for-specific-industries",                  "title": "IOSH MANAGING\nSAFELY FOR\nINDUSTRIES"},
]

W, H = 1200, 420
BORDER = 24
PANEL_W = 450
TILE = 24


def page_zone(idx):
    r = idx // GRID_COLS
    c = idx % GRID_COLS
    return (c / GRID_COLS, r / GRID_ROWS, (c + 1) / GRID_COLS, (r + 1) / GRID_ROWS)


def get_font(size, bold=True):
    candidates = (
        [r"C:\Windows\Fonts\arialbd.ttf", r"C:\Windows\Fonts\calibrib.ttf",
         r"C:\Windows\Fonts\verdanab.ttf", r"C:\Windows\Fonts\trebucbd.ttf"]
        if bold else
        [r"C:\Windows\Fonts\arial.ttf", r"C:\Windows\Fonts\calibri.ttf",
         r"C:\Windows\Fonts\verdana.ttf"]
    )
    for p in candidates:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()


def zone_crop(img, zone):
    iw, ih = img.size
    x0, y0 = int(zone[0] * iw), int(zone[1] * ih)
    x1, y1 = int(zone[2] * iw), int(zone[3] * ih)
    return img.crop((max(0, x0), max(0, y0), min(iw, x1), min(ih, y1)))


def fit_crop(img, w, h):
    iw, ih = img.size
    scale = max(w / iw, h / ih)
    nw, nh = int(iw * scale + 0.5), int(ih * scale + 0.5)
    img = img.resize((nw, nh), Image.LANCZOS)
    x, y = (nw - w) // 2, (nh - h) // 2
    return img.crop((x, y, x + w, y + h))


def draw_diamond_tile(draw, cx, cy, radius, fill, dot):
    pts = [(cx, cy - radius), (cx + radius, cy), (cx, cy + radius), (cx - radius, cy)]
    draw.polygon(pts, fill=fill)
    d = max(2, radius // 4)
    draw.ellipse([(cx - d, cy - d), (cx + d, cy + d)], fill=dot)


def draw_border(draw, brand, accent):
    draw.rectangle([(0, 0), (W, BORDER)], fill=brand)
    draw.rectangle([(0, H - BORDER), (W, H)], fill=brand)
    draw.rectangle([(0, 0), (BORDER, H)], fill=brand)
    draw.rectangle([(W - BORDER, 0), (W, H)], fill=brand)
    r, dot, half = TILE // 2 - 2, (255, 255, 255), TILE // 2
    for x in range(half, W, TILE):
        draw_diamond_tile(draw, x, BORDER // 2, r, accent, dot)
        draw_diamond_tile(draw, x, H - BORDER // 2, r, accent, dot)
    for y in range(BORDER + half, H - BORDER, TILE):
        draw_diamond_tile(draw, BORDER // 2, y, r, accent, dot)
        draw_diamond_tile(draw, W - BORDER // 2, y, r, accent, dot)


def panel_gradient(draw, px, py, pw, ph, panel):
    fade_w = 60
    for i in range(fade_w):
        alpha = int(255 * (1 - i / fade_w))
        x = px + pw - fade_w + i
        draw.rectangle([(x, py), (x + 1, py + ph)], fill=(*panel, alpha))


def generate(page, client, source, zone):
    brand, accent, panel = client["brand"], client["accent"], client["panel"]
    inner_x, inner_y = BORDER, BORDER
    inner_w, inner_h = W - 2 * BORDER, H - 2 * BORDER
    photo_x, photo_w = inner_x + PANEL_W, inner_w - PANEL_W

    photo_crop = fit_crop(zone_crop(source, zone).convert("RGB"), photo_w, inner_h)
    canvas = Image.new("RGB", (W, H), brand)
    canvas.paste(photo_crop, (photo_x, inner_y))

    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rectangle([(inner_x, inner_y), (inner_x + PANEL_W, inner_y + inner_h)], fill=panel)
    panel_gradient(draw, inner_x, inner_y, PANEL_W, inner_h, panel)

    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(inner_x, inner_y), (inner_x + PANEL_W, inner_y + 6)], fill=accent)

    title_font = get_font(38)
    tx, ty = inner_x + 32, inner_y + 28
    for line in page["title"].split("\n"):
        draw.text((tx + 2, ty + 2), line, fill=(0, 0, 0), font=title_font)
        draw.text((tx, ty), line, fill=(255, 255, 255), font=title_font)
        ty += 50
    draw.rectangle([(tx, ty + 10), (tx + 56, ty + 14)], fill=accent)

    logo_y = inner_y + inner_h - 64
    draw.text((tx, logo_y),      client["logo_line1"], fill=accent,          font=get_font(22))
    draw.text((tx, logo_y + 28), client["logo_line2"], fill=(190, 200, 220), font=get_font(13, bold=False))
    draw_border(draw, brand, accent)

    os.makedirs(client["output_dir"], exist_ok=True)
    canvas.save(os.path.join(client["output_dir"], page["slug"] + ".webp"), "WEBP", quality=92)
    print(f"  OK  {page['slug']}.webp")


if __name__ == "__main__":
    exts = ("*.png", "*.jpg", "*.jpeg", "*.webp", "*.PNG", "*.JPG")
    imgs = []
    for ext in exts:
        imgs += glob.glob(os.path.join(CLIENT["input_dir"], ext))
    if not imgs:
        print(f"No image found in:\n  {CLIENT['input_dir']}")
        print("Add a grid image and re-run.")
        exit(1)
    imgs.sort()
    source = Image.open(imgs[0])
    print(f"Source: {os.path.basename(imgs[0])}  ({source.size[0]}x{source.size[1]}, {source.mode})")
    print(f"Grid:   {GRID_COLS} cols x {GRID_ROWS} rows  ({GRID_COLS*GRID_ROWS} cells for {len(PAGES)} pages)\n")
    for i, page in enumerate(PAGES):
        zone = page.get("zone") or page_zone(i)
        generate(page, CLIENT, source, zone)
    print(f"\nDone -> {CLIENT['output_dir']}")
