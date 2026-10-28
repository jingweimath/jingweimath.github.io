# -*- coding: utf-8 -*-
r"""独立数值验证：老板新改的第 2 题与第 4 题。

验证路径与推导路径完全分离：
  - 题 2 不做变量代换，直接对原被积函数 sin(t-x) 自适应积分，再除以 x^2
  - 题 4 不做变量代换，直接对原被积函数 arctan(tx) 自适应积分，再除以 x
判定用「两尺度 + 收敛阶自洽」：d2 < 1e-6 且实测阶 p > 0.5
"""
import mpmath as mp

mp.mp.dps = 60
PASS = 0
FAIL = 0


def limit_chk(n, desc, claimed, f, xs):
    """f 接受 x 返回表达式数值；xs 为 (粗尺度, 细尺度)"""
    global PASS, FAIL
    claim = mp.mpf(claimed)
    x1, x2 = mp.mpf(xs[0]), mp.mpf(xs[1])
    v1, v2 = f(x1), f(x2)
    d1, d2 = abs(v1 - claim), abs(v2 - claim)
    ratio = abs(x1 / x2) if abs(x1) > abs(x2) else abs(x2 / x1)
    p = mp.log(d1 / d2) / mp.log(ratio) if d2 > 0 else mp.mpf('inf')
    ok = (d2 < mp.mpf('1e-6')) and (p > mp.mpf('0.5'))
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print('题 %-3d %-42s 声称=%s' % (n, desc, mp.nstr(claim, 10)))
    print('      x=%-9s 数值=%s  偏差=%.3e' % (mp.nstr(x1, 3), mp.nstr(v1, 14), float(d1)))
    print('      x=%-9s 数值=%s  偏差=%.3e' % (mp.nstr(x2, 3), mp.nstr(v2, 14), float(d2)))
    print('      实测收敛阶 p=%.2f   判定 %s' % (float(p), 'PASS' if ok else 'FAIL'))
    print()


# ---- 题 2：lim_{x->0} (int_0^x sin(t-x) dt) / x^2 ，声称 -1/2 ----
# 原样积分，不做代换。理论渐近： (cos x - 1)/x^2 = -1/2 + x^2/24 - ... -> 误差 O(x^2)
def f2(x):
    return mp.quad(lambda t: mp.sin(t - x), [0, x]) / x**2


limit_chk(2, 'int_0^x sin(t-x)dt / x^2', '-0.5', f2, ('0.002', '0.001'))

# ---- 题 4：lim_{x->0} (int_0^1 arctan(tx) dt) / x ，声称 1/2 ----
# 理论渐近： 1/2 - x^2/9 + ... -> 误差 O(x^2)
def f4(x):
    return mp.quad(lambda t: mp.atan(t * x), [0, 1]) / x


limit_chk(4, 'int_0^1 arctan(tx)dt / x', '0.5', f4, ('0.002', '0.001'))

print('=' * 60)
print('PASS %d / FAIL %d' % (PASS, FAIL))

# 附带：把两个原函数直接积出来作交叉印证（用与推导不同的闭式路径）
for x in ('0.01', '0.001'):
    xv = mp.mpf(x)
    # 题2 闭式：cos x - 1
    print('题2 x=%s  数值积分=%s   闭式(cosx-1)/x^2=%s'
          % (x, mp.nstr(f2(xv), 14), mp.nstr((mp.cos(xv) - 1) / xv**2, 14)))
    # 题4 闭式：arctan(x) - ln(1+x^2)/(2x)  ... 由 ∫_0^1 arctan(tx)dt 直接算
    #   ∫ arctan(tx)dt = t*arctan(tx) - ln(1+t^2x^2)/(2x)，t:0->1
    closed = (mp.atan(xv) - mp.log(1 + xv**2) / (2 * xv)) / xv
    print('题4 x=%s  数值积分=%s   闭式=%s'
          % (x, mp.nstr(f4(xv), 14), mp.nstr(closed, 14)))
