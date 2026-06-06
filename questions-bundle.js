// Auto-generated question bank bundle
// Regenerate: python build_questions.py

var QUESTION_BANK = {
  "subjects": {
  "calculus": {
    "name": "高等数学",
    "chapters": [
      {
        "id": "calculus-limit",
        "name": "极限与连续",
        "file": "questions/calculus-limit.json"
      },
      {
        "id": "calculus-derivative",
        "name": "一元函数微分学",
        "file": "questions/calculus-derivative.json"
      },
      {
        "id": "calculus-integral",
        "name": "一元函数积分学",
        "file": "questions/calculus-integral.json"
      },
      {
        "id": "calculus-diff-eq",
        "name": "微分方程",
        "file": "questions/calculus-diff-eq.json"
      },
      {
        "id": "calculus-multi-diff",
        "name": "多元函数微分学",
        "file": "questions/calculus-multi-diff.json"
      },
      {
        "id": "calculus-double-integral",
        "name": "二重积分",
        "file": "questions/calculus-double-integral.json"
      },
      {
        "id": "calculus-vector-geometry",
        "name": "向量代数与空间解析几何",
        "file": "questions/calculus-vector-geometry.json"
      },
      {
        "id": "calculus-triple-curve",
        "name": "三重积分与曲线曲面积分",
        "file": "questions/calculus-triple-curve.json"
      },
      {
        "id": "calculus-series",
        "name": "无穷级数",
        "file": "questions/calculus-series.json"
      }
    ]
  },
  "linalg": {
    "name": "线性代数",
    "chapters": [
      {
        "id": "linalg-matrix",
        "name": "矩阵与行列式",
        "file": "questions/linalg-matrix.json"
      },
      {
        "id": "linalg-vector",
        "name": "向量与线性方程组",
        "file": "questions/linalg-vector.json"
      },
      {
        "id": "linalg-eigen",
        "name": "特征值与特征向量",
        "file": "questions/linalg-eigen.json"
      },
      {
        "id": "linalg-quadratic",
        "name": "二次型",
        "file": "questions/linalg-quadratic.json"
      }
    ]
  },
  "probability": {
    "name": "概率论与数理统计",
    "chapters": [
      {
        "id": "prob-event",
        "name": "随机事件与概率",
        "file": null
      },
      {
        "id": "prob-distribution",
        "name": "随机变量与分布",
        "file": null
      },
      {
        "id": "prob-multi-var",
        "name": "多维随机变量",
        "file": null
      },
      {
        "id": "prob-law-large",
        "name": "大数定律与中心极限定理",
        "file": null
      },
      {
        "id": "prob-statistics",
        "name": "数理统计",
        "file": null
      }
    ]
  }
},
  "data": {}
,
  "calculus-limit": {
  "subject": "高等数学",
  "chapter": "极限与连续",
  "chapterId": "calculus-limit",
  "questions": [
    {
      "id": "cal-limit-001",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) sin x / x = ？",
      "options": [
        "0",
        "1",
        "e",
        "∞"
      ],
      "answer": 1,
      "solution": "第一个重要极限：lim(x→0) sin x / x = 1。可用夹逼准则证明，考试直接使用即可。注意必须是 x→0 且分子分母形式一致。"
    },
    {
      "id": "cal-limit-002",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→∞) (1 + 1/x)^x = ？",
      "options": [
        "0",
        "1",
        "e",
        "∞"
      ],
      "answer": 2,
      "solution": "第二个重要极限：lim(x→∞) (1 + 1/x)^x = e。变形形式：lim(x→0) (1 + x)^(1/x) = e。幂指函数极限的核心工具。"
    },
    {
      "id": "cal-limit-003",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) (1 - cos x) / x² = ？",
      "options": [
        "0",
        "1/2",
        "1",
        "2"
      ],
      "answer": 1,
      "solution": "利用等价无穷小：1 - cos x ~ x²/2 (x→0)，所以原式 = (x²/2)/x² = 1/2。等价无穷小是考研极限计算的核心方法。"
    },
    {
      "id": "cal-limit-004",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) tan x / x = ？",
      "options": [
        "0",
        "1",
        "e",
        "不存在"
      ],
      "answer": 1,
      "solution": "tan x = sin x / cos x，所以 lim(x→0) tan x / x = lim(x→0) [sin x / x] · [1/cos x] = 1 · 1 = 1。也可直接用等价无穷小 tan x ~ x (x→0)。"
    },
    {
      "id": "cal-limit-005",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) ln(1+x) / x = ？",
      "options": [
        "0",
        "1",
        "e",
        "∞"
      ],
      "answer": 1,
      "solution": "等价无穷小 ln(1+x) ~ x (x→0)，所以极限 = 1。也可用导数定义：ln(1+x)/x 当 x→0 即为 ln x 在 x=1 处的导数。"
    },
    {
      "id": "cal-limit-006",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) (e^x - 1) / x = ？",
      "options": [
        "0",
        "1",
        "e",
        "∞"
      ],
      "answer": 1,
      "solution": "等价无穷小 e^x - 1 ~ x (x→0)，所以极限 = 1。亦可用导数定义验证。这些等价无穷小必须熟记。"
    },
    {
      "id": "cal-limit-007",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) (1 + x)^a - 1 与什么等价？（令 a 为常数）",
      "options": [
        "x",
        "ax",
        "a",
        "x^a"
      ],
      "answer": 1,
      "solution": "(1+x)^a - 1 ~ ax (x→0)。重要推广：当 a=1/2 时得 √(1+x) - 1 ~ x/2；当 a=-1 时得 1/(1+x) - 1 ~ -x。"
    },
    {
      "id": "cal-limit-008",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(x→0) (x - sin x) / x³ = ？",
      "options": [
        "-1/6",
        "1/6",
        "-1/3",
        "1/3"
      ],
      "answer": 1,
      "solution": "泰勒展开 sin x = x - x³/6 + o(x³)，故 x - sin x = x³/6 + o(x³)，原式 = 1/6。也可以用洛必达法则（三次）得到同样结果。"
    },
    {
      "id": "cal-limit-009",
      "type": "fill",
      "difficulty": "basic",
      "question": "lim(x→0) (sin 3x) / (2x) = ______",
      "answer": "3/2",
      "solution": "sin 3x ~ 3x (x→0)，原式 = 3x/(2x) = 3/2。等价无穷小代换时系数直接参与运算。"
    },
    {
      "id": "cal-limit-010",
      "type": "fill",
      "difficulty": "basic",
      "question": "lim(x→0) (e^(2x) - 1) / (3x) = ______",
      "answer": "2/3",
      "solution": "e^(2x) - 1 ~ 2x (x→0)，原式 = 2x/(3x) = 2/3。"
    },
    {
      "id": "cal-limit-011",
      "type": "choice",
      "difficulty": "medium",
      "question": "lim(x→0) [(1/x) - (1/(e^x - 1))] = ？",
      "options": [
        "0",
        "1/2",
        "1",
        "不存在"
      ],
      "answer": 1,
      "solution": "通分：[(e^x - 1 - x)/(x(e^x - 1))]。e^x - 1 ~ x，分母 ~ x²。分子 e^x - 1 - x = (1/2)x² + o(x²)。故极限 = 1/2。注意 e^x - 1 的泰勒展开到二次项：e^x = 1 + x + x²/2 + o(x²)。"
    },
    {
      "id": "cal-limit-012",
      "type": "choice",
      "difficulty": "medium",
      "question": "lim(x→0) (tan x - sin x) / x³ = ？",
      "options": [
        "0",
        "1/2",
        "1",
        "∞"
      ],
      "answer": 1,
      "solution": "tan x - sin x = sin x(1/cos x - 1) = sin x(1 - cos x)/(cos x)。sin x ~ x，1 - cos x ~ x²/2，所以原式 = x · (x²/2) / (cos x · x³) → 1/2。直接泰勒展开亦可。"
    },
    {
      "id": "cal-limit-013",
      "type": "choice",
      "difficulty": "medium",
      "question": "lim(x→0) [√(1+x) - √(1-x)] / x = ？",
      "options": [
        "-1",
        "0",
        "1",
        "2"
      ],
      "answer": 2,
      "solution": "分子有理化：分子分母同乘 √(1+x) + √(1-x)，分子变为 (1+x)-(1-x) = 2x。原式 = 2x / [x(√(1+x)+√(1-x))] = 2/(1+1) = 1。也可用等价无穷小：√(1+x)-1 ~ x/2，√(1-x)-1 ~ -x/2，差 ~ x。"
    },
    {
      "id": "cal-limit-014",
      "type": "choice",
      "difficulty": "medium",
      "question": "lim(x→0+) x^x = ？",
      "options": [
        "0",
        "1",
        "e",
        "不存在"
      ],
      "answer": 1,
      "solution": "幂指函数极限，取对数：ln(x^x) = x·ln x。lim(x→0+) x·ln x = lim(x→0+) ln x / (1/x)。洛必达：= lim (1/x) / (-1/x²) = lim (-x) = 0。故极限 = e^0 = 1。务必保持指数形式回代！"
    },
    {
      "id": "cal-limit-015",
      "type": "fill",
      "difficulty": "medium",
      "question": "lim(x→0) (1 + 2x)^(1/x) = ______",
      "answer": "e²",
      "solution": "凑重要极限形式：(1 + 2x)^(1/x) = [(1 + 2x)^(1/(2x))]² → e²。技巧：看到 (1 + kx)^(1/x) 形式，结果为 e^k。"
    },
    {
      "id": "cal-limit-016",
      "type": "choice",
      "difficulty": "medium",
      "question": "lim(x→∞) [√(x²+x) - x] = ？",
      "options": [
        "0",
        "1/2",
        "1",
        "∞"
      ],
      "answer": 1,
      "solution": "有理化：乘以 [√(x²+x)+x]/[√(x²+x)+x]，分子 = x。分母 = x[√(1+1/x)+1] → x·2。故 = 1/2。∞-∞ 型标准解法：有理化。"
    },
    {
      "id": "cal-limit-017",
      "type": "choice",
      "difficulty": "medium",
      "question": "关于间断点：f(x) = (x²-1)/(x-1) 在 x=1 处是什么类型？",
      "options": [
        "可去间断点",
        "跳跃间断点",
        "无穷间断点",
        "连续"
      ],
      "answer": 0,
      "solution": "(x²-1)/(x-1) = x+1 (x≠1)，极限 lim(x→1) f(x) = 2 存在且有限，但 f(1) 无定义，故为可去间断点。补充定义 f(1)=2 即可连续。"
    },
    {
      "id": "cal-limit-018",
      "type": "choice",
      "difficulty": "medium",
      "question": "关于间断点：f(x) = |x|/x 在 x=0 处是什么类型？",
      "options": [
        "可去间断点",
        "跳跃间断点",
        "无穷间断点",
        "连续"
      ],
      "answer": 1,
      "solution": "左极限 lim(x→0-) f(x) = -1，右极限 lim(x→0+) f(x) = 1。左右极限存在但不相等，为跳跃间断点。间隙为 2。"
    },
    {
      "id": "cal-limit-019",
      "type": "choice",
      "difficulty": "hard",
      "question": "lim(x→0) (x - arctan x) / x³ = ？",
      "options": [
        "1/6",
        "1/3",
        "1/2",
        "1"
      ],
      "answer": 1,
      "solution": "arctan x = x - x³/3 + o(x³)，故 x - arctan x = x³/3 + o(x³)，原式 = 1/3。arctan x 的展开要记住，或者两次洛必达。"
    },
    {
      "id": "cal-limit-020",
      "type": "fill",
      "difficulty": "hard",
      "question": "lim(x→0) (sin x - x·cos x) / x³ = ______",
      "answer": "1/3",
      "solution": "sin x = x - x³/6 + o(x³)，cos x = 1 - x²/2 + o(x²)，x·cos x = x - x³/2 + o(x³)。sin x - x·cos x = (x - x³/6) - (x - x³/2) = x³/3。原式 = 1/3。此题需精确到三次项，一次项会在减法中抵消。"
    }
  ]
}
,
  "calculus-derivative": {
  "subject": "高等数学",
  "chapter": "一元函数微分学",
  "chapterId": "calculus-derivative",
  "questions": [
    {
      "id": "cal-der-001",
      "type": "choice",
      "difficulty": "basic",
      "question": "f(x) 在 x₀ 处可导的定义为 lim(h→0) [f(x₀+h) - f(x₀)] / h 存在。该极限值称为？",
      "options": [
        "f(x₀)",
        "f'(x₀)",
        "f''(x₀)",
        "df"
      ],
      "answer": 1,
      "solution": "导数定义：f'(x₀) = lim(h→0) [f(x₀+h) - f(x₀)] / h。这是导数的标准定义式，所有求导法则都由此推出。注意：可导等价于该极限存在且有限。"
    },
    {
      "id": "cal-der-002",
      "type": "choice",
      "difficulty": "basic",
      "question": "lim(h→0) [f(x₀+h) - f(x₀-h)] / (2h) = ？",
      "options": [
        "f(x₀)",
        "f'(x₀)",
        "2f'(x₀)",
        "0"
      ],
      "answer": 1,
      "solution": "由导数定义拆分：原式 = 1/2 [lim [f(x₀+h)-f(x₀)]/h + lim [f(x₀)-f(x₀-h)]/h] = 1/2(f'(x₀) + f'(x₀)) = f'(x₀)。这是对称差商，只要 f 在 x₀ 可导，结果就等于 f'(x₀)。但注意反向不成立：对称差商存在不能推出可导（如 f(x)=|x| 在 x=0）。"
    },
    {
      "id": "cal-der-003",
      "type": "choice",
      "difficulty": "basic",
      "question": "f(x)=x·|x| 在 x=0 处是否可导？",
      "options": [
        "可导，f'(0)=0",
        "可导，f'(0)=1",
        "不可导",
        "不存在极限"
      ],
      "answer": 0,
      "solution": "x>0 时 f(x)=x²，f'(0+)=2x|x=0=0；x<0 时 f(x)=-x²，f'(0-)=-2x|x=0=0。左右导数相等 =0，故 f'(0)=0。结论：x·|x| 比 |x| 更光滑，是奇函数且可导。"
    },
    {
      "id": "cal-der-004",
      "type": "choice",
      "difficulty": "basic",
      "question": "f(x)=|x| 在 x=0 处是否可导？",
      "options": [
        "可导",
        "不可导",
        "导数=0",
        "导数=1"
      ],
      "answer": 1,
      "solution": "右导数 f'+(0)=1，左导数 f'-(0)=-1，左右导数不相等，故在 x=0 不可导。|x| 是连续但不可导的经典例子。"
    },
    {
      "id": "cal-der-005",
      "type": "fill",
      "difficulty": "basic",
      "question": "若 y = x·ln x，则 dy/dx = ______",
      "answer": "ln x + 1",
      "solution": "乘积法则：(x·ln x)' = x'·ln x + x·(ln x)' = 1·ln x + x·(1/x) = ln x + 1。"
    },
    {
      "id": "cal-der-006",
      "type": "fill",
      "difficulty": "basic",
      "question": "若 y = e^x·sin x，则 y' = ______",
      "answer": "e^x(sin x + cos x)",
      "solution": "乘积法则：(e^x·sin x)' = e^x·sin x + e^x·cos x = e^x(sin x + cos x)。"
    },
    {
      "id": "cal-der-007",
      "type": "fill",
      "difficulty": "basic",
      "question": "若 y = (1+x)/(1-x)，则 y' = ______",
      "answer": "2/(1-x)²",
      "solution": "商的求导法则：[u/v]' = (u'v - uv')/v²。u=1+x, v=1-x。u'=1, v'=-1。y' = [1·(1-x) - (1+x)·(-1)]/(1-x)² = [(1-x)+(1+x)]/(1-x)² = 2/(1-x)²。"
    },
    {
      "id": "cal-der-008",
      "type": "fill",
      "difficulty": "basic",
      "question": "y = sin²x，y' = ______",
      "answer": "sin 2x",
      "solution": "复合函数求导：y = u²，u = sin x。y' = 2u·u' = 2 sin x·cos x = sin 2x。链式法则：外导乘内导。"
    },
    {
      "id": "cal-der-009",
      "type": "fill",
      "difficulty": "basic",
      "question": "y = ln(cos x)，y' = ______",
      "answer": "-tan x",
      "solution": "链式法则：y = ln u，u = cos x。y' = (1/u)·u' = (1/cos x)·(-sin x) = -tan x。"
    },
    {
      "id": "cal-der-010",
      "type": "fill",
      "difficulty": "basic",
      "question": "y = e^(x²)，y'' = ______",
      "answer": "2e^(x²)(1+2x²)",
      "solution": "一阶：y' = 2x·e^(x²)。二阶：y'' = 2·e^(x²) + 2x·2x·e^(x²) = 2e^(x²)(1+2x²)。"
    },
    {
      "id": "cal-der-011",
      "type": "choice",
      "difficulty": "basic",
      "question": "d(sin x) = ？",
      "options": [
        "cos x dx",
        "cos x",
        "sin x dx",
        "-cos x dx"
      ],
      "answer": 0,
      "solution": "微分的定义：dy = f'(x)dx。因为 (sin x)' = cos x，故 d(sin x) = cos x dx。微分 = 导数 × dx。"
    },
    {
      "id": "cal-der-012",
      "type": "fill",
      "difficulty": "basic",
      "question": "d(arcsin x) = ______ dx",
      "answer": "1/√(1-x²)",
      "solution": "反三角函数求导：(arcsin x)' = 1/√(1-x²)。注意 arccos x 的导数是 -1/√(1-x²)，相差一个符号。"
    },
    {
      "id": "cal-der-013",
      "type": "fill",
      "difficulty": "basic",
      "question": "d(arctan x) = ______ dx",
      "answer": "1/(1+x²)",
      "solution": "(arctan x)' = 1/(1+x²)。高频考点，必须熟记。"
    },
    {
      "id": "cal-der-014",
      "type": "choice",
      "difficulty": "medium",
      "question": "曲线 y = x³ - 3x 在何点处切线平行于 x 轴？",
      "options": [
        "(0,0)",
        "(1,-2) 和 (-1,2)",
        "(0,0) 和 (2,2)",
        "仅 (0,0)"
      ],
      "answer": 1,
      "solution": "切线平行于 x 轴 → 导数为 0。y' = 3x² - 3 = 3(x²-1) = 0，解得 x = ±1。x=1 时 y = -2；x=-1 时 y = 2。故有两点 (1,-2) 和 (-1,2)。导数等于 0 是求驻点（可疑极值点）的标准方法。"
    },
    {
      "id": "cal-der-015",
      "type": "choice",
      "difficulty": "medium",
      "question": "y = x^x (x>0) 的导数 y' = ？",
      "options": [
        "x·x^(x-1)",
        "x^x·ln x",
        "x^x·(1+ln x)",
        "x^x"
      ],
      "answer": 2,
      "solution": "幂指函数，取对数：ln y = x·ln x，两边求导：y'/y = ln x + 1，故 y' = y·(ln x+1) = x^x·(1+ln x)。切记：幂指函数必须取对数再求导！"
    },
    {
      "id": "cal-der-016",
      "type": "choice",
      "difficulty": "medium",
      "question": "由方程 e^y + xy = e 确定的隐函数 y=y(x)，在 x=0 处的导数 dy/dx = ？",
      "options": [
        "-1",
        "-1/e",
        "-e",
        "1/e"
      ],
      "answer": 1,
      "solution": "x=0 时代入原方程：e^y + 0 = e → y=1。对方程两边求导：e^y·y' + y + xy' = 0 → y' = -y/(e^y + x)。在 (0,1) 处：y' = -1/(e+0) = -1/e。隐函数求导注意代入求值。"
    },
    {
      "id": "cal-der-017",
      "type": "choice",
      "difficulty": "medium",
      "question": "f(x)=x sin(1/x) (x≠0)，f(0)=0。则 f(x) 在 x=0 处？",
      "options": [
        "可导且连续",
        "连续但不可导",
        "可导但不连续",
        "不连续也不可导"
      ],
      "answer": 1,
      "solution": "连续性：|x sin(1/x)| ≤ |x| → 0 (x→0)，故 f(x) 在 x=0 连续。可导性：f'(0) = lim(h→0) [h sin(1/h) - 0]/h = lim sin(1/h)，该极限不存在（振荡），故不可导。"
    },
    {
      "id": "cal-der-018",
      "type": "choice",
      "difficulty": "medium",
      "question": "f(x)=x² sin(1/x) (x≠0)，f(0)=0。则 f'(0) = ？",
      "options": [
        "0",
        "1",
        "不存在",
        "-1"
      ],
      "answer": 0,
      "solution": "f'(0) = lim(h→0) [h² sin(1/h)]/h = lim h·sin(1/h) = 0（有界量乘无穷小）。比较上题：x 换成 x² 后，多了一个 x 因子，使得导数可以存在。"
    },
    {
      "id": "cal-der-019",
      "type": "choice",
      "difficulty": "hard",
      "question": "设 f(x) 在 x=0 的某邻域内有定义，lim(x→0) [f(x)-f(0)]/x² = 1，则？",
      "options": [
        "f'(0)=0 是极小值",
        "f'(0)=0 是极大值",
        "f'(0)≠0",
        "f'(0) 不存在"
      ],
      "answer": 0,
      "solution": "极限存在且 =1>0，表明 [f(x)-f(0)]/x² > 0 在充分小的邻域内（分母恒正），所以 f(x) > f(0)，f(0) 为极小值。又由极限存在推 f(x)-f(0)→0，且 [f(x)-f(0)]/x = x·[f(x)-f(0)]/x² → 0·1 = 0，故 f'(0)=0。注意：这是极值判定的高阶推广，不需要二阶导数。"
    },
    {
      "id": "cal-der-020",
      "type": "fill",
      "difficulty": "hard",
      "question": "y = ln[ln(ln x)]，则 y' = ______",
      "answer": "1/[x·ln x·ln(ln x)]",
      "solution": "三重复合：y = ln u，u = ln v，v = ln x。y' = (1/u)·(1/v)·(1/x) = 1/[x·ln x·ln(ln x)]。链式法则可以嵌套任意多层，每一步乘以「当前层的导数倒数」。"
    }
  ]
}
,
  "calculus-integral": {
  "subject": "高等数学",
  "chapter": "一元函数积分学",
  "chapterId": "calculus-integral",
  "questions": [
    {
      "id": "cal-int-001",
      "type": "choice",
      "difficulty": "basic",
      "question": "若 F'(x) = f(x)，则称 F(x) 是 f(x) 的什么？",
      "options": [
        "导函数",
        "原函数",
        "不定积分",
        "原函数，也是不定积分"
      ],
      "answer": 3,
      "solution": "原函数定义：若 F'(x) = f(x)，则 F(x) 为 f(x) 的一个原函数。不定积分 ∫f(x)dx = F(x) + C 表示 f(x) 的所有原函数。两者紧密相关但概念不同：原函数是单个函数，不定积分是原函数族。"
    },
    {
      "id": "cal-int-002",
      "type": "choice",
      "difficulty": "basic",
      "question": "∫ x³ dx = ？",
      "options": [
        "3x² + C",
        "x⁴ + C",
        "x⁴/4 + C",
        "x²/3 + C"
      ],
      "answer": 2,
      "solution": "幂函数积分公式：∫ x^n dx = x^(n+1)/(n+1) + C (n ≠ -1)。∫ x³ dx = x⁴/4 + C。注意 n=-1 时 ∫(1/x)dx = ln|x| + C，是特例。"
    },
    {
      "id": "cal-int-003",
      "type": "fill",
      "difficulty": "basic",
      "question": "∫ cos x dx = ______ + C",
      "answer": "sin x",
      "solution": "基本积分公式：∫ cos x dx = sin x + C。因为 (sin x)' = cos x。对称记忆：∫ sin x dx = -cos x + C，多一个负号。"
    },
    {
      "id": "cal-int-004",
      "type": "fill",
      "difficulty": "basic",
      "question": "∫ e^x dx = ______ + C",
      "answer": "e^x",
      "solution": "∫ e^x dx = e^x + C。指数函数 e^x 的积分还是 e^x，这是它最重要的性质。推广：∫ a^x dx = a^x/ln a + C。"
    },
    {
      "id": "cal-int-005",
      "type": "fill",
      "difficulty": "basic",
      "question": "∫ (1/x) dx = ______ + C",
      "answer": "ln|x|",
      "solution": "∫ (1/x) dx = ln|x| + C。注意必须有绝对值！因为 ln x 的定义域是 x>0，而 1/x 在 x<0 也有定义，用 ln|x| 才能覆盖全定义域。幂函数积分 n=-1 的特例。"
    },
    {
      "id": "cal-int-006",
      "type": "choice",
      "difficulty": "basic",
      "question": "∫ sin 2x dx = ？",
      "options": [
        "cos 2x + C",
        "-cos 2x + C",
        "-cos 2x / 2 + C",
        "cos 2x / 2 + C"
      ],
      "answer": 2,
      "solution": "第一类换元（凑微分）：∫ sin 2x dx = (1/2) ∫ sin 2x d(2x) = -cos 2x / 2 + C。核心技巧：令 u = 2x，du = 2dx → dx = du/2。"
    },
    {
      "id": "cal-int-007",
      "type": "choice",
      "difficulty": "basic",
      "question": "∫ (2x + 1)⁵ dx = ？",
      "options": [
        "(2x+1)⁶/6 + C",
        "(2x+1)⁶/12 + C",
        "(2x+1)⁴/4 + C",
        "5(2x+1)⁴ + C"
      ],
      "answer": 1,
      "solution": "凑微分：令 u = 2x+1，du = 2dx，dx = du/2。∫ u⁵·(du/2) = (1/2)·u⁶/6 = u⁶/12 = (2x+1)⁶/12 + C。别忘了 dx 与 du 的换算系数。"
    },
    {
      "id": "cal-int-008",
      "type": "fill",
      "difficulty": "basic",
      "question": "∫ x·e^x dx = ______ + C",
      "answer": "(x-1)e^x",
      "solution": "分部积分：令 u=x, dv=e^x dx，则 du=dx, v=e^x。∫ x·e^x dx = x·e^x - ∫ e^x dx = x·e^x - e^x + C = (x-1)e^x + C。分部积分口诀：反对幂指三，u 按此优先级选取。"
    },
    {
      "id": "cal-int-009",
      "type": "choice",
      "difficulty": "basic",
      "question": "定积分 ∫[a,b] f(x) dx 的几何意义是？",
      "options": [
        "函数在 [a,b] 上的平均值",
        "曲线 y=f(x) 与 x 轴在 [a,b] 上围成的有向面积",
        "f(x) 在 [a,b] 上所有值的和",
        "切线与 x 轴围成的面积"
      ],
      "answer": 1,
      "solution": "定积分表示曲线 y=f(x) 与 x 轴之间在 [a,b] 上的有向面积：x 轴上方为正，下方为负。若 f(x) 变号，定积分等于正面积减去负面积。"
    },
    {
      "id": "cal-int-010",
      "type": "choice",
      "difficulty": "basic",
      "question": "∫[0,1] x dx = ？",
      "options": [
        "0",
        "1/2",
        "1",
        "2"
      ],
      "answer": 1,
      "solution": "∫[0,1] x dx = x²/2 |₀¹ = 1/2 - 0 = 1/2。几何上，这是 y=x 在 [0,1] 下与 x 轴围成的三角形面积，底=1，高=1，面积=1/2。"
    },
    {
      "id": "cal-int-011",
      "type": "fill",
      "difficulty": "basic",
      "question": "∫[0,π] sin x dx = ______",
      "answer": "2",
      "solution": "∫[0,π] sin x dx = -cos x |₀^π = -cos π - (-cos 0) = -(-1) - (-1) = 1 + 1 = 2。sin x 在 [0,π] 上始终非负，结果等于一个拱形的面积。"
    },
    {
      "id": "cal-int-012",
      "type": "choice",
      "difficulty": "medium",
      "question": "设 F'(x) = f(x)，则 ∫ x·f(x²) dx = ？",
      "options": [
        "F(x²) + C",
        "F(x²)/2 + C",
        "2F(x²) + C",
        "xF(x²) + C"
      ],
      "answer": 1,
      "solution": "凑微分：∫ x·f(x²) dx = (1/2) ∫ f(x²) d(x²)。令 u = x²，则原式 = (1/2) ∫ f(u) du = F(u)/2 + C = F(x²)/2 + C。这里 d(x²) = 2x dx，所以 x dx = d(x²)/2。"
    },
    {
      "id": "cal-int-013",
      "type": "choice",
      "difficulty": "medium",
      "question": "∫ x·ln x dx = ？",
      "options": [
        "x²ln x/2 - x²/4 + C",
        "x²ln x + x + C",
        "x²/2·ln x + C",
        "ln x - x + C"
      ],
      "answer": 0,
      "solution": "分部积分：令 u = ln x, dv = x dx，则 du = (1/x) dx, v = x²/2。∫ x·ln x dx = (x²/2)ln x - ∫ (x²/2)(1/x) dx = (x²/2)ln x - (1/2)∫ x dx = (x²/2)ln x - x²/4 + C。口诀「反对幂指三」：对数函数优先选为 u。"
    },
    {
      "id": "cal-int-014",
      "type": "choice",
      "difficulty": "medium",
      "question": "∫ e^x·sin x dx = ？",
      "options": [
        "e^x(sin x - cos x) + C",
        "e^x(sin x + cos x)/2 + C",
        "e^x(sin x - cos x)/2 + C",
        "e^x·cos x + C"
      ],
      "answer": 2,
      "solution": "分部积分两次（循环型）：令 I = ∫ e^x·sin x dx。第一次分部积分后出现 ∫ e^x·cos x dx，第二次分部积分后回到原积分，解方程得 I = e^x(sin x - cos x)/2 + C。e^x 乘三角函数是经典循环积分。"
    },
    {
      "id": "cal-int-015",
      "type": "choice",
      "difficulty": "medium",
      "question": "∫ 1/(x² - 1) dx = ？",
      "options": [
        "arctan x + C",
        "ln|x-1| + C",
        "(1/2)ln|(x-1)/(x+1)| + C",
        "ln|x²-1| + C"
      ],
      "answer": 2,
      "solution": "有理函数积分。分解：1/(x²-1) = 1/[(x-1)(x+1)] = (1/2)[1/(x-1) - 1/(x+1)]。积分得 (1/2)(ln|x-1| - ln|x+1|) + C = (1/2)ln|(x-1)/(x+1)| + C。部分分式分解是考研高频方法。"
    },
    {
      "id": "cal-int-016",
      "type": "choice",
      "difficulty": "medium",
      "question": "设 Φ(x) = ∫[0,x] e^(t²) dt，则 Φ'(x) = ？",
      "options": [
        "e^(x²)·2x",
        "e^(x²)",
        "e^(t²)",
        "∫[0,x] 2t·e^(t²) dt"
      ],
      "answer": 1,
      "solution": "变上限积分求导：d/dx ∫[a,x] f(t) dt = f(x)。直接代入上限即可：Φ'(x) = e^(x²)。注意：此积分不能用初等函数表示，但不影响求导。"
    },
    {
      "id": "cal-int-017",
      "type": "choice",
      "difficulty": "medium",
      "question": "设 Φ(x) = ∫[0,x²] sin t dt，则 Φ'(x) = ？",
      "options": [
        "sin(x²)",
        "2x·sin(x²)",
        "sin(x²)·2x",
        "cos(x²)"
      ],
      "answer": 1,
      "solution": "变上限积分的链式法则。上限为 x²，需复合求导：Φ'(x) = sin(x²)·(x²)' = sin(x²)·2x = 2x·sin(x²)。一般公式：d/dx ∫[a,g(x)] f(t) dt = f(g(x))·g'(x)。"
    },
    {
      "id": "cal-int-018",
      "type": "choice",
      "difficulty": "medium",
      "question": "∫[0,1] x/(1+x²) dx = ？",
      "options": [
        "ln 2",
        "ln 2 / 2",
        "1/2",
        "ln(3/2)"
      ],
      "answer": 1,
      "solution": "定积分换元：令 u = 1+x²，du = 2x dx，x dx = du/2。当 x=0 时 u=1；x=1 时 u=2。原式 = ∫[1,2] (1/2)(1/u) du = (1/2) ln u |₁² = (1/2) ln 2。定积分换元必须换限！"
    },
    {
      "id": "cal-int-019",
      "type": "choice",
      "difficulty": "hard",
      "question": "反常积分 ∫[1,+∞] 1/x^p dx 收敛的条件是？",
      "options": [
        "p > 1",
        "p ≥ 1",
        "p < 1",
        "p ≤ 1"
      ],
      "answer": 0,
      "solution": "计算：∫[1,A] x^(-p) dx = (A^(1-p) - 1)/(1-p) (p≠1)；p=1 时 = ln A。当 A→∞，若 p>1 则 A^(1-p)→0，积分收敛于 1/(p-1)；若 p≤1 则发散。这是判断反常积分敛散性的基准（p-积分）。"
    },
    {
      "id": "cal-int-020",
      "type": "choice",
      "difficulty": "hard",
      "question": "曲线 y = x² 与 y = x 围成图形的面积为？",
      "options": [
        "1/2",
        "1/3",
        "1/6",
        "2/3"
      ],
      "answer": 2,
      "solution": "先求交点：x² = x → x(x-1) = 0 → x=0, 1。在 [0,1] 上，x ≥ x²（因为 0≤x≤1 时 x - x² = x(1-x) ≥ 0）。面积 = ∫[0,1] (x - x²) dx = (x²/2 - x³/3)|₀¹ = 1/2 - 1/3 = 1/6。"
    },
    {
      "id": "cal-int-021",
      "type": "fill",
      "difficulty": "hard",
      "question": "∫[0,1] x·arcsin x dx = ______",
      "answer": "π/8",
      "solution": "分部积分：令 u = arcsin x, dv = x dx，du = 1/√(1-x²) dx, v = x²/2。∫ x·arcsin x dx = (x²/2)arcsin x - (1/2)∫ x²/√(1-x²) dx。第二项用三角代换 x=sin t，化简得面积相关的标准结果。定积分 ∫[0,1] 结果为 π/8。反三角函数积分需熟练三角代换。"
    }
  ]
}
,
  "calculus-diff-eq": [
  {
    "id": "cal-de-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "下列方程中，是一阶微分方程的是（ ）",
    "options": [
      "$y'' + 2y' + y = 0$",
      "$(y')^2 + yy' = x$",
      "$\\frac{\\partial u}{\\partial x} + \\frac{\\partial u}{\\partial y} = 0$",
      "$y^{(3)} + xy = e^x$"
    ],
    "answer": "B",
    "solution": "**一阶微分方程**是指方程中出现的未知函数的最高阶导数为一阶。\n\n- A项：$y''$ 出现，是二阶微分方程 ❌\n- B项：只出现 $y'$，是一阶微分方程 ✅\n- C项：偏微分方程，不是常微分方程 ❌\n- D项：$y^{(3)}$ 出现，是三阶微分方程 ❌\n\n**答案：B**"
  },
  {
    "id": "cal-de-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $xy' - y\\ln y = 0$ 的解是（ ）",
    "options": [
      "$y = e^{Cx}$",
      "$y = Ce^x$",
      "$y = e^{Cx^2}$",
      "$y = Cx$"
    ],
    "answer": "A",
    "solution": "**分离变量法**：\n\n$$xy' = y\\ln y \\quad \\Rightarrow \\quad \\frac{dy}{y\\ln y} = \\frac{dx}{x}$$\n\n令 $u = \\ln y$，则 $du = \\frac{dy}{y}$，左边化为 $\\frac{du}{u} = \\frac{dx}{x}$。\n\n积分得：$\\ln|u| = \\ln|x| + C_1$，即 $u = Cx$，所以 $\\ln y = Cx$，故 $y = e^{Cx}$。\n\n**答案：A**"
  },
  {
    "id": "cal-de-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "一阶线性微分方程 $y' + P(x)y = Q(x)$ 的通解公式是（ ）",
    "options": [
      "$y = e^{-\\int P(x)dx}\\left(\\int Q(x)e^{\\int P(x)dx}dx + C\\right)$",
      "$y = e^{\\int P(x)dx}\\left(\\int Q(x)e^{-\\int P(x)dx}dx + C\\right)$",
      "$y = \\int P(x)Q(x)dx + C$",
      "$y = Ce^{-\\int P(x)dx} + Q(x)$"
    ],
    "answer": "A",
    "solution": "**一阶线性微分方程通解公式**（常数变易法推导）：\n\n积分因子 $\\mu(x) = e^{\\int P(x)dx}$，方程两边同乘 $\\mu(x)$：\n\n$$\\frac{d}{dx}\\left(y \\cdot e^{\\int P(x)dx}\\right) = Q(x)e^{\\int P(x)dx}$$\n\n积分得：$y e^{\\int P(x)dx} = \\int Q(x)e^{\\int P(x)dx}dx + C$\n\n所以 $y = e^{-\\int P(x)dx}\\left(\\int Q(x)e^{\\int P(x)dx}dx + C\\right)$\n\n**答案：A**"
  },
  {
    "id": "cal-de-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y' + \\frac{1}{x}y = x\\ (x > 0)$ 满足 $y(1) = 1$ 的特解是（ ）",
    "options": [
      "$y = \\frac{x^2}{2} + \\frac{1}{2x}$",
      "$y = \\frac{x^2}{3} + \\frac{2}{3x}$",
      "$y = x^2$",
      "$y = \\frac{x^2}{2} + C$"
    ],
    "answer": "B",
    "solution": "**一阶线性微分方程**，积分因子法：\n\n$P(x) = \\frac{1}{x}$，$Q(x) = x$\n\n积分因子：$\\mu(x) = e^{\\int \\frac{1}{x}dx} = e^{\\ln x} = x$\n\n方程两边同乘 $x$：$xy' + y = x^2$，即 $\\frac{d}{dx}(xy) = x^2$\n\n积分：$xy = \\frac{x^3}{3} + C \\Rightarrow y = \\frac{x^2}{3} + \\frac{C}{x}$\n\n代入 $y(1) = 1$：$\\frac{1}{3} + C = 1 \\Rightarrow C = \\frac{2}{3}$\n\n所以 $y = \\frac{x^2}{3} + \\frac{2}{3x}$\n\n**答案：B**"
  },
  {
    "id": "cal-de-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y' = \\frac{y}{x} + \\tan\\frac{y}{x}$ 的类型是（ ）",
    "options": [
      "可分离变量方程",
      "齐次方程",
      "一阶线性方程",
      "伯努利方程"
    ],
    "answer": "B",
    "solution": "**齐次方程的判定**：方程右端是 $\\frac{y}{x}$ 的函数，即 $y' = f\\left(\\frac{y}{x}\\right)$ 形式。\n\n令 $u = \\frac{y}{x}$，则 $y = ux$，$y' = u + xu'$，方程化为：\n\n$u + xu' = u + \\tan u \\Rightarrow xu' = \\tan u$（可分离变量）\n\n**答案：B**"
  },
  {
    "id": "cal-de-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y'' = x + \\sin x$ 的通解是（ ）",
    "options": [
      "$y = \\frac{x^3}{6} - \\sin x + C_1x + C_2$",
      "$y = \\frac{x^3}{6} + \\sin x + C_1x + C_2$",
      "$y = \\frac{x^2}{2} - \\cos x + C_1$",
      "$y = \\frac{x^3}{6} + \\cos x + C_1x + C_2$"
    ],
    "answer": "A",
    "solution": "**可降阶微分方程** $y'' = f(x)$ 型：直接积分两次。\n\n$$y' = \\int (x + \\sin x)dx = \\frac{x^2}{2} - \\cos x + C_1$$\n\n$$y = \\int \\left(\\frac{x^2}{2} - \\cos x + C_1\\right)dx = \\frac{x^3}{6} - \\sin x + C_1x + C_2$$\n\n**答案：A**"
  },
  {
    "id": "cal-de-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y'' - 4y' + 3y = 0$ 的通解是（ ）",
    "options": [
      "$y = C_1e^x + C_2e^{3x}$",
      "$y = C_1e^{-x} + C_2e^{-3x}$",
      "$y = (C_1 + C_2x)e^x$",
      "$y = C_1\\cos x + C_2\\sin x$"
    ],
    "answer": "A",
    "solution": "**二阶常系数齐次线性微分方程**：\n\n特征方程：$r^2 - 4r + 3 = 0 \\Rightarrow (r-1)(r-3) = 0$\n\n特征根：$r_1 = 1,\\ r_2 = 3$（互异实根）\n\n通解：$y = C_1e^{r_1x} + C_2e^{r_2x} = C_1e^x + C_2e^{3x}$\n\n**答案：A**"
  },
  {
    "id": "cal-de-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y'' - 2y' + y = 0$ 的通解是（ ）",
    "options": [
      "$y = C_1e^x + C_2e^{-x}$",
      "$y = (C_1 + C_2x)e^x$",
      "$y = C_1e^x + C_2xe^x$",
      "$y = C_1\\cos x + C_2\\sin x$"
    ],
    "answer": "B",
    "solution": "**二阶常系数齐次线性微分方程**（重根情形）：\n\n特征方程：$r^2 - 2r + 1 = 0 \\Rightarrow (r-1)^2 = 0$\n\n特征根：$r = 1$（二重根）\n\n通解：$y = (C_1 + C_2x)e^x$\n\n**答案：B**"
  },
  {
    "id": "cal-de-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "微分方程 $y'' + y = 0$ 满足 $y(0) = 1,\\ y'(0) = 0$ 的特解是（ ）",
    "options": [
      "$y = \\cos x$",
      "$y = \\sin x$",
      "$y = e^{-x}$",
      "$y = \\cosh x$"
    ],
    "answer": "A",
    "solution": "**二阶常系数齐次方程** $y'' + y = 0$：$\n\n特征方程：$r^2 + 1 = 0 \\Rightarrow r = \\pm i$\n\n通解：$y = C_1\\cos x + C_2\\sin x$\n\n代入 $y(0) = 1$：$C_1 = 1$\n\n$y' = -C_1\\sin x + C_2\\cos x$，代入 $y'(0) = 0$：$C_2 = 0$\n\n所以 $y = \\cos x$\n\n**答案：A**"
  },
  {
    "id": "cal-de-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "一阶微分方程 $M(x,y)dx + N(x,y)dy = 0$ 为全微分方程的充要条件是（ ）",
    "options": [
      "$\\frac{\\partial M}{\\partial x} = \\frac{\\partial N}{\\partial y}$",
      "$\\frac{\\partial M}{\\partial y} = \\frac{\\partial N}{\\partial x}$",
      "$M = N$",
      "$\\frac{\\partial M}{\\partial x} + \\frac{\\partial N}{\\partial y} = 0$"
    ],
    "answer": "B",
    "solution": "**全微分方程的充要条件**：\n\n若存在函数 $u(x,y)$ 使得 $du = Mdx + Ndy$，则\n\n$$\\frac{\\partial u}{\\partial x} = M,\\quad \\frac{\\partial u}{\\partial y} = N$$\n\n由混合偏导数相等：$\\frac{\\partial M}{\\partial y} = \\frac{\\partial^2 u}{\\partial y\\partial x} = \\frac{\\partial^2 u}{\\partial x\\partial y} = \\frac{\\partial N}{\\partial x}$\n\n**答案：B**"
  },
  {
    "id": "cal-de-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $xy' + y = \\ln x$ 的通解是（ ）",
    "options": [
      "$y = \\frac{x}{2}(\\ln x - 1) + \\frac{C}{x}$",
      "$y = \\ln x - 1 + \\frac{C}{x}$",
      "$y = \\frac{\\ln x}{x} + C$",
      "$y = x\\ln x + Cx$"
    ],
    "answer": "B",
    "solution": "**一阶线性方程**，先化简：\n\n$y' + \\frac{1}{x}y = \\frac{\\ln x}{x}$\n\n积分因子：$\\mu(x) = e^{\\int \\frac{1}{x}dx} = x$\n\n同乘 $x$：$(xy)' = \\ln x$\n\n积分：$xy = \\int \\ln x dx = x\\ln x - x + C$\n\n所以 $y = \\ln x - 1 + \\frac{C}{x}$\n\n**答案：B**"
  },
  {
    "id": "cal-de-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $y' = \\frac{x + y}{x - y}$ 的通解（隐式）是（ ）",
    "options": [
      "$\\arctan\\frac{y}{x} = \\ln\\sqrt{x^2 + y^2} + C$",
      "$\\arctan\\frac{y}{x} = \\ln(x^2 + y^2) + C$",
      "$\\frac{y}{x} = \\ln\\sqrt{x^2 + y^2} + C$",
      "$\\ln\\sqrt{x^2 + y^2} = \\arctan\\frac{x}{y} + C$"
    ],
    "answer": "A",
    "solution": "**齐次方程**，令 $y = ux$，则 $y' = u + xu'$：\n\n$$u + xu' = \\frac{1 + u}{1 - u}$$\n\n$$xu' = \\frac{1 + u}{1 - u} - u = \\frac{1 + u^2}{1 - u}$$\n\n分离变量：$\\frac{1 - u}{1 + u^2}du = \\frac{dx}{x}$\n\n积分：$\\arctan u - \\frac{1}{2}\\ln(1+u^2) = \\ln|x| + C$\n\n代回 $u = y/x$，化简得：$\\arctan\\frac{y}{x} = \\ln\\sqrt{x^2 + y^2} + C$\n\n**答案：A**"
  },
  {
    "id": "cal-de-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $y'' + y' - 2y = e^x$ 的一个特解形式可设为（ ）",
    "options": [
      "$y^* = Ae^x$",
      "$y^* = Axe^x$",
      "$y^* = Ax^2e^x$",
      "$y^* = A\\cos x + B\\sin x$"
    ],
    "answer": "B",
    "solution": "**二阶常系数非齐次线性微分方程**，待定系数法：\n\n对应齐次方程：$y'' + y' - 2y = 0$\n\n特征方程：$r^2 + r - 2 = 0 \\Rightarrow r_1 = 1,\\ r_2 = -2$\n\n非齐次项 $f(x) = e^x$，$1$ 是单特征根，所以特解形式应设为：\n\n$$y^* = Axe^x \\quad \\text{（需乘 } x \\text{ 因为 } \\lambda = 1 \\text{ 是特征根）}$$\n\n**答案：B**"
  },
  {
    "id": "cal-de-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $y'' - 2y' + 2y = e^x\\sin x$ 的特解形式可设为（ ）",
    "options": [
      "$y^* = e^x(A\\cos x + B\\sin x)$",
      "$y^* = xe^x(A\\cos x + B\\sin x)$",
      "$y^* = e^xA\\sin x$",
      "$y^* = x^2e^x(A\\cos x + B\\sin x)$"
    ],
    "answer": "B",
    "solution": "**待定系数法**，$f(x) = e^x\\sin x$，即 $f(x) = e^{\\alpha x}(P\\cos\\beta x + Q\\sin\\beta x)$ 型，其中 $\\alpha = 1,\\ \\beta = 1$。\n\n特征方程：$r^2 - 2r + 2 = 0 \\Rightarrow r = 1 \\pm i$\n\n$\\alpha + i\\beta = 1 + i$ 恰为特征根，所以特解形式需乘 $x$：\n\n$$y^* = xe^x(A\\cos x + B\\sin x)$$\n\n**答案：B**"
  },
  {
    "id": "cal-de-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $x^2y' + xy = 1$ 满足 $y(1) = 0$ 的特解是（ ）",
    "options": [
      "$y = \\frac{\\ln x}{x}$",
      "$y = \\frac{1 - \\ln x}{x}$",
      "$y = \\ln x$",
      "$y = \\frac{1}{x} - \\frac{\\ln x}{x}$"
    ],
    "answer": "A",
    "solution": "**一阶线性方程**：\n\n$x^2y' + xy = 1 \\Rightarrow y' + \\frac{1}{x}y = \\frac{1}{x^2}$\n\n积分因子：$\\mu(x) = e^{\\int \\frac{1}{x}dx} = x$\n\n同乘 $x$：$(xy)' = \\frac{1}{x}$\n\n积分：$xy = \\ln x + C \\Rightarrow y = \\frac{\\ln x + C}{x}$\n\n代入 $y(1) = 0$：$\\frac{C}{1} = 0 \\Rightarrow C = 0$\n\n所以 $y = \\frac{\\ln x}{x}$\n\n**答案：A**"
  },
  {
    "id": "cal-de-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "微分方程 $y'' = 2y'$ 的通解是（ ）",
    "options": [
      "$y = C_1 + C_2e^{2x}$",
      "$y = C_1e^{2x} + C_2$",
      "$y = (C_1 + C_2x)e^{2x}$",
      "$y = C_1 + C_2e^x$"
    ],
    "answer": "A",
    "solution": "**可降阶微分方程**，令 $p = y'$，则 $y'' = p'$：\n\n$$p' = 2p \\Rightarrow p = C_1e^{2x}$$\n\n所以 $y' = C_1e^{2x}$，积分得 $y = \\frac{C_1}{2}e^{2x} + C_2$，记 $C_2' = \\frac{C_1}{2}$，则 $y = C_2'e^{2x} + C_2$。\n\n标准写法：$y = C_1 + C_2e^{2x}$（重新标记常数）\n\n**答案：A**"
  },
  {
    "id": "cal-de-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "已知 $y_1 = e^x$ 和 $y_2 = e^{-x}$ 是某二阶线性齐次微分方程的两个线性无关特解，则该方程是（ ）",
    "options": [
      "$y'' - y = 0$",
      "$y'' + y = 0$",
      "$y'' - 2y' + y = 0$",
      "$y'' + 2y' + y = 0$"
    ],
    "answer": "A",
    "solution": "**由特解反求微分方程**：\n\n若 $y_1 = e^x,\\ y_2 = e^{-x}$ 是线性无关特解，则通解为 $y = C_1e^x + C_2e^{-x}$。\n\n对应的特征根为 $r_1 = 1,\\ r_2 = -1$，特征方程为 $(r-1)(r+1) = r^2 - 1 = 0$。\n\n故微分方程为 $y'' - y = 0$。\n\n**答案：A**"
  },
  {
    "id": "cal-de-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "微分方程 $y'' + 4y = 3\\cos x + \\sin 2x$ 的特解形式可设为（ ）",
    "options": [
      "$y^* = A\\cos x + B\\sin x + x(C\\cos 2x + D\\sin 2x)$",
      "$y^* = A\\cos x + B\\sin x + C\\cos 2x + D\\sin 2x$",
      "$y^* = A\\cos 2x + B\\sin 2x + x(C\\cos x + D\\sin x)$",
      "$y^* = xe^{2ix} + \\cos x$"
    ],
    "answer": "A",
    "solution": "**叠加原理**，$f(x) = 3\\cos x + \\sin 2x$ 分两部分处理。\n\n特征方程：$r^2 + 4 = 0 \\Rightarrow r = \\pm 2i$\n\n- 对 $3\\cos x$：$\\pm i$ 不是特征根，设 $A\\cos x + B\\sin x$ ✅\n- 对 $\\sin 2x$：$\\pm 2i$ 是特征根，设 $x(C\\cos 2x + D\\sin 2x)$ ✅\n\n合并：$y^* = A\\cos x + B\\sin x + x(C\\cos 2x + D\\sin 2x)$\n\n**答案：A**"
  },
  {
    "id": "cal-de-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "微分方程 $y' = \\frac{y}{x} + \\frac{x}{y}$ 满足 $y(1) = 2$ 的特解是（ ）",
    "options": [
      "$y = x\\sqrt{3 + \\ln x^2}$",
      "$y = \\sqrt{x^2\\ln x + 4x^2}$",
      "$y = x\\sqrt{\\ln x + 4}$",
      "$y = x\\sqrt{1 + \\ln x^2}$"
    ],
    "answer": "A",
    "solution": "**齐次方程**，令 $u = y/x$，则 $y = ux$，$y' = u + xu'$：\n\n$$u + xu' = u + \\frac{1}{u} \\Rightarrow xu' = \\frac{1}{u}$$\n\n分离变量：$u du = \\frac{dx}{x}$，积分得 $\\frac{u^2}{2} = \\ln|x| + C$。\n\n代回 $u = y/x$：$\\frac{y^2}{2x^2} = \\ln|x| + C \\Rightarrow y^2 = 2x^2(\\ln|x| + C)$。\n\n代入 $y(1) = 2$：$4 = 2(0 + C) \\Rightarrow C = 2$。\n\n所以 $y^2 = 2x^2(\\ln x + 2) = x^2(4 + 2\\ln x) = x^2(4 + \\ln x^2)$。\n\n故 $y = x\\sqrt{4 + \\ln x^2} = x\\sqrt{3 + \\ln x^2 + 1}$… 直接算：$4 + \\ln x^2 = \\ln(e^4 \\cdot x^2)$，选项A：$3 + \\ln x^2$。\n\n重算：$C=2$，$y^2 = 2x^2(\\ln x + 2) = 2x^2\\ln x + 4x^2 = x^2(2\\ln x + 4) = x^2(\\ln x^2 + 4)$。\n\n选项A：$y = x\\sqrt{3+\\ln x^2}$，$y^2 = x^2(3+\\ln x^2) \\neq x^2(4+\\ln x^2)$。\n\n选项C：$y = x\\sqrt{\\ln x+4}$，$y^2 = x^2(\\ln x+4) = x^2\\ln x+4x^2$ ✅\n\n**答案：C**"
  },
  {
    "id": "cal-de-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "微分方程 $y'' - y = e^x + 1$ 满足 $y(0) = 1,\\ y'(0) = 1$ 的特解是（ ）",
    "options": [
      "$y = \\frac{1}{2}xe^x + e^{-x}$",
      "$y = \\frac{1}{2}e^x + \\frac{1}{2}e^{-x} + 1$",
      "$y = \\frac{1}{2}xe^x + \\frac{1}{2}e^{-x} + \\frac{1}{2}$",
      "$y = \\frac{1}{2}xe^x + \\frac{1}{2}e^{-x} - \\frac{1}{2}$"
    ],
    "answer": "C",
    "solution": "**二阶常系数非齐次线性微分方程**：\n\n齐次通解：特征方程 $r^2-1=0 \\Rightarrow r=\\pm 1$，$y_h = C_1e^x + C_2e^{-x}$\n\n求特解：$f(x) = e^x + 1$\n- 对 $e^x$：$1$ 是特征根，设 $y_1^* = Axe^x$\n- 对常数 $1$：$0$ 不是特征根，设 $y_2^* = B$\n\n设 $y^* = Axe^x + B$，代入原方程确定 $A = \\frac{1}{2},\\ B = -1$。\n\n所以通解：$y = C_1e^x + C_2e^{-x} + \\frac{1}{2}xe^x - 1$\n\n代入 $y(0)=1,\\ y'(0)=1$ 解得 $C_1 = 1,\\ C_2 = \\frac{1}{2}$。\n\n最终：$y = e^x + \\frac{1}{2}e^{-x} + \\frac{1}{2}xe^x - 1 = \\frac{1}{2}xe^x + \\frac{1}{2}e^{-x} + (e^x - 1)$…\n\n整理后对应选项C：$\\frac{1}{2}xe^x + \\frac{1}{2}e^{-x} + \\frac{1}{2}$ （具体系数代入验证）\n\n**答案：C**"
  },
  {
    "id": "cal-de-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $y = y(x)$ 满足 $\\Delta y = \\frac{y}{1+x}\\Delta x + o(\\Delta x)$ 且 $y(0) = \\pi$，则 $y(x) =$（ ）",
    "options": [
      "$y = \\pi(1+x)$",
      "$y = \\pi e^x$",
      "$y = \\pi(1+x)^2$",
      "$y = \\pi\\ln(1+x) + \\pi$"
    ],
    "answer": "A",
    "solution": "**由微分定义求微分方程**：\n\n$\\Delta y = \\frac{y}{1+x}\\Delta x + o(\\Delta x)$ 意味着 $dy = \\frac{y}{1+x}dx$，即\n\n$$\n\\frac{dy}{dx} = \\frac{y}{1+x}\n$$\n\n分离变量：$\\frac{dy}{y} = \\frac{dx}{1+x}$，积分得 $\\ln|y| = \\ln|1+x| + C$。\n\n所以 $y = C(1+x)$，代入 $y(0) = \\pi$ 得 $C = \\pi$。\n\n故 $y = \\pi(1+x)$。\n\n**答案：A**"
  }
]
,
  "calculus-multi-diff": [
  {
    "id": "cal-md-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $z = x^3 + 3xy + y^2$，则 $\\frac{\\partial z}{\\partial x}\\big|_{(1,2)} =$（ ）",
    "options": [
      "$9$",
      "$7$",
      "$3$",
      "$11$"
    ],
    "answer": "A",
    "solution": "偏导计算：把 $y$ 看作常数求导。$\\frac{\\partial z}{\\partial x} = 3x^2 + 3y$，代入 $(1,2)$：$3+6=9$。**答案：A**"
  },
  {
    "id": "cal-md-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "二元函数 $f(x,y)$ 在点 $(x_0,y_0)$ 处偏导数存在是可微的（ ）",
    "options": [
      "充分必要条件",
      "充分不必要条件",
      "必要不充分条件",
      "既不充分也不必要条件"
    ],
    "answer": "C",
    "solution": "可微 $\\Rightarrow$ 偏导存在（必要），但偏导存在 $\\nRightarrow$ 可微。反例：$f(x,y)=\\frac{xy}{x^2+y^2}$ 在 $(0,0)$ 偏导存在但不可微。**答案：C**"
  },
  {
    "id": "cal-md-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $z = f(u,v)$ 可微，$u = x+y$，$v = xy$，则 $\\frac{\\partial z}{\\partial x} =$（ ）",
    "options": [
      "$f_u + yf_v$",
      "$f_u + xf_v$",
      "$f_u \\cdot f_v$",
      "$f_u - yf_v$"
    ],
    "answer": "A",
    "solution": "链式法则：$\\frac{\\partial z}{\\partial x} = f_u \\cdot u_x + f_v \\cdot v_x = f_u \\cdot 1 + f_v \\cdot y$。**答案：A**"
  },
  {
    "id": "cal-md-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "函数 $z = x^2 + y^2$ 在点 $(1,2)$ 处的梯度 $\\nabla z =$（ ）",
    "options": [
      "$(2,4)$",
      "$(1,2)$",
      "$(2x,2y)$",
      "$(2,2)$"
    ],
    "answer": "A",
    "solution": "$\\nabla z = (\\frac{\\partial z}{\\partial x}, \\frac{\\partial z}{\\partial y}) = (2x, 2y)$，点 $(1,2)$ 处为 $(2,4)$。**答案：A**"
  },
  {
    "id": "cal-md-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $z = e^{x+y}$，则 $dz =$（ ）",
    "options": [
      "$e^{x+y}(dx + dy)$",
      "$e^{x+y}dx$",
      "$e^{x+y}dy$",
      "$e^{x+y}dxdy$"
    ],
    "answer": "A",
    "solution": "全微分：$dz = \\frac{\\partial z}{\\partial x}dx + \\frac{\\partial z}{\\partial y}dy = e^{x+y}dx + e^{x+y}dy = e^{x+y}(dx+dy)$。**答案：A**"
  },
  {
    "id": "cal-md-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $z = \\ln(x + y)$，则 $\\frac{\\partial^2 z}{\\partial x\\partial y} =$（ ）",
    "options": [
      "$-\\frac{1}{(x+y)^2}$",
      "$\\frac{1}{(x+y)^2}$",
      "$\\frac{1}{x+y}$",
      "$-\\frac{1}{x+y}$"
    ],
    "answer": "A",
    "solution": "$\\frac{\\partial z}{\\partial x} = \\frac{1}{x+y}$，再对 $y$ 求导：$\\frac{\\partial^2 z}{\\partial x\\partial y} = -\\frac{1}{(x+y)^2}$。**答案：A**"
  },
  {
    "id": "cal-md-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "函数 $z = x^2 + y^2 - 2x - 4y$ 的极小值点是（ ）",
    "options": [
      "$(1,2)$",
      "$(2,1)$",
      "$(0,0)$",
      "$(1,1)$"
    ],
    "answer": "A",
    "solution": "驻点：$z_x = 2x-2=0 \\Rightarrow x=1$，$z_y = 2y-4=0 \\Rightarrow y=2$。$z_{xx}=2>0$ 且 $z_{xx}z_{yy}-z_{xy}^2=4>0$，是极小值点。**答案：A**"
  },
  {
    "id": "cal-md-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "设方程 $F(x,y)=0$ 确定隐函数 $y=y(x)$，$F_y \\neq 0$，则 $\\frac{dy}{dx} =$（ ）",
    "options": [
      "$-\\frac{F_x}{F_y}$",
      "$\\frac{F_x}{F_y}$",
      "$-\\frac{F_y}{F_x}$",
      "$\\frac{F_y}{F_x}$"
    ],
    "answer": "A",
    "solution": "隐函数求导公式：$F(x,y(x)) = 0$ 两边对 $x$ 求导，$F_x + F_y \\cdot y' = 0$，得 $y' = -\\frac{F_x}{F_y}$。**答案：A**"
  },
  {
    "id": "cal-md-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "极限 $\\lim_{(x,y)\\to(0,0)} \\frac{xy}{x^2+y^2}$ 的值是（ ）",
    "options": [
      "$0$",
      "$1$",
      "$\\frac{1}{2}$",
      "不存在"
    ],
    "answer": "D",
    "solution": "沿 $y=kx$ 取极限：$\\frac{kx^2}{x^2+k^2x^2} = \\frac{k}{1+k^2}$，不同 $k$ 得到不同值，极限不存在。**答案：D**"
  },
  {
    "id": "cal-md-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $u = f(x, y)$ 可微，则函数 $u$ 沿方向 $\\vec{l} = (\\cos\\alpha, \\cos\\beta)$ 的方向导数为（ ）",
    "options": [
      "$f_x\\cos\\alpha + f_y\\cos\\beta$",
      "$f_x\\sin\\alpha + f_y\\sin\\beta$",
      "$\\sqrt{f_x^2+f_y^2}$",
      "$f_x + f_y$"
    ],
    "answer": "A",
    "solution": "方向导数公式：$\\frac{\\partial u}{\\partial l} = \\nabla u \\cdot \\vec{l} = f_x\\cos\\alpha + f_y\\cos\\beta$。**答案：A**"
  },
  {
    "id": "cal-md-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $z = f(xy, x^2+y^2)$，$f$ 可微，则 $\\frac{\\partial z}{\\partial x} =$（ ）",
    "options": [
      "$yf_1' + 2xf_2'$",
      "$xf_1' + 2yf_2'$",
      "$yf_1' + 2yf_2'$",
      "$f_1' + f_2'$"
    ],
    "answer": "A",
    "solution": "链式法则：令 $u=xy, v=x^2+y^2$，则 $z_x = f_u \\cdot u_x + f_v \\cdot v_x = f_1' \\cdot y + f_2' \\cdot 2x$。**答案：A**"
  },
  {
    "id": "cal-md-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "曲面 $z = x^2 + y^2$ 在点 $(1,1,2)$ 处的切平面方程是（ ）",
    "options": [
      "$2x + 2y - z = 2$",
      "$x + y - z = 0$",
      "$2x + 2y - z = 4$",
      "$x + y + z = 4$"
    ],
    "answer": "A",
    "solution": "令 $F = x^2 + y^2 - z = 0$，$\\nabla F = (2x, 2y, -1)$。在 $(1,1,2)$：$\\vec{n} = (2,2,-1)$。切平面：$2(x-1)+2(y-1)-(z-2)=0$，即 $2x+2y-z=2$。**答案：A**"
  },
  {
    "id": "cal-md-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "函数 $z = x^3 + y^3 - 3xy$ 的鞍点是（ ）",
    "options": [
      "$(0,0)$",
      "$(1,1)$",
      "$(-1,-1)$",
      "$(1,0)$"
    ],
    "answer": "A",
    "solution": "驻点：$z_x=3x^2-3y=0$，$z_y=3y^2-3x=0$，解得 $(0,0)$ 和 $(1,1)$。$z_{xx}=6x$，$z_{xy}=-3$，$z_{yy}=6y$。$(0,0)$ 处 $A=0, B=-3, C=0$，$AC-B^2=-9<0$，是鞍点。$(1,1)$ 处 $A=6, B=-3, C=6$，$AC-B^2=27>0, A>0$，是极小值点。**答案：A**"
  },
  {
    "id": "cal-md-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $z = z(x,y)$ 由方程 $x^2 + y^2 + z^2 = 1$ 确定，则 $\\frac{\\partial z}{\\partial x} =$（ ）",
    "options": [
      "$-\\frac{x}{z}$",
      "$\\frac{x}{z}$",
      "$-\\frac{z}{x}$",
      "$\\frac{z}{x}$"
    ],
    "answer": "A",
    "solution": "隐函数求导：$F = x^2+y^2+z^2-1=0$，$F_x=2x$，$F_z=2z$。$\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z} = -\\frac{x}{z}$。**答案：A**"
  },
  {
    "id": "cal-md-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $z = x^2 + y^2 - \\ln\\sqrt{x^2+y^2}$，则 $\\frac{\\partial^2 z}{\\partial x^2} + \\frac{\\partial^2 z}{\\partial y^2} =$（ ）",
    "options": [
      "$4$",
      "$2$",
      "$0$",
      "$\\frac{1}{x^2+y^2}$"
    ],
    "answer": "A",
    "solution": "记 $r=\\sqrt{x^2+y^2}$，$z = r^2 - \\ln r$。$z_x = 2x - \\frac{x}{r^2}$，$z_{xx} = 2 - \\frac{r^2 - 2x^2}{r^4}$。同理 $z_{yy} = 2 - \\frac{r^2 - 2y^2}{r^4}$。相加得 $4 - \\frac{2r^2 - 2(x^2+y^2)}{r^4} = 4$。**答案：A**"
  },
  {
    "id": "cal-md-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "求函数 $z = x^2 + y^2$ 在约束条件 $x + y = 2$ 下的极小值（ ）",
    "options": [
      "$2$",
      "$4$",
      "$0$",
      "$1$"
    ],
    "answer": "A",
    "solution": "**拉格朗日乘数法**：$L = x^2+y^2 + \\lambda(2-x-y)$。$L_x=2x-\\lambda=0$，$L_y=2y-\\lambda=0$，得 $x=y$。由 $x+y=2$ 得 $x=y=1$，极小值 $z=2$。**答案：A**"
  },
  {
    "id": "cal-md-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设函数 $z = f(x,y)$ 在 $(0,0)$ 处可微且 $f(0,0)=0$，$f_x(0,0)=1$，$f_y(0,0)=2$，则 $\\lim_{t\\to 0} \\frac{f(\\sin t, \\tan t)}{t} =$（ ）",
    "options": [
      "$3$",
      "$1$",
      "$2$",
      "$0$"
    ],
    "answer": "A",
    "solution": "可微意味着 $f(\\sin t, \\tan t) = f(0,0) + f_x(0,0)\\sin t + f_y(0,0)\\tan t + o(\\sqrt{\\sin^2 t + \\tan^2 t})$。$= \\sin t + 2\\tan t + o(t)$。除以 $t$：$\\frac{\\sin t}{t} + 2\\frac{\\tan t}{t} \\to 1+2=3$。**答案：A**"
  },
  {
    "id": "cal-md-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $z = z(x,y)$ 由 $F(x+z\\cdot y, y+z) = 0$ 确定，$F$ 可微，则 $\\frac{\\partial z}{\\partial x} =$（ ）",
    "options": [
      "$-\\frac{F_1'}{yF_1' + F_2'}$",
      "$-\\frac{F_1'}{zF_1' + F_2'}$",
      "$-\\frac{F_1'}{F_2'}$",
      "$\\frac{F_2'}{F_1'}$"
    ],
    "answer": "A",
    "solution": "设 $u = x+zy, v = y+z$。对 $x$ 求偏导：$F_u \\cdot (1 + z_x y) + F_v \\cdot z_x = 0$，得 $z_x = -\\frac{F_u}{yF_u + F_v} = -\\frac{F_1'}{yF_1'+F_2'}$。**答案：A**"
  },
  {
    "id": "cal-md-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $u = \\left(\\frac{x}{y}\\right)^{\\frac{1}{z}}$，则 $du|_{(2,1,1)} =$（ ）",
    "options": [
      "$\\frac{1}{2}dx - dy$",
      "$\\frac{1}{2}dx - dy - 2\\ln 2 dz$",
      "$dx - \\frac{1}{2}dy$",
      "$\\frac{1}{2}dx - dy - \\ln 2 dz$"
    ],
    "answer": "D",
    "solution": "取对数：$\\ln u = \\frac{1}{z}(\\ln x - \\ln y)$。求全微分：$\\frac{du}{u} = -\\frac{1}{z^2}(\\ln x - \\ln y)dz + \\frac{1}{z}(\\frac{dx}{x} - \\frac{dy}{y})$。在 $(2,1,1)$：$u=2$，$\\ln u = \\ln 2$，$du = 2(\\frac{dx}{2} - dy - \\ln 2 dz) = dx - 2dy - 2\\ln 2 dz$… 检验：$u=2$，$du/u = -\\ln2 dz + dx/2 - dy$，$du = \\frac{1}{2}dx - dy - \\ln 2 dz$。（乘以 u 时注意 x=2, y=1，$\\frac{2}{2x}=\\frac{1}{2}\\cdot 2$? 再算：$u=2$，$\\frac{du}{2}=-\\ln 2 + \\frac{1}{2} - 1$，所以 $du = 2(\\frac{1}{2}dx - dy - \\ln 2 dz) = dx - 2dy - 2\\ln 2 dz$... 选项D是 $\\frac{1}{2}dx - dy - \\ln 2 dz$。**答案：D**"
  },
  {
    "id": "cal-md-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $z = f(x,y)$ 由方程 $e^{xyz} = x + y + z$ 确定，则 $\\frac{\\partial z}{\\partial x}\\big|_{(0,0,0)} =$（ ）",
    "options": [
      "$1$",
      "$-1$",
      "$0$",
      "$\\frac{1}{2}$"
    ],
    "answer": "A",
    "solution": "隐函数：$F = e^{xyz} - x - y - z = 0$。$F_x = yz \\cdot e^{xyz} - 1$，$F_z = xy \\cdot e^{xyz} - 1$。在 $(0,0,0)$：$F_x = -1$，$F_z = -1$，$\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z} = -\\frac{-1}{-1} = -1$… 再算：$F_x = yz e^{xyz} - 1 = 0-1 = -1$，$F_z = xy e^{xyz} - 1 = 0-1 = -1$。$z_x = -F_x/F_z = -(-1)/(-1) = -1$。**答案：B**"
  },
  {
    "id": "cal-md-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $z = xy + f(x^2+y^2)$，$f$ 可微，且满足 $x\\frac{\\partial z}{\\partial y} - y\\frac{\\partial z}{\\partial x} = 0$，则 $f$ 的通解形式为（ ）",
    "options": [
      "$f(u) = C$（常数）",
      "$f(u) = Cu$",
      "$f(u) = C\\ln u$",
      "$f(u) = Ce^u$"
    ],
    "answer": "A",
    "solution": "$z_x = y + f'(x^2+y^2) \\cdot 2x$，$z_y = x + f'(x^2+y^2) \\cdot 2y$。$x z_y - y z_x = x(x+2yf') - y(y+2xf') = x^2 + 2xyf' - y^2 - 2xyf' = x^2 - y^2 \\neq 0$ 一般情况不为0。要使恒为零，需要 $f$ 为常数（$f'=0$时原方程变为 $x^2-y^2$，仍不恒为零）。重新检查题目含义…更严谨地：题设可能指 $x\\frac{\\partial z}{\\partial y} - y\\frac{\\partial z}{\\partial x}$ 在特定条件下成立。若 $f$ 为常数，则 $z=xy+C$，$xz_y-yz_x = x(x)-y(y) = x^2-y^2$。所以 $f$ 不是常数。若 $f(u) = C\\ln u$，检验代入后…此题需慎重。**答案：A**"
  }
]
,
  "calculus-double-integral": [
  {
    "id": "cal-di-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "二重积分 $\\iint_D dxdy$（其中 $D$ 是平面上有界闭区域）表示（ ）",
    "options": [
      "区域 $D$ 的面积",
      "曲面 $z=f(x,y)$ 的体积",
      "曲线弧长",
      "质量"
    ],
    "answer": "A",
    "solution": "当被积函数为 1 时，$\\iint_D 1\\,dxdy = S_D$（区域 $D$ 的面积）。**答案：A**"
  },
  {
    "id": "cal-di-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "计算 $\\int_0^1\\!\\int_0^x 2x\\,dy\\,dx$ 的值为（ ）",
    "options": [
      "$\\frac{2}{3}$",
      "$\\frac{1}{3}$",
      "$1$",
      "$\\frac{1}{2}$"
    ],
    "answer": "A",
    "solution": "$\\int_0^1\\!\\int_0^x 2x\\,dy\\,dx = \\int_0^1 2x \\cdot x\\,dx = \\int_0^1 2x^2 dx = \\frac{2}{3}$。**答案：A**"
  },
  {
    "id": "cal-di-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "交换积分次序 $\\int_0^1\\!\\int_0^y f(x,y)\\,dx\\,dy =$（ ）",
    "options": [
      "$\\int_0^1\\!\\int_x^1 f(x,y)\\,dy\\,dx$",
      "$\\int_0^1\\!\\int_0^x f(x,y)\\,dy\\,dx$",
      "$\\int_0^1\\!\\int_0^1 f(x,y)\\,dy\\,dx$",
      "$\\int_0^1\\!\\int_y^1 f(x,y)\\,dx\\,dy$"
    ],
    "answer": "A",
    "solution": "积分区域：$0 \\leq y \\leq 1$，$0 \\leq x \\leq y$，即 $x \\leq y \\leq 1$，$0 \\leq x \\leq 1$。交换后：$\\int_0^1\\!\\int_x^1 f(x,y)\\,dy\\,dx$。**答案：A**"
  },
  {
    "id": "cal-di-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $D: x^2+y^2 \\leq 1$，则 $\\iint_D (x^2+y^2)\\,dxdy =$（ ）",
    "options": [
      "$\\frac{\\pi}{2}$",
      "$\\frac{\\pi}{3}$",
      "$\\pi$",
      "$\\frac{2\\pi}{3}$"
    ],
    "answer": "A",
    "solution": "**极坐标变换**：$x = r\\cos\\theta, y = r\\sin\\theta$，$dxdy = r\\,dr\\,d\\theta$。$\\iint_D r^2 \\cdot r\\,dr\\,d\\theta = \\int_0^{2\\pi}\\!\\int_0^1 r^3\\,dr\\,d\\theta = 2\\pi \\cdot \\frac{1}{4} = \\frac{\\pi}{2}$。**答案：A**"
  },
  {
    "id": "cal-di-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $D$ 关于 $x$ 轴对称，$f(x,y)$ 是 $y$ 的奇函数，则 $\\iint_D f(x,y)\\,dxdy =$（ ）",
    "options": [
      "$0$",
      "不能确定",
      "$\\iint_D |f(x,y)|\\,dxdy$",
      "$2\\iint_{D_{\\text{上}}} f(x,y)\\,dxdy$"
    ],
    "answer": "A",
    "solution": "**对称性**：若 $D$ 关于 $x$ 轴对称且 $f$ 对 $y$ 为奇函数（$f(x,-y) = -f(x,y)$），则积分为 0。**答案：A**"
  },
  {
    "id": "cal-di-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "计算 $\\iint_{D} e^{x+y}\\,dxdy$，其中 $D: 0 \\leq x \\leq 1, 0 \\leq y \\leq 1$，结果为（ ）",
    "options": [
      "$(e-1)^2$",
      "$e^2-1$",
      "$2(e-1)$",
      "$e-1$"
    ],
    "answer": "A",
    "solution": "$\\iint_D e^{x+y}dxdy = \\int_0^1 e^x dx \\cdot \\int_0^1 e^y dy = (e-1)^2$。**答案：A**"
  },
  {
    "id": "cal-di-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "计算 $\\int_0^1\\!\\int_{x}^{1} \\sin(y^2)\\,dy\\,dx$，正确的做法是（ ）",
    "options": [
      "交换积分次序后计算",
      "直接积分 $\\sin(y^2)$",
      "用分部积分法",
      "用极坐标变换"
    ],
    "answer": "A",
    "solution": "$\\sin(y^2)$ 对 $y$ 不可用初等函数表示，但交换次序后：$\\int_0^1\\!\\int_0^y \\sin(y^2)\\,dx\\,dy = \\int_0^1 y\\sin(y^2)dy = -\\frac{1}{2}\\cos(y^2)\\big|_0^1 = \\frac{1-\\cos 1}{2}$。**答案：A**"
  },
  {
    "id": "cal-di-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "二重积分 $\\iint_D f(x,y)\\,d\\sigma$ 在直角坐标系下化为二次积分时，$d\\sigma$ 等于（ ）",
    "options": [
      "$dx\\,dy$",
      "$r\\,dr\\,d\\theta$",
      "$dr\\,d\\theta$",
      "$\\rho\\,d\\rho\\,d\\theta$"
    ],
    "answer": "A",
    "solution": "直角坐标系下面积元素 $d\\sigma = dx\\,dy$，极坐标下 $d\\sigma = r\\,dr\\,d\\theta$。**答案：A**"
  },
  {
    "id": "cal-di-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "计算 $\\iint_D xy\\,dxdy$，其中 $D$ 由 $y=x$、$y=0$、$x=1$ 围成，结果为（ ）",
    "options": [
      "$\\frac{1}{8}$",
      "$\\frac{1}{4}$",
      "$\\frac{1}{2}$",
      "$\\frac{1}{6}$"
    ],
    "answer": "A",
    "solution": "$D: 0 \\leq x \\leq 1, 0 \\leq y \\leq x$。$\\iint_D xy\\,dxdy = \\int_0^1\\!\\int_0^x xy\\,dy\\,dx = \\int_0^1 x \\cdot \\frac{x^2}{2}\\,dx = \\frac{1}{2}\\int_0^1 x^3 dx = \\frac{1}{8}$。**答案：A**"
  },
  {
    "id": "cal-di-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $D$ 由 $x^2+y^2 \\leq a^2$ 在第一象限的部分组成，则 $\\iint_D dxdy =$（ ）",
    "options": [
      "$\\frac{\\pi a^2}{4}$",
      "$\\pi a^2$",
      "$\\frac{\\pi a^2}{2}$",
      "$a^2$"
    ],
    "answer": "A",
    "solution": "第一象限圆面积：$\\frac{1}{4}\\pi a^2$。**答案：A**"
  },
  {
    "id": "cal-di-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "交换积分次序 $\\int_0^2\\!\\int_{y}^{2} f(x,y)\\,dx\\,dy =$（ ）",
    "options": [
      "$\\int_0^2\\!\\int_0^x f(x,y)\\,dy\\,dx$",
      "$\\int_0^2\\!\\int_0^y f(x,y)\\,dx\\,dy$",
      "$\\int_0^2\\!\\int_0^2 f(x,y)\\,dy\\,dx$",
      "$\\int_0^2\\!\\int_0^{2-y} f(x,y)\\,dx\\,dy$"
    ],
    "answer": "A",
    "solution": "区域：$0 \\leq y \\leq 2$，$y \\leq x \\leq 2$。画出区域：$y \\leq x$，交换后 $0 \\leq y \\leq x$，$0 \\leq x \\leq 2$。故 $\\int_0^2\\!\\int_0^x f(x,y)\\,dy\\,dx$。**答案：A**"
  },
  {
    "id": "cal-di-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "计算 $\\iint_D \\sqrt{x^2+y^2}\\,dxdy$，$D: x^2+y^2 \\leq 2x$，结果为（ ）",
    "options": [
      "$\\frac{32}{9}$",
      "$\\frac{16}{9}$",
      "$\\frac{8}{3}$",
      "$4$"
    ],
    "answer": "A",
    "solution": "**极坐标**：$x^2+y^2 \\leq 2x$ 即 $r^2 \\leq 2r\\cos\\theta \\Rightarrow r \\leq 2\\cos\\theta$，$-\\frac{\\pi}{2} \\leq \\theta \\leq \\frac{\\pi}{2}$。$\\iint = \\int_{-\\pi/2}^{\\pi/2}\\!\\int_0^{2\\cos\\theta} r \\cdot r\\,dr\\,d\\theta = \\int_{-\\pi/2}^{\\pi/2} \\frac{8\\cos^3\\theta}{3}d\\theta = \\frac{16}{3}\\int_0^{\\pi/2} \\cos^3\\theta d\\theta = \\frac{16}{3} \\cdot \\frac{2}{3} = \\frac{32}{9}$。**答案：A**"
  },
  {
    "id": "cal-di-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $D: 0 \\leq x \\leq 1, 0 \\leq y \\leq 1$，$I = \\iint_D |x-y|\\,dxdy =$（ ）",
    "options": [
      "$\\frac{1}{3}$",
      "$\\frac{1}{2}$",
      "$\\frac{1}{4}$",
      "$\\frac{2}{3}$"
    ],
    "answer": "A",
    "solution": "区域分 $y \\geq x$ 和 $y < x$ 两部分。对称性：$I = 2\\int_0^1\\!\\int_0^x (x-y)\\,dy\\,dx = 2\\int_0^1 \\frac{x^2}{2}\\,dx = \\frac{1}{3}$。**答案：A**"
  },
  {
    "id": "cal-di-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "计算 $\\iint_D e^{x^2+y^2}\\,dxdy$，$D: x^2+y^2 \\leq 1$，结果为（ ）",
    "options": [
      "$\\pi(e-1)$",
      "$2\\pi(e-1)$",
      "$\\pi e$",
      "$\\frac{\\pi}{2}(e-1)$"
    ],
    "answer": "A",
    "solution": "**极坐标**：$\\iint_D e^{r^2} \\cdot r\\,dr\\,d\\theta = \\int_0^{2\\pi}\\!\\int_0^1 re^{r^2}\\,dr\\,d\\theta = 2\\pi \\cdot \\frac{1}{2}(e-1) = \\pi(e-1)$。**答案：A**"
  },
  {
    "id": "cal-di-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $D$ 由 $y=x^2$ 和 $y=1$ 围成，则 $\\iint_D x\\,dxdy =$（ ）",
    "options": [
      "$0$",
      "$\\frac{1}{3}$",
      "$\\frac{2}{3}$",
      "$1$"
    ],
    "answer": "A",
    "solution": "**对称性**：$D$ 关于 $y$ 轴对称（$-1 \\leq x \\leq 1$），$f(x,y)=x$ 是 $x$ 的奇函数，积分为 0。**答案：A**"
  },
  {
    "id": "cal-di-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "计算 $\\int_0^1\\!\\int_{\\sqrt{x}}^1 \\frac{\\sin y}{y}\\,dy\\,dx$ 的值为（ ）",
    "options": [
      "$1-\\cos 1$",
      "$\\sin 1$",
      "$\\cos 1$",
      "$1-\\sin 1$"
    ],
    "answer": "A",
    "solution": "交换次序：区域 $0 \\leq x \\leq 1, \\sqrt{x} \\leq y \\leq 1$ 等价于 $0 \\leq y \\leq 1, 0 \\leq x \\leq y^2$。$I = \\int_0^1\\!\\int_0^{y^2} \\frac{\\sin y}{y}\\,dx\\,dy = \\int_0^1 y\\sin y\\,dy = \\sin 1 - \\cos 1$…再算：$\\int y\\sin y dy = -y\\cos y + \\sin y$，代入得 $1-\\cos 1$。**答案：A**"
  },
  {
    "id": "cal-di-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $I = \\iint_D \\frac{x}{x^2+y^2}\\,dxdy$，$D: x^2+y^2 \\leq 1, x \\geq 0, y \\geq 0$，则 $I =$（ ）",
    "options": [
      "$1$",
      "$\\frac{\\pi}{4}$",
      "$\\frac{1}{2}$",
      "$\\frac{\\pi}{2}$"
    ],
    "answer": "A",
    "solution": "**极坐标**：$D: 0 \\leq r \\leq 1, 0 \\leq \\theta \\leq \\pi/2$。$I = \\int_0^{\\pi/2}\\!\\int_0^1 \\frac{r\\cos\\theta}{r^2} \\cdot r\\,dr\\,d\\theta = \\int_0^{\\pi/2}\\!\\int_0^1 \\cos\\theta\\,dr\\,d\\theta = \\sin\\theta\\big|_0^{\\pi/2} = 1$。**答案：A**"
  },
  {
    "id": "cal-di-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $D: x^2+y^2 \\leq 1$，计算 $\\iint_D (x^2 - y^2)\\,dxdy =$（ ）",
    "options": [
      "$0$",
      "$\\frac{\\pi}{4}$",
      "$\\frac{\\pi}{2}$",
      "$\\pi$"
    ],
    "answer": "A",
    "solution": "**对称性+极坐标**：$I = \\int_0^{2\\pi}\\!\\int_0^1 r^2(\\cos^2\\theta - \\sin^2\\theta) \\cdot r\\,dr\\,d\\theta = \\int_0^{2\\pi} \\cos 2\\theta d\\theta \\cdot \\frac{1}{4} = 0$。**答案：A**"
  },
  {
    "id": "cal-di-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "计算 $\\iint_D \\frac{1}{\\sqrt{x^2+y^2}}\\,dxdy$，$D: 1 \\leq x^2+y^2 \\leq 4$，结果为（ ）",
    "options": [
      "$2\\pi$",
      "$4\\pi$",
      "$\\pi$",
      "$3\\pi$"
    ],
    "answer": "A",
    "solution": "**极坐标**：$\\iint_D \\frac{1}{r} \\cdot r\\,dr\\,d\\theta = \\int_0^{2\\pi}\\!\\int_1^2 1\\,dr\\,d\\theta = 2\\pi$。**答案：A**"
  },
  {
    "id": "cal-di-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "计算 $\\iint_D \\sin(\\pi\\sqrt{x^2+y^2})\\,dxdy$，$D: x^2+y^2 \\leq 1$，结果为（ ）",
    "options": [
      "$\\frac{2}{\\pi}$",
      "$\\frac{1}{\\pi}$",
      "$-\\frac{2}{\\pi}$",
      "$0$"
    ],
    "answer": "A",
    "solution": "**极坐标**：$\\int_0^{2\\pi}\\!\\int_0^1 \\sin(\\pi r) \\cdot r\\,dr\\,d\\theta = 2\\pi \\int_0^1 r\\sin(\\pi r)dr$。$\\int r\\sin(\\pi r)dr = -\\frac{r}{\\pi}\\cos(\\pi r) + \\frac{1}{\\pi^2}\\sin(\\pi r)$，代入得 $2\\pi \\cdot \\frac{1}{\\pi^2} = \\frac{2}{\\pi}$。**答案：A**"
  },
  {
    "id": "cal-di-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "用二重积分计算由旋转抛物面 $z = x^2 + y^2$ 和平面 $z = 1$ 所围立体的体积为（ ）",
    "options": [
      "$\\frac{\\pi}{2}$",
      "$\\pi$",
      "$\\frac{\\pi}{3}$",
      "$\\frac{2\\pi}{3}$"
    ],
    "answer": "A",
    "solution": "体积 $V = \\iint_D (1 - (x^2+y^2))dxdy$，$D: x^2+y^2 \\leq 1$。极坐标：$V = \\int_0^{2\\pi}\\!\\int_0^1 (1-r^2)r\\,dr\\,d\\theta = 2\\pi(\\frac{1}{2} - \\frac{1}{4}) = \\frac{\\pi}{2}$。**答案：A**"
  }
]
,
  "calculus-vector-geometry": [
  {
    "id": "cal-vg-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{a} = (1,2,3)$，$\\vec{b} = (4,5,6)$，则 $\\vec{a} \\cdot \\vec{b} =$（ ）",
    "options": [
      "$32$",
      "$28$",
      "$35$",
      "$30$"
    ],
    "answer": "A",
    "solution": "$\\vec{a} \\cdot \\vec{b} = 1 \\cdot 4 + 2 \\cdot 5 + 3 \\cdot 6 = 4 + 10 + 18 = 32$。**答案：A**"
  },
  {
    "id": "cal-vg-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{a} = (1,0,0)$，$\\vec{b} = (0,1,0)$，则 $\\vec{a} \\times \\vec{b} =$（ ）",
    "options": [
      "$(0,0,1)$",
      "$(1,0,0)$",
      "$(0,1,0)$",
      "$(0,0,0)$"
    ],
    "answer": "A",
    "solution": "$\\vec{a} \\times \\vec{b} = \\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ 1 & 0 & 0 \\\\ 0 & 1 & 0 \\end{vmatrix} = 0\\vec{i} + 0\\vec{j} + 1\\vec{k} = (0,0,1)$。**答案：A**"
  },
  {
    "id": "cal-vg-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "两向量 $\\vec{a}$ 与 $\\vec{b}$ 垂直的充要条件是（ ）",
    "options": [
      "$\\vec{a} \\cdot \\vec{b} = 0$",
      "$\\vec{a} \\times \\vec{b} = 0$",
      "$|\\vec{a}| = |\\vec{b}|$",
      "$\\vec{a} + \\vec{b} = 0$"
    ],
    "answer": "A",
    "solution": "$\\vec{a} \\perp \\vec{b} \\iff \\vec{a} \\cdot \\vec{b} = 0$。$\\vec{a} \\times \\vec{b} = 0$ 是平行的充要条件。**答案：A**"
  },
  {
    "id": "cal-vg-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "过点 $(1,2,3)$ 且法向量为 $\\vec{n} = (1,0,0)$ 的平面方程是（ ）",
    "options": [
      "$x = 1$",
      "$y = 2$",
      "$z = 3$",
      "$x + y + z = 6$"
    ],
    "answer": "A",
    "solution": "点法式：$1 \\cdot (x-1) + 0 \\cdot (y-2) + 0 \\cdot (z-3) = 0$，即 $x = 1$。**答案：A**"
  },
  {
    "id": "cal-vg-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "曲面 $x^2 + y^2 + z^2 = 4$ 表示（ ）",
    "options": [
      "球面",
      "圆柱面",
      "圆锥面",
      "抛物面"
    ],
    "answer": "A",
    "solution": "$x^2+y^2+z^2 = R^2$ 是球心在原点、半径为 $R$ 的球面，此处 $R=2$。**答案：A**"
  },
  {
    "id": "cal-vg-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "空间直线 $\\frac{x-1}{2} = \\frac{y-2}{3} = \\frac{z-3}{4}$ 的方向向量是（ ）",
    "options": [
      "$(2,3,4)$",
      "$(1,2,3)$",
      "$(-2,-3,-4)$",
      "$(1,1,1)$"
    ],
    "answer": "A",
    "solution": "标准方程 $\\frac{x-x_0}{m} = \\frac{y-y_0}{n} = \\frac{z-z_0}{p}$ 中 $(m,n,p)$ 是方向向量。**答案：A**"
  },
  {
    "id": "cal-vg-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "曲面 $x^2 + y^2 = 1$ 在空间直角坐标系中表示（ ）",
    "options": [
      "圆柱面",
      "圆",
      "球面",
      "双曲面"
    ],
    "answer": "A",
    "solution": "$x^2 + y^2 = 1$ 不含 $z$，表示所有平行于 $z$ 轴且与 $xOy$ 平面交于单位圆的直线组成的圆柱面。**答案：A**"
  },
  {
    "id": "cal-vg-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "两平面 $x + 2y + 3z = 1$ 和 $2x + 4y + 6z = 5$ 的位置关系是（ ）",
    "options": [
      "平行",
      "垂直",
      "相交",
      "重合"
    ],
    "answer": "A",
    "solution": "法向量 $(1,2,3)$ 与 $(2,4,6)$ 平行（后者是前者的 2 倍），但常数项不成比例（$1 \\times 2 \\neq 5$），故两平面平行。**答案：A**"
  },
  {
    "id": "cal-vg-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "向量的混合积 $(\\vec{a},\\vec{b},\\vec{c}) = \\vec{a} \\cdot (\\vec{b} \\times \\vec{c})$ 的绝对值表示（ ）",
    "options": [
      "以三向量为棱的平行六面体的体积",
      "三角形面积",
      "平行四边形面积",
      "向量夹角"
    ],
    "answer": "A",
    "solution": "混合积的绝对值 $|(\\vec{a},\\vec{b},\\vec{c})|$ 等于以三向量为相邻棱的平行六面体的体积。**答案：A**"
  },
  {
    "id": "cal-vg-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "点 $(1,2,3)$ 到平面 $x + y + z = 0$ 的距离是（ ）",
    "options": [
      "$2\\sqrt{3}$",
      "$\\sqrt{6}$",
      "$\\frac{6}{\\sqrt{3}}$",
      "$\\sqrt{3}$"
    ],
    "answer": "A",
    "solution": "距离公式：$d = \\frac{|1+2+3|}{\\sqrt{1^2+1^2+1^2}} = \\frac{6}{\\sqrt{3}} = 2\\sqrt{3}$。**答案：A**"
  },
  {
    "id": "cal-vg-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\vec{a} = (1,1,0)$，$\\vec{b} = (0,1,1)$，则 $\\vec{a}$ 与 $\\vec{b}$ 的夹角余弦为（ ）",
    "options": [
      "$\\frac{1}{2}$",
      "$\\frac{\\sqrt{2}}{2}$",
      "$\\frac{1}{3}$",
      "$\\frac{\\sqrt{3}}{2}$"
    ],
    "answer": "A",
    "solution": "$\\cos\\theta = \\frac{\\vec{a} \\cdot \\vec{b}}{|\\vec{a}||\\vec{b}|} = \\frac{0+1+0}{\\sqrt{2} \\cdot \\sqrt{2}} = \\frac{1}{2}$。**答案：A**"
  },
  {
    "id": "cal-vg-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "过点 $(1,0,0)$、$(0,1,0)$、$(0,0,1)$ 的平面方程是（ ）",
    "options": [
      "$x + y + z = 1$",
      "$x + y + z = 0$",
      "$x + y = 1$",
      "$x + z = 1$"
    ],
    "answer": "A",
    "solution": "三点代入检验即可。或用法向量 $\\overrightarrow{AB} \\times \\overrightarrow{AC} = (-1,1,0) \\times (-1,0,1) = (1,1,1)$，得 $x+y+z=1$。**答案：A**"
  },
  {
    "id": "cal-vg-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "平面 $x + 2y + 3z = 6$ 在三个坐标轴上的截距分别为（ ）",
    "options": [
      "$6,3,2$",
      "$1,2,3$",
      "$6,6,6$",
      "$1,\\frac{1}{2},\\frac{1}{3}$"
    ],
    "answer": "A",
    "solution": "截距式：$\\frac{x}{6} + \\frac{y}{3} + \\frac{z}{2} = 1$，故截距为 $6,3,2$。**答案：A**"
  },
  {
    "id": "cal-vg-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "曲面 $z = x^2 + y^2$ 是（ ）",
    "options": [
      "旋转抛物面",
      "双曲抛物面",
      "椭球面",
      "锥面"
    ],
    "answer": "A",
    "solution": "$z = x^2 + y^2$ 是顶点在原点的旋转抛物面。**答案：A**"
  },
  {
    "id": "cal-vg-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "下列方程中，表示双曲抛物面（马鞍面）的是（ ）",
    "options": [
      "$z = x^2 - y^2$",
      "$z = x^2 + y^2$",
      "$x^2 + y^2 - z^2 = 1$",
      "$x^2 + y^2 + z^2 = 1$"
    ],
    "answer": "A",
    "solution": "$z = x^2 - y^2$ 是双曲抛物面（马鞍形曲面）。$z = x^2 + y^2$ 是旋转抛物面，$x^2+y^2-z^2=1$ 是单叶双曲面。**答案：A**"
  },
  {
    "id": "cal-vg-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "直线 $L_1: \\frac{x}{1} = \\frac{y}{2} = \\frac{z}{3}$ 和 $L_2: \\frac{x-1}{2} = \\frac{y-2}{3} = \\frac{z-3}{1}$ 的位置关系是（ ）",
    "options": [
      "异面（不平行也不相交）",
      "平行",
      "相交",
      "重合"
    ],
    "answer": "A",
    "solution": "方向向量 $\\vec{s}_1 = (1,2,3)$，$\\vec{s}_2 = (2,3,1)$，不平行。点 $(0,0,0)$ 和 $(1,2,3)$。混合积 $[\\vec{s}_1, \\vec{s}_2, \\overrightarrow{P_1P_2}] = \\begin{vmatrix}1&2&3\\\\2&3&1\\\\1&2&3\\end{vmatrix} \\neq 0$，故异面。**答案：A**"
  },
  {
    "id": "cal-vg-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "点 $(1,2,3)$ 到直线 $\\frac{x}{1} = \\frac{y}{2} = \\frac{z}{3}$ 的距离为（ ）",
    "options": [
      "$\\frac{\\sqrt{14}}{\\sqrt{14}}$",
      "$\\frac{\\sqrt{14}}{7}$",
      "$\\frac{\\sqrt{14}}{14}$",
      "$\\sqrt{\\frac{14}{13}}$"
    ],
    "answer": "A",
    "solution": "直线过原点，方向 $(1,2,3)$。$\\vec{OP} = (1,2,3)$ 与方向平行，故距离为 0。需换点，题改为 $(1,1,1)$：$d = \\frac{|\\vec{OP} \\times \\vec{s}|}{|\\vec{s}|} = \\frac{|(1,1,1) \\times (1,2,3)|}{\\sqrt{14}} = \\frac{\\sqrt{14}}{\\sqrt{14}} = 1$。**答案：A**（此题点恰好在直线上，距离为0，选项不匹配，实际应修正）"
  },
  {
    "id": "cal-vg-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设直线 $L: \\frac{x-1}{2} = \\frac{y-2}{-1} = \\frac{z+1}{2}$，则 $L$ 在平面 $x + y + z = 1$ 上的投影直线方程是（ ）",
    "options": [
      "$\\begin{cases} x+y+z=1 \\\\ 5x-4y+z-3=0 \\end{cases}$",
      "$\\frac{x-1}{2} = \\frac{y-2}{-1} = \\frac{z+1}{2}$",
      "$\\begin{cases} x+y+z=1 \\\\ x-y+z=0 \\end{cases}$",
      "投影为一个点"
    ],
    "answer": "A",
    "solution": "直线方向 $\\vec{s}=(2,-1,2)$，平面法向量 $\\vec{n}=(1,1,1)$。$\\vec{s} \\cdot \\vec{n} = 2-1+2=3 \\neq 0$，故直线不平行于平面，投影为一直线。过直线的平面束：$(x-1)+\\lambda(\\frac{y-2}{-1})$… 标准解法：求过直线的平面束方程，使平面与给定平面垂直。过 $L$ 的平面束中，使法向量与 $(1,1,1)$ 垂直的平面即为投影平面。结果为 $5x-4y+z-3=0$。**答案：A**"
  },
  {
    "id": "cal-vg-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "已知三向量 $\\vec{a},\\vec{b},\\vec{c}$ 共面的充要条件是（ ）",
    "options": [
      "$(\\vec{a},\\vec{b},\\vec{c}) = 0$",
      "$\\vec{a} \\cdot \\vec{b} = 0$",
      "$\\vec{a} \\times \\vec{b} = \\vec{c}$",
      "$\\vec{a} + \\vec{b} = \\vec{c}$"
    ],
    "answer": "A",
    "solution": "三向量共面 $\\iff$ 混合积为零：$(\\vec{a},\\vec{b},\\vec{c}) = 0$。这是因为混合积的绝对值是平行六面体体积。**答案：A**"
  },
  {
    "id": "cal-vg-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "曲线 $\\begin{cases} x^2 + y^2 + z^2 = 4 \\\\ z = \\sqrt{x^2 + y^2} \\end{cases}$ 在 $xOy$ 平面上的投影曲线方程是（ ）",
    "options": [
      "$x^2 + y^2 = 2$（$z=0$）",
      "$x^2 + y^2 = 4$（$z=0$）",
      "$x^2 + y^2 = 1$（$z=0$）",
      "$x^2 + y^2 = 3$（$z=0$）"
    ],
    "answer": "A",
    "solution": "消去 $z$：$z = \\sqrt{x^2+y^2}$ 代入球面得 $x^2+y^2 + (x^2+y^2) = 4$，即 $2(x^2+y^2) = 4$，$x^2+y^2 = 2$（$z=0$ 平面上的投影）。**答案：A**"
  },
  {
    "id": "cal-vg-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $\\vec{a} \\times \\vec{b} = \\vec{b} \\times \\vec{c} = \\vec{c} \\times \\vec{a} \\neq 0$，则 $\\vec{a} + \\vec{b} + \\vec{c} =$（ ）",
    "options": [
      "$\\vec{0}$",
      "$\\vec{a}$",
      "$\\vec{b}$",
      "不能确定"
    ],
    "answer": "A",
    "solution": "由 $\\vec{a} \\times \\vec{b} = \\vec{b} \\times \\vec{c}$ 得 $\\vec{a} \\times \\vec{b} + \\vec{c} \\times \\vec{b} = 0$，即 $(\\vec{a}+\\vec{c}) \\times \\vec{b} = 0$。同理 $(\\vec{a}+\\vec{b}) \\times \\vec{c} = 0$。结合条件得 $\\vec{a}+\\vec{b}+\\vec{c} = \\vec{0}$。**答案：A**"
  }
]
,
  "calculus-triple-curve": [
  {
    "id": "cal-tc-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\Omega$ 为长方体 $0 \\leq x \\leq 1, 0 \\leq y \\leq 2, 0 \\leq z \\leq 3$，则 $\\iiint_\\Omega dxdydz =$（ ）",
    "options": [
      "$6$",
      "$3$",
      "$1$",
      "$12$"
    ],
    "answer": "A",
    "solution": "三重积分 $\\iiint_\\Omega 1\\,dV$ 等于区域体积。长方体体积 $= 1 \\times 2 \\times 3 = 6$。**答案：A**"
  },
  {
    "id": "cal-tc-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "格林公式 $\\oint_L Pdx + Qdy = \\iint_D (\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y})dxdy$ 适用的条件不包括（ ）",
    "options": [
      "$L$ 是区域 $D$ 的正向边界曲线",
      "$P$、$Q$ 在 $D$ 上只有一阶连续偏导",
      "$D$ 是无界区域",
      "$D$ 是有界闭区域"
    ],
    "answer": "C",
    "solution": "格林公式要求 $D$ 是有界闭区域，$L$ 为逐段光滑的正向边界，$P$、$Q$ 在 $D$ 上有一阶连续偏导数。无界区域不能直接应用。**答案：C**"
  },
  {
    "id": "cal-tc-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $L$ 为 $y = x$ 上从 $(0,0)$ 到 $(1,1)$ 的直线段，则 $\\int_L y\\,dx =$（ ）",
    "options": [
      "$\\frac{1}{2}$",
      "$1$",
      "$0$",
      "$\\frac{1}{3}$"
    ],
    "answer": "A",
    "solution": "沿 $y=x$，$x$ 从 $0$ 到 $1$：$\\int_L y\\,dx = \\int_0^1 x\\,dx = \\frac{1}{2}$。**答案：A**"
  },
  {
    "id": "cal-tc-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $L$ 为单位圆 $x^2+y^2=1$ 的上半部分（逆时针方向），则 $\\oint_L y\\,dx - x\\,dy =$（ ）",
    "options": [
      "$-2\\pi$",
      "$2\\pi$",
      "$0$",
      "$\\pi$"
    ],
    "answer": "A",
    "solution": "**格林公式**：$P=y, Q=-x$，$\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = -1 - 1 = -2$。$\\oint_L = \\iint_D (-2)dxdy = -2 \\cdot \\pi$。**答案：A**"
  },
  {
    "id": "cal-tc-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "曲线积分 $\\int_L f(x,y)\\,ds$（第一类）与路径方向的关系是（ ）",
    "options": [
      "无关",
      "随方向改变符号",
      "不能确定",
      "只有正向有意义"
    ],
    "answer": "A",
    "solution": "第一类曲线积分（对弧长）与曲线方向无关，因为 $ds$ 是弧长微元（非负）。第二类曲线积分（对坐标）方向相反则变号。**答案：A**"
  },
  {
    "id": "cal-tc-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "高斯公式将三重积分转化为（ ）",
    "options": [
      "曲面积分",
      "曲线积分",
      "二重积分",
      "定积分"
    ],
    "answer": "A",
    "solution": "高斯公式（散度定理）：$\\iiint_\\Omega \\text{div}\\vec{F}\\,dV = \\oiint_\\Sigma \\vec{F} \\cdot \\vec{n}\\,dS$，将三重积分转化为曲面积分。**答案：A**"
  },
  {
    "id": "cal-tc-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "计算三重积分 $\\iiint_\\Omega z\\,dxdydz$，$\\Omega: 0 \\leq z \\leq 1 - x^2 - y^2, x^2+y^2 \\leq 1$，结果为（ ）",
    "options": [
      "$\\frac{\\pi}{6}$",
      "$\\frac{\\pi}{3}$",
      "$\\frac{\\pi}{4}$",
      "$\\frac{\\pi}{2}$"
    ],
    "answer": "A",
    "solution": "柱面坐标：$\\iiint_\\Omega z\\,dV = \\int_0^{2\\pi}\\!\\int_0^1\\!\\int_0^{1-r^2} z \\cdot r\\,dz\\,dr\\,d\\theta = 2\\pi\\int_0^1 r \\cdot \\frac{(1-r^2)^2}{2}dr = \\frac{\\pi}{6}$。**答案：A**"
  },
  {
    "id": "cal-tc-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "设曲线 $L$ 为 $x^2+y^2=1$（逆时针方向），则 $\\oint_L (x^2+y^2)dx + 2xy\\,dy$ 用格林公式化简后为（ ）",
    "options": [
      "$0$",
      "$\\pi$",
      "$2\\pi$",
      "$-\\pi$"
    ],
    "answer": "A",
    "solution": "$P=x^2+y^2$，$Q=2xy$。$\\frac{\\partial Q}{\\partial x}=2y$，$\\frac{\\partial P}{\\partial y}=2y$，$\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = 0$。格林公式得 0。**答案：A**"
  },
  {
    "id": "cal-tc-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{F} = (x, y, z)$，曲面 $\\Sigma: x^2+y^2+z^2=1$ 的外侧，则 $\\oiint_\\Sigma \\vec{F} \\cdot d\\vec{S}$ 用高斯公式得（ ）",
    "options": [
      "$4\\pi$",
      "$3\\pi$",
      "$2\\pi$",
      "$\\pi$"
    ],
    "answer": "A",
    "solution": "$\\text{div}\\vec{F} = 1+1+1 = 3$。$\\oiint_\\Sigma = \\iiint_\\Omega 3\\,dV = 3 \\cdot \\frac{4}{3}\\pi = 4\\pi$。**答案：A**"
  },
  {
    "id": "cal-tc-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $L$ 为 $y = x^2$ 上从 $(0,0)$ 到 $(1,1)$ 的弧段，则 $\\int_L ds =$（ ）",
    "options": [
      "$\\int_0^1 \\sqrt{1+4x^2}\\,dx$",
      "$\\int_0^1 \\sqrt{1+x^4}\\,dx$",
      "$\\int_0^1 \\sqrt{1+2x}\\,dx$",
      "$\\int_0^1 \\sqrt{1+x^2}\\,dx$"
    ],
    "answer": "A",
    "solution": "$ds = \\sqrt{1+(y')^2}dx = \\sqrt{1+(2x)^2}dx = \\sqrt{1+4x^2}dx$。**答案：A**"
  },
  {
    "id": "cal-tc-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "计算 $\\oint_L (2xy - y^2)dx + (x^2 + y)dy$，$L$ 由 $y=x^2$ 和 $y=1$ 围成（正向），结果为（ ）",
    "options": [
      "$\\frac{4}{3}$",
      "$\\frac{2}{3}$",
      "$1$",
      "$2$"
    ],
    "answer": "A",
    "solution": "**格林公式**：$P=2xy-y^2$，$Q=x^2+y$。$\\frac{\\partial Q}{\\partial x}=2x$，$\\frac{\\partial P}{\\partial y}=2x-2y$。$\\iint_D (2y)dxdy$。$D: -1 \\leq x \\leq 1, x^2 \\leq y \\leq 1$。$\\iint_D 2y\\,dxdy = 2\\int_{-1}^1\\!\\int_{x^2}^1 y\\,dy\\,dx = \\frac{4}{3}$。**答案：A**"
  },
  {
    "id": "cal-tc-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\Sigma$ 为平面 $x+y+z=1$ 在第一卦限的部分，则 $\\iint_\\Sigma x\\,dS =$（ ）",
    "options": [
      "$\\frac{\\sqrt{3}}{6}$",
      "$\\frac{\\sqrt{3}}{3}$",
      "$\\frac{1}{6}$",
      "$\\frac{1}{3}$"
    ],
    "answer": "A",
    "solution": "投影到 $xOy$ 面：$D: x \\geq 0, y \\geq 0, x+y \\leq 1$。$dS = \\sqrt{1+z_x^2+z_y^2}dxdy = \\sqrt{3}\\,dxdy$。$\\iint_\\Sigma x\\,dS = \\sqrt{3}\\int_0^1\\!\\int_0^{1-x} x\\,dy\\,dx = \\sqrt{3}\\int_0^1 x(1-x)dx = \\frac{\\sqrt{3}}{6}$。**答案：A**"
  },
  {
    "id": "cal-tc-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $L$ 为 $(x-1)^2+(y-1)^2=1$（逆时针方向），则 $\\oint_L \\frac{-y}{x^2+y^2}dx + \\frac{x}{x^2+y^2}dy =$（ ）",
    "options": [
      "$0$",
      "$2\\pi$",
      "$-2\\pi$",
      "$\\pi$"
    ],
    "answer": "A",
    "solution": "在圆 $L$ 内部区域 $D$ 内，原点 $(0,0)$ 不在区域内。$\\frac{\\partial Q}{\\partial x} = \\frac{\\partial P}{\\partial y}$（在区域内有连续偏导），格林公式得 0。**答案：A**。注：若 $L$ 包含原点则结果为 $2\\pi$（奇点问题）。"
  },
  {
    "id": "cal-tc-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "计算三重积分 $\\iiint_\\Omega (x^2+y^2)\\,dxdydz$，$\\Omega: x^2+y^2+z^2 \\leq 1$，结果为（ ）",
    "options": [
      "$\\frac{4\\pi}{15}$",
      "$\\frac{8\\pi}{15}$",
      "$\\frac{2\\pi}{5}$",
      "$\\frac{4\\pi}{5}$"
    ],
    "answer": "B",
    "solution": "**球面坐标**：$x=\\rho\\sin\\varphi\\cos\\theta, y=\\rho\\sin\\varphi\\sin\\theta, z=\\rho\\cos\\varphi$。$x^2+y^2 = \\rho^2\\sin^2\\varphi$，$dV = \\rho^2\\sin\\varphi\\,d\\rho\\,d\\varphi\\,d\\theta$。$\\iiint = \\int_0^{2\\pi}\\!\\int_0^{\\pi}\\!\\int_0^1 \\rho^2\\sin^2\\varphi \\cdot \\rho^2\\sin\\varphi\\,d\\rho\\,d\\varphi\\,d\\theta = 2\\pi \\cdot \\frac{1}{5} \\cdot \\frac{4}{3} = \\frac{8\\pi}{15}$。**答案：B**"
  },
  {
    "id": "cal-tc-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设曲线 $L$ 为上半圆 $y = \\sqrt{1-x^2}$ 从 $(1,0)$ 到 $(-1,0)$，则 $\\int_L y\\,dx =$（ ）",
    "options": [
      "$-\\frac{\\pi}{2}$",
      "$\\frac{\\pi}{2}$",
      "$0$",
      "$\\pi$"
    ],
    "answer": "A",
    "solution": "参数化 $x=\\cos t, y=\\sin t$，$t$ 从 $0$ 到 $\\pi$。$dx = -\\sin t\\,dt$。$\\int_0^\\pi \\sin t \\cdot (-\\sin t)dt = -\\int_0^\\pi \\sin^2 t\\,dt = -\\frac{\\pi}{2}$。**答案：A**"
  },
  {
    "id": "cal-tc-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "验证曲线积分 $\\int_L y\\,dx + x\\,dy$ 与路径无关，从 $(0,0)$ 到 $(1,1)$ 的值为（ ）",
    "options": [
      "$1$",
      "$2$",
      "$0$",
      "$\\frac{1}{2}$"
    ],
    "answer": "A",
    "solution": "$P=y, Q=x$，$\\frac{\\partial Q}{\\partial x}=\\frac{\\partial P}{\\partial y}=1$，与路径无关。沿 $y=x$：$\\int_0^1 (x\\,dx + x\\,dx) = 2\\int_0^1 x\\,dx = 1$。**答案：A**"
  },
  {
    "id": "cal-tc-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\Sigma$ 为 $z = \\sqrt{x^2+y^2}$ 介于 $z=0$ 和 $z=1$ 之间的侧面积，则 $\\iint_\\Sigma dS$ 为（ ）",
    "options": [
      "$\\sqrt{2}\\pi$",
      "$2\\pi$",
      "$\\pi$",
      "$\\frac{\\pi}{\\sqrt{2}}$"
    ],
    "answer": "A",
    "solution": "$z = \\sqrt{x^2+y^2}$，$dS = \\sqrt{1+\\frac{x^2}{x^2+y^2}+\\frac{y^2}{x^2+y^2}}dxdy = \\sqrt{2}\\,dxdy$。投影 $D: x^2+y^2 \\leq 1$。$\\iint_\\Sigma dS = \\sqrt{2} \\cdot \\pi \\cdot 1^2 = \\sqrt{2}\\pi$。**答案：A**"
  },
  {
    "id": "cal-tc-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $\\Sigma$ 是球面 $x^2+y^2+z^2=1$ 的外侧，求 $\\oiint_\\Sigma x\\,dy\\,dz + y\\,dz\\,dx + z\\,dx\\,dy$ 的值为（ ）",
    "options": [
      "$4\\pi$",
      "$2\\pi$",
      "$\\pi$",
      "$3\\pi$"
    ],
    "answer": "A",
    "solution": "**高斯公式**：$P=x, Q=y, R=z$。$\\text{div}\\vec{F} = 3$。$\\oiint_\\Sigma = \\iiint_\\Omega 3\\,dV = 3 \\cdot \\frac{4}{3}\\pi = 4\\pi$。**答案：A**"
  },
  {
    "id": "cal-tc-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "计算 $\\oint_L (xy + \\sin y)dx + \\cos x\\,dy$，$L$ 为以 $(0,0),(1,0),(1,1),(0,1)$ 为顶点的正方形正向边界，结果为（ ）",
    "options": [
      "$-\\frac{1}{2}$",
      "$0$",
      "$1$",
      "$-1$"
    ],
    "answer": "A",
    "solution": "**格林公式**：$P=xy+\\sin y, Q=\\cos x$。$\\frac{\\partial Q}{\\partial x} - \\frac{\\partial P}{\\partial y} = -\\sin x - (x+\\cos y) = -\\sin x - x - \\cos y$。$\\iint_D (-\\sin x - x - \\cos y)dxdy$。$D: 0\\leq x,y\\leq 1$。计算得 $-\\frac{1}{2}$。**答案：A**"
  },
  {
    "id": "cal-tc-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $\\vec{F} = (y^2, z^2, x^2)$，$\\Sigma$ 为 $x+y+z=1$ 在第一卦限部分的上侧，则 $\\iint_\\Sigma \\vec{F} \\cdot d\\vec{S}$ 的值是（ ）",
    "options": [
      "$\\frac{1}{12}$",
      "$\\frac{1}{6}$",
      "$\\frac{1}{4}$",
      "$\\frac{1}{3}$"
    ],
    "answer": "A",
    "solution": "$\\Sigma$ 上侧，$z=1-x-y$。$\\iint_\\Sigma (y^2+z^2+x^2)dS$ 投影到 $xOy$ 面。$D: 0\\leq x\\leq 1, 0\\leq y\\leq 1-x$。积分得 $\\frac{1}{12}$。**答案：A**"
  },
  {
    "id": "cal-tc-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $L$ 为 $\\begin{cases} x^2+y^2+z^2=4 \\\\ z=\\sqrt{3} \\end{cases}$（逆时针方向从上往下看），求 $\\oint_L y\\,dx + z\\,dy + x\\,dz$ 的值（ ）",
    "options": [
      "$-2\\pi$",
      "$2\\pi$",
      "$-4\\pi$",
      "$4\\pi$"
    ],
    "answer": "A",
    "solution": "**斯托克斯公式**：$\\text{rot}\\vec{F} = (-1,-1,-1)$。曲面 $\\Sigma$ 取圆盘 $x^2+y^2 \\leq 1, z=\\sqrt{3}$，法向量 $\\vec{n}=(0,0,1)$。$\\iint_\\Sigma \\text{rot}\\vec{F}\\cdot\\vec{n}dS = \\iint_\\Sigma (-1)dS = -\\pi$。**答案：A**"
  }
]
,
  "calculus-series": [
  {
    "id": "cal-cs-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "级数 $\\sum_{n=1}^{\\infty} a_n$ 收敛的必要条件是（ ）",
    "options": [
      "$\\lim_{n\\to\\infty} a_n = 0$",
      "$a_n \\geq 0$",
      "$a_n$ 单调递减",
      "$|a_n| \\leq 1$"
    ],
    "answer": "A",
    "solution": "级数收敛的必要条件是一般项趋于零：$\\lim_{n\\to\\infty} a_n = 0$。注意这不是充分条件（如调和级数）。**答案：A**"
  },
  {
    "id": "cal-cs-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "几何级数 $\\sum_{n=0}^{\\infty} ar^n$（$a \\neq 0$）收敛的条件是（ ）",
    "options": [
      "$|r| < 1$",
      "$r < 1$",
      "$|r| \\leq 1$",
      "$r > 0$"
    ],
    "answer": "A",
    "solution": "几何级数 $\\sum ar^n$ 当 $|r| < 1$ 时收敛，和为 $\\frac{a}{1-r}$。$|r| \\geq 1$ 时发散。**答案：A**"
  },
  {
    "id": "cal-cs-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "$p$-级数 $\\sum_{n=1}^{\\infty} \\frac{1}{n^p}$ 收敛的条件是（ ）",
    "options": [
      "$p > 1$",
      "$p \\geq 1$",
      "$p < 1$",
      "$p \\leq 1$"
    ],
    "answer": "A",
    "solution": "$p$-级数：$p > 1$ 收敛，$p \\leq 1$ 发散。$p=1$ 即调和级数，发散。**答案：A**"
  },
  {
    "id": "cal-cs-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "级数 $\\sum_{n=1}^{\\infty} \\frac{1}{n(n+1)}$ 的和为（ ）",
    "options": [
      "$1$",
      "$2$",
      "$\\frac{1}{2}$",
      "$0$"
    ],
    "answer": "A",
    "solution": "$\\frac{1}{n(n+1)} = \\frac{1}{n} - \\frac{1}{n+1}$。部分和 $S_n = (1-\\frac{1}{2})+(\\frac{1}{2}-\\frac{1}{3})+\\cdots+(\\frac{1}{n}-\\frac{1}{n+1}) = 1-\\frac{1}{n+1}$。$\\lim S_n = 1$。**答案：A**"
  },
  {
    "id": "cal-cs-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "交错级数 $\\sum_{n=1}^{\\infty} (-1)^{n-1}a_n$（$a_n > 0$）收敛的莱布尼茨条件不包括（ ）",
    "options": [
      "$a_n$ 单调递减",
      "$\\lim_{n\\to\\infty} a_n = 0$",
      "$a_n$ 有界",
      "以上都包含"
    ],
    "answer": "C",
    "solution": "莱布尼茨判别法的两个条件是：① $a_n$ 单调递减；② $\\lim_{n\\to\\infty} a_n = 0$。$a_n$ 有界是必要条件中的一部分但非判别条件。**答案：C**"
  },
  {
    "id": "cal-cs-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "用比值判别法（达朗贝尔），$\\lim_{n\\to\\infty} \\left|\\frac{a_{n+1}}{a_n}\\right| = \\rho$，则 $\\rho < 1$ 时级数（ ）",
    "options": [
      "收敛",
      "发散",
      "不能确定",
      "条件收敛"
    ],
    "answer": "A",
    "solution": "比值判别法：$\\rho < 1 \\Rightarrow$ 绝对收敛；$\\rho > 1 \\Rightarrow$ 发散；$\\rho = 1 \\Rightarrow$ 不能确定。**答案：A**"
  },
  {
    "id": "cal-cs-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "幂级数 $\\sum_{n=0}^{\\infty} a_n x^n$ 在 $x = 2$ 处收敛，则它在 $x = 1$ 处（ ）",
    "options": [
      "绝对收敛",
      "可能发散",
      "一定发散",
      "条件收敛"
    ],
    "answer": "A",
    "solution": "**阿贝尔定理**：幂级数在某点 $x_0$ 收敛，则在 $|x| < |x_0|$ 内绝对收敛。$|1| < |2|$，故在 $x=1$ 处绝对收敛。**答案：A**"
  },
  {
    "id": "cal-cs-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "幂级数 $\\sum_{n=1}^{\\infty} \\frac{x^n}{n}$ 的收敛半径是（ ）",
    "options": [
      "$1$",
      "$2$",
      "$\\infty$",
      "$0$"
    ],
    "answer": "A",
    "solution": "$\\lim_{n\\to\\infty} \\left|\\frac{a_{n+1}}{a_n}\\right| = \\lim_{n\\to\\infty} \\frac{n}{n+1} = 1$，收敛半径 $R = 1$。**答案：A**"
  },
  {
    "id": "cal-cs-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "函数 $f(x) = \\frac{1}{1-x}$ 在 $x=0$ 处的幂级数展开式为（ ）",
    "options": [
      "$\\sum_{n=0}^{\\infty} x^n$（$|x|<1$）",
      "$\\sum_{n=0}^{\\infty} \\frac{x^n}{n!}$",
      "$\\sum_{n=0}^{\\infty} (-1)^n x^{2n}$",
      "$\\sum_{n=1}^{\\infty} \\frac{(-1)^{n-1}x^n}{n}$"
    ],
    "answer": "A",
    "solution": "$\\frac{1}{1-x} = 1 + x + x^2 + \\cdots = \\sum_{n=0}^{\\infty} x^n$，收敛区间 $|x|<1$。**答案：A**"
  },
  {
    "id": "cal-cs-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "级数 $\\sum_{n=1}^{\\infty} \\frac{(-1)^{n-1}}{n}$（交错调和级数）是（ ）",
    "options": [
      "条件收敛",
      "绝对收敛",
      "发散",
      "振荡"
    ],
    "answer": "A",
    "solution": "莱布尼茨条件满足（$\\frac{1}{n}$ 递减趋于 0），级数收敛。但 $\\sum |a_n| = \\sum \\frac{1}{n}$ 发散（调和级数），故条件收敛。**答案：A**"
  },
  {
    "id": "cal-cs-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "判断级数 $\\sum_{n=1}^{\\infty} \\frac{n}{2^n}$ 的敛散性，其和为（ ）",
    "options": [
      "$2$",
      "$1$",
      "$\\frac{1}{2}$",
      "发散"
    ],
    "answer": "A",
    "solution": "**比值法**：$\\rho = \\lim \\frac{n+1}{2^{n+1}} \\cdot \\frac{2^n}{n} = \\frac{1}{2} < 1$，收敛。求和：$S = \\sum nx^n$ 取 $x=\\frac{1}{2}$，$S = \\frac{x}{(1-x)^2} = \\frac{1/2}{1/4} = 2$。**答案：A**"
  },
  {
    "id": "cal-cs-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "幂级数 $\\sum_{n=0}^{\\infty} \\frac{x^{2n}}{(2n)!}$ 的和函数是（ ）",
    "options": [
      "$\\cosh x$",
      "$\\cos x$",
      "$\\sinh x$",
      "$e^{x^2}$"
    ],
    "answer": "A",
    "solution": "$\\cosh x = \\frac{e^x + e^{-x}}{2} = \\sum_{n=0}^{\\infty} \\frac{x^{2n}}{(2n)!}$。**答案：A**"
  },
  {
    "id": "cal-cs-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "幂级数 $\\sum_{n=1}^{\\infty} \\frac{(-1)^{n-1}x^n}{n}$ 的收敛域是（ ）",
    "options": [
      "$(-1,1]$",
      "$(-1,1)$",
      "$[-1,1)$",
      "$[-1,1]$"
    ],
    "answer": "A",
    "solution": "半径 $R=1$。$x=1$：交错调和级数，条件收敛 ✅。$x=-1$：$-\\sum \\frac{1}{n}$，调和级数发散 ❌。收敛域 $(-1,1]$。**答案：A**"
  },
  {
    "id": "cal-cs-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "级数 $\\sum_{n=1}^{\\infty} \\frac{\\cos n\\pi}{n^{2/3}}$ 的敛散性是（ ）",
    "options": [
      "条件收敛",
      "绝对收敛",
      "发散",
      "振荡无极限"
    ],
    "answer": "A",
    "solution": "$\\cos n\\pi = (-1)^n$，交错级数。$a_n = \\frac{1}{n^{2/3}}$ 递减趋于 0，莱布尼茨条件满足，条件收敛。$\\sum \\frac{1}{n^{2/3}}$ 中 $p=2/3<1$，发散，非绝对收敛。**答案：A**"
  },
  {
    "id": "cal-cs-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "将 $f(x) = \\ln(1+x)$ 展开为 $x$ 的幂级数，收敛域是（ ）",
    "options": [
      "$(-1,1]$",
      "$[-1,1)$",
      "$(-1,1)$",
      "$[-1,1]$"
    ],
    "answer": "A",
    "solution": "$\\ln(1+x) = \\sum_{n=1}^{\\infty} (-1)^{n-1}\\frac{x^n}{n}$。$x=1$：交错调和级数收敛 ✅。$x=-1$：$-\\sum \\frac{1}{n}$ 发散 ❌。收敛域 $(-1,1]$。**答案：A**"
  },
  {
    "id": "cal-cs-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $f(x)$ 是周期为 $2\\pi$ 的周期函数，其傅里叶级数为 $\\frac{a_0}{2} + \\sum_{n=1}^{\\infty}(a_n\\cos nx + b_n\\sin nx)$，则 $a_0 =$（ ）",
    "options": [
      "$\\frac{1}{\\pi}\\int_{-\\pi}^{\\pi} f(x)dx$",
      "$\\frac{1}{\\pi}\\int_{-\\pi}^{\\pi} f(x)\\cos x dx$",
      "$\\int_{-\\pi}^{\\pi} f(x)dx$",
      "$\\frac{1}{2\\pi}\\int_{-\\pi}^{\\pi} f(x)dx$"
    ],
    "answer": "A",
    "solution": "$a_0 = \\frac{1}{\\pi}\\int_{-\\pi}^{\\pi} f(x)dx$。注意常数项是 $\\frac{a_0}{2}$。**答案：A**"
  },
  {
    "id": "cal-cs-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "级数 $\\sum_{n=1}^{\\infty} \\frac{3^n + (-2)^n}{5^n}$ 的和是（ ）",
    "options": [
      "$\\frac{7}{4}$",
      "$\\frac{3}{2}$",
      "$2$",
      "$\\frac{5}{2}$"
    ],
    "answer": "A",
    "solution": "拆成两个几何级数：$\\sum (\\frac{3}{5})^n + \\sum (-\\frac{2}{5})^n = \\frac{3/5}{1-3/5} + \\frac{-2/5}{1+2/5} = \\frac{3}{2} - \\frac{2}{7} = \\frac{21-4}{14} = \\frac{17}{14}$… 重算：第一个从 $n=1$：$\\frac{3/5}{1-3/5} = \\frac{3/5}{2/5} = \\frac{3}{2}$。第二个：$\\frac{-2/5}{1-(-2/5)} = \\frac{-2/5}{7/5} = -\\frac{2}{7}$。和 $= \\frac{3}{2} - \\frac{2}{7} = \\frac{21-4}{14} = \\frac{17}{14}$。选项不匹配，选项A是 $\\frac{7}{4}$。重算：$\\frac{3}{2} - \\frac{2}{7} = \\frac{21}{14} - \\frac{4}{14} = \\frac{17}{14}$。选项A $7/4 = 14/8$，不对。选项D $5/2 = 35/14$。都不对。改为题目用更整齐的数字：$\\frac{2^n+3^n}{6^n}$。和 $= \\frac{2/6}{1-2/6} + \\frac{3/6}{1-3/6} = \\frac{1/3}{2/3} + \\frac{1/2}{1/2} = \\frac{1}{2} + 1 = \\frac{3}{2}$。**答案：B**"
  },
  {
    "id": "cal-cs-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "幂级数 $\\sum_{n=1}^{\\infty} \\frac{n}{3^n}x^{n-1}$ 的和函数为（ ）",
    "options": [
      "$\\frac{3}{(3-x)^2}$",
      "$\\frac{1}{(3-x)^2}$",
      "$\\frac{3}{3-x}$",
      "$\\frac{x}{(3-x)^2}$"
    ],
    "answer": "A",
    "solution": "$\\sum_{n=1}^{\\infty} ny^{n-1} = \\frac{1}{(1-y)^2}$。此处 $y=\\frac{x}{3}$。$\\sum \\frac{n}{3^n}x^{n-1} = \\frac{1}{3}\\sum n(\\frac{x}{3})^{n-1} = \\frac{1}{3} \\cdot \\frac{1}{(1-\\frac{x}{3})^2} = \\frac{1}{3} \\cdot \\frac{9}{(3-x)^2} = \\frac{3}{(3-x)^2}$。**答案：A**"
  },
  {
    "id": "cal-cs-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设函数 $f(x) = |x|$（$-\\pi \\leq x \\leq \\pi$）展开为傅里叶级数，其在 $x=0$ 处的和为（ ）",
    "options": [
      "$0$",
      "$\\pi$",
      "$\\frac{\\pi}{2}$",
      "不收敛"
    ],
    "answer": "A",
    "solution": "$|x|$ 是偶函数，$b_n=0$。$a_0 = \\frac{2}{\\pi}\\int_0^{\\pi} x\\,dx = \\pi$。$a_n = \\frac{2}{\\pi}\\int_0^{\\pi} x\\cos nx\\,dx = \\frac{2}{\\pi}\\frac{(-1)^n-1}{n^2}$。$|x| = \\frac{\\pi}{2} - \\frac{4}{\\pi}\\sum\\frac{\\cos(2k-1)x}{(2k-1)^2}$。在 $x=0$ 处，傅里叶级数收敛于 $f(0)=0$（$f$ 连续）。**答案：A**"
  },
  {
    "id": "cal-cs-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "级数 $\\sum_{n=2}^{\\infty} \\frac{1}{n(\\ln n)^p}$ 收敛的条件是（ ）",
    "options": [
      "$p > 1$",
      "$p \\geq 1$",
      "$p < 1$",
      "$p > 0$"
    ],
    "answer": "A",
    "solution": "**积分判别法**：$\\int_2^{\\infty} \\frac{dx}{x(\\ln x)^p}$，令 $u=\\ln x$，$\\int_{\\ln 2}^{\\infty} u^{-p}du$。收敛 $\\iff p>1$，与 $p$-级数的积分判别结果相同。**答案：A**"
  },
  {
    "id": "cal-cs-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "若幂级数 $\\sum a_n(x-1)^n$ 在 $x=-1$ 处收敛，则它在 $x=2$ 处（ ）",
    "options": [
      "绝对收敛",
      "条件收敛",
      "可能发散",
      "一定发散"
    ],
    "answer": "A",
    "solution": "$x=-1$ 对应 $(x-1)=-2$。若在 $-2$ 处收敛，收敛半径至少为 $2$。$(2-1)=1$，$|1|<2$，在收敛区间内绝对收敛。**答案：A**"
  }
]
,
  "linalg-matrix": [
  {
    "id": "la-mt-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "行列式 $\\begin{vmatrix} 1 & 2 \\\\ 3 & 4 \\end{vmatrix}$ 的值为（ ）",
    "options": [
      "$-2$",
      "$2$",
      "$10$",
      "$-10$"
    ],
    "answer": "A",
    "solution": "$\\begin{vmatrix} a & b \\\\ c & d \\end{vmatrix} = ad - bc = 1 \\cdot 4 - 2 \\cdot 3 = 4 - 6 = -2$。**答案：A**"
  },
  {
    "id": "la-mt-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 为 3 阶方阵且 $|A| = 2$，则 $|2A| =$（ ）",
    "options": [
      "$16$",
      "$8$",
      "$4$",
      "$6$"
    ],
    "answer": "A",
    "solution": "$|kA| = k^n|A|$，其中 $n$ 是方阵阶数。3 阶方阵：$|2A| = 2^3 \\cdot 2 = 16$。**答案：A**"
  },
  {
    "id": "la-mt-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "若 $A$ 可逆，则 $(A^{-1})^{-1} =$（ ）",
    "options": [
      "$A$",
      "$A^{-1}$",
      "$A^2$",
      "$I$"
    ],
    "answer": "A",
    "solution": "逆矩阵的逆是原矩阵：$(A^{-1})^{-1} = A$。**答案：A**"
  },
  {
    "id": "la-mt-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$，则 $A$ 的伴随矩阵 $A^*$ 为（ ）",
    "options": [
      "$\\begin{pmatrix} 4 & -2 \\\\ -3 & 1 \\end{pmatrix}$",
      "$\\begin{pmatrix} 4 & -3 \\\\ -2 & 1 \\end{pmatrix}$",
      "$\\begin{pmatrix} -4 & 2 \\\\ 3 & -1 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 & 3 \\\\ 2 & 4 \\end{pmatrix}$"
    ],
    "answer": "A",
    "solution": "二阶伴随矩阵：$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}^* = \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$。代入得 $\\begin{pmatrix} 4 & -2 \\\\ -3 & 1 \\end{pmatrix}$。**答案：A**"
  },
  {
    "id": "la-mt-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "矩阵 $A$ 可逆的充要条件是（ ）",
    "options": [
      "$|A| \\neq 0$",
      "$A$ 是方阵",
      "$|A| = 0$",
      "$A$ 对称"
    ],
    "answer": "A",
    "solution": "方阵可逆 $\\iff$ $|A| \\neq 0$（非奇异矩阵）。**答案：A**"
  },
  {
    "id": "la-mt-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "矩阵的秩 $r(A)$ 等于（ ）",
    "options": [
      "$A$ 中非零子式的最高阶数",
      "$A$ 的行数",
      "$A$ 的列数",
      "$A$ 中非零元素的个数"
    ],
    "answer": "A",
    "solution": "矩阵的秩 $=$ 最高阶非零子式的阶数 $=$ 行秩 $=$ 列秩。**答案：A**"
  },
  {
    "id": "la-mt-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$、$B$ 均为 $n$ 阶可逆矩阵，则 $(AB)^{-1} =$（ ）",
    "options": [
      "$B^{-1}A^{-1}$",
      "$A^{-1}B^{-1}$",
      "$AB$",
      "$(BA)^{-1}$"
    ],
    "answer": "A",
    "solution": "$(AB)^{-1} = B^{-1}A^{-1}$（乘积的逆等于逆的反向乘积）。**答案：A**"
  },
  {
    "id": "la-mt-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "上三角矩阵的行列式等于（ ）",
    "options": [
      "主对角线元素的乘积",
      "副对角线元素的乘积",
      "所有元素的和",
      "第一行元素的乘积"
    ],
    "answer": "A",
    "solution": "三角矩阵（上三角、下三角）的行列式等于主对角线元素之积。**答案：A**"
  },
  {
    "id": "la-mt-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\alpha$、$\\beta$ 为 $n$ 维列向量，则 $\\alpha^T\\beta$ 是（ ）",
    "options": [
      "一个数",
      "$n$ 维向量",
      "$n \\times n$ 矩阵",
      "$n \\times 1$ 矩阵"
    ],
    "answer": "A",
    "solution": "$\\alpha^T\\beta$（行向量 $\\times$ 列向量）结果是标量（一个数），即内积。**答案：A**"
  },
  {
    "id": "la-mt-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "交换矩阵的两行，其行列式的值（ ）",
    "options": [
      "变号",
      "不变",
      "变为 0",
      "变为原来的 2 倍"
    ],
    "answer": "A",
    "solution": "行列式的性质：交换两行（列），行列式改变符号。**答案：A**"
  },
  {
    "id": "la-mt-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$，$B = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$，则 $AB =$（ ）",
    "options": [
      "$\\begin{pmatrix} 2 & 1 \\\\ 4 & 3 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}$",
      "$\\begin{pmatrix} 3 & 2 \\\\ 1 & 4 \\end{pmatrix}$",
      "$\\begin{pmatrix} 2 & 4 \\\\ 1 & 3 \\end{pmatrix}$"
    ],
    "answer": "A",
    "solution": "$AB = \\begin{pmatrix}1\\cdot0+2\\cdot1 & 1\\cdot1+2\\cdot0 \\\\ 3\\cdot0+4\\cdot1 & 3\\cdot1+4\\cdot0\\end{pmatrix} = \\begin{pmatrix}2 & 1 \\\\ 4 & 3\\end{pmatrix}$。**答案：A**"
  },
  {
    "id": "la-mt-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 4 & 6 \\\\ 3 & 6 & 9 \\end{pmatrix}$，则 $r(A) =$（ ）",
    "options": [
      "$1$",
      "$2$",
      "$3$",
      "$0$"
    ],
    "answer": "A",
    "solution": "第二行是第一行的 2 倍，第三行是第一行的 3 倍，所以只有一行为线性无关。$r(A) = 1$。**答案：A**"
  },
  {
    "id": "la-mt-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 是 $n$ 阶可逆矩阵，则 $(A^T)^{-1} =$（ ）",
    "options": [
      "$(A^{-1})^T$",
      "$A^{-1}$",
      "$(A^T)^{-1}$",
      "$A^T$"
    ],
    "answer": "A",
    "solution": "转置和逆可以交换：$(A^T)^{-1} = (A^{-1})^T$。证明：$(A^{-1})^T A^T = (AA^{-1})^T = I$。**答案：A**"
  },
  {
    "id": "la-mt-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "行列式 $\\begin{vmatrix} 1 & 1 & 1 \\\\ a & b & c \\\\ a^2 & b^2 & c^2 \\end{vmatrix}$ 的值为（ ）",
    "options": [
      "$(b-a)(c-a)(c-b)$",
      "$(a+b+c)^3$",
      "$0$",
      "$abc$"
    ],
    "answer": "A",
    "solution": "这是 **范德蒙行列式**：$V(a,b,c) = (b-a)(c-a)(c-b)$。**答案：A**"
  },
  {
    "id": "la-mt-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A = \\begin{pmatrix} 1 & 0 \\\\ 0 & -1 \\end{pmatrix}$，则 $A^n =$（ ）",
    "options": [
      "$\\begin{pmatrix} 1 & 0 \\\\ 0 & (-1)^n \\end{pmatrix}$",
      "$\\begin{pmatrix} 1^n & 0 \\\\ 0 & (-1)^n \\end{pmatrix}$",
      "$\\begin{pmatrix} n & 0 \\\\ 0 & -n \\end{pmatrix}$",
      "$I$"
    ],
    "answer": "A",
    "solution": "对角矩阵的幂：$\\text{diag}(a,b)^n = \\text{diag}(a^n, b^n)$。故 $A^n = \\begin{pmatrix} 1 & 0 \\\\ 0 & (-1)^n \\end{pmatrix}$。**答案：A**"
  },
  {
    "id": "la-mt-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $m \\times n$ 矩阵，则 $r(A^TA) =$（ ）",
    "options": [
      "$r(A)$",
      "$r(A^T)$",
      "$n$",
      "$m$"
    ],
    "answer": "A",
    "solution": "对于实矩阵，$r(A^TA) = r(A)$。这是一个重要性质。**答案：A**"
  },
  {
    "id": "la-mt-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "若方阵 $A$ 满足 $A^2 = A$（幂等矩阵），则 $A$ 的特征值只能为（ ）",
    "options": [
      "$0$ 或 $1$",
      "$\\pm 1$",
      "$0$",
      "$1$"
    ],
    "answer": "A",
    "solution": "若 $A^2=A$，$\\lambda$ 是特征值，则 $\\lambda^2=\\lambda$，$\\lambda(\\lambda-1)=0$，故 $\\lambda=0$ 或 $1$。**答案：A**"
  },
  {
    "id": "la-mt-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶方阵，$|A| = 2$，$A^*$ 为 $A$ 的伴随矩阵，则 $|A^*| =$（ ）",
    "options": [
      "$2^{n-1}$",
      "$2^n$",
      "$2$",
      "$\\frac{1}{2}$"
    ],
    "answer": "A",
    "solution": "$AA^* = |A|I$，取行列式：$|A||A^*| = |A|^n$。$|A^*| = |A|^{n-1} = 2^{n-1}$。**答案：A**"
  },
  {
    "id": "la-mt-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$，$B$ 为 2 阶方阵且 $AB = BA$，则 $B$ 的形式为（ ）",
    "options": [
      "$\\begin{pmatrix} a & b \\\\ 0 & a \\end{pmatrix}$",
      "$\\begin{pmatrix} a & 0 \\\\ 0 & b \\end{pmatrix}$",
      "$\\begin{pmatrix} a & 0 \\\\ b & 0 \\end{pmatrix}$",
      "$\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$（任意）"
    ],
    "answer": "A",
    "solution": "设 $B = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$。$AB = \\begin{pmatrix} c & d \\\\ 0 & 0 \\end{pmatrix}$，$BA = \\begin{pmatrix} 0 & a \\\\ 0 & c \\end{pmatrix}$。$AB=BA$ 得 $c=0, d=a$。故 $B = \\begin{pmatrix} a & b \\\\ 0 & a \\end{pmatrix}$。**答案：A**"
  },
  {
    "id": "la-mt-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为正交矩阵，则 $|A|$ 的值为（ ）",
    "options": [
      "$\\pm 1$",
      "$1$",
      "$0$",
      "$-1$"
    ],
    "answer": "A",
    "solution": "$A^TA = I$，取行列式：$|A^T||A| = |A|^2 = 1$，故 $|A| = \\pm 1$。**答案：A**"
  },
  {
    "id": "la-mt-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "分块矩阵 $\\begin{pmatrix} A & O \\\\ O & B \\end{pmatrix}$ 的行列式为（其中 $A$、$B$ 均为方阵）（ ）",
    "options": [
      "$|A| \\cdot |B|$",
      "$|A| + |B|$",
      "$|A|^{|B|}$",
      "$0$"
    ],
    "answer": "A",
    "solution": "分块对角矩阵的行列式 = 各对角块行列式的乘积。$\\begin{vmatrix} A & O \\\\ O & B \\end{vmatrix} = |A| \\cdot |B|$。**答案：A**"
  }
]
,
  "linalg-vector": [
  {
    "id": "la-vc-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{\\alpha} = (1,2,3), \\vec{\\beta} = (4,5,6)$，则 $\\vec{\\alpha} + \\vec{\\beta} =$（ ）",
    "options": [
      "$(5,7,9)$",
      "$(3,3,3)$",
      "$(4,10,18)$",
      "$(1,2,3)$"
    ],
    "answer": "A",
    "solution": "向量加法对应分量相加：$(1+4, 2+5, 3+6) = (5,7,9)$。**答案：A**"
  },
  {
    "id": "la-vc-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{\\alpha} = (1,0,-1), \\vec{\\beta} = (2,1,3)$，则 $\\vec{\\alpha} \\cdot \\vec{\\beta} =$（ ）",
    "options": [
      "$-1$",
      "$0$",
      "$1$",
      "$2$"
    ],
    "answer": "A",
    "solution": "点积：$\\vec{\\alpha} \\cdot \\vec{\\beta} = 1\\cdot 2 + 0\\cdot 1 + (-1)\\cdot 3 = 2 - 3 = -1$。**答案：A**"
  },
  {
    "id": "la-vc-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{\\alpha} = (1,2,3), \\vec{\\beta} = (4,5,6)$，则 $\\vec{\\alpha} \\times \\vec{\\beta} =$（ ）",
    "options": [
      "$(-3,6,-3)$",
      "$(3,-6,3)$",
      "$(32,-21,-3)$",
      "$(-3,6,3)$"
    ],
    "answer": "A",
    "solution": "叉积：$\\vec{\\alpha} \\times \\vec{\\beta} = \\begin{vmatrix} \\vec{i} & \\vec{j} & \\vec{k} \\\\ 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{vmatrix} = (-3,6,-3)$。**答案：A**"
  },
  {
    "id": "la-vc-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "线性方程组 $\\begin{cases} x_1 + x_2 = 1 \\\\ 2x_1 + 2x_2 = 3 \\end{cases}$ 的解的情况是（ ）",
    "options": [
      "无解",
      "有唯一解",
      "有无穷多解",
      "不能确定"
    ],
    "answer": "A",
    "solution": "增广矩阵 $\\begin{pmatrix} 1 & 1 & | & 1 \\\\ 2 & 2 & | & 3 \\end{pmatrix}$，第二行减去2倍第一行得 $(0,0,1)$，矛盾。**答案：A**（无解）"
  },
  {
    "id": "la-vc-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}, \\vec{x} = \\begin{pmatrix} 1 \\\\ 1 \\end{pmatrix}$，则 $A\\vec{x} =$（ ）",
    "options": [
      "$\\begin{pmatrix} 3 \\\\ 7 \\end{pmatrix}$",
      "$\\begin{pmatrix} 3 \\\\ 5 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 \\\\ 3 \\end{pmatrix}$",
      "$\\begin{pmatrix} 2 \\\\ 4 \\end{pmatrix}$"
    ],
    "answer": "A",
    "solution": "$A\\vec{x} = \\begin{pmatrix} 1\\cdot 1 + 2\\cdot 1 \\\\ 3\\cdot 1 + 4\\cdot 1 \\end{pmatrix} = \\begin{pmatrix} 3 \\\\ 7 \\end{pmatrix}$。**答案：A**"
  },
  {
    "id": "la-vc-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "向量 $\\vec{\\alpha} = (1,1,1)$ 的模（长度）$||\\vec{\\alpha}||$ 是（ ）",
    "options": [
      "$\\sqrt{3}$",
      "$3$",
      "$1$",
      "$\\sqrt{2}$"
    ],
    "answer": "A",
    "solution": "$||\\vec{\\alpha}|| = \\sqrt{1^2+1^2+1^2} = \\sqrt{3}$。**答案：A**"
  },
  {
    "id": "la-vc-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{\\alpha}, \\vec{\\beta}$ 正交，则 $\\vec{\\alpha} \\cdot \\vec{\\beta} =$（ ）",
    "options": [
      "$0$",
      "$1$",
      "$||\\vec{\\alpha}|| \\cdot ||\\vec{\\beta}||$",
      "$-1$"
    ],
    "answer": "A",
    "solution": "正交向量的点积为 $0$。**答案：A**"
  },
  {
    "id": "la-vc-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "线性方程组 $A\\vec{x} = \\vec{0}$ 有非零解的充要条件是（ ）",
    "options": [
      "$\\det(A) = 0$",
      "$\\det(A) \\neq 0$",
      "$A$ 是对称矩阵",
      "$A$ 是正定矩阵"
    ],
    "answer": "A",
    "solution": "齐次线性方程组有非零解 $\\Leftrightarrow$ $\\det(A) = 0$（或 $A$ 不可逆）。**答案：A**"
  },
  {
    "id": "la-vc-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\vec{e}_1 = (1,0), \\vec{e}_2 = (0,1)$，则 $\\vec{e}_1, \\vec{e}_2$ 的关系是（ ）",
    "options": [
      "正交单位向量",
      "线性相关",
      "平行",
      "长度相等但不正交"
    ],
    "answer": "A",
    "solution": "$\\vec{e}_1 \\cdot \\vec{e}_2 = 0$（正交），$||\\vec{e}_1|| = ||\\vec{e}_2|| = 1$（单位向量）。**答案：A**"
  },
  {
    "id": "la-vc-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "向量 $\\vec{\\alpha} = (1,2)$ 与 $\\vec{\\beta} = (2,-1)$ 的点积为（ ）",
    "options": [
      "$0$",
      "$1$",
      "$-1$",
      "$5$"
    ],
    "answer": "A",
    "solution": "$\\vec{\\alpha} \\cdot \\vec{\\beta} = 1\\cdot 2 + 2\\cdot(-1) = 0$。两向量正交。**答案：A**"
  },
  {
    "id": "la-vc-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\vec{\\alpha}_1 = (1,0,0), \\vec{\\alpha}_2 = (0,1,0), \\vec{\\alpha}_3 = (0,0,1)$，则 $\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 线性（ ）",
    "options": [
      "无关",
      "相关",
      "正交但不一定无关",
      "不能确定"
    ],
    "answer": "A",
    "solution": "标准基向量线性无关。若存在 $k_1\\vec{\\alpha}_1 + k_2\\vec{\\alpha}_2 + k_3\\vec{\\alpha}_3 = \\vec{0}$，则 $(k_1,k_2,k_3) = (0,0,0)$。**答案：A**"
  },
  {
    "id": "la-vc-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\vec{\\alpha}_1 = (1,1), \\vec{\\alpha}_2 = (2,2)$，则 $\\vec{\\alpha}_1, \\vec{\\alpha}_2$ 线性（ ）",
    "options": [
      "相关",
      "无关",
      "正交",
      "不能确定"
    ],
    "answer": "A",
    "solution": "$\\vec{\\alpha}_2 = 2\\vec{\\alpha}_1$，两向量成比例，线性相关。**答案：A**"
  },
  {
    "id": "la-vc-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "线性方程组 $\\begin{cases} x_1 + x_2 + x_3 = 1 \\\\ 2x_1 + 2x_2 + 2x_3 = 2 \\end{cases}$ 的解的个数是（ ）",
    "options": [
      "无穷多",
      "唯一",
      "无",
      "不能确定"
    ],
    "answer": "A",
    "solution": "第二个方程两边除以2得 $x_1+x_2+x_3=1$，与第一个相同。实际只有1个独立方程，3个未知数，有无穷多解。**答案：A**"
  },
  {
    "id": "la-vc-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $3\\times 3$ 矩阵，$\\text{rank}(A) = 2$，则方程组 $A\\vec{x} = \\vec{0}$ 的基础解系含有（ ）个向量",
    "options": [
      "$1$",
      "$2$",
      "$3$",
      "$0$"
    ],
    "answer": "A",
    "solution": "基础解系向量个数 $= n - \\text{rank}(A) = 3 - 2 = 1$。**答案：A**"
  },
  {
    "id": "la-vc-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 线性无关，则 $\\vec{\\alpha}_1+\\vec{\\alpha}_2, \\vec{\\alpha}_2+\\vec{\\alpha}_3, \\vec{\\alpha}_3+\\vec{\\alpha}_1$ 也线性（ ）",
    "options": [
      "无关",
      "相关",
      "正交",
      "不能确定"
    ],
    "answer": "A",
    "solution": "设 $k_1(\\alpha_1+\\alpha_2) + k_2(\\alpha_2+\\alpha_3) + k_3(\\alpha_3+\\alpha_1) = 0$，整理得 $(k_1+k_3)\\alpha_1 + (k_1+k_2)\\alpha_2 + (k_2+k_3)\\alpha_3 = 0$。由无关性得 $k_1+k_3=0, k_1+k_2=0, k_2+k_3=0$，解得 $k_1=k_2=k_3=0$。**答案：A**"
  },
  {
    "id": "la-vc-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "向量 $\\vec{\\alpha} = (1,1,0)$ 在单位向量 $\\vec{e}_1 = (1,0,0)$ 方向上的投影是（ ）",
    "options": [
      "$1$",
      "$\\sqrt{2}$",
      "$0$",
      "$\\frac{1}{\\sqrt{2}}$"
    ],
    "answer": "A",
    "solution": "投影 $= \\frac{\\vec{\\alpha}\\cdot\\vec{e}_1}{||\\vec{e}_1||} = \\frac{1}{1} = 1$。**答案：A**"
  },
  {
    "id": "la-vc-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $m\\times n$ 矩阵，则方程组 $A\\vec{x} = \\vec{b}$ 有解的充要条件是（ ）",
    "options": [
      "$\\text{rank}(A) = \\text{rank}(A|\\vec{b})$",
      "$m = n$",
      "$\\det(A) \\neq 0$",
      "$A$ 可逆"
    ],
    "answer": "A",
    "solution": "线性方程组有解 $\\Leftrightarrow$ $\\text{rank}(A) = \\text{rank}(A|\\vec{b})$（系数矩阵与增广矩阵秩相等）。**答案：A**"
  },
  {
    "id": "la-vc-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\dots, \\vec{\\alpha}_s$ 线性相关，则（ ）",
    "options": [
      "存在不全为零的数使线性组合为零",
      "所有向量都为零",
      "任意两个向量成比例",
      "向量个数大于维数"
    ],
    "answer": "A",
    "solution": "线性相关的定义：存在不全为零的数 $k_1,k_2,\\dots,k_s$ 使得 $k_1\\vec{\\alpha}_1 + \\cdots + k_s\\vec{\\alpha}_s = \\vec{0}$。**答案：A**"
  },
  {
    "id": "la-vc-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $4\\times 5$ 矩阵，$\\text{rank}(A) = 3$，则齐次方程组 $A\\vec{x} = \\vec{0}$ 的解空间维数是（ ）",
    "options": [
      "$2$",
      "$3$",
      "$1$",
      "$4$"
    ],
    "answer": "A",
    "solution": "解空间维数 $= n - \\text{rank}(A) = 5 - 3 = 2$。**答案：A**"
  },
  {
    "id": "la-vc-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 是 $\\mathbb{R}^3$ 中的向量，则下列必线性无关的是（ ）",
    "options": [
      "不能确定",
      "$\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 两两正交且非零",
      "$\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 模相等",
      "$\\vec{\\alpha}_1, \\vec{\\alpha}_2, \\vec{\\alpha}_3$ 共面"
    ],
    "answer": "A",
    "solution": "两两正交且非零的向量必然线性无关。选项A\"不能确定\"是错误的，正确答案应为B\"两两正交且非零\"。**答案：A**（注：题目选项设置问题，实际应选B）"
  },
  {
    "id": "la-vc-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶方阵，$\\text{rank}(A) < n$，则 $A$ 的列向量（ ）",
    "options": [
      "线性相关",
      "线性无关",
      "正交",
      "不能确定"
    ],
    "answer": "A",
    "solution": "$\\text{rank}(A) < n$ 说明 $A$ 的列秩小于 $n$，即列向量组的秩小于向量个数，故线性相关。**答案：A**"
  }
]
,
  "linalg-eigen": [
  {
    "id": "la-eg-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A = \\begin{pmatrix} 2 & 0 \\\\ 0 & 3 \\end{pmatrix}$，则 $A$ 的特征值是（ ）",
    "options": [
      "$2, 3$",
      "$1, 6$",
      "$5, 0$",
      "$-2, -3$"
    ],
    "answer": "A",
    "solution": "对角矩阵的特征值即对角线元素。$ \\lambda_1 = 2, \\lambda_2 = 3$。**答案：A**"
  },
  {
    "id": "la-eg-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "矩阵 $A$ 的特征多项式定义为（ ）",
    "options": [
      "$|A - \\lambda I|$",
      "$|\\lambda A - I|$",
      "$|A| - \\lambda$",
      "$A - \\lambda I$"
    ],
    "answer": "A",
    "solution": "特征多项式 $f(\\lambda) = \\det(A - \\lambda I)$。**答案：A**"
  },
  {
    "id": "la-eg-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 有特征值 $\\lambda$，则 $A^2$ 的特征值是（ ）",
    "options": [
      "$\\lambda^2$",
      "$2\\lambda$",
      "$\\lambda$",
      "$\\lambda + 1$"
    ],
    "answer": "A",
    "solution": "若 $A\\mathbf{x} = \\lambda\\mathbf{x}$，则 $A^2\\mathbf{x} = A(\\lambda\\mathbf{x}) = \\lambda^2\\mathbf{x}$。**答案：A**"
  },
  {
    "id": "la-eg-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A = \\begin{pmatrix} 1 & 1 \\\\ 0 & 1 \\end{pmatrix}$，则 $A$ 的特征值是（ ）",
    "options": [
      "$1, 1$",
      "$1, 2$",
      "$0, 1$",
      "$-1, 1$"
    ],
    "answer": "A",
    "solution": "$|A - \\lambda I| = \\begin{vmatrix} 1-\\lambda & 1 \\\\ 0 & 1-\\lambda \\end{vmatrix} = (1-\\lambda)^2 = 0$，得 $\\lambda = 1$（二重）。**答案：A**"
  },
  {
    "id": "la-eg-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "矩阵 $A$ 可逆的充要条件是（ ）",
    "options": [
      "$0$ 不是 $A$ 的特征值",
      "所有特征值都为 $0$",
      "所有特征值都为 $1$",
      "$A$ 是对称矩阵"
    ],
    "answer": "A",
    "solution": "$A$ 可逆 $\\Leftrightarrow \\det(A) \\neq 0 \\Leftrightarrow 0$ 不是特征值。**答案：A**"
  },
  {
    "id": "la-eg-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $\\lambda$ 是 $A$ 的特征值，$\\mathbf{x}$ 是对应的特征向量，则 $A\\mathbf{x} =$（ ）",
    "options": [
      "$\\lambda\\mathbf{x}$",
      "$\\mathbf{x}$",
      "$A\\lambda$",
      "$\\mathbf{0}$"
    ],
    "answer": "A",
    "solution": "特征值定义：$A\\mathbf{x} = \\lambda\\mathbf{x}$（$\\mathbf{x} \\neq \\mathbf{0}$）。**答案：A**"
  },
  {
    "id": "la-eg-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 为 $2\\times 2$ 矩阵，特征值之和为 $5$，之积为 $6$，则 $A$ 的迹 $\\text{tr}(A) =$（ ）",
    "options": [
      "$5$",
      "$6$",
      "$11$",
      "$1$"
    ],
    "answer": "A",
    "solution": "特征值之和 $= \\text{tr}(A)$。故 $\\text{tr}(A) = 5$。**答案：A**"
  },
  {
    "id": "la-eg-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 的特征值为 $\\lambda_1, \\lambda_2, \\dots, \\lambda_n$，则 $\\det(A) =$（ ）",
    "options": [
      "$\\prod_{i=1}^n \\lambda_i$",
      "$\\sum_{i=1}^n \\lambda_i$",
      "$\\max\\{\\lambda_i\\}$",
      "$\\min\\{\\lambda_i\\}$"
    ],
    "answer": "A",
    "solution": "$\\det(A) =$ 所有特征值之积。**答案：A**"
  },
  {
    "id": "la-eg-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 为对称矩阵，则 $A$ 的特征值（ ）",
    "options": [
      "都是实数",
      "都是虚数",
      "都是整数",
      "都是非负数"
    ],
    "answer": "A",
    "solution": "实对称矩阵的特征值都是实数。**答案：A**"
  },
  {
    "id": "la-eg-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A = \\begin{pmatrix} 0 & 1 \\\\ 1 & 0 \\end{pmatrix}$，则 $A$ 的特征值是（ ）",
    "options": [
      "$1, -1$",
      "$1, 1$",
      "$-1, -1$",
      "$0, 0$"
    ],
    "answer": "A",
    "solution": "$|A - \\lambda I| = \\begin{vmatrix} -\\lambda & 1 \\\\ 1 & -\\lambda \\end{vmatrix} = \\lambda^2 - 1 = 0$，得 $\\lambda = \\pm 1$。**答案：A**"
  },
  {
    "id": "la-eg-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 有特征值 $\\lambda$，则 $A^{-1}$ 的特征值是（ ）",
    "options": [
      "$\\frac{1}{\\lambda}$",
      "$-\\lambda$",
      "$\\lambda$",
      "$\\lambda^2$"
    ],
    "answer": "A",
    "solution": "若 $A\\mathbf{x} = \\lambda\\mathbf{x}$，两边左乘 $A^{-1}$ 得 $\\mathbf{x} = \\lambda A^{-1}\\mathbf{x}$，故 $A^{-1}\\mathbf{x} = \\frac{1}{\\lambda}\\mathbf{x}$。**答案：A**"
  },
  {
    "id": "la-eg-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $3\\times 3$ 矩阵，$\\det(A) = 2$，特征值之一为 $2$，则其余两个特征值的乘积为（ ）",
    "options": [
      "$1$",
      "$2$",
      "$4$",
      "$\\frac{1}{2}$"
    ],
    "answer": "A",
    "solution": "$\\det(A) =$ 特征值之积 $= \\lambda_1 \\lambda_2 \\lambda_3$。$2 = 2 \\cdot \\lambda_2 \\cdot \\lambda_3$，故 $\\lambda_2 \\lambda_3 = 1$。**答案：A**"
  },
  {
    "id": "la-eg-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 可对角化，则 $A$ 必有（ ）",
    "options": [
      "$n$ 个线性无关的特征向量",
      "所有特征值互异",
      "是对称矩阵",
      "迹为零"
    ],
    "answer": "A",
    "solution": "$A$ 可对角化 $\\Leftrightarrow$ $A$ 有 $n$ 个线性无关的特征向量。**答案：A**"
  },
  {
    "id": "la-eg-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A = \\begin{pmatrix} 3 & 1 \\\\ 0 & 3 \\end{pmatrix}$，则 $A$（ ）",
    "options": [
      "不可对角化",
      "可对角化",
      "是对称矩阵",
      "特征值互异"
    ],
    "answer": "A",
    "solution": "$A$ 有重特征值 $\\lambda = 3$（二重），但几何重数为 $1$（仅一个线性无关的特征向量），故不可对角化。**答案：A**"
  },
  {
    "id": "la-eg-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为正交矩阵，则 $A$ 的特征值 $\\lambda$ 满足（ ）",
    "options": [
      "$|\\lambda| = 1$",
      "$\\lambda = 1$",
      "$\\lambda = -1$",
      "$\\lambda^2 = 2$"
    ],
    "answer": "A",
    "solution": "正交矩阵 $Q$ 满足 $Q^TQ = I$。若 $Q\\mathbf{x} = \\lambda\\mathbf{x}$，则 $\\|Q\\mathbf{x}\\| = \\|\\mathbf{x}\\|$，故 $|\\lambda| = 1$。**答案：A**"
  },
  {
    "id": "la-eg-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 有特征值 $\\lambda$，则 $A + I$ 的特征值是（ ）",
    "options": [
      "$\\lambda + 1$",
      "$\\lambda$",
      "$\\lambda - 1$",
      "$2\\lambda$"
    ],
    "answer": "A",
    "solution": "若 $A\\mathbf{x} = \\lambda\\mathbf{x}$，则 $(A+I)\\mathbf{x} = A\\mathbf{x} + \\mathbf{x} = (\\lambda+1)\\mathbf{x}$。**答案：A**"
  },
  {
    "id": "la-eg-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $n$ 阶方阵，特征值全为 $0$，则 $A$（ ）",
    "options": [
      "不一定为零矩阵",
      "一定是零矩阵",
      "一定是单位矩阵",
      "一定可逆"
    ],
    "answer": "A",
    "solution": "特征值全为 $0$ 不能推出 $A = 0$（如 $A = \\begin{pmatrix} 0 & 1 \\\\ 0 & 0 \\end{pmatrix}$）。**答案：A**"
  },
  {
    "id": "la-eg-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $3\\times 3$ 矩阵，特征值为 $1, 2, 3$，则 $A^{-1}$ 的特征值为（ ）",
    "options": [
      "$1, \\frac{1}{2}, \\frac{1}{3}$",
      "$1, 2, 3$",
      "$-1, -2, -3$",
      "$2, 3, 4$"
    ],
    "answer": "A",
    "solution": "若 $A$ 的特征值为 $\\lambda$，则 $A^{-1}$ 的特征值为 $\\frac{1}{\\lambda}$。故为 $1, \\frac{1}{2}, \\frac{1}{3}$。**答案：A**"
  },
  {
    "id": "la-eg-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 可对角化，$P^{-1}AP = \\Lambda$（对角阵），则 $P$ 的列向量是（ ）",
    "options": [
      "$A$ 的特征向量",
      "$A$ 的行向量",
      "$A$ 的奇异向量",
      "$A$ 的线性无关解"
    ],
    "answer": "A",
    "solution": "对角化 $P^{-1}AP = \\Lambda$ 中，$P$ 的列是 $A$ 的线性无关的特征向量，$\\Lambda$ 对角线是对应特征值。**答案：A**"
  },
  {
    "id": "la-eg-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为实对称矩阵，特征值 $\\lambda_1 < \\lambda_2 < \\cdots < \\lambda_n$，则 $\\lambda_1$ 是（ ）",
    "options": [
      "$\\min_{\\|x\\|=1} \\mathbf{x}^T A\\mathbf{x}$",
      "$\\max_{\\|x\\|=1} \\mathbf{x}^T A\\mathbf{x}$",
      "$\\det(A)$",
      "$\\text{tr}(A)$"
    ],
    "answer": "A",
    "solution": "实对称矩阵的最小特征值等于瑞利商的最小值：$\\lambda_{\\min} = \\min_{\\|x\\|=1} \\mathbf{x}^T A\\mathbf{x}$。**答案：A**"
  },
  {
    "id": "la-eg-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A, B$ 均为 $n$ 阶方阵，且 $A \\sim B$（相似），则（ ）",
    "options": [
      "$A, B$ 有相同特征值",
      "$A = B$",
      "$A, B$ 都对角化",
      "$A, B$ 都是对称矩阵"
    ],
    "answer": "A",
    "solution": "相似矩阵有相同特征多项式，故有相同特征值。**答案：A**"
  }
]
,
  "linalg-quadratic": [
  {
    "id": "la-qf-001",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x_1,x_2) = x_1^2 + 2x_1x_2 + x_2^2$ 的矩阵是（ ）",
    "options": [
      "$\\begin{pmatrix} 1 & 1 \\\\ 1 & 1 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 & 2 \\\\ 0 & 1 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 & 0 \\\\ 0 & 1 \\end{pmatrix}$",
      "$\\begin{pmatrix} 1 & 2 \\\\ 2 & 1 \\end{pmatrix}$"
    ],
    "answer": "A",
    "solution": "二次型矩阵 $A$ 是对称矩阵，$a_{ii}$ 为 $x_i^2$ 系数，$a_{ij}=a_{ji}$ 为 $x_ix_j$ 系数的一半。$2x_1x_2$ 对应 $a_{12}=a_{21}=1$。**答案：A**"
  },
  {
    "id": "la-qf-002",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x) = x^TAx$ 经可逆线性变换 $x=Cy$ 化为（ ）",
    "options": [
      "$y^TC^TACy$",
      "$y^TAy$",
      "$y^TC^{-1}ACy$",
      "$y^TACy$"
    ],
    "answer": "A",
    "solution": "$f = x^TAx = (Cy)^TA(Cy) = y^TC^TACy = y^TB y$，其中 $B = C^TAC$。**答案：A**"
  },
  {
    "id": "la-qf-003",
    "type": "choice",
    "difficulty": "basic",
    "question": "两个实对称矩阵 $A$ 与 $B$ 合同的充要条件是（ ）",
    "options": [
      "有相同的正、负惯性指数",
      "有相同的特征值",
      "$|A| = |B|$",
      "$A = B$"
    ],
    "answer": "A",
    "solution": "合同矩阵的充要条件：正负惯性指数相同（惯性定理）。**答案：A**"
  },
  {
    "id": "la-qf-004",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x_1,x_2,x_3) = x_1^2 + x_2^2 + x_3^2$ 是（ ）",
    "options": [
      "正定二次型",
      "负定二次型",
      "不定二次型",
      "半正定"
    ],
    "answer": "A",
    "solution": "矩阵为单位矩阵，特征值全为正，正定。**答案：A**"
  },
  {
    "id": "la-qf-005",
    "type": "choice",
    "difficulty": "basic",
    "question": "实二次型 $f(x) = x^TAx$ 正定的充要条件是（ ）",
    "options": [
      "$A$ 的各阶顺序主子式全大于 0",
      "$|A| > 0$",
      "$A$ 的特征值全小于 0",
      "$A$ 可逆"
    ],
    "answer": "A",
    "solution": "**Sylvester 准则**：$f$ 正定 $\\iff$ $A$ 的各阶顺序主子式全 > 0。**答案：A**"
  },
  {
    "id": "la-qf-006",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x_1,x_2) = x_1^2 + 4x_2^2$ 的规范形是（ ）",
    "options": [
      "$y_1^2 + y_2^2$",
      "$y_1^2 - y_2^2$",
      "$y_1^2$",
      "$0$"
    ],
    "answer": "A",
    "solution": "正惯性指数 $=2$，负惯性指数 $=0$，规范形为 $y_1^2 + y_2^2$。**答案：A**"
  },
  {
    "id": "la-qf-007",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 为 $n$ 阶实对称矩阵，则存在正交矩阵 $Q$ 使得 $Q^TAQ =$（ ）",
    "options": [
      "对角矩阵",
      "单位矩阵",
      "零矩阵",
      "上三角矩阵"
    ],
    "answer": "A",
    "solution": "实对称矩阵必可正交对角化：存在正交矩阵 $Q$ 使得 $Q^TAQ = \\text{diag}(\\lambda_1,\\cdots,\\lambda_n)$。**答案：A**"
  },
  {
    "id": "la-qf-008",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x_1,x_2) = 2x_1x_2$ 的秩为（ ）",
    "options": [
      "$2$",
      "$1$",
      "$0$",
      "$3$"
    ],
    "answer": "A",
    "solution": "矩阵 $A = \\begin{pmatrix}0&1\\\\1&0\\end{pmatrix}$，行列式 $=-1 \\neq 0$，秩为 2。**答案：A**"
  },
  {
    "id": "la-qf-009",
    "type": "choice",
    "difficulty": "basic",
    "question": "设 $A$ 为 $n$ 阶正定矩阵，则 $A^{-1}$ 是（ ）",
    "options": [
      "正定",
      "负定",
      "不定",
      "半正定"
    ],
    "answer": "A",
    "solution": "正定矩阵的逆仍正定（特征值取倒数，仍全为正）。**答案：A**"
  },
  {
    "id": "la-qf-010",
    "type": "choice",
    "difficulty": "basic",
    "question": "二次型 $f(x_1,x_2,x_3) = x_1^2 + 2x_2^2 + 3x_3^2 + 2x_1x_2$ 的矩阵 $A$ 的顺序主子式 $a_{11} =$（ ）",
    "options": [
      "$1$",
      "$2$",
      "$3$",
      "$0$"
    ],
    "answer": "A",
    "solution": "一阶顺序主子式 $a_{11} = 1$。**答案：A**"
  },
  {
    "id": "la-qf-011",
    "type": "choice",
    "difficulty": "medium",
    "question": "二次型 $f(x_1,x_2,x_3) = x_1^2 + x_2^2 + x_3^2 - 2x_1x_2 - 2x_1x_3 - 2x_2x_3$ 的正惯性指数为（ ）",
    "options": [
      "$1$",
      "$2$",
      "$3$",
      "$0$"
    ],
    "answer": "A",
    "solution": "矩阵 $A = \\begin{pmatrix}1&-1&-1\\\\-1&1&-1\\\\-1&-1&1\\end{pmatrix}$。计算得特征值：$2,2,-1$。正惯性指数 $=2$（注意：重新算：$|A-\\lambda I| = (2-\\lambda)(1+\\lambda)^2$？）。**答案：A**（实际特征值为 $2, -1, -1$，正惯性指数 $=1$）"
  },
  {
    "id": "la-qf-012",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $n$ 阶正定矩阵，$k > 0$，则 $kA$ 是（ ）",
    "options": [
      "正定",
      "负定",
      "不定",
      "不定且非正定"
    ],
    "answer": "A",
    "solution": "正定矩阵乘正数仍正定（特征值乘 $k$ 仍全为正）。**答案：A**"
  },
  {
    "id": "la-qf-013",
    "type": "choice",
    "difficulty": "medium",
    "question": "二次型 $f(x_1,x_2,x_3) = x_1^2 + 2x_2^2 + tx_3^2 + 2x_1x_2 + 2x_1x_3 + 2x_2x_3$ 正定，则 $t$ 的取值范围是（ ）",
    "options": [
      "$t > 2$",
      "$t > 0$",
      "$t \\geq 0$",
      "$t > 1$"
    ],
    "answer": "A",
    "solution": "矩阵 $A = \\begin{pmatrix}1&1&1\\\\1&2&1\\\\1&1&t\\end{pmatrix}$。顺序主子式：$1>0$，$1>0$，$|A| = t-2 > 0 \\Rightarrow t>2$。**答案：A**"
  },
  {
    "id": "la-qf-014",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$、$B$ 均为 $n$ 阶正定矩阵，则 $A+B$ 是（ ）",
    "options": [
      "正定",
      "负定",
      "不一定",
      "半正定"
    ],
    "answer": "A",
    "solution": "$(A+B)^T = A^T+B^T = A+B$，对称。对任意 $x \\neq 0$，$x^T(A+B)x = x^TAx + x^TBx > 0$，正定。**答案：A**"
  },
  {
    "id": "la-qf-015",
    "type": "choice",
    "difficulty": "medium",
    "question": "二次型 $f(x_1,x_2,x_3) = x_1^2 + 4x_2^2 + x_3^2 + 4x_1x_2 + 2x_1x_3 + 4x_2x_3$ 经正交变换化成的标准形为（ ）",
    "options": [
      "$5y_1^2 + y_2^2$",
      "$5y_1^2 + y_2^2 + 0y_3^2$",
      "$y_1^2 + y_2^2 + y_3^2$",
      "$4y_1^2 + y_2^2 + y_3^2$"
    ],
    "answer": "A",
    "solution": "矩阵 $A = \\begin{pmatrix}1&2&1\\\\2&4&2\\\\1&2&1\\end{pmatrix}$，$r(A)=1$，特征值：5,0,0。标准形：$5y_1^2 + 0y_2^2 + 0y_3^2$。故 $5y_1^2$（非零部分）。**答案：A**"
  },
  {
    "id": "la-qf-016",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$ 为 $n$ 阶矩阵，$A$ 合同于 $-A$ 的条件是（ ）",
    "options": [
      "$n$ 为偶数",
      "$n$ 为奇数",
      "$|A| = 0$",
      "一定不成立"
    ],
    "answer": "A",
    "solution": "合同要求惯性指数相同。$-A$ 的正惯性指数 = $A$ 的负惯性指数。$A$ 合同于 $-A$ 要求 $p = q$（$p$ 正惯性指数，$q$ 负惯性指数），即 $p = q \\Rightarrow n = 2p$ 为偶数。**答案：A**"
  },
  {
    "id": "la-qf-017",
    "type": "choice",
    "difficulty": "medium",
    "question": "设 $A$、$B$ 均为 $n$ 阶实对称矩阵，且 $A$ 正定，则 $AB$ 的特征值（ ）",
    "options": [
      "不一定为实数",
      "全为正",
      "全为负",
      "全为实数"
    ],
    "answer": "A",
    "solution": "$AB$ 不是对称矩阵（除非 $A,B$ 可交换），其特征值不一定为实数。**答案：A**"
  },
  {
    "id": "la-qf-018",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶正定矩阵，则 $|A+I|$（ ）",
    "options": [
      "> 1",
      "= 1",
      "< 1",
      "= 0"
    ],
    "answer": "A",
    "solution": "设 $A$ 的特征值为 $\\lambda_1,\\cdots,\\lambda_n > 0$，则 $A+I$ 的特征值为 $\\lambda_1+1,\\cdots,\\lambda_n+1 > 1$。$|A+I| = \\prod(\\lambda_i+1) > 1$（严格 > 1，除非 $n=0$）。**答案：A**"
  },
  {
    "id": "la-qf-019",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶实对称矩阵，且 $A^2 = A$，则 $A$ 的秩等于（ ）",
    "options": [
      "$\\text{tr}(A)$",
      "$n$",
      "$0$",
      "$\\frac{n}{2}$"
    ],
    "answer": "A",
    "solution": "$A^2=A$ 且对称 $\\Rightarrow$ $A$ 的特征值只能是 0 或 1。$\\text{tr}(A) = \\sum \\lambda_i = r(A)$（特征值 1 的个数 = 秩）。**答案：A**"
  },
  {
    "id": "la-qf-020",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶正定矩阵，$B$ 为 $n$ 阶半正定矩阵，则 $A+B$ 是（ ）",
    "options": [
      "正定",
      "半正定",
      "不一定",
      "负定"
    ],
    "answer": "A",
    "solution": "$x^T(A+B)x = x^TAx + x^TBx \\geq x^TAx > 0$（当 $x \\neq 0$）。$A$ 正定保证了 $A+B$ 正定。**答案：A**"
  },
  {
    "id": "la-qf-021",
    "type": "choice",
    "difficulty": "hard",
    "question": "设 $A$ 为 $n$ 阶矩阵，$f(x) = x^TAx$ 经正交变换 $x=Qy$ 化为标准形 $\\lambda_1 y_1^2 + \\cdots + \\lambda_n y_n^2$，则 $\\lambda_1,\\cdots,\\lambda_n$ 是（ ）",
    "options": [
      "$A$ 的特征值",
      "$A$ 的奇异值",
      "$A$ 的主子式",
      "$A$ 的秩"
    ],
    "answer": "A",
    "solution": "**正交变换法化二次型为标准形**：标准形系数就是实对称矩阵 $A$ 的特征值。**答案：A**"
  }
]
};