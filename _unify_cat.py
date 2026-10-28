# -*- coding: utf-8 -*-
"""把全库 cat 统一为 11 个学科块。

策略：
  1) 非「综合题目」章节：按章节名机械映射（零判断风险）
  2) 「综合题目」章节：含糊的 61 道（极限与微分41/多元微积分17/几何应用3）按 ID 逐题定，
     其余按原有 cat 词映射

用法：先 dry-run，确认无误后 --apply
"""
import json, io, os, sys, glob, shutil, collections
sys.stdout.reconfigure(encoding='utf-8')

ROOT = os.path.dirname(os.path.abspath(__file__))
QD = os.path.join(ROOT, 'questions')
TAG = '20261028cat'

BLOCKS = ['极限与连续', '一元微分学', '一元积分学', '多元微分学', '二重积分',
          '三重·曲线曲面积分', '微分方程', '无穷级数', '向量代数与空间解析几何',
          '线性代数', '概率统计']

# ---- 1) 章节 -> 块（机械映射） ----
CH2BLOCK = {
    '极限与连续': '极限与连续',
    '一元函数微分学': '一元微分学',
    '一元函数积分学': '一元积分学',
    '多元函数微分学': '多元微分学',
    '二重积分': '二重积分',
    '三重积分与曲线曲面积分': '三重·曲线曲面积分',
    '微分方程': '微分方程',
    '无穷级数': '无穷级数',
    '向量代数与空间解析几何': '向量代数与空间解析几何',
    '矩阵与行列式': '线性代数',
    '向量与线性方程组': '线性代数',
    '特征值与特征向量': '线性代数',
    '二次型': '线性代数',
    '随机事件与概率': '概率统计',
    '随机变量与分布': '概率统计',
    '多维随机变量': '概率统计',
    '大数定律与中心极限定理': '概率统计',
    '数理统计': '概率统计',
}

# ---- 2) 综合题：含糊词逐题定（已通读题面/选项/解析） ----
COMP_BY_ID = {}

# 「极限与微分」41 道拆分
for _i in ['001', '002', '005', '006', '008', '009', '010', '020', '201', '202',
           '204', '206', '211', '213', '214', '216', '217', '220', '223', '225', '226']:
    COMP_BY_ID['comp-' + _i] = '一元微分学'
for _i in ['003', '004', '007', '011', '203', '205', '207', '208', '209', '212',
           '218', '219', '221', '222']:
    COMP_BY_ID['comp-' + _i] = '极限与连续'
for _i in ['210', '215', '224', '227', '228']:
    COMP_BY_ID['comp-' + _i] = '一元积分学'          # 变限积分（在分子/分母）与有界性
COMP_BY_ID['comp-229'] = '无穷级数'                  # 证明 Σ[f(1/n)-1] 收敛

# 「多元微积分」17 道拆分
for _i in ['035', '036', '037', '038', '042', '043', '044', '095', '096', '097',
           '243', '245']:
    COMP_BY_ID['comp-' + _i] = '多元微分学'
for _i in ['246', '247', '248']:
    COMP_BY_ID['comp-' + _i] = '二重积分'
for _i in ['244', '249']:
    COMP_BY_ID['comp-' + _i] = '三重·曲线曲面积分'    # 244 曲面积分 / 249 三重积分

# 「几何应用」3 道拆分
COMP_BY_ID['comp-094'] = '向量代数与空间解析几何'      # 二次曲面类型
COMP_BY_ID['comp-312'] = '一元微分学'                # 斜渐近线
COMP_BY_ID['comp-318'] = '一元积分学'                # 面积 + 旋转体体积

# ---- 3) 综合题：其余按原 cat 词映射 ----
COMP_CAT2BLOCK = {
    '微分方程': '微分方程',
    '一元积分学': '一元积分学',
    '曲线曲面积分': '三重·曲线曲面积分',
    '无穷级数': '无穷级数',
    '线性代数': '线性代数',
    '特征值': '线性代数',
    '变限积分': '一元积分学',
    '二次型': '线性代数',
    '数列极限': '极限与连续',
    '二重积分': '二重积分',
    '中值定理': '一元微分学',
    '多元微分': '多元微分学',
    '无穷小阶的比较': '极限与连续',
    '物理应用': '一元积分学',
    '导数定义与可导性': '一元微分学',
    '线性方程组': '线性代数',
    '矩阵的秩': '线性代数',
    '特征值与特征向量': '线性代数',
    '反常积分': '一元积分学',
    '定积分计算': '一元积分学',
}


def read_json(p):
    with io.open(p, encoding='utf-8', newline='') as f:
        raw = f.read()
    crlf = '\r\n' in raw
    return json.loads(raw), crlf


def write_json(p, data, crlf):
    txt = json.dumps(data, ensure_ascii=False, indent=2)
    if crlf:
        txt = txt.replace('\n', '\r\n')
    with io.open(p, 'w', encoding='utf-8', newline='') as f:
        f.write(txt)


def main():
    apply = '--apply' in sys.argv
    files = sorted(glob.glob(os.path.join(QD, '*.json')))
    print('=' * 62)
    print('cat 统一为 11 个学科块   [%s]' % ('APPLY' if apply else 'DRY-RUN'))
    print('=' * 62)

    allstat = collections.Counter()
    unknown = []
    changed = 0
    total = 0

    for p in files:
        data, crlf = read_json(p)
        ch = data.get('chapter') or os.path.basename(p)[:-5]
        qs = data.get('questions', [])
        local = collections.Counter()
        chg = 0
        for q in qs:
            total += 1
            if ch == '综合题目':
                if q['id'] in COMP_BY_ID:
                    nb = COMP_BY_ID[q['id']]
                else:
                    oc = str(q.get('cat', '')).strip()
                    nb = COMP_CAT2BLOCK.get(oc)
                    if nb is None:
                        unknown.append((p, q['id'], oc))
            else:
                nb = CH2BLOCK.get(ch)
                if nb is None:
                    unknown.append((p, q['id'], '章节<%s>无映射' % ch))
            old = str(q.get('cat', '')).strip()
            if old != nb:
                chg += 1
                if apply:
                    q['cat'] = nb
            local[nb] += 1
            allstat[nb] += 1
        if chg:
            changed += chg
            print('  %-34s %3d 题 | 变更 %3d | %s'
                  % (ch[:34], len(qs), chg, dict(local)))
        if apply and chg:
            write_json(p, data, crlf)

    print()
    print('总题数 %d | 变更 %d 道' % (total, changed))
    print('未确定归属:', unknown if unknown else '无')
    print()
    print('=== 归一后各块题数 ===')
    for b in BLOCKS:
        print('  %-22s %4d' % (b, allstat.get(b, 0)))
    other = {k: v for k, v in allstat.items() if k not in BLOCKS}
    print('  非白名单词:', other if other else '无')
    print('  合计:', sum(allstat.values()))
    bad = [k for k in allstat if k not in BLOCKS]
    if bad:
        print('  !! 出现非白名单词，拒绝写盘')
        return 1
    if unknown:
        print('  !! 有未确定归属，拒绝写盘')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
