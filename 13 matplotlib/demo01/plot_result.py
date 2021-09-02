# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/5/30 17:06
# @Author    :   Chasion
# Description:
import pandas as pd
import matplotlib.pyplot as plt


path = 'datasets/data1.csv'
data = pd.read_csv(path).values
x = data[:, 0]
y = data[:, 1]

plt.xlim(0, 400)
plt.ylim(0, 1)
plt.scatter(x, y)
plt.show()