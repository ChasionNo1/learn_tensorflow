"""
文件说明

"""
import numpy as np

a = np.floor(100 * np.random.random((2, 3)))
b = np.floor(100 * np.random.random((2, 3)))
print(a)
print('--------------------')
print(b)

print('----------np.hstack():横向拼接，增加特征量------------')
print(np.hstack((a, b)))

print('----------np.vstack():纵向拼接，增加样本个数------------')
print(np.vstack((a, b)))


print(np.array([[1, 2, 3], [2, 4, 9], [5, 9, 3]]).T)
a1 = 10
b1 = 10
assert a1 == b1

x = np.array([[1, 2, 3]])
print(x.shape)

