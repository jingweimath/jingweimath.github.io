# -*- coding: utf-8 -*-
r"""多元 27 题（数一）数据 · 第 1-14 题。

来源：老板桌面《考研数学多元(数一).pptx》，用 pptx_omml2latex 提取 OMML 原生公式后人工整理。
整理时做的改动（都有依据，见 _verify_duoyuan.py）：
  - 字符归一化：Unicode 数学斜体字母 → ASCII，非断空格 → 普通空格，全角括号 → 半角
  - 公式单独 $ 包裹，中文一律留在数学模式外
  - 方程组 \left{...\right) → \begin{cases}...\end{cases}（原提取把两个方程拉平成一行的已还原）
  - 补回被提取脚本吞掉的 \int（nary 无 chr 属性时默认积分号）
  - 修明显缺字：题 3「截距之和对于 a」→「等于 a」；题 4「因为继极限」→「因为极限」等
  - **修算错的结果**：题 8 → 16π/3（原 8π/3）；题 15 → -πa⁴/2（原 -πa⁴/8）
  - 修过程笔误：题 1 法平面点代入 (y-2)→(y+2)、雅可比 -3→-6；题 25 中间步 2R→2R²；题 27 的 θ 范围 [0,2π]→[0,π/2]
  - 题 10 区域半径 a 与被积系数 a 重名 → 区域改记 R
"""

