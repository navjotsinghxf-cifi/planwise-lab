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
