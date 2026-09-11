# Master tasks

All worker owners are role reservations until registration and explicit manager assignment.
No implementation is assigned to an unregistered worker.

Dependency order: REG -> ARCH -> UI; ARCH -> ENGINE -> SERVER; UI -> WEB and CONTENT; ENGINE + SERVER + WEB + CONTENT -> INTEGRATE -> QA -> SECOPS -> ACCEPT.
Architecture/design can proceed when their specific worker is registered; all six need not register simultaneously. Security-sensitive approvals still require a registered security reviewer.

Frontend and backend may work in parallel only after contract freeze and path reservation. Each task is further split by the manager into bounded issues if its registered worker cannot checkpoint it independently. QA findings become new scoped fix issues before acceptance.

## REG

TASK_ID: REG
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/1
TITLE: Register six independently authorized workers
OWNER: manager
DEPENDENCIES: NONE
INPUT_FILES: docs/WORKER_ONBOARDING.md, AGENTS.md
ALLOWED_PATHS: coordination/WORKER_REGISTRATION.txt; worker's own status/outbox; own checkpoint; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Six reviewed registrations; distinct roles and capability records
ACCEPTANCE_CRITERIA: Verify each worker's user authorization and unique identity; no implementation assigned before approval
REQUIRED_TESTS: Registration schema and append-only diff review
PR_REQUIRED: YES
STATUS: WAITING_DEPENDENCY — independent workers must register
PR_URL: NONE
REVIEWER: manager

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## ARCH

TASK_ID: ARCH
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/2
TITLE: Approve architecture, data model, engine contracts and mocks
OWNER: UNASSIGNED (reserved role: architect; registered worker required)
DEPENDENCIES: REG
INPUT_FILES: docs/PROJECT_BRIEF.md, docs/ADSENSE_READINESS.md
ALLOWED_PATHS: docs/ARCHITECTURE.md; docs/API_CONTRACT.md; docs/DATABASE_SCHEMA.md; packages/contracts/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Reviewed versioned contracts, examples, mocks and technology decisions
ACCEPTANCE_CRITERIA: Specify edge cases for all four tools, ownership and auth boundaries, document allowed implementation paths; manager records freeze
REQUIRED_TESTS: Contract schema validation; valid/invalid examples; mock compatibility
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: manager, security_devops

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## UI

TASK_ID: UI
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/3
TITLE: Specify accessible tool workflows and editorial design
OWNER: UNASSIGNED (reserved role: designer; registered worker required)
DEPENDENCIES: ARCH
INPUT_FILES: docs/PROJECT_BRIEF.md, docs/API_CONTRACT.md
ALLOWED_PATHS: docs/UI_SPEC.md; docs/design/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Complete responsive page and interaction specification
ACCEPTANCE_CRITERIA: All four tools, errors, impossible schedules, charts/tables, keyboard navigation and ad-safe layout specified
REQUIRED_TESTS: Design walkthrough; contrast and keyboard-order review
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: manager, frontend

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## ENGINE

TASK_ID: ENGINE
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/4
TITLE: Implement deterministic planning and comparison algorithms
OWNER: UNASSIGNED (reserved role: backend; registered worker required)
DEPENDENCIES: ARCH
INPUT_FILES: docs/ARCHITECTURE.md, packages/contracts/
ALLOWED_PATHS: packages/engine/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Tested critical-path, capacity, decision and study scheduling engines
ACCEPTANCE_CRITERIA: Match frozen contracts; cycles, ties, invalid weights, date boundaries, impossible schedules and 200-task cases handled
REQUIRED_TESTS: Unit/property tests; independent worked-example fixtures; benchmark
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: architect, qa

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## SERVER

TASK_ID: SERVER
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/5
TITLE: Implement private project persistence and authentication
OWNER: UNASSIGNED (reserved role: backend; registered worker required)
DEPENDENCIES: ENGINE
INPUT_FILES: docs/API_CONTRACT.md, docs/DATABASE_SCHEMA.md
ALLOWED_PATHS: apps/web/src/app/api/; apps/web/src/server/; supabase/; tests/backend/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Scoped API handlers, migrations, authenticated ownership checks and persistence tests
ACCEPTANCE_CRITERIA: Anonymous tools independent of server; cross-user access denied; optimistic concurrency and import size limits enforced
REQUIRED_TESTS: Integration tests for anonymous/cross-user access, CRUD, conflicts and migration application
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: security_devops, architect

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## WEB

TASK_ID: WEB
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/6
TITLE: Implement responsive public pages and interactive workspaces
OWNER: UNASSIGNED (reserved role: frontend; registered worker required)
DEPENDENCIES: UI, ARCH
INPUT_FILES: docs/UI_SPEC.md, packages/contracts/, approved mocks
ALLOWED_PATHS: apps/web/ excluding src/app/api/ and src/server/; package.json; package-lock.json; tsconfig.json; tests/frontend/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Functional frontend, workspace, exports, navigation and content rendering
ACCEPTANCE_CRITERIA: Use approved engine adapters/mocks; all tools usable anonymously; no fabricated editorial identities; clearly mark mocks in development; ads disabled
REQUIRED_TESTS: Component/browser checks; keyboard flows; responsive layouts; validation, import/export and persistence
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: designer, qa

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## CONTENT

