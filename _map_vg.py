# -*- coding: utf-8 -*-
"""向量代数与空间解析几何（52 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '向量代数与空间解析几何'
FILES = ['calculus-vector-geometry.json', 'calculus-multi-diff.json', 'comprehensive.json']

VOCAB = [
    '向量运算',
    '平面方程',
    '直线方程与线面关系',
    '距离与夹角',
    '二次曲面与空间曲线',
]

A = '向量运算'              # 模、数量积、向量积、混合积、夹角、投影、平行与共面判定
B = '平面方程'              # 点法式、三点式、截距、平面间位置关系、关于平面的对称点、切平面
C = '直线方程与线面关系'    # 对称式与参数式、方向向量、两直线关系、直线在平面上的投影
D = '距离与夹角'            # 点到平面/直线距离、线面夹角
E = '二次曲面与空间曲线'    # 曲面类型识别、旋转曲面、投影曲线与交线

TOPIC = {
    # --- 向量运算 ---
    'cal-vg-001': A, 'cal-vg-002': A, 'cal-vg-003': A, 'cal-vg-009': A,
    'cal-vg-011': A, 'cal-vg-019': A, 'cal-vg-021': A, 'cal-vg-022': A,
    'cal-vg-023': A, 'cal-vg-024': A, 'cal-vg-026': A, 'cal-vg-027': A,
    'cal-vg-032': A, 'cal-vg-036': A, 'cal-vg-037': A, 'cal-vg-038': A,
    'cal-vg-039': A, 'cal-vg-041': A, 'cal-vg-043': A,

    # --- 平面方程 ---
    'cal-vg-004': B, 'cal-vg-008': B, 'cal-vg-012': B, 'cal-vg-013': B,
    'cal-vg-025': B, 'cal-vg-030': B, 'cal-vg-031': B, 'cal-vg-033': B,
    'cal-vg-034': B, 'cal-vg-044': B, 'cal-vg-046': B, 'cal-vg-047': B,

    # --- 直线方程与线面关系 ---
    'cal-vg-006': C, 'cal-vg-016': C, 'cal-vg-018': C, 'cal-vg-029': C,
    'cal-vg-040': C,

    # --- 距离与夹角 ---
    'cal-vg-010': D, 'cal-vg-017': D, 'cal-vg-028': D, 'cal-vg-035': D,
    'cal-vg-042': D, 'cal-md-047': D,

    # --- 二次曲面与空间曲线 ---
    'cal-vg-005': E, 'cal-vg-007': E, 'cal-vg-014': E, 'cal-vg-015': E,
    'cal-vg-020': E, 'cal-vg-045': E, 'cal-vg-048': E, 'cal-vg-049': E,
    'cal-vg-050': E, 'comp-094': E,
}

CATFIX = {}
