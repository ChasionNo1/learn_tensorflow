# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/8/16 20:26
# @Author    :   Chasion
# Description:
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(40, 180, 1000)
max_p = 0.5

min_th = 40
max_th = 180
y1 = max_p * ((t - min_th) / (max_th - min_th))
y2 = max_p/2 + (max_p/2) * ((2 * t - min_th - max_th)**3 / (max_th - min_th)**3)

plt.plot(t,  y2, c='r')
plt.plot(t, y1, c='b')
plt.show()
