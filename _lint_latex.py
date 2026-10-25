# -*- coding: utf-8 -*-
"""
LaTeX 花括号平衡检查器：扫全库 question / solution / answer / options。
检查：{} 平衡（考虑 \\{ \\} 转义）、$ 配对、\\left \\right 配对。
"""
import io
import json
import os
import re
import glob
import sys

QDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')


def scan_braces(tex):
    """返回 [(pos, 问题描述)]。考虑 \\{ \\} 转义。"""
    errs = []
    depth = 0
    stack = []
    i = 0
    n = len(tex)
    while i < n:
        c = tex[i]
        if c == '\\':
            if i + 1 < n and tex[i + 1] in '{}':
                i += 2
                continue
            i += 2
            continue
        if c == '{':
            depth += 1
            stack.append(i)
        elif c == '}':
            depth -= 1
            if depth < 0:
                errs.append((i, '多余的右花括号 }'))
                depth = 0
            else:
                stack.pop()
        i += 1
    if depth > 0:
        errs.append((stack[0] if stack else 0, '缺少右花括号，有 %d 个未闭合的 {' % depth))
    return errs


def check_dollars(tex):
    """粗查 $ 配对：跳过 \\$，成对计数。返回错误列表。"""
    errs = []
    cnt = 0
    i = 0
    n = len(tex)
    while i < n:
        if tex[i] == '\\':
            i += 2
            continue
        if tex[i] == '$':
            cnt += 1
        i += 1
    if cnt % 2 != 0:
        errs.append((0, '$ 不配对（共 %d 个）' % cnt))
    return errs


def check_left_right(tex):
    nleft = len(re.findall(r'\\left(?![a-zA-Z])', tex))
    nright = len(re.findall(r'\\right(?![a-zA-Z])', tex))
    if nleft != nright:
        return [(0, '\\left %d 个 vs \\right %d 个' % (nleft, nright))]
    return []


def extract_math(s):
    """把 $...$ / $$...$$ / \\(...\\) / \\[...\\] 里的内容拼出来扫。"""
    parts = []
    i = 0
    n = len(s)
    while i < n:
        if s.startswith('$$', i):
            j = s.find('$$', i + 2)
            if j < 0:
                parts.append(s[i + 2:])
                break
            parts.append(s[i + 2:j])
            i = j + 2
        elif s[i] == '$':
            j = s.find('$', i + 1)
            if j < 0:
                parts.append(s[i + 1:])
                break
            parts.append(s[i + 1:j])
            i = j + 1
        elif s.startswith('\\(', i) or s.startswith('\\[', i):
            close = '\\)' if s[i + 1] == '(' else '\\]'
            j = s.find(close, i + 2)
            if j < 0:
                parts.append(s[i + 2:])
                break
            parts.append(s[i + 2:j])
            i = j + 2
        else:
            i += 1
    return '\n'.join(parts)


FIELDS = ['question', 'solution', 'answer']


def main():
    problems = []
    for f in sorted(glob.glob(os.path.join(QDIR, '*.json'))):
        if os.path.basename(f) == 'index.json':
            continue
        d = json.loads(io.open(f, encoding='utf-8').read())
        items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
        for q in items:
            fields = [(k, q[k]) for k in FIELDS if isinstance(q.get(k), str)]
            for i, o in enumerate(q.get('options') or []):
                fields.append(('options[%d]' % i, o))
            for fld, val in fields:
                tex = extract_math(val)
                for pos, why in scan_braces(tex):
                    ctx = tex[max(0, pos - 40):pos + 40]
                    problems.append((q['id'], fld, why, ctx))
                for pos, why in check_dollars(val):
                    problems.append((q['id'], fld, why, val[:80]))
                for pos, why in check_left_right(tex):
                    problems.append((q['id'], fld, why, val[:80]))
    print('发现 %d 处问题：' % len(problems))
    for pid, fld, why, ctx in problems:
        print('-' * 70)
        print('%s / %s / %s' % (pid, fld, why))
        print('  ...%s...' % ctx.replace('\n', '\\n'))
    return problems


if __name__ == '__main__':
    main()
