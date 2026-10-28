# -*- coding: utf-8 -*-
"""线性代数（153 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '线性代数'
FILES = ['linalg-matrix.json', 'linalg-eigen.json', 'linalg-quadratic.json',
         'linalg-vector.json', 'comprehensive.json']

VOCAB = [
    '矩阵运算与行列式',
    '矩阵的秩',
    '向量组的线性相关性',
    '线性方程组',
    '特征值与特征向量',
    '相似对角化与实对称矩阵',
    '二次型标准形与合同',
    '正定二次型',
]

A = '矩阵运算与行列式'        # 乘法、逆、伴随、初等矩阵、矩阵方程、矩阵幂、行列式与代数余子式、正交矩阵
B = '矩阵的秩'                # 秩的计算、秩的不等式、秩与可逆、AB=O 的秩结论
C = '线性方程组'              # 解的判定、基础解系、通解与解的结构、公共解
D = '向量组的线性相关性'      # 线性组合与表出、相关无关判定、极大无关组、等价、内积与正交化
E = '特征值与特征向量'        # 特征多项式、特征值性质、矩阵多项式的特征值、迹与行列式
F = '相似对角化与实对称矩阵'  # 可对角化判定、求 P、实对称与正交矩阵性质
G = '二次型标准形与合同'      # 矩阵表示、正交变换与配方法化标准形、规范形、合同、惯性指数
H = '正定二次型'              # 正定判别（顺序主子式/特征值）、参数范围、正定性质

TOPIC = {
    # ============ 矩阵运算与行列式 (22) ============
    'la-mt-001': A, 'la-mt-002': A, 'la-mt-003': A, 'la-mt-004': A,
    'la-mt-005': A, 'la-mt-006': A, 'la-mt-007': A, 'la-mt-010': A,
    'la-mt-012': A, 'la-mt-013': A, 'la-mt-016': A, 'la-mt-017': A,
    'la-mt-018': A, 'la-mt-021': A, 'la-mt-022': A, 'la-mt-024': A,
    'la-mt-025': A, 'la-mt-026': A, 'la-mt-027': A, 'la-mt-028': A,
    'la-mt-030': A, 'comp-268': A,

    # ============ 矩阵的秩 (15) ============
    'la-mt-008': B, 'la-mt-011': B, 'la-mt-020': B, 'la-mt-029': B,
    'la-vc-007': B, 'la-vc-008': B, 'la-vc-011': B, 'la-vc-013': B,
    'la-vc-014': B, 'la-vc-017': B, 'la-vc-022': B, 'la-vc-026': B,
    'la-vc-028': B, 'comp-267': B, 'comp-310': B,

    # ============ 向量组的线性相关性 (16) ============
    'la-vc-001': D, 'la-vc-002': D, 'la-vc-004': D, 'la-vc-006': D,
    'la-vc-009': D, 'la-vc-012': D, 'la-vc-016': D, 'la-vc-018': D,
    'la-vc-021': D, 'la-vc-023': D, 'la-vc-025': D,
    'comp-088': D, 'comp-090': D, 'comp-093': D, 'comp-269': D,
    'comp-270': D,

    # ============ 线性方程组 (14) ============
    'la-vc-003': C, 'la-vc-005': C, 'la-vc-010': C, 'la-vc-015': C,
    'la-vc-019': C, 'la-vc-020': C, 'la-vc-024': C, 'la-vc-027': C,
    'la-vc-029': C, 'la-vc-030': C,
    'comp-271': C, 'comp-274': C, 'comp-275': C, 'comp-309': C,

    # ============ 特征值与特征向量 (24) ============
    'la-eg-002': E, 'la-eg-004': E, 'la-eg-005': E, 'la-eg-007': E,
    'la-eg-008': E, 'la-eg-015': E, 'la-eg-016': E, 'la-eg-017': E,
    'la-eg-019': E, 'la-eg-024': E, 'la-eg-026': E, 'la-eg-028': E,
    'la-eg-029': E,
    'la-mt-009': E, 'la-mt-014': E, 'la-mt-019': E,
    'comp-076': E, 'comp-077': E, 'comp-080': E, 'comp-081': E,
    'comp-082': E, 'comp-085': E, 'comp-266': E, 'comp-316': E,

    # ============ 相似对角化与实对称矩阵 (21) ============
    'la-eg-009': F, 'la-eg-011': F, 'la-eg-012': F, 'la-eg-013': F,
    'la-eg-018': F, 'la-eg-020': F, 'la-eg-021': F, 'la-eg-022': F,
    'la-eg-023': F, 'la-eg-025': F, 'la-eg-027': F, 'la-eg-030': F,
    'la-mt-023': F,
    'comp-078': F, 'comp-079': F, 'comp-083': F, 'comp-084': F,
    'comp-272': F, 'comp-273': F, 'comp-276': F, 'comp-322': F,

    # ============ 二次型标准形与合同 (28) ============
    'la-qf-001': G, 'la-qf-002': G, 'la-qf-003': G, 'la-qf-004': G,
    'la-qf-006': G, 'la-qf-007': G, 'la-qf-008': G, 'la-qf-009': G,
    'la-qf-010': G, 'la-qf-013': G, 'la-qf-014': G, 'la-qf-015': G,
    'la-qf-016': G, 'la-qf-017': G, 'la-qf-018': G, 'la-qf-019': G,
    'la-qf-020': G, 'la-qf-021': G, 'la-qf-023': G, 'la-qf-024': G,
    'la-qf-026': G, 'la-qf-028': G, 'la-qf-030': G,
    'comp-086': G, 'comp-089': G, 'comp-099': G, 'comp-308': G,
    'comp-315': G,

    # ============ 正定二次型 (13) ============
    'la-qf-005': H, 'la-qf-011': H, 'la-qf-012': H, 'la-qf-022': H,
    'la-qf-025': H, 'la-qf-027': H, 'la-qf-029': H,
    'la-mt-015': H,
    'comp-087': H, 'comp-091': H, 'comp-092': H, 'comp-098': H,
    'comp-100': H,
}

CATFIX = {}
