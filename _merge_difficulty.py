# -*- coding: utf-8 -*-
"""难度四档 → 三档：把 expert（拔高）并入 hard（较难）。

只改 difficulty 字段，其他一个字不动。
部分题目原本就标 expert 的 → 改成 hard；已是 hard 的不动。
"""
import io
import json
import glob
import os
import sys
import collections

QDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
APPLY = '--apply' in sys.argv
OLD, NEW = 'expert', 'hard'

changed = []
before = collections.Counter()
after = collections.Counter()

for f in sorted(glob.glob(os.path.join(QDIR, '*.json'))):
    if os.path.basename(f) == 'index.json':
        continue
    raw = io.open(f, encoding='utf-8').read()
    d = json.loads(raw)
    items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
    local = 0
    for q in items:
        old = q.get('difficulty')
        before[old] += 1
        new = old
        if old == OLD:
            new = NEW
            local += 1
            changed.append((os.path.basename(f), q['id']))
        q['difficulty'] = new
        after[new] += 1
    out = json.dumps(d, ensure_ascii=False, indent=2)
    if APPLY and local:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(out)

print('=' * 70)
print('难度四档 → 三档%s' % ('（写入）' if APPLY else '（预演，未写入）'))
print('=' * 70)
print('改前：', dict(before))
print('改后：', dict(after))
print('改动的题数：%d' % len(changed))
by_file = collections.Counter(c[0] for c in changed)
for k, v in by_file.most_common():
    print('  %-32s %d 道' % (k, v))
if len(changed) != before[OLD]:
    print('✗ 数量对不上：应改 %d，实改 %d' % (before[OLD], len(changed)))
    sys.exit(1)
