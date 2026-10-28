# -*- coding: utf-8 -*-
"""二重积分（75 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '二重积分'
FILES = ['calculus-double-integral.json', 'comprehensive.json']

VOCAB = [
    '直角坐标计算',
    '极坐标计算',
    '交换积分次序',
    '对称性与轮换',
    '分段函数与最值',
    '重积分极限与求导',
    '积分比较',
    '二重积分几何应用',
    '积分方程',
]

A = '直角坐标计算'          # 区域与被积函数都按 x,y 直接定限，含一般曲线围成区域
B = '极坐标计算'            # 圆域/圆环/平移圆/椭圆域，含广义极坐标与泊松积分
C = '交换积分次序'          # 换序才能算的累次积分、直角与极坐标累次积分互化
D = '对称性与轮换'          # 区域对称 + 奇偶性、轮换对称、形心与平均值
E = '分段函数与最值'        # 被积函数含绝对值 / max / min，需按曲线分割区域
F = '重积分极限与求导'      # 重积分中值定理取极限、变限重积分求导、累次积分求导
G = '积分比较'              # 不计算而比较重积分大小
H = '二重积分几何应用'      # 用二重积分求立体体积
I = '积分方程'              # 未知函数藏在二重积分号下，化为 ODE 求解

TOPIC = {
    # --- 直角坐标计算 ---
    'cal-di-015': A, 'cal-di-049': A, 'cal-di-050': A, 'cal-di-057': A,
    'cal-di-113': A, 'comp-039': A,

    # --- 极坐标计算 ---
    'cal-di-012': B, 'cal-di-014': B, 'cal-di-017': B, 'cal-di-020': B,
    'cal-di-031': B, 'cal-di-032': B, 'cal-di-034': B, 'cal-di-044': B,
    'cal-di-046': B, 'cal-di-052': B, 'cal-di-055': B, 'cal-di-061': B,
    'cal-di-064': B, 'cal-di-065': B, 'cal-di-066': B, 'cal-di-069': B,
    'cal-di-075': B, 'cal-di-079': B, 'cal-di-114': B, 'comp-246': B,
    'comp-040': B,

    # --- 交换积分次序 ---
    'cal-di-007': C, 'cal-di-011': C, 'cal-di-016': C, 'cal-di-045': C,
    'cal-di-051': C, 'cal-di-062': C, 'cal-di-063': C, 'cal-di-071': C,
    'cal-di-078': C, 'cal-di-109': C, 'cal-di-110': C, 'cal-di-111': C,
    'comp-041': C, 'comp-231': C, 'comp-239': C, 'comp-248': C,
    'comp-305': C,

    # --- 对称性与轮换 ---
    'cal-di-018': D, 'cal-di-053': D, 'cal-di-060': D, 'cal-di-070': D,
    'cal-di-072': D, 'cal-di-080': D, 'cal-di-101': D, 'cal-di-102': D,
    'cal-di-103': D, 'cal-di-112': D, 'cal-di-115': D,

    # --- 分段函数与最值 ---
    'cal-di-013': E, 'cal-di-048': E, 'cal-di-054': E, 'cal-di-056': E,
    'cal-di-059': E, 'cal-di-073': E, 'comp-247': E, 'comp-321': E,

    # --- 重积分极限与求导 ---
    'cal-di-058': F, 'cal-di-068': F, 'cal-di-076': F, 'cal-di-077': F,
    'cal-di-106': F,

    # --- 积分比较 ---
    'cal-di-074': G, 'cal-di-107': G, 'cal-di-108': G,

    # --- 二重积分几何应用 ---
    'cal-di-021': H, 'cal-di-067': H,

    # --- 积分方程 ---
    'cal-di-104': I, 'cal-di-105': I,
}

CATFIX = {}
