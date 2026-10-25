# -*- coding: utf-8 -*-
"""
修复 MathJax 语法错误（老板 2026-10-25 晚截图反馈「Extra close brace」黄条）：
1) 66 处填空占位符 `( )_}__}` → `（　）`（多余 } 导致 math 模式报错）
2) cal-di-069 / cal-int-028 / cal-limit-011 的 solution 整段被 $ 包裹且 $ 不配对 → 重写
3) comp-219 / comp-234 的 fill answer 字段被截断（\\dfrac{\\pi}{ 处戛然而止）→ 按解析补全

用法： python _fix_latex_syntax.py [--apply]
"""
import io
import json
import os
import re
import sys

APPLY = '--apply' in sys.argv
ROOT = os.path.dirname(os.path.abspath(__file__))
QDIR = os.path.join(ROOT, 'questions')

BAD_PH = re.compile(r'\(\s*\)_\}__\}')

# (文件, 题id, 字段, 旧串, 新串)
MANUAL = [
    ('calculus-double-integral.json', 'cal-di-069', 'solution',
     '$极坐标：\\int_0^{2\\pi}\\int_0^R e^{-r^2} r\\,dr\\,d\\theta = \\pi(1-e^{-R^2}) \\to \\pi$（R\\to+\\infty）。$',
     '极坐标：$\\int_0^{2\\pi}\\int_0^R e^{-r^2} r\\,dr\\,d\\theta = \\pi(1-e^{-R^2}) \\to \\pi$（$R\\to+\\infty$）。'),
    ('calculus-integral.json', 'cal-int-028', 'solution',
     '$几何意义：$y=\\sqrt{1-x^{2}}$ 表示上半圆',
     '**几何意义**：$y=\\sqrt{1-x^{2}}$ 表示上半圆'),
    ('calculus-limit.json', 'cal-limit-011', 'solution',
     '$连续性条件：$\\lim_{x\\to 0}f(x) = f(0) = 0$',
     '**连续性条件**：$\\lim_{x\\to 0}f(x) = f(0) = 0$'),
    ('comprehensive.json', 'comp-219', 'answer', None, 'b≠-1，a任意'),
    ('comprehensive.json', 'comp-234', 'answer', None, 'π/6'),
]


def main():
    n_ph = 0
    n_manual = 0
    for fn in sorted(os.listdir(QDIR)):
        if not fn.endswith('.json') or fn == 'index.json':
            continue
        path = os.path.join(QDIR, fn)
        d = json.loads(io.open(path, encoding='utf-8').read())
        items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
        touched = False
        for q in items:
            for fld in ('question', 'solution', 'answer'):
                s = q.get(fld)
                if not isinstance(s, str):
                    continue
                if '_}__}' in s:
                    new, k = BAD_PH.subn('（　）', s)
                    if k:
                        print('%s / %s / %s : 替换占位符 %d 处' % (q['id'], fn, fld, k))
                        q[fld] = new
                        n_ph += k
                        touched = True
                for f2, qid, fld2, old, new in MANUAL:
                    if fn == f2 and q['id'] == qid and fld == fld2:
                        if old is None:
                            print('%s / %s / %s : answer 重写 → %r' % (q['id'], fn, fld, new))
                            q[fld] = new
                        else:
                            if old not in s:
                                print('%s / %s / %s : !! 旧串未匹配，跳过' % (q['id'], fn, fld))
                                continue
                            q[fld] = s.replace(old, new)
                            print('%s / %s / %s : 重写段落' % (q['id'], fn, fld))
                        n_manual += 1
                        touched = True
        if touched and APPLY:
            io.open(path, 'w', encoding='utf-8').write(
                json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print()
    print('占位符替换 %d 处，手工修复 %d 处' % (n_ph, n_manual))
    print('模式：%s' % ('写入' if APPLY else '预演（未写文件）'))


if __name__ == '__main__':
    main()
