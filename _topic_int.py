# -*- coding: utf-8 -*-
"""
一元积分学（cat=一元积分学，97 题）topic 定标。
判据：一个 topic = 真题里能单独当一个考点的东西。
用法: _topic_int.py [--apply]
"""
import os, json, io, sys, collections

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
APPLY = '--apply' in sys.argv
CATNAME = '一元积分学'

# 本块 topic 词表（9 个）
VOCAB = [
    '不定积分计算',
    '定积分计算',
    '变限积分求导',
    '变限积分求极限',
    '变限积分函数性质',
    '积分方程',
    '反常积分',
    '定积分几何应用',
    '定积分物理应用',
]

I = '不定积分计算'
D = '定积分计算'
DQ = '变限积分求导'
DL = '变限积分求极限'
DP = '变限积分函数性质'
IE = '积分方程'
IM = '反常积分'
G = '定积分几何应用'
P = '定积分物理应用'

TOPIC = {
    # ---- calculus-integral.json ----
    'cal-int-001': I, 'cal-int-002': I, 'cal-int-003': I, 'cal-int-004': I,
    'cal-int-006': I, 'cal-int-007': I, 'cal-int-008': I, 'cal-int-012': I,
    'cal-int-014': I, 'cal-int-022': I, 'cal-int-023': I, 'cal-int-026': I,
    'cal-int-027': I, 'cal-int-029': I, 'cal-int-036': I, 'cal-int-047': I,
    'cal-int-005': D, 'cal-int-009': D, 'cal-int-010': D, 'cal-int-011': D,
    'cal-int-021': D, 'cal-int-024': D, 'cal-int-025': D, 'cal-int-028': D,
    'cal-int-045': D, 'cal-int-050': D,
    'cal-int-016': DQ, 'cal-int-017': DQ,
    'cal-int-020': G, 'cal-int-048': G, 'cal-int-052': G, 'cal-int-053': G,
    'cal-int-054': G, 'cal-int-055': G, 'cal-int-056': G, 'cal-int-057': G,
    'cal-int-058': G, 'cal-int-059': G, 'cal-int-064': G,
    'cal-int-060': P, 'cal-int-061': P, 'cal-int-062': P, 'cal-int-063': P,
    'cal-int-065': P,
    'cal-int-049': IM,
    'cal-int-101': DL, 'cal-int-102': DL, 'cal-int-103': DL, 'cal-int-104': DL,
    'cal-int-105': DL, 'cal-int-106': DL, 'cal-int-107': DL, 'cal-int-108': DL,
    'cal-int-109': DL, 'cal-int-110': DL,
    'cal-int-111': IM, 'cal-int-112': IM, 'cal-int-113': IM, 'cal-int-114': IM,
    'cal-int-115': IM, 'cal-int-116': IM, 'cal-int-117': IM,
    # ---- comprehensive.json ----
    'comp-013': DQ, 'comp-014': DQ, 'comp-017': DQ, 'comp-018': DQ, 'comp-227': DQ,
    'comp-015': IE, 'comp-016': IE, 'comp-019': IE, 'comp-034': IE,
    'comp-241': IE, 'comp-242': IE,
    'comp-021': D, 'comp-022': D, 'comp-023': D, 'comp-235': D, 'comp-317': D,
    'comp-024': DL, 'comp-210': DL, 'comp-215': DL, 'comp-224': DL, 'comp-228': DL,
    'comp-230': DP, 'comp-232': DP, 'comp-237': DP, 'comp-302': DP,
    'comp-233': G, 'comp-234': G, 'comp-318': G,
    'comp-306': P,
    'comp-238': IM, 'comp-311': IM,
}

# 顺带修正上一轮 cat 归错的 4 道题（这些题主考点不在一元积分学）
CATFIX = {
    'comp-231': ('二重积分', '二重积分换序'),
    'comp-239': ('二重积分', '二重积分换序'),
    'comp-236': ('一元微分学', '渐近线'),
    'comp-240': ('微分方程', ''),          # topic 等微分方程块定词表时再补
}

TARGET_FILES = ['calculus-integral.json', 'comprehensive.json']


def load(fn):
    p = os.path.join(BASE, fn)
    with io.open(p, encoding='utf-8', newline='') as fh:
        raw = fh.read()
    crlf = '\r\n' in raw
    data = json.loads(raw)
    return data, crlf


def dump(fn, data, crlf):
    p = os.path.join(BASE, fn)
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    if crlf:
        txt = txt.replace('\n', '\r\n')
    with io.open(p, 'w', encoding='utf-8', newline='') as fh:
        fh.write(txt)


def main():
    # ---- 前置校验 ----
    errs = []
    allids = {}
    for fn in TARGET_FILES:
        data, _ = load(fn)
        qs = data.get('questions', [])
        for q in qs:
            allids[q['id']] = q

    for qid, tp in TOPIC.items():
        if qid not in allids:
            errs.append('MAP 里的 id 不存在: %s' % qid)
            continue
        if tp not in VOCAB:
            errs.append('%s 的 topic 不在本块词表: %s' % (qid, tp))
        c = allids[qid].get('cat') or ''
        if c != CATNAME:
            errs.append('%s 的 cat 是「%s」，不是「%s」' % (qid, c, CATNAME))
    for qid, (c, t) in CATFIX.items():
        if qid not in allids:
            errs.append('CATFIX 里的 id 不存在: %s' % qid)

    # 覆盖检查：本块 97 题是否全部被 MAP 覆盖
    block = [q for q in allids.values() if (q.get('cat') or '') == CATNAME]
    missed = [q['id'] for q in block if q['id'] not in TOPIC and q['id'] not in CATFIX]
    if missed:
        errs.append('本块有 %d 题未分配 topic: %s' % (len(missed), missed))

    if errs:
        print('!! 前置校验未通过，共 %d 条：' % len(errs))
        for e in errs:
            print('   -', e)
        return 1

    print('前置校验通过')
    print('本块题数 %d，MAP 覆盖 %d，CATFIX %d' % (len(block), len(TOPIC), len(CATFIX)))
    print('改动题数 %d' % (len(TOPIC) + len(CATFIX)))
    print()
    print('=== topic 分布（本块 97 题）===')
    cnt = collections.Counter(TOPIC.values())
    for v in VOCAB:
        print('  %-12s %3d 题' % (v, cnt.get(v, 0)))
    print()
    print('=== cat 修正 ===')
    for qid, (c, t) in sorted(CATFIX.items()):
        print('  %-12s %s -> %s   topic=%s' % (qid, allids[qid].get('cat'), c, t or '(留空待定)'))

    if not APPLY:
        print()
        print('[dry-run] 未写入。加 --apply 才写。')
        return 0

    # ---- 写入 ----
    for fn in TARGET_FILES:
        data, crlf = load(fn)
        qs = data.get('questions', [])
        n = 0
        for q in qs:
            if q['id'] in TOPIC:
                q['topic'] = TOPIC[q['id']]
                n += 1
            if q['id'] in CATFIX:
                c, t = CATFIX[q['id']]
                q['cat'] = c
                q['topic'] = t          # comp-240 置空，等微分方程块定词表再补
                n += 1
        dump(fn, data, crlf)
        print('写入 %s：改动 %d 题（换行符 %s）' % (fn, n, 'CRLF' if crlf else 'LF'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
