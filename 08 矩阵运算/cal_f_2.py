# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/26 18:28
# @Author    :   Chasion
# Description:
import sympy as sp
import numpy as np


# n -- > eta
n1, n2, r1, r2 = sp.symbols('n1, n2, r1, r2')
x, c,  h, cgps = sp.symbols('x, c,  h, cgps')
a2, a3, a4, l2, l3, l4, h2, h3, h4 = sp.symbols('a2, a3, a4, l2, l3, l4, h2, h3, h4')
u2, u3, u4 = sp.symbols('u2, u3, u4')

l1 = (n1 * r2 + n2 * r1) / (r1 + r2)
# r_l1 = l1.evalf(subs={n1:50, n2:30, r1:0.2, r2:0.8})
# print('l1:', r_l1)
tx = h4 * x / ((c - l1 - l2 - l3 - l4) * (h4 - 1))
# r_tx = tx.evalf(subs={n1:50, a2:1.0, a3:1.0, a4:0.5, r1:0.2, h2:0.8, h3:0.8, h4:0.8, n2:30, l2:60, l3:26, l4:50, r2:0.8, c:200, u2:0.4, u3:0.4, u4:0.2})
# print('rtx', r_tx)
v1 = (n1 * r2 + n2 * r1) ** 2 * tx**2 / (r1 + r2) ** 2 + 2 * (n1 - n2) * r1 * r2 * tx / (r1 + r2) ** 3 - 2 * (n1 - n2) ** 2 * r1 * r2 * (1 - sp.exp(-(r1 + r2) * tx)) / (r1 + r2) ** 4

sx = h4 * x / ((cgps - l2 - l3 - l4) * (h4 - 1))

v2 = a2 * l2 * tx ** (2*h2)
v3 = a3 * l3 * tx ** (2*h3)
v4 = a4 * l4 * tx ** (2*h4)

vs2 = a2 * l2 * sx ** (2*h2)
vs3 = a3 * l3 * sx ** (2*h3)
vs4 = a4 * l4 * sx ** (2*h4)


theta = (-x + (c - l1 - l2 - l3 - l4) * tx) ** 2 / (v1 + v2 + v3 + v4)
r_theta = theta.evalf(subs={n1:50, a2:1.0, a3:1.0, a4:0.5, r1:0.2, h2:0.8, h3:0.8, h4:0.8, n2:30, l2:60, l3:26, l4:50, r2:0.8, c:200})
print(r_theta)


epis = (-x + (cgps - l2 - l3 - l4) * sx) ** 2 / (vs2 + vs3 + vs4)

# print(epis)
r_epis = epis.evalf(subs={n1:50, a2:1.0, a3:1.0, a4:0.5, r1:0.2, h2:0.8, h3:0.8, h4:0.8, n2:30, l2:60, l3:26, l4:50, r2:0.8, c:200})
print(r_epis)

gx = theta - epis

gx2 = gx.evalf(subs={n1:50, a2:1.0, a3:1.0, a4:0.5, r1:0.2, h2:0.8, h3:0.8, h4:0.8, n2:30, l2:60, l3:26, l4:50, r2:0.8, c:200})
print(gx2)
# f1 = sp.lambdify(cgps, gx2, 'numpy')
# print('f1:', f1)
result = sp.solve(sp.Eq(gx2, 0), cgps, dict=True)
# print(result)
# print(len(result))
# print('-' * 40)
# for i in result:
#     print(i)
# print('-' * 40)
c2 = u2 * cgps
tx2 = h4 * x / ((c2 - l2) * (h4 - 1))
vtx2 = a2 * l2 * tx2 ** (2*h2)
theta2 = (-x + (c2 - l2) * tx2) ** 2 / vtx2

p = sp.exp(-0.5 * theta2) / (2 * sp.pi * (1 + theta2 ** 0.5) ** 2) ** 0.25
print('p:', p)

r_p = p.evalf(subs={n1:50, a2:1.0, a3:1.0, a4:0.5, r1:0.2, h2:0.8, h3:0.8, h4:0.8, n2:30, l2:60, l3:26, l4:50, r2:0.8, c:200, u2:0.4, u3:0.4, u4:0.2, cgps:result[4][cgps]})
print(r_p)
y = sp.symbols('y')
last_f = r_p - y
r_last_f = sp.lambdify(y, last_f, 'numpy')
ff4 = r_last_f(0.1)
print(ff4)

# r_p = sp.lambdify(y, r_p, 'numpy')
#
#
# result2 = sp.solve(sp.Eq(r_p, 0.1), x)
# print('result2:', result2)
