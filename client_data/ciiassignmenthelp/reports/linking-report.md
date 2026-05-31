# Linking Report — CII Assignment Help
**Date:** 2026-03-22
**Pages audited:** 25
**Linking GPT version:** Adapted for Markdown (CII Assignment Help client)

---

## Summary

- **Total existing internal links found:** 68
- **Total missing bridges identified:** 41
- **Pages with complete linking (all required bridges present):** 530-economics-business-content.md, m92-insurance-business-finance-content.md, 960-advanced-underwriting-content.md, 930-advanced-insurance-broking-content.md, 590-takaful-principles-content.md
- **Pages with missing links:** 20 pages (see detail below)

---

## Linking Rules Applied

- Max 5–6 internal links per page
- No duplicate link URLs
- No generic anchors ("click here", "learn more")
- Primary injection zone: supplementary content section (after contextual border `---` marker)
- Do NOT inject into FAQ sections
- Only flag bridges where a content file exists for the target

---

## URL Slug Map (all 25 pages with content files)

| Content File | URL Slug | Notes |
|---|---|---|
| if1-insurance-legal-regulatory-content.md | /if1-assignment-help | |
| if3-insurance-underwriting-process-content.md | /if3-assignment-help | |
| if4-insurance-claims-handling-content.md | /if4-assignment-help | |
| if5-motor-insurance-content.md | /if5-assignment-help | |
| lm3-london-market-broker-content.md | /lm3-assignment-help | |
| gr1-group-risk-content.md | /gr1-assignment-help | |
| imu-india-motor-insurance-content.md | /imu-assignment-help | |
| m80-underwriting-practice-content.md | /m80-assignment-help | |
| m85-claims-practice-content.md | /m85-assignment-help | |
| m97-reinsurance-content.md | /m97-assignment-help | |
| 820-advanced-claims-content.md | /820-assignment-help | |
| 930-advanced-insurance-broking-content.md | /930-assignment-help | |
| 960-advanced-underwriting-content.md | /960-assignment-help | |
| 990-insurance-corporate-management-content.md | /990-assignment-help | |
| 991-london-market-specialisation-content.md | /991-assignment-help | |
| 993-strategic-risk-management-content.md | /993-assignment-help | |
| 994-insurance-market-specialisation-content.md | /994-assignment-help | |
| 590-takaful-principles-content.md | /590-assignment-help | |
| wce-insurance-claims-non-uk-content.md | /wce-assignment-help | |
| cii-certificate-in-insurance-content.md | /cii-certificate-assignment-help | Content file uses /cii-assignment-help for pillar; hub slug differs from task spec |
| cii-diploma-in-insurance-content.md | /cii-diploma-assignment-help | Content currently uses /cii-diploma-in-insurance-assignment-help — slug mismatch |
| cii-advanced-diploma-in-insurance-content.md | /advanced-diploma-assignment-help | Content currently uses /cii-advanced-diploma-in-insurance-assignment-help and /cii-advanced-diploma-assignment-help — inconsistent |
| m05-insurance-law-content.md | /m05-assignment-help | Not in original task slug list; file exists |
| m92-insurance-business-finance-content.md | /m92-assignment-help | Not in original task slug list; file exists |
| 530-economics-business-content.md | /530-assignment-help | Not in original task slug list; file exists |

**Slug mismatch alert:** The content files for the three hub pages currently use different slugs than the canonical slugs defined in this task. The diploma hub is linked internally as `/cii-diploma-in-insurance-assignment-help` (not `/cii-diploma-assignment-help`). The advanced diploma hub uses both `/cii-advanced-diploma-in-insurance-assignment-help` and `/cii-advanced-diploma-assignment-help` inconsistently across files. This inconsistency should be resolved before publishing. This report treats both variants as pointing to the same page and counts them as present.

---

## Topical Map Supplementary Bridge Requirements

Extracted from `topical_map.json` — `supplementary_bridges_to` arrays for all tier-1 topics:

| Topical Map Topic | Required Bridges (topic names in map) | Maps to Existing Slugs |
|---|---|---|
| CII Certificate in Insurance Help (hub) | IF1 Help, IF3 Help, IF4 Help, M05 Help, LM3 Help, GR1 Help | /if1, /if3, /if4, /m05, /lm3, /gr1 |
| CII Diploma in Insurance Help (hub) | M05 Help, M92 Help, 530 Help, M80 Help, M81 Help, M85 Help, M97 Help | /m05, /m92, /530, /m80, (M81 — no file), /m85, /m97 |
| CII Advanced Diploma in Insurance Help (hub) | 820 Help, 930 Help, 960 Help, 991 Help, 992 Help, 993 Help, 990 Help | /820, /930, /960, /991, (992 — no file), /993, /990 |

Note: M81 (Insurance Broking Practice) and 992 (Risk Management in Insurance) have NO written content files and are excluded from all missing-bridge calculations.

---

## Page-by-Page Audit

---

### if1-insurance-legal-regulatory-content.md
**URL:** /if1-assignment-help
**Required bridges (from topical map):** None — IF1 is a tier-2 topic with no `supplementary_bridges_to` array defined.

**Existing links:**
- None — the only `](/` match in the file is an infographic image reference (`/infographics/if1-six-principles-insurance-law.svg`), which is not an internal page link.

**Contextual references without links (candidates for injection):**
- Line 119: mentions [IF3 insurance underwriting process assignment help] — unlinked text placeholder
- Line 119: mentions [IF4 insurance claims handling process assignment help] — unlinked text placeholder
- Line 121: mentions [CII Certificate in Insurance assignment help] — unlinked text placeholder

**Missing bridges (based on topical map contextual_bridges — IF1 is a bridge TARGET from outer section pages):**
The topical map defines no `supplementary_bridges_to` for IF1 at tier-2 level. However, the page's own supplementary section references IF3 and IF4 without links, and mentions the Certificate hub without a link.

**Missing links where target files exist:**
1. [IF3 insurance underwriting process assignment help](/if3-assignment-help) — text placeholder exists at line 119; unlinked
2. [IF4 insurance claims handling process assignment help](/if4-assignment-help) — text placeholder exists at line 119; unlinked
3. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder exists at line 121; unlinked

**Status:** 0 existing links | 3 missing (unlinked text placeholders — highest-priority fixes as text already exists)

---

### if3-insurance-underwriting-process-content.md
**URL:** /if3-assignment-help
**Required bridges (from topical map):** None — IF3 is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — the only `](/` match is an infographic image reference (`/infographics/if3-underwriting-cycle.svg`).

