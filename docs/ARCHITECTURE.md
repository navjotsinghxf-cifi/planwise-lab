# Architecture Decision Document — proposal for review
**Status:** Proposed, not approved or frozen
**Owner:** `architect-chatgpt-02`
**Issue:** #21 / ARCH-01
**Base:** `777e7b254697e301f90ce8b143ba377be2c52fc6`
**Last reviewed:** 2026-09-11
## 1. Scope and architectural principles
Planwise Lab is an English-language planning and learning site for students, freelancers, and small teams. The first release contains four deterministic tools: project planning, capacity planning, decision comparison, and study scheduling. Anonymous use is the primary path. Optional authenticated persistence is a secondary capability and must never become a prerequisite for calculations.
The architecture separates five concerns:
1. **Public presentation:** crawlable explanatory pages, guides, navigation, metadata, and static/tool landing content.
2. **Interactive workspace:** client-side state, forms, validation feedback, result views, import/export, print views, and accessibility behavior.
3. **Pure engine:** deterministic calculations with no browser, network, database, authentication, or wall-clock dependencies.
4. **Optional persistence:** authenticated private project storage, ownership enforcement, and concurrency handling.
5. **Shared contracts/validation:** versioned TypeScript types and runtime validation used at boundaries. These remain proposals until a later contract-freeze review.
Core architectural rule: **calculation correctness must not depend on persistence or authentication.** A user can open a tool, enter valid inputs, calculate results, export the workspace, close the browser, and repeat the same calculation later with the same versioned input and engine behavior.
The existing proposal of Next.js/TypeScript, pure shared engines, and optional Supabase persistence is retained but made more explicit here. It remains subject to manager/security review and a later contract freeze.
## 2. Anonymous-first workspace and public/private boundary
### Public and indexable
The following are public candidates and may be server-rendered as crawlable HTML:
- product/tool landing pages;
- tool methodology and explanatory content;
- original editorial guides;
- About, Contact, Privacy, Terms, editorial policy, and correction-process pages once real owner information exists;
- public examples that contain no private user data;
- sitemap, canonical metadata, and other search-facing metadata.
Public pages must not depend on a logged-in session. They must not expose private workspace state, draft calculations, user identifiers, or internal diagnostics.
### Private and non-indexable
The following are private application state:
- a user's saved projects;
- authenticated workspace records;
- private calculation inputs and outputs when persisted;
- account/session information;
- server-side diagnostics that could expose identifiers or infrastructure details;
- import/export data supplied by a user until explicitly published through a separate, approved product capability.
Private workspaces must be excluded from search indexing through application routing and appropriate robots/canonical behavior. Robots rules are defense-in-depth, not an authorization mechanism. Authorization must be enforced server-side for every authenticated data access.
### Anonymous browser state
Anonymous workspaces live in browser memory during the active session. An explicit user action may save them to browser storage. The UI must make save, overwrite, export, import, and delete actions clear. No automatic upload to the server occurs merely because a user calculates a plan.
## 3. Recommended stack and version policy
### Proposed baseline
<table header-row="true">
<tr>
<td>Layer</td>
<td>Recommendation</td>
<td>Rationale / status</td>
</tr>
<tr>
<td>Web framework</td>
<td>Next.js 16.3.x, App Router</td>
<td>Active LTS line; use the latest security-fixed 16.3 patch available when implementation is pinned.</td>
</tr>
<tr>
<td>UI runtime</td>
<td>React 19.3.x</td>
<td>Current stable React major/minor at review time; released 2026-09-09.</td>
</tr>
<tr>
<td>Language</td>
<td>TypeScript 6.0.x initially</td>
<td>Conservative compatibility choice for the proposed stack; TypeScript 6.0 is a stable transition release. Re-evaluate TypeScript 7 after framework/tooling compatibility is explicitly checked.</td>
</tr>
<tr>
<td>Runtime</td>
<td>Node.js 24.21.0 LTS</td>
<td>Current Node 24 LTS release at review time; prefer LTS over Current for production.</td>
</tr>
<tr>
<td>Styling</td>
<td>Tailwind CSS, version to be pinned during frontend bootstrap</td>
<td>Keep styling implementation separate from engine/contracts. Exact version requires implementation-time lockfile review.</td>
</tr>
<tr>
<td>Validation</td>
<td>Zod or equivalent runtime schema library, exact version to be pinned</td>
<td>Required at import/API boundaries; exact dependency is a contract implementation decision.</td>
</tr>
<tr>
<td>Persistence</td>
<td>Supabase PostgreSQL + Auth, optional</td>
<td>Matches existing proposal; private persistence only.</td>
</tr>
<tr>
<td>Supabase SSR</td>
<td>`@supabase/ssr`</td>
<td>Supabase currently recommends this package for cookie-based sessions in SSR frameworks such as Next.js.</td>
</tr>
<tr>
<td>Tests</td>
<td>Unit/property tests for engines; browser/accessibility tests later</td>
<td>Exact test runner is an implementation decision and is not frozen here.</td>
</tr>
</table>
Official-source verification performed 2026-09-11:
- Next.js official support policy lists 16.x as Active LTS. The official Next.js August 2026 security release recommends 16.3.3 for the security-fixed 16.x line: [https://nextjs.org/support-policy](https://nextjs.org/support-policy) and [https://nextjs.org/blog](https://nextjs.org/blog)
- React official versions page lists 19.3 as latest, with React 19.3.0 released September 9, 2026: [https://react.dev/versions](https://react.dev/versions) and [https://react.dev/blog/2026/09/09/react-19-3](https://react.dev/blog/2026/09/09/react-19-3)
- TypeScript official 6.0 release notes describe TypeScript 6.0 as the current stable transition release toward TypeScript 7.0: [https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html)
- Node.js official release page lists v24.21.0 as LTS and v26.8.2 as Current. Production should use an LTS line: [https://nodejs.org/en/download](https://nodejs.org/en/download) and [https://nodejs.org/en/about/previous-releases](https://nodejs.org/en/about/previous-releases)
- Supabase official documentation recommends `@supabase/ssr` for cookie-based sessions in SSR frameworks and provides a current Next.js quickstart: [https://supabase.com/docs/guides/auth/choosing-a-server-package](https://supabase.com/docs/guides/auth/choosing-a-server-package) and [https://supabase.com/docs/guides/getting-started/quickstarts/nextjs](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs)
**Version approval boundary:** exact package patch versions and the final lockfile are not frozen by this document. The implementation owner must verify peer dependencies and security advisories immediately before bootstrap, record the selected versions in the repository, and obtain the normal review. Do not silently substitute a major framework or runtime version.
## 4. Proposed module and ownership map
```plain text
apps/web/
  src/app/                 Next.js routes, public pages, workspace routes
  src/components/          Accessible presentation components
  src/features/            Tool-specific UI adapters and view models
  src/lib/browser/         Browser persistence/import/export helpers
  src/lib/auth/            Client/server auth adapters only
  src/server/              Authenticated persistence/application services

packages/engine/
  project/                 dependency graph, scheduling, critical path, float, PERT
  capacity/                availability, nonworking dates, allocation, overload
  decision/                normalization, weighted scoring, sensitivity, ties
  study/                   study slots, spaced reviews, impossible schedules
  shared/                   date/workday primitives and deterministic utilities

packages/contracts/
  tool input/output shapes
  version identifiers
  runtime validation schemas
  error/result discriminated unions
  import/export envelope definitions

content/guides/
  reviewed original guides and examples

tests/
  unit/                    pure engine tests
  property/                invariant/property tests
  fixtures/                independent worked examples
  frontend/                browser/component tests
  accessibility/           automated/manual evidence
  e2e/                     end-to-end flows
```
This is a proposed ownership map. It does not authorize creation of these directories in this task. Existing role reservations remain unchanged.
### Four-tool module map
<table header-row="true">
<tr>
<td>Tool</td>
<td>Engine module</td>
<td>Primary responsibilities</td>
</tr>
<tr>
<td>Project planning</td>
<td>`packages/engine/project`</td>
<td>dependency validation, cycle detection, topological scheduling, critical path, float, PERT three-point estimates</td>
</tr>
<tr>
<td>Capacity planning</td>
<td>`packages/engine/capacity`</td>
<td>weekly availability, nonworking dates, workload allocation, overload comparison, deadline preservation</td>
</tr>
<tr>
<td>Decision comparison</td>
<td>`packages/engine/decision`</td>
<td>positive weights, benefit/cost handling, normalization, weighted scores, ties, missing inputs, sensitivity</td>
</tr>
<tr>
<td>Study scheduling</td>
<td>`packages/engine/study`</td>
<td>available slots, deadlines, spaced reviews, editable sessions, impossible-schedule reporting</td>
</tr>
</table>
The engine modules must be callable independently and must not import Next.js, React, browser storage, Supabase, HTTP clients, or authentication libraries.
## 5. Deterministic calculation boundary
Every engine follows the same conceptual interface:
```plain text
validated input + explicit calculation options
        |
        v
pure deterministic engine
        |
        +--> result
        +--> structured validation/domain errors
        +--> diagnostics/warnings where needed
```
The engine must not read the current date/time implicitly. If “today” is relevant, the caller supplies an explicit reference date. If a timezone matters, it is explicit input. This prevents the same saved input from producing different results merely because it was opened on another day or machine.
Floating-point and rounding rules must be explicit. Intermediate calculations should retain sufficient precision; presentation rounding occurs at the UI boundary unless a mathematical method explicitly requires rounded intermediate values. The engine result should retain enough information for an explanation and independent verification.
### Project planning assumptions
- Task duration is represented explicitly as either calendar duration or workday duration; the mode is never inferred.
- A duration of zero is allowed only if the contract explicitly permits milestone-like tasks; negative durations are invalid.
- Dependencies are directed edges from predecessor to successor.
- Duplicate task IDs are invalid.
- Missing dependency IDs are invalid.
- Cycles are a domain error and must be reported with enough information to identify the cycle, not silently broken.
- Topological ordering must be deterministic. When multiple tasks are simultaneously eligible, use a documented stable tie-break such as task ID order.
- Critical path and float are computed only after a valid acyclic schedule exists.
- PERT expected duration uses the standard three-point estimate `(optimistic + 4 * mostLikely + pessimistic) / 6` when that method is selected. Estimates must satisfy the selected domain constraints, such as optimistic \<= mostLikely \<= pessimistic.
- Calendar-day and workday scheduling are separate modes. Workday calculations require an explicit working-calendar definition.
- A schedule that cannot satisfy constraints must return an impossible-schedule/domain result rather than silently dropping dependencies or moving a deadline.
### Capacity planning assumptions
- Each person has explicit weekly availability, represented in hours or another single declared unit.
- Nonworking dates are explicit calendar dates. If recurring holidays are later supported, recurrence rules must be normalized before engine calculation.
- Allocation cannot exceed the defined availability without producing an overload result/warning.
- Capacity planning does not silently move project deadlines. If demand exceeds capacity, the result reports overload, remaining demand, or an explicit scheduling consequence.
- Workload allocation must be deterministic when multiple people are equally eligible. A stable person identifier is the final tie-breaker.
- Time zones are not inferred from browser locale for persisted calculations; any date/time-sensitive contract must carry the intended calendar/timezone semantics.
### Decision comparison assumptions
- Criteria weights must be positive and their normalization rule must be explicit.
- Benefit criteria score higher values as better; cost criteria invert the direction through the documented normalization function.
- Missing criterion values are not treated as zero unless the contract explicitly says so. Default behavior should produce a structured missing-input error or a clearly defined incomplete result.
- Ties are first-class results. Do not force a unique winner by arbitrary ordering.
- If sensitivity analysis produces equal or near-equal scores, preserve the tie/range information rather than presenting false precision.
- Numeric normalization must define behavior when all alternatives have the same value for a criterion, including the zero-range case.
- Invalid, negative, NaN, infinite, or otherwise non-finite numeric inputs are rejected at the validation boundary.
### Study scheduling assumptions
- Topics have explicit identifiers and estimated effort/duration where required by the selected scheduling method.
- Available study slots are explicit. A slot is not invented because the browser happens to have free time.
- Deadline semantics are explicit, including whether a session ending exactly at the deadline is valid.
- Spaced reviews are generated from a documented interval policy. The policy is a calculation option, not a claim of guaranteed learning outcomes.
- If the requested workload cannot fit before a deadline, return an impossible-schedule result identifying the limiting constraint(s).
- Editing a generated session produces user-owned state. Recalculation must define whether edited sessions are preserved, regenerated, or treated as fixed constraints. This behavior must be frozen in the later contract review.
- When several valid sessions have equal priority, use deterministic tie-breaking based on explicit stable fields.
## 6. Invalid input, cycle, impossible-schedule, and tie handling
These are engine-level domain concepts, not UI-only messages.
- **Invalid input:** rejected by shared boundary validation before engine execution where possible; engine still protects its invariants.
- **Cycle:** project-engine domain error after dependency graph validation. It must include a reproducible representation of the detected cycle or affected nodes.
- **Impossible schedule:** a validly shaped request whose constraints cannot all be satisfied. It is a domain result, not a generic validation error.
- **Tie:** a valid calculation result containing multiple equally ranked/critical candidates. The engine preserves the tie; UI decides how to explain it.
- **Warning:** non-fatal information that does not invalidate the calculation, such as overload or sensitivity. Warnings must be structured, not embedded only in prose.
This separation prevents the frontend from having to reverse-engineer whether a message means malformed data, a mathematically impossible request, or a legitimate tie.
## 7. Data flow
### Anonymous calculation
```plain text
Public route / workspace
        |
        v
UI input model
        |
        v
runtime validation
        |
        v
versioned engine input
        |
        v
pure engine
        |
        v
versioned engine result
        |
        +--> result view
        +--> explanation / warnings
        +--> print view
        +--> browser save
        +--> JSON export
```
No server request is required for this path.
### Optional authenticated save
```plain text
browser workspace
   -> explicit Save
   -> authenticated request
   -> server authorization
   -> ownership-scoped persistence operation
   -> database
   -> version/concurrency result
   -> browser state
```
The browser must never receive a server secret or a database service-role credential. Server access must use the authenticated user's identity and database row-level security or an equivalently strong ownership boundary.
### Public content
Public content should be statically rendered or server-rendered into crawlable HTML. Interactive tool pages may hydrate client components after initial content is available. Public content and private workspace data use separate route/data boundaries so that a private record cannot accidentally become part of an indexable page.
## 8. Browser persistence, import/export, and versioning
Browser persistence is a convenience layer, not the canonical shared database.
Recommended envelope shape at the architectural level:
```json
{
  "format": "planwise-workspace",
  "schemaVersion": 1,
  "tool": "project",
  "savedAt": "2026-09-11T00:00:00Z",
  "payload": {}
}
```
The exact TypeScript schema belongs in `packages/contracts/` and is intentionally not frozen here.
Rules:
1. Every export includes a format identifier and schema version.
2. Imports are parsed as untrusted data.
3. Validate the complete envelope before replacing current workspace state.
4. Unknown future versions are rejected with a recoverable message unless an explicit migration exists.
5. Older supported versions may be migrated through deterministic, versioned migration functions.
6. Never execute imported data as code or treat imported strings as trusted HTML.
7. Use size limits to protect the browser and server. Proposed initial limit: 1 MiB per JSON workspace export and 10 MiB total browser-managed workspace data per origin. These values require implementation/UX review and may be reduced on constrained devices.
8. Limit collection sizes such as task count, criteria count, and study sessions to values that can be validated and benchmarked. The 200-task requirement is the primary performance target; proposed higher hard limits should not be accepted without benchmark evidence.
9. Exported timestamps are metadata, not hidden scheduling inputs. Calculation reference dates remain explicit in the payload/options.
10. A failed import must leave the current valid workspace unchanged.
## 9. Authentication and ownership trust boundaries
Authentication is optional for the product's core path.
**Boundary A: browser to public application**
Treat all client data as untrusted. Client-side validation improves UX but is not authorization.
**Boundary B: browser to authenticated server**
The server establishes identity from the authenticated session. It must not trust a user ID supplied in request JSON, URL parameters, or hidden form fields as proof of ownership.
**Boundary C: application to database**
Every private read/write is ownership-scoped. Supabase Row Level Security is the preferred database enforcement layer if Supabase is retained. Server-side checks remain explicit for sensitive operations and error handling.
**Boundary D: public rendering/search**
No authenticated workspace record is rendered into public pages or metadata. Private IDs must not be used as public canonical URLs.
**Boundary E: import/export**
Imported JSON is hostile input. Enforce schema, size, depth/collection limits, numeric validity, string limits, and safe rendering. Never render imported HTML directly.
**Boundary F: credentials and secrets**
Only public client configuration may be exposed to browser code. Database service-role keys and other privileged secrets stay server-side. No secret is stored in source control or an export file.
## 10. Accessibility and 200-task performance
The architecture supports accessibility by keeping calculations independent of visualization libraries and requiring every chart to have a tabular/text equivalent. Result explanations must remain usable without color, hover, animation, or pointer interaction.
Required UI architecture principles:
- semantic headings and landmarks;
- keyboard-operable controls and reorder/edit actions;
- visible focus indicators;
- labels and programmatic relationships for inputs and errors;
- status updates that are announced appropriately without trapping focus;
- tables or text summaries for chart data;
- no essential information conveyed by color alone;
- reduced-motion behavior where animation is used;
- responsive layouts without horizontal scrolling for ordinary task workflows.
For 200 tasks, the engine should remain pure and run synchronously only when measured to remain responsive. If profiling shows expensive recalculation, use memoization, incremental recalculation, worker-based computation, or deferred rendering at the UI boundary without changing deterministic engine semantics.
The 200-task benchmark must record hardware, browser, dataset characteristics, calculation type, cold/warm state, and measured latency. The project brief's responsiveness target is a product acceptance target, not a claim that this architecture has already met it.
## 11. Security and privacy risks
<table header-row="true">
<tr>
<td>Risk</td>
<td>Architectural mitigation</td>
<td>Review owner</td>
</tr>
<tr>
<td>Cross-user data access</td>
<td>authenticated ownership checks + RLS</td>
<td>security_devops + backend</td>
</tr>
<tr>
<td>Import-based XSS</td>
<td>strict JSON validation; no raw HTML execution</td>
<td>security_devops + frontend</td>
</tr>
<tr>
<td>Oversized/deep imports</td>
<td>byte, collection, depth, and field limits</td>
<td>backend + security_devops</td>
</tr>
<tr>
<td>IDOR through private URLs</td>
<td>server-side authorization independent of supplied IDs</td>
<td>backend + security_devops</td>
</tr>
<tr>
<td>Secret exposure</td>
<td>server-only privileged credentials; public publishable configuration only</td>
<td>security_devops</td>
</tr>
<tr>
<td>Search indexing of private data</td>
<td>route/data separation + indexing controls; authorization remains primary</td>
<td>frontend + security_devops</td>
</tr>
<tr>
<td>Nondeterministic calculations</td>
<td>explicit dates/timezones/options; pure engine</td>
<td>architect + backend</td>
</tr>
<tr>
<td>Floating-point presentation errors</td>
<td>documented precision/rounding boundary</td>
<td>architect + QA</td>
</tr>
<tr>
<td>Dependency vulnerabilities</td>
<td>lockfile, supported LTS versions, CI audit/review</td>
<td>security_devops</td>
</tr>
<tr>
<td>Sensitive data in logs</td>
<td>structured error handling and redaction policy</td>
<td>backend + security_devops</td>
</tr>
<tr>
<td>Repeated expensive calculations</td>
<td>input limits and benchmark-driven optimization</td>
<td>backend + frontend</td>
</tr>
<tr>
<td>CSRF/session mistakes</td>
<td>framework-supported cookie/session handling and security review</td>
<td>security_devops</td>
</tr>
</table>
Advertising remains disabled by default. No AdSense approval, publisher identity, contact identity, ads.txt identifier, or account eligibility is invented by this architecture.
## 12. Test architecture
### Engine layer
- deterministic unit tests for each calculation rule;
- property/invariant tests for graph validity, monotonicity where mathematically applicable, conservation/availability constraints, and normalization behavior;
- invalid-input tests;
- cycle detection tests;
- impossible-schedule tests;
- tie and stable-order tests;
- date-boundary and nonworking-day tests;
- floating-point/rounding tests;
- 200-task benchmark.
### Contract layer
- runtime schema validation for valid and invalid examples;
- version migration tests;
- engine mock compatibility;
- import/export round-trip tests.
### Browser layer
- keyboard navigation;
- accessible validation and error recovery;
- import/export failure recovery;
- print view;
- responsive behavior;
- anonymous operation without network persistence;
- optional authenticated save flows once implemented.
### Security layer
- cross-user access denial;
- malformed/oversized imports;
- XSS payload handling;
- authentication/session boundary tests;
- private-route indexing checks;
- dependency and secret scanning.
No application tests are claimed as passed by this architecture submission. The above are required test layers for subsequent implementation.
## 13. Worked-example strategy
Each tool should have at least one small, independently reproducible example in tests/fixtures and one explanatory public example after editorial review.
Examples should include:
- Project: a small dependency graph with a critical path, one noncritical task with float, and a separate cyclic invalid example.
- Capacity: two people with different weekly availability and a nonworking date that creates an overload without silently moving the deadline.
- Decision: three alternatives, benefit and cost criteria, normalized positive weights, plus an intentional tie.
- Study: a deadline with available slots that fits, followed by the same workload with insufficient slots producing an impossible-schedule result.
Worked examples must state inputs, assumptions, expected output, units, dates, and rounding rules so another implementation can reproduce them without relying on the UI.
## 14. Proposed implementation ownership map
<table header-row="true">
<tr>
<td>Path</td>
<td>Proposed owner</td>
<td>Boundary</td>
</tr>
<tr>
<td>`docs/ARCHITECTURE.md`</td>
<td>architect</td>
<td>architecture decisions and rationale</td>
</tr>
<tr>
<td>`docs/API_CONTRACT.md`</td>
<td>architect</td>
<td>later reviewed API contract</td>
</tr>
<tr>
<td>`docs/DATABASE_SCHEMA.md`</td>
<td>architect</td>
<td>later reviewed persistence model</td>
</tr>
<tr>
<td>`packages/contracts/`</td>
<td>architect with backend/frontend review</td>
<td>shared types and validation</td>
</tr>
<tr>
<td>`packages/engine/`</td>
<td>backend</td>
<td>pure deterministic algorithms</td>
</tr>
<tr>
<td>`apps/web/`</td>
<td>frontend</td>
<td>presentation, workspace and public pages</td>
</tr>
<tr>
<td>`apps/web/src/app/api/`</td>
<td>backend</td>
<td>authenticated API surface</td>
</tr>
<tr>
<td>`apps/web/src/server/`</td>
<td>backend</td>
<td>persistence/application services</td>
</tr>
<tr>
<td>`supabase/`</td>
<td>backend + security_devops review</td>
<td>database/auth configuration</td>
</tr>
<tr>
<td>`content/`</td>
<td>content/editorial owner</td>
<td>original guides and publisher drafts</td>
</tr>
<tr>
<td>`tests/frontend/`, `tests/e2e/`</td>
<td>QA/frontend</td>
<td>browser and interaction coverage</td>
</tr>
<tr>
<td>`tests/accessibility/`</td>
<td>QA</td>
<td>automated/manual accessibility evidence</td>
</tr>
<tr>
<td>`.github/`</td>
<td>security_devops with manager coordination</td>
<td>CI/security/deployment controls</td>
</tr>
<tr>
<td>`docs/ADSENSE_READINESS.md`</td>
<td>security_devops + manager</td>
<td>release/readiness evidence</td>
</tr>
</table>
This map is proposed. It does not alter existing role reservations or assign implementation work.
## 15. Next small contract deliverable
The next bounded architecture deliverable should be `packages/contracts/` plus the corresponding `docs/API_CONTRACT.md` update, after this document is independently reviewed and approved.
That contract task should define, for each of the four tools:
1. versioned input and output schemas;
2. structured error/result types;
3. date, timezone, workday, precision, and rounding semantics;
4. import/export envelope and migration rules;
5. mock fixtures and at least one valid/invalid example;
6. deterministic tie and impossible-schedule representations;
7. ownership/auth boundary inputs for persisted operations without coupling the pure engine to authentication.
No contract freeze occurs until the manager records approval and the required security/architecture review gates are satisfied.
## 16. Unresolved decisions and deferred inputs
1. Exact package patch versions and lockfile are pending implementation-time verification.
2. Exact runtime test framework is not frozen.
3. Exact persistence API shape and database schema are not frozen.
4. Browser storage technology and quota-handling strategy need implementation validation.
5. Import/export hard limits need benchmark and UX confirmation.
6. Study-session edit/recalculation semantics need contract review.
7. Workday calendar model needs contract review, including locale/holiday behavior.
8. Authentication provider configuration is not activated.
9. Hosting/deployment target is proposed but unactivated.
10. Owner publisher identity, contact route, domain, ad account eligibility, and production/account configuration remain release inputs.
11. AdSense readiness is not AdSense approval.
12. No production deployment, paid activation, domain change, or advertising activation is authorized by this document.
## 17. Requirement-to-section checklist
<table header-row="true">
<tr>
<td>Issue #21 requirement</td>
<td>Section(s)</td>
<td>Status</td>
</tr>
<tr>
<td>Anonymous-first browser workspace; deterministic engine; optional private persistence; public vs private</td>
<td>1, 2, 6, 7, 8, 9</td>
<td>Covered</td>
</tr>
<tr>
<td>Stack and compatible versions with official-source verification; approval choices</td>
<td>3</td>
<td>Covered; exact package lock remains pending</td>
</tr>
<tr>
<td>All four tools, numeric/date/workday assumptions, cycle/invalid/impossible/tie handling</td>
<td>5, 6</td>
<td>Covered</td>
</tr>
<tr>
<td>Data flow, browser persistence/import/export versioning and limits</td>
<td>7, 8</td>
<td>Covered; proposed limits require approval</td>
</tr>
<tr>
<td>Authentication/ownership trust boundaries</td>
<td>9</td>
<td>Covered</td>
</tr>
<tr>
<td>Accessibility and 200-task performance</td>
<td>10</td>
<td>Covered; benchmark evidence remains future work</td>
</tr>
<tr>
<td>Practical folder/path ownership map</td>
<td>4, 14</td>
<td>Covered</td>
</tr>
<tr>
<td>Next small contract deliverable</td>
<td>15</td>
<td>Covered</td>
</tr>
<tr>
<td>Test layers and independent worked examples</td>
<td>12, 13</td>
<td>Covered; no tests claimed passed</td>
</tr>
<tr>
<td>Key security risks</td>
<td>11</td>
<td>Covered</td>
</tr>
<tr>
<td>Unresolved decisions and deferred deployment/account inputs</td>
<td>16</td>
<td>Covered</td>
</tr>
<tr>
<td>No invented publisher identity or AdSense guarantee</td>
<td>11, 16</td>
<td>Covered</td>
</tr>
<tr>
<td>Internal references and official version citations</td>
<td>3, 17</td>
<td>Covered</td>
</tr>
<tr>
<td>Actual check evidence and limitations</td>
<td>18</td>
<td>Covered</td>
</tr>
</table>
## 18. Checks and evidence
### Check A — source/input review
**Command/tool action:** fetched the issue and required repository inputs from approved base `777e7b254697e301f90ce8b143ba377be2c52fc6`.
**Evidence:** issue #21, `AGENTS.md`, `docs/PROJECT_BRIEF.md`, existing `docs/ARCHITECTURE.md`, `docs/ADSENSE_READINESS.md`, `docs/NOTION_WORKFLOW.md`, `coordination/MASTER_TASKS.md`, and `coordination/DECISIONS.md` were read before drafting.
**Result:** PASS for source review. No application files were edited.
### Check B — official version/source verification
**Result:** PASS for current-source review on 2026-09-11.
- Next.js 16.x is Active LTS; official Next.js security guidance identifies 16.3.3 as the security-fixed 16.x release in August 2026.
- React 19.3.0 is the current stable release listed by the official React versions page and release post.
- TypeScript 6.0 official release notes were reviewed. TypeScript 7 is not adopted as a frozen project requirement because framework/toolchain compatibility still needs explicit implementation-time verification.
- Node.js 24.21.0 is the current LTS release listed by the official Node.js download/release pages.
- Supabase's current official documentation recommends `@supabase/ssr` for cookie-based SSR sessions and documents Next.js integration.
### Check C — internal-reference consistency
**Result:** PASS by document review.
Referenced repository paths exist in the approved-base inputs or are explicitly proposed future paths. The document does not treat proposed future directories as existing implementation. Issue #21 is the source of assignment scope and allowed-path limits.
### Check D — `git diff --check`
**Result:** NOT RUN.
**Exact limitation:** this submission session has repository read/inspection access and Notion publication capability, but no local Git working tree/branch was created and no GitHub write operation was required by issue #21. Therefore a local `git diff --check` against a worker branch cannot honestly be reported as executed.
**Manual verification procedure:** manager transfers the exact UTF-8 file content to `docs/ARCHITECTURE.md` on a fresh branch from the latest approved main, runs `git diff --check`, inspects the scoped diff, and records the command output in the transfer PR.
### Check E — application tests
**Result:** NOT RUN / NOT APPLICABLE to this design-only submission.
No application implementation exists in this task, so no application test pass is claimed. The future test layers are specified in Section 12.
## 19. Submission and review boundary
This document is a proposed architecture decision record only. It does not freeze APIs, schemas, engine contracts, UI behavior, authentication configuration, deployment, or advertising.
Manager should transfer the artifact to a fresh scoped PR from the latest approved main, preserve the original Notion submission and source attribution, verify the exact file content/path/hash, run the feasible checks above, and obtain independent manager and security-devops review. Changes to this document after review require a new submission/review cycle.
