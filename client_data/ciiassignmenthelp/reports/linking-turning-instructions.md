# Internal Linking — Turning Instructions
**Client:** CII Assignment Help
**Date:** 2026-03-22
**Based on:** linking-report.md
**Scope:** Fix all broken slugs, remove duplicate links, inject missing links into 20 content files

---

## How to Use This Document

Work through the three phases in order. Each instruction specifies the exact file, the exact line range, and the exact change to make. Do not skip Phase 1 — broken slugs will make Phase 3 injections point to 404s.

---

## Phase 1 — Fix Broken Slugs (Global Find-and-Replace)

Do these three find-and-replace operations across ALL files in `written-content/` before touching anything else.

### 1A — Advanced Diploma Hub Slug

**Find (all variants):**
- `/cii-advanced-diploma-in-insurance-assignment-help`
- `/cii-advanced-diploma-assignment-help`

**Replace all with:**
```
/advanced-diploma-assignment-help
```

**Files affected:** 820, 930, 960, 993, 994, 990, 991, cii-advanced-diploma, m97 (any instance)

---

### 1B — Diploma Hub Slug

**Find:**
```
/cii-diploma-in-insurance-assignment-help
```

**Replace with:**
```
/cii-diploma-assignment-help
```

**Files affected:** M80, M85, M97, M92, 530, M05, cii-diploma, cii-certificate, 820

---

### 1C — M80 Slug

**Find:**
```
/m80-underwriting-practice-assignment-help
```

**Replace with:**
```
/m80-assignment-help
```

**Files affected:** m85-claims-practice-content.md (line 220), m97-reinsurance-content.md (line 187)

---

## Phase 2 — Remove Duplicate Links

Fix duplicate URLs within individual files. A URL must appear only once per page.

---

### 2A — cii-diploma-in-insurance-content.md

**Issue:** M05 linked 3 times; M80, M85, M97, /cii-assignment-help each linked twice.

**Action 1:** Find all three instances of `/m05-assignment-help`. Keep the one at line 39 (main content). For lines 73 and 159 — convert the linked text to plain text (remove the `[` `](/m05-assignment-help)` markdown link syntax, keep just the words).

**Action 2:** Find both instances of `/m80-assignment-help`. Keep the one at line 115. Convert the line 160 instance to plain text.

**Action 3:** Find both instances of `/m85-assignment-help`. Keep the one at line 115. Convert the line 162 instance to plain text.

**Action 4:** Find both instances of `/m97-assignment-help`. Keep the one at line 115. Convert the line 163 instance to plain text.

**Action 5:** Find both instances of `/cii-assignment-help`. Keep the one in main content (line 15). Remove or convert the supplementary instance at line 137 to plain text.

---

### 2B — cii-advanced-diploma-in-insurance-content.md

**Issue:** 820, 930, 960, 991 each linked in both main content and supplementary; M05 and Diploma hub each linked twice in supplementary.

**Action:** For each of the following URLs, keep the supplementary section instance and convert the main content instance to plain text:
- `/820-assignment-help` — keep supplementary (line 137), convert main content (line 37) to plain text
- `/930-assignment-help` — keep supplementary (line 138), convert main content (line 45) to plain text
- `/960-assignment-help` — keep supplementary (line 139), convert main content (line 53) to plain text
- `/991-assignment-help` — keep supplementary (line 140), convert main content (line 77) to plain text

**Action:** For `/m05-assignment-help` at lines 97 and 117 — keep line 97, convert line 117 to plain text.

**Action:** For `/cii-diploma-assignment-help` at lines 97 and 117 — keep line 97, convert line 117 to plain text.

---

### 2C — 994-insurance-market-specialisation-content.md

**Issue:** `/993-assignment-help` appears at both line 193 and line 211.

**Action:** Keep line 193. At line 211, replace the `/993-assignment-help` link with `/930-assignment-help`:

Find at line 211:
```
[993 strategic risk management assignment help](/993-assignment-help)
```
Replace with:
```
[930 advanced insurance broking assignment help](/930-assignment-help)
```

---

### 2D — m85-claims-practice-content.md

**Issue:** `/m05-assignment-help` appears at lines 215 and 221.

**Action:** Keep line 221 (in the bullet list). Convert line 215 instance to plain text.

---

### 2E — cii-certificate-in-insurance-content.md

**Issue:** `/cii-assignment-help` appears at lines 15 and 103.

**Action:** Keep line 15. Convert line 103 instance to plain text.

---

## Phase 3 — Inject Missing Links

Add the missing internal links to the supplementary sections of each file listed below.

For each file, the "inject after" instruction tells you which line or section to append the link to. All injections go into the supplementary content section (after the `---` contextual border marker, before the FAQ `## Frequently Asked Questions` heading).

