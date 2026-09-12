# Project planner contract package v1

## Files
- `index.ts`: framework-independent TypeScript input/output/error/envelope/adapter contracts.
- `schema.json`: JSON Schema Draft 2020-12 for project input, result fragments, and versioned workspace envelope.
- `fixtures/fixtures.json`: successful and negative fixtures with expected outputs/errors.
- `mock.ts`: deterministic fixture-backed mock implementing the planned `ProjectPlanner.calculate()` interface. It is a mock, not a scheduler.
- `validation-runner.py`: standalone schema/domain classification and worked-arithmetic checks.

## Semantics
- IDs are stable caller-owned strings, unique within a project. Task and dependency arrays are deterministically ordered by task ID for engine results; ties in critical-path enumeration are lexicographic by task ID.
- Durations are non-negative numbers. JSON cannot represent NaN/Infinity; in-memory TypeScript callers must reject non-finite numbers before engine execution.
- Fixed duration is used as supplied. PERT expected duration is `(optimistic + 4*mostLikely + pessimistic)/6`; estimates require optimistic <= mostLikely <= pessimistic.
- Zero duration is a valid milestone. It starts and finishes on the same working/calendar date and adds zero elapsed units.
- Day zero is the explicit reference date. For calendar days, positive duration `d` occupies offsets `[start, start+d)` and the displayed finish date is the date at offset `start+d-1`. For workdays, scheduling advances only through `workingWeekdays` minus `nonWorkingDates`; a positive-duration task begins on the first eligible working date at/after its predecessor-ready date/reference date.
- Predecessor completion makes a successor eligible on the next scheduling unit for calendar-day mode and next eligible workday for workday mode. This prevents overlapping dependent tasks.
- Earliest values use forward pass; latest values use backward pass from project duration; `float = latestStart - earliestStart`. Critical means zero float. All values are expressed in the selected duration unit.
- Critical paths are all maximal source-to-sink paths whose tasks are critical, returned in deterministic lexicographic task-ID order. Equal critical branches are preserved.
- Nonworking dates apply only to workday mode. Timezone is carried as explicit metadata and must not be inferred from the browser. Dates are date-only values in v1, not timestamps.
- Optional deadline feasibility is a result annotation. A deadline is inclusive: feasible when project finish date <= deadline. It never silently changes durations or moves the deadline.

## Validation layers
1. JSON Schema validates shape, required fields, primitive ranges, string lengths, collection counts, and envelope version.
2. Domain validation checks duplicate task IDs, dependency references, self/cyclic graphs, PERT ordering, valid calendar semantics, and finite numeric values in in-memory callers.
3. Scheduling engine returns structured cycle/impossible/deadline outcomes and never drops edges to make a plan appear feasible.

## Import/export security and limits
- Accepted JSON workspace: UTF-8 JSON string/bytes, <= 1 MiB after decoding and before deep traversal. Maximum nesting depth: 16. Maximum tasks: 200. Maximum dependency edges: 19,900 (200*199/2). Maximum task ID/name: 128/256 UTF-8 code points. Maximum nonworking dates: 3,660. Reject unsupported `schemaVersion` and unknown envelope/tool values.
- Suggested additional implementation guardrails: maximum total string data 256 KiB, maximum JSON array/object property traversal count 25,000, and maximum input parsing work bounded before schema/domain validation. These are proposed resource limits and should be benchmarked by backend/security before freeze.
- Parse into a fresh candidate object, validate fully, then replace workspace state only on success. A failed or unsupported import must leave the prior valid workspace unchanged.
- No identity, account, auth token, session, or database fields belong in the anonymous envelope.

## Deferred from v1
Hourly/time-of-day scheduling, resource leveling, calendars with exceptions beyond date lists, task constraints other than dependencies, recurring work patterns, and user-edited-session preservation/regeneration are explicitly deferred. They must be versioned later rather than silently inferred.

## Mock boundary
The planned engine and mock both expose `calculate(input: ProjectInput): ProjectResponse`. The mock performs exact fixture matching and returns cloned fixture results. It has no clock, browser, network, framework, auth, persistence, or scheduling logic.
