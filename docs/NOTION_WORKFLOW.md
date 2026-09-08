# Notion operational workflow

Mailbox: https://app.notion.com/p/3d5e4d9a8cbb80ec9810f1c552f51861

This workflow takes effect after independent review and merge of the coordination PR for issue #12. While pending, user-authorized mailbox setup, registration requests and administrative workflow review may proceed; implementation remains blocked.

## Authority and channels
GitHub main is the accepted source for code, specs, registrations and decisions. Issues define ownership, paths and acceptance criteria. Notion is the operational transport, not an approval substitute. Conflicts with main require a proposed GitHub change and recorded approval.
Preserve TEST-001 and TEST-002 and all message history. Each role has a separate inbox (manager writes) and outbox (worker writes). Registration has separate inbox/outbox pages for the two actual connected sessions until roles are resolved. Remaining roles stay vacant. Deliverables use a separate child page per submission/revision; messages link to artifacts rather than embedding long files.
Every message includes MESSAGE_ID, TIMESTAMP_UTC, FROM, TO, RELATED_TASK, PRIORITY, MESSAGE and RESPONSE_REQUIRED. Replies include REPLY_TO. Manager appends HANDLED_BY, HANDLED_AT_UTC and RESULT_REFERENCE after verifying evidence; never rewrites old messages.

## Submission and transfer
Each deliverable includes author AGENT_ID, role, issue, message ID, source URL, UTC timestamp, approved base commit, exact file paths, full files or unified patch, required checks with actual output, limitations and remaining criteria. Do not include secrets or invent Git identities.
Manager fetches the artifact, inspects all files, checks path scope and base commit, and transfers valid work to a fresh scoped branch from latest approved main. Resolve stale bases with the author; never silently change frozen contracts. Preserve original submission and record manager adjustments separately.
Each transfer PR includes source URL/message ID, author AGENT_ID, base commit, transferred file list and manager verification evidence. Use commit trailers Source-URL and Worker-Agent-ID; use Co-authored-by only when the author provided a legitimate identity. Public GitHub evidence must omit personal contact details and secrets.
Direct worker PRs remain supported. Both routes require the same tests and independent review. Submission statuses are SUBMITTED, NOT_TRANSFERRED, TRANSFERRED_TO_PR, CHANGES_REQUESTED and ACCEPTED; these are artifact states, not new worker status values. Only merged accepted artifacts satisfy dependencies.

## Independent review
An independently authorized, suitably capable reviewer may publish review evidence in Notion when GitHub writes are unavailable. Identify reviewer AGENT_ID/session, independence, exact PR head SHA, scope, findings and APPROVE or CHANGES_REQUESTED. Manager copies a faithful attributed record and source link into the PR. This is external review evidence, never a GitHub approval impersonation; platform-required approvals still apply. Changed material requires renewed review.
For the initial administrative workflow PR only, the existing connected sessions may review before registration approval after identifying themselves and confirming user authorization/capability. This administrative exception permits no implementation. Manager cannot independently approve their own PR. Keep it open until suitable review exists; unresolved policy choices go to the user with the concrete diff.
Security-sensitive changes require security_devops review. Integration-sensitive changes require manager review; manager-authored changes also need an independent reviewer. Run feasible checks and state exact reasons for unavailable tests. No deployment, paid activation, domain change, destructive database action or AdSense submission without explicit owner approval.

## Checkpoints
Workers without GitHub writing publish recoverable files/patches and checkpoints to Notion, mark NOT_TRANSFERRED, and link them from their outbox. Manager transfers and commits/pushes with attribution. Record failures exactly. No automatic session replacement or credential sharing.
