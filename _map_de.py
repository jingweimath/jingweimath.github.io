# -*- coding: utf-8 -*-
"""微分方程（91 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '微分方程'
FILES = ['calculus-diff-eq.json', 'comprehensive.json']

VOCAB = [
    '可分离变量与齐次方程',
    '一阶线性方程',
    '伯努利方程',
    '全微分方程',
    '可降阶方程',
    '二阶常系数齐次',
    '二阶常系数非齐次',
    '高阶线性方程与解的结构',
    '欧拉方程',
    '积分方程化为微分方程',
    '微分方程应用与综合',
]

A = '可分离变量与齐次方程'    # 分离变量、u=y/x 代换、类型识别
B = '一阶线性方程'            # 标准形、积分因子、以 y 为自变量反解、常数变易
C = '伯努利方程'
D = '全微分方程'              # 充要条件、凑全微分
E = '可降阶方程'              # y''=f(x)、不显含 y / 不显含 x
F = '二阶常系数齐次'          # 特征方程、初值问题、由解反推方程、有界性
G = '二阶常系数非齐次'        # 特解形式（共振情形）、待定系数、初值问题
H = '高阶线性方程与解的结构'  # 线性无关解、常数变易、由通解/特解反推参数、方程组
I = '欧拉方程'
J = '积分方程化为微分方程'    # 变限积分方程、卷积方程求导转化
K = '微分方程应用与综合'      # 几何/物理建模、与反常积分等的综合

TOPIC = {
    # --- 可分离变量与齐次方程 ---
    'cal-de-001': A, 'cal-de-002': A, 'cal-de-005': A, 'cal-de-012': A,
    'cal-de-019': A, 'cal-de-041': A, 'cal-diffeq-071': A,
    'cal-de-ode-01': A, 'cal-de-ode-02': A, 'cal-de-ode-19': A,
    'comp-025': A, 'comp-029': A, 'comp-030': A,

    # --- 一阶线性方程 ---
    'cal-de-004': B, 'cal-de-011': B, 'cal-de-015': B, 'cal-de-033': B,
    'cal-de-044': B, 'cal-de-050': B, 'cal-diffeq-052': B,
    'cal-diffeq-053': B, 'cal-diffeq-061': B, 'cal-diffeq-062': B,
    'cal-diffeq-065': B, 'cal-diffeq-066': B, 'cal-diffeq-067': B,
    'cal-de-ode-03': B, 'cal-de-ode-04': B, 'cal-de-ode-18': B,
    'comp-026': B, 'comp-033': B, 'comp-258': B,

    # --- 伯努利方程 ---
    'cal-de-047': C, 'cal-diffeq-068': C, 'cal-de-ode-05': C,

    # --- 全微分方程 ---
    'cal-de-010': D, 'cal-de-ode-06': D, 'cal-de-ode-20': D,

    # --- 可降阶方程 ---
    'cal-de-006': E, 'cal-de-049': E, 'cal-diffeq-058': E,
    'cal-diffeq-070': E, 'cal-de-ode-07': E,

    # --- 二阶常系数齐次 ---
    'cal-de-007': F, 'cal-de-009': F, 'cal-de-017': F,
    'cal-de-ode-11': F, 'cal-de-ode-12': F,
    'comp-027': F, 'comp-028': F, 'comp-031': F,

    # --- 二阶常系数非齐次 ---
    'cal-de-013': G, 'cal-de-014': G, 'cal-de-018': G, 'cal-de-020': G,
    'cal-de-034': G, 'cal-de-046': G, 'cal-diffeq-054': G,
    'cal-diffeq-059': G, 'cal-diffeq-060': G,
    'cal-de-ode-08': G, 'cal-de-ode-09': G, 'cal-de-ode-10': G,
    'comp-032': G, 'comp-072': G, 'comp-314': G, 'comp-261': G,

    # --- 高阶线性方程与解的结构 ---
    'cal-diffeq-063': H, 'cal-diffeq-064': H, 'comp-240': H,
    'comp-259': H, 'comp-260': H, 'comp-262': H, 'comp-303': H,

    # --- 欧拉方程 ---
    'cal-de-048': I, 'cal-diffeq-055': I, 'cal-de-ode-21': I,

    # --- 积分方程化为微分方程 ---
    'cal-diffeq-056': J, 'cal-diffeq-069': J,
    'cal-de-ode-13': J, 'cal-de-ode-14': J,

    # --- 微分方程应用与综合 ---
    'cal-de-021': K, 'cal-diffeq-057': K, 'cal-de-ode-15': K,
    'cal-de-ode-16': K, 'cal-de-ode-17': K, 'comp-075': K,
}

# 归错的 4 道：
#  comp-263/264 数列递推极限 -> 极限与连续·数列极限
#  comp-265   弧长下界+等号成立求最值 -> 一元积分学·定积分几何应用
#  comp-071   幂级数解 y'=y -> 无穷级数（topic 等该块定词表时补）
CATFIX = {
    'comp-263': ('极限与连续', '数列极限'),
    'comp-264': ('极限与连续', '数列极限'),
    'comp-265': ('一元积分学', '定积分几何应用'),
    'comp-071': ('无穷级数', None),
}
