# Independent worker onboarding

Worker roles are: architect, designer, frontend, backend, qa, security_devops.
Workers are independent user-authorized sessions. Manager does not launch sessions, create accounts or request credentials. Platform names do not determine roles.

## Registration
Read AGENTS.md, docs/PROJECT_BRIEF.md, coordination/MASTER_TASKS.md, coordination/DECISIONS.md and docs/NOTION_WORKFLOW.md from approved main.
Open the Notion mailbox and the registration inbox for your verified unique AGENT_ID/session. Ask manager to resolve conflicting identities before proceeding. Do not reuse another session channel. Claude channels are historical only; the user discontinued that session. Consult accepted registrations to determine role availability.
Reply in that session's registration outbox with a unique AGENT_ID, one requested role, AVAILABLE status, CURRENT_ISSUE: NONE, actual UTC timestamp, capabilities, user authorization confirmation, GitHub read/write capability, and branch (NONE if unavailable). Do not retry GitHub authentication to register.
Manager checks role availability, independent user authorization and capabilities, resolves duplicate claims, and records registration through a PR associated with issue #1. Direct registration PRs remain supported on agent/<role>/1-register.
Requests and connection tests do not authorize implementation. Wait for approved registration, approved workflow, and a scoped issue assignment in your role inbox and GitHub.

## Assigned work
Use the latest approved main commit specified in the assignment. Work only within its allowed paths and contracts. Workers with GitHub access use agent/<role>/<issue-number>-<short-name>; other workers submit complete files or patches through Notion for manager transfer.
Publish tests with exact commands, environment, output and limitations. Follow the checkpoint and attribution rules in docs/NOTION_WORKFLOW.md.

## Review and wakeups
Reviews must be independent of the artifact author and identify the reviewed commit and evidence. Shared GitHub identities do not turn self-approval into independent review.
Workers do not wake automatically. The user sends a short inbox-check prompt; responses and artifacts travel through Notion. No continuous monitoring is configured.