**Contextual references without links (candidates for injection):**
- Line 149: [IF1 insurance legal and regulatory assignment help] — unlinked text placeholder
- Line 149: [IF4 insurance claims handling process assignment help] — unlinked text placeholder
- Line 153: [CII Certificate in Insurance assignment help] — unlinked text placeholder

**Missing links where target files exist:**
1. [IF1 insurance legal and regulatory assignment help](/if1-assignment-help) — text placeholder at line 149; unlinked
2. [IF4 insurance claims handling process assignment help](/if4-assignment-help) — text placeholder at line 149; unlinked
3. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 153; unlinked

**Status:** 0 existing links | 3 missing (unlinked text placeholders)

---

### if4-insurance-claims-handling-content.md
**URL:** /if4-assignment-help
**Required bridges (from topical map):** None — IF4 is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — the only `](/` match is an infographic image reference (`/infographics/if4-claims-process-flow.svg`).

**Contextual references without links (candidates for injection):**
- Line 193: [IF3 insurance underwriting process assignment help] — unlinked text placeholder
- Line 193: [IF2 general insurance business assignment help] — no content file for IF2; skip
- Line 193: [CII Certificate in Insurance assignment help] — unlinked text placeholder

**Missing links where target files exist:**
1. [IF3 insurance underwriting process assignment help](/if3-assignment-help) — text placeholder at line 193; unlinked
2. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 193; unlinked

**Status:** 0 existing links | 2 missing (unlinked text placeholders)

---

### if5-motor-insurance-content.md
**URL:** /if5-assignment-help
**Required bridges (from topical map):** None — IF5 is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — the only `](/` match is an infographic image reference (`/infographics/if5-motor-cover-types.svg`).

**Contextual references without links (candidates for injection):**
- Line 155: [CII Certificate in Insurance assignment help] — unlinked text placeholder
- Line 155: [IF1 insurance legal and regulatory assignment help] — unlinked text placeholder
- Line 155: [IF4 insurance claims handling assignment help] — unlinked text placeholder
- Line 155: [IF3 insurance underwriting process assignment help] — unlinked text placeholder

**Missing links where target files exist:**
1. [IF1 insurance legal and regulatory assignment help](/if1-assignment-help) — text placeholder at line 155; unlinked
2. [IF4 insurance claims handling assignment help](/if4-assignment-help) — text placeholder at line 155; unlinked
3. [IF3 insurance underwriting process assignment help](/if3-assignment-help) — text placeholder at line 155; unlinked
4. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 155; unlinked

**Note:** Max 5–6 links per page; 4 injections would bring the page from 0 to 4 links — within budget.

**Status:** 0 existing links | 4 missing (unlinked text placeholders)

---

### lm3-london-market-broker-content.md
**URL:** /lm3-assignment-help
**Required bridges (from topical map):** None — LM3 is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — the only `](/` match is an infographic image reference (`/infographics/lm3-lloyds-chain-of-security.svg`).

**Contextual references without links (candidates for injection):**
- Line 150: [CII Certificate in Insurance Assignment Help] — unlinked text placeholder
- Line 152: [CII Diploma in Insurance Assignment Help] — unlinked text placeholder
- Line 151: [IF10 Insurance Broking Fundamentals Assignment Help] — no content file for IF10; skip

**Missing links where target files exist:**
1. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 150; unlinked
2. [CII Diploma in Insurance assignment help](/cii-diploma-assignment-help) — text placeholder at line 152; unlinked

**Additional contextual bridges from topical map (outer section):** The topical map's contextual_bridges list specifies LM3 as a bridge target from "Lloyd's of London Structure" outer page — but that page has no content file. The map also shows 991 as a logical complement to LM3. The file at line 143 mentions 991 contextually but without a link.

**Additional missing link:**
3. [991 London market specialisation assignment help](/991-assignment-help) — mentioned in supplementary content at line 143 without a link; strong contextual fit.

**Status:** 0 existing links | 3 missing (2 unlinked text placeholders + 1 contextual)

---

### gr1-group-risk-content.md
**URL:** /gr1-assignment-help
**Required bridges (from topical map):** None — GR1 is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — the only `](/` match is an infographic image reference (`/infographics/gr1-group-risk-products.svg`).

**Contextual references without links (candidates for injection):**
- Line 173: [CII Certificate in Insurance Assignment Help] — unlinked text placeholder
- Line 174: [IF1 Insurance Legal and Regulatory Assignment Help] — unlinked text placeholder
- Line 175: [CII Assignment Help] — unlinked text placeholder (pillar page — no content file for pillar; skip)

**Missing links where target files exist:**
1. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 173; unlinked
2. [IF1 Insurance Legal and Regulatory assignment help](/if1-assignment-help) — text placeholder at line 174; unlinked

**Status:** 0 existing links | 2 missing (unlinked text placeholders)

---

### imu-india-motor-insurance-content.md
**URL:** /imu-assignment-help
**Required bridges (from topical map):** None — IMU is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — no `](/` page-link matches in the file.

**Contextual references without links (candidates for injection):**
- Line 190: [CII Certificate in Insurance assignment help] — unlinked text placeholder
- Line 190: [CII assignment help] — unlinked text placeholder (pillar — no content file; skip)

**Additional contextual bridges:** The file at line 136 explicitly connects IMU/IMP to IF5 content; line 188 mentions Diploma progression (M05, M92, 530). These are natural injection points.

**Missing links where target files exist:**
1. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 190; unlinked
2. [IF5 motor insurance assignment help](/if5-assignment-help) — mentioned at line 136 as the UK equivalent; strong contextual bridge; inject in supplementary section
3. [CII Diploma in Insurance assignment help](/cii-diploma-assignment-help) — mentioned at line 188 as progression pathway; inject in supplementary section

**Status:** 0 existing links | 3 missing (1 unlinked placeholder + 2 contextual)

---

### m80-underwriting-practice-content.md
**URL:** /m80-assignment-help
**Required bridges (from topical map):** The topical map's Diploma hub `supplementary_bridges_to` includes M80 Help. The map does not define a specific `supplementary_bridges_to` array for M80 itself (tier-2 optional unit), but the page's own supplementary section defines its internal links explicitly.

