# Project planner contract v1.1.0

Framework/runtime independent contract for the anonymous planner. No auth, account, session, database or wall-clock dependency.

## Semantics
- Numeric scheduling intervals are half-open `[start, finish)`. `earliestFinish` and `latestFinish` are exclusive elapsed offsets and therefore satisfy `finish = start + duration` within engine tolerance.
- `startOffset` is the displayed start offset. `finishOffset = ceil(exclusiveFinish) - 1` for positive duration. Zero duration displays at the start offset. Thus a 4.333... task beginning at offset 0 displays finishOffset 4, while its exclusive finish remains 4.333....
- Display dates identify the calendar/workday containing the occupied interval's final fractional unit. A one-unit task beginning day zero has start and finish date equal to the reference date.
- Workday weekday numbering is 0 Sunday through 6 Saturday. A workday is eligible only when its weekday is in `workingWeekdays` and it is not in `nonWorkingDates`. Successors become ready when predecessor exclusive finish is reached; zero-duration milestones therefore do not add a gap.
- PERT expected duration is `(optimistic + 4*mostLikely + pessimistic)/6`. When `calculatePertExpectedDuration=true`, the expected value is used. When false, PERT tasks use `mostLikely` deterministically and `pertExpectedDurations` is empty. Fixed tasks are unaffected.
- Engine output uses deterministic task/edge ordering by stable task ID, and critical edges require scheduling tightness: successor earliest start equals predecessor earliest finish and both endpoints have zero float. Zero-float nodes alone do not define an edge.
- Critical paths are bounded to 1024 emitted paths. `criticalPaths.totalPathCount` is an exact decimal string and `truncated=true` when more paths exist than emitted. Paths are ordered lexicographically by task ID traversal.
- `checkDeadline=true` requires a deadline. A deadline is inclusive at the displayed finish date. Missing deadline is `INVALID_CALENDAR` in v1.1.

## Validation layers
JSON Schema validates structure, types, known fields, supported transport version, and finite non-negative numeric bounds. Domain validation handles duplicate IDs, dependency references, cycles, PERT ordering, calendar consistency, deadline option combinations, and non-finite in-memory numbers. JSON cannot transport NaN/Infinity, so those require direct in-memory tests.

## Resource boundaries
Import must check raw UTF-8 byte length before JSON parsing: <= 1 MiB. After parsing, enforce max depth 16, aggregate UTF-8 string bytes <= 256 KiB, traversal/property budget <= 25,000, <=200 tasks, and <=19,900 distinct dependency edges. 19,900 is the maximum distinct edges in a DAG of 200 tasks, not all directed pairs. Per-task duration and date horizon are capped at 1,000,000 units/days. Reject unsupported versions, unknown fields, malformed UTF-8, budget overflow, schema errors and domain errors without mutating the current workspace. Valid workspace state is preserved on every failed import.

## Envelope
`{format:"planwise-workspace", schemaVersion:2, tool:"project", savedAt:ISO-8601, payload:ProjectInput}`. The envelope contains no identity/auth/account/session fields. Unknown fields are rejected. Unsupported versions are rejected before replacement. v1.1 defines no automatic migration; future versions must provide an explicit migration table or be rejected.

## Deferred
Resource leveling, task calendars, lag/lead, negative lag, date/time-of-day scheduling, persisted projects, collaboration, authentication, engine implementation, UI and other tool contracts are outside v1.1.
