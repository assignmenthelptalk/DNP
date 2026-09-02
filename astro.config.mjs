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
  'https://www.dnpcapstoneproject.help/thank-you/',
  'https://www.dnpcapstoneproject.help/orders/signup/',
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
  site: 'https://www.dnpcapstoneproject.help',
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
