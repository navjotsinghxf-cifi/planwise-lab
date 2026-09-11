# Repository working agreement

## Authority and current state
The user authorized the manager to choose the product and create this repository, initially private and subsequently made public with explicit user approval.
There are seven roles: manager, architect, designer, frontend, backend, qa, security_devops.
Workers are independent user-authorized sessions. Do not spawn or automate sessions, create accounts, share credentials, or bypass limits.
No implementation may be assigned to an unregistered worker.
Manager bootstrap may establish the initial main branch with coordination documents only. All subsequent changes use pull requests.
The initial main commit is the approved integration base. After initialization, use latest approved main; never treat an unreviewed branch as approved.

## Required workflow
1. Read docs/PROJECT_BRIEF.md, coordination/MASTER_TASKS.md, coordination/DECISIONS.md, and your own inbox before work.
2. Work only on an assigned GitHub issue. Each task has one primary owner and explicit allowed paths.
3. Branch from approved main: agent/<role>/<issue-number>-<short-name>. Never commit directly to main.
4. Workers update only their own status and outbox among communication files. Manager owns inboxes, the master plan, decisions and integration log.
5. Administrative exception: a worker may submit registration through Notion for manager transfer to a PR associated with the registration issue, or append its own entry through a direct PR. Rebase to preserve every other registration.
6. Workers may create their own checkpoint and handoff files. Implementation files must stay inside the task's allowed paths.
7. Submit implementation through scoped pull requests, directly or through manager transfer of Notion deliverables with author/source attribution. Never overwrite another worker's unfinished work.
8. Never silently change approved APIs or schemas. Propose changes in your outbox and await recorded approval.
9. Pull/rebase latest approved main before final submission. Run relevant tests and attach actual output or CI links. Give exact reproduction steps for bugs.
10. Commit and push a checkpoint before pausing. Never commit passwords, cookies, keys, tokens, or other credentials. Do not request or reveal them.
11. Manager inspects repository, issues, registrations, branches, PRs, dependencies and path conflicts before every assignment.
12. No public release, production deployment, paid activation, domain changes, or destructive database action without explicit user approval.

## Registration
Submit the template from coordination/WORKER_REGISTRATION.txt through Notion or a registration PR; use a unique AGENT_ID, one requested available role, UTC timestamp, branch (NONE when unavailable) and capabilities. Include independent user authorization, actual GitHub read/write capability and source message reference. Manager records verified requests in GitHub through a PR; a request alone is not approved registration.
A registration PR is administrative work only, not permission to implement.
Manager verifies user authorization, approves the registration, then records an assignment in the role inbox and task issue.
Role reservation in a task is not assignment to a real worker. Duplicate role claims require manager resolution.

## Communication format
Append timestamped messages; do not replace history:
MESSAGE_ID:
TIMESTAMP_UTC:
FROM:
TO:
RELATED_TASK:
PRIORITY:
MESSAGE:
RESPONSE_REQUIRED:

Manager marks processed inbox instructions with HANDLED_BY, HANDLED_AT_UTC, RESULT_REFERENCE based on worker evidence.
Notion is the operational channel: separate role inboxes/outboxes, registration requests and deliverable pages. Workers reply only in their own channels; manager owns inboxes and mirrors accepted decisions, assignments and status into GitHub through PRs. Repository communication files preserve historical records. Important decisions also go in coordination/DECISIONS.md.
Code, specs and test logs may be submitted as Notion deliverables with explicit paths and base commit; accepted artifacts belong in GitHub. A Notion submission is not a merged change or completed task. See docs/NOTION_WORKFLOW.md for transfer and review rules.

## Worker status values
AVAILABLE, ASSIGNED, IN_PROGRESS, WAITING_DEPENDENCY, BLOCKED, READY_FOR_REVIEW,
CHANGES_REQUESTED, COMPLETED, PAUSED_QUOTA, PAUSED_MANUALLY, FAILED.
UNREGISTERED is a separate registration field, not a worker status.
Tasks may use BLOCKED or PAUSED when an owner is unavailable.

## Checkpoints
Checkpoint when a provider warning is visible, operations fail because of usage restrictions,
the next operation may not finish in the available session, or the user requests a pause.
Save valid work; run feasible quick tests; commit and push implementation; update status;
write coordination/checkpoints/<agent-id>.md with last completed step, remaining acceptance criteria,
affected files, tests, known problems, commit reference and exact next action; append outbox handoff;
commit/push coordination updates; stop changing files.
If push or tests cannot complete, record the exact failure without claiming success.
Workers without GitHub write access publish checkpoints and complete files/patches to Notion and hand off in their outbox. Manager commits/pushes on their behalf with attribution. Until transferred, label the submission NOT_TRANSFERRED; never claim it is committed. Do not repeat failed authentication attempts or request credentials.
Do not infer hidden quotas. No automatic account replacement.
A replacement needs independent user authorization, registration and a new manager assignment,
normally on a new branch after reading the preserved checkpoint.

## Parallelism and review gates
Freeze relevant contracts, dependencies, paths and acceptance criteria before parallel implementation.
Frontend uses approved mock contracts for unfinished backend endpoints.
Merge only with satisfied acceptance criteria, passing relevant tests, scoped changes, updated docs,
compatible contracts, and at least one suitable review.
Security-sensitive changes need security_devops review; integration-sensitive changes need manager review.
If tests cannot run, record the exact reason and an explicit manual verification plan; do not call them passed.
Self-approval does not satisfy independent review. If a suitable reviewer is unavailable, keep the PR open.
Never claim completion without commits/PRs, passing tests without output, or deployment without live verification.

## Completion
Features and integration work; migrations and environment variable names are documented without secrets;
automated tests and major accessibility checks pass; no critical security findings remain;
release instructions and README are complete; user receives features, evidence, risks and deployment steps.
AdSense readiness is distinct from Google approval.
