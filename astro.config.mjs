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

const CORE_T2_PROJECT_TYPE = new Set([
  'dnp-quality-improvement-project-help',
  'dnp-evidence-based-practice-project-help',
  'dnp-program-evaluation-capstone-help',
  'dnp-policy-change-project-help',
]);

const CORE_T2_TRACKS = new Set([
  'fnp-dnp-capstone-project-help',
  'pmhnp-dnp-capstone-project-help',
  'agacnp-dnp-capstone-project-help',
  'crna-dnp-capstone-project-help',
  'nurse-executive-dnp-capstone-help',
  'population-health-dnp-capstone-help',
  'nursing-informatics-dnp-capstone-help',
]);

const OUTER = new Set([
  'dnp-vs-phd-nursing',
  'aacn-dnp-essentials-capstone',
  'ebp-frameworks-dnp-projects',
  'picot-framework-nursing',
  'systematic-vs-scoping-review-dnp',
  'irb-protocol-nursing-projects',
  'statistical-methods-dnp-capstone',
]);

function getSlug(url) {
  return url.replace(/^https?:\/\/[^/]+\//, '').replace(/\/$/, '');
}

export default defineConfig({
  site: 'https://www.dnp-capstone-project.help',
  redirects: {
    '/faq-on-dnp-capstone-project-help/': '/',
    '/blog/': '/',
  },
  integrations: [
    sitemap({
      serialize(item) {
        const slug = getSlug(item.url);

        if (slug === '') {
          item.priority = 1.0;
          item.changefreq = 'weekly';
        } else if (CORE_T1.has(slug)) {
          item.priority = 0.9;
          item.changefreq = 'weekly';
        } else if (CORE_T2_PROJECT_TYPE.has(slug) || CORE_T2_TRACKS.has(slug)) {
          item.priority = 0.8;
          item.changefreq = 'monthly';
        } else if (OUTER.has(slug)) {
          item.priority = 0.65;
          item.changefreq = 'monthly';
        } else {
          item.priority = 0.6;
          item.changefreq = 'monthly';
        }

        return item;
      },
    }),
  ],
});
