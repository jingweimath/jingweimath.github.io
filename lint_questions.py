# -*- coding: utf-8 -*-
"""经纬题库体检器：构建前必跑。

用法：
    python lint_questions.py            # 默认：ERROR 会退出码 1，WARN 只提示
    python lint_questions.py --warn-only  # 全部降级为提示（迁移老数据时用）
    python lint_questions.py --quiet    # 只打汇总

被 build_questions.py 自动调用；语法/数据有 ERROR 时构建直接失败，
避免坏题上线（读者看到 MathJax 黄条、点选项永远判错等）。

检查项分两级：
  ERROR = 会直接伤害读者（渲染失败、判分错误、题目失踪）
  WARN  = 不影响使用但应治理（脏格式、缺字段）
"""
import io
import json
import os
import re
import glob
import sys
import collections

QDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')

VALID_TYPES = ('choice', 'fill', 'proof')
VALID_DIFF = ('basic', 'medium', 'hard')  # 2026-10-27 起三档（原 expert 拔高并入 hard 较难）


# ---------------------------------------------------------------- LaTeX 部分
def scan_braces(tex):
    """{} 平衡（考虑 \\{ \\} 转义）。返回 [(pos, why)]。"""
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
                errs.append((i, '多余的右花括号 }（MathJax 会报 "Extra close brace"）'))
                depth = 0
            else:
                stack.pop()
        i += 1
    if depth > 0:
        errs.append((stack[0] if stack else 0,
                     '缺少右花括号，有 %d 个未闭合的 {（MathJax 会报 "Missing open brace"）' % depth))
    return errs


def check_dollars(s):
    errs = []
    cnt = 0
    i = 0
    n = len(s)
    while i < n:
        if s[i] == '\\':
            i += 2
            continue
        if s[i] == '$':
            cnt += 1
        i += 1
    if cnt % 2 != 0:
        errs.append((0, '数学模式 $ 不配对（共 %d 个）' % cnt))
    return errs


def check_left_right(tex):
    nleft = len(re.findall(r'\\left(?![a-zA-Z])', tex))
    nright = len(re.findall(r'\\right(?![a-zA-Z])', tex))
    if nleft != nright:
        return [(0, '\\left %d 个 vs \\right %d 个' % (nleft, nright))]
    return []


def extract_math(s):
    """拼出 $...$ / $$...$$ / \\(...\\) / \\[...\\] 内的内容。"""
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


BAD_PLACEHOLDER = '_}__}'


# ------------------------------------------------------------ 脏格式（WARN）
# 题面里手写选项导致线上显示两遍。两套正则，缺一必漏。
RE_OPT_LINE = re.compile(r'(^|\n)\s*\(?A\s*[.、．）\)]')
RE_OPT_INLINE = re.compile(r'　\s*A\s*[.、．]')
# 切题时把下一节标题粘到上一题尾巴
RE_STRAY_HEAD = re.compile(r'(#{1,3}\s*[一二三四五六七八九十]、|^\s*[二三][、.]?\s*(填空|解答))')

TEXTFIELDS = ['question', 'solution', 'answer']


def iter_questions(qdir=QDIR):
    for f in sorted(glob.glob(os.path.join(qdir, '*.json'))):
        if os.path.basename(f) == 'index.json':
            continue
        d = json.loads(io.open(f, encoding='utf-8').read())
        items = d['questions'] if isinstance(d, dict) and 'questions' in d else d
        for q in items:
            yield os.path.basename(f), q


