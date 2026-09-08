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
