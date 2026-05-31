from pathlib import Path

ROOT = Path(r"c:\Users\jobmu\agentic-workflow\semantic-seo-workflow")
PAGES = ROOT / "client_data" / "ot-assignment-help" / "pages"
DOMAIN = "https://otassignmenthelp.co.uk"

RELATED = {
    "dementia-ot-assignment-help.html": [
        ("Assistive technology and environmental modification in OT assignments", "assistive-technology-environmental-modification-ot.html"),
        ("Occupational therapy ethics and professional identity", "occupational-therapy-ethics-assignment.html"),
        ("Occupational therapy assignment help", "occupational-therapy-assignment-help.html"),
    ],
    "neurological-ot-assignment-help.html": [
        ("Assistive technology and environmental modification in OT assignments", "assistive-technology-environmental-modification-ot.html"),
        ("OT assessment tools assignment help", "ot-assessment-tools-assignment-help.html"),
        ("Occupational therapy assignment help", "occupational-therapy-assignment-help.html"),
    ],
    "ot-assessment-tools-assignment-help.html": [
        ("Neurological OT assignment help", "neurological-ot-assignment-help.html"),
        ("Dementia OT assignment help", "dementia-ot-assignment-help.html"),
        ("OTPF assignment help", "otpf-assignment-help.html"),
    ],
    "paediatric-ot-assignment-help.html": [
        ("Sensory integration theory for OT students", "sensory-integration-theory-occupational-therapy.html"),
        ("Occupational therapy assignment help", "occupational-therapy-assignment-help.html"),
        ("OT reflective essay assignment help", "ot-reflective-essay-assignment-help.html"),
    ],
    "assistive-technology-environmental-modification-ot.html": [
        ("Neurological OT assignment help", "neurological-ot-assignment-help.html"),
        ("Dementia OT assignment help", "dementia-ot-assignment-help.html"),
        ("NHS structure and OT service delivery", "nhs-structure-occupational-therapy.html"),
    ],
    "how-to-reference-occupational-therapy-assignment.html": [
        ("OT literature review assignment help", "ot-literature-review-assignment-help.html"),
        ("OT dissertation research proposal help", "ot-dissertation-research-proposal-help.html"),
        ("Occupational therapy assignment help", "occupational-therapy-assignment-help.html"),
    ],
    "occupational-therapy-degree-programme.html": [
        ("OT practice placement assignment help", "ot-practice-placement-assignment-help.html"),
        ("Occupational therapy career pathways and CPD", "occupational-therapy-career-pathways-cpd.html"),
        ("Occupational therapy assignment help", "occupational-therapy-assignment-help.html"),
    ],
    "global-cultural-context-occupational-therapy.html": [
        ("Kawa model in occupational therapy assignments", "kawa-model-occupational-therapy-assignment.html"),
        ("Occupational science for OT students", "occupational-science-for-ot-students.html"),
        ("Occupational therapy ethics and professional identity", "occupational-therapy-ethics-assignment.html"),
    ],
    "kawa-model-occupational-therapy-assignment.html": [
        ("Global and cultural context of occupational therapy", "global-cultural-context-occupational-therapy.html"),
        ("CMOP-E assignment help", "cmop-e-assignment-help.html"),
        ("MOHO assignment help", "moho-assignment-help.html"),
    ],
    "mdt-interprofessional-practice-occupational-therapy.html": [
        ("NHS structure and OT service delivery", "nhs-structure-occupational-therapy.html"),
        ("Neurological OT assignment help", "neurological-ot-assignment-help.html"),
        ("OT practice placement assignment help", "ot-practice-placement-assignment-help.html"),
    ],
    "nhs-structure-occupational-therapy.html": [
        ("MDT and interprofessional practice in OT assignments", "mdt-interprofessional-practice-occupational-therapy.html"),
        ("Occupational therapy career pathways and CPD", "occupational-therapy-career-pathways-cpd.html"),
        ("OT practice placement assignment help", "ot-practice-placement-assignment-help.html"),
    ],
    "occupational-therapy-career-pathways-cpd.html": [
        ("NHS structure and OT service delivery", "nhs-structure-occupational-therapy.html"),
        ("OT practice placement assignment help", "ot-practice-placement-assignment-help.html"),
        ("Occupational therapy degree programme overview", "occupational-therapy-degree-programme.html"),
    ],
    "occupational-therapy-ethics-assignment.html": [
        ("Dementia OT assignment help", "dementia-ot-assignment-help.html"),
        ("OT reflective essay assignment help", "ot-reflective-essay-assignment-help.html"),
        ("Global and cultural context of occupational therapy", "global-cultural-context-occupational-therapy.html"),
    ],
    "sensory-integration-theory-occupational-therapy.html": [
        ("Paediatric OT assignment help", "paediatric-ot-assignment-help.html"),
        ("Occupational science for OT students", "occupational-science-for-ot-students.html"),
        ("OT assignment help", "occupational-therapy-assignment-help.html"),
    ],
    "occupational-science-for-ot-students.html": [
        ("Global and cultural context of occupational therapy", "global-cultural-context-occupational-therapy.html"),
        ("Kawa model in occupational therapy assignments", "kawa-model-occupational-therapy-assignment.html"),
        ("OTPF assignment help", "otpf-assignment-help.html"),
    ],
}


STYLE = (
    ".related-links{background:#eef6f8;border:1px solid #d7e6ec;border-radius:10px;padding:20px 22px;margin:34px 0}"
    ".related-links h2{margin:0 0 12px;color:#163a5f;font-size:1.2rem}"
    ".related-links ul{margin:0 0 0 18px;padding:0}.related-links li{margin:0 0 8px}"
    ".related-links a{color:#2a9d8f;text-decoration:underline}"
)


def slug_to_url(slug: str) -> str:
    return f"{DOMAIN}/{slug[:-5]}"


def build_related(filename: str) -> str:
    links = RELATED.get(filename, [])
    if not links:
        return ""
    items = "".join(f"<li><a href='{href}'>{label}</a></li>" for label, href in links)
    return f"<section class='related-links'><h2>Related OT Pages</h2><ul>{items}</ul></section>"


for path in RELATED:
    file_path = PAGES / path
    if not file_path.exists():
        continue
    content = file_path.read_text(encoding="utf-8")
    title_start = content.find("<title>") + len("<title>")
    title_end = content.find("</title>")
    title = content[title_start:title_end]
    desc_marker = "meta name='description' content='"
    desc_start = content.find(desc_marker) + len(desc_marker)
    desc_end = content.find("'>", desc_start)
    description = content[desc_start:desc_end]
    head_insert = (
        f"<meta name='robots' content='index, follow'>"
        f"<link rel='canonical' href='{slug_to_url(path)}'>"
        f"<meta property='og:title' content='{title}'>"
        f"<meta property='og:description' content='{description}'>"
        f"<meta property='og:type' content='article'>"
        f"<meta property='og:url' content='{slug_to_url(path)}'>"
    )
    if "meta name='robots'" not in content:
        content = content.replace("</title>", f"</title>{head_insert}", 1)
    if ".related-links{" not in content:
        content = content.replace("</style>", STYLE + "</style>", 1)
    related_html = build_related(path)
    if related_html and "Related OT Pages" not in content:
        content = content.replace("<section id='faq'>", related_html + "<section id='faq'>", 1)
    file_path.write_text(content, encoding="utf-8")

print("postprocessed", len(RELATED), "generated pages")
