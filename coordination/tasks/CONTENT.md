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
