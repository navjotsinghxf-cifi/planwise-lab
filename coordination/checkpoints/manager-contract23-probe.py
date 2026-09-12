import json
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path(__file__).resolve().parents[2]
package = root / 'packages/contracts/project'
schema = json.loads((package / 'schema.json').read_text(encoding='utf-8'))
fixtures = json.loads((package / 'fixtures/fixtures.json').read_text(encoding='utf-8'))['fixtures']
Draft202012Validator.check_schema(schema)
print('PASS: Draft 2020-12 schema syntax')
issues = []
for fixture in fixtures:
    if not fixture['expected']['ok']:
        continue
    for task in fixture['expected']['result']['schedule']:
        if abs(task['latestFinish'] - task['latestStart'] - task['duration']) > 1e-10:
            issues.append(f"{fixture['id']}/{task['taskId']}: latestFinish {task['latestFinish']} != latestStart {task['latestStart']} + duration {task['duration']}")
for problem in issues:
    print('FAIL:', problem)
if 'response' not in schema['$defs']:
    print('FAIL: no complete ProjectResponse discriminated-union schema')
error_schema = schema['$defs']['error']
if not list(Draft202012Validator(error_schema).iter_errors({'code': 'NOT_A_REAL_CODE', 'message': 'x'})):
    print('FAIL: error schema accepts code absent from TypeScript error-code union')
print('INFO: 40 binary choice layers need at most 82 tasks and yield 2**40 paths; unlimited criticalPaths enumeration is not bounded by 200-task input limit')
print('INFO: runner validates fixture inputs only; output/envelope/mock checks must be added before freeze')
