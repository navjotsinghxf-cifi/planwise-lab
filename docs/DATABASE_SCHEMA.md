# Database schema — not frozen
Architect specifies; backend implements reviewed migrations.
Proposed entities: authenticated users managed by auth provider and private saved projects with owner,
tool kind, schema version, validated document, optimistic version and timestamps.
Specify foreign keys, indexes, deletion behavior, maximum document size and row-level policies for every operation.
Test cross-user reads/writes/deletes, anonymous denial and concurrent update conflicts.
Do not store calculation drafts remotely without user action.
Document forward migrations, rollback limitations and safe nonproduction verification.
