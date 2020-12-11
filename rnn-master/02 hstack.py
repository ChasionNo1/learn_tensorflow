"""
文件说明

一维数组的hstack是随意的
hstack必须要第二维度是一样的
"""
import numpy as np


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# 参数为tuple元组的形式
print(np.vstack((arr1, arr2)))
'''
[[1 2 3]
 [4 5 6]]
'''
print(np.hstack((arr1, arr2)))
'''
[1 2 3 4 5 6]
'''
# 维度必须一样,
a1 = np.array([[1, 4, 5], [2, 9, 3]])
a2 = np.array([[6, 0, 3], [2, 3, 5]])
print(a1)
print(a2)
print(np.hstack((a1, a2)))
print(np.vstack((a1, a2)))
'''
[[1 4 5 6 0 1]
 [2 9 3 2 3 6]]
[[1 4 5]
 [2 9 3]
 [6 0 1]
 [2 3 6]]

'''

