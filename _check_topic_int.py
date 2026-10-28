# -*- coding: utf-8 -*-
"""核对 _topic_int.py 的改动：逐字段 diff 备份 vs 新文件，确认只动了 topic 与 4 道 cat"""
import os, json, io, sys, collections

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
TAG = 'bak-20261028topic'
FILES = ['calculus-integral.json', 'comprehensive.json']
CATFIX_IDS = {'comp-231', 'comp-236', 'comp-239', 'comp-240'}


def load(fn):
    with io.open(os.path.join(BASE, fn), encoding='utf-8') as fh:
        d = json.load(fh)
    return {q['id']: q for q in d.get('questions', [])}


def main():
    bad = 0
    changed_fields = collections.Counter()
    topic_pairs = collections.Counter()
    cat_pairs = collections.Counter()
    n_changed = 0

    for fn in FILES:
        old = load(fn + '.' + TAG)
        new = load(fn)
        if set(old) != set(new):
            print('!! %s 题目集合变了：新增 %s 丢失 %s' % (
                fn, set(new) - set(old), set(old) - set(new)))
            bad += 1
            continue
        for qid in old:
            o, n = old[qid], new[qid]
            if o == n:
                continue
            n_changed += 1
            keys = set(o) | set(n)
            diff = [k for k in keys if o.get(k) != n.get(k)]
            for k in diff:
                changed_fields[k] += 1
            if diff == ['topic']:
                topic_pairs[(o.get('topic', ''), n.get('topic', ''))] += 1
            elif diff == ['cat'] and qid in CATFIX_IDS:
                cat_pairs[(o.get('cat', ''), n.get('cat', ''))] += 1
            elif set(diff) == {'cat', 'topic'} and qid in CATFIX_IDS:
                cat_pairs[(o.get('cat', ''), n.get('cat', ''))] += 1
                topic_pairs[('<cat修正>', n.get('topic', ''))] += 1
            else:
                print('!! 意外改动 %s (%s)：字段 %s' % (qid, fn, diff))
                for k in diff:
                    print('     %s: %r -> %r' % (k, o.get(k), n.get(k)))
                bad += 1

    print('改动题数 %d' % n_changed)
    print('被改字段统计：', dict(changed_fields))
    print()
    print('=== 新 topic 分布（本次写入）===')
    tot = collections.Counter()
    for (o, n), c in topic_pairs.items():
        tot[n] += c
    for k, v in tot.most_common():
        print('  %-14s %3d 题' % (k or '(置空)', v))
    print()
    print('=== cat 修正 ===')
    for (o, n), c in cat_pairs.items():
        print('  %s -> %s  (%d 题)' % (o, n, c))
    print()
    ok_fields = set(changed_fields) <= {'topic', 'cat'}
    print('字段是否只限于 topic/cat：', 'PASS' if ok_fields else 'FAIL')
    if not ok_fields:
        bad += 1
    print('结论：', 'PASS（零意外损伤）' if bad == 0 else 'FAIL（%d 处问题）' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
