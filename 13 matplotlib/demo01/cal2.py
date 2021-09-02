from sympy import symbols, diff
import sympy
import numpy as np
import math
import matplotlib.pylab as plt

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
# print(Vf)

# y1 = Vf.evalf(subs={af:1.0, lf:80, hf:0.8})
# print(y1)


lj, Cgps, s, ls, aj, aas = symbols('lj, Cgps, s, ls, aj, aas')

f1 = ls
f2 = aas * ls

s1 = sympy.summation(f1, (s, 1, 100))
s2 = sympy.summation(f2, (s, 1, 100))

Cj = lj + (Cgps - s1) * np.power(aj*lj/s2, 1/2*hf)
# print(Cj)

af2 = [1, 1]
h = [0.9, 0.6]
l = [80, 80]

"""
f1 = ls
f2 = aas * ls

s1 = sympy.summation(f1, (s, 1, 100))
s2 = sympy.summation(f2, (s, 1, 100))

Cj = lj + (Cgps - s1) * np.power(aj*lj/s2, 1/2*h)

lj, Cgps, s, ls, aj, aas, h = symbols('lj, Cgps, s, ls, aj, aas, h')
"""
sum = 0.0
for i in range(2):
    # aas_list = np.delete(np.array(af), i).tolist()
    # ls_list =np.delete(np.array(l), i).tolist()
    sum_ls = 0.0
    sum_as_ls = 0.0
    for j in range(len(af2)):
        sum_ls = sum_ls + l[j]
        sum_as_ls = sum_as_ls + af2[j] * l[j]
    y1 = Cj.evalf(subs={lj: l[i], aj: af2[i], hf: h[i], s1: sum_ls, s2: sum_as_ls})
    sum = sum + y1
print('sum_c:', sum)

# 解方程
y4 = sum - Cgps
result3 = sympy.solve(y4, Cgps)
# print(result3)
Cgps2 = result3[0]
Cj_list = []
for i in range(2):
    sum_ls = 0.0
    sum_as_ls = 0.0
    for j in range(len(af2)):
        sum_ls = sum_ls + l[j]
        sum_as_ls = sum_as_ls + af2[j] * l[j]
    y6 = Cj.evalf(subs={lj: l[i], aj: af2[i], hf: h[i], s1: sum_ls, s2: sum_as_ls, Cgps: Cgps2})
    Cj_list.append(y6)
print('Cj_list:', Cj_list)


x, t = symbols('x, t')
Cj2 = symbols('Cj2')
sitat = np.power(-x + (Cj2 - lj) * t, 2) / Vf
print("sitat:", sitat)

"""
x, t = symbols('x, t')
sitat = np.power(-x + (Cj - lj) * t, 2) / Vf
print(sitat)
"""
y5 = []
for i in range(2):
    """
    af, lf, hf, t = symbols("af lf hf t")
    Vf = af * lf * np.power(t, 2*hf)
    af*lf*t**(2*hf)
    """
    vf = Vf.evalf(subs={af: af2[i], lf: l[i], hf: h[i]})
    # print('vf:', vf)
    y5.append(sitat.evalf(subs={Cj2: Cj_list[i], lj: l[i], Vf: vf}))
print('sitat_result:', y5)

sitat_diff = []
point_diff = []
for i in range(2):
    sitat_diff.append(diff(y5[i], t))
    # 求一阶偏导为0的驻点
    point_diff.append(sympy.solve(sitat_diff, t))
print('sitat_diff:', sitat_diff)
print('point_diff', point_diff)

# 选择合适驻点
point_diff = [point_diff[0][-1][0], point_diff[1][-1][0]]
print('point-diff：', point_diff)

# 将sitat中的t用x表示，替换掉，得到新的sitat_new
sitat_new = []
for i in range(2):
    sitat_new.append(y5[i].evalf(subs={t:point_diff[i]}))

print('sita_new:', sitat_new)


# 计算x和deltaf的关系

sitak, tx = symbols('sitak tx')
y3 = sitat.evalf(subs={t: tx})
# print(y3)
# math.exp(-1 * y3/2)
px_list = []
for i in range(2):
    Px = math.e ** (-1 * sitat_new[i] / 2) / np.power(2 * np.pi * np.power(1 + np.power(sitat_new[i], 1 / 2), 2), 1 / 4)
    px_list.append(Px)

print('px_List:', px_list)

# y = f(x)
# last_one = []
# f = symbols('f')
# for i in range(2):
#     last_one.append(sympy.solve(px_list[i] - f, x))
#
# print('last_one:', last_one)  , 0.00001, 0.0001, 0.001, 0.01, 0.1, 1
yy = []
xx = [0, 100, 200, 300, 400, 500, 600, 700, 800]
for i in range(len(xx)):
    yy.append(px_list[0].evalf(subs={x: xx[i]}))
print(yy)

plt.plot(xx, yy)
plt.ylim(0.00000001, 10)
plt.show()


# sitat_diff =
#
# result = sympy.solve(sitat_diff, t)
# x1 = result[0]
# x2 = result[1]


# y2 = sitat.evalf(subs={t: x1})
# print(y2)


sitak, tx = symbols('sitak tx')
y3 = sitat.evalf(subs={t: tx})
# print(y3)
# math.exp(-1 * y3/2)
Px = math.e ** (-1 * y3/2) / np.power(2 * np.pi * np.power(1+np.power(y3, 1/2), 2), 1/4)
# print(Px)

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

# print(s5)






