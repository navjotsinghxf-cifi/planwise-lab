# API contract — not frozen
Architect owns initial specification and packages/contracts.
Specify versioned project documents for project, capacity, decision and study tools;
input ranges/limits, errors, dates/time zones, schema evolution, import validation and examples.
Proposed persistence operations: list, create, read, update and delete current user's projects.
Define authentication, ownership, conflict/version semantics, pagination, size limits, rate limits and error envelopes.
Include anonymous engine interfaces and approved mocks so frontend can proceed independently of server implementation.
No endpoint name or schema in this bootstrap is an approved contract.

## Project planner v1.1 — proposed, not frozen

The anonymous project planner exposes exactly:
```plain text
ProjectPlanner.calculate(input: ProjectInput): ProjectResponse
```
`ProjectInput`, `ProjectResponse`, `ProjectWorkspaceEnvelope`, and the planner interface are framework/runtime independent and live under `packages/contracts/project/index.ts`. The engine must not depend on browser state, network, wall clock, authentication, account identity, persistence, or database access.
Scheduling uses half-open numeric intervals `[start, finish)`. `earliestFinish` and `latestFinish` are exclusive elapsed offsets and satisfy `finish = start + duration` within the engine numeric tolerance. Display `finishOffset` and `finishDate` identify the last occupied displayed unit, using `ceil(exclusiveFinish)-1` for positive duration and the start position for zero duration. PERT expected duration is `(O + 4M + P)/6` when enabled; when disabled, PERT tasks use `mostLikely` deterministically and no expected-duration entry is emitted. Zero-duration milestones complete immediately, so a successor may have the same numeric start offset.
Calendar weekdays use 0 Sunday through 6 Saturday. Workday dates are eligible only when the weekday is listed and the date is not in `nonWorkingDates`. Task and dependency ordering is deterministic by stable task ID and edge tuple. Forward pass computes earliest times; backward pass computes latest times from project duration; `float = latestStart - earliestStart`. A critical edge requires successor earliest start equal predecessor earliest finish and zero float at both endpoints. Zero-float nodes alone do not define critical paths.
`criticalPaths` is bounded to 1024 emitted paths. `totalPathCount` is an exact decimal string. `truncated=true` means the emitted list is not exhaustive. Consumers must inspect `truncated` before assuming all critical paths were returned.
`ProjectResponse` is a discriminated union. Success is `{ ok: true, result }`; failure is `{ ok: false, error }`. Schema validation handles structure, types, known fields, version and primitive limits. Domain validation handles duplicate IDs, dependency references, cycles, PERT ordering, calendar semantics, deadline combinations and non-finite in-memory numbers. JSON cannot encode NaN/Infinity, so those require direct in-memory domain tests.
Import/export uses `ProjectWorkspaceEnvelope`: `format=planwise-workspace`, `schemaVersion=2`, `tool=project`, ISO-8601 `savedAt`, and a `ProjectInput` payload. The envelope has no identity/auth/session/account/database fields. Raw UTF-8 byte length must be checked before parsing. Enforce depth, aggregate string, traversal, task, edge, duration and date-horizon limits. Parse into a fresh candidate and replace current workspace only after all checks succeed. Any failed import leaves the prior valid workspace unchanged. Unsupported versions are rejected; v1.1 defines no automatic migration.
