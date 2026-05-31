# HND Assignment Help — Internal Linking Map

> Implementation rule: **never add a link to a page that is not yet live**. Each phase section below lists the
> URLs that become available. When a phase goes live, uncomment those links in the `related-pages` navs of
> every page in the "Receives links from" column.

---

## Slug Registry — Authoritative URL Reference

| Slug | Page Title | Phase | Status |
|------|-----------|-------|--------|
| `hnd-assignment-help` | HND Assignment Help (hub) | 1 | ✅ Live |
| `hnd-business-assignment-help` | HND Business Assignment Help | 1 | ✅ Live |
| `hnd-computing-assignment-help` | HND Computing Assignment Help | 1 | ✅ Live |
| `hnd-engineering-assignment-help` | HND Engineering Assignment Help | 1 | ✅ Live |
| `hnd-health-and-social-care-assignment-help` | HND Health and Social Care Assignment Help | 1 | ✅ Live |
| `hnd-assignment-grading-criteria-explained` | HND Assignment Grading Criteria Explained | 2 | 🔜 Written, not deployed |
| `how-to-achieve-distinction-in-hnd-assignments` | How to Achieve Distinction in HND Assignments | 2 | 🔜 Written, not deployed |
| `hnd-assignment-resubmission-guide` | HND Assignment Resubmission Guide | 2 | 🔜 Written, not deployed |
| `hnd-business-research-project-assignment-help` | HND Business Research Project Assignment Help | 2 | 🔜 Written, not deployed |
| `hnd-assignment-brief-how-to-read-and-interpret-it` | How to Read an HND Assignment Brief | 3 | ⏳ Not written |
| `harvard-referencing-for-hnd-assignments` | Harvard Referencing for HND Assignments | 3 | ⏳ Not written |
| `hnd-hospitality-management-assignment-help` | HND Hospitality Management Assignment Help | 3 | ⏳ Not written |
| `hnd-construction-and-the-built-environment-assignment-help` | HND Construction Assignment Help | 3 | ⏳ Not written |
| `hnd-sport-and-exercise-science-assignment-help` | HND Sport and Exercise Science Assignment Help | 3 | ⏳ Not written |
| `hnd-early-childhood-studies-assignment-help` | HND Early Childhood Studies Assignment Help | 3 | ⏳ Not written |
| `hnd-business-research-project-assignment-help` | HND Business Research Project | 3 | ⏳ Not written |

---

## Phase 1 — Currently Live

**Target: 2026-04-11 (complete)**

All five pages have `related-pages` navs with cross-links. Phase 2+ links are commented out.

### Link matrix

| From page | Links to (live only) |
|-----------|---------------------|
| Hub (`hnd-assignment-help`) | Business, Computing, Engineering, Health & Social Care |
| Business | Hub, Computing, Engineering, Health & Social Care |
| Computing | Hub, Business, Engineering, Health & Social Care |
| Engineering | Hub, Business, Computing, Health & Social Care |
| Health & Social Care | Hub, Business, Computing, Engineering |

### Phase 1 → Phase 2 upgrade checklist (do when Phase 2 goes live)
Uncomment in each Phase 1 page's `related-pages` nav:

**Hub** — uncomment all four Phase 2 links:
- `/hnd-assignment-grading-criteria-explained/`
- `/how-to-achieve-distinction-in-hnd-assignments/`
- `/hnd-assignment-resubmission-guide/`
- `/hnd-business-research-project-assignment-help/`

**Business** — uncomment:
- `/hnd-assignment-grading-criteria-explained/`
- `/how-to-achieve-distinction-in-hnd-assignments/`
- `/hnd-assignment-resubmission-guide/`
- `/hnd-business-research-project-assignment-help/`

**Computing** — uncomment:
- `/hnd-assignment-grading-criteria-explained/`
- `/how-to-achieve-distinction-in-hnd-assignments/`

**Engineering** — uncomment:
- `/hnd-assignment-grading-criteria-explained/`
- `/how-to-achieve-distinction-in-hnd-assignments/`

**Health & Social Care** — uncomment:
- `/hnd-assignment-grading-criteria-explained/`
- `/how-to-achieve-distinction-in-hnd-assignments/`
- `/hnd-assignment-resubmission-guide/`

---

## Phase 2 — Written, not yet deployed

**Target: 2026-04-30 (publishing_schedule.md weeks 4–5)**

HTML files are in `client_data/New-sites/hnd-assignment-help/pages/` using the correct slugs.
To deploy: copy to `src/content/pages/` in the Astro project.

