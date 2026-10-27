# -*- coding: utf-8 -*-
"""多元 27 题（数一）数据 · 第 15-27 题。来源与处理说明见 _dy_data_a.py 的文档字符串。"""

Q2 = [
    dict(n=15, ch='tc', type='fill', diff='medium',
         cat='曲线积分', topic='第二类曲线积分·格林公式',
         q='计算 $\\displaystyle\\oint_{L}x^{2}y\\,dx-xy^{2}dy$，其中 $L$ 为正向圆周 $x^{2}+y^{2}=a^{2}$。',
         a='$-\\dfrac{\\pi a^{4}}{2}$', opts=None,
         s='''**方法一：参数方程**

$L$ 的正向（逆时针）参数方程：$x=a\\cos\\theta,\\ y=a\\sin\\theta,\\ \\theta:0\\to2\\pi$，
$$dx=-a\\sin\\theta\\,d\\theta,\\quad dy=a\\cos\\theta\\,d\\theta$$

$$\\oint_{L}x^{2}y\\,dx-xy^{2}dy=\\int_{0}^{2\\pi}\\left[a^{2}\\cos^{2}\\theta\\cdot a\\sin\\theta\\cdot(-a\\sin\\theta)-a\\cos\\theta\\cdot a^{2}\\sin^{2}\\theta\\cdot a\\cos\\theta\\right]d\\theta$$

$$=-a^{4}\\int_{0}^{2\\pi}2\\cos^{2}\\theta\\sin^{2}\\theta\\,d\\theta
=-2a^{4}\\int_{0}^{2\\pi}\\frac{\\sin^{2}2\\theta}{4}d\\theta
=-\\frac{a^{4}}{2}\\cdot\\pi=-\\frac{\\pi a^{4}}{2}$$

（用到 $\\int_{0}^{2\\pi}\\sin^{2}2\\theta\\,d\\theta=\\pi$）

**方法二：格林公式**

$P=x^{2}y,\\ Q=-xy^{2}$，则 $\\dfrac{\\partial Q}{\\partial x}-\\dfrac{\\partial P}{\\partial y}=-y^{2}-x^{2}=-(x^{2}+y^{2})$

$$\\oint_{L}=\\iint_{D}-(x^{2}+y^{2})dA=-\\int_{0}^{2\\pi}d\\theta\\int_{0}^{a}r^{2}\\cdot r\\,dr=-2\\pi\\cdot\\frac{a^{4}}{4}=-\\frac{\\pi a^{4}}{2}$$

**答案**：$-\\dfrac{\\pi a^{4}}{2}$

**校注**：常见错答 $-\\dfrac{\\pi a^{4}}{8}$，是把 $\\int_{0}^{2\\pi}\\cos^{2}\\theta\\sin^{2}\\theta\\,d\\theta$ 算成了 $\\dfrac{\\pi}{8}$（正确值是 $\\dfrac{\\pi}{4}$），或漏掉了 $dx,dy$ 带来的两个 $a$ 因子。上面结果已用参数化数值积分与格林公式两条独立路径互验（取 $a=1$ 均为 $-1.5708=-\\pi/2$）。'''),

    dict(n=16, ch='tc', type='proof', diff='hard',
         cat='曲线积分', topic='格林公式·挖洞法（奇点处理）',
         q='计算 $\\displaystyle\\oint_{L}\\frac{x\\,dy-y\\,dx}{x^{2}+y^{2}}$，其中 $L$ 为分段光滑且不经过原点的连续封闭曲线，$L$ 的方向为逆时针方向。',
         a='', opts=None,
         s='''**记**：$L$ 围成的闭区域为 $D$。被积式写成 $P\\,dx+Q\\,dy$，其中
$$P=\\frac{-y}{x^{2}+y^{2}},\\qquad Q=\\frac{x}{x^{2}+y^{2}}$$

**验证恰当性**（在原点以外）：
$$\\frac{\\partial Q}{\\partial x}=\\frac{(x^{2}+y^{2})-x\\cdot2x}{(x^{2}+y^{2})^{2}}=\\frac{y^{2}-x^{2}}{(x^{2}+y^{2})^{2}}$$
$$\\frac{\\partial P}{\\partial y}=\\frac{-(x^{2}+y^{2})-(-y)\\cdot2y}{(x^{2}+y^{2})^{2}}=\\frac{y^{2}-x^{2}}{(x^{2}+y^{2})^{2}}$$

两者相等，所以在不含原点的单连通区域上积分与路径无关。

**情形一：$(0,0)\\notin D$**

此时 $P,Q$ 在 $D$ 上连续可微，满足格林公式条件：
$$\\oint_{L}\\frac{x\\,dy-y\\,dx}{x^{2}+y^{2}}=\\iint_{D}\\left(\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y}\\right)dA=\\iint_{D}0\\,dA=0$$

**情形二：$(0,0)\\in D$**

$P,Q$ 在原点无定义、在 $D$ 上不连续，**不能直接用格林公式**。取充分小的 $r>0$，在 $D$ 内作圆周
$$l:\\ x^{2}+y^{2}=r^{2}\\quad(\\text{取逆时针方向})$$

记 $L$ 与 $l$ 围成的环形区域为 $D_{1}$（$D_{1}$ 不含原点），在 $D_{1}$ 上应用格林公式：
$$\\oint_{L+l^{-}}\\frac{x\\,dy-y\\,dx}{x^{2}+y^{2}}=0$$

于是 $\\displaystyle\\oint_{L}=\\oint_{l}$（注意 $l^{-}$ 是顺时针，移项后变号）：
$$\\oint_{l}\\frac{x\\,dy-y\\,dx}{x^{2}+y^{2}}
=\\int_{0}^{2\\pi}\\frac{r\\cos\\theta\\cdot r\\cos\\theta\\,d\\theta-r\\sin\\theta\\cdot(-r\\sin\\theta\\,d\\theta)}{r^{2}}
=\\int_{0}^{2\\pi}1\\,d\\theta=2\\pi$$

**结论**：
$$\\oint_{L}\\frac{x\\,dy-y\\,dx}{x^{2}+y^{2}}=\\begin{cases}0, & (0,0)\\notin D\\\\[4pt] 2\\pi, & (0,0)\\in D\\end{cases}$$

**点睛**：这就是"挖洞法"——奇点把区域挖掉，沿小洞的积分反而最好算。本题的被积式正是极角微分 $d\\theta$，绕原点一圈积累 $2\\pi$。'''),

    dict(n=17, ch='tc', type='fill', diff='medium',
         cat='曲线积分', topic='路径无关性·改走简单路径',
         q='计算第二类线积分 $\\displaystyle\\int_{L}ye^{y^{2}}dx+(xe^{y^{2}}+2xy^{2}e^{y^{2}})dy$，其中 $L$ 是曲线 $y=\\sqrt[3]{x}$ 从 $O(0,0)$ 到 $A(1,1)$ 的一段弧。',
         a='$e$', opts=None,
         s='''**先验证路径无关**：
$$P=ye^{y^{2}},\\quad Q=xe^{y^{2}}+2xy^{2}e^{y^{2}}$$
$$\\frac{\\partial P}{\\partial y}=e^{y^{2}}+2y^{2}e^{y^{2}},\\qquad \\frac{\\partial Q}{\\partial x}=e^{y^{2}}+2y^{2}e^{y^{2}}$$

两者相等，故积分与路径无关，**可以改走从 $O$ 到 $A$ 的直线段 $y=x$**。

**计算**（$y=x,dy=dx$）：
$$\\int_{O}^{A}=\\int_{0}^{1}\\left[xe^{x^{2}}+(xe^{x^{2}}+2x^{3}e^{x^{2}})\\right]dx
=\\underbrace{\\int_{0}^{1}2xe^{x^{2}}dx}_{I_{1}}+\\underbrace{\\int_{0}^{1}2x^{3}e^{x^{2}}dx}_{I_{2}}$$

$$I_{1}=\\left[e^{x^{2}}\\right]_{0}^{1}=e-1$$

$$I_{2}\\overset{u=x^{2}}{=}\\int_{0}^{1}ue^{u}du=\\left[(u-1)e^{u}\\right]_{0}^{1}=0-(-1)=1$$

**结论**：$\\displaystyle\\int_{L}=I_{1}+I_{2}=(e-1)+1=e$

**答案**：$e$

**注**：也可改走折线 $O(0,0)\\to B(1,0)\\to A(1,1)$：$OB$ 上 $y=0,dy=0$，积分为 $0$；$BA$ 上 $dx=0$，积分 $\\int_{0}^{1}(e^{y^{2}}+2y^{2}e^{y^{2}})dy$，用分部积分同样得 $e$。'''),

    dict(n=18, ch='tc', type='proof', diff='hard',
         cat='微分方程', topic='全微分方程·凑原函数',
         q='求解方程 $(5x^{4}+3xy^{2}-y^{3})dx+(3x^{2}y-3xy^{2}+y^{2})dy=0$ 的通解。',
         a='', opts=None,
         s='''**判别全微分**：
$$P=5x^{4}+3xy^{2}-y^{3},\\qquad Q=3x^{2}y-3xy^{2}+y^{2}$$
$$\\frac{\\partial P}{\\partial y}=6xy-3y^{2},\\qquad \\frac{\\partial Q}{\\partial x}=6xy-3y^{2}$$

两者相等，故为**全微分方程**，存在原函数 $U$ 使 $dU=P\\,dx+Q\\,dy$。

**求原函数**（取起点 $(0,0)$，走折线）：

$$U(x,y)=\\int_{(0,0)}^{(x,y)}P\\,dx+Q\\,dy$$

- 沿 $x$ 轴 $(0,0)\\to(x,0)$：$y=0,dy=0$
$$\\int_{0}^{x}5t^{4}dt=x^{5}$$

- 沿竖直线 $(x,0)\\to(x,y)$：$dx=0$
$$\\int_{0}^{y}(3x^{2}t-3xt^{2}+t^{2})dt=\\frac{3}{2}x^{2}y^{2}-xy^{3}+\\frac{1}{3}y^{3}$$

$$U(x,y)=x^{5}+\\frac{3}{2}x^{2}y^{2}-xy^{3}+\\frac{1}{3}y^{3}$$

**通解**：
$$x^{5}+\\frac{3}{2}x^{2}y^{2}-xy^{3}+\\frac{1}{3}y^{3}=C$$

**注**：折线法的关键在于走平行于坐标轴的折线，使每段上只有一个变量在变（$x$ 轴上 $dy=0$，竖直段上 $dx=0$），这样每段都是一元积分。'''),

    dict(n=19, ch='tc', type='fill', diff='hard',
         cat='曲线积分', topic='格林公式·变力做功',
         q='设平面曲线 $L$ 是从点 $O(0,0)$ 到点 $A(\\pi,\\pi)$ 的半圆弧，试求该平面内一质点在变力 $\\vec{F}=(e^{x}\\sin y-4y)\\vec{i}+(e^{x}\\cos y-1)\\vec{j}$ 作用下，沿圆弧 $L$ 从 $O$ 移动到 $A$ 所做的功。',
         a='$-\\pi^{3}-2\\pi^{2}-\\pi$', opts=None,
         s='''**物理意义**：变力做功 $W=\\displaystyle\\int_{L}P\\,dx+Q\\,dy$，其中
$$P=e^{x}\\sin y-4y,\\qquad Q=e^{x}\\cos y-1$$

**补线成闭**：补上有向线段 $AO$（从 $A$ 回到 $O$），与半圆弧 $L$ 围成半圆区域 $D$，闭曲线 $L+AO$ 是**负向**（顺时针）。

**用格林公式**：
$$\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y}=e^{x}\\cos y-(e^{x}\\cos y-4)=4$$

$$\\oint_{L+AO}=\\iint_{D}(-4)\\,dA=-4\\cdot|D|$$

半圆以 $OA$ 为直径，直径长 $\\sqrt{\\pi^{2}+\\pi^{2}}=\\sqrt{2}\\pi$，半径 $\\dfrac{\\sqrt{2}\\pi}{2}=\\dfrac{\\pi}{\\sqrt{2}}$，
$$|D|=\\frac{1}{2}\\pi\\left(\\frac{\\pi}{\\sqrt{2}}\\right)^{2}=\\frac{\\pi^{3}}{4}$$

故 $\\displaystyle\\oint_{L+AO}=-4\\cdot\\frac{\\pi^{3}}{4}=-\\pi^{3}$。

**减去补线段的贡献**：线段 $AO$ 在直线 $y=x$ 上，$x$ 从 $\\pi$ 到 $0$，

$$\\int_{AO}=\\int_{\\pi}^{0}\\left[(e^{x}\\sin x-4x)+(e^{x}\\cos x-1)\\right]dx$$

$$\\int_{0}^{\\pi}e^{x}\\sin x\\,dx=\\left[\\frac{e^{x}(\\sin x-\\cos x)}{2}\\right]_{0}^{\\pi}=\\frac{e^{\\pi}+1}{2}$$
$$\\int_{0}^{\\pi}e^{x}\\cos x\\,dx=\\left[\\frac{e^{x}(\\sin x+\\cos x)}{2}\\right]_{0}^{\\pi}=-\\frac{e^{\\pi}+1}{2}$$

两项相消，故
$$\\int_{AO}=-\\int_{0}^{\\pi}(-4x-1)dx=4\\cdot\\frac{\\pi^{2}}{2}+\\pi=2\\pi^{2}+\\pi$$

**结论**：
$$W=\\int_{L}=\\oint_{L+AO}-\\int_{AO}=-\\pi^{3}-(2\\pi^{2}+\\pi)=-\\pi^{3}-2\\pi^{2}-\\pi$$

**答案**：$-\\pi^{3}-2\\pi^{2}-\\pi$'''),

    dict(n=20, ch='tc', type='fill', diff='hard',
         cat='微分方程', topic='由线积分性质反推·欧拉型方程',
         q='设 $f(x)$ 具有二阶连续导数，$f(1)=f\'(1)=1$；且 $\\displaystyle\\oint_{L}\\left[\\frac{y^{2}}{x}+xf\\left(\\frac{y}{x}\\right)\\right]dx+\\left[y-xf\'\\left(\\frac{y}{x}\\right)\\right]dy=0$，其中 $L$ 是右半平面 $x>0$ 内任一光滑封闭曲线，求 $f(x)$。',
         a='$f(x)=x^{3}-x^{2}+1$', opts=None,
         s='''**把条件翻译成偏导等式**：闭曲线积分恒为零 $\\Leftrightarrow$ 积分与路径无关 $\\Leftrightarrow\\dfrac{\\partial P}{\\partial y}=\\dfrac{\\partial Q}{\\partial x}$。

$$P=\\frac{y^{2}}{x}+xf\\left(\\frac{y}{x}\\right),\\qquad Q=y-xf\'\\left(\\frac{y}{x}\\right)$$

$$\\frac{\\partial P}{\\partial y}=\\frac{2y}{x}+x\\cdot f\'\\left(\\frac{y}{x}\\right)\\cdot\\frac{1}{x}=\\frac{2y}{x}+f\'\\left(\\frac{y}{x}\\right)$$
$$\\frac{\\partial Q}{\\partial x}=-\\left[f\'\\left(\\frac{y}{x}\\right)+x\\cdot f\'\'\\left(\\frac{y}{x}\\right)\\cdot\\left(-\\frac{y}{x^{2}}\\right)\\right]=-f\'\\left(\\frac{y}{x}\\right)+\\frac{y}{x}f\'\'\\left(\\frac{y}{x}\\right)$$

令两者相等：
$$\\frac{2y}{x}+f\'\\left(\\frac{y}{x}\\right)=-f\'\\left(\\frac{y}{x}\\right)+\\frac{y}{x}f\'\'\\left(\\frac{y}{x}\\right)$$

**换元**：设 $t=\\dfrac{y}{x}$，整理得
$$t\\,f\'\'(t)-2f\'(t)=2t\\quad\\Rightarrow\\quad f\'\'(t)-\\frac{2}{t}f\'(t)=2$$

**降阶**：令 $u=f\'(t)$，得到一阶线性方程 $u\'-\\dfrac{2}{t}u=2$。

积分因子 $e^{\\int-\\frac{2}{t}dt}=t^{-2}$：
$$\\left(u\\,t^{-2}\\right)\'=2t^{-2}\\quad\\Rightarrow\\quad u\\,t^{-2}=-\\frac{2}{t}+C_{1}\\quad\\Rightarrow\\quad u=-2t+C_{1}t^{2}$$

即 $f\'(t)=-2t+C_{1}t^{2}$。由 $f\'(1)=1$：$-2+C_{1}=1$，得 $C_{1}=3$。

**再积分**：
$$f(t)=\\int(-2t+3t^{2})dt=-t^{2}+t^{3}+C_{2}$$

由 $f(1)=1$：$-1+1+C_{2}=1$，得 $C_{2}=1$。

**答案**：$f(x)=x^{3}-x^{2}+1$'''),

    dict(n=21, ch='tc', type='fill', diff='medium',
         cat='曲面积分', topic='第二类曲面积分·分面投影',
         q='计算曲面积分 $\\displaystyle\\iint_{\\Sigma}z\\,dxdy$，其中 $\\Sigma$ 是球面 $x^{2}+y^{2}+z^{2}=1$ 外侧在 $x\\ge0,y\\ge0$ 的部分。',
         a='$\\dfrac{\\pi}{3}$', opts=None,
         s='''**分面**：$\\Sigma$ 由上下两片组成
$$\\Sigma_{1}:\\ z=\\sqrt{1-x^{2}-y^{2}}\\ (\\text{上侧}),\\qquad \\Sigma_{2}:\\ z=-\\sqrt{1-x^{2}-y^{2}}\\ (\\text{下侧})$$

两者在 $xOy$ 面的投影都是 $D_{xy}=\\{(x,y)\\mid x\\ge0,y\\ge0,x^{2}+y^{2}\\le1\\}$（第一象限的 $\\frac{1}{4}$ 圆）。

**化为二重积分**（第二类曲面积分 $\\iint z\\,dxdy$，上侧取正、下侧取负）：
$$\\iint_{\\Sigma}z\\,dxdy=\\iint_{\\Sigma_{1}}z\\,dxdy+\\iint_{\\Sigma_{2}}z\\,dxdy$$
$$=\\iint_{D_{xy}}\\sqrt{1-x^{2}-y^{2}}\\,dxdy+\\iint_{D_{xy}}\\left(-\\sqrt{1-x^{2}-y^{2}}\\right)\\cdot(-1)\\,dxdy$$
$$=2\\iint_{D_{xy}}\\sqrt{1-x^{2}-y^{2}}\\,dxdy$$

**极坐标**：$D_{xy}$ 对应 $\\theta\\in\\left[0,\\dfrac{\\pi}{2}\\right],\\ r\\in[0,1]$：
$$=2\\int_{0}^{\\frac{\\pi}{2}}d\\theta\\int_{0}^{1}\\sqrt{1-r^{2}}\\cdot r\\,dr
=2\\cdot\\frac{\\pi}{2}\\cdot\\frac{1}{3}=\\frac{\\pi}{3}$$

（其中 $\\int_{0}^{1}r\\sqrt{1-r^{2}}dr=\\left[-\\dfrac{(1-r^{2})^{3/2}}{3}\\right]_{0}^{1}=\\dfrac{1}{3}$）

**答案**：$\\dfrac{\\pi}{3}$'''),

    dict(n=22, ch='tc', type='fill', diff='hard',
         cat='曲面积分', topic='高斯公式·补面法',
         q='计算曲面积分 $\\displaystyle\\iint_{\\Sigma}(z^{2}+x)\\,dydz-z\\,dxdy$，其中 $\\Sigma$ 是旋转抛物面 $z=x^{2}+y^{2}$ 介于平面 $z=0$ 与 $z=4$ 之间的部分的下侧。',
         a='$16\\pi$', opts=None,
         s='''**认清被积式**：$\\displaystyle\\iint_{\\Sigma}P\\,dydz+Q\\,dzdx+R\\,dxdy$，其中
$$P=z^{2}+x,\\qquad Q=0,\\qquad R=-z$$

**补面用高斯**：$\\Sigma$ 是下侧（不封闭），补上平面 $\\Sigma_{1}:z=4$ 的**上侧**，则 $\\Sigma+\\Sigma_{1}$ 围成闭区域 $\\Omega$（取外法向）。

$$\\frac{\\partial P}{\\partial x}+\\frac{\\partial Q}{\\partial y}+\\frac{\\partial R}{\\partial z}=1+0+(-1)=0$$

故由高斯公式：
$$\\iint_{\\Sigma+\\Sigma_{1}}=\\iiint_{\\Omega}0\\,dV=0\\quad\\Rightarrow\\quad \\iint_{\\Sigma}=-\\iint_{\\Sigma_{1}}$$

**算补面 $\\Sigma_{1}$ 的积分**：$\\Sigma_{1}$ 上 $z=4$（常数），

- $dydz$ 项：曲面是水平面，在 $yOz$ 面投影退化为线段，故 $\\displaystyle\\iint_{\\Sigma_{1}}(z^{2}+x)dydz=0$
- $dxdy$ 项：上侧取正，投影区域 $D_{xy}:x^{2}+y^{2}\\le4$
$$\\iint_{\\Sigma_{1}}-z\\,dxdy=-\\iint_{D_{xy}}4\\,dxdy=-4\\cdot\\pi\\cdot2^{2}=-16\\pi$$

**结论**：
$$\\iint_{\\Sigma}=-\\iint_{\\Sigma_{1}}=-(-16\\pi)=16\\pi$$

**答案**：$16\\pi$

**点睛**：本题散度恰为 $0$，所以补面后闭曲面积分为零，原积分直接等于补面积分的相反数——散度为 $0$ 的向量场，穿过任何闭曲面的通量为零，是高斯公式里最好用的一类。'''),

    dict(n=23, ch='tc', type='fill', diff='medium',
         cat='曲面积分', topic='第一类曲面积分·对称性与形心',
         q='计算 $\\displaystyle\\iint_{\\Sigma}(x^{2}+y^{2}+z^{2})\\,dS$，其中 $\\Sigma$ 为球面 $x^{2}+y^{2}+z^{2}=2z$。',
         a='$8\\pi$', opts=None,
         s='''**先化简被积函数**：曲面方程是 $x^{2}+y^{2}+z^{2}=2z$，即 $x^{2}+y^{2}+(z-1)^{2}=1$（球心 $(0,0,1)$、半径 $1$）。在 $\\Sigma$ 上恒有 $x^{2}+y^{2}+z^{2}=2z$，代入得

$$\\iint_{\\Sigma}(x^{2}+y^{2}+z^{2})dS=\\iint_{\\Sigma}2z\\,dS$$

**方法一：对称性**（推荐）

$\\Sigma$ 关于平面 $z=1$ 对称，故 $\\displaystyle\\iint_{\\Sigma}(z-1)dS=0$，于是
$$\\iint_{\\Sigma}2z\\,dS=2\\iint_{\\Sigma}\\left[(z-1)+1\\right]dS=2\\iint_{\\Sigma}1\\,dS=2\\cdot|\\Sigma|=2\\cdot4\\pi=8\\pi$$

（球面半径 $1$，表面积 $4\\pi R^{2}=4\\pi$）

**方法二：形心公式**

$$\\iint_{\\Sigma}z\\,dS=\\bar{z}\\cdot|\\Sigma|=1\\cdot4\\pi=4\\pi$$

故原式 $=2\\cdot4\\pi=8\\pi$。

**答案**：$8\\pi$

**点睛**：第一类（对面积的）曲面积分可以**把曲面方程代入被积函数**化简——因为积分变量在曲面上满足该关系。这一点与第一类曲线积分类似，但要注意与第二类积分区分开。'''),

    dict(n=24, ch='tc', type='fill', diff='hard',
         cat='曲线积分', topic='空间曲线积分·参数方程',
         q='计算曲线积分 $I=\\displaystyle\\oint_{L}y^{2}dx+z^{2}dy+x^{2}dz$，其中 $L$ 为曲线 $\\begin{cases}x^{2}+y^{2}+z^{2}=4\\\\ x^{2}+y^{2}=2x\\end{cases}\\ (z\\ge0)$，从 $z$ 轴正向看取逆时针方向。',
         a='$-2\\pi$', opts=None,
         s='''**求参数方程**：由 $x^{2}+y^{2}=2x$ 得 $(x-1)^{2}+y^{2}=1$，是母线平行于 $z$ 轴的圆柱面。

代入球面 $x^{2}+y^{2}+z^{2}=4$：$2x+z^{2}=4$，即 $z^{2}=4-2x$。

取参数 $\\theta$ 使 $x=1+\\cos\\theta,\\ y=\\sin\\theta$（$\\theta:0\\to2\\pi$），则
$$z^{2}=4-2(1+\\cos\\theta)=2-2\\cos\\theta=4\\sin^{2}\\frac{\\theta}{2}$$
由 $z\\ge0$ 得 $z=2\\sin\\dfrac{\\theta}{2}$。

$$x\'=-\\sin\\theta,\\qquad y\'=\\cos\\theta,\\qquad z\'=\\cos\\frac{\\theta}{2}$$

**代入积分**：
$$I=\\int_{0}^{2\\pi}\\left[\\sin^{2}\\theta\\cdot(-\\sin\\theta)+4\\sin^{2}\\frac{\\theta}{2}\\cdot\\cos\\theta+(1+\\cos\\theta)^{2}\\cdot\\cos\\frac{\\theta}{2}\\right]d\\theta$$

**第一项**：$\\displaystyle\\int_{0}^{2\\pi}-\\sin^{3}\\theta\\,d\\theta=0$

**第二项**（用 $\\sin^{2}\\frac{\\theta}{2}=\\frac{1-\\cos\\theta}{2}$）：
$$4\\int_{0}^{2\\pi}\\frac{1-\\cos\\theta}{2}\\cos\\theta\\,d\\theta=2\\int_{0}^{2\\pi}(\\cos\\theta-\\cos^{2}\\theta)d\\theta=2(0-\\pi)=-2\\pi$$

**第三项**（用 $1+\\cos\\theta=2\\cos^{2}\\frac{\\theta}{2}$）：
$$\\int_{0}^{2\\pi}4\\cos^{4}\\frac{\\theta}{2}\\cos\\frac{\\theta}{2}\\,d\\theta\\overset{\\varphi=\\theta/2}{=}8\\int_{0}^{\\pi}\\cos^{5}\\varphi\\,d\\varphi=0$$

**结论**：$I=0+(-2\\pi)+0=-2\\pi$

**答案**：$-2\\pi$'''),

    dict(n=25, ch='tc', type='fill', diff='hard',
         cat='曲线积分', topic='第一类曲线积分·质心',
         q='求八分之一球面 $x^{2}+y^{2}+z^{2}=R^{2}\\ (x\\ge0,y\\ge0,z\\ge0)$ 的边界曲线的质心（设密度为 $1$）。',
         a='$\\dfrac{4R}{3\\pi}$', opts=None,
         s='''**认清边界**：八分之一球面的边界由三段 $\\frac{1}{4}$ 圆弧组成，分别在三个坐标面上：
$$l_{1}:x^{2}+y^{2}=R^{2}(z=0),\\quad l_{2}:y^{2}+z^{2}=R^{2}(x=0),\\quad l_{3}:x^{2}+z^{2}=R^{2}(y=0)$$
记 $L=l_{1}+l_{2}+l_{3}$。

**质心公式**：
$$\\bar{x}=\\frac{\\oint_{L}x\\rho\\,ds}{\\oint_{L}\\rho\\,ds}=\\frac{\\oint_{L}x\\,ds}{\\oint_{L}ds}$$

**分母**（总弧长）：每段是 $\\frac{1}{4}$ 圆周，弧长 $\\dfrac{2\\pi R}{4}=\\dfrac{\\pi R}{2}$，
$$\\oint_{L}ds=3\\cdot\\frac{\\pi R}{2}=\\frac{3\\pi R}{2}$$

**分子**：
- 在 $l_{1}$（$z=0$）上，取 $x=R\\cos\\theta,\\ ds=R\\,d\\theta,\\ \\theta:0\\to\\frac{\\pi}{2}$：
$$\\int_{l_{1}}x\\,ds=R^{2}\\int_{0}^{\\frac{\\pi}{2}}\\cos\\theta\\,d\\theta=R^{2}$$
- 在 $l_{2}$（$x=0$）上：$x\\equiv0$，积分为 $0$
- 在 $l_{3}$（$y=0$）上，取 $x=R\\cos\\theta$：同理得 $R^{2}$

$$\\oint_{L}x\\,ds=R^{2}+0+R^{2}=2R^{2}$$

**质心**：由对称性 $\\bar{x}=\\bar{y}=\\bar{z}$，
$$\\bar{x}=\\frac{2R^{2}}{\\frac{3\\pi R}{2}}=\\frac{4R}{3\\pi}$$

**答案**：$\\bar{x}=\\bar{y}=\\bar{z}=\\dfrac{4R}{3\\pi}$，即质心为 $\\left(\\dfrac{4R}{3\\pi},\\dfrac{4R}{3\\pi},\\dfrac{4R}{3\\pi}\\right)$

**校注**：用 $xOy$ 面上的弧长微元直接算也行——在 $l_{1}$ 上 $ds=\\sqrt{1+\\left(\\frac{dy}{dx}\\right)^{2}}dx=\\dfrac{R}{\\sqrt{R^{2}-x^{2}}}dx$，则 $\\int_{0}^{R}x\\cdot\\dfrac{R}{\\sqrt{R^{2}-x^{2}}}dx=R^{2}$，结果一致。'''),

    dict(n=26, ch='tc', type='fill', diff='hard',
         cat='曲面积分', topic='第一类曲面积分·锥面·对称性',
         q='计算 $\\displaystyle\\iint_{\\Sigma}(xy+yz+zx)\\,dS$，其中 $\\Sigma$ 为圆锥面 $z=\\sqrt{x^{2}+y^{2}}$ 被圆柱面 $x^{2}+y^{2}=2x$ 所截的部分。',
         a='$\\dfrac{64\\sqrt{2}}{15}$', opts=None,
         s='''**投影区域**：柱面 $x^{2}+y^{2}=2x$ 即 $(x-1)^{2}+y^{2}=1$，故
$$D_{xy}=\\{(x,y)\\mid (x-1)^{2}+y^{2}\\le1\\}$$

**用对称性消去两项**：$\\Sigma$ 关于 $xOz$ 坐标面对称（$y\\to-y$ 不变），而 $xy$ 与 $yz$ 关于 $y$ 是奇函数，故
$$\\iint_{\\Sigma}xy\\,dS=\\iint_{\\Sigma}yz\\,dS=0$$

于是
$$\\iint_{\\Sigma}(xy+yz+zx)dS=\\iint_{\\Sigma}zx\\,dS$$

**面积微元**：$z=\\sqrt{x^{2}+y^{2}}$，$z_{x}=\\dfrac{x}{\\sqrt{x^{2}+y^{2}}},\\ z_{y}=\\dfrac{y}{\\sqrt{x^{2}+y^{2}}}$
$$dS=\\sqrt{1+z_{x}^{2}+z_{y}^{2}}\\,dxdy=\\sqrt{1+\\frac{x^{2}}{x^{2}+y^{2}}+\\frac{y^{2}}{x^{2}+y^{2}}}\\,dxdy=\\sqrt{2}\\,dxdy$$

**化为二重积分并转极坐标**：
$$\\iint_{\\Sigma}zx\\,dS=\\iint_{D_{xy}}\\sqrt{x^{2}+y^{2}}\\cdot x\\cdot\\sqrt{2}\\,dxdy$$

$D$ 的极坐标表示：$r^{2}=2r\\cos\\theta$，即 $r=2\\cos\\theta,\\ \\theta\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$：
$$=\\sqrt{2}\\int_{-\\frac{\\pi}{2}}^{\\frac{\\pi}{2}}d\\theta\\int_{0}^{2\\cos\\theta}r\\cos\\theta\\cdot r\\cdot r\\,dr
=\\sqrt{2}\\int_{-\\frac{\\pi}{2}}^{\\frac{\\pi}{2}}\\cos\\theta\\cdot\\frac{(2\\cos\\theta)^{4}}{4}\\,d\\theta$$
$$=4\\sqrt{2}\\int_{-\\frac{\\pi}{2}}^{\\frac{\\pi}{2}}\\cos^{5}\\theta\\,d\\theta
=4\\sqrt{2}\\cdot2\\int_{0}^{\\frac{\\pi}{2}}\\cos^{5}\\theta\\,d\\theta
=8\\sqrt{2}\\cdot\\frac{8}{15}=\\frac{64\\sqrt{2}}{15}$$

（用到 $\\int_{0}^{\\pi/2}\\cos^{5}\\theta\\,d\\theta=\\dfrac{4}{5}\\cdot\\dfrac{2}{3}\\cdot1=\\dfrac{8}{15}$）

**答案**：$\\dfrac{64\\sqrt{2}}{15}$'''),

    dict(n=27, ch='tc', type='fill', diff='medium',
         cat='曲面积分', topic='第二类曲面积分·分面投影',
         q='设 $\\Sigma$ 是球面 $x^{2}+y^{2}+z^{2}=1\\ (x\\ge0,y\\ge0)$ 的外侧，求曲面积分 $\\displaystyle\\iint_{\\Sigma}xyz\\,dxdy$。',
         a='$\\dfrac{2}{15}$', opts=None,
         s='''**分面**：$\\Sigma$ 由上下两片组成
$$\\Sigma_{1}:z=\\sqrt{1-x^{2}-y^{2}}\\ (\\text{上侧}),\\qquad \\Sigma_{2}:z=-\\sqrt{1-x^{2}-y^{2}}\\ (\\text{下侧})$$

**注意投影区域**：因为 $\\Sigma$ 只取 $x\\ge0,y\\ge0$ 的部分，两片在 $xOy$ 面的投影是
$$D_{xy}=\\{(x,y)\\mid x\\ge0,\\ y\\ge0,\\ x^{2}+y^{2}\\le1\\}$$
即第一象限的 $\\frac{1}{4}$ 圆（不是整个圆）。

**化为二重积分**（上侧取正、下侧取负）：
$$\\iint_{\\Sigma}xyz\\,dxdy=\\iint_{D_{xy}}xy\\sqrt{1-x^{2}-y^{2}}\\,dxdy+\\iint_{D_{xy}}xy(-\\sqrt{1-x^{2}-y^{2}})\\cdot(-1)\\,dxdy$$
$$=2\\iint_{D_{xy}}xy\\sqrt{1-x^{2}-y^{2}}\\,dxdy$$

**极坐标**（$D_{xy}$ 对应 $\\theta\\in\\left[0,\\dfrac{\\pi}{2}\\right],\\ r\\in[0,1]$）：
$$=2\\int_{0}^{\\frac{\\pi}{2}}d\\theta\\int_{0}^{1}r\\cos\\theta\\cdot r\\sin\\theta\\cdot\\sqrt{1-r^{2}}\\cdot r\\,dr$$
$$=2\\left(\\int_{0}^{\\frac{\\pi}{2}}\\cos\\theta\\sin\\theta\\,d\\theta\\right)\\left(\\int_{0}^{1}r^{3}\\sqrt{1-r^{2}}\\,dr\\right)$$

前者 $=\\dfrac{1}{2}$；后者令 $u=1-r^{2}$：
$$\\int_{0}^{1}r^{3}\\sqrt{1-r^{2}}dr=\\frac{1}{2}\\int_{0}^{1}(1-u)u^{1/2}du=\\frac{1}{2}\\left(\\frac{2}{3}-\\frac{2}{5}\\right)=\\frac{2}{15}$$

$$\\iint_{\\Sigma}xyz\\,dxdy=2\\cdot\\frac{1}{2}\\cdot\\frac{2}{15}=\\frac{2}{15}$$

**答案**：$\\dfrac{2}{15}$

**校注**：这一步的 $\\theta$ 上限必须随 $x\\ge0,y\\ge0$ 写 $\\dfrac{\\pi}{2}$。若误写成 $[0,2\\pi]$，则 $\\int_{0}^{2\\pi}\\cos\\theta\\sin\\theta\\,d\\theta=0$，会得到 $0$（与第一象限外的部分正负相消）——结果就错了。'''),
]
