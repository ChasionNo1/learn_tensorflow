# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/23 15:54
# @Author    :   Chasion
# Description:
import sympy as sp

# l:lambda
x, t, c, l1, l2, a1, a2, h1, h2 = sp.symbols('x, t, c, l1, l2, a1, a2, h1, h2')
n1, n2, r1, r2 = sp.symbols('n1, n2, r1, r2')
# x, c,  h, cgps = sp.symbols('x, c,  h, cgps')
# a2, a3, a4, l2, l3, l4, h2, h3, h4 = sp.symbols('a2, a3, a4, l2, l3, l4, h2, h3, h4')
u2, u3, u4 = sp.symbols('u2, u3, u4')


vt1 = a1 * l1 * t ** (2 * h1)
vt2 = a2 * l2 * t ** (2 * h2)
v1 = (n1 * r2 + n2 * r1) ** 2 * t**2 / (r1 + r2) ** 2 + 2 * (n1 - n2) * r1 * r2 * t / (r1 + r2) ** 3 - 2 * (n1 - n2) ** 2 * r1 * r2 * (1 - sp.exp(-(r1 + r2) * t)) / (r1 + r2) ** 4
sita = ((-x + (c - l1 - l2) * t) ** 2) / (v1 + a1 * l1 * t ** (2 * h1) + a2 * l2 * t ** (2 * h1))
diff_sita = sp.diff(sita, t)
# sp.Eq(diff_sita, 0)
result = sp.solve(diff_sita, t, dict=True)

print(diff_sita)
print(result)

# result2 = diff_sita.evalf(subs={t:result[0][t]})
# print(result2)

# x, y = sp.symbols('x y')
# z = x**2 + y**2
# diff_z = sp.diff(z, x)
# print(diff_z)
# x = y**2*3
# y=2
# print(x)