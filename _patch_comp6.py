# -*- coding: utf-8 -*-
"""在 comprehensive.html 的卡片区首位置插入「经纬研选（五）·多元微积分（数一）」卡片。
- 只在 anchor 处做锚点替换，不整页覆盖
- 保证 NEW 徽章唯一（摘掉其余卡片的 new-badge）
"""
import io, re, sys

SRC = '_live_comp_new.html'
OUT = '_patched_comp.html'
APPLY = '--apply' in sys.argv

with io.open(SRC, encoding='utf-8', newline='') as f:
    html = f.read()

ANCHOR = '  <div class="card-grid">\n'
assert html.count(ANCHOR) == 1, 'card-grid 锚点不唯一：%d' % html.count(ANCHOR)

NEW_CARD = '''  <div class="card-grid">
    <!-- 第五部分：多元微积分（数一） -->
    <div class="comp-card" id="comprehensive-6">
      <span class="new-badge">NEW</span>
      <div class="comp-title">经纬研选（五）·多元微积分（数一）</div>
      <div class="comp-desc">多元微积分精选练习，共 27 题，涵盖多元函数微分学的几何应用（空间曲线的切线与法平面、曲面的切平面与法线）、方向导数与梯度、多元函数极值与条件极值、三重积分（先一后二 / 先二后一、球坐标换序）、第一类与第二类曲线积分、第一类与第二类曲面积分（含高斯公式）等数学一核心考点。</div>
      <div class="comp-tags">
        <span class="comp-tag tag-blue">多元微分</span>
        <span class="comp-tag tag-orange">三重积分</span>
        <span class="comp-tag tag-red">曲线积分</span>
        <span class="comp-tag tag-green">曲面积分</span>
      </div>
      <div class="comp-links">
        <a class="comp-link" href="comprehensive-6-questions.pdf?v=20261027" target="_blank">
          <span class="icon">\U0001F4C4</span>
          <span class="label">题目 PDF（27题）</span>
          <span class="badge badge-q">题目</span>
        </a>
        <a class="comp-link" href="comprehensive-6-solutions.pdf?v=20261027" target="_blank">
          <span class="icon">\U0001F4D6</span>
          <span class="label">AI 参考解析（27题）</span>
          <span class="badge badge-s">AI 解析</span>
        </a>
      </div>
    </div>
'''

out = html.replace(ANCHOR, NEW_CARD, 1)

# 保证 NEW 唯一：新卡插在最前，其余卡片的 new-badge 一律摘掉
head, sep, tail = out.partition('</div>\n\n    <!-- 模拟卷：数学二第七套 -->')
if not sep:
    # 结构可能不同，退化为：除第一处外全部删除
    first = out.find('<span class="new-badge">NEW</span>')
    rest = out[first + len('<span class="new-badge">NEW</span>'):]
    tail_part = rest.replace('      <span class="new-badge">NEW</span>\n', '')
    out = out[:first + len('<span class="new-badge">NEW</span>')] + tail_part
else:
    out = head + '</div>\n' + tail.replace('      <span class="new-badge">NEW</span>\n', '')

n_new = out.count('<span class="new-badge">NEW</span>')
print('NEW 徽章数量（应为 1）:', n_new)
assert n_new == 1, 'NEW 徽章不唯一'

checks = {
    '卡片标题': '经纬研选（五）·多元微积分（数一）',
    '题目 PDF 链接': 'comprehensive-6-questions.pdf?v=20261027',
    '解析 PDF 链接': 'comprehensive-6-solutions.pdf?v=20261027',
    'card-grid 锚点': '<div class="card-grid">',
}
for k, v in checks.items():
    ok = v in out
    print('  %-14s %s' % (k, 'OK' if ok else '缺失'))
    assert ok, k

print('原大小 %d -> 新大小 %d' % (len(html), len(out)))
# 除新增卡片外，其余内容必须与线上一致
diff_only = out.replace(NEW_CARD, ANCHOR).replace(
    '      <span class="new-badge">NEW</span>\n', '') == html.replace(
    '      <span class="new-badge">NEW</span>\n', '')
print('除插卡+摘 NEW 外与线上一致:', diff_only)
assert diff_only

if APPLY:
    with io.open(OUT, 'w', encoding='utf-8', newline='') as f:
        f.write(out)
    print('已写出 %s' % OUT)
else:
    print('dry-run，未写文件（加 --apply 生效）')
