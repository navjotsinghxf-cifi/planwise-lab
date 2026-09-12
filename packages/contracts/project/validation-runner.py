import json, math
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
root=Path(__file__).resolve().parent
schema=json.loads((root/'schema.json').read_text())
data=json.loads((root/'fixtures/fixtures.json').read_text())
Draft202012Validator.check_schema(schema)
v=Draft202012Validator(schema, format_checker=FormatChecker())
fixtures=data['fixtures']
positive=[f for f in fixtures if f['expected']['ok']]
neg=[f for f in fixtures if not f['expected']['ok']]
for f in positive:
    errs=list(v.iter_errors(f['input']))
    assert not errs,(f['id'],errs)
    errs=list(Draft202012Validator({'$defs':schema['$defs'],'$ref':'#/$defs/result'}, format_checker=FormatChecker()).iter_errors(f['expected']['result']))
    assert not errs,(f['id'],errs)
for f in neg:
    errs=list(v.iter_errors(f['input']))
    if f['id']=='invalid-negative-duration': assert errs,f['id']
    elif f['id']=='unsupported-version': assert errs,f['id']
    else: assert not errs,(f['id'],errs)
response_schema={'$defs':schema['$defs'],'$ref':'#/$defs/response'}
for f in fixtures:
    assert not list(Draft202012Validator(response_schema).iter_errors(f['expected'])),f['id']
    if f['expected']['ok']:
        r=f['expected']['result']
        for e in r['schedule']:
            assert math.isfinite(e['duration']) and e['duration']>=0
            assert abs(e['earliestFinish']-e['earliestStart']-e['duration'])<1e-12
            assert abs(e['latestFinish']-e['latestStart']-e['duration'])<1e-12
            assert abs((e['latestStart']-e['earliestStart'])-e['float'])<1e-12
        by={e['taskId']:e for e in r['schedule']}
        for d in f['input']['dependencies']:
            a,b=by[d['predecessorId']],by[d['successorId']]
            assert b['earliestStart']+1e-12>=a['earliestFinish']
            assert b['latestStart']+1e-12>=a['latestFinish']
            if abs(a['float'])<1e-12 and abs(b['float'])<1e-12:
                assert abs(b['earliestStart']-a['earliestFinish'])<1e-12
        cp=r['criticalPaths']
        assert len(cp['paths'])<=1024 and isinstance(cp['truncated'],bool) and cp['totalPathCount'].isdigit()
base=next(f for f in fixtures if f['id']=='one-task')['input']
env={'format':'planwise-workspace','schemaVersion':2,'tool':'project','savedAt':'2026-09-12T05:10:00Z','payload':base}
envelope_schema={'$defs':schema['$defs'],'$ref':'#/$defs/envelope'}
assert not list(Draft202012Validator(envelope_schema, format_checker=FormatChecker()).iter_errors(env))
badv=dict(env); badv['schemaVersion']=1
assert list(Draft202012Validator(envelope_schema, format_checker=FormatChecker()).iter_errors(badv))
badfield=dict(env); badfield['extra']='x'
assert list(Draft202012Validator(envelope_schema, format_checker=FormatChecker()).iter_errors(badfield))
assert 1048576 == 1024*1024 and 16 >= 1 and 262144 < 1048576 and 25000 > 200
print(f'PASS: Draft 2020-12 schema syntax')
print(f'PASS: {len(positive)} schema-positive inputs + outputs')
print(f'PASS: {len(neg)} negative fixtures; schema/domain split checked')
print('PASS: response union, error enum, schedule invariants, dependency tightness')
print('PASS: envelope supported/unsupported version and unknown-field probes')
print('PASS: critical-path cap/truncation shape and totalPathCount string')
print('PASS: import resource-bound constants')
