# -*- coding: utf-8 -*-
"""极限与连续（98 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '极限与连续'
FILES = ['calculus-limit.json', 'comprehensive.json']

VOCAB = [
    '函数极限计算',
    '数列极限',
    '幂指函数极限',
    '和式极限·定积分定义',
    '无穷小阶的比较',
    '极限反推',
    '极限性质辨析',
    '间断点分类',
    '连续性与闭区间性质',
    '变限积分求极限',   # 与一元积分学同名，跨块聚合
]

F = '函数极限计算'      # 一般函数极限：等价无穷小/泰勒/通分/有理化/洛必达
S = '数列极限'          # 递推、夹逼、单调有界、Stolz、阶乘根值
P = '幂指函数极限'      # 1^∞ 型（函数形式）
R = '和式极限·定积分定义'  # n 项和化黎曼和
O = '无穷小阶的比较'
B = '极限反推'          # 由极限反求参数 / 反推函数 / 反推极值
N = '极限性质辨析'      # 保号性、存在性、海涅、左右极限
J = '间断点分类'
C = '连续性与闭区间性质'  # 连续性判定、零点定理、介值定理、有界性
V = '变限积分求极限'

TOPIC = {
    'cal-limit-001': F, 'cal-limit-006': F, 'cal-limit-009': F, 'cal-limit-012': F,
    'cal-limit-013': F, 'cal-limit-014': F, 'cal-limit-015': F, 'cal-limit-018': F,
    'cal-limit-024': F, 'cal-limit-025': F, 'cal-limit-026': F, 'cal-limit-032': F,
    'cal-limit-033': F, 'cal-limit-034': F, 'cal-limit-035': F, 'cal-limit-036': F,
    'cal-limit-037': F, 'cal-limit-038': F, 'cal-limit-046': F, 'cal-limit-109': F,
    'cal-limit-113': F, 'cal-limit-115': F,
    'cal-limit-002': P, 'cal-limit-004': P, 'cal-limit-010': P, 'cal-limit-017': P,
    'cal-limit-028': P, 'cal-limit-105': P,
    'cal-limit-007': S, 'cal-limit-008': S, 'cal-limit-039': S, 'cal-limit-043': S,
    'cal-limit-045': S, 'cal-limit-101': S, 'cal-limit-102': S, 'cal-limit-104': S,
    'cal-limit-106': S, 'cal-limit-107': S, 'cal-limit-108': S, 'cal-limit-114': S,
    'cal-limit-044': R, 'cal-limit-103': R,
    'cal-limit-005': O,
    'cal-limit-042': B, 'cal-limit-111': B, 'cal-limit-112': B,
    'cal-limit-040': N, 'cal-limit-048': N, 'cal-limit-050': N, 'cal-limit-051': N,
    'cal-limit-052': N, 'cal-limit-053': N, 'cal-limit-054': N, 'cal-limit-055': N,
    'cal-limit-066': N,
    'cal-limit-019': J, 'cal-limit-020': J, 'cal-limit-031': J, 'cal-limit-049': J,
    'cal-limit-056': J, 'cal-limit-057': J, 'cal-limit-058': J,
    'cal-limit-011': C, 'cal-limit-059': C, 'cal-limit-060': C, 'cal-limit-061': C,
    'cal-limit-062': C, 'cal-limit-063': C, 'cal-limit-064': C, 'cal-limit-065': C,
    'cal-limit-067': C, 'cal-limit-068': C, 'cal-limit-069': C,
    'cal-limit-003': V, 'cal-limit-110': V,
    'comp-003': F, 'comp-004': F, 'comp-221': F,
    'comp-007': P,
    'comp-063': S, 'comp-064': S, 'comp-068': S, 'comp-069': S, 'comp-070': S,
    'comp-207': S,
    'comp-065': R, 'comp-066': R, 'comp-313': R,
    'comp-205': O, 'comp-304': O,
    'comp-011': B, 'comp-203': B, 'comp-208': B, 'comp-209': B, 'comp-212': B,
    'comp-222': B,
    'comp-218': J, 'comp-219': J,
}

CATFIX = {}