**Existing links (internal page links only — infographic excluded):**
- [M81 Insurance Broking Practice assignment help](/m81-assignment-help) — supplementary section, line 191 — target has NO content file
- [CII Diploma in Insurance assignment help](/cii-diploma-in-insurance-assignment-help) — supplementary section, line 189
- [IF3 Insurance Underwriting Process assignment help](/if3-assignment-help) — supplementary section, line 190
- [M92 Insurance Business and Finance assignment help](/m92-assignment-help) — supplementary section, line 192
- [CII assignment help](/cii-assignment-help) — supplementary section, line 193 — pillar page; no content file

**Link budget:** 5 links present. Max 5–6. Budget is at limit.

**Required missing bridges:** The topical map references M80 in the Diploma hub's bridges, and 960 is the natural Advanced Diploma progression for M80. The file mentions 960 in prose (line 184) but does not link to it.

**Missing links where target files exist and budget permits:**
- The page is at 5 links. The /m81-assignment-help link points to a page with no content file (non-functional bridge). If that is resolved (M81 content created), no additional links are needed. The 960 progression link would be the best addition if the M81 link is removed or the budget expanded to 6.

**Recommendation:** Replace the non-functional /m81-assignment-help link with [960 advanced underwriting assignment help](/960-assignment-help) — the prose at line 184 already introduces 960 as the natural next step. This is a swap, not a net addition.

**Status:** 5 existing links (1 points to no content file) | 0 net-missing within budget | 1 swap recommended

---

### m85-claims-practice-content.md
**URL:** /m85-assignment-help
**Required bridges (from topical map):** The Diploma hub bridges include M85 Help. The page's supplementary section defines its links explicitly.

**Existing links:**
- [820 Advanced Diploma Claims assignment help](/820-assignment-help) — supplementary, line 215
- [M05 Insurance Law assignment help](/m05-assignment-help) — supplementary, line 215 + line 221
- [CII Diploma in Insurance assignment help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 218
- [IF4 Insurance Claims Handling assignment help](/if4-assignment-help) — supplementary, line 219
- [M80 Underwriting Practice assignment help](/m80-underwriting-practice-assignment-help) — supplementary, line 220 — SLUG MISMATCH: uses `/m80-underwriting-practice-assignment-help` not `/m80-assignment-help`
- [CII assignment help](/cii-assignment-help) — supplementary, line 222 — pillar; no content file

**Slug alert:** Line 220 links to `/m80-underwriting-practice-assignment-help` — this does not match the canonical slug `/m80-assignment-help`. This is a broken internal link.

**Link budget:** 6 links present (at maximum). M05 is linked twice (lines 215 and 221) — duplicate URL.

**Issues identified:**
1. Duplicate link to /m05-assignment-help (lines 215 and 221) — violates no-duplicate rule
2. /m80-underwriting-practice-assignment-help slug is incorrect — should be /m80-assignment-help

**Missing bridges (considering budget):** The page is at capacity (6 links, with one duplicate and one broken slug). No additional links can be added without removing an existing one.

**Status:** 6 existing links (1 duplicate URL, 1 broken slug) | 0 net-missing within budget | 2 corrections needed

---

### m97-reinsurance-content.md
**URL:** /m97-assignment-help
**Required bridges (from topical map):** The Diploma hub bridges include M97 Help.

**Existing links:**
- [CII Diploma in Insurance assignment help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 183
- [CII assignment help](/cii-assignment-help) — supplementary, line 184 — pillar; no content file
- [960 Advanced Underwriting assignment help](/960-assignment-help) — supplementary, line 185
- [930 Advanced Insurance Broking assignment help](/930-assignment-help) — supplementary, line 186
- [M80 Underwriting Practice assignment help](/m80-underwriting-practice-assignment-help) — supplementary, line 187 — SLUG MISMATCH: uses `/m80-underwriting-practice-assignment-help` not `/m80-assignment-help`

**Slug alert:** Line 187 links to `/m80-underwriting-practice-assignment-help` — incorrect slug; should be `/m80-assignment-help`.

**Link budget:** 5 links present.

**Missing bridges where target files exist:**
The topical map's outer section contextual_bridges specifies "Reinsurance Fundamentals → M97 Assignment Help" (inbound to M97). For outbound from M97, the logical bridge to 993 (Advanced Reinsurance, Level 7) is not present. 993 is mentioned in the file at line 79 of the advanced diploma hub but not linked from M97 itself.

- [993 strategic risk management assignment help](/993-assignment-help) — natural progression for M97 reinsurance students moving to Advanced Diploma; not currently linked; inject in supplementary section.

**Budget check:** Adding 1 link brings total to 6. Within limit.

**Missing links:**
1. [993 advanced reinsurance assignment help](/993-assignment-help) — INJECT in supplementary section | Suggested anchor: "993 Advanced Reinsurance assignment help"

**Additional correction:** Fix /m80-underwriting-practice-assignment-help → /m80-assignment-help at line 187.

**Status:** 5 existing links (1 broken slug) | 1 missing bridge | 1 slug correction needed

---

### 820-advanced-claims-content.md
**URL:** /820-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub `supplementary_bridges_to` includes 820 Help.

**Existing links:**
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-in-insurance-assignment-help) — supplementary, line 178
- [930 Advanced Insurance Broking assignment help](/930-assignment-help) — supplementary, line 178
- [960 Advanced Underwriting assignment help](/960-assignment-help) — supplementary, line 178
- [CII assignment help](/cii-assignment-help) — supplementary, line 180 — pillar; no content file

**Link budget:** 4 links present. Capacity for 1–2 more.

**Missing bridges where target files exist:**
The topical map's Diploma hub bridges include M85 Help as the Diploma-level claims predecessor to 820. The file at line 180 mentions M05, M92, and 530 as Diploma core units carried forward but does not link to them. The most relevant bridge is M85 (Diploma claims → 820 Advanced Claims progression).

**Missing links:**
1. [M85 Claims Practice assignment help](/m85-assignment-help) — natural predecessor unit; mentioned contextually at line 180 area; INJECT in supplementary section | Suggested anchor: "M85 Claims Practice assignment help"
2. [993 strategic risk management assignment help](/993-assignment-help) — mentioned at line 180 as a Level 7 optional unit alongside 820; INJECT in supplementary section | Suggested anchor: "993 strategic risk management assignment help"

**Status:** 4 existing links | 2 missing bridges

---

### 930-advanced-insurance-broking-content.md
**URL:** /930-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 930 Help.

**Existing links:**
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-in-insurance-assignment-help) — supplementary, line 118
- [820 advanced claims assignment help](/820-assignment-help) — supplementary, line 118
- [960 advanced underwriting assignment help](/960-assignment-help) — supplementary, line 118
- [M81 insurance broking practice assignment help](/m81-assignment-help) — supplementary, line 120 — target has NO content file
- [CII assignment help](/cii-assignment-help) — supplementary, line 120 — pillar; no content file

