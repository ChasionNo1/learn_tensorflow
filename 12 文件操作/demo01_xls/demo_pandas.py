# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/4/23 17:01
# @Author    :   Chasion
# Description:
from scipy.io import arff
import pandas as pd


path = ''
data, meta = arff.loadarff(path)
N = data.shape[0]
df = pd.DataFrame(data)
print(df.head(N))
print(df.columns)
