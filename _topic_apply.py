# -*- coding: utf-8 -*-
"""
topic 定标通用框架。用法: _topic_apply.py <map模块名> [--apply]
map 模块需提供：CATNAME, FILES, VOCAB, TOPIC, CATFIX
  CATNAME : 本块 cat 名
  FILES   : 涉及的文件名列表
  VOCAB   : 本块 topic 词表
  TOPIC   : {id: topic}
  CATFIX  : {id: (新cat, 新topic)}  顺带修正 cat 归错的题
"""
import os, json, io, sys, collections, importlib

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')


def load(fn):
    with io.open(os.path.join(BASE, fn), encoding='utf-8', newline='') as fh:
        raw = fh.read()
    return json.loads(raw), ('\r\n' in raw)


def dump(fn, data, crlf):
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    if crlf:
        txt = txt.replace('\n', '\r\n')
    with io.open(os.path.join(BASE, fn), 'w', encoding='utf-8', newline='') as fh:
        fh.write(txt)


def main():
    if len(sys.argv) < 2:
        print('用法: _topic_apply.py <map模块名> [--apply]')
        return 1
    m = importlib.import_module(sys.argv[1])
    APPLY = '--apply' in sys.argv
    CATNAME, FILES, VOCAB, TOPIC, CATFIX = m.CATNAME, m.FILES, m.VOCAB, m.TOPIC, m.CATFIX

    errs = []
    allids = {}
    for fn in FILES:
        data, _ = load(fn)
        for q in data.get('questions', []):
            allids[q['id']] = q

    for qid, tp in TOPIC.items():
        if qid not in allids:
            errs.append('TOPIC 里的 id 不存在: %s' % qid)
            continue
        if tp not in VOCAB:
            errs.append('%s 的 topic 不在本块词表: %s' % (qid, tp))
        c = allids[qid].get('cat') or ''
        if c != CATNAME:
            errs.append('%s 的 cat 是「%s」，不是「%s」' % (qid, c, CATNAME))
    for qid in CATFIX:
        if qid not in allids:
            errs.append('CATFIX 里的 id 不存在: %s' % qid)

    block = [q for q in allids.values() if (q.get('cat') or '') == CATNAME]
    missed = [q['id'] for q in block if q['id'] not in TOPIC and q['id'] not in CATFIX]
    if missed:
        errs.append('本块有 %d 题未分配 topic: %s' % (len(missed), missed))

    if errs:
        print('!! 前置校验未通过，共 %d 条：' % len(errs))
        for e in errs:
            print('   -', e)
        return 1

    print('前置校验通过：本块 %d 题，TOPIC %d 条，CATFIX %d 条' % (len(block), len(TOPIC), len(CATFIX)))
    print()
    print('=== topic 分布（写入后）===')
    cnt = collections.Counter(TOPIC.values())
    for v in VOCAB:
        print('  %-16s %3d 题' % (v, cnt.get(v, 0)))
    print('  合计 %d 题，%d 种' % (sum(cnt.values()), len([v for v in VOCAB if cnt.get(v)])))
    if CATFIX:
        print()
        print('=== cat 修正 ===')
        for qid, (c, t) in sorted(CATFIX.items()):
            print('  %-12s %s -> %s   topic=%s' % (qid, allids[qid].get('cat'), c, t or '(留空待定)'))

    if not APPLY:
        print()
        print('[dry-run] 未写入。加 --apply 才写。')
        return 0

    for fn in FILES:
        data, crlf = load(fn)
        n = 0
        for q in data.get('questions', []):
            if q['id'] in TOPIC:
                q['topic'] = TOPIC[q['id']]
                n += 1
            if q['id'] in CATFIX:
                c, t = CATFIX[q['id']]
                q['cat'] = c
                q['topic'] = t
                n += 1
        if n:
            dump(fn, data, crlf)
        print('写入 %s：改动 %d 题（%s）' % (fn, n, 'CRLF' if crlf else 'LF'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