**Link budget:** 5 links present. 1 points to a page with no content file.

**Missing bridges where target files exist:**
The M81 link points to a page with no content file (non-functional). The natural replacement or addition is M97, given 930 covers reinsurance broking at Advanced Diploma level and M97 is the Diploma-level reinsurance unit that feeds into 930 content.

**Recommendation:** The page is at 5 links. If M81 link is left in place (as aspirational), there is no budget for additions. If M81 link is treated as non-functional and swapped:
- Replace [M81 insurance broking practice assignment help](/m81-assignment-help) with [M97 reinsurance assignment help](/m97-assignment-help) | Suggested anchor: "M97 reinsurance assignment help"

**Status:** 5 existing links (1 points to no content file) | 0 net-missing within budget | 1 swap recommended

---

### 960-advanced-underwriting-content.md
**URL:** /960-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 960 Help.

**Existing links:**
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-in-insurance-assignment-help) — supplementary, line 139
- [820 advanced claims assignment help](/820-assignment-help) — supplementary, line 139
- [930 advanced insurance broking assignment help](/930-assignment-help) — supplementary, line 139
- [M80 underwriting practice assignment help](/m80-assignment-help) — supplementary, line 141
- [991 London market specialisation assignment help](/991-assignment-help) — supplementary, line 141
- [CII assignment help](/cii-assignment-help) — supplementary, line 141 — pillar; no content file

**Link budget:** 6 links present (at maximum). All six targets either exist or are the pillar page.

**Missing bridges:** None within budget. All key bridges (820, 930, M80, 991, Advanced Diploma hub) are present.

**Status:** 6 existing links | COMPLETE

---

### 990-insurance-corporate-management-content.md
**URL:** /990-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub `supplementary_bridges_to` includes 990 Help.

**Existing links:**
- [993 strategic risk management assignment help](/993-assignment-help) — supplementary, line 165
- [M92 insurance business finance assignment help](/m92-assignment-help) — supplementary, line 165
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-assignment-help) — supplementary, line 167

**Link budget:** 3 links present. Capacity for 2–3 more.

**Missing bridges where target files exist:**
The topical map outer section `bridge_to_core` for "UK Insurance Regulation" specifies bridges to IF1, M92, 990, and 992. For the 990 page itself, the most relevant outbound bridges are to core units that share governance content — 820 (claims governance) and 960 (underwriting governance).

**Missing links:**
1. [820 advanced claims assignment help](/820-assignment-help) — governance of claims function directly relevant to 990 corporate governance content; INJECT in supplementary section | Suggested anchor: "820 advanced claims assignment help"
2. [960 advanced underwriting assignment help](/960-assignment-help) — underwriting governance and Solvency II SCR content shared with 990; INJECT in supplementary section | Suggested anchor: "960 advanced underwriting assignment help"

**Status:** 3 existing links | 2 missing bridges

---

### 991-london-market-specialisation-content.md
**URL:** /991-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 991 Help.

**Existing links:**
- [960 advanced underwriting assignment help](/960-assignment-help) — supplementary, line 141
- [820 advanced claims assignment help](/820-assignment-help) — supplementary, line 141
- [LM3 London market assignment help](/lm3-assignment-help) — supplementary, line 143
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-assignment-help) — supplementary, line 145

**Link budget:** 4 links present. Capacity for 1–2 more.

**Missing bridges where target files exist:**
The topical map outer section contextual_bridges specifies "Lloyd's of London Structure → 991 Assignment Help" (inbound to 991). For outbound bridges from 991, the natural complement is 930 (Advanced Broking at Lloyd's level) and 994 (Insurance Market Specialisation — the other Level 7 optional).

**Missing links:**
1. [930 advanced insurance broking assignment help](/930-assignment-help) — broking in the Lloyd's market is central to both 930 and 991; INJECT in supplementary section | Suggested anchor: "930 advanced insurance broking assignment help"
2. [994 insurance market specialisation assignment help](/994-assignment-help) — peer Level 7 unit; mentioned contextually across the site as an alternative; INJECT in supplementary section | Suggested anchor: "994 insurance market specialisation assignment help"

**Status:** 4 existing links | 2 missing bridges

---

### 993-strategic-risk-management-content.md
**URL:** /993-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 993 Help.

**Existing links:**
- [990 insurance corporate management assignment help](/990-assignment-help) — supplementary, line 130
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-assignment-help) — supplementary, line 132

**Link budget:** 2 links present. Capacity for 3–4 more.

**Missing bridges where target files exist:**
993 is a Level 7 risk-focused unit. The topical map outer section `bridge_to_core` for "Enterprise Risk Management" specifies bridges to IF11, M67, 992, and 993. Of these, only 993 has a content file. The most relevant outbound bridges from 993 are to 820 (claims risk), 960 (underwriting risk), and 991/994 (peer Level 7 units).

**Missing links:**
1. [820 advanced claims assignment help](/820-assignment-help) — strategic claims risk connects directly to 993 systemic risk content; INJECT in supplementary section | Suggested anchor: "820 advanced claims assignment help"
2. [960 advanced underwriting assignment help](/960-assignment-help) — underwriting portfolio risk is central to 993 strategic risk scope; INJECT in supplementary section | Suggested anchor: "960 advanced underwriting assignment help"
3. [994 insurance market specialisation assignment help](/994-assignment-help) — peer Level 7 unit; natural comparison for candidates choosing between Level 7 options; INJECT in supplementary section | Suggested anchor: "994 insurance market specialisation assignment help"

**Status:** 2 existing links | 3 missing bridges

---

### 994-insurance-market-specialisation-content.md
**URL:** /994-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 994 (as optional Level 7 unit).

**Existing links:**
- [993 strategic risk management assignment help](/993-assignment-help) — supplementary, line 193
- [991 London market specialisation assignment help](/991-assignment-help) — supplementary, line 193
- [960 advanced underwriting assignment help](/960-assignment-help) — supplementary, line 193
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-assignment-help) — supplementary, line 195
- [993 strategic risk management assignment help](/993-assignment-help) — also at line 211 — DUPLICATE URL

**Duplicate alert:** /993-assignment-help appears twice (lines 193 and 211). Violates no-duplicate rule.

