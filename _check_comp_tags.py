# -*- coding: utf-8 -*-
"""
标签核验：对本轮新标的 99 道题，按 cat 分组打印「题面 + 标签」供人工逐条复核。
另保留 3 条**高精度**交叉规则（不会有歧义的那些）。
"""
import io
import json
import os
import re
import sys
import collections

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, 'questions', 'comprehensive.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

d = json.load(io.open(SRC, encoding='utf-8', newline=''))
qs = d['questions']
import _add_comp_tags as m
NEW = m.MAP
new = [q for q in qs if q['id'] in NEW]

BS = chr(92)
# ---- 高精度规则：这些词出现时，归属几乎无歧义 ----
RULES = [
    ('题面明写「微分方程/通解/特解/积分因子」', re.compile(r'微分方程|积分因子'), {'微分方程'}),
    ('题面明写「偏导/偏导数」或含 \\partial', re.compile(r'偏导|' + BS + BS + r'partial|∂'), {'多元微积分'}),
    ('题面明写「换积分次序/交换次序」', re.compile(r'交换积分次序|交换次序|换积分次序'), {'二重积分'}),
    ('题面明写「幂级数/麦克劳林/敛散性」', re.compile(r'幂级数|麦克劳林|敛散性'), {'无穷级数'}),
    ('题面明写「二次型」', re.compile(r'二次型'), {'二次型'}),
    ('题面明写「特征值」', re.compile(r'特征值'), {'特征值', '二次型'}),
    ('题面明写「可导/可微/导数定义」', re.compile(r'可导|可微|导数定义'), {'极限与微分', '多元微积分'}),
]
print('=' * 80)
print('高精度交叉规则检查（只挑题面明写关键词的）')
print('=' * 80)
bad = 0
for name, rx, should in RULES:
    for q in qs:
        if rx.search(q.get('question', '')):
            if str(q.get('cat', '')).strip() not in should:
                bad += 1
                print('  ✗ %s  cat=%s  | %s' % (q['id'], q.get('cat'),
                                                re.sub(r'\s+', ' ', q['question'])[:70]))
print('  冲突数：%d' % bad)
print()

# ---- 分组逐条列出本轮新标的题 ----
print('=' * 80)
print('本轮新标 99 题 · 按 cat 分组（人工复核用）')
print('=' * 80)
groups = collections.defaultdict(list)
for q in new:
    groups[q.get('cat', '?')].append(q)
for cat in sorted(groups, key=lambda c: -len(groups[c])):
    lst = groups[cat]
    print()
    print('── %s  （%d 题）' % (cat, len(lst)))
    for q in lst:
        t = re.sub(r'\s+', ' ', q['question'])
        t = t.replace('$', '')
        print('   %-11s %-26s %s' % (q['id'], q.get('topic', '')[:24], t[:88]))
print()
print('=' * 80)
print('topic 重复度检查（同一 topic 出现多次 → 可能区分度不够）')
print('=' * 80)
cnt = collections.Counter(q.get('topic', '') for q in new)
rep = [(k, v) for k, v in cnt.items() if v > 1]
if rep:
    for k, v in sorted(rep, key=lambda x: -x[1]):
        print('  ×%d  %s' % (v, k))
else:
    print('  无重复')
print()
print('topic 总词数：%d 种 / 99 题' % len(cnt))
