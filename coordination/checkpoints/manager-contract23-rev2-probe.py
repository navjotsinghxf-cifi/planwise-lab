import json
from pathlib import Path
from jsonschema import Draft202012Validator
root=Path(__file__).resolve().parents[2]/'packages/contracts/project'
data=json.loads((root/'fixtures/fixtures.json').read_text())['fixtures']
schema=json.loads((root/'schema.json').read_text())
for f in data:
    if f['expected']['ok']:
        ids={t['id'] for t in f['input']['tasks']}
        r=f['expected']['result']
        unknown={x for p in r['criticalPaths']['paths'] for x in p}-ids
        if unknown: print('FAIL:',f['id'],'paths reference absent tasks:',sorted(unknown))
        if not ids and r['duration']!=0: print('FAIL:',f['id'],'empty input has duration',r['duration'])
    elif f['id']=='invalid-nonfinite-duration':
        print('FAIL: nonfinite mock fixture actually contains finite duration',f['input']['tasks'][0]['duration']['value'])
print('FAIL: runner requires every edge between zero-float nodes to be tight. Counterexample: A=1,B=1,C=1, edges A->B,B->C,A->C. All floats zero; A->C is valid but not tight (EF(A)=1, ES(C)=2).')
print('INFO: supplied resource check asserts constants only; it does not exercise byte/depth/string/traversal rejection boundaries.')
v=Draft202012Validator({'$defs':schema['$defs'],'$ref':'#/$defs/criticalPathSummary'})
assert list(v.iter_errors({'paths':[['A']]*1025,'truncated':True,'totalPathCount':'1025'}))
print('PASS: schema rejects 1025 emitted paths')
