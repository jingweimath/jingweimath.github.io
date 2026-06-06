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
        "file": null
      },
      {
        "id": "calculus-multi-diff",
        "name": "多元函数微分学",
        "file": null
      },
      {
        "id": "calculus-double-integral",
        "name": "二重积分",
        "file": null
      },
      {
        "id": "calculus-vector-geometry",
        "name": "向量代数与空间解析几何",
        "file": null
      },
      {
        "id": "calculus-triple-curve",
        "name": "三重积分与曲线曲面积分",
        "file": null
      },
      {
        "id": "calculus-series",
        "name": "无穷级数",
        "file": null
      }
    ]
  },
  "linalg": {
    "name": "线性代数",
    "chapters": [
      {
        "id": "linalg-matrix",
        "name": "矩阵与行列式",
        "file": null
      },
      {
        "id": "linalg-vector",
        "name": "向量与线性方程组",
        "file": null
      },
      {
        "id": "linalg-eigen",
        "name": "特征值与特征向量",
        "file": null
      },
      {
        "id": "linalg-quadratic",
        "name": "二次型",
        "file": null
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
};