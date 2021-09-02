# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/29 8:37
# @Author    :   Chasion
# Description:
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer


testdata = pd.DataFrame({'pet': ['cat', 'dog', 'dog', 'fish'], 'age': [4, 6, 3, 3],
                         'salary': [4, 5, 1, 1]})
onehot = OneHotEncoder(sparse=False).fit_transform(testdata[['age']])
print(onehot)

# 字符串类型的编码
# 方法一: LabelEncoder() + OneHotEncoder()
a = LabelEncoder().fit_transform(testdata['pet'])
pet_onehot = OneHotEncoder(sparse=False).fit_transform(a.reshape(-1, 1))  # 注意: 这里把 a 用 reshape 转换成 2-D array

# 方法二: 直接用 LabelBinarizer()

pet_binary = LabelBinarizer().fit_transform(testdata['pet'])
print(pet_binary)
print(pet_onehot)

df = pd.get_dummies(testdata, columns=testdata.columns).values
print(df)