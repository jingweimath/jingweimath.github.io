# -*- coding: utf-8 -*-
r"""扫描题库里的 LaTeX 转义事故残留（控制字符）。

事故机理：在非 raw 的 Python 字符串里写 \frac / \right 时若只写一个反斜杠，
会被 Python 解释成控制字符：
    \r → CR(0x0D)  \f → FF(0x0C)  \t → TAB(0x09)  \b → BS(0x08)  \a → BEL(0x07)
这些字符进了题面/解析，轻则公式残缺，重则 MathJax 直接报错。

只扫 0x00-0x08、0x0B、0x0C、0x0E-0x1F（0x0A 换行是正常设计，0x0D 单独出现才是事故）。
"""
import io
import json
import glob
import os
import sys
import collections

ROOT = os.path.dirname(os.path.abspath(__file__))
BADCODES = set(list(range(0, 9)) + [11, 12] + list(range(14, 32)))
NAMES = {0x0D: 'CR 回车（\\r 被吃了，多半是 \\right）',
         0x0C: 'FF 换页（\\f 被吃了，多半是 \\frac）',
         0x09: 'TAB（\\t 被吃了，多半是 \\tfrac）',
         0x08: 'BS 退格（\\b）',
         0x07: 'BEL 响铃（\\a，多半是 \\alpha）',
         0x0B: 'VT 垂直制表（\\v）'}


def scan_text(s, where, hits):
    for i, ch in enumerate(s):
        code = ord(ch)
        if code in BADCODES:
            ctx = s[max(0, i - 30):i + 20].replace('\n', ' | ')
            hits.append((where, NAMES.get(code, 'CTRL 0x%02X' % code), repr(ctx)))


def main():
    hits = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'questions', '*.json'))):
        if os.path.basename(f) == 'index.json':
            continue
        # newline='' 很关键：文本模式会把 \r 当换行转换掉，那样 CR 残留根本扫不出来
        d = json.loads(io.open(f, encoding='utf-8', newline='').read())
        items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
        for q in items:
            for fld in ('question', 'solution', 'answer'):
                v = q.get(fld)
                if isinstance(v, str):
                    scan_text(v, '%s / %s / %s' % (os.path.basename(f), q['id'], fld), hits)
            for i, o in enumerate(q.get('options') or []):
                scan_text(o, '%s / %s / options[%d]' % (os.path.basename(f), q['id'], i), hits)

    if not hits:
        print('=' * 70)
        print('控制字符扫描：干净 ✓（无 LaTeX 转义事故残留）')
        print('=' * 70)
        return 0

    print('=' * 70)
    print('发现 %d 处控制字符残留：' % len(hits))
    print('=' * 70)
    agg = collections.Counter(h[1] for h in hits)
    for k, v in agg.most_common():
        print('  %-45s %d 处' % (k, v))
    print()
    for w, why, ctx in hits[:30]:
        print('  %s' % w)
        print('      %s  %s' % (why, ctx))
    return 1


if __name__ == '__main__':
    sys.exit(main())
