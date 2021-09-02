from sympy import symbols, diff
import sympy
import numpy as np
import math


# x, y = symbols('x y', real=True)
# rec = diff(x**2+y**3, y)
# print(rec)

# af = 1.2
# lamdaf = 1.0
# Hf = 0.1
#
# t = np.random.random(10)
# Vf = af * lamdaf * np.power(t, Hf)

#
# x=sympy.Symbol('x')
# fx=5*x+4
# #使用evalf函数传值
# y1=fx.evalf(subs={x:6})
# print(y1)

af, lf, hf, t = symbols("af lf hf t")
Vf = af * lf * np.power(t, 2*hf)
print(Vf)

# y1 = Vf.evalf(subs={af:1.0, lf:80, hf:0.8})
# print(y1)


lj, Cgps, s, ls, aj, aas, h = symbols('lj, Cgps, s, ls, aj, aas, h')

f1 = ls
f2 = aas * ls

s1 = sympy.summation(f1, (s, 1, 100))
s2 = sympy.summation(f2, (s, 1, 100))

Cj = lj + (Cgps - s1) * np.power(aj*lj/s2, 1/2*h)
print(Cj)


x, t = symbols('x, t')
sitat = np.power(-x + (Cj - lj) * t, 2) / Vf
print(sitat)
# sitat_diff = diff(sitat, t)
#
# result = sympy.solve(sitat_diff, t)
# x1 = result[0]
# x2 = result[1]


# y2 = sitat.evalf(subs={t: x1})
# print(y2)


sitak, tx = symbols('sitak tx')
y3 = sitat.evalf(subs={t: tx})
print(y3)
# math.exp(-1 * y3/2)
Px = math.e ** (-1 * y3/2) / np.power(2 * np.pi * np.power(1+np.power(y3, 1/2), 2), 1/4)
print(Px)

deltaf = symbols('deltaf')

deltaf = Px

k, lk, ak, S, hk = symbols('k, lk, ak, S, hk')
f3 = lk
f4 = ak * lk * np.power(S, 2 * hk)
s3 = sympy.summation(f3, (k, 4, 8))
s4 = sympy.summation(f4, (k, 4, 8))
epis = np.power(-x + (Cgps - s3) * S, 2) / s4


ck = symbols('Cj')
tao = np.power(-x/(hk - 1), 2) / ak * lk * np.power(hk * x / ((Cj - x) * (hk - 1)), 2)

f5 = Cj
s5 = sympy.summation(f5, (k, 4, 8))

print(s5)
af = [1, 1]
h = [0.9, 0.6]
l = [80, 80]

lj_list = [1, 2, 3, 4, 5]
aj_list = [1, 2, 4, 5, 6]
sum = 0.0
for i in range(2):
    y1 = Cj.evalf(subs={lj: lj_list[i], aj: aj_list[i]})
    sum = sum + y1
print(sum)

