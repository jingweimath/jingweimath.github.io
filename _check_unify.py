# -*- coding: utf-8 -*-
"""核对 cat 统一是否只改了 cat 字段，且题数/ID/内容零损伤。"""
import json, io, os, sys, glob, collections
sys.stdout.reconfigure(encoding='utf-8')

QD = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
BLOCKS = set(['极限与连续', '一元微分学', '一元积分学', '多元微分学', '二重积分',
              '三重·曲线曲面积分', '微分方程', '无穷级数', '向量代数与空间解析几何',
              '线性代数', '概率统计'])

allold, allnew = [], []
diffs = []
for p in sorted(glob.glob(os.path.join(QD, '*.json'))):
    b = p + '.bak-20261028cat'
    if not os.path.exists(b):
        print('!! 缺备份:', p)
        continue
    o = json.load(io.open(b, encoding='utf-8', newline=''))
    n = json.load(io.open(p, encoding='utf-8', newline=''))
    if 'questions' not in n:
        if o == n:
            continue
        diffs.append((p, '<无 questions 却被改>', '', ''))
        continue
    if sorted(o.keys()) != sorted(n.keys()):
        diffs.append((p, '<顶层键>', sorted(o.keys()), sorted(n.keys())))
    for k in o:
        if k != 'questions' and o[k] != n[k]:
            diffs.append((p, '<章节元字段 %s>' % k, str(o[k])[:30], str(n[k])[:30]))
    od = {q['id']: q for q in o['questions']}
    nd = {q['id']: q for q in n['questions']}
    if set(od) != set(nd):
        diffs.append((p, '<ID 集合>', len(od), len(nd)))
    for i in nd:
        if i not in od:
            continue
        a, c = od[i], nd[i]
        if set(a) != set(c):
            added, removed = set(c) - set(a), set(a) - set(c)
            if added == {'cat'} and not removed:
                diffs.append((i, '<新增字段 cat>', '', ''))   # 原本无 cat 键，属预期
                for f in a:
                    if a.get(f) != c.get(f):
                        diffs.append((i, f + '(新增cat时)', str(a.get(f))[:26], str(c.get(f))[:26]))
                continue
            diffs.append((i, '<字段集异常>', sorted(added), sorted(removed)))
            continue
        for f in c:
            if a.get(f) != c.get(f):
                diffs.append((i, f, str(a.get(f))[:26], str(c.get(f))[:26]))
    allold += o['questions']
    allnew += n['questions']

print('旧题数 %d | 新题数 %d' % (len(allold), len(allnew)))
print()
byfield = collections.Counter(d[1] for d in diffs)
print('发生变化的字段统计:', dict(byfield))
other = [d for d in diffs if d[1] not in ('cat', '<新增字段 cat>')]
print('非 cat 的改动:', other or '无')
print('  （cat=%d 表示原有值被改写，<新增字段 cat>=%d 表示原本无此键、本次补上）'
      % (byfield.get('cat', 0), byfield.get('<新增字段 cat>', 0)))
print()

# cat 全覆盖 + 白名单
empty = [q['id'] for q in allnew if not str(q.get('cat', '')).strip()]
bad = [q['id'] for q in allnew if q.get('cat') not in BLOCKS]
print('cat 为空:', len(empty))
print('cat 不在 11 块白名单:', len(bad), bad[:5])
print()
print('=== 统一后 cat 分布 ===')
c = collections.Counter(q.get('cat') for q in allnew)
for k, v in c.most_common():
    print('  %-22s %4d' % (k, v))
print('  词数:', len(c), '| 合计:', sum(c.values()))
print()
# 换的到底是什么：抽样看几条
print('=== 抽样：改前 -> 改后 ===')
od = {q['id']: q for q in allold}
shown = 0
for q in allnew:
    o = od.get(q['id'])
    if o and str(o.get('cat', '')).strip() != q.get('cat'):
        print('  %-12s %-14s -> %s' % (q['id'], repr(str(o.get('cat', '')))[:16], q['cat']))
        shown += 1
        if shown >= 12:
            break
print()
print('核对结论:', 'PASS' if (not empty and not bad and not other) else 'FAIL')
