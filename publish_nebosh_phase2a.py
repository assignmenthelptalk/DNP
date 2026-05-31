"""
publish_nebosh_phase2a.py
Converts the 6 Phase 2A written-content .md files to .html files,
copies them to src/content/pages/, and adds page entries to content.json.
"""

import json, os, re

CONTENT_DIR  = r"C:\Users\jobmu\agentic-workflow\semantic-seo-workflow\client_data\New-sites\nebosh-assignment-help\written-content"
PAGES_DIR    = r"C:\Users\jobmu\my-second-projects\nebosh-assignment-help\src\content\pages"
CONTENT_JSON = r"C:\Users\jobmu\my-second-projects\nebosh-assignment-help\content.json"

# ── Page metadata ─────────────────────────────────────────────────────────────
PAGES = [
    {
        "slug": "nebosh-assignment-marking-criteria-explained",
        "tier": 2,
        "title": "NEBOSH Assignment Marking Criteria Explained",
        "metaTitle": "NEBOSH Assignment Marking Criteria: How Examiners Grade Your Work | NEBOSH Assignment Help",
        "metaDescription": "Understand NEBOSH's grading bands — Pass, Merit, Distinction, and Refer — with command word expectations and examiner insights. Expert guidance included.",
        "h1": "NEBOSH Assignment Marking Criteria: How Your Work Is Graded and What Examiners Want",
        "intro": "Understand exactly how NEBOSH grades your assignment — grading bands, command word compliance, and what examiners specifically look for at each level.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH IG1 Model Answers", "slug": "nebosh-ig1-assignment-model-answers"},
            {"title": "How to Pass NEBOSH Assignment First Time", "slug": "how-to-pass-nebosh-assignment-first-time"},
            {"title": "NEBOSH Open Book Exam Help", "slug": "nebosh-open-book-exam-obe-help"},
        ],
        "contextualQuestion": "How does NEBOSH's marking philosophy connect answer depth to practical health and safety application?",
        "headerImage": {
            "src": "/header_nebosh-assignment-marking-criteria-explained.webp",
            "alt": "NEBOSH Assignment Marking Criteria — Grading Bands and Examiner Expectations",
            "title": "NEBOSH Assignment Marking Criteria — Grading Bands and Examiner Expectations",
            "width": 1200,
            "height": 420,
        },
        "md_file": "nebosh-assignment-marking-criteria-explained-content.md",
    },
    {
        "slug": "how-to-pass-nebosh-assignment-first-time",
        "tier": 2,
        "title": "How to Pass NEBOSH Assignment First Time",
        "metaTitle": "How to Pass Your NEBOSH Assignment First Time: Proven Strategies | NEBOSH Assignment Help",
        "metaDescription": "Avoid NEBOSH referral with proven strategies: command word compliance, examiner report analysis, answer structure, and OBE time management. Expert guidance.",
        "h1": "How to Pass Your NEBOSH Assignment First Time: Proven Strategies From Safety Professionals",
        "intro": "Proven strategies to pass your NEBOSH OBE on the first attempt — command word compliance, answer structure, examiner report intelligence, and pre-submission checklist.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH Assignment Marking Criteria Explained", "slug": "nebosh-assignment-marking-criteria-explained"},
            {"title": "NEBOSH IG1 Model Answers", "slug": "nebosh-ig1-assignment-model-answers"},
            {"title": "NEBOSH Assignment Word Count Requirements", "slug": "nebosh-assignment-word-count-requirements"},
        ],
        "contextualQuestion": "What preparation habits distinguish distinction students from those who receive a referral?",
        "headerImage": {
            "src": "/header_nebosh-how-to-pass-assignment-first-time.webp",
            "alt": "How to Pass Your NEBOSH Assignment First Time — Expert Strategy Guide",
            "title": "How to Pass Your NEBOSH Assignment First Time — Expert Strategy Guide",
            "width": 1200,
            "height": 420,
        },
        "md_file": "how-to-pass-nebosh-assignment-first-time-content.md",
    },
    {
        "slug": "nebosh-ig1-assignment-model-answers",
        "tier": 2,
        "title": "NEBOSH IG1 Assignment Model Answers",
        "metaTitle": "NEBOSH IG1 Model Answers: How a Distinction-Grade Assignment Looks | NEBOSH Assignment Help",
        "metaDescription": "See how distinction-grade NEBOSH IG1 answers are structured — task by task, with command word compliance, element references, and real workplace application.",
        "h1": "NEBOSH IG1 Model Answers: How a Distinction-Grade Assignment Looks",
        "intro": "Distinction-grade NEBOSH IG1 answer anatomy — task structure, annotated examples, all 11 IGC elements, hazard identification technique, and the merit-distinction gap.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH IGC Assignment Help", "slug": "nebosh-igc-assignment-help"},
            {"title": "NEBOSH Assignment Marking Criteria Explained", "slug": "nebosh-assignment-marking-criteria-explained"},
            {"title": "NEBOSH IG2 Practical Assessment Help", "slug": "nebosh-ig2-practical-assessment-help"},
        ],
        "contextualQuestion": "How does the IG1 marking scheme define sufficient depth for each open book exam element?",
        "headerImage": {
            "src": "/header_nebosh-ig1-assignment-model-answers.webp",
            "alt": "NEBOSH IG1 Model Answers — Distinction-Grade Assignment Structure",
            "title": "NEBOSH IG1 Model Answers — Distinction-Grade Assignment Structure",
            "width": 1200,
            "height": 420,
        },
        "md_file": "nebosh-ig1-assignment-model-answers-content.md",
    },
    {
        "slug": "nebosh-ig2-practical-assessment-help",
        "tier": 2,
        "title": "NEBOSH IG2 Practical Assessment Help",
        "metaTitle": "NEBOSH IG2 Practical Assessment Help: Complete Your Workplace Report | NEBOSH Assignment Help",
        "metaDescription": "Expert guidance on completing the NEBOSH IG2 practical assessment — workplace inspection, risk assessment format, management report, and submission requirements.",
        "h1": "NEBOSH IG2 Practical Assessment Help: Complete Your Workplace Inspection Report",
        "intro": "Step-by-step guidance for the NEBOSH IG2 — workplace inspection methodology, risk assessment format with all mandatory fields, SMART management report writing.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH IGC Assignment Help", "slug": "nebosh-igc-assignment-help"},
            {"title": "NEBOSH IG1 Model Answers", "slug": "nebosh-ig1-assignment-model-answers"},
            {"title": "NEBOSH Assignment Referral Recovery", "slug": "nebosh-assignment-referral-recovery"},
        ],
        "contextualQuestion": "How does the NEBOSH IG2 connect workplace hazard identification to health and safety management principles?",
        "headerImage": {
            "src": "/header_nebosh-ig2-practical-assessment-help.webp",
            "alt": "NEBOSH IG2 Practical Assessment Help — Workplace Inspection and Risk Assessment",
            "title": "NEBOSH IG2 Practical Assessment Help — Workplace Inspection and Risk Assessment",
            "width": 1200,
            "height": 420,
        },
        "md_file": "nebosh-ig2-practical-assessment-help-content.md",
    },
    {
        "slug": "nebosh-assignment-word-count-requirements",
        "tier": 2,
        "title": "NEBOSH Assignment Word Count Requirements",
        "metaTitle": "NEBOSH Assignment Word Count: What Each Unit Requires (IG1, NG1, Diploma) | NEBOSH Assignment Help",
        "metaDescription": "Word count guidance for NEBOSH IG1, NG1, and Diploma assignments — what NEBOSH expects per task, how length connects to marking, and how to write with depth.",
        "h1": "NEBOSH Assignment Word Count: What Each Unit Requires and How to Manage It",
        "intro": "Unit-specific word count benchmarks for NEBOSH IG1, NG1, and Diploma assignments — with per-mark targets, over/under-writing effects, and concise writing technique.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH Assignment Marking Criteria Explained", "slug": "nebosh-assignment-marking-criteria-explained"},
            {"title": "How to Pass NEBOSH Assignment First Time", "slug": "how-to-pass-nebosh-assignment-first-time"},
            {"title": "NEBOSH IG1 Model Answers", "slug": "nebosh-ig1-assignment-model-answers"},
        ],
        "contextualQuestion": "How does NEBOSH's approach to word count connect to the examiner's expectation for quality over quantity?",
        "headerImage": {
            "src": "/header_nebosh-assignment-word-count-requirements.webp",
            "alt": "NEBOSH Assignment Word Count Requirements — IG1, NG1, and Diploma Guidance",
            "title": "NEBOSH Assignment Word Count Requirements — IG1, NG1, and Diploma Guidance",
            "width": 1200,
            "height": 420,
        },
        "md_file": "nebosh-assignment-word-count-requirements-content.md",
    },
    {
        "slug": "nebosh-assignment-referral-recovery",
        "tier": 2,
        "title": "NEBOSH Assignment Referral Recovery",
        "metaTitle": "NEBOSH Assignment Referral: What It Means and What to Do Next | NEBOSH Assignment Help",
        "metaDescription": "Received a NEBOSH referral? Understand exactly what went wrong, what the re-submission process involves, and how to avoid a second referral with expert help.",
        "h1": "NEBOSH Assignment Referral: What It Means, Why It Happens, and What to Do Next",
        "intro": "Received a NEBOSH referral? Understand what it means, why it happened, and the exact re-submission process — with strategies to prevent a second referral.",
        "h2Sections": [],
        "relatedPages": [
            {"title": "NEBOSH Assignment Marking Criteria Explained", "slug": "nebosh-assignment-marking-criteria-explained"},
            {"title": "How to Pass NEBOSH Assignment First Time", "slug": "how-to-pass-nebosh-assignment-first-time"},
            {"title": "NEBOSH IGC Assignment Help", "slug": "nebosh-igc-assignment-help"},
        ],
        "contextualQuestion": "What is the fastest path from a NEBOSH referral to a successful re-submission?",
        "headerImage": {
            "src": "/header_nebosh-assignment-referral-recovery.webp",
            "alt": "NEBOSH Assignment Referral Recovery — Re-submission Guidance and Expert Help",
            "title": "NEBOSH Assignment Referral Recovery — Re-submission Guidance and Expert Help",
            "width": 1200,
            "height": 420,
        },
        "md_file": "nebosh-assignment-referral-recovery-content.md",
    },
]


