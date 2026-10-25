# -*- coding: utf-8 -*-
"""撞击测试：故意注入坏题，验证 build_questions.py 会不会真的拦住。

三种坏法（都是历史上真出现过的）：
  A. 题面 LaTeX 多余 }         → 读者看到 MathJax 黄条
  B. 选择题 answer 存成 'A'    → 点选项永远判错
  C. id 重复                   → 抽题/错题本串题
每轮：注入 → 跑 build → 断言 exit!=0 且 bundle 未被覆盖 → 恢复。
"""
import io
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.join(ROOT, 'questions', 'comprehensive.json')
BAK = TARGET + '.bak-gatetest'
BUNDLE = os.path.join(ROOT, 'questions-bundle-v2.js')
PYTHON = sys.executable


def md5(p):
    import hashlib
    return hashlib.md5(open(p, 'rb').read()).hexdigest()


def run_build(extra=()):
    r = subprocess.run([PYTHON, os.path.join(ROOT, 'build_questions.py'),
                        '--no-version', *extra],
                       capture_output=True, text=True, cwd=ROOT)
    return r.returncode, r.stdout + r.stderr


def inject(mutate):
    d = json.loads(io.open(TARGET, encoding='utf-8').read())
    mutate(d['questions'])
    with open(TARGET, 'w', encoding='utf-8') as f:
        f.write(json.dumps(d, ensure_ascii=False, indent=2))


CASES = []


def case(name):
    def deco(fn):
        CASES.append((name, fn))
        return fn
    return deco


@case('A. 题面 LaTeX 多余右花括号（MathJax 黄条）')
def _a(qs):
    q = qs[0]
    q['question'] = q['question'] + r' 设 $f(x)=\frac{1}{x}}$ 求极限'


@case('B. 选择题 answer 存成字母 A（点选项永远判错）')
def _b(qs):
    for q in qs:
        if q.get('type') == 'choice':
            q['answer'] = 'A'
            return
    raise SystemExit('没找到选择题')


@case('C. id 重复（抽题/错题本串题）')
def _c(qs):
    qs[1]['id'] = qs[0]['id']


@case('D. 填空题 answer 被清空（会被随机自测跳过）')
def _d(qs):
    for q in qs:
        if q.get('type') == 'fill':
            q['answer'] = ''
            return
    raise SystemExit('没找到填空题')


def main():
    shutil.copy(TARGET, BAK)
    before = md5(BUNDLE)
    ok = True
    try:
        for name, fn in CASES:
            inject(fn)
            code, out = run_build()
            after = md5(BUNDLE)
            blocked = (code != 0)
            untouched = (after == before)
            verdict = '拦截' if (blocked and untouched) else '漏网'
            if not (blocked and untouched):
                ok = False
            print('%-50s %s  (exit=%d, bundle未变=%s)' % (name, verdict, code, untouched))
            if not blocked:
                print('    ↑↑↑ 居然没拦住！输出尾部：')
                print('\n'.join('      ' + l for l in out.strip().split('\n')[-6:]))
            shutil.copy(BAK, TARGET)
    finally:
        shutil.copy(BAK, TARGET)
        os.remove(BAK)
        # 恢复 bundle（万一被改过）
        print()
    print()
    print('=' * 70)
    print('撞击测试结果：%s' % ('全部拦截 ✓  坏题出不包' if ok else '有漏网 ✗  闸门无效'))
    print('=' * 70)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
