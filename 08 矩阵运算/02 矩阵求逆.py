import numpy as np


# a = np.array([[2,1,1],
#               [1,2,1],
#               [1,1,2]])
# b = np.array([[1,2,2],
#               [2,1,2],
#               [2,2,1]])
# a_inv = np.linalg.inv(a)
# print(a_inv*4)
# # 点乘
# print(np.multiply(a_inv, b))
# # 矩阵乘法
# print(np.matmul(a_inv, b)*4)
#
#
# c = np.array([[2,0,0],
#               [1,1,2],
#               [0,1,3]])
# c_inv = np.linalg.inv(c)
# x = np.array([[1],[1],[1]])
# print(np.matmul(c_inv, x))
# d_inv = np.linalg.inv(np.array([[1,1,1],[1,1,2],[3,0,-1]]))
# e = np.array([[1,1,2],[6,0,-2],[0,0,0]])
# print(np.matmul(d_inv, e))
m1 = np.matmul(np.array([[2,-2,-2],[1,1,-3],[1,1,-3]]), np.array([[2,-2,-2],[1,1,-3],[1,1,-3]]))
print(np.matmul(m1, m1))
