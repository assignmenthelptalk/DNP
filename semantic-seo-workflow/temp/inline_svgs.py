"""
inline_svgs.py
Replaces all <img src="../infographics/xxx.svg"> and
<object data="../infographics/xxx.svg"> patterns in HTML files
with the SVG content inlined directly.
"""

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from workspace_paths import get_client_path


CLIENT_NAME = os.getenv("CLIENT_NAME", "ot-assignment-help")
CLIENT_DIR = get_client_path(CLIENT_NAME)
PAGES_DIR = CLIENT_DIR / "pages"
INFOGRAPHICS_DIR = CLIENT_DIR / "infographics"

def clean_svg(svg_content):
    """Strip XML declaration and make SVG embed-ready."""
    # Remove XML declaration
    svg_content = re.sub(r'<\?xml[^?]*\?>', '', svg_content)
    # Remove DOCTYPE if any
    svg_content = re.sub(r'<!DOCTYPE[^>]*>', '', svg_content)
    svg_content = svg_content.strip()
    return svg_content

def get_svg_filename_from_path(path):
    """Extract filename from a path like ../infographics/xxx.svg"""
    return os.path.basename(path)

def load_svg(filename):
    svg_path = INFOGRAPHICS_DIR / filename
    if not svg_path.exists():
        print(f"  WARNING: SVG not found: {svg_path}")
        return None
    with open(svg_path, 'r', encoding='utf-8') as f:
        return clean_svg(f.read())

def wrap_inline_svg(svg_content, alt_text=""):
    """Wrap inline SVG in a figure with caption for accessibility."""
    return f'<figure class="infographic-figure" style="margin:0;">\n{svg_content}\n</figure>'

def process_html_file(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changes = 0

    # Pattern 1: <object data="../infographics/xxx.svg" ...>...</object>
    # This may contain a nested <img> fallback — replace the whole object block
    def replace_object(m):
        nonlocal changes
        svg_filename = get_svg_filename_from_path(m.group(1))
        svg_content = load_svg(svg_filename)
        if svg_content is None:
            return m.group(0)
        changes += 1
        print(f"  Inlined (object): {svg_filename}")
        return wrap_inline_svg(svg_content)

    content = re.sub(
        r'<object\s+data="\.\./infographics/([^"]+\.svg)"[^>]*>.*?</object>',
        replace_object,
        content,
        flags=re.DOTALL
    )

    # Pattern 2: standalone <img src="../infographics/xxx.svg" ...>
    # (self-closing or with />)
    def replace_img(m):
        nonlocal changes
        full_tag = m.group(0)
        # Extract src
        src_match = re.search(r'src="\.\./infographics/([^"]+\.svg)"', full_tag)
        if not src_match:
            return full_tag
        svg_filename = src_match.group(1)
        # Extract alt text
        alt_match = re.search(r'alt="([^"]*)"', full_tag)
        alt_text = alt_match.group(1) if alt_match else ""
        svg_content = load_svg(svg_filename)
        if svg_content is None:
            return full_tag
        changes += 1
        print(f"  Inlined (img):    {svg_filename}")
        return wrap_inline_svg(svg_content, alt_text)

    content = re.sub(
        r'<img\s[^>]*src="\.\./infographics/[^"]+\.svg"[^>]*/?>',
        replace_img,
        content,
        flags=re.DOTALL
    )

    if changes > 0:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Saved {changes} replacement(s) -> {os.path.basename(html_path)}")
    else:
        print(f"  No changes -> {os.path.basename(html_path)}")

    return changes

def main():
    if not PAGES_DIR.exists():
        raise FileNotFoundError(f"Pages directory not found: {PAGES_DIR}")

    html_files = [f for f in os.listdir(PAGES_DIR) if f.endswith('.html')]
    total = 0
    for filename in sorted(html_files):
        path = os.path.join(PAGES_DIR, filename)
        print(f"\nProcessing: {filename}")
        total += process_html_file(path)
    print(f"\nDone. {total} SVG(s) inlined across {len(html_files)} HTML file(s).")

if __name__ == '__main__':
    main()
