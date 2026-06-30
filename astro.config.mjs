// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

const CORE_T1 = new Set([
  'dnp-capstone-project-help',
  'dnp-capstone-proposal-help',
  'dnp-picot-question-help',
  'dnp-literature-review-help',
  'dnp-irb-proposal-help',
  'dnp-implementation-plan-help',
  'dnp-data-analysis-help',
  'dnp-capstone-manuscript-help',
]);

const CORE_T1C = new Set([
  '50-dnp-capstone-project-ideas',
  '60-dnp-picot-question-examples',
  'dnp-capstone-project-examples',
]);

const CORE_T2_PROJECT_TYPE = new Set([
  'dnp-quality-improvement-project',
  'dnp-ebp-implementation-project',
  'dnp-program-evaluation-project',
  'dnp-policy-change-project',
]);

const CORE_T2_TRACKS = new Set([
  'dnp-fnp-capstone-help',
  'dnp-pmhnp-capstone-help',
  'dnp-agacnp-capstone-help',
  'dnp-crna-capstone-help',
  'dnp-nurse-executive-capstone-help',
  'dnp-population-health-capstone-help',
  'dnp-nursing-informatics-capstone-help',
]);

const CORE_T2C = new Set([
  'bsn-capstone-project-help',
  'msn-capstone-project-help',
]);

const CORE_T2D = new Set([
  'dnp-discussion-board-help',
  'dnp-powerpoint-presentation-help',
  'dnp-admission-essay-help',
  'dnp-letter-of-intent-help',
]);

const OUTER = new Set([
  'dnp-vs-phd-nursing',
  'aacn-dnp-essentials-2021',
  'ebp-frameworks-dnp',
  'picot-framework-explained',
  'systematic-vs-scoping-review',
  'irb-protocol-dnp',
  'statistical-methods-dnp',
  'apa-7th-edition-dnp',
]);

// Tier 0 utility pages — low crawl priority, rarely change
const UTILITY = new Set([
  'about-us',
  'contact-us',
  'services',
  'faq',
  'samples',
  'our-policy',
  'privacy-policy',
  'refund-policy',
  'money-back-guarantee',
  'term-conditions',
  'cookie-policy',
  'orders',
]);

// Pages to exclude from sitemap entirely
const EXCLUDED = new Set([
  'https://dnpcapstoneproject.help/thank-you/',
  'https://dnpcapstoneproject.help/orders/signup/',
]);

const UNIVERSITY = new Set([
  'dnp-capstone-project-help-grand-canyon-university',
  'dnp-capstone-project-help-aspen-university',
  'walden-university-dnp-capstone-help',
  'capella-dnp-capstone-help',
]);

