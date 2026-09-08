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
