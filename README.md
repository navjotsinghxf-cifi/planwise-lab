# Planwise Lab

Useful planning tools and original educational guides for students, freelancers, and small teams.

**Status: coordination bootstrap only. No website is implemented or deployed. AdSense approval has not been obtained.**
Repository: https://github.com/navjotsinghxf-cifi/planwise-lab (public with owner approval; application deployment is not authorized).

## Product
- Project dependency planner: cycle detection, critical path, earliest/latest dates, slack, and transparent PERT estimates.
- Workload planner: weekly capacity, holidays, overload warnings, and what-if comparisons.
- Decision workbench: weighted criteria, benefit/cost direction, missing-data handling, and sensitivity analysis.
- Study planner: available-time constraints, deadlines, spaced review sessions, and manual adjustments.
- Original guides with reproducible worked examples, assumptions, limitations, and editorial review.
- Anonymous use, browser saving/export, and optional private account-based project saving.

## Start here
Read docs/PROJECT_BRIEF.md, AGENTS.md, coordination/MASTER_TASKS.md, and coordination/DECISIONS.md.
Independent workers: read docs/WORKER_ONBOARDING.md and docs/NOTION_WORKFLOW.md. Consult accepted registrations and current issues for role availability. Security/DevOps registration was accepted through PR #17; architect identity remains unresolved. Platform names do not identify workers. Notion carries operational messages and submissions; GitHub holds accepted work.

## Proposed layout
- apps/web/ — Next.js pages, components, server routes
- packages/contracts/ — shared validated input/output contracts
- packages/engine/ — deterministic planning algorithms
- content/guides/ — reviewed educational content
- supabase/migrations/ — database and access policies
- tests/ — integration, browser, and accessibility checks
- docs/ — product, architecture, editorial, and release specifications
- coordination/ — separate worker inboxes, outboxes, status, checkpoints
- .github/workflows/ — CI (to be implemented)

## Development and deployment
The architect must approve versions and commands before implementation. No install, test, or deployment commands are represented as operational yet.
Proposed stack: Next.js App Router, TypeScript, PostgreSQL/Supabase, Vitest, Playwright, axe.
Proposed hosting: Vercel plus Supabase, subject to cost review and explicit production approval.
See docs/ADSENSE_READINESS.md and docs/DEPLOYMENT.md.
