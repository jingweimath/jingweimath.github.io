# -*- coding: utf-8 -*-
"""把「变限积分与反常积分专项 17 题」写入 questions/calculus-integral.json

安全流程：备份 → dry-run → --apply → 逐题核对
字段映射：n→id, type, diff→difficulty, q→question, opts→options, a→answer,
          s→solution, cat, topic, source（固定）
"""
import io
import json
import os
import sys
import shutil
import time

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from _newint_a import A as PART_A
from _newint_b import B as PART_B

TARGET = os.path.join(ROOT, 'questions', 'calculus-integral.json')
ID_FMT = 'cal-int-1%02d'          # 101 ~ 117
SOURCE = '经纬自编·变限积分与反常积分专项'
VALID_DIFF = ('basic', 'medium', 'hard')

ALL = sorted(PART_A + PART_B, key=lambda x: x['n'])


def build_items():
    """把数据转成题库字段格式，同时做完整性校验。"""
    items = []
    seen = set()
    for k, q in enumerate(ALL, start=1):
        n = q['n']
        qid = ID_FMT % k
        assert qid not in seen, 'ID 重复: %s' % qid
        seen.add(qid)

        assert n == k, '题号与顺序不符: %s' % n
        assert q['type'] in ('choice', 'fill', 'proof'), '非法题型: %s' % q['type']
        assert q['diff'] in VALID_DIFF, '难度非法: 第%d题 %s' % (n, q['diff'])
        assert q['q'].strip(), '第%d题 缺题面' % n
        assert q['s'].strip(), '第%d题 缺解析' % n

        item = {
            'id': qid,
            'type': q['type'],
            'difficulty': q['diff'],
            'question': q['q'],
            'solution': q['s'],
            'cat': q['cat'],
            'topic': q['topic'],
            'source': SOURCE,
        }
        if q['type'] == 'choice':
            assert len(q['opts']) == 4, '第%d题 选项数不为4' % n
            assert isinstance(q['a'], int) and 0 <= q['a'] <= 3, \
                '第%d题 答案索引非法: %r' % (n, q['a'])
            item['options'] = list(q['opts'])
            item['answer'] = q['a']
        elif q['type'] == 'fill':
            assert str(q['a']).strip(), '第%d题 填空题缺答案' % n
            item['answer'] = q['a']
        else:  # proof
            item['answer'] = str(q.get('a', '') or '')
        items.append(item)
    return items


def main():
    apply = '--apply' in sys.argv
    items = build_items()

    data = json.load(io.open(TARGET, encoding='utf-8'))
    before = len(data['questions'])
    exist_ids = {qq['id'] for qq in data['questions']}
    clash = [it['id'] for it in items if it['id'] in exist_ids]
    assert not clash, 'ID 与现有题库冲突: %s' % clash

    print('目标文件: %s' % TARGET)
    print('现有题数: %d' % before)
    print('待写入  : %d' % len(items))
    print()
    for it in items:
        ans = it['answer']
        if isinstance(ans, str):
            shown = ans[:30] + ('…' if len(ans) > 30 else '')
        else:
            shown = '索引 %d' % ans
        print('  %-14s %-6s %-6s %-22s 答案=%s'
              % (it['id'], it['type'], it['difficulty'], it['topic'][:20], shown))
    print()

    if not apply:
        print('>>> dry-run，未写入。加 --apply 执行。')
        return

    stamp = time.strftime('%Y%m%d')
    bak = TARGET + '.bak-' + stamp + 'newint17'
    shutil.copy2(TARGET, bak)
    print('已备份: %s' % os.path.basename(bak))

    data['questions'].extend(items)
    with io.open(TARGET, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('已写入，题数 %d -> %d' % (before, len(data['questions'])))


if __name__ == '__main__':
    main()
