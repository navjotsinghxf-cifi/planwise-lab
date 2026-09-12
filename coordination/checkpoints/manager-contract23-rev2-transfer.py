import hashlib, json, re
from pathlib import Path
root=Path(__file__).resolve().parents[2]
src=root/'coordination/checkpoints/manager-contract23-rev2-source.json'
page=json.loads(json.loads(src.read_text(encoding='utf-8'))['content'][0]['text'])['text']
files=re.findall(r'## Complete file: `([^`]+)`\n```[^\n]*\n([\s\S]*?)\n```',page)
fixture=re.search(r'## Complete fixture source[\s\S]*?```json\n([\s\S]*?)\n```',page).group(1)
files.append(('packages/contracts/project/fixtures/fixtures.json',fixture))
lines=['Source UTF-8 snapshot SHA256: '+hashlib.sha256(src.read_bytes()).hexdigest()]
for name,body in files:
    assert name.startswith('packages/contracts/project/') and '..' not in name
    raw=(body.rstrip()+'\n').encode('utf-8')
    (root/name).write_bytes(raw)
    lines.append(name+' '+hashlib.sha256(raw).hexdigest()+' EXTRACT_IDENTICAL=True')
api=root/'docs/API_CONTRACT.md'
base=api.read_text(encoding='utf-8').split('\n## Project planner v1')[0]
section=page.split('## Revised API contract section for `docs/API_CONTRACT.md`\n')[1].split('\n## Complete file:')[0]
api.write_bytes((base.rstrip()+'\n\n## Project planner v1.1 — proposed, not frozen\n\n'+section.rstrip()+'\n').encode('utf-8'))
lines.append('docs/API_CONTRACT.md '+hashlib.sha256(api.read_bytes()).hexdigest()+' MANAGER_HEADING; approved bootstrap preserved')
(root/'coordination/checkpoints/manager-contract23-rev2-manifest.txt').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print('\n'.join(lines))
