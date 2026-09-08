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