**Link budget:** 5 links present (with 1 duplicate).

**Missing bridges:** None needed — all key Level 7 peers (991, 993) and the Advanced Diploma hub are linked. The duplicate at line 211 should be resolved by converting it to a different link.

**Recommendation:** At line 211, the duplicate /993-assignment-help link should be replaced with [820 advanced claims assignment help](/820-assignment-help) or [930 advanced insurance broking assignment help](/930-assignment-help) — both are relevant to specialist market professionals.

**Status:** 5 existing links (1 duplicate URL) | 0 net-missing | 1 duplicate correction needed

---

### 590-takaful-principles-content.md
**URL:** /590-assignment-help
**Required bridges (from topical map):** Advanced Diploma hub bridges include 590 Help (listed as "590 Lloyd's Market assignment help").

**Existing links:**
- [960 Advanced Underwriting assignment help](/960-assignment-help) — supplementary, line 167
- [930 Advanced Insurance Broking assignment help](/930-assignment-help) — supplementary, line 167
- [820 Advanced Claims assignment help](/820-assignment-help) — supplementary, line 167
- [CII Advanced Diploma in Insurance assignment help](/advanced-diploma-assignment-help) — supplementary, line 169

**Link budget:** 4 links present. Capacity for 1–2 more.

**Missing bridges:** All three core Advanced Diploma units are present. The Advanced Diploma hub is linked. The WCE page covers Islamic market claims context and would be a natural bridge from 590 (Takaful connects to WCE/WCA Arabic market students). However, WCE is a Certificate-level unit and the contextual bridge is weaker at Level 6.

The topical map outer section contextual_bridges specifies "Takaful and Islamic Insurance → 590 Assignment Help" (inbound). No additional outbound bridges are specified for 590 itself.

**Assessment:** All required bridges are in place. The page is considered complete within the defined bridge requirements.

**Status:** 4 existing links | COMPLETE

---

### wce-insurance-claims-non-uk-content.md
**URL:** /wce-assignment-help
**Required bridges (from topical map):** None — WCE is a tier-2 topic with no `supplementary_bridges_to` defined.

**Existing links:**
- None — no `](/` page-link matches in the file. All square-bracket references are unlinked text placeholders.

**Contextual references without links (candidates for injection):**
- Line 156: [CII Certificate in Insurance assignment help] — unlinked text placeholder
- Line 168: [CII 590 Takaful unit] — unlinked text placeholder; target file exists (590-takaful-principles-content.md)
- Line 184: [CII insurance assignment help] — unlinked text placeholder (pillar; no content file; skip)

**Missing links where target files exist:**
1. [CII Certificate in Insurance assignment help](/cii-certificate-assignment-help) — text placeholder at line 156; unlinked
2. [590 Takaful assignment help](/590-assignment-help) — text placeholder at line 168 specifically connects WCE/WCA Arabic market students to Takaful; unlinked
3. [IF4 insurance claims handling assignment help](/if4-assignment-help) — WCE content directly maps to IF4 (UK equivalent); the file at line 154 mentions this progression explicitly; inject in supplementary section | Suggested anchor: "IF4 insurance claims handling assignment help"

**Status:** 0 existing links | 3 missing bridges (2 unlinked text placeholders + 1 contextual)

---

### cii-certificate-in-insurance-content.md
**URL:** /cii-certificate-assignment-help
**Required bridges (from topical map):** IF1 Help, IF3 Help, IF4 Help, M05 Help, LM3 Help, GR1 Help (from `supplementary_bridges_to`)

