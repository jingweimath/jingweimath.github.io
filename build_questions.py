# -*- coding: utf-8 -*-
"""重建 questions-bundle-v2.js。

流程（2026-10-25 加固）：
  1. 构建前跑 lint_questions.py 体检 —— 有 ERROR 直接中止，坏题不上线
  2. 重建 bundle
  3. 构建后自检：题数一致、choice answer 必须是 0-3 整数、id 无重复
  4. **自动把 practice.html 里的 ?v=版本号 改成新版本号**（以前靠人肉记，忘了就走缓存）

用法：
    python build_questions.py                  # 正常：体检不过就不出包
    python build_questions.py --force-lint     # 带着 ERROR 强行出包（应急用，不建议）
    python build_questions.py --no-version     # 不改 practice.html 版本号
"""
import json
import os
import re
import sys
import datetime

workspace = os.path.dirname(os.path.abspath(__file__))
qdir = os.path.join(workspace, 'questions')

sys.path.insert(0, workspace)
import lint_questions  # noqa: E402

FORCE = '--force-lint' in sys.argv
NO_VERSION = '--no-version' in sys.argv

# ---------------------------------------------------------------- 1. 体检
print('=' * 70)
print('步骤 1/4  构建前体检')
print('=' * 70)
errors, warns, src_total = lint_questions.lint()
if errors:
    print('发现 %d 处 ERROR：' % len(errors))
    for fname, qid, fld, why, ctx in errors:
        print('  %s  %s / %s / %s' % (fname, qid, fld, why))
        if ctx:
            print('      ...%s...' % ctx)
    if not FORCE:
        print('\n✗ 构建中止：坏题不能上线。')
        print('  修完再跑，或确需应急出包用：python build_questions.py --force-lint')
        sys.exit(1)
    print('\n⚠ --force-lint 已指定，继续出包（坏题会一并上线）')
else:
    print('✓ 体检通过：%d 道题，0 ERROR' % src_total)
if warns:
    import collections
    agg = collections.Counter(w[3] for w in warns)
    print('  WARN %d 处：' % len(warns) +
          '、'.join('%s %d' % (k, v) for k, v in agg.most_common()))

# ------------------------------------------------------------ 2. 重建 bundle
print()
print('=' * 70)
print('步骤 2/4  重建 bundle')
print('=' * 70)

VERSION_DATE = datetime.datetime.now().strftime('%Y%m%d')

index = json.load(open(os.path.join(qdir, 'index.json'), encoding='utf-8'))


def fill_topic_labels(data, chapter_name):
    """考点标签兜底：cat/topic 缺失时用章节名回填。

    不改源文件——源文件里老板以后补了真考点会自动生效，
    这里只保证打进 bundle 的题 100% 带标签（薄弱诊断/考点错误率依赖它）。
    """
    qs = data.get('questions', []) if isinstance(data, dict) else data
    filled = 0
    for q in qs:
        cat = (q.get('cat') or '').strip()
        topic = (q.get('topic') or '').strip()
        if not cat:
            cat = chapter_name
            q['cat'] = cat
            filled += 1
        if not topic:
            q['topic'] = cat
            filled += 1
    return filled


FILL_TOTAL = 0

# 综合训练按内容判断适用科目（章节级标记是 ALL，这里逐题收紧）
PROB_KW = ['概率', '随机变量', '分布函数', '密度函数', '期望', '方差', '正态分布', '泊松',
           '数理统计', '估计量', '假设检验', '置信区间', '样本均值', '协方差', '相关系数',
           '大数定律', '中心极限定理', '分布律']
ADV_KW = ['三重积分', '曲线积分', '曲面积分', '向量积', '混合积', '数量积', '空间直线',
          '平面方程', '柱面', '锥面', '旋度', '散度', '高斯公式', '斯托克斯']
SERIES_KW = ['幂级数', '收敛半径', '收敛域', '和函数', '傅里叶', '级数']

ALL_PAPERS = ['shu1', 'shu2', 'shu3']


def fill_papers(data, chapter_papers, is_comprehensive=False):
    """给每题打适用科目。综合训练按题面关键词收紧，其余用章节标记。"""
    qs = data.get('questions', []) if isinstance(data, dict) else data
    for q in qs:
        if is_comprehensive:
            text = str(q.get('question', '')) + ' ' + str(q.get('topic', '')) + ' ' + str(q.get('cat', ''))
            if any(k in text for k in ADV_KW):
                q['papers'] = ['shu1']
            elif any(k in text for k in PROB_KW):
                q['papers'] = ['shu1', 'shu3']
            elif any(k in text for k in SERIES_KW):
                q['papers'] = ['shu1', 'shu3']
            else:
                q['papers'] = list(ALL_PAPERS)
        else:
            q['papers'] = list(chapter_papers)


lines = []

subjects_json = json.dumps(index['subjects'], ensure_ascii=False, indent=2)
lines.append('  "subjects": ' + subjects_json)