### File names (match content.json slugs exactly)
- `hnd-assignment-grading-criteria-explained.html`
- `how-to-achieve-distinction-in-hnd-assignments.html`
- `hnd-assignment-resubmission-guide.html`
- `hnd-business-research-project-assignment-help.html`

### Link matrix (Phase 2 pages already contain these links)

| From page | Links to Phase 1 (live) | Links to Phase 2 siblings (live together) |
|-----------|------------------------|------------------------------------------|
| Grading Criteria | Hub, Business, Computing, Engineering, H&SC | Distinction, Resubmission, Business Project |
| Distinction | Hub, Business, Computing, Engineering, H&SC | Grading Criteria, Resubmission, Business Project |
| Resubmission | Hub, Business, Computing, Engineering, H&SC | Grading Criteria, Distinction |
| Business Project | Hub, Business | Grading Criteria, Distinction |

### Phase 2 → Phase 3 upgrade checklist (do when Phase 3 pages go live)
Grading Criteria — uncomment:
- `/hnd-assignment-brief-how-to-read-and-interpret-it/`
- `/harvard-referencing-for-hnd-assignments/`

Distinction — uncomment:
- `/hnd-assignment-brief-how-to-read-and-interpret-it/`

Resubmission — uncomment:
- `/hnd-assignment-brief-how-to-read-and-interpret-it/`

Business Project — uncomment:
- `/harvard-referencing-for-hnd-assignments/`

---

## Phase 3 — Not yet written

**Target: 2026-05-12+ (publishing_schedule.md weeks 6–18)**

### Planned pages and their outbound links when published

| New page | Links to Phase 1 | Links to Phase 2 | Links to Phase 3 siblings |
|----------|-----------------|-----------------|--------------------------|
| Assignment Brief | Hub, Business, Computing | Grading Criteria, Distinction | — |
| Harvard Referencing | Hub, Business | Grading Criteria | — |
| Hospitality | Hub | Grading Criteria, Distinction | — |
| Construction | Hub, Engineering | Grading Criteria, Distinction | — |
| Sport | Hub | Grading Criteria, Distinction | — |
| Early Childhood | Hub, Health & Social Care | Grading Criteria, Distinction, Resubmission | — |

### Phase 3 additions to Phase 1/2 related-pages (uncomment when each page goes live)

**Hub** (Phase 3 block already commented):
- `/hnd-assignment-brief-how-to-read-and-interpret-it/`
- `/harvard-referencing-for-hnd-assignments/`
- `/hnd-hospitality-management-assignment-help/`
- `/hnd-construction-and-the-built-environment-assignment-help/`
- `/hnd-sport-and-exercise-science-assignment-help/`
- `/hnd-early-childhood-studies-assignment-help/`

**Engineering** — add when Construction published:
- `/hnd-construction-and-the-built-environment-assignment-help/`

**Health & Social Care** — add when Early Childhood published:
- `/hnd-early-childhood-studies-assignment-help/`

---

## Contextual bridges (topical map anchors)

These are the preferred anchor texts for in-body contextual links, derived from the topical map `supplementary_bridges_to` fields:

| Destination page | Preferred anchor text |
|-----------------|----------------------|
| Hub | "HND assignment help" / "HND Level 5 assignment support" |
| Business | "HND Business assignment help" / "HND Business unit guidance at Level 5" |
| Computing | "HND Computing assignment help" / "HND Computing analytical writing standard" |
| Engineering | "HND Engineering assignment help" / "HND Engineering unit guidance" |
| Health & Social Care | "HND Health and Social Care assignment help" / "HND Health and Social Care Level 5 assignments" |
| Grading Criteria | "HND assignment grading criteria" / "HND Pass, Merit, and Distinction criteria" |
| Distinction | "how to achieve distinction in HND assignments" / "HND Distinction strategy" |
| Resubmission | "HND assignment resubmission" / "HND referral and resubmission rules" |
| Business Project | "HND Business Research Project" / "HND Managing a Successful Business Project" |

---

## Implementation notes

1. The `related-pages` nav appears immediately before `<section class="contact-form">` in every HTML file.
2. Use HTML comments `<!-- Phase N — uncomment when published (YYYY-MM-DD) -->` to mark future links.
3. The `content.json` slug is the URL — file names must match slugs exactly for Astro static paths to resolve.
4. Never link to a slug that is not in `content.json` with a matching HTML file in `src/content/pages/`.
5. When adding a new page, also update this map.
