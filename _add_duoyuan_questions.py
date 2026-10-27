# -*- coding: utf-8 -*-
"""把研选（五）·多元 27 题写入题库。

ID 分配（接在现有最大编号之后）：
  多元函数微分学 6 题  → cal-md-116 ~ cal-md-121
  三重积分与曲线曲面积分 21 题 → cal-tc-054 ~ cal-tc-074

默认 dry-run，加 --apply 才写文件。
"""
import io
import json
import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _dy_data_a import Q1
from _dy_data_b import Q2

ROOT = os.path.dirname(os.path.abspath(__file__))
APPLY = '--apply' in sys.argv

FILE = {'md': os.path.join(ROOT, 'questions', 'calculus-multi-diff.json'),
        'tc': os.path.join(ROOT, 'questions', 'calculus-triple-curve.json')}
PREFIX = {'md': 'cal-md-%03d', 'tc': 'cal-tc-%03d'}
START = {'md': 116, 'tc': 54}

ALL = sorted(Q1 + Q2, key=lambda x: x['n'])


def load(p):
    d = json.loads(io.open(p, encoding='utf-8').read())
    return d, (d['questions'] if isinstance(d, dict) and 'questions' in d else d)


def main():
    print('=' * 70)
    print('研选五·多元 27 题入库%s' % ('（写入）' if APPLY else '（预演，未写入）'))
    print('=' * 70)

    # 先收集现有 ID，防冲突
    existing = set()
    for f in FILE.values():
        _, items = load(f)
        for q in items:
            existing.add(q['id'])

    counters = {'md': START['md'], 'tc': START['tc']}
    newby = {'md': [], 'tc': []}
    for q in ALL:
        ch = q['ch']
        qid = PREFIX[ch] % counters[ch]
        counters[ch] += 1
        if qid in existing:
            print('✗ ID 冲突：%s' % qid)
            return 1
        existing.add(qid)
        item = dict(id=qid, type=q['type'], difficulty=q['diff'],
                    question=q['q'], solution=q['s'],
                    cat=q['cat'], topic=q['topic'], source='经纬研选（五）·数一多元')
        if q['type'] == 'choice':
            item['options'] = list(q['opts'])
            item['answer'] = int(q['a'])
        else:
            item['answer'] = q['a']
        newby[ch].append(item)
        print('  第 %2d 题 → %s  %-6s %-6s %s' % (q['n'], qid, q['type'], q['diff'], q['topic']))

    for ch, f in FILE.items():
        d, items = load(f)
        before = len(items)
        items.extend(newby[ch])
        print('%s: %d → %d 题' % (os.path.basename(f), before, len(items)))
        if APPLY:
            out = json.dumps(d, ensure_ascii=False, indent=2)
            io.open(f, 'w', encoding='utf-8').write(out)

    c = collections.Counter(q['diff'] for q in ALL)
    print('新增难度分布:', dict(c))
    print()
    print('写入：%s' % ('是' if APPLY else '否（dry-run）'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
