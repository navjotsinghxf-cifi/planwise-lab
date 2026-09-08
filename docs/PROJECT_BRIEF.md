# Project brief

## Decision and audience
The user delegated product, stack, design and hosting choices on 2026-09-08.
Build Planwise Lab, an English-language planning and learning site for students, freelancers and small teams.
Success means helping users make and explain a realistic plan, with reproducible calculations and practical original content.

## First release scope
1. Project planning: tasks, durations, dependencies, cycle errors, topological scheduling, critical path, float, PERT three-point estimates. Label workdays versus calendar days explicitly.
2. Capacity planning: per-person weekly availability, nonworking dates, workload allocation and overload comparisons. Capacity changes must not silently move deadlines.
3. Decision comparison: named alternatives and criteria, positive weights, benefit/cost criteria, normalization, ties, missing inputs and rank sensitivity.
4. Study scheduling: topics, deadlines, available slots, spaced reviews, editable sessions, impossible-schedule reporting. No guaranteed learning outcomes.
5. Unified workspace: anonymous tools, browser persistence, validated JSON import/export, print views; optional private cloud saving with authentication.
6. Public content: tool explanations plus an initial editorial target of 12 substantial original guides, three per tool. This is a product target, NOT Google's minimum or a guarantee.
7. Search, responsive navigation, keyboard access, mobile views and charts with tabular equivalents.
8. Truthful About, Contact, Privacy, Terms, editorial policy and correction process. Real publisher identity and contact details must come from the owner before release.
9. Crawlable public content, metadata, sitemap, canonical URLs and exclusion of private or transient workspace pages from indexing.
10. Advertising stays disabled until owner configuration, consent review and applicable Google readiness/review steps.

## Quality and acceptance
Each tool has validated inputs, meaningful errors, deterministic examples and edge-case tests.
Original guides explain methodology, inputs, results, limitations, and real use cases; a named responsible editor reviews drafts before publication.
No fabricated authors, credentials, user counts, testimonials, contact details or endorsements.
Core anonymous use works without login or paid services. Private projects are isolated by user and never publicly indexed.
Automated browser and algorithm tests plus manual keyboard and screen-reader checks are required.
Performance targets: responsive interaction with 200 tasks; measure and record benchmark hardware.
Launch performance targets: LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1 where field measurement is available; lab results are not field proof.

## Non-goals
Public user-generated posts, financial/medical advice, scraping, mass-generated SEO pages, paid subscriptions, guaranteed rankings or guaranteed AdSense acceptance.

## Open release inputs
Owner's public publisher/contact identity, domain, hosting/account choices and cost approval if needed,
actual ad account eligibility and configuration. Do not invent these or request secret values.
These do not block architecture/design, but publication and AdSense submission remain blocked.
