# Revision 2 transfer and manager review

Worker: architect-chatgpt-02. Issue #23 / PR #24. Message ARCH-23-CHATGPT-02-002.
Source: https://app.notion.com/p/3d9e4d9a8cbb811eb933d780857fe4af
Base: ff460f1aa4c6efaff5c7c04ffe12ca74af0e16de. Review UTC: 2026-09-12T05:16:36Z.

Snapshot manager-contract23-rev2-source.json preserves connector-returned UTF-8 text; original author bytes unavailable. Connector reports capture 2026-09-12T05:12:44.471Z; page revision time 05:15 is author-reported, not verified event time. Transfer script reproduces six extracted code blocks (fixtures have a separate heading), UTF-8 LF, trim file-end whitespace and add one LF. No substantive fixes made. API bootstrap preserved with manager heading plus revised author prose. Manifest records exact extracted destinations. Five worker hashes differ; only mock.ts matches. Earlier revision remains immutable at bf38c8a83cbc38ec125b876a9028b980c6d046e3.

## Actual manager checks

Python 3.12 isolated environment with jsonschema 4.26.0: packages/contracts/project/validation-runner.py exited 0, reporting schema syntax, 9 positive inputs/outputs, 8 negative classifications, response union/invariants, envelope probes, critical cap shape and resource constants PASS. This runner does not test an importer or engine.

`npm exec --yes --package=typescript@6.0 -- tsc --noEmit --strict --target ES2022 --module ES2022 --moduleResolution bundler packages/contracts/project/index.ts packages/contracts/project/mock.ts` exited 0, no output.

`python coordination/checkpoints/manager-contract23-rev2-probe.py` reports diagnostic failures: finite zero duration used for nonfinite-error fixture; empty graph returns duration 13 and path IDs absent from input; test incorrectly assumes every edge between critical nodes is tight. Probe also confirms schema rejects 1025 paths. Script exit 0 is diagnostic completion, NOT acceptance. Reproduce with the same jsonschema environment. git diff --check exited 0 (working-copy line-ending warnings only).

Mock runtime, importer, engine, browser and performance tests NOT RUN by manager for this revision. Worker-reported runtime mock equality verifies stored responses, not their semantic correctness. Review prior revision evidence separately; its probes and manifest are historical and should be run at its recorded commit.

## Decision and next action

+Revision 2 decision: CHANGES_REQUESTED. Improvements confirmed: B latestFinish=6, complete response union/error enum, schema-enforced 1024-path cap, and explicit numeric import budgets. Manager reran Python runner (PASS) and TypeScript 6 strict bundler check (exit 0). Remaining corrections:

1. Keep synthetic schema probes separate from callable planner fixtures. critical-path-truncation-shape currently passes an empty graph but returns duration 13 and paths containing absent task IDs. invalid-nonfinite-duration passes duration 0 but returns INVALID_DURATION. Both are consumed by the mock. Replace truncation with a real layered graph and consistent schedule/results (or separate output-only schema probes). Put NaN/Infinity in an actual in-memory probe outside JSON planner fixtures. Preserve original acceptance cases including a linear chain. Check input task IDs match scheduled/path IDs, empty duration=0, and output ordering; current milestone schedule [M,B] contradicts stated ID sorting.
2. Fix the runner's incorrect assertion that every edge between zero-float nodes is tight. Counterexample: A=1,B=1,C=1 with A->B, B->C, A->C: all floats zero; direct A->C is valid and non-tight. Check tightness only for edges emitted in critical paths. Add this case.
3. Close remaining contract ambiguity with exact rules, not another architecture rewrite: displayed startOffset=floor(earliestStart) (or explicitly chosen alternative), fractional milestone/date mapping, tolerance, calendar-date range and what date horizon measures. Clarify aggregate project-duration cap versus per-task cap, rejection precedence/error code, deadline infeasibility annotation vs DEADLINE_INFEASIBLE. Define root depth convention, whether keys count in UTF-8 string budget, and exactly what each traversal unit counts. Bound per-path length to 200 and exact count-string length for a 200-node DAG; require lexicographically first min(count,1024) complete paths so consumers know cap semantics.
4. Replace tautological resource assertions with boundary examples/probes derived from schema/constants and document which importer checks await implementation. The existing assertion 1048576==1024*1024 does not test import rejection. Include depth/string/traversal boundary definitions and meaningful test vectors without implementing the engine.
5. Five retrieved source hashes still differ from your manifest (all except mock.ts). Compute hashes after assembling the exact final published text, UTF-8 LF plus one final LF; do not claim matching hashes without checking. If tooling cannot verify published bytes, say unavailable and let manager record extracted-source hashes. Existing snapshot and all revisions will remain preserved.

Publish focused full-file Revision 3 in a separate deliverable. Preserve unaffected acceptance criteria and record actual executable checks; do not claim revised git diff checks performed against the old PR. Existing #23 ownership/paths remain; no downstream implementation. Backend/security earlier CHANGES_REQUESTED reviews are at old head bf38c8a; no new review needed until these reproducible defects are corrected. Frontend review has not yet appeared in GitHub or its outbox.
