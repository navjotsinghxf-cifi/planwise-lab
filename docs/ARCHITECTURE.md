# Architecture Decision Document — Revision 2
**Status:** Proposed, not approved or frozen
**Owner:** `architect-chatgpt-02`
**Issue:** #21 / ARCH-01
**Base:** `777e7b254697e301f90ce8b143ba377be2c52fc6`
**Revision:** 2
**Last reviewed:** 2026-09-12
## 1. Scope and architectural principles
Planwise Lab is an English-language planning and learning site for students, freelancers, and small teams. The first release contains four deterministic tools: project planning, capacity planning, decision comparison, and study scheduling. Anonymous use is the primary path. Optional authenticated persistence is secondary and must never become a prerequisite for calculations.
The architecture separates five concerns:
1. **Public presentation:** crawlable explanatory pages, guides, navigation, metadata, and static/tool landing content.
2. **Interactive workspace:** client-side state, forms, validation feedback, result views, import/export, print views, and accessibility behavior.
3. **Pure engine:** deterministic calculations with no browser, network, database, authentication, or wall-clock dependencies.
4. **Optional persistence:** authenticated private project storage, ownership enforcement, and concurrency handling.
5. **Shared contracts/validation:** versioned TypeScript types and runtime validation used at boundaries. These remain proposals until a later contract-freeze review.
Core rule: **calculation correctness must not depend on persistence or authentication.** The same versioned input and explicit calculation options must produce reproducible engine behavior independent of browser, network, database, or current clock.
The existing Next.js/TypeScript, pure shared engines, and optional Supabase proposal is retained. This document recommends boundaries and checks; it does not silently freeze implementation choices.
## 2. Anonymous-first workspace and public/private boundary
### Public and indexable
Public candidates may include tool landing pages, methodology/explanatory content, original editorial guides, About/Contact/Privacy/Terms/editorial-policy pages once real owner information exists, public examples without private data, sitemap output, canonical metadata, and other search-facing metadata.
Public pages must not depend on a logged-in session and must not expose private workspace state, draft calculations, user identifiers, internal diagnostics, or authenticated state.
### Private and non-indexable
Private state includes saved projects, authenticated workspace records, persisted private inputs/outputs, account/session information, server diagnostics that could expose identifiers/infrastructure, and user import/export data until explicitly published through a separate approved capability.
Private routes must emit an explicit non-indexable policy and must not be placed in generated sitemap output or public metadata. Authenticated/private responses must not be shared through public/static caches. Robots/canonical behavior is defense-in-depth only. Authorization is server-side.
### Anonymous browser state
Anonymous workspaces live in browser memory during the active session. Explicit user action may save them to browser storage. Save, overwrite, export, import, and delete must be clear. No automatic upload occurs merely because a user calculates a plan.
## 3. Recommended stack and version policy
### Proposed baseline
<table header-row="true">
<tr>
<td>Layer</td>
<td>Recommendation</td>
<td>Status</td>
</tr>
<tr>
<td>Web framework</td>
<td>Next.js 16.3.x, App Router</td>
<td>Proposed Active-LTS line; exact patch must be revalidated before bootstrap.</td>
</tr>
<tr>
<td>UI runtime</td>
<td>React 19.3.x + matching react-dom</td>
<td>Proposed current stable line at review time; exact dependency lock remains unverified.</td>
</tr>
<tr>
<td>Language</td>
<td>TypeScript 6.0.x initially</td>
<td>Proposed; exact framework/toolchain compatibility is unverified.</td>
</tr>
<tr>
<td>Runtime</td>
<td>Node.js 24.21.0 LTS</td>
<td>Proposed LTS runtime; exact repository build compatibility remains a bootstrap check.</td>
</tr>
<tr>
<td>Styling</td>
<td>Tailwind CSS, version pinned during bootstrap</td>
<td>Proposed; exact version not frozen.</td>
</tr>
<tr>
<td>Validation</td>
<td>Zod or equivalent runtime schema library</td>
<td>Required boundary capability; exact package/version not frozen.</td>
</tr>
<tr>
<td>Persistence</td>
<td>Supabase PostgreSQL + Auth, optional</td>
<td>Private persistence only; retained from existing proposal.</td>
</tr>
<tr>
<td>SSR auth</td>
<td>`@supabase/ssr`</td>
<td>Recommended by current Supabase SSR guidance; exact version not frozen.</td>
</tr>
<tr>
<td>Tests</td>
<td>Unit/property engine tests; browser/accessibility tests later</td>
<td>Exact test runner not frozen.</td>
</tr>
</table>
### Inspectable official-source evidence
Accessed/reviewed **2026-09-12 UTC**:
- Next.js installation requirements: [https://nextjs.org/docs/app/getting-started/installation](https://nextjs.org/docs/app/getting-started/installation) . The official documentation states Node.js \>=20.9 and TypeScript \>=5.1.0 and documents installation of `next`, `react`, and `react-dom`.
- Next.js support policy: [https://nextjs.org/support-policy](https://nextjs.org/support-policy) . It identifies the 16.x line as Active LTS.
- Next.js security guidance/blog: [https://nextjs.org/blog](https://nextjs.org/blog) . The August 2026 security guidance identifies 16.3.3 as the security-fixed 16.x release.
- Next.js 16.3.4 package page: [https://www.npmjs.com/package/next/v/16.3.4](https://www.npmjs.com/package/next/v/16.3.4) . This establishes that the exact proposed patch exists; it does **not** prove the repository dependency combination is compatible.
- React versions: [https://react.dev/versions](https://react.dev/versions) . React 19.3 is listed as the latest release line.
- React 19.3 release: [https://react.dev/blog/2026/09/09/react-19-3](https://react.dev/blog/2026/09/09/react-19-3) . React 19.3.0 release date is 2026-09-09.
- react-dom 19.3.0 package page: [https://www.npmjs.com/package/react-dom/v/19.3.0](https://www.npmjs.com/package/react-dom/v/19.3.0) . The matching package exists.
- TypeScript 6.0 release notes: [https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-6-0.html) . This establishes the 6.0 release line, not exact Next.js/toolchain compatibility.
- Node.js download: [https://nodejs.org/en/download](https://nodejs.org/en/download) and previous releases: [https://nodejs.org/en/about/previous-releases](https://nodejs.org/en/about/previous-releases) . Node 24.21.0 is an LTS release.
- Supabase server-package guidance: [https://supabase.com/docs/guides/auth/choosing-a-server-package](https://supabase.com/docs/guides/auth/choosing-a-server-package) .
- Supabase Next.js quickstart: [https://supabase.com/docs/guides/getting-started/quickstarts/nextjs](https://supabase.com/docs/guides/getting-started/quickstarts/nextjs) . These support the proposed `@supabase/ssr` cookie/session integration direction.
**Compatibility status: UNVERIFIED, not PASS.** Version existence, official minimum requirements, release status, and recommended integration direction are evidenced. The exact dependency combination has not been clean-installed, resolved, listed, or built in this architecture-only task.
### Correct reproducible compatibility sequence
Before implementation pins versions, use a clean temporary workspace and record output in the transfer evidence:
1. `npm view next@16.3.4 engines peerDependencies --json`
2. `npm view react@19.3.0 version --json`
3. `npm view react-dom@19.3.0 version --json`
4. `npm view typescript@6.0.x version --json`
5. `npm install next@16.3.4 react@19.3.0 react-dom@19.3.0 typescript@6.0.x --package-lock-only`
6. `npm ci` using the generated lockfile, which is the first step that installs `node_modules` for this validation sequence
7. `npm ls next react react-dom typescript --all`
8. Run `npm run build` from a minimal App Router scaffold using that installed lockfile.
Expected acceptance: peer requirements resolve without overrides or `legacy-peer-deps`; one intended React/React-DOM pair resolves; selected Node LTS executes the build; and the minimal build completes without dependency/runtime version errors. If a check fails, revise the version set rather than forcing installation. **All steps above are NOT RUN for this architecture submission.** This task does not authorize bootstrap or dependency installation in the project.
## 4. Exact path ownership and exclusions
The table below mirrors current role reservations. Ownership is not implementation authorization outside the explicitly assigned issue.
<table header-row="true">
<tr>
<td>Role</td>
<td>Exact owned/allowed paths</td>
<td>Explicit exclusions / notes</td>
</tr>
<tr>
<td>Manager</td>
<td>`coordination/`; integration transfer evidence; manager-owned workflow files</td>
<td>Owns inboxes, master plan, decisions and integration log. Does not silently edit worker deliverables.</td>
</tr>
<tr>
<td>Architect</td>
<td>`docs/ARCHITECTURE.md`; own status/outbox/checkpoint/handoff</td>
<td>Current #21 scope is architecture only. No API/schema/contracts/application implementation.</td>
</tr>
<tr>
<td>Designer</td>
<td>`docs/UI_SPEC.md`; `docs/design/`; `content/`; `docs/EDITORIAL_REVIEW.md`</td>
<td>Owns current design/editorial reservations. No frontend application implementation.</td>
</tr>
<tr>
<td>Frontend</td>
<td>`apps/web/` excluding `apps/web/src/app/api/` and `apps/web/src/server/`; `package.json`; `package-lock.json`; `tsconfig.json`; `tests/frontend/`</td>
<td>Owns root build configuration. Backend API/server paths, engine, and contracts are excluded.</td>
</tr>
<tr>
<td>Backend</td>
<td>`packages/engine/`; `apps/web/src/app/api/`; `apps/web/src/server/`; `supabase/`; `tests/backend/`</td>
<td>Consumes approved contracts. No frontend UI or editorial ownership.</td>
</tr>
<tr>
<td>QA</td>
<td>`tests/e2e/`; `tests/accessibility/`; `docs/QA_REPORT.md`; `docs/BUGS.md`</td>
<td>Owns verification/evidence, not product implementation.</td>
</tr>
<tr>
<td>Security/DevOps</td>
<td>`.github/`; `docs/SECURITY_REVIEW.md`; `docs/DEPLOYMENT.md`; `docs/ADSENSE_READINESS.md`; security configuration subject to manager path reservation</td>
<td>Security-sensitive changes require review. No production/paid activation is implied.</td>
</tr>
</table>
Cross-cutting rule: workers update only their own status/outbox/checkpoint/handoff. Manager owns role inboxes and coordination. No role reservation alone authorizes implementation.
## 5. Module boundaries
```plain text
apps/web/
  src/app/                 Next.js routes, public pages, workspace routes
  src/components/          accessible presentation
  src/features/            tool-specific UI adapters/view models
  src/lib/browser/         browser persistence/import/export
  src/lib/auth/            client/server auth adapters
  src/server/              authenticated persistence/application services

packages/engine/
  project/                 dependency graph, scheduling, critical path, float, PERT
  capacity/                availability, nonworking dates, allocation, overload
  decision/                normalization, weighted scoring, sensitivity, ties
  study/                   study slots, spaced reviews, impossible schedules
  shared/                  date/workday primitives and deterministic utilities

packages/contracts/
  versioned tool input/output shapes
  runtime validation schemas
  error/result discriminated unions
  import/export envelope definitions

content/guides/             reviewed original guides and examples

tests/
  unit/                     pure engine tests
  property/                 invariant/property tests
  fixtures/                 independent worked examples
  frontend/                 browser/component tests
  accessibility/            automated/manual evidence
  e2e/                      end-to-end flows
```
The pure engine must not import Next.js, React, browser APIs, HTTP clients, Supabase, or authentication libraries. These are proposed boundaries and do not authorize directory creation in this task.
## 6. Four-tool calculation boundaries
### Project planning
Task duration is explicitly calendar or workday based. Zero duration is allowed only if the later contract permits milestones; negative durations are invalid. Duplicate task IDs and missing dependency IDs are invalid. Cycles are domain errors and must identify affected nodes. Topological order is deterministic using a documented stable tie-break such as task ID. Critical path/float require an acyclic graph. PERT uses `(optimistic + 4 * mostLikely + pessimistic) / 6` when selected, with domain constraints such as optimistic \<= mostLikely \<= pessimistic. Workday calendars are explicit. Unsatisfiable constraints return an impossible-schedule result rather than silently dropping dependencies or moving deadlines.
### Capacity planning
Each person has explicit availability and nonworking dates. Allocation beyond availability produces overload information. Deadlines are not silently moved. Equal allocation choices use deterministic stable tie-breaking. Date/time semantics are explicit and not inferred from browser locale for persisted calculations.
### Decision comparison
Weights are positive and normalization is explicit. Benefit/cost direction is explicit. Missing values are not silently zero. Ties are first-class. Zero-range normalization is defined. Invalid, negative, NaN, infinite, or otherwise non-finite numeric inputs are rejected. Sensitivity preserves ties/ranges rather than false precision.
### Study scheduling
Topics, effort, available slots, and deadlines are explicit. Review intervals are a declared calculation policy, not a learning guarantee. Impossible schedules identify limiting constraints. Edited sessions require an explicit later preservation/regeneration/fixed-constraint contract. Equal-priority sessions use deterministic stable fields for tie-breaking.
## 7. Invalid input, cycle, impossible-schedule, and tie handling
- **Invalid input:** boundary validation rejects malformed data; engine invariants remain defensive.
- **Cycle:** project-domain error with reproducible affected nodes/cycle representation.
- **Impossible schedule:** validly shaped request whose constraints cannot all be satisfied.
- **Tie:** valid result containing multiple equally ranked/critical candidates; no forced winner.
- **Warning:** non-fatal structured information such as overload or sensitivity.
UI text is not the source of truth for these states.
## 8. Determinism and dates
Engines receive explicit reference dates, timezone/calendar semantics, and calculation options. They never read the current clock implicitly. Intermediate numerical precision is retained; presentation rounding happens at the UI boundary unless the selected mathematical method explicitly requires otherwise. Results retain enough information for explanation and independent verification.
## 9. Data flow
### Anonymous calculation
```plain text
Public route / workspace
 -> UI input model
 -> runtime validation
 -> versioned engine input
 -> pure engine
 -> versioned engine result
 -> result view / explanation / print / browser save / JSON export
```
No server request is required.
### Optional authenticated save
```plain text
browser workspace
 -> explicit Save
 -> authenticated request
 -> session validation
 -> ownership authorization
 -> validated payload
 -> atomic version-precondition persistence
 -> database
 -> success or stale-write conflict
 -> browser state
```
The browser never receives server secrets or database service-role credentials.
### Public content
Public content may be static or server-rendered into crawlable HTML. Private workspace data uses separate route/data boundaries and must never be introduced into public props, generated metadata, sitemap output, or shared/static caches.
## 10. Browser persistence, import/export, and versioning
Browser persistence is a convenience layer, not the canonical shared database.
Proposed architectural envelope:
```json
{
  "format": "planwise-workspace",
  "schemaVersion": 1,
  "tool": "project",
  "savedAt": "2026-09-12T00:00:00Z",
  "payload": {}
}
```
The exact TypeScript schema belongs in `packages/contracts/` and is not frozen here.
Rules:
1. Every export contains a format identifier and schema version.
2. Imports are untrusted data.
3. Validate the complete envelope before replacing current workspace state.
4. Unknown future versions are rejected with a recoverable message unless an explicit migration exists.
5. Older supported versions use deterministic, versioned migrations.
6. Imported data is never executed as code and imported strings are never trusted as HTML.
7. Proposed initial limits: **1 MiB per JSON workspace export** and **10 MiB total browser-managed workspace data per origin**, subject to implementation/UX review and possible reduction on constrained devices.
8. Collection limits must include task count, criteria count, study-session count, string lengths, nesting depth, and other expensive fields. The 200-task target is the primary performance target; higher hard limits require benchmark evidence.
9. Export timestamps are metadata, not hidden scheduling inputs; calculation reference dates remain explicit.
10. A failed import leaves the current valid workspace unchanged.
11. For authenticated API/import paths, enforce request/body byte limits **before expensive parsing**. Schema validation additionally enforces maximum object depth, string length, collection length, and numeric validity.
## 11. Authentication, session, RLS, and ownership trust boundaries
Authentication is optional for the core product path.
**Boundary A: browser to public application.** Client data is untrusted. Client validation is UX only, not authorization.
**Boundary B: browser to authenticated server.** The server derives identity from a framework-supported authenticated session. It never trusts client-supplied user IDs in JSON, URLs, hidden fields, or route parameters as proof of ownership.
**Secure cookie/session requirements.** Where cookie-backed sessions are used, use framework/provider-supported secure cookie handling. Production cookies must be protected against script access where appropriate, use secure transport, and use an explicit same-site policy consistent with the authentication flow. State-changing requests require CSRF protection appropriate to the chosen session mechanism. Session refresh must rotate/refresh credentials according to the provider's supported flow; logout/revocation must invalidate the usable session; expired, revoked, malformed, and refresh-failure states must fail closed and return a generic recoverable authentication error without leaking session details.
**Boundary C: application to database.** If Supabase is retained, **RLS is mandatory on every private table and every private read/write path**. Each policy must derive ownership from the authenticated database/session identity, not request-supplied ownership fields. Server authorization checks remain explicit but do not substitute for RLS.
**Atomic concurrency rule.** Persisted records carry a monotonic `version` (or an equivalently explicit precondition token). Update requests include the version observed by the client. The database update must atomically require `WHERE id = ... AND owner_id = authenticated_identity AND version = expected_version`, then increment the version. Zero affected rows due to an existing newer version returns a structured stale-write conflict, not a silent overwrite. The conflict response identifies that the workspace changed and requires reload/reconcile behavior without exposing another user's data.
**Boundary D: public rendering/search.** No authenticated workspace record is rendered into public pages, metadata, static caches, sitemap output, or server-rendered public props. Private IDs are not public canonical URLs.
**Boundary E: import/export.** Imported JSON is hostile input. Enforce byte, depth, string, collection, numeric, and schema limits before expensive work; never execute imported data or render imported HTML directly.
**Boundary F: credentials/secrets.** Only public client configuration may reach browser code. Service-role/database credentials stay server-side and never enter source control or exports.
## 12. Accessibility, performance, and security test architecture
### Accessibility/presentation
Charts require tabular/text equivalents. Result explanations must work without color, hover, animation, or pointer interaction. Required principles include semantic headings/landmarks, keyboard-operable controls, visible focus, labels and programmatic error relationships, accessible status updates, no color-only information, reduced-motion behavior, and ordinary workflows without horizontal scrolling.
### 200-task performance
Engine benchmarks are independent of network/database latency. Browser performance is measured separately on recorded hardware. If recalculation is expensive, use memoization, incremental recalculation, worker-based computation, or deferred rendering without changing engine semantics. Benchmark records hardware, browser, dataset, calculation type, cold/warm state, and latency. The target is not claimed as already met.
### Security test matrix required before persistence is enabled
<table header-row="true">
<tr>
<td>Area</td>
<td>Required cases</td>
<td>Expected result</td>
</tr>
<tr>
<td>Session/cookies</td>
<td>valid session; missing/expired/revoked session; malformed cookie; refresh success; refresh failure; logout/revocation</td>
<td>authorized state only on valid session; failure is closed and non-sensitive</td>
</tr>
<tr>
<td>CSRF</td>
<td>valid state-changing request; missing/invalid CSRF proof; cross-site request attempt</td>
<td>valid request succeeds; invalid/cross-site mutation rejected</td>
</tr>
<tr>
<td>RLS/ownership</td>
<td>owner read/write; non-owner read/write; forged owner ID; missing owner ID; direct private-table access</td>
<td>owner permitted; all cross-user/forged access denied</td>
</tr>
<tr>
<td>Import limits</td>
<td>body just below/at/above limit; excessive depth; excessive string; excessive collection; malformed JSON; hostile payload</td>
<td>bounded rejection before expensive processing; no state replacement on failure</td>
</tr>
<tr>
<td>Concurrency</td>
<td>two clients read vN; first writes vN; second writes stale vN</td>
<td>first succeeds to vN+1; second receives structured stale-write conflict; no overwrite</td>
</tr>
<tr>
<td>Private indexing/cache</td>
<td>private route, metadata generation, sitemap generation, static cache/public prop inspection</td>
<td>explicit noindex; no private data in metadata/sitemap/public props/shared cache</td>
</tr>
</table>
No runtime/security test is claimed as passed in this architecture submission.
## 13. Security and privacy risks
<table header-row="true">
<tr>
<td>Risk</td>
<td>Mitigation</td>
<td>Review owner</td>
</tr>
<tr>
<td>Cross-user access/IDOR</td>
<td>session-derived identity + server authorization + mandatory RLS + negative tests</td>
<td>security_devops + backend</td>
</tr>
<tr>
<td>Import XSS</td>
<td>strict JSON schema; no raw HTML execution</td>
<td>security_devops + frontend</td>
</tr>
<tr>
<td>Oversized/deep imports</td>
<td>early body-size enforcement + depth/string/collection/field limits</td>
<td>backend + security_devops</td>
</tr>
<tr>
<td>Stale overwrite</td>
<td>atomic version precondition + structured conflict</td>
<td>backend + security_devops</td>
</tr>
<tr>
<td>Session/CSRF errors</td>
<td>framework-supported secure cookie/session handling, CSRF controls, refresh/revocation tests</td>
<td>security_devops</td>
</tr>
<tr>
<td>Private indexing/cache leakage</td>
<td>explicit noindex/no shared-cache policy; metadata/sitemap/public-prop exclusion</td>
<td>frontend + security_devops</td>
</tr>
<tr>
<td>Secret exposure</td>
<td>server-only privileged credentials</td>
<td>security_devops</td>
</tr>
<tr>
<td>Nondeterminism</td>
<td>explicit dates/timezones/options; pure engine</td>
<td>architect + backend</td>
</tr>
<tr>
<td>Precision errors</td>
<td>documented precision/rounding boundary</td>
<td>architect + QA</td>
</tr>
<tr>
<td>Dependency vulnerabilities</td>
<td>lockfile, supported LTS lines, CI/security review</td>
<td>security_devops</td>
</tr>
<tr>
<td>Sensitive logs</td>
<td>structured errors and redaction policy</td>
<td>backend + security_devops</td>
</tr>
</table>
Advertising remains disabled by default. No publisher identity, AdSense approval, contact identity, ads.txt identifier, or account eligibility is invented.
## 14. Proposed implementation ownership map
This is a future planning map and does not override the exact role/path reservations in Section 4.
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
<td>architect, later reviewed by affected implementers</td>
<td>future API contract; not part of current #21 implementation</td>
</tr>
<tr>
<td>`docs/DATABASE_SCHEMA.md`</td>
<td>architect, later reviewed by backend/security</td>
<td>future persistence model; not part of current #21 implementation</td>
</tr>
<tr>
<td>`packages/contracts/`</td>
<td>architect with backend/frontend review</td>
<td>future shared types/validation; next bounded deliverable</td>
</tr>
<tr>
<td>`packages/engine/`</td>
<td>backend</td>
<td>pure deterministic algorithms</td>
</tr>
<tr>
<td>`apps/web/` excluding backend paths</td>
<td>frontend</td>
<td>presentation/workspace/public pages</td>
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
<td>designer/editorial owner under current reservations</td>
<td>original guides/publisher drafts</td>
</tr>
<tr>
<td>`tests/frontend/`, `tests/e2e/`</td>
<td>frontend / QA according to exact reservation</td>
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
The future map is informational. It does not grant current implementation authority.
## 15. Next bounded contract deliverable and future architect reservations
After this architecture document is independently approved, the next bounded deliverable under parent issue **#2** should be `packages/contracts/` plus the corresponding `docs/API_CONTRACT.md` update. This is a **future reservation**, not current #21 scope.
That later contract task should define for all four tools: versioned input/output schemas; structured error/result types; date/timezone/workday/precision/rounding semantics; import/export envelope and migration rules; mock fixtures with valid/invalid examples; deterministic ties and impossible-schedule representations; and ownership/auth boundary inputs for persisted operations without coupling the pure engine to authentication.
No contract freeze occurs until manager approval, required independent review, and a corresponding decision record are complete.
## 16. Unresolved decisions and deferred release inputs
1. Exact package patch versions and final lockfile remain pending compatibility/security verification.
2. Exact runtime test framework is not frozen.
3. Exact persistence API shape and database schema are not frozen.
4. Browser storage technology and quota-handling strategy need implementation validation.
5. Proposed import/export hard limits need benchmark and UX confirmation.
6. Request/body, depth, string, and collection hard limits need contract/implementation validation while retaining early rejection.
7. Study-session edit/recalculation semantics need contract review.
8. Workday calendar model needs contract review, including locale/holiday behavior.
9. Authentication provider configuration is not activated.
10. Hosting/deployment target is proposed but unactivated.
11. Owner publisher identity, contact route, domain, ad account eligibility, and production/account configuration remain release inputs.
12. AdSense readiness is not AdSense approval.
13. No production deployment, paid activation, domain change, or advertising activation is authorized by this document.
## 17. Worked-example strategy
Each tool must have at least one small, independently reproducible fixture and one explanatory public example after editorial review.
- **Project:** dependency graph with critical path, one noncritical task with float, plus a separate cyclic-invalid example.
- **Capacity:** two people with different weekly availability and a nonworking date that creates overload without silently moving the deadline.
- **Decision:** three alternatives, benefit and cost criteria, normalized positive weights, plus an intentional tie.
- **Study:** a deadline with available slots that fits, plus the same workload with insufficient slots producing an impossible-schedule result.
Every example states inputs, assumptions, expected output, units, dates, reference timezone/calendar semantics, and rounding rules. Fixtures are independent of UI rendering.
## 18. Requirement-to-section checklist
<table header-row="true">
<tr>
<td>Requirement/finding</td>
<td>Section(s)</td>
<td>Status</td>
</tr>
<tr>
<td>Anonymous-first browser workspace; deterministic engine; optional private persistence; public/private separation</td>
<td>1, 2, 5, 8, 9, 10</td>
<td>Covered</td>
</tr>
<tr>
<td>Stack/version recommendations and inspectable official evidence</td>
<td>3</td>
<td>Covered; exact compatibility remains UNVERIFIED</td>
</tr>
<tr>
<td>Correct ownership/path exclusions from MASTER_TASKS</td>
<td>4, 14</td>
<td>Covered</td>
</tr>
<tr>
<td>All four tools and numeric/date/workday assumptions</td>
<td>6</td>
<td>Covered</td>
</tr>
<tr>
<td>Invalid/cycle/impossible/tie handling</td>
<td>7</td>
<td>Covered</td>
</tr>
<tr>
<td>Import/export envelope versioning, migration/rejection, failed-import preservation, proposed limits</td>
<td>10</td>
<td>Covered</td>
</tr>
<tr>
<td>Early request/body limits plus depth/string/collection limits</td>
<td>10, 13</td>
<td>Covered</td>
</tr>
<tr>
<td>Secure cookie/session, CSRF, refresh/revocation/failure semantics</td>
<td>11, 12, 13</td>
<td>Covered</td>
</tr>
<tr>
<td>Mandatory RLS and cross-user negative tests</td>
<td>11, 12, 13</td>
<td>Covered</td>
</tr>
<tr>
<td>Atomic version-precondition updates and stale-write conflict test</td>
<td>9, 11, 12, 13</td>
<td>Covered</td>
</tr>
<tr>
<td>Explicit private noindex/no shared-cache policy; exclude private data from metadata/sitemap/public props</td>
<td>2, 9, 12, 13</td>
<td>Covered</td>
</tr>
<tr>
<td>Accessibility and 200-task performance</td>
<td>12</td>
<td>Covered; evidence remains future work</td>
</tr>
<tr>
<td>Security risks and test architecture</td>
<td>12, 13</td>
<td>Covered; no runtime tests claimed passed</td>
</tr>
<tr>
<td>Worked examples for all four tools</td>
<td>17</td>
<td>Covered</td>
</tr>
<tr>
<td>Next bounded contract deliverable and future #2 reservation</td>
<td>15</td>
<td>Covered; not current #21 scope</td>
</tr>
<tr>
<td>Unresolved release inputs and no invented AdSense guarantee</td>
<td>16</td>
<td>Covered</td>
</tr>
<tr>
<td>Actual check evidence and limitations</td>
<td>19</td>
<td>Covered</td>
</tr>
</table>
## 19. Checks, evidence, finding resolution, and limitations
### Finding-to-section resolution
<table header-row="true">
<tr>
<td>Finding</td>
<td>Resolution</td>
<td>Evidence/status</td>
</tr>
<tr>
<td>Manager: Revision 1 dropped required scope</td>
<td>Revision 2 restores complete architecture scope from the original, including import/export, worked examples, contract deliverable, release inputs, and checklist.</td>
<td>Document review; no implementation.</td>
</tr>
<tr>
<td>Manager: exact role/path ownership</td>
<td>Section 4 uses exact primary owners/exclusions; Section 14 is explicitly future/informational and cannot override reservations.</td>
<td>Aligned to manager instruction and MASTER_TASKS evidence reviewed for this assignment.</td>
</tr>
<tr>
<td>Manager: unsupported stack compatibility</td>
<td>Section 3 separates version existence from compatibility proof and marks compatibility UNVERIFIED. Official direct URLs and access date are recorded.</td>
<td>Current-source review; exact lock/build NOT RUN.</td>
</tr>
<tr>
<td>Security: secure session/cookie and CSRF boundary</td>
<td>Section 11 defines framework-supported secure cookie/session handling, same-site/secure expectations, CSRF protection, refresh/revocation, failure-closed behavior; Section 12 defines the test matrix.</td>
<td>Architecture requirement; runtime test NOT RUN.</td>
</tr>
<tr>
<td>Security: mandatory RLS</td>
<td>Section 11 makes RLS mandatory for every private Supabase table/read/write path and requires session-derived ownership.</td>
<td>Architecture requirement; RLS test NOT RUN.</td>
</tr>
<tr>
<td>Security: cross-user negative tests</td>
<td>Section 12 requires owner and non-owner/forged-owner/direct-table negative cases.</td>
<td>Required future test; NOT RUN.</td>
</tr>
<tr>
<td>Security: early body limits and schema resource limits</td>
<td>Section 10 requires body byte rejection before expensive parsing plus depth/string/collection/numeric/schema limits.</td>
<td>Architecture requirement; runtime test NOT RUN.</td>
</tr>
<tr>
<td>Security: atomic concurrency</td>
<td>Section 11 defines monotonic version precondition, atomic owner/version condition, increment, and structured stale-write conflict; Section 12 tests stale writes.</td>
<td>Architecture requirement; integration test NOT RUN.</td>
</tr>
<tr>
<td>Security: private indexing/shared-cache leakage</td>
<td>Sections 2, 9, 12, and 13 require explicit noindex, no sitemap/metadata/public-prop leakage, and no shared/static cache for private responses.</td>
<td>Architecture/release gate; browser/runtime test NOT RUN.</td>
</tr>
</table>
### Check A — source/input review
**Action:** inspected manager inbox `MGR-ARCH21-REV2-001`, PR #22 discussion/review at head `ccf944d400875ae81bd8dc8ef730420bdd7a8d81`, the preserved original architecture submission, and Revision 1 evidence before drafting.
**Result:** PASS for source review. No application implementation was performed.
### Check B — official-source verification
**Action:** reviewed the direct official URLs recorded in Section 3 on 2026-09-12 UTC.
**Result:** PASS for source/version existence and documented requirements. This is not compatibility proof.
### Check C — compatibility resolution/build
**Result:** NOT RUN.
**Limitation:** no project bootstrap, dependency installation, lockfile generation, `npm ci`, `npm ls`, or application build was authorized or performed. The corrected sequence in Section 3 explicitly distinguishes `--package-lock-only` from installation of `node_modules`.
### Check D — application/security tests
**Result:** NOT RUN / NOT APPLICABLE to this architecture-only submission.
No RLS, browser, CSRF, session, concurrency, indexing, or application runtime test is represented as passed. Section 12 is the required future matrix.
### Check E — git diff/build transfer checks
**Result:** NOT RUN in this session.
**Limitation:** this submission was prepared in Notion for manager transfer; no local worker Git branch was created and no GitHub write operation was required. Manager should transfer the exact content to `docs/ARCHITECTURE.md` from the latest approved main, then run `git diff --check`, inspect the scoped diff, and record the result.
### Review boundary
Security/DevOps should review this consolidated Revision 2 after manager transfer. Revision 1 is superseded as a source proposal but remains preserved as historical evidence. No implementation beyond this architecture document is assigned.
## Submission boundary
This document does not freeze APIs, schemas, engine contracts, UI behavior, authentication configuration, deployment, or advertising. Manager transfer, exact-content/path/hash verification, feasible checks, and independent security-devops review remain required before approval.