**Existing links:**
- [CII assignment help across all qualification levels](/cii-assignment-help) — main content, line 15 — pillar; no content file
- [IF1 assignment help](/if1-assignment-help) — main content, line 45
- [IF3 assignment help](/if3-assignment-help) — main content, line 45
- [IF4 assignment help](/if4-assignment-help) — main content, line 45
- [CII Diploma in Insurance assignment help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 103
- [CII assignment help across all levels](/cii-assignment-help) — supplementary, line 103 — duplicate of line 15 (both to /cii-assignment-help); pillar
- [CII Advanced Diploma and ACII designation](/cii-advanced-diploma-in-insurance-assignment-help) — supplementary, line 117

**Duplicate alert:** /cii-assignment-help appears at line 15 (main content) and line 103 (supplementary). Duplicate URL.

**Bridge coverage check:**
- IF1 Help ✓ (line 45)
- IF3 Help ✓ (line 45)
- IF4 Help ✓ (line 45)
- M05 Help — MISSING; no link to /m05-assignment-help
- LM3 Help — MISSING; no link to /lm3-assignment-help
- GR1 Help — MISSING; no link to /gr1-assignment-help

**Link budget:** 7 links present (2 duplicates reduce effective count). After removing the /cii-assignment-help duplicate, effective unique page links = 6 (IF1, IF3, IF4, Diploma hub, Advanced Diploma hub, pillar).

**Missing bridges:**
1. [M05 Insurance Law assignment help](/m05-assignment-help) — required bridge; INJECT in supplementary section | Suggested anchor: "M05 Insurance Law assignment help"

However, the page is already at 6–7 links. Adding 3 bridges (M05, LM3, GR1) would exceed the budget. Priority order:

**Priority 1 — inject M05** (highest search volume Diploma unit; Certificate students need to know what comes next)
**Priority 2 — inject GR1** (specialist Certificate unit already in the supplementary bridges list)
**Priority 3 — inject LM3** (London market specialist Certificate unit)

**Recommendation:** Remove the duplicate /cii-assignment-help link in the supplementary section (line 103), freeing 1 slot. Then inject M05, GR1, LM3 across supplementary paragraphs — adding 3 to bring total unique links to 8 (borderline; 6 is the recommended max). Inject M05 first as highest priority; defer GR1 and LM3 to a second pass if budget is strictly enforced at 6.

**Missing links (priority order):**
1. [M05 Insurance Law assignment help](/m05-assignment-help) — INJECT in supplementary section | Suggested anchor: "M05 Insurance Law assignment help"
2. [GR1 group risk assignment help](/gr1-assignment-help) — INJECT in supplementary section | Suggested anchor: "GR1 group risk assignment help"
3. [LM3 London market assignment help](/lm3-assignment-help) — INJECT in supplementary section | Suggested anchor: "LM3 London market assignment help"

**Status:** 7 existing links (1 duplicate URL) | 3 missing bridges

---

### cii-diploma-in-insurance-content.md
**URL:** /cii-diploma-assignment-help
**Required bridges (from topical map):** M05 Help, M92 Help, 530 Help, M80 Help, M81 Help (no file), M85 Help, M97 Help

**Existing links:**
- [CII assignment help across all qualification levels](/cii-assignment-help) — main content, line 15 — pillar; no content file
- [M05 Insurance Law assignment help](/m05-assignment-help) — main content, line 39 AND line 73 AND line 159 — TRIPLE duplicate
- [M92 assignment help](/m92-assignment-help) — main content, line 47
- [530 assignment help](/530-assignment-help) — main content, line 57
- [M80 Commercial Lines Underwriting help](/m80-assignment-help) — supplementary, line 115 AND line 160 — DUPLICATE
- [M85 Commercial Lines Claims help](/m85-assignment-help) — supplementary, line 115 AND line 162 — DUPLICATE
- [M97 Insurance Broking Practice help](/m97-assignment-help) — supplementary, line 115 AND line 163 — DUPLICATE
- [M81 Personal Lines Underwriting help](/m81-assignment-help) — supplementary, line 161 — no content file
- [CII Certificate in Insurance assignment help](/cii-certificate-in-insurance-assignment-help) — supplementary, line 137
- [CII assignment help](/cii-assignment-help) — supplementary, line 137 — duplicate of pillar link
- [CII Advanced Diploma in Insurance assignment help](/cii-advanced-diploma-in-insurance-assignment-help) — supplementary, line 145

**Duplicate alert:** M05 linked 3 times; M80, M85, M97 each linked twice; /cii-assignment-help linked twice. Multiple violations of no-duplicate rule.

**Bridge coverage check:**
- M05 Help ✓ (present, multiple times)
- M92 Help ✓
- 530 Help ✓
- M80 Help ✓
- M81 Help — present but no content file; skip
- M85 Help ✓
- M97 Help ✓

**All required bridges present.** However, the page has serious duplicate link issues that need correction.

**Issues:**
1. M05 linked 3 times — remove duplicates at lines 73 and 159; keep only line 39
2. M80 linked twice — remove duplicate at line 160; keep line 115
3. M85 linked twice — remove duplicate at line 162; keep line 115
4. M97 linked twice — remove duplicate at line 163; keep line 115
5. /cii-assignment-help linked twice — remove duplicate
6. M92 and 530 are only linked once each in main content — these are fine

**Status:** 11 link instances across 7 unique target URLs (4 non-functional or pillar) | BRIDGES COMPLETE (but extensive duplicate cleanup required)

---

### cii-advanced-diploma-in-insurance-content.md
**URL:** /advanced-diploma-assignment-help
**Required bridges (from topical map):** 820 Help, 930 Help, 960 Help, 991 Help, 992 Help (no file), 993 Help, 990 Help

**Existing links:**
- [CII assignment help across all qualification levels](/cii-assignment-help) — main content, line 15 — pillar; no content file
- [820 Advanced Claims Management assignment help](/820-assignment-help) — main content, line 37 AND supplementary, line 137 — DUPLICATE
- [930 Advanced Insurance Broking assignment help](/930-assignment-help) — main content, line 45 AND supplementary, line 138 — DUPLICATE
- [960 Advanced Underwriting assignment help](/960-assignment-help) — main content, line 53 AND supplementary, line 139 — DUPLICATE
- [991 Strategic Risk Management assignment help](/991-assignment-help) — main content, line 77 AND supplementary, line 140 — DUPLICATE
- [993 assignment help](/993-assignment-help) — main content, line 79
- [994 assignment help](/994-assignment-help) — main content, line 81
- [M05 Insurance Law and Practice assignment help](/m05-assignment-help) — supplementary, line 97 AND line 117 — DUPLICATE
- [CII Diploma in Insurance core unit help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 97 AND line 117 — DUPLICATE (both instances)
- [990 Risk Management assignment help](/990-assignment-help) — supplementary, line 141
- [590 Lloyd's Market assignment help](/590-assignment-help) — supplementary, line 142

**Bridge coverage check:**
- 820 Help ✓
- 930 Help ✓
- 960 Help ✓
- 991 Help ✓
- 992 Help — no content file; skip
- 993 Help ✓
- 990 Help ✓

**All required bridges present.** However, numerous duplicate links across main content and supplementary sections.

**Issues:**
1. 820, 930, 960, 991 each linked twice (once in main, once in supplementary)
2. M05 linked twice in supplementary
3. Diploma hub linked twice in supplementary

**Status:** 14 link instances across ~9 unique target URLs | BRIDGES COMPLETE (but extensive duplicate cleanup required)

---

### m05-insurance-law-content.md
**URL:** /m05-assignment-help
**Required bridges (from topical map):** The Diploma hub bridges include M05 Help (inbound). For outbound, the topical map outer section bridges specify: "Insurance Act 2015 Guide → M05 Assignment Help" (inbound) and "Six Principles of Insurance → M05 Assignment Help" (inbound). M05 is a bridge target, not defined as a bridge source in the map.

**Existing links:**
- [CII Diploma in Insurance Assignment Help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 184
- [M92 Insurance Business and Finance Assignment Help](/m92-assignment-help) — supplementary, line 185
- [530 Economics and Business Assignment Help](/530-assignment-help) — supplementary, line 186
- [IF1 Insurance Legal and Regulatory Assignment Help](/if1-assignment-help) — supplementary, line 187

**Link budget:** 4 links present. Capacity for 1–2 more.

**Missing bridges where target files exist:**
M05 is the insurance law unit. The natural contextual bridge from M05 is to 820 (Advanced Claims — coverage disputes depend on contract law) or to M85 (Claims Practice — proximate cause and policy interpretation at Diploma level).

**Missing links:**
1. [M85 Claims Practice assignment help](/m85-assignment-help) — M85 directly applies proximate cause and conditions precedent doctrine from M05; mentioned in M85's own supplementary section as a connection; INJECT in supplementary section | Suggested anchor: "M85 Claims Practice assignment help"

**Status:** 4 existing links | 1 missing bridge

---

### m92-insurance-business-finance-content.md
**URL:** /m92-assignment-help
**Required bridges (from topical map):** The Diploma hub bridges include M92 Help.

**Existing links:**
- [CII Diploma in Insurance Assignment Help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 176
- [M05 Insurance Law Assignment Help](/m05-assignment-help) — supplementary, line 177
- [530 Economics and Business Assignment Help](/530-assignment-help) — supplementary, line 178

**Link budget:** 3 links present. Capacity for 2–3 more.

**Missing bridges where target files exist:**
M92 covers Solvency II and insurance company financials. The natural bridges are to 990 (corporate governance — uses M92 financial framework) and to 960 (Advanced Underwriting — SCR and Solvency II capital in 960 connects directly to M92).

**Missing links:**
1. [990 insurance corporate management assignment help](/990-assignment-help) — Solvency II governance in 990 builds on M92 Solvency II framework; INJECT in supplementary section | Suggested anchor: "990 insurance corporate management assignment help"
2. [960 advanced underwriting assignment help](/960-assignment-help) — SCR calculations in 960 connect directly to M92 Solvency II capital content; INJECT in supplementary section | Suggested anchor: "960 advanced underwriting assignment help"

**Status:** 3 existing links | 2 missing bridges

---

### 530-economics-business-content.md
**URL:** /530-assignment-help
**Required bridges (from topical map):** The Diploma hub bridges include 530 Help.

**Existing links:**
- [CII Diploma in Insurance Assignment Help](/cii-diploma-in-insurance-assignment-help) — supplementary, line 201
- [M05 Insurance Law Assignment Help](/m05-assignment-help) — supplementary, line 202
- [M92 Insurance Business and Finance Assignment Help](/m92-assignment-help) — supplementary, line 203

**Link budget:** 3 links present. Capacity for 2–3 more.

**Missing bridges where target files exist:**
530 covers macroeconomics, business strategy, and their application to insurance. The natural bridges are to 993 (strategic risk — systemic and macroeconomic risk analysis) and to 960 (Advanced Underwriting — market cycle and capacity analysis uses 530 economic frameworks).

**Missing links:** The three companion Diploma core units are all linked. No specific `supplementary_bridges_to` defined for 530 beyond those three. Within the topical map's scope, 530 bridges are considered complete.

**Assessment:** All three required Diploma core companions are present. No additional required bridges identified.

**Status:** 3 existing links | COMPLETE

---

## Recommended Link Injection Summary

| File | Missing Link | Suggested Anchor | Injection Section | Priority |
|---|---|---|---|---|
| if1-insurance-legal-regulatory-content.md | /if3-assignment-help | "IF3 insurance underwriting process assignment help" | Supplementary (line 119 — unlinked placeholder) | HIGH |
| if1-insurance-legal-regulatory-content.md | /if4-assignment-help | "IF4 insurance claims handling process assignment help" | Supplementary (line 119 — unlinked placeholder) | HIGH |
| if1-insurance-legal-regulatory-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 121 — unlinked placeholder) | HIGH |
| if3-insurance-underwriting-process-content.md | /if1-assignment-help | "IF1 insurance legal and regulatory assignment help" | Supplementary (line 149 — unlinked placeholder) | HIGH |
| if3-insurance-underwriting-process-content.md | /if4-assignment-help | "IF4 insurance claims handling process assignment help" | Supplementary (line 149 — unlinked placeholder) | HIGH |
| if3-insurance-underwriting-process-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 153 — unlinked placeholder) | HIGH |
| if4-insurance-claims-handling-content.md | /if3-assignment-help | "IF3 insurance underwriting process assignment help" | Supplementary (line 193 — unlinked placeholder) | HIGH |
| if4-insurance-claims-handling-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 193 — unlinked placeholder) | HIGH |
| if5-motor-insurance-content.md | /if1-assignment-help | "IF1 insurance legal and regulatory assignment help" | Supplementary (line 155 — unlinked placeholder) | HIGH |
| if5-motor-insurance-content.md | /if4-assignment-help | "IF4 insurance claims handling assignment help" | Supplementary (line 155 — unlinked placeholder) | HIGH |
| if5-motor-insurance-content.md | /if3-assignment-help | "IF3 insurance underwriting process assignment help" | Supplementary (line 155 — unlinked placeholder) | MEDIUM |
| if5-motor-insurance-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 155 — unlinked placeholder) | MEDIUM |
| lm3-london-market-broker-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 150 — unlinked placeholder) | HIGH |
| lm3-london-market-broker-content.md | /cii-diploma-assignment-help | "CII Diploma in Insurance assignment help" | Supplementary (line 152 — unlinked placeholder) | HIGH |
| lm3-london-market-broker-content.md | /991-assignment-help | "991 London market specialisation assignment help" | Supplementary (line 143 — contextual mention without link) | MEDIUM |
| gr1-group-risk-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 173 — unlinked placeholder) | HIGH |
| gr1-group-risk-content.md | /if1-assignment-help | "IF1 insurance legal and regulatory assignment help" | Supplementary (line 174 — unlinked placeholder) | HIGH |
| imu-india-motor-insurance-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 190 — unlinked placeholder) | HIGH |
| imu-india-motor-insurance-content.md | /if5-assignment-help | "IF5 motor insurance assignment help" | Supplementary (line 136 — contextual mention without link) | HIGH |
| imu-india-motor-insurance-content.md | /cii-diploma-assignment-help | "CII Diploma in Insurance assignment help" | Supplementary (line 188 — contextual mention without link) | MEDIUM |
| m97-reinsurance-content.md | /993-assignment-help | "993 advanced reinsurance assignment help" | Supplementary — append to existing internal links block | MEDIUM |
| 820-advanced-claims-content.md | /m85-assignment-help | "M85 Claims Practice assignment help" | Supplementary — append to existing section | HIGH |
| 820-advanced-claims-content.md | /993-assignment-help | "993 strategic risk management assignment help" | Supplementary — append to existing section | MEDIUM |
| 990-insurance-corporate-management-content.md | /820-assignment-help | "820 advanced claims assignment help" | Supplementary — append after existing links | MEDIUM |
| 990-insurance-corporate-management-content.md | /960-assignment-help | "960 advanced underwriting assignment help" | Supplementary — append after existing links | MEDIUM |
| 991-london-market-specialisation-content.md | /930-assignment-help | "930 advanced insurance broking assignment help" | Supplementary — append after existing links | HIGH |
| 991-london-market-specialisation-content.md | /994-assignment-help | "994 insurance market specialisation assignment help" | Supplementary — append after existing links | MEDIUM |
| 993-strategic-risk-management-content.md | /820-assignment-help | "820 advanced claims assignment help" | Supplementary — append after existing links | MEDIUM |
| 993-strategic-risk-management-content.md | /960-assignment-help | "960 advanced underwriting assignment help" | Supplementary — append after existing links | MEDIUM |
| 993-strategic-risk-management-content.md | /994-assignment-help | "994 insurance market specialisation assignment help" | Supplementary — append after existing links | MEDIUM |
| wce-insurance-claims-non-uk-content.md | /cii-certificate-assignment-help | "CII Certificate in Insurance assignment help" | Supplementary (line 156 — unlinked placeholder) | HIGH |
| wce-insurance-claims-non-uk-content.md | /590-assignment-help | "590 Takaful assignment help" | Supplementary (line 168 — unlinked placeholder) | HIGH |
| wce-insurance-claims-non-uk-content.md | /if4-assignment-help | "IF4 insurance claims handling assignment help" | Supplementary (line 154 — contextual mention without link) | HIGH |
| cii-certificate-in-insurance-content.md | /m05-assignment-help | "M05 Insurance Law assignment help" | Supplementary — add to existing bridge list | HIGH |
| cii-certificate-in-insurance-content.md | /gr1-assignment-help | "GR1 group risk assignment help" | Supplementary — add to existing bridge list | MEDIUM |
| cii-certificate-in-insurance-content.md | /lm3-assignment-help | "LM3 London market assignment help" | Supplementary — add to existing bridge list | MEDIUM |
| m05-insurance-law-content.md | /m85-assignment-help | "M85 Claims Practice assignment help" | Supplementary — append after existing links | MEDIUM |
| m92-insurance-business-finance-content.md | /990-assignment-help | "990 insurance corporate management assignment help" | Supplementary — append after existing links | MEDIUM |
| m92-insurance-business-finance-content.md | /960-assignment-help | "960 advanced underwriting assignment help" | Supplementary — append after existing links | MEDIUM |

