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
