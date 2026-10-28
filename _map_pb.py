# -*- coding: utf-8 -*-
"""概率统计（200 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '概率统计'
FILES = ['prob-distribution.json', 'prob-event.json', 'prob-law-large.json',
         'prob-multi-var.json', 'prob-statistics.json']

VOCAB = [
    '随机事件与概率',
    '一维随机变量及其分布',
    '随机变量的数字特征',
    '多维随机变量及其分布',
    '协方差与相关系数',
    '抽样分布',
    '参数估计',
    '区间估计与假设检验',
    '大数定律与中心极限定理',
]

A = '随机事件与概率'          # 古典概型、几何概型、条件概率、独立性、全概率与贝叶斯
B = '一维随机变量及其分布'    # 分布函数与密度、常见离散/连续分布、随机变量函数的分布
C = '随机变量的数字特征'      # 一维期望、方差、矩、随机变量函数的期望
D = '多维随机变量及其分布'    # 联合与边缘分布、独立性、两个随机变量函数的分布
E = '协方差与相关系数'        # 协方差、相关系数、方差的和差、条件期望
F = '抽样分布'                # 卡方/t/F 分布、样本均值与样本方差的分布
G = '参数估计'                # 矩估计、极大似然、无偏性、有效性、相合性、充分性
H = '区间估计与假设检验'      # 置信区间、枢轴量、两类错误、显著性水平与 p 值
I = '大数定律与中心极限定理'  # 依概率收敛、切比雪夫不等式、大数定律、中心极限定理应用

TOPIC = {
    # ============ 随机事件与概率 (37) ============
    'prob-ev-001': A, 'prob-ev-002': A, 'prob-ev-003': A, 'prob-ev-004': A,
    'prob-ev-005': A, 'prob-ev-006': A, 'prob-ev-007': A, 'prob-ev-008': A,
    'prob-ev-009': A, 'prob-ev-010': A, 'prob-ev-011': A, 'prob-ev-012': A,
    'prob-ev-013': A, 'prob-ev-014': A, 'prob-ev-015': A, 'prob-ev-016': A,
    'prob-ev-017': A, 'prob-ev-018': A, 'prob-ev-019': A, 'prob-ev-020': A,
    'prob-ev-021': A, 'prob-ev-022': A, 'prob-ev-024': A, 'prob-ev-025': A,
    'prob-ev-026': A, 'prob-ev-027': A, 'prob-ev-028': A, 'prob-ev-029': A,
    'prob-ev-030': A, 'prob-ev-031': A, 'prob-ev-032': A, 'prob-ev-035': A,
    'prob-ev-036': A, 'prob-ev-037': A, 'prob-ev-038': A, 'prob-ev-039': A,
    'prob-ev-040': A,

    # ============ 一维随机变量及其分布 (29) ============
    'prob-ev-023': B, 'prob-ev-033': B, 'prob-ev-034': B,
    'prob-dist-001': B, 'prob-dist-002': B, 'prob-dist-004': B,
    'prob-dist-008': B, 'prob-dist-009': B, 'prob-dist-010': B,
    'prob-dist-011': B, 'prob-dist-012': B, 'prob-dist-013': B,
    'prob-dist-014': B, 'prob-dist-015': B, 'prob-dist-017': B,
    'prob-dist-018': B, 'prob-dist-020': B, 'prob-dist-021': B,
    'prob-dist-022': B, 'prob-dist-023': B, 'prob-dist-025': B,
    'prob-dist-027': B, 'prob-dist-028': B, 'prob-dist-029': B,
    'prob-dist-032': B, 'prob-dist-034': B, 'prob-dist-037': B,
    'prob-dist-038': B, 'prob-dist-039': B,

    # ============ 随机变量的数字特征 (14) ============
    'prob-dist-003': C, 'prob-dist-005': C, 'prob-dist-006': C,
    'prob-dist-007': C, 'prob-dist-016': C, 'prob-dist-019': C,
    'prob-dist-024': C, 'prob-dist-026': C, 'prob-dist-030': C,
    'prob-dist-031': C, 'prob-dist-033': C, 'prob-dist-035': C,
    'prob-dist-036': C, 'prob-dist-040': C,

    # ============ 多维随机变量及其分布 (18) ============
    'prob-mv-001': D, 'prob-mv-002': D, 'prob-mv-003': D, 'prob-mv-011': D,
    'prob-mv-012': D, 'prob-mv-015': D, 'prob-mv-016': D, 'prob-mv-018': D,
    'prob-mv-020': D, 'prob-mv-022': D, 'prob-mv-023': D, 'prob-mv-024': D,
    'prob-mv-025': D, 'prob-mv-026': D, 'prob-mv-030': D, 'prob-mv-031': D,
    'prob-mv-035': D, 'prob-mv-038': D,

    # ============ 协方差与相关系数 (18) ============
    'prob-ll-012': E,
    'prob-mv-004': E, 'prob-mv-005': E, 'prob-mv-006': E, 'prob-mv-007': E,
    'prob-mv-008': E, 'prob-mv-009': E, 'prob-mv-010': E, 'prob-mv-014': E,
    'prob-mv-019': E, 'prob-mv-021': E, 'prob-mv-027': E, 'prob-mv-028': E,
    'prob-mv-029': E, 'prob-mv-032': E, 'prob-mv-034': E, 'prob-mv-036': E,
    'prob-mv-039': E,

    # ============ 抽样分布 (10) ============
    'prob-mv-013': F, 'prob-mv-017': F, 'prob-mv-033': F, 'prob-mv-037': F,
    'prob-mv-040': F,
    'prob-stat-001': F, 'prob-stat-003': F, 'prob-stat-004': F,
    'prob-stat-010': F, 'prob-stat-023': F,

    # ============ 参数估计 (22) ============
    'prob-stat-002': G, 'prob-stat-005': G, 'prob-stat-006': G,
    'prob-stat-011': G, 'prob-stat-012': G, 'prob-stat-013': G,
    'prob-stat-014': G, 'prob-stat-015': G, 'prob-stat-018': G,
    'prob-stat-020': G, 'prob-stat-021': G, 'prob-stat-022': G,
    'prob-stat-024': G, 'prob-stat-028': G, 'prob-stat-030': G,
    'prob-stat-033': G, 'prob-stat-034': G, 'prob-stat-035': G,
    'prob-stat-036': G, 'prob-stat-037': G, 'prob-stat-039': G,
    'prob-stat-040': G,

    # ============ 区间估计与假设检验 (13) ============
    'prob-stat-007': H, 'prob-stat-008': H, 'prob-stat-009': H,
    'prob-stat-016': H, 'prob-stat-017': H, 'prob-stat-019': H,
    'prob-stat-025': H, 'prob-stat-026': H, 'prob-stat-027': H,
    'prob-stat-029': H, 'prob-stat-031': H, 'prob-stat-032': H,
    'prob-stat-038': H,

    # ============ 大数定律与中心极限定理 (39) ============
    'prob-ll-001': I, 'prob-ll-002': I, 'prob-ll-003': I, 'prob-ll-004': I,
    'prob-ll-005': I, 'prob-ll-006': I, 'prob-ll-007': I, 'prob-ll-008': I,
    'prob-ll-009': I, 'prob-ll-010': I, 'prob-ll-011': I, 'prob-ll-013': I,
    'prob-ll-014': I, 'prob-ll-015': I, 'prob-ll-016': I, 'prob-ll-017': I,
    'prob-ll-018': I, 'prob-ll-019': I, 'prob-ll-020': I, 'prob-ll-021': I,
    'prob-ll-022': I, 'prob-ll-023': I, 'prob-ll-024': I, 'prob-ll-025': I,
    'prob-ll-026': I, 'prob-ll-027': I, 'prob-ll-028': I, 'prob-ll-029': I,
    'prob-ll-030': I, 'prob-ll-031': I, 'prob-ll-032': I, 'prob-ll-033': I,
    'prob-ll-034': I, 'prob-ll-035': I, 'prob-ll-036': I, 'prob-ll-037': I,
    'prob-ll-038': I, 'prob-ll-039': I, 'prob-ll-040': I,
}

CATFIX = {}
