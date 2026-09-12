"""Validation runner for project-planner v1 fixtures.
Requires: python -m pip install jsonschema
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
schema = json.loads((ROOT / 'schema.json').read_text())
data = json.loads((ROOT / 'fixtures' / 'fixtures.json').read_text())
validator = Draft202012Validator(schema)

positive = [f for f in data['fixtures'] if f['expected']['ok']]
negative = [f for f in data['fixtures'] if not f['expected']['ok']]
schema_negative = {'invalid-negative-duration'}

for fixture in positive:
    errors = list(validator.iter_errors(fixture['input']))
    if errors:
        raise SystemExit(f"FAIL schema-positive {fixture['id']}: {errors}")
for fixture in negative:
    errors = list(validator.iter_errors(fixture['input']))
    if fixture['id'] in schema_negative:
        if not errors:
            raise SystemExit(f"FAIL schema-negative {fixture['id']}: unexpectedly valid")
    elif errors:
        raise SystemExit(f"FAIL domain-negative {fixture['id']}: schema rejected domain case: {errors}")

pert = next(f for f in data['fixtures'] if f['id'] == 'pert')
assert abs(pert['expected']['result']['pertExpectedDurations']['A'] - ((2 + 4*4 + 8) / 6)) < 1e-12
branch = next(f for f in data['fixtures'] if f['id'] == 'branching-float')
assert next(x for x in branch['expected']['result']['schedule'] if x['taskId'] == 'B')['float'] == 2
milestone = next(f for f in data['fixtures'] if f['id'] == 'zero-milestone')
assert milestone['expected']['result']['duration'] == 0
cycle = next(f for f in data['fixtures'] if f['id'] == 'invalid-cycle')
assert cycle['expected']['error']['code'] == 'CYCLE_DETECTED'

print(f'PASS: {len(positive)} schema-positive fixtures')
print('PASS: 1 schema-negative fixture')
print(f'PASS: {len(negative)-1} domain-negative fixtures accepted by schema for engine validation')
print('PASS: PERT arithmetic; branching float arithmetic; milestone semantics; cycle classification')
