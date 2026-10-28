# -*- coding: utf-8 -*-
"""打印指定 cat 下 topic 的最终分布。用法: _stat_cat_topic.py <cat名>"""
import os, json, io, sys, collections

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
CAT = sys.argv[1] if len(sys.argv) > 1 else '一元积分学'
cnt = collections.Counter()
n = 0
for f in sorted(os.listdir(BASE)):
    if not f.endswith('.json'):
        continue
    with io.open(os.path.join(BASE, f), encoding='utf-8') as fh:
        d = json.load(fh)
    qs = d.get('questions', []) if isinstance(d, dict) else d
    if isinstance(qs, dict):
        qs = list(qs.values())
    for q in qs:
        if (q.get('cat') or '') == CAT:
            n += 1
            cnt[q.get('topic') or '(空)'] += 1
print('cat=%s  共 %d 题，topic 种数 %d' % (CAT, n, len([k for k in cnt if k != '(空)'])))
for k, v in cnt.most_common():
    print('  %3d  %s' % (v, k))