# ── Markdown → HTML converter ─────────────────────────────────────────────────

def md_inline(text):
    """Convert inline markdown: bold, italic, links, code."""
    # Links [text](url)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic *text*
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Inline code `code`
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text


def md_to_html(md_text):
    """
    Convert a Phase 2A markdown content file to HTML.
    Rules:
      - Skip the # H1 title line (handled by page hero)
      - Skip the intro paragraph immediately after title (handled by page hero)
      - Skip --- dividers between title and ## MAIN CONTENT
      - Wrap ## MAIN CONTENT block in <div class="main-content">
      - Wrap ## SUPPLEMENTARY CONTENT block in <div class="supplementary">
      - ### heading  → <h2>
      - #### heading → <h3>
      - | table |    → <table>
      - HTML blocks  → pass through unchanged
      - Blank lines separate paragraphs
    """
    lines = md_text.split('\n')

    # ── Pass 1: identify structural sections ──────────────────────────────────
    # Find where MAIN CONTENT and SUPPLEMENTARY CONTENT start
    main_start = supp_start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '## MAIN CONTENT':
            main_start = i
        elif stripped == '## SUPPLEMENTARY CONTENT':
            supp_start = i

    # ── Pass 2: convert line by line ──────────────────────────────────────────
    html_parts = []
    in_html_block = False       # inside a raw HTML element (SVG, div, figure…)
    in_table = False
    in_main = False
    in_supp = False
    para_lines = []             # accumulate paragraph lines

    def flush_para():
        nonlocal para_lines
        if para_lines:
            joined = ' '.join(para_lines).strip()
            if joined:
                html_parts.append(f'<p>{md_inline(joined)}</p>')
            para_lines = []

    def flush_table(rows):
        """Convert markdown table rows to HTML table."""
        if len(rows) < 2:
            return
        html_parts.append('<table class="nebosh-table" style="width:100%;border-collapse:collapse;margin:1rem 0;">')
        for ri, row in enumerate(rows):
            if re.match(r'^\|[\s\-|]+\|$', row.strip()):
                continue  # separator row
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            tag = 'th' if ri == 0 else 'td'
            style = 'border:1px solid #e5e7eb;padding:0.5rem 0.75rem;text-align:left;'
            if ri == 0:
                style += 'background:#7C1D1D;color:#fff;font-weight:700;'
            elif ri % 2 == 0:
                style += 'background:#f9fafb;'
            html_parts.append('<tr>' + ''.join(f'<{tag} style="{style}">{md_inline(c)}</{tag}>' for c in cells) + '</tr>')
        html_parts.append('</table>')

    table_rows = []
    skip_until_main = True   # skip everything before ## MAIN CONTENT
    title_skipped = False
    intro_skipped = False
    dividers_after_title = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Skip H1 title ──────────────────────────────────────────────────
        if not title_skipped and stripped.startswith('# ') and not stripped.startswith('## '):
            title_skipped = True
            i += 1
            continue

        # ── Track section markers ──────────────────────────────────────────
        if stripped == '## MAIN CONTENT':
            flush_para()
            if in_supp:
                html_parts.append('</div><!-- /supplementary -->')
                in_supp = False
            if in_main:
                html_parts.append('</div><!-- /main-content -->')
                in_main = False
            html_parts.append('<div class="main-content">')
            in_main = True
            skip_until_main = False
            i += 1
            continue

        if stripped == '## SUPPLEMENTARY CONTENT':
            flush_para()
            if in_main:
                html_parts.append('</div><!-- /main-content -->')
                in_main = False
            if in_supp:
                html_parts.append('</div><!-- /supplementary -->')
                in_supp = False
            html_parts.append('<div class="supplementary">')
            in_supp = True
            i += 1
            continue

        # Skip content before MAIN CONTENT marker
        if skip_until_main:
            i += 1
            continue

        # ── Detect raw HTML blocks ─────────────────────────────────────────
        # An HTML block starts with < (opening tag) and ends when we hit a blank line
        # after the block closes. We track open/close for common block elements.
        if not in_html_block and stripped.startswith('<') and not stripped.startswith('</'):
            # Could be start of an HTML block - pass through until it's "done"
            # Heuristic: collect lines until we see a closing tag or blank line after content
            flush_para()
            html_block = []
            depth = 0
            # Simple block collection: collect until we see matching close or standalone blank
            j = i
            while j < len(lines):
                l = lines[j]
                html_block.append(l)
                # Count opening tags (rough)
                opens = len(re.findall(r'<(?!/)(?!br)(?!img)(?!input)([a-zA-Z][a-zA-Z0-9]*)[^>]*(?<!/)>', l))
                closes = len(re.findall(r'</[a-zA-Z][a-zA-Z0-9]*>', l))
                depth += opens - closes
                j += 1
                # Stop when depth is back to 0 and we've consumed at least one line
                if j > i and depth <= 0 and l.strip():
                    # Check if next line is blank or another block-level element
                    if j >= len(lines) or not lines[j].strip() or lines[j].strip().startswith('<'):
                        break
                    # also stop if next line is markdown heading
                    if lines[j].strip().startswith('#'):
                        break
            html_parts.append('\n'.join(html_block))
            i = j
            continue

        # ── ### H2 heading ────────────────────────────────────────────────
        if stripped.startswith('### '):
            flush_para()
            if in_table:
                flush_table(table_rows)
                table_rows = []
                in_table = False
            heading_text = stripped[4:].strip()
            html_parts.append(f'<h2>{md_inline(heading_text)}</h2>')
            i += 1
            continue

        # ── #### H3 heading ───────────────────────────────────────────────
        if stripped.startswith('#### '):
            flush_para()
            if in_table:
                flush_table(table_rows)
                table_rows = []
                in_table = False
            heading_text = stripped[5:].strip()
            html_parts.append(f'<h3>{md_inline(heading_text)}</h3>')
            i += 1
            continue

        # ── Table row ─────────────────────────────────────────────────────
        if stripped.startswith('|') and stripped.endswith('|'):
            flush_para()
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(stripped)
            i += 1
            continue
        elif in_table:
            flush_table(table_rows)
            table_rows = []
            in_table = False

        # ── Horizontal rule --- ───────────────────────────────────────────
        if stripped == '---':
            flush_para()
            i += 1
            continue

        # ── Blank line ────────────────────────────────────────────────────
        if not stripped:
            flush_para()
            i += 1
            continue

        # ── Bullet list item ─  ──────────────────────────────────────────
        if stripped.startswith('- ') or re.match(r'^\d+\. ', stripped):
            flush_para()
            # Collect list items
            list_lines = []
            ordered = bool(re.match(r'^\d+\. ', stripped))
            tag = 'ol' if ordered else 'ul'
            while i < len(lines) and (lines[i].strip().startswith('- ') or re.match(r'^\d+\. ', lines[i].strip())):
                item_text = re.sub(r'^[-*]\s+|^\d+\.\s+', '', lines[i].strip())
                list_lines.append(f'<li>{md_inline(item_text)}</li>')
                i += 1
            html_parts.append(f'<{tag}>{"".join(list_lines)}</{tag}>')
            continue

        # ── Regular text line → accumulate into paragraph ─────────────────
        para_lines.append(stripped)
        i += 1

    # Flush any remaining
    flush_para()
    if in_table:
        flush_table(table_rows)
    if in_main:
        html_parts.append('</div><!-- /main-content -->')
    if in_supp:
        html_parts.append('</div><!-- /supplementary -->')

    return '\n'.join(html_parts)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Load existing content.json
    with open(CONTENT_JSON, encoding='utf-8') as f:
        content = json.load(f)

    existing_slugs = {p['slug'] for p in content.get('pages', [])}

    for page_meta in PAGES:
        slug    = page_meta['slug']
        md_file = page_meta.pop('md_file')

        # ── Convert markdown → HTML ────────────────────────────────────────
        md_path = os.path.join(CONTENT_DIR, md_file)
        with open(md_path, encoding='utf-8') as f:
            md_text = f.read()

        html = md_to_html(md_text)

        html_out = os.path.join(PAGES_DIR, slug + '.html')
        with open(html_out, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'  HTML  {slug}.html')

        # ── Add to content.json if not already present ─────────────────────
        if slug not in existing_slugs:
            content['pages'].append(page_meta)
            existing_slugs.add(slug)
            print(f'  JSON  {slug} added to content.json')
        else:
            # Update existing entry
            for i, p in enumerate(content['pages']):
                if p['slug'] == slug:
                    content['pages'][i] = page_meta
                    break
            print(f'  JSON  {slug} updated in content.json')

    # Write back content.json
    with open(CONTENT_JSON, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)
    print(f'\nDone. content.json updated with {len(PAGES)} Phase 2A pages.')


if __name__ == '__main__':
    main()
