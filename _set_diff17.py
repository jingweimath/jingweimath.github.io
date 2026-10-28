# -*- coding: utf-8 -*-
"""按老板 10-27 23:00 定档：最后那题(17) 适中，其余 16 道全基础。

只改 diff 字段，不动题干/答案/解析。
用法：先 dry-run（默认），确认后 --apply
"""
import io
import re
import sys
import os

APPLY = '--apply' in sys.argv
TARGET = {'17': 'medium'}   # 老板指定：最后一题适中
DEFAULT = 'basic'           # 其余全部基础

FILES = ['_newint_a.py', '_newint_b.py']

# 匹配形如  dict(n=17, type='proof', diff='hard', 中的 diff 部分
PAT = re.compile(r"(dict\(n=(\d+),[^\n]*?diff=')(\w+)(')")


def process(path):
    src = io.open(path, encoding='utf-8', newline='').read()
    changes = []

    def repl(m):
        old = m.group(3)
        new = TARGET.get(m.group(2), DEFAULT)
        if old == new:
            return m.group(0)
        changes.append((m.group(2), old, new))
        return m.group(1) + new + m.group(4)

    out = PAT.sub(repl, src)
    print('=== %s ===' % path)
    if not changes:
        print('  无改动')
    for n, o, w in changes:
        print('  第 %s 题: %s -> %s' % (n, o, w))
    if APPLY and changes:
        io.open(path, 'w', encoding='utf-8', newline='').write(out)
        print('  已写入')
    return len(changes)


total = sum(process(f) for f in FILES)
print()
print('改动总数 %d 处%s' % (total, '（已应用）' if APPLY else '（dry-run，未写入）'))
