# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      :   2021/7/28 14:44
# @Author    :   Chasion
# Description:
from sklearn import preprocessing
from sklearn import tree

# help(preprocessing.LabelBinarizer)#取消注释可以查看详细用法

# 特征矩阵
featureList=[[1,0],[1,1],[0,0],[0,1]]
# 标签矩阵
labelList=['yes', 'no', 'no', 'yes']
# 将标签矩阵二值化
lb = preprocessing.LabelBinarizer()
dummY=lb.fit_transform(labelList)
# print(dummY)
# 模型建立和训练
clf = tree.DecisionTreeClassifier()
clf = clf.fit(featureList, dummY)
p=clf.predict([[1,0]])
# print(p)#取消注释可以查看p的值

# 逆过程
yesORno=lb.inverse_transform(p)
print(yesORno)