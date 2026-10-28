# -*- coding: utf-8 -*-
"""一���微分学（104 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '一元微分学'
FILES = ['calculus-derivative.json', 'comprehensive.json']

VOCAB = [
    '导数定义与可导性',
    '导数计算',
    '中值定理与泰勒公式',
    '单调性与极值',
    '凹凸性与拐点',
    '导数几何应用',
    '零点与方程根',
    '微分与近似',
]

A = '导数定义与可导性'      # 导数定义式凑形、可导性判定、分段/振荡因子
B = '导数计算'              # 隐函数、参数方程、幂指、复合、高阶导
E = '中值定理与泰勒公式'    # 罗尔/拉格朗日/柯西、构造辅助函数、双中值、泰勒估计
M = '单调性与极值'          # 单调性判定、极值与最值、反求参数
T = '凹凸性与拐点'          # 凹凸性判定、拐点、琴生不等式
G = '导数几何应用'          # 切线法线、渐近线、曲率
Z = '零点与方程根'          # 零点定理、根的个数与唯一性
W = '微分与近似'            # 微分近似计算、相关变化率

TOPIC = {
    'cal-der-001': A, 'cal-der-011': A, 'cal-der-017': A, 'cal-der-019': A,
    'cal-der-101': A, 'cal-der-102': A, 'cal-der-103': A, 'cal-der-104': A,
    'comp-001': A, 'comp-002': A, 'comp-005': A, 'comp-006': A, 'comp-008': A,
    'comp-204': A, 'comp-220': A, 'comp-225': A, 'comp-307': A,

    'cal-der-002': B, 'cal-der-003': B, 'cal-der-004': B, 'cal-der-005': B,
    'cal-der-006': B, 'cal-der-007': B, 'cal-der-012': B, 'cal-der-013': B,
    'cal-der-020': B, 'cal-der-021': B, 'cal-der-022': B, 'cal-der-033': B,
    'cal-der-048': B, 'cal-der-105': B, 'cal-der-106': B, 'cal-der-107': B,
    'comp-009': B, 'comp-216': B,

    'cal-der-041': E, 'cal-der-047': E, 'cal-der-050': E, 'cal-der-051': E,
    'cal-der-052': E, 'cal-der-053': E, 'cal-der-054': E, 'cal-der-055': E,
    'cal-der-056': E, 'cal-der-063': E, 'cal-der-108': E, 'cal-der-109': E,
    'cal-der-110': E, 'cal-der-111': E, 'cal-der-112': E, 'cal-der-113': E,
    'cal-der-114': E, 'cal-der-117': E, 'cal-der-118': E, 'cal-der-125': E,
    'comp-012': E, 'comp-201': E, 'comp-206': E, 'comp-211': E, 'comp-226': E,
    'comp-319': E,

    'cal-der-018': M, 'cal-der-025': M, 'cal-der-026': M, 'cal-der-030': M,
    'cal-der-032': M, 'cal-der-035': M, 'cal-der-036': M, 'cal-der-037': M,
    'cal-der-049': M, 'cal-der-121': M, 'cal-der-123': M,
    'comp-020': M, 'comp-214': M, 'comp-223': M,

    'cal-der-027': T, 'cal-der-043': T, 'cal-der-045': T, 'cal-der-057': T,
    'cal-der-058': T, 'cal-der-059': T, 'cal-der-060': T, 'cal-der-061': T,
    'cal-der-062': T, 'cal-der-064': T, 'cal-der-116': T,
    'comp-202': T,

    'cal-der-008': G, 'cal-der-009': G, 'cal-der-014': G, 'cal-der-028': G,
    'cal-der-034': G, 'cal-der-119': G, 'cal-der-122': G,
    'comp-010': G, 'comp-217': G, 'comp-236': G, 'comp-312': G,

    'cal-der-115': Z, 'cal-der-120': Z, 'cal-der-124': Z,
    'comp-213': Z,

    'cal-der-010': W, 'cal-der-023': W,
}

CATFIX = {}
