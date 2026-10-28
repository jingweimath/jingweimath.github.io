# -*- coding: utf-8 -*-
"""三重·曲线曲面积分（87 题）topic 映射。判据：一个 topic = 真题里能单独当一个考点的东西。"""

CATNAME = '三重·曲线曲面积分'
FILES = ['calculus-triple-curve.json', 'comprehensive.json']

VOCAB = [
    '三重积分计算',
    '第一类曲线积分',
    '第二类曲线积分·参数化',
    '格林公式',
    '路径无关与全微分',
    '第一类曲面积分',
    '第二类曲面积分·投影法',
    '高斯公式',
    '斯托克斯公式',
]

A = '三重积分计算'              # 直角/柱坐标/球坐标、先一后二与先二后一、对称性与体积
B = '第一类曲线积分'            # 对弧长：弧长、对称性、质心与转动惯量等物理应用
C = '第二类曲线积分·参数化'     # 对坐标：直接参数化定限计算（含空间曲线）
D = '格林公式'                  # 闭曲线化二重积分，含挖洞法处理奇点、变力做功
E = '路径无关与全微分'          # 保守场判定、改走简单路径、凑原函数、全微分方程
F = '第一类曲面积分'            # 对面积：曲面面积、对称性与形心
G = '第二类曲面积分·投影法'     # 对坐标：分面投影直接计算
H = '高斯公式'                  # 闭曲面化三重积分，含补面法
I = '斯托克斯公式'              # 空间闭曲线化曲面积分

TOPIC = {
    # --- 三重积分计算 ---
    'cal-tc-001': A, 'cal-tc-007': A, 'cal-tc-014': A, 'cal-tc-022': A,
    'cal-tc-023': A, 'cal-tc-024': A, 'cal-tc-026': A, 'cal-tc-028': A,
    'cal-tc-032': A, 'cal-tc-036': A, 'cal-tc-038': A, 'cal-tc-039': A,
    'cal-tc-040': A, 'cal-tc-043': A, 'cal-tc-046': A, 'cal-tc-052': A,
    'cal-tc-054': A, 'cal-tc-055': A, 'cal-tc-056': A, 'cal-tc-057': A,

    # --- 第一类曲线积分 ---
    'cal-tc-005': B, 'cal-tc-010': B, 'cal-tc-025': B, 'cal-tc-037': B,
    'cal-tc-041': B, 'cal-tc-047': B, 'cal-tc-058': B, 'cal-tc-059': B,
    'cal-tc-072': B, 'comp-045': B, 'comp-051': B, 'comp-052': B,

    # --- 第二类曲线积分·参数化 ---
    'cal-tc-003': C, 'cal-tc-004': C, 'cal-tc-015': C, 'cal-tc-053': C,
    'cal-tc-060': C, 'cal-tc-061': C, 'cal-tc-071': C,

    # --- 格林公式 ---
    'cal-tc-002': D, 'cal-tc-008': D, 'cal-tc-011': D, 'cal-tc-013': D,
    'cal-tc-019': D, 'cal-tc-027': D, 'cal-tc-029': D, 'cal-tc-031': D,
    'cal-tc-033': D, 'cal-tc-042': D, 'cal-tc-045': D, 'cal-tc-062': D,
    'cal-tc-063': D, 'cal-tc-066': D, 'comp-046': D, 'comp-047': D,
    'comp-049': D,

    # --- 路径无关与全微分 ---
    'cal-tc-016': E, 'cal-tc-064': E, 'cal-tc-065': E, 'cal-tc-067': E,
    'comp-048': E, 'comp-250': E, 'comp-251': E,

    # --- 第一类曲面积分 ---
    'cal-tc-012': F, 'cal-tc-017': F, 'cal-tc-048': F, 'cal-tc-070': F,
    'cal-tc-073': F,

    # --- 第二类曲面积分·投影法 ---
    'cal-tc-020': G, 'cal-tc-044': G, 'cal-tc-068': G, 'cal-tc-074': G,
    'comp-053': G, 'comp-253': G,

    # --- 高斯公式 ---
    'cal-tc-006': H, 'cal-tc-009': H, 'cal-tc-018': H, 'cal-tc-030': H,
    'cal-tc-035': H, 'cal-tc-069': H, 'comp-050': H, 'comp-244': H,
    'comp-252': H,

    # --- 斯托克斯公式 ---
    'cal-tc-021': I, 'cal-tc-034': I, 'comp-054': I,
}

# comp-249：全平面上的卷积型二重积分 f(x)g(y-x)，不是曲线曲面积分
CATFIX = {
    'comp-249': ('二重积分', '直角坐标计算'),
}
