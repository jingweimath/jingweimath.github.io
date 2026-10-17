import re
import json
import glob

# 定义替换规则
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
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])cot(?![a-zA-Z])', r'\\cot', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])sec(?![a-zA-Z])', r'\\sec', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])csc(?![a-zA-Z])', r'\\csc', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])arcsin(?![a-zA-Z])', r'\\arcsin', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])arccos(?![a-zA-Z])', r'\\arccos', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])arctan(?![a-zA-Z])', r'\\arctan', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])ln(?![a-zA-Z])', r'\\ln', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])log(?![a-zA-Z])', r'\\log', text)
    text = re.sub(r'(?<!\\)(?<![a-zA-Z])lim(?![a-zA-Z])', r'\\lim', text)

    # 4. 修复函数调用格式
    text = re.sub(r'\\arctan\(([^)]+)\)', r'\\arctan \1', text)
    text = re.sub(r'\\arcsin\(([^)]+)\)', r'\\arcsin \1', text)
    text = re.sub(r'\\ln\(([^)]+)\)', r'\\ln \1', text)
    text = re.sub(r'\\sin\(([^)]+)\)', r'\\sin \1', text)
    text = re.sub(r'\\cos\(([^)]+)\)', r'\\cos \1', text)
    text = re.sub(r'\\tan\(([^)]+)\)', r'\\tan \1', text)

    # 5. 分数: (1/2) → \frac{1}{2}
    text = re.sub(r'\(([^()]+)\/\([^()]+\)\)', lambda m: r'\\frac{' + m.group(1) + '}{' + m.group(2) + '}', text)

    # 6. 幂: x² → x^{2}, x³ → x^{3}
    text = re.sub(r'x²', r'x^{2}', text)
    text = re.sub(r'x³', r'x^{3}', text)

    return text

# 处理所有JSON文件
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
            print(f"Fixed: {f}")
    except Exception as e:
        print(f"Error {f}: {e}")

print(f"\nTotal: {fixed_count}/{len(files)} files fixed")
