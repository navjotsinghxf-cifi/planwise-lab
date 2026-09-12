# API contract — not frozen
Architect owns initial specification and packages/contracts.
Specify versioned project documents for project, capacity, decision and study tools;
input ranges/limits, errors, dates/time zones, schema evolution, import validation and examples.
Proposed persistence operations: list, create, read, update and delete current user's projects.
Define authentication, ownership, conflict/version semantics, pagination, size limits, rate limits and error envelopes.
Include anonymous engine interfaces and approved mocks so frontend can proceed independently of server implementation.
No endpoint name or schema in this bootstrap is an approved contract.

## Project planner v1 — proposed, not frozen

The anonymous engine boundary is:
```plain text
ProjectPlanner.calculate(input: ProjectInput): ProjectResponse
```
Input is `ProjectInput` from `packages/contracts/project/index.ts`. The engine has no framework, browser, network, auth, persistence or wall-clock dependency. Frontend/backend consumers must treat `ProjectResponse` as the shared source of truth. The mock adapter has the same public method signature.
A successful result contains deterministic schedule entries, earliest/latest values, float, critical paths, PERT expected-duration values where requested, warnings, and optional deadline feasibility. Failure is a discriminated `{ ok: false, error }` response with stable machine-readable error codes. Cycle and impossible-schedule states are domain outcomes, not schema failures.
Import/export uses the versioned `ProjectWorkspaceEnvelope`. Imports are untrusted and must be bounded and fully validated before replacing workspace state. Cloud identity/auth fields are forbidden in this anonymous envelope.
