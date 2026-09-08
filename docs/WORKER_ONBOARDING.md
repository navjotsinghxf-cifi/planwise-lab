# Independent worker onboarding

Six independent user-authorized workers are needed: architect, designer, frontend, backend, qa, security_devops.
The manager does not create/control consumer sessions, add accounts or share credentials.
The user opens each worker in an independently authorized environment with its own legitimate repository access.

## Copy this instruction into each worker session
You are the <ROLE> worker for https://github.com/navjotsinghxf-cifi/planwise-lab.
Your authorization comes from the user opening this session, not from another worker.
Clone the repository using your already-authorized GitHub access; never request or expose credentials.
Read AGENTS.md, docs/PROJECT_BRIEF.md, coordination/MASTER_TASKS.md, coordination/DECISIONS.md and coordination/inbox/<ROLE>.txt.
Find the manager's worker-registration GitHub issue in MASTER_TASKS.
Create branch agent/<ROLE>/<registration-issue-number>-register.
Append your own registration entry with a unique AGENT_ID, role, AVAILABLE status, branch,
CURRENT_ISSUE: NONE, capabilities, LIMIT_WARNING_VISIBLE: NO and actual UTC update timestamp.
Update only your own status/outbox; append registration without changing others.
Open a registration PR referencing the registration issue. Do not claim implementation ownership.
Wait until the manager approves registration and gives you a specific implementation issue.
Then use a fresh agent/<ROLE>/<issue-number>-<short-name> branch from approved main.
Follow scoped paths, approved contracts, review gates and checkpointing requirements.

## Registration acceptance
Manager verifies role availability, user authorization, unique ID, scope, branch and capabilities.
Workers sharing the same GitHub identity still need genuinely separate sessions and review evidence.
GitHub may prohibit self-approval; do not bypass or label it independent approval.
Registration is not proof that implementation has started or that a worker is still available.

## Coordination
The manager inspects status when this task is resumed; no continuous monitor has been configured.
Ask the user to return here once registration PRs are ready.
No implementation assignment is made until registration is approved.
