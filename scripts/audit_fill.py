"""审计填空题答案的输入友好度：识别读者难以用纯文本输入的答案。"""
import json, io, re, collections, os

ROOT = r'C:/Users/yuwei/WorkBuddy/2026-06-03-task-2'
idx = json.load(io.open(os.path.join(ROOT, 'questions/index.json'), encoding='utf-8'))

fills = []
for sk, sv in idx['subjects'].items():
    for c in sv['chapters']:
        d = json.load(io.open(os.path.join(ROOT, c['file']), encoding='utf-8'))
        qs = d['questions'] if isinstance(d, dict) else d
        for q in qs:
            if q['type'] == 'fill':
                a = str(q.get('answer') or '').strip()
                if a:
                    fills.append({'id': q['id'], 'a': a, 'ch': c['name'], 'q': q.get('question', '')[:60]})

print('有效填空题:', len(fills))

BS = chr(92)  # 反斜杠
pat = collections.Counter()
hard = []
for it in fills:
    a = it['a']
    flags = []
    if '^' in a or '**' in a or '²' in a or '³' in a:
        flags.append('上标')
    if 'frac' in a or 'dfrac' in a or '/e' in a:
        flags.append('分式')
    if 'sqrt' in a:
        flags.append('根号')
    if 'matrix' in a or 'begin' in a or 'array' in a:
        flags.append('矩阵/环境')
    if '_' in a and '{' in a:
        flags.append('下标')
    if BS in a:
        flags.append('LaTeX命令')
    if len(a) > 14:
        flags.append('过长')
    if 'pi' in a or 'infty' in a:
        flags.append('希腊字母')
    for f in flags:
        pat[f] += 1
    if flags:
        it['flags'] = flags
        hard.append(it)

print()
print('%-14s %s' % ('特征', '题数'))
for k, v in pat.most_common():
    print('%-14s %3d  (%.1f%%)' % (k, v, 100 * v / len(fills)))
print()
print('难输入题合计: %d / %d  (%.1f%%)' % (len(hard), len(fills), 100 * len(hard) / len(fills)))
print()
print('样例 30 条:')
for it in hard[:30]:
    print('  %-16s %-26s %-14s %s' % (it['id'], it['a'][:26], it['ch'], ','.join(it['flags'])))

# 按章节汇总
print()
print('按章节分布（难输入占比）:')
by = collections.Counter()
tot = collections.Counter()
for it in fills:
    tot[it['ch']] += 1
for it in hard:
    by[it['ch']] += 1
for ch in tot:
    print('  %-24s %3d/%3d' % (ch, by[ch], tot[ch]))

# 二次型标准形这类典型
print()
print('含 x^2 / y^2 之类二次型标准形答案的题:')
n = 0
for it in fills:
    if re.search(r'[xyz]\s*\^?\s*2|[xyz]1?\^2', it['a']):
        n += 1
        if n <= 12:
            print('  %-16s %s' % (it['id'], it['a'][:50]))
print('  合计', n)
