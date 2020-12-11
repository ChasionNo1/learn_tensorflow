"""
文件说明

"""
import numpy as np
from numpy.linalg import *


# 生成对角矩阵
lst = np.eye(3)

lst1 = np.array([[1, 2], [3, 4]])
# 矩阵的逆
print(inv(lst1))

# 矩阵转置
print(lst1.transpose())

# 计算行列式, 第一个元祖是特征值，第二个为对应的特征向量
print(eig(lst1))
