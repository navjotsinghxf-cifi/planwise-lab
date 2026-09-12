"""Reproduce extraction comparisons and destination SHA-256 evidence."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
snapshot = root / 'coordination/checkpoints/manager-contract23-source.json'
response = json.loads(snapshot.read_text(encoding='utf-8'))
page = json.loads(response['content'][0]['text'])['text']
files = re.findall(r'## Complete file: `([^`]+)`\n```[^\n]*\n([\s\S]*?)\n```', page)
print('Snapshot SHA256:', hashlib.sha256(snapshot.read_bytes()).hexdigest())
for name, body in files:
    expected = (body.rstrip() + '\n').encode('utf-8')
    actual = (root / name).read_bytes()
    digest = hashlib.sha256(actual).hexdigest()
    print(name, digest, 'EXTRACT_IDENTICAL=' + str(actual == expected))
    assert actual == expected, name
name = 'docs/API_CONTRACT.md'
print(name, hashlib.sha256((root / name).read_bytes()).hexdigest(), 'MANAGER_WRAPPER_ADDED; see git diff')
