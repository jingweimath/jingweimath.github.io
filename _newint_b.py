# -*- coding: utf-8 -*-
r"""反常积分 10 题 —— 第 11~17 题
字段：n 题号 / type / diff / cat / topic / q 题面 / a 答案 / opts 选项 / s 详解
"""
B = [
 dict(n=11, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·分部积分',
      q=r'计算 $\int_{0}^{+\infty}xe^{-x}\,dx$。',
      a=r'$1$',
      s=r'分部积分：'
        r'$$\int_{0}^{A}xe^{-x}dx=\bigl[-xe^{-x}\bigr]_{0}^{A}+\int_{0}^{A}e^{-x}dx'
        r'=-Ae^{-A}+\left(1-e^{-A}\right).$$'
        r'令 $A\to+\infty$，$Ae^{-A}\to0$（指数衰减快于幂增长），$e^{-A}\to0$，故值为 $1$。'
        r'**推广**：$\int_0^{+\infty}x^ne^{-x}dx=n!$（$n$ 为正整数），本题 $n=1$。'),

 dict(n=12, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·部分分式',
      q=r'计算 $\int_{1}^{+\infty}\dfrac{1}{x(x+1)}\,dx$。',
      a=r'$\ln 2$',
      s=r'先部分分式：$\dfrac{1}{x(x+1)}=\dfrac{1}{x}-\dfrac{1}{x+1}$。'
        r'$$\int_{1}^{A}\left(\frac{1}{x}-\frac{1}{x+1}\right)dx'
        r'=\left[\ln\frac{x}{x+1}\right]_{1}^{A}=\ln\frac{A}{A+1}-\ln\frac{1}{2}.$$'
        r'令 $A\to+\infty$，$\dfrac{A}{A+1}\to1$，$\ln\dfrac{A}{A+1}\to0$，故值为 $\ln 2$。'
        r'**易错点**：不要分别算 $\int_1^\infty\dfrac1x dx$ 与 $\int_1^\infty\dfrac1{x+1}dx$——'
        r'两个都发散，$\infty-\infty$ 没有意义；必须先合成一个对数再取极限。'),

 dict(n=13, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·瑕积分',
      q=r'计算 $\int_{0}^{1}\dfrac{1}{\sqrt{x}}\,dx$。',
      a=r'$2$',
      s=r'$x=0$ 是**瑕点**（被积函数无界），按瑕积分定义：'
        r'$$\int_{0}^{1}\frac{1}{\sqrt{x}}dx=\lim_{\varepsilon\to0^{+}}\int_{\varepsilon}^{1}x^{-1/2}dx'
        r'=\lim_{\varepsilon\to0^{+}}\bigl[2\sqrt{x}\bigr]_{\varepsilon}^{1}'
        r'=\lim_{\varepsilon\to0^{+}}\left(2-2\sqrt{\varepsilon}\right)=2.$$'
        r'**结论**：$\int_0^1\dfrac{dx}{x^q}$ 当 $q<1$ 时收敛于 $\dfrac{1}{1-q}$，'
        r'当 $q\ge1$ 时发散。本题 $q=\dfrac12$，值为 $2$。'
        r'**提醒**：瑕积分与无穷限积分的判别条件形式相反，别记串。'),

 dict(n=14, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·分部积分',
      q=r'计算 $\int_{0}^{+\infty}e^{-x}\sin x\,dx$。',
      a=r'$\dfrac{1}{2}$',
      s=r'连续两次分部积分后自解。对 $A>0$：'
        r'$$\int_{0}^{A}e^{-x}\sin x\,dx'
        r'=\bigl[-e^{-x}\sin x\bigr]_{0}^{A}+\int_{0}^{A}e^{-x}\cos x\,dx,$$'
        r'$$\int_{0}^{A}e^{-x}\cos x\,dx'
        r'=\bigl[-e^{-x}\cos x\bigr]_{0}^{A}-\int_{0}^{A}e^{-x}\sin x\,dx.$$'
        r'令 $A\to+\infty$，带因子 $e^{-A}$ 的项均趋于 $0$，记 '
        r'$I=\int_{0}^{+\infty}e^{-x}\sin x\,dx$，则第二式给出 $I=1-I$，'
        r'故 $2I=1$，$I=\dfrac{1}{2}$。'
        r'**公式记忆**：$\int_0^{+\infty}e^{-ax}\sin bx\,dx=\dfrac{b}{a^{2}+b^{2}}$（$a>0$）。'
        r'本题 $a=b=1$，得 $\dfrac{1}{2}$。'),

 dict(n=15, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·三角代换',
      q=r'计算 $\int_{0}^{+\infty}\dfrac{1}{(1+x^{2})^{2}}\,dx$。',
      a=r'$\dfrac{\pi}{4}$',
      s=r'令 $x=\tan\theta$，则 $dx=\sec^{2}\theta\,d\theta$、$(1+x^{2})^{2}=\sec^{4}\theta$，'
        r'积分限 $x:0\to+\infty$ 对应 $\theta:0\to\dfrac{\pi}{2}$：'
        r'$$\int_{0}^{+\infty}\frac{dx}{(1+x^{2})^{2}}'
        r'=\int_{0}^{\pi/2}\frac{\sec^{2}\theta}{\sec^{4}\theta}\,d\theta'
        r'=\int_{0}^{\pi/2}\cos^{2}\theta\,d\theta$$'
        r'$$=\int_{0}^{\pi/2}\frac{1+\cos 2\theta}{2}\,d\theta'
        r'=\left[\frac{\theta}{2}+\frac{\sin 2\theta}{4}\right]_{0}^{\pi/2}=\frac{\pi}{4}.$$'
        r'**方法点睛**：三角代换把无穷区间变成了有限区间 $\left[0,\dfrac{\pi}{2}\right]$，'
        r'这是处理 $\dfrac{1}{(a^2+x^2)^n}$ 型反常积分的标准手法。'),

 dict(n=16, type='fill', diff='basic',
      cat='一元函数积分学', topic='反常积分·分部积分与 Dirichlet 积分',
      q=r'已知 $\int_{0}^{+\infty}\dfrac{\sin x}{x}\,dx=\dfrac{\pi}{2}$，'
        r'求 $\int_{0}^{+\infty}\dfrac{\sin^{2}x}{x^{2}}\,dx$。',
      a=r'$\dfrac{\pi}{2}$',
      s=r'分部积分，取 $u=\sin^{2}x$、$dv=\dfrac{1}{x^{2}}dx$（则 $v=-\dfrac{1}{x}$）：'
        r'$$\int_{\varepsilon}^{A}\frac{\sin^{2}x}{x^{2}}dx'
        r'=\left[-\frac{\sin^{2}x}{x}\right]_{\varepsilon}^{A}'
        r'+\int_{\varepsilon}^{A}\frac{2\sin x\cos x}{x}\,dx.$$'
        r'取极限：端点项在 $A\to+\infty$ 时趋于 $0$（有界量除以 $A$），'
        r'在 $\varepsilon\to0^{+}$ 时 $\dfrac{\sin^2\varepsilon}{\varepsilon}\to0$（因 $\sin^2 x\sim x^2$），故端点项消失。'
        r'于是 $$I=\int_{0}^{+\infty}\frac{\sin 2x}{x}\,dx.$$'
        r'令 $t=2x$：'
        r'$$I=\int_{0}^{+\infty}\frac{\sin t}{t/2}\cdot\frac{dt}{2}=\int_{0}^{+\infty}\frac{\sin t}{t}\,dt=\frac{\pi}{2}.$$'
        r'**要点**：$x=0$ 不是瑕点，因为 $\dfrac{\sin^2x}{x^2}\to1$；'
        r'无穷远处收敛靠 $\dfrac{1}{x^2}$ 的衰减，被积函数非负故绝对收敛。'),

 dict(n=17, type='proof', diff='medium',
      cat='一元函数积分学', topic='反常积分·收敛性判定与分部积分',
      q=r'证明反常积分 $\int_{1}^{+\infty}\dfrac{\ln x}{x^{2}}\,dx$ 收敛，并求其值。',
      a=r'$1$',
      s=r'**证明（分部积分法）**：对 $A>1$，'
        r'$$\int_{1}^{A}\frac{\ln x}{x^{2}}dx=\int_{1}^{A}\ln x\,d\left(-\frac{1}{x}\right)$$'
        r'$$=\left[-\frac{\ln x}{x}\right]_{1}^{A}+\int_{1}^{A}\frac{1}{x}\cdot\frac{1}{x}\,dx'
        r'=-\frac{\ln A}{A}+0+\int_{1}^{A}\frac{1}{x^{2}}\,dx$$'
        r'$$=-\frac{\ln A}{A}+\left(1-\frac{1}{A}\right).$$'
        r'当 $A\to+\infty$ 时，$\dfrac{\ln A}{A}\to0$（对数增长慢于幂增长）、$\dfrac{1}{A}\to0$，'
        r'故极限存在且有限，积分**收敛**，值为 $1$。'

        r'**另证（比较判别法）**：当 $x$ 充分大时 $\ln x\le\sqrt{x}$，于是'
        r'$$\frac{\ln x}{x^{2}}\le\frac{\sqrt{x}}{x^{2}}=\frac{1}{x^{3/2}},$$'
        r'而 $\int_1^{+\infty}\dfrac{dx}{x^{3/2}}$ 收敛（$p=\dfrac32>1$），由比较判别法知原积分收敛。'
        r'（此证法只判收敛，要求值仍用上面的分部积分。）'

        r'**结论**：$\int_1^{+\infty}\dfrac{\ln x}{x^2}dx=1$。'),
]