---

### 3A — if1-insurance-legal-regulatory-content.md

**Target lines:** ~119 and ~121 in the supplementary section. The text already uses square-bracket notation without URLs — add the `(/slug)` component.

Find at line ~119:
```
[IF3 insurance underwriting process assignment help]
```
Replace with:
```
[IF3 insurance underwriting process assignment help](/if3-assignment-help)
```

Find at line ~119:
```
[IF4 insurance claims handling process assignment help]
```
Replace with:
```
[IF4 insurance claims handling process assignment help](/if4-assignment-help)
```

Find at line ~121:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

---

### 3B — if3-insurance-underwriting-process-content.md

**Target lines:** ~149 and ~153 in the supplementary section.

Find at line ~149:
```
[IF1 insurance legal and regulatory assignment help]
```
Replace with:
```
[IF1 insurance legal and regulatory assignment help](/if1-assignment-help)
```

Find at line ~149:
```
[IF4 insurance claims handling process assignment help]
```
Replace with:
```
[IF4 insurance claims handling process assignment help](/if4-assignment-help)
```

Find at line ~153:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

---

### 3C — if4-insurance-claims-handling-content.md

**Target lines:** ~193 in the supplementary section.

Find at line ~193:
```
[IF3 insurance underwriting process assignment help]
```
Replace with:
```
[IF3 insurance underwriting process assignment help](/if3-assignment-help)
```

Find at line ~193:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

---

### 3D — if5-motor-insurance-content.md

**Target lines:** ~155 in the supplementary section.

Find at line ~155:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

Find at line ~155:
```
[IF1 insurance legal and regulatory assignment help]
```
Replace with:
```
[IF1 insurance legal and regulatory assignment help](/if1-assignment-help)
```

Find at line ~155:
```
[IF4 insurance claims handling assignment help]
```
Replace with:
```
[IF4 insurance claims handling assignment help](/if4-assignment-help)
```

Find at line ~155:
```
[IF3 insurance underwriting process assignment help]
```
Replace with:
```
[IF3 insurance underwriting process assignment help](/if3-assignment-help)
```

---

### 3E — lm3-london-market-broker-content.md

**Target lines:** ~143, ~150, ~152 in the supplementary section.

