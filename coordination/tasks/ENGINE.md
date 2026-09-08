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
