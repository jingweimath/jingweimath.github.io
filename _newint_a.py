# -*- coding: utf-8 -*-
r"""变限积分（分式型）10 题 —— 第 1~10 题
字段：n 题号 / type / diff / cat / topic / q 题面 / a 答案 / opts 选项 / s 详解
"""
# —— 第 1~10 题：变限积分出现在分式（分子或分母）中 ——
A = [
 dict(n=1, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·洛必达法则',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}\sin 2t\,dt}{x^{2}}$。',
      a=r'$1$',
      s=r'$\dfrac{0}{0}$ 型，洛必达：'
        r'$$\lim_{x\to 0}\frac{\int_{0}^{x}\sin 2t\,dt}{x^{2}}'
        r'=\lim_{x\to 0}\frac{\sin 2x}{2x}=1,$$'
        r'最后一步用等价无穷小 $\sin 2x\sim 2x\ (x\to0)$。'
        r'**易错点**：被积函数是 $\sin 2t$ 不是 $\sin t$，'
        r'洛必达后得到的是 $\dfrac{\sin 2x}{2x}$ 而不是 $\dfrac{\sin 2x}{x}$；'
        r'漏掉系数 2 会得出 $\dfrac{1}{2}$ 的错误结果。'),

 dict(n=2, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·卷积型变量代换后洛必达',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}\sin(t-x)\,dt}{x^{2}}$。',
      a=r'$-\dfrac{1}{2}$',
      s=r'这是 $\dfrac{0}{0}$ 型。注意这里的 $x$ 既是积分上限、又出现在被积函数内部'
        r'（$\sin(t-x)$ 是「卷积型」），**先做变量代换把 $x$ 从被积函数里挪到积分限上**，'
        r'再用洛必达。'
        r'令 $u=x-t$，则 $t=0$ 时 $u=x$、$t=x$ 时 $u=0$，且 $dt=-du$、$\sin(t-x)=-\sin u$，'
        r'$$\int_{0}^{x}\sin(t-x)\,dt=\int_{x}^{0}(-\sin u)(-du)=\int_{x}^{0}\sin u\,du'
        r'=-\int_{0}^{x}\sin u\,du.$$'
        r'于是'
        r'$$\lim_{x\to 0}\frac{\int_{0}^{x}\sin(t-x)\,dt}{x^{2}}'
        r'=\lim_{x\to 0}\frac{-\int_{0}^{x}\sin u\,du}{x^{2}}'
        r'=\lim_{x\to 0}\frac{-\sin x}{2x}=-\frac{1}{2}.$$'
        r'**方法点睛（本题考点）**：被积函数是 $\sin(t-x)$、$\arctan(tx)$ 这类'
        r'「参数 $x$ 嵌在被积函数内部」的形式时，必须**先变量代换**、把 $x$ 移到积分限上，'
        r'再用 $\bigl(\int_{a}^{\varphi(x)}f(t)\,dt\bigr)^{\prime}=f[\varphi(x)]\varphi^{\prime}(x)$ 求导。'
        r'若跳过代换直接对 $x$ 求导，就要用积分号下求导（莱布尼茨公式），既容易漏项，'
        r'也不在考纲要求的常规路径上。'),

 dict(n=3, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·洛必达法则',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}\sin t^{2}\,dt}{x^{3}}$。',
      a=r'$\dfrac{1}{3}$',
      s=r'被积函数 $\sin t^2$ 没有初等原函数，**不能先积分**，直接洛必达：'
        r'$$\lim_{x\to 0}\frac{\int_{0}^{x}\sin t^{2}\,dt}{x^{3}}'
        r'=\lim_{x\to 0}\frac{\sin x^{2}}{3x^{2}}=\frac{1}{3}.$$'
        r'**方法点睛**：这类题的通用套路是「洛必达一次 → 等价无穷小收尾」，'
        r'$\dfrac{d}{dx}\int_a^x f(t)\,dt=f(x)$ 这一步把积分号直接消掉。'),

 dict(n=4, type='choice', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·卷积型变量代换后洛必达',
      q=r'$\lim_{x\to 0}\dfrac{\int_{0}^{1}\arctan(tx)\,dt}{x}$ 的值为（　　）',
      opts=[r'$0$', r'$\dfrac{1}{2}$', r'$1$', r'不存在'],
      a=1,
      s=r'选 **B**。这是 $\dfrac{0}{0}$ 型，但 $x$ 嵌在被积函数 $\arctan(tx)$ 内部，'
        r'**先做变量代换把 $x$ 移出被积函数、落到积分限上**，再用洛必达。'
        r'令 $u=tx$，则 $dt=\dfrac{du}{x}$；$t=0$ 时 $u=0$，$t=1$ 时 $u=x$，'
        r'$$\int_{0}^{1}\arctan(tx)\,dt=\frac{1}{x}\int_{0}^{x}\arctan u\,du.$$'
        r'于是'
        r'$$\lim_{x\to 0}\frac{\int_{0}^{1}\arctan(tx)\,dt}{x}'
        r'=\lim_{x\to 0}\frac{\int_{0}^{x}\arctan u\,du}{x^{2}}'
        r'=\lim_{x\to 0}\frac{\arctan x}{2x}=\frac{1}{2},$$'
        r'最后一步用等价无穷小 $\arctan x\sim x$。'
        r'**方法点睛（本题考点）**：$x$ 是被积函数里的参数时，积分限（这里是从 0 到 1）'
        r'与 $x$ 无关，直接洛必达就要算 $\dfrac{d}{dx}\int_{0}^{1}\arctan(tx)\,dt'
        r'=\int_{0}^{1}\dfrac{t}{1+t^{2}x^{2}}\,dt=\dfrac{\ln(1+x^{2})}{2x^{2}}$，'
        r'中间又冒出一个 $\dfrac{0}{0}$，还得再算一次；'
        r'先代换则一步到位、只做一次洛必达。'),

 dict(n=5, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分作分母·等价无穷小',
      q=r'求 $\lim_{x\to 0}\dfrac{x-\sin x}{\int_{0}^{x}t\sin t\,dt}$。',
      a=r'$\dfrac{1}{2}$',
      s=r'**变限积分在分母**上。分子分母都趋于 0，可用等价无穷小直接比阶：'
        r'$$x-\sin x\sim\frac{x^{3}}{6},\qquad'
        r'\int_{0}^{x}t\sin t\,dt\sim\int_{0}^{x}t\cdot t\,dt=\frac{x^{3}}{3}.$$'
        r'故 $$\lim_{x\to0}\frac{x-\sin x}{\int_0^x t\sin t\,dt}'
        r'=\frac{1/6}{1/3}=\frac{1}{2}.$$'
        r'**方法点睛**：分母是变限积分时，先用等价无穷小把被积函数替换为幂函数，'
        r'积分就变成了普通幂函数积分，比连做三次洛必达干净得多。'

        r'（若用洛必达：$\dfrac{1-\cos x}{x\sin x}\to\dfrac{\sin x}{\sin x+x\cos x}'
        r'\to\dfrac{\cos x}{2\cos x-x\sin x}\to\dfrac12$，需三次。）'),

 dict(n=6, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分作分母·等价无穷小',
      q=r'求 $\lim_{x\to 0}\dfrac{\tan x-x}{\int_{0}^{x}t^{2}\cos t\,dt}$。',
      a=r'$1$',
      s=r'**变限积分在分母**。用等价无穷小定阶：'
        r'$$\tan x-x\sim\frac{x^{3}}{3},\qquad'
        r'\int_{0}^{x}t^{2}\cos t\,dt\sim\int_{0}^{x}t^{2}\,dt=\frac{x^{3}}{3}.$$'
        r'故极限 $=\dfrac{1/3}{1/3}=1$。'
        r'**易错点**：$\tan x-x$ 的主部是 $\dfrac{x^3}{3}$ 而不是 $\dfrac{x^3}{6}$'
        r'（后者是 $x-\sin x$ 的），记混了答案会差一倍。'),

 dict(n=7, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·洛必达法则',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}(e^{t^{2}}-1)\,dt}{x^{3}}$。',
      a=r'$\dfrac{1}{3}$',
      s=r'被积函数 $e^{t^2}-1$ 无初等原函数，用洛必达：'
        r'$$\lim_{x\to 0}\frac{\int_{0}^{x}(e^{t^{2}}-1)\,dt}{x^{3}}'
        r'=\lim_{x\to 0}\frac{e^{x^{2}}-1}{3x^{2}}=\frac{1}{3},$$'
        r'最后一步用 $e^{u}-1\sim u$（这里 $u=x^2\to0$）。'),

 dict(n=8, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·泰勒展开',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}\cos t^{2}\,dt-x}{x^{5}}$。',
      a=r'$-\dfrac{1}{10}$',
      s=r'**要用泰勒展开**，因为本题洛必达一次后是 $\dfrac{\cos x^2-1}{5x^4}$，'
        r'再做下去会越来越繁。直接对被积函数展开：'
        r'$$\cos t^{2}=1-\frac{(t^{2})^{2}}{2!}+o(t^{4})=1-\frac{t^{4}}{2}+o(t^{4}),$$'
        r'逐项积分：'
        r'$$\int_{0}^{x}\cos t^{2}\,dt=\int_{0}^{x}\left(1-\frac{t^{4}}{2}+o(t^{4})\right)dt'
        r'=x-\frac{x^{5}}{10}+o(x^{5}).$$'
        r'代入：$$\lim_{x\to0}\frac{\left(x-\dfrac{x^{5}}{10}+o(x^{5})\right)-x}{x^{5}}'
        r'=-\frac{1}{10}.$$'
        r'**易错点**：分子两个主项恰好相消（都是 $x$），必须保留到 $x^5$ 项；'
        r'只展开到 $\cos t^2=1+o(1)$ 会得出「极限为 0」的错误结论。'),

 dict(n=9, type='fill', diff='basic',
      cat='一元函数积分学', topic='变限积分求极限·泰勒展开',
      q=r'求 $\lim_{x\to 0}\dfrac{\int_{0}^{x}\dfrac{\sin t}{t}\,dt-x}{x^{3}}$。',
      a=r'$-\dfrac{1}{18}$',
      s=r'被积函数 $\dfrac{\sin t}{t}$ 无初等原函数（它的原函数是正弦积分 $\mathrm{Si}$），'
        r'只能展开逐项积分：'
        r'$$\frac{\sin t}{t}=\frac{t-\dfrac{t^{3}}{6}+o(t^{3})}{t}'
        r'=1-\frac{t^{2}}{6}+o(t^{2}),$$'
        r'$$\int_{0}^{x}\frac{\sin t}{t}\,dt=x-\frac{x^{3}}{18}+o(x^{3}).$$'
        r'故 $$\lim_{x\to0}\frac{\left(x-\dfrac{x^{3}}{18}+o(x^{3})\right)-x}{x^{3}}'
        r'=-\frac{1}{18}.$$'
        r'**方法点睛**：$\dfrac{\sin t}{t}$ 在 $t=0$ 处是可去奇点，补充定义值为 1，'
        r'积分本身没有瑕点。'),

 dict(n=10, type='fill', diff='basic',
      cat='一元函数积分学', topic='积分上限函数·渐近分析与洛必达',
      q=r'求 $\lim_{x\to +\infty}\dfrac{x\int_{0}^{x}e^{t^{2}}\,dt}{e^{x^{2}}}$。',
      a=r'$\dfrac{1}{2}$',
      s=r'这是 $\dfrac{\infty}{\infty}$ 型。对分子用乘积求导法则：'
        r'$$\bigl(x\int_{0}^{x}e^{t^{2}}\,dt\bigr)^{\prime}=\int_{0}^{x}e^{t^{2}}\,dt+xe^{x^{2}},'
        r'\qquad (e^{x^{2}})^{\prime}=2xe^{x^{2}}.$$'
        r'洛必达后拆成两项：'
        r'$$\frac{\int_{0}^{x}e^{t^{2}}dt+xe^{x^{2}}}{2xe^{x^{2}}}'
        r'=\underbrace{\frac{xe^{x^{2}}}{2xe^{x^{2}}}}_{=\frac12}'
        r'+\frac{\int_{0}^{x}e^{t^{2}}dt}{2xe^{x^{2}}}.$$'
        r'对余项再用一次洛必达：'
        r'$$\lim_{x\to+\infty}\frac{e^{x^{2}}}{2e^{x^{2}}+4x^{2}e^{x^{2}}}'
        r'=\lim_{x\to+\infty}\frac{1}{2+4x^{2}}=0.$$'
        r'故原极限 $=\dfrac12+0=\dfrac12$。'
        r'**结论记忆**：$\int_0^x e^{t^2}dt\sim\dfrac{e^{x^2}}{2x}\ (x\to+\infty)$，'
        r'即 $x\int_0^xe^{t^2}dt\sim\dfrac{e^{x^2}}{2}$。'
        r'**易错点**：洛必达后如果不拆项、直接对整式再洛必达，会陷入死循环。'),
]
