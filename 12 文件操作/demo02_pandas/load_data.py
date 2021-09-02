# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/6/29 19:23
# @Author    :   Chasion
# Description:
import pandas as pd
import numpy as np


path = 'datasets/score1.xlsx'
data = pd.read_excel(path, header=None).values
data = data.reshape(-1)
r = np.random.randint(-5, 6, data.shape[0])
print(r)
data = data + r
print(data)
data = pd.DataFrame(data)
data.to_excel('datasets/score2.xlsx')