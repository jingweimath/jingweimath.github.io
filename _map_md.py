# -*- coding: utf-8 -*-
"""多元微分学（82 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '多元微分学'
FILES = ['calculus-multi-diff.json', 'comprehensive.json']

VOCAB = [
    '偏导数与全微分',
    '多元函数极值',
    '隐函数求偏导',
    '方向导数与梯度',
    '多元极限与可微性',
    '条件极值',
    '曲面切平面与法线',
]

A = '偏导数与全微分'        # 具体/抽象复合链式法则、混合偏导、全微分与还原
B = '隐函数求偏导'          # 单方程与方程组确定的隐函数
C = '方向导数与梯度'        # 方向导数、梯度、矩阵形式梯度与 Hessian
D = '多元极限与可微性'      # 二元极限、连续性、偏导存在与可微的关系
E = '多元函数极值'          # 驻点、鞍点、无条件极值、闭区域最值
F = '条件极值'              # 拉格朗日乘数法
G = '曲面切平面与法线'      # 切平面、法向量、空间曲线切线与法平面

TOPIC = {
    'cal-md-001': A, 'cal-md-003': A, 'cal-md-005': A, 'cal-md-006': A,
    'cal-md-011': A, 'cal-md-015': A, 'cal-md-019': A, 'cal-md-021': A,
    'cal-md-023': A, 'cal-md-025': A, 'cal-md-026': A, 'cal-md-027': A,
    'cal-md-028': A, 'cal-md-033': A, 'cal-md-039': A, 'cal-md-042': A,
    'cal-md-103': A, 'cal-md-104': A, 'cal-md-105': A, 'cal-md-108': A,
    'cal-md-109': A, 'cal-md-110': A, 'cal-md-112': A,
    'comp-035': A, 'comp-036': A,

    'cal-md-007': E, 'cal-md-013': E, 'cal-md-024': E, 'cal-md-034': E,
    'cal-md-036': E, 'cal-md-037': E, 'cal-md-046': E, 'cal-md-049': E,
    'cal-md-111': E, 'cal-md-113': E,
    'comp-042': E, 'comp-097': E, 'comp-245': E, 'comp-320': E,

    'cal-md-008': B, 'cal-md-014': B, 'cal-md-018': B, 'cal-md-020': B,
    'cal-md-029': B, 'cal-md-048': B, 'cal-md-106': B, 'cal-md-107': B,
    'comp-044': B, 'comp-301': B,

    'cal-md-004': C, 'cal-md-010': C, 'cal-md-041': C, 'cal-md-044': C,
    'cal-md-119': C, 'cal-md-120': C, 'cal-md-121': C,
    'comp-038': C, 'comp-095': C, 'comp-096': C,

    'cal-md-002': D, 'cal-md-009': D, 'cal-md-017': D, 'cal-md-022': D,
    'cal-md-032': D, 'cal-md-101': D, 'cal-md-102': D,
    'comp-037': D, 'comp-243': D,

    'cal-md-016': F, 'cal-md-030': F, 'cal-md-045': F, 'cal-md-050': F,
    'cal-md-114': F, 'cal-md-115': F,
    'comp-043': F,

    'cal-md-012': G, 'cal-md-031': G, 'cal-md-040': G, 'cal-md-116': G,
    'cal-md-117': G, 'cal-md-118': G,
}

# 点到平面距离是空间解析几何考点，不属于多元微分学
CATFIX = {
    'cal-md-047': ('向量代数与空间解析几何', ''),
}
