"""
文件说明

"""
import numpy as np
from numpy.linalg import *
import math

a = np.array([[1, 1, 0],
              [0, 0, 1]])
Cx = np.array([[7, 3, 2],
               [3, 4, 1],
               [2, 1, 2]])
aT = np.array([[1, 0],
               [1, 0],
               [0, 1]])
x1 = np.matmul(a, Cx)
x2 = np.matmul(x1, aT)
print(x1)
print(x2)
print(inv(x2))


n1 = np.matmul(inv(np.array([[1, 1/2], [1/2, 1/3]])), np.array([math.e - 1, 1]))
print(n1)