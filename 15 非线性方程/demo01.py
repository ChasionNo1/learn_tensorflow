# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/27 9:32
# @Author    :   Chasion
# Description:
import sympy as sp
from sympy import exp

x, y = sp.symbols('x y')
f = 2 * x * exp(x)
ff = sp.lambdify(x, f, 'numpy')
print(ff(2))