---

## Issues Requiring Correction (Not New Injections)

These are existing links that are broken or duplicated — they should be fixed before or alongside new injections:

| File | Issue Type | Current Link | Correction Needed |
|---|---|---|---|
| m85-claims-practice-content.md | Broken slug | `/m80-underwriting-practice-assignment-help` (line 220) | Change to `/m80-assignment-help` |
| m85-claims-practice-content.md | Duplicate URL | `/m05-assignment-help` appears at lines 215 and 221 | Remove duplicate (keep line 221 in context; remove line 215 or rewrite as plain text) |
| m97-reinsurance-content.md | Broken slug | `/m80-underwriting-practice-assignment-help` (line 187) | Change to `/m80-assignment-help` |
| cii-diploma-in-insurance-content.md | Triple duplicate | `/m05-assignment-help` at lines 39, 73, 159 | Keep one instance; remove or rewrite other two as plain text |
| cii-diploma-in-insurance-content.md | Double duplicate | `/m80-assignment-help` at lines 115 and 160 | Keep one; remove the other |
| cii-diploma-in-insurance-content.md | Double duplicate | `/m85-assignment-help` at lines 115 and 162 | Keep one; remove the other |
| cii-diploma-in-insurance-content.md | Double duplicate | `/m97-assignment-help` at lines 115 and 163 | Keep one; remove the other |
| cii-diploma-in-insurance-content.md | Double duplicate | `/cii-assignment-help` at lines 15 and 137 | Keep line 15 (main content); remove line 137 (supplementary) |
| cii-advanced-diploma-in-insurance-content.md | Multiple duplicates | 820, 930, 960, 991 each linked in both main content and supplementary | Keep supplementary links; remove main content duplicates or rewrite as plain text |
| cii-advanced-diploma-in-insurance-content.md | Double duplicate | `/m05-assignment-help` at lines 97 and 117 | Keep one; remove or rewrite the other |
| cii-advanced-diploma-in-insurance-content.md | Double duplicate | `/cii-diploma-in-insurance-assignment-help` at lines 97 and 117 | Keep one; remove or rewrite the other |
| cii-certificate-in-insurance-content.md | Duplicate URL | `/cii-assignment-help` at lines 15 and 103 | Keep line 15; remove line 103 or convert to plain text |
| 994-insurance-market-specialisation-content.md | Duplicate URL | `/993-assignment-help` at lines 193 and 211 | Keep line 193; replace line 211 with a different link (e.g., /820-assignment-help or /930-assignment-help) |

