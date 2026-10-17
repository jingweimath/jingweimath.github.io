# -*- coding: utf-8 -*-
import re
import json
import glob
import os

# 获取脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def fix_latex(text):
    if not isinstance(text, str):
        return text
    
    # 1. 极限: lim(x→0) → \lim_{x \to 0}
    text = re.sub(r'lim\(x\\?rightarrow0\)', r'\\lim_{x \\to 0}', text)
    text = re.sub(r'lim\(x\\?rightarrow0\+\)', r'\\lim_{x \\to 0^{+}}', text)
    text = re.sub(r'lim\(x\\?rightarrow0-\)', r'\\lim_{x \\to 0^{-}}', text)
    text = re.sub(r'lim\(x\\?rightarrow\\infty\)', r'\\lim_{x \\to \\infty}', text)
    text = re.sub(r'lim\(x\\?rightarrow-\\infty\)', r'\\lim_{x \\to -\\infty}', text)
    text = re.sub(r'lim\(n\\?rightarrow\\infty\)', r'\\lim_{n \\to \\infty}', text)
    
    # 2. 根号: \sqrt(1+x) → \sqrt{1+x}
    text = re.sub(r'\\sqrt\(([^)]+)\)', r'\\sqrt{\1}', text)
    
    # 3. 三角函数缺少反斜杠
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])tan(?![a-zA-Z])', r'\\tan', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])sin(?![a-zA-Z])', r'\\sin', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])cos(?![a-zA-Z])', r'\\cos', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])arctan(?![a-zA-Z])', r'\\arctan', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])ln(?![a-zA-Z])', r'\\ln', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])lim(?![a-zA-Z])', r'\\lim', text)
    
    # 4. 幂
    text = re.sub(r'x²', r'x^{2}', text)
    text = re.sub(r'x³', r'x^{3}', text)
    
    return text

files = glob.glob('*.json')
fixed_count = 0
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        
        modified = False
        if 'questions' in data:
            for q in data['questions']:
                for field in ['question', 'solution']:
                    if field in q:
                        original = q[field]
                        q[field] = fix_latex(q[field])
                        if original != q[field]:
                            modified = True
                if 'options' in q:
                    for i, opt in enumerate(q['options']):
                        original = opt
                        q['options'][i] = fix_latex(opt)
                        if original != q['options'][i]:
                            modified = True
        
        if modified:
            with open(f, 'w', encoding='utf-8') as fp:
                json.dump(data, fp, ensure_ascii=False, indent=2)
            fixed_count += 1
            print('Fixed: ' + f)
    except Exception as e:
        print('Error ' + f + ': ' + str(e))

print('Total: ' + str(fixed_count) + '/' + str(len(files)) + ' files fixed')
