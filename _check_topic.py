# -*- coding: utf-8 -*-
"""通用核对：逐字段 diff 备份 vs 新文件，确认只动了 topic 与 CATFIX 里的 cat。
用法: _check_topic.py <map模块名> <备份TAG>"""
import os, json, io, sys, collections, importlib

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')


def load(fn):
    with io.open(os.path.join(BASE, fn), encoding='utf-8') as fh:
        d = json.load(fh)
    return {q['id']: q for q in d.get('questions', [])}


def main():
    m = importlib.import_module(sys.argv[1])
    TAG = sys.argv[2]
    FILES, CATFIX_IDS = m.FILES, set(m.CATFIX)
    bad = 0
    changed_fields = collections.Counter()
    topic_new = collections.Counter()
    cat_pairs = collections.Counter()
    n_changed = 0

    for fn in FILES:
        old = load(fn + '.' + TAG)
        new = load(fn)
        if set(old) != set(new):
            print('!! %s 题目集合变了：新增 %s 丢失 %s' % (fn, set(new) - set(old), set(old) - set(new)))
            bad += 1
            continue
        for qid in old:
            o, n = old[qid], new[qid]
            if o == n:
                continue
            n_changed += 1
            diff = [k for k in (set(o) | set(n)) if o.get(k) != n.get(k)]
            for k in diff:
                changed_fields[k] += 1
            if diff == ['topic']:
                topic_new[n.get('topic', '')] += 1
            elif set(diff) <= {'cat', 'topic'} and qid in CATFIX_IDS:
                cat_pairs[(o.get('cat', ''), n.get('cat', ''))] += 1
                if 'topic' in diff:
                    topic_new[n.get('topic', '')] += 1
            else:
                print('!! 意外改动 %s (%s)：字段 %s' % (qid, fn, diff))
                for k in diff:
                    print('     %s: %r -> %r' % (k, o.get(k), n.get(k)))
                bad += 1

    print('改动题数 %d' % n_changed)
    print('被改字段统计：', dict(changed_fields))
    print()
    print('=== 新 topic 计数（本次实际写入的题）===')
    for k, v in topic_new.most_common():
        print('  %3d  %s' % (v, k or '(置空)'))
    if cat_pairs:
        print()
        print('=== cat 修正 ===')
        for (o, n), c in cat_pairs.items():
            print('  %s -> %s  (%d 题)' % (o, n, c))
    print()
    ok = set(changed_fields) <= {'topic', 'cat'}
    print('字段是否只限于 topic/cat：', 'PASS' if ok else 'FAIL')
    if not ok:
        bad += 1
    print('结论：', 'PASS（零意外损伤）' if bad == 0 else 'FAIL（%d 处问题）' % bad)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