def lint(qdir=QDIR):
    """返回 (errors, warns)，元素为 (file, qid, field, why, ctx)。"""
    errors, warns = [], []
    seen = {}
    total = 0

    for fname, q in iter_questions(qdir):
        total += 1
        qid = str(q.get('id', '<无id>'))

        # ---- id 唯一
        if qid in seen:
            errors.append((fname, qid, 'id', 'id 重复（另见 %s）' % seen[qid], ''))
        seen[qid] = fname

        # ---- 必备字段
        if not str(q.get('id', '')).strip():
            errors.append((fname, qid, 'id', 'id 为空', ''))
        if q.get('type') not in VALID_TYPES:
            errors.append((fname, qid, 'type', 'type 非法：%r' % q.get('type'), ''))
        if not str(q.get('question', '')).strip():
            errors.append((fname, qid, 'question', '题面为空', ''))
        diff = q.get('difficulty')
        if diff and diff not in VALID_DIFF:
            errors.append((fname, qid, 'difficulty', '难度值非法：%r' % diff, ''))

        # ---- 答案可判性（canJudge 规则的镜像）
        ans = q.get('answer')
        if q.get('type') == 'choice':
            if not isinstance(ans, int) or isinstance(ans, bool) or not (0 <= ans <= 3):
                errors.append((fname, qid, 'answer',
                               '选择题 answer 必须是 0-3 的整数索引，当前 %r（存字母会导致点选项永远判错）' % (ans,),
                               str(ans)[:60]))
            opts = q.get('options') or []
            if len(opts) < 2:
                errors.append((fname, qid, 'options', '选择题 options 不足 2 项：%d' % len(opts), ''))
            elif isinstance(ans, int) and not isinstance(ans, bool) and ans >= len(opts):
                errors.append((fname, qid, 'answer',
                               'answer=%d 超出 options 范围（共 %d 项）' % (ans, len(opts)), ''))
        elif q.get('type') == 'fill':
            if not str(ans or '').strip():
                errors.append((fname, qid, 'answer',
                               '填空题 answer 为空（会被随机自测跳过）', ''))
        else:  # proof：靠自评，只要有解析
            if not str(q.get('solution', '')).strip():
                errors.append((fname, qid, 'solution',
                               '解答题无解析（既不能判分也不能自评）', ''))

        # ---- 逐字段文本检查
        fields = [(k, q[k]) for k in TEXTFIELDS if isinstance(q.get(k), str)]
        for i, o in enumerate(q.get('options') or []):
            fields.append(('options[%d]' % i, o))

        for fld, val in fields:
            if BAD_PLACEHOLDER in val:
                errors.append((fname, qid, fld,
                               '坏占位符 %s（多余的 } 会让整题渲染失败）' % BAD_PLACEHOLDER,
                               val[:80].replace('\n', '\\n')))
            tex = extract_math(val)
            for pos, why in scan_braces(tex):
                errors.append((fname, qid, fld, why,
                               tex[max(0, pos - 40):pos + 40].replace('\n', '\\n')))
            for pos, why in check_dollars(val):
                errors.append((fname, qid, fld, why, val[:80].replace('\n', '\\n')))
            for pos, why in check_left_right(tex):
                errors.append((fname, qid, fld, why, val[:80].replace('\n', '\\n')))
            if RE_STRAY_HEAD.search(val):
                warns.append((fname, qid, fld, '残留试卷分节标题', val[:80].replace('\n', '\\n')))
            if fld == 'question' and q.get('options'):
                if RE_OPT_LINE.search(val) or RE_OPT_INLINE.search(val):
                    errors.append((fname, qid, 'question',
                                   '题面里手写了 A./B./C./D.，options 又存一份 → 线上选项显示两遍',
                                   val[-60:].replace('\n', '\\n')))

        # ---- WARN：字段缺失 / 脏格式
        if not str(q.get('solution', '')).strip() and q.get('type') != 'proof':
            warns.append((fname, qid, 'solution', '无解析', ''))
        if not str(q.get('cat', '')).strip() or not str(q.get('topic', '')).strip():
            warns.append((fname, qid, 'cat/topic', '考点标签缺失（构建时会被章节名兜底）', ''))
        qs = str(q.get('question', ''))
        if qs.startswith('$') and qs.count('$') == 2 and len(qs) > 60:
            warns.append((fname, qid, 'question',
                          '整段题干被塞进 $...$（中文进了数学模式，一个坏字符就整题报废）',
                          qs[:60].replace('\n', '\\n')))

    return errors, warns, total


def main():
    warn_only = '--warn-only' in sys.argv
    quiet = '--quiet' in sys.argv

    errors, warns, total = lint()
    by_why = collections.Counter(e[3].split('（')[0].split('：')[0] for e in errors)

    if not quiet:
        print('=' * 70)
        print('题库体检：扫描 %d 道题' % total)
        print('=' * 70)
        if errors:
            print('\n【ERROR】%d 处 —— 必须修，否则坏题上线：' % len(errors))
            for fname, qid, fld, why, ctx in errors:
                print('  %s  %s / %s / %s' % (fname, qid, fld, why))
                if ctx:
                    print('      ...%s...' % ctx)
        else:
            print('\n【ERROR】0 处 ✓')
        if warns:
            print('\n【WARN】%d 处 —— 不影响使用，建议治理：' % len(warns))
            agg = collections.Counter(w[3] for w in warns)
            for why, c in agg.most_common():
                print('  %-40s %d 处' % (why, c))
        else:
            print('\n【WARN】0 处 ✓')

    if errors and not warn_only:
        print('\n构建中止：请先修掉上述 ERROR。')
        print('（若确需带着问题出包，用 python build_questions.py --force-lint 或 lint_questions.py --warn-only）')
        sys.exit(1)
    return 0 if not errors else 1


if __name__ == '__main__':
    sys.exit(main())
