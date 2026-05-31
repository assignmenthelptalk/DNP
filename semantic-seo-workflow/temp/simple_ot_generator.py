from pathlib import Path
import html
import json
import sys

ROOT = Path(r"c:\Users\jobmu\agentic-workflow\semantic-seo-workflow")
PAGES = ROOT / "client_data" / "ot-assignment-help" / "pages"
PAGES.mkdir(parents=True, exist_ok=True)

CSS = """body{margin:0;font-family:'Inter','Segoe UI',Arial,sans-serif;line-height:1.7;background:#f4f8fb;color:#243447}article{max-width:980px;margin:0 auto;background:#fff;box-shadow:0 10px 34px rgba(21,58,95,.08)}.breadcrumb{background:#163a5f;color:#d8e7f2;padding:12px 28px;font-size:13px}.breadcrumb a{color:#d8e7f2;text-decoration:none}.hero{padding:44px 32px 36px;background:linear-gradient(135deg,#163a5f 0%,#2f6b8a 100%);color:#fff}.hero h1{margin:0 0 14px;font-size:clamp(1.8rem,3vw,2.5rem);line-height:1.2}.hero p{max-width:760px;margin:0 0 12px;color:#d7e7f2}.hero .cta{display:inline-block;margin-top:10px;padding:12px 20px;border-radius:6px;background:#2aa198;color:#fff;text-decoration:none;font-weight:700}main{padding:30px 32px 44px}section{margin:0 0 34px}h2{margin:0 0 12px;color:#163a5f;font-size:1.45rem;line-height:1.3}p{margin:0 0 14px}ul{margin:0 0 16px 20px;padding:0}li{margin:0 0 8px}.contextual{background:#163a5f;color:#fff;padding:22px 24px;border-radius:10px;margin:36px 0}.contextual h2{color:#fff}.contextual p{color:#d9ebf4}.callout{background:#eef7f8;border-left:4px solid #2aa198;padding:16px 18px;border-radius:0 8px 8px 0}.infographic{margin:20px 0 24px;border:1px solid #d4e4ec;border-radius:12px;overflow:hidden;background:#f8fcfd}.infographic figcaption{padding:10px 14px 14px;text-align:center;font-size:.86rem;color:#496579}.faq-item{border:1px solid #d8e6ee;border-radius:8px;overflow:hidden;margin-bottom:12px}.faq-q{background:#edf5f8;padding:14px 16px;font-weight:700;color:#163a5f}.faq-a{padding:14px 16px}"""


def esc(value):
    return html.escape(value, quote=True)


def make_info(info):
    items = info["items"][:4]
    cards = []
    for i, (title, body) in enumerate(items):
        x = 40 + i * 185
        cards.append(
            f"<rect x='{x}' y='140' width='170' height='210' rx='16' fill='white' stroke='#cfe0e8'/>"
            f"<text x='{x+18}' y='178' font-size='19' font-weight='700' fill='#163a5f'>{esc(title)}</text>"
            f"<foreignObject x='{x+18}' y='196' width='134' height='136'><div xmlns='http://www.w3.org/1999/xhtml' style='font-family:Inter,Segoe UI,Arial,sans-serif;font-size:14px;line-height:1.45;color:#355061'>{esc(body)}</div></foreignObject>"
        )
    return f"<figure class='infographic'><svg viewBox='0 0 800 390' width='100%' xmlns='http://www.w3.org/2000/svg' role='img'><rect width='800' height='390' fill='#f3f8fb'/><text x='40' y='54' font-size='28' font-weight='800' fill='#163a5f'>{esc(info['title'])}</text><text x='40' y='84' font-size='15' fill='#4f6879'>{esc(info['desc'])}</text>{''.join(cards)}</svg><figcaption>{esc(info['desc'])}</figcaption></figure>"


def section_html(sec):
    parts = [f"<section><h2>{esc(sec['title'])}</h2><p>{sec['lead']}</p>"]
    if sec.get("bullets"):
        parts.append("<ul>" + "".join(f"<li>{item}</li>" for item in sec["bullets"]) + "</ul>")
    if sec.get("info"):
        parts.append(make_info(sec["info"]))
    if sec.get("note"):
        parts.append(f"<div class='callout'><strong>Assignment note:</strong> {sec['note']}</div>")
    parts.append("</section>")
    return "".join(parts)


def render(page):
    sections = "".join(section_html(s) for s in page["sections"])
    supp = "".join(section_html(s) for s in page.get("supplementary", []))
    faqs = "".join(f"<div class='faq-item'><div class='faq-q'>{esc(q)}</div><div class='faq-a'><p>{a}</p></div></div>" for q, a in page["faqs"])
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in page["faqs"]]}
    return f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>{esc(page['meta_title'])}</title><meta name='description' content='{esc(page['meta_description'])}'><style>{CSS}</style></head><body><article><div class='breadcrumb'><a href='occupational-therapy-assignment-help.html'>Occupational Therapy Assignment Help</a> / <span>{esc(page['h1'])}</span></div><header class='hero'><h1>{esc(page['h1'])}</h1><p>{page['intro']}</p><a class='cta' href='#faq'>Get help with this OT assignment topic</a></header><main>{sections}<div class='contextual'><h2>{esc(page['contextual_title'])}</h2><p>{page['contextual_body']}</p></div>{supp}<section id='faq'><h2>Frequently Asked Questions</h2>{faqs}</section></main></article><script type='application/ld+json'>{json.dumps(schema, ensure_ascii=False)}</script></body></html>"


if __name__ == "__main__":
    pages = json.loads(sys.stdin.read())
    for page in pages:
        (PAGES / page["slug"]).write_text(render(page), encoding="utf-8")
    print(f"generated {len(pages)} pages")