for subject_key, subject in index['subjects'].items():
    for chapter in subject['chapters']:
        fname = chapter.get('file', '')
        if fname:
            fpath = os.path.join(workspace, fname)
            if os.path.exists(fpath):
                data = json.load(open(fpath, encoding='utf-8'))
                # Normalize: if data is a raw list, wrap it in dict format
                if isinstance(data, list):
                    data = {
                        'subject': subject['name'],
                        'chapter': chapter['name'],
                        'chapterId': chapter['id'],
                        'questions': data
                    }
                FILL_TOTAL += fill_topic_labels(data, chapter['name'])
                fill_papers(data, chapter.get('papers', ALL_PAPERS),
                            is_comprehensive=(chapter['id'] == 'comprehensive'))
                chapter_data = json.dumps(data, ensure_ascii=False, indent=2)
                lines.append(',')
                lines.append('  ' + json.dumps(chapter['id']) + ': ' + chapter_data)

# ------------------------------------------------------------ 3. 构建后自检
print()
print('=' * 70)
print('步骤 3/4  构建后自检')
print('=' * 70)

body = '{\n' + '\n'.join(lines) + '\n}'
try:
    parsed = json.loads(body)
except Exception as e:
    print('✗ bundle 不是合法 JSON：%s' % e)
    sys.exit(1)

bank_total = 0
post_err = []
seen_ids = set()
for key, val in parsed.items():
    if key == 'subjects' or not isinstance(val, dict) or 'questions' not in val:
        continue
    for q in val['questions']:
        bank_total += 1
        qid = q.get('id')
        if qid in seen_ids:
            post_err.append('%s: id 重复' % qid)
        seen_ids.add(qid)
        if q.get('type') == 'choice':
            a = q.get('answer')
            opts = q.get('options') or []
            if not isinstance(a, int) or isinstance(a, bool) or not (0 <= a < len(opts)):
                post_err.append('%s: choice answer=%r 不是合法索引（options %d 项）'
                                % (qid, a, len(opts)))
        if not str(q.get('cat', '')).strip() or not str(q.get('topic', '')).strip():
            post_err.append('%s: 考点标签兜底失败' % qid)
        if not q.get('papers'):
            post_err.append('%s: papers 为空' % qid)

if bank_total != src_total:
    post_err.append('题数不一致：源 %d vs bundle %d' % (src_total, bank_total))

if post_err:
    print('✗ 自检失败 %d 项：' % len(post_err))
    for e in post_err[:20]:
        print('  ' + e)
    sys.exit(1)

print('✓ 题数一致：源 %d = bundle %d' % (src_total, bank_total))
print('✓ choice answer 索引合法、id 无重复、考点标签 100%、papers 齐全')

# ------------------------------------------------- 4. 写文件 + 自动版本号
output_path = os.path.join(workspace, 'questions-bundle-v2.js')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('// Auto-generated question bank bundle\n')
    f.write('// Regenerate: python build_questions.py\n')
    f.write('// Version: %s\n' % VERSION_DATE)
    f.write('var QUESTION_BANK = ')
    f.write(body)
    f.write(';\n')

print()
print('=' * 70)
print('步骤 4/4  同步 practice.html 版本号')
print('=' * 70)

PRACTICE = os.path.join(workspace, 'practice.html')
VERSION = VERSION_DATE
if NO_VERSION:
    print('--no-version 已指定，跳过版本号同步')
else:
    with open(PRACTICE, encoding='utf-8') as f:
        html = f.read()
    m = re.search(r'questions-bundle-v2\.js\?v=([0-9]{8})([a-z]?)', html)
    if not m:
        print('⚠ 没在 practice.html 里找到 questions-bundle-v2.js?v=... ，未改版本号')
    else:
        old_date, old_suffix = m.group(1), m.group(2)
        if old_date == VERSION_DATE:
            # 同一天再次构建：字母后缀递增 a→b→…→z
            nxt = chr(ord(old_suffix) + 1) if old_suffix and old_suffix != 'z' else \
                  ('a' if not old_suffix else 'z')
            VERSION = VERSION_DATE + nxt
        else:
            VERSION = VERSION_DATE
        html = html.replace(m.group(0), 'questions-bundle-v2.js?v=' + VERSION)
        with open(PRACTICE, 'w', encoding='utf-8') as f:
            f.write(html)
        print('✓ practice.html: ?v=%s%s  →  ?v=%s' % (old_date, old_suffix, VERSION))

print()
print('Bundle generated: %s' % output_path)
print('Version: %s' % VERSION)
print('Chapters loaded: %d' % (len(lines) - 1))
if FILL_TOTAL:
    print('考点标签兜底回填: %d 处（cat/topic 缺失，用章节名填充）' % FILL_TOTAL)
print()
print('下一步：scp questions-bundle-v2.js practice.html editor-data.js root@62.234.131.123:/var/www/jingweimath/')