function getSlug(url) {
  return url.replace(/^https?:\/\/[^/]+\//, '').replace(/\/$/, '');
}

export default defineConfig({
  site: 'https://dnpcapstoneproject.help',
  redirects: {
    // ── Legacy catch-all ────────────────────────────────────────────────────
    '/faq-on-dnp-capstone-project-help/': '/',
    '/blog/': '/',

    // ── Service page redirects ───────────────────────────────────────────────
    '/dnp-capstone-project-writing/': '/dnp-capstone-project-help/',
    '/dnp-capstone-project-writing-services/': '/dnp-capstone-project-help/',
    '/dnp-capstone-proposal-writing-services/': '/dnp-capstone-proposal-help/',
    '/dnp-capstone-services/': '/services/',
    '/dnp-capstone-coursework-writing-help/': '/dnp-capstone-project-help/',
    '/dnp-project-proposal-examples/': '/dnp-capstone-project-examples/',
    '/dnp-project-editor/': '/services/',
    '/dnp-project-literature-review-help/': '/dnp-literature-review-help/',
    '/dnp-literature-review/': '/dnp-literature-review-help/',
    '/dpi-literature-review-help/': '/dnp-literature-review-help/',
    '/dpi-project-writer/': '/services/',
    '/dnp-discussion-posts-writing-services/': '/dnp-discussion-board-help/',
    '/dnp-final-project-presentations/': '/dnp-powerpoint-presentation-help/',
    '/np-dnp-letter-of-recommendation/': '/services/',
    '/irb-proposal-writing-services/': '/dnp-irb-proposal-help/',
    '/proposal-writing-for-clinical-nursing-and-dnp-projects/': '/dnp-capstone-proposal-help/',
    '/hire-dnp-capstone-statistician/': '/dnp-data-analysis-help/',
    '/online-dnp-assignment-exam-help/': '/services/',
    '/online-dnp-project-tutors/': '/services/',
    '/help-with-dnp-class/': '/services/',
    '/help-with-dnp-picot-question/': '/dnp-picot-question-help/',
    '/help-with-dnp-prospectus/': '/dnp-capstone-proposal-help/',
    '/nursing-assignment-help/': '/services/',
    '/nursing-help/': '/services/',
    '/nursing-thesis-statement-writing-services/': '/services/',
    '/pie-nursing-writing-services/': '/services/',
    '/pathophysiology-discussion-board-writing-help/': '/dnp-discussion-board-help/',
    '/online-nursing-essays-discussions-and-assignments-papers/': '/services/',
    '/doctoral-level-nursing-essay-help/': '/services/',
    '/ihuman-assignment-help/': '/services/',
    '/shadow-health-assignment-help/': '/services/',
    '/walden-university-online-nursing-assignment-writing-company/': '/walden-university-dnp-capstone-help/',
    '/bsn-capstone-project-writing-services/': '/bsn-capstone-project-help/',
    '/bsn-capstone-services/': '/bsn-capstone-project-help/',
    '/msn-capstone-project-writing-services/': '/msn-capstone-project-help/',
    '/msn-capstone-services/': '/msn-capstone-project-help/',

    // ── Blog / SEO article redirects ─────────────────────────────────────────
    '/dnp-picot-question-examples/': '/60-dnp-picot-question-examples/',
    '/dnp-evidence-based-practice-project-picot-questions/': '/60-dnp-picot-question-examples/',
    '/evidence-based-project-ebp-picot-question/': '/dnp-capstone-project-help/',
    '/pediatrics-picot-questions-examples/': '/60-dnp-picot-question-examples/',
    '/picot-new-diabetics/': '/60-dnp-picot-question-examples/',
    '/dnp-essentials/': '/dnp-capstone-project-help/',
    '/dnp-doctor-of-nursing-practice/': '/dnp-capstone-project-help/',
    '/dnp-dpi-proposal-template/': '/dnp-capstone-proposal-help/',
    '/dnp-crna-project/': '/dnp-capstone-project-help/',
    '/dnp-healthcare-administration-capstone/': '/dnp-capstone-project-help/',
    '/dnp-scholarly-project-and-phd-dissertation/': '/dnp-capstone-project-help/',
    '/dnp-projects-aacn-essentials/': '/dnp-capstone-project-help/',
    '/dnp-project-proposal-management-and-prevention-of-type-2-diabetes/': '/50-dnp-capstone-project-ideas/',
    '/inspiring-dnp-project-ideas-in-psychiatric-mental-health/': '/50-dnp-capstone-project-ideas/',
    '/oncology-dnp-project-ideas-for-dnp-bsn-msn/': '/50-dnp-capstone-project-ideas/',
    '/pediatric-dnp-project-ideas/': '/50-dnp-capstone-project-ideas/',
    '/what-should-i-do-for-my-dnp-project/': '/50-dnp-capstone-project-ideas/',
    '/latest-pediatric-nursing-research-topics/': '/50-dnp-capstone-project-ideas/',
    '/nursing-practicum-objectives-examples/': '/dnp-capstone-project-help/',
    '/nursing-practicum-project-ideas/': '/50-dnp-capstone-project-ideas/',
    '/nursing-literature-review-matrix/': '/dnp-literature-review-help/',
    '/nursing-quality-improvement-paper-essay-example/': '/dnp-capstone-project-help/',
    '/nursing-quality-indicator-improvement/': '/dnp-capstone-project-help/',
    '/nursing-project-of-fall-prevention-using-ebp-of-exercise/': '/50-dnp-capstone-project-ideas/',
    '/nursing-roles-graphic-organizer/': '/dnp-capstone-project-help/',
    '/evidence-based-practice-nursing-essays-and-research-papers/': '/dnp-capstone-project-help/',
    '/evidence-based-practice-paper-in-nursing/': '/dnp-capstone-project-help/',
    '/change-project-paper-in-nursing/': '/dnp-implementation-plan-help/',
    '/ihi-triple-aim/': '/dnp-capstone-project-help/',
    '/soap-note/': '/services/',
    '/walden-dissertation-checklist/': '/walden-university-dnp-capstone-help/',
    '/walden-msn-program/': '/msn-capstone-project-help/',
    '/walden-university-discussion-post/': '/dnp-discussion-board-help/',
    '/capella-rn-to-bsn-in-just-3-months/': '/bsn-capstone-project-help/',
    '/career-paths-for-nurse-informaticist/': '/dnp-capstone-project-help/',
    '/nurse-educator-scope-of-practice-essay/': '/services/',
    '/nurse-manager-interview-questions-and-answers/': '/dnp-capstone-project-help/',
    '/long-term-goals-for-nurse-practitioner-student-example-essay/': '/dnp-capstone-project-help/',
    '/self-directed-learning-plan/': '/dnp-capstone-project-help/',
    '/tables-graphs-and-histograms-in-nursing-essay/': '/dnp-data-analysis-help/',
    '/how-to-use-the-epidemiologic-triangle/': '/dnp-capstone-project-help/',
    '/quality-healthcare-measuring-np-performance/': '/dnp-capstone-project-help/',
    '/quality-improvement-initiative-executive-summary/': '/dnp-capstone-project-help/',
    '/effective-approaches-in-leadership-and-management/': '/dnp-capstone-project-help/',
    '/roles-of-professional-nursing-organizations/': '/dnp-capstone-project-help/',
    '/johns-hopkins-nursing-evidence-based-practice-jhnebp-and-the-six-sigma-model/': '/dnp-capstone-project-help/',
    '/accountability-in-healthcare-essay-example/': '/services/',
    '/covid-19-evaluation-and-management/': '/services/',
    '/affordable-care-act-aca-nursing-homework-help/': '/services/',

    // ── GCU course pages → GCU hub ───────────────────────────────────────────
    '/dnp-801a-introduction-to-dnp-studies/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-805a-health-care-informatics/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-810a-emerging-areas-of-human-health/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-815a-scientific-underpinnings/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-820a-translational-research-and-evidence-based-practice/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-825a-population-management/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-830a-data-analysis/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-835a-patient-outcomes-and-sustainable-change/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-838a-nursing-program-development-and-educational-leadership/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-840a-leadership-for-advanced-nursing-practice/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-955a-dpi-project-part-i/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-960a-dpi-project-part-ii/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/dnp-965a-dpi-project-part-iii/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/nrs-415-creating-change-through-advocacy/': '/dnp-capstone-project-help-grand-canyon-university/',
    '/nrs-415-nursing-leadership-and-interprofessional-collaboration/': '/dnp-capstone-project-help-grand-canyon-university/',

    // ── Walden course pages → Walden hub ─────────────────────────────────────
    '/nurs-6501-advanced-pathophysiology-discussion-essay-assignments-and-question-and-answer-quizzes/': '/walden-university-dnp-capstone-help/',
    '/nurs-6512-advanced-health-assessment-and-diagnostic-reasoning-discussion-essay-assignments-and-question-and-answer-quizzes/': '/walden-university-dnp-capstone-help/',
    '/nurs-6521-advanced-pharmacology-discussion-essay-assignments-and-question-and-answer-quizzes/': '/walden-university-dnp-capstone-help/',
    '/nurs-6531-advanced-practice-care-of-adults-across-the-lifespan/': '/walden-university-dnp-capstone-help/',
    '/nurs-6540-advanced-practice-care-of-frail-elders-discussion-essay-assignments-and-question-and-answer-quizzes/': '/walden-university-dnp-capstone-help/',
    '/nurs-6551-primary-care-of-women-essay-assignment-papers-and-exam-questions-and-answers/': '/walden-university-dnp-capstone-help/',
    '/nurs-6600-capstone-synthesis-practicum-writing-services/': '/walden-university-dnp-capstone-help/',
    '/nurs-8000-foundations-and-essentials-of-doctoral-study-in-nursing-discussion-essay-assignments/': '/walden-university-dnp-capstone-help/',
    '/nurs-8100-identification-of-a-practice-issue-for-the-evidence-based-practice-ebp-essay-assignment/': '/walden-university-dnp-capstone-help/',
    '/nurs-8410-best-practices-in-nursing-specialties-weekly-discussion-essay-assignments/': '/walden-university-dnp-capstone-help/',
    '/nurs-fpx-9901-nursing-doctoral-project-1/': '/walden-university-dnp-capstone-help/',
    '/leadership-and-management-master-of-science-in-nursing-msn-nurs-6600-nurs-6201-nurs-6241-nurs-6231-nurs-6221-nurs-6211/': '/walden-university-dnp-capstone-help/',

    // ── Capella course pages → Capella hub ───────────────────────────────────
    '/nur-513-introduction-to-advanced-registered-nursing-essays/': '/capella-dnp-capstone-help/',
    '/nur-514-organizational-leadership-and-informatics/': '/capella-dnp-capstone-help/',
    '/nur-550-translational-research-nursing-essay-example/': '/capella-dnp-capstone-help/',
    '/nur-700-theory-selection-and-critical-analysis/': '/capella-dnp-capstone-help/',
    '/msn-fp6610-comprehensive-needs-assessment-essay/': '/capella-dnp-capstone-help/',

    // ── Generic DNP course series → pillar ───────────────────────────────────
    '/dnp800-theoretical-and-scientific-underpinnings/': '/dnp-capstone-project-help/',
    '/dnp805-organizational-and-systems-leadership/': '/dnp-capstone-project-help/',
    '/dnp810-evidence-based-practice-for-quality-improvement/': '/dnp-capstone-project-help/',
    '/dnp820-health-policy-and-advocacy-essay-help/': '/dnp-capstone-project-help/',
    '/dnp865-healthcare-technologies-and-informatics/': '/dnp-capstone-project-help/',
    '/dnp870-health-policy-advocacy-and-partnerships/': '/dnp-capstone-project-help/',
    '/dnp875-population-health-and-person-centered-care/': '/dnp-capstone-project-help/',
    '/dnp880-strategic-leadership-and-business-management/': '/dnp-capstone-project-help/',
    '/dnp885-strategic-planning-and-financial-management/': '/dnp-capstone-project-help/',
    '/dnp890-dnp-practicum/': '/dnp-capstone-project-help/',
    '/dnp899-dnp-project-capstone/': '/dnp-capstone-project-help/',
    '/gonzaga-university-dnp-course-essay-assignments-nurs-563-700-701-705-710-720-730-761-764/': '/dnp-capstone-project-help/',
  },
  integrations: [
    sitemap({
      filter: (page) => !EXCLUDED.has(page),
      serialize(item) {
        const slug = getSlug(item.url);
        const today = new Date().toISOString().split('T')[0];

        if (slug === '') {
          item.priority = 1.0;
          item.changefreq = 'weekly';
        } else if (CORE_T1.has(slug)) {
          item.priority = 0.9;
          item.changefreq = 'weekly';
        } else if (CORE_T1C.has(slug)) {
          item.priority = 0.85;
          item.changefreq = 'weekly';
        } else if (CORE_T2_PROJECT_TYPE.has(slug) || CORE_T2_TRACKS.has(slug)) {
          item.priority = 0.8;
          item.changefreq = 'monthly';
        } else if (CORE_T2C.has(slug) || CORE_T2D.has(slug)) {
          item.priority = 0.75;
          item.changefreq = 'monthly';
        } else if (UNIVERSITY.has(slug)) {
          item.priority = 0.7;
          item.changefreq = 'monthly';
        } else if (OUTER.has(slug)) {
          item.priority = 0.65;
          item.changefreq = 'monthly';
        } else if (UTILITY.has(slug)) {
          item.priority = 0.5;
          item.changefreq = 'yearly';
        } else {
          item.priority = 0.6;
          item.changefreq = 'monthly';
        }

        item.lastmod = today;
        return item;
      },
    }),
  ],
});
