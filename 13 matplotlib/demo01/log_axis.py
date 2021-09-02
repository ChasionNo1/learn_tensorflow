# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/30 15:49
# @Author    :   Chasion
# Description:
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

dt = 0.01
t = np.arange(dt, 20.0, dt)

ax.semilogx(t, np.exp(-t / 5.0))
ax.grid()

plt.show()