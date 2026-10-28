# -*- coding: utf-8 -*-
"""生成「变限积分与反常积分专项 20 题」的题目卷 / 详解卷 md。

卷面规矩（老板 2026-10-23 定）：
- 题目卷：不写考点/提示，每题只写「第 N 题」（选择题带 ABCD 选项）
- 详解卷：写考点、难度、答案、详解；AI 产出的解析必须标「AI 参考解析」
"""
import io
import os
import sys
import collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _newint_a import A
from _newint_b import B

ALL = sorted(A + B, key=lambda x: x['n'])
NTOTAL = len(ALL)
NVAR = sum(1 for q in ALL if q['n'] <= 10)   # 变限积分部分
NABN = NTOTAL - NVAR                        # 反常积分部分

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'outputs')

TITLE = '变限积分与反常积分专项（%d 题）' % NTOTAL
DIFF_CN = {'basic': '基础', 'medium': '适中', 'hard': '较难'}


def build_questions_md():
    L = []
    L.append('# ' + TITLE)
    L.append('')
    L.append('> **题目卷**　共 %d 题：**变限积分（分式型）**第 1~%d 题，'
             '**反常积分**第 %d~%d 题。' % (NTOTAL, NVAR, NVAR + 1, NTOTAL))
    L.append('>')
    _c = collections.Counter(q['diff'] for q in ALL)
    L.append('> 难度构成：' + ' · '.join('%s %d 题' % (DIFF_CN[k], _c[k])
                                        for k in ('basic', 'medium', 'hard') if _c[k]))
    L.append('>')
    L.append('> 建议先独立完成，再对照详解卷批改。')
    L.append('')
    for q in ALL:
        L.append('### 第 %d 题' % q['n'])
        L.append('')
        L.append(q['q'])
        L.append('')
        if q['type'] == 'choice':
            L.append('（A）%s　　（B）%s　　（C）%s　　（D）%s'
                     % (q['opts'][0], q['opts'][1], q['opts'][2], q['opts'][3]))
            L.append('')
    return '\n'.join(L)


def build_solutions_md():
    L = []
    L.append('# ' + TITLE + '　AI 参考解析')
    L.append('')
    L.append('> 本卷解析由 AI 整理生成，**仅供参考**。')
    L.append('>')
    L.append('> 全部 %d 题的结论均已用**独立于推导的数值方法**复核：' % NTOTAL + ''
             'mpmath 60 位高精度自适应积分；极限题采用两尺度收敛阶自洽检验'
             '（误差随尺度缩小的实测阶数须与被积函数展开阶数吻合），'
             '无穷远极限另做 $1/x^{2}$ 型 Richardson 外推。')
    L.append('>')
    L.append('> 如发现仍有不妥，欢迎反馈修订。')
    L.append('')
    for q in ALL:
        L.append('### 第 %d 题' % q['n'])
        L.append('')
        L.append('**【考点】**%s · %s　　**【难度】**%s'
                 % (q['cat'], q['topic'], DIFF_CN[q['diff']]))
        L.append('')
        L.append('**【题目】**' + q['q'])
        L.append('')
        L.append('**【详解】**')
        L.append('')
        L.append(q['s'])
        L.append('')
        # proof 题若题面要求「求值」，同样给答案；纯证明题答案为空则不输出
        if q['type'] in ('fill', 'proof') and str(q['a']).strip():
            L.append('**【答案】**' + q['a'])
            L.append('')
        elif q['type'] == 'choice':
            L.append('**【答案】**（%s）' % 'ABCD'[q['a']])
            L.append('')
        L.append('---')
        L.append('')
    return '\n'.join(L)


def main():
    qmd = build_questions_md()
    smd = build_solutions_md()
    qp = os.path.join(OUT, '变限积分与反常积分专项-题目.md')
    sp = os.path.join(OUT, '变限积分与反常积分专项-详解.md')
    io.open(qp, 'w', encoding='utf-8').write(qmd)
    io.open(sp, 'w', encoding='utf-8').write(smd)
    print('题目卷: %s (%d 字节)' % (qp, len(qmd)))
    print('详解卷: %s (%d 字节)' % (sp, len(smd)))

    # ---------------- 自检 ----------------
    ns = [q['n'] for q in ALL]
    assert ns == list(range(1, NTOTAL + 1)), '题号不连续: %s' % ns
    for q in ALL:
        if q['type'] == 'fill':
            assert str(q['a']).strip(), '填空题 %d 缺答案' % q['n']
        elif q['type'] == 'choice':
            assert len(q['opts']) == 4, '选择题 %d 选项数不为 4' % q['n']
            assert 0 <= q['a'] <= 3, '选择题 %d 答案索引越界' % q['n']
        elif q['type'] == 'proof':
            assert q['s'].strip(), '证明题 %d 缺解析' % q['n']
        else:
            raise AssertionError('非法题型: %s' % q['type'])
        assert q['diff'] in ('basic', 'medium', 'hard'), '难度非法: %s' % q['diff']
        assert q['cat'] and q['topic'], '缺考点: %d' % q['n']
        assert q['q'].strip(), '缺题面: %d' % q['n']
    c = collections.Counter(q['diff'] for q in ALL)
    c2 = collections.Counter(q['type'] for q in ALL)
    print('题数:', len(ALL))
    print('难度分布:', dict(c))
    print('题型分布:', dict(c2))
    print('自检通过')


if __name__ == '__main__':
    main()
