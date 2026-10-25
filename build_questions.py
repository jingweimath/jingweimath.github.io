import json, os, datetime

qdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
workspace = os.path.dirname(os.path.abspath(__file__))

# 自动生成版本号：今天日期
VERSION = datetime.datetime.now().strftime('%Y%m%d')

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

lines = [
    '// Auto-generated question bank bundle',
    '// Regenerate: python build_questions.py',
    '// Version: ' + VERSION,
    '',
    'var QUESTION_BANK = {',
]

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
                chapter_data = json.dumps(data, ensure_ascii=False, indent=2)
                # Add comma before all items including first (after 'subjects')
                lines.append(',')
                lines.append('  ' + json.dumps(chapter['id']) + ': ' + chapter_data)

lines.append('};')

output_path = os.path.join(workspace, 'questions-bundle-v2.js')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Bundle generated: {output_path}')
print(f'Version: {VERSION}')
print('Remember to update practice.html to use ?v=' + VERSION)
cnt = len(lines) - 5
print(f'Chapters loaded: {cnt}')
if FILL_TOTAL:
    print(f'考点标签兜底回填: {FILL_TOTAL} 处（cat/topic 缺失，用章节名填充）')