TASK_ID: CONTENT
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/7
TITLE: Write and review original guides and publisher page drafts
OWNER: UNASSIGNED (reserved role: designer; registered worker required)
DEPENDENCIES: UI
INPUT_FILES: docs/PROJECT_BRIEF.md, docs/ADSENSE_READINESS.md, docs/API_CONTRACT.md
ALLOWED_PATHS: content/; docs/EDITORIAL_REVIEW.md; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Twelve substantial original guides, methodology and publisher-page drafts
ACCEPTANCE_CRITERIA: Three guides per tool, reproduced examples and limitations; editor signoff required; missing real identity/contact blocks publication; no filler or unsupported claims
REQUIRED_TESTS: Editorial originality review; calculation cross-checks; links and rendering checks
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: architect, manager

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## INTEGRATE

TASK_ID: INTEGRATE
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/8
TITLE: Integrate approved frontend, engines, persistence and content
OWNER: manager
DEPENDENCIES: ENGINE, SERVER, WEB, CONTENT
INPUT_FILES: Approved PRs, coordination/DECISIONS.md
ALLOWED_PATHS: Integration changes only; coordinate any needed implementation edits with original path owner; coordination/INTEGRATION_LOG.md; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Integrated application on reviewed integration PR
ACCEPTANCE_CRITERIA: No production mocks remain; real end-to-end anonymous and authenticated flows; dependencies compatible; preserve worker work
REQUIRED_TESTS: Build, typecheck, algorithm and end-to-end suite with recorded output
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: qa, architect

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## QA

TASK_ID: QA
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/9
TITLE: Verify functionality, accessibility and regressions
OWNER: UNASSIGNED (reserved role: qa; registered worker required)
DEPENDENCIES: INTEGRATE
INPUT_FILES: docs/PROJECT_BRIEF.md, docs/UI_SPEC.md
ALLOWED_PATHS: tests/e2e/; tests/accessibility/; docs/QA_REPORT.md; docs/BUGS.md; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Automated suites, manual evidence and reproducible defect reports
ACCEPTANCE_CRITERIA: All four tools and cloud isolation covered; mobile/keyboard checks; no untriaged release blockers; fixes get bounded issues
REQUIRED_TESTS: Browser suites; accessibility scan plus manual checks; independent numerical examples
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: manager

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## SECOPS

TASK_ID: SECOPS
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/10
TITLE: Review security, CI, deployment and advertising readiness
OWNER: UNASSIGNED (reserved role: security_devops; registered worker required)
DEPENDENCIES: QA
INPUT_FILES: docs/ADSENSE_READINESS.md, docs/DEPLOYMENT.md, docs/QA_REPORT.md
ALLOWED_PATHS: .github/; docs/SECURITY_REVIEW.md; docs/DEPLOYMENT.md; docs/ADSENSE_READINESS.md; security configuration with manager path reservation; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: CI, security findings, safe deployment and rollback runbook; AdSense evidence matrix
ACCEPTANCE_CRITERIA: No unresolved critical findings; review XSS/import handling, auth/RLS, dependencies, secrets and privacy; no paid/production changes
REQUIRED_TESTS: CI execution; adversarial ownership/import tests; headers/config checks; readiness evidence audit
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: manager, architect

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.


## ACCEPT

TASK_ID: ACCEPT
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/11
TITLE: Complete acceptance review and prepare owner release approval
OWNER: manager
DEPENDENCIES: QA, SECOPS
INPUT_FILES: All reports, approved PRs and requirements
ALLOWED_PATHS: README.md; docs/RELEASE_REVIEW.md; coordination/; for workers, own status/outbox and own checkpoint/handoff
EXPECTED_OUTPUT: Evidence-backed feature/test/risk summary and concrete release proposal
ACCEPTANCE_CRITERIA: All blockers fixed through scoped issues; real publisher inputs resolved; user approval required before production; Google approval never presumed
REQUIRED_TESTS: Recheck actual acceptance evidence; after authorized deployment verify live core flows
PR_REQUIRED: YES
STATUS: BLOCKED — dependency/registration gates
PR_URL: NONE
REVIEWER: qa, security_devops

Role reservations do not assign work to unregistered workers. Manager must inspect repository state and explicitly assign before implementation. Root build configuration is initially frontend-owned; other workers propose changes through outboxes. Security contract review can be requested after that reviewer registers without waiting for final SECOPS task.

## COORD
TASK_ID: COORD
GITHUB_ISSUE: https://github.com/navjotsinghxf-cifi/planwise-lab/issues/12
OWNER: manager
ALLOWED_PATHS: AGENTS.md; README.md; docs/WORKER_ONBOARDING.md; docs/NOTION_WORKFLOW.md; coordination/MASTER_TASKS.md; coordination/DECISIONS.md; coordination/status/manager.txt; coordination/checkpoints/manager.md; coordination/INTEGRATION_LOG.md; coordination/notion-channels.json
STATUS: IN_PROGRESS — workflow proposal; independent review required
ACCEPTANCE_CRITERIA: Notion channels, attributed manager transfers, preserved review gates, authorized public visibility recorded; no premature implementation assignments
REQUIRED_TESTS: git diff --check; scoped diff review; Notion readback
REVIEWER: independently authorized suitable reviewer, not manager
