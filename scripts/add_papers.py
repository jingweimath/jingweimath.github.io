"""给 questions/index.json 的每个章节打上适用科目标记 papers。

考纲口径由老板 2026-10-25 拍板：
  数一 = 高数 9 章 + 线代 4 章 + 概率 5 章
  数二 = 高数 6 章（极限/一元微分/一元积分/多元微分/二重积分/微分方程）+ 线代 4 章（含二次型）
  数三 = 高数 7 章（+无穷级数）+ 线代 4 章 + 概率 5 章
"""
import json, io, os, shutil

ROOT = r'C:/Users/yuwei/WorkBuddy/2026-06-03-task-2'
path = os.path.join(ROOT, 'questions/index.json')

ALL = ['shu1', 'shu2', 'shu3']
NO_SHU2 = ['shu1', 'shu3']   # 数二不考
SHU1_ONLY = ['shu1']         # 只有数一考

PAPERS = {
    'calculus-limit': ALL,
    'calculus-derivative': ALL,
    'calculus-integral': ALL,
    'calculus-diff-eq': ALL,
    'calculus-multi-diff': ALL,
    'calculus-double-integral': ALL,
    'calculus-vector-geometry': SHU1_ONLY,
    'calculus-triple-curve': SHU1_ONLY,
    'calculus-series': NO_SHU2,
    'linalg-matrix': ALL,
    'linalg-vector': ALL,
    'linalg-eigen': ALL,
    'linalg-quadratic': ALL,
    'prob-event': NO_SHU2,
    'prob-distribution': NO_SHU2,
    'prob-multi-var': NO_SHU2,
    'prob-law-large': NO_SHU2,
    'prob-statistics': NO_SHU2,
    'comprehensive': ALL,   # 综合题按内容逐题判断，见 build_questions.py
}

shutil.copy(path, path + '.bak-20261025papers')
idx = json.load(io.open(path, encoding='utf-8'))

n = 0
for sk, sv in idx['subjects'].items():
    for c in sv['chapters']:
        p = PAPERS.get(c['id'])
        if p is None:
            print('!! 未定义章节:', c['id'], c['name'])
            continue
        c['papers'] = p
        n += 1

with io.open(path, 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)

print('已标记章节:', n)
print()
print('%-30s %s' % ('章节', '适用科目'))
for sk, sv in idx['subjects'].items():
    for c in sv['chapters']:
        print('%-30s %s' % (c['name'], '/'.join(c['papers'])))
