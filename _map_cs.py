# -*- coding: utf-8 -*-
"""无穷级数（66 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '无穷级数'
FILES = ['calculus-series.json', 'comprehensive.json']

VOCAB = [
    '数项级数敛散性判别',
    '数项级数求和',
    '幂级数收敛域',
    '幂级数和函数',
    '函数展开为幂级数',
    '绝对收敛与条件收敛',
    '傅里叶级数',
]

A = '数项级数敛散性判别'    # 几何/p级数、比较/比值/积分判别、莱布尼茨、必要条件
B = '数项级数求和'          # 裂项、等比、借麦克劳林级数代入求具体和、近似计算
C = '幂级数收敛域'          # 收敛半径、收敛区间端点、阿贝尔定理推论
D = '幂级数和函数'          # 逐项求导/积分求和函数、和函数满足的微分方程、逐项积分算定积分
E = '函数展开为幂级数'      # 麦克劳林展开、间接展开、泰勒系数
F = '绝对收敛与条件收敛'    # 绝对/条件收敛判定与参数范围、级数综合证明
G = '傅里叶级数'            # 傅里叶系数、收敛定理（和函数在间断点的值）

TOPIC = {
    # --- 数项级数敛散性判别 ---
    'cal-cs-001': A, 'cal-cs-002': A, 'cal-cs-003': A, 'cal-cs-005': A,
    'cal-cs-006': A, 'cal-cs-010': A, 'cal-cs-014': A, 'cal-cs-020': A,
    'cal-series-022': A, 'cal-series-024': A, 'cal-series-025': A,
    'cal-series-026': A, 'cal-series-028': A, 'cal-series-031': A,
    'cal-series-032': A, 'cal-series-033': A, 'cal-series-041': A,
    'comp-067': A, 'comp-257': A,

    # --- 数项级数求和 ---
    'cal-cs-004': B, 'cal-cs-011': B, 'cal-cs-017': B,
    'cal-series-023': B, 'cal-series-029': B, 'cal-series-037': B,
    'cal-series-038': B, 'cal-series-039': B, 'cal-series-040': B,
    'cal-series-042': B, 'cal-series-044': B, 'cal-series-047': B,
    'cal-series-049': B, 'cal-series-050': B,

    # --- 幂级数收敛域 ---
    'cal-cs-007': C, 'cal-cs-008': C, 'cal-cs-013': C, 'cal-cs-021': C,
    'cal-series-027': C, 'cal-series-035': C, 'comp-255': C,

    # --- 幂级数和函数 ---
    'cal-cs-012': D, 'cal-cs-018': D, 'cal-series-030': D,
    'cal-series-043': D, 'cal-series-048': D, 'comp-055': D,
    'comp-057': D, 'comp-061': D, 'comp-062': D, 'comp-071': D,
    'comp-073': D, 'comp-074': D,

    # --- 函数展开为幂级数 ---
    'cal-cs-009': E, 'cal-cs-015': E, 'cal-series-034': E,
    'cal-series-036': E, 'cal-series-045': E, 'cal-series-046': E,
    'comp-056': E, 'comp-058': E, 'comp-059': E,

    # --- 绝对收敛与条件收敛 ---
    'comp-229': F, 'comp-254': F, 'comp-256': F,

    # --- 傅里叶级数 ---
    'cal-cs-016': G, 'cal-cs-019': G,
}

CATFIX = {}
