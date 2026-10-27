# -*- coding: utf-8 -*-
"""由 27 题数据生成经纬研选（五）的题目卷 / 详解卷 md。

卷面规矩（老板 2026-10-23 定）：
- 题目卷：不写考点/提示，只写「第 N 题」
- 详解卷：写考点、方法点睛；AI 产出的解析必须标「AI 参考解析」
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _dy_data_a import Q1
from _dy_data_b import Q2

ALL = sorted(Q1 + Q2, key=lambda x: x['n'])

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'outputs')

TITLE = '经纬研选（五）·多元微积分（数一）'


def build_questions_md():
    L = []
    L.append('# ' + TITLE)
    L.append('')
    L.append('> **题目卷**　共 27 题，涵盖多元函数微分学的几何应用、方向导数、三重积分、'
             '第一类/第二类曲线积分、第一类/第二类曲面积分。')
    L.append('>')
    L.append('> 建议先独立完成，再对照详解卷批改。')
    L.append('')
    for q in ALL:
        L.append('### 第 %d 题' % q['n'])
        L.append('')
        L.append(q['q'])
        L.append('')
    return '\n'.join(L)


def build_solutions_md():
    L = []
    L.append('# ' + TITLE + '　AI 参考解析')
    L.append('')
    L.append('> 本卷解析由 AI 整理生成，**仅供参考**。')
    L.append('>')
    L.append('> 全部计算结论均已用独立于推导的数值方法（蒙特卡洛抽样 / 数值积分 / '
             '多种解法互验）复核；其中第 8 题、第 15 题的原稿结果有误，'
             '已按数值验证结果更正（详见各题校注）。')
    L.append('>')
    L.append('> 如发现仍有不妥，欢迎反馈修订。')
    L.append('')
    for q in ALL:
        L.append('### 第 %d 题' % q['n'])
        L.append('')
        L.append('**【考点】**%s · %s' % (q['cat'], q['topic']))
        L.append('')
        L.append('**【题目】**' + q['q'])
        L.append('')
        L.append('**【详解】**')
        L.append('')
        L.append(q['s'])
        L.append('')
        if q['type'] == 'fill' and q['a']:
            L.append('**【答案】**' + q['a'])
            L.append('')
        elif q['type'] == 'choice':
            L.append('**【答案】**' + 'ABCD'[q['a']])
            L.append('')
        L.append('---')
        L.append('')
    return '\n'.join(L)


def main():
    qp = os.path.join(OUT, '研选五-题目.md')
    sp = os.path.join(OUT, '研选五-详解.md')
    io.open(qp, 'w', encoding='utf-8').write(build_questions_md())
    io.open(sp, 'w', encoding='utf-8').write(build_solutions_md())
    print('题目卷: %s (%d 字节)' % (qp, len(build_questions_md())))
    print('详解卷: %s (%d 字节)' % (sp, len(build_solutions_md())))
    print('题数:', len(ALL))
    # 自检
    ids = [q['n'] for q in ALL]
    assert ids == list(range(1, 28)), '题号不连续: %s' % ids
    for q in ALL:
        if q['type'] == 'fill':
            assert q['a'], '填空题 %d 缺答案' % q['n']
        if q['type'] == 'choice':
            assert q['opts'] and len(q['opts']) == 4, '选择题 %d 选项不全' % q['n']
        if q['type'] == 'proof':
            assert q['s'].strip(), '解答题 %d 缺解析' % q['n']
        assert q['diff'] in ('basic', 'medium', 'hard'), '难度非法: %s' % q['diff']
        assert q['cat'] and q['topic'], '缺考点: %d' % q['n']
    import collections
    c = collections.Counter(q['diff'] for q in ALL)
    print('难度分布:', dict(c))
    c2 = collections.Counter(q['ch'] for q in ALL)
    print('章节分布:', dict(c2))
    print('自检通过 ✓')


if __name__ == '__main__':
    main()
