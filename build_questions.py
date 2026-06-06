import json, os

qdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'questions')
workspace = os.path.dirname(os.path.abspath(__file__))

index = json.load(open(os.path.join(qdir, 'index.json'), encoding='utf-8'))

lines = [
    '// Auto-generated question bank bundle',
    '// Regenerate: python build_questions.py',
    '',
    'var QUESTION_BANK = {',
]

subjects_json = json.dumps(index['subjects'], ensure_ascii=False, indent=2)
lines.append('  "subjects": ' + subjects_json + ',')
lines.append('  "data": {}')

for subject_key, subject in index['subjects'].items():
    for chapter in subject['chapters']:
        fname = chapter.get('file', '')
        if fname:
            fpath = os.path.join(workspace, fname)
            if os.path.exists(fpath):
                data = json.load(open(fpath, encoding='utf-8'))
                chapter_data = json.dumps(data, ensure_ascii=False, indent=2)
                lines.append(',')
                lines.append('  ' + json.dumps(chapter['id']) + ': ' + chapter_data)

lines.append('};')

output_path = os.path.join(workspace, 'questions-bundle.js')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Bundle generated: {output_path}')
cnt = len(lines) - 5
print(f'Chapters loaded: {cnt}')