Find at line ~150:
```
[CII Certificate in Insurance Assignment Help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

Find at line ~152:
```
[CII Diploma in Insurance Assignment Help]
```
Replace with:
```
[CII Diploma in Insurance assignment help](/cii-diploma-assignment-help)
```

Find at line ~143 (contextual mention of 991 without a link):
Wrap the 991 reference in a link. Find the text that reads something like `991 London market specialisation` and replace with:
```
[991 London market specialisation assignment help](/991-assignment-help)
```

---

### 3F — gr1-group-risk-content.md

**Target lines:** ~173–175 in the supplementary section.

Find at line ~173:
```
[CII Certificate in Insurance Assignment Help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

Find at line ~174:
```
[IF1 Insurance Legal and Regulatory Assignment Help]
```
Replace with:
```
[IF1 insurance legal and regulatory assignment help](/if1-assignment-help)
```

---

### 3G — imu-india-motor-insurance-content.md

**Target lines:** ~136, ~188, ~190 in the supplementary section.

Find at line ~190:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

Find at line ~136 where IF5 is mentioned as the UK equivalent — wrap in a link:
Find the phrase `IF5` or `IF5 motor insurance` and replace the nearest plain text reference with:
```
[IF5 motor insurance assignment help](/if5-assignment-help)
```

Find at line ~188 where Diploma progression is mentioned — wrap the Diploma hub reference:
```
[CII Diploma in Insurance assignment help](/cii-diploma-assignment-help)
```

---

### 3H — wce-insurance-claims-non-uk-content.md

**Target lines:** ~154, ~156, ~168 in the supplementary section.

Find at line ~156:
```
[CII Certificate in Insurance assignment help]
```
Replace with:
```
[CII Certificate in Insurance assignment help](/cii-certificate-assignment-help)
```

Find at line ~168:
```
[CII 590 Takaful unit]
```
Replace with:
```
[590 Takaful assignment help](/590-assignment-help)
```

Find at line ~154 where IF4 is mentioned as the UK equivalent — wrap the reference:
```
[IF4 insurance claims handling assignment help](/if4-assignment-help)
```

---

### 3I — m97-reinsurance-content.md

Append one new link to the existing supplementary bullet list (after line 187):

```markdown
- [993 strategic risk management assignment help](/993-assignment-help) — Advanced Diploma strategic risk unit for candidates progressing from M97 reinsurance content
```

---

### 3J — 820-advanced-claims-content.md

Append two new links to the existing supplementary links block (after the last existing bullet):

```markdown
- [M85 Claims Practice assignment help](/m85-assignment-help) — Diploma-level claims predecessor to 820
- [993 strategic risk management assignment help](/993-assignment-help) — Level 7 unit covering systemic risk and strategic claims governance
```

---

### 3K — 990-insurance-corporate-management-content.md

Append two new links to the existing supplementary section (after line 167):

```markdown
- [820 advanced claims assignment help](/820-assignment-help) — claims governance and Solvency II claims impact
- [960 advanced underwriting assignment help](/960-assignment-help) — underwriting governance and SCR capital framework
```

---

### 3L — 991-london-market-specialisation-content.md

Append two new links to the existing supplementary section (after line 145):

```markdown
- [930 advanced insurance broking assignment help](/930-assignment-help) — Advanced Diploma broking unit for Lloyd's and London market placement professionals
- [994 insurance market specialisation assignment help](/994-assignment-help) — peer Level 7 unit covering specialist insurance markets
```

---

### 3M — 993-strategic-risk-management-content.md

Append three new links to the existing supplementary section (after line 132):

```markdown
- [820 advanced claims assignment help](/820-assignment-help) — strategic claims risk and systemic exposure management
- [960 advanced underwriting assignment help](/960-assignment-help) — underwriting portfolio risk and catastrophe accumulation
- [994 insurance market specialisation assignment help](/994-assignment-help) — peer Level 7 unit for candidates choosing between Level 7 options
```

---

### 3N — cii-certificate-in-insurance-content.md

Append three new links to the existing supplementary section bridge list. After the last existing bridge link in the supplementary section, add:

```markdown
- [M05 Insurance Law assignment help](/m05-assignment-help) — the most studied Diploma unit; Certificate candidates often progress to M05 after completing their IF units
- [GR1 group risk assignment help](/gr1-assignment-help) — specialist Certificate unit covering group life, income protection and critical illness
- [LM3 London market assignment help](/lm3-assignment-help) — specialist Certificate unit for Lloyd's and London market professionals
```

---

### 3O — m05-insurance-law-content.md

Append one new link to the existing supplementary section (after line 187):

```markdown
- [M85 Claims Practice assignment help](/m85-assignment-help) — claims unit that applies M05 proximate cause doctrine and conditions precedent in practice scenarios
```

---

### 3P — m92-insurance-business-finance-content.md

Append two new links to the existing supplementary section (after line 178):

```markdown
- [990 insurance corporate management assignment help](/990-assignment-help) — Advanced Diploma corporate governance unit that builds directly on M92 Solvency II and ORSA content
- [960 advanced underwriting assignment help](/960-assignment-help) — Advanced Diploma underwriting unit applying M92 SCR and capital framework to portfolio strategy
```

---

### 3Q — m80-underwriting-practice-content.md

**Swap recommended** (page is at 5-link budget): Replace the non-functional `/m81-assignment-help` link (no content file exists for M81) with:

Find:
```
[M81 Insurance Broking Practice assignment help](/m81-assignment-help)
```
Replace with:
```
[960 advanced underwriting assignment help](/960-assignment-help)
```

---

### 3R — 930-advanced-insurance-broking-content.md

**Swap recommended** (page is at 5-link budget): Replace the non-functional `/m81-assignment-help` link with M97:

Find:
```
[M81 insurance broking practice assignment help](/m81-assignment-help)
```
Replace with:
```
[M97 reinsurance assignment help](/m97-assignment-help)
```

---

## Verification Checklist

After completing all three phases, run these checks:

### Check 1 — No broken slug variants remain
Search all `written-content/` files for these strings — result should be zero:
- `/cii-advanced-diploma-in-insurance-assignment-help`
- `/cii-diploma-in-insurance-assignment-help`
- `/m80-underwriting-practice-assignment-help`

### Check 2 — No duplicate URLs per page
For each file, list all internal links and confirm no URL appears more than once.

### Check 3 — Zero-link pages resolved
Confirm these 8 files now have at least 2 working internal links each:
- if1, if3, if4, if5, lm3, gr1, imu, wce

### Check 4 — Link budget respected
Confirm no page exceeds 6 total internal links.

### Check 5 — No links into FAQ sections
Confirm no `[text](/slug)` links appear inside `## Frequently Asked Questions` sections.

---

## Post-Launch Note

Two pages are linked from multiple content files but have no content file yet:
- `/m81-assignment-help` — M81 Insurance Broking Practice (referenced from M80, 930)
- `/cii-assignment-help` — CII Assignment Help pillar page (referenced from M80, M85, M97, 930)

Once those pages are published, verify the references are still using the correct slugs.
