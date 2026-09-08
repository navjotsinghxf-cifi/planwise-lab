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