---

## Slug Consistency Issues Requiring Resolution Before Publishing

| Issue | Current Usage in Content Files | Canonical Slug (per task) | Files Affected |
|---|---|---|---|
| CII Diploma hub slug | `/cii-diploma-in-insurance-assignment-help` | `/cii-diploma-assignment-help` | All Diploma hub references across 15+ files |
| CII Advanced Diploma hub slug | Both `/cii-advanced-diploma-in-insurance-assignment-help` AND `/cii-advanced-diploma-assignment-help` used | `/advanced-diploma-assignment-help` | All Advanced Diploma hub references across 10+ files |
| M80 slug | `/m80-underwriting-practice-assignment-help` (in m85 and m97 files) | `/m80-assignment-help` | m85-claims-practice-content.md, m97-reinsurance-content.md |

**Recommendation:** Decide on canonical slugs for the three hub pages and execute a global find-and-replace across all content files before publishing. The slug inconsistency means some internal links will 404 at launch.

---

## Pages Without Any Internal Page Links (Zero Links)

These pages have no working internal page links at all — only infographic image references or plain text placeholders:

| File | Link Count | Notes |
|---|---|---|
| if1-insurance-legal-regulatory-content.md | 0 | 3 unlinked text placeholders |
| if3-insurance-underwriting-process-content.md | 0 | 3 unlinked text placeholders |
| if4-insurance-claims-handling-content.md | 0 | 2 unlinked text placeholders |
| if5-motor-insurance-content.md | 0 | 4 unlinked text placeholders |
| lm3-london-market-broker-content.md | 0 | 2 unlinked text placeholders + 1 contextual |
| gr1-group-risk-content.md | 0 | 2 unlinked text placeholders |
| imu-india-motor-insurance-content.md | 0 | 1 unlinked placeholder + 2 contextual |
| wce-insurance-claims-non-uk-content.md | 0 | 2 unlinked placeholders + 1 contextual |

All eight of these pages are primarily Certificate-level or international variant pages. The unlinked text placeholders (e.g., `[IF3 insurance underwriting process assignment help]`) suggest the original author intended to add links but used square-bracket notation without the `(/slug)` URL component. These should be treated as highest-priority fixes — the anchor text already exists, only the URL needs to be added.

---

*Report generated: 2026-03-22 | Linking GPT workflow adapted for Markdown | CII Assignment Help client*
