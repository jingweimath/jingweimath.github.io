# -*- coding: utf-8 -*-
"""
拿改前备份 questions/*.json.bak-20261025dup 与当前文件逐题逐字段核对：
- 题数、id 集合是否一致（不能有增删改）
- 每个字段：没动过的必须完全一致；动过的必须能由「预期规则」解释
- 任何解释不了的差异 → 报警（可能是脚本改错了）

预期规则：
  R1 占位符：`( )_}__}` → `（　）`
  R2 五处手工修复（solution 段落 / 两个 answer）
  R3 删题面里手写的选项段
  R4 删粘连的试卷分节标题
"""
import io
import json
import os
import re
import glob
import collections

ROOT = os.path.dirname(os.path.abspath(__file__))
QDIR = os.path.join(ROOT, 'questions')

BAD_PH = re.compile(r'\(\s*\)_\}__\}')
STRAY1 = re.compile(r'\n\s*\n[-—]{3,}\s*\n+#{1,3}\s*[^\n]*\n*')
STRAY2 = re.compile(r'\n+#{1,3}\s*[^\n]*\s*$')

MANUAL = {
    ('cal-di-069', 'solution'), ('cal-int-028', 'solution'),
    ('cal-limit-011', 'solution'), ('comp-219', 'answer'), ('comp-234', 'answer'),
}

# 只在这些字段上允许存在差异
EDITABLE = {'question', 'solution', 'answer'}


def load(path):
    d = json.loads(io.open(path, encoding='utf-8').read())
    items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
    return {q['id']: q for q in items}


def explain(old, new):
    """返回能解释 old→new 的规则名；解释不了返回 None"""
    if old == new:
        return 'unchanged'
    # R1 占位符
    if BAD_PH.sub('（　）', old) == new:
        return 'R1 占位符'
    # R2 手工
    # R4 标题（带 --- 的）
    t = STRAY1.sub('\n', old)
    t = STRAY2.sub('', t).rstrip() + '\n'
    if t == new:
        return 'R4 删标题'
    # R3 删选项段：new 必须是 old 的前缀（删尾部）
    if old.startswith(new.rstrip('\n')) and len(new) < len(old):
        return 'R3 删选项段'
    # 组合：先删选项段再清标题
    t2 = STRAY1.sub('\n', new)
    t2 = STRAY2.sub('', t2).rstrip() + '\n'
    if old.startswith(t2.rstrip('\n')):
        return 'R3+R4'
    # 组合：占位符 + 删选项段
    if BAD_PH.sub('（　）', old).startswith(new.rstrip('\n')):
        return 'R1+R3'
    return None


def main():
    totals = {'old': 0, 'new': 0}
    stat = collections.Counter()
    alerts = []
    samples = {}
    for cur_path in sorted(glob.glob(os.path.join(QDIR, '*.json'))):
        fn = os.path.basename(cur_path)
        if fn == 'index.json':
            continue
        bak_path = cur_path + '.bak-20261025dup'
        if not os.path.exists(bak_path):
            alerts.append(('缺备份', fn))
            continue
        old = load(bak_path)
        new = load(cur_path)
        totals['old'] += len(old)
        totals['new'] += len(new)
        only_old = set(old) - set(new)
        only_new = set(new) - set(old)
        if only_old:
            alerts.append(('题丢失', fn, sorted(only_old)))
        if only_new:
            alerts.append(('题新增', fn, sorted(only_new)))
        for qid in sorted(set(old) & set(new)):
            o, n = old[qid], new[qid]
            keys = set(o) | set(n)
            for k in sorted(keys):
                ov, nv = o.get(k), n.get(k)
                if ov == nv:
                    continue
                if k not in EDITABLE:
                    alerts.append(('非文本字段被改', qid, k, repr(ov)[:60], repr(nv)[:60]))
                    continue
                why = explain(ov, nv)
                if why is None and (qid, k) in MANUAL:
                    why = 'R2 手工修复'
                if why is None:
                    alerts.append(('★解释不了的差异', qid, k, repr(ov)[:120], repr(nv)[:120]))
                else:
                    stat[why] += 1
                    samples.setdefault(why, []).append((qid, k))
    print('改前题数 %d / 改后题数 %d' % (totals['old'], totals['new']))
    print()
    print('改动分类统计：')
    for k, v in stat.most_common():
        print('  %-14s %d 处   例：%s' % (k, v, samples[k][:2]))
    print()
    if alerts:
        print('!!! 报警 %d 条：' % len(alerts))
        for a in alerts[:40]:
            print('  ', a)
    else:
        print('无无法解释的差异 —— 所有改动都能归类，题数/id 集合一致，非文本字段零改动')


if __name__ == '__main__':
    main()