# n: 题号  ch: md=多元函数微分学 / tc=三重积分与曲线曲面积分
# type: choice/fill/proof  diff: basic/medium/hard
Q1 = [
    dict(n=1, ch='md', type='proof', diff='medium',
         cat='多元函数微分学', topic='隐函数求导·空间曲线的切线与法平面',
         q='求曲线 $\\begin{cases}x^{2}+y^{2}+z^{2}=6\\\\ x+y+z=0\\end{cases}$ 在点 $(1,-2,1)$ 处的切线及法平面。',
         a='', opts=None,
         s='''设 $F=x^{2}+y^{2}+z^{2}-6$，$G=x+y+z$。

**思路**：把曲线看成隐函数组 $y=y(x),z=z(x)$，方程两边对 $x$ 求导。

**求导**：对两方程两边对 $x$ 求导并移项，得
$$\\begin{cases}y\\frac{dy}{dx}+z\\frac{dz}{dx}=-x\\\\[4pt] \\frac{dy}{dx}+\\frac{dz}{dx}=-1\\end{cases}$$

由克拉默法则，
$$\\frac{dy}{dx}=\\frac{\\begin{vmatrix}-x & z\\\\ -1 & 1\\end{vmatrix}}{\\begin{vmatrix}y & z\\\\ 1 & 1\\end{vmatrix}}=\\frac{z-x}{y-z}=0,\\qquad
\\frac{dz}{dx}=\\frac{\\begin{vmatrix}y & -x\\\\ 1 & -1\\end{vmatrix}}{\\begin{vmatrix}y & z\\\\ 1 & 1\\end{vmatrix}}=\\frac{x-y}{y-z}=-1$$

**切向量**：$T=\\left(1,\\frac{dy}{dx},\\frac{dz}{dx}\\right)=(1,0,-1)$。

**切线方程**：
$$\\frac{x-1}{1}=\\frac{y+2}{0}=\\frac{z-1}{-1}$$
或写成 $\\begin{cases}x+z-2=0\\\\ y+2=0\\end{cases}$。

**法平面方程**（点法式）：
$$1\\cdot(x-1)+0\\cdot(y+2)+(-1)\\cdot(z-1)=0$$
即 $x-z=0$。

**注**：因为 $\\frac{\\partial(F,G)}{\\partial(y,z)}\\Big|_{(1,-2,1)}=2y-2z\\Big|_{(1,-2,1)}=-6\\neq0$，由隐函数存在定理确实确定了 $y=y(x),z=z(x)$，所以上面的求导是合法的。'''),

    dict(n=2, ch='md', type='fill', diff='medium',
         cat='多元函数微分学', topic='曲面切平面·两平面夹角',
         q='求旋转椭球面 $3x^{2}+y^{2}+z^{2}=16$ 上点 $(-1,-2,3)$ 处的切平面与 $xOy$ 面夹角的余弦。',
         a='$\\dfrac{3}{\\sqrt{22}}$', opts=None,
         s='''**分析**：切平面与 $xOy$ 面的夹角，等于切平面的法线与 $z$ 轴的夹角，也就是法向量与 $z$ 轴单位向量 $\\vec{e}=(0,0,1)$ 的夹角。

设 $F=3x^{2}+y^{2}+z^{2}-16$，则
$$F_{x}=6x,\\quad F_{y}=2y,\\quad F_{z}=2z$$

在 $(-1,-2,3)$ 处法向量 $\\vec{n}=(-6,-4,6)$。

由两向量夹角余弦公式，
$$\\cos\\gamma=\\frac{|\\vec{n}\\cdot\\vec{e}|}{|\\vec{n}|\\,|\\vec{e}|}
=\\frac{|(-6)\\cdot0+(-4)\\cdot0+6\\cdot1|}{\\sqrt{36+16+36}\\times1}
=\\frac{6}{\\sqrt{88}}=\\frac{3}{\\sqrt{22}}$$

**答案**：$\\dfrac{3}{\\sqrt{22}}$（也可写成 $\\dfrac{3\\sqrt{22}}{22}$）。'''),

    dict(n=3, ch='md', type='proof', diff='hard',
         cat='多元函数微分学', topic='曲面切平面·截距之和',
         q='试证曲面 $\\sqrt{x}+\\sqrt{y}+\\sqrt{z}=\\sqrt{a}\\ (a>0)$ 上任何点处的切平面在三个坐标轴上的截距之和等于 $a$。',
         a='', opts=None,
         s='''**证明**：设 $P_{0}(x_{0},y_{0},z_{0})$ 为曲面上任意一点，则 $\\sqrt{x_{0}}+\\sqrt{y_{0}}+\\sqrt{z_{0}}=\\sqrt{a}$。

**法向量**：令 $F=\\sqrt{x}+\\sqrt{y}+\\sqrt{z}-\\sqrt{a}$，则
$$\\vec{n}=\\left(\\frac{1}{2\\sqrt{x_{0}}},\\frac{1}{2\\sqrt{y_{0}}},\\frac{1}{2\\sqrt{z_{0}}}\\right)$$

**切平面方程**：
$$\\frac{x-x_{0}}{2\\sqrt{x_{0}}}+\\frac{y-y_{0}}{2\\sqrt{y_{0}}}+\\frac{z-z_{0}}{2\\sqrt{z_{0}}}=0$$

整理为截距式形式：
$$\\frac{x}{2\\sqrt{x_{0}}}+\\frac{y}{2\\sqrt{y_{0}}}+\\frac{z}{2\\sqrt{z_{0}}}
=\\frac{x_{0}}{2\\sqrt{x_{0}}}+\\frac{y_{0}}{2\\sqrt{y_{0}}}+\\frac{z_{0}}{2\\sqrt{z_{0}}}
=\\frac{\\sqrt{x_{0}}+\\sqrt{y_{0}}+\\sqrt{z_{0}}}{2}=\\frac{\\sqrt{a}}{2}$$

**三个截距**：令 $y=z=0$ 得 $x$ 轴截距 $\\dfrac{\\sqrt{a}}{2}\\cdot2\\sqrt{x_{0}}=\\sqrt{ax_{0}}$；同理得 $y$ 轴、$z$ 轴截距分别为 $\\sqrt{ay_{0}},\\sqrt{az_{0}}$。

**求和**：
$$\\sqrt{ax_{0}}+\\sqrt{ay_{0}}+\\sqrt{az_{0}}
=\\sqrt{a}\\left(\\sqrt{x_{0}}+\\sqrt{y_{0}}+\\sqrt{z_{0}}\\right)
=\\sqrt{a}\\cdot\\sqrt{a}=a$$

故截距之和恒为 $a$，与所取的点无关。证毕。'''),

    dict(n=4, ch='md', type='proof', diff='hard',
         cat='多元函数微分学', topic='方向导数·偏导数存在性',
         q='函数 $z=\\sqrt{x^{2}+y^{2}}$ 在点 $(0,0)$ 处沿 $(1,0)$ 方向的方向导数 $\\dfrac{\\partial z}{\\partial l}=1$，证明函数在 $(0,0)$ 的偏导数 $\\dfrac{\\partial z}{\\partial x}$ 不存在。',
         a='', opts=None,
         s='''**证明**：记 $f(x,y)=\\sqrt{x^{2}+y^{2}}$。

**方向导数**（沿 $\\vec{l}=(1,0)$，由定义）：
$$\\frac{\\partial z}{\\partial l}\\Big|_{(0,0)}
=\\lim_{t\\to0^{+}}\\frac{f(t,0)-f(0,0)}{t}
=\\lim_{t\\to0^{+}}\\frac{\\sqrt{t^{2}}}{t}
=\\lim_{t\\to0^{+}}\\frac{|t|}{t}=1$$

**偏导数**（仍由定义，注意这里是双侧极限）：
$$\\frac{\\partial z}{\\partial x}\\Big|_{(0,0)}
=\\lim_{x\\to0}\\frac{f(x,0)-f(0,0)}{x}
=\\lim_{x\\to0}\\frac{\\sqrt{x^{2}}}{x}
=\\lim_{x\\to0}\\frac{|x|}{x}$$

右极限为 $1$，左极限为 $-1$，两者不相等，故该极限不存在。

**结论**：偏导数 $\\dfrac{\\partial z}{\\partial x}$ 不存在。

**点睛**：方向导数用的是**单侧**极限 $t\\to0^{+}$，偏导数用的是**双侧**极限 $x\\to0$。沿某方向的方向导数存在，推不出偏导数存在——这是本题的要害。'''),

    dict(n=5, ch='md', type='choice', diff='medium',
         cat='多元函数微分学', topic='方向导数·偏导数存在性',
         q='函数 $z=\\sqrt{x^{2}+y^{2}}$ 在点 $(0,0)$ 处，下面哪个正确？',
         a=3,
         opts=['不连续', '方向导数不存在', '偏导数存在', '沿任意方向的方向导数存在'],
         s='''逐项判断。

**A 错**：$z=\\sqrt{x^{2}+y^{2}}$ 是连续函数的复合，在 $(0,0)$ 处连续。

**C 错**：由上一题，$\\dfrac{\\partial z}{\\partial x}\\Big|_{(0,0)}=\\lim\\limits_{x\\to0}\\dfrac{|x|}{x}$ 不存在，偏导数不存在。

**B 错、D 对**：设任意单位方向 $\\vec{l}=(\\cos\\alpha,\\cos\\beta)$，由定义
$$\\frac{\\partial f}{\\partial l}\\Big|_{(0,0)}
=\\lim_{t\\to0^{+}}\\frac{f(t\\cos\\alpha,\\,t\\cos\\beta)-f(0,0)}{t}
=\\lim_{t\\to0^{+}}\\frac{\\sqrt{t^{2}(\\cos^{2}\\alpha+\\cos^{2}\\beta)}}{t}
=\\lim_{t\\to0^{+}}\\frac{t\\cdot1}{t}=1$$

即沿**任意**方向的方向导数都存在且都等于 $1$。

**答案：D**'''),

    dict(n=6, ch='md', type='proof', diff='medium',
         cat='多元函数微分学', topic='梯度·方向导数·变化率为零的方向',
         q='设 $f(x,y)=\\dfrac{1}{2}(x^{2}+y^{2})$，点 $P_{0}(1,1)$，求：（1）$f(x,y)$ 在 $P_{0}$ 处增加最快的方向以及沿这个方向的方向导数；（2）$f(x,y)$ 在 $P_{0}$ 处变化率为零的方向。',
         a='', opts=None,
         s='''**（1）增加最快的方向**

增加最快的方向就是梯度方向。
$$f_{x}=x,\\quad f_{y}=y\\quad\\Rightarrow\\quad \\nabla f(1,1)=(1,1)$$

其方向余弦为 $\\left(\\dfrac{1}{\\sqrt{2}},\\dfrac{1}{\\sqrt{2}}\\right)$，即方向与 $x$ 轴正向成 $45^{\\circ}$。

沿该方向的方向导数等于梯度的模：
$$\\frac{\\partial f}{\\partial l}\\Big|_{(1,1)}
=1\\cdot\\frac{1}{\\sqrt{2}}+1\\cdot\\frac{1}{\\sqrt{2}}=\\sqrt{2}$$

**（2）变化率为零的方向**

方向导数 $\\dfrac{\\partial f}{\\partial l}=\\nabla f\\cdot\\vec{l}^{\\,\\circ}=0$ 意味着方向与梯度垂直。

与 $(1,1)$ 垂直的单位向量有两个：
$$\\left(-\\frac{1}{\\sqrt{2}},\\frac{1}{\\sqrt{2}}\\right)\\quad\\text{或}\\quad\\left(\\frac{1}{\\sqrt{2}},-\\frac{1}{\\sqrt{2}}\\right)$$

**点睛**：变化率为零的方向是**等值线（等高线）的切线方向**。本题等值线是圆 $x^{2}+y^{2}=C$，在 $(1,1)$ 处切线方向正是上述两个方向。'''),

    dict(n=7, ch='tc', type='fill', diff='medium',
         cat='三重积分', topic='先一后二·投影区域确定',
         q='计算三重积分 $\\displaystyle\\iiint_{\\Omega}x\\,dxdydz$，其中 $\\Omega$ 为三个坐标面以及平面 $x+2y+z=1$ 所围成的闭区域。',
         a='$\\dfrac{1}{48}$', opts=None,
         s='''**确定投影区域**：$\\Omega$ 由 $x\\ge0,y\\ge0,z\\ge0$ 与 $x+2y+z\\le1$ 围成（四面体）。

投影到 $xOy$ 面上：
$$D_{xy}=\\left\\{(x,y)\\ \\Big|\\ 0\\le x\\le1,\\ 0\\le y\\le\\frac{1-x}{2}\\right\\}$$

**先一后二**（先对 $z$ 积分）：
$$\\iiint_{\\Omega}x\\,dV=\\int_{0}^{1}dx\\int_{0}^{\\frac{1-x}{2}}dy\\int_{0}^{1-x-2y}x\\,dz$$

对 $z$ 积分（被积与 $z$ 无关）：
$$=\\int_{0}^{1}x\\,dx\\int_{0}^{\\frac{1-x}{2}}(1-x-2y)\\,dy$$

内层：$\\displaystyle\\int_{0}^{\\frac{1-x}{2}}(1-x-2y)dy=\\left[(1-x)y-y^{2}\\right]_{0}^{\\frac{1-x}{2}}=\\frac{(1-x)^{2}}{4}$

外层：$\\displaystyle\\frac{1}{4}\\int_{0}^{1}x(1-x)^{2}dx=\\frac{1}{4}\\cdot\\frac{1}{12}=\\frac{1}{48}$

（其中 $\\int_{0}^{1}x(1-x)^{2}dx=B(2,3)=\\dfrac{1}{12}$）

**答案**：$\\dfrac{1}{48}$'''),

    dict(n=8, ch='tc', type='fill', diff='medium',
         cat='三重积分', topic='旋转曲面·柱坐标',
         q='设 $\\Omega$ 为平面曲线 $\\begin{cases}y^{2}=2z\\\\ x=0\\end{cases}$ 绕 $z$ 轴旋转一周所成的曲面与平面 $z=2$ 所围成的区域，求 $\\displaystyle\\iiint_{\\Omega}(x^{2}+y^{2})\\,dV$。',
         a='$\\dfrac{16\\pi}{3}$', opts=None,
         s='''**旋转曲面方程**：平面曲线 $y^{2}=2z$（在 $yOz$ 面内）绕 $z$ 轴旋转，把 $y$ 换成 $\\pm\\sqrt{x^{2}+y^{2}}$，得

$$x^{2}+y^{2}=2z$$

与平面 $z=2$ 围成的区域为旋转抛物面的内部，$z\\in\\left[\\dfrac{x^{2}+y^{2}}{2},\\,2\\right]$。

**投影区域**：$z=2$ 时 $x^{2}+y^{2}=4$，故在 $xOy$ 面投影为圆盘 $x^{2}+y^{2}\\le4$。

**用柱坐标**（$x^{2}+y^{2}=r^{2}$，$dV=r\\,dr\\,d\\theta\\,dz$）：
$$\\iiint_{\\Omega}(x^{2}+y^{2})dV
=\\int_{0}^{2\\pi}d\\theta\\int_{0}^{2}dr\\int_{\\frac{r^{2}}{2}}^{2}r^{2}\\cdot r\\,dz
=2\\pi\\int_{0}^{2}r^{3}\\left(2-\\frac{r^{2}}{2}\\right)dr$$

计算内层：
$$\\int_{0}^{2}r^{3}\\left(2-\\frac{r^{2}}{2}\\right)dr=\\left[\\frac{r^{4}}{2}-\\frac{r^{6}}{12}\\right]_{0}^{2}=8-\\frac{16}{3}=\\frac{8}{3}$$

故
$$\\iiint_{\\Omega}(x^{2}+y^{2})dV=2\\pi\\cdot\\frac{8}{3}=\\frac{16\\pi}{3}$$

**答案**：$\\dfrac{16\\pi}{3}$

**校注**：本题容易在最后一步把 $2\\pi$ 漏掉而错答 $\\dfrac{8\\pi}{3}$。上面结果已用蒙特卡洛抽样独立复核（抽样值 $16.82$，与 $16\\pi/3\\approx16.755$ 吻合，与 $8\\pi/3\\approx8.378$ 差一倍）。'''),

    dict(n=9, ch='tc', type='fill', diff='hard',
         cat='三重积分', topic='球坐标·积分限的确定',
         q='计算 $I=\\displaystyle\\iiint_{\\Omega}\\frac{1}{\\sqrt{x^{2}+y^{2}+z^{2}}}\\,dV$，其中 $\\Omega$ 由 $x^{2}+y^{2}+(z-1)^{2}\\le1,\\ z\\ge1,\\ y\\ge0$ 所确定。',
         a='$\\dfrac{(7-4\\sqrt{2})\\pi}{6}$', opts=None,
         s='''**认清区域**：$x^{2}+y^{2}+(z-1)^{2}\\le1$ 是球心 $(0,0,1)$、半径 $1$ 的球体；$z\\ge1$ 取其上半球；$y\\ge0$ 再取一半（共 $\\frac{1}{4}$ 球体）。

**用球坐标**（以**原点**为极点，这样被积函数 $\\frac{1}{r}$ 才最简）：
$$x=r\\sin\\varphi\\cos\\theta,\\quad y=r\\sin\\varphi\\sin\\theta,\\quad z=r\\cos\\varphi$$
$$dV=r^{2}\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta$$

**确定 $r$ 的范围**（这是本题最难的一步）：

- 球面方程展开：$x^{2}+y^{2}+z^{2}-2z+1\\le1$，即 $r^{2}\\le2r\\cos\\varphi$，得 $r\\le2\\cos\\varphi$
- 条件 $z\\ge1$：$r\\cos\\varphi\\ge1$，得 $r\\ge\\dfrac{1}{\\cos\\varphi}$

两者要相容：$\\dfrac{1}{\\cos\\varphi}\\le2\\cos\\varphi\\ \\Rightarrow\\ \\cos^{2}\\varphi\\ge\\dfrac{1}{2}\\ \\Rightarrow\\ \\varphi\\in\\left[0,\\dfrac{\\pi}{4}\\right]$

**确定 $\\theta$ 的范围**：$y\\ge0$ 即 $\\sin\\theta\\ge0$，故 $\\theta\\in[0,\\pi]$。

**积分**：
$$I=\\int_{0}^{\\pi}d\\theta\\int_{0}^{\\frac{\\pi}{4}}d\\varphi\\int_{\\frac{1}{\\cos\\varphi}}^{2\\cos\\varphi}\\frac{1}{r}\\cdot r^{2}\\sin\\varphi\\,dr$$

对 $r$ 积分：
$$=\\pi\\int_{0}^{\\frac{\\pi}{4}}\\sin\\varphi\\cdot\\frac{(2\\cos\\varphi)^{2}-\\left(\\frac{1}{\\cos\\varphi}\\right)^{2}}{2}\\,d\\varphi
=\\frac{\\pi}{2}\\int_{0}^{\\frac{\\pi}{4}}\\left(4\\cos^{2}\\varphi-\\sec^{2}\\varphi\\right)\\sin\\varphi\\,d\\varphi$$

令 $u=\\cos\\varphi$：
$$=\\frac{\\pi}{2}\\int_{\\frac{1}{\\sqrt{2}}}^{1}\\left(4u^{2}-\\frac{1}{u^{2}}\\right)du
=\\frac{\\pi}{2}\\left[\\frac{4u^{3}}{3}+\\frac{1}{u}\\right]_{\\frac{1}{\\sqrt{2}}}^{1}$$

$$=\\frac{\\pi}{2}\\left[\\left(\\frac{4}{3}+1\\right)-\\left(\\frac{4}{3}\\cdot\\frac{1}{2\\sqrt{2}}+\\sqrt{2}\\right)\\right]
=\\frac{\\pi}{2}\\left(\\frac{7}{3}-\\frac{\\sqrt{2}}{3}-\\sqrt{2}\\right)
=\\frac{\\pi}{2}\\cdot\\frac{7-4\\sqrt{2}}{3}
=\\frac{(7-4\\sqrt{2})\\pi}{6}$$

**答案**：$\\dfrac{(7-4\\sqrt{2})\\pi}{6}\\approx0.7032$（已数值复核）'''),

    dict(n=10, ch='tc', type='fill', diff='hard',
         cat='三重积分', topic='奇偶对称性·轮换对称性',
         q='计算 $\\displaystyle\\iiint_{\\Omega}(ax+by+cz)^{2}\\,dV$，其中 $\\Omega$ 为球体 $x^{2}+y^{2}+z^{2}\\le R^{2}$。',
         a='$\\dfrac{4\\pi R^{5}}{15}(a^{2}+b^{2}+c^{2})$', opts=None,
         s='''**展开被积函数**：
$$(ax+by+cz)^{2}=\\underbrace{(a^{2}x^{2}+b^{2}y^{2}+c^{2}z^{2})}_{\\text{平方项}}+\\underbrace{(2abxy+2bcyz+2acxz)}_{\\text{交叉项}}$$

**交叉项用奇偶性消掉**：$\\Omega$ 关于三个坐标面都对称，而 $xy$ 关于 $x$（也关于 $y$）是奇函数，故
$$\\iiint_{\\Omega}xy\\,dV=\\iiint_{\\Omega}yz\\,dV=\\iiint_{\\Omega}xz\\,dV=0$$

**平方项用轮换对称性**：$\\Omega$ 关于 $x,y,z$ 完全对称，故
$$\\iiint_{\\Omega}x^{2}dV=\\iiint_{\\Omega}y^{2}dV=\\iiint_{\\Omega}z^{2}dV=\\frac{1}{3}\\iiint_{\\Omega}(x^{2}+y^{2}+z^{2})dV$$

于是
$$\\iiint_{\\Omega}(a^{2}x^{2}+b^{2}y^{2}+c^{2}z^{2})dV=\\frac{a^{2}+b^{2}+c^{2}}{3}\\iiint_{\\Omega}(x^{2}+y^{2}+z^{2})dV$$

**球坐标计算**：
$$\\iiint_{\\Omega}(x^{2}+y^{2}+z^{2})dV=\\int_{0}^{2\\pi}d\\theta\\int_{0}^{\\pi}d\\varphi\\int_{0}^{R}r^{2}\\cdot r^{2}\\sin\\varphi\\,dr
=2\\pi\\cdot2\\cdot\\frac{R^{5}}{5}=\\frac{4\\pi R^{5}}{5}$$

**合并**：
$$\\iiint_{\\Omega}(ax+by+cz)^{2}dV=\\frac{a^{2}+b^{2}+c^{2}}{3}\\cdot\\frac{4\\pi R^{5}}{5}=\\frac{4\\pi R^{5}}{15}(a^{2}+b^{2}+c^{2})$$

**答案**：$\\dfrac{4\\pi R^{5}}{15}(a^{2}+b^{2}+c^{2})$

**注**：原题中球体半径也记作 $a$，与被积函数的系数 $a$ 重名，容易混淆，这里把球体半径改记为 $R$。'''),

    dict(n=11, ch='tc', type='fill', diff='medium',
         cat='曲线积分', topic='第一类曲线积分·转动惯量',
         q='计算半径为 $R$、中心角为 $2\\alpha$ 的圆弧 $L$ 对于其对称轴的转动惯量 $I$（设线密度 $\\mu=1$）。',
         a='$R^{3}(\\alpha-\\sin\\alpha\\cos\\alpha)$', opts=None,
         s='''**建系**：取对称轴为 $x$ 轴，圆心在原点，则 $L$ 的参数方程为
$$\\begin{cases}x=R\\cos\\theta\\\\ y=R\\sin\\theta\\end{cases}\\quad(-\\alpha\\le\\theta\\le\\alpha)$$

**转动惯量**：对 $x$ 轴的转动惯量为 $\\displaystyle I=\\int_{L}y^{2}\\mu\\,ds=\\int_{L}y^{2}ds$。

**弧长微元**：
$$ds=\\sqrt{(-R\\sin\\theta)^{2}+(R\\cos\\theta)^{2}}\\,d\\theta=R\\,d\\theta$$

**代入计算**：
$$I=\\int_{-\\alpha}^{\\alpha}(R\\sin\\theta)^{2}\\cdot R\\,d\\theta
=R^{3}\\int_{-\\alpha}^{\\alpha}\\sin^{2}\\theta\\,d\\theta$$

$$\\int_{-\\alpha}^{\\alpha}\\sin^{2}\\theta\\,d\\theta=\\left[\\frac{\\theta}{2}-\\frac{\\sin2\\theta}{4}\\right]_{-\\alpha}^{\\alpha}=\\alpha-\\frac{\\sin2\\alpha}{2}=\\alpha-\\sin\\alpha\\cos\\alpha$$

**答案**：$I=R^{3}(\\alpha-\\sin\\alpha\\cos\\alpha)$'''),

    dict(n=12, ch='tc', type='fill', diff='hard',
         cat='曲线积分', topic='第一类曲线积分·轮换对称性',
         q='设曲线 $L:\\begin{cases}x^{2}+y^{2}+z^{2}=4\\\\ x+y+z=0\\end{cases}$，求第一类曲线积分 $\\displaystyle\\int_{L}(x+y)^{2}ds$。',
         a='$\\dfrac{16\\pi}{3}$', opts=None,
         s='''**化简被积函数**：在 $L$ 上恒有 $x+y=-z$，故
$$\\int_{L}(x+y)^{2}ds=\\int_{L}z^{2}ds$$

**用轮换对称性**：$L$ 的方程组关于 $x,y,z$ 完全对称，故
$$\\int_{L}z^{2}ds=\\int_{L}x^{2}ds=\\int_{L}y^{2}ds$$

于是
$$3\\int_{L}z^{2}ds=\\int_{L}(x^{2}+y^{2}+z^{2})ds=\\int_{L}4\\,ds=4\\cdot|L|$$

**求弧长**：$L$ 是球面 $x^{2}+y^{2}+z^{2}=4$ 与过球心的平面 $x+y+z=0$ 的交圆，半径为球的半径 $2$，故
$$|L|=2\\pi\\cdot2=4\\pi$$

**结论**：
$$\\int_{L}(x+y)^{2}ds=\\frac{4}{3}\\cdot4\\pi=\\frac{16\\pi}{3}$$

**答案**：$\\dfrac{16\\pi}{3}$

**点睛**：第一类（对弧长的）曲线积分可以把曲线方程代入被积函数化简——因为积分变量满足这些关系。**但第二类曲线积分不可以这样代入**，代入会改变 $\\cos\\alpha$ 等方向余弦，从而改变结果。'''),

    dict(n=13, ch='tc', type='fill', diff='medium',
         cat='曲线积分', topic='第二类曲线积分·参数化',
         q='计算第二类曲线积分 $\\displaystyle\\int_{L}\\sin^{2}x\\,dx+(x^{2}-1)y\\,dy$，其中 $L$ 是曲线 $y=\\sin x$ 从点 $(0,0)$ 到 $(\\pi,0)$ 的一段。',
         a='$\\dfrac{\\pi}{2}-\\dfrac{\\pi^{2}}{4}$', opts=None,
         s='''**参数化**：以 $x$ 为参数，$y=\\sin x$，$dy=\\cos x\\,dx$，$x:0\\to\\pi$。

$$\\int_{L}\\sin^{2}x\\,dx+(x^{2}-1)y\\,dy
=\\int_{0}^{\\pi}\\left[\\sin^{2}x+(x^{2}-1)\\sin x\\cos x\\right]dx$$

**第一项**：
$$\\int_{0}^{\\pi}\\sin^{2}x\\,dx=\\frac{\\pi}{2}$$

**第二项**（分部积分）：
$$\\int_{0}^{\\pi}(x^{2}-1)\\sin x\\cos x\\,dx=\\frac{1}{2}\\int_{0}^{\\pi}(x^{2}-1)\\sin2x\\,dx$$

其中
$$\\int_{0}^{\\pi}x^{2}\\sin2x\\,dx=\\left[-\\frac{x^{2}\\cos2x}{2}\\right]_{0}^{\\pi}+\\int_{0}^{\\pi}x\\cos2x\\,dx=-\\frac{\\pi^{2}}{2}+0=-\\frac{\\pi^{2}}{2}$$
$$\\int_{0}^{\\pi}\\sin2x\\,dx=\\left[-\\frac{\\cos2x}{2}\\right]_{0}^{\\pi}=0$$

故第二项 $=\\dfrac{1}{2}\\left(-\\dfrac{\\pi^{2}}{2}-0\\right)=-\\dfrac{\\pi^{2}}{4}$。

**结论**：
$$\\int_{L}\\sin^{2}x\\,dx+(x^{2}-1)y\\,dy=\\frac{\\pi}{2}-\\frac{\\pi^{2}}{4}$$

**答案**：$\\dfrac{\\pi}{2}-\\dfrac{\\pi^{2}}{4}$'''),

    dict(n=14, ch='tc', type='fill', diff='basic',
         cat='曲线积分', topic='第二类曲线积分·参数化',
         q='计算 $\\displaystyle\\int_{L}2xy\\,dx+x^{2}dy$，其中 $L$ 为抛物线 $y=x^{2}$ 上从 $O(0,0)$ 到 $(1,1)$ 的一段弧。',
         a='$1$', opts=None,
         s='''**参数化**：以 $x$ 为参数，$y=x^{2}$，$dy=2x\\,dx$，$x:0\\to1$。

$$\\int_{L}2xy\\,dx+x^{2}dy=\\int_{0}^{1}\\left(2x\\cdot x^{2}+x^{2}\\cdot2x\\right)dx=\\int_{0}^{1}4x^{3}dx=\\left[x^{4}\\right]_{0}^{1}=1$$

**答案**：$1$

**验证（路径无关）**：$P=2xy,Q=x^{2}$，$\\dfrac{\\partial Q}{\\partial x}=2x=\\dfrac{\\partial P}{\\partial y}$，故积分与路径无关。改走折线 $O(0,0)\\to(1,0)\\to(1,1)$：

- $O\\to(1,0)$：$y=0,dy=0$，积分为 $0$
- $(1,0)\\to(1,1)$：$dx=0,x=1$，积分 $=\\int_{0}^{1}1\\,dy=1$

结果一致。'''),
]
