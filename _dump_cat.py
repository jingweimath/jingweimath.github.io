# -*- coding: utf-8 -*-
"""按 cat 导出题目摘要：id / 文件 / 现有topic / 题干前N字。用法: _dump_cat.py <cat名> [截断长度]"""
import os, json, io, sys, re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
CAT = sys.argv[1] if len(sys.argv) > 1 else '一元积分学'
N = int(sys.argv[2]) if len(sys.argv) > 2 else 130

out = []
for f in sorted(os.listdir(BASE)):
    if not f.endswith('.json'):
        continue
    with io.open(os.path.join(BASE, f), encoding='utf-8') as fh:
        data = json.load(fh)
    qs = data.get('questions', []) if isinstance(data, dict) else data
    if isinstance(qs, dict):
        qs = list(qs.values())
    for q in qs:
        if (q.get('cat') or '') != CAT:
            continue
        stem = re.sub(r'\s+', ' ', (q.get('question') or ''))[:N]
        out.append((q.get('id'), f.replace('.json', ''), q.get('topic') or '', stem))

print('### cat=%s  共 %d 题' % (CAT, len(out)))
for i, (qid, fn, tp, stem) in enumerate(out, 1):
    print('%3d|%s|%s|%s|%s' % (i, qid, fn, tp, stem))
