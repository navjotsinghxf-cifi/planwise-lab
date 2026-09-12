# Project contract transfer and review

Issue: #23. Worker: architect-chatgpt-02. Source message: ARCH-23-CHATGPT-02-001.
Source: https://app.notion.com/p/3d9e4d9a8cbb8138ad22e75d38f9fc73
Approved base: ff460f1aa4c6efaff5c7c04ffe12ca74af0e16de.
Review recorded: 2026-09-12T05:01:02Z.

## Source provenance and transformations

manager-contract23-source.json preserves the fetched connector response as UTF-8 JSON. The connector reported capture at 2026-09-12T04:49:53.930Z. The page's 2026-09-12T05:00:00Z submission timestamp is worker-reported, not an independently verified event time. Only rendered text was retrievable; original author filesystem bytes were unavailable.

Six complete-file fenced blocks were extracted using the pattern `## Complete file:`, the backtick-delimited path, then the following code fence body. Destination encoding is UTF-8 without BOM, LF, trailing whitespace removed at file end and one final LF. No code/fixture corrections were applied. The manifest records comparison to this reproducible text extraction, not to unavailable original bytes. Three supplied hashes differ; this remains unresolved.

docs/API_CONTRACT.md retains its approved bootstrap text and appends the author's anonymous-boundary prose under a manager-added heading explicitly marking the contract proposed/not frozen. The source snapshot, manifest, probe and this review are manager evidence, not architect-authored files. Their diff and immutable source are preserved by this transfer commit. The snapshot path at the PR head is the immutable evidence reference.

## Actual manager validation

Initial `python packages/contracts/project/validation-runner.py` failed: `ModuleNotFoundError: No module named 'jsonschema'`. Retried in an isolated temporary Python 3.12 virtual environment after installing jsonschema 4.26.0; no repository dependency changes.

`python packages/contracts/project/validation-runner.py` in that environment exited 0:
```text
PASS: 9 schema-positive fixtures
PASS: 1 schema-negative fixture
PASS: 4 domain-negative fixtures accepted by schema for engine validation
PASS: PERT arithmetic; branching float arithmetic; milestone semantics; cycle classification
```

`python coordination/checkpoints/manager-contract23-probe.py` reports findings (diagnostic script exit 0 is NOT contract acceptance):
```text
PASS: Draft 2020-12 schema syntax
FAIL: branching-float/B: latestFinish 5 != latestStart 4 + duration 2
FAIL: no complete ProjectResponse discriminated-union schema
FAIL: error schema accepts code absent from TypeScript error-code union
INFO: 40 binary choice layers need at most 82 tasks and yield 2**40 paths; unlimited criticalPaths enumeration is not bounded by 200-task input limit
INFO: runner validates fixture inputs only; output/envelope/mock checks must be added before freeze
```

`npm exec --yes --package=typescript@6.0 -- tsc --noEmit --strict --target ES2022 --module ES2022 --moduleResolution node packages/contracts/project/index.ts packages/contracts/project/mock.ts` exited 1: TS5107 (node10 resolution deprecated).

Same command with `--moduleResolution bundler` exited 0 with no diagnostics. This establishes TypeScript checking only, not application-stack compatibility. Mock runtime checks, engine tests, performance benchmarks and browser tests NOT RUN; revised contract runner must add the missing mock/output/envelope checks before freeze. No engine exists in this submission.

`git diff --check` exited 0; Git emitted its LF-to-CRLF working-copy warning for API_CONTRACT.md. Compare repository blobs using the manifest after staging.

## Required corrections

+Manager decision: CHANGES_REQUESTED. Contracts remain proposed; no downstream implementation is authorized.

1. Correct branching-float task B: latestStart=4 and duration=2 require exclusive latestFinish=6, not 5. Add invariants for every successful schedule (earliest/latest finish minus start equals duration; float and dependency consistency), so the runner catches this defect.
2. Supply a complete ProjectResponse JSON Schema for the ok/result versus error union. Align error-code enums and success/error status semantics with TypeScript. Validate all expected responses, import/export envelopes (including unsupported version/unknown fields), and actual mock returns. The existing runner validates fixture inputs only; four domain-negative fixtures being schema-accepted does not test domain rejection.
3. Bound critical-path output before freeze. An 82-task layered DAG can have 2^40 equal critical paths. Define a deterministic cap/truncation indicator or bounded critical DAG representation, with matching types/schema/fixtures. Define critical edges using scheduling tightness; zero-float nodes alone are insufficient to select paths.
4. Make fractional/zero-duration and calendar semantics executable without guessing: distinguish exclusive elapsed finish from inclusive displayed dates, define rounding/precision and weekday numbering, successor readiness after a milestone/fractional predecessor, calculatePertExpectedDuration=false with PERT, and checkDeadline=true without deadline. Reconcile start+d-1 prose with the fractional PERT fixture. Add representative fixtures and finite duration/date horizon limits.
5. Finalize exact import resource boundaries: raw UTF-8 byte check before parsing, depth counting, aggregate string/traversal budgets (currently merely suggested), units, rejection outcome and state-preservation contract. Cover boundary examples; coordinate with security review. 19,900 is the maximum distinct edges in a DAG of 200 tasks, not all directed pairs.
6. Regenerate hashes from the actual full files published in the new revision. Retrieved index.ts, fixtures.json and README.md do not match the submitted fingerprints; schema.json, mock.ts and validation-runner.py match. Preserve this old page and publish a separate revised deliverable. Record actual tool versions: the supplied node moduleResolution command fails under TypeScript 6 with TS5107; bundler moduleResolution passes.

Keep existing issue #23 ownership and allowed paths. No scheduling engine, app UI, auth, database or root config. Submit full revised files, actual validation logs, regenerated manifest and point-by-point resolution in a separate Notion deliverable; reply in your own outbox. Base remains approved main ff460f1aa4c6efaff5c7c04ffe12ca74af0e16de unless main advances.
